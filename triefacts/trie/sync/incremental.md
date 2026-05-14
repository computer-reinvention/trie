---
trie_version: 0.1.0
source: trie/sync/incremental.py
file_fingerprint: bad2de2ee56a1e9fe1a37eb2a5b144587629f8bf8b45150581a077f5da9dd3b8
last_synced_at: '2026-05-14T17:28:35Z'
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
  lines: 95-193
incoming_refs: 14
outgoing_refs: 9
---
<!-- trie:section symbol=trie/sync/incremental:IncrementalWorklist fingerprint=612b09824da967027fa1ef2e5eecde2e7f8e7f1e16a554538c49f86b588aa911 body_fp=53b07e0034bb235ee009730ffaca7b89c825c7d8c8b8bb1fca8b561049a37772 -->
## `IncrementalWorklist`

Read-only preview of files `run_incremental` would touch, produced by `compute_incremental_worklist`.

- `affected_files`: union of directly stale and cascaded files
- `directly_stale`: files whose triefacts are outdated relative to source
- `cascaded_files`: files added via cascade from stale symbols
- `orphan_triefacts`: triefact paths whose source file no longer exists
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/incremental:IncrementalResult fingerprint=44d8d13db810a81ea27f75709b870895913876f1c8dbdc95aa93ed09cc9916cf body_fp=b49bc25b9d804956c5a7fcd787dd9f1a48c73b09ae3722cc31f648f70df2214a -->
## `IncrementalResult`

Frozen dataclass holding aggregated statistics from a completed `run_incremental` call.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/incremental:compute_incremental_worklist fingerprint=b08baa6ed9200186afbab7173f99dbd4dc9915aca4e1de8b8900728330e16a92 body_fp=7f70aa5ced502b747fc8d8ae1f8b8fa78836661ed2c6cf398ce1c28356d3569d -->
## `compute_incremental_worklist(*, project_root: Path, config: Config, store: Store) -> IncrementalWorklist`

Run scan, check, and cascade to produce a read-only preview of files `run_incremental` would touch.

- Does **not** delete orphans or invoke the LLM.
- Excludes stale items whose source file no longer exists (treated as orphans).
- `orphan_triefacts`: triefact paths with no matching source; caller decides removal.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/incremental:run_incremental fingerprint=68fb4c3ca22993cce87020a4973923817f2841975a2c5241fea5d300e345e292 body_fp=3f77bd74d2c3c7be7ca05c1a68103766a9385b6c7b83c526f848872c472197a4 -->
## `run_incremental(*, project_root: Path, config: Config, store: Store, client: ModelClient, pricing: ModelPricing | None = None, budget_usd: float | None = None, limit: int | None = None, progress: ProgressCallback | None = None) -> IncrementalResult`

Refresh stale triefacts and their cascade, deleting orphans and invoking the LLM per affected file.

- `budget_usd`: stops queuing new files once cumulative cost meets or exceeds this value.
- `limit`: stops queuing new files once this many have been successfully synced.
- `pricing`: if `None`, cost tracking is skipped and `actual_cost_usd` stays `0.0`.
- `progress`: uses `NULL_PROGRESS` when omitted; no-op safe.
<!-- trie:end -->