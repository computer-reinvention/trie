"""Wave-based file scheduler for parallel triefact sync.

Both bootstrap and incremental sync used to walk files one at a time. Each file's
sync is dominated by LLM round-trips (seconds), so processing them serially left
the provider's rate budget mostly idle. This module parallelises across files.

Two levers, deliberately decoupled:

  - **file_workers** — how many files generate concurrently (a thread pool).
  - **max_inflight_requests** — a process-wide cap on TOTAL concurrent LLM calls,
    enforced by a global semaphore inside the model client (see
    `trie.models.configure_inflight_limit`). `file_workers x per-file concurrency`
    may exceed this; the semaphore is the real throttle and lets the 429 backoff
    absorb bursts. This is "go as fast as the provider allows."

**Depth-banded waves.** When the caller supplies a hop-distance per file
(`hop_by_file` from the cascade), files are grouped into bands by hop and bands
run sequentially: band 0 (directly-changed) fully completes before band 1
(its callers) starts, and so on. This preserves the diff-aware invariant that a
cascade section can reference the already-refreshed prose of its upstream
neighbours. Within a band there is no such dependency, so its files run fully in
parallel. Callers with no hop information get a single band (max parallelism).

**Thread safety.** Each worker runs `process_file` (closure provided by the
caller, typically wrapping `sync_single_file`). Generation is pure network I/O;
the `Store` is made thread-safe by an internal lock, so workers may touch it.
Disk writes are per-file and independent. Budget/limit accounting happens on the
scheduler thread as results arrive, so submission stops deterministically.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from dataclasses import dataclass

from trie import telemetry
from trie.sync.progress import NULL_PROGRESS, ProgressCallback
from trie.sync.single_file import FileSyncResult


@dataclass(frozen=True)
class FileTask:
    """One file to sync. `rel_path` is source-root-relative; `hop` is its cascade
    hop distance (0 = directly changed) and bands the waves. `regen_qnames` is the
    per-symbol regen target (None = full-file regen)."""

    rel_path: str
    hop: int = 0
    regen_qnames: set[str] | None = None


@dataclass
class SchedulerResult:
    results: list[FileSyncResult]
    skipped_budget: int
    skipped_other: int


def run_waves(
    tasks: list[FileTask],
    *,
    process_file: Callable[[FileTask], FileSyncResult | None],
    file_workers: int,
    progress: ProgressCallback | None = None,
    budget_usd: float | None = None,
    limit: int | None = None,
    cost_of: Callable[[FileSyncResult], float] | None = None,
) -> SchedulerResult:
    """Run `tasks` in depth-banded parallel waves.

    The main scheduler entry point that coordinates wave-based parallel file
    processing with budget and limit enforcement. When budget_usd or limit is
    active, concurrency is forced to 1 for deterministic cost/limit caps without
    concurrent overshoot. Files are grouped into hop-distance bands and executed
    band-by-band to preserve dependency ordering, with full parallelism within
    each band.

    `process_file(task)` performs the actual sync for one file and returns its
    `FileSyncResult` (or None to signal "nothing to do, skip"). It must be
    thread-safe with respect to shared state (the Store handles its own locking;
    the model client governs global request concurrency). It should NOT enforce
    budget/limit — the scheduler does that here, stopping submission once a cap is
    hit (in-flight files still finish).

    `cost_of(result)` returns the USD cost of a completed file, accumulated to
    enforce `budget_usd`. When omitted, budget is not enforced (limit still is).

    Progress callbacks fire as files start/finish; because files run in parallel,
    `on_start`/`on_done` interleave across the wave. `idx` passed to `on_start` is
    the global completion-independent submission index for display only.
    """
    cb: ProgressCallback = progress if progress is not None else NULL_PROGRESS
    total = len(tasks)
    # When a budget or limit is active the caller wants predictable capping more
    # than raw speed (these are smoke-test / cost-preview flows), and parallel
    # priming would overshoot the cap by up to `file_workers` files. Fall back to
    # serial in that case; unbounded runs (the common full-sync / refresh path)
    # get the full parallel wave.
    bounded = budget_usd is not None or limit is not None
    workers = 1 if bounded else max(1, file_workers)

    state = _RunState(
        cb=cb,
        process_file=process_file,
        workers=workers,
        total=total,
        budget_usd=budget_usd,
        limit=limit,
        cost_of=cost_of,
    )
    bands = _group_into_bands(tasks)

    with telemetry.timed("sync_waves", files=total, bands=len(bands), file_workers=workers) as tele:
        for band_index, band in enumerate(bands):
            if state.stop:
                state.skip_all(band)
                continue
            with telemetry.timed("sync_wave", band=band_index, files=len(band)):
                state.run_band(band)

        tele["files_synced"] = len(state.results)
        tele["actual_cost_usd"] = state.actual_cost

    return SchedulerResult(
        results=state.results,
        skipped_budget=state.skipped_budget,
        skipped_other=state.skipped_other,
    )


class _RunState:
    """Mutable accumulator for a `run_waves` invocation.

    Holds the cross-band running totals (results, costs, skip counts, the `stop`
    flag) and the per-call config. Keeping band execution on a method rather than
    an in-loop closure avoids late-binding of loop variables and keeps the
    submit/drain logic in one place.
    """

    def __init__(
        self,
        *,
        cb: ProgressCallback,
        process_file: Callable[[FileTask], FileSyncResult | None],
        workers: int,
        total: int,
        budget_usd: float | None,
        limit: int | None,
        cost_of: Callable[[FileSyncResult], float] | None,
    ) -> None:
        self.cb = cb
        self.process_file = process_file
        self.workers = workers
        self.total = total
        self.budget_usd = budget_usd
        self.limit = limit
        self.cost_of = cost_of
        self.results: list[FileSyncResult] = []
        self.skipped_budget = 0
        self.skipped_other = 0
        self.actual_cost = 0.0
        self.submitted = 0
        self.stop = False

    def _cap_reason(self) -> str:
        if self.limit is not None and len(self.results) >= self.limit:
            return "limit reached"
        return "budget reached"

    def skip_all(self, tasks: Iterable[FileTask]) -> None:
        reason = self._cap_reason()
        for task in tasks:
            self.skipped_budget += 1
            self.cb.on_skip(task.rel_path, reason)

    def run_band(self, band: list[FileTask]) -> None:
        it = iter(band)
        with ThreadPoolExecutor(max_workers=self.workers) as pool:
            pending: set = set()

            def submit_next() -> None:
                task = next(it, None)
                if task is None:
                    return
                self.submitted += 1
                self.cb.on_start(task.rel_path, self.submitted, self.total)
                fut = pool.submit(self.process_file, task)
                fut._trie_task = task  # type: ignore[attr-defined]
                pending.add(fut)

            # Prime the pool with up to `workers` files, then refill on completion
            # — keeps exactly `workers` files in flight without materialising all
            # the band's futures up front.
            for _ in range(self.workers):
                submit_next()

            while pending:
                done, pending = wait(pending, return_when=FIRST_COMPLETED)
                for fut in done:
                    self._collect(fut)
                    if not self.stop:
                        submit_next()

        # A cap that halted submission mid-band leaves an unconsumed remainder.
        if self.stop:
            self.skip_all(it)

    def _collect(self, fut) -> None:  # type: ignore[no-untyped-def]
        task: FileTask = fut._trie_task  # type: ignore[attr-defined]
        try:
            result = fut.result()
        except Exception as exc:  # one file failing must not sink the wave
            self.skipped_other += 1
            self.cb.on_skip(task.rel_path, f"error: {exc}")
            telemetry.emit("sync_file_error", path=task.rel_path, error=str(exc))
            return
        if result is None:
            self.skipped_other += 1
            self.cb.on_skip(task.rel_path, "no symbols to document")
            return
        self.results.append(result)
        if self.cost_of is not None:
            self.actual_cost += self.cost_of(result)
        self.cb.on_done(task.rel_path, result, self.actual_cost)
        if self.limit is not None and len(self.results) >= self.limit:
            self.stop = True
        if self.budget_usd is not None and self.actual_cost >= self.budget_usd:
            self.stop = True


def _group_into_bands(tasks: Iterable[FileTask]) -> list[list[FileTask]]:
    """Group tasks into hop-ordered bands. Each band runs fully before the next.

    Tasks with the same hop share a band (parallel); bands are ordered ascending
    by hop so directly-changed files (hop 0) complete before their callers. When
    every task is hop 0 (no cascade info), this is a single band.
    """
    by_hop: dict[int, list[FileTask]] = {}
    for t in tasks:
        by_hop.setdefault(t.hop, []).append(t)
    return [by_hop[h] for h in sorted(by_hop)]
