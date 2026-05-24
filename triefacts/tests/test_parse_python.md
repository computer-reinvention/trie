---
trie_version: 0.1.2
source: tests/test_parse_python.py
file_fingerprint: d3bccd8b18bdb9a160ab7d82799c0145fbd272fd43dfeb6e8b83da2a731cd106
last_synced_at: '2026-05-23T23:24:40Z'
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
<!-- trie:section symbol=tests/test_parse_python:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=ceefa0e2d1e74520b119204375cdb632e40d67b79b21931875d2db55d204ab72 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `tests/test_parse_python`

Test suite for `extract_symbols` and the `Symbol` dataclass from `trie.parse.python`.

- Covers: symbol extraction, privacy rules, hashing, deduplication, decorators, constants, and the synthetic `__module__` symbol.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:SAMPLE fingerprint=fb639546095eaf4b64bb3b8f29171c987afa4a72e204834daeb24e359a0c65c3 body_fp=532530e9180feba7100e1439c5a7d0b24b317227bd0792782066e51247fa7c8a source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `SAMPLE`

Fixture Python source string used as input for `extract_symbols` tests across the module.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:sample_file fingerprint=b7680b900a9acc188dfba8463fe039b88faa6b62e35109621d52f1e117bae469 body_fp=0a4d33be6167645ce82b9feb83b5e30c02206eefca23e61c8eff30ad99ae27cc source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `sample_file(tmp_path: Path) -> Path`

Pytest fixture that writes `SAMPLE` source text to a temporary file and returns its path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:_by_qname fingerprint=0a85addfd9a9878b63811e01d3b7e72652f5ffa26a39429ed2e9ea7d11f485eb body_fp=fc6f750b5cd07e6b6d72dfd38155acd78902cff265647a476b85fd0bfa025d58 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `_by_qname(syms: list[Symbol]) -> dict[str, Symbol]`

Index a list of `Symbol` objects by their `qualified_name`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_extracts_top_level_functions fingerprint=2985cdbe318b6e5e9115926392340dadffa4a0be631eb0fdbc5f85bcbf864298 body_fp=31df3e919d9d83604ae7baf15d1f1040a40149204aeaa636cf634b5b59a80e98 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_extracts_top_level_functions(sample_file: Path)`

Assert that `extract_symbols` extracts top-level functions with correct kind, visibility, and docstring.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_private_marked_correctly fingerprint=28601d753007fcef28c01a9129bc9b368715630da23d964e9e62072196c9d979 body_fp=1586eb4d59a470bd4c5776b1832281589c43b15326e13c9f9d984c70f82cb480 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_private_marked_correctly(sample_file: Path)`

Assert that `_private_fn` has `is_public == False` in the extracted symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_decorated_function_is_extracted fingerprint=d2d7ce46ca962dc7c71ac1b6c70d42bf492ef2f9d2dc8b42481dceed2df1046b body_fp=239a916b29244f894e3719b20e7f8fae43cc7526d6fe2acbcb63d7634c6f511e source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_decorated_function_is_extracted(sample_file: Path)`

Assert that a `@staticmethod`-decorated top-level function is included in extracted symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_class_and_methods fingerprint=511da3a4934e700fc6fc494d44925a03c492be4e0832580d9500872a2a9aba9e body_fp=7c6f594740a21bbf44b907d154c8d5ffc9f9fb1d1fdea88844a41f48c8523864 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_class_and_methods(sample_file: Path)`

Assert that `Greeter` is extracted as a class with correctly typed and privacy-tagged methods.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_decorated_class_and_methods fingerprint=b3273d90f06a67f481b7a5017a2b75c82ee9fe1bb786eb654b7e6608c6d7be1e body_fp=ade974633f9f4c31e54c400419a75a3c5489bc7cf405564214bd244348b5eeaa source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_decorated_class_and_methods(sample_file: Path)`

Assert that a decorated class and its methods are extracted with correct kinds.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_methods_of_private_class_inherit_privacy fingerprint=efb1e4c674bde3acc66af7113cbf8b87ddf3787d7e87ad8809a2fe54952c9a58 body_fp=d067716bc3da9677ed25824ad0618ef4bd8ee69830b3fd08d49661550a4e7f5a source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_methods_of_private_class_inherit_privacy(tmp_path: Path)`

