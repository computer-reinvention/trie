---
trie_version: 0.3.0
source: tests/test_parse_python.py
file_fingerprint: 0867d135d52592bbce73d22f09c32b3222da06eb2432a757ad9427c4274dcf58
last_synced_at: '2026-08-02T21:19:01Z'
defines:
- kind: module
  qualified_name: tests/test_parse_python:__module__
  lines: 1-445
- kind: constant
  qualified_name: tests/test_parse_python:SAMPLE
  lines: 9-57
- kind: function
  qualified_name: tests/test_parse_python:sample_file
  lines: 61-64
  signature: 'def sample_file(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_parse_python:_by_qname
  lines: 67-68
  signature: 'def _by_qname(syms: list[Symbol]) -> dict[str, Symbol]'
- kind: function
  qualified_name: tests/test_parse_python:test_extracts_top_level_functions
  lines: 71-76
  signature: 'def test_extracts_top_level_functions(sample_file: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_private_marked_correctly
  lines: 79-81
  signature: 'def test_private_marked_correctly(sample_file: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_decorated_function_is_extracted
  lines: 84-86
  signature: 'def test_decorated_function_is_extracted(sample_file: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_class_and_methods
  lines: 89-95
  signature: 'def test_class_and_methods(sample_file: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_decorated_class_and_methods
  lines: 98-101
  signature: 'def test_decorated_class_and_methods(sample_file: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_methods_of_private_class_inherit_privacy
  lines: 104-118
  signature: 'def test_methods_of_private_class_inherit_privacy(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_module_docstring_is_not_a_symbol
  lines: 121-131
  signature: 'def test_module_docstring_is_not_a_symbol(sample_file: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_module_level_constants_are_indexed
  lines: 134-145
  signature: 'def test_module_level_constants_are_indexed(sample_file: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_signature_includes_annotations_and_return_type
  lines: 148-154
  signature: 'def test_signature_includes_annotations_and_return_type(sample_file: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_signature_preserves_kwonly_and_posonly_markers
  lines: 157-167
  signature: 'def test_signature_preserves_kwonly_and_posonly_markers(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_multi_line_signature_is_captured_verbatim_and_squeezes_to_one_line
  lines: 170-183
  signature: 'def test_multi_line_signature_is_captured_verbatim_and_squeezes_to_one_line(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_body_normalized_hash_is_stable_across_whitespace
  lines: 186-193
  signature: 'def test_body_normalized_hash_is_stable_across_whitespace(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_body_normalized_hash_ignores_comments
  lines: 196-203
  signature: 'def test_body_normalized_hash_ignores_comments(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_body_normalized_hash_changes_on_real_change
  lines: 206-213
  signature: 'def test_body_normalized_hash_changes_on_real_change(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_signature_hash_changes_on_signature_change
  lines: 216-223
  signature: 'def test_signature_hash_changes_on_signature_change(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_qualified_name_uses_source_root
  lines: 226-233
  signature: 'def test_qualified_name_uses_source_root(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_line_numbers_are_one_indexed
  lines: 236-241
  signature: 'def test_line_numbers_are_one_indexed(sample_file: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_typing_overloads_dedupe_to_implementation
  lines: 244-266
  signature: 'def test_typing_overloads_dedupe_to_implementation(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_property_setter_pair_dedupes
  lines: 269-284
  signature: 'def test_property_setter_pair_dedupes(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_dunder_constants_are_public
  lines: 292-303
  signature: 'def test_dunder_constants_are_public(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_annotated_constants_are_indexed
  lines: 306-314
  signature: 'def test_annotated_constants_are_indexed(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_tuple_unpacking_assignment_is_not_indexed
  lines: 317-328
  signature: 'def test_tuple_unpacking_assignment_is_not_indexed(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_module_symbol_emitted_for_setup_py_style_call
  lines: 331-353
  signature: 'def test_module_symbol_emitted_for_setup_py_style_call(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_module_symbol_not_emitted_for_pure_defs_with_imports
  lines: 356-378
  signature: 'def test_module_symbol_not_emitted_for_pure_defs_with_imports(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_method_has_parent_class
  lines: 381-385
  signature: 'def test_method_has_parent_class(sample_file: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_function_has_no_parent_class
  lines: 388-390
  signature: 'def test_function_has_no_parent_class(sample_file: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_class_has_no_parent_class
  lines: 393-395
  signature: 'def test_class_has_no_parent_class(sample_file: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_decorator_captured_on_method
  lines: 398-400
  signature: 'def test_decorator_captured_on_method(sample_file: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_decorator_captured_on_class
  lines: 403-405
  signature: 'def test_decorator_captured_on_class(sample_file: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_undecorated_method_has_empty_decorators
  lines: 408-410
  signature: 'def test_undecorated_method_has_empty_decorators(sample_file: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_property_decorator_captured
  lines: 413-418
  signature: 'def test_property_decorator_captured(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_symbols_sorted_by_start_line
  lines: 421-433
  signature: 'def test_symbols_sorted_by_start_line(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_parse_python:test_module_symbol_emitted_for_if_main_block
  lines: 436-444
  signature: 'def test_module_symbol_emitted_for_if_main_block(tmp_path: Path)'
