---
trie_version: 0.1.2
source: tests/test_e2e_sync.py
file_fingerprint: 79b65409efae0ed16ba77f82d63dc68cc6914f24061f6e722d81f9c5b23a3fb7
last_synced_at: '2026-05-23T23:48:15Z'
description: End-to-end test for `trie sync --file` against the tiny fixture repo.
defines:
- kind: module
  qualified_name: tests/test_e2e_sync:__module__
  lines: 1-376
- kind: constant
  qualified_name: tests/test_e2e_sync:FIXTURE_DIR
  lines: 22-22
- kind: class
  qualified_name: tests/test_e2e_sync:FakeClient
  lines: 26-50
- kind: method
  qualified_name: tests/test_e2e_sync:FakeClient.__post_init__
  lines: 33-34
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
  lines: 70-102
- kind: function
  qualified_name: tests/test_e2e_sync:test_human_prose_between_sections_survives_resync
  lines: 105-140
- kind: function
  qualified_name: tests/test_e2e_sync:test_resync_updates_section_when_source_changes
  lines: 143-174
- kind: function
  qualified_name: tests/test_e2e_sync:test_resync_removes_section_when_symbol_deleted
  lines: 177-202
- kind: function
  qualified_name: tests/test_e2e_sync:test_first_call_creates_cache_subsequent_calls_read
  lines: 205-219
- kind: function
  qualified_name: tests/test_e2e_sync:test_cli_sync_auto_bootstraps_first_run
  lines: 222-235
- kind: function
  qualified_name: tests/test_e2e_sync:test_cli_sync_errors_on_missing_file
  lines: 238-242
- kind: function
  qualified_name: tests/test_e2e_sync:test_cli_sync_errors_when_no_config
  lines: 245-251
- kind: function
  qualified_name: tests/test_e2e_sync:_init_git
  lines: 257-263
- kind: function
  qualified_name: tests/test_e2e_sync:test_first_sync_in_git_repo_stamps_source_ref
  lines: 266-284
- kind: function
  qualified_name: tests/test_e2e_sync:test_sync_outside_git_repo_omits_source_ref
  lines: 287-299
- kind: function
  qualified_name: tests/test_e2e_sync:test_resync_with_committed_history_takes_diff_aware_path
  lines: 302-342
- kind: function
  qualified_name: tests/test_e2e_sync:test_resync_after_uncommitted_change_falls_back_to_cold
  lines: 345-375
incoming_refs: 0
outgoing_refs: 29
---
<!-- trie:section symbol=tests/test_e2e_sync:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=c8312f9875b0f542090e16c6680523fffe7b9317feff679738af264eacc6a6bf source_ref=de4967ffd03ab7a1cb0403f02d212520ddf339e8 -->
## `tests/test_e2e_sync`

End-to-end tests for `trie sync --file` using a deterministic `FakeClient` instead of a live LLM.

- `FIXTURE_DIR`: path to the `tiny_repo` fixture used by all tests
- `FakeClient`: offline stub recording calls and returning canned `GenerationResponse` objects
- `project`: pytest fixture that copies `tiny_repo` into a temp dir with a minimal `trie.toml`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:FIXTURE_DIR fingerprint=2635a439793a81128764c32977c9356050865c2ac61f8264769219675508cca2 body_fp=d2360ff167d79ad4122c62246d7cf3306eaceaf1fb803b65b26f79209d254f74 source_ref=de4967ffd03ab7a1cb0403f02d212520ddf339e8 -->
## `FIXTURE_DIR: Path`

Absolute path to the `tests/fixtures/tiny_repo` directory used as the test fixture source.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:FakeClient fingerprint=464e2049df41370146411117991983091506f10d89f570b2aa42a935790758e0 body_fp=5ecb03dcd45daccf6ec927e4b098bbe5586540b1733beb0f42ebb547b4992ba0 source_ref=de4967ffd03ab7a1cb0403f02d212520ddf339e8 -->
## `FakeClient`

Deterministic LLM client stub that returns canned `GenerationResponse` objects and records calls for cache-token assertions.

- `calls`: incremented on each `generate` call; first call simulates cache creation, subsequent calls simulate cache reads.
- `requests_seen`: accumulates every `GenerationRequest` passed to `generate`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:FakeClient.__post_init__ fingerprint=acb5f189b6faf4617c18bdcf095ff513902e065e9313e669660eb6579ac7a01f body_fp=2cf6e359491388a86ed6f45661a2472968ce30e8ca885c14936701059ef6f682 source_ref=de4967ffd03ab7a1cb0403f02d212520ddf339e8 -->
## `FakeClient.__post_init__(self) -> None`

