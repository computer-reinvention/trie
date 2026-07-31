"""Ephemeral local activity state for trie, backed by SQLite.

trie's write paths run as independent processes — a terminal `trie sync`, the
end-of-turn `trie sync --graph-only` hook, an editor plugin's graph sync. None
of them share memory, so the live writer status and the working-tree (stale)
set live in a small on-disk database any process can read while a writer
updates it.

SQLite is the right tool: atomic transactions (no torn reads), WAL mode for
concurrent readers during a write, and a single file instead of a litter of
hand-rolled JSON snapshots. The database is **ephemeral** — it lives at
`.trie/activity.db` (gitignored, regenerable) and holds only transient runtime
state, never durable artefacts.

Two tables:

  - `status` — a single row (id=1) describing what the active writer is doing
    right now: state, op, pid, current file, done/total. Reset to idle on clean
    exit. Crash-safe: a reader cross-checks the row's `pid` for liveness, so a
    stale "running" row from a crashed process reads as idle.

  - `pending` — one row per stale source file (the working-tree status), written
    by a graph-only refresh and cleared as `trie sync` regenerates files.

Durable telemetry stays in `debug.jsonl` (see `trie.telemetry`); this module is
strictly live runtime state.
"""

from __future__ import annotations

import os
import sqlite3
import time
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path

DB_FILENAME = "activity.db"

_SCHEMA = """
CREATE TABLE IF NOT EXISTS status (
    id           INTEGER PRIMARY KEY CHECK (id = 1),
    state        TEXT NOT NULL DEFAULT 'idle',
    op           TEXT NOT NULL DEFAULT '',
    pid          INTEGER NOT NULL DEFAULT 0,
    started_at   INTEGER NOT NULL DEFAULT 0,
    updated_at   INTEGER NOT NULL DEFAULT 0,
    current_file TEXT,
    done         INTEGER NOT NULL DEFAULT 0,
    total        INTEGER NOT NULL DEFAULT 0,
    error        TEXT
);
CREATE TABLE IF NOT EXISTS pending (
    source_path TEXT PRIMARY KEY,
    head        TEXT NOT NULL DEFAULT '',
    computed_at INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS meta (
    key   TEXT PRIMARY KEY,
    value TEXT NOT NULL
);
"""


def db_path(project_root: Path) -> Path:
    return project_root / ".trie" / DB_FILENAME


@contextmanager
def _connect(project_root: Path) -> Iterator[sqlite3.Connection]:
    """Open the ephemeral activity DB, creating it + schema on first use.

    WAL mode lets `trie status` / other readers poll while a writer commits.
    `busy_timeout` makes brief lock contention block-and-retry rather than raise.
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


# ---------------------------------------------------------------------------
# meta — small key/value runtime state (apply session note, cli session id, ...).
# ---------------------------------------------------------------------------


def get_meta(project_root: Path, key: str) -> str | None:
    """Return the meta value for `key`, or None. Never raises on a missing DB."""
    path = db_path(project_root)
    if not path.exists():
        return None
    try:
        with _connect(project_root) as conn:
            row = conn.execute("SELECT value FROM meta WHERE key = ?", (key,)).fetchone()
    except sqlite3.Error:
        return None
    return row[0] if row else None


def set_meta(project_root: Path, key: str, value: str) -> None:
    """Upsert a meta key/value. Best-effort; swallows DB errors."""
    try:
        with _connect(project_root) as conn, conn:
            conn.execute("INSERT OR REPLACE INTO meta (key, value) VALUES (?, ?)", (key, value))
    except sqlite3.Error:
        pass


def clear_meta(project_root: Path, key: str) -> None:
    """Delete a meta key. Best-effort."""
    try:
        with _connect(project_root) as conn, conn:
            conn.execute("DELETE FROM meta WHERE key = ?", (key,))
    except sqlite3.Error:
        pass


# ---------------------------------------------------------------------------
# pending — the working-tree (stale) set.
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Pending:
    stale: tuple[str, ...]
    head: str
    computed_at: int

    @property
    def count(self) -> int:
        return len(self.stale)


def write_pending(project_root: Path, *, stale: list[str], head: str) -> None:
    """Replace the stale set with `stale`. An empty list records 'clean, freshly
    computed' (distinct from 'never computed', which has no rows and reads None)."""
    now = int(time.time())
    rows = [(s, head, now) for s in sorted(set(stale))]
    with _connect(project_root) as conn, conn:
        conn.execute("DELETE FROM pending")
        conn.executemany(
            "INSERT INTO pending (source_path, head, computed_at) VALUES (?, ?, ?)", rows
        )
        # Marker so a reader can tell 'computed, empty' from 'never computed'.
        conn.execute(
            "INSERT OR REPLACE INTO meta (key, value) VALUES ('pending_computed_at', ?)",
            (str(now),),
        )


