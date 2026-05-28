---
trie_version: 0.1.5
source: tests/test_triefact_metadata.py
file_fingerprint: c9ca8a05dc8bfff00b6d53711b19041182ab22506e795915e8ed0e2a2fb05b19
last_synced_at: '2026-05-28T14:39:43Z'
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
<!-- trie:section symbol=tests/test_triefact_metadata:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=b560688d5393243a5b2a015428d65b11f42491ec8a8a25a2d22cf81882f9353b source_ref=a472f3ac583e637383ff06da45f7bb5ef9707f56 -->
## `tests/test_triefact_metadata`

Test front-matter enrichment written by `sync_single_file` alongside each triefact.

- Covers timestamps, module-docstring description, public-symbol roster, and cross-file ref counts.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:project fingerprint=495f251e3dd8b92a847acbd1c63dafa2c313097bc04492791267e04d649c9a0f body_fp=465574900bd1cf48b15dbf6ec4befc71229a0489907f4d03a967c7a025ac678f source_ref=a472f3ac583e637383ff06da45f7bb5ef9707f56 -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal two-module project tree with a `trie.toml` config and returns the project root.

- **`alpha.py`**: has a module docstring, imports `beta`, defines `alpha()`, `A`, and `A.m`.
- **`beta.py`**: single function `beta()` returning `2`, no docstring.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:_front_matter fingerprint=668ca6fd53da0259864ac2c0b688a4812d05787a2d27b80e431d7ae671be580b body_fp=48ce71396d36591c90bc5d15235402356fb89371cd57f8a21dc85dbda95e7ee2 source_ref=a472f3ac583e637383ff06da45f7bb5ef9707f56 -->
## `_front_matter(path: Path) -> dict`

Parse and return the YAML front-matter block from a triefact Markdown file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:_sync fingerprint=15a91710c2ea87b25b9abba5b9a815fd6245540e6ebd1242c6ef3c40ec522383 body_fp=c9fde6fbee4731037f0ffb8450a6933178097bd5acb15470dd0666b7df493156 source_ref=05954546e31c15368c9e6e45fc073fbf819f6008 -->
## `_sync(project: Path, *, with_store: bool) -> Path`

Run `sync_single_file` on `src/alpha.py` within the test project, optionally with a populated `Store`, and return the output triefact path.

- `with_store`: if `True`, scans the project and passes a `Store` to `sync_single_file`; otherwise omits it.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_carries_description_from_module_docstring fingerprint=8382ac45827d28b6e82e57d71ea0153446d0a7c49f452c6ce845989b65cd5fb0 body_fp=bb63b294e63e23ddae40e9047140e79902b49af93ab1e7e6f8bf372639e09da5 source_ref=a472f3ac583e637383ff06da45f7bb5ef9707f56 -->
## `test_front_matter_carries_description_from_module_docstring(project: Path)`

Assert that the triefact front-matter `description` field equals the module docstring's first line.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_omits_description_when_no_module_docstring fingerprint=1ee8dbebdb7f5ea55e0d640aa93915d6b617d2c688611772b19d73910bb214c9 body_fp=b9df161ebd7420540762dcc2f71810d74aabf99741a3fe71027b9e7500dce4ef source_ref=a472f3ac583e637383ff06da45f7bb5ef9707f56 -->
## `test_front_matter_omits_description_when_no_module_docstring(project: Path)`

Assert that the triefact front matter omits the `description` key when the source file has no module docstring.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_lists_public_symbols_in_source_order fingerprint=78597adaf60dc4f243778382a5c9c01d935960ed0d3507573ba5a9fe4af8af8b body_fp=060aadfbb6cd5aa6573c84c431cde61c2373fe4af92e39f7c87df5fee07c823c source_ref=a472f3ac583e637383ff06da45f7bb5ef9707f56 -->
## `test_front_matter_lists_public_symbols_in_source_order(project: Path)`

