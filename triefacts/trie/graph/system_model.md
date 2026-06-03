---
trie_version: 0.1.5
source: trie/graph/system_model.py
file_fingerprint: cc1c8c516fd7c1a0ff05f20d295f0ea219fd60f0becfdeb3e80db74a330bf3ef
last_synced_at: '2026-06-03T21:12:09Z'
description: Assemble a high-level *system model* from the symbol graph.
defines:
- kind: module
  qualified_name: trie/graph/system_model:__module__
  lines: 1-523
- kind: constant
  qualified_name: trie/graph/system_model:_ENTRY_DECORATOR_RE
  lines: 34-39
- kind: constant
  qualified_name: trie/graph/system_model:_NON_PRODUCTION_PREFIXES
  lines: 43-43
- kind: class
  qualified_name: trie/graph/system_model:SystemNode
  lines: 47-63
- kind: class
  qualified_name: trie/graph/system_model:RoleFlow
  lines: 67-70
- kind: class
  qualified_name: trie/graph/system_model:RoleSummary
  lines: 74-78
- kind: class
  qualified_name: trie/graph/system_model:SystemModel
  lines: 82-86
- kind: function
  qualified_name: trie/graph/system_model:_is_production
  lines: 94-95
- kind: function
  qualified_name: trie/graph/system_model:_load_raw
  lines: 98-140
- kind: function
  qualified_name: trie/graph/system_model:_pyproject_entry_targets
  lines: 143-167
- kind: function
  qualified_name: trie/graph/system_model:_betweenness
  lines: 175-213
- kind: function
  qualified_name: trie/graph/system_model:_communities
  lines: 216-246
- kind: function
  qualified_name: trie/graph/system_model:_depth_from_entries
  lines: 249-265
- kind: function
  qualified_name: trie/graph/system_model:_has_entry_decorator
  lines: 273-274
- kind: function
  qualified_name: trie/graph/system_model:_classify
  lines: 277-313
- kind: function
  qualified_name: trie/graph/system_model:_salience
  lines: 316-344
- kind: function
  qualified_name: trie/graph/system_model:build_system_model
  lines: 352-481
- kind: function
  qualified_name: trie/graph/system_model:system_model_to_dict
  lines: 484-522
incoming_refs: 9
outgoing_refs: 0
---
<!-- trie:section symbol=trie/graph/system_model:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=2cb19fd18d8441ca0d0b19bc931dd683fa8f1a07659292fe8e8f7aa25fa78723 source_ref=8a6a7770f2c56a96f3cc380d783818f7deedc2b1 -->
Transforms raw symbol graph data from the store into a complete system model for visualization.

- Computes graph metrics (betweenness centrality, community detection, depth from entry points)
- Classifies nodes as door/hub/bedrock/exit/orphan/normal using multi-signal rubric
- Calculates salience scores to determine what symbols are worth drawing
- Aggregates role-to-role flows and generates landmark lists for hierarchical views
- Uses hand-rolled algorithms (Brandes betweenness, label propagation) to stay dependency-free
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_ENTRY_DECORATOR_RE fingerprint=70f0e823bd31abcfe30bab355b5cd64d9e1dfef2c4937205758ff6a32fe9bce1 body_fp=8da67480a0e09302ef08bd39f277d3c8b21c82154c031083f0a5dc802243f7ba source_ref=8a6a7770f2c56a96f3cc380d783818f7deedc2b1 -->
Regex pattern matching decorator syntax that marks framework-registered entry points.

- Matches CLI commands, HTTP routes, MCP tools, and task decorators
- Used to identify symbols callable from outside the system
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_NON_PRODUCTION_PREFIXES fingerprint=f5275496ed74668667104761a71f0b59ac51be595d98854992e7d17abacf1074 body_fp=17a64e2c7c3bfcba18958d03ef399ea5df9f7a4f8741874e69cf9219d8f6a57b source_ref=8a6a7770f2c56a96f3cc380d783818f7deedc2b1 -->
Tuple of file path prefixes that identify non-production code directories.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:SystemNode fingerprint=52de175dc75cdf812bf03ad19966ddcca1a975fb41f0fdcb96c89e1d8579b2ec body_fp=a84a49ba212a86f4ee2a20837f6cfe84d9eeb91c2f513c14cb8a1409bee3e61f source_ref=8a6a7770f2c56a96f3cc380d783818f7deedc2b1 -->
Represents a node in the system model with computed metrics and architectural classification.

