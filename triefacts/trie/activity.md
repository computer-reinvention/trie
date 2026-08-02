---
trie_version: 0.3.0
source: trie/activity.py
file_fingerprint: 84b0d12203b4721c535e71aa2fd6c389c02f71d036e173f9b81b1ef9e5cc3840
last_synced_at: '2026-07-26T20:27:48Z'
description: Ephemeral local activity state for trie, backed by SQLite.
defines:
- kind: module
  qualified_name: trie/activity:__module__
  lines: 1-405
- kind: constant
  qualified_name: trie/activity:DB_FILENAME
  lines: 39-39
- kind: constant
  qualified_name: trie/activity:_SCHEMA
  lines: 41-63
- kind: function
  qualified_name: trie/activity:db_path
  lines: 66-67
  signature: 'def db_path(project_root: Path) -> Path'
- kind: function
  qualified_name: trie/activity:_connect
  lines: 71-86
  signature: 'def _connect(project_root: Path) -> Iterator[sqlite3.Connection]'
- kind: function
  qualified_name: trie/activity:get_meta
  lines: 94-104
  signature: 'def get_meta(project_root: Path, key: str) -> str | None'
- kind: function
  qualified_name: trie/activity:set_meta
  lines: 107-113
  signature: 'def set_meta(project_root: Path, key: str, value: str) -> None'
- kind: function
  qualified_name: trie/activity:clear_meta
  lines: 116-122
  signature: 'def clear_meta(project_root: Path, key: str) -> None'
- kind: class
  qualified_name: trie/activity:Pending
  lines: 131-138
  signature: class Pending
- kind: method
  qualified_name: trie/activity:Pending.count
  lines: 137-138
  signature: def count(self) -> int
- kind: function
  qualified_name: trie/activity:write_pending
  lines: 141-155
  signature: 'def write_pending(project_root: Path, *, stale: list[str], head: str) -> None'
- kind: function
  qualified_name: trie/activity:read_pending
  lines: 158-181
  signature: 'def read_pending(project_root: Path) -> Pending | None'
- kind: function
  qualified_name: trie/activity:clear_pending
  lines: 184-191
  signature: 'def clear_pending(project_root: Path, *, synced: list[str], head: str) -> None'
- kind: class
  qualified_name: trie/activity:Status
  lines: 200-213
  signature: class Status
- kind: method
  qualified_name: trie/activity:Status.is_active
  lines: 212-213
  signature: def is_active(self) -> bool
- kind: function
  qualified_name: trie/activity:_pid_alive
  lines: 216-227
  signature: 'def _pid_alive(pid: int) -> bool'
- kind: function
  qualified_name: trie/activity:read_status
  lines: 230-261
  signature: 'def read_status(project_root: Path) -> Status'
- kind: class
  qualified_name: trie/activity:ActivityWriter
  lines: 269-350
  signature: class ActivityWriter
- kind: method
  qualified_name: trie/activity:ActivityWriter.__init__
  lines: 278-289
  signature: 'def __init__(self, project_root: Path, op: str) -> None'
- kind: method
  qualified_name: trie/activity:ActivityWriter.__enter__
  lines: 291-293
  signature: def __enter__(self) -> ActivityWriter
- kind: method
  qualified_name: trie/activity:ActivityWriter.__exit__
  lines: 295-299
  signature: 'def __exit__(self, exc_type, exc, tb) -> None: # type: ignore[no-untyped-def]'
- kind: method
  qualified_name: trie/activity:ActivityWriter.set_total
  lines: 301-303
  signature: 'def set_total(self, total: int) -> None'
- kind: method
  qualified_name: trie/activity:ActivityWriter.file_start
  lines: 305-307
  signature: 'def file_start(self, rel_path: str, idx: int, total: int) -> None'
- kind: method
  qualified_name: trie/activity:ActivityWriter.file_done
  lines: 309-311
  signature: 'def file_done(self, rel_path: str, *, symbols: int = 0, cost_usd: float = 0.0) -> None'
