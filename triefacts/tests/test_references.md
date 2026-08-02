---
trie_version: 0.3.0
source: tests/test_references.py
file_fingerprint: 31d34bead6a71a40d8647b7c19d2fb34878be91c5edb289e504f52798bb97687
last_synced_at: '2026-08-01T00:20:41Z'
defines:
- kind: module
  qualified_name: tests/test_references:__module__
  lines: 1-263
- kind: function
  qualified_name: tests/test_references:_refs_by_src
  lines: 8-13
  signature: def _refs_by_src(file_data) -> dict[str, list[str]]
- kind: function
  qualified_name: tests/test_references:test_intra_file_function_calls_create_edges
  lines: 16-26
  signature: 'def test_intra_file_function_calls_create_edges(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_references:test_intra_file_class_to_function_edge
  lines: 29-36
  signature: 'def test_intra_file_class_to_function_edge(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_references:test_imports_create_cross_file_edges
  lines: 39-44
  signature: 'def test_imports_create_cross_file_edges(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_references:test_aliased_import_resolves_to_original
  lines: 47-52
  signature: 'def test_aliased_import_resolves_to_original(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_references:test_dotted_module_import
  lines: 55-60
  signature: 'def test_dotted_module_import(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_references:test_relative_imports_skipped
  lines: 63-71
  signature: 'def test_relative_imports_skipped(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_references:test_no_self_references
  lines: 74-82
  signature: 'def test_no_self_references(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_references:test_unresolved_names_silently_dropped
  lines: 85-91
  signature: 'def test_unresolved_names_silently_dropped(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_references:test_class_methods_inherit_class_qname_in_src
  lines: 94-102
  signature: 'def test_class_methods_inherit_class_qname_in_src(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_references:test_extract_file_data_includes_symbols
  lines: 105-110
  signature: 'def test_extract_file_data_includes_symbols(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_references:test_both_import_and_intra_file_edges_resolve
  lines: 113-123
  signature: 'def test_both_import_and_intra_file_edges_resolve(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_references:test_plain_import_attribute_access
  lines: 131-137
  signature: 'def test_plain_import_attribute_access(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_references:test_aliased_plain_import_attribute_access
  lines: 140-147
  signature: 'def test_aliased_plain_import_attribute_access(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_references:test_dotted_import_attribute_access
  lines: 150-160
  signature: 'def test_dotted_import_attribute_access(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_references:test_from_import_submodule_attribute_resolves
  lines: 163-175
  signature: 'def test_from_import_submodule_attribute_resolves(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_references:test_module_attribute_emitted_even_for_stdlib
  lines: 178-189
  signature: 'def test_module_attribute_emitted_even_for_stdlib(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_references:test_mixed_from_and_plain_import
  lines: 192-204
  signature: 'def test_mixed_from_and_plain_import(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_references:test_attribute_access_through_local_var_not_treated_as_module
  lines: 207-219
  signature: 'def test_attribute_access_through_local_var_not_treated_as_module(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_references:test_module_attribute_no_self_edge
  lines: 222-233
  signature: 'def test_module_attribute_no_self_edge(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_references:test_function_local_import_creates_edge
  lines: 236-246
  signature: 'def test_function_local_import_creates_edge(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_references:test_import_nested_in_conditional_creates_edge
  lines: 249-262
  signature: 'def test_import_nested_in_conditional_creates_edge(tmp_path: Path)'
incoming_refs: 0
outgoing_refs: 21
---
<!-- trie:section symbol=tests/test_references:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=d05f7a619001e77a71db28d519558a058d7cdd1a63f5e2942ccaf592eb2f5256 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 role=test-infrastructure -->
Tests for reference extraction functionality in the trie.parse.references module.

