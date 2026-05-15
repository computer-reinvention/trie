---
trie_version: 0.1.0
source: tests/test_symbol_level_sync.py
file_fingerprint: 314947ec0ba7fe9251e77a47882cf832d597ea954048a88d19549d75a33f7847
last_synced_at: '2026-05-15T13:03:06Z'
description: 'Symbol-level sync: regenerate only the symbols actually asked for.'
defines:
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
<!-- trie:section symbol=tests/test_symbol_level_sync:FakeClient fingerprint=0d80adc413a3af8296ca6503769d906403e78bf44faefe56114fdf4ddcf3012f body_fp=d92cf6191644c0c52b93accb33f0e65c778f887b276061ef4e0b340b53542fb7 source_ref=fa134483fd00a273f698b4911ec0dd6f111c2d3f -->
## `FakeClient(model_id: str = "fake/test", calls: int = 0)`

Deterministic LLM stub that returns uniquely-tagged text per call and tracks invocation count.

- `generate`: increments `calls`, returns body tagged with call number and alternating cache token counts.
- `count_tokens`: always returns 100.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_symbol_level_sync:FakeClient.generate fingerprint=313b4ec89a7fb9e750cc159c39486ab80b5c3b9e2d9c42b0ac3c9d649e437b55 body_fp=6731eab37490665ca3f23d9155b272d843242711bdbbf6b6fed83073ef5044fd source_ref=fa134483fd00a273f698b4911ec0dd6f111c2d3f -->
## `generate(self, req: GenerationRequest) -> GenerationResponse`

Return a deterministic `GenerationResponse` with a uniquely-tagged body, incrementing the call counter.

- First call uses cache-creation tokens; subsequent calls use cache-read tokens.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_symbol_level_sync:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=0cc8e4c60852ed2343ba12efc7686b2f040b2c6b012d45e134249772b72c93f1 source_ref=fa134483fd00a273f698b4911ec0dd6f111c2d3f -->
## `count_tokens(self, _req: GenerationRequest) -> int`

Return a fixed token count of 100 for any request.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_symbol_level_sync:_make_project fingerprint=c97c2c26a919c215f8014b8f1407e668c378af04f12f290758ef0642a790e528 body_fp=3aff745ff8fd576ac8459fb34eae963d52bb507bdf2aaa94abbc7c09e6ff9017 source_ref=fa134483fd00a273f698b4911ec0dd6f111c2d3f -->
## `_make_project(tmp_path: Path) -> Path`

Copy the tiny-repo fixture into `tmp_path/demo` and write a `trie.toml` config, returning the project root.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_symbol_level_sync:project fingerprint=31b657a420ab0ee010f44136750460d44af36302a21bf48ce10670807d6c13bc body_fp=8935dfc250bd1fe221ba2cdd938c55aad8b68f321a257a99616dfdb694a22f3b source_ref=fa134483fd00a273f698b4911ec0dd6f111c2d3f -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a temporary copy of the tiny-repo fixture project.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_symbol_level_sync:test_symbols_to_regen_none_regens_every_symbol fingerprint=56f56f0bfb90cebcbbfd32fd8a0eb4b70a367831586d3858e7d65c32bccb8744 body_fp=5b5e4c57daade2acc7230a5d2c8e6e57aad7001b62526e7c33a0cfdf705ac665 source_ref=fa134483fd00a273f698b4911ec0dd6f111c2d3f -->
## `test_symbols_to_regen_none_regens_every_symbol(project: Path)`

Assert that passing `symbols_to_regen=None` to `sync_single_file` regenerates all 6 symbols and skips none.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_symbol_level_sync:test_symbols_to_regen_subset_only_regenerates_listed_symbols fingerprint=2837aef94b9855cf05279bdf45a1db43a8f52c2d91b02d2ca71db673e3ab5b76 body_fp=6cf97d68562ae1cd963a7ff223b961a28082364f0983e140c40ff9da58e7f1b3 source_ref=fa134483fd00a273f698b4911ec0dd6f111c2d3f -->
## `test_symbols_to_regen_subset_only_regenerates_listed_symbols(project: Path)`

Verify that `sync_single_file` with a subset `symbols_to_regen` calls the LLM only for listed symbols and passes all others through byte-identically.

