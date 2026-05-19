---
trie_version: 0.1.1
source: tests/test_mcp.py
file_fingerprint: d218c8963e8f6a6df5142104106456bfb95ddbe3f7ca4830f87da01c6cb6318e
last_synced_at: '2026-05-19T10:38:21Z'
description: 'Tests for the MCP tool surface: `grep`, `read`, `trace`.'
defines:
- kind: module
  qualified_name: tests/test_mcp:__module__
  lines: 1-515
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
  lines: 483-494
- kind: function
  qualified_name: tests/test_mcp:test_build_server_wire_names_bind_to_internal_methods
  lines: 497-514
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

















































<!-- trie:section symbol=tests/test_mcp:test_build_server_registers_three_verbs fingerprint=017fbe1b09387e95619e1a41502d43b523d63dea07b52425d55d1381011d3029 body_fp=ba6e6f40c711df5f3ea55226930fd8037c92b25805e2eed509991c769c399bca source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_build_server_registers_three_verbs(populated_project: Path)`

Verify `build_server` returns a FastMCP instance with exactly `grep`, `read`, and `trace` registered as tools.
<!-- trie:end -->



















<!-- trie:section symbol=tests/test_mcp:test_trie_tools_init_fails_clearly_when_rg_missing fingerprint=2ea97d1b02ea695fbca32b81cfd8377a7e1da3159c9b30a1815fe2099d25638b body_fp=2a96793ec1cda466eeaaf3c09ac0b655fcf2e8eb2f47306256a27b1b78c5d47b source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_trie_tools_init_fails_clearly_when_rg_missing(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `TrieTools` raises `RipgrepNotFoundError` with an actionable message when `rg` is absent from `PATH`.

- `monkeypatch`: stubs `shutil.which` to return `None`, simulating missing `rg`.
- Error message must contain `"rg"` and either `"install"` or `"ripgrep"`.
<!-- trie:end -->



<!-- trie:section symbol=tests/test_mcp:test_build_server_wire_names_bind_to_internal_methods fingerprint=a480374391cd52c59bd6c51db2664d53e9150773ce64b5a08555c94f8cf832c5 body_fp=2d3f7fa4a7536b286b48c5ccef2a35d2dbc21df0d1eaa745de4f1f227510545c source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_build_server_wire_names_bind_to_internal_methods(populated_project: Path)`

Assert each FastMCP wire tool's `fn` attribute points to the matching `TrieTools` method.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_grep_name_contains_returns_matches fingerprint=13a70b013b95687914be7cf11a6a2926e39e6d256ed6ee0fc19ec38c6f2bcffb body_fp=09e4936084d84fe138daaf8c45a55d8fb344a06d72a915334e5e7c57e629d51c source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_grep_name_contains_returns_matches(tools: TrieTools)`

Assert that `grep` with `name_contains` returns matching symbols and omits the fallback envelope.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_grep_returns_one_liner_from_section_body fingerprint=37a68231e58a6658814f1e064b7c136eeaa7a7f879f70bdfd4eaa836d69779ad body_fp=103b6ba0d0ec96ddde1d75abd10338a8cf5c18f01bf287417fdbd9b6f2222374 source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_grep_returns_one_liner_from_section_body(tools: TrieTools)`

Assert that grep hits include a `one_liner` field derived from the triefact section body.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_grep_returns_file_pointer fingerprint=fd44c10f827063015b2af6e12727ce6f8e2d67973fc32ea706be0a403274f87e body_fp=2a998bd16e7316172b31f19ac977015bf90977d4b4765b966c73f24be2a99657 source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_grep_returns_file_pointer(tools: TrieTools)`

Assert that `grep` hits include a `file_pointer` of the form `<filename>:<line>`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_grep_kind_filter fingerprint=05f736a15cd7708beed46d7beef0835ba93bb4867f848cec7c0d4da66a5d31bf body_fp=7f2f3da9891b906225e5f3242042e85be2507061a59930863fc9e5df4229bafe source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_grep_kind_filter(tools: TrieTools)`

Assert that filtering by `kind="class"` returns zero hits when only functions exist in the fixture.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_grep_invalid_kind_returns_error fingerprint=93c63e643ced72ef46d974b15a6f15362abaa72e8e7b439e17f8d46411602d2e body_fp=4af18d263328b07ad0260e8f5d44a00017f2bb8e185a33cd693d4478ca8d44e7 source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_grep_invalid_kind_returns_error(tools: TrieTools)`

