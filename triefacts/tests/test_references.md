---
trie_version: 0.1.2
source: tests/test_references.py
file_fingerprint: 2fdf44916f20a130ea326a24211998cb1e4938e538a0ba45d36ee96cd481d6a7
last_synced_at: '2026-05-23T23:50:00Z'
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
<!-- trie:section symbol=tests/test_references:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=ca545c3e009e43a0fa0aab5d0a905488c212a74be57d980a570b2bb730b15e6d source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
## `tests/test_references`

Integration tests for `extract_file_data` reference extraction, covering intra-file, cross-file, import alias, and module-attribute resolution edge cases.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:_refs_by_src fingerprint=9008a0d0cd30929c25a818e62440a5015ef19e44627b3d4e097d9be3eba52021 body_fp=87d5d283f650cd217e0a78762c3b1bff0da39c343318fa97df21da8d893b0bf9 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
## `_refs_by_src(file_data) -> dict[str, list[str]]`

Build a mapping from each `src_qname` to a sorted list of its `target_qname`s from a `FileData` object.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_intra_file_function_calls_create_edges fingerprint=f59ed7b0886dada67f2106498921a398c3ef4d7b0dabcf68629f2e9682a8866c body_fp=c515e6109a6c7b14caaead81af10ad87dffbf42fb25ba18e6c40f5d1221ce43c source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
## `test_intra_file_function_calls_create_edges(tmp_path: Path)`

Verify that intra-file function calls produce deduplicated reference edges between qualified names.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_intra_file_class_to_function_edge fingerprint=adcdb1040d5e3e90cdab10fd997a7fe730601dfc1212cc4dc872313fc16da8e1 body_fp=bb8d843c59db2f3cddc4da3d62a10386409252bfa9719a959feaa34bdea8bc82 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
## `test_intra_file_class_to_function_edge(tmp_path: Path)`

Verify that a class method calling a module-level function produces an intra-file reference edge.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_imports_create_cross_file_edges fingerprint=03c21101344781b8aff3ba8df3898b34ead9ffe3d5c5f248e9d95c8bba9042b2 body_fp=4cd337b44a0138da87051628da667a4fc552d20266f0ce9b24898fd87c33a1bb source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
## `test_imports_create_cross_file_edges(tmp_path: Path)`

Assert that a `from helpers import helper` statement produces a `mod:run` → `helpers:helper` reference edge.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_aliased_import_resolves_to_original fingerprint=03c21101344781b8aff3ba8df3898b34ead9ffe3d5c5f248e9d95c8bba9042b2 body_fp=e5fa6565db5fdc7a7be8de2c569ebc951f11825ce5c41d1ddfb51409a3dd5f3e source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
## `test_aliased_import_resolves_to_original(tmp_path: Path)`

Verify that an aliased `from X import Y as Z` import resolves the alias back to the original qualified name.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_dotted_module_import fingerprint=a669dbba4d5f289f095822c5fdaa1aeb35019ddd4136e96fdcd6976913ab5c34 body_fp=a231145adc960081559641837498f9d042d3ac0ea42c3dc8af626a22b95a950a source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
## `test_dotted_module_import(tmp_path: Path)`

Assert that `from foo.bar import baz` resolves the target qname to `foo/bar:baz`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_relative_imports_skipped fingerprint=a932a8034d6ca1b3fda32e58fc083098dfabcdee9a0784e23f448b51e3573a33 body_fp=5c0d60a75e848158823a0fd09370e4f99cfa47d76262535fffd912e0271cd4a1 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
## `test_relative_imports_skipped(tmp_path: Path)`

Assert that relative imports produce no reference edges from the calling symbol.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_no_self_references fingerprint=b40e3e9191a7a230558fd500e8d4191dcea1b1556d0d3b1fae1b17f881438199 body_fp=31f4ae1b6bf7e79b17400ab100af4b84b9f5060d8e2b0579c68d1424f992afe9 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
## `test_no_self_references(tmp_path: Path)`

Assert that a directly recursive function produces no self-referential edge in `extract_file_data` output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_unresolved_names_silently_dropped fingerprint=6eaa0933d7f7b603204566b92e79d1dd51918c9819eab15dcc74dbe69d8048eb body_fp=9aa4f1bc80b58b187b9959617d85b5bc3972f8d7c792875ede1fda5b8044bf1d source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
## `test_unresolved_names_silently_dropped(tmp_path: Path)`

Assert that names neither imported nor defined locally produce no reference edges.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_class_methods_inherit_class_qname_in_src fingerprint=27656fb38d31ffb0baaaa90f4a3d536791e132132f1dc6f54d4520a4f4563830 body_fp=a3adc3e44bd95aeed39e2933e87a7ce1142ab17fb710e5108d0af9e279c87a55 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
## `test_class_methods_inherit_class_qname_in_src(tmp_path: Path)`