- `_refs_by_src()` — Helper function that groups file references by source qualified name
- `test_intra_file_function_calls_create_edges()` — Verifies function-to-function calls within same file generate references
- `test_intra_file_class_to_function_edge()` — Tests method-to-function references within same file
- `test_imports_create_cross_file_edges()` — Validates imported symbols create cross-file references
- `test_aliased_import_resolves_to_original()` — Ensures aliased imports resolve to original symbol names
- `test_dotted_module_import()` — Tests dotted module import resolution
- `test_relative_imports_skipped()` — Confirms relative imports are ignored in extraction
- `test_no_self_references()` — Verifies recursive functions don't create self-edges
- `test_unresolved_names_silently_dropped()` — Tests unresolved names are filtered out
- `test_class_methods_inherit_class_qname_in_src()` — Validates method qualified names include class prefix
- `test_extract_file_data_includes_symbols()` — Tests symbol extraction alongside reference extraction
- `test_both_import_and_intra_file_edges_resolve()` — Verifies mixed import and local references work together
- `test_plain_import_attribute_access()` — Tests module.attribute resolution for plain imports
- `test_aliased_plain_import_attribute_access()` — Tests attribute access through aliased module imports
- `test_dotted_import_attribute_access()` — Tests attribute resolution for dotted module imports
- `test_from_import_submodule_attribute_resolves()` — Tests submodule attribute access patterns
- `test_module_attribute_emitted_even_for_stdlib()` — Ensures stdlib module attributes generate candidate edges
- `test_mixed_from_and_plain_import()` — Tests combination of different import styles
- `test_attribute_access_through_local_var_not_treated_as_module()` — Prevents local variable attribute access from creating module edges
- `test_module_attribute_no_self_edge()` — Ensures module self-references don't create edges
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:_refs_by_src fingerprint=9008a0d0cd30929c25a818e62440a5015ef19e44627b3d4e097d9be3eba52021 body_fp=a3f1267d218040b2ad38fd7a8c1844c4656609193832e89111f9a71c2d463150 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 role=test-infrastructure -->
## `def _refs_by_src(file_data) -> dict[str, list[str]]`

Converts file_data references into a dictionary mapping source qualified names to sorted lists of target qualified names.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_intra_file_function_calls_create_edges fingerprint=f59ed7b0886dada67f2106498921a398c3ef4d7b0dabcf68629f2e9682a8866c body_fp=53faccca1801b017a3ae7fb4dfcf4133802f3ffd2760fc6591d7d2dbbb147f0b source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 role=test-infrastructure -->
## `def test_intra_file_function_calls_create_edges(tmp_path: Path)`

Tests that function calls within the same file create reference edges and duplicate calls are deduplicated.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_intra_file_class_to_function_edge fingerprint=adcdb1040d5e3e90cdab10fd997a7fe730601dfc1212cc4dc872313fc16da8e1 body_fp=93c56416539255defcdd81013b88b5a6128d4cc37ff95e5d7ed91d6f9a129f8f source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 role=source-parsing -->
## `def test_intra_file_class_to_function_edge(tmp_path: Path)`

Verifies that a method calling a function in the same file creates a reference edge from method to function.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_imports_create_cross_file_edges fingerprint=03c21101344781b8aff3ba8df3898b34ead9ffe3d5c5f248e9d95c8bba9042b2 body_fp=1bea4cc5431b515b873ab44a70e42b42d8dfdcd673c48c9df5b1b94a288e05a7 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 role=source-parsing -->
## `def test_imports_create_cross_file_edges(tmp_path: Path)`

Verifies that importing a function from another module creates cross-file reference edges when that function is called.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_aliased_import_resolves_to_original fingerprint=03c21101344781b8aff3ba8df3898b34ead9ffe3d5c5f248e9d95c8bba9042b2 body_fp=ba9475f82a714a5a1378e7711e87f69e2dfe4f2c5f87a66b73c0d202f84a80bd source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 role=source-parsing -->
## `def test_aliased_import_resolves_to_original(tmp_path: Path)`

Verifies that import aliases resolve to their original qualified names, not the alias names.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_dotted_module_import fingerprint=a669dbba4d5f289f095822c5fdaa1aeb35019ddd4136e96fdcd6976913ab5c34 body_fp=888114b96be8bd6bb83762a7fdd0be50e5644cc525ad0ecfa4f5b91d2d684bd8 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 role=test-infrastructure -->
## `def test_dotted_module_import(tmp_path: Path)`