Assert that passing an unrecognised `kind` value returns an `invalid_argument` error dict.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_grep_scope_prefix_filter fingerprint=4087ec669cf402755c9ebcba58be379db4f126a23aaa314712e20b33ffa6a9f0 body_fp=75113f58734cf7b41af95f4b9cb5f978cae16b7e6e71c3564565be0b26a43a1a source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_grep_scope_prefix_filter(tools: TrieTools)`

Assert that `grep` with `scope_prefix` returns only hits whose file paths start with that prefix.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_grep_scope_exclude_filter fingerprint=d9ed58e0d2cb505d72e32ca79f8f8032c881eff47584a5bf9377a006626e5793 body_fp=8f0f8424014ac84df63ffc33ddd349183edd76ef7180f363527d75882544d18a source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_grep_scope_exclude_filter(tools: TrieTools)`

Verify that `scope_exclude` removes matching scopes from `grep` results.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_grep_inbound_count_predicate fingerprint=29ed9feb09b2e5254bd1cef76cabd75536142afaac8b064dcc196599c69f7b0b body_fp=bb16cb7153c6d67c51c7f1a179e5f3970ce0f57edbd341f94d83774db04fd7c0 source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_grep_inbound_count_predicate(tools: TrieTools)`

Verify that `grep` with `inbound_count: {min: 1}` returns symbols with inbound edges and excludes those with none.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_grep_rank_by_inbound_count fingerprint=956741b97e66e5508ccc0365fd3a6a04e6e7c6f3cb7da4770fc673b73a03477e body_fp=d08117d04063a03ac0a2a5ecae66304ff3bce908f088b088daa9fef41ca0bce4 source_ref=b8a4bd60079a901c70ffa0704165e5211e078db6 -->
## `test_grep_rank_by_inbound_count(tools: TrieTools)`

Assert that `grep` with `rank_by="inbound_count"` returns hits in descending inbound-count order.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_grep_limit_respected fingerprint=80407aa581af3497200f623a81e718ea1e94ee91389ac126830562e3b69348af body_fp=cc707794291cc445710a69357ad9a79deb343a473ed805122c8ca4000a8b8e4a source_ref=b8a4bd60079a901c70ffa0704165e5211e078db6 -->
## `test_grep_limit_respected(tools: TrieTools)`

Assert that passing `limit=1` to `grep` returns exactly one hit.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_grep_unknown_predicate_field_silently_ignored fingerprint=d932c0e53093906441747dbaef79cf5c314d42057b100dc5b2f257cc7518c2f0 body_fp=15b5b14a500d36307b23e45fb3db149c422266c4a0ab2352e469188a56e506cf source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_grep_unknown_predicate_field_silently_ignored(tools: TrieTools)`

Assert that unrecognised predicate fields are silently ignored and valid filters still return matches.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_grep_invalid_predicate_returns_error fingerprint=a7cc46c17ae0d8aa0cd7f2ea984b0423139fb7ac60d05209e81e0ff92529668d body_fp=17bda2f7ed9818b2b9b4d783c28f59e522b238ef1bb7a7ac3d4f17d8afcd6da6 source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_grep_invalid_predicate_returns_error(tools: TrieTools)`

Assert that passing a non-dict predicate to `grep` returns an `invalid_argument` error dict.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_kind_none_when_no_name_contains fingerprint=4e6e6519556d6b7fd8d18bba3fffc5f082582756e2362308de5d5c28e746be5e body_fp=27d4f8b1530becd58604970b0e61a7015dab834d6d3f63e9b22163af40dfb98c source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_grep_fallback_kind_none_when_no_name_contains(tools: TrieTools)`

