---
trie_version: 0.3.0
source: tests/test_mcp.py
file_fingerprint: 5447bd92f06cadcac330100492c33f1afe405bc083502fe89dd1cd73c1425448
last_synced_at: '2026-08-01T02:17:30Z'
description: 'Tests for the MCP tool surface: `grep`, `read`, `trace`.'
defines:
- kind: module
  qualified_name: tests/test_mcp:__module__
  lines: 1-1181
- kind: constant
  qualified_name: tests/test_mcp:PROJECT_TOML
  lines: 21-30
- kind: function
  qualified_name: tests/test_mcp:project
  lines: 34-50
  signature: 'def project(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_mcp:populated_project
  lines: 54-79
  signature: 'def populated_project(project: Path) -> Path'
- kind: function
  qualified_name: tests/test_mcp:tools
  lines: 83-86
  signature: 'def tools(populated_project: Path)'
- kind: function
  qualified_name: tests/test_mcp:test_trie_tools_init_fails_clearly_when_rg_missing
  lines: 92-113
  signature: 'def test_trie_tools_init_fails_clearly_when_rg_missing( populated_project: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_mcp:test_grep_name_contains_returns_matches
  lines: 119-124
  signature: 'def test_grep_name_contains_returns_matches(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_returns_one_liner_from_section_body
  lines: 127-133
  signature: 'def test_grep_returns_one_liner_from_section_body(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_returns_file_pointer
  lines: 136-138
  signature: 'def test_grep_returns_file_pointer(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_kind_filter
  lines: 141-147
  signature: "def test_grep_kind_filter(tools: TrieTools): # Both fixtures define only functions; class filter should return zero hits. # The fallback will fire because `name_contains` is present \u2014 the text # search finds `slug` in source bodies. That's the new contract; we # assert on hits being empty rather than the whole result."
- kind: function
  qualified_name: tests/test_mcp:test_grep_invalid_kind_returns_error
  lines: 150-153
  signature: 'def test_grep_invalid_kind_returns_error(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_accepts_constant_and_module_kinds
  lines: 156-168
  signature: 'def test_grep_accepts_constant_and_module_kinds(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_scope_prefix_filter
  lines: 171-174
  signature: 'def test_grep_scope_prefix_filter(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_scope_exclude_filter
  lines: 177-180
  signature: 'def test_grep_scope_exclude_filter(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_inbound_count_predicate
  lines: 183-188
  signature: 'def test_grep_inbound_count_predicate(tools: TrieTools): # slugify has one inbound edge from make_url.'
- kind: function
  qualified_name: tests/test_mcp:test_grep_rank_by_inbound_count
  lines: 191-198
  signature: "def test_grep_rank_by_inbound_count(tools: TrieTools): # `public_only: true` is the documented orientation query \u2014 every public # symbol in scope, ranked by centrality. Using a real filter here also # avoids the empty-predicate rejection path that `grep` enforces."
- kind: function
  qualified_name: tests/test_mcp:test_grep_limit_respected
  lines: 201-205
  signature: 'def test_grep_limit_respected(tools: TrieTools): # Same trick: a non-empty predicate keeps us out of the empty-predicate # rejection path while still exercising the `limit` clamp.'
- kind: function
  qualified_name: tests/test_mcp:test_grep_empty_predicate_returns_invalid_argument
  lines: 208-222
  signature: 'def test_grep_empty_predicate_returns_invalid_argument(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_empty_predicate_rejected_regardless_of_rank_by
  lines: 225-231
  signature: 'def test_grep_empty_predicate_rejected_regardless_of_rank_by(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_unknown_predicate_field_silently_ignored
  lines: 234-237
  signature: "def test_grep_unknown_predicate_field_silently_ignored(tools: TrieTools): # Extra fields don't break the call \u2014 we just ignore them."
- kind: function
  qualified_name: tests/test_mcp:test_grep_invalid_predicate_returns_error
  lines: 240-243
  signature: 'def test_grep_invalid_predicate_returns_error(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_fallback_kind_none_when_no_name_contains
  lines: 249-258
  signature: 'def test_grep_fallback_kind_none_when_no_name_contains(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_fallback_kind_text_match_empty_for_unseen_string
  lines: 261-268
  signature: 'def test_grep_fallback_kind_text_match_empty_for_unseen_string(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_fallback_kind_text_match_redirects_via_body_match
  lines: 271-289
  signature: 'def test_grep_fallback_kind_text_match_redirects_via_body_match(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_fallback_ranks_by_inbound_count_desc
  lines: 292-306
  signature: 'def test_grep_fallback_ranks_by_inbound_count_desc(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_fallback_caps_matches_and_notes_truncation
  lines: 309-335
  signature: 'def test_grep_fallback_caps_matches_and_notes_truncation( tools: TrieTools, )'
- kind: function
  qualified_name: tests/test_mcp:test_grep_fallback_capped_by_request_limit
  lines: 338-343
  signature: 'def test_grep_fallback_capped_by_request_limit(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_partial_name_hits_fill_up_with_related
  lines: 346-361
  signature: 'def test_grep_partial_name_hits_fill_up_with_related(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_full_hits_skip_related_fill_up
  lines: 364-368
  signature: 'def test_grep_full_hits_skip_related_fill_up(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_fallback_omits_truncation_note_when_under_cap
  lines: 371-379
  signature: 'def test_grep_fallback_omits_truncation_note_when_under_cap(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_fallback_honours_scope_prefix
  lines: 382-397
  signature: 'def test_grep_fallback_honours_scope_prefix(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_normal_hits_path_omits_fallback_key
  lines: 400-406
  signature: 'def test_grep_normal_hits_path_omits_fallback_key(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_read_returns_prose_and_neighbours
  lines: 412-419
  signature: 'def test_read_returns_prose_and_neighbours(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_read_source_pointer_shape
  lines: 422-425
  signature: 'def test_read_source_pointer_shape(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_read_neighbour_carries_one_liner
  lines: 428-431
  signature: 'def test_read_neighbour_carries_one_liner(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_read_unknown_qname_returns_not_found
  lines: 434-437
  signature: 'def test_read_unknown_qname_returns_not_found(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_read_fuzzy_suggestion_for_typo
  lines: 440-446
  signature: 'def test_read_fuzzy_suggestion_for_typo(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_read_file_path_returns_compact_triefact_view
  lines: 452-462
  signature: 'def test_read_file_path_returns_compact_triefact_view(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_read_file_path_full_returns_prose_without_sentinels
  lines: 465-472
  signature: 'def test_read_file_path_full_returns_prose_without_sentinels(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_read_file_path_show_source_returns_numbered_source
  lines: 475-479
  signature: 'def test_read_file_path_show_source_returns_numbered_source(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_read_file_path_offset_limit_implies_source
  lines: 482-487
  signature: 'def test_read_file_path_offset_limit_implies_source(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_read_non_indexed_file_falls_back_to_source
  lines: 490-494
  signature: 'def test_read_non_indexed_file_falls_back_to_source(tools: TrieTools, populated_project: Path)'
- kind: function
  qualified_name: tests/test_mcp:test_read_file_with_line_suffix_reads_source_window
  lines: 497-501
  signature: 'def test_read_file_with_line_suffix_reads_source_window(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_trace_callers_returns_topology
  lines: 507-513
  signature: 'def test_trace_callers_returns_topology(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_trace_callees_returns_outbound
  lines: 516-519
  signature: 'def test_trace_callees_returns_outbound(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_trace_both_directions
  lines: 522-527
  signature: 'def test_trace_both_directions(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_trace_invalid_direction_returns_error
  lines: 530-533
  signature: 'def test_trace_invalid_direction_returns_error(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_trace_unknown_qname_returns_not_found
  lines: 536-539
  signature: 'def test_trace_unknown_qname_returns_not_found(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_trace_depth_zero_returns_only_root
  lines: 542-545
  signature: 'def test_trace_depth_zero_returns_only_root(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_trace_depth_clamp_adds_note
  lines: 548-552
  signature: 'def test_trace_depth_clamp_adds_note(tools: TrieTools): # trace_max_depth defaults to 5; ask for more and expect a note.'
