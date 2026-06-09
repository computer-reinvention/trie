---
trie_version: 0.1.5
source: tests/test_mcp.py
file_fingerprint: 84281240afaf8272fbc86b16d6ea3dc4701d63021e4ec1aad04b74713fc3a453
last_synced_at: '2026-06-07T03:57:16Z'
description: 'Tests for the MCP tool surface: `grep`, `read`, `trace`.'
defines:
- kind: module
  qualified_name: tests/test_mcp:__module__
  lines: 1-691
- kind: constant
  qualified_name: tests/test_mcp:PROJECT_TOML
  lines: 21-30
- kind: function
  qualified_name: tests/test_mcp:project
  lines: 34-50
- kind: function
  qualified_name: tests/test_mcp:populated_project
  lines: 54-79
- kind: function
  qualified_name: tests/test_mcp:tools
  lines: 83-86
- kind: function
  qualified_name: tests/test_mcp:test_trie_tools_init_fails_clearly_when_rg_missing
  lines: 92-113
- kind: function
  qualified_name: tests/test_mcp:test_grep_name_contains_returns_matches
  lines: 119-124
- kind: function
  qualified_name: tests/test_mcp:test_grep_returns_one_liner_from_section_body
  lines: 127-133
- kind: function
  qualified_name: tests/test_mcp:test_grep_returns_file_pointer
  lines: 136-138
- kind: function
  qualified_name: tests/test_mcp:test_grep_kind_filter
  lines: 141-147
- kind: function
  qualified_name: tests/test_mcp:test_grep_invalid_kind_returns_error
  lines: 150-153
- kind: function
  qualified_name: tests/test_mcp:test_grep_accepts_constant_and_module_kinds
  lines: 156-168
- kind: function
  qualified_name: tests/test_mcp:test_grep_scope_prefix_filter
  lines: 171-174
- kind: function
  qualified_name: tests/test_mcp:test_grep_scope_exclude_filter
  lines: 177-180
- kind: function
  qualified_name: tests/test_mcp:test_grep_inbound_count_predicate
  lines: 183-188
- kind: function
  qualified_name: tests/test_mcp:test_grep_rank_by_inbound_count
  lines: 191-198
- kind: function
  qualified_name: tests/test_mcp:test_grep_limit_respected
  lines: 201-205
- kind: function
  qualified_name: tests/test_mcp:test_grep_empty_predicate_returns_invalid_argument
  lines: 208-222
- kind: function
  qualified_name: tests/test_mcp:test_grep_empty_predicate_rejected_regardless_of_rank_by
  lines: 225-231
- kind: function
  qualified_name: tests/test_mcp:test_grep_unknown_predicate_field_silently_ignored
  lines: 234-237
- kind: function
  qualified_name: tests/test_mcp:test_grep_invalid_predicate_returns_error
  lines: 240-243
- kind: function
  qualified_name: tests/test_mcp:test_grep_fallback_kind_none_when_no_name_contains
  lines: 249-258
- kind: function
  qualified_name: tests/test_mcp:test_grep_fallback_kind_text_match_empty_for_unseen_string
  lines: 261-268
- kind: function
  qualified_name: tests/test_mcp:test_grep_fallback_kind_text_match_redirects_via_body_match
  lines: 271-289
- kind: function
  qualified_name: tests/test_mcp:test_grep_fallback_ranks_by_inbound_count_desc
  lines: 292-306
- kind: function
  qualified_name: tests/test_mcp:test_grep_fallback_caps_matches_and_notes_truncation
  lines: 309-335
- kind: function
  qualified_name: tests/test_mcp:test_grep_fallback_omits_truncation_note_when_under_cap
  lines: 338-346
- kind: function
  qualified_name: tests/test_mcp:test_grep_fallback_honours_scope_prefix
  lines: 349-364
- kind: function
  qualified_name: tests/test_mcp:test_grep_normal_hits_path_omits_fallback_key
  lines: 367-373
- kind: function
  qualified_name: tests/test_mcp:test_read_returns_prose_and_neighbours
  lines: 379-386
- kind: function
  qualified_name: tests/test_mcp:test_read_source_pointer_shape
  lines: 389-392
- kind: function
  qualified_name: tests/test_mcp:test_read_neighbour_carries_one_liner
  lines: 395-398
