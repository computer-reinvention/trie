---
trie_version: 0.1.0
source: tests/test_triefact_metadata.py
file_fingerprint: cbb246bc77d50bccca68c7617723e48dd6f8da7b2b32e7047937c0f361c36eed
last_synced_at: '2026-05-12T18:25:35Z'
description: Front-matter enrichment in `sync_single_file`.
defines:
- kind: class
  qualified_name: tests/test_triefact_metadata:FakeClient
  lines: 25-40
- kind: method
  qualified_name: tests/test_triefact_metadata:FakeClient.generate
  lines: 29-37
- kind: method
  qualified_name: tests/test_triefact_metadata:FakeClient.count_tokens
  lines: 39-40
- kind: function
  qualified_name: tests/test_triefact_metadata:project
  lines: 44-65
- kind: function
  qualified_name: tests/test_triefact_metadata:test_front_matter_carries_description_from_module_docstring
  lines: 98-101
- kind: function
  qualified_name: tests/test_triefact_metadata:test_front_matter_omits_description_when_no_module_docstring
  lines: 104-108
- kind: function
  qualified_name: tests/test_triefact_metadata:test_front_matter_lists_public_symbols_in_source_order
  lines: 111-117
- kind: function
  qualified_name: tests/test_triefact_metadata:test_front_matter_carries_iso8601_timestamp
  lines: 120-129
- kind: function
  qualified_name: tests/test_triefact_metadata:test_front_matter_includes_ref_counts_when_store_provided
  lines: 132-137
- kind: function
  qualified_name: tests/test_triefact_metadata:test_front_matter_omits_ref_counts_when_store_omitted
  lines: 140-144
- kind: function
  qualified_name: tests/test_triefact_metadata:test_extract_module_docstring_handles_triple_and_single
  lines: 147-155
- kind: function
  qualified_name: tests/test_triefact_metadata:test_extract_module_docstring_returns_none_when_first_stmt_is_code
  lines: 158-161
- kind: function
  qualified_name: tests/test_triefact_metadata:test_strip_string_literal_handles_prefixes
  lines: 164-167
- kind: function
  qualified_name: tests/test_triefact_metadata:test_store_file_ref_counts_excludes_intra_file_edges
  lines: 170-182
incoming_refs: 0
outgoing_refs: 14
---
<!-- trie:section symbol=tests/test_triefact_metadata:FakeClient fingerprint=e41cdf8484085fe52836a78fa046003a64b4ee976928802814aeb5dfbe564b63 body_fp=1b496272bef82c17364b580aa5fdf5f81889b8bb63bd6a67701df1a5be4bad64 -->
## `FakeClient`

Stub AI client that records call counts and returns a fixed `GenerationResponse`.

- `calls`: incremented on each `generate` invocation.
- `generate`: always returns a minimal two-token triefact body.
- `count_tokens`: always returns 100.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_triefact_metadata:FakeClient.generate fingerprint=7328b86a4ba976097f1e8eec40c045a8090951dfeca29ef5debd39c4e6fc9a4b body_fp=769257e856ce225d912f33570a8095523e233a8803cac52faca3e98e4f6cee55 -->
## `generate(self, _req: GenerationRequest) -> GenerationResponse`

Return a fixed `GenerationResponse` and increment the call counter.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_triefact_metadata:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=0cc8e4c60852ed2343ba12efc7686b2f040b2c6b012d45e134249772b72c93f1 -->
## `count_tokens(self, _req: GenerationRequest) -> int`

Return a fixed token count of 100 for any request.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_triefact_metadata:project fingerprint=495f251e3dd8b92a847acbd1c63dafa2c313097bc04492791267e04d649c9a0f body_fp=10331576144a760b33fee18fcf1b344615c31aa3b54bb8a783dbeaf0624ea2bb -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal two-module project tree with `trie.toml` config under `tmp_path`.

- **returns** `tmp_path`: root of the temporary project with `src/alpha.py`, `src/beta.py`, and config.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_carries_description_from_module_docstring fingerprint=8382ac45827d28b6e82e57d71ea0153446d0a7c49f452c6ce845989b65cd5fb0 body_fp=d2c5853b95a7f09e2352a3192b55fe2067290dc7411b89d0a7ea3d589508bfbd -->
## `test_front_matter_carries_description_from_module_docstring(project: Path)`

