---
trie_version: 0.1.0
source: tests/test_mcp.py
file_fingerprint: 529a00357bd248b8813c896be09747bf213b01bda28a4ec9661295d1893b5897
last_synced_at: '2026-05-14T17:15:40Z'
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
<!-- trie:section symbol=tests/test_mcp:FakeClient fingerprint=b75f9ea63fb9bc13ffc916b979d6caad8ac663e1050c6f0b56c79dbb9959eb47 body_fp=dc0babce9833502de45ab34f80fcb4e502ba3506c01638ce97635b155ab87c48 -->
## `FakeClient`

Stand-in `ModelClient` returning a fixed text body and hardcoded token counts.

- `body`: Markdown string returned verbatim by `generate`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:FakeClient.generate fingerprint=a28c91031810d416f079e2d7a57f5ed7651bd8c3315cf78d1ec869c3b812915e body_fp=b17eab3005977b70de57b4419c6044b8b9bddaadf3aac746529c37131f8d29e5 -->
## `generate(_req: GenerationRequest) -> GenerationResponse`

Return a fixed `GenerationResponse` with preset token counts, ignoring the request.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=9d067b772e73f67b1bb1b8cb6fc3a256c95035c670c6695fa426a36018030c0b -->
## `count_tokens(_req: GenerationRequest) -> int`

Return a fixed token count of 100 for any request.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:project fingerprint=3077c7d6e147cf70f7507fd05cf0d2907ab77c43051babf48292425cc858b8a9 body_fp=61436565f5aeea992dda5d4869b52787216211d9470315b2171faaf3f5ec5248 -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that writes a minimal two-file Python project with a `trie.toml` config into a temp directory.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:populated_project fingerprint=779924a7456d208bcc1a0fe11b3bef22c37c98cb3bf38f148e8308cc4c0d2790 body_fp=0253a54204882baddbb2bfeff666b6c11baa68ab4ecb5d1737b2b3ade74920b9 -->
## `populated_project(project: Path) -> Path`

Fixture that runs scan and sync on both source files so MCP tools have queryable triefact data.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:tools fingerprint=b89f3ca1611ed5226f820d82ffc6f4d3db27942f64390976744c1fbf0d5e67de body_fp=7e10b59b39ab7356705fdb1ef3757108bb207ef862a9e9c8b47b53fbcaa882d9 -->
## `tools(populated_project: Path)`

Yield a `TrieTools` instance bound to the populated project, closing it after the test.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_name_contains_returns_matches fingerprint=606e12bdc96207727e2b6009db77dae4cd2811e33ba8af8a59cc14b251299355 body_fp=a84b59dbeeadd31bfd9506e2e63e968aa97959de456d2b9b1c157230c57c066a -->
## `test_locate_name_contains_returns_matches(tools: TrieTools)`

Assert that `locate` with a `name_contains` predicate returns symbols whose qualified name includes the substring.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_returns_one_liner_from_section_body fingerprint=be37bc61373388869ba68113cc729055294dd6741ed64109fe45f987dff3e459 body_fp=b5a470dbd10880dd350523be4c42a490984e94cd5b2b967bdfa760962f4e5379 -->
## `test_locate_returns_one_liner_from_section_body(tools: TrieTools)`

Assert that `locate` extracts a one-liner from the generated triefact section body.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_returns_file_pointer fingerprint=79636fdb413dd327c25791ed12bcb2541141315f20f6283c328a0a82a770d053 body_fp=9f6925e751064c5ec512442e20a2d2d8e7e991d94077a8cf98d0eb415eb24ec4 -->
## `test_locate_returns_file_pointer(tools: TrieTools)`

Assert that `locate` results include a `file_pointer` ending with the filename and line number.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_kind_filter fingerprint=204a6a70347cc56f83903016bec042e257b538c1c4215c90c18ae8eaa15808e1 body_fp=b64a5649ac311db60f160dd06e91b1f54b00c03fbedc6c6169b4271c7a11b710 -->
## `test_locate_kind_filter(tools: TrieTools)`

Assert that filtering by `kind="class"` returns no results when only functions exist.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_invalid_kind_returns_error fingerprint=4acadfe17294720f526183f87a2494bf1f6dcc403e4e8cc81dad65fb23d29cf6 body_fp=0d87d05a57e96adee77345ad800ac13d29936f05f156570ec25c847878dddbbc -->
## `test_locate_invalid_kind_returns_error(tools: TrieTools)`