def read_pending(project_root: Path) -> Pending | None:
    """Return the recorded stale set, or None if pending was never computed.

    A present-but-empty set returns `Pending(stale=())`."""
    path = db_path(project_root)
    if not path.exists():
        return None
    try:
        with _connect(project_root) as conn:
            rows = conn.execute(
                "SELECT source_path, head, computed_at FROM pending ORDER BY source_path"
            ).fetchall()
            # Distinguish 'computed empty' from 'never computed' via the marker
            # write_pending sets — independent of writer status.
            has_marker = conn.execute(
                "SELECT 1 FROM meta WHERE key='pending_computed_at'"
            ).fetchone()
    except sqlite3.Error:
        return None
    if not rows and not has_marker:
        return None
    head = rows[0][1] if rows else ""
    computed_at = rows[0][2] if rows else 0
    return Pending(stale=tuple(r[0] for r in rows), head=head, computed_at=computed_at)


def clear_pending(project_root: Path, *, synced: list[str], head: str) -> None:
    """Remove `synced` files from the stale set after a successful sync."""
    if not synced:
        return
    with _connect(project_root) as conn, conn:
        conn.executemany("DELETE FROM pending WHERE source_path = ?", [(s,) for s in synced])
        if head:
            conn.execute("UPDATE pending SET head = ?", (head,))


# ---------------------------------------------------------------------------
# status — the live writer snapshot.
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Status:
    state: str  # "idle" | "scanning" | "syncing" | "refreshing" | "error"
    op: str
    pid: int
    started_at: int
    updated_at: int
    current_file: str | None = None
    done: int = 0
    total: int = 0
    error: str | None = None

    @property
    def is_active(self) -> bool:
        return self.state not in ("idle", "error")


def _pid_alive(pid: int) -> bool:
    """True if a process with `pid` exists — POSIX `kill(pid, 0)` liveness probe.
    Used to treat a crashed writer's stale 'running' row as idle."""
    if pid <= 0:
        return False
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def read_status(project_root: Path) -> Status:
    """Return the current writer status. Missing DB, missing row, or a 'running'
    row whose pid is dead all read as idle — a crashed writer never leaves the
    project looking permanently busy."""
    idle = Status(state="idle", op="", pid=0, started_at=0, updated_at=0)
    path = db_path(project_root)
    if not path.exists():
        return idle
    try:
        with _connect(project_root) as conn:
            row = conn.execute(
                "SELECT state, op, pid, started_at, updated_at, current_file, done, total, error "
                "FROM status WHERE id = 1"
            ).fetchone()
    except sqlite3.Error:
        return idle
    if row is None:
        return idle
    state, op, pid = str(row[0]), str(row[1]), int(row[2] or 0)
    if state not in ("idle", "error") and not _pid_alive(pid):
        return idle
    return Status(
        state=state,
        op=op,
        pid=pid,
        started_at=int(row[3] or 0),
        updated_at=int(row[4] or 0),
        current_file=row[5] or None,
        done=int(row[6] or 0),
        total=int(row[7] or 0),
        error=row[8] or None,
    )


# ---------------------------------------------------------------------------
# ActivityWriter — owns the status row for one write run.
# ---------------------------------------------------------------------------


