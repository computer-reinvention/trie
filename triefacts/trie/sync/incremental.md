---
trie_version: 0.1.2
source: trie/sync/incremental.py
file_fingerprint: 4c7a99e1ffa4459b158c5183633f0aad1eb6be7c6327019a3cdf30e8c64c2def
last_synced_at: '2026-05-24T00:25:26Z'
defines:
- kind: module
  qualified_name: trie/sync/incremental:__module__
  lines: 1-277
- kind: class
  qualified_name: trie/sync/incremental:IncrementalWorklist
  lines: 19-51
- kind: class
  qualified_name: trie/sync/incremental:IncrementalResult
  lines: 55-63
- kind: function
  qualified_name: trie/sync/incremental:compute_incremental_worklist
  lines: 66-142
- kind: function
  qualified_name: trie/sync/incremental:run_incremental
  lines: 145-276
incoming_refs: 19
outgoing_refs: 9
---
<!-- trie:section symbol=trie/sync/incremental:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=8b7d1eb492e35680875ff812049bdbfad96048d597c588c3e5ad7e97c657a6fa source_ref=75fad555723fb0d9fdc38c5f729779434c0a4951 -->
## `trie/sync/incremental`

Orchestrate incremental triefact sync: scan, staleness check, cascade, and per-symbol LLM regeneration.

- `IncrementalWorklist`: read-only preview of files and symbols a sync run would touch.
- `IncrementalResult`: summary counts and costs from a completed sync run.
- `compute_incremental_worklist`: build the worklist without mutating state or calling the LLM.
- `run_incremental`: execute the full incremental sync, deleting orphans and regenerating stale triefacts.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/incremental:IncrementalWorklist fingerprint=cdb0112edfc993b6d288ef8defa85093653d6f39080b9837798d5a3fddcb71a5 body_fp=a5e650806ef6ca88a19ac14204ce8b471e20b7c149f080e2b84cb4faac14980b source_ref=75fad555723fb0d9fdc38c5f729779434c0a4951 -->
## `IncrementalWorklist`

Frozen dataclass holding a read-only preview of files `run_incremental` would touch.

- `affected_files`: sorted union of directly-stale and cascade-pulled files.
- `directly_stale`: files whose triefacts are out of date relative to source.
- `cascaded_files`: files pulled in transitively via the cascade walk.
- `hop_by_file`: minimum cascade hops from any seed; stale files map to 0.
- `regen_qnames_by_file`: per-file set of qnames to regenerate; absent key means full-file regen.
- `orphan_triefacts`: triefact paths whose source file no longer exists.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/incremental:IncrementalResult fingerprint=44d8d13db810a81ea27f75709b870895913876f1c8dbdc95aa93ed09cc9916cf body_fp=6faeec0e9f86141b6311a2d5a4c3eb03079e35cfcac606e9b06f9aa90d5d0970 source_ref=75fad555723fb0d9fdc38c5f729779434c0a4951 -->
## `IncrementalResult`

Frozen dataclass summarising the outcome of a `run_incremental` call.

- `files_skipped_no_budget`: count of files skipped due to cost or limit cap.
- `files_skipped_no_symbols`: count of files with no documentable symbols.
- `actual_cost_usd`: total LLM cost incurred; zero when no pricing model supplied.
- `orphan_triefacts_removed`: triefact files deleted because their source was gone.
- `sync_results`: per-file `FileSyncResult` for every file actually processed.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/incremental:compute_incremental_worklist fingerprint=3c8386c7f8572fc00dc5dc15bce15bda702346e82a53d1bfc3344998aa6c6c47 body_fp=9001f6a49ff52b1bbfa25b2c668bca3733ea5e81a249ec76925120ca5553aff2 source_ref=75fad555723fb0d9fdc38c5f729779434c0a4951 -->
## `compute_incremental_worklist(*, project_root: Path, config: Config, store: Store) -> IncrementalWorklist`

Run scan + check + cascade and return the read-only worklist of files and symbols `run_incremental` would touch, without deleting orphans or calling the LLM.

- `store`: mutated by `scan_project` (hash-driven, idempotent); otherwise read-only.
- Returns `IncrementalWorklist` with empty lists if no stale files are found.
- Files missing from disk are excluded from stale lists and appear only in `orphan_triefacts`.
- `MISSING_TRIEFACT` items are omitted from `regen_qnames_by_file`, signalling full-file regen to the runner.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/incremental:run_incremental fingerprint=4f4334832b6715ee217168385cf25f369872022f8b2bc4bc7fcde9c19db2c193 body_fp=600b094eaa3ff5d58551f548484c8e99b644819267b52fe60d24c506bbbffb28 source_ref=75fad555723fb0d9fdc38c5f729779434c0a4951 -->
## `run_incremental(*, project_root: Path, config: Config, store: Store, client: ModelClient, pricing: ModelPricing | None = None, budget_usd: float | None = None, limit: int | None = None, progress: ProgressCallback | None = None) -> IncrementalResult`

Scan, check, cascade, and regenerate all stale triefacts plus their referencing files, deleting orphans.

- `budget_usd`: stops accepting new files once cumulative LLM cost meets or exceeds this value.
- `limit`: stops accepting new files once this many have been successfully synced.
- `pricing`: if `None`, cost tracking is skipped and `actual_cost_usd` is 0.
- `progress`: receives `on_start` / `on_done` / `on_skip` callbacks; defaults to a no-op.
- Directly-stale files are processed first; cascade-pulled files follow ordered by hop distance.
- Orphan triefact files are unlinked before syncing begins.
<!-- trie:end -->