from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from pathlib import Path

from trie.config import Config
from trie.parse.python import extract_symbols
from trie.scope import discover_files
from trie.sync.writer import Section, TriefactFile


class StaleReason(StrEnum):
    MISSING_TRIEFACT = "missing_triefact"  # source has public symbols but no triefact file
    MISSING_SECTION = "missing_section"  # public symbol present, no section for it
    STALE_SECTION = "stale_section"  # section fingerprint != current source hash
    ORPHAN_SECTION = "orphan_section"  # section exists but symbol is gone


@dataclass(frozen=True)
class StaleItem:
    source_path: str  # source-root-relative
    triefact_path: str  # source-root-relative
    reason: StaleReason
    qualified_name: str | None  # set for symbol-level reasons; None for missing_triefact


@dataclass(frozen=True)
class CheckResult:
    items: list[StaleItem] = field(default_factory=list)

    @property
    def is_clean(self) -> bool:
        return not self.items


def _triefact_path_for(rel_source: str, config: Config) -> str:
    """Mirror src/foo.py -> {triefacts.root}/src/foo.md as a source-root-relative path."""
    p = Path(rel_source)
    return str(Path(config.triefacts.root) / p.with_suffix(".md"))


def check_project(*, project_root: Path, config: Config) -> CheckResult:
    """Compute stale items by comparing each in-scope source file's symbols to its triefact.

    No DB access — the source is the source of truth, and the triefact's sentinels carry
    the fingerprints used to detect drift. Designed to be fast: a few thousand files run
    in well under a second on a modern machine.
    """
    project_root = project_root.resolve()
    src_root = (project_root / config.triefacts.source_root).resolve()
    discovered = discover_files(project_root, config.scope)

    items: list[StaleItem] = []

    for abs_source in discovered:
        if not abs_source.is_relative_to(src_root):
            continue
        rel_source = str(abs_source.relative_to(src_root))

        symbols = extract_symbols(abs_source, source_root=src_root)
        public = [s for s in symbols if s.is_public]
        rel_triefact = _triefact_path_for(rel_source, config)
        abs_triefact = project_root / rel_triefact
        triefact_exists = abs_triefact.exists()

        if not public and not triefact_exists:
            # Nothing to document, nothing to check.
            continue

        if public and not triefact_exists:
            items.append(
                StaleItem(
                    source_path=rel_source,
                    triefact_path=rel_triefact,
                    reason=StaleReason.MISSING_TRIEFACT,
                    qualified_name=None,
                )
            )
            continue

        # triefact_exists is True at this point — check section-level staleness regardless
        # of whether `public` is empty. An empty public set means every existing section is
        # orphaned (the symbol it documents was renamed, made private, or removed).
        triefact = TriefactFile.parse(abs_triefact.read_text())
        existing_sections = {c.qualified_name: c for c in triefact.chunks if isinstance(c, Section)}
        symbol_index = {sym.qualified_name: sym for sym in public}

        for qname, sym in symbol_index.items():
            sec = existing_sections.get(qname)
            if sec is None:
                items.append(
                    StaleItem(
                        source_path=rel_source,
                        triefact_path=rel_triefact,
                        reason=StaleReason.MISSING_SECTION,
                        qualified_name=qname,
                    )
                )
                continue
            if sec.fingerprint != sym.body_normalized_hash:
                items.append(
                    StaleItem(
                        source_path=rel_source,
                        triefact_path=rel_triefact,
                        reason=StaleReason.STALE_SECTION,
                        qualified_name=qname,
                    )
                )

        for qname in existing_sections:
            if qname not in symbol_index:
                items.append(
                    StaleItem(
                        source_path=rel_source,
                        triefact_path=rel_triefact,
                        reason=StaleReason.ORPHAN_SECTION,
                        qualified_name=qname,
                    )
                )

    return CheckResult(items=items)