Verifies that importing from a dotted module path creates a reference with forward-slash-separated target qname.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_relative_imports_skipped fingerprint=a932a8034d6ca1b3fda32e58fc083098dfabcdee9a0784e23f448b51e3573a33 body_fp=559043c758d6c5761279d3390df29127ddbf5c457dd067f626c2168a2d90468f source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 role=test-infrastructure -->
## `def test_relative_imports_skipped(tmp_path: Path)`

Verifies that relative imports are ignored and do not create reference edges in the extracted file data.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_no_self_references fingerprint=b40e3e9191a7a230558fd500e8d4191dcea1b1556d0d3b1fae1b17f881438199 body_fp=17e2eb793b5716e0272bbd0ea032033c843adb01a20b89bbc5f952e1c86691b8 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 role=source-parsing -->
## `def test_no_self_references(tmp_path: Path)`

Verifies that recursive function calls do not create self-referencing edges in the extracted references.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_unresolved_names_silently_dropped fingerprint=6eaa0933d7f7b603204566b92e79d1dd51918c9819eab15dcc74dbe69d8048eb body_fp=68d5551eb12f4de36e61da914095e3aeee27fd87ff54c50e181cff5aa4c33ea1 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 role=source-parsing -->
## `def test_unresolved_names_silently_dropped(tmp_path: Path)`

Tests that unresolved function names produce no reference edges in the extracted file data.

• Creates test module with calls to undefined `some_global` and builtin `len`
• Verifies no spurious references are generated for unresolvable symbols
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_class_methods_inherit_class_qname_in_src fingerprint=27656fb38d31ffb0baaaa90f4a3d536791e132132f1dc6f54d4520a4f4563830 body_fp=b3bd02dfceab67cb922a3898de8a467d9a60f3a425bb0d87c9ebf87d935c9ff8 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 role=test-infrastructure -->
## `def test_class_methods_inherit_class_qname_in_src(tmp_path: Path)`

Verifies that class method references include the full qualified name with class prefix in src_qname.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_extract_file_data_includes_symbols fingerprint=a9dd60ee72bd3fda7c5c8c7f7afcfb096f2df081102db374bf41c0e7bffd2fc4 body_fp=c24a81ee7fc966347f0eb4f92390614c82530af2d287528e89f80a5d96182654 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 role=test-infrastructure -->
## `def test_extract_file_data_includes_symbols(tmp_path: Path)`

Verifies that `extract_file_data` correctly identifies and returns all symbols defined in a Python file with their qualified names.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_both_import_and_intra_file_edges_resolve fingerprint=c43fc568966bf2fdbaaf95b67a808d17ad4abc1e688e7df6846e7d7d8e4f4081 body_fp=8fbd3a8fc7d601c11e63a8473d71688b8121b9843e71d7896dec93432cd41d64 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 role=source-parsing -->
## `def test_both_import_and_intra_file_edges_resolve(tmp_path: Path)`

Verifies that `extract_file_data` correctly identifies both cross-file import references and intra-file function call references from the same source symbol.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_plain_import_attribute_access fingerprint=9db43c1bc6facc99a0f5bd980f2976af5d303a71998ea31d579ad82b44395c7f body_fp=9cd4705c36d760a4350b3b86307692abab55be080639fa0d7906e3d500f7c82a source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 role=source-parsing -->
## `def test_plain_import_attribute_access(tmp_path: Path)`

Verifies that `import foo` followed by `foo.bar()` creates a reference to `foo:bar`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_aliased_plain_import_attribute_access fingerprint=8f322e134ab11d36dc9413ddd7c8458cddc834ff56fe7034b931f13e2364b653 body_fp=ff5ba5e1673f7261529498085002ab0620395f53ce02008aed075dfc85553370 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 role=source-parsing -->
## `def test_aliased_plain_import_attribute_access(tmp_path: Path)`

Tests that aliased module imports resolve attribute access to the original module name.

