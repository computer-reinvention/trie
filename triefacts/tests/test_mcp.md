---
trie_version: 0.1.0
source: tests/test_mcp.py
file_fingerprint: c7b3f3ca31d88881e095b2de9c99c873a41f39e5fae7d1e21adba10193859511
last_synced_at: '2026-05-16T13:39:45Z'
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
  qualified_name: tests/test_mcp:test_trie_tools_init_fails_clearly_when_rg_missing
  lines: 104-125
- kind: function
  qualified_name: tests/test_mcp:test_locate_name_contains_returns_matches
  lines: 131-136
- kind: function
  qualified_name: tests/test_mcp:test_locate_returns_one_liner_from_section_body
  lines: 139-145
- kind: function
  qualified_name: tests/test_mcp:test_locate_returns_file_pointer
  lines: 148-150
- kind: function
  qualified_name: tests/test_mcp:test_locate_kind_filter
  lines: 153-159
- kind: function
  qualified_name: tests/test_mcp:test_locate_invalid_kind_returns_error
  lines: 162-165
- kind: function
  qualified_name: tests/test_mcp:test_locate_scope_prefix_filter
  lines: 168-171
- kind: function
  qualified_name: tests/test_mcp:test_locate_scope_exclude_filter
  lines: 174-177
- kind: function
  qualified_name: tests/test_mcp:test_locate_inbound_count_predicate
  lines: 180-185
- kind: function
  qualified_name: tests/test_mcp:test_locate_rank_by_inbound_count
  lines: 188-192
- kind: function
  qualified_name: tests/test_mcp:test_locate_limit_respected
  lines: 195-197
- kind: function
  qualified_name: tests/test_mcp:test_locate_unknown_predicate_field_silently_ignored
  lines: 200-203
- kind: function
  qualified_name: tests/test_mcp:test_locate_invalid_predicate_returns_error
  lines: 206-209
- kind: function
  qualified_name: tests/test_mcp:test_locate_fallback_kind_none_when_no_name_contains
  lines: 215-224
- kind: function
  qualified_name: tests/test_mcp:test_locate_fallback_kind_grep_empty_for_unseen_string
  lines: 227-234
- kind: function
  qualified_name: tests/test_mcp:test_locate_fallback_kind_grep_redirects_via_body_match
  lines: 237-255
- kind: function
  qualified_name: tests/test_mcp:test_locate_fallback_ranks_by_inbound_count_desc
  lines: 258-272
- kind: function
  qualified_name: tests/test_mcp:test_locate_fallback_caps_matches_and_notes_truncation
  lines: 275-301
- kind: function
  qualified_name: tests/test_mcp:test_locate_fallback_omits_truncation_note_when_under_cap
  lines: 304-312
- kind: function
  qualified_name: tests/test_mcp:test_locate_fallback_honours_scope_prefix
  lines: 315-330
- kind: function
  qualified_name: tests/test_mcp:test_locate_normal_hits_path_omits_fallback_key
  lines: 333-339
- kind: function
  qualified_name: tests/test_mcp:test_explain_returns_prose_and_neighbours
  lines: 345-352
- kind: function
  qualified_name: tests/test_mcp:test_explain_source_pointer_shape
  lines: 355-358
- kind: function
  qualified_name: tests/test_mcp:test_explain_neighbour_carries_one_liner
  lines: 361-364
- kind: function
  qualified_name: tests/test_mcp:test_explain_unknown_qname_returns_not_found
  lines: 367-370
- kind: function
  qualified_name: tests/test_mcp:test_explain_fuzzy_suggestion_for_typo
  lines: 373-379
- kind: function
  qualified_name: tests/test_mcp:test_walk_callers_returns_topology
  lines: 385-391
- kind: function
  qualified_name: tests/test_mcp:test_walk_callees_returns_outbound
  lines: 394-397
- kind: function
  qualified_name: tests/test_mcp:test_walk_both_directions
  lines: 400-405
