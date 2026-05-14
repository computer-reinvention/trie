---
trie_version: 0.1.0
source: tests/test_check.py
file_fingerprint: ac7fbf92efc2dfbf2e8ab4463024a0d17c51e48012a0b8a4b89bdad20636eb20
last_synced_at: '2026-05-14T18:24:24Z'
defines:
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
  qualified_name: tests/test_check:test_no_public_symbols_no_triefact_required
  lines: 107-115
- kind: function
  qualified_name: tests/test_check:test_clean_when_all_in_sync_with_human_prose
  lines: 118-126
- kind: function
  qualified_name: tests/test_check:test_cli_verify_exits_zero_when_clean
  lines: 129-135
- kind: function
  qualified_name: tests/test_check:test_cli_verify_exits_nonzero_when_stale
  lines: 138-146
- kind: function
  qualified_name: tests/test_check:test_cli_verify_quiet_mode
  lines: 149-160
- kind: function
  qualified_name: tests/test_check:test_cli_verify_detects_tampered_body
  lines: 163-177
- kind: function
  qualified_name: tests/test_check:test_check_project_detects_tampered_body
  lines: 180-194
- kind: function
  qualified_name: tests/test_check:test_check_project_detects_legacy_section
  lines: 197-215
incoming_refs: 0
outgoing_refs: 29
---
<!-- trie:section symbol=tests/test_check:FakeClient fingerprint=e41cdf8484085fe52836a78fa046003a64b4ee976928802814aeb5dfbe564b63 body_fp=1a7773762467014063f6fa775394493ea9f203e81ec41f6f10201abbe543f351 -->
## `FakeClient`

Stub LLM client returning fixed generated text for use in tests.

- `calls`: incremented on each `generate` invocation to track usage.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:FakeClient.generate fingerprint=7328b86a4ba976097f1e8eec40c045a8090951dfeca29ef5debd39c4e6fc9a4b body_fp=94099b6151ffd3d1b4e8ecc9715c04a89e03e2e9348b7e11c5b1f6501b57b82a -->
## `generate(self, _req: GenerationRequest) -> GenerationResponse`

Increment call counter and return a fixed stub `GenerationResponse`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=0cc8e4c60852ed2343ba12efc7686b2f040b2c6b012d45e134249772b72c93f1 -->
## `count_tokens(self, _req: GenerationRequest) -> int`

Return a fixed token count of 100 for any request.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:project fingerprint=6c084affeb9451e9736e35692da0379b565f57e450c09c6aba378a475b9970df body_fp=f30de9cfcbb8497df66f08cb2e635971f31f1462a26de66b60a850f9ba94e79c -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a temporary trie project with config, and two Python source files.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:test_clean_after_fresh_sync fingerprint=13234c9b3bc113d2f6251099e2ed19680cbd1fec19486fcfd1f2ee688dd6877d body_fp=deff2b34597254468cca0867ea11ef33c343682dc0b44b312a9505fe3300cdd4 -->
## `test_clean_after_fresh_sync(project: Path)`

Assert that `check_project` reports a clean state immediately after syncing all source files.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:test_missing_triefact_detected fingerprint=198beaed352ba1847c55b9b432a978f034dd94e3c19901ab32419c89cde856e4 body_fp=957c953449a4be961c31a7a88fa242014e1783efea35a9c4d58f2c03a4877e3e -->
## `test_missing_triefact_detected(project: Path)`

Assert that `check_project` reports `StaleReason.MISSING_TRIEFACT` when no triefacts have been generated.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:test_stale_section_detected fingerprint=90186c99480bfe6049209b581e100daba72eae24b8cba2c726aa6b104934f5d9 body_fp=7451f7ef63338d33e1aa0ce418cfe434aaf7d0015fea9a0f4aba0605a8bbb77a -->
## `test_stale_section_detected(project: Path)`

Assert that modifying a source symbol's body causes `check_project` to report `StaleReason.STALE_SECTION` for that symbol.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:test_missing_section_detected fingerprint=474be3f403d0bc036a4e3b21eaa0aa313c358d28ce4173c0b1d0ede526d616de body_fp=17944f63331335841e34445bb0f8f785fe1f017324f7463c5ebdbf75e8440745 -->
## `test_missing_section_detected(project: Path)`

