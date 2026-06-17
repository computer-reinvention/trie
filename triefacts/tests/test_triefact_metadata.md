---
trie_version: 0.1.9
source: tests/test_triefact_metadata.py
file_fingerprint: c9ca8a05dc8bfff00b6d53711b19041182ab22506e795915e8ed0e2a2fb05b19
last_synced_at: '2026-06-17T16:43:18Z'
description: Front-matter enrichment in `sync_single_file`.
defines:
- kind: module
  qualified_name: tests/test_triefact_metadata:__module__
  lines: 1-163
- kind: function
  qualified_name: tests/test_triefact_metadata:project
  lines: 24-45
- kind: function
  qualified_name: tests/test_triefact_metadata:_front_matter
  lines: 48-53
- kind: function
  qualified_name: tests/test_triefact_metadata:_sync
  lines: 56-75
- kind: function
  qualified_name: tests/test_triefact_metadata:test_front_matter_carries_description_from_module_docstring
  lines: 78-81
- kind: function
  qualified_name: tests/test_triefact_metadata:test_front_matter_omits_description_when_no_module_docstring
  lines: 84-88
- kind: function
  qualified_name: tests/test_triefact_metadata:test_front_matter_lists_public_symbols_in_source_order
  lines: 91-97
- kind: function
  qualified_name: tests/test_triefact_metadata:test_front_matter_carries_iso8601_timestamp
  lines: 100-109
- kind: function
  qualified_name: tests/test_triefact_metadata:test_front_matter_includes_ref_counts_when_store_provided
  lines: 112-117
- kind: function
  qualified_name: tests/test_triefact_metadata:test_front_matter_omits_ref_counts_when_store_omitted
  lines: 120-124
- kind: function
  qualified_name: tests/test_triefact_metadata:test_extract_module_docstring_handles_triple_and_single
  lines: 127-135
- kind: function
  qualified_name: tests/test_triefact_metadata:test_extract_module_docstring_returns_none_when_first_stmt_is_code
  lines: 138-141
- kind: function
  qualified_name: tests/test_triefact_metadata:test_strip_string_literal_handles_prefixes
  lines: 144-147
- kind: function
  qualified_name: tests/test_triefact_metadata:test_store_file_ref_counts_excludes_intra_file_edges
  lines: 150-162
incoming_refs: 0
outgoing_refs: 12
---
<!-- trie:section symbol=tests/test_triefact_metadata:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=35c3bdc591d6f1f3f652a1de07411fd3794110dea69b172568cf6610f2146e13 source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 role=test-infrastructure -->
Tests front-matter enrichment in `sync_single_file` covering metadata blocks written alongside triefacts.

- Verifies timestamps, file descriptions from module docstrings, public symbol rosters, and cross-file reference counts
- Tests both with and without Store for reference counting functionality
- Includes helper functions for parsing YAML front matter and string literal extraction
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:project fingerprint=495f251e3dd8b92a847acbd1c63dafa2c313097bc04492791267e04d649c9a0f body_fp=952dd92bac3f955f75f9f58b7414f37dbc72cb1691fadb78ecbd308c3b06485b source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 role=test-infrastructure -->
Pytest fixture creating test project with trie.toml config and sample Python modules for metadata testing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:_front_matter fingerprint=668ca6fd53da0259864ac2c0b688a4812d05787a2d27b80e431d7ae671be580b body_fp=618c749e671f44d1cd3be461099cd7c0d0a8df183e37d95469ade4c39d00b8a6 source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 role=test-infrastructure -->
Parses YAML front matter from a file and returns it as a dictionary for test assertions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:_sync fingerprint=15a91710c2ea87b25b9abba5b9a815fd6245540e6ebd1242c6ef3c40ec522383 body_fp=fad1d29b0d54db194a2063f70d0b47f5ec0de014777c6d5be7961bb600c88171 source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 role=test-infrastructure -->
Syncs alpha.py in test project and returns path to generated triefact, optionally using Store for cross-file analysis.

