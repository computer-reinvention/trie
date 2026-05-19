---
trie_version: 0.1.1
source: tests/test_parse_python.py
file_fingerprint: 7a7f5dc85073e3c01732755848109f060f12e1bedc84505a49eeda69b299bb72
last_synced_at: '2026-05-19T10:38:47Z'
defines:
- kind: module
  qualified_name: tests/test_parse_python:__module__
  lines: 1-361
- kind: constant
  qualified_name: tests/test_parse_python:SAMPLE
  lines: 9-57
- kind: function
  qualified_name: tests/test_parse_python:sample_file
  lines: 61-64
- kind: function
  qualified_name: tests/test_parse_python:_by_qname
  lines: 67-68
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
  lines: 121-131
- kind: function
  qualified_name: tests/test_parse_python:test_module_level_constants_are_indexed
  lines: 134-145
- kind: function
  qualified_name: tests/test_parse_python:test_signature_includes_annotations_and_return_type
  lines: 148-154
- kind: function
  qualified_name: tests/test_parse_python:test_body_normalized_hash_is_stable_across_whitespace
  lines: 157-164
- kind: function
  qualified_name: tests/test_parse_python:test_body_normalized_hash_ignores_comments
  lines: 167-174
- kind: function
  qualified_name: tests/test_parse_python:test_body_normalized_hash_changes_on_real_change
  lines: 177-184
- kind: function
  qualified_name: tests/test_parse_python:test_signature_hash_changes_on_signature_change
  lines: 187-194
- kind: function
  qualified_name: tests/test_parse_python:test_qualified_name_uses_source_root
  lines: 197-204
- kind: function
  qualified_name: tests/test_parse_python:test_line_numbers_are_one_indexed
  lines: 207-212
- kind: function
  qualified_name: tests/test_parse_python:test_typing_overloads_dedupe_to_implementation
  lines: 215-237
- kind: function
  qualified_name: tests/test_parse_python:test_property_setter_pair_dedupes
  lines: 240-255
- kind: function
  qualified_name: tests/test_parse_python:test_dunder_constants_are_public
  lines: 263-274
- kind: function
  qualified_name: tests/test_parse_python:test_annotated_constants_are_indexed
  lines: 277-285
- kind: function
  qualified_name: tests/test_parse_python:test_tuple_unpacking_assignment_is_not_indexed
  lines: 288-299
- kind: function
  qualified_name: tests/test_parse_python:test_module_symbol_emitted_for_setup_py_style_call
  lines: 302-324
- kind: function
  qualified_name: tests/test_parse_python:test_module_symbol_not_emitted_for_pure_defs_with_imports
  lines: 327-349
- kind: function
  qualified_name: tests/test_parse_python:test_module_symbol_emitted_for_if_main_block
  lines: 352-360
incoming_refs: 0
outgoing_refs: 23
---
<!-- trie:section symbol=tests/test_parse_python:sample_file fingerprint=b7680b900a9acc188dfba8463fe039b88faa6b62e35109621d52f1e117bae469 body_fp=1a3a12b6ceae4916fdd22099ed0d7c812b82ae0fe8bfbd5985f80b5985f8013b source_ref=c1ada9d77b60fb66c2b1e14e94d08485646b4e02 -->
## `sample_file(tmp_path: Path) -> Path`

Write `SAMPLE` source text to a temp file and return its path.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_extracts_top_level_functions fingerprint=2985cdbe318b6e5e9115926392340dadffa4a0be631eb0fdbc5f85bcbf864298 body_fp=595ee15d4442b32bc7d737a46eaa0af1fcc69af58ae9a5166a28a55482e3fcc0 source_ref=c1ada9d77b60fb66c2b1e14e94d08485646b4e02 -->
## `test_extracts_top_level_functions(sample_file: Path)`

Assert that `extract_symbols` finds `public_fn`, marks it as a public function, and captures its docstring.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_private_marked_correctly fingerprint=28601d753007fcef28c01a9129bc9b368715630da23d964e9e62072196c9d979 body_fp=e9f844682b5e93d4eceebc2e0bbe1a4327c2ed05824b67142b3838d1c11b7bd1 source_ref=c1ada9d77b60fb66c2b1e14e94d08485646b4e02 -->
## `test_private_marked_correctly(sample_file: Path)`

