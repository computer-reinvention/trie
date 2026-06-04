---
trie_version: 0.1.5
source: tests/test_mcp.py
file_fingerprint: 84281240afaf8272fbc86b16d6ea3dc4701d63021e4ec1aad04b74713fc3a453
last_synced_at: '2026-06-04T00:38:27Z'
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
<!-- trie:section symbol=tests/test_mcp:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=ba0aac06062a7cf422c9fa5151a89bcf728b124ae7d0f1e8296bcb8c9008dd5b source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Test suite for MCP tools (`grep`, `read`, `trace`) exercised via TrieTools directly.

- **Fixtures**: Create temporary projects with code samples and populated triefact databases
- **Core tools**: Test `grep` symbol search with filters, `read` symbol details, `trace` call graphs
- **Fallback behavior**: Test text-match fallback when symbol queries find no hits
- **Error handling**: Test invalid arguments, missing dependencies, unknown symbols
- **Extended toolset**: Test fuzzy matching tools like `grep_entry_points`, `grep_symbol`
- **Server construction**: Verify FastMCP server registration and tool binding
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:PROJECT_TOML fingerprint=3f524fd58415aac9f548f19d4ad2554a2e411c44f7f8907ce1944fa2fa35a62e body_fp=9a192c06eeff08fa186de5836a33a8641403f275187736fee2dee04558c97f7b source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
TOML configuration string containing test project settings for trie.

- Defines scope includes/excludes, triefacts paths, model choices, and MCP tool limits
- Used by test fixtures to create temporary projects with realistic config
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:project fingerprint=3e4b4f7d19d96699d52f90f1396ef4a3c695e286383233613202fea1c0b09b6b body_fp=94e918ec7308b2d2652ebb31bc767f1ae80ca9d891c825b9738860f8e30dcafc source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
## project

Creates a temporary project directory with trie configuration and Python modules for testing.

- Returns the temporary directory path containing the test project structure
- `lib.py` contains `slugify` and `capitalize` functions with docstrings
- `app.py` imports `slugify` and defines `make_url` function that uses it
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:populated_project fingerprint=a54e186816ee0ef181cf7cc6e7058686a0354458a8b46b1d8f711321355a76b5 body_fp=8455313342aec3495670ebe8d35cacfe422a0582bc4360a8f31bf72cc9a71166 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Pytest fixture that creates a project with scanned symbols and synchronized triefacts for MCP tool testing.

- Runs scan_project to populate the graph database with symbol relationships
- Syncs lib.py and app.py with fake triefact content using FakeTrieClient
- Returns the project path with .trie/graph.db ready for MCP tool queries
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:tools fingerprint=b89f3ca1611ed5226f820d82ffc6f4d3db27942f64390976744c1fbf0d5e67de body_fp=b3e2925cf9fca4a40b6393a4fc86442b09d99a13504093c90ee6bab38814ec3f source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Creates a TrieTools instance for the populated project and yields it, closing on teardown.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trie_tools_init_fails_clearly_when_rg_missing fingerprint=2ea97d1b02ea695fbca32b81cfd8377a7e1da3159c9b30a1815fe2099d25638b body_fp=baf1d269da23210b2de412b024416fd6955e8530680e82f315eae4b5dd5d8ad7 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Tests that TrieTools initialization raises RipgrepNotFoundError when the `rg` binary is missing.

