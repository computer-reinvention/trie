---
trie_version: 0.3.0
source: tests/test_check.py
file_fingerprint: e15bc328b0061088438e35ef3f6d2525dbdeacc17cfdbaeed2d978ac887eb031
last_synced_at: '2026-08-01T01:52:37Z'
defines:
- kind: module
  qualified_name: tests/test_check:__module__
  lines: 1-216
- kind: function
  qualified_name: tests/test_check:project
  lines: 16-28
  signature: 'def project(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_check:_sync_all
  lines: 31-34
  signature: 'def _sync_all(project: Path) -> None'
- kind: function
  qualified_name: tests/test_check:test_clean_after_fresh_sync
  lines: 37-41
  signature: 'def test_clean_after_fresh_sync(project: Path)'
- kind: function
  qualified_name: tests/test_check:test_missing_triefact_detected
  lines: 44-50
  signature: 'def test_missing_triefact_detected(project: Path): # No triefacts generated at all'
- kind: function
  qualified_name: tests/test_check:test_stale_section_detected
  lines: 53-60
  signature: 'def test_stale_section_detected(project: Path)'
- kind: function
  qualified_name: tests/test_check:test_missing_section_detected
  lines: 63-72
  signature: 'def test_missing_section_detected(project: Path)'
- kind: function
  qualified_name: tests/test_check:test_orphan_section_detected
  lines: 75-84
  signature: 'def test_orphan_section_detected(project: Path)'
- kind: function
  qualified_name: tests/test_check:test_private_only_file_requires_a_triefact
  lines: 87-98
  signature: 'def test_private_only_file_requires_a_triefact(project: Path)'
- kind: function
  qualified_name: tests/test_check:test_file_with_no_parser_surfaced_symbols_needs_no_triefact
  lines: 101-112
  signature: 'def test_file_with_no_parser_surfaced_symbols_needs_no_triefact(project: Path)'
- kind: function
  qualified_name: tests/test_check:test_clean_when_all_in_sync_with_human_prose
  lines: 115-123
  signature: 'def test_clean_when_all_in_sync_with_human_prose(project: Path)'
- kind: function
  qualified_name: tests/test_check:test_cli_verify_exits_zero_when_clean
  lines: 126-132
  signature: 'def test_cli_verify_exits_zero_when_clean(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_check:test_cli_verify_exits_nonzero_when_stale
  lines: 135-143
  signature: 'def test_cli_verify_exits_nonzero_when_stale(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_check:test_cli_verify_quiet_mode
  lines: 146-157
  signature: 'def test_cli_verify_quiet_mode(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_check:test_cli_verify_detects_tampered_body
  lines: 160-177
  signature: 'def test_cli_verify_detects_tampered_body(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_check:test_check_project_detects_tampered_body
  lines: 180-194
  signature: 'def test_check_project_detects_tampered_body(project: Path)'
- kind: function
  qualified_name: tests/test_check:test_check_project_detects_legacy_section
  lines: 197-215
  signature: 'def test_check_project_detects_legacy_section(project: Path)'
incoming_refs: 0
outgoing_refs: 45
---
<!-- trie:section symbol=tests/test_check:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=97308f7817fb8c482d92ae937b7891d355b4fe238363f0ab657692b451bf851b source_ref=647efc202801e8ab3384c135027857bcb77efcb4 role=test-infrastructure -->
Test suite for trie's check functionality that detects stale triefacts and synchronization issues.

- **project**: Creates temporary project structure with trie.toml config and sample Python files
- **test_clean_after_fresh_sync**: Verifies freshly synced project reports clean status
- **test_missing_triefact_detected**: Checks detection when no triefacts exist for source files
- **test_stale_section_detected**: Validates identification of outdated triefact sections after source changes
- **test_missing_section_detected**: Tests detection of new symbols not yet documented
- **test_orphan_section_detected**: Confirms identification of triefact sections for deleted symbols
- **test_private_only_file_requires_a_triefact**: Ensures files with only underscore-prefixed symbols still need documentation
- **test_file_with_no_parser_surfaced_symbols_needs_no_triefact**: Verifies import-only files are excluded from checks
- **test_clean_when_all_in_sync_with_human_prose**: Confirms hand-written content doesn't trigger false positives
- **test_cli_verify_exits_zero_when_clean**: Tests CLI verify command success on clean projects
- **test_cli_verify_exits_nonzero_when_stale**: Tests CLI verify command failure on stale projects
- **test_cli_verify_quiet_mode**: Validates quiet flag suppresses detailed output while preserving summary
- **test_cli_verify_detects_tampered_body**: Tests detection of manually edited triefact content
- **test_check_project_detects_tampered_body**: Unit test for tampered body detection
- **test_check_project_detects_legacy_section**: Tests identification of pre-fingerprint triefact sections
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:project fingerprint=6c084affeb9451e9736e35692da0379b565f57e450c09c6aba378a475b9970df body_fp=6687333e38156cd1335111960b8673e421efdcf7427dc5537e36f6bda7477bf6 source_ref=647efc202801e8ab3384c135027857bcb77efcb4 role=test-infrastructure -->
## `def project(tmp_path: Path) -> Path`

