---
trie_version: 0.3.0
source: tests/test_activity.py
file_fingerprint: 04002d8d8af80b2b98784e08f110cb113e800112ba2de32d7b8e1c9dbae7011a
last_synced_at: '2026-07-26T20:28:35Z'
description: Tests for the SQLite-backed local activity state (trie/activity.py).
defines:
- kind: module
  qualified_name: tests/test_activity:__module__
  lines: 1-130
- kind: function
  qualified_name: tests/test_activity:test_pending_round_trip
  lines: 20-26
  signature: 'def test_pending_round_trip(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_activity:test_pending_never_computed_returns_none
  lines: 29-30
  signature: 'def test_pending_never_computed_returns_none(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_activity:test_pending_computed_empty_is_not_none
  lines: 33-38
  signature: 'def test_pending_computed_empty_is_not_none(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_activity:test_clear_pending_subtracts_synced
  lines: 41-47
  signature: 'def test_clear_pending_subtracts_synced(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_activity:test_status_idle_by_default
  lines: 53-54
  signature: 'def test_status_idle_by_default(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_activity:test_activity_writer_lifecycle
  lines: 57-72
  signature: 'def test_activity_writer_lifecycle(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_activity:test_activity_writer_records_error_on_exception
  lines: 75-83
  signature: 'def test_activity_writer_records_error_on_exception(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_activity:test_stale_status_from_dead_pid_reads_idle
  lines: 86-98
  signature: 'def test_stale_status_from_dead_pid_reads_idle(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_activity:test_activity_progress_mirrors_to_writer_and_inner
  lines: 104-129
  signature: 'def test_activity_progress_mirrors_to_writer_and_inner(tmp_path: Path)'
incoming_refs: 0
outgoing_refs: 24
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
<!-- trie:section symbol=tests/test_activity:test_pending_round_trip fingerprint=320c9f34360e08f359cdb5c8a73aa56f1f9f1ac72020539733be0e1e26f4c943 body_fp=971c74c26578886772865385bad0c580e4c47cfb6a44f1d88ba253e515338427 source_ref=e1eaf0ecfeb690f7162443ed903ca4791f2cc3e5 role=test -->
## `def test_pending_round_trip(tmp_path: Path)`

Tests that pending activity data can be written and read back with sorting and deduplication.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_activity:test_pending_never_computed_returns_none fingerprint=b9b8a0f975b6e44f4a84f5bb09fa012e84dfd1b380f42488e194296bb5082fb5 body_fp=e0eee26dbc0d1abcf636ba251793c77b1cae0275d858b3aec7f5d8bfad7edb72 source_ref=e1eaf0ecfeb690f7162443ed903ca4791f2cc3e5 role=test -->
## `def test_pending_never_computed_returns_none(tmp_path: Path)`

Tests that `read_pending` returns `None` when no pending activity has been written to the database.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_activity:test_pending_computed_empty_is_not_none fingerprint=6fe0539811ad3bb01032d1f00aa30b6e140315fd741cb26692ee516d62aba605 body_fp=9787855fcc01e522e72a4de4360e6c7569302f17b83dd0d9c9f3c1012c03efd2 source_ref=e1eaf0ecfeb690f7162443ed903ca4791f2cc3e5 role=test -->
## `def test_pending_computed_empty_is_not_none(tmp_path: Path)`

Verifies that writing an empty stale list still creates a non-None pending record.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_activity:test_clear_pending_subtracts_synced fingerprint=3c77fe06d07d0a57f085a0223b9f4ddd84e2a02756f067f10aa6f05f0c5095bc body_fp=5dd7ef923b7b8fdbfc7b05356fe11a4bf8900cef496b71e6d5aa0e342ead7de2 source_ref=e1eaf0ecfeb690f7162443ed903ca4791f2cc3e5 role=test -->
## `def test_clear_pending_subtracts_synced(tmp_path: Path)`

Tests that `clear_pending` removes synced files from the stale list and updates the head commit.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_activity:test_status_idle_by_default fingerprint=ef1b2db24329d4759333a15ea0ed731603ed67b5c4e8397db39d4bf3f2973b41 body_fp=4c965d1bbb70c1dfa5068876ac7ca5da63e9b744b59bc25b0e26f2b9842cdff4 source_ref=e1eaf0ecfeb690f7162443ed903ca4791f2cc3e5 role=test -->
## `def test_status_idle_by_default(tmp_path: Path)`

Verifies that `read_status` returns idle state when no activity has been recorded.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_activity:test_activity_writer_lifecycle fingerprint=144edaa84d35b80cb768b5f9e5b130ede9db4942e91d2649af21d7d0902418af body_fp=c88e0ef4514ce81176f2f7f8f2de96151f1bd70b267c76fd2caa0339a390be7b source_ref=e1eaf0ecfeb690f7162443ed903ca4791f2cc3e5 role=test -->
## `def test_activity_writer_lifecycle(tmp_path: Path)`

Tests that ActivityWriter properly tracks sync progress and resets to idle state on clean exit.

- Verifies that status tracking updates correctly during file processing
- Confirms that status resets to "idle" when context manager exits cleanly
<!-- trie:end -->
<!-- trie:section symbol=tests/test_activity:test_activity_writer_records_error_on_exception fingerprint=5246e224056c1621c67410b79aacb5e0f767499bf8c9362e5e0765f8cbc9253f body_fp=fcd6e4bd26784522dddbae68060d7b6e3b671015d649f1ebb287a0cda4a70dd2 source_ref=e1eaf0ecfeb690f7162443ed903ca4791f2cc3e5 role=test -->
## `def test_activity_writer_records_error_on_exception(tmp_path: Path)`

Verifies that ActivityWriter records error state and message when an exception occurs during context management.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_activity:test_stale_status_from_dead_pid_reads_idle fingerprint=a808de2c192a990ddded6d6b378ece20d6083b52885a2bafbca086b94684ce5f body_fp=642d44d9069b8b22c94cf394bb5dd58716a0a6f8d01ba2d494a9556eda95b7c4 source_ref=e1eaf0ecfeb690f7162443ed903ca4791f2cc3e5 role=test -->
## `def test_stale_status_from_dead_pid_reads_idle(tmp_path: Path)`

Verifies that activity status from a dead process ID is automatically treated as idle for crash recovery.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_activity:test_activity_progress_mirrors_to_writer_and_inner fingerprint=85273bace285dc4a08e3368dc4e421a655d8be0ebf037692058eb9c049e526a9 body_fp=4dc631f96d6de78827127b128e3150dc0e4e6424c3ee6663892f4546125b3246 source_ref=e1eaf0ecfeb690f7162443ed903ca4791f2cc3e5 role=test -->
## `def test_activity_progress_mirrors_to_writer_and_inner(tmp_path: Path)`

Tests that ActivityProgress forwards progress events to both the ActivityWriter and an inner progress handler.

- Creates mock inner handler that records method calls
- Verifies ActivityWriter receives file updates through ActivityProgress
- Confirms inner handler receives forwarded on_start and on_done calls
<!-- trie:end -->