- kind: method
  qualified_name: trie/activity:ActivityWriter.file_skip
  lines: 313-315
  signature: 'def file_skip(self, rel_path: str, reason: str) -> None'
- kind: method
  qualified_name: trie/activity:ActivityWriter._write
  lines: 317-350
  signature: 'def _write( self, *, state: str, current_file: str | None, op: str | None = None, error: str | None = None, ) -> None'
- kind: function
  qualified_name: trie/activity:activity_writer
  lines: 354-358
  signature: 'def activity_writer(project_root: Path, op: str) -> Iterator[ActivityWriter]'
- kind: class
  qualified_name: trie/activity:ActivityProgress
  lines: 368-404
  signature: class ActivityProgress
- kind: method
  qualified_name: trie/activity:ActivityProgress.__init__
  lines: 375-377
  signature: 'def __init__(self, writer: ActivityWriter, inner: object | None = None) -> None'
- kind: method
  qualified_name: trie/activity:ActivityProgress.on_plan
  lines: 379-383
  signature: 'def on_plan(self, *, direct: int, cascade: int) -> None: # Purely informational; mirror to the inner host callback if it cares.'
- kind: method
  qualified_name: trie/activity:ActivityProgress.on_section
  lines: 385-388
  signature: 'def on_section(self, *, label: str, count: int) -> None'
- kind: method
  qualified_name: trie/activity:ActivityProgress.on_start
  lines: 390-393
  signature: 'def on_start(self, rel_path: str, idx: int, total: int, *, cascade: bool = False) -> None'
- kind: method
  qualified_name: trie/activity:ActivityProgress.on_done
  lines: 395-399
  signature: 'def on_done(self, rel_path: str, result: object, running_cost_usd: float) -> None'
- kind: method
  qualified_name: trie/activity:ActivityProgress.on_skip
  lines: 401-404
  signature: 'def on_skip(self, rel_path: str, reason: str) -> None'
incoming_refs: 43
outgoing_refs: 0
---
<!-- trie:section symbol=trie/activity:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=14c1d957e81320f2a43c5f5cc90535b8747974f04adac72d17bd69ae06b4cddc source_ref=2f462a970066470f2a553a12b94d8ecdc7c9d2d9 role=persistence -->
Manages git-like on-disk state files under `.trie/` for coordination between independent trie processes.

- **pending.json**: tracks which triefacts are stale relative to source code
- **status.json**: records current writer process state and progress
- **activity.jsonl**: append-only event feed for live progress monitoring
- All writes use atomic temp-file-and-replace to prevent torn reads
- Activity feed is size-capped and rotated to prevent unbounded growth
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:DB_FILENAME fingerprint=1fad14c6b9558034a22e1fd6dd37514b8a6fe250d13371425abc8f08222f68f5 body_fp=b719450b8f3b3266cb234947fba99caee68901ed2bc44afe840e56a1c5e6b181 source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=config -->
Filename for the ephemeral SQLite database storing trie's runtime state.
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:_SCHEMA fingerprint=76717dadaa2d43a10390b56077e4a3f6a06b8304c5e8c0779c32ded542a0045f body_fp=aee85dcb0ea989bbdd788cbd8684125c733440f402ad272118619d16f4249c20 source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=persistence -->
SQLite schema creating three tables for ephemeral trie activity state.

- `status` — single-row table tracking active writer state (state, op, pid, file progress)
- `pending` — tracks stale source files needing regeneration (source_path, head, computed_at)  
- `meta` — key-value store for markers distinguishing computed-empty from never-computed states
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:db_path fingerprint=23fb5be98a9ec4515c2044254a25da56fe69f828f8d48f301452ebf9bb01a100 body_fp=32f1a1c00bb9af28b9115388c4c372695054075e50178d829a8f5521ffc3c0f3 source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=util -->
## `def db_path(project_root: Path) -> Path`

