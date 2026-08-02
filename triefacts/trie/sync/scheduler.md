---
trie_version: 0.3.0
source: trie/sync/scheduler.py
file_fingerprint: 505926ab4c10a176fb8bad547743c386de248551c991f6d6f1ff332d04f8eb34
last_synced_at: '2026-08-02T21:19:51Z'
description: Wave-based file scheduler for parallel triefact sync.
defines:
- kind: module
  qualified_name: trie/sync/scheduler:__module__
  lines: 1-267
- kind: class
  qualified_name: trie/sync/scheduler:FileTask
  lines: 43-50
  signature: class FileTask
- kind: class
  qualified_name: trie/sync/scheduler:SchedulerResult
  lines: 54-62
  signature: class SchedulerResult
- kind: function
  qualified_name: trie/sync/scheduler:run_waves
  lines: 65-151
  signature: 'def run_waves( tasks: list[FileTask], *, process_file: Callable[[FileTask], FileSyncResult | None], file_workers: int, progress: ProgressCallback | None = None, budget_usd: float | None = None, limit: int | None = None, cost_of: Callable[[FileSyncResult], float] | None = None, ) -> SchedulerResult'
- kind: class
  qualified_name: trie/sync/scheduler:_RunState
  lines: 154-253
  signature: class _RunState
- kind: method
  qualified_name: trie/sync/scheduler:_RunState.__init__
  lines: 163-187
  signature: 'def __init__( self, *, cb: ProgressCallback, process_file: Callable[[FileTask], FileSyncResult | None], workers: int, total: int, budget_usd: float | None, limit: int | None, cost_of: Callable[[FileSyncResult], float] | None, ) -> None'
- kind: method
  qualified_name: trie/sync/scheduler:_RunState._cap_reason
  lines: 189-192
  signature: def _cap_reason(self) -> str
- kind: method
  qualified_name: trie/sync/scheduler:_RunState.skip_all
  lines: 194-198
  signature: 'def skip_all(self, tasks: Iterable[FileTask]) -> None'
- kind: method
  qualified_name: trie/sync/scheduler:_RunState.run_band
  lines: 200-231
  signature: 'def run_band(self, band: list[FileTask]) -> None'
- kind: method
  qualified_name: trie/sync/scheduler:_RunState._collect
  lines: 233-253
  signature: 'def _collect(self, fut) -> None: # type: ignore[no-untyped-def]'
- kind: function
  qualified_name: trie/sync/scheduler:_group_into_bands
  lines: 256-266
  signature: 'def _group_into_bands(tasks: Iterable[FileTask]) -> list[list[FileTask]]'
incoming_refs: 20
outgoing_refs: 14
---
<!-- trie:section symbol=trie/sync/scheduler:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=64f63323bd54ba136d38c15726a4857ff89a86697d6e3eaa331ba5e9c1e1da11 source_ref=95bf65ae092aa07f5efb15802ab19c1bddc0a8e9 role=orchestration -->
Provides wave-based parallel file scheduler for triefact sync operations.

- **FileTask**: Represents one file to sync with hop distance for cascade ordering
- **SchedulerResult**: Accumulates sync results and skip counts from scheduler execution  
- **run_waves()**: Executes file tasks in depth-banded parallel waves with budget/limit controls
- **_RunState**: Internal mutable state tracker for cross-band totals and per-call configuration
- **_group_into_bands()**: Groups tasks by hop distance into sequential execution bands

Files are grouped by cascade hop distance into bands that execute sequentially (preserving diff-aware invariants), while files within each band run in parallel. Thread pool size and global LLM request limits are decoupled for optimal provider rate utilization.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/scheduler:FileTask fingerprint=eb478aa3b85470d657820963f81596094accb4897a0639ce46ca39b4c257d121 body_fp=9cf810746fd6eb18c5d3f085bbb9dee1a6d0122748e17b64d00eeaaa399b4943 source_ref=95bf65ae092aa07f5efb15802ab19c1bddc0a8e9 role=model -->
## `class FileTask`

Represents one file to sync with its relative path, hop distance for wave banding, and optional symbol regeneration targets.

- `hop`: cascade distance from directly-changed files (0 = directly changed)
- `regen_qnames`: specific symbols to regenerate (None = full file regeneration)
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/scheduler:SchedulerResult fingerprint=435622827bc2ed6fea5a22c236d213cb97d1e17f4c5ad6e2b6b3558dc817c9b2 body_fp=20a4c311402092fe66e634107619262aeae65f1e8001888ba6912e498887b9fa source_ref=4e206a1a3df5aaf86dc8fb7331c53af46fc6bc99 role=model -->
## `class SchedulerResult`

Holds the outcome of a wave-based file sync run with results, skip counts, and per-file errors.

- `skipped_budget`: Files skipped due to budget/limit caps
- `skipped_other`: Files legitimately skipped for having no symbols to document
- `errors`: `(rel_path, error_message)` pairs for files whose processing raised an exception
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/scheduler:run_waves fingerprint=1a9da311d4b6249446075c613a17db3a2f23c4c2e4c06c0aa4a5d2160d908d78 body_fp=d6ec10c8e08e25329ca4587e12b2e6c4461be17b368b26106091c9dd514831de source_ref=4e206a1a3df5aaf86dc8fb7331c53af46fc6bc99 role=orchestration -->
## `def run_waves( tasks: list[FileTask], *, process_file: Callable[[FileTask], FileSyncResult | None], file_workers: int, progress: ProgressCallback | None = None, budget_usd: float | None = None, limit: int | None = None, cost_of: Callable[[FileSyncResult], float] | None = None, ) -> SchedulerResult`

Executes file sync tasks in hop-distance bands with parallel processing and budget enforcement.