- kind: function
  qualified_name: tests/test_mcp:test_read_unknown_qname_returns_not_found
  lines: 401-404
- kind: function
  qualified_name: tests/test_mcp:test_read_fuzzy_suggestion_for_typo
  lines: 407-413
- kind: function
  qualified_name: tests/test_mcp:test_trace_callers_returns_topology
  lines: 419-425
- kind: function
  qualified_name: tests/test_mcp:test_trace_callees_returns_outbound
  lines: 428-431
- kind: function
  qualified_name: tests/test_mcp:test_trace_both_directions
  lines: 434-439
- kind: function
  qualified_name: tests/test_mcp:test_trace_invalid_direction_returns_error
  lines: 442-445
- kind: function
  qualified_name: tests/test_mcp:test_trace_unknown_qname_returns_not_found
  lines: 448-451
- kind: function
  qualified_name: tests/test_mcp:test_trace_depth_zero_returns_only_root
  lines: 454-457
- kind: function
  qualified_name: tests/test_mcp:test_trace_depth_clamp_adds_note
  lines: 460-464
- kind: function
  qualified_name: tests/test_mcp:test_build_server_registers_three_verbs
  lines: 470-493
- kind: function
  qualified_name: tests/test_mcp:test_build_server_wire_names_bind_to_internal_methods
  lines: 496-513
- kind: function
  qualified_name: tests/test_mcp:dual_rank_project
  lines: 522-579
- kind: function
  qualified_name: tests/test_mcp:test_grep_entry_points_niche_ranks_before_hub
  lines: 582-605
- kind: function
  qualified_name: tests/test_mcp:test_grep_entry_points_hits_carry_score
  lines: 608-620
- kind: function
  qualified_name: tests/test_mcp:test_grep_symbol_typo_tolerance
  lines: 623-629
- kind: function
  qualified_name: tests/test_mcp:test_grep_symbol_returns_score_field
  lines: 632-640
- kind: function
  qualified_name: tests/test_mcp:test_grep_fuzzy_prose_fallback
  lines: 643-658
- kind: function
  qualified_name: tests/test_mcp:test_grep_str_fuzzy_fallback
  lines: 661-671
- kind: function
  qualified_name: tests/test_mcp:test_grep_str_fuzzy_fallback_finds_close_name
  lines: 674-690
incoming_refs: 0
outgoing_refs: 12
---
<!-- trie:section symbol=tests/test_mcp:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=8aae9c0160792068985e2d8f76d0fb26134f6f6b03e5f03d32d39b128db471ad source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Tests for MCP tool surface (grep, read, trace) via direct TrieTools invocation.

- Uses FakeTrieClient to mock LLM responses during sync operations
- Sets up fixtures with sample Python code to test symbol resolution and graph navigation
- Exercises error conditions including missing ripgrep dependency and invalid parameters
- Tests fallback mechanisms when primary symbol lookups fail
- Validates wire protocol compatibility between CLI and MCP server interfaces
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:PROJECT_TOML fingerprint=3f524fd58415aac9f548f19d4ad2554a2e411c44f7f8907ce1944fa2fa35a62e body_fp=b996dcbae629f612c5f407796eb861fa2c62508470068b2ea245465383bdd52e source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
String constant containing a complete TOML configuration for test projects.

- Configures scope to include Python files excluding cache directories
- Sets triefacts root directory and source root paths
- Specifies Claude Sonnet 4.6 for bootstrap and cascade operations
- Defines MCP limits for grep results, trace depth, and node counts
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:project fingerprint=3e4b4f7d19d96699d52f90f1396ef4a3c695e286383233613202fea1c0b09b6b body_fp=9f79c581505467fc1c1c2ceb1a210ac1474951fe551c0183018cfd7fd0389843 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Creates a minimal test project with trie.toml config and two Python files.

- `lib.py`: Contains `slugify` (lowercase + dash-separate) and `capitalize` functions
- `app.py`: Contains `make_url` function that imports and uses `slugify`
- Returns the temporary directory path containing the project structure
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:populated_project fingerprint=a54e186816ee0ef181cf7cc6e7058686a0354458a8b46b1d8f711321355a76b5 body_fp=6982558aa1138901afc6357534efbacc8fa47ffc11035f0c948f6a5cbf2e94a0 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Creates a test project fixture with scanned symbols and generated triefacts for MCP tool testing.

