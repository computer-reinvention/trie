---
trie_version: 0.1.0
source: trie/sync/single_file.py
file_fingerprint: 9f5be9d3860069c70c1d27a3f803eb98ef19ed855938c95d313d29ba07731c05
last_synced_at: '2026-05-12T18:34:26Z'
defines:
- kind: class
  qualified_name: trie/sync/single_file:FileSyncResult
  lines: 23-31
- kind: function
  qualified_name: trie/sync/single_file:sync_single_file
  lines: 79-178
incoming_refs: 26
outgoing_refs: 6
---
<!-- trie:section symbol=trie/sync/single_file:FileSyncResult fingerprint=98597894ae6c0b0245b21ad3bcef4f65d4ce6d3bf7bf48b3c479c935d752ae23 body_fp=e25067714db1c08828d46774e7e4ba8beb0d528542044c1de3c7b6f27e497827 -->
## `FileSyncResult`

Frozen dataclass holding the outcome of syncing one source file to its triefact.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/single_file:sync_single_file fingerprint=ae4d0268002dabec2391c262051c9cac15fdda6421ae602bcecb2a6ee24e9ad8 body_fp=4be06751119b567d0cca02ee2a9d3e84cd95a18f9b8a24c7f9d09e71cd8aa930 -->
## `sync_single_file(source_path, *, project_root, config, client, dest_triefact_path=None, store=None) -> FileSyncResult`

Generate or refresh the triefact file for a single Python source file, upserting sections for public symbols and removing stale ones.

- `dest_triefact_path`: write output here instead of the canonical path; still reads canonical for preserved prose.
- `store`: when provided, enriches front matter with inbound/outbound cross-file ref counts.
- Raises `ValueError` if `source_path` is not under the configured `source_root`.
<!-- trie:end -->