---
trie_version: 0.1.5
source: trie/graph/system_model.py
file_fingerprint: d0e7f82dbdc16aa66cf4d458ba2c2407f3af301110d874e1c463d94ae0dacc23
last_synced_at: '2026-06-04T00:38:07Z'
description: Assemble a high-level *system model* from the symbol graph.
defines:
- kind: module
  qualified_name: trie/graph/system_model:__module__
  lines: 1-760
- kind: constant
  qualified_name: trie/graph/system_model:_ENTRY_DECORATOR_RE
  lines: 50-55
- kind: constant
  qualified_name: trie/graph/system_model:_TEST_PREFIXES
  lines: 59-59
- kind: constant
  qualified_name: trie/graph/system_model:_NON_PRODUCTION_PREFIXES
  lines: 60-60
- kind: constant
  qualified_name: trie/graph/system_model:_BETWEENNESS_EXACT_MAX
  lines: 64-64
- kind: constant
  qualified_name: trie/graph/system_model:_BETWEENNESS_PIVOTS
  lines: 65-65
- kind: constant
  qualified_name: trie/graph/system_model:_MODEL_CACHE_VERSION
  lines: 68-68
- kind: class
  qualified_name: trie/graph/system_model:SystemNode
  lines: 72-92
- kind: class
  qualified_name: trie/graph/system_model:GroupFlow
  lines: 96-99
- kind: class
  qualified_name: trie/graph/system_model:GroupSummary
  lines: 103-107
- kind: class
  qualified_name: trie/graph/system_model:ComponentAxis
  lines: 111-116
- kind: class
  qualified_name: trie/graph/system_model:SystemModel
  lines: 120-125
- kind: function
  qualified_name: trie/graph/system_model:_is_test
  lines: 133-134
- kind: function
  qualified_name: trie/graph/system_model:_is_production
  lines: 137-138
- kind: function
  qualified_name: trie/graph/system_model:_subsystem_of
  lines: 141-144
- kind: function
  qualified_name: trie/graph/system_model:_owning_class
  lines: 147-157
- kind: function
  qualified_name: trie/graph/system_model:_load_raw
  lines: 165-204
- kind: function
  qualified_name: trie/graph/system_model:_pyproject_entry_targets
  lines: 207-229
- kind: function
  qualified_name: trie/graph/system_model:_betweenness
  lines: 237-283
- kind: function
  qualified_name: trie/graph/system_model:_communities
  lines: 286-308
- kind: function
  qualified_name: trie/graph/system_model:_depth_from_entries
  lines: 311-327
- kind: function
  qualified_name: trie/graph/system_model:_layered_layout
  lines: 335-364
- kind: function
  qualified_name: trie/graph/system_model:_has_entry_decorator
  lines: 372-373
- kind: function
  qualified_name: trie/graph/system_model:_classify
  lines: 376-416
- kind: function
  qualified_name: trie/graph/system_model:_salience
  lines: 419-442
- kind: function
  qualified_name: trie/graph/system_model:_build_axis
  lines: 450-498
- kind: function
  qualified_name: trie/graph/system_model:build_system_model
  lines: 506-645
- kind: function
  qualified_name: trie/graph/system_model:system_model_to_dict
  lines: 648-697
- kind: function
  qualified_name: trie/graph/system_model:_graph_fingerprint
  lines: 705-717
- kind: function
  qualified_name: trie/graph/system_model:build_system_model_cached
  lines: 720-759
incoming_refs: 16
outgoing_refs: 0
---
<!-- trie:section symbol=trie/graph/system_model:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=2cb19fd18d8441ca0d0b19bc931dd683fa8f1a07659292fe8e8f7aa25fa78723 source_ref=8a6a7770f2c56a96f3cc380d783818f7deedc2b1 role=graph-database -->
Transforms raw symbol graph data from the store into a complete system model for visualization.

- Computes graph metrics (betweenness centrality, community detection, depth from entry points)
- Classifies nodes as door/hub/bedrock/exit/orphan/normal using multi-signal rubric
- Calculates salience scores to determine what symbols are worth drawing
- Aggregates role-to-role flows and generates landmark lists for hierarchical views
- Uses hand-rolled algorithms (Brandes betweenness, label propagation) to stay dependency-free
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_ENTRY_DECORATOR_RE fingerprint=70f0e823bd31abcfe30bab355b5cd64d9e1dfef2c4937205758ff6a32fe9bce1 body_fp=8da67480a0e09302ef08bd39f277d3c8b21c82154c031083f0a5dc802243f7ba source_ref=8a6a7770f2c56a96f3cc380d783818f7deedc2b1 role=graph-database -->
Regex pattern matching decorator syntax that marks framework-registered entry points.

