---
trie_version: 0.3.0
source: trie/sync/progress.py
file_fingerprint: af06a9fa87b258c20e0c29188a165c54a315ce135458a0ddb79aa94637335d99
last_synced_at: '2026-08-02T21:19:48Z'
defines:
- kind: module
  qualified_name: trie/sync/progress:__module__
  lines: 1-59
- kind: class
  qualified_name: trie/sync/progress:ProgressCallback
  lines: 9-25
  signature: class ProgressCallback(Protocol)
- kind: method
  qualified_name: trie/sync/progress:ProgressCallback.on_start
  lines: 21-21
  signature: 'def on_start(self, rel_path: str, idx: int, total: int, *, cascade: bool = False) -> None'
- kind: method
  qualified_name: trie/sync/progress:ProgressCallback.on_done
  lines: 23-23
  signature: 'def on_done(self, rel_path: str, result: FileSyncResult, running_cost_usd: float) -> None'
- kind: method
  qualified_name: trie/sync/progress:ProgressCallback.on_skip
  lines: 25-25
  signature: 'def on_skip(self, rel_path: str, reason: str) -> None'
- kind: function
  qualified_name: trie/sync/progress:emit_plan
  lines: 28-35
  signature: 'def emit_plan(cb: object, *, direct: int, cascade: int) -> None'
- kind: function
  qualified_name: trie/sync/progress:emit_section
  lines: 38-44
  signature: 'def emit_section(cb: object, *, label: str, count: int) -> None'
- kind: class
  qualified_name: trie/sync/progress:_NullProgress
  lines: 47-55
  signature: class _NullProgress
- kind: method
  qualified_name: trie/sync/progress:_NullProgress.on_start
  lines: 48-49
  signature: 'def on_start(self, rel_path: str, idx: int, total: int, *, cascade: bool = False) -> None'
- kind: method
  qualified_name: trie/sync/progress:_NullProgress.on_done
  lines: 51-52
  signature: 'def on_done(self, rel_path: str, result: FileSyncResult, running_cost_usd: float) -> None'
- kind: method
  qualified_name: trie/sync/progress:_NullProgress.on_skip
  lines: 54-55
  signature: 'def on_skip(self, rel_path: str, reason: str) -> None'
- kind: constant
  qualified_name: trie/sync/progress:NULL_PROGRESS
  lines: 58-58
incoming_refs: 23
outgoing_refs: 2
---
<!-- trie:section symbol=trie/sync/progress:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=c71d9fe7237248e128d2026a25d1658c47c4d3d80cbd892b8a7c97998f66b3ac source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d role=documentation-sync -->
Defines progress callback protocols and implementations for multi-file sync operations.

- `ProgressCallback`: Protocol for streaming per-file progress events during sync runs
- `_NullProgress`: No-op implementation that discards all progress events
- `NULL_PROGRESS`: Singleton null progress callback instance
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:ProgressCallback fingerprint=3d285461cb48d343efd4ae7f2b8bc480bb8761755c142df0de8edaf4288a7184 body_fp=2a34ff4601b24dc4811ca699c5ace2fa64c0c073fedd5f6b93d584709127b04b source_ref=824af364261107be2123a388ec334677a577a1c8 role=model -->
## `class ProgressCallback(Protocol)`

Protocol for reporting per-file progress during multi-file sync operations.

- `on_start`: Called before processing each file with path, index, total count, and cascade flag
- `on_done`: Called after successful file processing with path, result, and running cost
- `on_skip`: Called when a file is skipped with path and reason
- Optional hooks `on_plan` and `on_section` can be implemented for additional progress reporting
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:ProgressCallback.on_start fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=eeee7de013ecf0c5d3a560dad06dd0da60fa12d554990830f17bd71cc9ca430b source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d role=monitoring-telemetry -->
## `def on_start(self, rel_path: str, idx: int, total: int, *, cascade: bool = False) -> None`

ProgressCallback method called when sync starts processing a file.

- `idx`: Zero-based position of this file in the sync batch
- `total`: Total number of files to be processed in the batch
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:ProgressCallback.on_done fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=6968ed247100233f0c722eac4317522a80069a4738df424cd0dca81b1441721f source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d role=documentation-sync -->
## `def on_done(self, rel_path: str, result: FileSyncResult, running_cost_usd: float) -> None`

