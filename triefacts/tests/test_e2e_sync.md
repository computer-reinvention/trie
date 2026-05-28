---
trie_version: 0.1.5
source: tests/test_e2e_sync.py
file_fingerprint: 927e6b77c5b8b24d71444ae286de99af096680f8b42cc8f5e3c2c3bff8df0d03
last_synced_at: '2026-05-28T14:53:25Z'
description: End-to-end test for `trie sync --file` against the tiny fixture repo.
defines:
- kind: module
  qualified_name: tests/test_e2e_sync:__module__
  lines: 1-338
- kind: constant
  qualified_name: tests/test_e2e_sync:FIXTURE_DIR
  lines: 21-21
- kind: function
  qualified_name: tests/test_e2e_sync:project
  lines: 25-38
- kind: function
  qualified_name: tests/test_e2e_sync:test_sync_single_file_writes_triefact
  lines: 41-73
- kind: function
  qualified_name: tests/test_e2e_sync:test_human_prose_between_sections_survives_resync
  lines: 76-111
- kind: function
  qualified_name: tests/test_e2e_sync:test_resync_updates_section_when_source_changes
  lines: 114-145
- kind: function
  qualified_name: tests/test_e2e_sync:test_resync_removes_section_when_symbol_deleted
  lines: 148-173
- kind: function
  qualified_name: tests/test_e2e_sync:test_first_call_creates_cache_subsequent_calls_read
  lines: 176-190
- kind: function
  qualified_name: tests/test_e2e_sync:test_cli_sync_auto_bootstraps_first_run
  lines: 193-206
- kind: function
  qualified_name: tests/test_e2e_sync:test_cli_sync_errors_on_missing_file
  lines: 209-213
- kind: function
  qualified_name: tests/test_e2e_sync:test_cli_sync_errors_when_no_config
  lines: 216-222
- kind: function
  qualified_name: tests/test_e2e_sync:_init_git
  lines: 228-234
- kind: function
  qualified_name: tests/test_e2e_sync:test_first_sync_in_git_repo_stamps_source_ref
  lines: 237-255
- kind: function
  qualified_name: tests/test_e2e_sync:test_sync_outside_git_repo_omits_source_ref
  lines: 258-270
- kind: function
  qualified_name: tests/test_e2e_sync:test_resync_with_committed_history_takes_diff_aware_path
  lines: 273-306
- kind: function
  qualified_name: tests/test_e2e_sync:test_resync_after_uncommitted_change_falls_back_to_cold
  lines: 309-337
incoming_refs: 0
outgoing_refs: 36
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
<!-- trie:section symbol=tests/test_e2e_sync:project fingerprint=16df3ebd676a6f8d2473a730ffb75c5fd86a5da52f7caae13faab42c03ae674f body_fp=f6a1e7524674455f4a09e957fd2fcccbd82b99e7ec8d1677b49e0d0c8e59b099 source_ref=de4967ffd03ab7a1cb0403f02d212520ddf339e8 -->
## `project(tmp_path: Path) -> Path`

pytest fixture that copies the tiny fixture repo into a temp directory and writes a minimal `trie.toml`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_sync_single_file_writes_triefact fingerprint=2121e6316c2fa3f95a4d992213459338ae92f48da5d912f5f6b8f59b7d1c9b07 body_fp=35bff4e706b9a4cf948aabebb6285cc7ba1fb3525e639467c40ccbd3ffaf1b5c source_ref=64fa57905e1efe9489f5ca64acb79dfa4e7a99a1 -->
## `test_sync_single_file_writes_triefact(project: Path)`

Verify `sync_single_file` generates 6 sections (all symbols, including private), writes valid front matter, and records every expected qname.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_human_prose_between_sections_survives_resync fingerprint=d78590d8ab891f9ac8defc53cb0b9e62d7aef77faadb7f976af01e987fff1557 body_fp=d75abdad3cbc83d7a64f23f5464cb5f383ad036d285703001e7bc4e1bc6670ed source_ref=64fa57905e1efe9489f5ca64acb79dfa4e7a99a1 -->
## `test_human_prose_between_sections_survives_resync(project: Path)`

Assert that hand-written Markdown between trie-managed sections is preserved across a second sync.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_resync_updates_section_when_source_changes fingerprint=663c27217202cf7408645525b391142168f1625b4ac47b0fc35634aa95882ec6 body_fp=1297b81dc3235d7b51dcc870a4e930e0b3dc030624fcb0fef007910306948e01 source_ref=64fa57905e1efe9489f5ca64acb79dfa4e7a99a1 -->
## `test_resync_updates_section_when_source_changes(project: Path)`

