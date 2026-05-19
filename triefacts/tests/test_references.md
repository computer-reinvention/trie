---
trie_version: 0.1.2
source: tests/test_references.py
file_fingerprint: 24aa3c08899578f0fe7321610c519c21a0aaf6e5fe2a018b478f8685b94afa06
last_synced_at: '2026-05-19T10:38:54Z'
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
<!-- trie:section symbol=tests/test_references:test_intra_file_function_calls_create_edges fingerprint=f59ed7b0886dada67f2106498921a398c3ef4d7b0dabcf68629f2e9682a8866c body_fp=081f23272c512af4d4aea2849e881aed89fdccceb76a5bce5fc99b30cf0f191d source_ref=83e454d8231cd6f64c4000e41597feef296bf20c -->
## `test_intra_file_function_calls_create_edges(tmp_path: Path)`

Assert that intra-file function calls produce deduplicated reference edges between qualified names.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:test_intra_file_class_to_function_edge fingerprint=adcdb1040d5e3e90cdab10fd997a7fe730601dfc1212cc4dc872313fc16da8e1 body_fp=c2b3134d4b2341afee4b7c38eb8e6d78496f5d0b09a7a989e0616327ffa0c116 source_ref=83e454d8231cd6f64c4000e41597feef296bf20c -->
## `test_intra_file_class_to_function_edge(tmp_path: Path)`

Assert that a method calling a module-level function produces a `ClassName.method -> function` reference edge.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:test_imports_create_cross_file_edges fingerprint=03c21101344781b8aff3ba8df3898b34ead9ffe3d5c5f248e9d95c8bba9042b2 body_fp=091d98bd52f9a69c0f6c8d71235f511a0295789bf351162a99694f6bbf9de570 source_ref=83e454d8231cd6f64c4000e41597feef296bf20c -->
## `test_imports_create_cross_file_edges(tmp_path: Path)`

Assert that a `from module import name` statement produces a cross-file reference edge in extracted file data.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:test_aliased_import_resolves_to_original fingerprint=03c21101344781b8aff3ba8df3898b34ead9ffe3d5c5f248e9d95c8bba9042b2 body_fp=58e92a2636114e8600119e09e6dc75e5ff06d103db15c787829c4687a400406f source_ref=83e454d8231cd6f64c4000e41597feef296bf20c -->
## `test_aliased_import_resolves_to_original(tmp_path: Path)`

Verify that an aliased import (`from helpers import helper as h`) resolves edges to the original qualified name `helpers:helper`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:test_dotted_module_import fingerprint=a669dbba4d5f289f095822c5fdaa1aeb35019ddd4136e96fdcd6976913ab5c34 body_fp=1378768780bf718de0b3ca04b611ed742b6969e2eb974293ea8b8e82d51b69b1 source_ref=83e454d8231cd6f64c4000e41597feef296bf20c -->
## `test_dotted_module_import(tmp_path: Path)`

Verify that a `from foo.bar import baz` statement resolves to the target qname `foo/bar:baz`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:test_relative_imports_skipped fingerprint=a932a8034d6ca1b3fda32e58fc083098dfabcdee9a0784e23f448b51e3573a33 body_fp=7cd77ddaa30521ed6cbb34325cfae66de4cec2a03ca5fef45e2a1c5ab0d1671d source_ref=83e454d8231cd6f64c4000e41597feef296bf20c -->
## `test_relative_imports_skipped(tmp_path: Path)`

Assert that relative imports produce no reference edges in the extracted file data.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:test_no_self_references fingerprint=b40e3e9191a7a230558fd500e8d4191dcea1b1556d0d3b1fae1b17f881438199 body_fp=758129d51374781d892ef63e7cee2767955f9b7a575e5f83a259feccbbe940c8 source_ref=83e454d8231cd6f64c4000e41597feef296bf20c -->
## `test_no_self_references(tmp_path: Path)`

Assert that a directly recursive function produces no self-referencing edge in `fd.references`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:test_unresolved_names_silently_dropped fingerprint=6eaa0933d7f7b603204566b92e79d1dd51918c9819eab15dcc74dbe69d8048eb body_fp=88e078cea3cc873bb699601cc4b2053ebcbfeb52e6532600ab6682031944ea52 source_ref=83e454d8231cd6f64c4000e41597feef296bf20c -->
## `test_unresolved_names_silently_dropped(tmp_path: Path)`

Assert that calls to unimported, non-local names produce no reference edges.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:test_class_methods_inherit_class_qname_in_src fingerprint=27656fb38d31ffb0baaaa90f4a3d536791e132132f1dc6f54d4520a4f4563830 body_fp=3cb8ac6babcda196e5809b47a1b26053a508fec2d18d377cd7f4d11477d02071 source_ref=83e454d8231cd6f64c4000e41597feef296bf20c -->
## `test_class_methods_inherit_class_qname_in_src(tmp_path: Path)`

Assert that references from a method use the `ClassName.method` qualified name as `src_qname`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:test_extract_file_data_includes_symbols fingerprint=a9dd60ee72bd3fda7c5c8c7f7afcfb096f2df081102db374bf41c0e7bffd2fc4 body_fp=b3c717cacbfacbfd85a830328e63a486a4067d19b1a38fe94c7f832d0a540a89 source_ref=83e454d8231cd6f64c4000e41597feef296bf20c -->
## `test_extract_file_data_includes_symbols(tmp_path: Path)`

Verify that `extract_file_data` populates `fd.symbols` with the correct qualified names for all top-level functions.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:test_both_import_and_intra_file_edges_resolve fingerprint=c43fc568966bf2fdbaaf95b67a808d17ad4abc1e688e7df6846e7d7d8e4f4081 body_fp=8d5fe1266f641a26a7a28252fec7c8e74f852a1b11cc8773ea254035b83d34ac source_ref=83e454d8231cd6f64c4000e41597feef296bf20c -->
## `test_both_import_and_intra_file_edges_resolve(tmp_path: Path)`

