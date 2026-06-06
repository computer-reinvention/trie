from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from trie.check import check_project
from trie.config import Config
from trie.cost import ModelPricing, estimate_actual_cost
from trie.graph.store import Store
from trie.models import TrieClient, configure_inflight_limit
from trie.scan import scan_project
from trie.sync.cascade import compute_cascade
from trie.sync.progress import NULL_PROGRESS, ProgressCallback
from trie.sync.reconcile import find_orphan_triefacts
from trie.sync.scheduler import FileTask, run_waves
from trie.sync.single_file import FileSyncResult, backfill_section_records, sync_single_file


@dataclass(frozen=True)
class IncrementalWorklist:
    """Read-only preview of what `run_incremental` would touch.

    Produced by `compute_incremental_worklist`. Used by `trie plan` to show
    "what would sync actually do?" on established projects, and reused inside
    `run_incremental` so the prep pipeline (scan + check + cascade) lives in
    one place instead of two.

    `hop_by_file` is the cascade's hop distance map (file → minimum hops from
    any seed file). Stale files map to 0. Used to rank cascade-pulled files
    closest-to-the-change first.

    `regen_qnames_by_file` is the per-symbol regen target for each affected file.
    For each file in `affected_files`, the value is the set of qualified names that
    sync should hand to the LLM; every other symbol in the file is a pass-through
    (its existing section stays byte-identical). This is the load-bearing data for
    symbol-level sync: with file-level sync, every public symbol in a touched file
    was regenerated regardless of whether it changed; with this map, the LLM only
    sees symbols that actually need new prose.

    A special sentinel applies for the cold-write case: if a file has no triefact
    at all (`MISSING_TRIEFACT` from check), `regen_qnames_by_file` does not list it
    explicitly. The sync driver detects the missing triefact and passes
    `symbols_to_regen=None` to `sync_single_file`, which regenerates everything.
    Files mapped here always have *at least one* qname — empty sets are filtered
    out by `compute_incremental_worklist`."""

    affected_files: list[str]
    directly_stale: list[str]
    cascaded_files: list[str]
    orphan_triefacts: list[Path]
    hop_by_file: dict[str, int] = field(default_factory=dict)
    regen_qnames_by_file: dict[str, set[str]] = field(default_factory=dict)


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
    # Stale items that survive the file-existence filter, indexed both ways. The set of
    # files comes from the source_paths; the per-file qname set comes from items that
    # carry a qualified_name (everything except `MISSING_TRIEFACT`, which signals a
    # whole-file cold-write).
    stale_items_alive = [
        it for it in check.items if it.source_path and (src_root / it.source_path).is_file()
    ]
    directly_stale = sorted({it.source_path for it in stale_items_alive})

    # Per-file regen target: union of stale qnames (from check) and cascade-pulled qnames
    # (from the cascade walk). Files marked MISSING_TRIEFACT are NOT entered into this
    # map; their absence signals to the runner "regen everything in this file" via the
    # `symbols_to_regen=None` path in sync_single_file.
    regen_qnames_by_file: dict[str, set[str]] = {}
    files_needing_full_regen: set[str] = set()
    for it in stale_items_alive:
        if it.qualified_name is None:
            # MISSING_TRIEFACT — record so we skip the per-symbol path for this file.
            files_needing_full_regen.add(it.source_path)
            continue
        regen_qnames_by_file.setdefault(it.source_path, set()).add(it.qualified_name)

    if not directly_stale:
        return IncrementalWorklist(
            affected_files=[],
            directly_stale=[],
            cascaded_files=[],
            orphan_triefacts=orphans,
            hop_by_file={},
            regen_qnames_by_file={},
        )

    cascade = compute_cascade(
        changed_files=directly_stale,
        store=store,
        depth=config.cascade.default_depth,
        hub_threshold=config.cascade.hub_symbol_threshold,
    )

    # Project cascade-pulled qnames onto their owning files. Cascade-pulled symbols may
    # land in a file that's already directly-stale (callers in the same file as the
    # change); the set semantics handle that idempotently.
    for cqn, cfile in cascade.file_by_cascaded_qname.items():
        regen_qnames_by_file.setdefault(cfile, set()).add(cqn)

    # Files flagged for full-file regen drop out of the per-symbol map — the runner
    # will see them missing and pass `symbols_to_regen=None`, regenerating every symbol.
    for f in files_needing_full_regen:
        regen_qnames_by_file.pop(f, None)

    return IncrementalWorklist(
        affected_files=cascade.affected_files,
        directly_stale=directly_stale,
        cascaded_files=sorted(cascade.cascaded_from_change),
        orphan_triefacts=orphans,
        hop_by_file=cascade.hop_by_file,
        regen_qnames_by_file=regen_qnames_by_file,
    )