- `cls`: architectural class (door/hub/bedrock/exit/orphan/normal)
- `salience`: importance score 0..1 for drawing priority and node size
- `betweenness`: normalized centrality score showing bottleneck potential
- `depth`: BFS distance from nearest entry point (-1 if unreachable)
- `community`: connectivity cluster identifier
- `prod_inbound`: caller count excluding test/script files
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:RoleFlow fingerprint=ebebb70e07c576017b54df308fda7e402e2eb0b28d38004940a0af4c7e7044b7 body_fp=2490e3b3a1e75af65f4c26c1f61d8824802adf2605bd407b35d1502ae7e952f2 source_ref=8a6a7770f2c56a96f3cc380d783818f7deedc2b1 -->
Represents a weighted edge between two architectural roles in the system model.

- `weight`: count of call edges that cross from source role to target role
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:RoleSummary fingerprint=c623069cc80db0541a47ccf6678b572c8cf98171c4d84bf5cf21ac5004b8a3c4 body_fp=fdda735203f3f7613efc8d8f7717a3a84a7838e6ab6272178693a0b5ad708441 source_ref=8a6a7770f2c56a96f3cc380d783818f7deedc2b1 -->
Represents aggregated statistics for a single role across all symbols in the system model.

- `role`: the role tag (e.g., "api", "domain") or "untagged"
- `count`: total symbols with this role
- `door_count`: how many of these symbols are classified as entry points
- `hub_count`: how many are classified as highly-connected hubs
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:SystemModel fingerprint=950c806117c79f1e596e24b9a21039eea60b1dd808fc25d7410882d91c118216 body_fp=e16696c34a909483b17ed4f5e2fac2ef37c2e7dbbf55c29cd7b28ca42b3d59ca source_ref=8a6a7770f2c56a96f3cc380d783818f7deedc2b1 -->
Contains the complete processed system model for graph visualization.

- `nodes`: all symbols with computed classification, metrics, and salience scores
- `roles`: aggregated role statistics with door/hub counts per role
- `role_flows`: cross-role call flow edges with weights
- `landmarks`: most salient symbol qnames for the primary view (default 60)
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_is_production fingerprint=8c88f563ae4cfd55c03257cf6eaf41cd7b853e29fbb90217984156552bd80b48 body_fp=356df121573881dd5600b862f7d3e050a5cea781ff86a5c151963d389e2b09ee source_ref=8a6a7770f2c56a96f3cc380d783818f7deedc2b1 -->
Returns true if the file path does not start with test/script directory prefixes.

- Uses the `_NON_PRODUCTION_PREFIXES` tuple to exclude tests/, test/, scripts/, script/, examples/ paths
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_load_raw fingerprint=2ea65302fe96b5727e1df63f530ab2518e1adea30ce63f60789a956708047fb3 body_fp=58473d82fcb08bff80dca1d501a603c45b0e2ba665b1e03c7bcf59ce5ffb2abd source_ref=8a6a7770f2c56a96f3cc380d783818f7deedc2b1 -->
Extracts symbols and call edges from the Store, returning node dictionaries and edge tuples by qualified name.

- Returns tuple of (nodes dict keyed by qname, edge list of qname pairs)
- Filters out self-edges and edges to missing symbols
- Joins symbols with triefact_sections for role/boundary/one_liner metadata
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_pyproject_entry_targets fingerprint=a11c85301eaf43b809aaa2ab8e5c5242ba7b5ee238f2186945d92249d239b24b body_fp=2f645a8ad9ff26003201fda71c9f491caf86f80f6690c23bccb7985127a3941c source_ref=8a6a7770f2c56a96f3cc380d783818f7deedc2b1 -->
Parses `[project.scripts]` console entry targets from pyproject.toml into trie qname format.

- Returns qnames like `trie/cli:app` from pyproject entries like `trie = "trie.cli:app"`
- Returns empty set if pyproject.toml missing or parsing fails
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_betweenness fingerprint=22a6cf5645adf12a9bae6fff3f53578a3dbe9863be97c28656d714569c0908c3 body_fp=00194aa082bfba770dc4440f8ced591af625c3d4ebace16ea488f16fc1b35e90 source_ref=8a6a7770f2c56a96f3cc380d783818f7deedc2b1 -->
Calculates Brandes' betweenness centrality on directed graph, normalized to 0..1 by maximum value.

- `qnames`: all node identifiers in the graph
- `adj`: adjacency list mapping each node to its outgoing neighbors
- Returns: centrality score per node, measuring bottleneck importance
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_communities fingerprint=0ec2cc11c0d36eef2e5c1bd6c17f682fca11aebd403030b510915b1511b9ed85 body_fp=0d72ca62de80c330ade3f3ca42bee9017b80f0d7910a77010ea467a96214f172 source_ref=8a6a7770f2c56a96f3cc380d783818f7deedc2b1 -->
Detects connectivity communities in an undirected graph using deterministic label propagation with tie-breaking.

