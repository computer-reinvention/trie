---
trie_version: 0.1.0
source: trie/sync/single_file.py
file_fingerprint: 5e5b6d422cae704ce14f144920667b5222612b32761c0dfc091d9f6148bbcd91
last_synced_at: '2026-05-14T19:39:41Z'
defines:
- kind: class
  qualified_name: trie/sync/single_file:FileSyncResult
  lines: 24-32
- kind: function
  qualified_name: trie/sync/single_file:sync_single_file
  lines: 128-296
incoming_refs: 30
outgoing_refs: 12
---
<!-- trie:section symbol=trie/sync/single_file:FileSyncResult fingerprint=98597894ae6c0b0245b21ad3bcef4f65d4ce6d3bf7bf48b3c479c935d752ae23 body_fp=ef4b499a8cefee511c19ea98d1612c411099b30427444c2cbf337593051c0db4 source_ref=6636d7806f1c4af65b4757693deef0a5adc4368c -->
## `@dataclass(frozen=True) class FileSyncResult`

Immutable result record returned by `sync_single_file` summarising token usage and mutation counts.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/single_file:sync_single_file fingerprint=6250a80c01ed643935769342dbd4b88e3dcb0aa8db9714dc891f7b075ef246f8 body_fp=4b922302a123b39c74b4ef328d636fe2fb2f0bce6d2d997ccf3127a66b877aa4 source_ref=6636d7806f1c4af65b4757693deef0a5adc4368c -->
## `sync_single_file(source_path, *, project_root, config, client, dest_triefact_path=None, store=None) -> FileSyncResult`

Generate or refresh the triefact file for a single Python source file, upserting sections for public symbols and removing stale ones.

- `dest_triefact_path`: write output here instead of the canonical path; canonical file is still read for existing prose.
- `store`: when provided, enriches front matter with ref counts and records one-liner metadata; omit to skip graph queries.
- Raises `ValueError` if `source_path` is not under `config.triefacts.source_root`.
<!-- trie:end -->