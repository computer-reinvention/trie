"""Compressed attention-event capture, backed by SQLite under `.trie/`.

The desktop AGM runs its live attention simulation in memory from the opencode
SSE stream — this store is the *durable* side: a compressed, bounded log of
agent attention events that survives across processes and app restarts. It
serves two consumers:

  1. **Replay / hydration** — the desktop reads recent events on open so a
     re-launched app (or one that missed a CLI session) can reconstruct where
     attention has been, at investigation granularity.
  2. **The sync-time historical-mass fold** — `trie sync`, when it regenerates a
     symbol's triefact, asks this store which DISTINCT investigations drew
     attention to that symbol since the last sync, and folds that recurrence
     count into the symbol's historical mass (see `trie.sync`).

It is **ephemeral cache**: it lives at `.trie/attention.db` (gitignored,
regenerable), holds only transient runtime state, and is never the source of
truth for historical mass — the triefact sentinel is (see `trie.sync.writer`).

## Compression

Raw tool traffic is bursty (a grep can touch dozens of symbols). To keep the
log bounded we **coalesce**: repeated events with the same
(target, event_type, investigation_id) inside a short window collapse into one
row whose `weight` accumulates and whose `ts` advances to the latest. This keeps
"enough for replay" without storing every raw event forever.

## Retention

Old events are pruned on write: we keep events from the most recent
``MAX_INVESTIGATIONS`` investigations OR the last ``MAX_AGE_SECONDS``, whichever
is more generous. Everything older is dropped.

Best-effort throughout: a failed write never raises into the agent's tool path.
"""

from __future__ import annotations

import sqlite3
import time
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path

from trie.attention import EVENT_WEIGHTS, EventType

DB_FILENAME = "attention.db"

# Coalesce window: events on the same target/type/investigation within this many
# seconds merge into one accumulating row instead of inserting a new one.
COALESCE_WINDOW_SECONDS = 5.0

# Retention bounds (whichever keeps more): the most recent N investigations, or
# everything newer than D seconds.
MAX_INVESTIGATIONS = 20
MAX_AGE_SECONDS = 7 * 24 * 60 * 60

_SCHEMA = """
CREATE TABLE IF NOT EXISTS attention_events (
    id              INTEGER PRIMARY KEY,
    ts              REAL NOT NULL,
    event_type      TEXT NOT NULL,
    target          TEXT NOT NULL,
    weight          INTEGER NOT NULL,
    agent_id        TEXT NOT NULL DEFAULT '',
    session_id      TEXT NOT NULL DEFAULT '',
    investigation_id TEXT NOT NULL DEFAULT ''
);
CREATE INDEX IF NOT EXISTS idx_attn_target ON attention_events(target);
CREATE INDEX IF NOT EXISTS idx_attn_ts ON attention_events(ts);
CREATE INDEX IF NOT EXISTS idx_attn_inv ON attention_events(investigation_id);

-- Tracks the last time the sync fold consumed events, so the fold can ask
-- "which investigations touched this symbol SINCE last sync" without re-folding.
CREATE TABLE IF NOT EXISTS attention_meta (
    key   TEXT PRIMARY KEY,
    value TEXT NOT NULL
);
"""


def db_path(project_root: Path) -> Path:
    return project_root / ".trie" / DB_FILENAME


@contextmanager
def _connect(project_root: Path) -> Iterator[sqlite3.Connection]:
    """Open the attention DB, creating it + schema on first use.

    WAL mode lets the desktop read while a writer commits; `busy_timeout` makes
    brief lock contention block-and-retry rather than raise.
    """
    path = db_path(project_root)
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(path), timeout=5.0)
    try:
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA busy_timeout=5000")
        conn.executescript(_SCHEMA)
        yield conn
    finally:
        conn.close()


@dataclass(frozen=True)
class StoredEvent:
    ts: float
    event_type: str
    target: str
    weight: int
    agent_id: str
    session_id: str
    investigation_id: str


