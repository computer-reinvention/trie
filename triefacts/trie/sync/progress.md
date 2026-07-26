---
trie_version: 0.1.9
source: trie/sync/progress.py
file_fingerprint: af06a9fa87b258c20e0c29188a165c54a315ce135458a0ddb79aa94637335d99
last_synced_at: '2026-07-26T20:28:55Z'
defines:
- kind: module
  qualified_name: trie/sync/progress:__module__
  lines: 1-59
- kind: class
  qualified_name: trie/sync/progress:ProgressCallback
  lines: 9-25
- kind: method
  qualified_name: trie/sync/progress:ProgressCallback.on_start
  lines: 21-21
- kind: method
  qualified_name: trie/sync/progress:ProgressCallback.on_done
  lines: 23-23
- kind: method
  qualified_name: trie/sync/progress:ProgressCallback.on_skip
  lines: 25-25
- kind: function
  qualified_name: trie/sync/progress:emit_plan
  lines: 28-35
- kind: function
  qualified_name: trie/sync/progress:emit_section
  lines: 38-44
- kind: class
  qualified_name: trie/sync/progress:_NullProgress
  lines: 47-55
- kind: method
  qualified_name: trie/sync/progress:_NullProgress.on_start
  lines: 48-49
- kind: method
  qualified_name: trie/sync/progress:_NullProgress.on_done
  lines: 51-52
- kind: method
  qualified_name: trie/sync/progress:_NullProgress.on_skip
  lines: 54-55
- kind: constant
  qualified_name: trie/sync/progress:NULL_PROGRESS
  lines: 58-58
incoming_refs: 14
outgoing_refs: 2
---
<!-- trie:section symbol=trie/sync/progress:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=c71d9fe7237248e128d2026a25d1658c47c4d3d80cbd892b8a7c97998f66b3ac source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d role=documentation-sync -->
Defines progress callback protocols and implementations for multi-file sync operations.

- `ProgressCallback`: Protocol for streaming per-file progress events during sync runs
- `_NullProgress`: No-op implementation that discards all progress events
- `NULL_PROGRESS`: Singleton null progress callback instance
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:ProgressCallback fingerprint=3d285461cb48d343efd4ae7f2b8bc480bb8761755c142df0de8edaf4288a7184 body_fp=9334da25b6244a3106c68750de2e6848ece9ac0a792f2e6c1b64bb30898ad69f source_ref=824af364261107be2123a388ec334677a577a1c8 role=model -->
Protocol for reporting per-file progress during multi-file sync operations.

- `on_start`: Called before processing each file with path, index, total count, and cascade flag
- `on_done`: Called after successful file processing with path, result, and running cost
- `on_skip`: Called when a file is skipped with path and reason
- Optional hooks `on_plan` and `on_section` can be implemented for additional progress reporting
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:ProgressCallback.on_start fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=2668b19fdd87458fb44b4c04e2ac9cc106efdbf8b6e6ac8de8c8764faf638463 source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d role=monitoring-telemetry -->
ProgressCallback method called when sync starts processing a file.

- `idx`: Zero-based position of this file in the sync batch
- `total`: Total number of files to be processed in the batch
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:ProgressCallback.on_done fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=a59e88a20c208baf3371b113b86df86eccf6fad42f9ed2f86dc555356585fc62 source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d role=documentation-sync -->
ProgressCallback method called when a file sync operation completes successfully.

- `running_cost_usd`: cumulative cost across all files processed so far
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:ProgressCallback.on_skip fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=d74fa80f1f5a1170b4a0d33c2edd55e8b7d48f54acd89e978eff02af8f9a72fa source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d role=documentation-sync -->
Notifies ProgressCallback that a file was skipped during sync with an explanatory reason.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:emit_plan fingerprint=40910333b719ce4de8f3db067d3d25c3351e45e21bb1a95c6f34d15339a3327f body_fp=2932adc435cde3ded07c3e76caa19b999e0b8e21f06d6ad0d103bcfca49320f3 source_ref=824af364261107be2123a388ec334677a577a1c8 role=util -->
Safely invokes the optional `on_plan` hook on a callback object with file count information.

- `cb`: callback object, may or may not implement `on_plan` method
- `direct`: number of directly stale files to be processed
- `cascade`: number of cascade files to be processed
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:emit_section fingerprint=c06dc88dc569c9a39be4360b0737496757afbf71942cea088921f07b7d0efb8c body_fp=fc4324939747c9b96ecbee0ec1a07e74f6495ce38fea232e1d0fb997e1a84b9a source_ref=824af364261107be2123a388ec334677a577a1c8 role=util -->
Calls `on_section` on the callback if it exists to announce a new group of files.

- `cb`: Callback object that may implement `on_section`
- `label`: Description of the file group (e.g. "directly stale")
- `count`: Number of files in this group
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:_NullProgress fingerprint=2b8f552f563eb38a278c024c0bd729ed93d6c349b8f63bcd16eb664b256f55bb body_fp=046b5bd1ac91585406ea17fe6e4d2cdd7d8b78d481430814e80a2a5b61ff11eb source_ref=824af364261107be2123a388ec334677a577a1c8 role=model -->
No-op implementation of ProgressCallback that silently ignores all progress events.

- Used as default callback when no progress reporting is needed
- All methods return None without side effects
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:_NullProgress.on_start fingerprint=9f730a1a70a6144b0dc8da4942d9093cd268d625eafac5188775d0d6b8b25f08 body_fp=e092acc35db9f85278613cbe45375310aaf5c35a0c1c68f55f37c6c519b17502 source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d role=documentation-sync -->
_NullProgress.on_start does nothing when a file sync starts, providing a no-op implementation of the ProgressCallback protocol.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:_NullProgress.on_done fingerprint=9f730a1a70a6144b0dc8da4942d9093cd268d625eafac5188775d0d6b8b25f08 body_fp=0cff9c0a6f18ca67e77335f07491330d4804b992edd3c3e6980714303235eb72 source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d role=documentation-sync -->
_NullProgress.on_done method that does nothing when a file sync completes.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:_NullProgress.on_skip fingerprint=9f730a1a70a6144b0dc8da4942d9093cd268d625eafac5188775d0d6b8b25f08 body_fp=a971cd00b7510070747a4a0d841846db956d765825467b3928504a74574e467d source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d role=documentation-sync -->
_NullProgress.on_skip implements the ProgressCallback protocol with a no-op that returns None.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:NULL_PROGRESS fingerprint=f5526a45db3aeafec3262f11b51138473623ea67b987dab1455047e759350b0c body_fp=ef7277f76423dcc2f08c29ae9794365eb66764b0bb04d769b1ad14e20d3bbf74 source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d role=documentation-sync -->
Singleton instance of `_NullProgress` that provides a no-op implementation of `ProgressCallback`.
<!-- trie:end -->