Returns the path to the activity database file within the project's .trie directory.
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:_connect fingerprint=b537be28250ba75a498addd6d084740480b373fe68dc93dc0179375ad3b43f0a body_fp=22f2fcd525cf6f0ea9dbe1f7c6c662f563aacbd9728de1fd7cb5de9c3a702f3e source_ref=159836de03874c9d962e001a7754ae78f6e97e63 role=persistence -->
## `def _connect(project_root: Path) -> Iterator[sqlite3.Connection]`

Opens ephemeral SQLite activity database with WAL journaling and schema initialization.

- Creates `.trie` directory and database file if missing
- Enables WAL mode for concurrent reads during writes
- Sets 5-second timeout for lock contention retry
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:get_meta fingerprint=5c53113e190974614145cfefe536cf4b846e5757523fd0ed9a332e79d6b25bdd body_fp=423734a24c18b417818091701609dd102d7bf0972aa3d1dd7fdfbfe8156cfc0d source_ref=c4c8fffb97eb7849d22babb462a59d2b2ab0f821 role=persistence -->
## `def get_meta(project_root: Path, key: str) -> str | None`

Retrieves a meta value by key from the activity database, returning None if the key or database doesn't exist.
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:set_meta fingerprint=694baf44dfba103017e8753ccdb569fbbb04c22b1c8546a1e7d5655832f5d9c3 body_fp=5d4b0df599df812a3f91ca18197c2542985d958a18746769ba5f4836ca14ad9c source_ref=c4c8fffb97eb7849d22babb462a59d2b2ab0f821 role=persistence -->
## `def set_meta(project_root: Path, key: str, value: str) -> None`

Upserts a meta key/value pair into the activity database, swallowing any SQLite errors.
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:clear_meta fingerprint=d4e29514cefb5ba413402ad57a85eb00d16787b36c6fe17b18314f8546365b66 body_fp=a3f9dce5b45945dff2d3e6267abd390cc4240407636043c24ef647b5a829d35d source_ref=c4c8fffb97eb7849d22babb462a59d2b2ab0f821 role=persistence -->
## `def clear_meta(project_root: Path, key: str) -> None`

Deletes a meta key from the activity database, swallowing any SQLite errors.
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:Pending fingerprint=6a433a570089775c0f496c5c89261697ebe8b2f3621392dacc01563b0f5e4425 body_fp=b0df47faf1a035b5715750b6aea4c0cca9a1e7b9545c60d198fa9c006f0f08fa source_ref=2f462a970066470f2a553a12b94d8ecdc7c9d2d9 role=model -->
## `class Pending`

Represents the stale file set recorded on disk for tracking which triefacts need regeneration.

- `stale`: file paths that are stale relative to source code
- `head`: git commit SHA when the staleness was computed
- `computed_at`: unix timestamp when the staleness was computed
- `count`: number of stale files in the set
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:Pending.count fingerprint=bb877695fb18c4a56d078472ae41d11b5215a4e8ade25804178fd36f29b4140a body_fp=586ae1e8a20a0e1a16b6a4671d4b0ed116d7b6fb7dcde792834860a7f9961fd1 source_ref=2f462a970066470f2a553a12b94d8ecdc7c9d2d9 role=model -->
## `def count(self) -> int`

Returns the number of stale files in the Pending stale set.
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:write_pending fingerprint=20834a8f2cfc1033dc31c0fb365921244e54b27a6aa283435aae96eb4cbbcf2f body_fp=8e607364de10656cf029b9eac426102a47be1c1becea7abf3bf9077b6ac54c21 source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=persistence -->
## `def write_pending(project_root: Path, *, stale: list[str], head: str) -> None`

Replaces the stale file set in the activity database with the provided list.

- Empty `stale` list records a clean state (distinct from never computed)
- Adds metadata marker to distinguish computed-empty from never-computed states
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:read_pending fingerprint=3483116a3b69871ae093c2d2151bc41506b358b19f21f1d06c68c6b1bbc36918 body_fp=c1840ad2128ef7ac421cc64db2427ea8451b3946fcff7782f97c86ca819f3687 source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=persistence -->
## `def read_pending(project_root: Path) -> Pending | None`

