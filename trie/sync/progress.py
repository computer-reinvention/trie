from __future__ import annotations

from typing import Protocol, runtime_checkable

from trie.sync.single_file import FileSyncResult


@runtime_checkable
class ProgressCallback(Protocol):
    """Hooks for streaming per-file progress out of multi-file sync runs.

    The CLI wires these into a Reporter-backed implementation. Sync internals call
    `on_start` before and `on_done` / `on_skip` after each file, with no awareness
    of how the host renders them.

    `on_plan` and `on_section` are OPTIONAL informational hooks: sync emits them
    via `emit_plan` / `emit_section` (which no-op when the callback doesn't
    implement them), so existing minimal callbacks need not define them.
    """

    def on_start(self, rel_path: str, idx: int, total: int, *, cascade: bool = False) -> None: ...

    def on_done(self, rel_path: str, result: FileSyncResult, running_cost_usd: float) -> None: ...

    def on_skip(self, rel_path: str, reason: str) -> None: ...


def emit_plan(cb: object, *, direct: int, cascade: int) -> None:
    """Best-effort: tell the callback how many direct vs cascade files are coming.

    Called once before any file starts so the host can print a summary header.
    Safe no-op for callbacks that don't implement `on_plan`."""
    hook = getattr(cb, "on_plan", None)
    if callable(hook):
        hook(direct=direct, cascade=cascade)


def emit_section(cb: object, *, label: str, count: int) -> None:
    """Best-effort: announce a new group of files (e.g. 'directly stale',
    'pulled in by the cascade') so the host can print a separator before them.
    Safe no-op for callbacks that don't implement `on_section`."""
    hook = getattr(cb, "on_section", None)
    if callable(hook):
        hook(label=label, count=count)


class _NullProgress:
    def on_start(self, rel_path: str, idx: int, total: int, *, cascade: bool = False) -> None:
        return None

    def on_done(self, rel_path: str, result: FileSyncResult, running_cost_usd: float) -> None:
        return None

    def on_skip(self, rel_path: str, reason: str) -> None:
        return None


NULL_PROGRESS: ProgressCallback = _NullProgress()
