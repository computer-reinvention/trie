---
trie_version: 0.1.5
source: tests/test_reporter.py
file_fingerprint: 2a312d540691237fe4d78d91e1298c168ea3453009e339901e94e9669a4eff48
last_synced_at: '2026-06-09T10:07:38Z'
defines:
- kind: module
  qualified_name: tests/test_reporter:__module__
  lines: 1-143
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
  qualified_name: tests/test_reporter:test_progress_marks_cascade_files
  lines: 82-93
- kind: function
  qualified_name: tests/test_reporter:test_progress_adapter_prints_plan_header_and_section_separators
  lines: 96-115
- kind: function
  qualified_name: tests/test_reporter:test_progress_adapter_plan_is_silent_when_nothing_to_sync
  lines: 118-125
- kind: function
  qualified_name: tests/test_reporter:test_root_quiet_and_verbose_are_mutually_exclusive
  lines: 131-135
- kind: function
  qualified_name: tests/test_reporter:test_root_version_still_works_with_verbosity_flags
  lines: 138-142
incoming_refs: 0
outgoing_refs: 14
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
<!-- trie:section symbol=tests/test_reporter:test_mute_suppresses_info_and_success fingerprint=f63e90635d0ad62f227a9b8d564b4d187a86cc47cd33366b448730a2d327eca7 body_fp=888100b3ad2cbca6e995972ade7c5da25810cf67ed5f9e6d956a1bcc0db67c5b source_ref=df741a005acc31e764a566519cdb2c64bda589ef role=test-infrastructure -->
Verifies that Reporter with MUTE verbosity suppresses info, success, and detail messages.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_mute_still_emits_errors fingerprint=a7e2fa1d4951cdb11c6b26264cfd3101e79815e5b529673f4a8442c60569171f body_fp=6efde0b22762af16dc57625e4c69387dc3d014ac78fd323ec72bb6dcce626b19 source_ref=df741a005acc31e764a566519cdb2c64bda589ef role=test-infrastructure -->
Verifies that Reporter with MUTE verbosity still outputs error messages despite suppressing other output types.
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
<!-- trie:section symbol=tests/test_reporter:test_progress_adapter_prints_plan_header_and_section_separators fingerprint=14c1be964a148c7de54e5e5fe16096e891205e13b5555dbee9a8e06097533ecd body_fp=4ce95c2df5604b6b6d065318879bb99fb2955272717228cc0158addef1281425 source_ref=996d2328867a89c082141e47e065fa13da717a8d role=test -->
Tests that _ProgressAdapter emits plan headers and section separators with proper formatting and labels.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_progress_adapter_plan_is_silent_when_nothing_to_sync fingerprint=e8c27274f61b673117fc3274337aeafead20a3462ddff91a582aff8774b9b59e body_fp=b26150d7b960a86ec996dc943b3f07bd0107ea35ab8410028065f1e102a0fada source_ref=996d2328867a89c082141e47e065fa13da717a8d role=test -->
Tests that `_ProgressAdapter` produces no output when the plan contains zero files to sync.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_root_quiet_and_verbose_are_mutually_exclusive fingerprint=12ec037a8e879ad498003721a687247e59e8f6edf8c01e71e67eb34cb28d3025 body_fp=1e58c13470b9c6d1b035a0734fbd34f0946e0c9a9a0131f2d5296e44213ab227 source_ref=df741a005acc31e764a566519cdb2c64bda589ef role=test-infrastructure -->
Tests that the CLI app rejects simultaneous --quiet and --verbose flags with exit code 2.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_root_version_still_works_with_verbosity_flags fingerprint=5ebb9f2d21656e52d546fcb380daa1d871633799b1be641ea740a7beb2ef265e body_fp=5be24f7cd8a059ac80bb4295414225b338b235b53aa0c3daebe9df12aab98a08 source_ref=df741a005acc31e764a566519cdb2c64bda589ef role=test-infrastructure -->
Tests that CLI version flag works correctly when combined with verbosity flags.
<!-- trie:end -->