---
trie_version: 0.1.0
source: tests/test_parse_python.py
file_fingerprint: 2c71d961810a8958fdb4cb5ae028dd577ed513a31e5fd9b2f3d7fdd551c473ce
last_synced_at: '2026-05-14T17:20:21Z'
defines:
- kind: function
  qualified_name: tests/test_parse_python:sample_file
  lines: 61-64
- kind: function
  qualified_name: tests/test_parse_python:test_extracts_top_level_functions
  lines: 71-76
- kind: function
  qualified_name: tests/test_parse_python:test_private_marked_correctly
  lines: 79-81
- kind: function
  qualified_name: tests/test_parse_python:test_decorated_function_is_extracted
  lines: 84-86
- kind: function
  qualified_name: tests/test_parse_python:test_class_and_methods
  lines: 89-95
- kind: function
  qualified_name: tests/test_parse_python:test_decorated_class_and_methods
  lines: 98-101
- kind: function
  qualified_name: tests/test_parse_python:test_methods_of_private_class_inherit_privacy
  lines: 104-118
- kind: function
  qualified_name: tests/test_parse_python:test_module_docstring_is_not_a_symbol
  lines: 121-127
- kind: function
  qualified_name: tests/test_parse_python:test_signature_includes_annotations_and_return_type
  lines: 130-136
- kind: function
  qualified_name: tests/test_parse_python:test_body_normalized_hash_is_stable_across_whitespace
  lines: 139-146
- kind: function
  qualified_name: tests/test_parse_python:test_body_normalized_hash_ignores_comments
  lines: 149-156
- kind: function
  qualified_name: tests/test_parse_python:test_body_normalized_hash_changes_on_real_change
  lines: 159-166
- kind: function
  qualified_name: tests/test_parse_python:test_signature_hash_changes_on_signature_change
  lines: 169-176
- kind: function
  qualified_name: tests/test_parse_python:test_qualified_name_uses_source_root
  lines: 179-186
- kind: function
  qualified_name: tests/test_parse_python:test_line_numbers_are_one_indexed
  lines: 189-194
- kind: function
  qualified_name: tests/test_parse_python:test_typing_overloads_dedupe_to_implementation
  lines: 197-219
- kind: function
  qualified_name: tests/test_parse_python:test_property_setter_pair_dedupes
  lines: 222-237
incoming_refs: 0
outgoing_refs: 16
---
<!-- trie:section symbol=tests/test_parse_python:sample_file fingerprint=b7680b900a9acc188dfba8463fe039b88faa6b62e35109621d52f1e117bae469 body_fp=1a3a12b6ceae4916fdd22099ed0d7c812b82ae0fe8bfbd5985f80b5985f8013b -->
## `sample_file(tmp_path: Path) -> Path`

Write `SAMPLE` source text to a temp file and return its path.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_extracts_top_level_functions fingerprint=2985cdbe318b6e5e9115926392340dadffa4a0be631eb0fdbc5f85bcbf864298 body_fp=595ee15d4442b32bc7d737a46eaa0af1fcc69af58ae9a5166a28a55482e3fcc0 -->
## `test_extracts_top_level_functions(sample_file: Path)`

Assert that `extract_symbols` finds `public_fn`, marks it as a public function, and captures its docstring.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_private_marked_correctly fingerprint=28601d753007fcef28c01a9129bc9b368715630da23d964e9e62072196c9d979 body_fp=e9f844682b5e93d4eceebc2e0bbe1a4327c2ed05824b67142b3838d1c11b7bd1 -->
## `test_private_marked_correctly(sample_file: Path)`

Assert that `_private_fn` has `is_public == False` after symbol extraction.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_decorated_function_is_extracted fingerprint=d2d7ce46ca962dc7c71ac1b6c70d42bf492ef2f9d2dc8b42481dceed2df1046b body_fp=bc1028363bbcd00deefa229bf9d1956d5615e8f8c370709ffdcb1f7c321c2e48 -->
## `test_decorated_function_is_extracted(sample_file: Path)`

Assert that a `@staticmethod`-decorated top-level function appears in the extracted symbols.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_class_and_methods fingerprint=511da3a4934e700fc6fc494d44925a03c492be4e0832580d9500872a2a9aba9e body_fp=7c6f594740a21bbf44b907d154c8d5ffc9f9fb1d1fdea88844a41f48c8523864 -->
## `test_class_and_methods(sample_file: Path)`

Assert that `Greeter` is extracted as a class with correctly typed and privacy-tagged methods.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_decorated_class_and_methods fingerprint=b3273d90f06a67f481b7a5017a2b75c82ee9fe1bb786eb654b7e6608c6d7be1e body_fp=f7be1bdf2226622f99be61f4715111eebb5f6c2194eba308da98b127cc6e630e -->
## `test_decorated_class_and_methods(sample_file: Path)`

