from __future__ import annotations

import sqlite3
import time
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path

from trie.parse.python import Symbol
from trie.parse.references import Reference

SCHEMA_VERSION = 2

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
    UNIQUE (file_path, qualified_name)
);
CREATE INDEX IF NOT EXISTS idx_symbols_file ON symbols(file_path);
CREATE INDEX IF NOT EXISTS idx_symbols_qname ON symbols(qualified_name);

CREATE TABLE IF NOT EXISTS edges (
    src_symbol_id INTEGER NOT NULL REFERENCES symbols(id) ON DELETE CASCADE,
    dst_symbol_id INTEGER NOT NULL REFERENCES symbols(id) ON DELETE CASCADE,
    PRIMARY KEY (src_symbol_id, dst_symbol_id)
);
CREATE INDEX IF NOT EXISTS idx_edges_dst ON edges(dst_symbol_id);

CREATE TABLE IF NOT EXISTS triefact_sections (
    triefact_path TEXT NOT NULL,
    symbol_id INTEGER NOT NULL REFERENCES symbols(id) ON DELETE CASCADE,
    section_fingerprint TEXT NOT NULL,
    one_liner TEXT,
    last_generated_at INTEGER NOT NULL,
    PRIMARY KEY (triefact_path, symbol_id)
);
CREATE INDEX IF NOT EXISTS idx_sections_symbol ON triefact_sections(symbol_id);
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


@dataclass(frozen=True)
class LocatePredicate:
    """Server-side filter object for `Store.locate_symbols`.

    Mirrors the agent-facing `locate.predicate` shape. Every field is optional;
    omitted fields mean "don't filter on this." `scope_prefix` and `scope_exclude`
    match against `file_path`. `inbound_count` / `outbound_count` accept
    `(min, max)` tuples (either bound may be None).
    """

    name_contains: str | None = None
    kind: str | None = None  # "function" | "class" | "method" | "any" | None
    scope_prefix: str | None = None
    scope_exclude: tuple[str, ...] = ()
    public_only: bool = False
    inbound_count_min: int | None = None
    inbound_count_max: int | None = None
    outbound_count_min: int | None = None
    outbound_count_max: int | None = None


class Store:
    """SQLite-backed persistence for trie's symbol graph and file fingerprints.

    Use as a context manager to ensure the connection is closed:

        with Store(db_path) as store:
            store.upsert_file(...)
    """

    def __init__(self, db_path: Path) -> None:
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._open()

    def _open(self) -> None:
        self._conn = sqlite3.connect(str(self.db_path))
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
            self._conn = sqlite3.connect(str(self.db_path))
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
                    body_normalized_hash, signature_hash, is_public, start_line, end_line
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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

        rows: list[tuple[int, int]] = []
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
                rows.append((src_id, dst_id))

        with self.transaction() as conn:
            conn.execute("DELETE FROM edges")
            conn.executemany(
                "INSERT INTO edges (src_symbol_id, dst_symbol_id) VALUES (?, ?)",
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

    def qnames_in_file(self, file_path: str) -> list[str]:
        """Return qualified_names of all symbols defined in `file_path`."""
        rows = self._conn.execute(
            "SELECT qualified_name FROM symbols WHERE file_path = ? ORDER BY start_line",
            (file_path,),
        ).fetchall()
        return [row[0] for row in rows]

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
        now: int | None = None,
    ) -> None:
        """Record (or refresh) the metadata trie keeps in lockstep with a generated section.

        Looks up the symbol's current id from `symbols`. If the symbol no longer exists
        (e.g. renamed/deleted between scan and sync), the row is silently skipped — the
        next scan + sync will clean things up.
        """
        ts = now if now is not None else int(time.time())
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
                (triefact_path, symbol_id, section_fingerprint, one_liner, last_generated_at)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(triefact_path, symbol_id) DO UPDATE SET
                section_fingerprint = excluded.section_fingerprint,
                one_liner = excluded.one_liner,
                last_generated_at = excluded.last_generated_at
            """,
            (triefact_path, symbol_id, section_fingerprint, one_liner, ts),
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
                ) AS one_liner
            FROM symbols s
            WHERE s.qualified_name = ?
            LIMIT 1
            """,
            (qualified_name,),
        ).fetchone()
        if row is None:
            return None
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
        )

    def locate_symbols(
        self,
        predicate: LocatePredicate,
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

        if rank_by == "inbound_count":
            order = "in_count DESC, s.is_public DESC, s.qualified_name"
        elif rank_by == "alphabetical":
            order = "s.qualified_name"
        else:  # public_first or unknown
            order = "s.is_public DESC, s.qualified_name"

        where_sql = ("WHERE " + " AND ".join(clauses)) if clauses else ""
        sql = f"""
            SELECT
                s.qualified_name, s.name, s.kind, s.file_path,
                s.start_line, s.end_line, s.signature, s.is_public,
                {in_subq} AS in_count,
                {out_subq} AS out_count,
                COALESCE(
                    (SELECT one_liner FROM triefact_sections WHERE symbol_id = s.id LIMIT 1),
                    ''
                ) AS one_liner
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
