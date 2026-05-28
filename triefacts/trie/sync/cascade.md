---
trie_version: 0.1.5
source: trie/sync/cascade.py
file_fingerprint: a2176696d2fee6d099b05d37586bee9de5c5a369112381c68408097ca450fdfc
last_synced_at: '2026-05-23T23:54:23Z'
defines:
- kind: module
  qualified_name: trie/sync/cascade:__module__
  lines: 1-153
- kind: class
  qualified_name: trie/sync/cascade:CascadeResult
  lines: 11-45
- kind: function
  qualified_name: trie/sync/cascade:compute_cascade
  lines: 48-152
incoming_refs: 9
outgoing_refs: 1
---
<!-- trie:section symbol=trie/sync/cascade:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=09e763ffab27c5abde9b6b3a407970fe2ed7899a21ebee7021787a39aca7c117 source_ref=c1c2b9ed991a072e6f2783f4adee6e8e49fa2f32 -->
## `cascade`

Compute cascading file and symbol invalidation sets from a seed set of changed files.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/cascade:CascadeResult fingerprint=4427fc9e9b33bd6592de10605387006d37145125ccdcf08ffbaaff4711fb0c21 body_fp=fea5670998293f2b7036267b3392049bbd1df6bd139d0021709b364dba20abd4 source_ref=c1c2b9ed991a072e6f2783f4adee6e8e49fa2f32 -->
## `CascadeResult`

Frozen dataclass holding files and symbols requiring regeneration after a set of source changes.

- `affected_files`: sorted list of all files; seed files plus cascade-pulled files.
- `cascaded_from_change`: files reached via inbound-edge walk, excluding direct seed files.
- `hop_by_file`: minimum BFS hop distance from any seed file; seed files have hop 0.
- `cascaded_qnames`: qualified names reached by cascade walk; seed-file symbols excluded.
- `hop_by_qname`: minimum BFS hop distance per symbol; seed qnames have hop 0.
- `file_by_cascaded_qname`: maps each cascaded qname to its own defining file path.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/cascade:compute_cascade fingerprint=8519ed9bd06d4dfad5495cde3895289ce7ff3011a537bb7ff9faa35cbc3fea8d body_fp=d2a294d5975eec43135254c85a38e5dd967bb393af025e03f53c053699d854ce source_ref=c1c2b9ed991a072e6f2783f4adee6e8e49fa2f32 -->
## `compute_cascade(*, changed_files: Iterable[str], store: Store, depth: int = 1, hub_threshold: int = 20) -> CascadeResult`

Compute the cascade closure for a set of changed files by BFS-walking inbound symbol edges.

- `depth`: maximum number of hops to follow from seed-file symbols.
- `hub_threshold`: symbols with more inbound references than this are not expanded.
- `store`: queried for per-symbol inbound counts, qnames per file, and referencing symbols with their files.
<!-- trie:end -->