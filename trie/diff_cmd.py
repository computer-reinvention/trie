from __future__ import annotations

import difflib
from dataclasses import dataclass, field
from pathlib import Path

from trie.check import check_project
from trie.config import Config
from trie.cost import ModelPricing, estimate_actual_cost
from trie.graph.store import Store
from trie.models import ModelClient
from trie.sync.progress import NULL_PROGRESS, ProgressCallback
from trie.sync.single_file import FileSyncResult, sync_single_file


@dataclass(frozen=True)
class FileDiff:
    source_path: str
    canonical_triefact_path: Path
    preview_triefact_path: Path
    unified_diff: str
    sync_result: FileSyncResult


@dataclass(frozen=True)
class DiffResult:
    diffs: list[FileDiff] = field(default_factory=list)
    files_skipped_no_budget: int = 0
    actual_cost_usd: float = 0.0


def diff_project(
    *,
    project_root: Path,
    config: Config,
    client: ModelClient,
    pricing: ModelPricing | None = None,
    budget_usd: float | None = None,
    limit: int | None = None,
    progress: ProgressCallback | None = None,
    store: Store | None = None,
) -> DiffResult:
    """Regenerate stale triefacts into `.trie/preview/` and produce unified diffs.

    The set of stale files is computed via `check_project`. Files with only orphan-section
    issues are still regenerated (the writer drops the orphan section). Files that don't
    have any stale items are skipped — `trie diff` is not a "show me everything" command.
    """
    project_root = project_root.resolve()
    src_root = (project_root / config.triefacts.source_root).resolve()
    triefacts_root = project_root / config.triefacts.root
    preview_root = project_root / ".trie" / "preview"

    check = check_project(project_root=project_root, config=config)
    stale_sources = sorted({it.source_path for it in check.items if it.source_path})

    cb: ProgressCallback = progress if progress is not None else NULL_PROGRESS
    diffs: list[FileDiff] = []
    skipped = 0
    actual_cost = 0.0
    total = len(stale_sources)

    for idx, rel_source in enumerate(stale_sources, start=1):
        if limit is not None and len(diffs) >= limit:
            skipped += 1
            cb.on_skip(rel_source, "limit reached")
            continue
        if budget_usd is not None and actual_cost >= budget_usd:
            skipped += 1
            cb.on_skip(rel_source, "budget reached")
            continue

        abs_source = src_root / rel_source
        if not abs_source.is_file():
            # Source was deleted entirely; trie sync's reconcile will handle this.
            # Diff has nothing useful to show for orphaned-source cases in v0.1.
            skipped += 1
            cb.on_skip(rel_source, "source missing")
            continue

        canonical = (triefacts_root / Path(rel_source).with_suffix(".md")).resolve()
        preview = (preview_root / Path(rel_source).with_suffix(".md")).resolve()

        cb.on_start(rel_source, idx, total)
        result = sync_single_file(
            abs_source,
            project_root=project_root,
            config=config,
            client=client,
            dest_triefact_path=preview,
            store=store,
        )

        original = canonical.read_text() if canonical.exists() else ""
        new = preview.read_text() if preview.exists() else ""
        unified = "".join(
            difflib.unified_diff(
                original.splitlines(keepends=True),
                new.splitlines(keepends=True),
                fromfile=str(canonical.relative_to(project_root))
                if canonical.is_relative_to(project_root)
                else str(canonical),
                tofile=str(preview.relative_to(project_root))
                if preview.is_relative_to(project_root)
                else str(preview),
            )
        )

        diffs.append(
            FileDiff(
                source_path=rel_source,
                canonical_triefact_path=canonical,
                preview_triefact_path=preview,
                unified_diff=unified,
                sync_result=result,
            )
        )
        if pricing is not None:
            actual_cost += estimate_actual_cost(
                cache_creation_input_tokens=result.cache_creation_input_tokens,
                cache_read_input_tokens=result.cache_read_input_tokens,
                input_tokens=result.input_tokens,
                output_tokens=result.output_tokens,
                pricing=pricing,
            )
        cb.on_done(rel_source, result, actual_cost)

    return DiffResult(diffs=diffs, files_skipped_no_budget=skipped, actual_cost_usd=actual_cost)