- Matches CLI commands, HTTP routes, MCP tools, and task decorators
- Used to identify symbols callable from outside the system
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_TEST_PREFIXES fingerprint=8a8ab89635d28eb23e385a89b6efc6486d7e695d87758b6fead8a03724c5305e body_fp=9c7542824b996a7849bc2611280533f26a73dd3a1df73ab92105e6b357f3a3ce source_ref=53916a96e0fd72b42dc0aa3b935f9f016be780e4 role=graph-database -->
Path prefixes identifying test file locations for exclusion from production models.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_NON_PRODUCTION_PREFIXES fingerprint=15a3a7cc92e0fcf4f32325c72ed6280d74ca4b500809bddec731a3ce56796676 body_fp=17a64e2c7c3bfcba18958d03ef399ea5df9f7a4f8741874e69cf9219d8f6a57b source_ref=53916a96e0fd72b42dc0aa3b935f9f016be780e4 role=graph-database -->
Tuple of file path prefixes that identify non-production code directories.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_BETWEENNESS_EXACT_MAX fingerprint=587700669c4fed01249fec87717a1f475082a3c8e460d250a4c3e87ff1568f91 body_fp=3853deea8c2e1735f4926abfa218f6427133d5703ff38272c73572e0741c6d19 source_ref=53916a96e0fd72b42dc0aa3b935f9f016be780e4 role=graph-database -->
Node count threshold above which betweenness centrality switches from exact Brandes algorithm to sampled approximation.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_BETWEENNESS_PIVOTS fingerprint=6763e5dcecb260985859aeaf225e3451643d832164b76ff52b4e194fae4844d6 body_fp=26f7329f5caabde3a11f8c798e97f402b0374d2b081893bad981fc191e6efcc3 source_ref=53916a96e0fd72b42dc0aa3b935f9f016be780e4 role=graph-database -->
Number of pivot sources to sample when computing approximate betweenness centrality for large graphs.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_MODEL_CACHE_VERSION fingerprint=f3fc2b11ab776a9f976183f492d503c835a143a85282bfada1936f18487d3642 body_fp=42d923b7a9ec94a1e3dacc8b83e35ea703a437f6d3fe9edcc4b5ac71bfbabf23 source_ref=53916a96e0fd72b42dc0aa3b935f9f016be780e4 role=graph-database -->
Cache format version constant that invalidates all cached models when incremented.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:SystemNode fingerprint=a6ef5dc13efba272de1e6f3a7a4ab80486159a2b2a4f91748b9a2ec8a214d918 body_fp=d9fc1983fc7fd176a775291e6b90e30aa2bd435d085352d7b2bbd43583f415a8 source_ref=53916a96e0fd72b42dc0aa3b935f9f016be780e4 role=graph-database -->
Represents a node in the system model with computed metrics and architectural classification.

- `cls`: architectural class (door/hub/bedrock/exit/orphan/normal/internal/test)
- `salience`: importance score 0..1 for drawing priority and node size
- `betweenness`: normalized centrality score showing bottleneck potential
- `depth`: BFS distance from nearest entry point (-1 if unreachable)
- `community`: connectivity cluster identifier
- `prod_inbound`: caller count excluding test/script files
- `subsystem`: top-level directory grouping for component analysis
- `x`: precomputed horizontal layout position
- `y`: precomputed vertical layout position
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:GroupFlow fingerprint=ebebb70e07c576017b54df308fda7e402e2eb0b28d38004940a0af4c7e7044b7 body_fp=ec338b149bd16ee9e69064e73b3d7774658a5bf141da26dab9a6562ec0d36e0a source_ref=53916a96e0fd72b42dc0aa3b935f9f016be780e4 role=graph-database -->
Represents aggregated call flow between two component groups in the system model.

- `weight` — number of individual call edges crossing this group boundary
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:GroupSummary fingerprint=84d082dd04a5b929af82a2dbbe3a8fb0b2c9156efeb18fc15776bcccfd9a688b body_fp=d6ee823d2210bc2609bcd08874ad66fc224290581d0bb4389ece6dcc7c47689e source_ref=53916a96e0fd72b42dc0aa3b935f9f016be780e4 role=graph-database -->
Represents aggregated statistics for a component group in the system model.

