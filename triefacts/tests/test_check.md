---
trie_version: 0.1.1
source: tests/test_check.py
file_fingerprint: 71316276873baedc05039e8faedd4ce056d9ee6f5d9c788811ec89339c459a5b
last_synced_at: '2026-05-19T10:37:29Z'
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
<!-- trie:section symbol=tests/test_check:FakeClient fingerprint=e41cdf8484085fe52836a78fa046003a64b4ee976928802814aeb5dfbe564b63 body_fp=12bc935f908c1e630237fe9e607b3f2869cfd6efa2c01f334f947b7b3d2be1f1 source_ref=8d039b4accde06e724a1524de1f79d0a628e9c5f -->
## `FakeClient`

Test double for an LLM client; returns a fixed `GenerationResponse` and counts `generate` calls.

- `calls`: incremented on each `generate` invocation for assertion use.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:FakeClient.generate fingerprint=7328b86a4ba976097f1e8eec40c045a8090951dfeca29ef5debd39c4e6fc9a4b body_fp=bec6bdf5a82e44a139080bba5a583f3ed56101392f115dc60741ed825721d196 source_ref=fc96c03d022e7a77097fa682a3129c583b33858c -->
## `FakeClient.generate(self, _req: GenerationRequest) -> GenerationResponse`

Increment call counter and return a fixed stub `GenerationResponse` with hardcoded token counts.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=9d067b772e73f67b1bb1b8cb6fc3a256c95035c670c6695fa426a36018030c0b source_ref=fc96c03d022e7a77097fa682a3129c583b33858c -->
## `count_tokens(_req: GenerationRequest) -> int`

Return a fixed token count of 100 for any request.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:project fingerprint=6c084affeb9451e9736e35692da0379b565f57e450c09c6aba378a475b9970df body_fp=2f6e8fbf77c7a5da26f1fd308ba3d1ddd8795b9bdf91b037fdc862ac9d1a1f7d source_ref=fc96c03d022e7a77097fa682a3129c583b33858c -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal trie project with config and two Python source files.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:test_clean_after_fresh_sync fingerprint=13234c9b3bc113d2f6251099e2ed19680cbd1fec19486fcfd1f2ee688dd6877d body_fp=deff2b34597254468cca0867ea11ef33c343682dc0b44b312a9505fe3300cdd4 source_ref=fc96c03d022e7a77097fa682a3129c583b33858c -->
## `test_clean_after_fresh_sync(project: Path)`

Assert that `check_project` reports a clean state immediately after syncing all source files.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:test_missing_triefact_detected fingerprint=198beaed352ba1847c55b9b432a978f034dd94e3c19901ab32419c89cde856e4 body_fp=957c953449a4be961c31a7a88fa242014e1783efea35a9c4d58f2c03a4877e3e source_ref=fc96c03d022e7a77097fa682a3129c583b33858c -->
## `test_missing_triefact_detected(project: Path)`

Assert that `check_project` reports `StaleReason.MISSING_TRIEFACT` when no triefacts have been generated.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:test_stale_section_detected fingerprint=90186c99480bfe6049209b581e100daba72eae24b8cba2c726aa6b104934f5d9 body_fp=7451f7ef63338d33e1aa0ce418cfe434aaf7d0015fea9a0f4aba0605a8bbb77a source_ref=fc96c03d022e7a77097fa682a3129c583b33858c -->
## `test_stale_section_detected(project: Path)`

Assert that modifying a source symbol's body causes `check_project` to report `StaleReason.STALE_SECTION` for that symbol.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:test_missing_section_detected fingerprint=474be3f403d0bc036a4e3b21eaa0aa313c358d28ce4173c0b1d0ede526d616de body_fp=b38c303c1880b53f6a8b6ed4688fe856bf5c04e72c4f907c09abf11786736b1f source_ref=fc96c03d022e7a77097fa682a3129c583b33858c -->
## `test_missing_section_detected(project: Path)`

Assert that adding a new symbol to a source file causes `check_project` to report `StaleReason.MISSING_SECTION` for that symbol.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:test_orphan_section_detected fingerprint=fa609789a15518cf4c7d41859858f0a90c64b76d6872c4b0a50099bbf1e2c602 body_fp=934c6063efad7e6afc6154e7d21132ec010791146f08c4871d9dfeaaea9aaae8 source_ref=fc96c03d022e7a77097fa682a3129c583b33858c -->
## `test_orphan_section_detected(project: Path)`

Assert that deleting a symbol from source causes `check_project` to report `StaleReason.ORPHAN_SECTION` for the removed qualified name.
<!-- trie:end -->



<!-- trie:section symbol=tests/test_check:test_clean_when_all_in_sync_with_human_prose fingerprint=5dc7b3e44dcb10bc2ccf33dc2fadca8bd2532b0be41200707c9eede67ea30fe1 body_fp=ee104198158354c794849e58fc6ff0560da063f98bee3d35b42040305f425fb9 source_ref=fc96c03d022e7a77097fa682a3129c583b33858c -->
## `test_clean_when_all_in_sync_with_human_prose(project: Path)`