ProgressCallback method called when a file sync operation completes successfully.

- `running_cost_usd`: cumulative cost across all files processed so far
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:ProgressCallback.on_skip fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=490252ba0c2db62d027bd9d8f9c6d1739311ab55af8e86717c5434108f4e5cac source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d role=documentation-sync -->
## `def on_skip(self, rel_path: str, reason: str) -> None`

Notifies ProgressCallback that a file was skipped during sync with an explanatory reason.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:emit_plan fingerprint=40910333b719ce4de8f3db067d3d25c3351e45e21bb1a95c6f34d15339a3327f body_fp=7fe9eb7d9bfbd25960aab02d985b1ca72988b08992b04130aae43b9fcdd68f4c source_ref=824af364261107be2123a388ec334677a577a1c8 role=util -->
## `def emit_plan(cb: object, *, direct: int, cascade: int) -> None`

Safely invokes the optional `on_plan` hook on a callback object with file count information.

- `cb`: callback object, may or may not implement `on_plan` method
- `direct`: number of directly stale files to be processed
- `cascade`: number of cascade files to be processed
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:emit_section fingerprint=c06dc88dc569c9a39be4360b0737496757afbf71942cea088921f07b7d0efb8c body_fp=467b05a54cce2d6012793bfdcbd5711979d0da6281d8fad5f53ec2a77a2c4a29 source_ref=824af364261107be2123a388ec334677a577a1c8 role=util -->
## `def emit_section(cb: object, *, label: str, count: int) -> None`

Calls `on_section` on the callback if it exists to announce a new group of files.

- `cb`: Callback object that may implement `on_section`
- `label`: Description of the file group (e.g. "directly stale")
- `count`: Number of files in this group
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:_NullProgress fingerprint=2b8f552f563eb38a278c024c0bd729ed93d6c349b8f63bcd16eb664b256f55bb body_fp=ac23b4bad6f1e2cbb9f1011319d249f6930c0abe228cda59b5a151d5548cda49 source_ref=824af364261107be2123a388ec334677a577a1c8 role=model -->
## `class _NullProgress`

No-op implementation of ProgressCallback that silently ignores all progress events.

- Used as default callback when no progress reporting is needed
- All methods return None without side effects
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:_NullProgress.on_start fingerprint=9f730a1a70a6144b0dc8da4942d9093cd268d625eafac5188775d0d6b8b25f08 body_fp=9475a8d827bfa403594bad6fc6fc6be3bd7fbffa92e916c2fee3e4c7abc0ca17 source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d role=documentation-sync -->
## `def on_start(self, rel_path: str, idx: int, total: int, *, cascade: bool = False) -> None`

_NullProgress.on_start does nothing when a file sync starts, providing a no-op implementation of the ProgressCallback protocol.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:_NullProgress.on_done fingerprint=9f730a1a70a6144b0dc8da4942d9093cd268d625eafac5188775d0d6b8b25f08 body_fp=a998a6f2509478522812904f0dc11a3f8121f0e56c7a8a3c3ce699590cca370b source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d role=documentation-sync -->
## `def on_done(self, rel_path: str, result: FileSyncResult, running_cost_usd: float) -> None`

_NullProgress.on_done method that does nothing when a file sync completes.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:_NullProgress.on_skip fingerprint=9f730a1a70a6144b0dc8da4942d9093cd268d625eafac5188775d0d6b8b25f08 body_fp=078b3d64c60631bc0b065e64e13950c79fe97a6760ad027a21631191e872557a source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d role=documentation-sync -->
## `def on_skip(self, rel_path: str, reason: str) -> None`

_NullProgress.on_skip implements the ProgressCallback protocol with a no-op that returns None.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/progress:NULL_PROGRESS fingerprint=f5526a45db3aeafec3262f11b51138473623ea67b987dab1455047e759350b0c body_fp=ef7277f76423dcc2f08c29ae9794365eb66764b0bb04d769b1ad14e20d3bbf74 source_ref=3711cd8c6acb475bbd3b2400719e537dec17211d role=documentation-sync -->
Singleton instance of `_NullProgress` that provides a no-op implementation of `ProgressCallback`.
<!-- trie:end -->