Return the recorded stale set from the activity database, or None if pending was never computed.

- Returns `Pending(stale=())` for an empty but computed stale set
- Returns None if the database doesn't exist or has no pending computation marker
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:clear_pending fingerprint=024fe337e53e5ec800221da196aa24ddb5f87463cb8f065d10cf038ed759114e body_fp=5b092330a948ed1e4723e96061f9c0f361b930cd0cab6a4b9d59394c0382d174 source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=persistence -->
## `def clear_pending(project_root: Path, *, synced: list[str], head: str) -> None`

Remove specified files from the pending stale set after successful synchronization.

- `synced`: list of file paths to remove from stale tracking
- `head`: git commit hash to update remaining pending files to
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:Status fingerprint=d4d7471b49f7a9ad56c2bf14cb07dbf1519434573768954a8386fe38a2cafbd5 body_fp=5cedd6a1be7a6ea250d16a9ac6876a5a7d8f6f2f025025abeaf6688bc8fc4268 source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=model -->
## `class Status`

Status represents the current state of an active writer process in the SQLite activity database.

- `state`: one of "idle", "scanning", "syncing", "refreshing", or "error"
- `is_active`: property returning True unless state is "idle" or "error"
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:Status.is_active fingerprint=cc53e644743f2305b8f9081dfb8bd9ae7868e5af76eec048f2717596e0201183 body_fp=df58d0ede51dd3d3016fa767b5f9663cb7f988af0e613c7611519d7de451db6f source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=model -->
## `def is_active(self) -> bool`

Status attribute indicating whether the writer process is currently performing work, excluding idle and error states.
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:_pid_alive fingerprint=b3925759d6be09763d33e318b655a1eba8a41fc29b52759865e18a20b09b1cb8 body_fp=62569640f56ff16575e3b6483aa5865b9fb1665413c94398ed1d16883d4dd3bc source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=util -->
## `def _pid_alive(pid: int) -> bool`

Checks if a process with the given PID exists using POSIX `kill(pid, 0)` liveness probe.

- Returns False for invalid PIDs (≤ 0) or non-existent processes
- Returns True if process exists, even when permission is denied to signal it
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:read_status fingerprint=8b02aa946651fd7fad9f3e01bbd9a2a29aa9731239c6ed21e8170ddf42ba34de body_fp=d10875905d54ff043055a2367a1165cf280ed36b523a762828d2dbdf0371c6bb source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=persistence -->
## `def read_status(project_root: Path) -> Status`

Returns the current writer status from the activity database, defaulting to idle for missing data or dead processes.

- Returns idle status if database/row missing or process with recorded PID is no longer alive
- Handles SQLite errors gracefully by returning idle status
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityWriter fingerprint=bf9123f5af0d2bbe8d8e83281db1cc9341ed21a5ff036d3cc4d1059b5523c1fa body_fp=b2c410bbfb37793c37ec37df3814738e40ceb92d3aa09b4e497a4b3d88762e71 source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=orchestration -->
## `class ActivityWriter`

Records write operation lifecycle into the SQLite status table via context manager pattern.

- On entry: writes running state to database with operation type and PID
- During operation: `file_start`/`file_done`/`file_skip` update current file and progress counters
- On exit: resets to idle state or error state if exception occurred
- All database writes are best-effort and never fail the operation
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityWriter.__init__ fingerprint=dd7987a05a476519726c3bc1764d03b652d5e16fddb3d7f51559b07412a9d944 body_fp=cf3c0bda6d0344c32a0dde47f24a6c9aa954ddfa835cdfaeb049ff6f896d525c source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=model -->
## `def __init__(self, project_root: Path, op: str) -> None`

Initializes ActivityWriter to track a write operation's progress in the activity database.

