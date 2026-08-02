---
trie_version: 0.3.0
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
  signature: 'def _make_reporter(level: Verbosity) -> tuple[Reporter, io.StringIO]'
- kind: function
  qualified_name: tests/test_reporter:_make_reporter_with_stderr
  lines: 18-23
  signature: 'def _make_reporter_with_stderr(level: Verbosity) -> tuple[Reporter, io.StringIO, io.StringIO]'
- kind: function
  qualified_name: tests/test_reporter:test_mute_suppresses_info_and_success
  lines: 26-31
  signature: def test_mute_suppresses_info_and_success()
- kind: function
  qualified_name: tests/test_reporter:test_mute_still_emits_errors
  lines: 34-37
  signature: def test_mute_still_emits_errors()
- kind: function
  qualified_name: tests/test_reporter:test_errors_go_to_stderr_not_stdout
  lines: 40-46
  signature: 'def test_errors_go_to_stderr_not_stdout(): # Subprocess wrappers (e.g. the opencode tool overrides) surface stderr # on failure; errors must land there, not on the stdout console.'
- kind: function
  qualified_name: tests/test_reporter:test_medium_emits_info_and_success_but_not_detail
  lines: 49-57
  signature: def test_medium_emits_info_and_success_but_not_detail()
- kind: function
  qualified_name: tests/test_reporter:test_verbose_emits_everything
  lines: 60-66
  signature: def test_verbose_emits_everything()
- kind: function
  qualified_name: tests/test_reporter:test_progress_mute_is_noop
  lines: 69-76
  signature: def test_progress_mute_is_noop()
- kind: function
  qualified_name: tests/test_reporter:test_progress_medium_prints_finish_lines
  lines: 79-87
  signature: def test_progress_medium_prints_finish_lines()
- kind: function
  qualified_name: tests/test_reporter:test_progress_verbose_includes_token_detail
  lines: 90-96
  signature: def test_progress_verbose_includes_token_detail()
- kind: function
  qualified_name: tests/test_reporter:test_progress_marks_cascade_files
  lines: 99-110
  signature: def test_progress_marks_cascade_files()
- kind: function
  qualified_name: tests/test_reporter:test_progress_adapter_prints_plan_header_and_section_separators
  lines: 113-132
  signature: def test_progress_adapter_prints_plan_header_and_section_separators()
- kind: function
  qualified_name: tests/test_reporter:test_progress_adapter_plan_is_silent_when_nothing_to_sync
  lines: 135-142
  signature: def test_progress_adapter_plan_is_silent_when_nothing_to_sync()
- kind: function
  qualified_name: tests/test_reporter:test_root_quiet_and_verbose_are_mutually_exclusive
  lines: 148-152
  signature: def test_root_quiet_and_verbose_are_mutually_exclusive()
- kind: function
  qualified_name: tests/test_reporter:test_root_version_still_works_with_verbosity_flags
  lines: 155-159
  signature: def test_root_version_still_works_with_verbosity_flags()
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
<!-- trie:section symbol=tests/test_reporter:_make_reporter fingerprint=44304bf94e6d49c89000ca5e595dd99f96ec8892f0358184b7d7ca51fb4da72c body_fp=98a1fb3264ad2f032f4755e3ac5c409d7984202ceb6a10d25b88d76e515a6b26 source_ref=5e48c05b6f5e1bb204453e3c25d35cc90260bfa1 role=test -->
## `def _make_reporter(level: Verbosity) -> tuple[Reporter, io.StringIO]`

Creates a Reporter instance with a string buffer console for testing purposes.

- Returns Reporter configured with given verbosity level and a StringIO buffer for capturing output
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:_make_reporter_with_stderr fingerprint=6096e5e51f6e4b433bae31820706b59e85ab319c3a3883521dd09d165e5e3069 body_fp=32b7ddce84f33768cd6245e3e2cd4ec2f9bffdd6e7dc69f89f378f2189821300 source_ref=924ac6da38ef7268ebeb8333be41cc9bf62c78d7 role=test -->
## `def _make_reporter_with_stderr(level: Verbosity) -> tuple[Reporter, io.StringIO, io.StringIO]`

Create a `Reporter` with separate stdout and stderr `StringIO` buffers for the given `Verbosity` level, returning all three.

- `returns` — `(reporter, out_buf, err_buf)` tuple for asserting channel separation
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_mute_suppresses_info_and_success fingerprint=f63e90635d0ad62f227a9b8d564b4d187a86cc47cd33366b448730a2d327eca7 body_fp=97f1d719fff808c547a5738131c6b901e909c3350b6928bed90c4611886a207f source_ref=df741a005acc31e764a566519cdb2c64bda589ef role=test-infrastructure -->
## `def test_mute_suppresses_info_and_success()`

Verifies that Reporter with MUTE verbosity suppresses info, success, and detail messages.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_mute_still_emits_errors fingerprint=d78cf44bbe3eaad650bd9aef8567186b5f60d24ac911dbb4f51fbc655b2464a8 body_fp=764c6b09bb86b017fee336a9a18dd8740318db9ce6883938e7f251a9a05a0664 source_ref=924ac6da38ef7268ebeb8333be41cc9bf62c78d7 role=test -->
## `def test_mute_still_emits_errors()`

Verifies that Reporter with MUTE verbosity still outputs error messages to stderr despite suppressing other output types.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_errors_go_to_stderr_not_stdout fingerprint=2b07e69584f55ab544c63df9addbbda11de4c778d60492e0108ac8c253e6e72d body_fp=2d63fa655b8e3e4ebf71f6ed4ac045223d8325e89d4503587ec7845d4956871c source_ref=924ac6da38ef7268ebeb8333be41cc9bf62c78d7 role=test -->
## `def test_errors_go_to_stderr_not_stdout(): # Subprocess wrappers (e.g. the opencode tool overrides) surface stderr # on failure; errors must land there, not on the stdout console.`