- Scans the project to populate the graph database with symbol relationships
- Syncs `lib.py` and `app.py` using FakeTrieClient to generate documentation
- Returns the project path with `.trie/graph.db` containing queryable data
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:tools fingerprint=b89f3ca1611ed5226f820d82ffc6f4d3db27942f64390976744c1fbf0d5e67de body_fp=03851a485a0bfaf6da9ce7379e6be9bbf9d979aecffc4d8f0ba33a8ec4d47b67 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test -->
Creates a TrieTools fixture for the populated test project and ensures cleanup after use.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trie_tools_init_fails_clearly_when_rg_missing fingerprint=2ea97d1b02ea695fbca32b81cfd8377a7e1da3159c9b30a1815fe2099d25638b body_fp=4df7c8bf2d3fc78317a7bf684cf1bca16d55c1971b6168ee2217d647e9423267 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test -->
Tests that TrieTools initialization fails with clear error message when ripgrep binary is missing.

- Simulates missing `rg` by stubbing `shutil.which` to return `None`
- Verifies `RipgrepNotFoundError` is raised with helpful installation guidance
- Ensures error message names the missing binary and provides recovery path
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_name_contains_returns_matches fingerprint=13a70b013b95687914be7cf11a6a2926e39e6d256ed6ee0fc19ec38c6f2bcffb body_fp=38a98c12720cc9939e66af58022964661ece443f86b7ff155573f5f4ef252ad2 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Verifies grep returns symbols with names containing the query string and omits fallback data when matches exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_returns_one_liner_from_section_body fingerprint=37a68231e58a6658814f1e064b7c136eeaa7a7f879f70bdfd4eaa836d69779ad body_fp=c79025cdf684f5b4a75f59f5575f378cff7a2df84451c549678d219d2e0891b5 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Verifies that TrieTools.grep extracts truncated one-liner summaries from triefact bodies.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_returns_file_pointer fingerprint=fd44c10f827063015b2af6e12727ce6f8e2d67973fc32ea706be0a403274f87e body_fp=916c63b90bf1a9714abe16d868b8d57fc080bae1889cb642c41bdb393496afba source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Verifies grep returns file_pointer with filename:line format for symbol locations.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_kind_filter fingerprint=05f736a15cd7708beed46d7beef0835ba93bb4867f848cec7c0d4da66a5d31bf body_fp=0dff48f54ba25b4cd87f4484b381080bd95cd7e919c913a97cfdb4aafe650052 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Tests that grep's kind filter correctly excludes symbols not matching the specified type.

- Uses `kind: "class"` filter with fixtures containing only functions, expecting empty hits
- Verifies fallback still triggers when `name_contains` is present but no symbols match the kind
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_invalid_kind_returns_error fingerprint=93c63e643ced72ef46d974b15a6f15362abaa72e8e7b439e17f8d46411602d2e body_fp=3c4f53351d79ae0a76ab3868a3ae90158f1665fe6bb74e7cffeac97b4617bdf8 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Test that `TrieTools.grep` rejects invalid `kind` filter values with `invalid_argument` error code.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_accepts_constant_and_module_kinds fingerprint=a7b0b5f6a91e85c5d7b2effde7c148be97b61ecfd7966d405518b3d26526bbed body_fp=2d0b57f4708c3e42dbaad9871be155671f3733d669b53446c4f3961f11bb710c source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Verifies that `TrieTools.grep` accepts `"constant"` and `"module"` as valid `kind` filter values without raising an `invalid_argument` error.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_scope_prefix_filter fingerprint=4087ec669cf402755c9ebcba58be379db4f126a23aaa314712e20b33ffa6a9f0 body_fp=623a642584e244aa5b4e4633eb9790d271db0e76af602baf4356776d23c5a09f source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Verify TrieTools.grep filters results to symbols whose file paths start with the given scope prefix.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_scope_exclude_filter fingerprint=d9ed58e0d2cb505d72e32ca79f8f8032c881eff47584a5bf9377a006626e5793 body_fp=43d92b68d7a88808d9897f43dba8eb557f7ef0444c7dcaf80ddb74bca8cca7a6 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Verify that `TrieTools.grep` excludes symbols from specified scopes via `scope_exclude` predicate.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_inbound_count_predicate fingerprint=29ed9feb09b2e5254bd1cef76cabd75536142afaac8b064dcc196599c69f7b0b body_fp=bb0d8f174d90c0da2df164feb5af60fef25555505fbc7ab38942a4595d9c10c5 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Verify that `tools.grep` with `inbound_count` filter returns symbols with at least the specified minimum incoming references.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_rank_by_inbound_count fingerprint=956741b97e66e5508ccc0365fd3a6a04e6e7c6f3cb7da4770fc673b73a03477e body_fp=7175b186b0eb3efd9b0dbd48981602733e903c01556f959d1290a5d1a1ffc285 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Verifies that `TrieTools.grep` results are correctly ranked by inbound_count when `rank_by="inbound_count"` is specified.