Assert that the `defines` front-matter list preserves source order and records correct qualified names and kinds.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_carries_iso8601_timestamp fingerprint=c01a330c8053d2fb886277c0c5308e29d38d36e2dbd239f103e82a71ffae16d6 body_fp=ee05d1bbbaa36775daeb9b98668b2398ebe0473eb5f7a7ddc6d6d130f8756f65 source_ref=a472f3ac583e637383ff06da45f7bb5ef9707f56 -->
## `test_front_matter_carries_iso8601_timestamp(project: Path)`

Assert that the `last_synced_at` front-matter field is a UTC ISO 8601 string ending in `Z`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_includes_ref_counts_when_store_provided fingerprint=7ce040e05d897c2c5a5ff45f54c130549d2fc394e8f9ffa47848b0b3d646c9be body_fp=0e7f41be8abaef41bbc0becc36732d6aa6dfb7acc7f8f1a2c8770034f54c7d97 source_ref=a472f3ac583e637383ff06da45f7bb5ef9707f56 -->
## `test_front_matter_includes_ref_counts_when_store_provided(project: Path)`

Assert that `incoming_refs` and `outgoing_refs` appear in front matter when a `Store` is supplied.

- `incoming_refs`: expected `0`; nothing outside `alpha.py` calls into it
- `outgoing_refs`: expected `1`; `alpha.py` has one cross-file import from `beta.py`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_front_matter_omits_ref_counts_when_store_omitted fingerprint=b8a11ed0dde2e80e66c5039c273850007dfd84c56d987d2572aa211bab042004 body_fp=99994642ea6cd4b5ca1d506793e3a21a4978fe0e77479a49b64ab3fe144a5d2c source_ref=a472f3ac583e637383ff06da45f7bb5ef9707f56 -->
## `test_front_matter_omits_ref_counts_when_store_omitted(project: Path)`

Assert that `incoming_refs` and `outgoing_refs` are absent from front matter when no `Store` is supplied.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_extract_module_docstring_handles_triple_and_single fingerprint=1cfd4844764f5e2082c950006db93fa6d0a41a109ff06111406258d599e7f3bc body_fp=d2b99dc9918c6ee954322a236f61a95ef26bbd3ce4a57518b2188cce0739e603 source_ref=a472f3ac583e637383ff06da45f7bb5ef9707f56 -->
## `test_extract_module_docstring_handles_triple_and_single(tmp_path: Path)`

Verify `extract_module_docstring` and `strip_string_literal` correctly parse triple-double-quote and single-quote module docstrings.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_extract_module_docstring_returns_none_when_first_stmt_is_code fingerprint=68b783549b5457bdd3f1846ee29508cfa2d1c27d734ffb2a0a8346d943c0838a body_fp=82e789a5a857a2496da5889fd0794d59b4815e5ee39c985aefe312ebae984f0f source_ref=a472f3ac583e637383ff06da45f7bb5ef9707f56 -->
## `test_extract_module_docstring_returns_none_when_first_stmt_is_code(tmp_path: Path)`

Assert `extract_module_docstring` returns `None` when the first statement is an import, not a string literal.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_strip_string_literal_handles_prefixes fingerprint=8b2d4eddda3179deef4980bea85d25288bf4e925a587700a787f76d9a0a38c2f body_fp=bed64cc271755650f40a8eb25839777294f25c2cb69843c4142a9d500e25a497 source_ref=a472f3ac583e637383ff06da45f7bb5ef9707f56 -->
## `test_strip_string_literal_handles_prefixes()`

Verify `strip_string_literal` correctly strips `r`, `rb`, and `f` string prefixes and surrounding quotes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_triefact_metadata:test_store_file_ref_counts_excludes_intra_file_edges fingerprint=7bb62d803209039d82fbe1de4e4a165960d12a629bb3466f5ab6d896bcea8933 body_fp=74c889fe3d0787383f4e36017b5d7f9ec039ba7575a2f49790fb51be89fb0921 source_ref=a472f3ac583e637383ff06da45f7bb5ef9707f56 -->
## `test_store_file_ref_counts_excludes_intra_file_edges(project: Path)`

Assert that `Store.file_ref_counts` counts only cross-file edges, ignoring intra-file symbol references.
<!-- trie:end -->