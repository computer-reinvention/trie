from __future__ import annotations

from typing import Protocol, runtime_checkable

from trie.sync.single_file import FileSyncResult


@runtime_checkable
class ProgressCallback(Protocol):
    """Hooks for streaming per-file progress out of multi-file sync runs.

    The CLI wires these into a Reporter-backed implementation. Sync internals call
    `on_start` before and `on_done` / `on_skip` after each file, with no awareness
    of how the host renders them.
    """

    def on_start(self, rel_path: str, idx: int, total: int) -> None: ...

    def on_done(self, rel_path: str, result: FileSyncResult, running_cost_usd: float) -> None: ...

    def on_skip(self, rel_path: str, reason: str) -> None: ...


class _NullProgress:
    def on_start(self, rel_path: str, idx: int, total: int) -> None:
        return None

    def on_done(self, rel_path: str, result: FileSyncResult, running_cost_usd: float) -> None:
        return None

    def on_skip(self, rel_path: str, reason: str) -> None:
        return None


NULL_PROGRESS: ProgressCallback = _NullProgress()
