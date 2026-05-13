---
trie_version: 0.1.0
source: trie/sync/progress.py
file_fingerprint: 9d32e2b8cd47ef1fc2895a61b413751e82e465eef96ca2f9b143ec43ebc0075e
last_synced_at: '2026-05-12T18:35:12Z'
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
<!-- trie:section symbol=trie/sync/progress:ProgressCallback fingerprint=0b8f3db623407572155daf2d39a483cab860bb0fa13d151dc56ec6de0b7d7a66 body_fp=91482ceb95a1ed0185c311026182b9fa522fed609cdae3a2d55c0c605408ed1b -->
## `class ProgressCallback(Protocol)`

Runtime-checkable protocol defining per-file progress hooks for multi-file sync runs.

- `on_start`: called before each file; `idx` is 1-based position among `total`.
- `on_done`: called after a file syncs; `running_cost_usd` is cumulative spend so far.
- `on_skip`: called when a file is skipped; `reason` is a human-readable explanation.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/progress:ProgressCallback.on_start fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=6aacf22d0d6665c1d8b88602822c6ac28daf455f5f5adda2cd851e5e52d46fb1 -->
## `on_start(self, rel_path: str, idx: int, total: int) -> None`

Called before syncing a single file begins.

- `idx`: 1-based position of the file in the current run.
- `total`: total number of files in the current run.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/progress:ProgressCallback.on_done fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=3f9165975c152e8e8b30e0198b6e58025db38d45e9fa3483736d7c1b1e0c3abb -->
## `on_done(self, rel_path: str, result: FileSyncResult, running_cost_usd: float) -> None`

Called after a file sync completes, reporting its result and cumulative cost.

- `running_cost_usd`: total USD spent across all files processed so far.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/progress:ProgressCallback.on_skip fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=b1666b5d80738393e42d078c663c4fc5aaab2e844c6bb563112a76b6476e9576 -->
## `on_skip(self, rel_path: str, reason: str) -> None`

Called after a file is skipped, supplying the relative path and the reason it was not synced.
<!-- trie:end -->