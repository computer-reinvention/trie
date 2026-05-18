---
trie_version: 0.1.1
source: trie/sync/incremental.py
file_fingerprint: 4c7a99e1ffa4459b158c5183633f0aad1eb6be7c6327019a3cdf30e8c64c2def
last_synced_at: '2026-05-16T11:47:03Z'
defines:
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
incoming_refs: 17
outgoing_refs: 9
---
<!-- trie:section symbol=trie/sync/incremental:IncrementalWorklist fingerprint=cdb0112edfc993b6d288ef8defa85093653d6f39080b9837798d5a3fddcb71a5 body_fp=65e8770ac5aeb349ce9d768ed38373a4c6c8a7d95f0efab27fb5808fd4cac946 source_ref=75fad555723fb0d9fdc38c5f729779434c0a4951 -->
## `IncrementalWorklist`

Read-only preview of files `run_incremental` would touch, produced by `compute_incremental_worklist`.

- `hop_by_file`: cascade hop distance per file; stale files map to 0; used to rank cascade files closest-to-change first.
- `regen_qnames_by_file`: per-file set of qualified names to regenerate; absent entry means full-file regen (`symbols_to_regen=None`); never contains empty sets.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/incremental:IncrementalResult fingerprint=44d8d13db810a81ea27f75709b870895913876f1c8dbdc95aa93ed09cc9916cf body_fp=e3dc3304e84e6612872b6348d91fdf60ffce9a2ebdf7c41741052a2be27170a0 source_ref=75fad555723fb0d9fdc38c5f729779434c0a4951 -->
## `IncrementalResult`

Frozen dataclass holding counts and cost totals returned by `run_incremental`.

- `files_skipped_no_budget`: files skipped due to `--limit` or `--budget` exhaustion.
- `files_skipped_no_symbols`: files skipped because they export no public symbols.
- `orphan_triefacts_removed`: paths of deleted stale triefacts with no source file.
- `sync_results`: one `FileSyncResult` per successfully processed file.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/incremental:compute_incremental_worklist fingerprint=3c8386c7f8572fc00dc5dc15bce15bda702346e82a53d1bfc3344998aa6c6c47 body_fp=b90d5d90c1d66ee747b4672b1dba07fcfd94c245c53d9b8e899366f702ae3596 source_ref=75fad555723fb0d9fdc38c5f729779434c0a4951 -->
## `compute_incremental_worklist(*, project_root: Path, config: Config, store: Store) -> IncrementalWorklist`

Scan, check, and cascade to produce a read-only preview of files `run_incremental` would touch.

- Does not delete orphan triefacts or invoke the LLM.
- Excludes stale entries whose source file no longer exists (treated as orphans).
- `orphan_triefacts` in result: caller decides whether to delete or just report.
- Populates `regen_qnames_by_file`: per-file set of qualified names needing regeneration.
- Files with no triefact (`MISSING_TRIEFACT`) are omitted from the map, signalling full-file regen.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/incremental:run_incremental fingerprint=4f4334832b6715ee217168385cf25f369872022f8b2bc4bc7fcde9c19db2c193 body_fp=46856a693c3caddea1815d5ab8117beb6a1f6ceda15db64addcb072148ac2e01 source_ref=75fad555723fb0d9fdc38c5f729779434c0a4951 -->
## `run_incremental(*, project_root: Path, config: Config, store: Store, client: ModelClient, pricing: ModelPricing | None = None, budget_usd: float | None = None, limit: int | None = None, progress: ProgressCallback | None = None) -> IncrementalResult`

Refresh triefacts for stale source files and their cascade of dependents, then remove orphan triefacts.

- `budget_usd`: stop syncing new files once cumulative cost meets or exceeds this value.
- `limit`: stop after this many files have been successfully synced.
- `pricing`: if `None`, cost tracking is disabled and `actual_cost_usd` is 0.
- `progress`: defaults to `NULL_PROGRESS` (no-op) when omitted.
- Passes `symbols_to_regen` from `worklist.regen_qnames_by_file` to `sync_single_file`; absent entry means full-file regen, present entry restricts the LLM to those qualified names.
- Files with no symbols and no removed sections and no skipped symbols are counted in `files_skipped_no_symbols`, not `files_synced`.
- Directly-stale files are synced before cascade-pulled files; cascade files are ordered by hop distance ascending.
<!-- trie:end -->