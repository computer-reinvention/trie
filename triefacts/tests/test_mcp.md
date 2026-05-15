---
trie_version: 0.1.0
source: tests/test_mcp.py
file_fingerprint: 529a00357bd248b8813c896be09747bf213b01bda28a4ec9661295d1893b5897
last_synced_at: '2026-05-15T13:10:22Z'
description: 'Tests for the MCP tool surface: `locate`, `explain`, `walk`.'
defines:
- kind: class
  qualified_name: tests/test_mcp:FakeClient
  lines: 34-50
- kind: method
  qualified_name: tests/test_mcp:FakeClient.generate
  lines: 40-47
- kind: method
  qualified_name: tests/test_mcp:FakeClient.count_tokens
  lines: 49-50
- kind: function
  qualified_name: tests/test_mcp:project
  lines: 54-66
- kind: function
  qualified_name: tests/test_mcp:populated_project
  lines: 70-91
- kind: function
  qualified_name: tests/test_mcp:tools
  lines: 95-98
- kind: function
  qualified_name: tests/test_mcp:test_locate_name_contains_returns_matches
  lines: 104-107
- kind: function
  qualified_name: tests/test_mcp:test_locate_returns_one_liner_from_section_body
  lines: 110-116
- kind: function
  qualified_name: tests/test_mcp:test_locate_returns_file_pointer
  lines: 119-121
- kind: function
  qualified_name: tests/test_mcp:test_locate_kind_filter
  lines: 124-127
- kind: function
  qualified_name: tests/test_mcp:test_locate_invalid_kind_returns_error
  lines: 130-133
- kind: function
  qualified_name: tests/test_mcp:test_locate_scope_prefix_filter
  lines: 136-139
- kind: function
  qualified_name: tests/test_mcp:test_locate_scope_exclude_filter
  lines: 142-145
- kind: function
  qualified_name: tests/test_mcp:test_locate_inbound_count_predicate
  lines: 148-153
- kind: function
  qualified_name: tests/test_mcp:test_locate_rank_by_inbound_count
  lines: 156-159
- kind: function
  qualified_name: tests/test_mcp:test_locate_limit_respected
  lines: 162-164
- kind: function
  qualified_name: tests/test_mcp:test_locate_unknown_predicate_field_silently_ignored
  lines: 167-170
- kind: function
  qualified_name: tests/test_mcp:test_locate_invalid_predicate_returns_error
  lines: 173-176
- kind: function
  qualified_name: tests/test_mcp:test_explain_returns_prose_and_neighbours
  lines: 182-189
- kind: function
  qualified_name: tests/test_mcp:test_explain_source_pointer_shape
  lines: 192-195
- kind: function
  qualified_name: tests/test_mcp:test_explain_neighbour_carries_one_liner
  lines: 198-201
- kind: function
  qualified_name: tests/test_mcp:test_explain_unknown_qname_returns_not_found
  lines: 204-207
- kind: function
  qualified_name: tests/test_mcp:test_explain_fuzzy_suggestion_for_typo
  lines: 210-216
- kind: function
  qualified_name: tests/test_mcp:test_walk_callers_returns_topology
  lines: 222-228
- kind: function
  qualified_name: tests/test_mcp:test_walk_callees_returns_outbound
  lines: 231-234
- kind: function
  qualified_name: tests/test_mcp:test_walk_both_directions
  lines: 237-242
- kind: function
  qualified_name: tests/test_mcp:test_walk_invalid_direction_returns_error
  lines: 245-248
- kind: function
  qualified_name: tests/test_mcp:test_walk_unknown_qname_returns_not_found
  lines: 251-254
- kind: function
  qualified_name: tests/test_mcp:test_walk_depth_zero_returns_only_root
  lines: 257-260
- kind: function
  qualified_name: tests/test_mcp:test_walk_depth_clamp_adds_note
  lines: 263-267
- kind: function
  qualified_name: tests/test_mcp:test_build_server_registers_three_verbs
  lines: 273-282
incoming_refs: 0
outgoing_refs: 7
---
<!-- trie:section symbol=tests/test_mcp:FakeClient fingerprint=b75f9ea63fb9bc13ffc916b979d6caad8ac663e1050c6f0b56c79dbb9959eb47 body_fp=2f6ce85a55a9885b27ad099612c9a4d867fff0b75aa4637d0fe35e2da66f4089 source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `FakeClient`

