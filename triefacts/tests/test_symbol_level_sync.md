---
trie_version: 0.2.0
source: tests/test_symbol_level_sync.py
file_fingerprint: 095b0684ddd187048875f6455f8b04df03ce17a17acbf58a3cab545a227f059e
last_synced_at: '2026-07-29T17:54:44Z'
description: 'Symbol-level sync: regenerate only the symbols actually asked for.'
defines:
- kind: module
  qualified_name: tests/test_symbol_level_sync:__module__
  lines: 1-424
- kind: constant
  qualified_name: tests/test_symbol_level_sync:FIXTURE_DIR
  lines: 31-31
- kind: function
  qualified_name: tests/test_symbol_level_sync:_make_project
  lines: 34-45
- kind: function
  qualified_name: tests/test_symbol_level_sync:project
  lines: 49-50
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_symbols_to_regen_none_regens_every_symbol
  lines: 58-73
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_symbols_to_regen_subset_only_regenerates_listed_symbols
  lines: 76-119
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_symbols_to_regen_empty_set_runs_no_llm_calls
  lines: 122-158
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_symbols_to_regen_ignores_unknown_qnames
  lines: 161-183
- kind: function
  qualified_name: tests/test_symbol_level_sync:_scanned_store
  lines: 191-195
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_worklist_collects_qnames_for_directly_stale_symbols
  lines: 198-233
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_worklist_omits_files_marked_missing_triefact
  lines: 236-251
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_run_incremental_regenerates_only_changed_symbol
  lines: 259-309
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_underscored_symbols_are_documented_and_can_go_stale
  lines: 312-340
- kind: function
  qualified_name: tests/test_symbol_level_sync:_cli_file_sync
  lines: 348-364
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_cli_file_sync_fresh_file_is_a_free_noop
  lines: 367-378
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_cli_file_sync_regenerates_only_stale_symbols
  lines: 381-400
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_cli_file_sync_force_rewrites_everything
  lines: 403-413
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_cli_file_sync_never_synced_file_gets_full_cold_write
  lines: 416-423
incoming_refs: 0
outgoing_refs: 60
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
<!-- trie:section symbol=tests/test_symbol_level_sync:_make_project fingerprint=c97c2c26a919c215f8014b8f1407e668c378af04f12f290758ef0642a790e528 body_fp=b43a195466656c99b9ad9eb01d87ae32f55ce2ced1b276a0b7f1a790caffb295 source_ref=471fc4733e80d0ab351edd7a2e2e799ae8379b1a role=test-infrastructure -->
Creates a test project by copying fixture files and generating a trie.toml configuration.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:project fingerprint=31b657a420ab0ee010f44136750460d44af36302a21bf48ce10670807d6c13bc body_fp=12769c491e4bf4a8ea08241bdf3aa73feb864431aed593f978cf78d870bbbe23 source_ref=471fc4733e80d0ab351edd7a2e2e799ae8379b1a role=test-infrastructure -->
Creates a temporary project directory with fixture files and trie configuration for testing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_symbols_to_regen_none_regens_every_symbol fingerprint=fb12d83380d332e73109d6d987b1a7ee655b9a8af3f03ea95aa40df27debcfd1 body_fp=cdfb40bd96eefdf06eec4036b179697b31e6177631481997e3ccfc49810ff09b source_ref=471fc4733e80d0ab351edd7a2e2e799ae8379b1a role=documentation-sync -->
Tests that sync_single_file with symbols_to_regen=None regenerates all symbols in the file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_symbols_to_regen_subset_only_regenerates_listed_symbols fingerprint=c0e0dc6b3ec9514aadc4bb7814ca2d4a764c576b17b5668912db430004ce00de body_fp=c1aea8c65de678b0ff14765aa8e13d050aabd454fd918de1b2b9ee2c54de0661 source_ref=471fc4733e80d0ab351edd7a2e2e799ae8379b1a role=documentation-sync -->
Verifies that `sync_single_file` with a specific symbols_to_regen set only regenerates those symbols while preserving all other sections byte-identically.

- Performs initial sync to establish baseline triefact content
- Captures pre-sync section state for comparison
- Runs targeted sync requesting only "calculator:add" symbol regeneration  
- Asserts exactly one LLM call made and one symbol generated
- Validates untouched symbols remain byte-identical in body, body_fingerprint, and fingerprint
- Confirms targeted symbol received fresh documentation body
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_symbols_to_regen_empty_set_runs_no_llm_calls fingerprint=db98c682cf2f1faecc4a6940c1e50fddb07a427c5dc860642f6970a32737a007 body_fp=da1d735fcda419ef50a2988cc9f31d22a0216a09560a6f043be0c2431eeee6f8 source_ref=471fc4733e80d0ab351edd7a2e2e799ae8379b1a role=documentation-sync -->
Tests that sync_single_file with empty symbols_to_regen set runs zero LLM calls but updates file front matter.