Assert that resyncing after a source change produces a section with a different fingerprint.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_resync_removes_section_when_symbol_deleted fingerprint=673de21fdb3f1dda0cf202daf792ec31139e2884e104d93e20a5e69b42a0b18d body_fp=4338148b2fe728e2ddbe91cca1d525708a12df94852870cb715def5000ade823 source_ref=64fa57905e1efe9489f5ca64acb79dfa4e7a99a1 -->
## `test_resync_removes_section_when_symbol_deleted(project: Path)`

Assert that resyncing after a symbol is deleted from source removes its triefact section and decrements `sections_removed`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_first_call_creates_cache_subsequent_calls_read fingerprint=71b11ded7011ab869391c4cffb47b16e972ba1ad5a80529fa9955f80101bd632 body_fp=83865f2fcccf6769df13b423be9e34140e027f0fbf3ac8382a33e5e52348a140 source_ref=64fa57905e1efe9489f5ca64acb79dfa4e7a99a1 -->
## `test_first_call_creates_cache_subsequent_calls_read(project: Path)`

Assert that syncing `calculator.py` makes 6 LLM calls, accumulating 600 cache creation tokens and 600 cache read tokens total.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_cli_sync_auto_bootstraps_first_run fingerprint=f8ac8941d8c66dd7a5fcadf8f18b78de6836b689711714fbc279bbbfc840e476 body_fp=0446152775d776eff4ac7f5b9b80d42d215160e6bfea16084c6c8a51c196e14b source_ref=64fa57905e1efe9489f5ca64acb79dfa4e7a99a1 -->
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
<!-- trie:section symbol=tests/test_e2e_sync:test_first_sync_in_git_repo_stamps_source_ref fingerprint=33d11105b1829e30a5df223660e0fa452090c1682228d299acb163aaa9e36dd5 body_fp=580f9e1e49d9076d1a1a83abe78dc9049804cfb6d8dad4fe7a63d605bd807566 source_ref=64fa57905e1efe9489f5ca64acb79dfa4e7a99a1 -->
## `test_first_sync_in_git_repo_stamps_source_ref(project: Path)`

Assert that syncing a git-managed file stamps a 40-character SHA-1 `source_ref` on every section.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_sync_outside_git_repo_omits_source_ref fingerprint=c4a59b57a38fc9c1313e196f759d91817d606129b39ad9dc5ff44c10ed3ed269 body_fp=0e8ea04101c9abc4f24c0c82b45c21d44c098fe50fcda52d5574ceab2d4af0eb source_ref=64fa57905e1efe9489f5ca64acb79dfa4e7a99a1 -->
## `test_sync_outside_git_repo_omits_source_ref(project: Path)`

Assert that syncing outside a git repository produces triefact sections with no `source_ref=` field.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_resync_with_committed_history_takes_diff_aware_path fingerprint=2500a2e8833c01b96853fdd0a8618dad6e2bb805468ca30c82840208dc366804 body_fp=1fe444a992a87779ded24ab4e073ad89b48cdc864f2770fe17bd519220ed365c source_ref=64fa57905e1efe9489f5ca64acb79dfa4e7a99a1 -->
## `test_resync_with_committed_history_takes_diff_aware_path(project: Path)`

Assert that resyncing a committed-then-modified file injects `<previous_source>` and `<previous_prose>` into the generation request.

- Syncs, commits, modifies `strings.py`, then resyncs; inspects `FakeTrieClient.last_user_prompt`.
- Confirms `<previous_source>`, `<previous_prose>`, and `<current_source>` appear in the last prompt.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_resync_after_uncommitted_change_falls_back_to_cold fingerprint=e2d41f6911f7282fc7dce6bf2ecf2f7413b786ca21f7d82187740907dfe0eba3 body_fp=3f064f5fcfc8b684e17be1f13ee08237a2b0c3bf18977c890f0a2fd67f67a4ba source_ref=64fa57905e1efe9489f5ca64acb79dfa4e7a99a1 -->
## `test_resync_after_uncommitted_change_falls_back_to_cold(project: Path)`

Verify that resync falls back to cold generation when the previous blob is unreachable in git due to no intervening commit.

- Stamps `source_ref` on first sync, then modifies the file without committing, making the blob unreachable.
- Asserts no `<previous_source>` block appears in any regeneration request.
<!-- trie:end -->