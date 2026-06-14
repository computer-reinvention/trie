from __future__ import annotations

import threading
import time
from contextlib import AbstractContextManager, suppress
from enum import IntEnum
from types import TracebackType
from typing import Any

try:
    from rich.console import Console  # type: ignore[import-untyped,import-not-found]
    from rich.progress import (  # type: ignore[import-untyped,import-not-found]
        BarColumn,
        MofNCompleteColumn,
        Progress,
        SpinnerColumn,
        TaskID,
        TextColumn,
    )
    from rich.text import Text  # type: ignore[import-untyped,import-not-found]
except ImportError as exc:  # pragma: no cover
    raise ImportError("rich is required: pip install rich") from exc


# The progress display mixes two kinds of task in one Progress: the determinate
# overall bar (total=N) and per-file spinner rows (total=None, indeterminate).
# Rich applies every column to every task, so a plain BarColumn/MofNCompleteColumn
# would render a meaningless `━━━ 0/?` next to each in-flight file. These
# subclasses render nothing for indeterminate tasks, so the bar + M/N appear only
# on the overall row and per-file rows stay "spinner + filename".


class _OverallOnlyBar(BarColumn):
    def render(self, task):  # type: ignore[no-untyped-def]
        if task.total is None:
            return ""
        return super().render(task)


class _OverallOnlyMofN(MofNCompleteColumn):
    def render(self, task):  # type: ignore[no-untyped-def]
        if task.total is None:
            return ""
        return super().render(task)


class _BottomBarProgress(Progress):
    """Progress that pins the determinate overall bar to the BOTTOM.

    Rich renders tasks in insertion order, and we add the overall bar first so
    it would sit on top of the in-flight file rows. We instead want the live
    layout to read top-to-bottom as: in-flight files, a blank separator, then the
    ``syncing ━━━ M/N`` bar last — so the moving bar stays anchored at the bottom
    just above the shell prompt. Override the render order: indeterminate (file)
    tasks first, then a spacer, then determinate (overall) tasks.
    """

    def get_renderables(self):  # type: ignore[no-untyped-def]
        file_tasks = [t for t in self.tasks if t.total is None]
        overall_tasks = [t for t in self.tasks if t.total is not None]
        if file_tasks:
            yield self.make_tasks_table(file_tasks)
        # Blank line separating the file list from the overall bar. Only emit it
        # when the bar is actually shown, so a trailing blank line never dangles.
        if overall_tasks:
            if file_tasks:
                yield Text("")
            yield self.make_tasks_table(overall_tasks)


class Verbosity(IntEnum):
    MUTE = 0
    MEDIUM = 1
    VERBOSE = 2


class Reporter:
    """Verbosity-gated console wrapper used across the CLI.

    The CLI builds one of these in the root callback and threads it through every
    subcommand handler. Sync internals never see this — they receive a `ProgressCallback`
    instead, so they stay Rich-free.
    """

    def __init__(self, verbosity: Verbosity = Verbosity.MEDIUM, console: Console | None = None):
        self.verbosity = verbosity
        self.console = console or Console()
        self._start = time.monotonic()

    def info(self, msg: str) -> None:
        if self.verbosity >= Verbosity.MEDIUM:
            self.console.print(msg)

    def detail(self, msg: str) -> None:
        if self.verbosity >= Verbosity.VERBOSE:
            self.console.print(msg)

    def success(self, msg: str) -> None:
        if self.verbosity >= Verbosity.MEDIUM:
            self.console.print(f"[green]✓[/green] {msg}")

    def warn(self, msg: str) -> None:
        # Warnings still suppressed in MUTE — only errors are unconditional.
        if self.verbosity >= Verbosity.MEDIUM:
            self.console.print(f"[yellow]![/yellow] {msg}")

    def error(self, msg: str) -> None:
        self.console.print(f"[red]error:[/red] {msg}")

    def status(self, msg: str) -> AbstractContextManager[Any]:
        """Render a transient spinner while a step is in flight (MEDIUM+ only)."""
        if self.verbosity >= Verbosity.MEDIUM:
            return self.console.status(msg)
        return _NullContext()

    def elapsed(self) -> str:
        """Return a human-readable wall-clock elapsed time since this Reporter was created."""
        elapsed = time.monotonic() - self._start
        return f"took {elapsed:.2f}s"

    def start_progress(self, total: int, label: str) -> ProgressHandle:
        return ProgressHandle(self, total=total, label=label)


class _NullContext:
    def __enter__(self) -> _NullContext:
        return self

    def __exit__(self, *exc: Any) -> None:
        return None


