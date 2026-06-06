---
trie_version: 0.1.5
source: tests/test_parse_python.py
file_fingerprint: d3bccd8b18bdb9a160ab7d82799c0145fbd272fd43dfeb6e8b83da2a731cd106
last_synced_at: '2026-06-06T13:23:42Z'
defines:
- kind: module
  qualified_name: tests/test_parse_python:__module__
  lines: 1-416
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
  qualified_name: tests/test_parse_python:test_method_has_parent_class
  lines: 352-356
- kind: function
  qualified_name: tests/test_parse_python:test_function_has_no_parent_class
  lines: 359-361
- kind: function
  qualified_name: tests/test_parse_python:test_class_has_no_parent_class
  lines: 364-366
- kind: function
  qualified_name: tests/test_parse_python:test_decorator_captured_on_method
  lines: 369-371
- kind: function
  qualified_name: tests/test_parse_python:test_decorator_captured_on_class
  lines: 374-376
- kind: function
  qualified_name: tests/test_parse_python:test_undecorated_method_has_empty_decorators
  lines: 379-381
- kind: function
  qualified_name: tests/test_parse_python:test_property_decorator_captured
  lines: 384-389
- kind: function
  qualified_name: tests/test_parse_python:test_symbols_sorted_by_start_line
  lines: 392-404
- kind: function
  qualified_name: tests/test_parse_python:test_module_symbol_emitted_for_if_main_block
  lines: 407-415
incoming_refs: 0
outgoing_refs: 31
---
<!-- trie:section symbol=tests/test_parse_python:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=fd8ebde63047b5f0f9b1ef8ef321e787f13ce8d34b482582f936cffef1247baa source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
Contains comprehensive test suite for Python symbol extraction functionality. Validates parsing of functions, classes, methods, constants, decorators, privacy rules, qualified naming, hash generation, and edge cases like overloads and property setters.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:SAMPLE fingerprint=fb639546095eaf4b64bb3b8f29171c987afa4a72e204834daeb24e359a0c65c3 body_fp=5b1ca041799eca3deab74b81f5cf53dc3bf125a2c9f6ec2ff4c5a60f6332d7d9 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
Multiline string containing sample Python code used across test fixtures to validate symbol extraction behavior.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:sample_file fingerprint=b7680b900a9acc188dfba8463fe039b88faa6b62e35109621d52f1e117bae469 body_fp=811d8a55ced9bbf2d1ab207c74ac69a1247c84ad1dc78acceb8c7373b303bfe3 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
Creates a temporary Python file containing the SAMPLE code and returns its path for testing.

