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
from trie.models import GenerationRequest, ModelClient
from trie.sync.generator import SYSTEM_PROMPT, FileGenerationContext, build_cached_context
from trie.sync.progress import NULL_PROGRESS, ProgressCallback
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
    client: ModelClient,
    only_files: Iterable[str] | None = None,
) -> BootstrapPlan:
    """Rank files by `LOC * public_symbol_count` and produce per-file cost estimates.

    Files with no public symbols are excluded — there's nothing for the generator to do.
    Files that disappeared between scan and now are skipped silently. The cached-prefix
    token count for each file comes from the Anthropic `count_tokens` API (free, but
    subject to its own RPM limit), giving accurate cost estimates instead of a heuristic.

    When `only_files` is provided, the plan is restricted to those source-relative paths
    — used by `trie plan` on established projects so the cost estimate matches the
    incremental worklist that `trie sync` would actually execute, not a hypothetical
    full re-bootstrap.
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
        if pricing is not None:
            ctx = FileGenerationContext(file_path=stats.path, source_text=text)
            count_req = GenerationRequest(
                system_prompt=SYSTEM_PROMPT,
                cached_context=build_cached_context(ctx),
                request="",
            )
            cached_prefix_tokens = client.count_tokens(count_req)
            est = estimate_file_cost(
                file_path=stats.path,
                cached_prefix_tokens=cached_prefix_tokens,
                public_symbols=stats.public_symbols,
                pricing=pricing,
            )
        else:
            est = FileEstimate(
                file_path=stats.path,
                public_symbols=stats.public_symbols,
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
    client: ModelClient,
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
    sync_results: list[FileSyncResult] = []
    actual_cost = 0.0
    estimated_cost = 0.0
    skipped = 0
    total = len(plan.items)

    for idx, item in enumerate(plan.items, start=1):
        if limit is not None and len(sync_results) >= limit:
            skipped += 1
            cb.on_skip(item.file_path, "limit reached")
            continue
        if budget_usd is not None and actual_cost >= budget_usd:
            skipped += 1
            cb.on_skip(item.file_path, "budget reached")
            continue

        abs_path = project_root / item.file_path
        if not abs_path.is_file():
            skipped += 1
            cb.on_skip(item.file_path, "source missing")
            continue

        cb.on_start(item.file_path, idx, total)
        result = sync_single_file(
            abs_path,
            project_root=project_root,
            config=config,
            client=client,
            store=store,
        )
        sync_results.append(result)
        estimated_cost += item.estimated.cost_usd
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
        cb.on_done(item.file_path, result, actual_cost)

    return BootstrapResult(
        files_synced=len(sync_results),
        files_skipped_no_budget=skipped,
        actual_cost_usd=actual_cost,
        estimated_cost_usd=estimated_cost,
        sync_results=sync_results,
    )