- Uses `public_only: True` predicate to avoid empty-predicate rejection
- Asserts first hit has highest `inbound_count` value among returned results
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_limit_respected fingerprint=80407aa581af3497200f623a81e718ea1e94ee91389ac126830562e3b69348af body_fp=f42cd78b9652dcb9ef6069ca81af49cddaea97b6e056dafe43cfca3eea1455ff source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Verifies TrieTools.grep respects the limit parameter by requesting only 1 result and asserting exactly 1 hit is returned.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_empty_predicate_returns_invalid_argument fingerprint=b276ee91748c22279c9a40988da4c4daaebfea8382927b5fe18d9f2f3c5b17ce body_fp=970401a29fe2d63d38ec1360b51f699418963a12f83e8c41a9d8e1d0f653dbee source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Tests that TrieTools.grep rejects empty predicates with invalid_argument error and helpful suggestion.

- Validates rejection for None, {}, {"name_contains": ""}, {"kind": "any"}
- Requires error.code == "invalid_argument" 
- Requires suggestion mentioning "name_contains" or "scope_prefix"
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_empty_predicate_rejected_regardless_of_rank_by fingerprint=173c7d0e853ec0b26f7e6b2344e5c2c4c42c2b1245b1081fca21ec158813dd8d body_fp=304e6ad1c39e44e4583ff581aade57b6f63cd2a2c211eb9018beb01dea1c1b47 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Verifies that TrieTools.grep rejects empty predicates even when rank_by and limit are specified.

- Tests rejection occurs before ranking is consulted
- Expects error.code of "invalid_argument"
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_unknown_predicate_field_silently_ignored fingerprint=d932c0e53093906441747dbaef79cf5c314d42057b100dc5b2f257cc7518c2f0 body_fp=6cef2b69149e11ce0c3cd36871c32e5f3eb9b30c86ff428012b7d18ad970b246 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Verifies that TrieTools.grep ignores unknown predicate fields without raising errors.

- Uses predicate with valid `name_contains` and invalid `totally_made_up_field`
- Confirms grep still returns hits despite the unknown field
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_invalid_predicate_returns_error fingerprint=a7cc46c17ae0d8aa0cd7f2ea984b0423139fb7ac60d05209e81e0ff92529668d body_fp=e01540afb59124e809757bcbf4348e89e83371542c9b3567c0a2187c539e4bbd source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Verifies grep rejects non-dictionary predicates with invalid_argument error code.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_kind_none_when_no_name_contains fingerprint=4e6e6519556d6b7fd8d18bba3fffc5f082582756e2362308de5d5c28e746be5e body_fp=808be44eca8add42062a7c6afeec9c843c474cbe665a93c014bbe159f59cda50 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Test that grep returns a fallback envelope with kind "none" when a predicate without name_contains yields no matches.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_kind_text_match_empty_for_unseen_string fingerprint=69f80642424418ade7fb9f362dc9f273b6a72bb84ecb843ccc644431f6056736 body_fp=ceea1ee2fe24393fa09592d6589d0ab2a6e29a7fb13ae5a76ac364c048e7a369 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Tests TrieTools.grep fallback behavior when name_contains query matches no source text.

- Verifies fallback reports `text_match_empty` kind for non-existent strings
- Confirms query string is preserved in fallback response
- Ensures empty hits list signals clear "doesn't exist" rather than ambiguous result
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_kind_text_match_redirects_via_body_match fingerprint=d62ca25bade3109437990a6051d0a8e8811a4c2b569a8dc05e9bff1f79505cb8 body_fp=a9f9890677f220139eb8d5bcaee30548fdc6d40c8bb8c6d75e5bb980734e9922 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Tests TrieTools.grep fallback text matching when query appears in symbol bodies but not names.

