---
trie_version: 0.3.0
source: tests/test_symbol_level_sync.py
file_fingerprint: 0e11602bef8ca5499b28b73a3759d358284a0941e17c9d7aa8502cfcee578b31
last_synced_at: '2026-08-02T21:18:59Z'
description: 'Symbol-level sync: regenerate only the symbols actually asked for.'
defines:
- kind: module
  qualified_name: tests/test_symbol_level_sync:__module__
  lines: 1-426
- kind: constant
  qualified_name: tests/test_symbol_level_sync:FIXTURE_DIR
  lines: 31-31
- kind: function
  qualified_name: tests/test_symbol_level_sync:_make_project
  lines: 34-45
  signature: 'def _make_project(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_symbol_level_sync:project
  lines: 49-50
  signature: 'def project(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_symbols_to_regen_none_regens_every_symbol
  lines: 58-73
  signature: 'def test_symbols_to_regen_none_regens_every_symbol(project: Path)'
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_symbols_to_regen_subset_only_regenerates_listed_symbols
  lines: 76-121
  signature: 'def test_symbols_to_regen_subset_only_regenerates_listed_symbols(project: Path)'
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_symbols_to_regen_empty_set_runs_no_llm_calls
  lines: 124-160
  signature: 'def test_symbols_to_regen_empty_set_runs_no_llm_calls(project: Path)'
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_symbols_to_regen_ignores_unknown_qnames
  lines: 163-185
  signature: 'def test_symbols_to_regen_ignores_unknown_qnames(project: Path)'
- kind: function
  qualified_name: tests/test_symbol_level_sync:_scanned_store
  lines: 193-197
  signature: 'def _scanned_store(project: Path) -> Store'
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_worklist_collects_qnames_for_directly_stale_symbols
  lines: 200-235
  signature: 'def test_worklist_collects_qnames_for_directly_stale_symbols(project: Path)'
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_worklist_omits_files_marked_missing_triefact
  lines: 238-253
  signature: 'def test_worklist_omits_files_marked_missing_triefact(project: Path)'
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_run_incremental_regenerates_only_changed_symbol
  lines: 261-311
  signature: 'def test_run_incremental_regenerates_only_changed_symbol(project: Path)'
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_underscored_symbols_are_documented_and_can_go_stale
  lines: 314-342
  signature: 'def test_underscored_symbols_are_documented_and_can_go_stale(project: Path)'
- kind: function
  qualified_name: tests/test_symbol_level_sync:_cli_file_sync
  lines: 350-366
  signature: 'def _cli_file_sync(project: Path, monkeypatch: pytest.MonkeyPatch, *args: str)'
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_cli_file_sync_fresh_file_is_a_free_noop
  lines: 369-380
  signature: 'def test_cli_file_sync_fresh_file_is_a_free_noop(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_cli_file_sync_regenerates_only_stale_symbols
  lines: 383-402
  signature: 'def test_cli_file_sync_regenerates_only_stale_symbols( project: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_cli_file_sync_force_rewrites_everything
  lines: 405-415
  signature: 'def test_cli_file_sync_force_rewrites_everything(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_cli_file_sync_never_synced_file_gets_full_cold_write
  lines: 418-425
  signature: 'def test_cli_file_sync_never_synced_file_gets_full_cold_write( project: Path, monkeypatch: pytest.MonkeyPatch )'
incoming_refs: 0
outgoing_refs: 63
---
<!-- trie:section symbol=tests/test_symbol_level_sync:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=da8aad35f588907e10af88c80b9961cbfdb6447ba33c348c07f99fa0427e2031 source_ref=471fc4733e80d0ab351edd7a2e2e799ae8379b1a role=test-infrastructure -->
Tests symbol-level sync functionality ensuring only requested symbols are regenerated while others remain byte-identical.

- Tests `sync_single_file` with `symbols_to_regen=None` (regenerates all symbols), subset selection (only specified symbols), and empty set (no LLM calls)
- Tests `compute_incremental_worklist` correctly identifies directly stale symbols and excludes files missing triefacts
- Tests `run_incremental` end-to-end behavior where single symbol edits trigger single symbol regenerations
- Validates underscored symbols are documented and participate in staleness detection
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:FIXTURE_DIR fingerprint=2635a439793a81128764c32977c9356050865c2ac61f8264769219675508cca2 body_fp=4cfd1dd2840cc5710ced1dc0cfeb73a77806e80815eb56e1b32623b9749e3835 source_ref=471fc4733e80d0ab351edd7a2e2e799ae8379b1a role=test-infrastructure -->
Path constant pointing to the test fixture directory containing a minimal repository for testing symbol-level sync behavior.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:_make_project fingerprint=c97c2c26a919c215f8014b8f1407e668c378af04f12f290758ef0642a790e528 body_fp=462d75a2d02496928d3648d0e2ce9b91a16d5fd87daa0715d75209d35e3a34c9 source_ref=471fc4733e80d0ab351edd7a2e2e799ae8379b1a role=test-infrastructure -->
## `def _make_project(tmp_path: Path) -> Path`

