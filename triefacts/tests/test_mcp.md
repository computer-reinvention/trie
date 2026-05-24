---
trie_version: 0.1.2
source: tests/test_mcp.py
file_fingerprint: 4457d81c89ebf7bf4d21dffb6407ca53d07d7b52dc6ed0a206cd8db2258c29da
last_synced_at: '2026-05-23T23:21:22Z'
description: 'Tests for the MCP tool surface: `grep`, `read`, `trace`.'
defines:
- kind: module
  qualified_name: tests/test_mcp:__module__
  lines: 1-704
- kind: constant
  qualified_name: tests/test_mcp:PROJECT_TOML
  lines: 22-31
- kind: class
  qualified_name: tests/test_mcp:FakeClient
  lines: 35-51
- kind: method
  qualified_name: tests/test_mcp:FakeClient.generate
  lines: 41-48
- kind: method
  qualified_name: tests/test_mcp:FakeClient.count_tokens
  lines: 50-51
- kind: function
  qualified_name: tests/test_mcp:project
  lines: 55-67
- kind: function
  qualified_name: tests/test_mcp:populated_project
  lines: 71-92
- kind: function
  qualified_name: tests/test_mcp:tools
  lines: 96-99
- kind: function
  qualified_name: tests/test_mcp:test_trie_tools_init_fails_clearly_when_rg_missing
  lines: 105-126
- kind: function
  qualified_name: tests/test_mcp:test_grep_name_contains_returns_matches
  lines: 132-137
- kind: function
  qualified_name: tests/test_mcp:test_grep_returns_one_liner_from_section_body
  lines: 140-146
- kind: function
  qualified_name: tests/test_mcp:test_grep_returns_file_pointer
  lines: 149-151
- kind: function
  qualified_name: tests/test_mcp:test_grep_kind_filter
  lines: 154-160
- kind: function
  qualified_name: tests/test_mcp:test_grep_invalid_kind_returns_error
  lines: 163-166
- kind: function
  qualified_name: tests/test_mcp:test_grep_accepts_constant_and_module_kinds
  lines: 169-181
- kind: function
  qualified_name: tests/test_mcp:test_grep_scope_prefix_filter
  lines: 184-187
- kind: function
  qualified_name: tests/test_mcp:test_grep_scope_exclude_filter
  lines: 190-193
- kind: function
  qualified_name: tests/test_mcp:test_grep_inbound_count_predicate
  lines: 196-201
- kind: function
  qualified_name: tests/test_mcp:test_grep_rank_by_inbound_count
  lines: 204-211
- kind: function
  qualified_name: tests/test_mcp:test_grep_limit_respected
  lines: 214-218
- kind: function
  qualified_name: tests/test_mcp:test_grep_empty_predicate_returns_invalid_argument
  lines: 221-235
- kind: function
  qualified_name: tests/test_mcp:test_grep_empty_predicate_rejected_regardless_of_rank_by
  lines: 238-244
- kind: function
  qualified_name: tests/test_mcp:test_grep_unknown_predicate_field_silently_ignored
  lines: 247-250
- kind: function
  qualified_name: tests/test_mcp:test_grep_invalid_predicate_returns_error
  lines: 253-256
- kind: function
  qualified_name: tests/test_mcp:test_grep_fallback_kind_none_when_no_name_contains
  lines: 262-271
- kind: function
  qualified_name: tests/test_mcp:test_grep_fallback_kind_text_match_empty_for_unseen_string
  lines: 274-281
- kind: function
  qualified_name: tests/test_mcp:test_grep_fallback_kind_text_match_redirects_via_body_match
  lines: 284-302
- kind: function
  qualified_name: tests/test_mcp:test_grep_fallback_ranks_by_inbound_count_desc
  lines: 305-319
- kind: function
  qualified_name: tests/test_mcp:test_grep_fallback_caps_matches_and_notes_truncation
  lines: 322-348
- kind: function
  qualified_name: tests/test_mcp:test_grep_fallback_omits_truncation_note_when_under_cap
  lines: 351-359
- kind: function
  qualified_name: tests/test_mcp:test_grep_fallback_honours_scope_prefix
  lines: 362-377