incoming_refs: 0
outgoing_refs: 34
---
<!-- trie:section symbol=tests/test_parse_python:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=8d07c36e8bfae9f0006b79610149085c213ce52e4bcecd1a32d9592082cff8a7 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
Test suite for the Python symbol extraction parser, verifying extraction of functions, classes, methods, constants, and module-level behavior.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:SAMPLE fingerprint=fb639546095eaf4b64bb3b8f29171c987afa4a72e204834daeb24e359a0c65c3 body_fp=bf12d518c94d2473e80b58ec835644401e5d700d4ef6937773db9d20edec4723 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
Multi-line string containing sample Python code with various constructs for testing symbol extraction.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:sample_file fingerprint=b7680b900a9acc188dfba8463fe039b88faa6b62e35109621d52f1e117bae469 body_fp=412dbd26b216bbad8da403b1dcd7f37accf9fc9bfbb9d77daa46a724a6d31a4d source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
## `def sample_file(tmp_path: Path) -> Path`

Creates a temporary Python file containing the SAMPLE test code for parsing tests.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:_by_qname fingerprint=0a85addfd9a9878b63811e01d3b7e72652f5ffa26a39429ed2e9ea7d11f485eb body_fp=b39404364613b2e8a2d8a41b8cb9fdf4e0c461f77c25e3653aae1e965da61279 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
## `def _by_qname(syms: list[Symbol]) -> dict[str, Symbol]`

Converts a list of Symbol objects into a dictionary keyed by their qualified names.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_extracts_top_level_functions fingerprint=2985cdbe318b6e5e9115926392340dadffa4a0be631eb0fdbc5f85bcbf864298 body_fp=9be741dc0126c9a84945b5df966533e83c351ed8ac07fbc84d4af1a57c9923ed source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
## `def test_extracts_top_level_functions(sample_file: Path)`

Verifies that extract_symbols correctly identifies and extracts top-level function definitions with proper metadata.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_private_marked_correctly fingerprint=28601d753007fcef28c01a9129bc9b368715630da23d964e9e62072196c9d979 body_fp=e5d379bd04d152d3faa98415a43f9f7f0fc880d239998941fd3aaad28d211378 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
## `def test_private_marked_correctly(sample_file: Path)`

Verifies that functions with leading underscores are correctly marked as private by the symbol extractor.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_decorated_function_is_extracted fingerprint=d2d7ce46ca962dc7c71ac1b6c70d42bf492ef2f9d2dc8b42481dceed2df1046b body_fp=0ea1320d31dcb94bde5ea3654bd44accd0dbd96cecef9b143fe88ce9c9329737 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
## `def test_decorated_function_is_extracted(sample_file: Path)`

Verifies that decorated functions are successfully extracted as symbols by the Python parser.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_class_and_methods fingerprint=511da3a4934e700fc6fc494d44925a03c492be4e0832580d9500872a2a9aba9e body_fp=fc1ec5653c9db1fb00082789c184582bf9374fa62c12a7bcbf18a1b4b432fe54 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
## `def test_class_and_methods(sample_file: Path)`

Verifies that extract_symbols correctly identifies classes and their methods with proper kind classification and privacy detection.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_decorated_class_and_methods fingerprint=b3273d90f06a67f481b7a5017a2b75c82ee9fe1bb786eb654b7e6608c6d7be1e body_fp=96af0c1676a71dd1e0fa6f32afb9e1b7c82f863989efd16cd1d8a09f51c2033d source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
## `def test_decorated_class_and_methods(sample_file: Path)`