- `key`: role name or subsystem path identifying the group
- `count`: total number of nodes in this group
- `door_count`: number of entry point nodes in this group
- `hub_count`: number of highly-connected hub nodes in this group
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:ComponentAxis fingerprint=8e735c3512a1b4b059bee218fb138784eb4b908887073fcf005cb104d80d31d3 body_fp=d4a95d3890b1fe2a51530dd3a4f9afbf2c05b1b2c631fe986a4fa264bfc24e39 source_ref=53916a96e0fd72b42dc0aa3b935f9f016be780e4 role=graph-database -->
Represents one L0 grouping axis containing component groups and inter-group flow.

- `axis`: Either "role" or "subsystem" grouping type
- `groups`: Summary of each component group with counts
- `flows`: Inter-group call flows above threshold
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:SystemModel fingerprint=ddc9e5cb1c13a921debfe4548f483585f923d1bc2a8a3068f87fb63d822af508 body_fp=c9665a9c9809bb176b378f05b6283818dd823cea6bef47c6c03efe600fef1ce3 source_ref=53916a96e0fd72b42dc0aa3b935f9f016be780e4 role=graph-database -->
Contains the complete processed system model for graph visualization.

- `nodes`: production symbols with computed classification, metrics, and salience scores
- `test_nodes`: test symbols, kept separate for frontend toggle functionality
- `axes`: component groupings by "role" and "subsystem" with aggregated flows
- `landmarks`: most salient symbol qnames for the primary view
- `stats`: computed graph statistics including node counts and class distributions
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_is_test fingerprint=5285ee47dd039db6e5d02c8d495f24af33c295004cd26f30a9212ba6cf171a88 body_fp=b9c13b6c6389d15e9976f1f4577720fa8dcacf4850a6d087d60c62df621f5ea1 source_ref=53916a96e0fd72b42dc0aa3b935f9f016be780e4 role=test-infrastructure -->
Returns whether a file path indicates a test file by checking if it starts with test directory prefixes.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_is_production fingerprint=8c88f563ae4cfd55c03257cf6eaf41cd7b853e29fbb90217984156552bd80b48 body_fp=356df121573881dd5600b862f7d3e050a5cea781ff86a5c151963d389e2b09ee source_ref=8a6a7770f2c56a96f3cc380d783818f7deedc2b1 role=graph-database -->
Returns true if the file path does not start with test/script directory prefixes.

- Uses the `_NON_PRODUCTION_PREFIXES` tuple to exclude tests/, test/, scripts/, script/, examples/ paths
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_subsystem_of fingerprint=e509c721b18b3c9e093bdb9e34d4dd1c47ca07a415a310e558c143402c959052 body_fp=873ed29be4b967b2cb8876012a8bfacd77f6bac0acf70c698df7e51ec032e919 source_ref=53916a96e0fd72b42dc0aa3b935f9f016be780e4 role=graph-database -->
Extract subsystem identifier from a file path by taking the first two path segments.

- Returns the first segment only if the path has fewer than two segments
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_owning_class fingerprint=2bbb40567385cd698a13bfc71c3a1c8584dccf5d340de0c8ff527472134359db body_fp=1364c7415beb02cc016d1ce8db8ae37d2eb5c1a9a3b0bf44561f8e8c91f82e2b source_ref=53916a96e0fd72b42dc0aa3b935f9f016be780e4 role=graph-database -->
Extracts the owning class qualified name from a method's qualified name.

- Returns `None` if the qualified name has no module separator or local part has no class
- Strips the method name from the local part to get the class name
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_load_raw fingerprint=202a814f55d86fc3addc92ff01cfccfb49077f3ce68498802b62299c431b613d body_fp=2b16fbedbf05118b2ed99f49afed25d622d6cbc9de11bc814452342e647e93ba source_ref=53916a96e0fd72b42dc0aa3b935f9f016be780e4 role=graph-database -->
Extracts symbols and call edges from the Store, returning node dictionaries and edge tuples by qualified name.

- Returns tuple of (nodes dict keyed by qname, edge list of qname pairs)
- Filters out module container nodes, self-edges and edges to missing symbols
- Joins symbols with triefact_sections for role/boundary/one_liner metadata
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_pyproject_entry_targets fingerprint=4d29875a2185d55700cc7554a105ef2386331d16ed93758e6f867173cf700b96 body_fp=2f645a8ad9ff26003201fda71c9f491caf86f80f6690c23bccb7985127a3941c source_ref=53916a96e0fd72b42dc0aa3b935f9f016be780e4 role=config-management -->
Parses `[project.scripts]` console entry targets from pyproject.toml into trie qname format.

