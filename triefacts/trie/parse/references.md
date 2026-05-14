---
trie_version: 0.1.0
source: trie/parse/references.py
file_fingerprint: e1e24f056cab1bd3e3acbd4c1ff5908a338dfe5ffe9f539eb9df9cc862890f86
last_synced_at: '2026-05-14T19:44:40Z'
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