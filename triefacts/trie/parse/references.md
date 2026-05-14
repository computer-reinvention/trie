---
trie_version: 0.1.0
source: trie/parse/references.py
file_fingerprint: e1e24f056cab1bd3e3acbd4c1ff5908a338dfe5ffe9f539eb9df9cc862890f86
last_synced_at: '2026-05-14T17:29:39Z'
description: Reference extraction via tree-sitter.
defines:
- kind: class
  qualified_name: trie/parse/references:Reference
  lines: 41-49
- kind: class
  qualified_name: trie/parse/references:FileData
  lines: 53-57
- kind: function
  qualified_name: trie/parse/references:extract_file_data
  lines: 140-187
incoming_refs: 14
outgoing_refs: 6
---
<!-- trie:section symbol=trie/parse/references:Reference fingerprint=be66059ea554ea6d31cdeb5487f51707421e9c4c7858b8f82520c5a8ef2093de body_fp=10c169aabc1e1b6cf3f1d1e5242cc39d26ee82c9e9f0e20fb3b3aa8b56017945 -->
## `Reference`

Immutable dataclass representing one outbound edge from a source symbol to a resolved target.

- `src_qname`: qualified name of the referencing symbol (e.g. `src/foo:bar`)
- `target_qname`: resolved qualified name of the target; persisted as a string before DB lookup
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/references:FileData fingerprint=d1e4f5799633450224d7f7fcf994c834a43d825b45a9734ebef2a7033ec8373e body_fp=2f03875c10de0cee18ac3108f6a317a66721f5a745f3677a06410c85e509615c -->
## `FileData`

Symbols and outbound references extracted from one file in a single tree-sitter parse.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/references:extract_file_data fingerprint=7759e9187d3c23502696a10df5356b60e647258980bdd29d9c63cfbb73732d0c body_fp=fa829bd5218c41af00066e27ac2d73cc2a7c47f05233d4948f526fce25689e72 -->
## `extract_file_data(file_path: Path, source_root: Path | None = None) -> FileData`

Parse a Python file once and return all its symbols and deduplicated outbound references.

- `source_root`: used to compute qualified names; defaults to `file_path.parent`.
<!-- trie:end -->