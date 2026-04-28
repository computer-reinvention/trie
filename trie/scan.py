from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path

from trie.config import Config
from trie.graph.store import Store
from trie.parse.references import Reference, extract_file_data
from trie.scope import discover_files


@dataclass(frozen=True)
class ScanResult:
    project_root: Path
    files_total: int
    files_new: int
    files_updated: int
    files_unchanged: int
    files_removed: int
    symbols_total: int
    edges_total: int


def file_fingerprint(text: str) -> str:
    return sha256(text.encode("utf-8")).hexdigest()


def scan_project(*, project_root: Path, config: Config, store: Store) -> ScanResult:
    """Walk the project, parse changed files, persist symbols. Idempotent.

    Files whose fingerprint matches the stored value are skipped without re-parsing.
    Files in the DB that are no longer in scope or on disk are removed (cascade deletes
    their symbols).
    """
    project_root = project_root.resolve()
    src_root = (project_root / config.docs.source_root).resolve()
    discovered = discover_files(project_root, config.scope)

    discovered_rel: dict[str, Path] = {}
    for p in discovered:
        if p.is_relative_to(src_root):
            rel = str(p.relative_to(src_root))
            discovered_rel[rel] = p

    db_index = {f.path: f for f in store.list_files()}

    files_new = 0
    files_updated = 0
    files_unchanged = 0
    files_removed = 0
    symbols_total = 0
    pending_refs: dict[str, list[Reference]] = {}

    for rel, abs_path in discovered_rel.items():
        text = abs_path.read_text()
        fp = file_fingerprint(text)
        existing = db_index.get(rel)

        # Always parse — tree-sitter is fast and we need the references regardless of
        # whether the symbols changed (cross-file targets may have moved).
        file_data = extract_file_data(abs_path, source_root=src_root)
        pending_refs[rel] = file_data.references

        if existing is not None and existing.fingerprint == fp:
            files_unchanged += 1
            symbols_total += store.count_symbols(file_path=rel)
            continue

        store.upsert_file(path=rel, fingerprint=fp)
        store.replace_file_symbols(rel, file_data.symbols)
        symbols_total += len(file_data.symbols)
        if existing is None:
            files_new += 1
        else:
            files_updated += 1

    for rel in db_index:
        if rel not in discovered_rel:
            store.delete_file(rel)
            files_removed += 1

    # Edges are regenerated from scratch on every scan — symbol IDs may have changed
    # for any updated file, invalidating prior edges via the FK CASCADE.
    edges_total = store.replace_all_edges(pending_refs)

    return ScanResult(
        project_root=project_root,
        files_total=len(discovered_rel),
        files_new=files_new,
        files_updated=files_updated,
        files_unchanged=files_unchanged,
        files_removed=files_removed,
        symbols_total=symbols_total,
        edges_total=edges_total,
    )
