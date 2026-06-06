---
trie_version: 0.1.5
source: trie/activity.py
file_fingerprint: 9c08d6257bd3b3edf1847daf2fb18bdef3c7c4b6f7571c500ddca934f0c7378d
last_synced_at: '2026-06-06T14:03:34Z'
description: Ephemeral local activity state for trie, backed by SQLite.
defines:
- kind: module
  qualified_name: trie/activity:__module__
  lines: 1-357
- kind: constant
  qualified_name: trie/activity:DB_FILENAME
  lines: 38-38
- kind: constant
  qualified_name: trie/activity:_SCHEMA
  lines: 40-62
- kind: function
  qualified_name: trie/activity:db_path
  lines: 65-66
- kind: function
  qualified_name: trie/activity:_connect
  lines: 70-85
- kind: class
  qualified_name: trie/activity:Pending
  lines: 94-101
- kind: method
  qualified_name: trie/activity:Pending.count
  lines: 100-101
- kind: function
  qualified_name: trie/activity:write_pending
  lines: 104-118
- kind: function
  qualified_name: trie/activity:read_pending
  lines: 121-144
- kind: function
  qualified_name: trie/activity:clear_pending
  lines: 147-154
- kind: class
  qualified_name: trie/activity:Status
  lines: 163-176
- kind: method
  qualified_name: trie/activity:Status.is_active
  lines: 175-176
- kind: function
  qualified_name: trie/activity:_pid_alive
  lines: 179-190
- kind: function
  qualified_name: trie/activity:read_status
  lines: 193-224
- kind: class
  qualified_name: trie/activity:ActivityWriter
  lines: 232-313
- kind: method
  qualified_name: trie/activity:ActivityWriter.__init__
  lines: 241-252
- kind: method
  qualified_name: trie/activity:ActivityWriter.__enter__
  lines: 254-256
- kind: method
  qualified_name: trie/activity:ActivityWriter.__exit__
  lines: 258-262
- kind: method
  qualified_name: trie/activity:ActivityWriter.set_total
  lines: 264-266
- kind: method
  qualified_name: trie/activity:ActivityWriter.file_start
  lines: 268-270
- kind: method
  qualified_name: trie/activity:ActivityWriter.file_done
  lines: 272-274
- kind: method
  qualified_name: trie/activity:ActivityWriter.file_skip
  lines: 276-278
- kind: method
  qualified_name: trie/activity:ActivityWriter._write
  lines: 280-313
- kind: function
  qualified_name: trie/activity:activity_writer
  lines: 317-321
- kind: class
  qualified_name: trie/activity:ActivityProgress
  lines: 331-356
- kind: method
  qualified_name: trie/activity:ActivityProgress.__init__
  lines: 338-340
- kind: method
  qualified_name: trie/activity:ActivityProgress.on_start
  lines: 342-345
- kind: method
  qualified_name: trie/activity:ActivityProgress.on_done
  lines: 347-351
- kind: method
  qualified_name: trie/activity:ActivityProgress.on_skip
  lines: 353-356
incoming_refs: 19
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
<!-- trie:section symbol=trie/activity:db_path fingerprint=23fb5be98a9ec4515c2044254a25da56fe69f828f8d48f301452ebf9bb01a100 body_fp=e09f60174cebdf90d6c74cf8ea6e0642e1c30cdaf89af7312bf4e25994856d11 source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=util -->
Returns the path to the activity database file within the project's .trie directory.
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:_connect fingerprint=5927a4b7c2aebadbee77c010465dd1de6bf5611df14f8cecb50a9847860291d4 body_fp=0cd5c70b5fdbe1ebea3b54c4e65f21cdc93ca38d43d11e17bd454abe4add3146 source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=persistence -->
Opens ephemeral SQLite activity database with WAL journaling and schema initialization.

- Creates `.trie` directory and database file if missing
- Enables WAL mode for concurrent reads during writes
- Sets 5-second timeout for lock contention retry
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:Pending fingerprint=6a433a570089775c0f496c5c89261697ebe8b2f3621392dacc01563b0f5e4425 body_fp=16e48de335594be8c5cdca8ecfffafad8cb2f24d7c20d233cc9a63833d91c006 source_ref=2f462a970066470f2a553a12b94d8ecdc7c9d2d9 role=model -->
Represents the stale file set recorded on disk for tracking which triefacts need regeneration.

- `stale`: file paths that are stale relative to source code
- `head`: git commit SHA when the staleness was computed
- `computed_at`: unix timestamp when the staleness was computed
- `count`: number of stale files in the set
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:Pending.count fingerprint=bb877695fb18c4a56d078472ae41d11b5215a4e8ade25804178fd36f29b4140a body_fp=b36f83f091c8cc678e8e9edc37f7f91e719f73b4440731b06cb637c767614add source_ref=2f462a970066470f2a553a12b94d8ecdc7c9d2d9 role=model -->
Returns the number of stale files in the Pending stale set.
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:write_pending fingerprint=20834a8f2cfc1033dc31c0fb365921244e54b27a6aa283435aae96eb4cbbcf2f body_fp=3fe3ee6db7dc5169c9b0aec08e6a7cf20399c93281b9062af5a9e2a0e036f32d source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=persistence -->
Replaces the stale file set in the activity database with the provided list.

