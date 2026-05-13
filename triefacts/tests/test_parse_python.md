---
trie_version: 0.1.0
source: tests/test_parse_python.py
file_fingerprint: 2c71d961810a8958fdb4cb5ae028dd577ed513a31e5fd9b2f3d7fdd551c473ce
last_synced_at: '2026-05-12T18:22:54Z'
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
<!-- trie:section symbol=tests/test_parse_python:sample_file fingerprint=b7680b900a9acc188dfba8463fe039b88faa6b62e35109621d52f1e117bae469 body_fp=b8d50d6d004cd0c1620963dcb733687ed1d4c5266f8a378568e866117a322e25 -->
## `sample_file(tmp_path: Path) -> Path`

Write `SAMPLE` source text to a temporary file and return its path.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_extracts_top_level_functions fingerprint=2985cdbe318b6e5e9115926392340dadffa4a0be631eb0fdbc5f85bcbf864298 body_fp=df3bf5af802e495ace822402606e363e846c22557b4c16cdd531609e068b35f1 -->
## `test_extracts_top_level_functions(sample_file: Path)`

Verify that `extract_symbols` extracts a public top-level function with correct kind, visibility, and docstring.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_private_marked_correctly fingerprint=28601d753007fcef28c01a9129bc9b368715630da23d964e9e62072196c9d979 body_fp=1dc89423637df47beca7061eaf10638d5768349cb79944b7428a493a376dd8fc -->
## `test_private_marked_correctly(sample_file: Path)`

Assert that `_private_fn` has `is_public` set to `False`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_decorated_function_is_extracted fingerprint=d2d7ce46ca962dc7c71ac1b6c70d42bf492ef2f9d2dc8b42481dceed2df1046b body_fp=04abacfdfc8d4d9893e03ac4c78fe5943004742e73f0822f25cad378074d8cfe -->
## `test_decorated_function_is_extracted(sample_file: Path)`

Assert that a `@staticmethod`-decorated top-level function appears in extracted symbols.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_class_and_methods fingerprint=511da3a4934e700fc6fc494d44925a03c492be4e0832580d9500872a2a9aba9e body_fp=63c553b0c1b1701ae76fd0aeb1f402cfabcb271b1371c7b676103ee593caf32b -->
## `test_class_and_methods(sample_file: Path)`

Assert that `Greeter` class and its methods are extracted with correct kinds and privacy flags.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_decorated_class_and_methods fingerprint=b3273d90f06a67f481b7a5017a2b75c82ee9fe1bb786eb654b7e6608c6d7be1e body_fp=904d6ee1a16a335213654758a4c886123f0b290de4eba8a81f0fcb91ec654220 -->
## `test_decorated_class_and_methods(sample_file: Path)`

Assert that a decorator-annotated class and its methods are extracted with correct kinds.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_methods_of_private_class_inherit_privacy fingerprint=efb1e4c674bde3acc66af7113cbf8b87ddf3787d7e87ad8809a2fe54952c9a58 body_fp=b60494c859f046b508d55e07441d4ee87f9b1c7590520bb070b80f3a84d84d88 -->
## `test_methods_of_private_class_inherit_privacy(tmp_path: Path)`

Verify that methods inside a private class are marked non-public regardless of their own name.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_module_docstring_is_not_a_symbol fingerprint=9acbbcaa19aac76bc0f06d2452f2582235b9a8775e89694c414cfee4d898d939 body_fp=b58ae905b64cbbb6fd54c743b616e08627f3c106e06ef70fcd0291d2ebcd8c51 -->
## `test_module_docstring_is_not_a_symbol(sample_file: Path)`

Assert that module docstrings and top-level constants are not extracted as symbols.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_signature_includes_annotations_and_return_type fingerprint=090a7534671717c9765df4e6a87a99ebaf966a0ca91c602042577835228e3b23 body_fp=2d7f05320f1fc85224790562551e79766c5c1895985a84ff580b0a9087a69ff0 -->
## `test_signature_includes_annotations_and_return_type(sample_file: Path)`

