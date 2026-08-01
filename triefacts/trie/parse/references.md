---
trie_version: 0.2.1
source: trie/parse/references.py
file_fingerprint: f269fe349d38cba12b56c6c73cc63ef99f3e1c77d5092b947736b5951f264e85
last_synced_at: '2026-08-01T00:20:38Z'
description: Reference extraction via tree-sitter.
defines:
- kind: module
  qualified_name: trie/parse/references:__module__
  lines: 1-474
- kind: class
  qualified_name: trie/parse/references:_ImportBindings
  lines: 56-74
- kind: function
  qualified_name: trie/parse/references:_collect_imports
  lines: 77-118
- kind: function
  qualified_name: trie/parse/references:_absorb_from_import
  lines: 121-162
- kind: function
  qualified_name: trie/parse/references:_absorb_plain_import
  lines: 165-192
- kind: function
  qualified_name: trie/parse/references:_collect_identifier_names
  lines: 195-213
- kind: function
  qualified_name: trie/parse/references:_collect_attribute_accesses
  lines: 216-254
- kind: function
  qualified_name: trie/parse/references:_dotted_text
  lines: 257-275
- kind: function
  qualified_name: trie/parse/references:_collect_call_target_names
  lines: 278-305
- kind: function
  qualified_name: trie/parse/references:_collect_class_bases
  lines: 308-327
- kind: constant
  qualified_name: trie/parse/references:_INTERFACE_BASES
  lines: 332-332
- kind: function
  qualified_name: trie/parse/references:_find_node_for_symbol
  lines: 335-357
- kind: function
  qualified_name: trie/parse/references:extract_file_data
  lines: 360-470
- kind: constant
  qualified_name: trie/parse/references:__all__
  lines: 473-473
incoming_refs: 22
outgoing_refs: 12
---
<!-- trie:section symbol=trie/parse/references:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=a8d190298548018a1815d39892ee468daee2697b58134c9028d373077fce37fd source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 role=source-parsing -->
Extracts symbol references from Python source files using tree-sitter parsing to build code dependency graphs.

- Uses heuristic parsing to identify import statements and attribute access patterns
- Emits candidate reference edges that get filtered by the store against known symbols
- Covers basic import forms, intra-file references, and attribute access on imported modules
- Does not handle relative imports, method calls on instances, or shadowed names
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:_ImportBindings fingerprint=258ba3eed612857752238ff104e7750b9c3c96518a8d5da922d56f34c4d7d883 body_fp=8c18c075fbd3cb30c7ab0ddc9f1776ed85c6614b86c30838a19b28b22b8bf67f source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 role=source-parsing -->
Holds separate binding tables for symbol imports and module imports from one file's import statements.

- `symbols`: maps local names from `from X import Y` to fully-qualified target qnames
- `modules`: maps local names from `import X` to module paths for attribute access resolution
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:_collect_imports fingerprint=a368369780d31bd24d4551efa6c2d77a221aa72e9be0dfe8520254e25b6316ad body_fp=265ae8f04fe36ca89067bff8518a35be091714903ad72ee280b155fb9d8f66ef source_ref=9663a3e7dd4ea3de78fe1f41cc8fc9f4d98fd096 role=parsing -->
Build symbol and module binding tables by parsing all import statements in a module's AST at any nesting depth.

- Traverses the full AST recursively, so function-local imports are included alongside top-level ones
- Skips relative imports (leading `.`) due to missing project root context
- Returns `_ImportBindings` with separate tables for direct symbol imports vs module imports
- Handles both `from X import Y` and `import X` forms including aliases
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:_absorb_from_import fingerprint=f44bc5cf3570282d83eb29c0e88f1bc4f2635353a7df45f310381378d4ffd3c5 body_fp=24c4572f6b833925f0c304193155c793301d0c4d2a981a2717b76f6f5bae06a9 source_ref=c9e7ab14ee34a35fa4a54bcd01dfaddd1082be0d role=parsing -->
Parses one `from X import Y` statement and populates symbol and module binding dictionaries.

- `modules`: When provided, imported names are also registered as candidate module bindings
- Skips relative imports (starting with `.`)
- Handles both direct imports (`from foo import bar`) and aliased imports (`from foo import bar as baz`)
- Converts dotted module names to slash-separated format for qualified names
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:_absorb_plain_import fingerprint=8be0e860e35c788cf1af00254ccccfa18c31d3fabc837b9233f29d6cd7a9d8ec body_fp=2b513c60c237d3d3f39ae9954d0ee90dbeabe1d7297f39aaaed5ac4dddb00e2d source_ref=c9e7ab14ee34a35fa4a54bcd01dfaddd1082be0d role=parsing -->
Parses one `import` statement node and populates the modules dictionary with name-to-module-path bindings.

