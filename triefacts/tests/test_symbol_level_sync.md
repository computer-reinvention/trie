---
trie_version: 0.1.2
source: tests/test_symbol_level_sync.py
file_fingerprint: 133aa06a0a1bad83a79c2c29c35c83c395c034f96cd89569410ac98f2b657e57
last_synced_at: '2026-05-23T23:49:07Z'
description: 'Symbol-level sync: regenerate only the symbols actually asked for.'
defines:
- kind: module
  qualified_name: tests/test_symbol_level_sync:__module__
  lines: 1-363
- kind: constant
  qualified_name: tests/test_symbol_level_sync:FIXTURE_DIR
  lines: 32-32
- kind: class
  qualified_name: tests/test_symbol_level_sync:FakeClient
  lines: 36-53
- kind: method
  qualified_name: tests/test_symbol_level_sync:FakeClient.generate
  lines: 42-50
- kind: method
  qualified_name: tests/test_symbol_level_sync:FakeClient.count_tokens
  lines: 52-53
- kind: function
  qualified_name: tests/test_symbol_level_sync:_make_project
  lines: 56-67
- kind: function
  qualified_name: tests/test_symbol_level_sync:project
  lines: 71-72
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_symbols_to_regen_none_regens_every_symbol
  lines: 80-95
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_symbols_to_regen_subset_only_regenerates_listed_symbols
  lines: 98-141
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_symbols_to_regen_empty_set_runs_no_llm_calls
  lines: 144-180
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_symbols_to_regen_ignores_unknown_qnames
  lines: 183-205
- kind: function
  qualified_name: tests/test_symbol_level_sync:_scanned_store
  lines: 213-217
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_worklist_collects_qnames_for_directly_stale_symbols
  lines: 220-255
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_worklist_omits_files_marked_missing_triefact
  lines: 258-273
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_run_incremental_regenerates_only_changed_symbol
  lines: 281-331
- kind: function
  qualified_name: tests/test_symbol_level_sync:test_underscored_symbols_are_documented_and_can_go_stale
  lines: 334-362
incoming_refs: 0
outgoing_refs: 29
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
<!-- trie:section symbol=tests/test_symbol_level_sync:FakeClient fingerprint=0d80adc413a3af8296ca6503769d906403e78bf44faefe56114fdf4ddcf3012f body_fp=63a55d96b8b3d77101f4b2e6e422fb890a8160a17a55e52d7a6dd81670c2e9be source_ref=0013b0d2bb1e2a586f0828e9253a2620db3d60a9 -->
## `FakeClient`

Deterministic LLM stub that returns a uniquely-tagged response body per call.

- `calls`: incremented on each `generate` invocation; use to assert LLM call counts.
- `generate`: returns call-number-tagged text; first call simulates cache creation, subsequent calls simulate cache reads.
- `count_tokens`: always returns 100.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:FakeClient.generate fingerprint=313b4ec89a7fb9e750cc159c39486ab80b5c3b9e2d9c42b0ac3c9d649e437b55 body_fp=fd5dedc561fbdf17a8f0e58e55cbb7ffaf963303e6b4d4a44c9538f69d0a79d1 source_ref=0013b0d2bb1e2a586f0828e9253a2620db3d60a9 -->
## `FakeClient.generate(self, req: GenerationRequest) -> GenerationResponse`

Increment `FakeClient.calls` and return a deterministic `GenerationResponse` with a uniquely-tagged body.

- `cache_creation_input_tokens`: 100 on first call, 0 thereafter.
- `cache_read_input_tokens`: 0 on first call, 100 thereafter.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=9da7fbd1eb150c6210f098f979f3a48c380092647d3561a0dbdc92d242f75ad9 source_ref=0013b0d2bb1e2a586f0828e9253a2620db3d60a9 -->
## `FakeClient.count_tokens(self, _req: GenerationRequest) -> int`

Always return 100 for any `FakeClient` token-count request.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:_make_project fingerprint=c97c2c26a919c215f8014b8f1407e668c378af04f12f290758ef0642a790e528 body_fp=36614e935e4107b4c01b60b74d4733a27228231c4b090a91bb74b3716cad5639 source_ref=0013b0d2bb1e2a586f0828e9253a2620db3d60a9 -->
## `_make_project(tmp_path: Path) -> Path`

Copy the `tiny_repo` fixture into `tmp_path/demo` and write a `trie.toml` config, returning the project root.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:project fingerprint=31b657a420ab0ee010f44136750460d44af36302a21bf48ce10670807d6c13bc body_fp=374bcef3b1a3bd7420e66ea76ea713073fc98e9a7e4e71732752e5d6a7d3f0d3 source_ref=0013b0d2bb1e2a586f0828e9253a2620db3d60a9 -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a temporary demo project copied from the fixture directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_symbols_to_regen_none_regens_every_symbol fingerprint=56f56f0bfb90cebcbbfd32fd8a0eb4b70a367831586d3858e7d65c32bccb8744 body_fp=ac5215a40e79f73f59cbeb3e88062ffc6767c0fb2f48bc27a03029e37211ecd5 source_ref=0013b0d2bb1e2a586f0828e9253a2620db3d60a9 -->
## `test_symbols_to_regen_none_regens_every_symbol(project: Path)`