- `op`: operation type that determines the running state ("sync", "bootstrap", "roles", "refresh", or defaults to "scanning")
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityWriter.__enter__ fingerprint=ca83a66452f5f5154d28cc744bbc9b41f33032c3a7fb05bceeb3903499a40802 body_fp=798ca0dfcf563f85c680b6367b2232c11dc88fe08b5d8eddc0d095cbab293c33 source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=orchestration -->
## `def __enter__(self) -> ActivityWriter`

Writes the ActivityWriter's running state to the status database row and returns self for context manager entry.
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityWriter.__exit__ fingerprint=193d29a60c6a4b2ceac23d2e5563bf4f8b29745c0675fa4e90ba0ae7fb7a5880 body_fp=0d02fb82c66e45cbfbe19238c5a07bde94b03647c810b703d3862fd64b33268b source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=util -->
## `def __exit__(self, exc_type, exc, tb) -> None: # type: ignore[no-untyped-def]`

Resets ActivityWriter status to idle on clean exit or error state on exception.
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityWriter.set_total fingerprint=1de68ab73dcbdbe08e1cb4fde33a7ebcecbcd650b327e7510be337f6409d2afa body_fp=389ecc6246e5114fbb8955ebf44fd73f59c39f7f2f887f4bee67b52379e913c9 source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=orchestration -->
## `def set_total(self, total: int) -> None`

Updates ActivityWriter's total file count and refreshes the status row.
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityWriter.file_start fingerprint=3a412c9c9ebb3b824fcf9aff1811da3d6318d4e7e360d398ffe96aee1bfbe6cc body_fp=81a9644f9db27a20c1dc0c74d322382fd8972fdec64d8692674da87b88538bd9 source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=orchestration -->
## `def file_start(self, rel_path: str, idx: int, total: int) -> None`

ActivityWriter.file_start updates the status row to show processing has begun on the specified file.

- `rel_path`: relative path to the file being processed
- `idx`: current file index (parameter accepted but not used)
- `total`: total number of files to process
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityWriter.file_done fingerprint=e18b59a44040a8efe4a80c37c566b2b2da9a8b3e05b7614c2ae244964b4b33b3 body_fp=f6d17f273f7d55ba85abb9092841fe8e6e50ff360e5d7aeaa29393bbd16b47f9 source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=orchestration -->
## `def file_done(self, rel_path: str, *, symbols: int = 0, cost_usd: float = 0.0) -> None`

Increments ActivityWriter's done counter and updates the status row to clear the current file.
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityWriter.file_skip fingerprint=e18b59a44040a8efe4a80c37c566b2b2da9a8b3e05b7614c2ae244964b4b33b3 body_fp=8377696f03c3a712019d19515448e72c2cbd5fc32ddfc0590854ff61e4b74fa5 source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=orchestration -->
## `def file_skip(self, rel_path: str, reason: str) -> None`

Increments ActivityWriter's done counter and clears current file when a file is skipped.
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityWriter._write fingerprint=764eb383a17b23c974da06e4f14e8a96c579e83e1b96f8e2559aeda8789c555e body_fp=d5032574be32e6d16dc6adc5d9eafce35ffa39e2a4f8795f8c22738288aad1e8 source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=persistence -->
## `def _write( self, *, state: str, current_file: str | None, op: str | None = None, error: str | None = None, ) -> None`

Updates ActivityWriter's status row in the database with current operation state and progress.

- Performs upsert operation to maintain single status row with id=1
- Swallows SQLite errors to prevent status updates from breaking actual operations
- Updates timestamp to current time on each call
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:activity_writer fingerprint=f31179a9514ae03fe4897e1afc6b770e0925463f9c51efe5b6e54a793be8f7ff body_fp=e08258945bc8e4b54f3013df3f8c454e6a3f8451e808d3a525161da1d80f8a3e source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=util -->
## `def activity_writer(project_root: Path, op: str) -> Iterator[ActivityWriter]`

Context manager that creates and manages an ActivityWriter instance for the given operation.

