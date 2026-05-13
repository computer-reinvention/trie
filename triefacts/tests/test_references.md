---
trie_version: 0.1.0
source: tests/test_references.py
file_fingerprint: 2b01e257de07718395a919313d217588b435ab25aa9d02bef561f555f8b9bcda
last_synced_at: '2026-05-12T18:28:57Z'
defines:
- kind: function
  qualified_name: tests/test_references:test_intra_file_function_calls_create_edges
  lines: 16-26
- kind: function
  qualified_name: tests/test_references:test_intra_file_class_to_function_edge
  lines: 29-36
- kind: function
  qualified_name: tests/test_references:test_imports_create_cross_file_edges
  lines: 39-47
- kind: function
  qualified_name: tests/test_references:test_aliased_import_resolves_to_original
  lines: 50-55
- kind: function
  qualified_name: tests/test_references:test_dotted_module_import
  lines: 58-63
- kind: function
  qualified_name: tests/test_references:test_relative_imports_skipped
  lines: 66-74
- kind: function
  qualified_name: tests/test_references:test_no_self_references
  lines: 77-85
- kind: function
  qualified_name: tests/test_references:test_unresolved_names_silently_dropped
  lines: 88-94
- kind: function
  qualified_name: tests/test_references:test_class_methods_inherit_class_qname_in_src
  lines: 97-105
- kind: function
  qualified_name: tests/test_references:test_extract_file_data_includes_symbols
  lines: 108-113
- kind: function
  qualified_name: tests/test_references:test_confidence_labels_are_distinguishable
  lines: 116-126
incoming_refs: 0
outgoing_refs: 11
---
<!-- trie:section symbol=tests/test_references:test_intra_file_function_calls_create_edges fingerprint=f59ed7b0886dada67f2106498921a398c3ef4d7b0dabcf68629f2e9682a8866c body_fp=081f23272c512af4d4aea2849e881aed89fdccceb76a5bce5fc99b30cf0f191d -->
## `test_intra_file_function_calls_create_edges(tmp_path: Path)`

Assert that intra-file function calls produce deduplicated reference edges between qualified names.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:test_intra_file_class_to_function_edge fingerprint=adcdb1040d5e3e90cdab10fd997a7fe730601dfc1212cc4dc872313fc16da8e1 body_fp=7959068d771aa7d7c0e92e35d0240c0c768e8b39eee7b2beaaece3a9e3702360 -->
## `test_intra_file_class_to_function_edge(tmp_path: Path)`

Verify that a class method calling a module-level function produces a reference edge from `ClassName.method` to the function.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:test_imports_create_cross_file_edges fingerprint=95a6d159066317cadbe60cf46cb8b8b35cbc0ed0540d9a306017c4e07c5ff737 body_fp=c4648e4892b9ab3aa46d651bc1cb40864cd7870d2cb42ab3c3e775867b759a93 -->
## `test_imports_create_cross_file_edges(tmp_path: Path)`

Verify that an imported name used inside a function produces a cross-file reference edge with `confidence == "tree_sitter_import"`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:test_aliased_import_resolves_to_original fingerprint=03c21101344781b8aff3ba8df3898b34ead9ffe3d5c5f248e9d95c8bba9042b2 body_fp=2af1a9fdd94ff479237f1752f47e0901e2a5da44489d610b3025333e49413cdc -->
## `test_aliased_import_resolves_to_original(tmp_path: Path)`

Verify that an aliased import (`from helpers import helper as h`) resolves to the original qualified name `helpers:helper`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:test_dotted_module_import fingerprint=a669dbba4d5f289f095822c5fdaa1aeb35019ddd4136e96fdcd6976913ab5c34 body_fp=20800f7d481219f9968c46abe39f9ca0d335010c135e2e8a3ce3af9517151319 -->
## `test_dotted_module_import(tmp_path: Path)`

Verify that a `from foo.bar import baz` import resolves `baz` calls to the qualified target `foo/bar:baz`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:test_relative_imports_skipped fingerprint=a932a8034d6ca1b3fda32e58fc083098dfabcdee9a0784e23f448b51e3573a33 body_fp=ae89ba92349527537bb8707b2c493c096da8b55fb71e7e20d9a32b97049d0cb8 -->
## `test_relative_imports_skipped(tmp_path: Path)`

Assert that relative imports produce no outbound edges from the calling function.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:test_no_self_references fingerprint=b40e3e9191a7a230558fd500e8d4191dcea1b1556d0d3b1fae1b17f881438199 body_fp=602877395777414e74b458c630d2a940865d2ec2b28bfcc0b74ebb46daeb8cea -->
## `test_no_self_references(tmp_path: Path)`

Assert that a directly recursive function produces no self-referencing edge in `extract_file_data` output.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:test_unresolved_names_silently_dropped fingerprint=6eaa0933d7f7b603204566b92e79d1dd51918c9819eab15dcc74dbe69d8048eb body_fp=88e078cea3cc873bb699601cc4b2053ebcbfeb52e6532600ab6682031944ea52 -->
## `test_unresolved_names_silently_dropped(tmp_path: Path)`

Assert that calls to unimported, non-local names produce no reference edges.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:test_class_methods_inherit_class_qname_in_src fingerprint=27656fb38d31ffb0baaaa90f4a3d536791e132132f1dc6f54d4520a4f4563830 body_fp=d0a9dc65df22b830384e6e47bc4443c571014d3e83fa787eb4fedd0b258f2bbd -->
## `test_class_methods_inherit_class_qname_in_src(tmp_path: Path)`

Assert that a method's `src_qname` uses the `ClassName.method` dotted form.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:test_extract_file_data_includes_symbols fingerprint=a9dd60ee72bd3fda7c5c8c7f7afcfb096f2df081102db374bf41c0e7bffd2fc4 body_fp=21ae5eeb20904768ee06a4d0953dde46a71f2d67d18f965b4840df3b3c7c8b6b -->
## `test_extract_file_data_includes_symbols(tmp_path: Path)`

Verify that `extract_file_data` populates `fd.symbols` with correct qualified names for all top-level functions.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_references:test_confidence_labels_are_distinguishable fingerprint=7bd056ef1de0e48e6c1d8c79890a6d73ea8611eaa3dc3292ebdb3833fd31a5b7 body_fp=543644aa16fe22faf2436cb3999e3cd393b2f44d3f8c71fca0fd07e3e78b26c1 -->
## `test_confidence_labels_are_distinguishable(tmp_path: Path)`

Verify that import-derived edges carry `"tree_sitter_import"` confidence and intra-file edges carry `"name_match"`.
<!-- trie:end -->