- Patches `shutil.which` to return None, simulating missing ripgrep dependency
- Verifies the error message mentions "rg" and includes installation guidance
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_name_contains_returns_matches fingerprint=13a70b013b95687914be7cf11a6a2926e39e6d256ed6ee0fc19ec38c6f2bcffb body_fp=4d9298120df94bdf6f6c182b56fc40d37f135254cf328b9da65bb8611d53c011 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Tests that TrieTools.grep returns matching symbols when name_contains filter finds hits.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_returns_one_liner_from_section_body fingerprint=37a68231e58a6658814f1e064b7c136eeaa7a7f879f70bdfd4eaa836d69779ad body_fp=643c43c1d084523b079d100e26f1bdda76b7e7ecbb93ae5a5dc985ff3bedb958 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Verifies that TrieTools.grep extracts a truncated one-liner from symbol documentation body.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_returns_file_pointer fingerprint=fd44c10f827063015b2af6e12727ce6f8e2d67973fc32ea706be0a403274f87e body_fp=d2096309fef3358e2c572a63734e3a63a1a7eb7919595d82e53bfb2e0ab89bda source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Verifies that TrieTools.grep returns file_pointer field in format "filename:line_number".
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_kind_filter fingerprint=05f736a15cd7708beed46d7beef0835ba93bb4867f848cec7c0d4da66a5d31bf body_fp=fd275224debc89469827ad45a9cb034675e5d5d801cf31d5f7853ff724ed14f6 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Verifies TrieTools.grep filters results by symbol kind, returning empty hits when filtering for classes in a function-only fixture.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_invalid_kind_returns_error fingerprint=93c63e643ced72ef46d974b15a6f15362abaa72e8e7b439e17f8d46411602d2e body_fp=c75e01d638974573d53d24913fb83abc3e4a42520761be287a3452fb110457cd source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Verifies TrieTools.grep returns an invalid_argument error when given an unsupported kind filter.

- Uses "macro" as an invalid kind value to trigger the error condition
- Asserts the error response has the expected structure and error code
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_accepts_constant_and_module_kinds fingerprint=a7b0b5f6a91e85c5d7b2effde7c148be97b61ecfd7966d405518b3d26526bbed body_fp=f36b4216b2f09fbf4c3a24470ae850788a88af3cc73a4ca84dffa7aeaddc1840 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Verifies that TrieTools.grep accepts "constant" and "module" as valid kind filter values without returning validation errors.

- Tests both `kind: "constant"` and `kind: "module"` predicates
- Asserts no `invalid_argument` error envelope is returned
- Does not verify hit content since fixture may lack these symbol types
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_scope_prefix_filter fingerprint=4087ec669cf402755c9ebcba58be379db4f126a23aaa314712e20b33ffa6a9f0 body_fp=62ced56e86cd34802febadb13dcea21dc7a3f784993549438b7e6c47a149aa48 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
## test_grep_scope_prefix_filter

Tests that `TrieTools.grep` respects the `scope_prefix` predicate by filtering hits to files starting with the specified prefix.

- Verifies all returned file paths begin with "lib"
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_scope_exclude_filter fingerprint=d9ed58e0d2cb505d72e32ca79f8f8032c881eff47584a5bf9377a006626e5793 body_fp=5215a2fbfb6bb02d573dac4f570c45eb140daa62abc20f489ba498aa02d901e4 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Validates TrieTools.grep excludes symbols from files matching scope_exclude patterns.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_inbound_count_predicate fingerprint=29ed9feb09b2e5254bd1cef76cabd75536142afaac8b064dcc196599c69f7b0b body_fp=e8b9c24f271ac62ac2355ae3c30fd472c186372a84a859b6240df62d8666b030 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Tests that `grep` correctly filters symbols by minimum inbound edge count using the `inbound_count` predicate.

- Verifies symbols with at least one caller (like `lib:slugify`) appear in results
- Confirms symbols with no callers (like `app:make_url`) are excluded from results
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_rank_by_inbound_count fingerprint=956741b97e66e5508ccc0365fd3a6a04e6e7c6f3cb7da4770fc673b73a03477e body_fp=e1fa8d3674b12b59613d2115477df6fc4209607070124788fcebadf926a66e27 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Verify that `TrieTools.grep` returns results sorted by inbound count descending when `rank_by="inbound_count"` is specified.

