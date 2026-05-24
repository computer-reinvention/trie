---
trie_version: 0.1.2
source: tests/test_reporter.py
file_fingerprint: d6f396d10b0e62e4fbf237881ec75c8c98d6135f86e045160be8f316bdb164cf
last_synced_at: '2026-05-23T23:53:35Z'
defines:
- kind: module
  qualified_name: tests/test_reporter:__module__
  lines: 1-97
- kind: function
  qualified_name: tests/test_reporter:_make_reporter
  lines: 12-15
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
outgoing_refs: 11
---
<!-- trie:section symbol=tests/test_reporter:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=f73a39cf1b585f2bdfd3534e113cb8651b940f8a996188d94617ffabb3d2d6b6 source_ref=df741a005acc31e764a566519cdb2c64bda589ef -->
## `tests/test_reporter`

Test suite for `Reporter` verbosity levels, `ProgressHandle` output, and CLI verbosity flag plumbing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:_make_reporter fingerprint=44304bf94e6d49c89000ca5e595dd99f96ec8892f0358184b7d7ca51fb4da72c body_fp=ffdd9217b882b155ca7678740377fc1efd51016e41b01a6d3299a91060a415d3 source_ref=df741a005acc31e764a566519cdb2c64bda589ef -->
## `_make_reporter(level: Verbosity) -> tuple[Reporter, io.StringIO]`

Construct a `Reporter` wired to an in-memory buffer for output capture in tests.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_mute_suppresses_info_and_success fingerprint=f63e90635d0ad62f227a9b8d564b4d187a86cc47cd33366b448730a2d327eca7 body_fp=e4f2a3957e1839db82a1542253b2e50d85a9dd3f5fc1cb86f7af1ee51840e264 source_ref=df741a005acc31e764a566519cdb2c64bda589ef -->
## `test_mute_suppresses_info_and_success()`

Assert that `Reporter` at `Verbosity.MUTE` writes nothing for `info`, `success`, or `detail` calls.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_mute_still_emits_errors fingerprint=a7e2fa1d4951cdb11c6b26264cfd3101e79815e5b529673f4a8442c60569171f body_fp=f543b4502d38663671d030d108e45ec2f8dc3e7fa7f6212863714d5a0f1917c0 source_ref=df741a005acc31e764a566519cdb2c64bda589ef -->
## `test_mute_still_emits_errors()`

Verify that `Reporter` at `Verbosity.MUTE` still writes error messages to output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_medium_emits_info_and_success_but_not_detail fingerprint=45c067950323a5746f4fd463459904b0cac10a32639cc3182a4984e4a08e46d8 body_fp=036c44ef7086065fcaa09e132d310c90cc59d40d3ce65a94875da7e198e22e1d source_ref=df741a005acc31e764a566519cdb2c64bda589ef -->
## `test_medium_emits_info_and_success_but_not_detail()`

Assert that `Verbosity.MEDIUM` outputs `info` and `success` messages but suppresses `detail`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_verbose_emits_everything fingerprint=cfd8de839612a0d19661908fd66e86f336b4b161357da402bdbdfcaccf1d5eb3 body_fp=16983e907919ded05c00dcbabd86d962b661b7b281d2c4ef9c61a05d813845ad source_ref=df741a005acc31e764a566519cdb2c64bda589ef -->
## `test_verbose_emits_everything()`

Assert that `Reporter` at `Verbosity.VERBOSE` emits both `info` and `detail` messages.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_progress_mute_is_noop fingerprint=deb8d792e1bd6544688bbde543c548462bc87799076f74d0e03ba6e2f3b9c29a body_fp=f09489a93cfe55db20ae5ee33bce5ea506c771c88b3512c888fb7afe7cc187ea source_ref=df741a005acc31e764a566519cdb2c64bda589ef -->
## `test_progress_mute_is_noop()`

Assert that `Reporter` at `Verbosity.MUTE` produces no output for all `ProgressHandle` operations.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_progress_medium_prints_finish_lines fingerprint=fe399880a95107a05afac2befdec9a6d1f5a69e10ac48f8ba85ea31f13739353 body_fp=9e68770c724b4aca13a3d71f814878bd598bdf4bb7089eddee27c673874bc3a9 source_ref=df741a005acc31e764a566519cdb2c64bda589ef -->
## `test_progress_medium_prints_finish_lines()`

Assert that `MEDIUM` verbosity progress output includes filename, cost, and symbol count.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_progress_verbose_includes_token_detail fingerprint=9d32223d2b10e1e386f4b03806a754977ce0ec191190a5bc058a989b571d0a65 body_fp=481656b93d5da9abeab9113fdb4c6b9e15920fb3f0be1311fa5a89711fd19b95 source_ref=df741a005acc31e764a566519cdb2c64bda589ef -->
## `test_progress_verbose_includes_token_detail()`

Assert that `VERBOSE` progress output includes token in/out detail in `"tok 100/50"` format.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_root_quiet_and_verbose_are_mutually_exclusive fingerprint=12ec037a8e879ad498003721a687247e59e8f6edf8c01e71e67eb34cb28d3025 body_fp=1f96eacd8603db7f3f412136449fcba5fec279b05da6e7e8bdac48c6af9dd2e5 source_ref=df741a005acc31e764a566519cdb2c64bda589ef -->
## `test_root_quiet_and_verbose_are_mutually_exclusive()`

Assert that passing `--quiet` and `--verbose` together exits with code 2 and a "mutually exclusive" error message.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_root_version_still_works_with_verbosity_flags fingerprint=5ebb9f2d21656e52d546fcb380daa1d871633799b1be641ea740a7beb2ef265e body_fp=9dab56222518bc43e93663f81784720638e79687ac16fee934224ed7911f0f4a source_ref=df741a005acc31e764a566519cdb2c64bda589ef -->
## `test_root_version_still_works_with_verbosity_flags()`

Assert that `--version` succeeds and prints "trie" when combined with `-v`.
<!-- trie:end -->