- Verifies no symbols are generated or sent to LLM when empty set provided
- Confirms all section bytes remain identical, only front-matter timestamps change
- Validates the degenerate case where file is visited but no symbols regenerated
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_symbols_to_regen_ignores_unknown_qnames fingerprint=ad0de3a19c2b3d9f728703a235bdd9d9d564ed295a5a2df4c9dca30198d9151c body_fp=42059ff1e549f377baf2a65b3970d823faeb4cc28fd1e3217053124bde6bfa5e source_ref=471fc4733e80d0ab351edd7a2e2e799ae8379b1a role=documentation-sync -->
Verifies that `sync_single_file` silently ignores qualified names in `symbols_to_regen` that don't exist in current source, making no LLM calls and skipping all symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:_scanned_store fingerprint=be2171d309873933c9dd828dece87833bd3c117974cc17e64314491077d352a8 body_fp=e565d8aed5e4d306bd640e1e46f3ee0a102a4cbb7c9bba5ec4db0e4facf482f4 source_ref=471fc4733e80d0ab351edd7a2e2e799ae8379b1a role=test-infrastructure -->
Creates and returns a Store instance populated with scanned project data from the given project directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_worklist_collects_qnames_for_directly_stale_symbols fingerprint=f89a09ff2d19d054811e97848e9b3407918d480797ee1db5e217233dc7a2d961 body_fp=aa8fe8929db6e4d31dba8df9447bec00ae11f4c671b910c41d76eb3ffc8c14a8 source_ref=471fc4733e80d0ab351edd7a2e2e799ae8379b1a role=test -->
Tests that `compute_incremental_worklist` correctly identifies directly stale symbols for symbol-level regeneration.

- Creates baseline triefacts for calculator.py and strings.py
- Modifies the `add` function body in calculator.py to make it stale
- Verifies worklist contains only the modified symbol qualified name, not the entire file
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_worklist_omits_files_marked_missing_triefact fingerprint=a4aa6fab8ebd4667cbcb0251c911c91c9b4ff411519f99919cadf8354d1e30a7 body_fp=edabd9699a32a5b9cf43ff9c5e719bc451868c21621df6e4ae1ed1d4e7696a98 source_ref=471fc4733e80d0ab351edd7a2e2e799ae8379b1a role=test -->
Tests that files without existing triefacts are excluded from symbol-level regeneration mapping and use cold-write path instead.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_run_incremental_regenerates_only_changed_symbol fingerprint=a65113dda9afce87564899c0db24eb8071924c986e5b7ab1d8d70355c2cd8e75 body_fp=871297bcc33ccff1421363eb20024b71502320808c0f58eebc9ff7502d7e48f4 source_ref=471fc4733e80d0ab351edd7a2e2e799ae8379b1a role=test -->
Tests that run_incremental regenerates only the changed symbol while preserving all other sections byte-identically.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_underscored_symbols_are_documented_and_can_go_stale fingerprint=83103e9fad1ddc9c6dd458d47055a45da52160bc322cc88d14089ac18bbf805e body_fp=db69723a57dd772b8f709fe607559aab7c3d6df39b40ab6db2453fec92179b3c source_ref=471fc4733e80d0ab351edd7a2e2e799ae8379b1a role=change-detection -->
Verifies that underscored symbols receive documentation and are properly detected as stale when modified.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:_cli_file_sync fingerprint=0b3e6d813667f6227abf39dcb32e11d50e803dd9f2a876370142718d4ac136d5 body_fp=8774fc9bfab26597f8f391db853c22d9e78744950b60677ab0e1b1486f1ca9e2 source_ref=fff2a035ad30c13465a614cfe02c144204714790 role=test -->
Invoke `trie sync --file calculator.py [args]` via `CliRunner`, patching `make_client` with `FakeTrieClient`, and return the CLI result and collected clients list.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_cli_file_sync_fresh_file_is_a_free_noop fingerprint=d2d3343d0be8016b81ce107c1ad695b6accce25de94ea4389b0f2c181b4f70bf body_fp=353316d084dd2af718d7993a86352af2ff1937a9576e862f8c87fb1cb74a5c1b source_ref=fff2a035ad30c13465a614cfe02c144204714790 role=test -->
Assert that `trie sync --file` on a fully-synced file skips client construction entirely and prints an "all symbols fresh" hint.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_cli_file_sync_regenerates_only_stale_symbols fingerprint=7e81753d701d27244e2196aff9b783a23ea7a1af1b6985a656c4e90e2355a470 body_fp=ea3c325307b43eece41ee53e3a6794e4478e60ab1b2720a591fe8d8a7dfdac1e source_ref=fff2a035ad30c13465a614cfe02c144204714790 role=test -->
Verify that `trie sync --file` regenerates only the single edited symbol, not every symbol in the file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_cli_file_sync_force_rewrites_everything fingerprint=f47d2c5ae0553736ca882c4f2dd8d6f243e7ccddf07be9053d8d168c6121762c body_fp=0b52c35e0f6547eee3ad1b5cc64aa806c6a54fe916b4b3c5c4f06b3a65d0f050 source_ref=fff2a035ad30c13465a614cfe02c144204714790 role=test -->
Verify that `trie sync --file calculator.py --force` regenerates all 6 symbols, preserving full-rewrite semantics.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_cli_file_sync_never_synced_file_gets_full_cold_write fingerprint=eaa8e537643dc8e93083be36cacf5a49c3078cb6915861801aaa370e6ca2eefb body_fp=b351a8c7ae2ba025ecb8d973274297921b0917fa84d1e52299df4622e2bd212a source_ref=fff2a035ad30c13465a614cfe02c144204714790 role=test -->
Assert that `trie sync --file` on a never-synced file performs a full cold write, calling the LLM for all 6 symbols.
<!-- trie:end -->