Assert that `Reporter.error` writes to stderr and not stdout under `Verbosity.MEDIUM`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_medium_emits_info_and_success_but_not_detail fingerprint=45c067950323a5746f4fd463459904b0cac10a32639cc3182a4984e4a08e46d8 body_fp=db4c94a83ca6aa707d8a09cb503841273788d38e2fd14b0e787fc852c5b608ed source_ref=df741a005acc31e764a566519cdb2c64bda589ef role=test-infrastructure -->
## `def test_medium_emits_info_and_success_but_not_detail()`

Tests that Reporter with medium verbosity outputs info and success messages but suppresses detail messages.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_verbose_emits_everything fingerprint=cfd8de839612a0d19661908fd66e86f336b4b161357da402bdbdfcaccf1d5eb3 body_fp=bf668f58da2d95145bcc386bc80fd83e627cf950afc3ecb1b824044dac8afd29 source_ref=df741a005acc31e764a566519cdb2c64bda589ef role=test-infrastructure -->
## `def test_verbose_emits_everything()`

Verifies that Reporter with VERBOSE verbosity outputs both info and detail messages.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_progress_mute_is_noop fingerprint=deb8d792e1bd6544688bbde543c548462bc87799076f74d0e03ba6e2f3b9c29a body_fp=18f3868b6413382964d7d33a17691545ec87b974930b90b823b2ea898866ccf6 source_ref=5e48c05b6f5e1bb204453e3c25d35cc90260bfa1 role=test -->
## `def test_progress_mute_is_noop()`

Tests that Reporter progress operations produce no output when verbosity is MUTE.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_progress_medium_prints_finish_lines fingerprint=fe399880a95107a05afac2befdec9a6d1f5a69e10ac48f8ba85ea31f13739353 body_fp=0cec53b9e1fe7106a710d5c7de9f71f3a49cbc2cabc345fabccc9efa8b352088 source_ref=df741a005acc31e764a566519cdb2c64bda589ef role=test-infrastructure -->
## `def test_progress_medium_prints_finish_lines()`

Tests that MEDIUM verbosity level shows file completion lines with cost and symbol count.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_progress_verbose_includes_token_detail fingerprint=9d32223d2b10e1e386f4b03806a754977ce0ec191190a5bc058a989b571d0a65 body_fp=d06763bf72758df97e2d33662396de28074c91b3d4791f14ad757a7ad753bcdf source_ref=df741a005acc31e764a566519cdb2c64bda589ef role=test-infrastructure -->
## `def test_progress_verbose_includes_token_detail()`

Tests that Reporter in verbose mode includes token input/output counts in progress file completion messages.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_progress_marks_cascade_files fingerprint=944720a995eb0b02425521b59ff4ed80094e06132a12dc5576e0d86e72cb0e5a body_fp=f248135fdefa81e0ac0c8ae3511ed97a19396e8a880f093c66fb64ada71ae14c source_ref=5e48c05b6f5e1bb204453e3c25d35cc90260bfa1 role=test -->
## `def test_progress_marks_cascade_files()`

Verifies that Reporter marks cascade files with "(cascade)" label while direct files show no label.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_progress_adapter_prints_plan_header_and_section_separators fingerprint=14c1be964a148c7de54e5e5fe16096e891205e13b5555dbee9a8e06097533ecd body_fp=24fe0f1407a4104403d100ad3caa8e0d4229bea57a660a1c452ef46a42753d57 source_ref=924ac6da38ef7268ebeb8333be41cc9bf62c78d7 role=test -->
## `def test_progress_adapter_prints_plan_header_and_section_separators()`

Tests that `_ProgressAdapter` emits plan headers and section separators with proper formatting and labels.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_progress_adapter_plan_is_silent_when_nothing_to_sync fingerprint=e8c27274f61b673117fc3274337aeafead20a3462ddff91a582aff8774b9b59e body_fp=136f10addeb0987f8a0961b61e368fd86d6d4a09c736b8874e1607f2649728dc source_ref=924ac6da38ef7268ebeb8333be41cc9bf62c78d7 role=test -->
## `def test_progress_adapter_plan_is_silent_when_nothing_to_sync()`

Tests that `_ProgressAdapter` produces no output when the plan contains zero files to sync.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_root_quiet_and_verbose_are_mutually_exclusive fingerprint=12ec037a8e879ad498003721a687247e59e8f6edf8c01e71e67eb34cb28d3025 body_fp=20e2f4e11122de88e26c922ecaa4e0863845f765ebb6464c8572c6aee1a14566 source_ref=df741a005acc31e764a566519cdb2c64bda589ef role=test-infrastructure -->
## `def test_root_quiet_and_verbose_are_mutually_exclusive()`

Tests that the CLI app rejects simultaneous --quiet and --verbose flags with exit code 2.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_reporter:test_root_version_still_works_with_verbosity_flags fingerprint=5ebb9f2d21656e52d546fcb380daa1d871633799b1be641ea740a7beb2ef265e body_fp=54287ec287340c65a4ac52f5c9efd1c2373db5a7c18c0f7406bed95c81a4f1ea source_ref=df741a005acc31e764a566519cdb2c64bda589ef role=test-infrastructure -->
## `def test_root_version_still_works_with_verbosity_flags()`

Tests that CLI version flag works correctly when combined with verbosity flags.
<!-- trie:end -->