---
trie_version: 0.1.0
source: trie/sync/progress.py
file_fingerprint: 9d32e2b8cd47ef1fc2895a61b413751e82e465eef96ca2f9b143ec43ebc0075e
last_synced_at: '2026-05-14T18:33:24Z'
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
<!-- trie:section symbol=trie/sync/progress:ProgressCallback fingerprint=0b8f3db623407572155daf2d39a483cab860bb0fa13d151dc56ec6de0b7d7a66 body_fp=e5af2a42616d943a2c760ebbb38110b690f5ef426e36b4da10c7fc6011159a99 -->
## `ProgressCallback`

Runtime-checkable protocol defining per-file progress hooks for multi-file sync runs.

- `on_start`: called before each file begins syncing.
- `on_done`: called after a file syncs; receives result and cumulative cost.
- `on_skip`: called when a file is skipped; receives human-readable reason.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/progress:ProgressCallback.on_start fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=8c4da404042776233f8968c2e69baf8d79b8df020ea1368ea81446b10bef9456 -->
## `on_start(self, rel_path: str, idx: int, total: int) -> None`

Called before processing a file begins in a multi-file sync run.

- `idx`: 1-based or 0-based position of the file in the batch.
- `total`: total number of files in the batch.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/progress:ProgressCallback.on_done fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=3f9165975c152e8e8b30e0198b6e58025db38d45e9fa3483736d7c1b1e0c3abb -->
## `on_done(self, rel_path: str, result: FileSyncResult, running_cost_usd: float) -> None`

Called after a file sync completes, reporting its result and cumulative cost.

- `running_cost_usd`: total USD spent across all files processed so far.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/progress:ProgressCallback.on_skip fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=cad2c5687c12113ff9eb334a02ac6ec028558a8ddd2d2cf5ba6ecc1764288abd -->
## `on_skip(self, rel_path: str, reason: str) -> None`

Called after a file is skipped during a multi-file sync run.

- `reason`: human-readable explanation for why the file was skipped.
<!-- trie:end -->