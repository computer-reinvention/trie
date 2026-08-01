---
trie_version: 0.2.1
source: tests/test_reporter.py
file_fingerprint: 2687fddcd8fd3190739e2dfc9f7de9cc4c857a52f2ef14254e74a34b8f2eab2b
last_synced_at: '2026-08-01T09:20:36Z'
defines:
- kind: module
  qualified_name: tests/test_reporter:__module__
  lines: 1-160
- kind: function
  qualified_name: tests/test_reporter:_make_reporter
  lines: 12-15
- kind: function
  qualified_name: tests/test_reporter:_make_reporter_with_stderr
  lines: 18-23
- kind: function
  qualified_name: tests/test_reporter:test_mute_suppresses_info_and_success
  lines: 26-31
- kind: function
  qualified_name: tests/test_reporter:test_mute_still_emits_errors
  lines: 34-37
- kind: function
  qualified_name: tests/test_reporter:test_errors_go_to_stderr_not_stdout
  lines: 40-46
- kind: function
  qualified_name: tests/test_reporter:test_medium_emits_info_and_success_but_not_detail
  lines: 49-57
- kind: function
  qualified_name: tests/test_reporter:test_verbose_emits_everything
  lines: 60-66
- kind: function
  qualified_name: tests/test_reporter:test_progress_mute_is_noop
  lines: 69-76
- kind: function
  qualified_name: tests/test_reporter:test_progress_medium_prints_finish_lines
  lines: 79-87
- kind: function
  qualified_name: tests/test_reporter:test_progress_verbose_includes_token_detail
  lines: 90-96
- kind: function
  qualified_name: tests/test_reporter:test_progress_marks_cascade_files
  lines: 99-110
- kind: function
  qualified_name: tests/test_reporter:test_progress_adapter_prints_plan_header_and_section_separators
  lines: 113-132
- kind: function
  qualified_name: tests/test_reporter:test_progress_adapter_plan_is_silent_when_nothing_to_sync
  lines: 135-142
- kind: function
  qualified_name: tests/test_reporter:test_root_quiet_and_verbose_are_mutually_exclusive
  lines: 148-152
- kind: function
  qualified_name: tests/test_reporter:test_root_version_still_works_with_verbosity_flags
  lines: 155-159
incoming_refs: 0
outgoing_refs: 47
---
<!-- trie:section symbol=tests/test_reporter:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=fa430be3ec87445f293f027c2caea83ff425a3a5b12a05014e7d843942d78fdb source_ref=df741a005acc31e764a566519cdb2c64bda589ef role=test-infrastructure -->
Tests the Reporter class and CLI verbosity handling across different output levels.

- `_make_reporter()`: Creates Reporter instance with StringIO buffer for testing output capture
- Tests verify mute/medium/verbose verbosity levels control which messages are emitted
- Progress handle tests ensure file processing output matches verbosity settings
- CLI flag tests validate --quiet and --verbose are mutually exclusive
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:_make_reporter fingerprint=44304bf94e6d49c89000ca5e595dd99f96ec8892f0358184b7d7ca51fb4da72c body_fp=d8f2418d457d03e9afebac42f9e9f3bae2aceb2cf04c3431cc238830a158ea69 source_ref=5e48c05b6f5e1bb204453e3c25d35cc90260bfa1 role=test -->
Creates a Reporter instance with a string buffer console for testing purposes.

- Returns Reporter configured with given verbosity level and a StringIO buffer for capturing output
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:_make_reporter_with_stderr fingerprint=6096e5e51f6e4b433bae31820706b59e85ab319c3a3883521dd09d165e5e3069 body_fp=58ab1af98b9984286f2e08f1c9e253a06271d688ffff4050c3d6a3d92e8978ac source_ref=924ac6da38ef7268ebeb8333be41cc9bf62c78d7 role=test -->
Create a `Reporter` with separate stdout and stderr `StringIO` buffers for the given `Verbosity` level, returning all three.