Assert that methods of a private class inherit `is_public=False` regardless of their own name.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_module_docstring_is_not_a_symbol fingerprint=7dc979836e617d67e06caed3d5613df17b104280125ca185cc48f8989c7beba0 body_fp=0ba08085e4041a3cb7aef5014dbce91cf1d7f426b78123dfa0a08bab475d9597 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_module_docstring_is_not_a_symbol(sample_file: Path)`

Assert that `extract_symbols` emits no `__module__` symbol when the only module-level residual is a docstring and imports.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_module_level_constants_are_indexed fingerprint=934c99099ef7470d0b0c8d198b66401aad6ad5ff62e14f91297468a441f10dd1 body_fp=c68ded05b1148030616cfc0b96229a33578106057b34f487720bc29fbceaa283 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_module_level_constants_are_indexed(sample_file: Path)`

Assert that module-level `NAME = value` assignments are extracted as `kind='constant'` symbols with correct `is_public` and `signature`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_signature_includes_annotations_and_return_type fingerprint=090a7534671717c9765df4e6a87a99ebaf966a0ca91c602042577835228e3b23 body_fp=c1e0e96fc5225e2d7f58b9172a53e904c7691c1844645b292c0794a2dda5e323 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_signature_includes_annotations_and_return_type(sample_file: Path)`

Assert that extracted `signature` includes parameter annotations, return type, and no trailing colon.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_body_normalized_hash_is_stable_across_whitespace fingerprint=722aceba521e563ec81b8fbc59f1cfc325655527cf1213ff75cc89d9c9b84628 body_fp=ae4392a16adc54855832cee03ba6e34fe4533948c46bddf4846a9ce285a88214 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_body_normalized_hash_is_stable_across_whitespace(tmp_path: Path)`

Assert that `body_normalized_hash` is identical for two functions differing only in whitespace.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_body_normalized_hash_ignores_comments fingerprint=722aceba521e563ec81b8fbc59f1cfc325655527cf1213ff75cc89d9c9b84628 body_fp=8ebf787e996bdff6d4bf8fc4a89c46a1a809d9882e48b010f01778aa4895010f source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_body_normalized_hash_ignores_comments(tmp_path: Path)`

Assert that `body_normalized_hash` is identical for two functions differing only by an inline comment.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_body_normalized_hash_changes_on_real_change fingerprint=4446d6e99a53f2e6e7b6d4f1141b8a4a8b57daa6028410d2650442448448b579 body_fp=283d3744a55c1d9a88492107dee2e1d35392967958eb29fb5d5308f7b3d7daa1 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_body_normalized_hash_changes_on_real_change(tmp_path: Path)`

Assert that `body_normalized_hash` differs when two functions have distinct return expressions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_signature_hash_changes_on_signature_change fingerprint=8f494b1008653349c4a28d6de4cac3606c19b823587f67ee9d47f1d8dc997c31 body_fp=617302440a1181d1dedc4dcfc703126479c148bfa48703a668e5b2c2cd731607 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_signature_hash_changes_on_signature_change(tmp_path: Path)`

Assert that `Symbol.signature_hash` differs when a function's parameter list changes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_qualified_name_uses_source_root fingerprint=5ead7033f892dc234c69e3a017e1ebbcbb11d875a209fc806a9fcba87aa132d9 body_fp=6a0776a21a18e2d72635964fd4f3e59cdd769ead6ed5e275c6d573616a1d93f3 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_qualified_name_uses_source_root(tmp_path: Path)`

