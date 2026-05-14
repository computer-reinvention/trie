---
trie_version: 0.1.0
source: tests/test_e2e_sync.py
file_fingerprint: aadb9c2d04cc1f2e5c5f0fd3b9704b5a44fd2866fe5fa69d11bc01a48d664983
last_synced_at: '2026-05-14T18:25:52Z'
description: End-to-end test for `trie sync --file` against the tiny fixture repo.
defines:
- kind: class
  qualified_name: tests/test_e2e_sync:FakeClient
  lines: 26-50
- kind: method
  qualified_name: tests/test_e2e_sync:FakeClient.generate
  lines: 36-47
- kind: method
  qualified_name: tests/test_e2e_sync:FakeClient.count_tokens
  lines: 49-50
- kind: function
  qualified_name: tests/test_e2e_sync:project
  lines: 54-67
- kind: function
  qualified_name: tests/test_e2e_sync:test_sync_single_file_writes_triefact
  lines: 70-100
- kind: function
  qualified_name: tests/test_e2e_sync:test_human_prose_between_sections_survives_resync
  lines: 103-138
- kind: function
  qualified_name: tests/test_e2e_sync:test_resync_updates_section_when_source_changes
  lines: 141-172
- kind: function
  qualified_name: tests/test_e2e_sync:test_resync_removes_section_when_symbol_deleted
  lines: 175-200
- kind: function
  qualified_name: tests/test_e2e_sync:test_first_call_creates_cache_subsequent_calls_read
  lines: 203-216
- kind: function
  qualified_name: tests/test_e2e_sync:test_cli_sync_auto_bootstraps_first_run
  lines: 219-229
- kind: function
  qualified_name: tests/test_e2e_sync:test_cli_sync_errors_on_missing_file
  lines: 232-236
- kind: function
  qualified_name: tests/test_e2e_sync:test_cli_sync_errors_when_no_config
  lines: 239-245
incoming_refs: 0
outgoing_refs: 17
---
<!-- trie:section symbol=tests/test_e2e_sync:FakeClient fingerprint=464e2049df41370146411117991983091506f10d89f570b2aa42a935790758e0 body_fp=d54b75b4ffc5603b572a454b39cebc8c569bf1fafc332402fe086410c9da79ee -->
## `FakeClient`

Deterministic LLM stub that returns templated responses and records call counts for cache-behaviour assertions.

- `calls`: incremented on each `generate` invocation.
- `requests_seen`: all `GenerationRequest` objects passed to `generate`.
- First call sets `cache_creation_input_tokens=100`; subsequent calls set `cache_read_input_tokens=100`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:FakeClient.generate fingerprint=32144d57a656826d76eaf8439dcfc814411dfe621be53b51e279bc7343b2ba1e body_fp=9543e3d62b90e01b2fe512dda9d5fc5267c12ff1337dab3bd2f680cae498a13a -->
## `generate(self, req: GenerationRequest) -> GenerationResponse`

Increment call counter, record the request, and return a canned `GenerationResponse` with deterministic cache token accounting.

- `cache_creation_input_tokens`: 100 on first call, 0 thereafter.
- `cache_read_input_tokens`: 0 on first call, 100 thereafter.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=0cc8e4c60852ed2343ba12efc7686b2f040b2c6b012d45e134249772b72c93f1 -->
## `count_tokens(self, _req: GenerationRequest) -> int`

Return a fixed token count of 100 for any request.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:project fingerprint=16df3ebd676a6f8d2473a730ffb75c5fd86a5da52f7caae13faab42c03ae674f body_fp=7e17aa0476b399b44a5bd9aba2e060deca1657fae7d341734129ad43d7cd5ca4 -->
## `project(tmp_path: Path) -> Path`

Copy the tiny fixture repo into a temp directory and write a minimal `trie.toml` config file.

