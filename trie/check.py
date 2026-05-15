from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from pathlib import Path

from trie import telemetry
from trie.config import Config
from trie.parse.python import extract_symbols
from trie.scope import discover_files
from trie.sync.writer import Section, TriefactFile, hash_body


class StaleReason(StrEnum):
    MISSING_TRIEFACT = "missing_triefact"  # source has public symbols but no triefact file
    MISSING_SECTION = "missing_section"  # public symbol present, no section for it
    STALE_SECTION = "stale_section"  # section fingerprint != current source hash (Code → Triefact)
    ORPHAN_SECTION = "orphan_section"  # section exists but symbol is gone (Triefact → Code)
    TAMPERED_BODY = "tampered_body"  # section body hash != recorded body_fp (Triefact → Code)
    LEGACY_SECTION = "legacy_section"  # section was written by trie ≤ 0.1, has no body_fp


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

    Bidirectional: covers both directions of drift.
      - Code → Triefact: source symbol changed but the section wasn't regenerated
        (`STALE_SECTION`); a public symbol exists with no matching section
        (`MISSING_SECTION`); whole triefact file missing (`MISSING_TRIEFACT`).
      - Triefact → Code: section exists for a symbol that's gone (`ORPHAN_SECTION`);
        section body was hand-edited or corrupted between sentinels (`TAMPERED_BODY`);
        section was written by trie ≤ 0.1 with no body fingerprint to verify
        (`LEGACY_SECTION` — re-sync to gain integrity verification).

    No DB access — the source is the source of truth, and the triefact's sentinels carry
    the fingerprints used to detect drift. Designed to be fast: a few thousand files run
    in well under a second on a modern machine.
    """
    with telemetry.timed("verify", project_root=str(project_root)) as tele:
        return _check_project_inner(project_root=project_root, config=config, _tele=tele)


def _check_project_inner(*, project_root: Path, config: Config, _tele: dict) -> CheckResult:
    project_root = project_root.resolve()
    src_root = (project_root / config.triefacts.source_root).resolve()
    discovered = discover_files(project_root, config.scope)

    items: list[StaleItem] = []
    files_checked = 0

    for abs_source in discovered:
        if not abs_source.is_relative_to(src_root):
            continue
        files_checked += 1
        rel_source = str(abs_source.relative_to(src_root))

        # Every parser-surfaced symbol is in scope for verification. The `is_public`
        # flag is descriptive metadata on Symbol but is NOT a filter — stale prose
        # is stale regardless of whether the author named the symbol with a leading
        # underscore, and sync documents the same set.
        symbols = extract_symbols(abs_source, source_root=src_root)
        rel_triefact = _triefact_path_for(rel_source, config)
        abs_triefact = project_root / rel_triefact
        triefact_exists = abs_triefact.exists()

        if not symbols and not triefact_exists:
            # Nothing to document, nothing to check.
            continue

        if symbols and not triefact_exists:
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
        # of whether `symbols` is empty. An empty symbol set means every existing section
        # is orphaned (the symbol it documents was renamed or removed).
        triefact = TriefactFile.parse(abs_triefact.read_text())
        existing_sections = {c.qualified_name: c for c in triefact.chunks if isinstance(c, Section)}
        symbol_index = {sym.qualified_name: sym for sym in symbols}

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
                continue
            # Source matches; now verify the triefact body wasn't tampered with.
            if sec.body_fingerprint is None:
                items.append(
                    StaleItem(
                        source_path=rel_source,
                        triefact_path=rel_triefact,
                        reason=StaleReason.LEGACY_SECTION,
                        qualified_name=qname,
                    )
                )
            elif hash_body(sec.body) != sec.body_fingerprint:
                items.append(
                    StaleItem(
                        source_path=rel_source,
                        triefact_path=rel_triefact,
                        reason=StaleReason.TAMPERED_BODY,
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

    # Telemetry: count by reason for the validation harness's "drift incidents" metric.
    by_reason: dict[str, int] = {}
    for it in items:
        by_reason[it.reason.value] = by_reason.get(it.reason.value, 0) + 1
    _tele["files_checked"] = files_checked
    _tele["issues_found"] = len(items)
    _tele["issues_by_reason"] = by_reason

    return CheckResult(items=items)
