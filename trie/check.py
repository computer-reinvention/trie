from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from pathlib import Path

from trie.config import Config
from trie.parse.python import extract_symbols
from trie.scope import discover_files
from trie.sync.writer import DocFile, Section


class StaleReason(StrEnum):
    MISSING_DOC = "missing_doc"  # source has public symbols but no doc file
    MISSING_SECTION = "missing_section"  # public symbol present, no section for it
    STALE_SECTION = "stale_section"  # section fingerprint != current source hash
    ORPHAN_SECTION = "orphan_section"  # section exists but symbol is gone


@dataclass(frozen=True)
class StaleItem:
    source_path: str  # source-root-relative
    doc_path: str  # source-root-relative
    reason: StaleReason
    qualified_name: str | None  # set for symbol-level reasons; None for missing_doc


@dataclass(frozen=True)
class CheckResult:
    items: list[StaleItem] = field(default_factory=list)

    @property
    def is_clean(self) -> bool:
        return not self.items


def _doc_path_for(rel_source: str, config: Config) -> str:
    """Mirror src/foo.py -> {docs.root}/src/foo.md as a source-root-relative path."""
    p = Path(rel_source)
    return str(Path(config.docs.root) / p.with_suffix(".md"))


def check_project(*, project_root: Path, config: Config) -> CheckResult:
    """Compute stale items by comparing each in-scope source file's symbols to its doc file.

    No DB access — the source is the source of truth, and the doc file's sentinels carry
    the fingerprints used to detect drift. Designed to be fast: a few thousand files run
    in well under a second on a modern machine.
    """
    project_root = project_root.resolve()
    src_root = (project_root / config.docs.source_root).resolve()
    discovered = discover_files(project_root, config.scope)

    items: list[StaleItem] = []

    for abs_source in discovered:
        if not abs_source.is_relative_to(src_root):
            continue
        rel_source = str(abs_source.relative_to(src_root))

        symbols = extract_symbols(abs_source, source_root=src_root)
        public = [s for s in symbols if s.is_public]
        rel_doc = _doc_path_for(rel_source, config)
        abs_doc = project_root / rel_doc
        doc_exists = abs_doc.exists()

        if not public and not doc_exists:
            # Nothing to document, nothing to check.
            continue

        if public and not doc_exists:
            items.append(
                StaleItem(
                    source_path=rel_source,
                    doc_path=rel_doc,
                    reason=StaleReason.MISSING_DOC,
                    qualified_name=None,
                )
            )
            continue

        # doc_exists is True at this point — check section-level staleness regardless of
        # whether `public` is empty. An empty public set means every existing section is
        # orphaned (the symbol it documents was renamed, made private, or removed).
        doc = DocFile.parse(abs_doc.read_text())
        existing_sections = {c.qualified_name: c for c in doc.chunks if isinstance(c, Section)}
        symbol_index = {sym.qualified_name: sym for sym in public}

        for qname, sym in symbol_index.items():
            sec = existing_sections.get(qname)
            if sec is None:
                items.append(
                    StaleItem(
                        source_path=rel_source,
                        doc_path=rel_doc,
                        reason=StaleReason.MISSING_SECTION,
                        qualified_name=qname,
                    )
                )
                continue
            if sec.fingerprint != sym.body_normalized_hash:
                items.append(
                    StaleItem(
                        source_path=rel_source,
                        doc_path=rel_doc,
                        reason=StaleReason.STALE_SECTION,
                        qualified_name=qname,
                    )
                )

        for qname in existing_sections:
            if qname not in symbol_index:
                items.append(
                    StaleItem(
                        source_path=rel_source,
                        doc_path=rel_doc,
                        reason=StaleReason.ORPHAN_SECTION,
                        qualified_name=qname,
                    )
                )

    return CheckResult(items=items)
