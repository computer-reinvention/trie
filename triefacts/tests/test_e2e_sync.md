---
trie_version: 0.3.0
source: tests/test_e2e_sync.py
file_fingerprint: f576b00e1e385a115d1ef9deab637569c1e98d4400b2e1dd3d8963882769f296
last_synced_at: '2026-08-02T21:19:01Z'
description: End-to-end test for `trie sync --file` against the tiny fixture repo.
defines:
- kind: module
  qualified_name: tests/test_e2e_sync:__module__
  lines: 1-383
- kind: constant
  qualified_name: tests/test_e2e_sync:FIXTURE_DIR
  lines: 21-21
- kind: function
  qualified_name: tests/test_e2e_sync:project
  lines: 25-38
  signature: 'def project(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_e2e_sync:test_sync_single_file_writes_triefact
  lines: 41-73
  signature: 'def test_sync_single_file_writes_triefact(project: Path)'
- kind: function
  qualified_name: tests/test_e2e_sync:test_sync_records_exact_signatures_everywhere
  lines: 76-118
  signature: 'def test_sync_records_exact_signatures_everywhere(project: Path)'
- kind: function
  qualified_name: tests/test_e2e_sync:test_human_prose_between_sections_survives_resync
  lines: 121-156
  signature: 'def test_human_prose_between_sections_survives_resync(project: Path)'
- kind: function
  qualified_name: tests/test_e2e_sync:test_resync_updates_section_when_source_changes
  lines: 159-190
  signature: 'def test_resync_updates_section_when_source_changes(project: Path)'
- kind: function
  qualified_name: tests/test_e2e_sync:test_resync_removes_section_when_symbol_deleted
  lines: 193-218
  signature: 'def test_resync_removes_section_when_symbol_deleted(project: Path)'
- kind: function
  qualified_name: tests/test_e2e_sync:test_first_call_creates_cache_subsequent_calls_read
  lines: 221-235
  signature: 'def test_first_call_creates_cache_subsequent_calls_read(project: Path)'
- kind: function
  qualified_name: tests/test_e2e_sync:test_cli_sync_auto_bootstraps_first_run
  lines: 238-251
  signature: 'def test_cli_sync_auto_bootstraps_first_run(project: Path, monkeypatch)'
- kind: function
  qualified_name: tests/test_e2e_sync:test_cli_sync_errors_on_missing_file
  lines: 254-258
  signature: 'def test_cli_sync_errors_on_missing_file(project: Path)'
- kind: function
  qualified_name: tests/test_e2e_sync:test_cli_sync_errors_when_no_config
  lines: 261-267
  signature: 'def test_cli_sync_errors_when_no_config(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_e2e_sync:_init_git
  lines: 273-279
  signature: 'def _init_git(repo: Path) -> None'
- kind: function
  qualified_name: tests/test_e2e_sync:test_first_sync_in_git_repo_stamps_source_ref
  lines: 282-300
  signature: 'def test_first_sync_in_git_repo_stamps_source_ref(project: Path)'
- kind: function
  qualified_name: tests/test_e2e_sync:test_sync_outside_git_repo_omits_source_ref
  lines: 303-315
  signature: 'def test_sync_outside_git_repo_omits_source_ref(project: Path)'
- kind: function
  qualified_name: tests/test_e2e_sync:test_resync_with_committed_history_takes_diff_aware_path
  lines: 318-351
  signature: 'def test_resync_with_committed_history_takes_diff_aware_path(project: Path)'
- kind: function
  qualified_name: tests/test_e2e_sync:test_resync_after_uncommitted_change_falls_back_to_cold
  lines: 354-382
  signature: 'def test_resync_after_uncommitted_change_falls_back_to_cold(project: Path)'
incoming_refs: 0
outgoing_refs: 66
---
<!-- trie:section symbol=tests/test_e2e_sync:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=653c3532b57d63cc34bb4a86676a78f1c7a4262f201852f3e89cef2d0aedf3a8 source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 role=test-infrastructure -->
End-to-end tests for `trie sync --file` command using a deterministic fake client for offline testing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:FIXTURE_DIR fingerprint=2635a439793a81128764c32977c9356050865c2ac61f8264769219675508cca2 body_fp=677a3f4ccac58c7bd543344a0bd7a7979f14f637426aef62522ce229056ea347 source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 role=test-infrastructure -->
Path to the tiny fixture repository used for end-to-end testing of sync operations.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:project fingerprint=16df3ebd676a6f8d2473a730ffb75c5fd86a5da52f7caae13faab42c03ae674f body_fp=dc84afe8e5433a7cae6fdf427285d92099897aea083d12b38983bd8af862b4ab source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 role=test-infrastructure -->
## `def project(tmp_path: Path) -> Path`

