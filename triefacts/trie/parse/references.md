---
trie_version: 0.1.5
source: trie/parse/references.py
file_fingerprint: eed188fddba8106bfbc20fc06b846e50088aab906f4d2690d3fab9228072a88f
last_synced_at: '2026-06-03T21:14:26Z'
description: Reference extraction via tree-sitter.
defines:
- kind: module
  qualified_name: trie/parse/references:__module__
  lines: 1-371
- kind: class
  qualified_name: trie/parse/references:Reference
  lines: 50-58
- kind: class
  qualified_name: trie/parse/references:FileData
  lines: 62-66
- kind: class
  qualified_name: trie/parse/references:_ImportBindings
  lines: 70-88
- kind: function
  qualified_name: trie/parse/references:_collect_imports
  lines: 91-117
- kind: function
  qualified_name: trie/parse/references:_absorb_from_import
  lines: 120-161
- kind: function
  qualified_name: trie/parse/references:_absorb_plain_import
  lines: 164-191
- kind: function
  qualified_name: trie/parse/references:_collect_identifier_names
  lines: 194-212
- kind: function
  qualified_name: trie/parse/references:_collect_attribute_accesses
  lines: 215-253
- kind: function
  qualified_name: trie/parse/references:_dotted_text
  lines: 256-274
- kind: function
  qualified_name: trie/parse/references:_find_node_for_symbol
  lines: 277-299
- kind: function
  qualified_name: trie/parse/references:extract_file_data
  lines: 302-367
- kind: constant
  qualified_name: trie/parse/references:__all__
  lines: 370-370
incoming_refs: 22
outgoing_refs: 9
---
<!-- trie:section symbol=trie/parse/references:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=a8d190298548018a1815d39892ee468daee2697b58134c9028d373077fce37fd source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 role=source-parsing -->
Extracts symbol references from Python source files using tree-sitter parsing to build code dependency graphs.

- Uses heuristic parsing to identify import statements and attribute access patterns
- Emits candidate reference edges that get filtered by the store against known symbols
- Covers basic import forms, intra-file references, and attribute access on imported modules
- Does not handle relative imports, method calls on instances, or shadowed names
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:Reference fingerprint=be66059ea554ea6d31cdeb5487f51707421e9c4c7858b8f82520c5a8ef2093de body_fp=8cfa86ea6e6944e9b06c2c54c8b7c14e85ac1f9d820be172bc65bf35146d4234 source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 role=source-parsing -->
Represents an outbound reference from one symbol to another within the codebase.

- `src_qname`: qualified name of the referencing symbol
- `target_qname`: qualified name of the referenced symbol target
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:FileData fingerprint=d1e4f5799633450224d7f7fcf994c834a43d825b45a9734ebef2a7033ec8373e body_fp=8ed03ed9cb8157cb89a0321e40c28967377563c8eed15127e8bd8b95cd10a0d3 source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 role=source-parsing -->
Holds symbols and outbound references extracted from one file in a single tree-sitter parse.

- `symbols`: List of symbols found in the file
- `references`: List of outbound references from symbols to qualified names
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:_ImportBindings fingerprint=258ba3eed612857752238ff104e7750b9c3c96518a8d5da922d56f34c4d7d883 body_fp=8c18c075fbd3cb30c7ab0ddc9f1776ed85c6614b86c30838a19b28b22b8bf67f source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 role=source-parsing -->
Holds separate binding tables for symbol imports and module imports from one file's import statements.

- `symbols`: maps local names from `from X import Y` to fully-qualified target qnames
- `modules`: maps local names from `import X` to module paths for attribute access resolution
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:_collect_imports fingerprint=2331c5c458cf82625623bc08d2dffc4a3ce446c63604d19b7ebc8807e7149e7a body_fp=2e0a2aa34c6f0bcdb57d0de133b5ec8d13571d7dde9528a6e3435a958b06b2d9 source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 role=source-parsing -->
Build symbol and module binding tables by parsing all import statements in a module's AST.