- Returns path to temporary file written with SAMPLE constant contents
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:_by_qname fingerprint=0a85addfd9a9878b63811e01d3b7e72652f5ffa26a39429ed2e9ea7d11f485eb body_fp=fee00d80e7429baf3ed2a83a4689cf47b1f5baba3dd5fa0ccf0643f4c9b875ff source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
Converts a list of Symbol objects into a dictionary keyed by their qualified names.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_extracts_top_level_functions fingerprint=2985cdbe318b6e5e9115926392340dadffa4a0be631eb0fdbc5f85bcbf864298 body_fp=51a98c0174fc65858a23f30dc742b03bf7fabb0a6bcb9bd194c66fd832a513c8 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
Verifies that `extract_symbols` correctly identifies and extracts public function definitions with proper metadata.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_private_marked_correctly fingerprint=28601d753007fcef28c01a9129bc9b368715630da23d964e9e62072196c9d979 body_fp=368b6644b1c4280fe23c525590b5ac0b733be71e63760d29c75047c249c242b0 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
Verifies that functions with leading underscore names are marked as non-public by the symbol extractor.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_decorated_function_is_extracted fingerprint=d2d7ce46ca962dc7c71ac1b6c70d42bf492ef2f9d2dc8b42481dceed2df1046b body_fp=50fd1406af166b1b24af1618a783d971ea0b6b1754ce1c21c56b5e6ed29be4ef source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
Verifies that `extract_symbols` finds functions with decorators.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_class_and_methods fingerprint=511da3a4934e700fc6fc494d44925a03c492be4e0832580d9500872a2a9aba9e body_fp=8f1d371b3f3ea8be53b64133870abb1078582d791f89c1f4785c2ae7e8fe6299 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
Verifies that extract_symbols correctly identifies class and method symbols with proper kind classification and privacy detection.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_decorated_class_and_methods fingerprint=b3273d90f06a67f481b7a5017a2b75c82ee9fe1bb786eb654b7e6608c6d7be1e body_fp=b72025ddf2e35a7ad16283fb1a4f292ea973cbd9ab6082b5c79eef387c2c4bbc source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
Verifies that extract_symbols correctly identifies decorated classes and their methods as separate symbols with proper kinds.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_methods_of_private_class_inherit_privacy fingerprint=efb1e4c674bde3acc66af7113cbf8b87ddf3787d7e87ad8809a2fe54952c9a58 body_fp=2d959ad737fdc98922e41e291cadfdf1576a8a003641de79801a72a964d2bc1c source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
Tests that methods inherit their parent class's privacy level: private class methods are always private regardless of their own naming.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_module_docstring_is_not_a_symbol fingerprint=7dc979836e617d67e06caed3d5613df17b104280125ca185cc48f8989c7beba0 body_fp=1c86580312142b2afdb8362d786de672316fd44df532213bd0861e17603a89b4 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
Tests that module docstrings don't generate spurious `__module__` symbols in the extracted symbol list.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_module_level_constants_are_indexed fingerprint=934c99099ef7470d0b0c8d198b66401aad6ad5ff62e14f91297468a441f10dd1 body_fp=5a41904adcd96bed9cc343bdcae635c695f149bef6a8883eb0a30561d3dfac7c source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
Verifies that module-level assignment statements are extracted as constant symbols with correct metadata.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_signature_includes_annotations_and_return_type fingerprint=090a7534671717c9765df4e6a87a99ebaf966a0ca91c602042577835228e3b23 body_fp=05f2cab12bac3036a1872990fa478daadee33671ee510b764ff947aad4b51b26 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
Verifies that Symbol.signature includes type annotations and return types without trailing colons.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_body_normalized_hash_is_stable_across_whitespace fingerprint=722aceba521e563ec81b8fbc59f1cfc325655527cf1213ff75cc89d9c9b84628 body_fp=a3eb1a7add548367e32a05f8b0b521bcf2d1b3d0956b056880336d1bd1770f3c source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
Verifies that Symbol.body_normalized_hash produces identical hashes for equivalent code with different whitespace formatting.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_body_normalized_hash_ignores_comments fingerprint=722aceba521e563ec81b8fbc59f1cfc325655527cf1213ff75cc89d9c9b84628 body_fp=60df54e8faae3c2789d467106cee81aca5ab8a5210f7d3dda38640cbfe29ffb4 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
Verifies that body_normalized_hash ignores comments when computing hash values for Symbol instances.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_body_normalized_hash_changes_on_real_change fingerprint=4446d6e99a53f2e6e7b6d4f1141b8a4a8b57daa6028410d2650442448448b579 body_fp=80c2f7842add19271a1bd22fca5b8fb749aa5763d5d17140e0b20fcdb0cd5ba9 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
Verifies that body_normalized_hash changes when function logic differs between two symbol instances.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_signature_hash_changes_on_signature_change fingerprint=8f494b1008653349c4a28d6de4cac3606c19b823587f67ee9d47f1d8dc997c31 body_fp=ae4ab0749d972606d1bc7aeb2b60cab5c061aa8631305e9be98d6b1a0be3668c source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
Verifies that Symbol.signature_hash differs when function signatures change between files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_qualified_name_uses_source_root fingerprint=5ead7033f892dc234c69e3a017e1ebbcbb11d875a209fc806a9fcba87aa132d9 body_fp=dd1335c3c762bddd48687f63782f4c55599c55d7a5a3f4bd0f1d8c5b2980f3ba source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
Tests that `extract_symbols` uses the `source_root` parameter to generate relative qualified names and file paths.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_line_numbers_are_one_indexed fingerprint=14041c3f38ae9dc76fc49a74415f83024112efbcab533580138927632b38a6c5 body_fp=1bc76871db73d6b22a7fd104416727fd3e4c5611f1ad7ae1bbf5625cabce934f source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
Tests that Symbol line numbers use one-based indexing and follow source order.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_typing_overloads_dedupe_to_implementation fingerprint=be44d906148f1dd356a1afe6dc9a4013e51f9b9188f9b317ced6edfc09edfee1 body_fp=423b0d1eb404f4784a35dde0995c49b228e654d3e047b9effb791b5f775d0ce9 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
Verifies that multiple `@overload` definitions with the same qualified name deduplicate to the implementation method.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_property_setter_pair_dedupes fingerprint=0122ca757e452aa9b2aa5bbf07419489fad3d5980db168e63267954ab4ac37c0 body_fp=c55498dc8375bc8337da2f7b1c96d9ab6ee0619eeb204d9ca4548d8abc7dbbf6 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
Verifies that property getter and setter methods with identical names merge to a single symbol entry.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_dunder_constants_are_public fingerprint=2c69ff739047f70d26441af78a6e2406119f44399ed77d34e911349518e3cf35 body_fp=297d81f876657fb47471a68813c70e9db44d2a05094fbd26f99319e1381233d2 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
Verifies that dunder constants like `__version__` and `__all__` are marked as public symbols despite underscore prefixes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_annotated_constants_are_indexed fingerprint=3ecf126e6835b79df3f0a1937a60781e754cd925c121094f84c904eb1744e7f8 body_fp=6dc0ef289920d349156961552e984c7c9ea331d2797a54be127fe6ab1402f540 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
Verifies that annotated assignments like `NAME: Type = value` are extracted as constant symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_tuple_unpacking_assignment_is_not_indexed fingerprint=8a67d2a581f1b300f468382b5c087928bb822a0fe09978c7cdd3abd22a8cc370 body_fp=c4c891eba259e3ede295b06104187b2dd943285b9f0126380bfb85a64b573095 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
Verifies that tuple unpacking assignments are not indexed while single-identifier assignments are.