- **Returns** the root path of the prepared project directory.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:test_sync_single_file_writes_triefact fingerprint=0b29e347e438cb839792d6f51ac929736b5244acac3d4251071390587f566a49 body_fp=34470b658df7243d3c9a4872f1ab20649e67dd5bdc95c4152b3833b6f3f7ffda -->
## `test_sync_single_file_writes_triefact(project: Path)`

Assert that syncing `calculator.py` generates exactly 5 public-symbol sections and writes a valid triefact file with correct front matter.

- `project`: temp directory fixture containing the tiny repo and `trie.toml`
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:test_human_prose_between_sections_survives_resync fingerprint=918ac4736b7f4fb6b3d9d2da82a2d4084996a1f4547563434cf25bfcc35c6abe body_fp=0fabd84e17358bdff0671c0a7ebb4a9cd28466e8bf856eb5330da6cc3647af97 -->
## `test_human_prose_between_sections_survives_resync(project: Path)`

Verify that hand-written prose inserted between trie-managed sections is preserved across a resync.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:test_resync_updates_section_when_source_changes fingerprint=511dda2600814a422bce301b8428b60e6ba80391945cfcaa349e66b7675df2bb body_fp=7cebc219b311258fae73489b9115377177f1707481409c3014a833914b9dc3da -->
## `test_resync_updates_section_when_source_changes(project: Path)`

Assert that re-syncing after modifying a symbol's source updates the triefact section fingerprint.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:test_resync_removes_section_when_symbol_deleted fingerprint=9f7d8ea0b59c3bde607537336b4d182624eb6e60374ad8f6f4307c66a3767229 body_fp=1032e10da8ec89a3fe917116ab9306e5363dc57378d3f6c25a1d2715fd31e6f2 -->
## `test_resync_removes_section_when_symbol_deleted(project: Path)`

Assert that a deleted source symbol's triefact section is removed on resync.

- `project`: temp directory fixture with tiny repo and `trie.toml`
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:test_first_call_creates_cache_subsequent_calls_read fingerprint=387e19cdf13b0a93927df45484e84aafbd347880a1bb9e517b1c675542a4a417 body_fp=64e09d5228eac0d5fd11f18c3357bc60368ac009892b10a9803abdeede35e833 -->
## `test_first_call_creates_cache_subsequent_calls_read(project: Path)`

Assert that the first LLM call creates cache tokens and all subsequent calls consume read tokens.

- `project`: fixture providing an isolated copy of the tiny repo.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:test_cli_sync_auto_bootstraps_first_run fingerprint=673cf069292418a390de6294d6cdf03dd74c745121894c272b2a5abed7230bbf body_fp=decea338756c88fe191639a66b5d4d1001a326dcc9c8406dd75713e5a5d9a4b3 -->
## `test_cli_sync_auto_bootstraps_first_run(project: Path, monkeypatch)`

Verify `trie sync --limit 10` succeeds in a fresh project by auto-detecting first-run bootstrap with a patched `FakeClient`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:test_cli_sync_errors_on_missing_file fingerprint=ac055df6cd0b2982d47b7f5ddf8e532f4a1c38dfbefaefb6c220970792004945 body_fp=4d1a9563784682a40bdde2ae37f1f7638df0d0faedd8fda6f7baee5f255368f0 -->
## `test_cli_sync_errors_on_missing_file(project: Path)`

Assert that `trie sync --file` exits with code 1 and reports "does not exist" for a non-existent path.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:test_cli_sync_errors_when_no_config fingerprint=f24a74ab8515b27a1593fa499df188e4ff6ff93508d61d9afbceebd6daffa72e body_fp=3125e879d9d08c1dc0472ea9536c0cf6c1268b9cad006304cad383a0507d7430 -->
## `test_cli_sync_errors_when_no_config(tmp_path: Path)`

Assert that `trie sync --file` exits with code 1 and mentions `trie.toml` when no config file exists.
<!-- trie:end -->