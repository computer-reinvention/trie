---
trie_version: 0.1.0
source: trie/sync/cascade.py
file_fingerprint: 29e08b15a221e482846dabfb845becf29b8c7bd413c16e4f38b825ec256ff798
last_synced_at: '2026-05-12T18:35:01Z'
defines:
- kind: class
  qualified_name: trie/sync/cascade:CascadeResult
  lines: 10-20
- kind: function
  qualified_name: trie/sync/cascade:compute_cascade
  lines: 23-79
incoming_refs: 9
outgoing_refs: 0
---
<!-- trie:section symbol=trie/sync/cascade:CascadeResult fingerprint=8ce9686496fd5022cd1a321752b0a1a34e058f9b70eccaa7ff85c65e47e1cef1 body_fp=fc5b17ab1a3644a5438fbab870a6a8ef6611e48763ab0f6e77afd5449e2a6924 -->
## `CascadeResult`

Immutable dataclass holding files that need regeneration after source changes.

- `affected_files`: sorted list of all files to regenerate, including seeds.
- `changed_files`: the seed set of directly edited files.
- `cascaded_from_change`: files pulled in by edge-walking, excluding direct changes.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/cascade:compute_cascade fingerprint=7afdde987459b8a1461cb2e4544cd0c73755fccd75bb37cb46c02cc4624f25ae body_fp=11d6dcb0fa3b08670ae26e1fd7ada9d9e09543a8e970afd0440e0452f459e8cd -->
## `compute_cascade(*, changed_files: Iterable[str], store: Store, depth: int = 1, hub_threshold: int = 20) -> CascadeResult`

Compute the cascade closure for a set of changed files by walking inbound edges up to `depth` hops.

- `depth`: number of inbound-edge hops to follow from seed symbols.
- `hub_threshold`: symbols with more inbound references than this are not expanded.
- `store`: provides symbol-to-file mappings and inbound reference data.
- Returns `CascadeResult` with sorted `affected_files`; seed files always included.
<!-- trie:end -->