- Creates test file with `X, Y = 1, 2` and `Z = 3` assignments
- Confirms `Z` symbol exists but `X` and `Y` symbols are excluded
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_module_symbol_emitted_for_setup_py_style_call fingerprint=7eb7703bc33208626441d8edc612fec9c8e18a4b96f8a9c5083d08a0111cdc05 body_fp=08c0d62d98b26b5ec62ad856755a0b4301d78f2dd40bc79921864fb44bb1b0ac source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
Tests that extract_symbols generates synthetic `__module__` symbols for files with module-level function calls.

- Creates a mock setup.py with a helper function and top-level setup() call
- Verifies the `__module__` symbol captures the setup() call in its body_text
- Ensures module-level behavior is indexed for triefact generation
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_module_symbol_not_emitted_for_pure_defs_with_imports fingerprint=69fcafd1e131f38c364a599dea3eec3d85ed75d0a690c32f6670dfbda8c690b0 body_fp=0633c056965eb96f6932bacb5084b68f3d2846ca5f2086384bbff6be8bd6b469 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
Tests that `extract_symbols` skips `__module__` synthetic symbols for files containing only imports, docstrings, and function/class definitions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_method_has_parent_class fingerprint=e53e2a74d075f82ac0a2cc7ecbc2da04848a4095fa19c0b9fce01a37cc7e442b body_fp=2e244541fe00fd3e5125b54cecc556031852794ddc52d4e306509680055ada8b source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
Verifies that extracted method symbols correctly populate parent_class attribute with their containing class name.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_function_has_no_parent_class fingerprint=1f1a400fa4137c04af90e081af41d153ac601d4be2a6c6e4fae3a30cfaad4106 body_fp=3dd9880874257d12ed344b991667baaf43e6bc17d1b22ebab06c0cb1bfc8b71a source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
Verifies that top-level functions have `parent_class` set to `None`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_class_has_no_parent_class fingerprint=da3991eeda890b014400054650ccb364d136972e2d28918a5c398983768a3b9f body_fp=dc8000126048656bd999573ce35ac24aa24d70c148d3b7939431157f06df4b05 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
Verifies that top-level classes have `parent_class` set to None.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_decorator_captured_on_method fingerprint=c84c1b0d44000aca8a33d0c8804d3a88a753603ea50813dddb7b5f054708c528 body_fp=3d39bd3fcba43b035c938dd8d896a20746f6ec68d10059d7fb4d02b0ed9fb8e4 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
Tests that `@classmethod` decorator is captured in the decorators field of `Greeter.make` symbol.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_decorator_captured_on_class fingerprint=c394950dd15965a621dcc90144b495a286007545795c15ceeab2f74319f331b9 body_fp=32f66680d784e5ac6fbf9d7d7c34e9694785b6eadaf825fda32aeea456837ebc source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
Verifies that class decorators are captured in the decorators field of extracted symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_undecorated_method_has_empty_decorators fingerprint=e8dec182e5cdb332ca11e6d0fefaa34b0a5871f91b71e9169e8b7269be4546cd body_fp=996baf7237a70605f69a0c13e23c82dea955405c32e0ac0881e63162b2febd20 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
Tests that undecorated methods have an empty tuple for their decorators attribute.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_property_decorator_captured fingerprint=d8e0b621e08bd5a0b07c897a55f9309be4e38eaf869ac83172e1d2753d349c8d body_fp=744d8fa2129f30e54f1d32e752d6d3aa3665ef2e056e249d7cc5134d758004a6 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
Verifies that the parser correctly captures @property decorators on method symbols and sets the parent_class field.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_symbols_sorted_by_start_line fingerprint=0dd0f63f1c1f08d24175aa2c2e2b008478a0fbd7c311d21c8665b296719c9ec8 body_fp=480ce77a16735ef75206cf1d032a42f637a549a6199e9a6d5e7f281df870d7a3 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=source-parsing -->
Verifies that `extract_symbols` returns symbols sorted by their source line numbers in ascending order.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_module_symbol_emitted_for_if_main_block fingerprint=4b26fd42e561b984ddd5a87821db2f718a35754e1127a3291eff52b85d1f33ed body_fp=c11350d6b59b98122b7c36164f6eeabbcb62b70f6f3d547519942e2b94fb3829 source_ref=93809e4913996946b57287c3e4db23faab7807bc role=test-infrastructure -->
Verifies that `if __name__ == '__main__':` blocks trigger creation of a `__module__` symbol containing the module-level execution code.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_parse_python:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=8d07c36e8bfae9f0006b79610149085c213ce52e4bcecd1a32d9592082cff8a7 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Test suite for the Python symbol extraction parser, verifying extraction of functions, classes, methods, constants, and module-level behavior.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:SAMPLE fingerprint=fb639546095eaf4b64bb3b8f29171c987afa4a72e204834daeb24e359a0c65c3 body_fp=bf12d518c94d2473e80b58ec835644401e5d700d4ef6937773db9d20edec4723 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Multi-line string containing sample Python code with various constructs for testing symbol extraction.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:sample_file fingerprint=b7680b900a9acc188dfba8463fe039b88faa6b62e35109621d52f1e117bae469 body_fp=19c167e6e3164a315144a3d9258adc039d7e7a485554fd48a732474f5e35b680 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Creates a temporary Python file containing the SAMPLE test code for parsing tests.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:_by_qname fingerprint=0a85addfd9a9878b63811e01d3b7e72652f5ffa26a39429ed2e9ea7d11f485eb body_fp=fee00d80e7429baf3ed2a83a4689cf47b1f5baba3dd5fa0ccf0643f4c9b875ff source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Converts a list of Symbol objects into a dictionary keyed by their qualified names.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_extracts_top_level_functions fingerprint=2985cdbe318b6e5e9115926392340dadffa4a0be631eb0fdbc5f85bcbf864298 body_fp=40d266140e450068097d785956d42ed3d1333f2e6e6e25f7054369a32dc7a617 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Verifies that extract_symbols correctly identifies and extracts top-level function definitions with proper metadata.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_private_marked_correctly fingerprint=28601d753007fcef28c01a9129bc9b368715630da23d964e9e62072196c9d979 body_fp=1f6c6a97914b556d2b33d94e849f29df7f21dc5a6b9f58484deb20fa7c7fc82a source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Verifies that functions with leading underscores are correctly marked as private by the symbol extractor.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_decorated_function_is_extracted fingerprint=d2d7ce46ca962dc7c71ac1b6c70d42bf492ef2f9d2dc8b42481dceed2df1046b body_fp=5736a0c605faa286f36d55754b8657abbcc193fa9f02967eedd0150cae416fdf source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Verifies that decorated functions are successfully extracted as symbols by the Python parser.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_class_and_methods fingerprint=511da3a4934e700fc6fc494d44925a03c492be4e0832580d9500872a2a9aba9e body_fp=45b605643c18c5150920e16c986b86300c244a99b78a36b259c85f5106728232 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Verifies that extract_symbols correctly identifies classes and their methods with proper kind classification and privacy detection.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_decorated_class_and_methods fingerprint=b3273d90f06a67f481b7a5017a2b75c82ee9fe1bb786eb654b7e6608c6d7be1e body_fp=72d1e5f865665eddd29cd974d11c3fa70c969cfbceece38d045100bfaf9bff8c source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Verifies that decorated classes and their methods are correctly extracted by the symbol parser.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_methods_of_private_class_inherit_privacy fingerprint=efb1e4c674bde3acc66af7113cbf8b87ddf3787d7e87ad8809a2fe54952c9a58 body_fp=a250b452424f88b6e44a46d0f284de1594ad3d1bb7dfa5a7d4eac2d591278a1d source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Tests that methods inherit privacy status from their parent class when the class is private.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_module_docstring_is_not_a_symbol fingerprint=7dc979836e617d67e06caed3d5613df17b104280125ca185cc48f8989c7beba0 body_fp=1249a52de5876715bf0a57af86bb4f99dbc294386dab32e65a984cbf857c36d4 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Verifies that module docstrings don't generate `__module__` symbols when no operational module-level code exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_module_level_constants_are_indexed fingerprint=934c99099ef7470d0b0c8d198b66401aad6ad5ff62e14f91297468a441f10dd1 body_fp=2ef14e5063f49b1020ac3accc5b452d17d9fd83cac42624e794b226c33d4d3d4 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Verifies that module-level variable assignments are extracted as constant symbols with proper metadata.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_signature_includes_annotations_and_return_type fingerprint=090a7534671717c9765df4e6a87a99ebaf966a0ca91c602042577835228e3b23 body_fp=cc6432e7570ab2195fec9aac4141090537d833c036a92b75f57b8169dec074e6 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Verifies that Symbol.signature includes type annotations and return type without trailing colon.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_body_normalized_hash_is_stable_across_whitespace fingerprint=722aceba521e563ec81b8fbc59f1cfc325655527cf1213ff75cc89d9c9b84628 body_fp=09a66799206e9ccadddaee1c4fa2cbdabffca3d7546a99c68bac249cf91e9f69 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Verifies that Symbol.body_normalized_hash produces identical values for functionally equivalent code with different whitespace formatting.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_body_normalized_hash_ignores_comments fingerprint=722aceba521e563ec81b8fbc59f1cfc325655527cf1213ff75cc89d9c9b84628 body_fp=886d0421f8b23d0d120a080902f32f20ff52c85c31b624377f585c5692017e0a source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Verifies that body_normalized_hash ignores comment differences between functionally identical code.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_body_normalized_hash_changes_on_real_change fingerprint=4446d6e99a53f2e6e7b6d4f1141b8a4a8b57daa6028410d2650442448448b579 body_fp=9f78081e67341148b48006293af2808d22fdac391582e93216e05613e62cb364 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Verifies that body_normalized_hash changes when function implementation differs meaningfully.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_signature_hash_changes_on_signature_change fingerprint=8f494b1008653349c4a28d6de4cac3606c19b823587f67ee9d47f1d8dc997c31 body_fp=69e36cb43ba170ff2f86a7b74df0a2290a2cfd1d728f4fbe72b011bb3b195e2e source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Verifies that Symbol.signature_hash differs when function signatures change.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_qualified_name_uses_source_root fingerprint=5ead7033f892dc234c69e3a017e1ebbcbb11d875a209fc806a9fcba87aa132d9 body_fp=bcafc49adfeaf1633a5abee501d9828860c1c8b4d15e70b30e82b0784c85d9cc source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Tests that `extract_symbols` correctly computes qualified names and file paths relative to the provided `source_root` parameter.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_line_numbers_are_one_indexed fingerprint=14041c3f38ae9dc76fc49a74415f83024112efbcab533580138927632b38a6c5 body_fp=66c5feceff0ac8b1c470b3dbed7c705c177824d37f65add5bb997fc460e01603 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Verifies that Symbol.start_line and Symbol.end_line use one-based indexing and are properly ordered.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_typing_overloads_dedupe_to_implementation fingerprint=be44d906148f1dd356a1afe6dc9a4013e51f9b9188f9b317ced6edfc09edfee1 body_fp=44d359dadfcdc1ea2235eb924647e6394763901151007258c60fc79cc051fd9d source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Verifies extract_symbols deduplicates typing.overload methods, keeping only the implementation.