Stand-in for `ModelClient` returning a fixed text body and constant token counts.

- `body`: Markdown string returned verbatim by `generate`.
- `count_tokens`: always returns `100`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:FakeClient.generate fingerprint=a28c91031810d416f079e2d7a57f5ed7651bd8c3315cf78d1ec869c3b812915e body_fp=ea0eb5c4ab34d747e404c49d0b651495c57100fadaa84548116077e66c0e9139 source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `generate(_req: GenerationRequest) -> GenerationResponse`

Return a fixed `GenerationResponse` with the configured body text and hardcoded token counts.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=a142375d4480002b844bfea575882ae869fb69530f0d8089bd3288730e68918e source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `count_tokens(_req: GenerationRequest) -> int`

Return a fixed token count of 100.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:project fingerprint=3077c7d6e147cf70f7507fd05cf0d2907ab77c43051babf48292425cc858b8a9 body_fp=70c22f8b03dff93fa3f49e94cf98a2a9fd5b62843bf49beba4a6ee894b68d52b source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal two-file Python project with a `trie.toml` config under `tmp_path`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:populated_project fingerprint=779924a7456d208bcc1a0fe11b3bef22c37c98cb3bf38f148e8308cc4c0d2790 body_fp=27c300dc845e60690cf15fb83b5392f48e30f4fcd32d2e820cc1846d0076415f source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `populated_project(project: Path) -> Path`

Fixture that runs scan and sync on both project files so MCP tools have queryable triefact data.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:tools fingerprint=b89f3ca1611ed5226f820d82ffc6f4d3db27942f64390976744c1fbf0d5e67de body_fp=13150bc965820ded8a1847c3a63898dd7ea8ff75aa1c327d4f91687c8756ef42 source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `tools(populated_project: Path)`

Yield a `TrieTools` instance for the populated project, closing it after the test.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_name_contains_returns_matches fingerprint=606e12bdc96207727e2b6009db77dae4cd2811e33ba8af8a59cc14b251299355 body_fp=fc217299b82e978273d787fe8509ba90db2711d975dbdd7c6fff3eccbd02b283 source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `test_locate_name_contains_returns_matches(tools: TrieTools)`

Assert that `locate` with a `name_contains` predicate returns symbols whose qname matches the substring.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_returns_one_liner_from_section_body fingerprint=be37bc61373388869ba68113cc729055294dd6741ed64109fe45f987dff3e459 body_fp=383fbd5e2f0e28a3dc9b4f25b62ca7578340611abab0a2ce10ae34dea195217d source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `test_locate_returns_one_liner_from_section_body(tools: TrieTools)`

Assert that `locate` results include a `one_liner` field extracted from the triefact prose body.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_returns_file_pointer fingerprint=79636fdb413dd327c25791ed12bcb2541141315f20f6283c328a0a82a770d053 body_fp=2f90abf5c26a8ddbbf1f614de0b7f94fca566c8b6a0f7ce35c34656e617e0183 source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `test_locate_returns_file_pointer(tools: TrieTools)`

Assert that `locate` results include a `file_pointer` ending with the correct filename and line number.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_kind_filter fingerprint=204a6a70347cc56f83903016bec042e257b538c1c4215c90c18ae8eaa15808e1 body_fp=d94a1feb29d44e856d01e2c8c09e90315c81d98866eb89f0c237cd6925ca46b4 source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `test_locate_kind_filter(tools: TrieTools)`

Assert `locate` with `kind="class"` returns no results when only functions exist.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_invalid_kind_returns_error fingerprint=4acadfe17294720f526183f87a2494bf1f6dcc403e4e8cc81dad65fb23d29cf6 body_fp=948be9cd8b1ec287cee4344342e767785b13cc449e5835b43ee25d92d6dd8f45 source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `test_locate_invalid_kind_returns_error(tools: TrieTools)`

Assert that `locate` with an unsupported `kind` value returns an `invalid_argument` error dict.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_scope_prefix_filter fingerprint=6b4664b9f03664fa85ec7ce8b26b5add03721da36c1d058c8a859088f234780b body_fp=6a8851978a46888f73796a53ccb9ffa202291e5b400a8f705fc0ec79b6bd2658 source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `test_locate_scope_prefix_filter(tools: TrieTools)`

