---
trie_version: 0.1.5
source: trie/sync/progress.py
file_fingerprint: 9d32e2b8cd47ef1fc2895a61b413751e82e465eef96ca2f9b143ec43ebc0075e
last_synced_at: '2026-06-03T21:16:15Z'
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
incoming_refs: 6
outgoing_refs: 2
---
<!-- trie:section symbol=trie/sync/progress:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=c71d9fe7237248e128d2026a25d1658c47c4d3d80cbd892b8a7c97998f66b3ac source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
Defines progress callback protocols and implementations for multi-file sync operations.

- `ProgressCallback`: Protocol for streaming per-file progress events during sync runs
- `_NullProgress`: No-op implementation that discards all progress events
- `NULL_PROGRESS`: Singleton null progress callback instance
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:ProgressCallback fingerprint=0b8f3db623407572155daf2d39a483cab860bb0fa13d151dc56ec6de0b7d7a66 body_fp=30b89f3f9e573ac61818f428e5fb7ca7322a915ff0b4d290fb2951a957be3e2a source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
Defines protocol for receiving per-file progress events during multi-file sync operations.

- `on_start`: called before processing each file with path, index, and total count
- `on_done`: called after successful file processing with result and cost
- `on_skip`: called when file is skipped with reason
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:ProgressCallback.on_start fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=2668b19fdd87458fb44b4c04e2ac9cc106efdbf8b6e6ac8de8c8764faf638463 source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
ProgressCallback method called when sync starts processing a file.

- `idx`: Zero-based position of this file in the sync batch
- `total`: Total number of files to be processed in the batch
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:ProgressCallback.on_done fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=a59e88a20c208baf3371b113b86df86eccf6fad42f9ed2f86dc555356585fc62 source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
ProgressCallback method called when a file sync operation completes successfully.

- `running_cost_usd`: cumulative cost across all files processed so far
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:ProgressCallback.on_skip fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=d74fa80f1f5a1170b4a0d33c2edd55e8b7d48f54acd89e978eff02af8f9a72fa source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
Notifies ProgressCallback that a file was skipped during sync with an explanatory reason.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:_NullProgress fingerprint=f1dc526d0962ddb43c7b0076178c5845f35929a2730c41265e44450eedfc1711 body_fp=1d6c4b7964671a4dc4368ffd473d7b4dec866f1adac831df6e6684e0ccb70310 source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
No-op implementation of ProgressCallback that ignores all sync progress events.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:_NullProgress.on_start fingerprint=9f730a1a70a6144b0dc8da4942d9093cd268d625eafac5188775d0d6b8b25f08 body_fp=e092acc35db9f85278613cbe45375310aaf5c35a0c1c68f55f37c6c519b17502 source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
_NullProgress.on_start does nothing when a file sync starts, providing a no-op implementation of the ProgressCallback protocol.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:_NullProgress.on_done fingerprint=9f730a1a70a6144b0dc8da4942d9093cd268d625eafac5188775d0d6b8b25f08 body_fp=0cff9c0a6f18ca67e77335f07491330d4804b992edd3c3e6980714303235eb72 source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
_NullProgress.on_done method that does nothing when a file sync completes.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:_NullProgress.on_skip fingerprint=9f730a1a70a6144b0dc8da4942d9093cd268d625eafac5188775d0d6b8b25f08 body_fp=a971cd00b7510070747a4a0d841846db956d765825467b3928504a74574e467d source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
_NullProgress.on_skip implements the ProgressCallback protocol with a no-op that returns None.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:NULL_PROGRESS fingerprint=f5526a45db3aeafec3262f11b51138473623ea67b987dab1455047e759350b0c body_fp=ef7277f76423dcc2f08c29ae9794365eb66764b0bb04d769b1ad14e20d3bbf74 source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d -->
Singleton instance of `_NullProgress` that provides a no-op implementation of `ProgressCallback`.
<!-- trie:end -->