- kind: function
  qualified_name: tests/test_mcp:test_grep_normal_hits_path_omits_fallback_key
  lines: 380-386
- kind: function
  qualified_name: tests/test_mcp:test_read_returns_prose_and_neighbours
  lines: 392-399
- kind: function
  qualified_name: tests/test_mcp:test_read_source_pointer_shape
  lines: 402-405
- kind: function
  qualified_name: tests/test_mcp:test_read_neighbour_carries_one_liner
  lines: 408-411
- kind: function
  qualified_name: tests/test_mcp:test_read_unknown_qname_returns_not_found
  lines: 414-417
- kind: function
  qualified_name: tests/test_mcp:test_read_fuzzy_suggestion_for_typo
  lines: 420-426
- kind: function
  qualified_name: tests/test_mcp:test_trace_callers_returns_topology
  lines: 432-438
- kind: function
  qualified_name: tests/test_mcp:test_trace_callees_returns_outbound
  lines: 441-444
- kind: function
  qualified_name: tests/test_mcp:test_trace_both_directions
  lines: 447-452
- kind: function
  qualified_name: tests/test_mcp:test_trace_invalid_direction_returns_error
  lines: 455-458
- kind: function
  qualified_name: tests/test_mcp:test_trace_unknown_qname_returns_not_found
  lines: 461-464
- kind: function
  qualified_name: tests/test_mcp:test_trace_depth_zero_returns_only_root
  lines: 467-470
- kind: function
  qualified_name: tests/test_mcp:test_trace_depth_clamp_adds_note
  lines: 473-477
- kind: function
  qualified_name: tests/test_mcp:test_build_server_registers_three_verbs
  lines: 483-506
- kind: function
  qualified_name: tests/test_mcp:test_build_server_wire_names_bind_to_internal_methods
  lines: 509-526
- kind: function
  qualified_name: tests/test_mcp:dual_rank_project
  lines: 535-592
- kind: function
  qualified_name: tests/test_mcp:test_grep_entry_points_niche_ranks_before_hub
  lines: 595-618
- kind: function
  qualified_name: tests/test_mcp:test_grep_entry_points_hits_carry_score
  lines: 621-633
- kind: function
  qualified_name: tests/test_mcp:test_grep_symbol_typo_tolerance
  lines: 636-642
- kind: function
  qualified_name: tests/test_mcp:test_grep_symbol_returns_score_field
  lines: 645-653
- kind: function
  qualified_name: tests/test_mcp:test_grep_fuzzy_prose_fallback
  lines: 656-671
- kind: function
  qualified_name: tests/test_mcp:test_grep_str_fuzzy_fallback
  lines: 674-684
- kind: function
  qualified_name: tests/test_mcp:test_grep_str_fuzzy_fallback_finds_close_name
  lines: 687-703
incoming_refs: 0
outgoing_refs: 13
---
<!-- trie:section symbol=tests/test_mcp:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=6004134ec6b6ccb1c69b37a1e9c79855c4229204d59f4817486cb1b836c91c43 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `tests/test_mcp`

Test suite for the MCP tool surface (`grep`, `read`, `trace`) via `TrieTools` directly.

- `FakeClient`: stub `ModelClient` returning fixed text and token counts
- `project`: `tmp_path` with `trie.toml`, `lib.py`, `app.py`
- `populated_project`: `project` after `scan_project` + `sync_single_file` for both files
- `tools`: `TrieTools` instance over `populated_project`, closed after each test
- `dual_rank_project`: two-symbol project wiring specific inbound-edge counts for ranking tests
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:PROJECT_TOML fingerprint=3f524fd58415aac9f548f19d4ad2554a2e411c44f7f8907ce1944fa2fa35a62e body_fp=af9c464c27a1e4a6ac5a209faec79433eece693974a5686e7d85d279e4163c5f source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `PROJECT_TOML`

TOML string used as `trie.toml` content in test fixtures.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:FakeClient fingerprint=b75f9ea63fb9bc13ffc916b979d6caad8ac663e1050c6f0b56c79dbb9959eb47 body_fp=154898f7d53bf9ff2f0fb2707df925737eb68fa3c0a115b779588fbc93b227c2 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `FakeClient(model_id: str = "fake/test", body: str = "## generated\n\nGenerated description.\n")`

