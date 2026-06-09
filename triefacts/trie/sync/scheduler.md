---
trie_version: 0.1.5
source: trie/sync/scheduler.py
file_fingerprint: 057955bf550d298b274c7a8c5babf3afd0a573bf9a3ebdef0f903ca782de13e1
last_synced_at: '2026-06-09T10:07:37Z'
description: Wave-based file scheduler for parallel triefact sync.
defines:
- kind: module
  qualified_name: trie/sync/scheduler:__module__
  lines: 1-260
- kind: class
  qualified_name: trie/sync/scheduler:FileTask
  lines: 43-50
- kind: class
  qualified_name: trie/sync/scheduler:SchedulerResult
  lines: 54-57
- kind: function
  qualified_name: trie/sync/scheduler:run_waves
  lines: 60-145
- kind: class
  qualified_name: trie/sync/scheduler:_RunState
  lines: 148-246
- kind: method
  qualified_name: trie/sync/scheduler:_RunState.__init__
  lines: 157-180
- kind: method
  qualified_name: trie/sync/scheduler:_RunState._cap_reason
  lines: 182-185
- kind: method
  qualified_name: trie/sync/scheduler:_RunState.skip_all
  lines: 187-191
- kind: method
  qualified_name: trie/sync/scheduler:_RunState.run_band
  lines: 193-224
- kind: method
  qualified_name: trie/sync/scheduler:_RunState._collect
  lines: 226-246
- kind: function
  qualified_name: trie/sync/scheduler:_group_into_bands
  lines: 249-259
incoming_refs: 18
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
<!-- trie:section symbol=trie/sync/scheduler:SchedulerResult fingerprint=7678564001789868c1fe5c436184675a84edb4fb64fca6dbac395d24a1ce04c8 body_fp=df20eb314be55ba33525b635fde8d9c59474163f453035bca32f810661c969b8 source_ref=95bf65ae092aa07f5efb15802ab19c1bddc0a8e9 role=model -->
Holds the outcome of a wave-based file sync run with results and skip counts.

- `skipped_budget`: Files skipped due to budget/limit caps
- `skipped_other`: Files skipped due to errors or having no symbols to document
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/scheduler:run_waves fingerprint=a6d1cebd99370e943099dceb84d1e69507217bd203e52ed11082cd211ae611fd body_fp=73f8c18f6c255ddcc7344aba2010e161660b9d14cc9530270eb74e0af5628b1e source_ref=2bf723ae8e006fdd21a9f434926ea4420d9cc1e2 role=orchestration -->
Executes file sync tasks in hop-distance bands with parallel processing and budget enforcement.

- `process_file`: callback that syncs one file and returns its result or None
- `file_workers`: concurrency level, forced to 1 when budget/limit is active
- `budget_usd`: USD spending cap, enforced by stopping submission when reached
- `limit`: maximum number of files to process successfully
- `cost_of`: function to extract USD cost from a completed file result
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/scheduler:_RunState fingerprint=6f1f2be822f4775274f6fe542479bec76b8444a21b0f93eae50985a0a9b69765 body_fp=a5f4ebc0ef55ee7752b4c32af12980b0ca0165777d0b0d945a7342b3302619c0 source_ref=0fc3ddd6f1f7339e910cd55f5cf4a4f3e622d659 role=orchestration -->
Tracks mutable state across file sync waves including results, costs, skip counts, and stop conditions.

- `stop`: halts further task submission when budget or limit reached
- `skipped_budget`: count of files skipped due to budget/limit caps
- `skipped_other`: count of files skipped due to errors or no symbols
- `actual_cost`: accumulated USD cost of completed files
- `submitted`: total files submitted for processing across all bands
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/scheduler:_RunState.__init__ fingerprint=075ca8698682dc1b1bc5d8c0433231e495a47add91c846d61e63c73459b73eb0 body_fp=23961dc48431b5f07d088490a981c783fd201e13b78f71a9f2072bf0d41d8bb7 source_ref=95bf65ae092aa07f5efb15802ab19c1bddc0a8e9 role=model -->
Initializes _RunState with scheduler configuration and zeroed accumulator state for tracking sync results and costs.
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
<!-- trie:section symbol=trie/sync/scheduler:_RunState._collect fingerprint=da494cbe44daab5723607919a57c0e361c26135a4bb57f79c75479847cb7e42d body_fp=a0476094bb511ad182d5a16d5af803e3be19a726b5da420f1c0e4e2fe754fece source_ref=95bf65ae092aa07f5efb15802ab19c1bddc0a8e9 role=orchestration -->
Processes completed file sync future, updating _RunState results and checking budget/limit caps.

- Catches exceptions from individual file failures to prevent wave collapse
- Skips files returning None (no symbols to document)
- Accumulates costs and sets stop flag when budget_usd or limit exceeded
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/scheduler:_group_into_bands fingerprint=e4081dea065b626f0ebc626b384187f219d17e7c6aeccc9a81f80c5ac5738200 body_fp=79b2c55d40a9c1841d3ce14586e32661ea90f303d4a39408af8e1d36d972b4d6 source_ref=95bf65ae092aa07f5efb15802ab19c1bddc0a8e9 role=orchestration -->
Groups tasks by hop distance into sequential bands for wave-based execution.

- Returns bands in ascending hop order so directly-changed files complete before callers
- Tasks with identical hop values share a band and run in parallel
<!-- trie:end -->