- Empty `stale` list records a clean state (distinct from never computed)
- Adds metadata marker to distinguish computed-empty from never-computed states
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:read_pending fingerprint=3483116a3b69871ae093c2d2151bc41506b358b19f21f1d06c68c6b1bbc36918 body_fp=ff0cf02c4d6cdf563a4c6d18dfc888b025f847462f61d13fdb4dbfafe82a371d source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=persistence -->
Return the recorded stale set from the activity database, or None if pending was never computed.

- Returns `Pending(stale=())` for an empty but computed stale set
- Returns None if the database doesn't exist or has no pending computation marker
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:clear_pending fingerprint=024fe337e53e5ec800221da196aa24ddb5f87463cb8f065d10cf038ed759114e body_fp=342866558cf436ec3b2e5ac2e003677a64e5d62b7d408cd260d67d81dbbeed6c source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=persistence -->
Remove specified files from the pending stale set after successful synchronization.

- `synced`: list of file paths to remove from stale tracking
- `head`: git commit hash to update remaining pending files to
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:Status fingerprint=d4d7471b49f7a9ad56c2bf14cb07dbf1519434573768954a8386fe38a2cafbd5 body_fp=c0f70bbd356e6c6b6aadbab686b0c5d7fad5a565ed977c38464f69b7bec13609 source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=model -->
Status represents the current state of an active writer process in the SQLite activity database.

- `state`: one of "idle", "scanning", "syncing", "refreshing", or "error"
- `is_active`: property returning True unless state is "idle" or "error"
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:Status.is_active fingerprint=cc53e644743f2305b8f9081dfb8bd9ae7868e5af76eec048f2717596e0201183 body_fp=fa628c953acbb0d5d52d16e35cdb20590d951da3c6af1811ffe948c0395db40b source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=model -->
Status attribute indicating whether the writer process is currently performing work, excluding idle and error states.
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:_pid_alive fingerprint=b3925759d6be09763d33e318b655a1eba8a41fc29b52759865e18a20b09b1cb8 body_fp=cda65365fe66dd88305d4823841978112823cf06f022f2c7496c14751eb63e1a source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=util -->
Checks if a process with the given PID exists using POSIX `kill(pid, 0)` liveness probe.

- Returns False for invalid PIDs (≤ 0) or non-existent processes
- Returns True if process exists, even when permission is denied to signal it
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:read_status fingerprint=8b02aa946651fd7fad9f3e01bbd9a2a29aa9731239c6ed21e8170ddf42ba34de body_fp=3bd73e16f2ad00b3a6efa43012a4339d9a07069db02f62f464bee77c44b2f04d source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=persistence -->
Returns the current writer status from the activity database, defaulting to idle for missing data or dead processes.

- Returns idle status if database/row missing or process with recorded PID is no longer alive
- Handles SQLite errors gracefully by returning idle status
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityWriter fingerprint=bf9123f5af0d2bbe8d8e83281db1cc9341ed21a5ff036d3cc4d1059b5523c1fa body_fp=df199c3afa378a7b538af45355fd92cefe6ca356170014d29f1e29083fc76331 source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=orchestration -->
Records write operation lifecycle into the SQLite status table via context manager pattern.

- On entry: writes running state to database with operation type and PID
- During operation: `file_start`/`file_done`/`file_skip` update current file and progress counters
- On exit: resets to idle state or error state if exception occurred
- All database writes are best-effort and never fail the operation
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityWriter.__init__ fingerprint=dd7987a05a476519726c3bc1764d03b652d5e16fddb3d7f51559b07412a9d944 body_fp=212541995582b488fc63861be0a4a41835820d8cb1e29c6ec25e826a37b8fcab source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=model -->
Initializes ActivityWriter to track a write operation's progress in the activity database.

- `op`: operation type that determines the running state ("sync", "bootstrap", "roles", "refresh", or defaults to "scanning")
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityWriter.__enter__ fingerprint=ca83a66452f5f5154d28cc744bbc9b41f33032c3a7fb05bceeb3903499a40802 body_fp=d052f3a481bcfd99250376b83ed0aaa8cf4f9ee8e02972f513f72a88077366c3 source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=orchestration -->
Writes the ActivityWriter's running state to the status database row and returns self for context manager entry.
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityWriter.__exit__ fingerprint=193d29a60c6a4b2ceac23d2e5563bf4f8b29745c0675fa4e90ba0ae7fb7a5880 body_fp=679ef7cd594d946e8c6d3c95e0ece19c8288960fc334cb3c87984612e01fe65f source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=util -->
Resets ActivityWriter status to idle on clean exit or error state on exception.
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityWriter.set_total fingerprint=1de68ab73dcbdbe08e1cb4fde33a7ebcecbcd650b327e7510be337f6409d2afa body_fp=b1d2828122d3b1c3755f7957f742ab1ec7bef983161e957dc7fa1b15d0a2ec0a source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=orchestration -->
Updates ActivityWriter's total file count and refreshes the status row.
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityWriter.file_start fingerprint=3a412c9c9ebb3b824fcf9aff1811da3d6318d4e7e360d398ffe96aee1bfbe6cc body_fp=22eea8217be60a76b259781c083dc49fc4cdbcd92fcfe925985700093f8d1045 source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=orchestration -->
ActivityWriter.file_start updates the status row to show processing has begun on the specified file.

