from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

from trie.config import Config
from trie.cost import (
    FileEstimate,
    ModelPricing,
    estimate_actual_cost,
    estimate_file_cost,
    get_pricing,
)
from trie.graph.store import Store
from trie.models import TrieClient, configure_inflight_limit
from trie.sync.generator import SYSTEM_PROMPT, FileGenerationContext, build_cached_context
from trie.sync.progress import NULL_PROGRESS, ProgressCallback
from trie.sync.scheduler import FileTask, run_waves
from trie.sync.single_file import FileSyncResult, sync_single_file


@dataclass(frozen=True)
class PlanItem:
    file_path: str  # source-root-relative
    public_symbols: int
    score: float
    estimated: FileEstimate


@dataclass(frozen=True)
class BootstrapPlan:
    items: list[PlanItem]
    pricing_known: bool
    total_estimated_cost: float


@dataclass(frozen=True)
class BootstrapResult:
    files_synced: int
    files_skipped_no_budget: int
    actual_cost_usd: float
    estimated_cost_usd: float
    sync_results: list[FileSyncResult]


def build_plan(
    *,
    project_root: Path,
    store: Store,
    model_id: str,
    client: TrieClient,
    only_files: Iterable[str] | None = None,
    regen_count_by_file: dict[str, int] | None = None,
) -> BootstrapPlan:
    """Rank files by `LOC * documented_symbol_count` and produce per-file cost estimates.

    Files with no documented symbols are excluded — there's nothing for the generator to do.
    Files that disappeared between scan and now are skipped silently. The cached-prefix
    token count for each file comes from the Anthropic `count_tokens` API (free, but
    subject to its own RPM limit), giving accurate cost estimates instead of a heuristic.

    When `only_files` is provided, the plan is restricted to those source-relative paths
    — used by `trie plan` on established projects so the cost estimate matches the
    incremental worklist that `trie sync` would actually execute, not a hypothetical
    full re-bootstrap.

    When `regen_count_by_file` is provided, the per-file cost estimate is scaled to the
    actual number of symbols that will hit the LLM (rather than every documented symbol
    in the file). Absence of a file from the map signals "regen everything" — the
    cold-write / `--file` path. This is the input that lets `trie plan` show the
    symbol-level reality instead of the file-level upper bound.

    `public_symbols` on the returned `PlanItem` always reflects the file's total
    documented symbol count, so the UI can show "N/M symbols" — the regen target
    against the file's full surface.
    """
    pricing = get_pricing(model_id)
    only_set = set(only_files) if only_files is not None else None
    items: list[PlanItem] = []
    for stats in store.file_stats():
        if only_set is not None and stats.path not in only_set:
            continue
        if stats.public_symbols == 0:
            continue
        abs_path = project_root / stats.path
        if not abs_path.is_file():
            continue
        text = abs_path.read_text()
        loc = max(1, text.count("\n"))
        score = float(loc * stats.public_symbols)
        # Default to "regen all" (full file) unless the caller specified a smaller
        # target. The map's absence-as-full-regen contract matches what the runner
        # does with `symbols_to_regen`.
        regen_symbols = (
            regen_count_by_file.get(stats.path, stats.public_symbols)
            if regen_count_by_file is not None
            else stats.public_symbols
        )
        if pricing is not None:
            ctx = FileGenerationContext(file_path=stats.path, source_text=text)
            cached_context = build_cached_context(ctx)
            cached_prefix_tokens = client.count_tokens(
                system_prompt=SYSTEM_PROMPT + ("\n\n" + cached_context if cached_context else ""),
                user_prompt="",
            )
            est = estimate_file_cost(
                file_path=stats.path,
                cached_prefix_tokens=cached_prefix_tokens,
                public_symbols=regen_symbols,
                pricing=pricing,
            )
        else:
            est = FileEstimate(
                file_path=stats.path,
                public_symbols=regen_symbols,
                cache_create_tokens=0,
                cache_read_tokens=0,
                request_tokens=0,
                output_tokens=0,
                cost_usd=0.0,
            )
        items.append(
            PlanItem(
                file_path=stats.path,
                public_symbols=stats.public_symbols,
                score=score,
                estimated=est,
            )
        )
    items.sort(key=lambda it: (-it.score, it.file_path))
    total = sum(it.estimated.cost_usd for it in items)
    return BootstrapPlan(items=items, pricing_known=pricing is not None, total_estimated_cost=total)


def run_bootstrap(
    *,
    plan: BootstrapPlan,
    project_root: Path,
    config: Config,
    client: TrieClient,
    pricing: ModelPricing | None,
    budget_usd: float | None,
    limit: int | None,
    progress: ProgressCallback | None = None,
    store: Store | None = None,
) -> BootstrapResult:
    """Execute the worklist. Stops when budget or limit is reached.

    Cost is checked *after* each file completes — the run may overshoot the budget by at
    most the cost of the final file. This trades a small overshoot risk for predictable
    "I asked for N files and got N files" semantics when --limit is set.
    """
    cb: ProgressCallback = progress if progress is not None else NULL_PROGRESS

    # Bootstrap is a full cold pass — no cascade dependencies between files, so
    # every file is hop 0 and the whole plan runs as one parallel wave. The
    # global request cap (the real throttle) is configured here.
    configure_inflight_limit(config.sync.max_inflight_requests)

    estimate_by_path = {item.file_path: item.estimated.cost_usd for item in plan.items}
    tasks = [
        FileTask(rel_path=item.file_path, hop=0)
        for item in plan.items
        if (project_root / item.file_path).is_file()
    ]
    missing = len(plan.items) - len(tasks)

    def _process(task: FileTask) -> FileSyncResult | None:
        return sync_single_file(
            project_root / task.rel_path,
            project_root=project_root,
            config=config,
            client=client,
            store=store,
        )

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
    actual_cost = sum(_cost(r) for r in sync_results)
    estimated_cost = sum(
        estimate_by_path.get(str(r.source_path.relative_to(project_root)), 0.0)
        for r in sync_results
    )

    return BootstrapResult(
        files_synced=len(sync_results),
        files_skipped_no_budget=sched.skipped_budget + missing,
        actual_cost_usd=actual_cost,
        estimated_cost_usd=estimated_cost,
        sync_results=sync_results,
    )
