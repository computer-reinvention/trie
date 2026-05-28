---
trie_version: 0.1.5
source: tests/test_symbol_level_sync.py
file_fingerprint: 557cc0ef4d2d6936d9449cad54b52e04caa6f9bc6c9c0b5ae7dabf808cdebcd5
last_synced_at: '2026-05-28T14:39:40Z'
description: 'Symbol-level sync: regenerate only the symbols actually asked for.'
defines:
- kind: module
  qualified_name: tests/test_symbol_level_sync:__module__
  lines: 1-341
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
incoming_refs: 0
outgoing_refs: 33
---
<!-- trie:section symbol=tests/test_symbol_level_sync:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=14c53c9f2656fb060ed16ca328e9b47aa46f05f215ff7f6f4313a96bec616dd9 source_ref=0013b0d2bb1e2a586f0828e9253a2620db3d60a9 -->
## `tests/test_symbol_level_sync`

Test suite for symbol-level sync: verifying partial regeneration, worklist computation, and end-to-end incremental sync behaviour.

- `FIXTURE_DIR`: points to `tests/fixtures/tiny_repo` source fixtures
- `FakeClient`: deterministic LLM stub; each call returns a uniquely-tagged body
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:FIXTURE_DIR fingerprint=2635a439793a81128764c32977c9356050865c2ac61f8264769219675508cca2 body_fp=8a16487de16ba9146dfdb7d585eaf10db7487d08248770243258eef11ae67233 source_ref=0013b0d2bb1e2a586f0828e9253a2620db3d60a9 -->
## `FIXTURE_DIR: Path`

Absolute path to the `tests/fixtures/tiny_repo` directory used as the base for test project copies.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:_make_project fingerprint=c97c2c26a919c215f8014b8f1407e668c378af04f12f290758ef0642a790e528 body_fp=36614e935e4107b4c01b60b74d4733a27228231c4b090a91bb74b3716cad5639 source_ref=0013b0d2bb1e2a586f0828e9253a2620db3d60a9 -->
## `_make_project(tmp_path: Path) -> Path`

Copy the `tiny_repo` fixture into `tmp_path/demo` and write a `trie.toml` config, returning the project root.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:project fingerprint=31b657a420ab0ee010f44136750460d44af36302a21bf48ce10670807d6c13bc body_fp=374bcef3b1a3bd7420e66ea76ea713073fc98e9a7e4e71732752e5d6a7d3f0d3 source_ref=0013b0d2bb1e2a586f0828e9253a2620db3d60a9 -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a temporary demo project copied from the fixture directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_symbols_to_regen_none_regens_every_symbol fingerprint=fb12d83380d332e73109d6d987b1a7ee655b9a8af3f03ea95aa40df27debcfd1 body_fp=ac5215a40e79f73f59cbeb3e88062ffc6767c0fb2f48bc27a03029e37211ecd5 source_ref=471fc4733e80d0ab351edd7a2e2e799ae8379b1a -->
## `test_symbols_to_regen_none_regens_every_symbol(project: Path)`

Assert that `sync_single_file` with `symbols_to_regen=None` regenerates all 6 symbols and skips none.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_symbols_to_regen_subset_only_regenerates_listed_symbols fingerprint=c0e0dc6b3ec9514aadc4bb7814ca2d4a764c576b17b5668912db430004ce00de body_fp=b6b2f56fc4529a5f6f053c33eb3e771ca9a015c5d79be443ff6dd6e88e29b4ea source_ref=471fc4733e80d0ab351edd7a2e2e799ae8379b1a -->
## `test_symbols_to_regen_subset_only_regenerates_listed_symbols(project: Path)`