Creates a temporary test project with configuration and sample Python files for trie functionality tests.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:_sync_all fingerprint=2319aaf7307a31aa136e06ddb84dd261f6ef7fdbb25fbcfbda6b959c3a11d06d body_fp=4ea91056b3b4268af1ed97e0e2a9464fc1c630a3d1ffb5bba7d44093d70fd11e source_ref=647efc202801e8ab3384c135027857bcb77efcb4 role=test-infrastructure -->
## `def _sync_all(project: Path) -> None`

Synchronizes all Python files in a test project's src directory using a fake client.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_clean_after_fresh_sync fingerprint=13234c9b3bc113d2f6251099e2ed19680cbd1fec19486fcfd1f2ee688dd6877d body_fp=de3d555b5ec37453104a4ec6e38db313d00524f84017bd2015d5794e0d652485 source_ref=30105b810f8b90b700150c01e3775337b5f88dda role=test -->
## `def test_clean_after_fresh_sync(project: Path)`

Verifies that `check_project` reports clean status after synchronizing all files in a test project.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_missing_triefact_detected fingerprint=198beaed352ba1847c55b9b432a978f034dd94e3c19901ab32419c89cde856e4 body_fp=f6a9efe842a7d1bb3bf85ed621b5547ac62763946b860ee555a6145b6690043e source_ref=30105b810f8b90b700150c01e3775337b5f88dda role=test -->
## `def test_missing_triefact_detected(project: Path): # No triefacts generated at all`

Tests that `check_project` detects when no triefacts exist for source symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_stale_section_detected fingerprint=90186c99480bfe6049209b581e100daba72eae24b8cba2c726aa6b104934f5d9 body_fp=88a0c97d7a9ea0f4e6b0600bc25585c50638240ab69990a9a5b1fa25bc12580e source_ref=30105b810f8b90b700150c01e3775337b5f88dda role=test -->
## `def test_stale_section_detected(project: Path)`

Verifies that `check_project` detects stale triefact sections after source code changes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_missing_section_detected fingerprint=474be3f403d0bc036a4e3b21eaa0aa313c358d28ce4173c0b1d0ede526d616de body_fp=6c5ffb9be386c7ea7004242486065d290097e37c48952957d9b1f6bc9d70c9f3 source_ref=30105b810f8b90b700150c01e3775337b5f88dda role=test -->
## `def test_missing_section_detected(project: Path)`

Tests that `check_project` detects when a new symbol in source code lacks a corresponding triefact section.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_orphan_section_detected fingerprint=fa609789a15518cf4c7d41859858f0a90c64b76d6872c4b0a50099bbf1e2c602 body_fp=b1ac78b79a3c93bc30c416dfb409ce4573e9af8c1a85d14a2965c533d6ed6d93 source_ref=30105b810f8b90b700150c01e3775337b5f88dda role=test -->
## `def test_orphan_section_detected(project: Path)`

Tests that `check_project` detects orphan sections when source symbol is deleted but triefact section remains.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_private_only_file_requires_a_triefact fingerprint=98ffaaffbffb6147cea08a7a5a60f8def21a95b776735ea3669398bf858f7064 body_fp=38061eb5f857147485a259e16c212c7d01ef047565d23553b6c62f0d48e193b0 source_ref=30105b810f8b90b700150c01e3775337b5f88dda role=test -->
## `def test_private_only_file_requires_a_triefact(project: Path)`

Verifies that files containing only underscore-prefixed symbols still trigger MISSING_TRIEFACT during check operations.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_file_with_no_parser_surfaced_symbols_needs_no_triefact fingerprint=f2ee7c27204c5bcfe8fe822d998b2b04f3982ae52c32d3ce7f7fd297a92696e3 body_fp=55204d4c826d73e9962455e1df9c0caa9a50b293627499c30381643b0df07fd6 source_ref=30105b810f8b90b700150c01e3775337b5f88dda role=test -->
## `def test_file_with_no_parser_surfaced_symbols_needs_no_triefact(project: Path)`