- `with_store`: when True, scans project and passes Store to sync_single_file for reference counting
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_carries_description_from_module_docstring fingerprint=8382ac45827d28b6e82e57d71ea0153446d0a7c49f452c6ce845989b65cd5fb0 body_fp=cd70a529ca0bb398646305e9c23394f825df539e5ec8dee706c21d8da8788cbd source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 role=test-infrastructure -->
Verifies that sync_single_file includes the first line of a module docstring as the description field in triefact front matter.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_omits_description_when_no_module_docstring fingerprint=1ee8dbebdb7f5ea55e0d640aa93915d6b617d2c688611772b19d73910bb214c9 body_fp=a71aec751da32383adcd08929f4f58a5c5dc656184e65b95d5ead68180d96e2f source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 role=test-infrastructure -->
Verifies that triefact front matter omits the description field when the module has no docstring.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_lists_public_symbols_in_source_order fingerprint=78597adaf60dc4f243778382a5c9c01d935960ed0d3507573ba5a9fe4af8af8b body_fp=0b1b660ef20e75239f612cd5061002c422001321f13c73302056835e4cf1e3ae source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 role=documentation-sync -->
Verifies triefact front matter contains public symbols in source declaration order with correct qualified names and kinds.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_carries_iso8601_timestamp fingerprint=c01a330c8053d2fb886277c0c5308e29d38d36e2dbd239f103e82a71ffae16d6 body_fp=b240c412588e48c2fe9018656c21c0bf8a4cfce68566d9eaeb5c17cccb60663e source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 role=test-infrastructure -->
Verifies that sync_single_file generates triefacts with valid ISO 8601 timestamps in the last_synced_at field.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_includes_ref_counts_when_store_provided fingerprint=7ce040e05d897c2c5a5ff45f54c130549d2fc394e8f9ffa47848b0b3d646c9be body_fp=6dc94134f686e2e8591933d28ff2a5333b6c086d7d937e9bb4037d87e27ef557 source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 role=test-infrastructure -->
Verifies that triefact front matter includes incoming and outgoing reference counts when a Store is provided.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_omits_ref_counts_when_store_omitted fingerprint=b8a11ed0dde2e80e66c5039c273850007dfd84c56d987d2572aa211bab042004 body_fp=cd1a31b8d26e61018b77384dc4f03c2926f0ae0dfda7af56b0aa63f545ab0646 source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 role=documentation-sync -->
Verifies that front matter excludes `incoming_refs` and `outgoing_refs` fields when no Store is provided to `sync_single_file`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_extract_module_docstring_handles_triple_and_single fingerprint=1cfd4844764f5e2082c950006db93fa6d0a41a109ff06111406258d599e7f3bc body_fp=a0399b4458cfbd93daf450c677f1d85923349b0b797f549396e123856d5a57b3 source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 role=test -->
Tests that `extract_module_docstring` correctly parses both triple-quoted and single-quoted module docstrings.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_extract_module_docstring_returns_none_when_first_stmt_is_code fingerprint=68b783549b5457bdd3f1846ee29508cfa2d1c27d734ffb2a0a8346d943c0838a body_fp=da5558860543c216cc2859a52f9433c6b9a3e8397af16dc4cdfc74935711683a source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 role=test -->
Verifies that `extract_module_docstring` returns None when the first statement is code rather than a docstring.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_strip_string_literal_handles_prefixes fingerprint=8b2d4eddda3179deef4980bea85d25288bf4e925a587700a787f76d9a0a38c2f body_fp=d057ab1d96ba832597508113ff05a2ca89b594f3b4dcf1a0c4f477cdd18dfda3 source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 role=test -->
Verifies `strip_string_literal` correctly removes prefixes and quotes from raw, bytes, and f-string literals.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_store_file_ref_counts_excludes_intra_file_edges fingerprint=7bb62d803209039d82fbe1de4e4a165960d12a629bb3466f5ab6d896bcea8933 body_fp=d154ec63946b7b7f849d55ae52289e700f24ed01dbd9aa1ab29f5d4cb442dabe source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 role=test-infrastructure -->
Verifies Store.file_ref_counts returns only cross-file references, excluding intra-file symbol calls.
<!-- trie:end -->