Assert that a dataclass-decorated class and its methods are extracted with correct kinds.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_methods_of_private_class_inherit_privacy fingerprint=efb1e4c674bde3acc66af7113cbf8b87ddf3787d7e87ad8809a2fe54952c9a58 body_fp=eae62596fdb9b21f58b1cd93c3bb89252731b82597abe269604bbc5ce5c2f496 -->
## `test_methods_of_private_class_inherit_privacy(tmp_path: Path)`

Assert that methods of a private class are marked non-public regardless of their own name.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_module_docstring_is_not_a_symbol fingerprint=9acbbcaa19aac76bc0f06d2452f2582235b9a8775e89694c414cfee4d898d939 body_fp=7e5aff603051e5a3b3f6fe9c18c4f4c6e99a2a47b2caf8424943c9e78e1cdfee -->
## `test_module_docstring_is_not_a_symbol(sample_file: Path)`

Assert that module docstrings and top-level constants are not emitted as tracked symbols.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_signature_includes_annotations_and_return_type fingerprint=090a7534671717c9765df4e6a87a99ebaf966a0ca91c602042577835228e3b23 body_fp=6a7e3fa4d32711a7ad3685f319e6b81fe031df74c59b1fd31f9f8ea3e163074d -->
## `test_signature_includes_annotations_and_return_type(sample_file: Path)`

Assert that a symbol's `signature` contains the function name, return type annotation, and no trailing colon.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_body_normalized_hash_is_stable_across_whitespace fingerprint=722aceba521e563ec81b8fbc59f1cfc325655527cf1213ff75cc89d9c9b84628 body_fp=5d276a0ec550dd3246a305860f98d782d0fa47d711d0891cc22d05d4c63fb926 -->
## `test_body_normalized_hash_is_stable_across_whitespace(tmp_path: Path)`

Assert that `body_normalized_hash` is identical for two functions differing only in indentation and trailing blank lines.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_body_normalized_hash_ignores_comments fingerprint=722aceba521e563ec81b8fbc59f1cfc325655527cf1213ff75cc89d9c9b84628 body_fp=8ebf787e996bdff6d4bf8fc4a89c46a1a809d9882e48b010f01778aa4895010f -->
## `test_body_normalized_hash_ignores_comments(tmp_path: Path)`

Assert that `body_normalized_hash` is identical for two functions differing only by an inline comment.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_body_normalized_hash_changes_on_real_change fingerprint=4446d6e99a53f2e6e7b6d4f1141b8a4a8b57daa6028410d2650442448448b579 body_fp=4b3e9d96659371b0a335cfdf0fd38b4830cdb858aee2282e472bb4bc62e74ce5 -->
## `test_body_normalized_hash_changes_on_real_change(tmp_path: Path)`

Assert that `body_normalized_hash` differs when a function's logic changes.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_signature_hash_changes_on_signature_change fingerprint=8f494b1008653349c4a28d6de4cac3606c19b823587f67ee9d47f1d8dc997c31 body_fp=fcd3541357a66bdda77cf30ae4dae7b1e5ea19d88791d81e87bba8683c7799e7 -->
## `test_signature_hash_changes_on_signature_change(tmp_path: Path)`

Assert that `signature_hash` differs when a function's parameter list changes.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_qualified_name_uses_source_root fingerprint=5ead7033f892dc234c69e3a017e1ebbcbb11d875a209fc806a9fcba87aa132d9 body_fp=bafda4df3c4d9a66555de6622554d819b6f4a2607f980c2a14f6bb49f75e24e4 -->
## `test_qualified_name_uses_source_root(tmp_path: Path)`

Verify that `extract_symbols` produces path-relative qualified names and `file_path` when `source_root` is supplied.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_line_numbers_are_one_indexed fingerprint=14041c3f38ae9dc76fc49a74415f83024112efbcab533580138927632b38a6c5 body_fp=db5150dae17fbb9573d6ae95a11f3fece268d03c72f693ec547fe4257eb33f1e -->
## `test_line_numbers_are_one_indexed(sample_file: Path)`

Assert that extracted symbol line numbers are one-indexed and `end_line` is not before `start_line`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_typing_overloads_dedupe_to_implementation fingerprint=be44d906148f1dd356a1afe6dc9a4013e51f9b9188f9b317ced6edfc09edfee1 body_fp=afdb925c385b9b8a6e37f26e1456b20e100fb5156e13854b8b4e5d24f1287d96 -->
## `test_typing_overloads_dedupe_to_implementation(tmp_path: Path)`

Assert that multiple `@overload` definitions with the same qualified name deduplicate to the single implementation, keeping the last (non-ellipsis) body.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_property_setter_pair_dedupes fingerprint=0122ca757e452aa9b2aa5bbf07419489fad3d5980db168e63267954ab4ac37c0 body_fp=aba82b469150cc6897c0a9a997d0bd07ce17ca94b71b41864d076ff5d60582ad -->
## `test_property_setter_pair_dedupes(tmp_path: Path)`

Assert that a `@property`/`@setter` pair with the same name deduplicates to a single symbol entry.
<!-- trie:end -->