Assert that `_private_fn` has `is_public == False` after symbol extraction.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_decorated_function_is_extracted fingerprint=d2d7ce46ca962dc7c71ac1b6c70d42bf492ef2f9d2dc8b42481dceed2df1046b body_fp=bc1028363bbcd00deefa229bf9d1956d5615e8f8c370709ffdcb1f7c321c2e48 source_ref=c1ada9d77b60fb66c2b1e14e94d08485646b4e02 -->
## `test_decorated_function_is_extracted(sample_file: Path)`

Assert that a `@staticmethod`-decorated top-level function appears in the extracted symbols.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_class_and_methods fingerprint=511da3a4934e700fc6fc494d44925a03c492be4e0832580d9500872a2a9aba9e body_fp=7c6f594740a21bbf44b907d154c8d5ffc9f9fb1d1fdea88844a41f48c8523864 source_ref=c1ada9d77b60fb66c2b1e14e94d08485646b4e02 -->
## `test_class_and_methods(sample_file: Path)`

Assert that `Greeter` is extracted as a class with correctly typed and privacy-tagged methods.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_decorated_class_and_methods fingerprint=b3273d90f06a67f481b7a5017a2b75c82ee9fe1bb786eb654b7e6608c6d7be1e body_fp=f7be1bdf2226622f99be61f4715111eebb5f6c2194eba308da98b127cc6e630e source_ref=c1ada9d77b60fb66c2b1e14e94d08485646b4e02 -->
## `test_decorated_class_and_methods(sample_file: Path)`

Assert that a dataclass-decorated class and its methods are extracted with correct kinds.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_methods_of_private_class_inherit_privacy fingerprint=efb1e4c674bde3acc66af7113cbf8b87ddf3787d7e87ad8809a2fe54952c9a58 body_fp=eae62596fdb9b21f58b1cd93c3bb89252731b82597abe269604bbc5ce5c2f496 source_ref=c1ada9d77b60fb66c2b1e14e94d08485646b4e02 -->
## `test_methods_of_private_class_inherit_privacy(tmp_path: Path)`

Assert that methods of a private class are marked non-public regardless of their own name.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_module_docstring_is_not_a_symbol fingerprint=7dc979836e617d67e06caed3d5613df17b104280125ca185cc48f8989c7beba0 body_fp=6aa108d3f1953189dd1ac13d8ed852e5a8077bd48b186e233dd0c2f642c8bc09 source_ref=1eefecb3e6c1169dba9ec1c1839975a2e278182f -->
## `test_module_docstring_is_not_a_symbol(sample_file: Path)`

Assert that module docstrings do not cause a `__module__` symbol to be emitted.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_signature_includes_annotations_and_return_type fingerprint=090a7534671717c9765df4e6a87a99ebaf966a0ca91c602042577835228e3b23 body_fp=6a7e3fa4d32711a7ad3685f319e6b81fe031df74c59b1fd31f9f8ea3e163074d source_ref=c1ada9d77b60fb66c2b1e14e94d08485646b4e02 -->
## `test_signature_includes_annotations_and_return_type(sample_file: Path)`

Assert that a symbol's `signature` contains the function name, return type annotation, and no trailing colon.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_body_normalized_hash_is_stable_across_whitespace fingerprint=722aceba521e563ec81b8fbc59f1cfc325655527cf1213ff75cc89d9c9b84628 body_fp=5d276a0ec550dd3246a305860f98d782d0fa47d711d0891cc22d05d4c63fb926 source_ref=c1ada9d77b60fb66c2b1e14e94d08485646b4e02 -->
## `test_body_normalized_hash_is_stable_across_whitespace(tmp_path: Path)`

Assert that `body_normalized_hash` is identical for two functions differing only in indentation and trailing blank lines.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_body_normalized_hash_ignores_comments fingerprint=722aceba521e563ec81b8fbc59f1cfc325655527cf1213ff75cc89d9c9b84628 body_fp=8ebf787e996bdff6d4bf8fc4a89c46a1a809d9882e48b010f01778aa4895010f source_ref=c1ada9d77b60fb66c2b1e14e94d08485646b4e02 -->
## `test_body_normalized_hash_ignores_comments(tmp_path: Path)`