Verifies that decorated classes and their methods are correctly extracted by the symbol parser.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_methods_of_private_class_inherit_privacy fingerprint=efb1e4c674bde3acc66af7113cbf8b87ddf3787d7e87ad8809a2fe54952c9a58 body_fp=4d1b87b317bed48db3fbbfa44fac27fa4ace7cd950fc43b3b955166f7d0aa692 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
## `def test_methods_of_private_class_inherit_privacy(tmp_path: Path)`

Tests that methods inherit privacy status from their parent class when the class is private.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_module_docstring_is_not_a_symbol fingerprint=7dc979836e617d67e06caed3d5613df17b104280125ca185cc48f8989c7beba0 body_fp=fb2ed2630a5de36672c91ffb05ebf5346575aa2c9cee797a0b275e2f53402a87 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
## `def test_module_docstring_is_not_a_symbol(sample_file: Path)`

Verifies that module docstrings don't generate `__module__` symbols when no operational module-level code exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_module_level_constants_are_indexed fingerprint=934c99099ef7470d0b0c8d198b66401aad6ad5ff62e14f91297468a441f10dd1 body_fp=b30c60d562077341bbba623c28b958f7805d5220e33d892d37518187097585ba source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
## `def test_module_level_constants_are_indexed(sample_file: Path)`

Verifies that module-level variable assignments are extracted as constant symbols with proper metadata.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_signature_includes_annotations_and_return_type fingerprint=090a7534671717c9765df4e6a87a99ebaf966a0ca91c602042577835228e3b23 body_fp=64fe05150950c14dd10089c20bab940e97ff6091d0831f32f040552a20b69255 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
## `def test_signature_includes_annotations_and_return_type(sample_file: Path)`

Verifies that Symbol.signature includes type annotations and return type without trailing colon.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_signature_preserves_kwonly_and_posonly_markers fingerprint=02897a8b4646121f57c5a04f68fb8ced32fa90e607be6be638bb22b94bacce74 body_fp=edd16cd974e7aa83d052748c1727eac8d7dbeea704914fbbae5571aa9cd54fab source_ref=8fc7f2b1bf5358154d86d90c1e41df9e5f9d3ad5 role=test -->
## `def test_signature_preserves_kwonly_and_posonly_markers(tmp_path: Path)`

Assert that `Symbol.signature` preserves positional-only (`/`) and keyword-only (`*`) parameter markers verbatim for a synthetic single-function module.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_multi_line_signature_is_captured_verbatim_and_squeezes_to_one_line fingerprint=d502f41db79e1a3d2302966b2e8e674e8e6479385a65067862ef063170918938 body_fp=3f602969d99a6936def44a38de36c8b6fb3ffed5b5736edd76eb1385f486123d source_ref=8fc7f2b1bf5358154d86d90c1e41df9e5f9d3ad5 role=test -->
## `def test_multi_line_signature_is_captured_verbatim_and_squeezes_to_one_line(tmp_path: Path)`

Asserts that `Symbol.signature` preserves raw newlines for a wrapped parameter list, and that `squeeze_signature` collapses them to a single line without losing any tokens.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_body_normalized_hash_is_stable_across_whitespace fingerprint=722aceba521e563ec81b8fbc59f1cfc325655527cf1213ff75cc89d9c9b84628 body_fp=b34f00f73d41f2de8b2475a1073a3de32da4156830eabfcc7f8a1189e1750fc5 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
## `def test_body_normalized_hash_is_stable_across_whitespace(tmp_path: Path)`

Verifies that Symbol.body_normalized_hash produces identical values for functionally equivalent code with different whitespace formatting.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_body_normalized_hash_ignores_comments fingerprint=722aceba521e563ec81b8fbc59f1cfc325655527cf1213ff75cc89d9c9b84628 body_fp=0694e0c4d6df82b2ae84c767caf84bcb45cb786050bce0dbaa1e7f822e080886 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
## `def test_body_normalized_hash_ignores_comments(tmp_path: Path)`

Verifies that body_normalized_hash ignores comment differences between functionally identical code.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_body_normalized_hash_changes_on_real_change fingerprint=4446d6e99a53f2e6e7b6d4f1141b8a4a8b57daa6028410d2650442448448b579 body_fp=c8979c56cbac2c3a987263c960f002a7a9ae25e0e1ff64f07dc4e80d50f104a9 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
## `def test_body_normalized_hash_changes_on_real_change(tmp_path: Path)`