Verify that `locate` with `scope_prefix` returns only symbols from files matching that prefix.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_scope_exclude_filter fingerprint=cf9b696feb6336a71d192478f5e92d1e0d5c998388e14477c6224acfac9d3432 body_fp=e44f7aa10dd40cf79d7ef089e53e79d188a2d76f5d572769d1d1e5a53f87209b source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `test_locate_scope_exclude_filter(tools: TrieTools)`

Verify that `scope_exclude` filters out symbols whose file paths match excluded scope prefixes.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_inbound_count_predicate fingerprint=a20e5ce95ff6e893140c63286f37f60ca370e2daa7a8dbff921e5264a0ec8924 body_fp=4801b49bb439e04cf86a723960b8236063f8c4f80921e722cac048a44f047d09 source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `test_locate_inbound_count_predicate(tools: TrieTools)`

Verify `locate` filters by minimum inbound edge count, including symbols with callers and excluding those without.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_rank_by_inbound_count fingerprint=dc4ab730d35d42d38a1a80cc30d17798bde411df9a92393d82880247ed51d2d6 body_fp=d92b6316abe5606c1ee8c0f8c3ca2ee1266b7538fe590dde2431f577dbc0073f source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `test_locate_rank_by_inbound_count(tools: TrieTools)`

Assert that `locate` results are ordered descending by `inbound_count` when `rank_by="inbound_count"`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_limit_respected fingerprint=5b43e7abc9e8ffcb48ad5a1eb15f29abae212a5d93cf3fafe469ace94394e557 body_fp=124bb5dbc0063dd9a48b27778ca4cef4dd1f479265723a09c3e251f8dd6c7ce6 source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `test_locate_limit_respected(tools: TrieTools)`

Assert that `locate` returns no more results than the specified `limit`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_unknown_predicate_field_silently_ignored fingerprint=7ce84e2b0dbbddf0f97aed48a2631f115ba3bff249327cde06a34f9a40a42eba body_fp=dabe4aab6fe241708f210fa5c7645fcbef3d45c39bef2a84f77e8e7850938771 source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `test_locate_unknown_predicate_field_silently_ignored(tools: TrieTools)`

Assert that unrecognised predicate fields are ignored and matching still succeeds.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_invalid_predicate_returns_error fingerprint=4e314afe4b532d9d019d5940ca22c60800d918b4905dbce70630b9ea7c4d876b body_fp=b22247dcc4c9443fa02e06e7b6cce7619aa6e1332dc28723323d3c5ada08e69c source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `test_locate_invalid_predicate_returns_error(tools: TrieTools)`

Assert that passing a non-dict predicate to `locate` returns an `invalid_argument` error dict.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_explain_returns_prose_and_neighbours fingerprint=ca0385a78e2823572e125385d4179dfec932d510ca279bb8c6ce49f7351da7d8 body_fp=1a5ce0afd38de584606fa3aecfd50345042e30968cedbaa2a888cd05e2099641 source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `test_explain_returns_prose_and_neighbours(tools: TrieTools)`

Verify `explain` returns prose, correct callers, and an empty callees list for `lib:slugify`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_explain_source_pointer_shape fingerprint=f3a209d4b72e5d5b8621ea6b0d721e45fd409d15bffc877f4da3759b9c8e47cc body_fp=5d98be4ff0748d2586219a3a6e7172edc3941b92c19ec956ab492030e1994667 source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `test_explain_source_pointer_shape(tools: TrieTools)`

Assert that `explain` returns a `source_pointer` in `"file.py:start-end"` format.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_explain_neighbour_carries_one_liner fingerprint=1d4855ce5510d06cacace44de9704c023a0793220048421e685ba9966b5ec7e7 body_fp=af0d7e79939f6deb8435c0dbc88e3ee544959505657270ed7af76b712979f276 source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `test_explain_neighbour_carries_one_liner(tools: TrieTools)`