- kind: function
  qualified_name: tests/test_mcp:test_build_server_registers_three_verbs
  lines: 558-581
  signature: 'def test_build_server_registers_three_verbs(populated_project: Path)'
- kind: function
  qualified_name: tests/test_mcp:test_build_server_wire_names_bind_to_internal_methods
  lines: 584-606
  signature: 'def test_build_server_wire_names_bind_to_internal_methods(populated_project: Path)'
- kind: function
  qualified_name: tests/test_mcp:dual_rank_project
  lines: 615-672
  signature: 'def dual_rank_project(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_mcp:test_grep_entry_points_niche_ranks_before_hub
  lines: 675-698
  signature: 'def test_grep_entry_points_niche_ranks_before_hub(dual_rank_project: Path)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_entry_points_hits_carry_score
  lines: 701-713
  signature: 'def test_grep_entry_points_hits_carry_score(dual_rank_project: Path)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_symbol_typo_tolerance
  lines: 716-722
  signature: 'def test_grep_symbol_typo_tolerance(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_symbol_returns_score_field
  lines: 725-733
  signature: 'def test_grep_symbol_returns_score_field(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_fuzzy_prose_fallback
  lines: 736-751
  signature: 'def test_grep_fuzzy_prose_fallback(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_str_fuzzy_fallback
  lines: 754-764
  signature: 'def test_grep_str_fuzzy_fallback(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_str_fuzzy_fallback_finds_close_name
  lines: 767-783
  signature: 'def test_grep_str_fuzzy_fallback_finds_close_name(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_str_all_finds_non_indexed_file
  lines: 789-795
  signature: 'def test_grep_str_all_finds_non_indexed_file(tools: TrieTools, populated_project: Path)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_str_all_attributes_indexed_hits_to_symbols
  lines: 798-802
  signature: 'def test_grep_str_all_attributes_indexed_hits_to_symbols(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_str_default_does_not_see_non_indexed
  lines: 805-810
  signature: 'def test_grep_str_default_does_not_see_non_indexed(tools: TrieTools, populated_project: Path)'
- kind: function
  qualified_name: tests/test_mcp:test_find_files_by_extension
  lines: 813-817
  signature: 'def test_find_files_by_extension(tools: TrieTools, populated_project: Path)'
- kind: function
  qualified_name: tests/test_mcp:test_find_files_by_bare_name
  lines: 820-823
  signature: 'def test_find_files_by_bare_name(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_find_files_indexed_only
  lines: 826-830
  signature: 'def test_find_files_indexed_only(tools: TrieTools, populated_project: Path)'
- kind: function
  qualified_name: tests/test_mcp:test_find_files_prunes_trie_dir
  lines: 833-836
  signature: 'def test_find_files_prunes_trie_dir(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_read_source_non_indexed_file
  lines: 839-844
  signature: 'def test_read_source_non_indexed_file(tools: TrieTools, populated_project: Path)'
- kind: function
  qualified_name: tests/test_mcp:test_read_source_offset_limit
  lines: 847-852
  signature: 'def test_read_source_offset_limit(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_read_source_missing_file_errors
  lines: 855-859
  signature: 'def test_read_source_missing_file_errors(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_read_source_directory_errors
  lines: 862-866
  signature: 'def test_read_source_directory_errors(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_blast_radius_reports_cascade
  lines: 869-875
  signature: 'def test_blast_radius_reports_cascade(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_blast_radius_unknown_symbol_errors
  lines: 878-882
  signature: 'def test_blast_radius_unknown_symbol_errors(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_write_file_creates_new_file
  lines: 885-891
  signature: 'def test_write_file_creates_new_file(tools: TrieTools, populated_project: Path)'
- kind: function
  qualified_name: tests/test_mcp:test_write_file_refuses_clobber_without_overwrite
  lines: 894-899
  signature: 'def test_write_file_refuses_clobber_without_overwrite(tools: TrieTools, populated_project: Path)'
- kind: function
  qualified_name: tests/test_mcp:test_write_file_overwrite_flag
  lines: 902-907
  signature: 'def test_write_file_overwrite_flag(tools: TrieTools, populated_project: Path)'
- kind: function
  qualified_name: tests/test_mcp:test_write_file_indexed_path_flags_needs_sync
  lines: 910-914
  signature: 'def test_write_file_indexed_path_flags_needs_sync(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_write_file_outside_root_errors
  lines: 917-921
  signature: 'def test_write_file_outside_root_errors(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_batch_patch_stages_mixed_items
  lines: 924-938
  signature: 'def test_batch_patch_stages_mixed_items(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_batch_patch_reports_bad_items_without_aborting
  lines: 941-955
  signature: 'def test_batch_patch_reports_bad_items_without_aborting(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_batch_patch_empty_list_errors
  lines: 958-961
  signature: 'def test_batch_patch_empty_list_errors(tools: TrieTools)'
- kind: function
  qualified_name: tests/test_mcp:test_read_warns_when_prose_is_stale
  lines: 967-1002
  signature: 'def test_read_warns_when_prose_is_stale(populated_project: Path)'
- kind: function
  qualified_name: tests/test_mcp:test_read_warns_when_graph_itself_is_stale
  lines: 1005-1019
  signature: 'def test_read_warns_when_graph_itself_is_stale(populated_project: Path)'
- kind: function
  qualified_name: tests/test_mcp:test_read_has_no_stale_warning_when_fresh
  lines: 1022-1031
  signature: 'def test_read_has_no_stale_warning_when_fresh(populated_project: Path)'
- kind: function
  qualified_name: tests/test_mcp:test_read_history_flag_surfaces_intent_trail
  lines: 1034-1063
  signature: 'def test_read_history_flag_surfaces_intent_trail(populated_project: Path)'
- kind: function
  qualified_name: tests/test_mcp:test_fuzzy_score_is_graded_not_binary
  lines: 1069-1083
  signature: def test_fuzzy_score_is_graded_not_binary()
- kind: function
  qualified_name: tests/test_mcp:project_with_tests
  lines: 1087-1109
  signature: 'def project_with_tests(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_mcp:test_grep_symbol_prefers_production_over_test_twin
  lines: 1112-1124
  signature: 'def test_grep_symbol_prefers_production_over_test_twin(project_with_tests: Path)'
- kind: function
  qualified_name: tests/test_mcp:test_trace_flow_fragment_resolves_to_production_symbol
  lines: 1127-1133
  signature: 'def test_trace_flow_fragment_resolves_to_production_symbol(project_with_tests: Path)'
- kind: function
  qualified_name: tests/test_mcp:test_grep_entry_points_excludes_test_symbols
  lines: 1136-1146
  signature: 'def test_grep_entry_points_excludes_test_symbols(project_with_tests: Path)'
- kind: function
  qualified_name: tests/test_mcp:test_mcp_wire_query_tools_return_text
  lines: 1152-1180
  signature: 'def test_mcp_wire_query_tools_return_text(populated_project: Path)'
incoming_refs: 0
outgoing_refs: 129
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
<!-- trie:section symbol=tests/test_mcp:project fingerprint=3e4b4f7d19d96699d52f90f1396ef4a3c695e286383233613202fea1c0b09b6b body_fp=f540e7b6050a0c450f386f40bab8c9916351d87baac08e07f24533ffb160c2b2 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
## `def project(tmp_path: Path) -> Path`

Creates a minimal test project with trie.toml config and two Python files.

