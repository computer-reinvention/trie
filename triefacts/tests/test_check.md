---
trie_version: 0.1.5
source: tests/test_check.py
file_fingerprint: 7c580b8c9143a2b2172cb5cc809adee8dfd121d71bda42e370ba4ac8b02b7b3e
last_synced_at: '2026-05-28T14:39:05Z'
defines:
- kind: module
  qualified_name: tests/test_check:__module__
  lines: 1-213
- kind: function
  qualified_name: tests/test_check:project
  lines: 16-28
- kind: function
  qualified_name: tests/test_check:_sync_all
  lines: 31-34
- kind: function
  qualified_name: tests/test_check:test_clean_after_fresh_sync
  lines: 37-41
- kind: function
  qualified_name: tests/test_check:test_missing_triefact_detected
  lines: 44-50
- kind: function
  qualified_name: tests/test_check:test_stale_section_detected
  lines: 53-60
- kind: function
  qualified_name: tests/test_check:test_missing_section_detected
  lines: 63-72
- kind: function
  qualified_name: tests/test_check:test_orphan_section_detected
  lines: 75-84
- kind: function
  qualified_name: tests/test_check:test_private_only_file_requires_a_triefact
  lines: 87-98
- kind: function
  qualified_name: tests/test_check:test_file_with_no_parser_surfaced_symbols_needs_no_triefact
  lines: 101-112
- kind: function
  qualified_name: tests/test_check:test_clean_when_all_in_sync_with_human_prose
  lines: 115-123
- kind: function
  qualified_name: tests/test_check:test_cli_verify_exits_zero_when_clean
  lines: 126-132
- kind: function
  qualified_name: tests/test_check:test_cli_verify_exits_nonzero_when_stale
  lines: 135-143
- kind: function
  qualified_name: tests/test_check:test_cli_verify_quiet_mode
  lines: 146-157
- kind: function
  qualified_name: tests/test_check:test_cli_verify_detects_tampered_body
  lines: 160-174
- kind: function
  qualified_name: tests/test_check:test_check_project_detects_tampered_body
  lines: 177-191
- kind: function
  qualified_name: tests/test_check:test_check_project_detects_legacy_section
  lines: 194-212
incoming_refs: 0
outgoing_refs: 34
---
<!-- trie:section symbol=tests/test_check:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=4bee1485e2f9b46fe939213e58ef2bffb7ef0975c4edc4e2c6b9c46df3f1e2e0 source_ref=bf5e6980d7a8f7a8c9f913d6ffde89bb4ac01942 -->
## `tests/test_check`

Integration and unit tests for `check_project` and the `verify` CLI command.

- `FakeClient`: stub LLM client returning fixed generated text for sync setup.
- `project`: `tmp_path`-based fixture with two Python source files and a `trie.toml`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:project fingerprint=6c084affeb9451e9736e35692da0379b565f57e450c09c6aba378a475b9970df body_fp=19e7fae98a84ee168fdea0018ff5a0966e59ee6898086e6e0466d7da34837dee source_ref=bf5e6980d7a8f7a8c9f913d6ffde89bb4ac01942 -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal trie project with `trie.toml`, `src/alpha.py`, and `src/beta.py`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:_sync_all fingerprint=2319aaf7307a31aa136e06ddb84dd261f6ef7fdbb25fbcfbda6b959c3a11d06d body_fp=9ffb225b04e130a9e93fe81471d9387102d7bd9e62ce3304705e5983db8b198e source_ref=647efc202801e8ab3384c135027857bcb77efcb4 -->
## `_sync_all(project: Path) -> None`

Sync every `.py` file under `project/src` using a `FakeClient`, populating triefacts for test assertions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_clean_after_fresh_sync fingerprint=13234c9b3bc113d2f6251099e2ed19680cbd1fec19486fcfd1f2ee688dd6877d body_fp=6895012c88fa6c7d21d3eb7718670d82ffcc135973ace12fae354b46a1e00855 source_ref=bf5e6980d7a8f7a8c9f913d6ffde89bb4ac01942 -->
## `test_clean_after_fresh_sync(project: Path)`

Assert that `check_project` reports a clean result immediately after syncing all source files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_missing_triefact_detected fingerprint=198beaed352ba1847c55b9b432a978f034dd94e3c19901ab32419c89cde856e4 body_fp=87d478181730b270b29f14764d4a3f4ab55a571d4e1be9b7ce5d53b076bce91f source_ref=bf5e6980d7a8f7a8c9f913d6ffde89bb4ac01942 -->
## `test_missing_triefact_detected(project: Path)`

Assert that `check_project` reports `StaleReason.MISSING_TRIEFACT` and marks the result unclean when no triefacts have been generated.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_stale_section_detected fingerprint=90186c99480bfe6049209b581e100daba72eae24b8cba2c726aa6b104934f5d9 body_fp=f50f269450d5371a7de457177964ba4736a53fe7852b6567768bac948651d533 source_ref=bf5e6980d7a8f7a8c9f913d6ffde89bb4ac01942 -->
## `test_stale_section_detected(project: Path)`

Assert that modifying a source symbol's body causes `check_project` to report `StaleReason.STALE_SECTION` for `src/alpha:alpha`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_missing_section_detected fingerprint=474be3f403d0bc036a4e3b21eaa0aa313c358d28ce4173c0b1d0ede526d616de body_fp=e5d484bfe14d4c0291cead94c63dabe2f884a6822cad1f821cb9977899accc9e source_ref=bf5e6980d7a8f7a8c9f913d6ffde89bb4ac01942 -->
## `test_missing_section_detected(project: Path)`

