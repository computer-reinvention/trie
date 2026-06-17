---
trie_version: 0.1.9
source: app/src/graph/doi.ts
file_fingerprint: d6540b3a9a770f5c9a683da23c8ad88bf0e4cc5fbd2dbc710f3466a0a2aba5c5
last_synced_at: '2026-06-17T16:39:16Z'
defines:
- kind: interface
  qualified_name: app/src/graph/doi:Adjacency
  lines: 12-15
- kind: function
  qualified_name: app/src/graph/doi:buildAdjacency
  lines: 18-33
- kind: function
  qualified_name: app/src/graph/doi:hopDistances
  lines: 36-64
- kind: interface
  qualified_name: app/src/graph/doi:AggregateBubble
  lines: 66-73
- kind: interface
  qualified_name: app/src/graph/doi:VisibleSet
  lines: 75-78
- kind: interface
  qualified_name: app/src/graph/doi:DoiParams
  lines: 80-93
- kind: function
  qualified_name: app/src/graph/doi:groupKeyOf
  lines: 95-96
- kind: function
  qualified_name: app/src/graph/doi:selectVisible
  lines: 103-156
- kind: type
  qualified_name: app/src/graph/doi:GroupCharacter
  lines: 160-160
- kind: interface
  qualified_name: app/src/graph/doi:ComponentGroup
  lines: 162-171
- kind: interface
  qualified_name: app/src/graph/doi:ComponentView
  lines: 175-178
- kind: function
  qualified_name: app/src/graph/doi:memberSubgroup
  lines: 181-193
- kind: function
  qualified_name: app/src/graph/doi:componentView
  lines: 195-248
incoming_refs: 7
outgoing_refs: 10
---
<!-- trie:section symbol=app/src/graph/doi:Adjacency fingerprint=3d45197dbaad54b6393b64cd65b0537c308f71040e4f43aee4799b893a28ccc6 body_fp=fc557028eace46f8f1fad1a17c6d4c8c91e20a6f4206d0e104e916896b067724 source_ref=a6bbeacd5389805f1da42cc0553b0e38f3b09a16 role=model -->
Holds an undirected adjacency index mapping each node qname to its set of neighbour qnames.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/doi:buildAdjacency fingerprint=c1006248c580628264f52588d2eccf90645d773fb5f848715dad272fc96e601f body_fp=be43b73c0c125d05d29266900b24aa5f2216145b14cf53f95e0c5e17d1eccfdb source_ref=a6bbeacd5389805f1da42cc0553b0e38f3b09a16 role=util -->
Build an undirected `Adjacency` index from a flat directed edge list by inserting both directions for each edge.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/doi:hopDistances fingerprint=b2c82016d0e2006b31ab2af96e572228072d47cc885d4efb1a58e3798302af1f body_fp=948ec7cfe1222c342bc7250c90a6c504c2030a8c0a33fa7e0ff08d0a737d8287 source_ref=a6bbeacd5389805f1da42cc0553b0e38f3b09a16 role=domain -->
BFS hop distances from a focus set across `adj`, returning a map of qname → distance capped at `maxHops`.

- `focus` — seed nodes assigned distance 0; duplicates ignored.
- `maxHops` — nodes beyond this hop count are not added to the result map.
- Returns only reachable nodes within `maxHops`; unreachable nodes are absent.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/doi:AggregateBubble fingerprint=a83bb1c857e0a8ca3bfbe650fbfb88242603fae15d69867dc4b6beb755d06560 body_fp=82fc91a01c7121acbc36bf6d508712d6446a930213c834217e746f6e06c402eb source_ref=a6bbeacd5389805f1da42cc0553b0e38f3b09a16 role=model -->
Represents a synthetic "+N" placeholder node for a group of real nodes folded out of the visible set.

- `id`: synthetic node id formatted as `+agg:{axis}:{key}`, never a real qname
- `key`: the role or subsystem label shared by all folded members
- `members`: qnames of folded nodes, used to expand the aggregate on click
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/doi:VisibleSet fingerprint=1f6d432fa64b1a28e3f7ccdf4adc5faaf046314e46443863c84f2da696e157a2 body_fp=299bdb16b993a6dea943fd2d1990bd91966b63df5ce41eb35a2907e942a48983 source_ref=a6bbeacd5389805f1da42cc0553b0e38f3b09a16 role=model -->
Return type of `selectVisible`: holds real nodes to render and synthetic aggregate placeholders for folded nodes.

- `nodes`: real nodes selected by DOI, capped at `budget`
- `aggregates`: one `AggregateBubble` per group with at least one folded member
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/doi:DoiParams fingerprint=63cb6bf1153019467b8111ba2247297d9ae22ad6eb45098f145a0beaa8f76ed2 body_fp=c6c39cc67b8fe42e6a12b1d03e50cc0ae1367ea84ab560314d4750e89f24908f source_ref=a6bbeacd5389805f1da42cc0553b0e38f3b09a16 role=model -->
Parameters bag consumed by `selectVisible` to control DOI-based node selection.