- Returns qnames like `trie/cli:app` from pyproject entries like `trie = "trie.cli:app"`
- Returns empty set if pyproject.toml missing or parsing fails
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_betweenness fingerprint=8a622a73abf04b7ccc7626d3b8b8da314028dd47196cdc36f70fc32654a18201 body_fp=a2d27c6c2f834a18b85f3e9d7cf0d8ff5006247283a322ae0707153f779b0d8d source_ref=53916a96e0fd72b42dc0aa3b935f9f016be780e4 role=graph-database -->
Calculates Brandes' betweenness centrality, using sampling approximation for graphs above 3000 nodes to maintain performance.

- `qnames`: all node identifiers in the graph  
- `adj`: adjacency list mapping each node to its outgoing neighbors
- Returns: centrality score per node normalized 0..1, measuring bottleneck importance
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_communities fingerprint=2126a3cf5bbd8df4a49fa3ef96cfd96fbff8d4c5543212476d9989337da6acfd body_fp=0d72ca62de80c330ade3f3ca42bee9017b80f0d7910a77010ea467a96214f172 source_ref=53916a96e0fd72b42dc0aa3b935f9f016be780e4 role=graph-database -->
Detects connectivity communities in an undirected graph using deterministic label propagation with tie-breaking.

- Processes nodes in sorted order and breaks ties by smallest label ID for determinism
- Caps iterations at 20 as a safety net though convergence is typically fast
- Compacts final community labels to contiguous IDs starting from 0
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_depth_from_entries fingerprint=6733e3c98482310a1e62d3bda5b559f897bcfa8b862c0b163b062900b9a6d615 body_fp=d6f1131772a6c1ca2b6b4d4d272011f1219cde03318bb1ec084289556ac8557b source_ref=53916a96e0fd72b42dc0aa3b935f9f016be780e4 role=graph-database -->
Computes BFS depth from entry points to all reachable symbols via caller-to-callee edges.

- Returns depth dictionary mapping qnames to hop count; -1 for unreachable symbols
- Entry points start at depth 0, their direct callees at depth 1, etc.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_layered_layout fingerprint=a0dd41c702ef88e4f8a779bcd53e9fb0023bd02900a1f892a1699c27412c8a43 body_fp=809162f71292a66a3badb68f9d82dfab6cc905dbe207af8b67620bbc065c46a8 source_ref=53916a96e0fd72b42dc0aa3b935f9f016be780e4 role=graph-database -->
Computes stable 2D layout positions for graph nodes with vertical layers by depth and horizontal subsystem grouping.

- Positions doors at top, deeper nodes below in 180-unit vertical bands
- Groups nodes by subsystem within each depth layer, spread horizontally with 90-unit gaps
- Places unreachable nodes (depth -1) in bottom band
- Returns rounded (x, y) coordinates as stable seed for client force-directed layout
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_has_entry_decorator fingerprint=668c8654d8a205435c3178f8951d885fc2ca542e12286690bdd4bf1a674f0296 body_fp=705580d29ae745ed2bf5d7385456d455694b5db33df80cd8c7b9d965a3152670 source_ref=8a6a7770f2c56a96f3cc380d783818f7deedc2b1 role=graph-database -->
Checks if a symbol has decorators matching framework entry-point patterns.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_classify fingerprint=514962a634ddb2ab5ed2f746f20a713cb1fb67b2cc5bf634db0ca6644bc80571 body_fp=2ee85a299f40cf55f703c4ea51836160baa5080c6173e7d18e4fa4034c343634 source_ref=53916a96e0fd72b42dc0aa3b935f9f016be780e4 role=graph-database -->
Assigns a skeleton class to a symbol using multi-signal heuristics across decorators, boundaries, and connectivity patterns.

- Returns one of: door, exit, hub, bedrock, internal, orphan, normal
- Uses precedence order: door beats all others, then exit, hub, bedrock, internal (blind-spot rule), orphan, normal  
- Door detection: entry decorators, pyproject targets, boundary="entry", or public+no-prod-inbound+has-outbound
- Blind-spot rule: zero-edge methods whose owning class is connected return "internal" instead of "orphan"
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_salience fingerprint=d035a0a3e0bef5a6bf235ebf49c6a2d5bb429942f9222690d8e37666d2503117 body_fp=fbf5e8371a13e9bef1ff00c2478d7c4b6b594efe56578aaa31b85c5b11f4ca00 source_ref=53916a96e0fd72b42dc0aa3b935f9f016be780e4 role=graph-database -->
Calculates importance score (0..1) for a system node by combining class weight, degree centrality, and betweenness.

