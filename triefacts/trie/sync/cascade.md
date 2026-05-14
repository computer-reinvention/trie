---
trie_version: 0.1.0
source: trie/sync/cascade.py
file_fingerprint: 4ea4243a2280709a036bf81b01dc051d950238f08be11f2a5ac5bd50b9c44269
last_synced_at: '2026-05-14T19:39:07Z'
defines:
- kind: class
  qualified_name: trie/sync/cascade:CascadeResult
  lines: 11-28
- kind: function
  qualified_name: trie/sync/cascade:compute_cascade
  lines: 31-114
incoming_refs: 9
outgoing_refs: 0
---
<!-- trie:section symbol=trie/sync/cascade:CascadeResult fingerprint=0f8414a5924aa3aa5e09f6937cb95207b418c1875d657a1b30d339d1aa090187 body_fp=8bdf31dbdc7d8bc6bb5697be69ff1eea19ecad0438531f7d5a6cd083a90ee5c5 source_ref=f98da06542c9f574aa10f65c02d99faa80d552c7 -->
## `CascadeResult`

Frozen dataclass holding files needing regeneration after a set of source changes.

- `affected_files`: sorted list of all files to regenerate, including seeds.
- `cascaded_from_change`: subset of `affected_files` reached via edge traversal, not direct edits.
- `hop_by_file`: minimum BFS hop distance from any seed file; seeds have hop 0.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/cascade:compute_cascade fingerprint=3d988d07b3e5416e383579b67e950df4e3506de08977a0df1d7710baaf14f6aa body_fp=a0d272da2ec0b7c4993f50a533c44b1819bdee814ed8b062a8a5d3696f821e8a source_ref=f98da06542c9f574aa10f65c02d99faa80d552c7 -->
## `compute_cascade(*, changed_files: Iterable[str], store: Store, depth: int = 1, hub_threshold: int = 20) -> CascadeResult`

Compute the cascade closure for a set of changed files by walking inbound edges up to `depth` hops.

- `depth`: maximum BFS hops to follow from seed symbols.
- `hub_threshold`: symbols with more inbound references than this are not expanded.
- `store`: graph store providing symbol-to-file mappings and inbound reference counts.
- Returns files sorted alphabetically; seed files always included with hop 0.
<!-- trie:end -->