Assert `locate` returns an `invalid_argument` error dict when given an unrecognised `kind` value.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_scope_prefix_filter fingerprint=6b4664b9f03664fa85ec7ce8b26b5add03721da36c1d058c8a859088f234780b body_fp=1c7bab677bd9af6ad985858becc5d242ad22994c1b22b54a919fe8d2e8cfe064 -->
## `test_locate_scope_prefix_filter(tools: TrieTools)`

Assert that `locate` with `scope_prefix` returns only symbols whose file path starts with the given prefix.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_scope_exclude_filter fingerprint=cf9b696feb6336a71d192478f5e92d1e0d5c998388e14477c6224acfac9d3432 body_fp=8e11cd8b227149ca0bbe2870a914f00de60cbbe95e30c498c9abb5b8a1457277 -->
## `test_locate_scope_exclude_filter(tools: TrieTools)`

Verify that `scope_exclude` removes symbols from the excluded scope from `locate` results.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_inbound_count_predicate fingerprint=a20e5ce95ff6e893140c63286f37f60ca370e2daa7a8dbff921e5264a0ec8924 body_fp=8df86086b0fd78958f91ef812e55a3c16996d356bf57441e3cabc7cc70c889c4 -->
## `test_locate_inbound_count_predicate(tools: TrieTools)`

Verify `locate` with `inbound_count` minimum filters in symbols with callers and excludes those without.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_rank_by_inbound_count fingerprint=dc4ab730d35d42d38a1a80cc30d17798bde411df9a92393d82880247ed51d2d6 body_fp=48d44b9413781c79a2bc4462632bb816e33c2c16ecf1587a950558fb0e23e575 -->
## `test_locate_rank_by_inbound_count(tools: TrieTools)`

Assert that `locate` returns results sorted descending by `inbound_count` when `rank_by="inbound_count"`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_limit_respected fingerprint=5b43e7abc9e8ffcb48ad5a1eb15f29abae212a5d93cf3fafe469ace94394e557 body_fp=124bb5dbc0063dd9a48b27778ca4cef4dd1f479265723a09c3e251f8dd6c7ce6 -->
## `test_locate_limit_respected(tools: TrieTools)`

Assert that `locate` returns no more results than the specified `limit`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_unknown_predicate_field_silently_ignored fingerprint=7ce84e2b0dbbddf0f97aed48a2631f115ba3bff249327cde06a34f9a40a42eba body_fp=cd7a237dac8e5c25be767313b61ce7d1f2da7010a5f83cd02f9b9788956d5f8f -->
## `test_locate_unknown_predicate_field_silently_ignored(tools: TrieTools)`

Assert that extra, unrecognised predicate fields do not raise errors and matches still return.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_locate_invalid_predicate_returns_error fingerprint=4e314afe4b532d9d019d5940ca22c60800d918b4905dbce70630b9ea7c4d876b body_fp=b22247dcc4c9443fa02e06e7b6cce7619aa6e1332dc28723323d3c5ada08e69c -->
## `test_locate_invalid_predicate_returns_error(tools: TrieTools)`

Assert that passing a non-dict predicate to `locate` returns an `invalid_argument` error dict.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_explain_returns_prose_and_neighbours fingerprint=ca0385a78e2823572e125385d4179dfec932d510ca279bb8c6ce49f7351da7d8 body_fp=d6d2d993f6e820c14682717b3e1ad9d4e40bbf6b888f875cdc8aa5575b40090b -->
## `test_explain_returns_prose_and_neighbours(tools: TrieTools)`

Verify `explain` returns prose, correct callers, and empty callees for `lib:slugify`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_explain_source_pointer_shape fingerprint=f3a209d4b72e5d5b8621ea6b0d721e45fd409d15bffc877f4da3759b9c8e47cc body_fp=88118c9b97559db824a9d1779d496cde13d2ad26076318da37da83e2e0973849 -->
## `test_explain_source_pointer_shape(tools: TrieTools)`

Assert that `explain` returns a `source_pointer` with format `"<file>:<start>-<end>"`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_explain_neighbour_carries_one_liner fingerprint=1d4855ce5510d06cacace44de9704c023a0793220048421e685ba9966b5ec7e7 body_fp=af0d7e79939f6deb8435c0dbc88e3ee544959505657270ed7af76b712979f276 -->
## `test_explain_neighbour_carries_one_liner(tools: TrieTools)`