Creates a temporary test project by copying the tiny fixture repo and writing a minimal trie.toml configuration file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_sync_single_file_writes_triefact fingerprint=2121e6316c2fa3f95a4d992213459338ae92f48da5d912f5f6b8f59b7d1c9b07 body_fp=af15aa3209051a6fa96028ee16a625815cc9ee97f02c2d3247d74c69f7394914 source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 role=test -->
## `def test_sync_single_file_writes_triefact(project: Path)`

Tests that `sync_single_file` generates complete triefact documentation with proper structure and metadata.

- Verifies all 6 symbols from calculator.py are documented (including private functions)
- Checks triefact file contains front matter with version, source path, and fingerprint
- Confirms all expected qualified names appear in generated sections
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_sync_records_exact_signatures_everywhere fingerprint=f3f795ab93199a5ef12fa15daaf4245ec6eab05bc3a05a075f951e65136b01a0 body_fp=f6300bca0beaadd8195f4f6492b50e503bc00244a88ba9c2ffd7122943afe8d0 source_ref=e988a898c119282008f98c54c982b2e0e356dbe3 role=test -->
## `def test_sync_records_exact_signatures_everywhere(project: Path)`

Assert that after syncing `calculator.py` with a LLM that emits deliberately wrong signature headings, every symbol's `defines` entry and section body carry the parser-derived signature instead.

- Verifies both frontmatter `signature` field (a) and leading `## \`sig\`` heading in section body (b).
- Symbols of `SIGNATURELESS_KINDS` are asserted to have no `signature` key in their `defines` entry.
- Sanity-checks the full return-annotated signature for `calculator:add` end-to-end.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_human_prose_between_sections_survives_resync fingerprint=d78590d8ab891f9ac8defc53cb0b9e62d7aef77faadb7f976af01e987fff1557 body_fp=aac60e08bdcd0bf7c1854638672e8dc53b3bee0f9ddcacc714db23a831934be3 source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 role=documentation-sync -->
## `def test_human_prose_between_sections_survives_resync(project: Path)`

Verifies that user-added prose between sections persists across triefact regenerations. Creates initial triefacts, adds custom content, resyncs, and confirms the manual additions survive while generated sections update.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_resync_updates_section_when_source_changes fingerprint=663c27217202cf7408645525b391142168f1625b4ac47b0fc35634aa95882ec6 body_fp=702807f462613c3138adac3bf0859b71e6f9747228afdb31e5c13265d9d30cd6 source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 role=test-infrastructure -->
## `def test_resync_updates_section_when_source_changes(project: Path)`

Tests that sync updates triefact sections when source code changes by modifying a function signature and verifying the section fingerprint changes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_resync_removes_section_when_symbol_deleted fingerprint=673de21fdb3f1dda0cf202daf792ec31139e2884e104d93e20a5e69b42a0b18d body_fp=73fd6d3c217aaf6292864c51fa591cd9dd13172ac6efd06822f2fffc50da85e4 source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 role=test-infrastructure -->
## `def test_resync_removes_section_when_symbol_deleted(project: Path)`

Verifies that sync removes triefact sections when their corresponding symbols are deleted from source.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_first_call_creates_cache_subsequent_calls_read fingerprint=71b11ded7011ab869391c4cffb47b16e972ba1ad5a80529fa9955f80101bd632 body_fp=20d7d56abff01dae5d1cedccfcd22f26fa21c1b0ec114c4f07de4edccc865071 source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 role=test-infrastructure -->
## `def test_first_call_creates_cache_subsequent_calls_read(project: Path)`

Verifies that sync operations correctly track prompt cache creation and read token counts across multiple LLM calls.

