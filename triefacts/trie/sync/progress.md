---
trie_version: 0.1.2
source: trie/sync/progress.py
file_fingerprint: 9d32e2b8cd47ef1fc2895a61b413751e82e465eef96ca2f9b143ec43ebc0075e
last_synced_at: '2026-05-24T00:25:28Z'
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
<!-- trie:section symbol=trie/sync/progress:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=9f208cb996d74b196fbe52e68b55fe07baf530fb0763756eb0eb9c19ad0f1244 source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
## `trie/sync/progress`

Define the `ProgressCallback` protocol and `NULL_PROGRESS` no-op singleton for per-file sync progress hooks.

- `ProgressCallback`: runtime-checkable protocol; implement to receive `on_start`, `on_done`, `on_skip` events.
- `NULL_PROGRESS`: drop-in no-op instance satisfying `ProgressCallback`; use when progress reporting is unwanted.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:ProgressCallback fingerprint=0b8f3db623407572155daf2d39a483cab860bb0fa13d151dc56ec6de0b7d7a66 body_fp=34b840ee249784fbe4a80e8984df8fe3502dd77a35def4e05fcc8a2fcecde091 source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
## `ProgressCallback`

Runtime-checkable protocol for receiving per-file progress events during multi-file sync runs.

- `on_start`: called before processing each file; `idx` is 1-based position in `total`
- `on_done`: called after successful sync; `running_cost_usd` is cumulative spend so far
- `on_skip`: called when a file is bypassed; `reason` explains why
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:ProgressCallback.on_start fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=e407c40006202c2f7422f1954468913b5ef0980d4ef3b51a00dbe01bc71d3004 source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
## `ProgressCallback.on_start(self, rel_path: str, idx: int, total: int) -> None`

Called by sync internals before processing each file in a multi-file run.

- `idx`: 1-based position of the current file
- `total`: total number of files in the run
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:ProgressCallback.on_done fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=e72bc863a3e87e7797ba409d9d127d7f197b7514b6070aef2fbd50848a951a53 source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
## `ProgressCallback.on_done(self, rel_path: str, result: FileSyncResult, running_cost_usd: float) -> None`

Called by sync internals after a file finishes processing.

- `running_cost_usd`: cumulative USD cost across all files processed so far.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:ProgressCallback.on_skip fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=f6ec62271b6f5d837b45b7fcb1e8194f4a977c7b1ff5816ccf394cfe1af50cad source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
## `ProgressCallback.on_skip(self, rel_path: str, reason: str) -> None`

Called by `ProgressCallback` sync internals after a file is skipped, passing the skip reason.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:_NullProgress fingerprint=f1dc526d0962ddb43c7b0076178c5845f35929a2730c41265e44450eedfc1711 body_fp=f643baf72871e3943de0e6ffacc7b09cd3a39b7a6b60f48305e3f190532ded50 source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
## `_NullProgress`

No-op implementation of `ProgressCallback` that silently discards all progress events.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:_NullProgress.on_start fingerprint=9f730a1a70a6144b0dc8da4942d9093cd268d625eafac5188775d0d6b8b25f08 body_fp=a82c97f4a17c62da94c6caabf77c5b7c13b011ed0fa7bc884d35eb2c909a546e source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
## `_NullProgress.on_start(self, rel_path: str, idx: int, total: int) -> None`

No-op implementation of `ProgressCallback.on_start` on `_NullProgress`.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:_NullProgress.on_done fingerprint=9f730a1a70a6144b0dc8da4942d9093cd268d625eafac5188775d0d6b8b25f08 body_fp=d888f99e41ad8d5474744ab41c55a4a24acd7940e75edbef4124b3eff05b8a88 source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
## `_NullProgress.on_done(self, rel_path: str, result: FileSyncResult, running_cost_usd: float) -> None`

No-op implementation of `ProgressCallback.on_done` on `_NullProgress`.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:_NullProgress.on_skip fingerprint=9f730a1a70a6144b0dc8da4942d9093cd268d625eafac5188775d0d6b8b25f08 body_fp=e1ac1e5d038896236079e88a7fa57c52000e9d76b7860dcf45ab66b751bf0cc5 source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
## `_NullProgress.on_skip(self, rel_path: str, reason: str) -> None`

No-op implementation of `ProgressCallback.on_skip` on `_NullProgress`.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:NULL_PROGRESS fingerprint=f5526a45db3aeafec3262f11b51138473623ea67b987dab1455047e759350b0c body_fp=8a5d0611d9f0ed03b67c30b6b24669ba7ec375ab8c3778cc773b02d7f8c3af89 source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
## `NULL_PROGRESS: ProgressCallback`

No-op `ProgressCallback` singleton whose methods silently discard all arguments.
<!-- trie:end -->