Assert that adding a new public symbol to a source file flags `StaleReason.MISSING_SECTION` for that symbol.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:test_orphan_section_detected fingerprint=fa609789a15518cf4c7d41859858f0a90c64b76d6872c4b0a50099bbf1e2c602 body_fp=03af7b0d74ea7757e9cf3d896b5e7b31cc154d4085c4172101ba64607e61ee6a -->
## `test_orphan_section_detected(project: Path)`

Assert that removing a symbol from source causes `check_project` to report `StaleReason.ORPHAN_SECTION` for the deleted symbol's triefact section.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:test_no_public_symbols_no_triefact_required fingerprint=b1880f912a31cce387f522f5a8bc16d42e42953fe89c985d9ca118e4cb5e7004 body_fp=e075d2d56e44b941851edc1729df8660d4a06ddce727d0ad29ae3a4dbbf2fe84 -->
## `test_no_public_symbols_no_triefact_required(project: Path)`

Assert that files containing only private symbols produce no check items.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:test_clean_when_all_in_sync_with_human_prose fingerprint=5dc7b3e44dcb10bc2ccf33dc2fadca8bd2532b0be41200707c9eede67ea30fe1 body_fp=3059e2b924619e89a9aae767eec4aa638465fb1d041a7ad4bc5651beeb220d2c -->
## `test_clean_when_all_in_sync_with_human_prose(project: Path)`

Assert that hand-written prose appended to a synced triefact does not trigger a stale check result.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:test_cli_verify_exits_zero_when_clean fingerprint=4b142fe69d236116d6658f92d84b9a946f18c6d243ff719e51eb5e82fedad9d4 body_fp=1d1e8682a71e49dc0bd36f551b05787e7c047fa0abf0c708a97dad2ad038094b -->
## `test_cli_verify_exits_zero_when_clean(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert the `verify` CLI command exits 0 and prints "coherent" when all triefacts are up to date.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:test_cli_verify_exits_nonzero_when_stale fingerprint=a2d2723a23ccfd370ddd351e2f787b5fc95d089db000fec0db9ecb9578e39a7f body_fp=ab8a4a7d3ab83d1245b04b713f2b015f8e79c3466f2787114b8a62cee00fdb58 -->
## `test_cli_verify_exits_nonzero_when_stale(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert `trie verify` exits with code 1 and reports the stale symbol when a source file is modified after sync.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:test_cli_verify_quiet_mode fingerprint=10e216c8132777b1f979db57b6c06e1b7243d2eb4597bd4e8198003dee828443 body_fp=ce9d0db69d9ff0824caef03c26e3241f46506a51c7bcdcfe012deee0bf9db8c8 -->
## `test_cli_verify_quiet_mode(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `-q` suppresses per-symbol detail lines while still emitting a summary containing "issue".
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:test_cli_verify_detects_tampered_body fingerprint=3f257a5401e691709ee97cb37ba08ba1fd44fae2fff9582e442a9f18a19f9985 body_fp=86617a2b5fcec456d763ec8ab119f7f8a771ebdf0ef24a9d787721ac559ba936 -->
## `test_cli_verify_detects_tampered_body(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that the `verify` CLI command exits 1 and reports `TAMPERED_BODY` when section content is edited directly.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:test_check_project_detects_tampered_body fingerprint=3b649f08b4086f9eedbf600a0d41fe047f1c06935c73fabb5fd8026b11c56d62 body_fp=24f73fe3a24910d6c849c5db15a9a6f16cbdf37f046412080d2ade264d92999f -->
## `test_check_project_detects_tampered_body(project: Path)`

Assert that `check_project` raises `TAMPERED_BODY` when section content is hand-edited after sync.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_check:test_check_project_detects_legacy_section fingerprint=d27ffa0d7a2aadf38f56555fa46b32219e8c85c046bdb7dd2e6303fd58d483e7 body_fp=23481e57c58ff546fd30e28c06580536443d96f643545985f288eaa6cbd6a034 -->
## `test_check_project_detects_legacy_section(project: Path)`

Assert that a triefact section missing the `body_fp=` attribute (pre-0.2 format) triggers `StaleReason.LEGACY_SECTION`.
<!-- trie:end -->