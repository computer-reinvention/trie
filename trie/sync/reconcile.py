from __future__ import annotations

from pathlib import Path

from trie.config import Config
from trie.parse import registry
from trie.scope import discover_files
from trie.sync.writer import TriefactFile


def _candidate_sources(rel_triefact: Path) -> list[str]:
    """Source paths a `.md` triefact could mirror, one per registered language.

    The triefact tree mirrors the source tree with `.md` swapped for the source
    suffix, so `foo/bar.md` could be `foo/bar.py`, `foo/bar.ts`, ... and
    `foo/bar.d.md` could be `foo/bar.d.ts`. Probing every registered suffix
    keeps a multi-language triefact from being flagged orphan just because it
    isn't Python.
    """
    candidates: list[str] = []
    for suffix in registry.source_suffixes():
        # `.d.ts` is a compound suffix; the triefact for it is `foo.d.md`, so
        # strip the trailing `.md` and append the full source suffix.
        base = str(rel_triefact)
        if base.endswith(".md"):
            base = base[: -len(".md")]
        # For compound source suffixes (".d.ts") the triefact base already
        # carries the inner part (".d"), so map ".d" + ".ts" forms correctly.
        if suffix.count(".") > 1:
            inner = suffix.rsplit(".", 1)[0]  # ".d.ts" -> ".d"
            if base.endswith(inner):
                candidates.append(base[: -len(inner)] + suffix)
            continue
        candidates.append(base + suffix)
    return candidates


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
        # Triefact tree mirrors the source tree. A `.md` triefact maps to one
        # source per registered language (foo.md -> foo.py | foo.ts | ...);
        # if any candidate is in scope the triefact is not an orphan.
        if any(src in in_scope_sources for src in _candidate_sources(rel_triefact)):
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