Assert that `qualified_name` and `file_path` are relativised to `source_root` when provided.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_line_numbers_are_one_indexed fingerprint=14041c3f38ae9dc76fc49a74415f83024112efbcab533580138927632b38a6c5 body_fp=d4295a6925d5442c50ad55307d59233045b801691249ecd7f308e09162d0a8a1 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_line_numbers_are_one_indexed(sample_file: Path)`

Assert that extracted symbols carry one-indexed line numbers with `end_line >= start_line`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_typing_overloads_dedupe_to_implementation fingerprint=be44d906148f1dd356a1afe6dc9a4013e51f9b9188f9b317ced6edfc09edfee1 body_fp=4b116b37b868a7bd3905f1375dbfb9eafee5fd30ea142e58130f6d0cf7b559eb source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_typing_overloads_dedupe_to_implementation(tmp_path: Path)`

Assert that multiple `@overload` definitions collapse to a single symbol retaining the concrete implementation body.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_property_setter_pair_dedupes fingerprint=0122ca757e452aa9b2aa5bbf07419489fad3d5980db168e63267954ab4ac37c0 body_fp=a2bf2c09f57160add55f19cbdb23bbc2790a5fd8c33569e856474948aa800cc2 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_property_setter_pair_dedupes(tmp_path: Path)`

Assert that `@property` and `@x.setter` definitions with the same name deduplicate to a single `Symbol`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_dunder_constants_are_public fingerprint=2c69ff739047f70d26441af78a6e2406119f44399ed77d34e911349518e3cf35 body_fp=5aa4da4d86c3edd26bb677aa7fd997aeb1f06b649ea2b7a69f4ca0b0aec4591d source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_dunder_constants_are_public(tmp_path: Path)`

Assert that dunder-named constants (`__version__`, `__all__`) are marked `is_public=True` while single-underscore names remain private.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_annotated_constants_are_indexed fingerprint=3ecf126e6835b79df3f0a1937a60781e754cd925c121094f84c904eb1744e7f8 body_fp=e04e65610902ee6eaa3ae3c8a3ceea04d80a229bbbf08624851dca1fa7999c8e source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_annotated_constants_are_indexed(tmp_path: Path)`

Assert that annotated assignments (`NAME: T = value`) are extracted as `kind='constant'` symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_tuple_unpacking_assignment_is_not_indexed fingerprint=8a67d2a581f1b300f468382b5c087928bb822a0fe09978c7cdd3abd22a8cc370 body_fp=20a4620e54b130aa74c2d5c3c01bcc5bc1a0b2b025a24636105f83a686d7da71 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_tuple_unpacking_assignment_is_not_indexed(tmp_path: Path)`

Assert that tuple-unpacking assignments (`X, Y = 1, 2`) are excluded from the symbol table while single-target assignments remain indexed.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_module_symbol_emitted_for_setup_py_style_call fingerprint=7eb7703bc33208626441d8edc612fec9c8e18a4b96f8a9c5083d08a0111cdc05 body_fp=53ff1a41eaff6ed39882e644a8f5182ffe9a89eae04eb31d3bf334a07cdf728c source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_module_symbol_emitted_for_setup_py_style_call(tmp_path: Path)`

Assert that a file with a module-level function call emits a `__module__` symbol containing that call in `body_text`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_module_symbol_not_emitted_for_pure_defs_with_imports fingerprint=69fcafd1e131f38c364a599dea3eec3d85ed75d0a690c32f6670dfbda8c690b0 body_fp=803f94a1ce8df19383587db65d63a3e11a9af93f5f95a6127a555192d788a3a0 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_module_symbol_not_emitted_for_pure_defs_with_imports(tmp_path: Path)`

