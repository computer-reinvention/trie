---
trie_version: 0.1.5
source: tests/test_references.py
file_fingerprint: 2fdf44916f20a130ea326a24211998cb1e4938e538a0ba45d36ee96cd481d6a7
last_synced_at: '2026-06-03T20:59:38Z'
defines:
- kind: module
  qualified_name: tests/test_references:__module__
  lines: 1-234
- kind: function
  qualified_name: tests/test_references:_refs_by_src
  lines: 8-13
- kind: function
  qualified_name: tests/test_references:test_intra_file_function_calls_create_edges
  lines: 16-26
- kind: function
  qualified_name: tests/test_references:test_intra_file_class_to_function_edge
  lines: 29-36
- kind: function
  qualified_name: tests/test_references:test_imports_create_cross_file_edges
  lines: 39-44
- kind: function
  qualified_name: tests/test_references:test_aliased_import_resolves_to_original
  lines: 47-52
- kind: function
  qualified_name: tests/test_references:test_dotted_module_import
  lines: 55-60
- kind: function
  qualified_name: tests/test_references:test_relative_imports_skipped
  lines: 63-71
- kind: function
  qualified_name: tests/test_references:test_no_self_references
  lines: 74-82
- kind: function
  qualified_name: tests/test_references:test_unresolved_names_silently_dropped
  lines: 85-91
- kind: function
  qualified_name: tests/test_references:test_class_methods_inherit_class_qname_in_src
  lines: 94-102
- kind: function
  qualified_name: tests/test_references:test_extract_file_data_includes_symbols
  lines: 105-110
- kind: function
  qualified_name: tests/test_references:test_both_import_and_intra_file_edges_resolve
  lines: 113-123
- kind: function
  qualified_name: tests/test_references:test_plain_import_attribute_access
  lines: 131-137
- kind: function
  qualified_name: tests/test_references:test_aliased_plain_import_attribute_access
  lines: 140-147
- kind: function
  qualified_name: tests/test_references:test_dotted_import_attribute_access
  lines: 150-160
- kind: function
  qualified_name: tests/test_references:test_from_import_submodule_attribute_resolves
  lines: 163-175
- kind: function
  qualified_name: tests/test_references:test_module_attribute_emitted_even_for_stdlib
  lines: 178-189
- kind: function
  qualified_name: tests/test_references:test_mixed_from_and_plain_import
  lines: 192-204
- kind: function
  qualified_name: tests/test_references:test_attribute_access_through_local_var_not_treated_as_module
  lines: 207-219
- kind: function
  qualified_name: tests/test_references:test_module_attribute_no_self_edge
  lines: 222-233
incoming_refs: 0
outgoing_refs: 19
---
<!-- trie:section symbol=tests/test_references:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=d05f7a619001e77a71db28d519558a058d7cdd1a63f5e2942ccaf592eb2f5256 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
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
<!-- trie:section symbol=tests/test_references:_refs_by_src fingerprint=9008a0d0cd30929c25a818e62440a5015ef19e44627b3d4e097d9be3eba52021 body_fp=18714f42b56df65c8b67b3c4add22650173698808720f90a6c0301b6018c7280 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
Converts file_data references into a dictionary mapping source qualified names to sorted lists of target qualified names.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_intra_file_function_calls_create_edges fingerprint=f59ed7b0886dada67f2106498921a398c3ef4d7b0dabcf68629f2e9682a8866c body_fp=07bbb7710381aad7cadec75e6619bdd7e93404e4f3436034a7b5bd56e2b71dbe source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
Tests that function calls within the same file create reference edges and duplicate calls are deduplicated.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_intra_file_class_to_function_edge fingerprint=adcdb1040d5e3e90cdab10fd997a7fe730601dfc1212cc4dc872313fc16da8e1 body_fp=4b82a1d21e9e123854aa0f42d33c6d6fbf553d7e2eb94e1d0dc3addff0f0816f source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
Verifies that a method calling a function in the same file creates a reference edge from method to function.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_imports_create_cross_file_edges fingerprint=03c21101344781b8aff3ba8df3898b34ead9ffe3d5c5f248e9d95c8bba9042b2 body_fp=d0065ec03415bc89a9ef5ce1b398223223381b76b6bda65966a17610ce343980 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
Verifies that importing a function from another module creates cross-file reference edges when that function is called.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_aliased_import_resolves_to_original fingerprint=03c21101344781b8aff3ba8df3898b34ead9ffe3d5c5f248e9d95c8bba9042b2 body_fp=9ab8dadd05dfa776380ee0ba40a278d398da0ffa42216ce0724d53ecf6ff21da source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
Verifies that import aliases resolve to their original qualified names, not the alias names.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_dotted_module_import fingerprint=a669dbba4d5f289f095822c5fdaa1aeb35019ddd4136e96fdcd6976913ab5c34 body_fp=830af44f7437d3c2e04763352cfb5efbde27d75152ba5148a79da0ac85b05d88 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
Verifies that importing from a dotted module path creates a reference with forward-slash-separated target qname.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_relative_imports_skipped fingerprint=a932a8034d6ca1b3fda32e58fc083098dfabcdee9a0784e23f448b51e3573a33 body_fp=479c78c035f0a298e76cea680b3d108abdf6482476ca785e6de946a0c0cf905d source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
Verifies that relative imports are ignored and do not create reference edges in the extracted file data.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_no_self_references fingerprint=b40e3e9191a7a230558fd500e8d4191dcea1b1556d0d3b1fae1b17f881438199 body_fp=5c63fad559b60fecee5e30bc246a81b56c01f580072390e520f9f8143a4c10e3 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
Verifies that recursive function calls do not create self-referencing edges in the extracted references.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_unresolved_names_silently_dropped fingerprint=6eaa0933d7f7b603204566b92e79d1dd51918c9819eab15dcc74dbe69d8048eb body_fp=872f7951bfc415024b0021f5bd2ef93388d079514e90e1e5de2cf3e4a171a2e1 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
Tests that unresolved function names produce no reference edges in the extracted file data.