Verifies that body_normalized_hash changes when function implementation differs meaningfully.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_signature_hash_changes_on_signature_change fingerprint=8f494b1008653349c4a28d6de4cac3606c19b823587f67ee9d47f1d8dc997c31 body_fp=b760712c6da350f994b697e6aec7071968e425941c63b6857adbfd748797127f source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
## `def test_signature_hash_changes_on_signature_change(tmp_path: Path)`

Verifies that Symbol.signature_hash differs when function signatures change.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_qualified_name_uses_source_root fingerprint=5ead7033f892dc234c69e3a017e1ebbcbb11d875a209fc806a9fcba87aa132d9 body_fp=c6ebb2c42be6d2ec5d25661410fb6988f5947e0f75b71ac4ff7a605f1ef44f15 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
## `def test_qualified_name_uses_source_root(tmp_path: Path)`

Tests that `extract_symbols` correctly computes qualified names and file paths relative to the provided `source_root` parameter.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_line_numbers_are_one_indexed fingerprint=14041c3f38ae9dc76fc49a74415f83024112efbcab533580138927632b38a6c5 body_fp=0ede33523b9d34e49d46aebe1d692a65d87316f9a3831d53df5b62ef7d4dcc90 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
## `def test_line_numbers_are_one_indexed(sample_file: Path)`

Verifies that Symbol.start_line and Symbol.end_line use one-based indexing and are properly ordered.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_typing_overloads_dedupe_to_implementation fingerprint=be44d906148f1dd356a1afe6dc9a4013e51f9b9188f9b317ced6edfc09edfee1 body_fp=b24ea94b28047e5c6e9819f08020ea21bd785adb1b63f8c9330cecb0491f0204 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
## `def test_typing_overloads_dedupe_to_implementation(tmp_path: Path)`

Verifies extract_symbols deduplicates typing.overload methods, keeping only the implementation.

- Creates file with @overload signatures and actual implementation
- Confirms exactly one symbol survives for the method name
- Ensures the kept symbol contains implementation body, not ellipsis stub
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_property_setter_pair_dedupes fingerprint=0122ca757e452aa9b2aa5bbf07419489fad3d5980db168e63267954ab4ac37c0 body_fp=0e3f9042ade5cbf6b3dd7be35216a55603abfb612a054ef42f2eedea0ae9761e source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
## `def test_property_setter_pair_dedupes(tmp_path: Path)`

Verifies that property getter and setter methods with the same name produce only one symbol in the extraction results.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_dunder_constants_are_public fingerprint=2c69ff739047f70d26441af78a6e2406119f44399ed77d34e911349518e3cf35 body_fp=d343a7b1dbf7ba9f33ca95249437e12783268a3556703afcb36a7ef110bc60a6 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
## `def test_dunder_constants_are_public(tmp_path: Path)`

Verifies that dunder constants like `__version__` and `__all__` are marked as public while single-underscore names remain private.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_annotated_constants_are_indexed fingerprint=3ecf126e6835b79df3f0a1937a60781e754cd925c121094f84c904eb1744e7f8 body_fp=c268e998b3c559941d63b279b7aa54e8ef5dc98fe4a703afb0f79e70ece4ad12 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
## `def test_annotated_constants_are_indexed(tmp_path: Path)`

Verifies that annotated assignments like `NAME: Type = value` are extracted as constant symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_tuple_unpacking_assignment_is_not_indexed fingerprint=8a67d2a581f1b300f468382b5c087928bb822a0fe09978c7cdd3abd22a8cc370 body_fp=e0b8c41571004f2d1fba55a2db11c43a1cba62f7b5f9a9598c56b3cc1b8ce476 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
## `def test_tuple_unpacking_assignment_is_not_indexed(tmp_path: Path)`

Verifies that tuple unpacking assignments are not indexed as constant symbols while single-target assignments are.

- Creates test file with `X, Y = 1, 2` (tuple unpacking) and `Z = 3` (single target)  
- Asserts only `Z` symbol is extracted, not `X` or `Y`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_module_symbol_emitted_for_setup_py_style_call fingerprint=7eb7703bc33208626441d8edc612fec9c8e18a4b96f8a9c5083d08a0111cdc05 body_fp=c068cad23906aa73637823fce5677e7e677f9efff72e7e862ab6209f258ebcc0 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
## `def test_module_symbol_emitted_for_setup_py_style_call(tmp_path: Path)`