- `lib.py`: Contains `slugify` (lowercase + dash-separate) and `capitalize` functions
- `app.py`: Contains `make_url` function that imports and uses `slugify`
- Returns the temporary directory path containing the project structure
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:populated_project fingerprint=a54e186816ee0ef181cf7cc6e7058686a0354458a8b46b1d8f711321355a76b5 body_fp=2380c40fbda7ded16f7368802ac9f532e5d1ab8810cc9e648feb7b17fe2dd289 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
## `def populated_project(project: Path) -> Path`

Creates a test project fixture with scanned symbols and generated triefacts for MCP tool testing.

- Scans the project to populate the graph database with symbol relationships
- Syncs `lib.py` and `app.py` using FakeTrieClient to generate documentation
- Returns the project path with `.trie/graph.db` containing queryable data
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:tools fingerprint=b89f3ca1611ed5226f820d82ffc6f4d3db27942f64390976744c1fbf0d5e67de body_fp=075c90ff2942f3d334598e5e8e20971406e93f8d7398271e7eb42d35f08abde3 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def tools(populated_project: Path)`

Creates a TrieTools fixture for the populated test project and ensures cleanup after use.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trie_tools_init_fails_clearly_when_rg_missing fingerprint=2ea97d1b02ea695fbca32b81cfd8377a7e1da3159c9b30a1815fe2099d25638b body_fp=d5b8f92ba92f5a052f6cd93c3f9fcce004263dd56d7160ff5933ef8ad91d83d8 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_trie_tools_init_fails_clearly_when_rg_missing( populated_project: Path, monkeypatch: pytest.MonkeyPatch )`

Tests that TrieTools initialization fails with clear error message when ripgrep binary is missing.

- Simulates missing `rg` by stubbing `shutil.which` to return `None`
- Verifies `RipgrepNotFoundError` is raised with helpful installation guidance
- Ensures error message names the missing binary and provides recovery path
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_name_contains_returns_matches fingerprint=13a70b013b95687914be7cf11a6a2926e39e6d256ed6ee0fc19ec38c6f2bcffb body_fp=38c0c42fdfabd805e35281cd8347b09eed9210cfcdd911d0b873cbf050b4f8f5 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
## `def test_grep_name_contains_returns_matches(tools: TrieTools)`

Verifies grep returns symbols with names containing the query string and omits fallback data when matches exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_returns_one_liner_from_section_body fingerprint=37a68231e58a6658814f1e064b7c136eeaa7a7f879f70bdfd4eaa836d69779ad body_fp=730672a7dde5ee230ae7bed36c541c6efa2d7bdf2f5972a37fc73b4b4827cf5e source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
## `def test_grep_returns_one_liner_from_section_body(tools: TrieTools)`

Verifies that TrieTools.grep extracts truncated one-liner summaries from triefact bodies.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_returns_file_pointer fingerprint=fd44c10f827063015b2af6e12727ce6f8e2d67973fc32ea706be0a403274f87e body_fp=acca3e5181af3bbb0639eeddceb1f85b0e4a3a4c85864e15a0928ae3f8e6268a source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
## `def test_grep_returns_file_pointer(tools: TrieTools)`

Verifies grep returns file_pointer with filename:line format for symbol locations.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_kind_filter fingerprint=05f736a15cd7708beed46d7beef0835ba93bb4867f848cec7c0d4da66a5d31bf body_fp=586ac048c08d4a62f2f4ef08ed1623b89e76e12626027d3d60c1a6056786d8ea source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
## `def test_grep_kind_filter(tools: TrieTools): # Both fixtures define only functions; class filter should return zero hits. # The fallback will fire because `name_contains` is present — the text # search finds `slug` in source bodies. That's the new contract; we # assert on hits being empty rather than the whole result.`

Tests that grep's kind filter correctly excludes symbols not matching the specified type.

- Uses `kind: "class"` filter with fixtures containing only functions, expecting empty hits
- Verifies fallback still triggers when `name_contains` is present but no symbols match the kind
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_invalid_kind_returns_error fingerprint=93c63e643ced72ef46d974b15a6f15362abaa72e8e7b439e17f8d46411602d2e body_fp=75153a3b731ba1a95523bd419b4aa6a92a02203b0f4469be912f42507b59a733 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
## `def test_grep_invalid_kind_returns_error(tools: TrieTools)`

Test that `TrieTools.grep` rejects invalid `kind` filter values with `invalid_argument` error code.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_accepts_constant_and_module_kinds fingerprint=a7b0b5f6a91e85c5d7b2effde7c148be97b61ecfd7966d405518b3d26526bbed body_fp=cf564de2a447413c22470e9bc763d8ff5908d57e7e0ff4e2f84d058fc80926e4 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
## `def test_grep_accepts_constant_and_module_kinds(tools: TrieTools)`

Verifies that `TrieTools.grep` accepts `"constant"` and `"module"` as valid `kind` filter values without raising an `invalid_argument` error.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_scope_prefix_filter fingerprint=4087ec669cf402755c9ebcba58be379db4f126a23aaa314712e20b33ffa6a9f0 body_fp=ea127f8d12bfb9e27e69d45ccea21a97e2b1b30437d5a4a5c5d9d2af2fd6dccf source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
## `def test_grep_scope_prefix_filter(tools: TrieTools)`

Verify TrieTools.grep filters results to symbols whose file paths start with the given scope prefix.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_scope_exclude_filter fingerprint=d9ed58e0d2cb505d72e32ca79f8f8032c881eff47584a5bf9377a006626e5793 body_fp=a0f2034dd07f1f653fbd6220b3bbfd1e3e383a287f7a05c4bc7a88f446389bde source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
## `def test_grep_scope_exclude_filter(tools: TrieTools)`

Verify that `TrieTools.grep` excludes symbols from specified scopes via `scope_exclude` predicate.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_inbound_count_predicate fingerprint=29ed9feb09b2e5254bd1cef76cabd75536142afaac8b064dcc196599c69f7b0b body_fp=4cf9deb0661714d4cdc8a6cfac58b8c6cb5458401a844a47d23ba9fa4fea40b4 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
## `def test_grep_inbound_count_predicate(tools: TrieTools): # slugify has one inbound edge from make_url.`

Verify that `tools.grep` with `inbound_count` filter returns symbols with at least the specified minimum incoming references.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_rank_by_inbound_count fingerprint=956741b97e66e5508ccc0365fd3a6a04e6e7c6f3cb7da4770fc673b73a03477e body_fp=404619aa2d49386479a4e740408076a2b718ed6e533168bcaf2702fb79871a8d source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
## `def test_grep_rank_by_inbound_count(tools: TrieTools): # `public_only: true` is the documented orientation query — every public # symbol in scope, ranked by centrality. Using a real filter here also # avoids the empty-predicate rejection path that `grep` enforces.`

Verifies that `TrieTools.grep` results are correctly ranked by inbound_count when `rank_by="inbound_count"` is specified.

- Uses `public_only: True` predicate to avoid empty-predicate rejection
- Asserts first hit has highest `inbound_count` value among returned results
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_limit_respected fingerprint=80407aa581af3497200f623a81e718ea1e94ee91389ac126830562e3b69348af body_fp=9cf9f3893916a967752b898c4e4cdfac623b99ad9f79c8c7b78940ee1dfa56df source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
## `def test_grep_limit_respected(tools: TrieTools): # Same trick: a non-empty predicate keeps us out of the empty-predicate # rejection path while still exercising the `limit` clamp.`

Verifies TrieTools.grep respects the limit parameter by requesting only 1 result and asserting exactly 1 hit is returned.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_empty_predicate_returns_invalid_argument fingerprint=b276ee91748c22279c9a40988da4c4daaebfea8382927b5fe18d9f2f3c5b17ce body_fp=fc6f8638533a917fc7789b911da32199539def6580c2a2031fdd9dec2cf15cda source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
## `def test_grep_empty_predicate_returns_invalid_argument(tools: TrieTools)`

Tests that TrieTools.grep rejects empty predicates with invalid_argument error and helpful suggestion.