- `returns` — `(reporter, out_buf, err_buf)` tuple for asserting channel separation
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_mute_suppresses_info_and_success fingerprint=f63e90635d0ad62f227a9b8d564b4d187a86cc47cd33366b448730a2d327eca7 body_fp=888100b3ad2cbca6e995972ade7c5da25810cf67ed5f9e6d956a1bcc0db67c5b source_ref=df741a005acc31e764a566519cdb2c64bda589ef role=test-infrastructure -->
Verifies that Reporter with MUTE verbosity suppresses info, success, and detail messages.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_mute_still_emits_errors fingerprint=d78cf44bbe3eaad650bd9aef8567186b5f60d24ac911dbb4f51fbc655b2464a8 body_fp=b0eaed99636682addaefb208b25b0a91eeaafcd5b9d99a9c571cc08be77e3b33 source_ref=924ac6da38ef7268ebeb8333be41cc9bf62c78d7 role=test -->
Verifies that Reporter with MUTE verbosity still outputs error messages to stderr despite suppressing other output types.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_errors_go_to_stderr_not_stdout fingerprint=2b07e69584f55ab544c63df9addbbda11de4c778d60492e0108ac8c253e6e72d body_fp=31ce075bc7d3c26401a54c0e3c1e36e043e2d103b1fdc7141aee207fc2a6751a source_ref=924ac6da38ef7268ebeb8333be41cc9bf62c78d7 role=test -->
Assert that `Reporter.error` writes to stderr and not stdout under `Verbosity.MEDIUM`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_medium_emits_info_and_success_but_not_detail fingerprint=45c067950323a5746f4fd463459904b0cac10a32639cc3182a4984e4a08e46d8 body_fp=3e0707280e03c87b9853987913da624121bc8274f1fcfe2c9a063a3d90d0b90d source_ref=df741a005acc31e764a566519cdb2c64bda589ef role=test-infrastructure -->
Tests that Reporter with medium verbosity outputs info and success messages but suppresses detail messages.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_verbose_emits_everything fingerprint=cfd8de839612a0d19661908fd66e86f336b4b161357da402bdbdfcaccf1d5eb3 body_fp=d72c9fca9056f14153617e5685370d3ab6d1449194a97f34d4fb506a6198fdd5 source_ref=df741a005acc31e764a566519cdb2c64bda589ef role=test-infrastructure -->
Verifies that Reporter with VERBOSE verbosity outputs both info and detail messages.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_progress_mute_is_noop fingerprint=deb8d792e1bd6544688bbde543c548462bc87799076f74d0e03ba6e2f3b9c29a body_fp=66e38729e9c37c2b18b37c915df3fa758945295feaebc125177a4b2497727cfd source_ref=5e48c05b6f5e1bb204453e3c25d35cc90260bfa1 role=test -->
Tests that Reporter progress operations produce no output when verbosity is MUTE.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_progress_medium_prints_finish_lines fingerprint=fe399880a95107a05afac2befdec9a6d1f5a69e10ac48f8ba85ea31f13739353 body_fp=925fc756586bc333a0ec1986310ca7949734ff225d8d1d44641a346b1573036f source_ref=df741a005acc31e764a566519cdb2c64bda589ef role=test-infrastructure -->
Tests that MEDIUM verbosity level shows file completion lines with cost and symbol count.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_progress_verbose_includes_token_detail fingerprint=9d32223d2b10e1e386f4b03806a754977ce0ec191190a5bc058a989b571d0a65 body_fp=dbbdc11e6c4a04772a8712981aee6aef261112f602bb9e16074473a3ddf1ce6b source_ref=df741a005acc31e764a566519cdb2c64bda589ef role=test-infrastructure -->
Tests that Reporter in verbose mode includes token input/output counts in progress file completion messages.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_progress_marks_cascade_files fingerprint=944720a995eb0b02425521b59ff4ed80094e06132a12dc5576e0d86e72cb0e5a body_fp=409492796a6a06e5fa3e0e62a05390410edddac04919a0231e2f169428b2c205 source_ref=5e48c05b6f5e1bb204453e3c25d35cc90260bfa1 role=test -->
Verifies that Reporter marks cascade files with "(cascade)" label while direct files show no label.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_progress_adapter_prints_plan_header_and_section_separators fingerprint=14c1be964a148c7de54e5e5fe16096e891205e13b5555dbee9a8e06097533ecd body_fp=588db6c3af8f5b1916b2ac7ce707134e5c8b60e5b54ab67a23363486213ff34e source_ref=924ac6da38ef7268ebeb8333be41cc9bf62c78d7 role=test -->
Tests that `_ProgressAdapter` emits plan headers and section separators with proper formatting and labels.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_progress_adapter_plan_is_silent_when_nothing_to_sync fingerprint=e8c27274f61b673117fc3274337aeafead20a3462ddff91a582aff8774b9b59e body_fp=b26150d7b960a86ec996dc943b3f07bd0107ea35ab8410028065f1e102a0fada source_ref=924ac6da38ef7268ebeb8333be41cc9bf62c78d7 role=test -->
Tests that `_ProgressAdapter` produces no output when the plan contains zero files to sync.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_root_quiet_and_verbose_are_mutually_exclusive fingerprint=12ec037a8e879ad498003721a687247e59e8f6edf8c01e71e67eb34cb28d3025 body_fp=1e58c13470b9c6d1b035a0734fbd34f0946e0c9a9a0131f2d5296e44213ab227 source_ref=df741a005acc31e764a566519cdb2c64bda589ef role=test-infrastructure -->
Tests that the CLI app rejects simultaneous --quiet and --verbose flags with exit code 2.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_root_version_still_works_with_verbosity_flags fingerprint=5ebb9f2d21656e52d546fcb380daa1d871633799b1be641ea740a7beb2ef265e body_fp=5be24f7cd8a059ac80bb4295414225b338b235b53aa0c3daebe9df12aab98a08 source_ref=df741a005acc31e764a566519cdb2c64bda589ef role=test-infrastructure -->
Tests that CLI version flag works correctly when combined with verbosity flags.
<!-- trie:end -->