Assert that a predicate with no `name_contains` and zero symbol hits returns `fallback.kind == "none"` with a note referencing `name_contains`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_kind_text_match_empty_for_unseen_string fingerprint=69f80642424418ade7fb9f362dc9f273b6a72bb84ecb843ccc644431f6056736 body_fp=da43a5552c767cb2ea30607a4261e831c637503e0329b4d2eec9e2fac33849a4 source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_grep_fallback_kind_text_match_empty_for_unseen_string(tools: TrieTools)`

Assert that `grep` returns `fallback.kind == "text_match_empty"` when `name_contains` matches no symbol name and no source body.

- `fallback.query` echoes back the searched string.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_kind_text_match_redirects_via_body_match fingerprint=d62ca25bade3109437990a6051d0a8e8811a4c2b569a8dc05e9bff1f79505cb8 body_fp=903b1a3a82b933d55114db06a79454a38cc2920aa211ee3cdb226aba8cc2cb4e source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_grep_fallback_kind_text_match_redirects_via_body_match(tools: TrieTools)`

Assert that when `name_contains` matches a string inside a symbol's body (not its name), the fallback returns the enclosing symbol with `kind == "text_match"`.

- `tools`: populated `TrieTools` fixture with `lib:slugify` and `app:make_url` synced.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_ranks_by_inbound_count_desc fingerprint=ef3ac182e9ce5a40ceecd0150cf8383538870bd63efa253d6c0217440cccaa12 body_fp=823f39060cfbdd44033d3339c50e470a3a35ce91254bd15694807eafe61bdcf0 source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_grep_fallback_ranks_by_inbound_count_desc(tools: TrieTools)`

Assert fallback candidates are ordered by `inbound_count` descending when no symbol name matches.

- Skips if the fixture gains a symbol literally named `"title"` or yields fewer than two candidates.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_caps_matches_and_notes_truncation fingerprint=ecfb2d89504fa8c1d8605600e0862e1c961e5ed2840d64902cb9fc4e173cb723 body_fp=cf4191707ad37d5c258ffe8a359b1590854b362654a854a4e74997c1a01655db source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_grep_fallback_caps_matches_and_notes_truncation(tools: TrieTools)`

Assert that broad fallback queries return a ranked top-N slice with a truncation note, not a refusal.

- Forces `grep_fallback_match_limit=1` to trigger truncation on the small fixture.
- Verifies `fallback.unique_symbols` exceeds the capped `matches` list length.
- Confirms the truncation note contains `"of"` (e.g. "Showing top 1 of N…").
- Checks the single returned match still carries `qname` and `inbound_count`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_omits_truncation_note_when_under_cap fingerprint=cf99e3b6a8f38acee3321f95f67be04eb837de301219103c85baec04b0a7bad0 body_fp=6caac8f17f077149611ce22c49734328b2420a4a705a637de12ae028ed2eae6e source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_grep_fallback_omits_truncation_note_when_under_cap(tools: TrieTools)`

Assert that no truncation note appears in the fallback envelope when match count is within the cap.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_grep_fallback_honours_scope_prefix fingerprint=31b191790a84b0b474a2cc9861f586ab8ea42430ceded08fcc62bdb2df882d24 body_fp=a4b85f803d10dc52cff8c65adddc0638eaad8e84e64e96d853dd7d413f5cfeb7 source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_grep_fallback_honours_scope_prefix(tools: TrieTools)`

Assert that `scope_prefix` filters fallback candidates so no out-of-scope symbols appear in fallback matches.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_grep_normal_hits_path_omits_fallback_key fingerprint=e4d4fa9ea51cf2db4cfeb5df2b356f09c2f3af9fb4af96059369c25e6b38f07d body_fp=c0f9fb82056027f99025af96bd69463433b507766eaee4a98977c25cbe71b07a source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_grep_normal_hits_path_omits_fallback_key(tools: TrieTools)`

Assert that a successful `grep` response contains no `fallback` key.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_read_returns_prose_and_neighbours fingerprint=8c1f77548638b430933ea0f0fab8a398b6ee3ac0f3dce12584d0dc79166d6f8e body_fp=6ecc648d5c7d4a7e3ef67005c3b9ae82bb69b43180f437bd95b3f5775be0d479 source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_read_returns_prose_and_neighbours(tools: TrieTools)`