Assert that `extract_symbols` omits the synthetic `__module__` symbol when residual module-level code is only imports and a docstring.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_method_has_parent_class fingerprint=e53e2a74d075f82ac0a2cc7ecbc2da04848a4095fa19c0b9fce01a37cc7e442b body_fp=e772d546fa833fff8b6f5a4e8cdb2aa9e8c2541c56fbcd8d5fdfd30e7e98898a source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_method_has_parent_class(sample_file: Path)`

Assert that extracted `Greeter` methods have `parent_class` set to `"Greeter"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_function_has_no_parent_class fingerprint=1f1a400fa4137c04af90e081af41d153ac601d4be2a6c6e4fae3a30cfaad4106 body_fp=5ef79ef4f9f714990b7ef1d22c12c9b6b2ea6d8aa59bb76ebbcb5c3b09d044a8 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_function_has_no_parent_class(sample_file: Path)`

Assert that a top-level function symbol has `parent_class` set to `None`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_class_has_no_parent_class fingerprint=da3991eeda890b014400054650ccb364d136972e2d28918a5c398983768a3b9f body_fp=f4ca1a0eca3f25980ee81fb590fcfa26da076a467a625aeedd26ea2b7a1622ca source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_class_has_no_parent_class(sample_file: Path)`

Assert that a top-level `Symbol` of kind `class` has `parent_class` set to `None`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_decorator_captured_on_method fingerprint=c84c1b0d44000aca8a33d0c8804d3a88a753603ea50813dddb7b5f054708c528 body_fp=5425846ace0f68f4ab721f4ac0d2c9ef94145fb61adac98d4fdb8809c749ce61 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_decorator_captured_on_method(sample_file: Path)`

Assert that `@classmethod` appears in the `decorators` field of `Greeter.make`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_decorator_captured_on_class fingerprint=c394950dd15965a621dcc90144b495a286007545795c15ceeab2f74319f331b9 body_fp=a221190b79758b1c20a2bf49cb10eb3b79794ed6c43e00a3781bcac73e34f43e source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_decorator_captured_on_class(sample_file: Path)`

Assert that the `@dataclass` decorator is recorded in the `decorators` field of the `Decorated` class symbol.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_undecorated_method_has_empty_decorators fingerprint=e8dec182e5cdb332ca11e6d0fefaa34b0a5871f91b71e9169e8b7269be4546cd body_fp=038e3d6eaa52cafa46f8149b3d8f9dfc09558d292da11452023c54aff5b1629d source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_undecorated_method_has_empty_decorators(sample_file: Path)`

Assert that `Greeter.hello`, which has no decorators, yields an empty `decorators` tuple.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_property_decorator_captured fingerprint=d8e0b621e08bd5a0b07c897a55f9309be4e38eaf869ac83172e1d2753d349c8d body_fp=b0c191c7eb5f5deebbd33b95ed3869950b85d32b010d49a6f953cff847910e42 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_property_decorator_captured(tmp_path: Path)`

Verify that `@property` appears in a method's `decorators` and `parent_class` is set correctly.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_symbols_sorted_by_start_line fingerprint=0dd0f63f1c1f08d24175aa2c2e2b008478a0fbd7c311d21c8665b296719c9ec8 body_fp=0e975a98bbef9bd48ecb6b5e0a1e4e4a1d595fcc039a3ae8fdc3d92dd3ea1ff8 source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_symbols_sorted_by_start_line(tmp_path: Path)`

Assert that `extract_symbols` returns symbols in ascending `start_line` order.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_parse_python:test_module_symbol_emitted_for_if_main_block fingerprint=4b26fd42e561b984ddd5a87821db2f718a35754e1127a3291eff52b85d1f33ed body_fp=60af1973ee497fa01849c670657e039ed7cbfa9e1e993c6943166dd0b140571b source_ref=93809e4913996946b57287c3e4db23faab7807bc -->
## `test_module_symbol_emitted_for_if_main_block(tmp_path: Path)`

Assert that a file containing `if __name__ == '__main__':` emits a `__module__` symbol whose `body_text` includes that block.
<!-- trie:end -->