- Validates rejection for None, {}, {"name_contains": ""}, {"kind": "any"}
- Requires error.code == "invalid_argument" 
- Requires suggestion mentioning "name_contains" or "scope_prefix"
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_empty_predicate_rejected_regardless_of_rank_by fingerprint=173c7d0e853ec0b26f7e6b2344e5c2c4c42c2b1245b1081fca21ec158813dd8d body_fp=0a58200ea81e6e6cbb3e2dfb78c8151e4363472b2c3a01a8139d1c17a0b53584 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
## `def test_grep_empty_predicate_rejected_regardless_of_rank_by(tools: TrieTools)`

Verifies that TrieTools.grep rejects empty predicates even when rank_by and limit are specified.

- Tests rejection occurs before ranking is consulted
- Expects error.code of "invalid_argument"
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_unknown_predicate_field_silently_ignored fingerprint=d932c0e53093906441747dbaef79cf5c314d42057b100dc5b2f257cc7518c2f0 body_fp=c6d7c6d9eed1c5e88a44e80397f2b41537b89026b72f444ec548e7b8274698dd source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
## `def test_grep_unknown_predicate_field_silently_ignored(tools: TrieTools): # Extra fields don't break the call — we just ignore them.`

Verifies that TrieTools.grep ignores unknown predicate fields without raising errors.

- Uses predicate with valid `name_contains` and invalid `totally_made_up_field`
- Confirms grep still returns hits despite the unknown field
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_invalid_predicate_returns_error fingerprint=a7cc46c17ae0d8aa0cd7f2ea984b0423139fb7ac60d05209e81e0ff92529668d body_fp=7f1f65cdffba166eb76edc1a5fa0ec28750f00d5ee01bec8036897078b79eebb source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
## `def test_grep_invalid_predicate_returns_error(tools: TrieTools)`

Verifies grep rejects non-dictionary predicates with invalid_argument error code.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_kind_none_when_no_name_contains fingerprint=4e6e6519556d6b7fd8d18bba3fffc5f082582756e2362308de5d5c28e746be5e body_fp=919dba084d442273b3b5a8497d757684a8ab1839e3772a435fdb47eccfb281d1 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
## `def test_grep_fallback_kind_none_when_no_name_contains(tools: TrieTools)`

Test that grep returns a fallback envelope with kind "none" when a predicate without name_contains yields no matches.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_kind_text_match_empty_for_unseen_string fingerprint=69f80642424418ade7fb9f362dc9f273b6a72bb84ecb843ccc644431f6056736 body_fp=a9e958ba8d0d0bb7c0887c22709361267bd8a58bc228f62ea4ea65f8f3f44cc6 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
## `def test_grep_fallback_kind_text_match_empty_for_unseen_string(tools: TrieTools)`

Tests TrieTools.grep fallback behavior when name_contains query matches no source text.

- Verifies fallback reports `text_match_empty` kind for non-existent strings
- Confirms query string is preserved in fallback response
- Ensures empty hits list signals clear "doesn't exist" rather than ambiguous result
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_kind_text_match_redirects_via_body_match fingerprint=d62ca25bade3109437990a6051d0a8e8811a4c2b569a8dc05e9bff1f79505cb8 body_fp=edc5244321effa6081babf3b1530fa11c3a387acfe7d38e42646109992f75d3e source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
## `def test_grep_fallback_kind_text_match_redirects_via_body_match(tools: TrieTools)`

Tests TrieTools.grep fallback text matching when query appears in symbol bodies but not names.

- Uses "replace" which appears in lib:slugify's body but is not a symbol name
- Verifies fallback returns text_match kind with enclosing symbols as matches
- Confirms matches include text_match_hits_in_body count and standard hit fields
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_ranks_by_inbound_count_desc fingerprint=ef3ac182e9ce5a40ceecd0150cf8383538870bd63efa253d6c0217440cccaa12 body_fp=59c1cc049b6139f3e1ab88587e17d341e27dbd3ed4c297c4b755d965b007d8fd source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
## `def test_grep_fallback_ranks_by_inbound_count_desc(tools: TrieTools)`

Verifies that grep's fallback text-match results rank by descending inbound_count.

- Queries for "title" which appears in source but not as symbol name
- Confirms fallback ordering prioritizes hub symbols before leaf symbols
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_caps_matches_and_notes_truncation fingerprint=ecfb2d89504fa8c1d8605600e0862e1c961e5ed2840d64902cb9fc4e173cb723 body_fp=5a433fb58d4c65fcd571dd7765aff6fc5978e83fec7ccf30c43878e591b5d755 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
## `def test_grep_fallback_caps_matches_and_notes_truncation( tools: TrieTools, )`

Tests that grep's fallback mechanism caps excessive matches and includes truncation notes.

- Forces a tiny match limit to exercise truncation on the small test fixture
- Verifies fallback returns exactly one match when capped at 1 
- Checks that `unique_symbols` indicates more candidates were found
- Ensures truncation note contains "of" to communicate incomplete results
- Confirms returned matches still carry standard fields like `qname` and `inbound_count`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_capped_by_request_limit fingerprint=591fab6b93894c7bcc93cf5d54e917e23d6971b7c50985b22c8c2e6036835dbf body_fp=688872e4f76e79c09925957fd12d2434f0938e0c3d4f3f3731a5b712b7cd3f1b source_ref=b16efa20b80176ac81a14f6db9840483ac4ba76c role=test -->
## `def test_grep_fallback_capped_by_request_limit(tools: TrieTools)`

Assert that `TrieTools.grep` fallback `matches` list is capped to the request's `limit`, not the config-level match cap.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_partial_name_hits_fill_up_with_related fingerprint=56b57e03bcb00e4f5ea110176ed32b1626be41a87df754c5ff3543dce5222f4b body_fp=dbac3b99e853471e7fd66ed9889234ade75197276e178e77ebfbed067094638b source_ref=b16efa20b80176ac81a14f6db9840483ac4ba76c role=test -->
## `def test_grep_partial_name_hits_fill_up_with_related(tools: TrieTools)`

Verify that partial name hits fill the remaining `limit` budget with `related` body-match candidates that exclude qnames already in `hits`.

- `related_kind` must equal `"text_match"` when fill-up runs.
- Combined `hits` + `related` count must not exceed `limit`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_full_hits_skip_related_fill_up fingerprint=9be62a2b4e4134d3b8f13fded1d11b986871900df64cafb9c88924a8c87d0a27 body_fp=7d80d76295f44c39f7778f17180ee2157c46b7e55b940c159dad01bb1bed45a8 source_ref=b16efa20b80176ac81a14f6db9840483ac4ba76c role=test -->
## `def test_grep_full_hits_skip_related_fill_up(tools: TrieTools)`

Assert that `TrieTools.grep` omits the `related` key when name hits already saturate the requested `limit`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_omits_truncation_note_when_under_cap fingerprint=cf99e3b6a8f38acee3321f95f67be04eb837de301219103c85baec04b0a7bad0 body_fp=b52086964725c62323ba8c3c30d1912242dd2f209bfab5090ddb4b85bad6dd00 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
## `def test_grep_fallback_omits_truncation_note_when_under_cap(tools: TrieTools)`

Tests that grep fallback omits truncation warnings when match count stays within limit.

- Searches for "replace" which appears in source but isn't a symbol name
- Verifies fallback response excludes "showing top" language when results fit within cap
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_honours_scope_prefix fingerprint=31b191790a84b0b474a2cc9861f586ab8ea42430ceded08fcc62bdb2df882d24 body_fp=31b897f12d182fb04d2144c47bfe8451010d6255b2d31463608fe6ebe6abf007 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
## `def test_grep_fallback_honours_scope_prefix(tools: TrieTools)`