Assert that a caller entry returned by `explain` includes a populated `one_liner` field.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_explain_unknown_qname_returns_not_found fingerprint=ed89721b2a059acd69c40a8e4fc1f616bb84478f78ccfd994bb8383ca9e3337b body_fp=8e27d2f0ff8fc838537d2180422871d27ce0f60e96501393a49b0470e0200739 source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `test_explain_unknown_qname_returns_not_found(tools: TrieTools)`

Assert that `explain` returns a `not_found` error for an unrecognised qualified name.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_explain_fuzzy_suggestion_for_typo fingerprint=edbecabb6ccce06dc30d515ff8354c91924411a9c0bb165018c2fea6dcf26bf9 body_fp=536ef1f0b53851b52c0e5c89e7ebf760010352562180e4bdbbcaa149a6d76ff5 source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `test_explain_fuzzy_suggestion_for_typo(tools: TrieTools)`

Assert that `explain` returns an error with a `suggestion` field when given a near-miss qname typo.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_walk_callers_returns_topology fingerprint=ffb593f85dec28894896ad20abb8ed225c671c776d0740e4ce527ce243cedb56 body_fp=378a7a4094a820d9b85c363667745dc9e517f450954031f95e4963f0cb9ef595 source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `test_walk_callers_returns_topology(tools: TrieTools)`

Assert `walk` with `direction="callers"` returns root node, caller in nodes, and a directed edge.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_walk_callees_returns_outbound fingerprint=fa8734200d06de865fcd132e548589d13d70a14ed49394bd6e9aa161bf58609f body_fp=8c9084d2d2919c63eec35d400fcabd7dfcedcf5e5ba5236f1b4796c53d688210 source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `test_walk_callees_returns_outbound(tools: TrieTools)`

Assert that walking callees from `app:make_url` includes `lib:slugify` as a node and edge.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_walk_both_directions fingerprint=cf5f9355a6720079c859a59ea6542b124965dcd5b6f404b9a3a1add6b650115f body_fp=433a2f733036f0e76b7fb3c0e7f102f920c5c6e9cff94d7646fa327db12de719 source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `test_walk_both_directions(tools: TrieTools)`

Verify `walk` with `direction="both"` returns inbound caller nodes and edges.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_walk_invalid_direction_returns_error fingerprint=34c2309e2b1fa5d072874d9c584d6503334cc59e01aac682c87dbe621b0216f6 body_fp=e2338b2c1898fcb19a63aefa0551ca1d97a2d570150cea55ef9df2ab084a560f source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `test_walk_invalid_direction_returns_error(tools: TrieTools)`

Assert that `walk` returns an `invalid_argument` error when given an unrecognised direction string.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_walk_unknown_qname_returns_not_found fingerprint=7db3c28c3e02fa3e0472794a781e83ca5834a982cd918918a0f53731bf6a165c body_fp=2485a16f4ee5d425081eb01430095e95b2517fc116900536920cfd52df8ba6de source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `test_walk_unknown_qname_returns_not_found(tools: TrieTools)`

Assert that `walk` returns a `not_found` error for an unrecognised qualified name.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_walk_depth_zero_returns_only_root fingerprint=d57a8c520de9f8f6fefef7187a528a58a0b97181e81473b05a4d2de2f3eede71 body_fp=79c3e220d75eef77191295f6e0fd7730dc157f7fb9a8b347e0a8e5de7603da12 source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `test_walk_depth_zero_returns_only_root(tools: TrieTools)`

Assert that `walk` with `depth=0` returns only the root node and no edges.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_walk_depth_clamp_adds_note fingerprint=5f2ad94096fc772644b9861e5bf2de89ff79fd7dfd3227d62b1cdceddd1e99f9 body_fp=1669a4c47ee15130361f9cac68195ad559af1ef528533180b65811d0267c2f07 source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `test_walk_depth_clamp_adds_note(tools: TrieTools)`

Assert that requesting a depth exceeding `walk_max_depth` clamps the value and adds a "clamped" note to the result.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_build_server_registers_three_verbs fingerprint=85dad67991b790d69cb121abd834d86095f73cb0b212d565f131c62b696e037a body_fp=a9b95af912c112255bb24083610bad19c8396f4f62f3966ca69660d1a0cf52d0 source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `test_build_server_registers_three_verbs(populated_project: Path)`

Verify `build_server` returns a FastMCP instance with exactly `locate`, `explain`, and `walk` tools registered.
<!-- trie:end -->