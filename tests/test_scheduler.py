"""Tests for the wave-based file scheduler (trie/sync/scheduler.py)."""

from __future__ import annotations

import threading
import time
from pathlib import Path

from trie.sync.scheduler import FileTask, run_waves
from trie.sync.single_file import FileSyncResult


def _result(rel: str) -> FileSyncResult:
    return FileSyncResult(
        source_path=Path(rel),
        triefact_path=Path(rel).with_suffix(".md"),
        symbols_generated=1,
        sections_removed=0,
        input_tokens=10,
        output_tokens=20,
        cache_creation_input_tokens=0,
        cache_read_input_tokens=0,
    )


def test_unbounded_run_processes_all_files():
    tasks = [FileTask(rel_path=f"f{i}.py") for i in range(10)]
    sched = run_waves(tasks, process_file=lambda t: _result(t.rel_path), file_workers=4)
    assert len(sched.results) == 10
    assert sched.skipped_budget == 0
    assert sched.skipped_other == 0


def test_files_actually_run_in_parallel():
    """With file_workers=4 and no caps, concurrent in-flight count exceeds 1."""
    max_concurrent = 0
    current = 0
    lock = threading.Lock()

    def process(_task: FileTask) -> FileSyncResult:
        nonlocal max_concurrent, current
        with lock:
            current += 1
            max_concurrent = max(max_concurrent, current)
        time.sleep(0.02)
        with lock:
            current -= 1
        return _result(_task.rel_path)

    tasks = [FileTask(rel_path=f"f{i}.py") for i in range(8)]
    run_waves(tasks, process_file=process, file_workers=4)
    assert max_concurrent >= 2  # genuine parallelism


def test_none_result_counts_as_skip():
    tasks = [FileTask(rel_path="a.py"), FileTask(rel_path="b.py")]
    sched = run_waves(
        tasks,
        process_file=lambda t: None if t.rel_path == "b.py" else _result(t.rel_path),
        file_workers=4,
    )
    assert len(sched.results) == 1
    assert sched.skipped_other == 1


def test_exception_in_one_file_does_not_sink_wave():
    def process(task: FileTask) -> FileSyncResult:
        if task.rel_path == "boom.py":
            raise RuntimeError("kaboom")
        return _result(task.rel_path)

    tasks = [FileTask(rel_path="ok1.py"), FileTask(rel_path="boom.py"), FileTask(rel_path="ok2.py")]
    sched = run_waves(tasks, process_file=process, file_workers=4)
    assert len(sched.results) == 2
    # Errors are first-class, NOT conflated with "no symbols" skips — callers
    # must be able to fail loudly when files errored.
    assert sched.skipped_other == 0
    assert sched.errors == [("boom.py", "kaboom")]


def test_all_files_erroring_is_not_a_silent_success():
    """Regression: a keyless/whole-run failure must be distinguishable from
    'nothing to do' — previously every error landed in skipped_other and the
    CLI reported a green 'synced 0 file(s)'."""

    def process(task: FileTask) -> FileSyncResult:
        raise RuntimeError("Could not resolve authentication method (missing api_key)")

    tasks = [FileTask(rel_path="a.py"), FileTask(rel_path="b.py")]
    sched = run_waves(tasks, process_file=process, file_workers=2)
    assert sched.results == []
    assert sched.skipped_other == 0
    assert len(sched.errors) == 2
    assert all("api_key" in err for _, err in sched.errors)


def test_limit_caps_and_reports_skips():
    tasks = [FileTask(rel_path=f"f{i}.py") for i in range(5)]
    skips: list[str] = []

    class Rec:
        def on_start(self, *a, **k):
            pass

        def on_done(self, *a, **k):
            pass

        def on_skip(self, rel, reason):
            skips.append(reason)

    sched = run_waves(
        tasks, process_file=lambda t: _result(t.rel_path), file_workers=4, limit=2, progress=Rec()
    )
    assert len(sched.results) == 2
    assert sched.skipped_budget == 3
    assert all(r == "limit reached" for r in skips)


def test_budget_caps_run():
    tasks = [FileTask(rel_path=f"f{i}.py") for i in range(5)]
    sched = run_waves(
        tasks,
        process_file=lambda t: _result(t.rel_path),
        file_workers=4,
        budget_usd=0.0001,
        cost_of=lambda r: 0.001,  # each file costs more than the budget
    )
    assert len(sched.results) == 1  # first file overshoots, then stop
    assert sched.skipped_budget == 4


def test_depth_banded_ordering_band0_before_band1():
    """Hop-0 files must all finish before any hop-1 file starts."""
    order: list[str] = []
    lock = threading.Lock()

    def process(task: FileTask) -> FileSyncResult:
        with lock:
            order.append(task.rel_path)
        return _result(task.rel_path)

    tasks = [
        FileTask(rel_path="b1a.py", hop=1),
        FileTask(rel_path="b0a.py", hop=0),
        FileTask(rel_path="b1b.py", hop=1),
        FileTask(rel_path="b0b.py", hop=0),
    ]
    run_waves(tasks, process_file=process, file_workers=4, limit=None)
    # Every hop-0 file appears before every hop-1 file.
    hop0_positions = [i for i, r in enumerate(order) if r.startswith("b0")]
    hop1_positions = [i for i, r in enumerate(order) if r.startswith("b1")]
    assert max(hop0_positions) < min(hop1_positions)


def test_global_inflight_semaphore_caps_concurrency():
    """configure_inflight_limit bounds concurrent _inflight_slot holders."""
    from trie import models

    models.configure_inflight_limit(2)
    max_held = 0
    held = 0
    lock = threading.Lock()

    def worker() -> None:
        nonlocal max_held, held
        with models._inflight_slot():
            with lock:
                held += 1
                max_held = max(max_held, held)
            time.sleep(0.02)
            with lock:
                held -= 1

    threads = [threading.Thread(target=worker) for _ in range(8)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    models.configure_inflight_limit(0)  # reset
    assert max_held <= 2