- Uses `public_only: True` predicate to avoid empty-predicate rejection
- Asserts first hit has highest inbound_count relative to last hit
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_limit_respected fingerprint=80407aa581af3497200f623a81e718ea1e94ee91389ac126830562e3b69348af body_fp=223014f29a2264aa3b55d7d8885c1d2d51e359b946d14e12e0a67b04149a82e8 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Verifies TrieTools.grep respects limit parameter by asserting result contains exactly one hit.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_empty_predicate_returns_invalid_argument fingerprint=b276ee91748c22279c9a40988da4c4daaebfea8382927b5fe18d9f2f3c5b17ce body_fp=e9e07f2458336744f492f7e98a0658fb1f8f202e656734bcbfc14bb6084d9314 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Tests that TrieTools.grep rejects empty predicates with invalid_argument error and helpful suggestion.

- Tests rejection of None, {}, {"name_contains": ""}, {"kind": "any"} predicates
- Verifies error.code is "invalid_argument" for each case  
- Confirms suggestion mentions usable filter like "name_contains" or "scope_prefix"
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_empty_predicate_rejected_regardless_of_rank_by fingerprint=173c7d0e853ec0b26f7e6b2344e5c2c4c42c2b1245b1081fca21ec158813dd8d body_fp=86d9e5b9f7645bb0adfdebf069575adcfd24d3906eb5cd4268df43b989ec1c6b source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Verifies that `TrieTools.grep` rejects empty predicates even when `rank_by` is specified.

- Tests that `rank_by` parameter doesn't bypass empty predicate validation
- Asserts error code is "invalid_argument" for empty dict predicate
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_unknown_predicate_field_silently_ignored fingerprint=d932c0e53093906441747dbaef79cf5c314d42057b100dc5b2f257cc7518c2f0 body_fp=433aa302ea332001f720288746887490122dfe206555a664961d29f17fe84717 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Verifies that TrieTools.grep ignores unknown predicate fields without raising errors.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_invalid_predicate_returns_error fingerprint=a7cc46c17ae0d8aa0cd7f2ea984b0423139fb7ac60d05209e81e0ff92529668d body_fp=5d94fd4cbc122c16bcf75ee840b5b265eae99c395620fd440d0aba4172d26917 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Verifies that TrieTools.grep returns an "invalid_argument" error when passed a non-dict predicate.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_kind_none_when_no_name_contains fingerprint=4e6e6519556d6b7fd8d18bba3fffc5f082582756e2362308de5d5c28e746be5e body_fp=2d13c68e8736765a17845297b37decf61ecd2f1cce97c29e9ab0461dd74b09c3 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Verifies grep fallback returns `kind="none"` when predicate lacks `name_contains` and finds no symbol matches.

- Tests predicate `{"inbound_count": {"min": 999}}` which matches no symbols in fixture
- Asserts `hits` is empty and `fallback.kind` is "none" 
- Confirms fallback note mentions "name_contains" to explain why text search was skipped
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_kind_text_match_empty_for_unseen_string fingerprint=69f80642424418ade7fb9f362dc9f273b6a72bb84ecb843ccc644431f6056736 body_fp=0bdc2ae1004237ded351277a28d24846149ff57087aa7997fcf0ed9e1fa3e071 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Tests that `grep` returns `text_match_empty` fallback when `name_contains` string doesn't exist in source.

- Verifies fallback kind is `text_match_empty` for nonexistent query strings
- Confirms fallback query field matches the original search term
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_kind_text_match_redirects_via_body_match fingerprint=d62ca25bade3109437990a6051d0a8e8811a4c2b569a8dc05e9bff1f79505cb8 body_fp=49d93bea4dcd0f3a85fb53672dcafcc0441183b9daab31dc84a13590e135ba34 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Tests that grep text-match fallback returns enclosing symbols when query appears in symbol bodies but not names.

- Verifies fallback.kind is "text_match" when name_contains query appears in source bodies
- Asserts fallback returns symbols containing the text with text_match_hits_in_body count
- Confirms returned matches include standard fields for agent hub-ranking
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_ranks_by_inbound_count_desc fingerprint=ef3ac182e9ce5a40ceecd0150cf8383538870bd63efa253d6c0217440cccaa12 body_fp=e1a58dd97421baa18d5db63c4f93541d0e0439fd321c9d91f0b1f9197e6e45b1 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Verifies that grep fallback text matches rank by inbound_count descending when multiple symbols contain the query string.