- kind: function
  qualified_name: tests/test_mcp:test_walk_invalid_direction_returns_error
  lines: 408-411
- kind: function
  qualified_name: tests/test_mcp:test_walk_unknown_qname_returns_not_found
  lines: 414-417
- kind: function
  qualified_name: tests/test_mcp:test_walk_depth_zero_returns_only_root
  lines: 420-423
- kind: function
  qualified_name: tests/test_mcp:test_walk_depth_clamp_adds_note
  lines: 426-430
- kind: function
  qualified_name: tests/test_mcp:test_build_server_registers_three_verbs
  lines: 436-445
incoming_refs: 0
outgoing_refs: 8
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

<!-- trie:section symbol=tests/test_mcp:test_locate_name_contains_returns_matches fingerprint=18e39f7284ba6a5d743a888fa0f66b235dd3907c917c79dea238f68b4becd3e2 body_fp=52a8601d55f8752796f6e571e917d9b4e564428d5ab7faf8a90e6fd64f4e8a37 source_ref=cab45f77d1dc61906302956ceaca9ec290ee6b94 -->
## `test_locate_name_contains_returns_matches(tools: TrieTools)`

Assert that `locate` with a `name_contains` predicate returns matching symbols under `result["hits"]` with no `fallback` key present.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_returns_one_liner_from_section_body fingerprint=4498143601b264c151125672d5320096658bda34fb59db7d3f21d4fccab01960 body_fp=383fbd5e2f0e28a3dc9b4f25b62ca7578340611abab0a2ce10ae34dea195217d source_ref=cab45f77d1dc61906302956ceaca9ec290ee6b94 -->
## `test_locate_returns_one_liner_from_section_body(tools: TrieTools)`

Assert that `locate` results include a `one_liner` field extracted from the triefact prose body.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_returns_file_pointer fingerprint=b912c6822fbf5e42d0b97795382267bc1d447d520c60a4abc35f9bf582854c9e body_fp=2f90abf5c26a8ddbbf1f614de0b7f94fca566c8b6a0f7ce35c34656e617e0183 source_ref=cab45f77d1dc61906302956ceaca9ec290ee6b94 -->
## `test_locate_returns_file_pointer(tools: TrieTools)`

Assert that `locate` results include a `file_pointer` ending with the correct filename and line number.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_kind_filter fingerprint=4ab6c522eeb7953030d8f3f238b4cdb988b24689c06c162b0e0756688c958042 body_fp=4fb6e97831d8ed8e41d535a8216f115ee4a94c3d8afb0e8fd0944d63dfa30166 source_ref=cab45f77d1dc61906302956ceaca9ec290ee6b94 -->
## `test_locate_kind_filter(tools: TrieTools)`

Assert `locate` with `kind="class"` returns empty `hits` when only functions exist, even when fallback grep fires.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_invalid_kind_returns_error fingerprint=4acadfe17294720f526183f87a2494bf1f6dcc403e4e8cc81dad65fb23d29cf6 body_fp=948be9cd8b1ec287cee4344342e767785b13cc449e5835b43ee25d92d6dd8f45 source_ref=6dbbdc95c4a370893e730330c3d0ef838e805585 -->
## `test_locate_invalid_kind_returns_error(tools: TrieTools)`

Assert that `locate` with an unsupported `kind` value returns an `invalid_argument` error dict.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_scope_prefix_filter fingerprint=17886df863c26934a3279442d7df5516e444f17b543636c1882909ab552c2903 body_fp=6a8851978a46888f73796a53ccb9ffa202291e5b400a8f705fc0ec79b6bd2658 source_ref=cab45f77d1dc61906302956ceaca9ec290ee6b94 -->
## `test_locate_scope_prefix_filter(tools: TrieTools)`