Creates a test project by copying fixture files and generating a trie.toml configuration.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:project fingerprint=31b657a420ab0ee010f44136750460d44af36302a21bf48ce10670807d6c13bc body_fp=396037efed80228868596502511586dfa8c586ef3d177c2ffb7ae3c550ba65f5 source_ref=471fc4733e80d0ab351edd7a2e2e799ae8379b1a role=test-infrastructure -->
## `def project(tmp_path: Path) -> Path`

Creates a temporary project directory with fixture files and trie configuration for testing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_symbols_to_regen_none_regens_every_symbol fingerprint=fb12d83380d332e73109d6d987b1a7ee655b9a8af3f03ea95aa40df27debcfd1 body_fp=c3939da91a0aa81c8345520b02a4580d3d99a445ecaefa4463b1f8c5f5b900b5 source_ref=471fc4733e80d0ab351edd7a2e2e799ae8379b1a role=documentation-sync -->
## `def test_symbols_to_regen_none_regens_every_symbol(project: Path)`

Tests that sync_single_file with symbols_to_regen=None regenerates all symbols in the file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_symbols_to_regen_subset_only_regenerates_listed_symbols fingerprint=de8f3cde059d8686b5ccdb200a9b2f52af54938e4e3b57ccfc3fffbb7b1bbb5d body_fp=5c38fe22eaace1b13c94da16892156006d70bc186c52b28adbc27cb73f48cb63 source_ref=ba132ca4ec16f79c91ab5de02848cba044a09111 role=documentation-sync -->
## `def test_symbols_to_regen_subset_only_regenerates_listed_symbols(project: Path)`

Verifies that `sync_single_file` with a specific symbols_to_regen set only regenerates those symbols while preserving all other sections byte-identically.

- Performs initial sync to establish baseline triefact content
- Captures pre-sync section state for comparison
- Runs targeted sync requesting only "calculator:add" symbol regeneration  
- Asserts exactly one LLM call made and one symbol generated
- Validates untouched symbols remain byte-identical in body, body_fingerprint, and fingerprint
- Confirms targeted symbol received fresh documentation body
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_symbols_to_regen_empty_set_runs_no_llm_calls fingerprint=db98c682cf2f1faecc4a6940c1e50fddb07a427c5dc860642f6970a32737a007 body_fp=e30bf2af930d259e9234d57eba52679315637e85abb57924d45cd1f3c2b5faad source_ref=471fc4733e80d0ab351edd7a2e2e799ae8379b1a role=documentation-sync -->
## `def test_symbols_to_regen_empty_set_runs_no_llm_calls(project: Path)`

Tests that sync_single_file with empty symbols_to_regen set runs zero LLM calls but updates file front matter.

- Verifies no symbols are generated or sent to LLM when empty set provided
- Confirms all section bytes remain identical, only front-matter timestamps change
- Validates the degenerate case where file is visited but no symbols regenerated
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_symbols_to_regen_ignores_unknown_qnames fingerprint=ad0de3a19c2b3d9f728703a235bdd9d9d564ed295a5a2df4c9dca30198d9151c body_fp=30e797a13b0095b5b53e5fa6639ad03ba73e0772070529fe1799ad829d707aeb source_ref=471fc4733e80d0ab351edd7a2e2e799ae8379b1a role=documentation-sync -->
## `def test_symbols_to_regen_ignores_unknown_qnames(project: Path)`

Verifies that `sync_single_file` silently ignores qualified names in `symbols_to_regen` that don't exist in current source, making no LLM calls and skipping all symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:_scanned_store fingerprint=be2171d309873933c9dd828dece87833bd3c117974cc17e64314491077d352a8 body_fp=c3d805e2f7fff16a1f4f8d55b882ec71cf29d78ac93da105ea2cb8d17818c5a5 source_ref=471fc4733e80d0ab351edd7a2e2e799ae8379b1a role=test-infrastructure -->
## `def _scanned_store(project: Path) -> Store`

Creates and returns a Store instance populated with scanned project data from the given project directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_worklist_collects_qnames_for_directly_stale_symbols fingerprint=f89a09ff2d19d054811e97848e9b3407918d480797ee1db5e217233dc7a2d961 body_fp=56bcb3f0eef7be21dc6ec6c42d8f0f12ead047bcfdedc2800f44ce16f5aaade3 source_ref=fff2a035ad30c13465a614cfe02c144204714790 role=test -->
## `def test_worklist_collects_qnames_for_directly_stale_symbols(project: Path)`

Tests that `compute_incremental_worklist` correctly identifies directly stale symbols for symbol-level regeneration.

