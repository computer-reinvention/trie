---
trie_version: 0.1.2
source: trie/sync/progress.py
file_fingerprint: 9d32e2b8cd47ef1fc2895a61b413751e82e465eef96ca2f9b143ec43ebc0075e
last_synced_at: '2026-05-19T10:42:09Z'
defines:
- kind: module
  qualified_name: trie/sync/progress:__module__
  lines: 1-36
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
- kind: class
  qualified_name: trie/sync/progress:_NullProgress
  lines: 24-32
- kind: method
  qualified_name: trie/sync/progress:_NullProgress.on_start
  lines: 25-26
- kind: method
  qualified_name: trie/sync/progress:_NullProgress.on_done
  lines: 28-29
- kind: method
  qualified_name: trie/sync/progress:_NullProgress.on_skip
  lines: 31-32
- kind: constant
  qualified_name: trie/sync/progress:NULL_PROGRESS
  lines: 35-35
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

<!-- trie:section symbol=trie/sync/progress:_NullProgress fingerprint=f1dc526d0962ddb43c7b0076178c5845f35929a2730c41265e44450eedfc1711 body_fp=f643baf72871e3943de0e6ffacc7b09cd3a39b7a6b60f48305e3f190532ded50 source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
## `_NullProgress`

No-op implementation of `ProgressCallback` that silently discards all progress events.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/progress:_NullProgress.on_start fingerprint=9f730a1a70a6144b0dc8da4942d9093cd268d625eafac5188775d0d6b8b25f08 body_fp=df8d60ae1665e6dff707e676c24a9d6bb92a06a31e9c3673af5505b716c14d26 source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
## `on_start(self, rel_path: str, idx: int, total: int) -> None`

No-op implementation of `ProgressCallback.on_start`.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/progress:_NullProgress.on_done fingerprint=9f730a1a70a6144b0dc8da4942d9093cd268d625eafac5188775d0d6b8b25f08 body_fp=e16c73e5e8f9b54d3462a0892b96e891f8d8cbc62bc8e21cd1f7461ebb733df2 source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
## `on_done(self, rel_path: str, result: FileSyncResult, running_cost_usd: float) -> None`

No-op implementation of the `on_done` progress hook.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/progress:_NullProgress.on_skip fingerprint=9f730a1a70a6144b0dc8da4942d9093cd268d625eafac5188775d0d6b8b25f08 body_fp=9c1631e45d6d8da254887f84e691acd36a1e8a4cb93913ede3fbbd70e56a7749 source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
## `on_skip(self, rel_path: str, reason: str) -> None`

No-op implementation of the skip callback; does nothing.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/progress:NULL_PROGRESS fingerprint=f5526a45db3aeafec3262f11b51138473623ea67b987dab1455047e759350b0c body_fp=19d81d4eb713c1fed58e120e1f3325a1bf8aaaec5f9b8f12533bc104e9fa776e source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
## `NULL_PROGRESS: ProgressCallback`

No-op `ProgressCallback` singleton; use when progress reporting is unwanted.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/progress:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=c79bd13d935ba8fa1b4f74b3b1f2dbf9d3a14a33235d09262cde1b8bb6196e6f source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
## `progress`

Define the `ProgressCallback` protocol and a no-op implementation for per-file sync progress hooks.

- `ProgressCallback`: runtime-checkable protocol; implement to receive sync lifecycle events.
- `NULL_PROGRESS`: singleton no-op instance satisfying `ProgressCallback`; use as default.
<!-- trie:end -->