---
trie_version: 0.1.5
source: tests/test_activity.py
file_fingerprint: de0bd1d21f40965dee5b8929411e1cb8e3d513a5163b4d669efa1df2ad43aefb
last_synced_at: '2026-06-06T14:03:16Z'
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
<!-- trie:section symbol=tests/test_activity:test_pending_round_trip fingerprint=320c9f34360e08f359cdb5c8a73aa56f1f9f1ac72020539733be0e1e26f4c943 body_fp=7c324aa1947b088e3f0f67cec2c0a62bc1b410236885e842df7aa91abe9ce566 source_ref=e3f9edc17147aef6e0bd7c3a08b1f7a39fb0e25c role=test -->
Tests that writing and reading pending activity state preserves data with sorting and deduplication.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_activity:test_pending_never_computed_returns_none fingerprint=b9b8a0f975b6e44f4a84f5bb09fa012e84dfd1b380f42488e194296bb5082fb5 body_fp=b4a55ea542994ad00ce9e65e0c7941fe92cdee3a83a64447924c21fe7ffaceff source_ref=e3f9edc17147aef6e0bd7c3a08b1f7a39fb0e25c role=test -->
Verifies that `read_pending` returns `None` when no pending state has been written to the activity database.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_activity:test_pending_computed_empty_is_not_none fingerprint=6fe0539811ad3bb01032d1f00aa30b6e140315fd741cb26692ee516d62aba605 body_fp=4e01b0edfcfc9b952f16156c41cfd220cb859d82907fe947d066acc7e9eb282b source_ref=e3f9edc17147aef6e0bd7c3a08b1f7a39fb0e25c role=test -->
Verifies that writing an empty stale list still creates a valid pending state object rather than returning None.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_activity:test_clear_pending_subtracts_synced fingerprint=3c77fe06d07d0a57f085a0223b9f4ddd84e2a02756f067f10aa6f05f0c5095bc body_fp=ac50f6b7ce6d4bb9b0de9d9ee14a57b7beee5a161c50af2f175a73823631a2df source_ref=e3f9edc17147aef6e0bd7c3a08b1f7a39fb0e25c role=test -->
Tests that clear_pending removes synced files from the stale list and updates the head commit.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_activity:test_status_idle_by_default fingerprint=ef1b2db24329d4759333a15ea0ed731603ed67b5c4e8397db39d4bf3f2973b41 body_fp=f255744abbe325db9859623e21f1df73553275aa5879c7ba0a958a68353fb8d3 source_ref=e3f9edc17147aef6e0bd7c3a08b1f7a39fb0e25c role=test -->
Verifies that `read_status` returns an idle state when no activity has been recorded.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_activity:test_activity_writer_lifecycle fingerprint=144edaa84d35b80cb768b5f9e5b130ede9db4942e91d2649af21d7d0902418af body_fp=956a418c08392b36bddbf24a36b18e25ed71f5095b6125ad4ee259d8afd8007a source_ref=e3f9edc17147aef6e0bd7c3a08b1f7a39fb0e25c role=test -->
Tests ActivityWriter context manager lifecycle from active state to idle cleanup.

- Verifies ActivityWriter updates status database with operation state, current file, and process ID
- Confirms status transitions from "syncing" during operation to "idle" after context exit
<!-- trie:end -->
<!-- trie:section symbol=tests/test_activity:test_activity_writer_records_error_on_exception fingerprint=5246e224056c1621c67410b79aacb5e0f767499bf8c9362e5e0765f8cbc9253f body_fp=aa2b22e040e4f13ff0a9e224e592ab241a1ba12cd3eee84e980bc29da4f2b32a source_ref=e3f9edc17147aef6e0bd7c3a08b1f7a39fb0e25c role=test -->
Tests that ActivityWriter records error state when an exception occurs during context management.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_activity:test_stale_status_from_dead_pid_reads_idle fingerprint=a808de2c192a990ddded6d6b378ece20d6083b52885a2bafbca086b94684ce5f body_fp=477fc19614fd2b4e662fe312bf9bfaaeaa1f4be41eb3ea1ccd0952ed9480045b source_ref=e3f9edc17147aef6e0bd7c3a08b1f7a39fb0e25c role=test -->
Tests that read_status returns idle state when a stale 'syncing' process record has a dead PID.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_activity:test_activity_progress_mirrors_to_writer_and_inner fingerprint=9961756579c067b84169b6c5154a673e67e84c6786ba9b6b35bb270db27f9356 body_fp=d96c61e44ab9e771cf5affc9656e4f0f95cb6477eb5b17eaa9c3c91e29553b24 source_ref=e3f9edc17147aef6e0bd7c3a08b1f7a39fb0e25c role=test -->
Tests that ActivityProgress delegates progress callbacks to both the ActivityWriter and an inner progress handler.

- Creates mock inner handler that records method calls in a list
- Verifies ActivityProgress forwards `on_start` and `on_done` calls to both the writer (updating database status) and the inner handler
- Confirms writer updates current file status while inner handler receives expected callback sequence
<!-- trie:end -->