Tests that extract_symbols creates a synthetic `__module__` symbol for files with operational module-level code like setup calls.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_module_symbol_not_emitted_for_pure_defs_with_imports fingerprint=69fcafd1e131f38c364a599dea3eec3d85ed75d0a690c32f6670dfbda8c690b0 body_fp=7ec2d1f1babbe7fe06d096899aec63c9d70606ef0ca040f3f22b4d9d4f0b45d9 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
## `def test_module_symbol_not_emitted_for_pure_defs_with_imports(tmp_path: Path)`

Verifies that extract_symbols does not emit a synthetic `__module__` symbol for files containing only imports and function definitions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_method_has_parent_class fingerprint=e53e2a74d075f82ac0a2cc7ecbc2da04848a4095fa19c0b9fce01a37cc7e442b body_fp=8e0f85a7333a04a66941cde958255cfa225e6d1b923296383d79e77d736ad26c source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
## `def test_method_has_parent_class(sample_file: Path)`

Verifies that extracted method symbols correctly populate their `parent_class` attribute with the containing class name.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_function_has_no_parent_class fingerprint=1f1a400fa4137c04af90e081af41d153ac601d4be2a6c6e4fae3a30cfaad4106 body_fp=ad8590bceb32cdd5a6f5ab859b64d5b3713d365800c532f5f0ba7178bb954740 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
## `def test_function_has_no_parent_class(sample_file: Path)`

Verifies that `extract_symbols` sets `parent_class` to `None` for top-level functions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_class_has_no_parent_class fingerprint=da3991eeda890b014400054650ccb364d136972e2d28918a5c398983768a3b9f body_fp=f1f66a8b2b4d75dd2cc1efdf8d4a8a690ced33a0826c79009a73bc508ff730de source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
## `def test_class_has_no_parent_class(sample_file: Path)`

Tests that top-level classes have no parent_class attribute set.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_decorator_captured_on_method fingerprint=c84c1b0d44000aca8a33d0c8804d3a88a753603ea50813dddb7b5f054708c528 body_fp=402c53845c33f063fcccd80997e652d69396d25b432b693261685190a2e8446b source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
## `def test_decorator_captured_on_method(sample_file: Path)`

Verifies that extract_symbols captures decorators on methods in the decorators field.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_decorator_captured_on_class fingerprint=c394950dd15965a621dcc90144b495a286007545795c15ceeab2f74319f331b9 body_fp=5d00ec327b42b23514493f1566d4bdb1fd2340050ced36f3e681a41ee35248c6 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
## `def test_decorator_captured_on_class(sample_file: Path)`

Verifies that class decorators are captured in the `decorators` field of extracted symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_undecorated_method_has_empty_decorators fingerprint=e8dec182e5cdb332ca11e6d0fefaa34b0a5871f91b71e9169e8b7269be4546cd body_fp=f9c5ffdbd20edc08cbde1fa2f61d379cac3b21430b5ad465937907de72666e71 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
## `def test_undecorated_method_has_empty_decorators(sample_file: Path)`

Verifies that methods without decorators have an empty decorators tuple in extracted symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_property_decorator_captured fingerprint=d8e0b621e08bd5a0b07c897a55f9309be4e38eaf869ac83172e1d2753d349c8d body_fp=86fb4dcc0978cb16cedd02ce47a4f916e9f016c51ef3228c4a6b80d6c0bb3b9c source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
## `def test_property_decorator_captured(tmp_path: Path)`

Verifies that Symbol extraction captures @property decorators on methods and correctly identifies parent class.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_symbols_sorted_by_start_line fingerprint=0dd0f63f1c1f08d24175aa2c2e2b008478a0fbd7c311d21c8665b296719c9ec8 body_fp=77fcae7b1f625f947ca362d4528ad22d92d0ff042cf1ea0e7c9c449dad482a41 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
## `def test_symbols_sorted_by_start_line(tmp_path: Path)`

Verifies that `extract_symbols` returns symbols sorted by their source file line numbers in ascending order.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_module_symbol_emitted_for_if_main_block fingerprint=4b26fd42e561b984ddd5a87821db2f718a35754e1127a3291eff52b85d1f33ed body_fp=4b9f49a0e44c402483b631d62855407577eb47a1ba9bb39282cd3a3e44622bee source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
## `def test_module_symbol_emitted_for_if_main_block(tmp_path: Path)`

Verifies that extract_symbols creates a `__module__` symbol containing `if __name__ == '__main__'` blocks.
<!-- trie:end -->