class ActivityWriter:
    """Records a single write operation's lifecycle into the `status` row.

    On enter: writes a `{state: <running>}` row. During: `file_start`/`file_done`/
    `file_skip` update the live row (current file, done/total). On exit: resets to
    idle (or error). Always resets on exception, and `read_status`'s pid liveness
    check covers an outright process kill.
    """

    def __init__(self, project_root: Path, op: str) -> None:
        self.project_root = project_root
        self.op = op
        self._running_state = {
            "sync": "syncing",
            "bootstrap": "syncing",
            "roles": "syncing",
            "refresh": "refreshing",
        }.get(op, "scanning")
        self._started = int(time.time())
        self._done = 0
        self._total = 0

    def __enter__(self) -> ActivityWriter:
        self._write(state=self._running_state, current_file=None)
        return self

    def __exit__(self, exc_type, exc, tb) -> None:  # type: ignore[no-untyped-def]
        if exc_type is not None:
            self._write(state="error", current_file=None, error=str(exc))
            return
        self._write(state="idle", op="", current_file=None)

    def set_total(self, total: int) -> None:
        self._total = total
        self._write(state=self._running_state, current_file=None)

    def file_start(self, rel_path: str, idx: int, total: int) -> None:
        self._total = total
        self._write(state=self._running_state, current_file=rel_path)

    def file_done(self, rel_path: str, *, symbols: int = 0, cost_usd: float = 0.0) -> None:
        self._done += 1
        self._write(state=self._running_state, current_file=None)

    def file_skip(self, rel_path: str, reason: str) -> None:
        self._done += 1
        self._write(state=self._running_state, current_file=None)

    def _write(
        self,
        *,
        state: str,
        current_file: str | None,
        op: str | None = None,
        error: str | None = None,
    ) -> None:
        try:
            with _connect(self.project_root) as conn, conn:
                conn.execute(
                    """
                    INSERT INTO status
                        (id, state, op, pid, started_at, updated_at, current_file, done, total, error)
                    VALUES (1, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(id) DO UPDATE SET
                        state=excluded.state, op=excluded.op, pid=excluded.pid,
                        updated_at=excluded.updated_at, current_file=excluded.current_file,
                        done=excluded.done, total=excluded.total, error=excluded.error
                    """,
                    (
                        state,
                        self.op if op is None else op,
                        os.getpid(),
                        self._started,
                        int(time.time()),
                        current_file,
                        self._done,
                        self._total,
                        error,
                    ),
                )
        except sqlite3.Error:
            pass  # status is best-effort; never sink a real run over a status write


@contextmanager
def activity_writer(project_root: Path, op: str) -> Iterator[ActivityWriter]:
    """Context-manager sugar around ActivityWriter."""
    writer = ActivityWriter(project_root, op)
    with writer:
        yield writer


# ---------------------------------------------------------------------------
# ActivityProgress — bridges the sync ProgressCallback protocol to ActivityWriter
# so every sync/refresh/roles run feeds the shared status with no per-call-site
# wiring. Always-on (independent of --json).
# ---------------------------------------------------------------------------


class ActivityProgress:
    """A `ProgressCallback` that mirrors per-file progress into an ActivityWriter.

    Wraps an inner ProgressCallback (the Rich/JSONL reporter) so both fire: the
    human/host UI AND the shared `status` row.
    """

    def __init__(self, writer: ActivityWriter, inner: object | None = None) -> None:
        self._writer = writer
        self._inner = inner

    def on_plan(self, *, direct: int, cascade: int) -> None:
        # Purely informational; mirror to the inner host callback if it cares.
        hook = getattr(self._inner, "on_plan", None)
        if callable(hook):
            hook(direct=direct, cascade=cascade)

    def on_section(self, *, label: str, count: int) -> None:
        hook = getattr(self._inner, "on_section", None)
        if callable(hook):
            hook(label=label, count=count)

    def on_start(self, rel_path: str, idx: int, total: int, *, cascade: bool = False) -> None:
        self._writer.file_start(rel_path, idx, total)
        if self._inner is not None:
            self._inner.on_start(rel_path, idx, total, cascade=cascade)  # type: ignore[attr-defined]

    def on_done(self, rel_path: str, result: object, running_cost_usd: float) -> None:
        symbols = getattr(result, "symbols_generated", 0)
        self._writer.file_done(rel_path, symbols=symbols, cost_usd=running_cost_usd)
        if self._inner is not None:
            self._inner.on_done(rel_path, result, running_cost_usd)  # type: ignore[attr-defined]

    def on_skip(self, rel_path: str, reason: str) -> None:
        self._writer.file_skip(rel_path, reason)
        if self._inner is not None:
            self._inner.on_skip(rel_path, reason)  # type: ignore[attr-defined]