Assert that references from a class method use the `ClassName.method` qualified name as `src_qname`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_extract_file_data_includes_symbols fingerprint=a9dd60ee72bd3fda7c5c8c7f7afcfb096f2df081102db374bf41c0e7bffd2fc4 body_fp=b57c7644d625a6ad34a0c340eb50799144d290a771d34f8e7c81f33a6e3aef1b source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
## `test_extract_file_data_includes_symbols(tmp_path: Path)`

Verify that `extract_file_data` populates `FileData.symbols` with the correct qualified names for all top-level functions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_both_import_and_intra_file_edges_resolve fingerprint=c43fc568966bf2fdbaaf95b67a808d17ad4abc1e688e7df6846e7d7d8e4f4081 body_fp=330a38aede9ae8aae0d015acb7e0b085e6089289540bda6a558fffa5e368d998 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
## `test_both_import_and_intra_file_edges_resolve(tmp_path: Path)`

Verify that a single caller resolves both cross-file import edges and intra-file name edges simultaneously.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_plain_import_attribute_access fingerprint=9db43c1bc6facc99a0f5bd980f2976af5d303a71998ea31d579ad82b44395c7f body_fp=72c931e96cd4edc65b53bdb425798dcc5f827020be3e53c073a0a144b54248f0 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
## `test_plain_import_attribute_access(tmp_path: Path)`

Assert that `import foo` followed by `foo.bar()` produces a reference edge targeting `foo:bar`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_aliased_plain_import_attribute_access fingerprint=8f322e134ab11d36dc9413ddd7c8458cddc834ff56fe7034b931f13e2364b653 body_fp=1392565bc4a22f496226e8aa39a003f966a78198199e3aaef45ec663d9dfb001 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
## `test_aliased_plain_import_attribute_access(tmp_path: Path)`

Assert that `import foo as f; f.bar()` resolves the reference target to `foo:bar`, not `f:bar`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_dotted_import_attribute_access fingerprint=0665796fe22e5e64a9401028fa5d7cbeea7071c344232d40f0d907111701a0e7 body_fp=630eb03ed2fb89b252cf56f52dc06976b0e3d0f343c60f33f83884857b4ad741 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
## `test_dotted_import_attribute_access(tmp_path: Path)`

Verify that `import foo.bar` followed by `foo.bar.baz()` resolves to the target qname `foo/bar:baz`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_from_import_submodule_attribute_resolves fingerprint=a9288b10b5a0ce3cf43d26aff94d869565c99035ad41a67a8e2e9e758fa7bc2a body_fp=0e72d315bf075c18d26f67a3f4217d45106756f12e1144ca1e460deb6b0c2086 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
## `test_from_import_submodule_attribute_resolves(tmp_path: Path)`

Assert that `from pkg import submod; submod.thing()` emits both `pkg:submod` and `pkg/submod:thing` as candidate reference targets.

- Both edges emitted; store's existence filter selects the real one at query time.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_module_attribute_emitted_even_for_stdlib fingerprint=f623eebef9d9e3d1d91d970bba554d84befea18cd3ef7203abc8d7bbf62bca27 body_fp=21a9d5c912f9fbccc183ccb541719e9b5ed3f38255ff87b58ab02f5d1e3d56b9 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
## `test_module_attribute_emitted_even_for_stdlib(tmp_path: Path)`

Assert that `extract_file_data` emits candidate module-attribute edges for stdlib imports without filtering at extraction time.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_mixed_from_and_plain_import fingerprint=7c85295591ddf8c3d91d011bf9f8a35ae696d5bd5f0bd8da85f8a51db484ea7f body_fp=87cde747f46b895b089bb76ec45d8c85c3b9981c4481799611a53f48957f9bea source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
## `test_mixed_from_and_plain_import(tmp_path: Path)`

Assert that `from X import Y` and `import Z; Z.W()` in the same file both produce reference edges.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_attribute_access_through_local_var_not_treated_as_module fingerprint=6a5fe3c17b6c9346eb0735615bbdc763de2cb87c685d39a15963410fad068caa body_fp=532058fbfff71b9142d0ef3b23281d822fdf9002056c5a4743d81ce0c21162a6 source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
## `test_attribute_access_through_local_var_not_treated_as_module(tmp_path: Path)`

Assert that attribute access on a local variable emits no module-attribute edge, only the intra-file call edge.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_references:test_module_attribute_no_self_edge fingerprint=33c0b251e18a1a4d26a6420f0b878d0abf794b7056b2139951eb33a3bc69dac7 body_fp=cc03bd29acc437e9d672e282a6ca148f585b6697d96ae0c92705e0a81e7a162c source_ref=cfc6a4f3993d1a1359e67c4f055e983eff884192 -->
## `test_module_attribute_no_self_edge(tmp_path: Path)`

Assert that a symbol accessing itself via module-attribute notation produces no self-edge in extracted references.
<!-- trie:end -->