- Registers both full dotted names and their leftmost component for multi-level imports
- Handles aliased imports by mapping the alias to the original module path
- Skips relative imports that start with `.`
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:_collect_identifier_names fingerprint=14e61530854ad003a4661c28eecd812b0f64dc8512a51897f73a102d433144fc body_fp=ee1244090456a896f10251dc3662ecf47315263025bd00c6a209ea4415be29b4 source_ref=c9e7ab14ee34a35fa4a54bcd01dfaddd1082be0d role=parsing -->
Return all identifier-looking names mentioned within `node`'s subtree.

- Skips comment nodes during traversal
- Extracts text from tree-sitter identifier nodes using `_node_text`
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:_collect_attribute_accesses fingerprint=1e2dee9c514469b945c5482fcd23f95801a61214bd30db5296208beb7f118535 body_fp=6d49e94b6f9e6f8e033c6537dca2f771dc574b391e14d778fbd65d3b9acddcc6 source_ref=c9e7ab14ee34a35fa4a54bcd01dfaddd1082be0d role=parsing -->
Extracts base-attribute pairs from all attribute accesses in a tree-sitter node subtree.

- Returns tuples like `("a", "b")` and `("a.b", "c")` from chained access `a.b.c`
- Skips comments and strings to focus on actual name references
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:_dotted_text fingerprint=b9ce22d23f574b321e6e8dfd4266a20a0bcb3b21de9d37d399b8339f4b1beda6 body_fp=2c36acac7bdb7081ebba0692ddc5d90a6b4c0f316384296f07b1cbc4a3ebe09c source_ref=c9e7ab14ee34a35fa4a54bcd01dfaddd1082be0d role=parsing -->
Renders tree-sitter attribute/identifier nodes back to dotted notation strings like "a.b.c".

- Returns empty string for unrecognized node shapes to avoid inventing module bindings
- Recursively processes nested attribute nodes via depth-first traversal
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:_collect_call_target_names fingerprint=2e5e67d8a23f292471d83cad6a5c4003511d5b8763fad190ef88fc3b56aec200 body_fp=86f87cabb8f9988f6a3d02619cd559f7109e4fe3f8c0d20f6da7ff40a105bef0 source_ref=c9e7ab14ee34a35fa4a54bcd01dfaddd1082be0d role=parsing -->
Extracts names appearing in call position within a tree-sitter node subtree.

- Returns function names from `foo()` calls and rightmost attribute names from `a.b.foo()` calls
- Skips comments and string literals during traversal
- Used to distinguish `calls` edges from `references` edges in reference resolution
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:_collect_class_bases fingerprint=a6e62eca9b0f49d914eefdee003f45f1484203bcb5644113740a0ee8d46a8de5 body_fp=222e8f4525d70cba4414d039a0b6dbfaf3eb5a472ada82db666034ee84f3fa9d source_ref=c9e7ab14ee34a35fa4a54bcd01dfaddd1082be0d role=parsing -->
Extracts base class names from a class definition's superclass list.

- Returns rightmost identifier only (`abc.ABC` → `"ABC"`, `Protocol` → `"Protocol"`)
- Returns empty list if class has no superclasses
- Caller handles inheritance vs implementation classification
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:_INTERFACE_BASES fingerprint=2423fb92e941f1ef3a86575dfbe62eee62ea7d985efd51e6780375f713504f8e body_fp=ecebdf3dca544010c9afe1f5470270b0e88b924e802f174a4409a514ad08411b source_ref=912662364552d5bafa76f7db8cdfe1dcab60e12a role=model -->
Set of base class names that indicate interface contracts rather than implementation inheritance.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:_find_node_for_symbol fingerprint=d28e2391caa09aeaa59c30d0cd7f1a91e4021635f2a7564303231a0c2e53b80e body_fp=0e2a02f435c8e88577ad9daca1e4ed9ce7981e6f5c9285242f75352b6f436cce source_ref=c9e7ab14ee34a35fa4a54bcd01dfaddd1082be0d role=parsing -->
Locates the tree-sitter node for a symbol by matching line numbers against function and class definitions.

- Searches top-level definitions and class methods one level deep
- Returns None if no matching node is found at the symbol's start_line
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:extract_file_data fingerprint=631856d37302e0d51611faa040bb5c2ebef3ec2788a232ab7b5ba1517c082ab3 body_fp=6f78e68f7b6cc860cb771e4f696de37db5bc839efb27332c50ff470d00baa97b source_ref=c9e7ab14ee34a35fa4a54bcd01dfaddd1082be0d role=parsing -->
Parses a Python file and extracts both its symbol definitions and typed reference edges using tree-sitter.

- `source_root`: Optional root path for computing qualified names; defaults to file's parent directory  
- Returns `FileData` containing symbols and references with typed edges (`calls`, `references`, `inherits`, `implements`, `contains`), deduplicating references while preserving the strongest relationship type per target
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:__all__ fingerprint=9bc78c305b022f72da1cfdbc0b7349422140eb7e0e905460ac531538b0e5f20c body_fp=bdcf44aa5db7444b87f930185b76f62997eadf83dfa9739f964b4136826d48e3 source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 role=source-parsing -->
Defines the public API symbols exported when the module is imported with `from trie.parse.references import *`.
<!-- trie:end -->