- Uses "replace" which appears in lib:slugify's body but is not a symbol name
- Verifies fallback returns text_match kind with enclosing symbols as matches
- Confirms matches include text_match_hits_in_body count and standard hit fields
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_ranks_by_inbound_count_desc fingerprint=ef3ac182e9ce5a40ceecd0150cf8383538870bd63efa253d6c0217440cccaa12 body_fp=4c047f8c4876a0041c77428401f6928bc800900ab0dde5ae5c7c81e00526778b source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Verifies that grep's fallback text-match results rank by descending inbound_count.

- Queries for "title" which appears in source but not as symbol name
- Confirms fallback ordering prioritizes hub symbols before leaf symbols
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_caps_matches_and_notes_truncation fingerprint=ecfb2d89504fa8c1d8605600e0862e1c961e5ed2840d64902cb9fc4e173cb723 body_fp=4defd77865a767ffb2f597072ddfcb3b196f615707169a8589a6e57facaaade9 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Tests that grep's fallback mechanism caps excessive matches and includes truncation notes.

- Forces a tiny match limit to exercise truncation on the small test fixture
- Verifies fallback returns exactly one match when capped at 1 
- Checks that `unique_symbols` indicates more candidates were found
- Ensures truncation note contains "of" to communicate incomplete results
- Confirms returned matches still carry standard fields like `qname` and `inbound_count`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_omits_truncation_note_when_under_cap fingerprint=cf99e3b6a8f38acee3321f95f67be04eb837de301219103c85baec04b0a7bad0 body_fp=a9548def3accc79b05d07ca23e28d0657120c151ae5ed0b29d520d382f4d5e8a source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Tests that grep fallback omits truncation warnings when match count stays within limit.

- Searches for "replace" which appears in source but isn't a symbol name
- Verifies fallback response excludes "showing top" language when results fit within cap
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_honours_scope_prefix fingerprint=31b191790a84b0b474a2cc9861f586ab8ea42430ceded08fcc62bdb2df882d24 body_fp=5b8b6c3a21bade6f9b855fef7b8af18c47c88c3ae07aa73de1db6192da4bba7c source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Verify that TrieTools.grep respects scope_prefix filter when falling back to text search for non-matching symbol names.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_normal_hits_path_omits_fallback_key fingerprint=e4d4fa9ea51cf2db4cfeb5df2b356f09c2f3af9fb4af96059369c25e6b38f07d body_fp=3a3f17e5a24da2b03ebf5366361c6f3ec8b60bdf54c478993e5c91b9f0779225 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Asserts that `TrieTools.grep` omits the `fallback` key when primary search returns hits.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_returns_prose_and_neighbours fingerprint=8c1f77548638b430933ea0f0fab8a398b6ee3ac0f3dce12584d0dc79166d6f8e body_fp=16835740c35ea08067deb52b701db95fbba764e04fe7e686d325bc2f1aa438b4 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Test that TrieTools.read returns structured output containing qname, prose documentation, and caller/callee neighbor lists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_source_pointer_shape fingerprint=420bf61a94fb75358593559620c310977d02c1bfeeb15481f3806550aeb73e97 body_fp=cbd3a6570ef2967647c16c1c10cf7de4fed58d730970e3bd9507f3f726d293e6 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Verifies that TrieTools.read returns a source_pointer field formatted as "file:start-end".
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_neighbour_carries_one_liner fingerprint=51c2f2f644f316fdeabf34c1c1d3b0dc3b57ec9e2f746d8c04d682b4cf8fd044 body_fp=23502f8d944170f55cbc44fe71314f48a1b892622d23e5a76988ef8b11a31a2e source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=mcp-server -->
Verifies that `read` returns caller/callee neighbours with a populated `one_liner` field from their triefact body.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_unknown_qname_returns_not_found fingerprint=3265a0090391b2d6756d124cacb28e9a01e3e19ee7b45fe0032c752b36efb7f7 body_fp=b60c7785a5ebf34813505cb2b42f5e28a9b0424e6cc9f344b300fbeaa7aebe57 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Verify TrieTools read method returns error envelope with not_found code for unknown symbol names.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_fuzzy_suggestion_for_typo fingerprint=656607d4483ca9d33fd84a8e21cd913fd53f6dfb9c395347ff19d836dabaa261 body_fp=1e16595f82f06d08d3af11310c2ed4e77f4fca84de607b81906dbf94fa9f0d91 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Tests that the read tool returns a fuzzy suggestion when given a qname with a typo.