- Uses "title" query which appears in multiple symbols but isn't a symbol name
- Skips test if fixture changes create actual symbol name matches or insufficient candidates
- Asserts fallback matches are ordered by descending inbound reference count
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_caps_matches_and_notes_truncation fingerprint=ecfb2d89504fa8c1d8605600e0862e1c961e5ed2840d64902cb9fc4e173cb723 body_fp=5f111a862c0e689d58e33aaf4a3576e1b5d58f8614fa0dc6377eba332fe1d94d source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Tests that grep fallback truncates many matches and includes a note indicating partial results.

- Forces a tiny match cap (1) to exercise truncation behavior on the test fixture
- Verifies fallback returns exactly one match despite finding multiple symbols
- Asserts truncation note contains "of" to communicate partial results to the agent
- Confirms returned match includes standard fields like qname and inbound_count
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_omits_truncation_note_when_under_cap fingerprint=cf99e3b6a8f38acee3321f95f67be04eb837de301219103c85baec04b0a7bad0 body_fp=d6752e8cbb8a130e50ac81b925354846e361238409b2b868104445f8a76fc223 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Tests grep fallback omits truncation note when matches fit within the configured limit.

Verifies that when grep's text fallback finds matches that don't exceed `grep_fallback_match_limit`, no "showing top N of M" note is appended to the response. The agent sees the complete result set without truncation warnings.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_honours_scope_prefix fingerprint=31b191790a84b0b474a2cc9861f586ab8ea42430ceded08fcc62bdb2df882d24 body_fp=7feb4724e46d63f31c27a4ed8c48741ccecc2eae5be69c5ce5bb7c81a14d9d5f source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Verifies that TrieTools.grep fallback text search respects scope_prefix filters, excluding symbols outside the specified scope even when their source contains the query text.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_normal_hits_path_omits_fallback_key fingerprint=e4d4fa9ea51cf2db4cfeb5df2b356f09c2f3af9fb4af96059369c25e6b38f07d body_fp=8642769c24669fab980dbeffa0cda962a4c220a6fa6b7fdd58d495d2469957c0 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Verifies that `TrieTools.grep` omits the `fallback` key when returning hits to avoid unnecessary response tokens.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_returns_prose_and_neighbours fingerprint=8c1f77548638b430933ea0f0fab8a398b6ee3ac0f3dce12584d0dc79166d6f8e body_fp=aa6fca2f04a3e37437a2c3cdf8be3ab2b1c101e63364467cb0cc1c696208a869 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Test that `TrieTools.read` returns qname, prose content, and caller/callee neighborhoods.

- Verifies prose contains documentation text and neighbor lists are populated correctly
- Asserts callees is empty when symbol has no outbound references
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_source_pointer_shape fingerprint=420bf61a94fb75358593559620c310977d02c1bfeeb15481f3806550aeb73e97 body_fp=74bb12b9455d7d3b447e1400071f4d730ef84d046c54a33aba54bf967fe2bca8 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Verifies that TrieTools.read returns a source_pointer field formatted as "filename:start-end".
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_neighbour_carries_one_liner fingerprint=51c2f2f644f316fdeabf34c1c1d3b0dc3b57ec9e2f746d8c04d682b4cf8fd044 body_fp=c161eabf26c3028e464e6acb4d25fcb65cb5aa047de81ecfdada1d68d4d4407f source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Verifies that TrieTools.read includes one-liner summaries in caller/callee neighbour records.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_unknown_qname_returns_not_found fingerprint=3265a0090391b2d6756d124cacb28e9a01e3e19ee7b45fe0032c752b36efb7f7 body_fp=01130405e011a3b39e89b16ca167f5a676f3876dd2b434e6721dc5ac1c8411d1 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Tests that TrieTools.read returns a not_found error for nonexistent qualified names.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_fuzzy_suggestion_for_typo fingerprint=656607d4483ca9d33fd84a8e21cd913fd53f6dfb9c395347ff19d836dabaa261 body_fp=d9bb4cc04e58dea01cf815b187c09b747a3670046fb5b8d5d447076c61755da9 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Verifies that `TrieTools.read` provides a helpful suggestion when given a typo in the qname.