Assert that a caller entry returned by `explain` includes a populated `one_liner` field.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_explain_unknown_qname_returns_not_found fingerprint=ed89721b2a059acd69c40a8e4fc1f616bb84478f78ccfd994bb8383ca9e3337b body_fp=f212d3b02a6997d9df155286c05ee9ef64aa4767b39f8900400c6638810a853a -->
## `test_explain_unknown_qname_returns_not_found(tools: TrieTools)`

Assert that `explain` returns a `not_found` error for a nonexistent qualified name.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_explain_fuzzy_suggestion_for_typo fingerprint=edbecabb6ccce06dc30d515ff8354c91924411a9c0bb165018c2fea6dcf26bf9 body_fp=5bf9bad9e648b1cd8a3c73997afac07e2ba30382e4249ed9d4118180f1f5e2d4 -->
## `test_explain_fuzzy_suggestion_for_typo(tools: TrieTools)`

Assert that explaining a misspelled qname returns an error with a useful suggestion.

- `suggestion` must contain `"slugify"` or `"locate("` to be actionable.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_walk_callers_returns_topology fingerprint=ffb593f85dec28894896ad20abb8ed225c671c776d0740e4ce527ce243cedb56 body_fp=f2862a2d89cf2db6fb9f23b8251efca3a3238442b9757cb79d4ced9dd397f227 -->
## `test_walk_callers_returns_topology(tools: TrieTools)`

Assert that `walk` with `direction="callers"` returns correct root, nodes, and directed edges.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_walk_callees_returns_outbound fingerprint=fa8734200d06de865fcd132e548589d13d70a14ed49394bd6e9aa161bf58609f body_fp=6f660bb5cf34356bc1c8ca528733489f7275ce2ffee55571cfebbdd554352557 -->
## `test_walk_callees_returns_outbound(tools: TrieTools)`

Assert that `walk` with `direction="callees"` includes `lib:slugify` as a node and edge target of `app:make_url`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_walk_both_directions fingerprint=cf5f9355a6720079c859a59ea6542b124965dcd5b6f404b9a3a1add6b650115f body_fp=af9c2df3da58d42ac37d249b760cd7fc353d8ee1f18a83bdcbfffb4fb079d418 -->
## `test_walk_both_directions(tools: TrieTools)`

Verify that `walk` with `direction="both"` returns inbound caller nodes and edges.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_walk_invalid_direction_returns_error fingerprint=34c2309e2b1fa5d072874d9c584d6503334cc59e01aac682c87dbe621b0216f6 body_fp=a7c21c273591b54137037475f4e5b257b7160797be5c0c83038ae4c11ee76072 -->
## `test_walk_invalid_direction_returns_error(tools: TrieTools)`

Assert `walk` returns an `invalid_argument` error when given an unrecognised direction string.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_walk_unknown_qname_returns_not_found fingerprint=7db3c28c3e02fa3e0472794a781e83ca5834a982cd918918a0f53731bf6a165c body_fp=2485a16f4ee5d425081eb01430095e95b2517fc116900536920cfd52df8ba6de -->
## `test_walk_unknown_qname_returns_not_found(tools: TrieTools)`

Assert that `walk` returns a `not_found` error for an unrecognised qualified name.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_walk_depth_zero_returns_only_root fingerprint=d57a8c520de9f8f6fefef7187a528a58a0b97181e81473b05a4d2de2f3eede71 body_fp=79c3e220d75eef77191295f6e0fd7730dc157f7fb9a8b347e0a8e5de7603da12 -->
## `test_walk_depth_zero_returns_only_root(tools: TrieTools)`

Assert that `walk` with `depth=0` returns only the root node and no edges.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_walk_depth_clamp_adds_note fingerprint=5f2ad94096fc772644b9861e5bf2de89ff79fd7dfd3227d62b1cdceddd1e99f9 body_fp=a97de18d406aaa0c24d6712a657c67422d8f486e45a92e6b4744309909cf6788 -->
## `test_walk_depth_clamp_adds_note(tools: TrieTools)`

Assert that requesting depth beyond `walk_max_depth` clamps the value and adds a "clamped" note to the result.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_build_server_registers_three_verbs fingerprint=85dad67991b790d69cb121abd834d86095f73cb0b212d565f131c62b696e037a body_fp=a9b95af912c112255bb24083610bad19c8396f4f62f3966ca69660d1a0cf52d0 -->
## `test_build_server_registers_three_verbs(populated_project: Path)`

Verify `build_server` returns a FastMCP instance with exactly `locate`, `explain`, and `walk` tools registered.
<!-- trie:end -->