Assert that `body_normalized_hash` is identical for two functions differing only by an inline comment.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_body_normalized_hash_changes_on_real_change fingerprint=4446d6e99a53f2e6e7b6d4f1141b8a4a8b57daa6028410d2650442448448b579 body_fp=4b3e9d96659371b0a335cfdf0fd38b4830cdb858aee2282e472bb4bc62e74ce5 source_ref=c1ada9d77b60fb66c2b1e14e94d08485646b4e02 -->
## `test_body_normalized_hash_changes_on_real_change(tmp_path: Path)`

Assert that `body_normalized_hash` differs when a function's logic changes.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_signature_hash_changes_on_signature_change fingerprint=8f494b1008653349c4a28d6de4cac3606c19b823587f67ee9d47f1d8dc997c31 body_fp=fcd3541357a66bdda77cf30ae4dae7b1e5ea19d88791d81e87bba8683c7799e7 source_ref=c1ada9d77b60fb66c2b1e14e94d08485646b4e02 -->
## `test_signature_hash_changes_on_signature_change(tmp_path: Path)`

Assert that `signature_hash` differs when a function's parameter list changes.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_qualified_name_uses_source_root fingerprint=5ead7033f892dc234c69e3a017e1ebbcbb11d875a209fc806a9fcba87aa132d9 body_fp=bafda4df3c4d9a66555de6622554d819b6f4a2607f980c2a14f6bb49f75e24e4 source_ref=c1ada9d77b60fb66c2b1e14e94d08485646b4e02 -->
## `test_qualified_name_uses_source_root(tmp_path: Path)`

Verify that `extract_symbols` produces path-relative qualified names and `file_path` when `source_root` is supplied.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_line_numbers_are_one_indexed fingerprint=14041c3f38ae9dc76fc49a74415f83024112efbcab533580138927632b38a6c5 body_fp=db5150dae17fbb9573d6ae95a11f3fece268d03c72f693ec547fe4257eb33f1e source_ref=c1ada9d77b60fb66c2b1e14e94d08485646b4e02 -->
## `test_line_numbers_are_one_indexed(sample_file: Path)`

Assert that extracted symbol line numbers are one-indexed and `end_line` is not before `start_line`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_typing_overloads_dedupe_to_implementation fingerprint=be44d906148f1dd356a1afe6dc9a4013e51f9b9188f9b317ced6edfc09edfee1 body_fp=afdb925c385b9b8a6e37f26e1456b20e100fb5156e13854b8b4e5d24f1287d96 source_ref=c1ada9d77b60fb66c2b1e14e94d08485646b4e02 -->
## `test_typing_overloads_dedupe_to_implementation(tmp_path: Path)`

Assert that multiple `@overload` definitions with the same qualified name deduplicate to the single implementation, keeping the last (non-ellipsis) body.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_property_setter_pair_dedupes fingerprint=0122ca757e452aa9b2aa5bbf07419489fad3d5980db168e63267954ab4ac37c0 body_fp=aba82b469150cc6897c0a9a997d0bd07ce17ca94b71b41864d076ff5d60582ad source_ref=c1ada9d77b60fb66c2b1e14e94d08485646b4e02 -->
## `test_property_setter_pair_dedupes(tmp_path: Path)`

Assert that a `@property`/`@setter` pair with the same name deduplicates to a single symbol entry.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:_by_qname fingerprint=0a85addfd9a9878b63811e01d3b7e72652f5ffa26a39429ed2e9ea7d11f485eb body_fp=578455a4d8c4793b48cb186f3bc6263c120610748ea4f68d6df7b1cc2c92fbaa source_ref=c1ada9d77b60fb66c2b1e14e94d08485646b4e02 -->
## `_by_qname(syms: list[Symbol]) -> dict[str, Symbol]`

Index a list of `Symbol` objects by their `qualified_name` for O(1) lookup in tests.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:SAMPLE fingerprint=fb639546095eaf4b64bb3b8f29171c987afa4a72e204834daeb24e359a0c65c3 body_fp=057dd4e0858351af488629ac876d2d6fe1bb2412b65de80f113bb807619a5913 source_ref=1eefecb3e6c1169dba9ec1c1839975a2e278182f -->
## `SAMPLE: str`

