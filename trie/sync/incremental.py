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
from trie.sync.reconcile import remove_orphan_triefacts
from trie.sync.single_file import FileSyncResult, sync_single_file


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

    scan_project(project_root=project_root, config=config, store=store)

    # Reconcile deletions before staleness check, so orphan triefact files don't show up
    # as stale (their sources are gone — they should just be removed).
    orphan_triefacts = remove_orphan_triefacts(project_root=project_root, config=config)

    check = check_project(project_root=project_root, config=config)
    directly_stale = sorted({it.source_path for it in check.items if it.source_path})

    if not directly_stale:
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

    cascade = compute_cascade(
        changed_files=directly_stale,
        store=store,
        depth=config.cascade.default_depth,
        hub_threshold=config.cascade.hub_symbol_threshold,
    )

    cb: ProgressCallback = progress if progress is not None else NULL_PROGRESS
    sync_results: list[FileSyncResult] = []
    actual_cost = 0.0
    skipped_budget = 0
    skipped_no_symbols = 0
    total = len(cascade.affected_files)

    for idx, rel in enumerate(cascade.affected_files, start=1):
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
        result = sync_single_file(abs_path, project_root=project_root, config=config, client=client)
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
        directly_stale_count=len(directly_stale),
        cascaded_count=len(cascade.cascaded_from_change),
        actual_cost_usd=actual_cost,
        orphan_triefacts_removed=orphan_triefacts,
        sync_results=sync_results,
    )