Verify that TrieTools.grep respects scope_prefix filter when falling back to text search for non-matching symbol names.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_normal_hits_path_omits_fallback_key fingerprint=e4d4fa9ea51cf2db4cfeb5df2b356f09c2f3af9fb4af96059369c25e6b38f07d body_fp=1667f10bff24dbf4124686bf82069b5225384ca5f6d2be42f97be014a92df755 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
## `def test_grep_normal_hits_path_omits_fallback_key(tools: TrieTools)`

Asserts that `TrieTools.grep` omits the `fallback` key when primary search returns hits.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_returns_prose_and_neighbours fingerprint=8c1f77548638b430933ea0f0fab8a398b6ee3ac0f3dce12584d0dc79166d6f8e body_fp=14ff32e41d3877657b43db96a1023fcd785cfe7be555830fb4148f2716a187fd source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_read_returns_prose_and_neighbours(tools: TrieTools)`

Test that `TrieTools.read` returns structured output containing qname, prose documentation, and caller/callee neighbor lists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_source_pointer_shape fingerprint=420bf61a94fb75358593559620c310977d02c1bfeeb15481f3806550aeb73e97 body_fp=9c10a7bd8462eeeffb067c77f6232e527d03965183c5ad752721d9fd8ba7428e source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test-infrastructure -->
## `def test_read_source_pointer_shape(tools: TrieTools)`

Verifies that TrieTools.read returns a source_pointer field formatted as "file:start-end".
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_neighbour_carries_one_liner fingerprint=51c2f2f644f316fdeabf34c1c1d3b0dc3b57ec9e2f746d8c04d682b4cf8fd044 body_fp=d269d855ea4d61ef3eff3008d58164595e80a9075d32ccef17bed856301ab1f1 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=mcp-server -->
## `def test_read_neighbour_carries_one_liner(tools: TrieTools)`

Verifies that `read` returns caller/callee neighbours with a populated `one_liner` field from their triefact body.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_unknown_qname_returns_not_found fingerprint=3265a0090391b2d6756d124cacb28e9a01e3e19ee7b45fe0032c752b36efb7f7 body_fp=846327008162625c4784ab2b7e4fb99c15ad5a626d2f2ffc6d8872d90037ee16 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_read_unknown_qname_returns_not_found(tools: TrieTools)`

Verify `TrieTools.read` returns an error envelope with `not_found` code for unknown symbol names.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_fuzzy_suggestion_for_typo fingerprint=656607d4483ca9d33fd84a8e21cd913fd53f6dfb9c395347ff19d836dabaa261 body_fp=8a7a73dca5f4317beca6fb9103732d7ecc7a420d2d7e4b1a7e021b767ac3d1cb source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_read_fuzzy_suggestion_for_typo(tools: TrieTools)`

Tests that `tools.read` returns a fuzzy suggestion when given a qname with a typo.

- Passes `"lib:slugfy"` (misspelled); expects `error` with a `suggestion` containing `"slugify"` or `"grep("`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_file_path_returns_compact_triefact_view fingerprint=6b57267237051b42a5318728289aa553c37e72ce7444fa3438811b3a536569d7 body_fp=7e2181bc34cf878595156609210c3baf920849d27420cc0c12b3f27a33f1e8d4 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_read_file_path_returns_compact_triefact_view(tools: TrieTools)`

Assert that `TrieTools.read` with a file path returns `mode="triefact_compact"` and an output body containing per-symbol prose, not line-numbered raw source.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_file_path_full_returns_prose_without_sentinels fingerprint=2f4863371456f360a8c3f384298cfc091e166fdff563fd1d4c2816c88fa27f8c body_fp=debb0b1507c402c766095e50f7898cc50e7dbfb01a5efa05e5f14614f01d495a source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_read_file_path_full_returns_prose_without_sentinels(tools: TrieTools)`

Assert that `TrieTools.read` with `full=True` returns mode `"triefact_full"` and strips `trie:section`/`trie:end` sentinels from the prose output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_file_path_show_source_returns_numbered_source fingerprint=f91ec45789a68f8762848156a39f5bf01e3ba346ce19be5133acb819801d71a4 body_fp=c5f77403712597e0c2a000dbd26cee73a023e2b86b5e45768a9c53dba8c81d22 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_read_file_path_show_source_returns_numbered_source(tools: TrieTools)`

Assert that `TrieTools.read` with `show_source=True` returns raw line-numbered source, bypassing any existing triefact.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_file_path_offset_limit_implies_source fingerprint=d13150b206237c05dd2aaa58c2cd5e6ecff3e3abbe8e63e8e23e6b0b390f5438 body_fp=9394f942d9876ea9ebb55c613f3f3eb74eb36d5fd59df115ee2df58b9efbdc3d source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_read_file_path_offset_limit_implies_source(tools: TrieTools)`

Assert that `TrieTools.read` with `offset`/`limit` returns a 2-line raw source window with 1-indexed line-number prefixes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_non_indexed_file_falls_back_to_source fingerprint=abde138a5ab1033de13f6c0d1070a9c412642989343f50d3f03160c83d074511 body_fp=ecde1640ecd4a8b80d1a6fc8275751fa4a8051434d8792ef509949943f957be8 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_read_non_indexed_file_falls_back_to_source(tools: TrieTools, populated_project: Path)`

Assert that `TrieTools.read` returns raw source lines for a real file with no triefact entry, rather than an error.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_file_with_line_suffix_reads_source_window fingerprint=27731a689d725ac5dca781084b196761ac061473f6052ff512d70e7120589537 body_fp=1eb7852d233e6b4b0f7c661333cd6f53111c65452e47476c4e06ebd299036b3a source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_read_file_with_line_suffix_reads_source_window(tools: TrieTools)`

Verify that `TrieTools.read` with a `path:LINE` cursor string returns a windowed source response with 1-indexed line-numbered output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_callers_returns_topology fingerprint=ba52df6ec0918227c8a41b6a0d14ab17f8fca12de24f0684dd8eb190b5e31c9d body_fp=138416ddcb9b6521996a573f01f4f63145e8b4c447b14f03b928137d3cc413e9 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test-infrastructure -->
## `def test_trace_callers_returns_topology(tools: TrieTools)`

Verifies that TrieTools.trace returns correct topology with root, nodes, and caller edges for direction="callers".
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_callees_returns_outbound fingerprint=0f7a79554ab1ccc241fd5da78d98609b43458bbc13f8ab26ace19fde87547dde body_fp=1a44d056bc05f9758de821999bf1aa9b9a5f5f6fad42a4359629ed32d9df7ced source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test-infrastructure -->
## `def test_trace_callees_returns_outbound(tools: TrieTools)`

Test that `TrieTools.trace` with `direction="callees"` returns outbound references in the graph structure.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_both_directions fingerprint=d982c36f43d513419ade4e39cc8a34a1405626cf97bdb9cf3043e5dc8e96bab0 body_fp=63fa90e2454ff770a396d5b946889cdc8b06ca7d3a50203ea0d9e663dcee61eb source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_trace_both_directions(tools: TrieTools)`

Tests TrieTools.trace with bidirectional flow discovery.

- Verifies callers appear in nodes when direction is "both"
- Checks edges carry directional metadata for visualization
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_invalid_direction_returns_error fingerprint=ee66239794f468126ebd3f5e9d557088e75a14791456cb94d3242b919f9a1712 body_fp=a2d547049143be7c5c917ee06f845b3faedd2015fa43ef66230588f13bedb666 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test-infrastructure -->
## `def test_trace_invalid_direction_returns_error(tools: TrieTools)`

