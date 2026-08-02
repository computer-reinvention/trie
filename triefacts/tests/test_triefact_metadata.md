---
trie_version: 0.3.0
source: tests/test_triefact_metadata.py
file_fingerprint: 667f022d1c470d70ee4d89db7944b156ce37117d281c1f5e5905a84cb1971aef
last_synced_at: '2026-08-02T21:19:11Z'
description: Front-matter enrichment in `sync_single_file`.
defines:
- kind: module
  qualified_name: tests/test_triefact_metadata:__module__
  lines: 1-304
- kind: function
  qualified_name: tests/test_triefact_metadata:project
  lines: 24-45
  signature: 'def project(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_triefact_metadata:_front_matter
  lines: 48-53
  signature: 'def _front_matter(path: Path) -> dict'
- kind: function
  qualified_name: tests/test_triefact_metadata:_sync
  lines: 56-75
  signature: 'def _sync(project: Path, *, with_store: bool) -> Path'
- kind: function
  qualified_name: tests/test_triefact_metadata:test_front_matter_carries_description_from_module_docstring
  lines: 78-81
  signature: 'def test_front_matter_carries_description_from_module_docstring(project: Path)'
- kind: function
  qualified_name: tests/test_triefact_metadata:test_front_matter_omits_description_when_no_module_docstring
  lines: 84-88
  signature: 'def test_front_matter_omits_description_when_no_module_docstring(project: Path)'
- kind: function
  qualified_name: tests/test_triefact_metadata:test_front_matter_lists_public_symbols_in_source_order
  lines: 91-97
  signature: 'def test_front_matter_lists_public_symbols_in_source_order(project: Path)'
- kind: function
  qualified_name: tests/test_triefact_metadata:test_front_matter_carries_iso8601_timestamp
  lines: 100-109
  signature: 'def test_front_matter_carries_iso8601_timestamp(project: Path)'
- kind: function
  qualified_name: tests/test_triefact_metadata:test_front_matter_includes_ref_counts_when_store_provided
  lines: 112-117
  signature: 'def test_front_matter_includes_ref_counts_when_store_provided(project: Path)'
- kind: function
  qualified_name: tests/test_triefact_metadata:test_front_matter_omits_ref_counts_when_store_omitted
  lines: 120-124
  signature: 'def test_front_matter_omits_ref_counts_when_store_omitted(project: Path)'
- kind: function
  qualified_name: tests/test_triefact_metadata:test_defines_carry_exact_parser_signatures
  lines: 127-142
  signature: 'def test_defines_carry_exact_parser_signatures(project: Path)'
- kind: function
  qualified_name: tests/test_triefact_metadata:test_defines_squeeze_multiline_signatures_to_one_line
  lines: 145-153
  signature: 'def test_defines_squeeze_multiline_signatures_to_one_line(project: Path)'
- kind: function
  qualified_name: tests/test_triefact_metadata:test_defines_omit_signature_for_constants_and_modules
  lines: 156-168
  signature: 'def test_defines_omit_signature_for_constants_and_modules(project: Path)'
- kind: function
  qualified_name: tests/test_triefact_metadata:test_section_bodies_start_with_parser_derived_heading
  lines: 171-190
  signature: 'def test_section_bodies_start_with_parser_derived_heading(project: Path)'
- kind: function
  qualified_name: tests/test_triefact_metadata:test_stale_llm_heading_is_replaced_with_parser_signature
  lines: 193-212
  signature: 'def test_stale_llm_heading_is_replaced_with_parser_signature(project: Path)'
- kind: function
  qualified_name: tests/test_triefact_metadata:test_metadata_refresh_migrates_pre_signature_tree_without_llm
  lines: 215-265
  signature: 'def test_metadata_refresh_migrates_pre_signature_tree_without_llm(project: Path)'
- kind: function
  qualified_name: tests/test_triefact_metadata:test_extract_module_docstring_handles_triple_and_single
  lines: 268-276
  signature: 'def test_extract_module_docstring_handles_triple_and_single(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_triefact_metadata:test_extract_module_docstring_returns_none_when_first_stmt_is_code
  lines: 279-282
  signature: 'def test_extract_module_docstring_returns_none_when_first_stmt_is_code(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_triefact_metadata:test_strip_string_literal_handles_prefixes
  lines: 285-288
  signature: def test_strip_string_literal_handles_prefixes()
- kind: function
  qualified_name: tests/test_triefact_metadata:test_store_file_ref_counts_excludes_intra_file_edges
  lines: 291-303
  signature: 'def test_store_file_ref_counts_excludes_intra_file_edges(project: Path)'
incoming_refs: 0
outgoing_refs: 37
---
<!-- trie:section symbol=tests/test_triefact_metadata:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=35c3bdc591d6f1f3f652a1de07411fd3794110dea69b172568cf6610f2146e13 source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 role=test-infrastructure -->
Tests front-matter enrichment in `sync_single_file` covering metadata blocks written alongside triefacts.