Verify that `locate` with `scope_prefix` returns only symbols from files matching that prefix.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_scope_exclude_filter fingerprint=f2d1ffb4462b9ec48e317f5c7c0fe4875e6e423ce2f7d24f7239597885e28f03 body_fp=e44f7aa10dd40cf79d7ef089e53e79d188a2d76f5d572769d1d1e5a53f87209b source_ref=cab45f77d1dc61906302956ceaca9ec290ee6b94 -->
## `test_locate_scope_exclude_filter(tools: TrieTools)`

Verify that `scope_exclude` filters out symbols whose file paths match excluded scope prefixes.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_inbound_count_predicate fingerprint=434010dc9271e7b19043e8ace55591ac26fb83b192daefa3a2760ff255b59bc1 body_fp=4801b49bb439e04cf86a723960b8236063f8c4f80921e722cac048a44f047d09 source_ref=cab45f77d1dc61906302956ceaca9ec290ee6b94 -->
## `test_locate_inbound_count_predicate(tools: TrieTools)`

Verify `locate` filters by minimum inbound edge count, including symbols with callers and excluding those without.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_rank_by_inbound_count fingerprint=076d3d599599b75bf4fd83a3ea668e14e235fbd05d177f0d682aa64c4766231b body_fp=d92b6316abe5606c1ee8c0f8c3ca2ee1266b7538fe590dde2431f577dbc0073f source_ref=cab45f77d1dc61906302956ceaca9ec290ee6b94 -->
## `test_locate_rank_by_inbound_count(tools: TrieTools)`

Assert that `locate` results are ordered descending by `inbound_count` when `rank_by="inbound_count"`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_limit_respected fingerprint=9cab3af0507419236f8af08a0db51cf56eff4fe83606dadac4334240029fe1d4 body_fp=124bb5dbc0063dd9a48b27778ca4cef4dd1f479265723a09c3e251f8dd6c7ce6 source_ref=cab45f77d1dc61906302956ceaca9ec290ee6b94 -->
## `test_locate_limit_respected(tools: TrieTools)`

Assert that `locate` returns no more results than the specified `limit`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_unknown_predicate_field_silently_ignored fingerprint=37daee59cfce4ce0f574b0ad0df138f2bbf583180c1947caa8954cbb9e7f7552 body_fp=dabe4aab6fe241708f210fa5c7645fcbef3d45c39bef2a84f77e8e7850938771 source_ref=cab45f77d1dc61906302956ceaca9ec290ee6b94 -->
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

<!-- trie:section symbol=tests/test_mcp:test_locate_fallback_kind_none_when_no_name_contains fingerprint=ce9789f41cdba22932d029e4852873c372192c4b42f1c1d90d0d7b1323e37ba1 body_fp=d1f99223ccf38dff1149fd4c86920c913d568679954a5c02a36b6101ffcba151 source_ref=cab45f77d1dc61906302956ceaca9ec290ee6b94 -->
## `test_locate_fallback_kind_none_when_no_name_contains(tools: TrieTools)`

Assert that a predicate with no `name_contains` field returns `fallback.kind == "none"` when no symbols match.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_fallback_kind_grep_empty_for_unseen_string fingerprint=8399484b13d1ee3b4a61223ffbc7bb5e7f7ae7c059b06744dc7765582514d70c body_fp=266e8102d60a4c2a7f65d30aab0e933abdaa9773b193901cff2868767075bc67 source_ref=cab45f77d1dc61906302956ceaca9ec290ee6b94 -->
## `test_locate_fallback_kind_grep_empty_for_unseen_string(tools: TrieTools)`

Assert that `locate` returns `fallback.kind == "grep_empty"` when `name_contains` matches no symbol name and no source body.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_fallback_kind_grep_redirects_via_body_match fingerprint=75dc0b85830bab88f98909d4f638c6cc05d44bf15325513cf056524676e7338d body_fp=0e9caf561b067c4bb9681f41d989d49692fe467be894a59252605d34b6d64750 source_ref=cab45f77d1dc61906302956ceaca9ec290ee6b94 -->
## `test_locate_fallback_kind_grep_redirects_via_body_match(tools: TrieTools)`

