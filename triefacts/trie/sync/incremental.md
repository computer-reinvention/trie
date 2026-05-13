---
trie_version: 0.1.0
source: trie/sync/incremental.py
file_fingerprint: bad2de2ee56a1e9fe1a37eb2a5b144587629f8bf8b45150581a077f5da9dd3b8
last_synced_at: '2026-05-12T18:32:01Z'
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
<!-- trie:section symbol=trie/sync/incremental:IncrementalWorklist fingerprint=612b09824da967027fa1ef2e5eecde2e7f8e7f1e16a554538c49f86b588aa911 body_fp=be453d893b49a0207a9fb9b19dfd344eea7851a216b9e6623495bdde6a04441a -->
## `IncrementalWorklist`

Read-only preview of files `run_incremental` would touch, produced by `compute_incremental_worklist`.

- `affected_files`: union of directly stale and cascaded files
- `directly_stale`: files whose triefacts are outdated relative to source
- `cascaded_files`: files transitively referencing a stale symbol
- `orphan_triefacts`: triefact paths whose source files no longer exist
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/incremental:IncrementalResult fingerprint=44d8d13db810a81ea27f75709b870895913876f1c8dbdc95aa93ed09cc9916cf body_fp=6984adb423c701d29a1316c0fd7c339031ef1b6e66c93fa3505c15d88269992e -->
## `IncrementalResult`

Frozen dataclass holding aggregate statistics from a completed `run_incremental` call.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/incremental:compute_incremental_worklist fingerprint=b08baa6ed9200186afbab7173f99dbd4dc9915aca4e1de8b8900728330e16a92 body_fp=c58c4b25f456b009d0936cea7ccc077a3c19bb75a88d424638ace539be297004 -->
## `compute_incremental_worklist(*, project_root: Path, config: Config, store: Store) -> IncrementalWorklist`

Run scan + check + cascade and return the file list `run_incremental` would touch, without mutating state or invoking the LLM.

- `orphan_triefacts`: triefacts whose source file no longer exists; returned for caller to act on.
- Stale items referencing non-existent source files are excluded from `directly_stale` and treated as orphans.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/incremental:run_incremental fingerprint=68fb4c3ca22993cce87020a4973923817f2841975a2c5241fea5d300e345e292 body_fp=28281d5719b6a614e4b64ff9cf4ff4f494a318e4957484a673113734ea6bd547 -->
## `run_incremental(*, project_root: Path, config: Config, store: Store, client: ModelClient, pricing: ModelPricing | None = None, budget_usd: float | None = None, limit: int | None = None, progress: ProgressCallback | None = None) -> IncrementalResult`

Refresh stale triefacts and their cascade, deleting orphans and invoking the LLM per affected file.

- `budget_usd`: stops scheduling new files once cumulative cost meets or exceeds this value.
- `limit`: stops scheduling new files once this many have been successfully synced.
- `pricing`: if `None`, cost tracking is skipped and `actual_cost_usd` remains `0.0`.
- `progress`: defaults to a no-op callback when `None`.
<!-- trie:end -->