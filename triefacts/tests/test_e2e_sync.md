---
trie_version: 0.1.0
source: tests/test_e2e_sync.py
file_fingerprint: aadb9c2d04cc1f2e5c5f0fd3b9704b5a44fd2866fe5fa69d11bc01a48d664983
last_synced_at: '2026-05-14T17:22:09Z'
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
<!-- trie:section symbol=tests/test_e2e_sync:FakeClient fingerprint=464e2049df41370146411117991983091506f10d89f570b2aa42a935790758e0 body_fp=5b467551dee9acba8ea27dcd7b410b17c5eb91cc7c936452587c5eedb0196181 -->
## `FakeClient`

Deterministic LLM client stub that returns templated responses and tracks call counts for cache-assertion tests.

- `calls`: incremented on each `generate` invocation; used to vary cache token fields.
- `requests_seen`: accumulates every `GenerationRequest` passed to `generate`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:FakeClient.generate fingerprint=32144d57a656826d76eaf8439dcfc814411dfe621be53b51e279bc7343b2ba1e body_fp=e0b2e5153e3b38c8e23aaeb7b2f76b15046ca83ce7d96fc23c77a274a009bf46 -->
## `generate(self, req: GenerationRequest) -> GenerationResponse`

Increment call counter, record the request, and return a templated `GenerationResponse` with deterministic cache token counts.

- `cache_creation_input_tokens`: 100 on first call, 0 thereafter.
- `cache_read_input_tokens`: 0 on first call, 100 thereafter.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=9d067b772e73f67b1bb1b8cb6fc3a256c95035c670c6695fa426a36018030c0b -->
## `count_tokens(_req: GenerationRequest) -> int`

Return a fixed token count of 100 for any request.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:project fingerprint=16df3ebd676a6f8d2473a730ffb75c5fd86a5da52f7caae13faab42c03ae674f body_fp=83cc5d23c8d10c350943d1c8d40944c523d0a9dc71e2f735be042f35e4c2a2e0 -->
## `project(tmp_path: Path) -> Path`

Copy the tiny fixture repo into a fresh temp dir and write a minimal `trie.toml` to make `Config.find_and_load` work.

- **returns** path to the project root inside `tmp_path`
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:test_sync_single_file_writes_triefact fingerprint=0b29e347e438cb839792d6f51ac929736b5244acac3d4251071390587f566a49 body_fp=7a5c346e9f432336d692eef0aed6e4b0debcd1e02e5eaaf9434c666d16d6ae59 -->
## `test_sync_single_file_writes_triefact(project: Path)`

Assert that `sync_single_file` generates exactly 5 public-symbol sections and writes a valid triefact file with correct front matter.

- `project`: temp directory populated by the `project` fixture
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:test_human_prose_between_sections_survives_resync fingerprint=918ac4736b7f4fb6b3d9d2da82a2d4084996a1f4547563434cf25bfcc35c6abe body_fp=49848c7da63f41c6e8b676f2aaf9ee4916c55ee51d45b30e41c2137fe41555e8 -->
## `test_human_prose_between_sections_survives_resync(project: Path)`

Verify that hand-written prose inserted between managed sections is preserved across a resync.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:test_resync_updates_section_when_source_changes fingerprint=511dda2600814a422bce301b8428b60e6ba80391945cfcaa349e66b7675df2bb body_fp=bab377e201df267408e43b8cbea964764ddc6a9e9382140665ebf455094f2e7a -->
## `test_resync_updates_section_when_source_changes(project: Path)`

Verify that modifying a symbol's source causes its triefact section fingerprint to change on resync.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:test_resync_removes_section_when_symbol_deleted fingerprint=9f7d8ea0b59c3bde607537336b4d182624eb6e60374ad8f6f4307c66a3767229 body_fp=625fe82e966cb2e9d90d9d5632ae50fd55e44bab22950393b7380b3d02a6e018 -->
## `test_resync_removes_section_when_symbol_deleted(project: Path)`

Assert that a triefact section is removed when its corresponding symbol is deleted from source.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:test_first_call_creates_cache_subsequent_calls_read fingerprint=387e19cdf13b0a93927df45484e84aafbd347880a1bb9e517b1c675542a4a417 body_fp=f80c60f6a2f4db8d87a2d62046138ae159a356f429768e75e33c52a614330e98 -->
## `test_first_call_creates_cache_subsequent_calls_read(project: Path)`

Assert that the first LLM call accumulates cache-creation tokens and all subsequent calls accumulate cache-read tokens.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:test_cli_sync_auto_bootstraps_first_run fingerprint=673cf069292418a390de6294d6cdf03dd74c745121894c272b2a5abed7230bbf body_fp=abe69222342b26bcdc9ceaad2913bc48e75e46b34a716a12af63ee303e10fc48 -->
## `test_cli_sync_auto_bootstraps_first_run(project: Path, monkeypatch)`

Assert that `trie sync --limit 10` exits successfully and emits "synced" on a fresh project with no prior triefacts.

- `monkeypatch`: patches `trie.cli.make_client` to return `FakeClient`, enabling offline execution.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:test_cli_sync_errors_on_missing_file fingerprint=ac055df6cd0b2982d47b7f5ddf8e532f4a1c38dfbefaefb6c220970792004945 body_fp=4079e2219a0ebdb6d714176ee6943a1218cbe15591f7023f71d96ecec7cf0413 -->
## `test_cli_sync_errors_on_missing_file(project: Path)`

Assert that `trie sync --file` exits with code 1 and reports "does not exist" for a nonexistent path.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_e2e_sync:test_cli_sync_errors_when_no_config fingerprint=f24a74ab8515b27a1593fa499df188e4ff6ff93508d61d9afbceebd6daffa72e body_fp=3125e879d9d08c1dc0472ea9536c0cf6c1268b9cad006304cad383a0507d7430 -->
## `test_cli_sync_errors_when_no_config(tmp_path: Path)`

Assert that `trie sync --file` exits with code 1 and mentions `trie.toml` when no config file exists.
<!-- trie:end -->