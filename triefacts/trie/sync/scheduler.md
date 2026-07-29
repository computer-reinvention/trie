---
trie_version: 0.1.9
source: trie/sync/scheduler.py
file_fingerprint: 505926ab4c10a176fb8bad547743c386de248551c991f6d6f1ff332d04f8eb34
last_synced_at: '2026-07-29T03:04:03Z'
description: Wave-based file scheduler for parallel triefact sync.
defines:
- kind: module
  qualified_name: trie/sync/scheduler:__module__
  lines: 1-267
- kind: class
  qualified_name: trie/sync/scheduler:FileTask
  lines: 43-50
- kind: class
  qualified_name: trie/sync/scheduler:SchedulerResult
  lines: 54-62
- kind: function
  qualified_name: trie/sync/scheduler:run_waves
  lines: 65-151
- kind: class
  qualified_name: trie/sync/scheduler:_RunState
  lines: 154-253
- kind: method
  qualified_name: trie/sync/scheduler:_RunState.__init__
  lines: 163-187
- kind: method
  qualified_name: trie/sync/scheduler:_RunState._cap_reason
  lines: 189-192
- kind: method
  qualified_name: trie/sync/scheduler:_RunState.skip_all
  lines: 194-198
- kind: method
  qualified_name: trie/sync/scheduler:_RunState.run_band
  lines: 200-231
- kind: method
  qualified_name: trie/sync/scheduler:_RunState._collect
  lines: 233-253
- kind: function
  qualified_name: trie/sync/scheduler:_group_into_bands
  lines: 256-266
incoming_refs: 20
outgoing_refs: 10
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
<!-- trie:section symbol=trie/sync/scheduler:FileTask fingerprint=eb478aa3b85470d657820963f81596094accb4897a0639ce46ca39b4c257d121 body_fp=5b174733d4641ef072b01ea4451efe642b0429d0e0d9c67ed612e73af12da9ba source_ref=95bf65ae092aa07f5efb15802ab19c1bddc0a8e9 role=model -->
Represents one file to sync with its relative path, hop distance for wave banding, and optional symbol regeneration targets.

- `hop`: cascade distance from directly-changed files (0 = directly changed)
- `regen_qnames`: specific symbols to regenerate (None = full file regeneration)
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/scheduler:SchedulerResult fingerprint=435622827bc2ed6fea5a22c236d213cb97d1e17f4c5ad6e2b6b3558dc817c9b2 body_fp=3b37383a16b9a4773049aa7b62bafad10d80dcb5456b5a96b47d8419622496a9 source_ref=4e206a1a3df5aaf86dc8fb7331c53af46fc6bc99 role=model -->
Holds the outcome of a wave-based file sync run with results, skip counts, and per-file errors.

- `skipped_budget`: Files skipped due to budget/limit caps
- `skipped_other`: Files legitimately skipped for having no symbols to document
- `errors`: `(rel_path, error_message)` pairs for files whose processing raised an exception
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/scheduler:run_waves fingerprint=1a9da311d4b6249446075c613a17db3a2f23c4c2e4c06c0aa4a5d2160d908d78 body_fp=b6aef2dc2b2785450877973ebc19838f285b90afcb22f574b72d581c594bce36 source_ref=4e206a1a3df5aaf86dc8fb7331c53af46fc6bc99 role=orchestration -->
Executes file sync tasks in hop-distance bands with parallel processing and budget enforcement.