Multi-definition Python source string used as fixture input across all `extract_symbols` tests.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_module_level_constants_are_indexed fingerprint=934c99099ef7470d0b0c8d198b66401aad6ad5ff62e14f91297468a441f10dd1 body_fp=101527132a0ce425dd6be70858c8f148f7aef00bcfbc1aea153b69facb4481b3 source_ref=1eefecb3e6c1169dba9ec1c1839975a2e278182f -->
## `test_module_level_constants_are_indexed(sample_file: Path)`

Assert that module-level `NAME = value` assignments are extracted as `kind='constant'` symbols with correct public visibility and signature text.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_dunder_constants_are_public fingerprint=2c69ff739047f70d26441af78a6e2406119f44399ed77d34e911349518e3cf35 body_fp=6dc8aa276a52b35ff0abf0259a702491cb05c1b41f6c7a251ddf9787627a1437 source_ref=1eefecb3e6c1169dba9ec1c1839975a2e278182f -->
## `test_dunder_constants_are_public(tmp_path: Path)`

Assert that dunder constants (`__version__`, `__all__`) have `is_public=True` while single-underscore names remain private.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_annotated_constants_are_indexed fingerprint=3ecf126e6835b79df3f0a1937a60781e754cd925c121094f84c904eb1744e7f8 body_fp=228c72d6e8901a9da696a6cb9a114520de7cea90c470239c1ee848d66f16c9fe source_ref=1eefecb3e6c1169dba9ec1c1839975a2e278182f -->
## `test_annotated_constants_are_indexed(tmp_path: Path)`

Assert that annotated module-level assignments (`NAME: T = value`) are indexed as `kind='constant'` symbols.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_tuple_unpacking_assignment_is_not_indexed fingerprint=8a67d2a581f1b300f468382b5c087928bb822a0fe09978c7cdd3abd22a8cc370 body_fp=20a4620e54b130aa74c2d5c3c01bcc5bc1a0b2b025a24636105f83a686d7da71 source_ref=1eefecb3e6c1169dba9ec1c1839975a2e278182f -->
## `test_tuple_unpacking_assignment_is_not_indexed(tmp_path: Path)`

Assert that tuple-unpacking assignments (`X, Y = 1, 2`) are excluded from the symbol table while single-target assignments remain indexed.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_module_symbol_emitted_for_setup_py_style_call fingerprint=7eb7703bc33208626441d8edc612fec9c8e18a4b96f8a9c5083d08a0111cdc05 body_fp=fafb0434d20cc78fe106b6b89fcf0b3e23ab8a00cb311ead024412b7a72c565d source_ref=1eefecb3e6c1169dba9ec1c1839975a2e278182f -->
## `test_module_symbol_emitted_for_setup_py_style_call(tmp_path: Path)`

Assert that a file with module-level function calls emits a synthetic `__module__` symbol containing the residual call expression.

- `__module__` symbol must have `kind == "module"` and `body_text` containing `setup(`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_module_symbol_not_emitted_for_pure_defs_with_imports fingerprint=69fcafd1e131f38c364a599dea3eec3d85ed75d0a690c32f6670dfbda8c690b0 body_fp=7157fc486ea22f9889ff53b200704e67754fe6b14828ec7483590c1322758be5 source_ref=1eefecb3e6c1169dba9ec1c1839975a2e278182f -->
## `test_module_symbol_not_emitted_for_pure_defs_with_imports(tmp_path: Path)`

Assert that `extract_symbols` does not emit a `__module__` symbol when a file contains only imports, a docstring, and function definitions.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:test_module_symbol_emitted_for_if_main_block fingerprint=4b26fd42e561b984ddd5a87821db2f718a35754e1127a3291eff52b85d1f33ed body_fp=a924e00143326ab0ed10c3a7ea769f78a4e0f374ac93d03c883e3ef574643474 source_ref=1eefecb3e6c1169dba9ec1c1839975a2e278182f -->
## `test_module_symbol_emitted_for_if_main_block(tmp_path: Path)`

Assert that an `if __name__ == '__main__':` block causes a `__module__` symbol to be emitted with the block's code in `body_text`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=6627db8bd92f8d034164adaf103671e5f854a358ad1504ae5ee960fd26525112 source_ref=1eefecb3e6c1169dba9ec1c1839975a2e278182f -->
## `tests/test_parse_python`

Test suite for `trie.parse.python.extract_symbols`, covering symbol extraction, hashing, privacy, deduplication, and module-level constant and `__module__` symbol behaviour.
<!-- trie:end -->