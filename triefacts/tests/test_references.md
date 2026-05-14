---
trie_version: 0.1.0
source: tests/test_references.py
file_fingerprint: 57b5f2c5ed4a13fefd04ad9cda47ab3013f6ffdbda1ba0c08c6bd20fe2eefdb3
last_synced_at: '2026-05-14T17:26:32Z'
defines:
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
incoming_refs: 0
outgoing_refs: 11
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