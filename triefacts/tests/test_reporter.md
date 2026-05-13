---
trie_version: 0.1.0
source: tests/test_reporter.py
file_fingerprint: d6f396d10b0e62e4fbf237881ec75c8c98d6135f86e045160be8f316bdb164cf
last_synced_at: '2026-05-12T18:31:47Z'
defines:
- kind: function
  qualified_name: tests/test_reporter:test_mute_suppresses_info_and_success
  lines: 18-23
- kind: function
  qualified_name: tests/test_reporter:test_mute_still_emits_errors
  lines: 26-29
- kind: function
  qualified_name: tests/test_reporter:test_medium_emits_info_and_success_but_not_detail
  lines: 32-40
- kind: function
  qualified_name: tests/test_reporter:test_verbose_emits_everything
  lines: 43-49
- kind: function
  qualified_name: tests/test_reporter:test_progress_mute_is_noop
  lines: 52-59
- kind: function
  qualified_name: tests/test_reporter:test_progress_medium_prints_finish_lines
  lines: 62-70
- kind: function
  qualified_name: tests/test_reporter:test_progress_verbose_includes_token_detail
  lines: 73-79
- kind: function
  qualified_name: tests/test_reporter:test_root_quiet_and_verbose_are_mutually_exclusive
  lines: 85-89
- kind: function
  qualified_name: tests/test_reporter:test_root_version_still_works_with_verbosity_flags
  lines: 92-96
incoming_refs: 0
outgoing_refs: 9
---
<!-- trie:section symbol=tests/test_reporter:test_mute_suppresses_info_and_success fingerprint=f63e90635d0ad62f227a9b8d564b4d187a86cc47cd33366b448730a2d327eca7 body_fp=5846caaf96eda4db7a6522201cd86c23b05890b05b6e825dc93eb3a71cde89e3 -->
## `test_mute_suppresses_info_and_success()`

Assert that `Verbosity.MUTE` produces no output for `info`, `success`, and `detail` calls.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_reporter:test_mute_still_emits_errors fingerprint=a7e2fa1d4951cdb11c6b26264cfd3101e79815e5b529673f4a8442c60569171f body_fp=4dfcd7aa8db13fbdc8afbc8bd9e615e0677b5f94025dfcb3c819f73188812122 -->
## `test_mute_still_emits_errors()`

Verify that `Reporter` at `MUTE` verbosity still outputs error messages.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_reporter:test_medium_emits_info_and_success_but_not_detail fingerprint=45c067950323a5746f4fd463459904b0cac10a32639cc3182a4984e4a08e46d8 body_fp=036c44ef7086065fcaa09e132d310c90cc59d40d3ce65a94875da7e198e22e1d -->
## `test_medium_emits_info_and_success_but_not_detail()`

Assert that `Verbosity.MEDIUM` outputs `info` and `success` messages but suppresses `detail`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_reporter:test_verbose_emits_everything fingerprint=cfd8de839612a0d19661908fd66e86f336b4b161357da402bdbdfcaccf1d5eb3 body_fp=4dabf2de9cc02cfbcbe9fb88d0ad8c91e8a545df65ff7bb344ba86a9346f96ad -->
## `test_verbose_emits_everything()`

Assert that `VERBOSE` verbosity causes both `info` and `detail` messages to appear in output.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_reporter:test_progress_mute_is_noop fingerprint=deb8d792e1bd6544688bbde543c548462bc87799076f74d0e03ba6e2f3b9c29a body_fp=61a4764abd981cf84f777766a50f135cd100abe70ed5b18732d3a889a39a56a3 -->
## `test_progress_mute_is_noop()`

Assert that `start_progress` under `Verbosity.MUTE` produces no console output despite file lifecycle calls.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_reporter:test_progress_medium_prints_finish_lines fingerprint=fe399880a95107a05afac2befdec9a6d1f5a69e10ac48f8ba85ea31f13739353 body_fp=cc1e5c326abc38b1014d20ee4f8b70dc1986f50c0d777d1f4ba7f5758cd168f3 -->
## `test_progress_medium_prints_finish_lines()`

Assert that `MEDIUM` verbosity progress emits filename, cost, and symbol count on file completion.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_reporter:test_progress_verbose_includes_token_detail fingerprint=9d32223d2b10e1e386f4b03806a754977ce0ec191190a5bc058a989b571d0a65 body_fp=c59d68bb16ff0d6620ffb025ec14987c5d087dc719a0d833366dc3b4743bab41 -->
## `test_progress_verbose_includes_token_detail()`

Assert that `VERBOSE` progress output includes token counts in `tok in/out` format.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_reporter:test_root_quiet_and_verbose_are_mutually_exclusive fingerprint=12ec037a8e879ad498003721a687247e59e8f6edf8c01e71e67eb34cb28d3025 body_fp=c47a156cbcca6f23bf31ea6ec416176932449ab860bce992eae1d59ae41b7779 -->
## `test_root_quiet_and_verbose_are_mutually_exclusive()`

Assert that passing `--quiet` and `--verbose` together exits with code 2 and a "mutually exclusive" error.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_reporter:test_root_version_still_works_with_verbosity_flags fingerprint=5ebb9f2d21656e52d546fcb380daa1d871633799b1be641ea740a7beb2ef265e body_fp=60034dd5df90c07a9812ef78b09ccf8b989f7e237488df8aa5c20386df090509 -->
## `test_root_version_still_works_with_verbosity_flags()`

Verify that `--version` succeeds and prints the app name when combined with `-v`.
<!-- trie:end -->