Assert that adding a new symbol to a synced file causes `check_project` to report `StaleReason.MISSING_SECTION` for that symbol.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_orphan_section_detected fingerprint=fa609789a15518cf4c7d41859858f0a90c64b76d6872c4b0a50099bbf1e2c602 body_fp=6a8cb574c7485fc351d9b11ea5d949169dd0197e1463713b60fbfc818bd49d54 source_ref=bf5e6980d7a8f7a8c9f913d6ffde89bb4ac01942 -->
## `test_orphan_section_detected(project: Path)`

Assert that `check_project` flags `ORPHAN_SECTION` when a triefact section has no matching source symbol.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_private_only_file_requires_a_triefact fingerprint=98ffaaffbffb6147cea08a7a5a60f8def21a95b776735ea3669398bf858f7064 body_fp=17fcc552d1f8a81fc4ef864d7984024808057383bea752896ae6487c29d03835 source_ref=bf5e6980d7a8f7a8c9f913d6ffde89bb4ac01942 -->
## `test_private_only_file_requires_a_triefact(project: Path)`

Assert that a file containing only underscore-prefixed symbols still triggers `StaleReason.MISSING_TRIEFACT`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_file_with_no_parser_surfaced_symbols_needs_no_triefact fingerprint=f2ee7c27204c5bcfe8fe822d998b2b04f3982ae52c32d3ce7f7fd297a92696e3 body_fp=4a12a9a56f6351654ff25816b30f032417120404c058a18eb9d1d94195211e27 source_ref=bf5e6980d7a8f7a8c9f913d6ffde89bb4ac01942 -->
## `test_file_with_no_parser_surfaced_symbols_needs_no_triefact(project: Path)`

Assert that `check_project` emits no items for a source file containing only import statements and no documentable symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_clean_when_all_in_sync_with_human_prose fingerprint=5dc7b3e44dcb10bc2ccf33dc2fadca8bd2532b0be41200707c9eede67ea30fe1 body_fp=e6597af490a30fc27b3447e4b5c7463e07eab90b21f80cd7e93947d070cbc515 source_ref=bf5e6980d7a8f7a8c9f913d6ffde89bb4ac01942 -->
## `test_clean_when_all_in_sync_with_human_prose(project: Path)`

Assert that hand-written prose appended to a triefact does not cause `check_project` to report staleness.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_cli_verify_exits_zero_when_clean fingerprint=4b142fe69d236116d6658f92d84b9a946f18c6d243ff719e51eb5e82fedad9d4 body_fp=45bc4730053e47e52a4be155c3a72fe4e4639cba765f2263a4e87d4a9b216ea6 source_ref=bf5e6980d7a8f7a8c9f913d6ffde89bb4ac01942 -->
## `test_cli_verify_exits_zero_when_clean(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert `trie verify` exits 0 and prints "coherent" when all triefacts are up to date.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_cli_verify_exits_nonzero_when_stale fingerprint=a2d2723a23ccfd370ddd351e2f787b5fc95d089db000fec0db9ecb9578e39a7f body_fp=a8eb0e8584ef2346f69cf47bc0264471667d1835e70b0f073f211185168d58b2 source_ref=bf5e6980d7a8f7a8c9f913d6ffde89bb4ac01942 -->
## `test_cli_verify_exits_nonzero_when_stale(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert `trie verify` exits 1 and names the stale symbol when a source file changes after sync.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_cli_verify_quiet_mode fingerprint=10e216c8132777b1f979db57b6c06e1b7243d2eb4597bd4e8198003dee828443 body_fp=ab126f83f41f6553e0e54c4577450b211911422d68cfebcbde118445d37bd790 source_ref=bf5e6980d7a8f7a8c9f913d6ffde89bb4ac01942 -->
## `test_cli_verify_quiet_mode(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie -q verify` suppresses per-symbol detail but still emits an issue summary on stale output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_cli_verify_detects_tampered_body fingerprint=1dbf23489cb261c47fd1656de1b75154589a3dc4fe22bc186249539be86a15f1 body_fp=ca06566f45cf6d27e254e7575604b2b9411428a8b04de29c355f62c5a374902f source_ref=647efc202801e8ab3384c135027857bcb77efcb4 -->
## `test_cli_verify_detects_tampered_body(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert `trie verify` exits 1 and reports "tampered" when a triefact section body is hand-edited.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_check_project_detects_tampered_body fingerprint=73497d814b012250d67621e3dd5ff6075add11f22f4e6c837fbdb9b4c4e0ef38 body_fp=510e52581ced74390e013b11ee13c45757387377e82095629eebcf3d765d5b48 source_ref=647efc202801e8ab3384c135027857bcb77efcb4 -->
## `test_check_project_detects_tampered_body(project: Path)`

Assert that `check_project` returns a `TAMPERED_BODY` item for `src/beta:beta` when its section body is hand-edited.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_check_project_detects_legacy_section fingerprint=be8f57710f083959038e5df3dc415177ec483a8b6d07023a86484d995bc81a3d body_fp=1fa0a0b12a823634e14e447d32a3ab0423e39e0e880394991fea64b2e10e4a20 source_ref=bf5e6980d7a8f7a8c9f913d6ffde89bb4ac01942 -->
## `test_check_project_detects_legacy_section(project: Path)`

Assert that `check_project` flags `LEGACY_SECTION` for triefact sections missing the `body_fp=` attribute produced by trie ≤ 0.1.
<!-- trie:end -->