Verifies that TrieTools.trace rejects an invalid direction parameter with an "invalid_argument" error code.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_unknown_qname_returns_not_found fingerprint=4a972421a152c7b560db28c9f942d12a1917d194cc1acb5041774f2b39f1b89d body_fp=f3d5eb1040745139d4c0b10c5b4114c512535bbe3f1aef32578983bc96980c3f source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_trace_unknown_qname_returns_not_found(tools: TrieTools)`

Verifies that TrieTools.trace returns a not_found error for nonexistent symbols.

- Tests the error envelope structure when an invalid qname is passed to trace
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_depth_zero_returns_only_root fingerprint=76be5ecaba8cb2a295a796f304e77c718a9dcc8d23868995efa57a5182d2a1c2 body_fp=d5d3058e0a83e508ad317c5cba08c8e9b6746d63edb64ca2fa310d2970f60b89 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test-infrastructure -->
## `def test_trace_depth_zero_returns_only_root(tools: TrieTools)`

Verifies that trace with depth=0 returns only the root symbol with no edges.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_depth_clamp_adds_note fingerprint=c455960b8dcfb8693c4e826945685a9217238b8705ee7806c1ca182dccf62c13 body_fp=41560787deea99202e725a1fa86da5ef9521fb357ec768f471416d4e0279432d source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_trace_depth_clamp_adds_note(tools: TrieTools): # trace_max_depth defaults to 5; ask for more and expect a note.`

Tests that `TrieTools.trace` adds a note when depth exceeds the configured maximum.

- Requests depth=99 against default max of 5 and verifies "clamped" appears in response notes
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_build_server_registers_three_verbs fingerprint=6b9681c689a428da5e4f2498ee941fd5a83453ab2b5fb8299f484f077f69d5a3 body_fp=50dab4abf624047e5d769cb42fc81293f74dfc0034c9046fc0f7b7b335085f0b source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_build_server_registers_three_verbs(populated_project: Path)`

Verify that build_server registers all expected tools in the FastMCP server.

- Core tools: `grep`, `read`, `trace` must be available
- Extended toolset: 8 additional tools including `grep_str`, `explain_symbol`, `trace_flow`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_build_server_wire_names_bind_to_internal_methods fingerprint=42abb0fbb0129220325c2595388e9ba5ed60fddb52d3f61e9c97dea78ec9535c body_fp=53a78fc1a71a9f7587ee76934c92e9e7eb68f99d6eccd93bb8edb7d6604a7d21 source_ref=f933e63abf1854a8a6ecb8b9c8cb4644acb3b90c role=test -->
## `def test_build_server_wire_names_bind_to_internal_methods(populated_project: Path)`

Verifies that MCP tool names dispatch to corresponding `TrieTools` methods.

- Query tools (`grep`, `read`, `trace`) are wrapped via `_textified`; assertions check `fn.__wrapped__`
- Edit tool (`patch`) binds directly; assertion checks `fn` without unwrapping
- Pins CLI and MCP surfaces to one implementation per verb
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:dual_rank_project fingerprint=ddb09bc1e817a930bec9a532e1c272d2dfef3a3e605bc48f4679ba42ed216ee6 body_fp=36312b5b418e5db68b94e118fc6562207856923cd6bdd7222eb75dbbc45037e7 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=test-infrastructure -->
## `def dual_rank_project(tmp_path: Path) -> Path`

Creates test project with two auth symbols ranked by inbound count for fuzzy matching tests.

- Returns populated temporary project with hub_authenticate (3 callers) and auth_check (2 callers)  
- Both symbols contain "auth" for equal text relevance but different centrality scores
- Tests sorting behavior where niche symbols rank before hubs at equal relevance
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_entry_points_niche_ranks_before_hub fingerprint=a5bf02d8993e8282336d29b02cec7ebb34624737bcbad9c62cbda7acad54290e body_fp=26244541e4b38025182dfad2c3da870f713cab045d65adec27a4fbe288313ee8 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_grep_entry_points_niche_ranks_before_hub(dual_rank_project: Path)`

Verifies `grep_entry_points` ranks niche symbols before hubs when relevance scores are equal.

- Uses `dual_rank_project` fixture with `auth_check` (2 inbound) and `hub_authenticate` (3 inbound)
- Queries "auth" to match both symbols with equal text relevance
- Asserts `auth_check` appears before `hub_authenticate` in results
- Tests the sort key: score DESC, inbound_count ASC
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_entry_points_hits_carry_score fingerprint=bf76df08b996d67ba20379770a38f838d8fe1c762948d49445555df41368cc37 body_fp=0da678684c72612dd7572e730336cd970345d9a486989d21a1ffb722bc705c31 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_grep_entry_points_hits_carry_score(dual_rank_project: Path)`

Verifies that grep_entry_points results include a numeric score field for ranking.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_symbol_typo_tolerance fingerprint=998a77d9bbc63dc7fa9771cbe44d66c7262382670d46446093a4c0102cb98e51 body_fp=0f25743db2a294dc0db44b7bc28eb6db47497b3b243fbda9358698613a6968ab source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=mcp-server -->
## `def test_grep_symbol_typo_tolerance(tools: TrieTools)`

Verifies that TrieTools.grep_symbol resolves single-character typos using fuzzy matching at cutoff 45.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_symbol_returns_score_field fingerprint=d875689a783594250d150f3a147a935eeeb38aeb1fadede0bc7712cc65914a22 body_fp=8d76aaa1cd4d54cbd8b8024d0fdfc2d2612614c191b9a4247f5b4a2667e60dd0 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test-infrastructure -->
## `def test_grep_symbol_returns_score_field(tools: TrieTools)`

Validates that `TrieTools.grep_symbol` returns symbols with numeric score fields in both match and similar arrays.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_fuzzy_prose_fallback fingerprint=0bdb61dcf7c038d93f1a7a4598b1a770d003ba2609b446451546db3192d4dd4e body_fp=31811a8441329f7dc63491205c1d59217cc88500d40b69f1fc146ff5d8ac3a15 source_ref=a1fd6852599cae8c3574868f3e9f120e8ba53eab role=mcp-server -->
## `def test_grep_fuzzy_prose_fallback(tools: TrieTools)`

Verifies grep's fuzzy prose fallback surfaces symbols containing concept words when name_contains finds no exact symbol name matches.

- Uses "lowercase dash separate" as a test phrase that appears in slugify's triefact body but not its name
- Expects either text_match (ripgrep literal match) or fuzzy_prose (fuzzy scoring) fallback types
- When fuzzy_prose fallback activates, validates slugify appears in the returned matches
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_str_fuzzy_fallback fingerprint=67380bf7bf45fed97698909288b028bd324ec109f63ba4924f1ec5a14d9de327 body_fp=f9fc8c1fd28dc0e571c972a869bd011c20d739480e4846ded9421b934331c725 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_grep_str_fuzzy_fallback(tools: TrieTools)`

Tests that `grep_str` returns fuzzy fallback when pattern matches nothing in source.

- Verifies empty hits array when nonsense pattern finds no regex matches
- Confirms response includes `hits` key to prevent crashes on malformed responses
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_str_fuzzy_fallback_finds_close_name fingerprint=0dc0ff2f1a636680859fd46f2db38dac736a30e6bc5ada90d65313099d97ec0b body_fp=032aa5c09b81c66987811ee6d60115e42788b3bb2b4816ddfd8277e1afb1afe8 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_grep_str_fuzzy_fallback_finds_close_name(tools: TrieTools)`

Verify grep_str returns fuzzy fallback when regex search fails but symbol name is close to query.

- Tests grep_str with typo "slugufy" expecting fuzzy_one_liner fallback to surface "slugify"
- Skips assertion if ripgrep accidentally finds literal matches in source
- Validates fallback contains expected symbol via name matching
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_str_all_finds_non_indexed_file fingerprint=dc3e9e6b1e196c6e51059cbdcecb830a3116e01b8410665633c730fb2cc90ef5 body_fp=a0edab26feb62960b87695a95e467f0794f7cc3502e291095c118e7fd2ee7e3f source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_grep_str_all_finds_non_indexed_file(tools: TrieTools, populated_project: Path)`

Tests that `TrieTools.grep_str_all` searches the entire repository including non-indexed files.