- Creates file with @overload signatures and actual implementation
- Confirms exactly one symbol survives for the method name
- Ensures the kept symbol contains implementation body, not ellipsis stub
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_property_setter_pair_dedupes fingerprint=0122ca757e452aa9b2aa5bbf07419489fad3d5980db168e63267954ab4ac37c0 body_fp=6c2b6f419362a5ba9d51694f1675ffb4fc8d1c5bdf955840a8e5dedd847c5d36 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Verifies that property getter and setter methods with the same name produce only one symbol in the extraction results.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_dunder_constants_are_public fingerprint=2c69ff739047f70d26441af78a6e2406119f44399ed77d34e911349518e3cf35 body_fp=8720832d0cea35897253b9682e3f77aa0fc6d50d7b4ad68c5d4940c9fd9efc8f source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Verifies that dunder constants like `__version__` and `__all__` are marked as public while single-underscore names remain private.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_annotated_constants_are_indexed fingerprint=3ecf126e6835b79df3f0a1937a60781e754cd925c121094f84c904eb1744e7f8 body_fp=6dc0ef289920d349156961552e984c7c9ea331d2797a54be127fe6ab1402f540 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Verifies that annotated assignments like `NAME: Type = value` are extracted as constant symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_tuple_unpacking_assignment_is_not_indexed fingerprint=8a67d2a581f1b300f468382b5c087928bb822a0fe09978c7cdd3abd22a8cc370 body_fp=61d11956a406ebf038967c2682d65b191376e5fbab7d601903bb148b3b162536 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Verifies that tuple unpacking assignments are not indexed as constant symbols while single-target assignments are.

