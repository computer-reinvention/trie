---
trie_version: 0.1.5
source: tests/test_activity.py
file_fingerprint: 04002d8d8af80b2b98784e08f110cb113e800112ba2de32d7b8e1c9dbae7011a
last_synced_at: '2026-06-09T10:08:00Z'
description: Tests for the SQLite-backed local activity state (trie/activity.py).
defines:
- kind: module
  qualified_name: tests/test_activity:__module__
  lines: 1-130
- kind: function
  qualified_name: tests/test_activity:test_pending_round_trip
  lines: 20-26
- kind: function
  qualified_name: tests/test_activity:test_pending_never_computed_returns_none
  lines: 29-30
- kind: function
  qualified_name: tests/test_activity:test_pending_computed_empty_is_not_none
  lines: 33-38
- kind: function
  qualified_name: tests/test_activity:test_clear_pending_subtracts_synced
  lines: 41-47
- kind: function
  qualified_name: tests/test_activity:test_status_idle_by_default
  lines: 53-54
- kind: function
  qualified_name: tests/test_activity:test_activity_writer_lifecycle
  lines: 57-72
- kind: function
  qualified_name: tests/test_activity:test_activity_writer_records_error_on_exception
  lines: 75-83
- kind: function
  qualified_name: tests/test_activity:test_stale_status_from_dead_pid_reads_idle
  lines: 86-98
- kind: function
  qualified_name: tests/test_activity:test_activity_progress_mirrors_to_writer_and_inner
  lines: 104-129
incoming_refs: 0
outgoing_refs: 18
---
<!-- trie:section symbol=tests/test_activity:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=ef21754fba1b431850f85031b88d12ae25e33c59729b2b426551a173dcafe44d source_ref=e3f9edc17147aef6e0bd7c3a08b1f7a39fb0e25c role=test -->
Tests for SQLite-backed local activity state functionality in trie/activity.py.

- **test_pending_round_trip**: Verifies pending state write/read cycle with deduplication and sorting
- **test_pending_never_computed_returns_none**: Confirms uninitialized pending state returns None
- **test_pending_computed_empty_is_not_none**: Tests empty pending state is distinct from uncomputed
- **test_clear_pending_subtracts_synced**: Validates clearing synced files from pending list
- **test_status_idle_by_default**: Checks default activity status is idle
- **test_activity_writer_lifecycle**: Tests ActivityWriter context manager and status updates
- **test_activity_writer_records_error_on_exception**: Verifies error state on exceptions
- **test_stale_status_from_dead_pid_reads_idle**: Tests crash recovery for dead process IDs
- **test_activity_progress_mirrors_to_writer_and_inner**: Validates ActivityProgress delegation
<!-- trie:end -->
<!-- trie:section symbol=tests/test_activity:test_pending_round_trip fingerprint=320c9f34360e08f359cdb5c8a73aa56f1f9f1ac72020539733be0e1e26f4c943 body_fp=f26f8e71a1369e53e5d661f0f41c0593f3eefd9d4c84502f48e0de810a60dd05 source_ref=e1eaf0ecfeb690f7162443ed903ca4791f2cc3e5 role=test -->
Tests that pending activity data can be written and read back with sorting and deduplication.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_activity:test_pending_never_computed_returns_none fingerprint=b9b8a0f975b6e44f4a84f5bb09fa012e84dfd1b380f42488e194296bb5082fb5 body_fp=61024ffbd03fa0b0c15f0b648fe87ea7c974956b7d11f44c1eff65758782b446 source_ref=e1eaf0ecfeb690f7162443ed903ca4791f2cc3e5 role=test -->
Tests that `read_pending` returns `None` when no pending activity has been written to the database.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_activity:test_pending_computed_empty_is_not_none fingerprint=6fe0539811ad3bb01032d1f00aa30b6e140315fd741cb26692ee516d62aba605 body_fp=d0e36ca993a24f6999a6443aa21f12df80bd93f4f145c650a84ab69db1c2bfed source_ref=e1eaf0ecfeb690f7162443ed903ca4791f2cc3e5 role=test -->
Verifies that writing an empty stale list still creates a non-None pending record.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_activity:test_clear_pending_subtracts_synced fingerprint=3c77fe06d07d0a57f085a0223b9f4ddd84e2a02756f067f10aa6f05f0c5095bc body_fp=0f193fe02a67bc2417f498151f2521830605eeec897119533940922437e06032 source_ref=e1eaf0ecfeb690f7162443ed903ca4791f2cc3e5 role=test -->
Tests that `clear_pending` removes synced files from the stale list and updates the head commit.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_activity:test_status_idle_by_default fingerprint=ef1b2db24329d4759333a15ea0ed731603ed67b5c4e8397db39d4bf3f2973b41 body_fp=fc48ca21dbbeca84327e94e29a342047098487467512eeec6c4658e1a4425468 source_ref=e1eaf0ecfeb690f7162443ed903ca4791f2cc3e5 role=test -->
Verifies that `read_status` returns idle state when no activity has been recorded.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_activity:test_activity_writer_lifecycle fingerprint=144edaa84d35b80cb768b5f9e5b130ede9db4942e91d2649af21d7d0902418af body_fp=a067e2db20a41f493d09d6ab4ab45600ce5f793c2f575591b95dc955cc15a671 source_ref=e1eaf0ecfeb690f7162443ed903ca4791f2cc3e5 role=test -->
Tests that ActivityWriter properly tracks sync progress and resets to idle state on clean exit.

- Verifies that status tracking updates correctly during file processing
- Confirms that status resets to "idle" when context manager exits cleanly
<!-- trie:end -->
<!-- trie:section symbol=tests/test_activity:test_activity_writer_records_error_on_exception fingerprint=5246e224056c1621c67410b79aacb5e0f767499bf8c9362e5e0765f8cbc9253f body_fp=c54a196ec7f796fd5932acb7016035a2c3473f15c5167c2feeb6daec92575672 source_ref=e1eaf0ecfeb690f7162443ed903ca4791f2cc3e5 role=test -->
Verifies that ActivityWriter records error state and message when an exception occurs during context management.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_activity:test_stale_status_from_dead_pid_reads_idle fingerprint=a808de2c192a990ddded6d6b378ece20d6083b52885a2bafbca086b94684ce5f body_fp=e0505bbd426c1b19dc90b3b8d2c54e98b7a15668e77981ba5badc857b62eb640 source_ref=e1eaf0ecfeb690f7162443ed903ca4791f2cc3e5 role=test -->
Verifies that activity status from a dead process ID is automatically treated as idle for crash recovery.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_activity:test_activity_progress_mirrors_to_writer_and_inner fingerprint=85273bace285dc4a08e3368dc4e421a655d8be0ebf037692058eb9c049e526a9 body_fp=7e6ecf31832bf0b839ddac9c1d2f20d9a109d1efdeae33aa5d96a7d2875aa16b source_ref=e1eaf0ecfeb690f7162443ed903ca4791f2cc3e5 role=test -->
Tests that ActivityProgress forwards progress events to both the ActivityWriter and an inner progress handler.

- Creates mock inner handler that records method calls
- Verifies ActivityWriter receives file updates through ActivityProgress
- Confirms inner handler receives forwarded on_start and on_done calls
<!-- trie:end -->