- Creates a `package.json` file with "WIDGET_MARKER" content outside the indexed scope
- Verifies the search result includes the non-indexed file in `text_hits`
- Confirms `text_match_count` reflects the found occurrence
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_str_all_attributes_indexed_hits_to_symbols fingerprint=df6205a39150a2009abb81500fad1584543648c73cb153c08b54c6cd57f835e7 body_fp=57f940da634f9c4fa5e49fd75a5d1c9f702048cf5fe35011574ff3e1db531a43 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_grep_str_all_attributes_indexed_hits_to_symbols(tools: TrieTools)`

Verifies that TrieTools.grep_str_all attributes in-scope code hits to their enclosing symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_str_default_does_not_see_non_indexed fingerprint=9db8d225679c2dce1b468229e31ae87ec020b5b954d63908f3a4c4f108635f3f body_fp=7dbff148db4c4e6b92460acfb5f89cde9963fa6767319fd149fde5bcbf0db391 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_grep_str_default_does_not_see_non_indexed(tools: TrieTools, populated_project: Path)`

Verifies that `grep_str` does not search non-indexed files outside project scope.

- Creates a `.txt` file with `ZEBRA_MARKER` pattern outside the indexed scope
- Asserts `grep_str` returns no hits, confirming scoped-only behavior
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_find_files_by_extension fingerprint=3a8a987763b83aaae5d875cdb249319b978d351ebbb637b3eb004bbd584b159c body_fp=0e00937b305ee9dbac239cc14b57a41921d6a40c0d8e21ddc1ab2d41340c6244 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_find_files_by_extension(tools: TrieTools, populated_project: Path)`

Test function verifying TrieTools.find_files locates files by glob pattern across the entire repository tree.

- Creates a JSON file and searches with `**/*.json` pattern
- Asserts the created file appears in the matches list
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_find_files_by_bare_name fingerprint=f972eb5809a15bbb04979f3fbce83b3413132ff55e7b5efaa8f378f0ba5a0297 body_fp=925248ad2960c03aa22265a051f0d7238119a45e64442bcd6b9ce2bf22fe890d source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_find_files_by_bare_name(tools: TrieTools)`

Test that `TrieTools.find_files` matches bare filename "trie.toml" anywhere in the project tree.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_find_files_indexed_only fingerprint=d654cd5e6aa952fa1f1123ea0a428e93948c4c9cc5b0d6cfac02074ae277e6d7 body_fp=cab8c78d78a2128208104a18a86c197f23e5e9917dddebba92cf713f90ae5bc6 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_find_files_indexed_only(tools: TrieTools, populated_project: Path)`

Verifies that `find_files` with `all_files=False` excludes files outside the configured project scope.

- Creates a `.json` file outside the indexed scope and confirms it doesn't appear in results
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_find_files_prunes_trie_dir fingerprint=5ff63a50b6fdfa1486e9b58342409a001ed12ea65d96cfecfd6942a8158bcce9 body_fp=6551f0f428e1689a9642065628f98e008b67bfc388f52acd6864c65576f80cc7 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_find_files_prunes_trie_dir(tools: TrieTools)`

Asserts that `find_files("**/*")` excludes .trie/ cache directory from results.

- Verifies no returned match starts with ".trie/"
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_source_non_indexed_file fingerprint=7bcc643759c4d737b2eaa5be5f86a2f4e6f512276ad440593df4406669703efb body_fp=06d448c211ab57a9c3e8166ed5ef909b8e9da6fa744cb4e08c96cd98f2480485 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_read_source_non_indexed_file(tools: TrieTools, populated_project: Path)`

Tests that `TrieTools.read_source` returns line-numbered content for files outside the indexed scope.

- Creates a YAML config file with test content
- Verifies the returned lines include proper 1-based line numbering prefixes
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_source_offset_limit fingerprint=1407d19f8963802f0fae065677fb9df4505f542ccb0fd625e11a248501483758 body_fp=62a53bb4bcf60c95b6e8e705c5face659125db7c55e39e6fce41682c9d3da447 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_read_source_offset_limit(tools: TrieTools)`

Tests that `read_source` respects offset/limit parameters for windowed file content with line-number prefixes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_source_missing_file_errors fingerprint=67f22f208b6e898839363540a119cef953279fef21d75cceb7ef35b60251f3be body_fp=ffdba52c0b925517ae51ee3e53718d588d15f7a5f10e3dd9694ef45e0426ddb6 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_read_source_missing_file_errors(tools: TrieTools)`

Tests that `read_source` returns a structured `not_found` error for missing files.

- Verifies error envelope format and error code when file doesn't exist
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_source_directory_errors fingerprint=0432aeb65c449a586591abad24f301a936208df89b04fcefba1af36edeb8ebf3 body_fp=c712a266f8d556c15f48f42f0c55fde3009d0cedc1e7f9052d4e272eef6c2e8c source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_read_source_directory_errors(tools: TrieTools)`

Verifies that TrieTools.read_source rejects directory paths with an invalid_argument error.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_blast_radius_reports_cascade fingerprint=d64d9faa1ca0fa081d2b8b0c081b4a7f35faab7d756d308316140c02a66f64be body_fp=8320423bedd5b175646d489030b6dffb0bd032bb5400f75942520cb31c18de0f source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_blast_radius_reports_cascade(tools: TrieTools)`

Verifies that TrieTools.blast_radius returns the cascade set of symbols affected by editing a given symbol.

- Tests with "lib:slugify" and asserts "make_url" appears in the cascade (symbols that reference slugify)
- Validates the response contains the original qname and no error field
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_blast_radius_unknown_symbol_errors fingerprint=5043abdf9e81ce86f69ffb20bce9e767e715283736669d4b5a376ff86a728711 body_fp=acda66b5ce057b915c6a5163e098f3ca7cb243c6b3ac66813621f5d7fcaaaecd source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_blast_radius_unknown_symbol_errors(tools: TrieTools)`

Tests that `blast_radius` returns a structured not_found error for unknown qnames.

- Verifies the error envelope contains code `"not_found"` for missing symbols
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_write_file_creates_new_file fingerprint=a625baeab49c1742208ace6e441a610b4522a4201b6c8c4fd509965b94b8133c body_fp=ab5a33231d8b2a7a566eb3eeb7fb9a456092cb4e791c3b193bd3fe65f28265fd source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_write_file_creates_new_file(tools: TrieTools, populated_project: Path)`

Verifies that TrieTools.write_file creates new files at arbitrary paths under the project root.

- Tests creation of a markdown file at `docs/GUIDE.md` with provided content
- Asserts `created` field is True in the response
- Verifies file content matches exactly what was written
- Confirms `needs_sync` is False for non-indexed files
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_write_file_refuses_clobber_without_overwrite fingerprint=6ca5633b82491578fc4bcb80623ea8727a340c20e211f4f4c775bb62b9a9868b body_fp=a674fb0030340d0c1f3bd47bccb1c0d2a77f1094c84b3498239bde8fdb22d192 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_write_file_refuses_clobber_without_overwrite(tools: TrieTools, populated_project: Path)`

Tests that `TrieTools.write_file` prevents overwriting existing files without an explicit overwrite flag.

- Creates existing file with "original" content
- Attempts write without overwrite=True should return error result
- Original file content must remain unchanged after failed write attempt
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_write_file_overwrite_flag fingerprint=890ca72e91e1add4c80c109ca4bd73e2e72e09750c27c8c4cf2ebd002a64dcbc body_fp=a89d1c242151fd691e09113dffb4b55bc7dd75d52bb03159c9888d71e133301f source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_write_file_overwrite_flag(tools: TrieTools, populated_project: Path)`

Tests that TrieTools `write_file` method replaces existing files when `overwrite=True` is specified.

- Creates an existing file then overwrites it with `overwrite=True`
- Verifies the `created` flag is `False` for replaced files
- Confirms the file content is actually replaced
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_write_file_indexed_path_flags_needs_sync fingerprint=a2e493e8b0c884519bdc58108821684efe510ef34a74485af80fff2e00065c95 body_fp=3dd083d6be00a17aec6976acdf2ba6f4a48ebf70ff3eaa8e0abfe473d787f9e3 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_write_file_indexed_path_flags_needs_sync(tools: TrieTools)`