Stand-in for `ModelClient` that returns fixed text and hardcoded token counts.

- `body`: the text returned verbatim in every `generate` response.
- `generate`: always reports 10 input / 20 output tokens.
- `count_tokens`: always returns 100.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:FakeClient.generate fingerprint=a28c91031810d416f079e2d7a57f5ed7651bd8c3315cf78d1ec869c3b812915e body_fp=803357a9663d8d69ff2f7725daa3d344b44e71aaa502caa6bf85ed281e8ca3d5 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `FakeClient.generate(self, _req: GenerationRequest) -> GenerationResponse`

Return a fixed `GenerationResponse` using `FakeClient.body` and hardcoded token counts.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=cc6c25933607afe775b24bc993befebab9ab8853947bdb7ba9e5394bb698adcf source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `FakeClient.count_tokens(self, _req: GenerationRequest) -> int`

Always returns 100 as a stub token count for `FakeClient`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:project fingerprint=3077c7d6e147cf70f7507fd05cf0d2907ab77c43051babf48292425cc858b8a9 body_fp=9c05cb50cfbf686a90be43108384667588aec96ba7bddc4acb5149858ae43e49 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `project(tmp_path: Path) -> Path`

Create a minimal two-file project fixture with `trie.toml`, `lib.py` (`slugify`), and `app.py` (`make_url`).
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:populated_project fingerprint=779924a7456d208bcc1a0fe11b3bef22c37c98cb3bf38f148e8308cc4c0d2790 body_fp=7811e01110fa7bcd06ec11a80c34929777469746b3b4176002e2a76a6d15ff6d source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `populated_project(project: Path) -> Path`

Extend the `project` fixture by running `scan_project` and `sync_single_file` for both source files, so MCP tools have graph data to query.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:tools fingerprint=b89f3ca1611ed5226f820d82ffc6f4d3db27942f64390976744c1fbf0d5e67de body_fp=026e308d5e75d885bcc8f2bc5a93cfcba07a5f01aa163867081122e30e977b8b source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `tools(populated_project: Path)`

