from __future__ import annotations

from contextlib import AbstractContextManager
from enum import IntEnum
from types import TracebackType
from typing import Any

from rich.console import Console
from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    SpinnerColumn,
    TextColumn,
    TimeRemainingColumn,
)


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

    def status(self, msg: str) -> AbstractContextManager:
        """Render a transient spinner while a step is in flight (MEDIUM+ only)."""
        if self.verbosity >= Verbosity.MEDIUM:
            return self.console.status(msg)
        return _NullContext()

    def start_progress(self, total: int, label: str) -> ProgressHandle:
        return ProgressHandle(self, total=total, label=label)


class _NullContext:
    def __enter__(self) -> _NullContext:
        return self

    def __exit__(self, *exc: Any) -> None:
        return None


class ProgressHandle:
    """Per-file progress reporter. MEDIUM+ shows a Rich progress bar with ETA;
    finished files print as `✓ rel_path · $cost` lines above the bar.
    VERBOSE adds a `→ rel_path` line when each file starts.
    MUTE is a complete no-op.
    """

    def __init__(self, reporter: Reporter, total: int, label: str):
        self.reporter = reporter
        self.total = total
        self.label = label
        self._progress: Progress | None = None
        self._task_id: int | None = None

    def __enter__(self) -> ProgressHandle:
        if self.reporter.verbosity >= Verbosity.MEDIUM and self.total > 0:
            self._progress = Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                MofNCompleteColumn(),
                TextColumn("•"),
                TimeRemainingColumn(),
                console=self.reporter.console,
                transient=False,
            )
            self._progress.__enter__()
            self._task_id = self._progress.add_task(self.label, total=self.total)
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        if self._progress is not None:
            self._progress.__exit__(exc_type, exc, tb)
            self._progress = None
            self._task_id = None

    def _print(self, line: str) -> None:
        # When the progress bar is live, route through its console so output lands
        # above the bar instead of fighting with it.
        if self._progress is not None:
            self._progress.console.print(line)
        else:
            self.reporter.console.print(line)

    def start_file(self, rel_path: str) -> None:
        if self._progress is not None and self._task_id is not None:
            self._progress.update(
                self._task_id, description=f"{self.label} [cyan]{rel_path}[/cyan]"
            )
        if self.reporter.verbosity >= Verbosity.VERBOSE:
            self._print(f"  [dim]→[/dim] {rel_path}")

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
        if self._progress is not None and self._task_id is not None:
            self._progress.advance(self._task_id)

        if self.reporter.verbosity < Verbosity.MEDIUM:
            return

        parts: list[str] = [f"  [green]✓[/green] {rel_path}"]
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
        if self._progress is not None and self._task_id is not None:
            self._progress.advance(self._task_id)
        if self.reporter.verbosity >= Verbosity.MEDIUM:
            self._print(f"  [yellow]⊘[/yellow] {rel_path} · skipped: {reason}")