Assert `read("lib:slugify")` returns prose content, correct callers, and an empty callees list.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_read_source_pointer_shape fingerprint=420bf61a94fb75358593559620c310977d02c1bfeeb15481f3806550aeb73e97 body_fp=2be51b834ede5aaae9cc28f0cbc5c755cd8e47c683807515e31f629ef650ff3c source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_read_source_pointer_shape(tools: TrieTools)`

Assert that `read` returns a `source_pointer` in `"file.py:start-end"` format.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_read_neighbour_carries_one_liner fingerprint=51c2f2f644f316fdeabf34c1c1d3b0dc3b57ec9e2f746d8c04d682b4cf8fd044 body_fp=71e9cf890c028244059f96cd1d9c50f1dc2516ce4cf313e7a658ce160345b500 source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_read_neighbour_carries_one_liner(tools: TrieTools)`

Assert that a caller neighbour returned by `read` includes a populated `one_liner` field.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_read_unknown_qname_returns_not_found fingerprint=3265a0090391b2d6756d124cacb28e9a01e3e19ee7b45fe0032c752b36efb7f7 body_fp=6df38ad52a7021926de83590054de13a74288db2501447381f019980661d3845 source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_read_unknown_qname_returns_not_found(tools: TrieTools)`

Assert that `read` returns a `not_found` error dict for an unrecognised qname.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_read_fuzzy_suggestion_for_typo fingerprint=656607d4483ca9d33fd84a8e21cd913fd53f6dfb9c395347ff19d836dabaa261 body_fp=7e9b2377ca51f3c8ca62bbb7f2192198b47967f84cff1a440cb8a4dbe0ddac76 source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_read_fuzzy_suggestion_for_typo(tools: TrieTools)`

Assert that a misspelled qname returns an error with an actionable suggestion containing the correct symbol name or a `grep()` hint.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_trace_callers_returns_topology fingerprint=ba52df6ec0918227c8a41b6a0d14ab17f8fca12de24f0684dd8eb190b5e31c9d body_fp=d020b40356b1299c663edb07760b76a20e949f623a74d0f57a071d78af06d0cd source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_trace_callers_returns_topology(tools: TrieTools)`

Assert that `trace` with `direction="callers"` returns the root node, reachable caller nodes, and correctly directed edges.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_trace_callees_returns_outbound fingerprint=0f7a79554ab1ccc241fd5da78d98609b43458bbc13f8ab26ace19fde87547dde body_fp=12d9bed00c44d5f21a8b4f721254ff2565414617af9292787099f26e42dc4925 source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_trace_callees_returns_outbound(tools: TrieTools)`

Verify `trace` with `direction="callees"` returns outbound edges from `app:make_url` to `lib:slugify`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_trace_both_directions fingerprint=d982c36f43d513419ade4e39cc8a34a1405626cf97bdb9cf3043e5dc8e96bab0 body_fp=92a02d467228e2f86dbf14163a1efdd202561becd07257a3c1d5d4c4c519bb1e source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_trace_both_directions(tools: TrieTools)`

Assert that `direction="both"` includes inbound caller nodes and edges in the trace result.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_trace_invalid_direction_returns_error fingerprint=ee66239794f468126ebd3f5e9d557088e75a14791456cb94d3242b919f9a1712 body_fp=a456ca3bdbddb5539516a7c34c0c71ad1e63c73292d78efb08aae16299995c29 source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_trace_invalid_direction_returns_error(tools: TrieTools)`

