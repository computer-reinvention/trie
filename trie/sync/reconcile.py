from __future__ import annotations

from pathlib import Path

from trie.config import Config
from trie.scope import discover_files
from trie.sync.writer import DocFile


def find_orphan_docs(*, project_root: Path, config: Config) -> list[Path]:
    """Return absolute paths of trie-owned doc files whose source has been deleted.

    A doc is trie-owned if its YAML front-matter contains a `trie_version` key. Hand-
    authored Markdown files in the doc tree (without that key) are left alone.
    Rename detection (orphan doc + new file with matching content fingerprint) is deferred
    to v0.2.
    """
    project_root = project_root.resolve()
    src_root = (project_root / config.docs.source_root).resolve()
    docs_root = project_root / config.docs.root

    if not docs_root.exists():
        return []

    in_scope_sources: set[str] = set()
    for p in discover_files(project_root, config.scope):
        if p.is_relative_to(src_root):
            in_scope_sources.add(str(p.relative_to(src_root)))

    orphans: list[Path] = []
    for doc_path in sorted(docs_root.rglob("*.md")):
        if not doc_path.is_file():
            continue
        try:
            rel_doc = doc_path.relative_to(docs_root)
        except ValueError:
            continue
        # Doc tree mirrors the source tree, so docs/foo/bar.md -> foo/bar.py
        expected_source = str(rel_doc.with_suffix(".py"))
        if expected_source in in_scope_sources:
            continue

        try:
            doc = DocFile.parse(doc_path.read_text())
        except (OSError, UnicodeDecodeError):
            continue
        if "trie_version" not in doc.front_matter:
            continue

        orphans.append(doc_path)

    return orphans


def remove_orphan_docs(*, project_root: Path, config: Config) -> list[Path]:
    """Delete orphan trie-owned doc files. Returns the absolute paths that were deleted."""
    orphans = find_orphan_docs(project_root=project_root, config=config)
    for path in orphans:
        path.unlink()
    return orphans
