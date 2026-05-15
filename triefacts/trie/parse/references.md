---
trie_version: 0.1.0
source: trie/parse/references.py
file_fingerprint: e1e24f056cab1bd3e3acbd4c1ff5908a338dfe5ffe9f539eb9df9cc862890f86
last_synced_at: '2026-05-15T13:06:51Z'
description: Reference extraction via tree-sitter.
defines:
- kind: class
  qualified_name: trie/parse/references:Reference
  lines: 41-49
- kind: class
  qualified_name: trie/parse/references:FileData
  lines: 53-57
- kind: function
  qualified_name: trie/parse/references:_collect_imports
  lines: 60-91
- kind: function
  qualified_name: trie/parse/references:_collect_identifier_names
  lines: 94-112
- kind: function
  qualified_name: trie/parse/references:_find_node_for_symbol
  lines: 115-137
- kind: function
  qualified_name: trie/parse/references:extract_file_data
  lines: 140-187
incoming_refs: 14
outgoing_refs: 6
---
<!-- trie:section symbol=trie/parse/references:Reference fingerprint=be66059ea554ea6d31cdeb5487f51707421e9c4c7858b8f82520c5a8ef2093de body_fp=5202bf2a195e34d954c9ca625ba30dd28b6a8c56cdfa4b10800b5c981cac7abb source_ref=49621fd1c7ec843b407b1123564512bc18c4a78c -->
## `Reference`

Immutable dataclass representing a single directed edge from one symbol to another.

- `src_qname`: qualified name of the referencing symbol (e.g. `src/foo:bar`)
- `target_qname`: qualified name of the resolved target; persisted as string before DB lookup
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/references:FileData fingerprint=d1e4f5799633450224d7f7fcf994c834a43d825b45a9734ebef2a7033ec8373e body_fp=1f910d86b5e7e7c449ec1ef0ba6ccfb87a57874e35e03067c470ac605b262d43 source_ref=49621fd1c7ec843b407b1123564512bc18c4a78c -->
## `FileData`

Holds symbols and outbound references extracted from one file in a single tree-sitter parse.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/references:extract_file_data fingerprint=7759e9187d3c23502696a10df5356b60e647258980bdd29d9c63cfbb73732d0c body_fp=a7fd2dc07268b7b5a1b968e6b316bd7cb8314ff3f5b57508b89f2eeabafdc25c source_ref=49621fd1c7ec843b407b1123564512bc18c4a78c -->
## `extract_file_data(file_path: Path, source_root: Path | None = None) -> FileData`

Parse a Python file once and return all its symbols and outbound references.

- `source_root`: used to compute qualified names; defaults to `file_path.parent`.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/references:_collect_imports fingerprint=e84e7ee8536c233cfaa7c34ea11ee529f8dbb937561cb5d6c81f8ca15851057b body_fp=6f90bcbb025ed298ffe3542e6a268197ce4bab490ebf61532b84f327fa1bae85 source_ref=49621fd1c7ec843b407b1123564512bc18c4a78c -->
## `_collect_imports(root: Node, source: bytes) -> dict[str, str]`

Build a local-name → qualified-target mapping from all `from X import Y` statements in the module.

- `root`: tree-sitter root node of the parsed module.
- Returns `{"local_name": "module/path:original_name"}` for each resolved binding.
- Skips relative imports and dotted local names.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/references:_collect_identifier_names fingerprint=14e61530854ad003a4661c28eecd812b0f64dc8512a51897f73a102d433144fc body_fp=08048a7727373f6c9e05170e261a28dd6199eb34d3285eb25cee4566593a7ac9 source_ref=49621fd1c7ec843b407b1123564512bc18c4a78c -->
## `_collect_identifier_names(node: Node, source: bytes) -> set[str]`

Return all identifier names mentioned within a node's subtree via recursive walk.

- Includes plain identifiers, attribute-expression names, and call targets.
- Skips comment nodes entirely; type-annotation identifiers are included as noise.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/references:_find_node_for_symbol fingerprint=d28e2391caa09aeaa59c30d0cd7f1a91e4021635f2a7564303231a0c2e53b80e body_fp=7152a6ecfe5ad1bf698493c82e7ebdd6a4534f5aadb64459ae98fa71a62be116 source_ref=49621fd1c7ec843b407b1123564512bc18c4a78c -->
## `_find_node_for_symbol(root: Node, symbol: Symbol) -> Node | None`

Locate the tree-sitter `function_definition` or `class_definition` node matching `symbol` by start line.

- `symbol.start_line`: 1-based line number used for matching against node start points.
- Returns the decorated-stripped node, or `None` if no match is found.
- Searches top-level children and one level into class bodies.
<!-- trie:end -->