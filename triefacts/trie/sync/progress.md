---
trie_version: 0.1.0
source: trie/sync/progress.py
file_fingerprint: 9d32e2b8cd47ef1fc2895a61b413751e82e465eef96ca2f9b143ec43ebc0075e
last_synced_at: '2026-05-14T19:45:12Z'
defines:
- kind: class
  qualified_name: trie/sync/progress:ProgressCallback
  lines: 9-21
- kind: method
  qualified_name: trie/sync/progress:ProgressCallback.on_start
  lines: 17-17
- kind: method
  qualified_name: trie/sync/progress:ProgressCallback.on_done
  lines: 19-19
- kind: method
  qualified_name: trie/sync/progress:ProgressCallback.on_skip
  lines: 21-21
incoming_refs: 3
outgoing_refs: 2
---
<!-- trie:section symbol=trie/sync/progress:ProgressCallback fingerprint=0b8f3db623407572155daf2d39a483cab860bb0fa13d151dc56ec6de0b7d7a66 body_fp=5ca601aac7404fb13825bd20b3e0a979344a1a503d6c332e184e949736ef97af source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
## `class ProgressCallback(Protocol)`

Runtime-checkable protocol defining per-file progress hooks for multi-file sync runs.

- `on_start`: called before each file is processed.
- `on_done`: called after sync completes; includes cumulative cost in USD.
- `on_skip`: called when a file is bypassed; includes human-readable reason.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/progress:ProgressCallback.on_start fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=19579d5f1ca5cd078b63dcf22df1421ce87dca2fbdc9c243f2e5fe069b1ed0b1 source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
## `on_start(self, rel_path: str, idx: int, total: int) -> None`

Called before processing a file begins during a multi-file sync run.

- `idx`: 1-based position of the file in the current batch.
- `total`: total number of files in the batch.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/progress:ProgressCallback.on_done fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=4f9e78fee88896bbab2a61d59c27e2105886ad232224f4dd5899c47bf6381d01 source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
## `on_done(self, rel_path: str, result: FileSyncResult, running_cost_usd: float) -> None`

Called after a file sync completes, reporting its result and cumulative cost.

- `running_cost_usd`: total USD spent across all files so far, not just this one.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/progress:ProgressCallback.on_skip fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=8d6a2ea246751a63712a099b20473cfaf0b00b2fb85768e42b37ad0f2a8af7f9 source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
## `on_skip(self, rel_path: str, reason: str) -> None`

Called when a file is skipped during a multi-file sync run.

- **`reason`**: human-readable explanation for why the file was skipped.
<!-- trie:end -->