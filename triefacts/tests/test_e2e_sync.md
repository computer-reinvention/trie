---
trie_version: 0.1.5
source: tests/test_e2e_sync.py
file_fingerprint: 0646622e2dfecd7e8ce9de6f63ce953220ab28e2635789a46005fd634b7bb164
last_synced_at: '2026-06-03T20:54:19Z'
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
<!-- trie:section symbol=tests/test_e2e_sync:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=653c3532b57d63cc34bb4a86676a78f1c7a4262f201852f3e89cef2d0aedf3a8 source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 -->
End-to-end tests for `trie sync --file` command using a deterministic fake client for offline testing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:FIXTURE_DIR fingerprint=2635a439793a81128764c32977c9356050865c2ac61f8264769219675508cca2 body_fp=a2760554a689e6ee3c7f0e09ea41b6dbb348c7b6f3b3703a513ce45cf45cfd55 source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 -->
Path to the tiny_repo test fixture directory used by end-to-end sync tests.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:project fingerprint=16df3ebd676a6f8d2473a730ffb75c5fd86a5da52f7caae13faab42c03ae674f body_fp=e3e8f73e4f6ebd6edf33fd3a083c9e2436c98a1c2c25dc119a1083a6fcd7f7ed source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 -->
Creates a test project by copying the tiny fixture repository to a temporary directory and writing a minimal trie.toml configuration file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_sync_single_file_writes_triefact fingerprint=2121e6316c2fa3f95a4d992213459338ae92f48da5d912f5f6b8f59b7d1c9b07 body_fp=486a500fae32748eadc39d24192d8b9546e73d7947fd0fc3d05cfea1bdcba468 source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 -->
Tests that sync_single_file generates triefact files with proper structure and documents all symbols.

- Verifies 6 symbols documented including private helpers
- Checks triefact file creation at expected path with front matter
- Validates all qualified names present in generated sections
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_human_prose_between_sections_survives_resync fingerprint=d78590d8ab891f9ac8defc53cb0b9e62d7aef77faadb7f976af01e987fff1557 body_fp=2bea34cd72d91b3edbee29eae6b1fbed62b5768f4f40005fa4e447b6935e90ee source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 -->
Tests that human-written prose between triefact sections survives resync operations.

- Creates triefact, adds human prose after metadata section, resyncs, verifies prose preserved
- Confirms generated sections still exist after manual edits
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_resync_updates_section_when_source_changes fingerprint=663c27217202cf7408645525b391142168f1625b4ac47b0fc35634aa95882ec6 body_fp=fb9f3b160ed1dff9543994f18b1770c3af6920b2233d1a2396b9b8a9135db53d source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 -->
Test that resyncing a file after modifying source code updates the corresponding triefact section with a new fingerprint.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_resync_removes_section_when_symbol_deleted fingerprint=673de21fdb3f1dda0cf202daf792ec31139e2884e104d93e20a5e69b42a0b18d body_fp=d230c594d9219276d1a941ab3a586b7150ab27bc219689d20c0c6e2555104be4 source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 -->
Verifies that resync removes triefact sections when their corresponding source symbols are deleted.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_first_call_creates_cache_subsequent_calls_read fingerprint=71b11ded7011ab869391c4cffb47b16e972ba1ad5a80529fa9955f80101bd632 body_fp=5f11a4b872e9b950df87bef08a0dbdbc6993bf40bdaa488a365dee16a2c5aff1 source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 -->
Verifies that sync_single_file correctly tracks cache creation and read tokens across multiple LLM client calls.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_cli_sync_auto_bootstraps_first_run fingerprint=f8ac8941d8c66dd7a5fcadf8f18b78de6836b689711714fbc279bbbfc840e476 body_fp=3a99d2cd0783a176e4b7dcda26b0ca0beb613447f4304c32ff2736ab9c1b41b9 source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 -->
Tests that `trie sync --limit 10` in a fresh project auto-detects first-run bootstrap and succeeds.

- Mocks `make_client` to return a `FakeTrieClient`
- Verifies exit code 0 and "synced" appears in output
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_cli_sync_errors_on_missing_file fingerprint=ac055df6cd0b2982d47b7f5ddf8e532f4a1c38dfbefaefb6c220970792004945 body_fp=7fbe5b3453091839d1ce3f1118e1095212d05c442c604ed2a1878a7781c120cc source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 -->
Verifies that `trie sync --file` with a non-existent file path returns exit code 1 and error message.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_cli_sync_errors_when_no_config fingerprint=f24a74ab8515b27a1593fa499df188e4ff6ff93508d61d9afbceebd6daffa72e body_fp=564fd6544d784684836ff3f03f6952170fcafed558a23f0bc99d97bde40bd16e source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 -->
Verifies the CLI exits with error when syncing a file outside a trie project directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:_init_git fingerprint=aa18a74813989bea6f6328ca8a6d8a11921def8852349e9daaea55280c606b4c body_fp=91ea844ccfad36fa319a1c2ec20ab280a0aa6772cc318083486616acc951434f source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 -->
Initializes a git repository in the specified directory for testing blob hash operations.

- Sets up git with test user credentials and main branch
- Enables `compute_blob_hash` and `retrieve_blob` functionality in tests
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_first_sync_in_git_repo_stamps_source_ref fingerprint=33d11105b1829e30a5df223660e0fa452090c1682228d299acb163aaa9e36dd5 body_fp=b8667562b8430cc73c44aaf467e93efcb08e4bc1233e69386e6146d63ffc5932 source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 -->
Tests that syncing a file in a git repository stamps source_ref with SHA-1 blob hashes in all generated sections.

- Initializes git repository and syncs strings.py module
- Verifies every triefact section contains a 40-character source_ref field
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_sync_outside_git_repo_omits_source_ref fingerprint=c4a59b57a38fc9c1313e196f759d91817d606129b39ad9dc5ff44c10ed3ed269 body_fp=d3245d64b6ce64366dc6f33821995a1b1ea3fe488b8d25c2303aef54725c1976 source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 -->
Verifies that sync operations outside git repositories omit source_ref fields from generated triefact sections.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_resync_with_committed_history_takes_diff_aware_path fingerprint=2500a2e8833c01b96853fdd0a8618dad6e2bb805468ca30c82840208dc366804 body_fp=1ce68bedaea4c0b54574f5f218de65d36895474e2ca3bfc8eb85676567a81949 source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 -->
Tests that resync after commit uses diff-aware mode by passing previous source and prose to the generator.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_resync_after_uncommitted_change_falls_back_to_cold fingerprint=e2d41f6911f7282fc7dce6bf2ecf2f7413b786ca21f7d82187740907dfe0eba3 body_fp=a9ab98a449554fbad28dd77412cbbb617c5a128029368ab9bcb00ff05d493332 source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 -->
Tests that resync falls back to cold generation when the previous source version isn't in git's object store.
<!-- trie:end -->