- Calls `tools.read("lib:slugfy")` with a misspelled qname ("slugfy" instead of "slugify")
- Verifies the response contains an error with a suggestion that either mentions "slugify" directly or guides the user to use `grep()`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_callers_returns_topology fingerprint=ba52df6ec0918227c8a41b6a0d14ab17f8fca12de24f0684dd8eb190b5e31c9d body_fp=97b4192f602a4fc81208a94636a971a6351aa38b31de0eb75dae3450189ceb73 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Verifies that TrieTools.trace returns correct topology with root, nodes, and caller edges for direction="callers".
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_callees_returns_outbound fingerprint=0f7a79554ab1ccc241fd5da78d98609b43458bbc13f8ab26ace19fde87547dde body_fp=e73e4d139ff8588d39ce912ac1e7dcb7ef7aeb2ebb6a2bce35ee473aa92feecb source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Test that `TrieTools.trace` with `direction="callees"` returns outbound references in the graph structure.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_both_directions fingerprint=d982c36f43d513419ade4e39cc8a34a1405626cf97bdb9cf3043e5dc8e96bab0 body_fp=38689dcece06e7c171172026c580aa12515acfe64c14f7d790201953f04bad11 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Tests TrieTools.trace with bidirectional flow discovery.

- Verifies callers appear in nodes when direction is "both"
- Checks edges carry directional metadata for visualization
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_invalid_direction_returns_error fingerprint=ee66239794f468126ebd3f5e9d557088e75a14791456cb94d3242b919f9a1712 body_fp=2f43d622b30b94e9c276107d37bbdb29e1e4abfd55bd1723cf00714e386c0da0 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Verifies that TrieTools.trace rejects an invalid direction parameter with an "invalid_argument" error code.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_unknown_qname_returns_not_found fingerprint=4a972421a152c7b560db28c9f942d12a1917d194cc1acb5041774f2b39f1b89d body_fp=9bc63f81e450e1bf480f07438eb1499e75152f77ac2c6d456b68f74caca42605 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
## test_trace_unknown_qname_returns_not_found

Verifies that TrieTools.trace returns a not_found error for nonexistent symbols.

- Tests the error envelope structure when an invalid qname is passed to trace
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_depth_zero_returns_only_root fingerprint=76be5ecaba8cb2a295a796f304e77c718a9dcc8d23868995efa57a5182d2a1c2 body_fp=11c567dde7da9bc8423d8827a4f588b836dddc74664fc8fd360db71e6bf9bcd0 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Verifies that trace with depth=0 returns only the root symbol with no edges.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_depth_clamp_adds_note fingerprint=c455960b8dcfb8693c4e826945685a9217238b8705ee7806c1ca182dccf62c13 body_fp=08f8f6001272fdf61e7b1e11b14cfdb2422712187f89ab03ab670e2f46a66336 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Tests that TrieTools.trace adds a note when depth exceeds the configured maximum.

- Requests depth=99 against default max of 5 and verifies "clamped" appears in response notes
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_build_server_registers_three_verbs fingerprint=6b9681c689a428da5e4f2498ee941fd5a83453ab2b5fb8299f484f077f69d5a3 body_fp=10ba7f1359654a3c30aae2d0fe93b17004beff410dd48f55cdfb9f1371dddd87 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Verify that build_server registers all expected tools in the FastMCP server.

- Core tools: `grep`, `read`, `trace` must be available
- Extended toolset: 8 additional tools including `grep_str`, `explain_symbol`, `trace_flow`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_build_server_wire_names_bind_to_internal_methods fingerprint=a480374391cd52c59bd6c51db2664d53e9150773ce64b5a08555c94f8cf832c5 body_fp=924f52c92dae919032980f65f3862c35e5efa14c489cb3b1e96fd0205a28b840 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Verifies that MCP tool names directly dispatch to corresponding TrieTools methods.