- Uses "lib:slugfy" as a deliberate typo of "lib:slugify"
- Expects either direct qname suggestion or guidance to use `grep()`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_callers_returns_topology fingerprint=ba52df6ec0918227c8a41b6a0d14ab17f8fca12de24f0684dd8eb190b5e31c9d body_fp=96b227fa86194df5c7c5edc3c1a7bc7e9278d99399a6f07fb669835541a065eb source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Verifies that TrieTools.trace returns caller topology with root qname, nodes dict containing callers, and directed edges from callers to root symbol.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_callees_returns_outbound fingerprint=0f7a79554ab1ccc241fd5da78d98609b43458bbc13f8ab26ace19fde87547dde body_fp=06b23e58c46c4b81978b304d2a6fce4672166539c4812b058fbf461c039d75c4 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Tests that `TrieTools.trace` with `direction="callees"` returns outbound edges from a symbol to its dependencies.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_both_directions fingerprint=d982c36f43d513419ade4e39cc8a34a1405626cf97bdb9cf3043e5dc8e96bab0 body_fp=563cf907e90d1ea2b1dd115f52e9480f65aaef621804e424c263b29ee5660cc1 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Verifies TrieTools.trace with direction="both" includes callers and marks edge directions correctly.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_invalid_direction_returns_error fingerprint=ee66239794f468126ebd3f5e9d557088e75a14791456cb94d3242b919f9a1712 body_fp=221012ceabcd6b78a015ba3c7cec2362fe68d462675e8872edda0b6f744f9cd1 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Asserts that TrieTools.trace rejects invalid direction values with `invalid_argument` error code.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_unknown_qname_returns_not_found fingerprint=4a972421a152c7b560db28c9f942d12a1917d194cc1acb5041774f2b39f1b89d body_fp=5556804909d8983046712bc0031dcf3380338e322cbb02e4fef171567276aaf6 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Test that TrieTools.trace returns `not_found` error for a non-existent qname.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_depth_zero_returns_only_root fingerprint=76be5ecaba8cb2a295a796f304e77c718a9dcc8d23868995efa57a5182d2a1c2 body_fp=8a19f9df92f68756777595f2fefefd6d54514bedd7f51ec843223cda4c8363e1 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Verifies trace() returns only the root symbol when depth is zero, with empty edges list.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_depth_clamp_adds_note fingerprint=c455960b8dcfb8693c4e826945685a9217238b8705ee7806c1ca182dccf62c13 body_fp=1761ac64281d12dc5e62ad4e9507097a2c765460055af5c264df182099098ea2 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Tests that TrieTools.trace adds a note when depth exceeds trace_max_depth configuration.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_build_server_registers_three_verbs fingerprint=6b9681c689a428da5e4f2498ee941fd5a83453ab2b5fb8299f484f077f69d5a3 body_fp=881215c889ecd41271b5ee83b004fe40b8a8e1612a31450148ebe93dd534f1bc source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Verifies that `build_server` registers the core MCP tools (`grep`, `read`, `trace`) plus the extended toolset (8 additional tools) with matching wire names.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_build_server_wire_names_bind_to_internal_methods fingerprint=a480374391cd52c59bd6c51db2664d53e9150773ce64b5a08555c94f8cf832c5 body_fp=bf5cee3a9b499fb766e1b4d2c61e59bb49ba0a885a0d2e2c366cf8fee86533d8 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Verifies MCP tool wire names dispatch to matching TrieTools methods to prevent silent behaviour swaps.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:dual_rank_project fingerprint=ddb09bc1e817a930bec9a532e1c272d2dfef3a3e605bc48f4679ba42ed216ee6 body_fp=4db26fd017a10427abce271fbc0882698693afe59afa2e6a72516dfa82a9a95c source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Creates a test project with two auth-related symbols having different inbound reference counts.