def record_event(
    project_root: Path,
    *,
    event_type: EventType,
    target: str,
    agent_id: str = "",
    session_id: str = "",
    investigation_id: str = "",
    ts: float | None = None,
) -> None:
    """Record one attention event, coalescing into a recent matching row.

    Best-effort: swallows DB errors so a capture failure never breaks the agent.
    Weight is taken from the canonical `EVENT_WEIGHTS` table. After writing, runs
    a bounded prune so the log can't grow without limit.
    """
    now = time.time() if ts is None else ts
    weight = EVENT_WEIGHTS[event_type]
    try:
        with _connect(project_root) as conn, conn:
            # Coalesce: find a recent row with the same identity and bump it.
            row = conn.execute(
                """
                SELECT id, weight FROM attention_events
                WHERE target = ? AND event_type = ? AND investigation_id = ?
                  AND session_id = ? AND agent_id = ? AND ts >= ?
                ORDER BY ts DESC LIMIT 1
                """,
                (
                    target,
                    event_type,
                    investigation_id,
                    session_id,
                    agent_id,
                    now - COALESCE_WINDOW_SECONDS,
                ),
            ).fetchone()
            if row is not None:
                conn.execute(
                    "UPDATE attention_events SET weight = ?, ts = ? WHERE id = ?",
                    (int(row[1]) + weight, now, int(row[0])),
                )
            else:
                conn.execute(
                    """
                    INSERT INTO attention_events
                        (ts, event_type, target, weight, agent_id, session_id, investigation_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (now, event_type, target, weight, agent_id, session_id, investigation_id),
                )
            _prune(conn, now)
    except sqlite3.Error:
        pass


def read_events(project_root: Path, *, since: float = 0.0, limit: int = 5000) -> list[StoredEvent]:
    """Return events with ts > `since`, oldest-first, capped at `limit`.

    Used by the desktop to hydrate / replay. Never raises on a missing DB."""
    path = db_path(project_root)
    if not path.exists():
        return []
    try:
        with _connect(project_root) as conn:
            rows = conn.execute(
                """
                SELECT ts, event_type, target, weight, agent_id, session_id, investigation_id
                FROM attention_events
                WHERE ts > ?
                ORDER BY ts ASC
                LIMIT ?
                """,
                (since, limit),
            ).fetchall()
    except sqlite3.Error:
        return []
    return [StoredEvent(*r) for r in rows]


def investigations_touching_symbol_since(
    project_root: Path, target: str, *, since: float = 0.0
) -> set[str]:
    """Return the set of DISTINCT investigation ids that drew attention to
    `target` after `since`.

    This is the recurrence signal the sync-time fold uses for historical mass:
    "how many distinct investigations have returned to this symbol?" The empty
    string (untracked investigation) counts as one anonymous investigation.
    """
    path = db_path(project_root)
    if not path.exists():
        return set()
    try:
        with _connect(project_root) as conn:
            rows = conn.execute(
                """
                SELECT DISTINCT investigation_id FROM attention_events
                WHERE target = ? AND ts > ?
                """,
                (target, since),
            ).fetchall()
    except sqlite3.Error:
        return set()
    return {r[0] for r in rows}


def get_last_fold_ts(project_root: Path) -> float:
    """Timestamp of the last historical-mass fold, or 0.0 if never folded."""
    path = db_path(project_root)
    if not path.exists():
        return 0.0
    try:
        with _connect(project_root) as conn:
            row = conn.execute(
                "SELECT value FROM attention_meta WHERE key = 'last_fold_ts'"
            ).fetchone()
    except sqlite3.Error:
        return 0.0
    return float(row[0]) if row else 0.0


def set_last_fold_ts(project_root: Path, ts: float) -> None:
    """Record the fold watermark. Best-effort."""
    try:
        with _connect(project_root) as conn, conn:
            conn.execute(
                "INSERT OR REPLACE INTO attention_meta (key, value) VALUES ('last_fold_ts', ?)",
                (str(ts),),
            )
    except sqlite3.Error:
        pass


def _prune(conn: sqlite3.Connection, now: float) -> None:
    """Drop events outside the retention bounds.

    Keep everything from the most recent MAX_INVESTIGATIONS investigations OR
    newer than MAX_AGE_SECONDS — whichever cutoff is older (more generous). Runs
    inside the caller's transaction.
    """
    age_cutoff = now - MAX_AGE_SECONDS

    # The ts of the newest event in the (MAX_INVESTIGATIONS)-th most recent
    # investigation. Investigations ordered by their latest activity.
    row = conn.execute(
        """
        SELECT MIN(last_ts) FROM (
            SELECT investigation_id, MAX(ts) AS last_ts
            FROM attention_events
            GROUP BY investigation_id
            ORDER BY last_ts DESC
            LIMIT ?
        )
        """,
        (MAX_INVESTIGATIONS,),
    ).fetchone()
    inv_cutoff = float(row[0]) if row and row[0] is not None else age_cutoff

    # Use the more generous (older) cutoff so neither bound alone over-prunes.
    cutoff = min(age_cutoff, inv_cutoff)
    conn.execute("DELETE FROM attention_events WHERE ts < ?", (cutoff,))
