---
trie_version: 0.1.0
source: trie/sync/single_file.py
file_fingerprint: c5062deafc634a7da26dd022c15be29f90f2f4e7885d1070d8d11dd615e83e75
last_synced_at: '2026-05-14T17:30:32Z'
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
<!-- trie:section symbol=trie/sync/single_file:FileSyncResult fingerprint=98597894ae6c0b0245b21ad3bcef4f65d4ce6d3bf7bf48b3c479c935d752ae23 body_fp=dcb882dabd1911cc0b7a60b654a3d7aa83b65d7428cf3da54c4a3e5903bb97dc -->
## `FileSyncResult`

Frozen dataclass holding the outcome of syncing one Python source file to its triefact.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/single_file:sync_single_file fingerprint=506de67ef69865afbf4611d99858bbd8db27d2a15f04d6f34c953b0805093ef9 body_fp=6f94f0a05e3e2aa6256360021ed3aec7a482bdacfc17da22e61e6d66d9fec055 -->
## `sync_single_file(source_path, *, project_root, config, client, dest_triefact_path=None, store=None) -> FileSyncResult`

Generate or refresh the triefact file for a single Python source file, preserving existing hand-written prose.

- `dest_triefact_path`: write output here instead of the canonical path; canonical file still read for existing prose.
- `store`: when provided, enriches front matter with ref counts and records section one-liners for MCP lookups.
- Raises `ValueError` if `source_path` is not under `config.triefacts.source_root`.
- Private symbols (leading underscore) are skipped entirely.
- Stale sections (symbols removed from source) are pruned from the triefact.
<!-- trie:end -->