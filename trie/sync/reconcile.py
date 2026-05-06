from __future__ import annotations

from pathlib import Path

from trie.config import Config
from trie.scope import discover_files
from trie.sync.writer import TriefactFile


def find_orphan_triefacts(*, project_root: Path, config: Config) -> list[Path]:
    """Return absolute paths of trie-owned triefact files whose source has been deleted.

    A triefact is trie-owned if its YAML front-matter contains a `trie_version` key. Hand-
    authored Markdown files in the triefact tree (without that key) are left alone.
    Rename detection (orphan triefact + new file with matching content fingerprint) is
    deferred to v0.2.
    """
    project_root = project_root.resolve()
    src_root = (project_root / config.triefacts.source_root).resolve()
    triefacts_root = project_root / config.triefacts.root

    if not triefacts_root.exists():
        return []

    in_scope_sources: set[str] = set()
    for p in discover_files(project_root, config.scope):
        if p.is_relative_to(src_root):
            in_scope_sources.add(str(p.relative_to(src_root)))

    orphans: list[Path] = []
    for triefact_path in sorted(triefacts_root.rglob("*.md")):
        if not triefact_path.is_file():
            continue
        try:
            rel_triefact = triefact_path.relative_to(triefacts_root)
        except ValueError:
            continue
        # Triefact tree mirrors the source tree, so triefacts/foo/bar.md -> foo/bar.py
        expected_source = str(rel_triefact.with_suffix(".py"))
        if expected_source in in_scope_sources:
            continue

        try:
            triefact = TriefactFile.parse(triefact_path.read_text())
        except (OSError, UnicodeDecodeError):
            continue
        if "trie_version" not in triefact.front_matter:
            continue

        orphans.append(triefact_path)

    return orphans


def remove_orphan_triefacts(*, project_root: Path, config: Config) -> list[Path]:
    """Delete orphan trie-owned triefact files. Returns the absolute paths that were deleted."""
    orphans = find_orphan_triefacts(project_root=project_root, config=config)
    for path in orphans:
        path.unlink()
    return orphans