- Pins the mapping `grep -> grep`, `read -> read`, `trace -> trace`
- Ensures CLI and MCP surfaces share one implementation per verb
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:dual_rank_project fingerprint=ddb09bc1e817a930bec9a532e1c272d2dfef3a3e605bc48f4679ba42ed216ee6 body_fp=f30f5d13836baf183f630d87fce9b19ec54d81ac3941644340d7026b3add5bae source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Creates test project with two auth symbols ranked by inbound count for fuzzy matching tests.

- Returns populated temporary project with hub_authenticate (3 callers) and auth_check (2 callers)  
- Both symbols contain "auth" for equal text relevance but different centrality scores
- Tests sorting behavior where niche symbols rank before hubs at equal relevance
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_entry_points_niche_ranks_before_hub fingerprint=a5bf02d8993e8282336d29b02cec7ebb34624737bcbad9c62cbda7acad54290e body_fp=5cf31bb5473fa0a0eca8dcd6199277e19d4abd1e61a76ed4f2d5d93228875539 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test -->
Verifies `grep_entry_points` ranks niche symbols before hubs when relevance scores are equal.

- Uses `dual_rank_project` fixture with `auth_check` (2 inbound) and `hub_authenticate` (3 inbound)
- Queries "auth" to match both symbols with equal text relevance
- Asserts `auth_check` appears before `hub_authenticate` in results
- Tests the sort key: score DESC, inbound_count ASC
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_entry_points_hits_carry_score fingerprint=bf76df08b996d67ba20379770a38f838d8fe1c762948d49445555df41368cc37 body_fp=249bc8f0cd416cd5944a6883261bdef30bb3eeacddb4863ef73ff7af41c2adb8 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test -->
Verifies that grep_entry_points results include a numeric score field for ranking.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_symbol_typo_tolerance fingerprint=998a77d9bbc63dc7fa9771cbe44d66c7262382670d46446093a4c0102cb98e51 body_fp=ba9922e48ca93082d1577f0aabfc32b42abc69ada104d608576ddc406a05d3e4 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=mcp-server -->
Verifies that TrieTools.grep_symbol resolves single-character typos using fuzzy matching at cutoff 45.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_symbol_returns_score_field fingerprint=d875689a783594250d150f3a147a935eeeb38aeb1fadede0bc7712cc65914a22 body_fp=b6522a8833f3c05954c06fb29adf9f56aa321ed8df6b0c53d4036121ee5d9a46 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Validates that `TrieTools.grep_symbol` returns symbols with numeric score fields in both match and similar arrays.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fuzzy_prose_fallback fingerprint=0bdb61dcf7c038d93f1a7a4598b1a770d003ba2609b446451546db3192d4dd4e body_fp=bbf5eef1f7e55f55c6a8149e2e35aa003eec554fd6c338e9f75af34114541326 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=mcp-server -->
Verifies grep's fuzzy prose fallback surfaces symbols containing concept words when name_contains finds no exact symbol name matches.

- Uses "lowercase dash separate" as a test phrase that appears in slugify's triefact body but not its name
- Expects either text_match (ripgrep literal match) or fuzzy_prose (fuzzy scoring) fallback types
- When fuzzy_prose fallback activates, validates slugify appears in the returned matches
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_str_fuzzy_fallback fingerprint=67380bf7bf45fed97698909288b028bd324ec109f63ba4924f1ec5a14d9de327 body_fp=9673fa25de4a0d63b8514286b76c720885febfc2e3b82f185b3c9511f11453df source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Tests that `grep_str` returns fuzzy fallback when pattern matches nothing in source.

- Verifies empty hits array when nonsense pattern finds no regex matches
- Confirms response includes `hits` key to prevent crashes on malformed responses
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_str_fuzzy_fallback_finds_close_name fingerprint=0dc0ff2f1a636680859fd46f2db38dac736a30e6bc5ada90d65313099d97ec0b body_fp=4712f18aa206c321f984553fd76b716f1c4b2eac2154ca80152bb5a6d3e7f9b6 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
Verify grep_str returns fuzzy fallback when regex search fails but symbol name is close to query.

- Tests grep_str with typo "slugufy" expecting fuzzy_one_liner fallback to surface "slugify"
- Skips assertion if ripgrep accidentally finds literal matches in source
- Validates fallback contains expected symbol via name matching
<!-- trie:end -->