---
trie_version: 0.1.0
source: trie/sync/single_file.py
file_fingerprint: b938e169ec464c3650c7e3226b9518a4545590917b66f8c1d1e6ad58a624eb4e
last_synced_at: '2026-05-14T18:33:31Z'
defines:
- kind: class
  qualified_name: trie/sync/single_file:FileSyncResult
  lines: 23-31
- kind: function
  qualified_name: trie/sync/single_file:sync_single_file
  lines: 79-201
incoming_refs: 26
outgoing_refs: 7
---
<!-- trie:section symbol=trie/sync/single_file:FileSyncResult fingerprint=98597894ae6c0b0245b21ad3bcef4f65d4ce6d3bf7bf48b3c479c935d752ae23 body_fp=ff8bf57f578c9fa8243e1c73e6a130ea6452cb19d843c559ed9d0ce1773ee4a2 -->
## `FileSyncResult`

Frozen dataclass holding counters and paths returned after syncing one source file.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/single_file:sync_single_file fingerprint=1a50cdd7b8df3ee00270bfb16a45a6ff50489b9498c7b99131e89e6d9d451327 body_fp=409c9d9d6b9ef5636100414a473c9833171139634c18769fb1b6edadb5ffd67d -->
## `sync_single_file(source_path, *, project_root, config, client, dest_triefact_path=None, store=None) -> FileSyncResult`

Generate or refresh the triefact file for a single Python source file, upserting sections for public symbols and removing stale ones.

- `dest_triefact_path`: write rendered output here instead of the canonical path; canonical file still used as load source.
- `store`: when provided, enriches front matter with ref counts and persists per-section one-liners for MCP lookups.
- Raises `ValueError` if `source_path` is not under `config.triefacts.source_root`.
- Private symbols (leading underscore) are skipped entirely.
<!-- trie:end -->