- Skips relative imports (leading `.`) due to missing project root context
- Returns `_ImportBindings` with separate tables for direct symbol imports vs module imports
- Handles both `from X import Y` and `import X` forms including aliases
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:_absorb_from_import fingerprint=f44bc5cf3570282d83eb29c0e88f1bc4f2635353a7df45f310381378d4ffd3c5 body_fp=24c4572f6b833925f0c304193155c793301d0c4d2a981a2717b76f6f5bae06a9 source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 role=source-parsing -->
Parses one `from X import Y` statement and populates symbol and module binding dictionaries.

- `modules`: When provided, imported names are also registered as candidate module bindings
- Skips relative imports (starting with `.`)
- Handles both direct imports (`from foo import bar`) and aliased imports (`from foo import bar as baz`)
- Converts dotted module names to slash-separated format for qualified names
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:_absorb_plain_import fingerprint=8be0e860e35c788cf1af00254ccccfa18c31d3fabc837b9233f29d6cd7a9d8ec body_fp=2b513c60c237d3d3f39ae9954d0ee90dbeabe1d7297f39aaaed5ac4dddb00e2d source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 role=source-parsing -->
Parses one `import` statement node and populates the modules dictionary with name-to-module-path bindings.

- Registers both full dotted names and their leftmost component for multi-level imports
- Handles aliased imports by mapping the alias to the original module path
- Skips relative imports that start with `.`
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:_collect_identifier_names fingerprint=14e61530854ad003a4661c28eecd812b0f64dc8512a51897f73a102d433144fc body_fp=ee1244090456a896f10251dc3662ecf47315263025bd00c6a209ea4415be29b4 source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 role=source-parsing -->
Return all identifier-looking names mentioned within `node`'s subtree.

- Skips comment nodes during traversal
- Extracts text from tree-sitter identifier nodes using `_node_text`
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:_collect_attribute_accesses fingerprint=1e2dee9c514469b945c5482fcd23f95801a61214bd30db5296208beb7f118535 body_fp=6d49e94b6f9e6f8e033c6537dca2f771dc574b391e14d778fbd65d3b9acddcc6 source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 role=source-parsing -->
Extracts base-attribute pairs from all attribute accesses in a tree-sitter node subtree.

- Returns tuples like `("a", "b")` and `("a.b", "c")` from chained access `a.b.c`
- Skips comments and strings to focus on actual name references
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:_dotted_text fingerprint=b9ce22d23f574b321e6e8dfd4266a20a0bcb3b21de9d37d399b8339f4b1beda6 body_fp=2c36acac7bdb7081ebba0692ddc5d90a6b4c0f316384296f07b1cbc4a3ebe09c source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 role=source-parsing -->
Renders tree-sitter attribute/identifier nodes back to dotted notation strings like "a.b.c".

- Returns empty string for unrecognized node shapes to avoid inventing module bindings
- Recursively processes nested attribute nodes via depth-first traversal
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:_find_node_for_symbol fingerprint=d28e2391caa09aeaa59c30d0cd7f1a91e4021635f2a7564303231a0c2e53b80e body_fp=0e2a02f435c8e88577ad9daca1e4ed9ce7981e6f5c9285242f75352b6f436cce source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 role=source-parsing -->
Locates the tree-sitter node for a symbol by matching line numbers against function and class definitions.

- Searches top-level definitions and class methods one level deep
- Returns None if no matching node is found at the symbol's start_line
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:extract_file_data fingerprint=9d2cbdf6af58a3d0716ed3e066ba4a263123ac990289dd09ca5cf255a8b713a2 body_fp=f72af56d38c8baaea2d1af70cccf84e8aac9116714a83c8857f3141e9f2ff8a7 source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 role=source-parsing -->
Parses a Python file and extracts both its symbol definitions and outbound reference edges using tree-sitter.

- `source_root`: Optional root path for computing qualified names; defaults to file's parent directory
- Returns `FileData` containing symbols and references, where references include both bare identifier usage and module attribute access patterns
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/references:__all__ fingerprint=9bc78c305b022f72da1cfdbc0b7349422140eb7e0e905460ac531538b0e5f20c body_fp=bdcf44aa5db7444b87f930185b76f62997eadf83dfa9739f964b4136826d48e3 source_ref=c6775babce628ee17704cd01d13e5bd434d47d37 role=source-parsing -->
Defines the public API symbols exported when the module is imported with `from trie.parse.references import *`.
<!-- trie:end -->