Yield a `TrieTools` instance backed by `populated_project`, closing it after the test.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trie_tools_init_fails_clearly_when_rg_missing fingerprint=2ea97d1b02ea695fbca32b81cfd8377a7e1da3159c9b30a1815fe2099d25638b body_fp=8de58518f72002837039f259c428b4f02ef37d9247d1f8f0b809f229d94582b8 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_trie_tools_init_fails_clearly_when_rg_missing(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert `TrieTools` raises `RipgrepNotFoundError` with an actionable message when `rg` is absent.

- Stubs `shutil.which` to return `None`, simulating a missing `rg` binary.
- Checks error message contains `"rg"` and an install hint.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_name_contains_returns_matches fingerprint=13a70b013b95687914be7cf11a6a2926e39e6d256ed6ee0fc19ec38c6f2bcffb body_fp=8e2740443913959e2dc6c77c5e8ecdc681b1010059aba2ee772bb542dee25282 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_name_contains_returns_matches(tools: TrieTools)`

Assert `grep` with `name_contains` returns matching symbols and omits the `fallback` key on success.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_returns_one_liner_from_section_body fingerprint=37a68231e58a6658814f1e064b7c136eeaa7a7f879f70bdfd4eaa836d69779ad body_fp=9f70f8db67a7f6bb03262f556e4b7ca1df2272abe69903df1abb1abf3c7205d2 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_returns_one_liner_from_section_body(tools: TrieTools)`

Verify `grep` hits include a `one_liner` extracted from the symbol's triefact prose body.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_returns_file_pointer fingerprint=fd44c10f827063015b2af6e12727ce6f8e2d67973fc32ea706be0a403274f87e body_fp=fa3f8559f8d2419bad4089787102a3b2f85859a87cfb1235bb0c15212fd4c3eb source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_returns_file_pointer(tools: TrieTools)`

Assert that each `grep` hit includes a `file_pointer` ending with `"app.py:4"` for `make_url`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_kind_filter fingerprint=05f736a15cd7708beed46d7beef0835ba93bb4867f848cec7c0d4da66a5d31bf body_fp=a3fd1d7e792971cfc53f85a5dc706bc97d9396fb479fc82ef2b55ef4cacd01e8 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_kind_filter(tools: TrieTools)`

Assert that filtering by `kind="class"` on a functions-only fixture returns empty `hits`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_invalid_kind_returns_error fingerprint=93c63e643ced72ef46d974b15a6f15362abaa72e8e7b439e17f8d46411602d2e body_fp=392e9da9a55e34e4faee4f74342da26bbcf39113ece94cfecb086f5618324e8e source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_invalid_kind_returns_error(tools: TrieTools)`

Assert that `TrieTools.grep` returns an `invalid_argument` error dict when given an unrecognised `kind` value.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_accepts_constant_and_module_kinds fingerprint=a7b0b5f6a91e85c5d7b2effde7c148be97b61ecfd7966d405518b3d26526bbed body_fp=8898a0a99fa985e4ebaa3ff2eb9925e49436139f88c2c605c172261701c721e8 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_accepts_constant_and_module_kinds(tools: TrieTools)`

Assert that `grep` accepts `"constant"` and `"module"` as valid `kind` predicate values without returning an `invalid_argument` error.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_scope_prefix_filter fingerprint=4087ec669cf402755c9ebcba58be379db4f126a23aaa314712e20b33ffa6a9f0 body_fp=d510ef4341d66e39de1460760d4da1947155d32f6559a6ba894e4fb15ca955b3 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_scope_prefix_filter(tools: TrieTools)`

Assert that `grep` with `scope_prefix="lib"` returns only hits whose file pointers start with `"lib"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_scope_exclude_filter fingerprint=d9ed58e0d2cb505d72e32ca79f8f8032c881eff47584a5bf9377a006626e5793 body_fp=87d14dcee9da87fc04c82ff2276e4642267729e04436318912df3a6e9491c8d5 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_scope_exclude_filter(tools: TrieTools)`

Verify that `scope_exclude` removes hits whose file path matches the excluded scope.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_inbound_count_predicate fingerprint=29ed9feb09b2e5254bd1cef76cabd75536142afaac8b064dcc196599c69f7b0b body_fp=fa14b65b47525a6fbac4378f1f9741bb55ab3a1264bd8c05d4a6a984e286dedc source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_inbound_count_predicate(tools: TrieTools)`

Verify `grep` filters symbols by minimum inbound edge count correctly.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_rank_by_inbound_count fingerprint=956741b97e66e5508ccc0365fd3a6a04e6e7c6f3cb7da4770fc673b73a03477e body_fp=4585e4037bbbc0ca24eb69c634d519136623613efbe5c811127dad6fae589a77 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_rank_by_inbound_count(tools: TrieTools)`

Assert that `TrieTools.grep` with `rank_by="inbound_count"` returns hits sorted by inbound count descending.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_limit_respected fingerprint=80407aa581af3497200f623a81e718ea1e94ee91389ac126830562e3b69348af body_fp=217d83a9234604c4174f10ed36193636585422318c7c684494b23de6b0f469c7 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_limit_respected(tools: TrieTools)`

Verify that `TrieTools.grep` honours the `limit` parameter and returns at most the requested number of hits.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_empty_predicate_returns_invalid_argument fingerprint=b276ee91748c22279c9a40988da4c4daaebfea8382927b5fe18d9f2f3c5b17ce body_fp=445c9efc683cd81d0dd28b845d03b08ea71dffb9ab13d5626cca3ff1a1a6c69e source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_empty_predicate_returns_invalid_argument(tools: TrieTools)`

Assert that `grep` rejects empty or vacuous predicates with `invalid_argument` and a recoverable suggestion.

- Tested predicates: `None`, `{}`, `{"name_contains": ""}`, `{"kind": "any"}`.
- Suggestion must mention `name_contains` or `scope_prefix`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_empty_predicate_rejected_regardless_of_rank_by fingerprint=173c7d0e853ec0b26f7e6b2344e5c2c4c42c2b1245b1081fca21ec158813dd8d body_fp=4e0ef6a98cbba86410a0004c8394055ebea13ed428f33f71645c80753280d92a source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_empty_predicate_rejected_regardless_of_rank_by(tools: TrieTools)`

Assert that `TrieTools.grep` rejects an empty predicate with `invalid_argument` even when `rank_by` is supplied.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_unknown_predicate_field_silently_ignored fingerprint=d932c0e53093906441747dbaef79cf5c314d42057b100dc5b2f257cc7518c2f0 body_fp=7e68127147298703edcfceeba8400ffc1bb524d2f4fcc9ad472717bbe9480089 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_unknown_predicate_field_silently_ignored(tools: TrieTools)`

Verify that unknown predicate fields are silently ignored and the matching still succeeds.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_invalid_predicate_returns_error fingerprint=a7cc46c17ae0d8aa0cd7f2ea984b0423139fb7ac60d05209e81e0ff92529668d body_fp=5e22a3f0d8cd032a940531dc3d26d2798d73a9396fee966dcbfb9fe2a82d785d source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_invalid_predicate_returns_error(tools: TrieTools)`

Assert that passing a non-dict predicate to `TrieTools.grep` returns an `invalid_argument` error envelope.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_kind_none_when_no_name_contains fingerprint=4e6e6519556d6b7fd8d18bba3fffc5f082582756e2362308de5d5c28e746be5e body_fp=46b1dc16f9985a4d25309ced50978929541ba0757cfa8cc6341222e4fb9c696f source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_fallback_kind_none_when_no_name_contains(tools: TrieTools)`

Assert that `grep` returns `fallback.kind == "none"` when the predicate lacks `name_contains` and yields no hits.

- `fallback.note` must mention `name_contains` to guide the agent.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_kind_text_match_empty_for_unseen_string fingerprint=69f80642424418ade7fb9f362dc9f273b6a72bb84ecb843ccc644431f6056736 body_fp=fe1db65d8e3d3b4e3be2675a33df1de8df72e659b4f62610465b77a5bff7ce2e source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_fallback_kind_text_match_empty_for_unseen_string(tools: TrieTools)`

Assert that a `name_contains` query matching no source yields `fallback.kind == "text_match_empty"` with the original query echoed back.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_kind_text_match_redirects_via_body_match fingerprint=d62ca25bade3109437990a6051d0a8e8811a4c2b569a8dc05e9bff1f79505cb8 body_fp=ab4cbdb5e5bb26660447e85d8efd53d1880af38de36b217fa9fcbb22bba8b5db source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_fallback_kind_text_match_redirects_via_body_match(tools: TrieTools)`

Assert that when a query string appears inside a symbol's body (not its name), `grep` fallback returns the enclosing symbol with `kind="text_match"`.

- `fallback.kind`: must equal `"text_match"` when body-only match occurs.
- `fallback.matches[*].text_match_hits_in_body`: count of in-body occurrences, ≥ 1.
- Each fallback match also carries `inbound_count` and `outbound_count` for hub-ranking.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_ranks_by_inbound_count_desc fingerprint=ef3ac182e9ce5a40ceecd0150cf8383538870bd63efa253d6c0217440cccaa12 body_fp=4036fa2a383890b49214b3231b74d08bc3fde3bf430ce0ce491d74fbc371a951 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_fallback_ranks_by_inbound_count_desc(tools: TrieTools)`

Assert that `grep` fallback candidates are ordered by `inbound_count` descending when multiple matches exist.

- Skips if the fixture yields a direct symbol hit or fewer than two fallback candidates.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_caps_matches_and_notes_truncation fingerprint=ecfb2d89504fa8c1d8605600e0862e1c961e5ed2840d64902cb9fc4e173cb723 body_fp=af3bc35382dc8aa3da7d5f0bdfaaed3af9d2602c3073aac90e501e7f84073e26 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_fallback_caps_matches_and_notes_truncation(tools: TrieTools)`

Assert that when `grep_fallback_match_limit` is 1, the fallback truncates matches to 1 and includes a truncation note.

- Forces `grep_fallback_match_limit=1` on `tools.mcp_cfg` to exercise truncation on a small fixture.
- Verifies `fallback.unique_symbols > 1` confirms more results exist beyond the cap.
- Confirms the single returned match still carries `qname` and `inbound_count`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_omits_truncation_note_when_under_cap fingerprint=cf99e3b6a8f38acee3321f95f67be04eb837de301219103c85baec04b0a7bad0 body_fp=360555f14542968638b9a0e9c6012e3d8ea7dde936a7d7e8acb4aad129f896d2 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_fallback_omits_truncation_note_when_under_cap(tools: TrieTools)`

Assert that `fallback.note` contains no truncation text when all matches fit within `match_limit`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_honours_scope_prefix fingerprint=31b191790a84b0b474a2cc9861f586ab8ea42430ceded08fcc62bdb2df882d24 body_fp=2f21cea8fbd1d14ed3e5000d629b41dba802f86fc3390d18b14197750d4a9bc2 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_fallback_honours_scope_prefix(tools: TrieTools)`

Assert that `scope_prefix` filters fallback candidates, excluding `lib:` symbols when prefix is `"app"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_normal_hits_path_omits_fallback_key fingerprint=e4d4fa9ea51cf2db4cfeb5df2b356f09c2f3af9fb4af96059369c25e6b38f07d body_fp=c0f9fb82056027f99025af96bd69463433b507766eaee4a98977c25cbe71b07a source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_normal_hits_path_omits_fallback_key(tools: TrieTools)`

Assert that a successful `grep` response contains no `fallback` key.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_returns_prose_and_neighbours fingerprint=8c1f77548638b430933ea0f0fab8a398b6ee3ac0f3dce12584d0dc79166d6f8e body_fp=76e5233bf1cac4b742b5a930a64bd860e15c012a52296f000ee1b631dc00a040 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_read_returns_prose_and_neighbours(tools: TrieTools)`

Verify `TrieTools.read` returns the prose body, correct callers, and empty callees for `lib:slugify`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_source_pointer_shape fingerprint=420bf61a94fb75358593559620c310977d02c1bfeeb15481f3806550aeb73e97 body_fp=da5b1aacc53b5069d616570f62b84111932370c7514ca7c10a256eca2929313a source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_read_source_pointer_shape(tools: TrieTools)`

Assert `read` returns a `source_pointer` in `"<file>:<start>-<end>"` format.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_neighbour_carries_one_liner fingerprint=51c2f2f644f316fdeabf34c1c1d3b0dc3b57ec9e2f746d8c04d682b4cf8fd044 body_fp=abf9024b5de4a7338d407d63f7a0b6e8d742d9069f0b865ba340b8bb3f96718e source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_read_neighbour_carries_one_liner(tools: TrieTools)`

Assert that each caller entry in `TrieTools.read` response includes a populated `one_liner` field.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_unknown_qname_returns_not_found fingerprint=3265a0090391b2d6756d124cacb28e9a01e3e19ee7b45fe0032c752b36efb7f7 body_fp=0439a0463cdbe60f7ae4835b2f3450dd4e5335f50e6ddb00158359f0b14a582e source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_read_unknown_qname_returns_not_found(tools: TrieTools)`

Assert `TrieTools.read` returns a `not_found` error envelope for an unrecognised qname.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_fuzzy_suggestion_for_typo fingerprint=656607d4483ca9d33fd84a8e21cd913fd53f6dfb9c395347ff19d836dabaa261 body_fp=45155667fcaf36e4349ecca28738468b6b738dc193c50843214fd45dff8f614b source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_read_fuzzy_suggestion_for_typo(tools: TrieTools)`

Assert that `TrieTools.read` returns an actionable suggestion when given a typo qname.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_callers_returns_topology fingerprint=ba52df6ec0918227c8a41b6a0d14ab17f8fca12de24f0684dd8eb190b5e31c9d body_fp=3f1739993e570447be4a276d95d9b226aec1250ebc36e14ba075db9358ef74f3 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_trace_callers_returns_topology(tools: TrieTools)`

Verify `TrieTools.trace` returns correct root, nodes, and directed edges when traversing callers.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_callees_returns_outbound fingerprint=0f7a79554ab1ccc241fd5da78d98609b43458bbc13f8ab26ace19fde87547dde body_fp=6fd8b8755b0463530864128c71b6fdb035f2b8f80cc076973257e9d73fc580d9 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_trace_callees_returns_outbound(tools: TrieTools)`

Verify `TrieTools.trace` returns outbound callee nodes and edges for `app:make_url`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_both_directions fingerprint=d982c36f43d513419ade4e39cc8a34a1405626cf97bdb9cf3043e5dc8e96bab0 body_fp=2ae2f49934bbb5f92fc0720a4e531990eb59118467152546f0b7b97080bdbe14 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_trace_both_directions(tools: TrieTools)`

Verify `TrieTools.trace` with `direction="both"` includes caller-side nodes and edges tagged `"in"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_invalid_direction_returns_error fingerprint=ee66239794f468126ebd3f5e9d557088e75a14791456cb94d3242b919f9a1712 body_fp=c445510a3eb6f58220ae2d670d4dff79585e8e4970ae5acfc8984795180a44b2 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_trace_invalid_direction_returns_error(tools: TrieTools)`

Assert `TrieTools.trace` returns an `invalid_argument` error when given an unrecognised `direction` value.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_unknown_qname_returns_not_found fingerprint=4a972421a152c7b560db28c9f942d12a1917d194cc1acb5041774f2b39f1b89d body_fp=bc0cd9f37142c4ab19640b6ac50229b8a7aea350c16fd4816c0f949ddd81b85b source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_trace_unknown_qname_returns_not_found(tools: TrieTools)`

Assert that `TrieTools.trace` returns a `not_found` error for an unrecognised qualified name.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_depth_zero_returns_only_root fingerprint=76be5ecaba8cb2a295a796f304e77c718a9dcc8d23868995efa57a5182d2a1c2 body_fp=bbda71aee68332e10ace905728dc4af7b79af4080895a78ef956893fb11e22a5 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_trace_depth_zero_returns_only_root(tools: TrieTools)`

Assert that `TrieTools.trace` with `depth=0` returns only the root node and no edges.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_depth_clamp_adds_note fingerprint=c455960b8dcfb8693c4e826945685a9217238b8705ee7806c1ca182dccf62c13 body_fp=f5000162458120fc225da17c0c6a0cd03d496152c382c1b3ee5c1a7fa20a84be source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_trace_depth_clamp_adds_note(tools: TrieTools)`

Assert that requesting a depth exceeding `trace_max_depth` adds a "clamped" note to the `trace` output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_build_server_registers_three_verbs fingerprint=6b9681c689a428da5e4f2498ee941fd5a83453ab2b5fb8299f484f077f69d5a3 body_fp=0e547bf3ddfa84680c97e6a03d12387c460dbd54bf9b369ad5c37222d5efc94f source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_build_server_registers_three_verbs(populated_project: Path)`

Assert that `build_server` returns a FastMCP instance with all 11 expected tool names registered.

- Checks core verbs: `grep`, `read`, `trace`.
- Checks extended verbs: `grep_str`, `grep_entry_points`, `grep_symbol`, `grep_symbol_and_neighbours`, `explain_symbol`, `explain_symbol_references`, `trace_flow`, `explain_flow`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_build_server_wire_names_bind_to_internal_methods fingerprint=a480374391cd52c59bd6c51db2664d53e9150773ce64b5a08555c94f8cf832c5 body_fp=7d09464ce00a1ac6c3e4d14473f0edbe70591a2069aeab7efbd860e85eeab3f9 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_build_server_wire_names_bind_to_internal_methods(populated_project: Path)`

Assert that each FastMCP wire tool's `fn` attribute is the matching `TrieTools` instance method.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:dual_rank_project fingerprint=af9da9099ff42de6faafedd130917c97fed67bb2a29f4c57a47dd28b104a936c body_fp=1a8271da2be5a1995d2376c2cc872938008ac0dbee25464cc3f5cc75d7f21401 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `dual_rank_project(tmp_path: Path) -> Path`

Pytest fixture that builds a scanned, synced project with two equal-text-score symbols differing only in inbound-edge count.

- `hub_authenticate`: 3 inbound refs across `svc_a/b/c.py`
- `auth_check`: 2 inbound refs across `check_a/b.py`; expected to rank first under `(score DESC, inbound_count ASC)`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_entry_points_niche_ranks_before_hub fingerprint=a5bf02d8993e8282336d29b02cec7ebb34624737bcbad9c62cbda7acad54290e body_fp=f50e4f2b4692eebeb34b0335344f3ac41679b136d9234b5cca6c5d6b5cac6d8d source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_entry_points_niche_ranks_before_hub(dual_rank_project: Path)`

Assert that `grep_entry_points` ranks the lower-inbound symbol before the higher-inbound hub when relevance scores are equal.

- `dual_rank_project`: fixture with `auth_check` (2 inbound) and `hub_authenticate` (3 inbound), both matching "auth".
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_entry_points_hits_carry_score fingerprint=bf76df08b996d67ba20379770a38f838d8fe1c762948d49445555df41368cc37 body_fp=59f5f8b276121a757974955f936f0375d5248ab5aa20a711abb36f488bbe71cb source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_entry_points_hits_carry_score(dual_rank_project: Path)`

Assert every hit from `TrieTools.grep_entry_points` contains a positive numeric `score` field.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_symbol_typo_tolerance fingerprint=998a77d9bbc63dc7fa9771cbe44d66c7262382670d46446093a4c0102cb98e51 body_fp=f8b6cdceabb8c8ab864e7522218e751844bfd9367be92dc409d353e7f68775a5 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_symbol_typo_tolerance(tools: TrieTools)`

Verify `TrieTools.grep_symbol` resolves a one-character typo to the correct symbol via rapidfuzz fuzzy matching.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_symbol_returns_score_field fingerprint=d875689a783594250d150f3a147a935eeeb38aeb1fadede0bc7712cc65914a22 body_fp=e48ac50c2bd2db8b559007d9066871f6ada87a7c90ec254a5e29c2105f25d507 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_symbol_returns_score_field(tools: TrieTools)`

Assert that `grep_symbol` returns a positive numeric `score` field on every item in `match` and `similar`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fuzzy_prose_fallback fingerprint=0bdb61dcf7c038d93f1a7a4598b1a770d003ba2609b446451546db3192d4dd4e body_fp=b12bcb32248e004b1731062532f8d8efe883cac7b7f5507f901142dc42409b68 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_fuzzy_prose_fallback(tools: TrieTools)`

Verify that `grep` with an unmatched `name_contains` activates `text_match` or `fuzzy_prose` fallback surfacing `lib:slugify`.

- `"lowercase dash separate"` matches no symbol name but appears in `slugify`'s prose body.
- Asserts `fallback.kind` is `"text_match"` or `"fuzzy_prose"`; if `fuzzy_prose`, asserts matches are non-empty and include `slugify`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_str_fuzzy_fallback fingerprint=67380bf7bf45fed97698909288b028bd324ec109f63ba4924f1ec5a14d9de327 body_fp=2a962922a4694a3f9010de9d3bb9c72a41f4386c5f24c20bb80258f68237c8b0 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_str_fuzzy_fallback(tools: TrieTools)`

Assert `grep_str` returns empty hits and no crash when the pattern matches nothing in source.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_str_fuzzy_fallback_finds_close_name fingerprint=0dc0ff2f1a636680859fd46f2db38dac736a30e6bc5ada90d65313099d97ec0b body_fp=6aebe8b387fe0b93903f66f556343059cb3585feb3a0a4ec6780fa14820ea794 source_ref=8fc83b82f7020ac6511f342049e4b34682ca4f2c -->
## `test_grep_str_fuzzy_fallback_finds_close_name(tools: TrieTools)`

Assert that `grep_str` returns a `fuzzy_one_liner` fallback containing `lib:slugify` when a typo pattern matches nothing via ripgrep.
<!-- trie:end -->