Assert that the triefact front matter `description` field equals the module's first docstring line.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_omits_description_when_no_module_docstring fingerprint=1ee8dbebdb7f5ea55e0d640aa93915d6b617d2c688611772b19d73910bb214c9 body_fp=d82de86d8b02de0fe6ef2c8fb26d432929e96d86ed34082fceb5e23718a056b6 -->
## `test_front_matter_omits_description_when_no_module_docstring(project: Path)`

Assert that `description` is absent from the front matter when the source file has no module docstring.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_lists_public_symbols_in_source_order fingerprint=78597adaf60dc4f243778382a5c9c01d935960ed0d3507573ba5a9fe4af8af8b body_fp=04aaf6620b16de97cd476a28e71486b1b8d66399c43db2a6a62315cb3c67b322 -->
## `test_front_matter_lists_public_symbols_in_source_order(project: Path)`

Assert that the `defines` front-matter list contains qualified names and kinds in source-declaration order.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_carries_iso8601_timestamp fingerprint=c01a330c8053d2fb886277c0c5308e29d38d36e2dbd239f103e82a71ffae16d6 body_fp=ee05d1bbbaa36775daeb9b98668b2398ebe0473eb5f7a7ddc6d6d130f8756f65 -->
## `test_front_matter_carries_iso8601_timestamp(project: Path)`

Assert that the `last_synced_at` front-matter field is a UTC ISO 8601 string ending in `Z`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_includes_ref_counts_when_store_provided fingerprint=7ce040e05d897c2c5a5ff45f54c130549d2fc394e8f9ffa47848b0b3d646c9be body_fp=65574caa4005706dd2c5b5bdeeba4a93468bcd2f82567119e3eed8bc9a34beee -->
## `test_front_matter_includes_ref_counts_when_store_provided(project: Path)`

Assert that `incoming_refs` and `outgoing_refs` are present and correct when a Store is supplied to `sync_single_file`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_omits_ref_counts_when_store_omitted fingerprint=b8a11ed0dde2e80e66c5039c273850007dfd84c56d987d2572aa211bab042004 body_fp=35c96c3c8bfe2cc9f976e634c101f502befab929c4042900bca901fa7f0ef58a -->
## `test_front_matter_omits_ref_counts_when_store_omitted(project: Path)`

Assert that `incoming_refs` and `outgoing_refs` are absent from front matter when no `Store` is passed to `sync_single_file`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_triefact_metadata:test_extract_module_docstring_handles_triple_and_single fingerprint=1cfd4844764f5e2082c950006db93fa6d0a41a109ff06111406258d599e7f3bc body_fp=1b5d033288e7f2d3fff65f45086eb137182d405fe9c9a1e0705fa6d0a654106a -->
## `test_extract_module_docstring_handles_triple_and_single(tmp_path: Path)`

Verify `extract_module_docstring` and `strip_string_literal` correctly handle triple-double-quote and single-quote string literals.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_triefact_metadata:test_extract_module_docstring_returns_none_when_first_stmt_is_code fingerprint=68b783549b5457bdd3f1846ee29508cfa2d1c27d734ffb2a0a8346d943c0838a body_fp=82e789a5a857a2496da5889fd0794d59b4815e5ee39c985aefe312ebae984f0f -->
## `test_extract_module_docstring_returns_none_when_first_stmt_is_code(tmp_path: Path)`

Assert `extract_module_docstring` returns `None` when the first statement is an import, not a string literal.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_triefact_metadata:test_strip_string_literal_handles_prefixes fingerprint=8b2d4eddda3179deef4980bea85d25288bf4e925a587700a787f76d9a0a38c2f body_fp=3ddce7e76774c2af3b194925207eab0f2d6b05c30672b982e0fdbd7ce6ffe845 -->
## `test_strip_string_literal_handles_prefixes()`

Verify `strip_string_literal` correctly strips `r`, `rb`, and `f` prefix variants from string literals.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_triefact_metadata:test_store_file_ref_counts_excludes_intra_file_edges fingerprint=7bb62d803209039d82fbe1de4e4a165960d12a629bb3466f5ab6d896bcea8933 body_fp=f6d0ac36e87d9ae1a1e820c1e57e2cf380fe2b6b5c5779cc27711d98954a49ea -->
## `test_store_file_ref_counts_excludes_intra_file_edges(project: Path)`

Assert that `store.file_ref_counts` counts only cross-file edges, ignoring intra-file calls.

- `project`: pytest fixture providing a temporary project with `alpha.py` importing `beta.py`.
<!-- trie:end -->