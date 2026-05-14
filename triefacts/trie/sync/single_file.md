---
trie_version: 0.1.0
source: trie/sync/single_file.py
file_fingerprint: c5062deafc634a7da26dd022c15be29f90f2f4e7885d1070d8d11dd615e83e75
last_synced_at: '2026-05-14T17:51:48Z'
defines:
- kind: class
  qualified_name: trie/sync/single_file:FileSyncResult
  lines: 23-31
- kind: function
  qualified_name: trie/sync/single_file:sync_single_file
  lines: 79-191
incoming_refs: 26
outgoing_refs: 7
---
<!-- trie:section symbol=trie/sync/single_file:FileSyncResult fingerprint=98597894ae6c0b0245b21ad3bcef4f65d4ce6d3bf7bf48b3c479c935d752ae23 body_fp=cca75718b166dcd1ad1e2aff007c055ee0652f4f129b12ba6631d03ca7074e51 -->
## `FileSyncResult`

Frozen dataclass capturing outcome metrics for a single triefact sync operation.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/single_file:sync_single_file fingerprint=506de67ef69865afbf4611d99858bbd8db27d2a15f04d6f34c953b0805093ef9 body_fp=63c5ac75658b5a51e3fba71af0b6c27d917ecab1f3943cd02bc9a99ef4dc3443 -->
## `sync_single_file(source_path, *, project_root, config, client, dest_triefact_path=None, store=None) -> FileSyncResult`

Generate or refresh the triefact file for a single Python source file, upserting sections for public symbols and removing stale ones.

- `dest_triefact_path`: write rendered output here instead of the canonical path; canonical is still read to preserve prose.
- `store`: when provided, enriches front matter with ref counts and records section one-liners for MCP lookups.
- Raises `ValueError` if `source_path` is not under the configured `source_root`.
<!-- trie:end -->