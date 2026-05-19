---
trie_version: 0.1.2
source: trie/sync/cascade.py
file_fingerprint: a2176696d2fee6d099b05d37586bee9de5c5a369112381c68408097ca450fdfc
last_synced_at: '2026-05-19T10:41:57Z'
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
<!-- trie:section symbol=trie/sync/cascade:CascadeResult fingerprint=4427fc9e9b33bd6592de10605387006d37145125ccdcf08ffbaaff4711fb0c21 body_fp=7fbc9344e99658e38dee40d3e7807f4952ab57d5450e4529e0c45cbb18dc0cbe source_ref=c1c2b9ed991a072e6f2783f4adee6e8e49fa2f32 -->
## `CascadeResult`

Frozen dataclass holding files and symbols needing regeneration after a set of source changes.

- `affected_files`: sorted list of all files to regenerate, including seeds.
- `cascaded_from_change`: subset of `affected_files` reached via edge traversal, not direct edits.
- `hop_by_file`: minimum BFS hop distance from any seed file; seeds have hop 0.
- `cascaded_qnames`: qualified names reached by the cascade walk; excludes seed-file symbols.
- `hop_by_qname`: minimum BFS hop distance per symbol; seed qnames map to 0.
- `file_by_cascaded_qname`: maps each cascaded qname to its defining file path.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/cascade:compute_cascade fingerprint=8519ed9bd06d4dfad5495cde3895289ce7ff3011a537bb7ff9faa35cbc3fea8d body_fp=f3af87d9bde76d875491a4527d73280cad5e8155e1c04420e33e5ec7067635ad source_ref=c1c2b9ed991a072e6f2783f4adee6e8e49fa2f32 -->
## `compute_cascade(*, changed_files: Iterable[str], store: Store, depth: int = 1, hub_threshold: int = 20) -> CascadeResult`

Compute the cascade closure for a set of changed files by walking inbound edges up to `depth` hops.

- `depth`: maximum BFS hops to follow from seed symbols.
- `hub_threshold`: symbols with more inbound references than this are not expanded.
- `store`: graph store providing symbol-to-file mappings and inbound reference counts.
- Returns files sorted alphabetically; seed files always included with hop 0; result now includes per-symbol sets `cascaded_qnames`, `hop_by_qname`, and `file_by_cascaded_qname`.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/cascade:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=5c94138ec4b801abf44854dda09199e8ea5fabe7697b1320f9ebbf7cb3002525 source_ref=c1c2b9ed991a072e6f2783f4adee6e8e49fa2f32 -->
## `cascade`

Compute file and symbol cascade closure from a set of changed source files using BFS over inbound reference edges.

- `CascadeResult`: frozen dataclass holding affected files, cascaded qnames, and hop distances
- `compute_cascade`: BFS walk with hub-guard and configurable depth; returns a `CascadeResult`
<!-- trie:end -->