---
trie_version: 0.1.0
source: trie/sync/cascade.py
file_fingerprint: bc0e23c7ff591ec064870cb006e32d66c68544513cb37be9b5c4d4f12e68b21f
last_synced_at: '2026-05-14T18:32:46Z'
defines:
- kind: class
  qualified_name: trie/sync/cascade:CascadeResult
  lines: 11-21
- kind: function
  qualified_name: trie/sync/cascade:compute_cascade
  lines: 24-94
incoming_refs: 9
outgoing_refs: 0
---
<!-- trie:section symbol=trie/sync/cascade:CascadeResult fingerprint=8ce9686496fd5022cd1a321752b0a1a34e058f9b70eccaa7ff85c65e47e1cef1 body_fp=c13e940d44ecca261dce9f0e91178e538e03156c9868e05f7880308508669d9f -->
## `CascadeResult`

Immutable dataclass holding files needing regeneration after source changes.

- `affected_files`: sorted list of all files requiring regeneration, including seed files.
- `changed_files`: the seed set of directly modified files.
- `cascaded_from_change`: files pulled in via edge traversal, excluding direct changes.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/cascade:compute_cascade fingerprint=6945a31c4ef3d0cb262687f24a5de7b96e60d702fa8dbeeda1f60739176c8edf body_fp=784b0450593a7fb1c33e824b6a1ca39e9e3a5079bf2f05eb006b3b10f8066c90 -->
## `compute_cascade(*, changed_files: Iterable[str], store: Store, depth: int = 1, hub_threshold: int = 20) -> CascadeResult`

Compute the cascade closure for a set of changed files by walking inbound dependency edges up to `depth` hops.

- `depth`: number of inbound-edge hops to expand from seed symbols.
- `hub_threshold`: symbols with more inbound references than this are not expanded, preventing utility modules from invalidating the whole graph.
- `changed_files`: empty input returns an empty `CascadeResult` immediately.
- Returns `affected_files` sorted alphabetically; seed files always included.
<!-- trie:end -->