Verifies that files containing only imports are excluded from staleness checks since they have no documentable symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_clean_when_all_in_sync_with_human_prose fingerprint=5dc7b3e44dcb10bc2ccf33dc2fadca8bd2532b0be41200707c9eede67ea30fe1 body_fp=58f46db933a35bb525fba224d6a19f719790500b2cc8ba8b5a28c08173d50d2f source_ref=30105b810f8b90b700150c01e3775337b5f88dda role=test -->
## `def test_clean_when_all_in_sync_with_human_prose(project: Path)`

Verifies `check_project` remains clean when triefacts contain manually added prose outside generated sections.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_cli_verify_exits_zero_when_clean fingerprint=4b142fe69d236116d6658f92d84b9a946f18c6d243ff719e51eb5e82fedad9d4 body_fp=5757460fc4b868c0bbacd2fe9666aee18b0428aabc3be80c9495f106c2480dee source_ref=647efc202801e8ab3384c135027857bcb77efcb4 role=test-infrastructure -->
## `def test_cli_verify_exits_zero_when_clean(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verifies that CLI `verify` command exits with code 0 when triefacts are coherent with source.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_cli_verify_exits_nonzero_when_stale fingerprint=a2d2723a23ccfd370ddd351e2f787b5fc95d089db000fec0db9ecb9578e39a7f body_fp=57bace313e37659f02e0ce3117dcd6d7aa7a8c838b07e366707d143f55eac3a0 source_ref=647efc202801e8ab3384c135027857bcb77efcb4 role=test-infrastructure -->
## `def test_cli_verify_exits_nonzero_when_stale(project: Path, monkeypatch: pytest.MonkeyPatch)`

Tests that CLI verify command exits with code 1 when triefacts are out of sync with source.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_cli_verify_quiet_mode fingerprint=10e216c8132777b1f979db57b6c06e1b7243d2eb4597bd4e8198003dee828443 body_fp=5a2b45485dd7c0f3205a7a34343502e346276eb728bb87bbeea5b58faec4dc94 source_ref=647efc202801e8ab3384c135027857bcb77efcb4 role=test-infrastructure -->
## `def test_cli_verify_quiet_mode(project: Path, monkeypatch: pytest.MonkeyPatch)`

Tests that CLI verify command with --quiet flag suppresses per-symbol details while preserving error summary.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_cli_verify_detects_tampered_body fingerprint=6d40d4f48e4430cd05b03f35a5184d65e3235d8a0b8ef65353ea5507a42fc0a0 body_fp=42eb4e9dd7a4cb2243bea6f37db0069b038f4460d87b479172d3d203b4a652b1 source_ref=30105b810f8b90b700150c01e3775337b5f88dda role=test -->
## `def test_cli_verify_detects_tampered_body(project: Path, monkeypatch: pytest.MonkeyPatch)`

Tests that the CLI `verify` command detects manually edited triefact section bodies and outputs "hand-edited", "outside", and the affected symbol name.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_check_project_detects_tampered_body fingerprint=73497d814b012250d67621e3dd5ff6075add11f22f4e6c837fbdb9b4c4e0ef38 body_fp=374ce27eded96e86b4ce14b6d6fb889dc6d0eca1ec0b746cf3d119872ab5aa3b source_ref=30105b810f8b90b700150c01e3775337b5f88dda role=test -->
## `def test_check_project_detects_tampered_body(project: Path)`

Tests that `check_project` detects manually edited content within triefact section sentinels via body fingerprint validation.

- Modifies generated triefact content by replacing the original text with "DIFFERENT TEXT"
- Verifies that `StaleReason.TAMPERED_BODY` is flagged for the modified section
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_check_project_detects_legacy_section fingerprint=be8f57710f083959038e5df3dc415177ec483a8b6d07023a86484d995bc81a3d body_fp=540ff80eae6d325e481a51b7e4a6103086563eab57d6dacb5a088b2cbcf0f7a2 source_ref=30105b810f8b90b700150c01e3775337b5f88dda role=test -->
## `def test_check_project_detects_legacy_section(project: Path)`

Tests that check_project detects sections missing body_fp attributes as legacy format requiring updates.
<!-- trie:end -->