Assert that the extracted signature contains the function name, return type annotation, and no trailing colon.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_body_normalized_hash_is_stable_across_whitespace fingerprint=722aceba521e563ec81b8fbc59f1cfc325655527cf1213ff75cc89d9c9b84628 body_fp=ae4392a16adc54855832cee03ba6e34fe4533948c46bddf4846a9ce285a88214 -->
## `test_body_normalized_hash_is_stable_across_whitespace(tmp_path: Path)`

Assert that `body_normalized_hash` is identical for two functions differing only in whitespace.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_body_normalized_hash_ignores_comments fingerprint=722aceba521e563ec81b8fbc59f1cfc325655527cf1213ff75cc89d9c9b84628 body_fp=8ebf787e996bdff6d4bf8fc4a89c46a1a809d9882e48b010f01778aa4895010f -->
## `test_body_normalized_hash_ignores_comments(tmp_path: Path)`

Assert that `body_normalized_hash` is identical for two functions differing only by an inline comment.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_body_normalized_hash_changes_on_real_change fingerprint=4446d6e99a53f2e6e7b6d4f1141b8a4a8b57daa6028410d2650442448448b579 body_fp=d1fa8de62037f89bcab4549e0ab6c47c90c310cb26eec18c1ae5578301ea2d69 -->
## `test_body_normalized_hash_changes_on_real_change(tmp_path: Path)`

Assert that `body_normalized_hash` differs when the function body logic changes.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_signature_hash_changes_on_signature_change fingerprint=8f494b1008653349c4a28d6de4cac3606c19b823587f67ee9d47f1d8dc997c31 body_fp=fcd3541357a66bdda77cf30ae4dae7b1e5ea19d88791d81e87bba8683c7799e7 -->
## `test_signature_hash_changes_on_signature_change(tmp_path: Path)`

Assert that `signature_hash` differs when a function's parameter list changes.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_qualified_name_uses_source_root fingerprint=5ead7033f892dc234c69e3a017e1ebbcbb11d875a209fc806a9fcba87aa132d9 body_fp=9924fe5eded96583bb6c69b9007ae5d6c1cb8e27ad563d6ef81be014cec2ab44 -->
## `test_qualified_name_uses_source_root(tmp_path: Path)`

Verify that `extract_symbols` produces slash-separated qualified names and file paths relative to `source_root`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_line_numbers_are_one_indexed fingerprint=14041c3f38ae9dc76fc49a74415f83024112efbcab533580138927632b38a6c5 body_fp=41f121f2e84937a8fc411c1435a7e4d00f16a89be2eddf861585c04d94e345cf -->
## `test_line_numbers_are_one_indexed(sample_file: Path)`

Assert that extracted symbols have one-indexed, ordered line numbers.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_typing_overloads_dedupe_to_implementation fingerprint=be44d906148f1dd356a1afe6dc9a4013e51f9b9188f9b317ced6edfc09edfee1 body_fp=fc326cf9dd4669db89bca1c29d7f521412297bddc2810d66de3f7e989eda8f3d -->
## `test_typing_overloads_dedupe_to_implementation(tmp_path: Path)`

Assert that multiple `@overload` definitions with the same qualified name deduplicate to the single implementation entry.

- The surviving symbol must be the implementation body, not an ellipsis stub.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_property_setter_pair_dedupes fingerprint=0122ca757e452aa9b2aa5bbf07419489fad3d5980db168e63267954ab4ac37c0 body_fp=8a842b24a06887e262f3f6552aecac0df2a2ff444b372bc27f052c3e4d4969bc -->
## `test_property_setter_pair_dedupes(tmp_path: Path)`

Assert that a `@property`/`@setter` pair with the same name deduplicates to one symbol.
<!-- trie:end -->