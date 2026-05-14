---
trie_version: 0.1.0
source: tests/test_triefact_metadata.py
file_fingerprint: cbb246bc77d50bccca68c7617723e48dd6f8da7b2b32e7047937c0f361c36eed
last_synced_at: '2026-05-14T17:23:19Z'
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
<!-- trie:section symbol=tests/test_triefact_metadata:FakeClient fingerprint=e41cdf8484085fe52836a78fa046003a64b4ee976928802814aeb5dfbe564b63 body_fp=51d6a95c6e3b54289b86c16cc52b60b488067a018ede0ede537d1a7c0f79b04e -->
## `FakeClient`

Stub AI client that records call counts and returns a fixed `GenerationResponse`.

- `calls`: incremented on each `generate` invocation.
- `generate`: always returns a hardcoded two-token triefact body.
- `count_tokens`: always returns `100`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_triefact_metadata:FakeClient.generate fingerprint=7328b86a4ba976097f1e8eec40c045a8090951dfeca29ef5debd39c4e6fc9a4b body_fp=769257e856ce225d912f33570a8095523e233a8803cac52faca3e98e4f6cee55 -->
## `generate(self, _req: GenerationRequest) -> GenerationResponse`

Return a fixed `GenerationResponse` and increment the call counter.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_triefact_metadata:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=0cc8e4c60852ed2343ba12efc7686b2f040b2c6b012d45e134249772b72c93f1 -->
## `count_tokens(self, _req: GenerationRequest) -> int`

Return a fixed token count of 100 for any request.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_triefact_metadata:project fingerprint=495f251e3dd8b92a847acbd1c63dafa2c313097bc04492791267e04d649c9a0f body_fp=8d57621bb0f41aed605798efa4d081d9b90867bf720013da5e91b4bc108a9c35 -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal two-module project tree with a `trie.toml` config under `tmp_path`.

- **returns** the project root `Path` (`tmp_path`)
<!-- trie:end -->

<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_carries_description_from_module_docstring fingerprint=8382ac45827d28b6e82e57d71ea0153446d0a7c49f452c6ce845989b65cd5fb0 body_fp=ee5974f3edb8ccb37c8f3677a8c5a07a6ef1569602c0fb1be33f352f6d216812 -->
## `test_front_matter_carries_description_from_module_docstring(project: Path)`

Assert that the triefact front matter `description` field equals the module docstring's first line.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_omits_description_when_no_module_docstring fingerprint=1ee8dbebdb7f5ea55e0d640aa93915d6b617d2c688611772b19d73910bb214c9 body_fp=c0a7307341d0a756a7028be36737e3939a029c97ca57fd3f9f0b7b3219dd8abe -->
## `test_front_matter_omits_description_when_no_module_docstring(project: Path)`

Assert that the `description` key is absent from front matter when the source file has no module docstring.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_lists_public_symbols_in_source_order fingerprint=78597adaf60dc4f243778382a5c9c01d935960ed0d3507573ba5a9fe4af8af8b body_fp=53ae60a93ec3e6d7e12d53e17313cb88a6b632228eb465e1b3f1d164d609b575 -->
## `test_front_matter_lists_public_symbols_in_source_order(project: Path)`

Assert that `defines` in the front-matter lists qualified names and kinds in source order.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_carries_iso8601_timestamp fingerprint=c01a330c8053d2fb886277c0c5308e29d38d36e2dbd239f103e82a71ffae16d6 body_fp=64ac0d3dcc3336dcf85952de418e27cc6a789595a3df05ec5c1d2efe8a02ba8c -->
## `test_front_matter_carries_iso8601_timestamp(project: Path)`

Assert that the `last_synced_at` field is a UTC ISO 8601 string ending in `Z`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_includes_ref_counts_when_store_provided fingerprint=7ce040e05d897c2c5a5ff45f54c130549d2fc394e8f9ffa47848b0b3d646c9be body_fp=c9344c984dce146de60798ed0535432574a447e8aab56c7ff6398c29eaa699d0 -->
## `test_front_matter_includes_ref_counts_when_store_provided(project: Path)`

Assert that `incoming_refs` and `outgoing_refs` appear in front-matter when a `Store` is passed to `sync_single_file`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_omits_ref_counts_when_store_omitted fingerprint=b8a11ed0dde2e80e66c5039c273850007dfd84c56d987d2572aa211bab042004 body_fp=35c96c3c8bfe2cc9f976e634c101f502befab929c4042900bca901fa7f0ef58a -->
## `test_front_matter_omits_ref_counts_when_store_omitted(project: Path)`

Assert that `incoming_refs` and `outgoing_refs` are absent from front matter when no `Store` is passed to `sync_single_file`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_triefact_metadata:test_extract_module_docstring_handles_triple_and_single fingerprint=1cfd4844764f5e2082c950006db93fa6d0a41a109ff06111406258d599e7f3bc body_fp=0adfd826c4b2b366d8b38f60e905553e9938a0ef61e50b8d57453056e482e0e6 -->
## `test_extract_module_docstring_handles_triple_and_single(tmp_path: Path)`

Verify `extract_module_docstring` and `strip_string_literal` correctly parse both triple-double-quote and single-quote module docstrings.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_triefact_metadata:test_extract_module_docstring_returns_none_when_first_stmt_is_code fingerprint=68b783549b5457bdd3f1846ee29508cfa2d1c27d734ffb2a0a8346d943c0838a body_fp=18c69f6de11b3d3d765da2314e8592a99a51511bb9c6038b571c718a9c40e2bb -->
## `test_extract_module_docstring_returns_none_when_first_stmt_is_code(tmp_path: Path)`

Assert that `extract_module_docstring` returns `None` when the first statement is an import, not a string literal.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_triefact_metadata:test_strip_string_literal_handles_prefixes fingerprint=8b2d4eddda3179deef4980bea85d25288bf4e925a587700a787f76d9a0a38c2f body_fp=5cd5f7e78d14ca8cb27c4b4fe7f19137f7b622596e8153619f1ffda21862e20d -->
## `test_strip_string_literal_handles_prefixes()`

Verify `strip_string_literal` correctly strips `r"""…"""`, `rb'…'`, and `f"…"` prefixed literals.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_triefact_metadata:test_store_file_ref_counts_excludes_intra_file_edges fingerprint=7bb62d803209039d82fbe1de4e4a165960d12a629bb3466f5ab6d896bcea8933 body_fp=ddb896e9abad41cd84db9e7893442616b76675f97d91e2723f3aa79bbe6b666c -->
## `test_store_file_ref_counts_excludes_intra_file_edges(project: Path)`

Assert that `store.file_ref_counts` counts only cross-file edges, ignoring intra-file calls.
<!-- trie:end -->