Verify that writing a Python file in scope sets the `needs_sync` flag to True.

- Tests the `write_file` method on TrieTools by creating a new `.py` file
- Asserts that `created` is True and `needs_sync` is True for indexed file types
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_write_file_outside_root_errors fingerprint=ffdc9ecc8c71ab21b24a1e08a3111cc2cb3d83f2a4372ef9fe180f1686049b11 body_fp=906e1c825ccae909909de67acda8669b3d8bae1a381b56c5bb592af2bda0cec1 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_write_file_outside_root_errors(tools: TrieTools)`

Tests that TrieTools.write_file rejects paths outside the project root with an "out_of_scope" error.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_batch_patch_stages_mixed_items fingerprint=3d00e899a80e9e08eeef7d73b4336b913c66c1de9778b844a3013c6fdc1b22bb body_fp=e46137b55cc9a6d0bcd1676d6c65f3c9cb84830373c1e1691b36d72f860a2e8c source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_batch_patch_stages_mixed_items(tools: TrieTools)`

Verify `TrieTools.batch_patch` stages a mixed list of `patch` and `create` operations in one call and reports per-item results with zero failures.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_batch_patch_reports_bad_items_without_aborting fingerprint=9a65c75c5ae6a3bd4f214a494038a2354da197d8c454e2ac0dfc5bb16569fc60 body_fp=83925c800a96c3550e55018a5551f099f78385f37952a822a4bad11999ff425a source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_batch_patch_reports_bad_items_without_aborting(tools: TrieTools)`

Assert that `batch_patch` reports per-item failures for a missing symbol and an empty note without aborting the remaining valid item.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_batch_patch_empty_list_errors fingerprint=fcc2566ebf71c33e9a5308d9357a7fa63ae48b40444578b6c6a0a1241780390f body_fp=7ea1b2f41706270e46163525ac4bbe6a9de8317f0851c91a5945ba23920722d0 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_batch_patch_empty_list_errors(tools: TrieTools)`

Assert that `TrieTools.batch_patch` returns an `invalid_argument` error when called with an empty list.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_warns_when_prose_is_stale fingerprint=354d1b9012fc3069a29ddd84391ffd87f628ae9dcc8b7548a06000e65dfc7fb6 body_fp=d5b81a8ac924b3c3118d56b1033f74759a13f611eb267e502388f443cd64f773 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_read_warns_when_prose_is_stale(populated_project: Path)`

Assert that `TrieTools.read` attaches a `STALE` note to a symbol whose prose predates a source edit followed by a re-scan, and that the compact file view also carries a `STALE PROSE` banner.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_warns_when_graph_itself_is_stale fingerprint=b73cd9b61ae0d89dba0ba5f3552d6856997e6654f5e2ed7c7bb876086ff76964 body_fp=92c5bec019bd88160ff295ef337648c25d216a5c2d7606122f7edb28b7d69c72 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_read_warns_when_graph_itself_is_stale(populated_project: Path)`

Assert that `TrieTools.read` includes a graph-stale warning when source is edited without a subsequent re-scan.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_has_no_stale_warning_when_fresh fingerprint=3a3f1a75d8300ad70c423063a319bb7366e2b6f86c1d3a1f4af6472a216317c6 body_fp=9cf8ab8f28ce1935a8f1079c92372dc59fbda90bd400f704ac438e3ab3f4ca34 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_read_has_no_stale_warning_when_fresh(populated_project: Path)`

Assert that `TrieTools.read` emits no stale warnings when prose and graph are both current.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_read_history_flag_surfaces_intent_trail fingerprint=624c588da05df6e2b0d1ce6b96520d641ed4853ebbbfd4985bfa1741a19ef510 body_fp=ece1bc17478c3717f80af088ca7f4bd559b688200ff10566a78485c2cb05067d source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_read_history_flag_surfaces_intent_trail(populated_project: Path)`

Verify that `history=True` on `TrieTools.read` and `explain_symbol` attaches the digest-archive intent trail, while the default call omits it.

- Writes a stub triediffs archive entry before constructing `TrieTools`.
- Asserts `history` key is absent from the default `read` envelope (opt-in contract).
- Asserts symbol read, file view, and `explain_symbol` all surface the parsed trail when `history=True`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_fuzzy_score_is_graded_not_binary fingerprint=e976182f5768720b693cf0e1b41b872184c7917b706a5db58f3841fd70e0bb9d body_fp=41a2ead542c4106f334f92d8bd8f147873baff7c6620682dd88f5360247ed460 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_fuzzy_score_is_graded_not_binary()`

Regression test asserting `_fuzzy_score` returns graded scores: exact match = 100.0 > prefix > tight substring > long substring.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:project_with_tests fingerprint=c6b917106000009b6d01d6ae84ee30d8d7b09ccac17e6b4dc9dab4b6abaea600 body_fp=8f08350b01c621954247c4ad7ffc508b5c57be4ce1645ce49c1573eb63b1ccb0 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def project_with_tests(tmp_path: Path) -> Path`

Pytest fixture that creates a scanned project containing a production symbol `lib:write_stamp` and a same-named test twin in `tests/test_lib.py`, both indexed.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_symbol_prefers_production_over_test_twin fingerprint=26d3f44e58a02c7e979b2426cffba9f94559a0f595a9be6225635e3aa30ade74 body_fp=feade8efc9db0a3683faacd8918d7e2d2acc9d6469a4413aaf1d578c19a8baab source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_grep_symbol_prefers_production_over_test_twin(project_with_tests: Path)`

Assert that `TrieTools.grep_symbol` resolves `"write_stamp"` to the production symbol `lib:write_stamp`, not the test function containing the query as a substring, and that the test twin still appears in `similar`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_trace_flow_fragment_resolves_to_production_symbol fingerprint=2f3a750b8661cd90c84dcc35d0ef1d1021047b99c6d7aa4a1e042aa1c2a1dc73 body_fp=d726486e8a678c0d073d43ed4de73b54228569143309f8127b5d76fd2d4a82f9 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_trace_flow_fragment_resolves_to_production_symbol(project_with_tests: Path)`

Verify that `trace_flow` resolves the fragment `"write_stamp"` to the production symbol `lib:write_stamp`, not a test twin.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_grep_entry_points_excludes_test_symbols fingerprint=3ac53333973fc4f3d4dd13b345aa2119e2d7261e419d22b5347deaf797cf1294 body_fp=7138a890b5ae9c3f9c61aa118e93703d26eaf9fcaa2358961eb18dc334c57358 source_ref=0e70e3437bf23750bbc0794f428d8b7859e56a53 role=test -->
## `def test_grep_entry_points_excludes_test_symbols(project_with_tests: Path)`

Assert that `TrieTools.grep_entry_points` never returns symbols whose qname starts with `tests/`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp:test_mcp_wire_query_tools_return_text fingerprint=7105fd56a7a42c3369936db238d9a7a0aa0e71f56c9f5c8281e2e274fc2b0ad7 body_fp=df190b5c04651c2cc475d6fee55795e22027b208f0e0636a9a2284d5e112a376 source_ref=f933e63abf1854a8a6ecb8b9c8cb4644acb3b90c role=test -->
## `def test_mcp_wire_query_tools_return_text(populated_project: Path)`

Assert that MCP query tools (`grep`, `trace_flow`) return rendered text, not JSON, while edit tools (`patch_list`) keep structured JSON envelopes.
<!-- trie:end -->