Assert that hand-written prose appended after generated sections does not cause `check_project` to report staleness.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:test_cli_verify_exits_zero_when_clean fingerprint=4b142fe69d236116d6658f92d84b9a946f18c6d243ff719e51eb5e82fedad9d4 body_fp=aa16006e628b7e2008b6876bb811a58ab01aeec5b6351435c89de640e9ec36c5 source_ref=fc96c03d022e7a77097fa682a3129c583b33858c -->
## `test_cli_verify_exits_zero_when_clean(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie verify` exits with code 0 and prints "coherent" when all triefacts are up to date.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:test_cli_verify_exits_nonzero_when_stale fingerprint=a2d2723a23ccfd370ddd351e2f787b5fc95d089db000fec0db9ecb9578e39a7f body_fp=4e2e36f869df4234722fad8a08aadd6cf36940ca9b2c487f03bc58719ed83224 source_ref=fc96c03d022e7a77097fa682a3129c583b33858c -->
## `test_cli_verify_exits_nonzero_when_stale(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie verify` exits with code 1 and reports the stale symbol when a source file is modified after sync.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:test_cli_verify_quiet_mode fingerprint=10e216c8132777b1f979db57b6c06e1b7243d2eb4597bd4e8198003dee828443 body_fp=065b13571078a10a8c02a32f84be4e5c0c4c9872c91ace465ac8eb5d9bf486ef source_ref=fc96c03d022e7a77097fa682a3129c583b33858c -->
## `test_cli_verify_quiet_mode(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie -q verify` suppresses per-symbol detail lines but still emits a summary and exits with code 1.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:test_cli_verify_detects_tampered_body fingerprint=3f257a5401e691709ee97cb37ba08ba1fd44fae2fff9582e442a9f18a19f9985 body_fp=e69d2addbf2ed459a5d2506472aad7c8b1e40a842d4316b724f179ab484327de source_ref=fc96c03d022e7a77097fa682a3129c583b33858c -->
## `test_cli_verify_detects_tampered_body(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert the CLI `verify` command exits 1 and reports `TAMPERED_BODY` when section content is hand-edited.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:test_check_project_detects_tampered_body fingerprint=3b649f08b4086f9eedbf600a0d41fe047f1c06935c73fabb5fd8026b11c56d62 body_fp=d10c24a4bc998777757ab1783c38f49447ebac8000cf8e4202d6824635bd8f6b source_ref=fc96c03d022e7a77097fa682a3129c583b33858c -->
## `test_check_project_detects_tampered_body(project: Path)`

Assert that `check_project` flags `TAMPERED_BODY` when section content is hand-edited after generation.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:test_check_project_detects_legacy_section fingerprint=be8f57710f083959038e5df3dc415177ec483a8b6d07023a86484d995bc81a3d body_fp=10292e298ab37b8224eb9ff71c37db66e25abc8d5261d49c6aa2ec9ae9cac80d source_ref=fc96c03d022e7a77097fa682a3129c583b33858c -->
## `test_check_project_detects_legacy_section(project: Path)`

Assert that a triefact section missing `body_fp=` (pre-0.1 format) is flagged as `LEGACY_SECTION`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:_sync_all fingerprint=3f2b125695b5b50997a8d53f68a89b4f3197dfff22f3493c8beab868ef6e100a body_fp=347c13417c7b2b31afa55ce6fdaef3f14d53bbfcda7b7cb3547ce58fc1261c2e source_ref=8d039b4accde06e724a1524de1f79d0a628e9c5f -->
## `_sync_all(project: Path) -> None`

Sync all `.py` source files in the project's `src/` directory using a `FakeClient`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:test_private_only_file_requires_a_triefact fingerprint=98ffaaffbffb6147cea08a7a5a60f8def21a95b776735ea3669398bf858f7064 body_fp=2ef638ae79aa49d67386de7a3959c201357293853947a5e9b2859193d708233e source_ref=8d039b4accde06e724a1524de1f79d0a628e9c5f -->
## `test_private_only_file_requires_a_triefact(project: Path)`

Assert that a file containing only underscore-prefixed symbols still requires a triefact and triggers `MISSING_TRIEFACT`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:test_file_with_no_parser_surfaced_symbols_needs_no_triefact fingerprint=f2ee7c27204c5bcfe8fe822d998b2b04f3982ae52c32d3ce7f7fd297a92696e3 body_fp=3ab307a50d9efd5b62d6159b3753c49a9e496c25803dadef6541a76b72b71301 source_ref=81d187ac12d82c70569f7158447eac4222307b93 -->
## `test_file_with_no_parser_surfaced_symbols_needs_no_triefact(project: Path)`

Assert that a file containing only imports (no assignments, no defs) produces no check items.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=6050b74f967645a15b6f66cad5c99ea3bfa726ed4741752fa05a89f6907b72da source_ref=81d187ac12d82c70569f7158447eac4222307b93 -->
## `tests/test_check`

Integration and unit tests for `check_project` and the `verify` CLI command.

- `FakeClient`: stub LLM client returning fixed generated text
- `project`: `tmp_path`-based fixture with two Python source files and a `trie.toml`
<!-- trie:end -->