Assert that `sync_single_file` with a subset `symbols_to_regen` calls the LLM only for listed symbols and leaves all other sections byte-identical.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_symbols_to_regen_empty_set_runs_no_llm_calls fingerprint=db98c682cf2f1faecc4a6940c1e50fddb07a427c5dc860642f6970a32737a007 body_fp=9052924d389beb69dfbbd5cec384a031ef36fe518fb4d96251dd9df2346762cc source_ref=471fc4733e80d0ab351edd7a2e2e799ae8379b1a -->
## `test_symbols_to_regen_empty_set_runs_no_llm_calls(project: Path)`

Assert that `sync_single_file` with `symbols_to_regen=set()` makes zero LLM calls, skips all 6 symbols, and preserves every section body byte-for-byte.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_symbols_to_regen_ignores_unknown_qnames fingerprint=ad0de3a19c2b3d9f728703a235bdd9d9d564ed295a5a2df4c9dca30198d9151c body_fp=30f48fdc722019b99762772e3bea51ac290a2467d61b37f17d265c609738087e source_ref=471fc4733e80d0ab351edd7a2e2e799ae8379b1a -->
## `test_symbols_to_regen_ignores_unknown_qnames(project: Path)`

Verify that qnames in `symbols_to_regen` that don't exist in the current source are silently ignored, triggering zero LLM calls.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:_scanned_store fingerprint=be2171d309873933c9dd828dece87833bd3c117974cc17e64314491077d352a8 body_fp=3304e352da39298e9fd1e9b5b3d9c7ec217e79779c79c2cc9168d1fb0acfe2fd source_ref=0013b0d2bb1e2a586f0828e9253a2620db3d60a9 -->
## `_scanned_store(project: Path) -> Store`

Create and return a `Store` populated by scanning the given project directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_worklist_collects_qnames_for_directly_stale_symbols fingerprint=f89a09ff2d19d054811e97848e9b3407918d480797ee1db5e217233dc7a2d961 body_fp=af452f4c3ad5341449d2844b3b47450f24bc3e07d30cc21fe2462351f3185694 source_ref=471fc4733e80d0ab351edd7a2e2e799ae8379b1a -->
## `test_worklist_collects_qnames_for_directly_stale_symbols(project: Path)`

Assert that editing a single symbol's body causes `compute_incremental_worklist` to populate `regen_qnames_by_file` with exactly that qname.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_worklist_omits_files_marked_missing_triefact fingerprint=a4aa6fab8ebd4667cbcb0251c911c91c9b4ff411519f99919cadf8354d1e30a7 body_fp=8ae363b46362adbdf180617472e7fe047c2329bc9989a53f70515316e01a369c source_ref=0013b0d2bb1e2a586f0828e9253a2620db3d60a9 -->
## `test_worklist_omits_files_marked_missing_triefact(project: Path)`

Assert that files with no existing triefact appear in `directly_stale` but not in `regen_qnames_by_file`, triggering full cold-write instead of symbol-level regen.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_run_incremental_regenerates_only_changed_symbol fingerprint=a65113dda9afce87564899c0db24eb8071924c986e5b7ab1d8d70355c2cd8e75 body_fp=2d890a9391357872ca8f2bf60617a42c3e501a45997851f8786eea3c4e3f6ecb source_ref=471fc4733e80d0ab351edd7a2e2e799ae8379b1a -->
## `test_run_incremental_regenerates_only_changed_symbol(project: Path)`

End-to-end verify that `run_incremental` regenerates exactly one symbol after a single-symbol source edit, leaving all other sections byte-identical.

- `project`: temp copy of `tiny_repo` fixture, bootstrapped with two synced files before the edit.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_underscored_symbols_are_documented_and_can_go_stale fingerprint=83103e9fad1ddc9c6dd458d47055a45da52160bc322cc88d14089ac18bbf805e body_fp=4105dd52a727c51a6a3c5885353ecd140dbb49a46c047f5b1302319dff7fe89d source_ref=471fc4733e80d0ab351edd7a2e2e799ae8379b1a -->
## `test_underscored_symbols_are_documented_and_can_go_stale(project: Path)`

Verify that underscore-prefixed symbols receive triefact sections and are flagged stale after source edits.
<!-- trie:end -->