class ProgressHandle:
    """`uv`-style live progress for parallel, out-of-order file processing.

    The display has two regions, rendered together by one Rich ``Progress``:

      • a pinned overall bar at the bottom (``label  ███  M/N • ETA``), and
      • one ephemeral spinner line per *in-flight* file above it.

    As files start, a per-file spinner line appears; as each finishes, its line
    is removed and a permanent ``✓ rel_path · …`` line is printed above the live
    region. Because every in-flight file owns its own Rich task (keyed by path),
    concurrent ``start_file``/``finish_file`` calls from the wave scheduler never
    stomp each other — the old single-description model garbled under parallelism.

    Thread-safe: the wave scheduler calls these from worker-completion handling on
    one thread today, but a lock guards the task map so it stays correct even if
    callbacks fire from multiple threads. MUTE is a complete no-op.
    """

    def __init__(self, reporter: Reporter, total: int, label: str):
        self.reporter = reporter
        self.total = total
        self.label = label
        self._progress: Progress | None = None
        self._overall: TaskID | None = None
        self._file_tasks: dict[str, TaskID] = {}
        # Remember which in-flight files were cascade-pulled so the persistent
        # ✓ line can carry the same marker the spinner showed.
        self._cascade_files: set[str] = set()
        self._lock = threading.Lock()

    def __enter__(self) -> ProgressHandle:
        # Only drive a live render when attached to a real terminal. In a pipe,
        # a redirected file, or any non-interactive shell, Rich's Live region
        # writes cursor-control escapes that corrupt the output and can clobber
        # the user's prompt on exit. There we fall back to plain printed lines
        # (the `_progress is None` paths in start_file/finish_file/skip_file).
        if (
            self.reporter.verbosity >= Verbosity.MEDIUM
            and self.total > 0
            and self.reporter.console.is_terminal
        ):
            progress = _BottomBarProgress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                _OverallOnlyBar(),
                _OverallOnlyMofN(),
                console=self.reporter.console,
                transient=False,
            )
            progress.__enter__()
            # Overall bar: a determinate task tracking completed files. Per-file
            # spinner tasks are added with total=None (spinner + description only).
            self._overall = progress.add_task(self.label, total=self.total)
            self._progress = progress
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        if self._progress is not None:
            # Drop any lingering per-file spinner rows so the live region tears
            # down cleanly, then close it (restores the cursor / shows it again).
            with self._lock:
                for task in self._file_tasks.values():
                    with suppress(KeyError):
                        self._progress.remove_task(task)
                self._file_tasks.clear()
            self._progress.__exit__(exc_type, exc, tb)
            self._progress = None
            self._overall = None
            # Belt-and-braces: Rich hides the cursor during the Live render and
            # restores it on normal exit, but an interrupted/odd teardown can
            # leave it hidden — which looks like the shell "ate" the prompt.
            # Force it visible.
            with suppress(Exception):
                self.reporter.console.show_cursor(True)

    def _print(self, line: str) -> None:
        # Route through the live Progress's console so output lands above the
        # live region instead of fighting with it.
        if self._progress is not None:
            self._progress.console.print(line)
        else:
            self.reporter.console.print(line)

    def start_file(self, rel_path: str, *, cascade: bool = False) -> None:
        # Cascade files (pulled in because they reference a directly-changed
        # symbol, not because their own source drifted) get a marker so the
        # operator can see why N files sync when only a few drifted.
        marker = " [magenta](cascade)[/magenta]" if cascade else ""
        if cascade:
            self._cascade_files.add(rel_path)
        if self._progress is None:
            if self.reporter.verbosity >= Verbosity.VERBOSE:
                plain = " (cascade)" if cascade else ""
                self._print(f"  [dim]→[/dim] {rel_path}{plain}")
            return
        with self._lock:
            if rel_path in self._file_tasks:
                return
            # An indeterminate (total=None) task renders as spinner + description
            # with no progress bar — one live line per in-flight file.
            task = self._progress.add_task(f"File: [cyan]{rel_path}[/cyan]{marker}", total=None)
            self._file_tasks[rel_path] = task

    def _end_file_task(self, rel_path: str) -> None:
        if self._progress is None:
            return
        with self._lock:
            task = self._file_tasks.pop(rel_path, None)
            if self._overall is not None:
                self._progress.advance(self._overall)
            if task is not None:
                self._progress.remove_task(task)

    def finish_file(
        self,
        rel_path: str,
        *,
        cost_usd: float | None = None,
        symbols: int | None = None,
        tokens_in: int | None = None,
        tokens_out: int | None = None,
        cache_read: int | None = None,
        cache_write: int | None = None,
    ) -> None:
        self._end_file_task(rel_path)
        is_cascade = rel_path in self._cascade_files
        self._cascade_files.discard(rel_path)

        if self.reporter.verbosity < Verbosity.MEDIUM:
            return

        marker = " [magenta](cascade)[/magenta]" if is_cascade else ""
        parts: list[str] = [f"  [green]✓[/green] {rel_path}{marker}"]
        if cost_usd is not None:
            parts.append(f"${cost_usd:.4f}")
        if symbols is not None:
            parts.append(f"{symbols} sym")
        line = " · ".join(parts)
        self._print(line)

        if self.reporter.verbosity >= Verbosity.VERBOSE:
            detail_bits: list[str] = []
            if tokens_in is not None or tokens_out is not None:
                detail_bits.append(f"tok {tokens_in or 0}/{tokens_out or 0}")
            if cache_read is not None or cache_write is not None:
                detail_bits.append(f"cache r{cache_read or 0}/w{cache_write or 0}")
            if detail_bits:
                self._print(f"      [dim]{' · '.join(detail_bits)}[/dim]")

    def skip_file(self, rel_path: str, reason: str) -> None:
        self._end_file_task(rel_path)
        self._cascade_files.discard(rel_path)
        if self.reporter.verbosity >= Verbosity.MEDIUM:
            self._print(f"  [yellow]⊘[/yellow] {rel_path} · skipped: {reason}")
