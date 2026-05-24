---
trie_version: 0.1.2
source: tests/test_check.py
file_fingerprint: a41f4091d397082d7d41592d9aa7e8f0bdddfc169fef2e2f4af17751db1ff09a
last_synced_at: '2026-05-23T23:50:28Z'
defines:
- kind: module
  qualified_name: tests/test_check:__module__
  lines: 1-233
- kind: class
  qualified_name: tests/test_check:FakeClient
  lines: 17-32
- kind: method
  qualified_name: tests/test_check:FakeClient.generate
  lines: 21-29
- kind: method
  qualified_name: tests/test_check:FakeClient.count_tokens
  lines: 31-32
- kind: function
  qualified_name: tests/test_check:project
  lines: 36-48
- kind: function
  qualified_name: tests/test_check:_sync_all
  lines: 51-54
- kind: function
  qualified_name: tests/test_check:test_clean_after_fresh_sync
  lines: 57-61
- kind: function
  qualified_name: tests/test_check:test_missing_triefact_detected
  lines: 64-70
- kind: function
  qualified_name: tests/test_check:test_stale_section_detected
  lines: 73-80
- kind: function
  qualified_name: tests/test_check:test_missing_section_detected
  lines: 83-92
- kind: function
  qualified_name: tests/test_check:test_orphan_section_detected
  lines: 95-104
- kind: function
  qualified_name: tests/test_check:test_private_only_file_requires_a_triefact
  lines: 107-118
- kind: function
  qualified_name: tests/test_check:test_file_with_no_parser_surfaced_symbols_needs_no_triefact
  lines: 121-132
- kind: function
  qualified_name: tests/test_check:test_clean_when_all_in_sync_with_human_prose
  lines: 135-143
- kind: function
  qualified_name: tests/test_check:test_cli_verify_exits_zero_when_clean
  lines: 146-152
- kind: function
  qualified_name: tests/test_check:test_cli_verify_exits_nonzero_when_stale
  lines: 155-163
- kind: function
  qualified_name: tests/test_check:test_cli_verify_quiet_mode
  lines: 166-177
- kind: function
  qualified_name: tests/test_check:test_cli_verify_detects_tampered_body
  lines: 180-194
- kind: function
  qualified_name: tests/test_check:test_check_project_detects_tampered_body
  lines: 197-211
- kind: function
  qualified_name: tests/test_check:test_check_project_detects_legacy_section
  lines: 214-232
incoming_refs: 0
outgoing_refs: 36
---
<!-- trie:section symbol=tests/test_check:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=4bee1485e2f9b46fe939213e58ef2bffb7ef0975c4edc4e2c6b9c46df3f1e2e0 source_ref=bf5e6980d7a8f7a8c9f913d6ffde89bb4ac01942 -->
## `tests/test_check`

Integration and unit tests for `check_project` and the `verify` CLI command.

- `FakeClient`: stub LLM client returning fixed generated text for sync setup.
- `project`: `tmp_path`-based fixture with two Python source files and a `trie.toml`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:FakeClient fingerprint=e41cdf8484085fe52836a78fa046003a64b4ee976928802814aeb5dfbe564b63 body_fp=2c9267865477be474704ed0a5e5fc68362e2c05b79d44cbf6b37e338e9deeebb source_ref=bf5e6980d7a8f7a8c9f913d6ffde89bb4ac01942 -->
## `FakeClient`

Test double for an LLM client; records call count and returns fixed `GenerationResponse` output.

- `calls`: incremented on each `generate` invocation.
- `generate`: always returns `"## generated\n\nbody."` with static token counts.
- `count_tokens`: always returns `100`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:FakeClient.generate fingerprint=7328b86a4ba976097f1e8eec40c045a8090951dfeca29ef5debd39c4e6fc9a4b body_fp=68c03a2d5308b635b78a6f88c213406b5afd83ad703a7840a3b38639f522f49f source_ref=bf5e6980d7a8f7a8c9f913d6ffde89bb4ac01942 -->
## `FakeClient.generate(self, _req: GenerationRequest) -> GenerationResponse`

Increment `FakeClient.calls` and return a fixed stub `GenerationResponse`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=7ad9fbaff5ec8a5bebb82c4d45eeefe81b2683204b2fd57dbba5e9b3e4c657e5 source_ref=bf5e6980d7a8f7a8c9f913d6ffde89bb4ac01942 -->
## `FakeClient.count_tokens(self, _req: GenerationRequest) -> int`

Return a fixed token count of 100 for any `FakeClient` generation request.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:project fingerprint=6c084affeb9451e9736e35692da0379b565f57e450c09c6aba378a475b9970df body_fp=19e7fae98a84ee168fdea0018ff5a0966e59ee6898086e6e0466d7da34837dee source_ref=bf5e6980d7a8f7a8c9f913d6ffde89bb4ac01942 -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal trie project with `trie.toml`, `src/alpha.py`, and `src/beta.py`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:_sync_all fingerprint=3f2b125695b5b50997a8d53f68a89b4f3197dfff22f3493c8beab868ef6e100a body_fp=9ffb225b04e130a9e93fe81471d9387102d7bd9e62ce3304705e5983db8b198e source_ref=bf5e6980d7a8f7a8c9f913d6ffde89bb4ac01942 -->
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
<!-- trie:section symbol=tests/test_check:test_cli_verify_detects_tampered_body fingerprint=3f257a5401e691709ee97cb37ba08ba1fd44fae2fff9582e442a9f18a19f9985 body_fp=ca06566f45cf6d27e254e7575604b2b9411428a8b04de29c355f62c5a374902f source_ref=bf5e6980d7a8f7a8c9f913d6ffde89bb4ac01942 -->
## `test_cli_verify_detects_tampered_body(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert `trie verify` exits 1 and reports "tampered" when a triefact section body is hand-edited.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_check_project_detects_tampered_body fingerprint=3b649f08b4086f9eedbf600a0d41fe047f1c06935c73fabb5fd8026b11c56d62 body_fp=510e52581ced74390e013b11ee13c45757387377e82095629eebcf3d765d5b48 source_ref=bf5e6980d7a8f7a8c9f913d6ffde89bb4ac01942 -->
## `test_check_project_detects_tampered_body(project: Path)`

Assert that `check_project` returns a `TAMPERED_BODY` item for `src/beta:beta` when its section body is hand-edited.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_check:test_check_project_detects_legacy_section fingerprint=be8f57710f083959038e5df3dc415177ec483a8b6d07023a86484d995bc81a3d body_fp=1fa0a0b12a823634e14e447d32a3ab0423e39e0e880394991fea64b2e10e4a20 source_ref=bf5e6980d7a8f7a8c9f913d6ffde89bb4ac01942 -->
## `test_check_project_detects_legacy_section(project: Path)`

Assert that `check_project` flags `LEGACY_SECTION` for triefact sections missing the `body_fp=` attribute produced by trie ≤ 0.1.
<!-- trie:end -->