Assert that `sync_single_file` with `symbols_to_regen=None` regenerates all 6 symbols and skips none.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_symbols_to_regen_subset_only_regenerates_listed_symbols fingerprint=2837aef94b9855cf05279bdf45a1db43a8f52c2d91b02d2ca71db673e3ab5b76 body_fp=b6b2f56fc4529a5f6f053c33eb3e771ca9a015c5d79be443ff6dd6e88e29b4ea source_ref=0013b0d2bb1e2a586f0828e9253a2620db3d60a9 -->
## `test_symbols_to_regen_subset_only_regenerates_listed_symbols(project: Path)`

Assert that `sync_single_file` with a subset `symbols_to_regen` calls the LLM only for listed symbols and leaves all other sections byte-identical.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_symbols_to_regen_empty_set_runs_no_llm_calls fingerprint=2ec4d2d18316c987764e6843021a79836ea4d2afc7f3c06a749d87fc12e838d3 body_fp=9052924d389beb69dfbbd5cec384a031ef36fe518fb4d96251dd9df2346762cc source_ref=0013b0d2bb1e2a586f0828e9253a2620db3d60a9 -->
## `test_symbols_to_regen_empty_set_runs_no_llm_calls(project: Path)`

Assert that `sync_single_file` with `symbols_to_regen=set()` makes zero LLM calls, skips all 6 symbols, and preserves every section body byte-for-byte.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_symbols_to_regen_ignores_unknown_qnames fingerprint=c9f642e8d56e9b0c6a8ececbd79ff587fcfa650d6644000d1d45c4fe343c3b54 body_fp=30f48fdc722019b99762772e3bea51ac290a2467d61b37f17d265c609738087e source_ref=0013b0d2bb1e2a586f0828e9253a2620db3d60a9 -->
## `test_symbols_to_regen_ignores_unknown_qnames(project: Path)`

Verify that qnames in `symbols_to_regen` that don't exist in the current source are silently ignored, triggering zero LLM calls.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:_scanned_store fingerprint=be2171d309873933c9dd828dece87833bd3c117974cc17e64314491077d352a8 body_fp=3304e352da39298e9fd1e9b5b3d9c7ec217e79779c79c2cc9168d1fb0acfe2fd source_ref=0013b0d2bb1e2a586f0828e9253a2620db3d60a9 -->
## `_scanned_store(project: Path) -> Store`

Create and return a `Store` populated by scanning the given project directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_worklist_collects_qnames_for_directly_stale_symbols fingerprint=5c9776a2e37db07efd2c9310c41fd585031f6483e22d32783e83202f15963d93 body_fp=af452f4c3ad5341449d2844b3b47450f24bc3e07d30cc21fe2462351f3185694 source_ref=0013b0d2bb1e2a586f0828e9253a2620db3d60a9 -->
## `test_worklist_collects_qnames_for_directly_stale_symbols(project: Path)`

Assert that editing a single symbol's body causes `compute_incremental_worklist` to populate `regen_qnames_by_file` with exactly that qname.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_worklist_omits_files_marked_missing_triefact fingerprint=a4aa6fab8ebd4667cbcb0251c911c91c9b4ff411519f99919cadf8354d1e30a7 body_fp=8ae363b46362adbdf180617472e7fe047c2329bc9989a53f70515316e01a369c source_ref=0013b0d2bb1e2a586f0828e9253a2620db3d60a9 -->
## `test_worklist_omits_files_marked_missing_triefact(project: Path)`

Assert that files with no existing triefact appear in `directly_stale` but not in `regen_qnames_by_file`, triggering full cold-write instead of symbol-level regen.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_run_incremental_regenerates_only_changed_symbol fingerprint=b6883c74e769bbd98c70241fb6c1c35ba7e5d5ff5c58189646015ddba775906e body_fp=2d890a9391357872ca8f2bf60617a42c3e501a45997851f8786eea3c4e3f6ecb source_ref=0013b0d2bb1e2a586f0828e9253a2620db3d60a9 -->
## `test_run_incremental_regenerates_only_changed_symbol(project: Path)`

End-to-end verify that `run_incremental` regenerates exactly one symbol after a single-symbol source edit, leaving all other sections byte-identical.

- `project`: temp copy of `tiny_repo` fixture, bootstrapped with two synced files before the edit.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_symbol_level_sync:test_underscored_symbols_are_documented_and_can_go_stale fingerprint=e05de0594ed6a7c979e91a47e7825be62eec93184873c3fedbc7af956eacc84a body_fp=4105dd52a727c51a6a3c5885353ecd140dbb49a46c047f5b1302319dff7fe89d source_ref=0013b0d2bb1e2a586f0828e9253a2620db3d60a9 -->
## `test_underscored_symbols_are_documented_and_can_go_stale(project: Path)`

Verify that underscore-prefixed symbols receive triefact sections and are flagged stale after source edits.
<!-- trie:end -->