- Creates test file with `X, Y = 1, 2` (tuple unpacking) and `Z = 3` (single target)  
- Asserts only `Z` symbol is extracted, not `X` or `Y`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_module_symbol_emitted_for_setup_py_style_call fingerprint=7eb7703bc33208626441d8edc612fec9c8e18a4b96f8a9c5083d08a0111cdc05 body_fp=a1eaddd30772e681af035cfc781f7031c3be075583a2fa8d7daae1816a8bfdbc source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Tests that extract_symbols creates a synthetic `__module__` symbol for files with operational module-level code like setup calls.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_module_symbol_not_emitted_for_pure_defs_with_imports fingerprint=69fcafd1e131f38c364a599dea3eec3d85ed75d0a690c32f6670dfbda8c690b0 body_fp=2c621ad09de12acf2d872d919a8e70fcbebac577ea204189c3c119457b33c6d4 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Verifies that extract_symbols does not emit a synthetic `__module__` symbol for files containing only imports and function definitions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_method_has_parent_class fingerprint=e53e2a74d075f82ac0a2cc7ecbc2da04848a4095fa19c0b9fce01a37cc7e442b body_fp=435c9feecd177b93abb137d96527caf84b2aa3379c74197f30b734e2fa330362 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Verifies that extracted method symbols correctly populate their `parent_class` attribute with the containing class name.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_function_has_no_parent_class fingerprint=1f1a400fa4137c04af90e081af41d153ac601d4be2a6c6e4fae3a30cfaad4106 body_fp=83b9bfc03167eeba8eb00e637c65bb082ac0948c6a6b7ea5c14dfb5a20f95e76 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Verifies that `extract_symbols` sets `parent_class` to `None` for top-level functions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_class_has_no_parent_class fingerprint=da3991eeda890b014400054650ccb364d136972e2d28918a5c398983768a3b9f body_fp=a0fdba4c1dea76b46b776f9566fdb5ceb2520ae9285b43d87cc2bdcac2b2f94e source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Tests that top-level classes have no parent_class attribute set.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_decorator_captured_on_method fingerprint=c84c1b0d44000aca8a33d0c8804d3a88a753603ea50813dddb7b5f054708c528 body_fp=3d0808bd36081505865c7e1d78e7972fe5856776b6c15ab8ca732b89aa8c08fc source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Verifies that extract_symbols captures decorators on methods in the decorators field.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_decorator_captured_on_class fingerprint=c394950dd15965a621dcc90144b495a286007545795c15ceeab2f74319f331b9 body_fp=34b2bbf890cd330d21e625967b94db1e55e1a89b1210559f0f64166289205551 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Verifies that class decorators are captured in the `decorators` field of extracted symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_undecorated_method_has_empty_decorators fingerprint=e8dec182e5cdb332ca11e6d0fefaa34b0a5871f91b71e9169e8b7269be4546cd body_fp=d17199bed04a60e78598f54c7412b0b1fc458b5c1524e6a2913c11c423ce287a source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Verifies that methods without decorators have an empty decorators tuple in extracted symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_property_decorator_captured fingerprint=d8e0b621e08bd5a0b07c897a55f9309be4e38eaf869ac83172e1d2753d349c8d body_fp=6ad274c7a20f4d9d59ffc680214f83ab1db56f39d5489e68f9234a2d11bc7ca3 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Verifies that Symbol extraction captures @property decorators on methods and correctly identifies parent class.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_symbols_sorted_by_start_line fingerprint=0dd0f63f1c1f08d24175aa2c2e2b008478a0fbd7c311d21c8665b296719c9ec8 body_fp=8fd3eb5b27233fc514f9cf06d347ddd9002ed629d522be28a405d654f8a5330d source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Verifies that `extract_symbols` returns symbols sorted by their source file line numbers in ascending order.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_module_symbol_emitted_for_if_main_block fingerprint=4b26fd42e561b984ddd5a87821db2f718a35754e1127a3291eff52b85d1f33ed body_fp=7bdcbd769d7a8ae7e990b09b69b2c452d0235a41fb0fcfea961daf8465cba834 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
Verifies that extract_symbols creates a `__module__` symbol containing `if __name__ == '__main__'` blocks.
<!-- trie:end -->