def run_incremental(
    *,
    project_root: Path,
    config: Config,
    store: Store,
    client: TrieClient,
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
        if store.count_section_records() < store.count_symbols():
            backfill_section_records(project_root, config, store)
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

    # Build depth-banded tasks: directly-stale files are hop 0, cascade-pulled
    # files carry their cascade hop. The scheduler runs band 0 fully before band 1
    # so diff-aware regen of a caller can reference its already-refreshed callee
    # prose. `affected_files` (the sorted union) is unchanged so `trie plan`'s
    # preview stays stable.
    stale_set = set(worklist.directly_stale)
    tasks: list[FileTask] = []
    for rel in worklist.directly_stale:
        if (src_root / rel).is_file():
            tasks.append(
                FileTask(rel_path=rel, hop=0, regen_qnames=worklist.regen_qnames_by_file.get(rel))
            )
    for rel in worklist.affected_files:
        if rel in stale_set:
            continue
        if not (src_root / rel).is_file():
            continue
        tasks.append(
            FileTask(
                rel_path=rel,
                hop=max(1, worklist.hop_by_file.get(rel, 1)),
                regen_qnames=worklist.regen_qnames_by_file.get(rel),
            )
        )

    # Cap total concurrent LLM requests for this run; the scheduler over-subscribes
    # workers and this is the real throttle.
    configure_inflight_limit(config.sync.max_inflight_requests)

    def _process(task: FileTask) -> FileSyncResult | None:
        result = sync_single_file(
            src_root / task.rel_path,
            project_root=project_root,
            config=config,
            client=client,
            store=store,
            symbols_to_regen=task.regen_qnames,
        )
        # A file with no symbols at all is a skip (None). Symbol-level pass-through
        # still counts as synced (front matter updated), distinguished by skipped>0.
        if (
            result.symbols_generated == 0
            and result.sections_removed == 0
            and result.symbols_skipped == 0
        ):
            return None
        return result

    def _cost(result: FileSyncResult) -> float:
        if pricing is None:
            return 0.0
        return estimate_actual_cost(
            cache_creation_input_tokens=result.cache_creation_input_tokens,
            cache_read_input_tokens=result.cache_read_input_tokens,
            input_tokens=result.input_tokens,
            output_tokens=result.output_tokens,
            pricing=pricing,
        )

    sched = run_waves(
        tasks,
        process_file=_process,
        file_workers=config.sync.file_workers,
        progress=cb,
        budget_usd=budget_usd,
        limit=limit,
        cost_of=_cost,
    )
    sync_results = sched.results
    skipped_budget = sched.skipped_budget
    skipped_no_symbols = sched.skipped_other
    actual_cost = sum(_cost(r) for r in sync_results)

    # Backfill any missing triefact_sections records. This ensures the
    # one-liner cache is populated even when sources were synced by an
    # older version that didn't store section metadata.
    if store.count_section_records() < store.count_symbols():
        backfill_section_records(project_root, config, store)

    # Auto-backfill role tags for any symbol still missing one. We're already in
    # the LLM-spending path, so filling the gaps now keeps the graph's role axis
    # complete without the user ever invoking `trie sync --roles-only`. The call
    # short-circuits for free when every symbol is already tagged (the steady
    # state — full syncs write roles inline). Imported lazily to avoid a module
    # import cycle (roles → single_file → … ).
    from trie.sync.roles import run_roles_only

    run_roles_only(
        project_root=project_root,
        config=config,
        store=store,
        client=client,
        progress=progress,
        only_missing=True,
    )

    # Clear the files we just regenerated from the pending (stale) set so
    # `trie status` and the editor reflect that the working tree is now coherent.
    from trie.activity import clear_pending
    from trie.git_helpers import current_head

    synced_rel = [str(r.source_path.relative_to(src_root)) for r in sync_results]
    if synced_rel:
        clear_pending(project_root, synced=synced_rel, head=current_head(project_root) or "")

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