Initialize `FakeClient.requests_seen` to an empty list after dataclass construction.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:FakeClient.generate fingerprint=32144d57a656826d76eaf8439dcfc814411dfe621be53b51e279bc7343b2ba1e body_fp=27d3c0871a874acc19fd91dd5c8df71e55bd5b7a449ecc056af203a34e002f98 source_ref=de4967ffd03ab7a1cb0403f02d212520ddf339e8 -->
## `FakeClient.generate(self, req: GenerationRequest) -> GenerationResponse`

Record the request and return a deterministic `GenerationResponse` with call-count-based cache token splits.

- First call sets `cache_creation_input_tokens=100`, subsequent calls set `cache_read_input_tokens=100`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=ca27c3bea5e2b96663b0946a5703f310915fce4c787a87fbd5c5da859942d202 source_ref=de4967ffd03ab7a1cb0403f02d212520ddf339e8 -->
## `FakeClient.count_tokens(_req: GenerationRequest) -> int`

Always returns 100 for any `FakeClient` token-count request.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:project fingerprint=16df3ebd676a6f8d2473a730ffb75c5fd86a5da52f7caae13faab42c03ae674f body_fp=f6a1e7524674455f4a09e957fd2fcccbd82b99e7ec8d1677b49e0d0c8e59b099 source_ref=de4967ffd03ab7a1cb0403f02d212520ddf339e8 -->
## `project(tmp_path: Path) -> Path`

pytest fixture that copies the tiny fixture repo into a temp directory and writes a minimal `trie.toml`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_sync_single_file_writes_triefact fingerprint=94b9928853195be421740237bfaca67bdaa59a4ba7330e35e51099530b458628 body_fp=35bff4e706b9a4cf948aabebb6285cc7ba1fb3525e639467c40ccbd3ffaf1b5c source_ref=de4967ffd03ab7a1cb0403f02d212520ddf339e8 -->
## `test_sync_single_file_writes_triefact(project: Path)`

Verify `sync_single_file` generates 6 sections (all symbols, including private), writes valid front matter, and records every expected qname.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_human_prose_between_sections_survives_resync fingerprint=918ac4736b7f4fb6b3d9d2da82a2d4084996a1f4547563434cf25bfcc35c6abe body_fp=d75abdad3cbc83d7a64f23f5464cb5f383ad036d285703001e7bc4e1bc6670ed source_ref=de4967ffd03ab7a1cb0403f02d212520ddf339e8 -->
## `test_human_prose_between_sections_survives_resync(project: Path)`

Assert that hand-written Markdown between trie-managed sections is preserved across a second sync.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_resync_updates_section_when_source_changes fingerprint=511dda2600814a422bce301b8428b60e6ba80391945cfcaa349e66b7675df2bb body_fp=1297b81dc3235d7b51dcc870a4e930e0b3dc030624fcb0fef007910306948e01 source_ref=de4967ffd03ab7a1cb0403f02d212520ddf339e8 -->
## `test_resync_updates_section_when_source_changes(project: Path)`

Assert that resyncing after a source change produces a section with a different fingerprint.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_resync_removes_section_when_symbol_deleted fingerprint=9f7d8ea0b59c3bde607537336b4d182624eb6e60374ad8f6f4307c66a3767229 body_fp=4338148b2fe728e2ddbe91cca1d525708a12df94852870cb715def5000ade823 source_ref=de4967ffd03ab7a1cb0403f02d212520ddf339e8 -->
## `test_resync_removes_section_when_symbol_deleted(project: Path)`

Assert that resyncing after a symbol is deleted from source removes its triefact section and decrements `sections_removed`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_first_call_creates_cache_subsequent_calls_read fingerprint=d349234f6f28f8ec4ddae981bc0d114c8a9720ace243788a9b245d233d30c096 body_fp=0ecb22f751804a9fa2d3bdba72e6c2d5c75a00c500d090b315acccc9a42c2af9 source_ref=de4967ffd03ab7a1cb0403f02d212520ddf339e8 -->
## `test_first_call_creates_cache_subsequent_calls_read(project: Path)`

Assert that syncing `calculator.py` makes 6 LLM calls, with cache creation tokens on the first and cache read tokens on the remaining five.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_cli_sync_auto_bootstraps_first_run fingerprint=2bcfc5f6118090e540d8bf670a676551d99e301c4e54623b6d9463d576f6ad4a body_fp=0446152775d776eff4ac7f5b9b80d42d215160e6bfea16084c6c8a51c196e14b source_ref=de4967ffd03ab7a1cb0403f02d212520ddf339e8 -->
## `test_cli_sync_auto_bootstraps_first_run(project: Path, monkeypatch)`