Assert that a `name_contains` query matching symbol bodies (not names) returns a `grep` fallback with enclosing symbols, occurrence counts, and graph metrics.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_fallback_ranks_by_inbound_count_desc fingerprint=2514a954811a9d24af90a85ab99d3d7c59b96d1ad2def48e5843b21bf2652a76 body_fp=df3c9e3ff2c0fd18448e16b378d7df67cd742bba135e5d3af539de9f93df8ce2 source_ref=cab45f77d1dc61906302956ceaca9ec290ee6b94 -->
## `test_locate_fallback_ranks_by_inbound_count_desc(tools: TrieTools)`

Assert that grep-fallback candidates are sorted by `inbound_count` descending when multiple matches exist.

- Skips if the fixture gains a symbol named `"title"` or if fewer than two fallback candidates are returned.
<!-- trie:end -->



<!-- trie:section symbol=tests/test_mcp:test_locate_fallback_honours_scope_prefix fingerprint=f2d122d82a9f89f3136c243fee5e421b5217ccb42f871475c2c753c079f99167 body_fp=a71c490af9fab098fed0835e13e664a858c73fd7864f9792bb6550b7446446ab source_ref=cab45f77d1dc61906302956ceaca9ec290ee6b94 -->
## `test_locate_fallback_honours_scope_prefix(tools: TrieTools)`

Assert that `scope_prefix` filters fallback grep candidates to the specified scope, excluding symbols from other scopes.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_normal_hits_path_omits_fallback_key fingerprint=c2ca83ed88936f3042d75b5b12246fd5322bcbcf449cdf0ff86efbf1abe808fd body_fp=e74208a20d62c69abfff203bdf55322f0d4030ddf84e2e4e8d1f0ae18a508f94 source_ref=cab45f77d1dc61906302956ceaca9ec290ee6b94 -->
## `test_locate_normal_hits_path_omits_fallback_key(tools: TrieTools)`

Assert that a successful `locate` response contains no `fallback` key when primary hits are found.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_fallback_caps_matches_and_notes_truncation fingerprint=bf572683898e4800cca4cf7f9ecf860ce8035308dd17a2de6611edb2fd95037e body_fp=feb63e551211b353edaac7de5471347efe66109f7533e0e4d167321825149d00 source_ref=5121a90af508a5817dab3b63572cb6f1f9499e4b -->
## `test_locate_fallback_caps_matches_and_notes_truncation(tools: TrieTools)`

Verify that fallback grep results are capped at `locate_fallback_match_limit` and the response includes a truncation note with total count.

- `tools`: fixture providing a `TrieTools` instance with the populated project; `mcp_cfg` is mutated to force `locate_fallback_match_limit=1`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_fallback_omits_truncation_note_when_under_cap fingerprint=07c3ee77b2a7505bba4da9c4bdc6f9281f3f4514d50e5b2d5bfadc78996bd759 body_fp=b70b324d2ec841712a880095c2ef1d3bc69fd8dabf77867bcdf573929b6394f3 source_ref=5121a90af508a5817dab3b63572cb6f1f9499e4b -->
## `test_locate_fallback_omits_truncation_note_when_under_cap(tools: TrieTools)`

Assert no truncation note appears in fallback when all grep matches fit within the match limit.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_trie_tools_init_fails_clearly_when_rg_missing fingerprint=e625643ba6a1b85500ca87f1c0222f623bf2bbbd7a2983711641f7d01846fb7a body_fp=2a96793ec1cda466eeaaf3c09ac0b655fcf2e8eb2f47306256a27b1b78c5d47b source_ref=080f8cf593472b38359d9336616c26fce746fcb9 -->
## `test_trie_tools_init_fails_clearly_when_rg_missing(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `TrieTools` raises `RipgrepNotFoundError` with an actionable message when `rg` is absent from `PATH`.

- `monkeypatch`: stubs `shutil.which` to return `None`, simulating missing `rg`.
- Error message must contain `"rg"` and either `"install"` or `"ripgrep"`.
<!-- trie:end -->