Verify that a single caller resolves both cross-file import edges and intra-file local edges simultaneously.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:_refs_by_src fingerprint=9008a0d0cd30929c25a818e62440a5015ef19e44627b3d4e097d9be3eba52021 body_fp=8aa5f61d3ed45382fcf0f8b04f2bb3d917280d60d70d90376764dd08ca34f67a source_ref=83e454d8231cd6f64c4000e41597feef296bf20c -->
## `_refs_by_src(file_data) -> dict[str, list[str]]`

Build a mapping from each source qualified name to a sorted list of its target qualified names.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:test_plain_import_attribute_access fingerprint=9db43c1bc6facc99a0f5bd980f2976af5d303a71998ea31d579ad82b44395c7f body_fp=54628f041e2bcfac0462cc4313d46f149c0e2f44761679ae455829d07288c843 source_ref=5a91a8c60b5e6b0f8348157ccb0c571d36a3d8a6 -->
## `test_plain_import_attribute_access(tmp_path: Path)`

Assert that `import foo` followed by `foo.bar()` resolves to a `foo:bar` reference edge.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:test_aliased_plain_import_attribute_access fingerprint=8f322e134ab11d36dc9413ddd7c8458cddc834ff56fe7034b931f13e2364b653 body_fp=1392565bc4a22f496226e8aa39a003f966a78198199e3aaef45ec663d9dfb001 source_ref=5a91a8c60b5e6b0f8348157ccb0c571d36a3d8a6 -->
## `test_aliased_plain_import_attribute_access(tmp_path: Path)`

Assert that `import foo as f; f.bar()` resolves the reference target to `foo:bar`, not `f:bar`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:test_dotted_import_attribute_access fingerprint=0665796fe22e5e64a9401028fa5d7cbeea7071c344232d40f0d907111701a0e7 body_fp=b139609ecea3b70a13ccb4101d261b4769777a0490a5c10475adb0ad0cb96d50 source_ref=5a91a8c60b5e6b0f8348157ccb0c571d36a3d8a6 -->
## `test_dotted_import_attribute_access(tmp_path: Path)`

Assert that `import foo.bar` followed by `foo.bar.baz()` resolves to the target qname `foo/bar:baz`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:test_from_import_submodule_attribute_resolves fingerprint=4779064a355c55a1b4e3262f650c10a0b45cdb543b6373f1358902ce134755fe body_fp=17ff51e48a4e33a298795064a99678502582dacbeda3840e0e00b0fae5029b30 source_ref=5a91a8c60b5e6b0f8348157ccb0c571d36a3d8a6 -->
## `test_from_import_submodule_attribute_resolves(tmp_path: Path)`

Assert that `from pkg import submod; submod.thing()` emits both bare-symbol and module-attribute candidate edges.

- `"pkg:submod"` — bare-name interpretation, as if `submod` is a symbol in `pkg`
- `"pkg/submod:thing"` — module-attribute interpretation for `submod.thing()`
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:test_module_attribute_emitted_even_for_stdlib fingerprint=f623eebef9d9e3d1d91d970bba554d84befea18cd3ef7203abc8d7bbf62bca27 body_fp=2f6d6538d6ec59f87d676515f22b5fe4e9c381e32d62f99918fb54484a7580e5 source_ref=5a91a8c60b5e6b0f8348157ccb0c571d36a3d8a6 -->
## `test_module_attribute_emitted_even_for_stdlib(tmp_path: Path)`

Assert that `import os; os.path.join(...)` emits a candidate reference edge without stdlib filtering at extraction time.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:test_mixed_from_and_plain_import fingerprint=7c85295591ddf8c3d91d011bf9f8a35ae696d5bd5f0bd8da85f8a51db484ea7f body_fp=42ce2b3ee7391da3f97ccf73a997d05b8de4cd89c63c1b44d29d0a4b536b5100 source_ref=5a91a8c60b5e6b0f8348157ccb0c571d36a3d8a6 -->
## `test_mixed_from_and_plain_import(tmp_path: Path)`

Assert that combining `from X import Y` and `import Z; Z.W()` in one file produces edges from both resolution paths.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:test_attribute_access_through_local_var_not_treated_as_module fingerprint=6a5fe3c17b6c9346eb0735615bbdc763de2cb87c685d39a15963410fad068caa body_fp=532058fbfff71b9142d0ef3b23281d822fdf9002056c5a4743d81ce0c21162a6 source_ref=5a91a8c60b5e6b0f8348157ccb0c571d36a3d8a6 -->
## `test_attribute_access_through_local_var_not_treated_as_module(tmp_path: Path)`

Assert that attribute access on a local variable emits no module-attribute edge, only the intra-file call edge.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:test_module_attribute_no_self_edge fingerprint=33c0b251e18a1a4d26a6420f0b878d0abf794b7056b2139951eb33a3bc69dac7 body_fp=49685159c1cde42dfc224b119e7bb6b808bc49d35badc1df076ae82ef4d67b26 source_ref=5a91a8c60b5e6b0f8348157ccb0c571d36a3d8a6 -->
## `test_module_attribute_no_self_edge(tmp_path: Path)`

Assert that a symbol referencing itself via module-attribute access does not produce a self-edge.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=6a8a5ccb9b8672de47576950bfeb889d390303432955d842c6470d85948620d1 source_ref=5a91a8c60b5e6b0f8348157ccb0c571d36a3d8a6 -->
## `tests/test_references`

Test suite for `extract_file_data` reference extraction, covering intra-file calls, imports, aliasing, attribute access, and self-edge suppression.
<!-- trie:end -->