- **cls**: Node classification (door=0.85, hub=0.8, exit=0.55, bedrock=0.45, normal=0.2, internal=0.18, orphan=0.1 base weights)
- **prod_inbound**: Production callers count (excluding tests/scripts)
- **outbound**: Callees count for degree calculation
- **betweenness**: Normalized betweenness centrality value
- **is_public**: Adds 0.05 bonus if symbol is public
- **inbound_hi**: High-threshold denominator for degree saturation
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_build_axis fingerprint=6801256783e05e16420858efdf2c72921c65a9b07a7baec091462046992f2c71 body_fp=cd0eefeedfe965957b659f0fcbab4c133facc37ce084166e096164d7bc03ba06 source_ref=53916a96e0fd72b42dc0aa3b935f9f016be780e4 role=graph-database -->
Aggregates production symbols into L0 component groups and computes thresholded inter-group flow for architecture visualization.

- Groups symbols by `key_of` mapping (role or subsystem), counting total nodes plus doors/hubs
- Flows keep top-3 outgoing per source group or any edge weight ≥10 to avoid visual hairball
- Returns ComponentAxis with groups sorted by descending count and flows by descending weight
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:build_system_model fingerprint=d7e821210d1dc85ebce7e71da4a5b89d2656510b0659d175052aaa5b19ee5a94 body_fp=cd1115d3867592bd42d0307a3d5d8ff0da5e620bf06b60970088e23268ca3ca0 source_ref=53916a96e0fd72b42dc0aa3b935f9f016be780e4 role=graph-database -->
Computes a complete system model from the store by separating production and test symbols, then classifying production nodes and computing graph metrics.

- `landmark_limit`: maximum number of highest-salience symbols to include in landmarks list  
- Returns SystemModel with production nodes, separate test nodes, role/subsystem axes with aggregated flows, and landmarks
- Builds production-only subgraph excluding tests to avoid polluting classification and flow analysis
- Calculates betweenness centrality, community detection, and depth-from-entries on production symbols only
- Classifies symbols as door/hub/bedrock/exit/orphan/normal/internal using multi-signal rubric with blind-spot rule
- Generates precomputed layered layout positions and component axes aggregating by role and subsystem
- Includes connected classes tracking for the blind-spot rule detecting dynamically dispatched methods
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:system_model_to_dict fingerprint=68297b3f83368a199aa1095e3f08af6bfbe0ca171940c91f6c0a36b85f4e393c body_fp=33b981ea399853473e6bcdfabc75f187c57c88f4b221c537c8061a85ba59c01c source_ref=53916a96e0fd72b42dc0aa3b935f9f016be780e4 role=graph-database -->
Serializes a SystemModel to the JSON shape that the desktop endpoint returns.

- `include_tests`: if True, combines model.nodes and model.test_nodes in output
- Transforms field names for web API compatibility (inbound → inbound_count, etc.)
- Serializes axes dictionary with group and flow data for component views
- Includes precomputed layout positions (x, y) and subsystem grouping metadata
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:_graph_fingerprint fingerprint=e7ad7a6e1ac246c7c6da5cb53dcc61d3dbd4f440e165f3ecc55b9b8b43e3aded body_fp=4b472daa5c2e71ff334f1c473e52d4f08b652a76bc34ba42ae0dee6ea90a0e8d source_ref=53916a96e0fd72b42dc0aa3b935f9f016be780e4 role=change-detection -->
Generates a SHA256 fingerprint of the graph state from symbol, edge, and section counts plus max section timestamp.

- Returns 16-character hex digest of the concatenated counts and version
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/system_model:build_system_model_cached fingerprint=a6de4af7cd5d6b100c9e43ff3f87ce9726e6642ef74cc0af5c7b046b8421bcbd body_fp=8a4ab9dc02a7d2793d64716bf51a4a61ceb1550f428c37dc9e16539b8aa28e01 source_ref=53916a96e0fd72b42dc0aa3b935f9f016be780e4 role=graph-database -->
Returns serialized system model using on-disk cache keyed by graph fingerprint for performance.

- Recomputes only when symbols, edges, or sections change since last build
- Cache stores full model with tests; `include_tests` filters returned view
- Cache path is `{project_root}/.trie/system_model.json`
- Falls back gracefully on cache read/write failures
<!-- trie:end -->