- `hub_authenticate` — receives 3 inbound references from separate files (hub symbol)
- `auth_check` — receives 2 inbound references from separate files (niche symbol)
- Both symbols match "auth" queries equally on text relevance
- Used to test ranking behavior where niche symbols rank before hubs at equal scores
- Project includes scanned symbols and synced documentation for complete test coverage
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_entry_points_niche_ranks_before_hub fingerprint=a5bf02d8993e8282336d29b02cec7ebb34624737bcbad9c62cbda7acad54290e body_fp=07244a835752fed0e1e370755ed08328f125ff9df608530ed6d0b0a8f7632ff9 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Tests that TrieTools.grep_entry_points ranks niche symbols before hubs when scores are equal.

- Uses `dual_rank_project` fixture with auth_check (2 inbounds) and hub_authenticate (3 inbounds)
- Verifies both symbols appear in results for "auth" query
- Asserts auth_check ranks higher than hub_authenticate due to lower inbound count
- Sort key is (score DESC, inbound_count ASC)
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_entry_points_hits_carry_score fingerprint=bf76df08b996d67ba20379770a38f838d8fe1c762948d49445555df41368cc37 body_fp=025eb6fde75c1ca362253dbb086e19af383fe994e77bac0bba4feaf5d90f7e5a source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Verify that every hit from TrieTools.grep_entry_points includes a positive numeric score field.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_symbol_typo_tolerance fingerprint=998a77d9bbc63dc7fa9771cbe44d66c7262382670d46446093a4c0102cb98e51 body_fp=b805007a8ef0fd66ee07fb0d43b37674b188a972ebdc696623ae5d4d49b7d742 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Verifies that TrieTools.grep_symbol resolves single-character typos using fuzzy matching.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_symbol_returns_score_field fingerprint=d875689a783594250d150f3a147a935eeeb38aeb1fadede0bc7712cc65914a22 body_fp=e4fe63fc6d00dda6a748695850fbb56aef67dd4e2100176fbe430762b9d2be67 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Verifies that `TrieTools.grep_symbol` returns symbols with numeric score fields in both match and similar results.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fuzzy_prose_fallback fingerprint=0bdb61dcf7c038d93f1a7a4598b1a770d003ba2609b446451546db3192d4dd4e body_fp=dd23f77da76fd31d4a4ccd5dbc86b599528e26311c797d57c1668d1ef4409e50 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Tests fuzzy prose fallback when name_contains finds no direct symbol name matches.

- Verifies `grep` with phrase "lowercase dash separate" triggers fallback since no symbol has that name
- Asserts fallback kind is either "text_match" or "fuzzy_prose" 
- For fuzzy_prose fallback, validates it returns matches and finds "slugify" symbol whose triefact body contains the concept
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_str_fuzzy_fallback fingerprint=67380bf7bf45fed97698909288b028bd324ec109f63ba4924f1ec5a14d9de327 body_fp=e593e9a60a6f76f5b6f844b90339b0a9cb2e7cd9dc5e763f71ab0a56bb2a10fc source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
Tests that `TrieTools.grep_str` returns fuzzy fallback when regex pattern finds no matches.

- Verifies empty hits list when pattern has no literal source matches
- Confirms presence of hits key in response structure regardless of match results
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_str_fuzzy_fallback_finds_close_name fingerprint=0dc0ff2f1a636680859fd46f2db38dac736a30e6bc5ada90d65313099d97ec0b body_fp=9818be19f15a4780a888b7031e360e1e6431f8bf1d3223473d6ae3e4fa7f8937 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab -->
## test_grep_str_fuzzy_fallback_finds_close_name

Tests that `grep_str` returns fuzzy fallback when regex search fails but close symbol name exists.

- Uses "slugufy" typo to verify fuzzy matching surfaces "slugify" symbol
- Expects `fallback.kind == "fuzzy_one_liner"` when regex finds no literal matches
- Skips assertion if regex accidentally matches something in source
<!-- trie:end -->