- Creates baseline triefacts for calculator.py and strings.py
- Modifies the `add` function body in calculator.py to make it stale
- Verifies worklist contains only the modified symbol qualified name, not the entire file
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_worklist_omits_files_marked_missing_triefact fingerprint=a4aa6fab8ebd4667cbcb0251c911c91c9b4ff411519f99919cadf8354d1e30a7 body_fp=48a9ba66a6f3d719ab2e84c1e39d567b6f002809c22d9417956e95eee59cc0d1 source_ref=fff2a035ad30c13465a614cfe02c144204714790 role=test -->
## `def test_worklist_omits_files_marked_missing_triefact(project: Path)`

Tests that files without existing triefacts are excluded from symbol-level regeneration mapping and use cold-write path instead.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_run_incremental_regenerates_only_changed_symbol fingerprint=a65113dda9afce87564899c0db24eb8071924c986e5b7ab1d8d70355c2cd8e75 body_fp=5f221339e2103dc0ba3e6b234c543f8fdd23bc55f6edf0d647ab0fb2d66b09d9 source_ref=fff2a035ad30c13465a614cfe02c144204714790 role=test -->
## `def test_run_incremental_regenerates_only_changed_symbol(project: Path)`

Tests that run_incremental regenerates only the changed symbol while preserving all other sections byte-identically.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_underscored_symbols_are_documented_and_can_go_stale fingerprint=83103e9fad1ddc9c6dd458d47055a45da52160bc322cc88d14089ac18bbf805e body_fp=648cee62c2df432c75efe045a65d0cf53c98a4be1e7e594839014abbc8970adf source_ref=fff2a035ad30c13465a614cfe02c144204714790 role=change-detection -->
## `def test_underscored_symbols_are_documented_and_can_go_stale(project: Path)`

Verifies that underscored symbols receive documentation and are properly detected as stale when modified.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:_cli_file_sync fingerprint=0b3e6d813667f6227abf39dcb32e11d50e803dd9f2a876370142718d4ac136d5 body_fp=a4380a267acfc444381975b0b81456992fe8833847d828f78fb23b82a9c09910 source_ref=fff2a035ad30c13465a614cfe02c144204714790 role=test -->
## `def _cli_file_sync(project: Path, monkeypatch: pytest.MonkeyPatch, *args: str)`

Invoke `trie sync --file calculator.py [args]` via `CliRunner`, patching `make_client` with `FakeTrieClient`, and return the CLI result and collected clients list.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_cli_file_sync_fresh_file_is_a_free_noop fingerprint=d2d3343d0be8016b81ce107c1ad695b6accce25de94ea4389b0f2c181b4f70bf body_fp=59e7d8a0693139f5e4e1ddd1eda2797e2fb249f9f2ddbac43a824e64b57db4db source_ref=fff2a035ad30c13465a614cfe02c144204714790 role=test -->
## `def test_cli_file_sync_fresh_file_is_a_free_noop(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync --file` on a fully-synced file skips client construction entirely and prints an "all symbols fresh" hint.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_cli_file_sync_regenerates_only_stale_symbols fingerprint=7e81753d701d27244e2196aff9b783a23ea7a1af1b6985a656c4e90e2355a470 body_fp=66ac68a1d1b74de796e64d2f5828b83e92091be35751da981ebec416b9880752 source_ref=fff2a035ad30c13465a614cfe02c144204714790 role=test -->
## `def test_cli_file_sync_regenerates_only_stale_symbols( project: Path, monkeypatch: pytest.MonkeyPatch )`

Verify that `trie sync --file` regenerates only the single edited symbol, not every symbol in the file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_cli_file_sync_force_rewrites_everything fingerprint=f47d2c5ae0553736ca882c4f2dd8d6f243e7ccddf07be9053d8d168c6121762c body_fp=c7c7d6b3b7c4d3b6f74cf942b94a84628b17c404c4b21e3e301bf026a041f633 source_ref=fff2a035ad30c13465a614cfe02c144204714790 role=test -->
## `def test_cli_file_sync_force_rewrites_everything(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify that `trie sync --file calculator.py --force` regenerates all 6 symbols, preserving full-rewrite semantics.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_cli_file_sync_never_synced_file_gets_full_cold_write fingerprint=eaa8e537643dc8e93083be36cacf5a49c3078cb6915861801aaa370e6ca2eefb body_fp=45e2421ca098afff499b77027108858627e9081b195ce44571d3622d20de399f source_ref=fff2a035ad30c13465a614cfe02c144204714790 role=test -->
## `def test_cli_file_sync_never_synced_file_gets_full_cold_write( project: Path, monkeypatch: pytest.MonkeyPatch )`

Assert that `trie sync --file` on a never-synced file performs a full cold write, calling the LLM for all 6 symbols.
<!-- trie:end -->