- **project_root**: Project directory containing `.trie/activity.db`
- **op**: Operation name for status tracking (sync, refresh, etc.)
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityProgress fingerprint=8b3a24b1cd776a41a35a09685dcbbe5d52a33e0220d9b37525ad74f6d7e87e97 body_fp=60dff9796ee9e685308b207aa6b1f01da4b3eaf193aa993f072faaf05c2d9e0e source_ref=b82d80d34dc370909873e7cec9d443b8c9307dea role=orchestration -->
## `class ActivityProgress`

Bridges ProgressCallback protocol to update ActivityWriter status while forwarding events to an inner callback.

- `writer`: ActivityWriter instance to update with progress events
- `inner`: Optional inner ProgressCallback to chain events to (Rich/JSONL reporter)
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityProgress.__init__ fingerprint=99b750a7f837e167129e086d2d82356e90fc853d388028d4f45f3f33daf71d87 body_fp=3aab25f2002029196d7fd30fea2ce2feaaee7c7a3d41d5eaced019bfaab5484c source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=model -->
## `def __init__(self, writer: ActivityWriter, inner: object | None = None) -> None`

Initializes ActivityProgress with an ActivityWriter and optional inner ProgressCallback to chain.
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityProgress.on_plan fingerprint=38b764691b898ba28fa36d48f4a6536476a0a00b7818c088a1514e0938fcbf6c body_fp=2d36da07b74b9985e1a267135ad4cec395ae8b20b41a3f946d07022ad1476d33 source_ref=b82d80d34dc370909873e7cec9d443b8c9307dea role=orchestration -->
## `def on_plan(self, *, direct: int, cascade: int) -> None: # Purely informational; mirror to the inner host callback if it cares.`

Forwards planning information to ActivityProgress's inner callback if it implements on_plan.
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityProgress.on_section fingerprint=55cd8347bc3e40170b95d55935b01b170d86bb47cf0c28e453fd1f5323fa5c09 body_fp=591858430f8869716b0549d606d931f80a02a5eafa526f149b73343100317d81 source_ref=b82d80d34dc370909873e7cec9d443b8c9307dea role=orchestration -->
## `def on_section(self, *, label: str, count: int) -> None`

Forwards section progress events to the wrapped inner ProgressCallback if it supports the `on_section` method.
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityProgress.on_start fingerprint=b2a31e9bebe346cd02173dd1ebf15922fb2a8c1ec852a603ec8ba566c973706a body_fp=f1f1aa72c88786e1e3b42205603aac3dd6dcd9e4707d8263d6214635d6aa5c89 source_ref=aa956e0bb55c07a04fe6a5e62c50cd40ce073915 role=orchestration -->
## `def on_start(self, rel_path: str, idx: int, total: int, *, cascade: bool = False) -> None`

Notifies ActivityProgress that processing has started on a file, forwarding to both the activity writer and inner callback with optional cascade parameter.
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityProgress.on_done fingerprint=c9204faea4db213640eac8154308dfc0d80d8a0d96f8990def99cc510a7531a5 body_fp=736bd8b9ac01d328810544725e5d12b2acedcf782acda69a3b9a457ca080b94e source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=orchestration -->
## `def on_done(self, rel_path: str, result: object, running_cost_usd: float) -> None`

ActivityProgress method that updates writer with file completion and forwards to inner callback.

- Extracts `symbols_generated` attribute from result object (defaults to 0 if missing)
- Delegates to inner callback's `on_done` method if present
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityProgress.on_skip fingerprint=3ae4223a769a1393abe7ee455a680728d07b15791414e54e3ff4dfdf3c5ff1d7 body_fp=5c2d46ddfc47d74e39c94bba2ca94f17711eed9f7cd403769d7ce425e0b3738f source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=util -->
## `def on_skip(self, rel_path: str, reason: str) -> None`

Reports file skip to ActivityProgress's writer and forwards to inner callback if present.
<!-- trie:end -->