- `budget`: maximum real nodes allowed on screen.
- `salienceFloor`: minimum salience for a node to qualify without focus proximity.
- `focus`: qnames of selected/agent nodes; empty triggers whole-system view.
- `distancePenalty`: DOI reduction per hop from focus; defaults to `0.25`.
- `restrictToGroups`: when set, limits candidates to nodes whose group key (on `axis`) is in this set.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/doi:groupKeyOf fingerprint=168dd0e826be3da99d86f891811d330fe0c6d9d922deef3dfb75759aabb9c609 body_fp=52937fbac241a44ae984e4423d67bc5efcb962a1ddaa616487809a29c924761c source_ref=a6bbeacd5389805f1da42cc0553b0e38f3b09a16 role=util -->
Return the group key of a `SystemModelNode` for the given axis: `n.role` (falling back to `"untagged"`) for `"role"`, or `n.subsystem` otherwise.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/doi:selectVisible fingerprint=18d76f136b6957be7c90f53b41560cf64f97f7156dc7d221ff630fcc12300e6f body_fp=248311d98c3d392c488c0864455924cf78eb4b8ab558fb5cae4697b30bedce00 source_ref=a6bbeacd5389805f1da42cc0553b0e38f3b09a16 role=domain -->
Select at most `budget` real nodes by DOI score and fold all remaining production nodes into per-group `AggregateBubble` entries.

- `params.distancePenalty` defaults to `0.25` if omitted.
- `restrictToGroups` drops the salience floor to `0` so all members in scope compete equally.
- Focus nodes always qualify regardless of salience floor.
- Nodes unreachable from focus (when focus is non-empty) receive a fixed distance term of `1.0`.
- Tie-breaks on equal DOI resolve by raw salience descending.
- Returns `VisibleSet` with `nodes` (≤ `budget`) and `aggregates` (one per group with folded members).
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/doi:GroupCharacter fingerprint=9844fd2fe522ebc3af099f7205884bc7021938d658df94cbc7805f1f4f7ea9ab body_fp=d18b98b6d5a5f53f511daa2eda38ee7b1ec711a058e1f4e4681afb7bedbbbd5f source_ref=a6bbeacd5389805f1da42cc0553b0e38f3b09a16 role=model -->
Discriminated union classifying how a `ComponentGroup` expands: entry-facing, foundational, or neither.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/doi:ComponentGroup fingerprint=deb5bee55c0390fe4d9ba0dccf0d42c8fe7fbb79580699fe523948a4d924ba47 body_fp=ea53d34f6586aef72b1c9e4fc64754db306df02751d3c2a256430028f82d8ded source_ref=a6bbeacd5389805f1da42cc0553b0e38f3b09a16 role=model -->
Describes a single axis-group in the L0 component view, carrying layout and character metadata.

- `avgDepth`: mean depth-from-door of members; small = entry side, large = foundation side.
- `order`: normalised `[0, 1]` position; drives left-to-right layout ordering.
- `character`: classifies the group as `"entry"`, `"foundation"`, or `"mixed"` to control expand behaviour.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/doi:ComponentView fingerprint=5d59e2372143cc2d459a587b38652919ec5543b8ef30dcb841e6e565ecf3d51b body_fp=d1ad20f012b182f4b29dfde9f190428b1861a5061ddd7adba4b947fdfd2dc4a4 source_ref=a6bbeacd5389805f1da42cc0553b0e38f3b09a16 role=model -->
Holds the L0 component overview: one `ComponentGroup` per axis-group and the thresholded inter-group flows.

- `flows`: weighted directed edges between group keys, pre-filtered by threshold.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/doi:memberSubgroup fingerprint=1d5bd7756fbfd6eefb3df8a44cfe007ea5c8eb9e266fc488e8748ef4fd58a988 body_fp=d6976d630fec364edfb20877500f79e446ffc76925ba07b120e80446e19fb1dc source_ref=a6bbeacd5389805f1da42cc0553b0e38f3b09a16 role=util -->
Return the sub-group label for a node inside an expanded container, varying by `grouping` strategy.

- `grouping="owningClass"`: method nodes return their class name extracted from `qname`; all others return `"(module-level)"`
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/doi:componentView fingerprint=b28db0f9cefb37bcf8332f04e4623aa623dc5c49a33a31be490e049d7a9fe911 body_fp=c1703ed1f67b9eda9389fd3b3d4cb17a6b7e0b595364a19f3c2d834997e93864 source_ref=a6bbeacd5389805f1da42cc0553b0e38f3b09a16 role=domain -->
Build the L0 `ComponentView` from a `SystemModel`, deriving per-group character, depth-normalized order, and inter-group flows for the given axis.

- `axis` — determines grouping key: `"role"` uses `n.role`, otherwise `n.subsystem`.
- `order` — normalized `[0,1]` float; low = entry side, high = foundation side.
- `character` — `"entry"` if door ratio ≥ 0.25 or key is `entrypoint`/`api`; `"foundation"` if bedrock ratio ≥ 0.15 or key is `util`/`model`/`config`; else `"mixed"`.
- Test nodes (`is_test`) are excluded from depth and bedrock aggregation.
<!-- trie:end -->