- `process_file`: callback that syncs one file and returns its result or None
- `file_workers`: concurrency level, forced to 1 when budget/limit is active
- `budget_usd`: USD spending cap, enforced by stopping submission when reached
- `limit`: maximum number of files to process successfully
- `cost_of`: function to extract USD cost from a completed file result
- returns `SchedulerResult` with `errors` populated for files whose processing raised
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/scheduler:_RunState fingerprint=9019a7d6a731b11e43c0b87ab6d8a283605257c0b64ce6a4abdc7689207b65f3 body_fp=3b5867f1a00411281163384488c2d4f8ebf0d1f5cd26882b726c91041df91abe source_ref=4e206a1a3df5aaf86dc8fb7331c53af46fc6bc99 role=orchestration -->
## `class _RunState`

Mutable state accumulator for wave-based parallel file processing with budget and limit enforcement.

- `stop`: boolean flag set when budget or limit cap is reached
- `actual_cost`: running USD cost total from completed files
- `skipped_budget`: count of files skipped due to budget/limit caps
- `skipped_other`: count of files skipped due to no symbols (errors are tracked separately)
- `errors`: list of `(rel_path, error_message)` tuples for files whose processing raised
- `run_band`: executes one hop-distance band using ThreadPoolExecutor with worker pool
- `skip_all`: marks remaining tasks as skipped when caps are hit
- `_collect`: processes completed futures, updates totals, and checks stop conditions
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/scheduler:_RunState.__init__ fingerprint=44d1d0b67ecd79a3c6a14c406bc009d78aac18d8bedb971976c9b5be6166081a body_fp=3f638c91722a46338bff0a10db76c703470e86d5da73e85d813373ccc2a00808 source_ref=4e206a1a3df5aaf86dc8fb7331c53af46fc6bc99 role=domain -->
## `def __init__( self, *, cb: ProgressCallback, process_file: Callable[[FileTask], FileSyncResult | None], workers: int, total: int, budget_usd: float | None, limit: int | None, cost_of: Callable[[FileSyncResult], float] | None, ) -> None`

Initializes `_RunState` with scheduler configuration and zeroed accumulator state for tracking sync results, costs, and per-file errors.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/scheduler:_RunState._cap_reason fingerprint=745db94439eb199837294a37912fe7401e59543bcc3a5d10be2a2d8dff59f02c body_fp=caa7bd3b37a0aa437ed6f4e3625b7d6f03a0a4ea5996a89c7d2d403a08382683 source_ref=95bf65ae092aa07f5efb15802ab19c1bddc0a8e9 role=util -->
## `def _cap_reason(self) -> str`

Returns the reason why `_RunState` should stop submitting files, checking limit before budget.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/scheduler:_RunState.skip_all fingerprint=7ddb9f4be8c6640d437b76d4281a78c0943d91a49daf8063ba2a3e7d70a46545 body_fp=cc61faf2d9cb0ca1008044195ed497e29d6501460f056a80f0a8a00ab66c97c8 source_ref=95bf65ae092aa07f5efb15802ab19c1bddc0a8e9 role=orchestration -->
## `def skip_all(self, tasks: Iterable[FileTask]) -> None`

Marks all tasks as skipped due to budget/limit caps and notifies the progress callback.

- Increments `skipped_budget` count for each task
- Uses `_cap_reason()` to determine the skip reason for callback
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/scheduler:_RunState.run_band fingerprint=33613a78c4b78bdb90ab5a5bcbc7ebf979191e3bef588f10fb8a7d652988bad6 body_fp=4d56a5a4ae83e1a995c1a65281cd852e755c16d0f78efbcc78328b2598c04273 source_ref=0fc3ddd6f1f7339e910cd55f5cf4a4f3e622d659 role=orchestration -->
## `def run_band(self, band: list[FileTask]) -> None`

Executes _RunState file tasks in parallel using a ThreadPoolExecutor with worker limit.

- Maintains exactly `self.workers` concurrent tasks by submitting new ones as others complete
- Passes `cascade` flag to progress callback based on task hop distance
- Stops submission when budget/limit caps are hit but allows in-flight tasks to finish
- Skips remaining tasks if execution was halted mid-band
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/scheduler:_RunState._collect fingerprint=1efea74038c33db180b0a269f85564dd1a8c5d7cacb43a340164a2b4d7b08a84 body_fp=68d7ca6f6bc138a541ef491e1e750b8abac26cc5c44ab4b2dac118be6153374f source_ref=4e206a1a3df5aaf86dc8fb7331c53af46fc6bc99 role=domain -->
## `def _collect(self, fut) -> None: # type: ignore[no-untyped-def]`

Processes completed file sync future, updating `_RunState` results and checking budget/limit caps.

- Catches exceptions from individual file failures to prevent wave collapse; appends `(rel_path, error)` to `self.errors` instead of incrementing `skipped_other`
- Skips files returning None (no symbols to document)
- Accumulates costs and sets stop flag when `budget_usd` or `limit` exceeded
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/scheduler:_group_into_bands fingerprint=e4081dea065b626f0ebc626b384187f219d17e7c6aeccc9a81f80c5ac5738200 body_fp=f2c7b749fe22dca55e5a0bdebd680a51af852a611984f623ca39c4d57b556fc6 source_ref=95bf65ae092aa07f5efb15802ab19c1bddc0a8e9 role=orchestration -->
## `def _group_into_bands(tasks: Iterable[FileTask]) -> list[list[FileTask]]`

Groups tasks by hop distance into sequential bands for wave-based execution.

- Returns bands in ascending hop order so directly-changed files complete before callers
- Tasks with identical hop values share a band and run in parallel
<!-- trie:end -->