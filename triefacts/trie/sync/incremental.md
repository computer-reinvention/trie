---
trie_version: 0.1.0
source: trie/sync/incremental.py
file_fingerprint: cf1bee01a114f9189beefb28dcd62d1a00006d9f59a1d63c333ccde5cc483664
last_synced_at: '2026-05-14T19:39:33Z'
defines:
- kind: class
  qualified_name: trie/sync/incremental:IncrementalWorklist
  lines: 19-36
- kind: class
  qualified_name: trie/sync/incremental:IncrementalResult
  lines: 40-48
- kind: function
  qualified_name: trie/sync/incremental:compute_incremental_worklist
  lines: 51-99
- kind: function
  qualified_name: trie/sync/incremental:run_incremental
  lines: 102-216
incoming_refs: 14
outgoing_refs: 9
---
<!-- trie:section symbol=trie/sync/incremental:IncrementalWorklist fingerprint=7826c19b1675dc11b7b99441f08cfd1c34dc9313071f237073b5192dc6021f55 body_fp=d2957bc5358efadeafd7fa77b03f9c5c01478290b97ad1295a5b9d934ffa80be source_ref=3d33f6931189bf5186ab59a9a7c0eaf8728c4797 -->
## `IncrementalWorklist`

Read-only preview of files `run_incremental` would touch, produced by `compute_incremental_worklist`.

- `hop_by_file`: cascade hop distance per file; stale files map to 0; used to rank cascade files closest-to-change first.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/incremental:IncrementalResult fingerprint=44d8d13db810a81ea27f75709b870895913876f1c8dbdc95aa93ed09cc9916cf body_fp=e3dc3304e84e6612872b6348d91fdf60ffce9a2ebdf7c41741052a2be27170a0 source_ref=3d33f6931189bf5186ab59a9a7c0eaf8728c4797 -->
## `IncrementalResult`

Frozen dataclass holding counts and cost totals returned by `run_incremental`.

- `files_skipped_no_budget`: files skipped due to `--limit` or `--budget` exhaustion.
- `files_skipped_no_symbols`: files skipped because they export no public symbols.
- `orphan_triefacts_removed`: paths of deleted stale triefacts with no source file.
- `sync_results`: one `FileSyncResult` per successfully processed file.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/incremental:compute_incremental_worklist fingerprint=e9fd2aa851cc9e5d4c1bf62d54211ae81d1a6f9a9d59f384e3be2668de57abad body_fp=e534a3d83eccc306724ef0e8340405acad09b7a6a350986c35157c87f4c27330 source_ref=3d33f6931189bf5186ab59a9a7c0eaf8728c4797 -->
## `compute_incremental_worklist(*, project_root: Path, config: Config, store: Store) -> IncrementalWorklist`

Scan, check, and cascade to produce a read-only preview of files `run_incremental` would touch.

- Does not delete orphan triefacts or invoke the LLM.
- Excludes stale entries whose source file no longer exists (treated as orphans).
- `orphan_triefacts` in result: caller decides whether to delete or just report.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/incremental:run_incremental fingerprint=cfe28cafc29ba473924756f0d5c3e6b6e6b4e0980f6aab68c6d1d243db28d1fa body_fp=8b816fdbcab95470ca72d25e82cf98005a81e1dc42add6a99625bad285120e62 source_ref=3d33f6931189bf5186ab59a9a7c0eaf8728c4797 -->
## `run_incremental(*, project_root: Path, config: Config, store: Store, client: ModelClient, pricing: ModelPricing | None = None, budget_usd: float | None = None, limit: int | None = None, progress: ProgressCallback | None = None) -> IncrementalResult`

Refresh triefacts for stale source files and their cascade of dependents, then remove orphan triefacts.

- `budget_usd`: stop syncing new files once cumulative cost meets or exceeds this value.
- `limit`: stop after this many files have been successfully synced.
- `pricing`: if `None`, cost tracking is disabled and `actual_cost_usd` is 0.
- `progress`: defaults to `NULL_PROGRESS` (no-op) when omitted.
- Files with no public symbols and no removed sections are counted in `files_skipped_no_symbols`, not `files_synced`.
- Directly-stale files are synced before cascade-pulled files; cascade files are ordered by hop distance ascending.
<!-- trie:end -->