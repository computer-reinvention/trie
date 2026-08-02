---
trie_version: 0.3.0
source: trie/sync/cascade.py
file_fingerprint: a2176696d2fee6d099b05d37586bee9de5c5a369112381c68408097ca450fdfc
last_synced_at: '2026-06-03T21:15:34Z'
defines:
- kind: module
  qualified_name: trie/sync/cascade:__module__
  lines: 1-153
- kind: class
  qualified_name: trie/sync/cascade:CascadeResult
  lines: 11-45
  signature: class CascadeResult
- kind: function
  qualified_name: trie/sync/cascade:compute_cascade
  lines: 48-152
  signature: 'def compute_cascade( *, changed_files: Iterable[str], store: Store, depth: int = 1, hub_threshold: int = 20, ) -> CascadeResult'
incoming_refs: 11
outgoing_refs: 1
---
<!-- trie:section symbol=trie/sync/cascade:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=b22e4f1aa2b8727fbd5154256a99c06199b2a9f2e2de2e01aeafdf0eff15acaf source_ref=c1c2b9ed991a072e6f2783f4adee6e8e49fa2f32 role=change-detection -->
Computes dependency cascade analysis to determine which files and symbols need regeneration after source changes.

- **CascadeResult**: dataclass containing affected files, cascaded symbols, and hop distances from change origins
- **compute_cascade()**: walks inbound reference graph up to specified depth, with hub detection to prevent excessive propagation
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/cascade:CascadeResult fingerprint=4427fc9e9b33bd6592de10605387006d37145125ccdcf08ffbaaff4711fb0c21 body_fp=0ec85f2f62a54c969d53ebb83aa75751251a342ae6d23e15c2d801935b133f7a source_ref=c1c2b9ed991a072e6f2783f4adee6e8e49fa2f32 role=change-detection -->
## `class CascadeResult`

Contains files and symbols needing regeneration after a dependency cascade from changed source files.

- `affected_files`: all files requiring regeneration, sorted alphabetically
- `changed_files`: original seed files that triggered the cascade
- `cascaded_from_change`: files pulled in by following inbound edges (subset of affected_files)
- `hop_by_file`: minimum hop distance from any seed file for each affected file
- `cascaded_qnames`: symbols reached by walking inbound edges (excludes seed-file symbols)
- `hop_by_qname`: minimum BFS distance from seed symbols for each cascaded symbol
- `file_by_cascaded_qname`: maps each cascaded symbol to its defining file path
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/cascade:compute_cascade fingerprint=8519ed9bd06d4dfad5495cde3895289ce7ff3011a537bb7ff9faa35cbc3fea8d body_fp=44938f70189c899cab4e799ebb9e8af221fe5414336d9067d679b55c7a5d3ec9 source_ref=c1c2b9ed991a072e6f2783f4adee6e8e49fa2f32 role=change-detection -->
## `def compute_cascade( *, changed_files: Iterable[str], store: Store, depth: int = 1, hub_threshold: int = 20, ) -> CascadeResult`

Walks inbound reference graph from changed files to find all files and symbols needing regeneration.

- `hub_threshold`: symbols with more inbound references are not expanded to prevent whole-codebase invalidation
- Returns BFS traversal with hop distances for prioritizing regeneration by proximity to changes
<!-- trie:end -->