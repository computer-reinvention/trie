---
trie_version: 0.1.0
source: trie/parse/references.py
file_fingerprint: 7218c719c91b2c2cf4926686370bb44e603c2d738ba3c8a7596ed85d69b39ce8
last_synced_at: '2026-05-12T18:32:56Z'
description: Heuristic reference extraction via tree-sitter.
defines:
- kind: class
  qualified_name: trie/parse/references:Reference
  lines: 38-47
- kind: class
  qualified_name: trie/parse/references:FileData
  lines: 51-55
- kind: function
  qualified_name: trie/parse/references:extract_file_data
  lines: 138-197
incoming_refs: 14
outgoing_refs: 6
---
<!-- trie:section symbol=trie/parse/references:Reference fingerprint=6a62952764b3eb1a7a54dbe4b0dff02892fd43fdf48fa4dfa5779df7df977f77 body_fp=de67e88b935129f482b48382d008248cb3a378529e0454f8664e062de3f48990 -->
## `Reference`

Immutable record of a single outbound reference from one symbol to another.

- `src_qname`: qualified name of the referencing symbol.
- `target_qname`: resolved qualified name of the target (e.g. `src/foo:bar`).
- `confidence`: `"tree_sitter_import"` for import-resolved edges; `"name_match"` for intra-file name matches.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/references:FileData fingerprint=d1e4f5799633450224d7f7fcf994c834a43d825b45a9734ebef2a7033ec8373e body_fp=ced930358f5cef8bbd15401b5ec237522bd7d93de51c28ddef56fd01139fe32a -->
## `FileData`

Aggregate symbols and outbound references extracted from one file in a single tree-sitter parse.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/references:extract_file_data fingerprint=7761936c78871b28894a938bf724661d7112da67e33514202a5c7a0dd5f66f2a body_fp=d9dfde2354acb0d0b97c4ee01fd0f09145f16b602825b5a817f45202635aed26 -->
## `extract_file_data(file_path: Path, source_root: Path | None = None) -> FileData`

Parse a Python file once and return all its symbols and outbound references.

- `source_root`: used to compute qualified names; defaults to `file_path.parent`.
- References carry `confidence` of `"tree_sitter_import"` or `"name_match"`.
<!-- trie:end -->