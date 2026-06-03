---
trie_version: 0.1.5
source: tests/test_reporter.py
file_fingerprint: d6f396d10b0e62e4fbf237881ec75c8c98d6135f86e045160be8f316bdb164cf
last_synced_at: '2026-06-03T21:00:14Z'
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
<!-- trie:section symbol=tests/test_reporter:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=fa430be3ec87445f293f027c2caea83ff425a3a5b12a05014e7d843942d78fdb source_ref=df741a005acc31e764a566519cdb2c64bda589ef -->
Tests the Reporter class and CLI verbosity handling across different output levels.

- `_make_reporter()`: Creates Reporter instance with StringIO buffer for testing output capture
- Tests verify mute/medium/verbose verbosity levels control which messages are emitted
- Progress handle tests ensure file processing output matches verbosity settings
- CLI flag tests validate --quiet and --verbose are mutually exclusive
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:_make_reporter fingerprint=44304bf94e6d49c89000ca5e595dd99f96ec8892f0358184b7d7ca51fb4da72c body_fp=af7f882a5823772308c1053ea6ae1df8653499ea4b50ebaa4ba5f7d0f7f0ebaa source_ref=df741a005acc31e764a566519cdb2c64bda589ef -->
Creates a Reporter instance with specified verbosity level and a string buffer for capturing output.

- Returns tuple of (Reporter, StringIO buffer) for testing output verification
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_mute_suppresses_info_and_success fingerprint=f63e90635d0ad62f227a9b8d564b4d187a86cc47cd33366b448730a2d327eca7 body_fp=888100b3ad2cbca6e995972ade7c5da25810cf67ed5f9e6d956a1bcc0db67c5b source_ref=df741a005acc31e764a566519cdb2c64bda589ef -->
Verifies that Reporter with MUTE verbosity suppresses info, success, and detail messages.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_mute_still_emits_errors fingerprint=a7e2fa1d4951cdb11c6b26264cfd3101e79815e5b529673f4a8442c60569171f body_fp=6efde0b22762af16dc57625e4c69387dc3d014ac78fd323ec72bb6dcce626b19 source_ref=df741a005acc31e764a566519cdb2c64bda589ef -->
Verifies that Reporter with MUTE verbosity still outputs error messages despite suppressing other output types.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_medium_emits_info_and_success_but_not_detail fingerprint=45c067950323a5746f4fd463459904b0cac10a32639cc3182a4984e4a08e46d8 body_fp=3e0707280e03c87b9853987913da624121bc8274f1fcfe2c9a063a3d90d0b90d source_ref=df741a005acc31e764a566519cdb2c64bda589ef -->
Tests that Reporter with medium verbosity outputs info and success messages but suppresses detail messages.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_verbose_emits_everything fingerprint=cfd8de839612a0d19661908fd66e86f336b4b161357da402bdbdfcaccf1d5eb3 body_fp=d72c9fca9056f14153617e5685370d3ab6d1449194a97f34d4fb506a6198fdd5 source_ref=df741a005acc31e764a566519cdb2c64bda589ef -->
Verifies that Reporter with VERBOSE verbosity outputs both info and detail messages.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_progress_mute_is_noop fingerprint=deb8d792e1bd6544688bbde543c548462bc87799076f74d0e03ba6e2f3b9c29a body_fp=a0aa1c5b48e81dfc1280a8e6b9915923929ded5862271dc7105a97c8687cb76e source_ref=df741a005acc31e764a566519cdb2c64bda589ef -->
Verifies that progress tracking operations produce no output when Reporter verbosity is set to MUTE.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_progress_medium_prints_finish_lines fingerprint=fe399880a95107a05afac2befdec9a6d1f5a69e10ac48f8ba85ea31f13739353 body_fp=925fc756586bc333a0ec1986310ca7949734ff225d8d1d44641a346b1573036f source_ref=df741a005acc31e764a566519cdb2c64bda589ef -->
Tests that MEDIUM verbosity level shows file completion lines with cost and symbol count.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_progress_verbose_includes_token_detail fingerprint=9d32223d2b10e1e386f4b03806a754977ce0ec191190a5bc058a989b571d0a65 body_fp=dbbdc11e6c4a04772a8712981aee6aef261112f602bb9e16074473a3ddf1ce6b source_ref=df741a005acc31e764a566519cdb2c64bda589ef -->
Tests that Reporter in verbose mode includes token input/output counts in progress file completion messages.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_root_quiet_and_verbose_are_mutually_exclusive fingerprint=12ec037a8e879ad498003721a687247e59e8f6edf8c01e71e67eb34cb28d3025 body_fp=1e58c13470b9c6d1b035a0734fbd34f0946e0c9a9a0131f2d5296e44213ab227 source_ref=df741a005acc31e764a566519cdb2c64bda589ef -->
Tests that the CLI app rejects simultaneous --quiet and --verbose flags with exit code 2.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_root_version_still_works_with_verbosity_flags fingerprint=5ebb9f2d21656e52d546fcb380daa1d871633799b1be641ea740a7beb2ef265e body_fp=5be24f7cd8a059ac80bb4295414225b338b235b53aa0c3daebe9df12aab98a08 source_ref=df741a005acc31e764a566519cdb2c64bda589ef -->
Tests that CLI version flag works correctly when combined with verbosity flags.
<!-- trie:end -->