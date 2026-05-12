from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from trie.check import check_project
from trie.config import Config
from trie.cost import ModelPricing, estimate_actual_cost
from trie.graph.store import Store
from trie.models import ModelClient
from trie.scan import scan_project
from trie.sync.cascade import compute_cascade
from trie.sync.progress import NULL_PROGRESS, ProgressCallback
from trie.sync.reconcile import find_orphan_triefacts
from trie.sync.single_file import FileSyncResult, sync_single_file


@dataclass(frozen=True)
class IncrementalWorklist:
    """Read-only preview of what `run_incremental` would touch.

    Produced by `compute_incremental_worklist`. Used by `trie plan` to show
    "what would sync actually do?" on established projects, and reused inside
    `run_incremental` so the prep pipeline (scan + check + cascade) lives in
    one place instead of two.
    """

    affected_files: list[str]
    directly_stale: list[str]
    cascaded_files: list[str]
    orphan_triefacts: list[Path]


@dataclass(frozen=True)
class IncrementalResult:
    files_synced: int
    files_skipped_no_budget: int
    files_skipped_no_symbols: int
    directly_stale_count: int
    cascaded_count: int
    actual_cost_usd: float
    orphan_triefacts_removed: list[Path] = field(default_factory=list)
    sync_results: list[FileSyncResult] = field(default_factory=list)


def compute_incremental_worklist(
    *, project_root: Path, config: Config, store: Store
) -> IncrementalWorklist:
    """Run scan + check + cascade and return the file list `run_incremental` would touch.

    Read-only: scans (which is idempotent and hash-driven), but does NOT delete orphan
    triefacts or invoke the LLM. The orphan list is returned so callers can either
    delete (sync) or just report (plan).

    Filters out staleness items whose source file no longer exists — those triefacts
    are orphans and would be removed by sync, not regenerated.
    """
    project_root = project_root.resolve()
    src_root = (project_root / config.triefacts.source_root).resolve()

    scan_project(project_root=project_root, config=config, store=store)
    orphans = find_orphan_triefacts(project_root=project_root, config=config)

    check = check_project(project_root=project_root, config=config)
    directly_stale = sorted(
        {
            it.source_path
            for it in check.items
            if it.source_path and (src_root / it.source_path).is_file()
        }
    )

    if not directly_stale:
        return IncrementalWorklist(
            affected_files=[],
            directly_stale=[],
            cascaded_files=[],
            orphan_triefacts=orphans,
        )

    cascade = compute_cascade(
        changed_files=directly_stale,
        store=store,
        depth=config.cascade.default_depth,
        hub_threshold=config.cascade.hub_symbol_threshold,
    )
    return IncrementalWorklist(
        affected_files=cascade.affected_files,
        directly_stale=directly_stale,
        cascaded_files=sorted(cascade.cascaded_from_change),
        orphan_triefacts=orphans,
    )


def run_incremental(
    *,
    project_root: Path,
    config: Config,
    store: Store,
    client: ModelClient,
    pricing: ModelPricing | None = None,
    budget_usd: float | None = None,
    limit: int | None = None,
    progress: ProgressCallback | None = None,
) -> IncrementalResult:
    """Refresh triefacts that drifted from source, plus the cascade of files referencing them.

    The flow:
      1. Scan to refresh the symbol graph and edges.
      2. Run `check_project` to find files whose triefacts are stale relative to source.
      3. Compute the cascade: every file whose symbols (transitively) reference a stale
         symbol, capped by the configured depth and hub threshold.
      4. Sync each affected file with `sync_single_file`, honoring --budget / --limit.

    A file with no public symbols is skipped silently (nothing for the generator to do).
    """
    project_root = project_root.resolve()
    src_root = (project_root / config.triefacts.source_root).resolve()

    # `compute_incremental_worklist` does the scan + check + cascade prep but does NOT
    # delete orphans (it's the read-only variant used by `trie plan`). Sync follows up
    # with the destructive removal here so the worklist + the actual run agree on what
    # files are in play.
    worklist = compute_incremental_worklist(project_root=project_root, config=config, store=store)
    orphan_triefacts = list(worklist.orphan_triefacts)
    for orphan in orphan_triefacts:
        orphan.unlink()

    if not worklist.affected_files:
        return IncrementalResult(
            files_synced=0,
            files_skipped_no_budget=0,
            files_skipped_no_symbols=0,
            directly_stale_count=0,
            cascaded_count=0,
            actual_cost_usd=0.0,
            orphan_triefacts_removed=orphan_triefacts,
            sync_results=[],
        )

    cb: ProgressCallback = progress if progress is not None else NULL_PROGRESS
    sync_results: list[FileSyncResult] = []
    actual_cost = 0.0
    skipped_budget = 0
    skipped_no_symbols = 0
    total = len(worklist.affected_files)

    for idx, rel in enumerate(worklist.affected_files, start=1):
        if limit is not None and len(sync_results) >= limit:
            skipped_budget += 1
            cb.on_skip(rel, "limit reached")
            continue
        if budget_usd is not None and actual_cost >= budget_usd:
            skipped_budget += 1
            cb.on_skip(rel, "budget reached")
            continue

        abs_path = src_root / rel
        if not abs_path.is_file():
            # Source removed since the cascade was computed; reconcile_deletions handles it.
            continue

        cb.on_start(rel, idx, total)
        result = sync_single_file(
            abs_path, project_root=project_root, config=config, client=client, store=store
        )
        if result.symbols_generated == 0 and result.sections_removed == 0:
            skipped_no_symbols += 1
            cb.on_skip(rel, "no public symbols")
            continue
        sync_results.append(result)
        file_cost = 0.0
        if pricing is not None:
            file_cost = estimate_actual_cost(
                cache_creation_input_tokens=result.cache_creation_input_tokens,
                cache_read_input_tokens=result.cache_read_input_tokens,
                input_tokens=result.input_tokens,
                output_tokens=result.output_tokens,
                pricing=pricing,
            )
            actual_cost += file_cost
        cb.on_done(rel, result, actual_cost)

    return IncrementalResult(
        files_synced=len(sync_results),
        files_skipped_no_budget=skipped_budget,
        files_skipped_no_symbols=skipped_no_symbols,
        directly_stale_count=len(worklist.directly_stale),
        cascaded_count=len(worklist.cascaded_files),
        actual_cost_usd=actual_cost,
        orphan_triefacts_removed=orphan_triefacts,
        sync_results=sync_results,
    )