- Expects 6 symbols to be documented from calculator.py (including private `_internal_helper`)
- Validates that 6 LLM calls generate 600 cache creation and 600 cache read tokens
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_cli_sync_auto_bootstraps_first_run fingerprint=f8ac8941d8c66dd7a5fcadf8f18b78de6836b689711714fbc279bbbfc840e476 body_fp=32e439d2924e207f3741849f26e906e6b1162b663c89af53a21ce5742fa5c369 source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 role=test-infrastructure -->
## `def test_cli_sync_auto_bootstraps_first_run(project: Path, monkeypatch)`

Tests that `trie sync --limit 10` auto-detects first-run bootstrap mode in a fresh project.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_cli_sync_errors_on_missing_file fingerprint=ac055df6cd0b2982d47b7f5ddf8e532f4a1c38dfbefaefb6c220970792004945 body_fp=b413950a099f2bbdd79dd1763e420afcbd435fe2a0c39003031a466ae7a03be3 source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 role=test-infrastructure -->
## `def test_cli_sync_errors_on_missing_file(project: Path)`

Verifies that `trie sync --file` exits with error code 1 when the specified file does not exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_cli_sync_errors_when_no_config fingerprint=f24a74ab8515b27a1593fa499df188e4ff6ff93508d61d9afbceebd6daffa72e body_fp=919a2d121f5f6b829ff9f337f10bc531338d8b380a40651038ca8a30a29594e5 source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 role=test-infrastructure -->
## `def test_cli_sync_errors_when_no_config(tmp_path: Path)`

Verifies that `trie sync --file` exits with code 1 when no trie.toml config file is found.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:_init_git fingerprint=aa18a74813989bea6f6328ca8a6d8a11921def8852349e9daaea55280c606b4c body_fp=c4f1e54a338162cb5865d8a9558232b2ad2b595a3fe70872714fa5460ac71943 source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 role=test-infrastructure -->
## `def _init_git(repo: Path) -> None`

Initialize a git repository in the specified directory for testing blob hash operations.

- Runs `git init` with quiet mode and main branch
- Sets test user email and name configuration
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_first_sync_in_git_repo_stamps_source_ref fingerprint=33d11105b1829e30a5df223660e0fa452090c1682228d299acb163aaa9e36dd5 body_fp=78e7b0b8e9871c61b710c69372df92ed4d9c65c9354497b0a74c3bdaf603e46d source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 role=test-infrastructure -->
## `def test_first_sync_in_git_repo_stamps_source_ref(project: Path)`

Tests that first sync against a git-managed file stamps SHA-1 source_ref in every generated section.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_sync_outside_git_repo_omits_source_ref fingerprint=c4a59b57a38fc9c1313e196f759d91817d606129b39ad9dc5ff44c10ed3ed269 body_fp=f5def10d2a5b5f1da955d11d06eaeae3fb9fe70f85dbfba77163bf45a58849d0 source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 role=test-infrastructure -->
## `def test_sync_outside_git_repo_omits_source_ref(project: Path)`

Verifies that sync operations outside git repositories omit source_ref fields in generated triefact sections.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_resync_with_committed_history_takes_diff_aware_path fingerprint=2500a2e8833c01b96853fdd0a8618dad6e2bb805468ca30c82840208dc366804 body_fp=4e86bb8d0d8f990114eb506671fb9e0ec1c740001ed8d600cb4b0aaf45b92ee5 source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 role=test-infrastructure -->
## `def test_resync_with_committed_history_takes_diff_aware_path(project: Path)`

Verifies that resync of a committed file provides previous source and prose to the generator for diff-aware regeneration.

- Sets up git repo, syncs file, commits, modifies source, then resyncs
- Asserts that second client receives previous_source, previous_prose, and current_source blocks
<!-- trie:end -->
<!-- trie:section symbol=tests/test_e2e_sync:test_resync_after_uncommitted_change_falls_back_to_cold fingerprint=e2d41f6911f7282fc7dce6bf2ecf2f7413b786ca21f7d82187740907dfe0eba3 body_fp=ca26746b464efb66dc43bb7a06024ed1d4d625046b63eed20ab52c99f4db55d2 source_ref=6175e8a219cd65bd2bd2bc0d015d010877051786 role=documentation-sync -->
## `def test_resync_after_uncommitted_change_falls_back_to_cold(project: Path)`

Verifies sync falls back to cold generation when previous blob is unreachable from git history.
<!-- trie:end -->