- Performs a cold sync first to establish a complete triefact baseline.
- Resyncs with `symbols_to_regen={"calculator:add"}`; asserts exactly one LLM call, one generated, five skipped.
- Asserts untouched sections have identical `body`, `body_fingerprint`, and `fingerprint`.
- Asserts the targeted symbol's `body` differs from its pre-sync value.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_symbol_level_sync:test_symbols_to_regen_empty_set_runs_no_llm_calls fingerprint=2ec4d2d18316c987764e6843021a79836ea4d2afc7f3c06a749d87fc12e838d3 body_fp=d94f41fc0f81390f29dc9d0a2888373bdf5d043a74e36d22fa6f645d3ea5910c source_ref=fa134483fd00a273f698b4911ec0dd6f111c2d3f -->
## `test_symbols_to_regen_empty_set_runs_no_llm_calls(project: Path)`

Assert that passing `symbols_to_regen=set()` skips all LLM calls while still updating file front matter.

- All six symbols are skipped; section bodies remain byte-identical.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_symbol_level_sync:test_symbols_to_regen_ignores_unknown_qnames fingerprint=c9f642e8d56e9b0c6a8ececbd79ff587fcfa650d6644000d1d45c4fe343c3b54 body_fp=5dbdbf8e4f6c61198104f02417f63c4090996f91dd422371bc8a21ecb5f60e47 source_ref=fa134483fd00a273f698b4911ec0dd6f111c2d3f -->
## `test_symbols_to_regen_ignores_unknown_qnames(project: Path)`

Verify that qnames absent from the current source are silently ignored, producing zero LLM calls and zero regenerated symbols.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_symbol_level_sync:_scanned_store fingerprint=be2171d309873933c9dd828dece87833bd3c117974cc17e64314491077d352a8 body_fp=000271c7954e833870a17bf30310b1a2052c86d589f824658a5bef294447e5b1 source_ref=fa134483fd00a273f698b4911ec0dd6f111c2d3f -->
## `_scanned_store(project: Path) -> Store`

Load config, scan the project into a fresh `Store`, and return it.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_symbol_level_sync:test_worklist_collects_qnames_for_directly_stale_symbols fingerprint=5c9776a2e37db07efd2c9310c41fd585031f6483e22d32783e83202f15963d93 body_fp=143d08e56f4989ce8d671c0688909cb6f628c6c4d842a2fd74a4356488288de6 source_ref=fa134483fd00a273f698b4911ec0dd6f111c2d3f -->
## `test_worklist_collects_qnames_for_directly_stale_symbols(project: Path)`

Assert that editing one symbol causes `compute_incremental_worklist` to populate `regen_qnames_by_file` with exactly that symbol's qname.

- `project`: pytest fixture providing a temporary copy of the tiny_repo fixture.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_symbol_level_sync:test_worklist_omits_files_marked_missing_triefact fingerprint=a4aa6fab8ebd4667cbcb0251c911c91c9b4ff411519f99919cadf8354d1e30a7 body_fp=16125b006e9b1f0f11edb61d9282468cc4d441b46c34cad7c9b41504e2ed9100 source_ref=fa134483fd00a273f698b4911ec0dd6f111c2d3f -->
## `test_worklist_omits_files_marked_missing_triefact(project: Path)`

Assert that files with no triefact are absent from `regen_qnames_by_file`, triggering the full cold-write path instead of symbol-level regen.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_symbol_level_sync:test_run_incremental_regenerates_only_changed_symbol fingerprint=b6883c74e769bbd98c70241fb6c1c35ba7e5d5ff5c58189646015ddba775906e body_fp=aaae7afe044bbdbb2f0d19213be98d00847f7c11a06de301df6e58be8d1e7e75 source_ref=fa134483fd00a273f698b4911ec0dd6f111c2d3f -->
## `test_run_incremental_regenerates_only_changed_symbol(project: Path)`

Verify that editing one symbol triggers exactly one LLM call and leaves all other triefact sections byte-identical.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_symbol_level_sync:test_underscored_symbols_are_documented_and_can_go_stale fingerprint=e05de0594ed6a7c979e91a47e7825be62eec93184873c3fedbc7af956eacc84a body_fp=684829c7313757f1192075967688c0382e5c11e7dcde5ec664678b960e87e71c source_ref=fa134483fd00a273f698b4911ec0dd6f111c2d3f -->
## `test_underscored_symbols_are_documented_and_can_go_stale(project: Path)`

Verify that underscore-prefixed symbols receive triefact sections and are flagged stale when their source body changes.
<!-- trie:end -->