- Verifies timestamps, file descriptions from module docstrings, public symbol rosters, and cross-file reference counts
- Tests both with and without Store for reference counting functionality
- Includes helper functions for parsing YAML front matter and string literal extraction
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:project fingerprint=495f251e3dd8b92a847acbd1c63dafa2c313097bc04492791267e04d649c9a0f body_fp=4c8e01ff048d5c96991da0efdc282d4f8f346d9c2ac1cff457fb462ed9583510 source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 role=test-infrastructure -->
## `def project(tmp_path: Path) -> Path`

Pytest fixture creating test project with trie.toml config and sample Python modules for metadata testing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:_front_matter fingerprint=668ca6fd53da0259864ac2c0b688a4812d05787a2d27b80e431d7ae671be580b body_fp=e3b431860a0fb1cb96415e373ec1190e7791ef51c7b97a95e820abef9c89ae34 source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 role=test-infrastructure -->
## `def _front_matter(path: Path) -> dict`

Parses YAML front matter from a file and returns it as a dictionary for test assertions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:_sync fingerprint=15a91710c2ea87b25b9abba5b9a815fd6245540e6ebd1242c6ef3c40ec522383 body_fp=5285e36781d4c0bede36dfbc91b80f6989f91afd4eaf9090aa3071a0906bd7b2 source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 role=test-infrastructure -->
## `def _sync(project: Path, *, with_store: bool) -> Path`

Syncs alpha.py in test project and returns path to generated triefact, optionally using Store for cross-file analysis.

- `with_store`: when True, scans project and passes Store to sync_single_file for reference counting
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_carries_description_from_module_docstring fingerprint=8382ac45827d28b6e82e57d71ea0153446d0a7c49f452c6ce845989b65cd5fb0 body_fp=8ff4d0a1c8c2316351c343fb5a0d8640cd7c86eb99b45cb401bba3a438b5a333 source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 role=test-infrastructure -->
## `def test_front_matter_carries_description_from_module_docstring(project: Path)`

Verifies that sync_single_file includes the first line of a module docstring as the description field in triefact front matter.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_omits_description_when_no_module_docstring fingerprint=1ee8dbebdb7f5ea55e0d640aa93915d6b617d2c688611772b19d73910bb214c9 body_fp=017c06e92303b7ed28207660aed65bf677d5f9783b762a03c5dfbc3ac42727e4 source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 role=test-infrastructure -->
## `def test_front_matter_omits_description_when_no_module_docstring(project: Path)`

Verifies that triefact front matter omits the description field when the module has no docstring.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_lists_public_symbols_in_source_order fingerprint=78597adaf60dc4f243778382a5c9c01d935960ed0d3507573ba5a9fe4af8af8b body_fp=b7dcba135a2d5bd9d0383f40227a9f747eb0a20223529b2f9d92eaf1081ef516 source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 role=documentation-sync -->
## `def test_front_matter_lists_public_symbols_in_source_order(project: Path)`

Verifies triefact front matter contains public symbols in source declaration order with correct qualified names and kinds.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_carries_iso8601_timestamp fingerprint=c01a330c8053d2fb886277c0c5308e29d38d36e2dbd239f103e82a71ffae16d6 body_fp=80ac7fdb809028dc480ddb5f750f71425f2c1b8186453c6989bcb5094348682d source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 role=test-infrastructure -->
## `def test_front_matter_carries_iso8601_timestamp(project: Path)`

Verifies that sync_single_file generates triefacts with valid ISO 8601 timestamps in the last_synced_at field.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_includes_ref_counts_when_store_provided fingerprint=7ce040e05d897c2c5a5ff45f54c130549d2fc394e8f9ffa47848b0b3d646c9be body_fp=5eac7d13c13776d0a03932d79f35f8d196166b9b39f4e492b78b9205baf8b393 source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 role=test-infrastructure -->
## `def test_front_matter_includes_ref_counts_when_store_provided(project: Path)`

Verifies that triefact front matter includes incoming and outgoing reference counts when a Store is provided.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_omits_ref_counts_when_store_omitted fingerprint=b8a11ed0dde2e80e66c5039c273850007dfd84c56d987d2572aa211bab042004 body_fp=f3c4bf53148004d4fc51f0ae362418d8117c3ad15c18e90d812aac74f9ad28f6 source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 role=documentation-sync -->
## `def test_front_matter_omits_ref_counts_when_store_omitted(project: Path)`

Verifies that front matter excludes `incoming_refs` and `outgoing_refs` fields when no Store is provided to `sync_single_file`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_defines_carry_exact_parser_signatures fingerprint=07c026ff0daac913a3b57deaedd9b0f46907fb68996d4c7ce11ac19b0d2f73ef body_fp=c053f9f01bfd3bdf0f9af8a9d4a1ee85da137ba26c75ff35ceb38115a10f4ab6 source_ref=52358386e3a9a3ceeb90611813e3687b6b419521 role=test -->
## `def test_defines_carry_exact_parser_signatures(project: Path)`

Assert that each `defines` entry in the front matter carries a `signature` field matching the parser's exact one-line source text, including `/` and `*` markers.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_defines_squeeze_multiline_signatures_to_one_line fingerprint=75b8669fad34ce1a85978a837b57354216127354402247e51043415922015c38 body_fp=9d22119fe45bb29e15548a1201358659d6396897bd6712939ca5071a4733ac41 source_ref=52358386e3a9a3ceeb90611813e3687b6b419521 role=test -->
## `def test_defines_squeeze_multiline_signatures_to_one_line(project: Path)`

