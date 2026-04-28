from __future__ import annotations

import sqlite3
import time
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path

from trie.parse.python import Symbol

SCHEMA_VERSION = 1

# All schema is created if not present. edges and doc_sections are defined now so that
# M4/M3 don't require a migration; they remain unpopulated until those milestones land.
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
    confidence TEXT NOT NULL,
    PRIMARY KEY (src_symbol_id, dst_symbol_id)
);
CREATE INDEX IF NOT EXISTS idx_edges_dst ON edges(dst_symbol_id);

CREATE TABLE IF NOT EXISTS doc_sections (
    doc_path TEXT NOT NULL,
    symbol_id INTEGER NOT NULL REFERENCES symbols(id) ON DELETE CASCADE,
    section_fingerprint TEXT NOT NULL,
    last_generated_at INTEGER NOT NULL,
    PRIMARY KEY (doc_path, symbol_id)
);
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


class Store:
    """SQLite-backed persistence for trie's symbol graph and file fingerprints.

    Use as a context manager to ensure the connection is closed:

        with Store(db_path) as store:
            store.upsert_file(...)
    """

    def __init__(self, db_path: Path) -> None:
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(str(self.db_path))
        self._conn.execute("PRAGMA foreign_keys = ON")
        self._conn.executescript(SCHEMA_SQL)
        existing = self._conn.execute("SELECT version FROM schema_version").fetchone()
        if existing is None:
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

    def file_stats(self) -> list[FileStats]:
        """Per-file counts joined from files + symbols, used by the bootstrap ranker."""
        rows = self._conn.execute(
            """
            SELECT
                f.path,
                COUNT(s.id) AS total,
                COUNT(CASE WHEN s.is_public = 1 THEN 1 END) AS public_count
            FROM files f
            LEFT JOIN symbols s ON s.file_path = f.path
            GROUP BY f.path
            ORDER BY f.path
            """
        ).fetchall()
        return [
            FileStats(path=row[0], total_symbols=int(row[1]), public_symbols=int(row[2]))
            for row in rows
        ]