• Creates test module with calls to undefined `some_global` and builtin `len`
• Verifies no spurious references are generated for unresolvable symbols
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_class_methods_inherit_class_qname_in_src fingerprint=27656fb38d31ffb0baaaa90f4a3d536791e132132f1dc6f54d4520a4f4563830 body_fp=4d3713cf6ed583f16ec720ca08f9fc1768cda2174a314c2b70110ba90397a86b source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
Verifies that class method references include the full qualified name with class prefix in src_qname.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_extract_file_data_includes_symbols fingerprint=a9dd60ee72bd3fda7c5c8c7f7afcfb096f2df081102db374bf41c0e7bffd2fc4 body_fp=11536cc2689af619d86ce9ab1aefb8d335afbf17c9d7d146f88ae13591b1b16f source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
Verifies that `extract_file_data` correctly identifies and returns all symbols defined in a Python file with their qualified names.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_both_import_and_intra_file_edges_resolve fingerprint=c43fc568966bf2fdbaaf95b67a808d17ad4abc1e688e7df6846e7d7d8e4f4081 body_fp=e57bbc33b27096b46a339926c157ebe9d28a8487f5172b2f27af54c733eca103 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
Verifies that `extract_file_data` correctly identifies both cross-file import references and intra-file function call references from the same source symbol.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_plain_import_attribute_access fingerprint=9db43c1bc6facc99a0f5bd980f2976af5d303a71998ea31d579ad82b44395c7f body_fp=0930b98ed48426247c396ab26018dc8000eb03def02f5ad6cd02ac9f497fcd7f source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
Verifies that `import foo` followed by `foo.bar()` creates a reference to `foo:bar`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_aliased_plain_import_attribute_access fingerprint=8f322e134ab11d36dc9413ddd7c8458cddc834ff56fe7034b931f13e2364b653 body_fp=4fc0031fc754ab492c628ffedda9182116f1047978399d5c05bc4457dc9394f3 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
Tests that aliased module imports resolve attribute access to the original module name.

- Creates code with `import foo as f` followed by `f.bar()` call
- Verifies the reference resolves to `foo:bar`, not the alias `f:bar`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_dotted_import_attribute_access fingerprint=0665796fe22e5e64a9401028fa5d7cbeea7071c344232d40f0d907111701a0e7 body_fp=a6664f712c2350bc1f6efbf79b5b628fa52c1deb9a2fd3f48da15f6ffe4fd6bf source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
Verifies that dotted imports like `import foo.bar` enable attribute access that resolves to correct qualified names with slash notation for nested modules.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_from_import_submodule_attribute_resolves fingerprint=a9288b10b5a0ce3cf43d26aff94d869565c99035ad41a67a8e2e9e758fa7bc2a body_fp=b44d0efa712f312db6bcaf6346bed3e61c53405b63d18012733649f95239da2c source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
Tests that submodule attribute access from `from pkg import submod; submod.thing()` generates both bare symbol and module attribute reference candidates.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_module_attribute_emitted_even_for_stdlib fingerprint=f623eebef9d9e3d1d91d970bba554d84befea18cd3ef7203abc8d7bbf62bca27 body_fp=03060fcb0b12bd2a880d294947a2a4431c87a505f9b6cf83d1b4b3e53846f373 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
Verifies that module attribute access on stdlib imports emits candidate edges without special-casing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_mixed_from_and_plain_import fingerprint=7c85295591ddf8c3d91d011bf9f8a35ae696d5bd5f0bd8da85f8a51db484ea7f body_fp=07dc2a4972ad71d4daf3dc182428f28296602494832a386b778e25350a6314a0 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
Tests that both `from X import Y` and `import Z; Z.W()` patterns in one file generate their respective reference edges.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_attribute_access_through_local_var_not_treated_as_module fingerprint=6a5fe3c17b6c9346eb0735615bbdc763de2cb87c685d39a15963410fad068caa body_fp=919de643fd49c099bed5ec4a5d4cc58da1d609f68096c7ebe256952e054a591d source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
Verifies that attribute access on local variables does not create spurious module-attribute edges in reference extraction.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_module_attribute_no_self_edge fingerprint=33c0b251e18a1a4d26a6420f0b878d0abf794b7056b2139951eb33a3bc69dac7 body_fp=cf087222731f51db630cb8d43f7c97a4b64b4385ea25a86b8a2c6284e249cd0e source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
Verifies that a function referencing itself via module attribute access does not create a self-edge in the reference graph.
<!-- trie:end -->