- `process_file`: callback that syncs one file and returns its result or None
- `file_workers`: concurrency level, forced to 1 when budget/limit is active
- `budget_usd`: USD spending cap, enforced by stopping submission when reached
- `limit`: maximum number of files to process successfully
- `cost_of`: function to extract USD cost from a completed file result
- returns `SchedulerResult` with `errors` populated for files whose processing raised
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/scheduler:_RunState fingerprint=9019a7d6a731b11e43c0b87ab6d8a283605257c0b64ce6a4abdc7689207b65f3 body_fp=590aedce020ad30bd5eefe42676bfdeaa4e319db10c90aac7bdbd70799ee4f53 source_ref=4e206a1a3df5aaf86dc8fb7331c53af46fc6bc99 role=orchestration -->
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
<!-- trie:section symbol=trie/sync/scheduler:_RunState.__init__ fingerprint=44d1d0b67ecd79a3c6a14c406bc009d78aac18d8bedb971976c9b5be6166081a body_fp=be4bc55dc68ed76de4aa8f4eb5a03e8b52bef84a743a6665935ac4a8d70a3e23 source_ref=4e206a1a3df5aaf86dc8fb7331c53af46fc6bc99 role=domain -->
Initializes `_RunState` with scheduler configuration and zeroed accumulator state for tracking sync results, costs, and per-file errors.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/scheduler:_RunState._cap_reason fingerprint=745db94439eb199837294a37912fe7401e59543bcc3a5d10be2a2d8dff59f02c body_fp=bf8642d1217240d4f2144cac8e75a6122272a86da463a24453aa13d06b594109 source_ref=95bf65ae092aa07f5efb15802ab19c1bddc0a8e9 role=util -->
Returns the reason why `_RunState` should stop submitting files, checking limit before budget.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/scheduler:_RunState.skip_all fingerprint=7ddb9f4be8c6640d437b76d4281a78c0943d91a49daf8063ba2a3e7d70a46545 body_fp=0170bc756335e41ba625177c884d1e94319aff372ca363b157a1ecae74597c1f source_ref=95bf65ae092aa07f5efb15802ab19c1bddc0a8e9 role=orchestration -->
Marks all tasks as skipped due to budget/limit caps and notifies the progress callback.

- Increments `skipped_budget` count for each task
- Uses `_cap_reason()` to determine the skip reason for callback
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/scheduler:_RunState.run_band fingerprint=33613a78c4b78bdb90ab5a5bcbc7ebf979191e3bef588f10fb8a7d652988bad6 body_fp=29ec570246d08a6e411322ebe973e08cffd29cbf930732df060eafeb5ab40ad0 source_ref=0fc3ddd6f1f7339e910cd55f5cf4a4f3e622d659 role=orchestration -->
Executes _RunState file tasks in parallel using a ThreadPoolExecutor with worker limit.

- Maintains exactly `self.workers` concurrent tasks by submitting new ones as others complete
- Passes `cascade` flag to progress callback based on task hop distance
- Stops submission when budget/limit caps are hit but allows in-flight tasks to finish
- Skips remaining tasks if execution was halted mid-band
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/scheduler:_RunState._collect fingerprint=1efea74038c33db180b0a269f85564dd1a8c5d7cacb43a340164a2b4d7b08a84 body_fp=fc828e9cc27360589f01da309f53313b4929f54ffa162c8597352f50de8b413c source_ref=4e206a1a3df5aaf86dc8fb7331c53af46fc6bc99 role=domain -->
Processes completed file sync future, updating `_RunState` results and checking budget/limit caps.

- Catches exceptions from individual file failures to prevent wave collapse; appends `(rel_path, error)` to `self.errors` instead of incrementing `skipped_other`
- Skips files returning None (no symbols to document)
- Accumulates costs and sets stop flag when `budget_usd` or `limit` exceeded
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/scheduler:_group_into_bands fingerprint=e4081dea065b626f0ebc626b384187f219d17e7c6aeccc9a81f80c5ac5738200 body_fp=79b2c55d40a9c1841d3ce14586e32661ea90f303d4a39408af8e1d36d972b4d6 source_ref=95bf65ae092aa07f5efb15802ab19c1bddc0a8e9 role=orchestration -->
Groups tasks by hop distance into sequential bands for wave-based execution.

- Returns bands in ascending hop order so directly-changed files complete before callers
- Tasks with identical hop values share a band and run in parallel
<!-- trie:end -->