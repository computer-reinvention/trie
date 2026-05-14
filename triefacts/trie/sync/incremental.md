---
trie_version: 0.1.0
source: trie/sync/incremental.py
file_fingerprint: 4a2fb47825d1a2c965cb8b7891fb5c7e4777a239d2062c7918114b303d594c70
last_synced_at: '2026-05-14T18:55:31Z'
defines:
- kind: class
  qualified_name: trie/sync/incremental:IncrementalWorklist
  lines: 19-31
- kind: class
  qualified_name: trie/sync/incremental:IncrementalResult
  lines: 35-43
- kind: function
  qualified_name: trie/sync/incremental:compute_incremental_worklist
  lines: 46-92
- kind: function
  qualified_name: trie/sync/incremental:run_incremental
  lines: 95-203
incoming_refs: 14
outgoing_refs: 9
---
<!-- trie:section symbol=trie/sync/incremental:IncrementalWorklist fingerprint=612b09824da967027fa1ef2e5eecde2e7f8e7f1e16a554538c49f86b588aa911 body_fp=2a0f89003fea4aa2dd85e91858e80dda752ac23ab1a350f0c34b5dd6205379b0 -->
## `IncrementalWorklist`

Frozen dataclass previewing which files and orphans `run_incremental` would touch, without making changes.

- **`affected_files`**: union of directly stale and cascaded files
- **`directly_stale`**: files whose triefacts are outdated relative to source
- **`cascaded_files`**: files pulled in transitively via the symbol graph
- **`orphan_triefacts`**: triefact paths with no corresponding source file
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/incremental:IncrementalResult fingerprint=44d8d13db810a81ea27f75709b870895913876f1c8dbdc95aa93ed09cc9916cf body_fp=4019202d14a6c4248b4e058c755061cbad02e8c84a44771671da2166f3217384 -->
## `IncrementalResult`

Frozen dataclass summarising the outcome of a `run_incremental` call.

- `files_skipped_no_budget`: count of files skipped due to budget or limit exhaustion.
- `files_skipped_no_symbols`: count of files skipped because they had no public symbols.
- `orphan_triefacts_removed`: paths of deleted triefacts with no matching source file.
- `sync_results`: per-file `FileSyncResult` for each successfully processed file.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/incremental:compute_incremental_worklist fingerprint=b08baa6ed9200186afbab7173f99dbd4dc9915aca4e1de8b8900728330e16a92 body_fp=d238b74ae0b94acba7502713463a0afd7adbad5cbdc762cd3ca3d213124cfff5 -->
## `compute_incremental_worklist(*, project_root: Path, config: Config, store: Store) -> IncrementalWorklist`

Scan, check, and cascade to produce a read-only preview of files `run_incremental` would touch.

- `orphan_triefacts`: listed but not deleted; caller decides whether to remove them.
- Stale items whose source file no longer exists are excluded and treated as orphans.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/incremental:run_incremental fingerprint=e18cb6747206cd56bea10f70f101430eb3af51714fbf0b2705ec7a4ebc2b81ec body_fp=a43ef448899853eb5ba0c726398456de54bfb8ec24f26b6e37e8dc2cf464d834 -->
## `run_incremental(*, project_root: Path, config: Config, store: Store, client: ModelClient, pricing: ModelPricing | None = None, budget_usd: float | None = None, limit: int | None = None, progress: ProgressCallback | None = None) -> IncrementalResult`

Refresh stale triefacts and their cascade of dependent files, then remove orphan triefacts.

- `budget_usd`: stops queuing new files once cumulative cost meets or exceeds this value.
- `limit`: stops queuing new files once this many have been successfully synced.
- `pricing`: if `None`, cost tracking is skipped and `actual_cost_usd` stays `0.0`.
- `progress`: if `None`, a no-op callback is used.
<!-- trie:end -->