- Processes nodes in sorted order and breaks ties by smallest label ID for determinism
- Caps iterations at 20 as a safety net though convergence is typically fast
- Compacts final community labels to contiguous IDs starting from 0
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_depth_from_entries fingerprint=ba121a390b707caa7d4d1de657f41593c7921d4f3aa39439b9ca3eec38a07b91 body_fp=d6f1131772a6c1ca2b6b4d4d272011f1219cde03318bb1ec084289556ac8557b source_ref=8a6a7770f2c56a96f3cc380d783818f7deedc2b1 -->
Computes BFS depth from entry points to all reachable symbols via caller-to-callee edges.

- Returns depth dictionary mapping qnames to hop count; -1 for unreachable symbols
- Entry points start at depth 0, their direct callees at depth 1, etc.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_has_entry_decorator fingerprint=668c8654d8a205435c3178f8951d885fc2ca542e12286690bdd4bf1a674f0296 body_fp=705580d29ae745ed2bf5d7385456d455694b5db33df80cd8c7b9d965a3152670 source_ref=8a6a7770f2c56a96f3cc380d783818f7deedc2b1 -->
Checks if a symbol has decorators matching framework entry-point patterns.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_classify fingerprint=9a4665883734fad5cddbdb905e81ddc01961d86c9829cd0ffad9d303b75ab995 body_fp=786e8a88304f87f679d6b29465a6db6bbaa65a8c6d72e4cc0e502856844dca8b source_ref=8a6a7770f2c56a96f3cc380d783818f7deedc2b1 -->
Assigns a skeleton class to a symbol using multi-signal heuristics across decorators, boundaries, and connectivity patterns.

- Returns one of: door, exit, hub, bedrock, orphan, normal
- Uses precedence order: door beats all others, then exit, hub, bedrock, orphan, normal
- Door detection: entry decorators, pyproject targets, boundary="entry", or public+no-prod-inbound+has-outbound
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_salience fingerprint=15c440e011411997548d9a93567f02dc783cfe782e5e423e57a79178bc127ecf body_fp=a46ef22c2b72fa890ebe7fbc0183665f869c742b39170fc7b1ae75b03d7e4263 source_ref=8a6a7770f2c56a96f3cc380d783818f7deedc2b1 -->
Calculates importance score (0..1) for a system node by combining class weight, degree centrality, and betweenness.

- **cls**: Node classification (door=0.85, hub=0.8, exit=0.55, bedrock=0.45, normal=0.2, orphan=0.1 base weights)
- **prod_inbound**: Production callers count (excluding tests/scripts)
- **outbound**: Callees count for degree calculation
- **betweenness**: Normalized betweenness centrality value
- **is_public**: Adds 0.05 bonus if symbol is public
- **inbound_hi**: High-threshold denominator for degree saturation
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:build_system_model fingerprint=4af5e939df6425db9ed3d9c62c07ddc07991924d8efa672663d4f9b8111ed722 body_fp=535801be0cd94b04aadf077985d35a523451f317f3fe8753efc3055b47062cbe source_ref=8a6a7770f2c56a96f3cc380d783818f7deedc2b1 -->
Computes a complete system model from the store by classifying symbols, calculating graph metrics, and aggregating role flows.

- `landmark_limit`: maximum number of highest-salience symbols to include in landmarks list
- Returns SystemModel with classified nodes, role summaries, cross-role flows, and landmark symbols
- Calculates betweenness centrality, community detection, and depth-from-entries for each symbol
- Classifies symbols as door/hub/bedrock/exit/orphan/normal using multi-signal rubric
- Aggregates symbols by role with door/hub counts and inter-role call flows
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:system_model_to_dict fingerprint=6001dc8d07848e4680df33b0ad9451270d8700d524dc9b41985c91f3967c558d body_fp=df4be4e43045573ef72d1119d7817bf15a3a285208dc4bec72d731a4bfa3dc99 source_ref=8a6a7770f2c56a96f3cc380d783818f7deedc2b1 -->
Serializes a SystemModel to the JSON shape that the desktop endpoint returns.

- Transforms field names for web API compatibility (inbound → inbound_count, etc.)
- Preserves all node metadata, role summaries, and flow relationships
- Returns ready-to-serialize dictionary matching frontend expectations
<!-- trie:end -->