from __future__ import annotations

import functools
import sqlite3
import threading
import time
from collections.abc import Callable, Iterator
from contextlib import contextmanager
from dataclasses import dataclass, field
from pathlib import Path

from trie.parse.python import Symbol
from trie.parse.references import Reference

# v8: extended symbol-kind vocabulary (interface/type/enum/enum_member/property)
# for multi-language indexing. The `kind` column is free-text so no schema change
# is needed — the bump forces a clean cache rebuild so TS files index cleanly.
SCHEMA_VERSION = 10

# All schema is created if not present. The DB is a regenerable cache under .trie/;
# bumping SCHEMA_VERSION blows it away and triggers a re-scan on next connect.
SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS schema_version (
    version INTEGER PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS files (
    path TEXT PRIMARY KEY,
    fingerprint TEXT NOT NULL,
    last_scanned_at INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS symbols (
    id INTEGER PRIMARY KEY,
    file_path TEXT NOT NULL REFERENCES files(path) ON DELETE CASCADE,
    qualified_name TEXT NOT NULL,
    name TEXT NOT NULL,
    kind TEXT NOT NULL,
    signature TEXT,
    docstring TEXT,
    body_normalized_hash TEXT NOT NULL,
    signature_hash TEXT NOT NULL,
    is_public INTEGER NOT NULL,
    start_line INTEGER NOT NULL,
    end_line INTEGER NOT NULL,
    decorators TEXT NOT NULL DEFAULT '',
    UNIQUE (file_path, qualified_name)
);
CREATE INDEX IF NOT EXISTS idx_symbols_file ON symbols(file_path);
CREATE INDEX IF NOT EXISTS idx_symbols_qname ON symbols(qualified_name);

CREATE TABLE IF NOT EXISTS edges (
    src_symbol_id INTEGER NOT NULL REFERENCES symbols(id) ON DELETE CASCADE,
    dst_symbol_id INTEGER NOT NULL REFERENCES symbols(id) ON DELETE CASCADE,
    kind TEXT NOT NULL DEFAULT 'calls',
    PRIMARY KEY (src_symbol_id, dst_symbol_id)
);
CREATE INDEX IF NOT EXISTS idx_edges_dst ON edges(dst_symbol_id);

CREATE TABLE IF NOT EXISTS triefact_sections (
    triefact_path TEXT NOT NULL,
    symbol_id INTEGER NOT NULL REFERENCES symbols(id) ON DELETE CASCADE,
    section_fingerprint TEXT NOT NULL,
    one_liner TEXT,
    role TEXT NOT NULL DEFAULT '',
    boundary TEXT NOT NULL DEFAULT '',
    last_generated_at INTEGER NOT NULL,
    PRIMARY KEY (triefact_path, symbol_id)
);
CREATE INDEX IF NOT EXISTS idx_sections_symbol ON triefact_sections(symbol_id);
CREATE INDEX IF NOT EXISTS idx_sections_role ON triefact_sections(role);
CREATE INDEX IF NOT EXISTS idx_sections_boundary ON triefact_sections(boundary);

-- Patch notes are keyed by qname TEXT, deliberately NOT by symbol_id FK:
-- a graph refresh recycles symbol rows, and an ON DELETE CASCADE here silently
-- destroyed staged intent (the long-standing loss bug). qname keys also let
-- removal notes (--gone) exist for symbols no longer in the graph.
-- `applied` + `session_note` are the apply seal: apply stamps rows in place;
-- the digest write consumes applied rows into the committed digest and deletes
-- them. No state files anywhere — staging lives here, the record lives in
-- triefacts.
CREATE TABLE IF NOT EXISTS patches (
    id INTEGER PRIMARY KEY,
    qname TEXT NOT NULL,
    note TEXT NOT NULL,
    reason TEXT NOT NULL,
    session_id TEXT NOT NULL,
    created_at INTEGER NOT NULL,
    kind TEXT NOT NULL DEFAULT 'modify',
    rename_to TEXT,
    applied INTEGER NOT NULL DEFAULT 0,
    session_note TEXT NOT NULL DEFAULT ''
);
CREATE INDEX IF NOT EXISTS idx_patches_qname ON patches(qname);
CREATE INDEX IF NOT EXISTS idx_patches_session ON patches(session_id);
CREATE INDEX IF NOT EXISTS idx_patches_applied ON patches(applied);

-- Create patches target a symbol that does NOT yet exist, so they cannot key on
-- symbol_id (which is NOT NULL elsewhere). Kept in their own table to avoid
-- threading NULLs through every symbol_id consumer.
CREATE TABLE IF NOT EXISTS create_patches (
    id INTEGER PRIMARY KEY,
    target_file TEXT NOT NULL,
    target_qname TEXT NOT NULL,
    anchor_qname TEXT,
    parent_class TEXT,
    note TEXT NOT NULL,
    reason TEXT NOT NULL,
    session_id TEXT NOT NULL,
    created_at INTEGER NOT NULL,
    applied INTEGER NOT NULL DEFAULT 0,
    session_note TEXT NOT NULL DEFAULT ''
);
CREATE INDEX IF NOT EXISTS idx_create_patches_file ON create_patches(target_file);
CREATE INDEX IF NOT EXISTS idx_create_patches_session ON create_patches(session_id);
"""


@dataclass(frozen=True)
class FileRecord:
    path: str
    fingerprint: str
    last_scanned_at: int


@dataclass(frozen=True)
class FileStats:
    path: str
    total_symbols: int
    public_symbols: int


@dataclass(frozen=True)
class SymbolHit:
    qualified_name: str
    name: str
    kind: str
    file_path: str
    start_line: int
    signature: str | None
    is_public: bool


@dataclass(frozen=True)
class SymbolDetail:
    """Full per-symbol record with graph counts and the cached one-liner.

    Used by the MCP tools (`locate` / `explain` / `walk`) so a single DB roundtrip
    yields everything an agent response needs.
    """

    qualified_name: str
    name: str
    kind: str
    file_path: str
    start_line: int
    end_line: int
    signature: str | None
    is_public: bool
    inbound_count: int
    outbound_count: int
    one_liner: str  # "" when no triefact section exists
    role: str = ""  # LLM-inferred architectural role; "" when unknown
    boundary: str = ""  # LLM-inferred boundary class: entry/exit/internal; "" unknown
    decorators: str = ""  # newline-joined decorator lines; "" when none
    fingerprint: str = ""  # body_normalized_hash from the last scan — the same value
    # stamped into section sentinels at generation time, so sentinel != this
    # means the prose predates the current source ("" when unavailable).
    pending_patches: list[dict] = field(default_factory=list)
    pending_patch_count: int = 0


@dataclass(frozen=True)
class GrepPredicate:
    """Server-side filter object for `Store.grep_symbols`.

    Mirrors the agent-facing `grep.predicate` shape. Every field is optional;
    omitted fields mean "don't filter on this." `scope_prefix` and `scope_exclude`
    match against `file_path`. `inbound_count` / `outbound_count` accept
    `(min, max)` tuples (either bound may be None).
    """

    name_contains: str | None = None
    kind: str | None = (
        # One of trie.parse.types.KINDS, or "any", or None. See KINDS for the
        # full vocabulary (function/class/method/constant/module + the typed-
        # language kinds interface/type/enum/enum_member/property).
        None
    )
    scope_prefix: str | None = None
    scope_exclude: tuple[str, ...] = ()
    public_only: bool = False
    inbound_count_min: int | None = None
    inbound_count_max: int | None = None
    outbound_count_min: int | None = None
    outbound_count_max: int | None = None


def _synchronized(method: Callable) -> Callable:
    """Wrap a Store method so its whole body runs under ``self._lock``.

    Store reuses a single sqlite3 connection across all sync workers
    (``check_same_thread=False``), and SQLite forbids concurrent use of one
    connection from multiple threads. Without serialisation the races surface
    as misleading errors — ``OperationalError: unable to open database file``,
    spurious "database is locked", or ``recursive use of cursors`` — rather
    than a clean failure. The re-entrant lock makes the documented invariant
    real: every public method holds it for the duration of its DB work.
    """

    @functools.wraps(method)
    def wrapper(self: Store, *args: object, **kwargs: object) -> object:
        with self._lock:
            return method(self, *args, **kwargs)

    return wrapper


def _synchronize_store(cls: type) -> type:
    """Class decorator: apply ``_synchronized`` to every public method.

    Skips dunders (``__init__`` / ``__enter__`` / ``__exit__`` manage the lock's
    own lifecycle) and the ``transaction`` contextmanager, which yields control
    back to caller code and must not hold the lock across that yield — callers
    that use ``transaction`` are already responsible for serialising access, and
    the methods they call inside it re-acquire the re-entrant lock harmlessly.
    """
    skip = {"transaction"}
    for name, attr in list(vars(cls).items()):
        if name.startswith("__"):
            continue
        if name in skip:
            continue
        if callable(attr) and not isinstance(attr, (staticmethod, classmethod)):
            setattr(cls, name, _synchronized(attr))
    return cls


@_synchronize_store
class Store:
    """SQLite-backed persistence for trie's symbol graph and file fingerprints.

    Use as a context manager to ensure the connection is closed:

        with Store(db_path) as store:
            store.upsert_file(...)
    """

    def __init__(self, db_path: Path) -> None:
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        # Re-entrant lock guarding all connection access. Wave-based sync runs
        # multiple files concurrently; each may read (file_ref_counts) or write
        # (upsert_section_record) the store from a worker thread. SQLite forbids
        # concurrent use of one connection, so every public method must hold this
        # lock for its whole body — enforced automatically by the
        # @_synchronize_store class decorator rather than by hand. The lock is
        # re-entrant so methods that call other Store methods nest safely. DB ops
        # are microseconds next to the multi-second LLM calls, so serialising them
        # costs nothing measurable.
        self._lock = threading.RLock()
        self._open()

    def _open(self) -> None:
        # check_same_thread=False because the lock — not thread affinity —
        # provides the mutual exclusion sqlite requires.
        self._conn = sqlite3.connect(str(self.db_path), check_same_thread=False)
        self._conn.execute("PRAGMA foreign_keys = ON")
        # Detect a stale schema and nuke the DB before applying the current one. The DB is
        # a regenerable cache under .trie/, so a bump triggers a clean rebuild on the next
        # scan. Cheaper and less bug-prone than running migrations.
        existing_version: int | None = None
        try:
            row = self._conn.execute("SELECT version FROM schema_version").fetchone()
            existing_version = int(row[0]) if row else None
        except sqlite3.OperationalError:
            existing_version = None
        if existing_version is not None and existing_version != SCHEMA_VERSION:
            self._conn.close()
            self.db_path.unlink(missing_ok=True)
            # Same check_same_thread=False as the primary open above: the lock,
            # not thread affinity, provides sqlite's required mutual exclusion.
            # Dropping it here broke threaded sync immediately after a schema bump.
            self._conn = sqlite3.connect(str(self.db_path), check_same_thread=False)
            self._conn.execute("PRAGMA foreign_keys = ON")
            existing_version = None
        self._conn.executescript(SCHEMA_SQL)
        if existing_version is None:
            self._conn.execute("INSERT INTO schema_version (version) VALUES (?)", (SCHEMA_VERSION,))
            self._conn.commit()

    def close(self) -> None:
        self._conn.close()

    def __enter__(self) -> Store:
        return self

    def __exit__(self, *_args: object) -> None:
        self.close()

    @contextmanager
    def transaction(self) -> Iterator[sqlite3.Connection]:
        try:
            yield self._conn
            self._conn.commit()
        except Exception:
            self._conn.rollback()
            raise

    # --- file ops ---

    def get_file(self, path: str) -> FileRecord | None:
        row = self._conn.execute(
            "SELECT path, fingerprint, last_scanned_at FROM files WHERE path = ?",
            (path,),
        ).fetchone()
        return FileRecord(*row) if row else None

    def upsert_file(self, *, path: str, fingerprint: str, now: int | None = None) -> None:
        ts = now if now is not None else int(time.time())
        self._conn.execute(
            """
            INSERT INTO files (path, fingerprint, last_scanned_at) VALUES (?, ?, ?)
            ON CONFLICT(path) DO UPDATE SET
                fingerprint = excluded.fingerprint,
                last_scanned_at = excluded.last_scanned_at
            """,
            (path, fingerprint, ts),
        )
        self._conn.commit()

    def delete_file(self, path: str) -> None:
        self._conn.execute("DELETE FROM files WHERE path = ?", (path,))
        self._conn.commit()

    def list_files(self) -> list[FileRecord]:
        return [
            FileRecord(*row)
            for row in self._conn.execute(
                "SELECT path, fingerprint, last_scanned_at FROM files ORDER BY path"
            )
        ]

    # --- symbol ops ---

    def replace_file_symbols(self, file_path: str, symbols: list[Symbol]) -> None:
        """Atomically replace all symbols for a file."""
        with self.transaction() as conn:
            conn.execute("DELETE FROM symbols WHERE file_path = ?", (file_path,))
            conn.executemany(
                """
                INSERT INTO symbols (
                    file_path, qualified_name, name, kind, signature, docstring,
                    body_normalized_hash, signature_hash, is_public, start_line, end_line,
                    decorators
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                [
                    (
                        s.file_path,
                        s.qualified_name,
                        s.name,
                        s.kind,
                        s.signature,
                        s.docstring,
                        s.body_normalized_hash,
                        s.signature_hash,
                        int(s.is_public),
                        s.start_line,
                        s.end_line,
                        "\n".join(s.decorators),
                    )
                    for s in symbols
                ],
            )

    def count_symbols(self, *, file_path: str | None = None, public_only: bool = False) -> int:
        sql = "SELECT COUNT(*) FROM symbols"
        clauses: list[str] = []
        params: list[object] = []
        if file_path is not None:
            clauses.append("file_path = ?")
            params.append(file_path)
        if public_only:
            clauses.append("is_public = 1")
        if clauses:
            sql += " WHERE " + " AND ".join(clauses)
        return int(self._conn.execute(sql, params).fetchone()[0])

    def count_section_records(self) -> int:
        """Return the number of rows in ``triefact_sections``."""
        return int(self._conn.execute("SELECT COUNT(*) FROM triefact_sections").fetchone()[0])

    def count_symbols_missing_role(self) -> int:
        """Count symbols with no non-empty role tag in ``triefact_sections``.

        A symbol is "missing a role" if it has no section record, or its section's
        role is the empty string. Drives the role auto-backfill's short-circuit:
        zero means every symbol is tagged and no LLM classification is needed.
        """
        return int(
            self._conn.execute(
                """
                SELECT COUNT(*) FROM symbols s
                WHERE NOT EXISTS (
                    SELECT 1 FROM triefact_sections ts
                    WHERE ts.symbol_id = s.id AND ts.role != ''
                )
                """
            ).fetchone()[0]
        )

    # --- edge ops ---

    def replace_all_edges(self, references_by_file: dict[str, list[Reference]]) -> int:
        """Wipe the edges table, resolve references against current symbols, insert edges.

        References whose src or dst qualified_name is not present in the symbols table are
        silently dropped (likely an external import or a name the resolver over-matched).
        Returns the number of edges actually inserted.
        """
        qname_to_id: dict[str, int] = {}
        for row in self._conn.execute("SELECT id, qualified_name FROM symbols"):
            qname_to_id[row[1]] = row[0]

        rows: list[tuple[int, int, str]] = []
        seen_pairs: set[tuple[int, int]] = set()
        for refs in references_by_file.values():
            for ref in refs:
                src_id = qname_to_id.get(ref.src_qname)
                dst_id = qname_to_id.get(ref.target_qname)
                if src_id is None or dst_id is None or src_id == dst_id:
                    continue
                pair = (src_id, dst_id)
                if pair in seen_pairs:
                    continue
                seen_pairs.add(pair)
                rows.append((src_id, dst_id, ref.kind))

        with self.transaction() as conn:
            conn.execute("DELETE FROM edges")
            conn.executemany(
                "INSERT INTO edges (src_symbol_id, dst_symbol_id, kind) VALUES (?, ?, ?)",
                rows,
            )
        return len(rows)

    def references_in(self, qualified_name: str) -> list[str]:
        """Return src_qnames for every symbol that references `qualified_name`."""
        rows = self._conn.execute(
            """
            SELECT s_src.qualified_name
            FROM edges e
            JOIN symbols s_src ON s_src.id = e.src_symbol_id
            JOIN symbols s_dst ON s_dst.id = e.dst_symbol_id
            WHERE s_dst.qualified_name = ?
            """,
            (qualified_name,),
        ).fetchall()
        return [row[0] for row in rows]

    def references_in_with_files(self, qualified_name: str) -> list[tuple[str, str]]:
        """Return (src_qname, src_file_path) for every inbound reference."""
        rows = self._conn.execute(
            """
            SELECT s_src.qualified_name, s_src.file_path
            FROM edges e
            JOIN symbols s_src ON s_src.id = e.src_symbol_id
            JOIN symbols s_dst ON s_dst.id = e.dst_symbol_id
            WHERE s_dst.qualified_name = ?
            """,
            (qualified_name,),
        ).fetchall()
        return [(row[0], row[1]) for row in rows]

    def symbol_hashes_for_file(self, file_path: str) -> dict[str, str]:
        """Return `{qualified_name: body_normalized_hash}` for one file's symbols.

        Feeds `check_project`'s store-trust fast path: when the file's content
        fingerprint matches the store, these hashes are exactly what a fresh
        parse would produce, without paying for the parse.
        """
        rows = self._conn.execute(
            "SELECT qualified_name, body_normalized_hash FROM symbols WHERE file_path = ?",
            (file_path,),
        ).fetchall()
        return {r[0]: r[1] for r in rows}

    def qnames_in_file(self, file_path: str) -> list[str]:
        """Return qualified_names of all symbols defined in `file_path`."""
        rows = self._conn.execute(
            "SELECT qualified_name FROM symbols WHERE file_path = ? ORDER BY start_line",
            (file_path,),
        ).fetchall()
        return [row[0] for row in rows]

    def symbols_in_file_with_lines(self, file_path: str) -> list[tuple[str, int, int]]:
        """Return `(qname, start_line, end_line)` for every symbol in `file_path`,
        ordered by start_line. Used by `locate`'s grep fallback to attribute a
        matched source line to the smallest enclosing symbol.

        Returns an empty list when no symbols are recorded for the path (a file
        outside the scanned set or a freshly-deleted file). The shape is a
        compact tuple rather than `SymbolHit`/`SymbolDetail` because the caller
        only needs the line-range bracket; full detail is fetched per-match.
        """
        rows = self._conn.execute(
            """
            SELECT qualified_name, start_line, end_line
            FROM symbols
            WHERE file_path = ?
            ORDER BY start_line
            """,
            (file_path,),
        ).fetchall()
        return [(row[0], int(row[1]), int(row[2])) for row in rows]

    def search_symbols(self, name_pattern: str, *, limit: int = 50) -> list[SymbolHit]:
        """Find symbols whose `name` (the local part, not qname) contains `name_pattern`.

        Case-insensitive substring match. Use this for "find_symbol" style queries from
        agents — they typically search by local name, not qualified name.
        """
        rows = self._conn.execute(
            """
            SELECT qualified_name, name, kind, file_path, start_line, signature, is_public
            FROM symbols
            WHERE name LIKE ?
            ORDER BY is_public DESC, qualified_name
            LIMIT ?
            """,
            (f"%{name_pattern}%", limit),
        ).fetchall()
        return [
            SymbolHit(
                qualified_name=row[0],
                name=row[1],
                kind=row[2],
                file_path=row[3],
                start_line=row[4],
                signature=row[5],
                is_public=bool(row[6]),
            )
            for row in rows
        ]

    def references_out(self, qualified_name: str) -> list[str]:
        """Return target_qnames for every reference originating from `qualified_name`."""
        rows = self._conn.execute(
            """
            SELECT s_dst.qualified_name
            FROM edges e
            JOIN symbols s_src ON s_src.id = e.src_symbol_id
            JOIN symbols s_dst ON s_dst.id = e.dst_symbol_id
            WHERE s_src.qualified_name = ?
            """,
            (qualified_name,),
        ).fetchall()
        return [row[0] for row in rows]

    def count_edges(self) -> int:
        return int(self._conn.execute("SELECT COUNT(*) FROM edges").fetchone()[0])

    def inbound_count_per_symbol(self) -> dict[str, int]:
        """qualified_name -> number of inbound edges. Used to detect hub symbols."""
        rows = self._conn.execute(
            """
            SELECT s.qualified_name, COUNT(*) FROM edges e
            JOIN symbols s ON s.id = e.dst_symbol_id
            GROUP BY s.qualified_name
            """
        ).fetchall()
        return {row[0]: int(row[1]) for row in rows}

    def file_ref_counts(self, file_path: str) -> tuple[int, int]:
        """Return (inbound, outbound) cross-file edge counts for `file_path`.

        Inbound: edges whose dst is a symbol in this file and whose src is in another file.
        Outbound: edges whose src is in this file and whose dst is in another file.
        Intra-file edges are excluded — they aren't "callers from elsewhere" or "calls
        out to elsewhere", which is what these counts surface in the triefact metadata.
        """
        with self._lock:
            inbound = int(
                self._conn.execute(
                    """
                    SELECT COUNT(*) FROM edges e
                    JOIN symbols s_dst ON s_dst.id = e.dst_symbol_id
                    JOIN symbols s_src ON s_src.id = e.src_symbol_id
                    WHERE s_dst.file_path = ? AND s_src.file_path != ?
                    """,
                    (file_path, file_path),
                ).fetchone()[0]
            )
            outbound = int(
                self._conn.execute(
                    """
                    SELECT COUNT(*) FROM edges e
                    JOIN symbols s_src ON s_src.id = e.src_symbol_id
                    JOIN symbols s_dst ON s_dst.id = e.dst_symbol_id
                    WHERE s_src.file_path = ? AND s_dst.file_path != ?
                    """,
                    (file_path, file_path),
                ).fetchone()[0]
            )
        return inbound, outbound

    def file_stats(self) -> list[FileStats]:
        """Per-file counts joined from files + symbols, used by the bootstrap ranker.

        The `public_symbols` field is a legacy name; under symbol-level sync trie
        documents every parser-surfaced symbol regardless of the leading-underscore
        convention, so the count returned here is "documentable symbols," which
        equals the total. The field name is preserved for API stability.
        """
        rows = self._conn.execute(
            """
            SELECT
                f.path,
                COUNT(s.id) AS total
            FROM files f
            LEFT JOIN symbols s ON s.file_path = f.path
            GROUP BY f.path
            ORDER BY f.path
            """
        ).fetchall()
        return [
            FileStats(path=row[0], total_symbols=int(row[1]), public_symbols=int(row[1]))
            for row in rows
        ]

    # --- triefact_sections ops ---

    def upsert_section_record(
        self,
        *,
        triefact_path: str,
        symbol_qname: str,
        section_fingerprint: str,
        one_liner: str,
        role: str = "",
        boundary: str = "",
        now: int | None = None,
    ) -> None:
        """Record (or refresh) the metadata trie keeps in lockstep with a generated section.

        Looks up the symbol's current id from `symbols`. If the symbol no longer exists
        (e.g. renamed/deleted between scan and sync), the row is silently skipped — the
        next scan + sync will clean things up.

        `role` is the LLM-inferred architectural role tag; '' when unknown. `boundary`
        is the LLM-inferred boundary class (entry/exit/internal); '' when unknown. An
        empty value on update does not clobber a previously-stored non-empty one, so a
        metadata-only refresh that lacks LLM inference preserves the existing tags.
        """
        ts = now if now is not None else int(time.time())
        with self._lock:
            row = self._conn.execute(
                "SELECT id FROM symbols WHERE qualified_name = ? LIMIT 1",
                (symbol_qname,),
            ).fetchone()
            if row is None:
                return
            symbol_id = int(row[0])
            self._conn.execute(
                """
                INSERT INTO triefact_sections
                    (triefact_path, symbol_id, section_fingerprint, one_liner, role,
                     boundary, last_generated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(triefact_path, symbol_id) DO UPDATE SET
                    section_fingerprint = excluded.section_fingerprint,
                    one_liner = excluded.one_liner,
                    role = CASE
                        WHEN excluded.role != '' THEN excluded.role
                        ELSE triefact_sections.role
                    END,
                    boundary = CASE
                        WHEN excluded.boundary != '' THEN excluded.boundary
                        ELSE triefact_sections.boundary
                    END,
                    last_generated_at = excluded.last_generated_at
                """,
                (
                    triefact_path,
                    symbol_id,
                    section_fingerprint,
                    one_liner,
                    role,
                    boundary,
                    ts,
                ),
            )
            self._conn.commit()

    def one_liner_for(self, qualified_name: str) -> str:
        """Return the cached one-liner for a symbol, or '' if no section exists yet."""
        row = self._conn.execute(
            """
            SELECT ts.one_liner FROM triefact_sections ts
            JOIN symbols s ON s.id = ts.symbol_id
            WHERE s.qualified_name = ?
            LIMIT 1
            """,
            (qualified_name,),
        ).fetchone()
        if row is None or row[0] is None:
            return ""
        return str(row[0])

    def one_liners_for(self, qnames: list[str]) -> dict[str, str]:
        """Batch one-liner lookup. Returns {qname: one_liner} for found entries only."""
        if not qnames:
            return {}
        placeholders = ",".join("?" for _ in qnames)
        rows = self._conn.execute(
            f"""
            SELECT s.qualified_name, ts.one_liner FROM triefact_sections ts
            JOIN symbols s ON s.id = ts.symbol_id
            WHERE s.qualified_name IN ({placeholders})
            """,
            qnames,
        ).fetchall()
        return {row[0]: (row[1] or "") for row in rows}

    def add_patch(
        self,
        qname: str,
        note: str,
        reason: str,
        session_id: str,
        *,
        kind: str = "modify",
        rename_to: str | None = None,
        require_symbol: bool = True,
    ) -> int:
        """Add a new patch (intent note) row keyed by qname.

        `kind` is one of 'modify' | 'delete' | 'rename'. `rename_to` is the new
        local name, required when kind == 'rename'. With `require_symbol`
        (default) a KeyError is raised when the qname isn't in the graph —
        typo protection; pass False for removal notes (`--gone`), whose
        symbols are gone from the graph by definition. Rows survive graph
        refreshes: they carry no FK into the symbols table.
        """
        if require_symbol:
            row = self._conn.execute(
                "SELECT id FROM symbols WHERE qualified_name = ? LIMIT 1",
                (qname,),
            ).fetchone()
            if row is None:
                raise KeyError(f"qname {qname!r} not found in the graph")
        now = int(time.time())
        cur = self._conn.execute(
            """INSERT INTO patches
               (qname, note, reason, session_id, created_at, kind, rename_to)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (qname, note, reason, session_id, now, kind, rename_to),
        )
        self._conn.commit()
        assert cur.lastrowid is not None, "INSERT of patch should produce a rowid"
        return int(cur.lastrowid)

    def add_delete_patch(self, qname: str, reason: str, session_id: str) -> int:
        """Stage a deletion of an existing symbol. Raises KeyError if absent."""
        return self.add_patch(qname, "", reason, session_id, kind="delete")

    def add_rename_patch(self, qname: str, new_name: str, reason: str, session_id: str) -> int:
        """Stage a rename of an existing symbol to `new_name` (local name)."""
        return self.add_patch(qname, "", reason, session_id, kind="rename", rename_to=new_name)

    def add_create_patch(
        self,
        *,
        target_file: str,
        target_qname: str,
        note: str,
        reason: str,
        session_id: str,
        anchor_qname: str | None = None,
        parent_class: str | None = None,
    ) -> int:
        """Stage creation of a NEW symbol that does not yet exist in the graph.

        Returns the new create_patch id. Does not validate that target_qname is
        absent — callers (the MCP tool) enforce that for a clean error message.
        """
        now = int(time.time())
        cur = self._conn.execute(
            """INSERT INTO create_patches
               (target_file, target_qname, anchor_qname, parent_class, note, reason,
                session_id, created_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (target_file, target_qname, anchor_qname, parent_class, note, reason, session_id, now),
        )
        self._conn.commit()
        assert cur.lastrowid is not None, "INSERT of create_patch should produce a rowid"
        return int(cur.lastrowid)

    def get_create_patches_grouped(self, *, applied: bool | None = None) -> dict[str, list[dict]]:
        """Create patches grouped by target_file; `applied` filters the seal state."""
        sql = """SELECT id, target_file, target_qname, anchor_qname, parent_class,
                      note, reason, session_id, created_at, applied, session_note
               FROM create_patches"""
        params: list = []
        if applied is not None:
            sql += " WHERE applied = ?"
            params.append(1 if applied else 0)
        rows = self._conn.execute(sql + " ORDER BY target_file, id", params).fetchall()
        result: dict[str, list[dict]] = {}
        for r in rows:
            result.setdefault(str(r[1]), []).append(
                {
                    "id": int(r[0]),
                    "target_file": r[1],
                    "target_qname": r[2],
                    "anchor_qname": r[3],
                    "parent_class": r[4],
                    "note": r[5],
                    "reason": r[6],
                    "session_id": r[7],
                    "created_at": int(r[8]),
                    "applied": bool(r[9]),
                    "session_note": r[10] or "",
                }
            )
        return result

    def delete_create_patches(
        self,
        *,
        target_qname: str | None = None,
        session_id: str | None = None,
        all: bool = False,
    ) -> int:
        """Delete create patches by target_qname / session_id / all."""
        if all:
            count = self._conn.execute("DELETE FROM create_patches").rowcount
            self._conn.commit()
            return count
        if target_qname is not None:
            count = self._conn.execute(
                "DELETE FROM create_patches WHERE target_qname = ?", (target_qname,)
            ).rowcount
            self._conn.commit()
            return count
        if session_id is not None:
            count = self._conn.execute(
                "DELETE FROM create_patches WHERE session_id = ?", (session_id,)
            ).rowcount
            self._conn.commit()
            return count
        return 0

    @staticmethod
    def _patch_row_to_dict(r) -> dict:
        return {
            "id": int(r[0]),
            "note": r[1],
            "reason": r[2],
            "session_id": r[3],
            "created_at": int(r[4]),
            "kind": r[5] or "modify",
            "rename_to": r[6],
            "applied": bool(r[7]),
            "session_note": r[8] or "",
        }

    _PATCH_COLS = "id, note, reason, session_id, created_at, kind, rename_to, applied, session_note"

    def get_patches_for_qname(self, qname: str, *, applied: bool | None = None) -> list[dict]:
        """Patches for one qname; `applied` filters the seal state (None = all)."""
        sql = f"SELECT {self._PATCH_COLS} FROM patches WHERE qname = ?"
        params: list = [qname]
        if applied is not None:
            sql += " AND applied = ?"
            params.append(1 if applied else 0)
        rows = self._conn.execute(sql + " ORDER BY id", params).fetchall()
        return [self._patch_row_to_dict(r) for r in rows]

    def get_all_patches_grouped(self, *, applied: bool | None = None) -> dict[str, list[dict]]:
        """All patches grouped by qname; `applied` filters the seal state."""
        sql = f"SELECT qname, {self._PATCH_COLS} FROM patches"
        params: list = []
        if applied is not None:
            sql += " WHERE applied = ?"
            params.append(1 if applied else 0)
        rows = self._conn.execute(sql + " ORDER BY qname, id", params).fetchall()
        result: dict[str, list[dict]] = {}
        for r in rows:
            result.setdefault(str(r[0]), []).append(self._patch_row_to_dict(r[1:]))
        return result

    def mark_patches_applied(self, session_note: str) -> int:
        """Seal every unapplied row (patches + creates) with the session note.

        The apply step: rows stay in the table until the digest write consumes
        them into the committed digest. Returns the number of rows sealed.
        """
        n = self._conn.execute(
            "UPDATE patches SET applied = 1, session_note = ? WHERE applied = 0",
            (session_note,),
        ).rowcount
        n += self._conn.execute(
            "UPDATE create_patches SET applied = 1, session_note = ? WHERE applied = 0",
            (session_note,),
        ).rowcount
        self._conn.commit()
        return n

    def delete_applied_patches(self) -> int:
        """Consume sealed rows — their content now lives in a committed digest."""
        n = self._conn.execute("DELETE FROM patches WHERE applied = 1").rowcount
        n += self._conn.execute("DELETE FROM create_patches WHERE applied = 1").rowcount
        self._conn.commit()
        return n

    def delete_patches(
        self,
        *,
        qname: str | None = None,
        session_id: str | None = None,
        all: bool = False,
    ) -> int:
        """Delete patches matching the given criteria. Returns number of deleted rows.

        At least one of qname / session_id / all must be set.
        """
        if all:
            count = self._conn.execute("DELETE FROM patches").rowcount
            self._conn.commit()
            return count
        if qname is not None:
            count = self._conn.execute("DELETE FROM patches WHERE qname = ?", (qname,)).rowcount
            self._conn.commit()
            return count
        if session_id is not None:
            count = self._conn.execute(
                "DELETE FROM patches WHERE session_id = ?", (session_id,)
            ).rowcount
            self._conn.commit()
            return count
        return 0

    def get_patched_qnames(self, *, applied: bool | None = None) -> list[str]:
        """Qnames with at least one patch row; `applied` filters the seal state."""
        sql = "SELECT DISTINCT qname FROM patches"
        params: list = []
        if applied is not None:
            sql += " WHERE applied = ?"
            params.append(1 if applied else 0)
        rows = self._conn.execute(sql + " ORDER BY qname", params).fetchall()
        return [r[0] for r in rows]

    def patch_summary(self) -> dict[str, object]:
        """Aggregate pending-patch state — the single shared reader for status /
        activity() / patch_list.

        Returns {total_patches, symbol_count, create_count, by_origin, qnames}.
        `by_origin` buckets symbols by patch session origin (agent/cascade/mixed).
        """
        patch_rows = self._conn.execute("SELECT qname, session_id FROM patches").fetchall()
        sessions_by_qname: dict[str, set[str]] = {}
        for qname, sid in patch_rows:
            sessions_by_qname.setdefault(qname, set()).add(sid)
        by_origin = {"agent": 0, "cascade": 0, "mixed": 0}
        for sessions in sessions_by_qname.values():
            if sessions == {"cascade"}:
                by_origin["cascade"] += 1
            elif len(sessions) > 1:
                by_origin["mixed"] += 1
            else:
                by_origin["agent"] += 1
        create_count = int(self._conn.execute("SELECT COUNT(*) FROM create_patches").fetchone()[0])
        return {
            "total_patches": len(patch_rows),
            "symbol_count": len(sessions_by_qname),
            "create_count": create_count,
            "by_origin": by_origin,
            "qnames": sorted(sessions_by_qname.keys()),
        }

    # --- symbol detail / locate ---

    def get_symbol_detail(self, qualified_name: str) -> SymbolDetail | None:
        """Return everything the agent surface needs about one symbol in a single query."""
        row = self._conn.execute(
            """
            SELECT
                s.qualified_name, s.name, s.kind, s.file_path,
                s.start_line, s.end_line, s.signature, s.is_public,
                (SELECT COUNT(*) FROM edges WHERE dst_symbol_id = s.id) AS in_count,
                (SELECT COUNT(*) FROM edges WHERE src_symbol_id = s.id) AS out_count,
                COALESCE(
                    (SELECT one_liner FROM triefact_sections WHERE symbol_id = s.id LIMIT 1),
                    ''
                ) AS one_liner,
                COALESCE(
                    (SELECT role FROM triefact_sections WHERE symbol_id = s.id LIMIT 1),
                    ''
                ) AS role,
                COALESCE(
                    (SELECT boundary FROM triefact_sections WHERE symbol_id = s.id LIMIT 1),
                    ''
                ) AS boundary,
                COALESCE(s.decorators, '') AS decorators,
                COALESCE(s.body_normalized_hash, '') AS fingerprint
            FROM symbols s
            WHERE s.qualified_name = ?
            LIMIT 1
            """,
            (qualified_name,),
        ).fetchone()
        if row is None:
            return None
        patches = self.get_patches_for_qname(qualified_name)
        return SymbolDetail(
            qualified_name=row[0],
            name=row[1],
            kind=row[2],
            file_path=row[3],
            start_line=int(row[4]),
            end_line=int(row[5]),
            signature=row[6],
            is_public=bool(row[7]),
            inbound_count=int(row[8]),
            outbound_count=int(row[9]),
            one_liner=row[10] or "",
            role=row[11] or "",
            boundary=row[12] or "",
            decorators=row[13] or "",
            fingerprint=row[14] or "",
            pending_patches=patches,
            pending_patch_count=len(patches),
        )

    def grep_symbols(
        self,
        predicate: GrepPredicate,
        *,
        rank_by: str = "public_first",
        limit: int = 10,
    ) -> list[SymbolDetail]:
        """Predicate-driven symbol search. Returns SymbolDetails sorted per `rank_by`.

        `rank_by` accepted values: `"public_first"`, `"inbound_count"`, `"alphabetical"`.
        Any other value falls back to `"public_first"`.
        """
        clauses: list[str] = []
        params: list[object] = []

        if predicate.name_contains:
            clauses.append("LOWER(s.name) LIKE LOWER(?)")
            params.append(f"%{predicate.name_contains}%")
        if predicate.kind and predicate.kind != "any":
            clauses.append("s.kind = ?")
            params.append(predicate.kind)
        if predicate.scope_prefix:
            clauses.append("s.file_path LIKE ?")
            params.append(f"{predicate.scope_prefix}%")
        for exc in predicate.scope_exclude:
            clauses.append("s.file_path NOT LIKE ?")
            params.append(f"{exc}%")
        if predicate.public_only:
            clauses.append("s.is_public = 1")

        # Edge-count predicates: evaluate via scalar subqueries inside the WHERE clause.
        # We can't use the SELECT aliases (in_count / out_count) here — SQLite resolves
        # WHERE before the SELECT list — so we repeat the subquery. The optimizer is
        # fine with this for the query volumes the agent surface drives.
        in_subq = "(SELECT COUNT(*) FROM edges WHERE dst_symbol_id = s.id)"
        out_subq = "(SELECT COUNT(*) FROM edges WHERE src_symbol_id = s.id)"
        if predicate.inbound_count_min is not None:
            clauses.append(f"{in_subq} >= ?")
            params.append(predicate.inbound_count_min)
        if predicate.inbound_count_max is not None:
            clauses.append(f"{in_subq} <= ?")
            params.append(predicate.inbound_count_max)
        if predicate.outbound_count_min is not None:
            clauses.append(f"{out_subq} >= ?")
            params.append(predicate.outbound_count_min)
        if predicate.outbound_count_max is not None:
            clauses.append(f"{out_subq} <= ?")
            params.append(predicate.outbound_count_max)

        # Production code before test code within every ranking bucket. This
        # must live in the SQL, not just the post-fetch scoring: with a LIMIT,
        # ASCII ordering ('tests/' < 'trie/') filled the entire result page
        # with test symbols before any production symbol was even fetched, so
        # no downstream re-ranking could ever repair it. Mirrors the path
        # heuristic in `trie.mcp_server._is_test_symbol`.
        test_demote = (
            "(CASE WHEN s.file_path LIKE 'tests/%' OR s.file_path LIKE '%/tests/%' "
            "OR s.file_path LIKE 'test\\_%' ESCAPE '\\' OR s.file_path LIKE '%/test\\_%' ESCAPE '\\' "
            "OR s.file_path LIKE '%conftest.py' THEN 1 ELSE 0 END)"
        )
        if rank_by == "inbound_count":
            order = f"in_count DESC, s.is_public DESC, {test_demote}, s.qualified_name"
        elif rank_by == "alphabetical":
            order = "s.qualified_name"
        else:  # public_first or unknown
            order = f"s.is_public DESC, {test_demote}, s.qualified_name"

        where_sql = ("WHERE " + " AND ".join(clauses)) if clauses else ""
        patch_subq = "(SELECT COUNT(*) FROM patches WHERE qname = s.qualified_name)"
        sql = f"""
            SELECT
                s.qualified_name, s.name, s.kind, s.file_path,
                s.start_line, s.end_line, s.signature, s.is_public,
                {in_subq} AS in_count,
                {out_subq} AS out_count,
                COALESCE(
                    (SELECT one_liner FROM triefact_sections WHERE symbol_id = s.id LIMIT 1),
                    ''
                ) AS one_liner,
                COALESCE(
                    (SELECT role FROM triefact_sections WHERE symbol_id = s.id LIMIT 1),
                    ''
                ) AS role,
                COALESCE(
                    (SELECT boundary FROM triefact_sections WHERE symbol_id = s.id LIMIT 1),
                    ''
                ) AS boundary,
                COALESCE(s.decorators, '') AS decorators,
                {patch_subq} AS patch_count
            FROM symbols s
            {where_sql}
            ORDER BY {order}
            LIMIT ?
        """
        params.append(limit)
        rows = self._conn.execute(sql, params).fetchall()
        return [
            SymbolDetail(
                qualified_name=row[0],
                name=row[1],
                kind=row[2],
                file_path=row[3],
                start_line=int(row[4]),
                end_line=int(row[5]),
                signature=row[6],
                is_public=bool(row[7]),
                inbound_count=int(row[8]),
                outbound_count=int(row[9]),
                one_liner=row[10] or "",
                role=row[11] or "",
                boundary=row[12] or "",
                decorators=row[13] or "",
                pending_patch_count=int(row[14]),
            )
            for row in rows
        ]

    def all_symbol_names(self) -> list[str]:
        """All local symbol names. Used to build fuzzy-match suggestions on not-found."""
        rows = self._conn.execute("SELECT DISTINCT name FROM symbols").fetchall()
        return [row[0] for row in rows]

    def all_qualified_names(self) -> list[str]:
        """All qualified names. Used to suggest near-misses on explain/walk not-found."""
        rows = self._conn.execute("SELECT qualified_name FROM symbols").fetchall()
        return [row[0] for row in rows]

    def survey_symbols(self, *, public_only: bool = False) -> list[tuple[str, str, str, str]]:
        """Return `(qualified_name, kind, one_liner, file_path)` for every symbol.

        Feeds role-taxonomy derivation: a compact, codebase-wide picture (names +
        one-line descriptions + location) the model uses to propose a coherent role
        vocabulary. The one_liner is the section's, '' when no triefact exists yet.
        """
        where = "WHERE s.is_public = 1" if public_only else ""
        rows = self._conn.execute(
            f"""
            SELECT s.qualified_name, s.kind,
                   COALESCE(ts.one_liner, '') AS one_liner,
                   s.file_path
            FROM symbols s
            LEFT JOIN triefact_sections ts ON ts.symbol_id = s.id
            {where}
            ORDER BY s.file_path, s.start_line
            """
        ).fetchall()
        return [(r[0], r[1], r[2], r[3]) for r in rows]

    def find_paths(
        self,
        from_qname: str,
        to_qname: str,
        *,
        max_depth: int = 6,
        hub_threshold: int = 20,
        max_paths: int = 3,
    ) -> list[list[str]]:
        """BFS path-finding between two symbols following callee edges (src → dst).

        Returns a list of paths (each path is an ordered list of qnames from `from_qname`
        to `to_qname`). At most `max_paths` shortest paths are returned; an empty list
        means no path was found within `max_depth` hops.

        Hub symbols (inbound count > `hub_threshold`) are skipped during expansion — the
        same guard used by the cascade — to prevent paths that route through utility hubs
        like a shared config object.

        The search follows *callee* edges (from_qname calls something, that calls something
        else, …). To find paths in the other direction the caller should swap the arguments.
        """
        if from_qname == to_qname:
            return [[from_qname]]

        inbound_counts: dict[str, int] = {}
        for row in self._conn.execute(
            "SELECT s.qualified_name, COUNT(*) FROM edges e "
            "JOIN symbols s ON s.id = e.dst_symbol_id "
            "GROUP BY s.qualified_name"
        ):
            inbound_counts[row[0]] = int(row[1])

        # BFS; frontier carries (current_qname, path_so_far)
        from collections import deque

        found: list[list[str]] = []
        # visited tracks qnames we have already *started* a path through, but we allow
        # the same node on different paths (different routes). We use a per-path visited
        # set instead to allow the top-N distinct paths.
        initial: deque[tuple[str, list[str]]] = deque([(from_qname, [from_qname])])

        # Track globally-seen (qname, depth) to avoid re-expanding the same node at the
        # same or greater depth — avoids exponential blowup while still finding multiple paths.
        globally_seen: dict[str, int] = {from_qname: 0}

        while initial and len(found) < max_paths:
            qname, path = initial.popleft()
            depth = len(path) - 1
            if depth >= max_depth:
                continue

            # Skip hub expansion (but allow the start node regardless).
            if qname != from_qname and inbound_counts.get(qname, 0) > hub_threshold:
                continue

            callees = self.references_out(qname)
            for callee in callees:
                if callee in path:
                    # Cycle — skip.
                    continue
                new_path = [*path, callee]
                if callee == to_qname:
                    found.append(new_path)
                    if len(found) >= max_paths:
                        break
                    continue
                new_depth = len(new_path) - 1
                prev = globally_seen.get(callee)
                if prev is not None and prev <= new_depth:
                    continue
                globally_seen[callee] = new_depth
                initial.append((callee, new_path))

        return found