Verify that `trie sync --limit 10` in a fresh project exits 0 and reports "synced" using a patched `FakeClient`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_cli_sync_errors_on_missing_file fingerprint=ac055df6cd0b2982d47b7f5ddf8e532f4a1c38dfbefaefb6c220970792004945 body_fp=593ae5999d6b35bcd0b42ab5918a3e43c2cf3bb9a096ff4742864a02c74979d6 source_ref=de4967ffd03ab7a1cb0403f02d212520ddf339e8 -->
## `test_cli_sync_errors_on_missing_file(project: Path)`

Assert that `trie sync --file` exits with code 1 and reports "does not exist" for a missing path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_cli_sync_errors_when_no_config fingerprint=f24a74ab8515b27a1593fa499df188e4ff6ff93508d61d9afbceebd6daffa72e body_fp=3125e879d9d08c1dc0472ea9536c0cf6c1268b9cad006304cad383a0507d7430 source_ref=de4967ffd03ab7a1cb0403f02d212520ddf339e8 -->
## `test_cli_sync_errors_when_no_config(tmp_path: Path)`

Assert that `trie sync --file` exits with code 1 and mentions `trie.toml` when no config file exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:_init_git fingerprint=aa18a74813989bea6f6328ca8a6d8a11921def8852349e9daaea55280c606b4c body_fp=a54ff2ff3011ab9866c452228548f0d818bfc09387280aa900756a80ff686006 source_ref=de4967ffd03ab7a1cb0403f02d212520ddf339e8 -->
## `_init_git(repo: Path) -> None`

Initialize a bare git repository with test identity config in the given directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_first_sync_in_git_repo_stamps_source_ref fingerprint=3cf6343c5a3f146e8cd69642be21dbf0170a9a1f397e446884acb686081434a3 body_fp=580f9e1e49d9076d1a1a83abe78dc9049804cfb6d8dad4fe7a63d605bd807566 source_ref=de4967ffd03ab7a1cb0403f02d212520ddf339e8 -->
## `test_first_sync_in_git_repo_stamps_source_ref(project: Path)`

Assert that syncing a git-managed file stamps a 40-character SHA-1 `source_ref` on every section.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_sync_outside_git_repo_omits_source_ref fingerprint=9cf4b71feeef97f2de3c2c1fc42f325f5326babf39a788ac1bf7f712228a8649 body_fp=0e8ea04101c9abc4f24c0c82b45c21d44c098fe50fcda52d5574ceab2d4af0eb source_ref=de4967ffd03ab7a1cb0403f02d212520ddf339e8 -->
## `test_sync_outside_git_repo_omits_source_ref(project: Path)`

Assert that syncing outside a git repository produces triefact sections with no `source_ref=` field.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_resync_with_committed_history_takes_diff_aware_path fingerprint=1bd65ccdbd4b8049db3ee27391af7a14573c6e435c527292269a33fabdac7c75 body_fp=1f40098a73eba8515ce3ffb678387f80ac5a8d72b727f6c93dafca1ea4c08811 source_ref=de4967ffd03ab7a1cb0403f02d212520ddf339e8 -->
## `test_resync_with_committed_history_takes_diff_aware_path(project: Path)`

Assert that resyncing a committed-then-modified file injects `<previous_source>` and `<previous_prose>` into the generation request.

- Syncs, commits, modifies `strings.py`, then resyncs; inspects `FakeClient.requests_seen`.
- Confirms both old and new `shout` signatures appear in the request payload.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_resync_after_uncommitted_change_falls_back_to_cold fingerprint=5d3a03ac89ffaf02efdd90a0b822ca9d456842b2602ae29c024e7470ef1b6530 body_fp=3f064f5fcfc8b684e17be1f13ee08237a2b0c3bf18977c890f0a2fd67f67a4ba source_ref=de4967ffd03ab7a1cb0403f02d212520ddf339e8 -->
## `test_resync_after_uncommitted_change_falls_back_to_cold(project: Path)`

Verify that resync falls back to cold generation when the previous blob is unreachable in git due to no intervening commit.

- Stamps `source_ref` on first sync, then modifies the file without committing, making the blob unreachable.
- Asserts no `<previous_source>` block appears in any regeneration request.
<!-- trie:end -->