Assert that `trace` with an unrecognised `direction` returns an `invalid_argument` error dict.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_trace_unknown_qname_returns_not_found fingerprint=4a972421a152c7b560db28c9f942d12a1917d194cc1acb5041774f2b39f1b89d body_fp=ab680909520a42548b3c41fac9d4e80c24a6b28e23d9c691c35b357b94db0c56 source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_trace_unknown_qname_returns_not_found(tools: TrieTools)`

Assert that `trace` returns a `not_found` error for an unrecognised qname.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_trace_depth_zero_returns_only_root fingerprint=76be5ecaba8cb2a295a796f304e77c718a9dcc8d23868995efa57a5182d2a1c2 body_fp=a4b8ce06db00f8a4bb692ac09198e4db99d9e6941e30384985978db8a09755b4 source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_trace_depth_zero_returns_only_root(tools: TrieTools)`

Assert that `trace` with `depth=0` returns only the root node and no edges.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_trace_depth_clamp_adds_note fingerprint=c455960b8dcfb8693c4e826945685a9217238b8705ee7806c1ca182dccf62c13 body_fp=2d992cf64b4fa107d6623a22849b59bb26c379f3f6a2e71c3c7e63f9cfb1ede7 source_ref=7e4137c7ffe5d4956c376bb1b09455ea1b946bb8 -->
## `test_trace_depth_clamp_adds_note(tools: TrieTools)`

Assert that requesting a depth exceeding `trace_max_depth` clamps the value and adds a "clamped" note to the response.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_grep_empty_predicate_returns_invalid_argument fingerprint=b276ee91748c22279c9a40988da4c4daaebfea8382927b5fe18d9f2f3c5b17ce body_fp=df6315d579f0a0e35b62b1eff063fbbac8b5d5fcccd804fdc7e9c221f34cf9a8 source_ref=b8a4bd60079a901c70ffa0704165e5211e078db6 -->
## `test_grep_empty_predicate_returns_invalid_argument(tools: TrieTools)`

Assert that empty or vacuous predicates return `invalid_argument` with a usable suggestion.

- Tested predicates: `None`, `{}`, `{"name_contains": ""}`, `{"kind": "any"}`.
- `suggestion` must contain `name_contains` or `scope_prefix`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_grep_empty_predicate_rejected_regardless_of_rank_by fingerprint=173c7d0e853ec0b26f7e6b2344e5c2c4c42c2b1245b1081fca21ec158813dd8d body_fp=825a090118a0b9bd6a12a1b3b21781d800556618991a2b370a83f250cd5ba9fe source_ref=b8a4bd60079a901c70ffa0704165e5211e078db6 -->
## `test_grep_empty_predicate_rejected_regardless_of_rank_by(tools: TrieTools)`

Assert that passing `rank_by` with an empty predicate still returns an `invalid_argument` error.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:PROJECT_TOML fingerprint=3f524fd58415aac9f548f19d4ad2554a2e411c44f7f8907ce1944fa2fa35a62e body_fp=0fca1d1a44f070a166493e00a2cf8698940a81923dbceeefdd59d6f53aa4a88c source_ref=c0685fb01624558013187827bb8d7c3fdadd8390 -->
## `PROJECT_TOML: str`

TOML configuration string used to initialise temporary test projects.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_grep_accepts_constant_and_module_kinds fingerprint=a7b0b5f6a91e85c5d7b2effde7c148be97b61ecfd7966d405518b3d26526bbed body_fp=2606698b8197b753667ca45c11843528f662a183c1817b3a6b809d3670504dc1 source_ref=c0685fb01624558013187827bb8d7c3fdadd8390 -->
## `test_grep_accepts_constant_and_module_kinds(tools: TrieTools)`

Assert that `grep` accepts `"constant"` and `"module"` as valid `kind` values without returning an `invalid_argument` error.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=fed67e9c87a965329571043d05996d114615d6b7be22cf5542b2f549fbf6a047 source_ref=c0685fb01624558013187827bb8d7c3fdadd8390 -->
## `tests/test_mcp`

Tests for the MCP tool surface (`grep`, `read`, `trace`) exercised via `TrieTools` directly.

- `FakeClient`: stub model client returning fixed text and token counts
- `project`: tmp dir fixture with `trie.toml`, `lib.py`, `app.py`
- `populated_project`: extends `project` with scan + sync so tools have data
- `tools`: yields a `TrieTools` instance over `populated_project`, closes on teardown
<!-- trie:end -->