- Creates code with `import foo as f` followed by `f.bar()` call
- Verifies the reference resolves to `foo:bar`, not the alias `f:bar`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_dotted_import_attribute_access fingerprint=0665796fe22e5e64a9401028fa5d7cbeea7071c344232d40f0d907111701a0e7 body_fp=f2d03a9499c21beb37596b9874474fc505c9f103d30811f7bfde06ca6ad4cfad source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 role=source-parsing -->
## `def test_dotted_import_attribute_access(tmp_path: Path)`

Verifies that dotted imports like `import foo.bar` enable attribute access that resolves to correct qualified names with slash notation for nested modules.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_from_import_submodule_attribute_resolves fingerprint=a9288b10b5a0ce3cf43d26aff94d869565c99035ad41a67a8e2e9e758fa7bc2a body_fp=58563044d405079b5f4ce75c546444bfbd7b25727183b0bf56e4c134b7a73750 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 role=source-parsing -->
## `def test_from_import_submodule_attribute_resolves(tmp_path: Path)`

Tests that submodule attribute access from `from pkg import submod; submod.thing()` generates both bare symbol and module attribute reference candidates.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_module_attribute_emitted_even_for_stdlib fingerprint=f623eebef9d9e3d1d91d970bba554d84befea18cd3ef7203abc8d7bbf62bca27 body_fp=d2b6f1c5cfb99e7f5e35553d3709e8f2d8e71de232ec895093bcc149f1a281ea source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 role=source-parsing -->
## `def test_module_attribute_emitted_even_for_stdlib(tmp_path: Path)`

Verifies that module attribute access on stdlib imports emits candidate edges without special-casing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_mixed_from_and_plain_import fingerprint=7c85295591ddf8c3d91d011bf9f8a35ae696d5bd5f0bd8da85f8a51db484ea7f body_fp=dd84ca602ded9f6095cac20f3ca2df13f906f65981a7a693ff0fa754ce700b14 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 role=source-parsing -->
## `def test_mixed_from_and_plain_import(tmp_path: Path)`

Tests that both `from X import Y` and `import Z; Z.W()` patterns in one file generate their respective reference edges.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_attribute_access_through_local_var_not_treated_as_module fingerprint=6a5fe3c17b6c9346eb0735615bbdc763de2cb87c685d39a15963410fad068caa body_fp=b4a962c2330c5bf0d7bebd7caebb45a2460703e62307bd5435ff0987e0b9137a source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 role=source-parsing -->
## `def test_attribute_access_through_local_var_not_treated_as_module(tmp_path: Path)`

Verifies that attribute access on local variables does not create spurious module-attribute edges in reference extraction.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_module_attribute_no_self_edge fingerprint=33c0b251e18a1a4d26a6420f0b878d0abf794b7056b2139951eb33a3bc69dac7 body_fp=256c0a5a4072ceb04e21e262d9c81a04e15c94074139f7878dfb22724a8f69f1 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 role=source-parsing -->
## `def test_module_attribute_no_self_edge(tmp_path: Path)`

Verifies that a function referencing itself via module attribute access does not create a self-edge in the reference graph.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_function_local_import_creates_edge fingerprint=a232ab954e3520c4556725e43c94bfa37a34c1b8bbd10b59aa17d4007fa3cf3e body_fp=e80f323f8eacc6ec610d96a518229307b5324822e072c3e84c9e6e2647470e79 source_ref=f8938b1ad034eede593979934b3db06bbce8988f role=test -->
## `def test_function_local_import_creates_edge(tmp_path: Path)`

Assert that a `from x import y` statement inside a function body still produces a reference edge to the imported symbol.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_import_nested_in_conditional_creates_edge fingerprint=7313287cc577e4b20653e5bba3e336db0057a693e832d6dcf8b3ed2243f3fb92 body_fp=e5e818fa355e581df82149ea982a12daf09433cc3756a501780e57fdb9694c40 source_ref=f8938b1ad034eede593979934b3db06bbce8988f role=test -->
## `def test_import_nested_in_conditional_creates_edge(tmp_path: Path)`

Assert that imports nested inside `if`/`try` blocks (e.g. `TYPE_CHECKING` guards) still bind names and produce reference edges.
<!-- trie:end -->