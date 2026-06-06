---
trie_version: 0.1.5
source: trie/sync/scheduler.py
file_fingerprint: 3d3128809fc3a3c0222b747581f10fe57a575c7401711dd31bcf90c210076dbd
last_synced_at: '2026-06-06T13:44:09Z'
description: Wave-based file scheduler for parallel triefact sync.
defines:
- kind: module
  qualified_name: trie/sync/scheduler:__module__
  lines: 1-236
- kind: class
  qualified_name: trie/sync/scheduler:FileTask
  lines: 43-50
- kind: class
  qualified_name: trie/sync/scheduler:SchedulerResult
  lines: 54-57
- kind: function
  qualified_name: trie/sync/scheduler:run_waves
  lines: 60-122
- kind: class
  qualified_name: trie/sync/scheduler:_RunState
  lines: 125-222
- kind: method
  qualified_name: trie/sync/scheduler:_RunState.__init__
  lines: 134-157
- kind: method
  qualified_name: trie/sync/scheduler:_RunState._cap_reason
  lines: 159-162
- kind: method
  qualified_name: trie/sync/scheduler:_RunState.skip_all
  lines: 164-168
- kind: method
  qualified_name: trie/sync/scheduler:_RunState.run_band
  lines: 170-200
- kind: method
  qualified_name: trie/sync/scheduler:_RunState._collect
  lines: 202-222
- kind: function
  qualified_name: trie/sync/scheduler:_group_into_bands
  lines: 225-235
incoming_refs: 18
outgoing_refs: 9
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
<!-- trie:section symbol=trie/sync/scheduler:run_waves fingerprint=cc141ff94869173cc8ab8535407bb877afe26468c716821bc16d898065867b05 body_fp=dbc06e1627e5af6016e1028d034c0a9178ee105482f3efec4cfe8d16f2cdf380 source_ref=95bf65ae092aa07f5efb15802ab19c1bddc0a8e9 role=orchestration -->
Executes file sync tasks in depth-banded parallel waves with budget and limit enforcement.

- `process_file`: Called for each task, must be thread-safe
- `file_workers`: Thread pool size (reduced to 1 if budget/limit active)
- `budget_usd`: USD cost cap (requires `cost_of` function)
- `limit`: Maximum number of files to process
- `cost_of`: Function to calculate USD cost from sync result
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/scheduler:_RunState fingerprint=afb5f0dc3d576d710f247c90526877e5c0228889cd94fb0224376b4f13076803 body_fp=a5f4ebc0ef55ee7752b4c32af12980b0ca0165777d0b0d945a7342b3302619c0 source_ref=95bf65ae092aa07f5efb15802ab19c1bddc0a8e9 role=orchestration -->
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
<!-- trie:section symbol=trie/sync/scheduler:_RunState.run_band fingerprint=b0d7f407434fdc72434446fa4ca3e8eba62b701de1f8f5547e1bdd91bc784633 body_fp=da296a2bf38c28ac62fd199c2f4cfaf7d0082c9a20e7ad42ccf123e26f7f5f84 source_ref=95bf65ae092aa07f5efb15802ab19c1bddc0a8e9 role=orchestration -->
Executes _RunState file tasks in parallel using a ThreadPoolExecutor with worker limit.

- Maintains exactly `self.workers` concurrent tasks by submitting new ones as others complete
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