- `rel_path`: relative path to the file being processed
- `idx`: current file index (parameter accepted but not used)
- `total`: total number of files to process
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityWriter.file_done fingerprint=e18b59a44040a8efe4a80c37c566b2b2da9a8b3e05b7614c2ae244964b4b33b3 body_fp=acc578192ec8e1112d0beaf820d6886882bf61272632bc632d535667fd222ee1 source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=orchestration -->
Increments ActivityWriter's done counter and updates the status row to clear the current file.
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityWriter.file_skip fingerprint=e18b59a44040a8efe4a80c37c566b2b2da9a8b3e05b7614c2ae244964b4b33b3 body_fp=4cf6ceff733a331f0e0d4f4ba53756cf6396f3505cd62582e49de927d9635029 source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=orchestration -->
Increments ActivityWriter's done counter and clears current file when a file is skipped.
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityWriter._write fingerprint=764eb383a17b23c974da06e4f14e8a96c579e83e1b96f8e2559aeda8789c555e body_fp=b9d46a75238308f7685cfc5cc402c3ed6ea9e5d6f8664545632b99718594b5bd source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=persistence -->
Updates ActivityWriter's status row in the database with current operation state and progress.

- Performs upsert operation to maintain single status row with id=1
- Swallows SQLite errors to prevent status updates from breaking actual operations
- Updates timestamp to current time on each call
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:activity_writer fingerprint=f31179a9514ae03fe4897e1afc6b770e0925463f9c51efe5b6e54a793be8f7ff body_fp=b8f6f77c5791be60301edb6b4016d6f7d0a54c87eeaeb001f8c8fe503aef0f41 source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=util -->
Context manager that creates and manages an ActivityWriter instance for the given operation.

- **project_root**: Project directory containing `.trie/activity.db`
- **op**: Operation name for status tracking (sync, refresh, etc.)
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityProgress fingerprint=7ecd87d2cc33e3ded458bfac36e13bd30a95c91a22916b0462b44d215d8d463a body_fp=52d93d62f597f52d19e18a33f9312d6663875b441f9870196d6f0fd32f181ab1 source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=orchestration -->
Bridges per-file progress callbacks to ActivityWriter, optionally wrapping an inner progress reporter.

- **writer**: ActivityWriter instance that receives mirrored progress updates
- **inner**: Optional wrapped ProgressCallback that also receives the same updates
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityProgress.__init__ fingerprint=99b750a7f837e167129e086d2d82356e90fc853d388028d4f45f3f33daf71d87 body_fp=887e3bbdfed24b8f29daf6ff2ce816e963311afd31c1bd0a3055303beca2d64a source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=model -->
Initializes ActivityProgress with an ActivityWriter and optional inner ProgressCallback to chain.
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityProgress.on_start fingerprint=16b0ad6889665700c8ebc80073cd49f3146fb3a1dfd5c072c431001030c762c6 body_fp=ef6af84d9348f3899183c049668d6ac241baba298c6e5f0bd700790f670032dc source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=orchestration -->
Notifies ActivityProgress that processing has started on a file, forwarding to both the activity writer and inner callback.
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityProgress.on_done fingerprint=c9204faea4db213640eac8154308dfc0d80d8a0d96f8990def99cc510a7531a5 body_fp=a66b78bb8fc085e5604bba1daf75d1f91fc32fdf49ee5afbb36bcbb291d51a9f source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=orchestration -->
ActivityProgress method that updates writer with file completion and forwards to inner callback.

- Extracts `symbols_generated` attribute from result object (defaults to 0 if missing)
- Delegates to inner callback's `on_done` method if present
<!-- trie:end -->
<!-- trie:section symbol=trie/activity:ActivityProgress.on_skip fingerprint=3ae4223a769a1393abe7ee455a680728d07b15791414e54e3ff4dfdf3c5ff1d7 body_fp=0faa11f82eaf67eee50b57444727204972941a3f3e84850265fbfbfb31af64be source_ref=cc1786342572b4c96d926421417b6f3c5cf4ce46 role=util -->
Reports file skip to ActivityProgress's writer and forwards to inner callback if present.
<!-- trie:end -->