Asserts that a multi-line source signature is collapsed to a single whitespace-joined line in the `defines` front-matter entry.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_defines_omit_signature_for_constants_and_modules fingerprint=af19d362bc643d632f5817e5f1eb20de78ec9f3eed04626970288c8eb0e0c7c2 body_fp=b0bf8eaf59b2452ad3d046b32998d76cb1c0eab59b9e5c56b4d75170c924e02a source_ref=52358386e3a9a3ceeb90611813e3687b6b419521 role=test -->
## `def test_defines_omit_signature_for_constants_and_modules(project: Path)`

Assert that `defines` entries for `constant` and `module` kinds carry no `signature` key rather than a null or fabricated value.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_section_bodies_start_with_parser_derived_heading fingerprint=7295a92f911ba89be804996393a78f0da6a142cdea12b2d933f9f1aa8518b37e body_fp=321b3e7cf105c90a7f4c7b3f5374901f23dca1c532d8af36ffbe05c015a6f198 source_ref=52358386e3a9a3ceeb90611813e3687b6b419521 role=test -->
## `def test_section_bodies_start_with_parser_derived_heading(project: Path)`

Assert that `sync_single_file` injects the parser-derived `## \`signature\`` heading even when the LLM body contains no heading at all.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_stale_llm_heading_is_replaced_with_parser_signature fingerprint=0cf0e8b7a4e1a3a81bf04aca45cfddfbb4be184e36eb0d1b502da58232d1e68c body_fp=9b972662855676a0be8bb677b88a9093c6079aee553a700d4a4c93edaae53730 source_ref=52358386e3a9a3ceeb90611813e3687b6b419521 role=test -->
## `def test_stale_llm_heading_is_replaced_with_parser_signature(project: Path)`

Assert that a mangled `## ...` heading produced by the LLM is overwritten with the parser-derived signature after `sync_single_file` runs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_metadata_refresh_migrates_pre_signature_tree_without_llm fingerprint=7094201db8830eb504f4010825cff998ecea71d6ac5d7048f80c06824112cc32 body_fp=e43ebc2a00345b8384c220f0f65c31bbe381f7982c53b404dc758c306c3f0698 source_ref=52358386e3a9a3ceeb90611813e3687b6b419521 role=test -->
## `def test_metadata_refresh_migrates_pre_signature_tree_without_llm(project: Path)`

Verify that `refresh_triefact_metadata` migrates a pre-fix triefact — adding `signature` to `defines` entries and normalising stale section-body headings — without invoking an LLM.

- Doctors a synced triefact into its pre-fix state (strips `signature` keys, injects a mangled heading) before calling the function under test.
- Asserts `result.changed is True` on first call and `again.changed is False` on a second call (idempotency).
- Confirms source `fingerprint` is preserved while `body_fingerprint` is recomputed to match the corrected body.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_extract_module_docstring_handles_triple_and_single fingerprint=1cfd4844764f5e2082c950006db93fa6d0a41a109ff06111406258d599e7f3bc body_fp=cb9adebc6a3663925cb93e2fd4394a22f9a41c5a8cd37aa928140c885b5e01da source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 role=test -->
## `def test_extract_module_docstring_handles_triple_and_single(tmp_path: Path)`

Tests that `extract_module_docstring` correctly parses both triple-quoted and single-quoted module docstrings.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_extract_module_docstring_returns_none_when_first_stmt_is_code fingerprint=68b783549b5457bdd3f1846ee29508cfa2d1c27d734ffb2a0a8346d943c0838a body_fp=79543f4abf45c8ba95d1244afb1ae2b884cd8ade6d2d436d7f70c7000cde3dbe source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 role=test -->
## `def test_extract_module_docstring_returns_none_when_first_stmt_is_code(tmp_path: Path)`

Verifies that `extract_module_docstring` returns None when the first statement is code rather than a docstring.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_strip_string_literal_handles_prefixes fingerprint=8b2d4eddda3179deef4980bea85d25288bf4e925a587700a787f76d9a0a38c2f body_fp=eead19a5f54669bcb4d60bd218c1e60aaa5a0e512c76dfe925ea54ebf6dc0a43 source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 role=test -->
## `def test_strip_string_literal_handles_prefixes()`

Verifies `strip_string_literal` correctly removes prefixes and quotes from raw, bytes, and f-string literals.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_store_file_ref_counts_excludes_intra_file_edges fingerprint=7bb62d803209039d82fbe1de4e4a165960d12a629bb3466f5ab6d896bcea8933 body_fp=8e6dbfba78ae47b665ebb9828251d570729a35d7d738a14e216296455b3542b1 source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 role=test-infrastructure -->
## `def test_store_file_ref_counts_excludes_intra_file_edges(project: Path)`

Verifies Store.file_ref_counts returns only cross-file references, excluding intra-file symbol calls.
<!-- trie:end -->