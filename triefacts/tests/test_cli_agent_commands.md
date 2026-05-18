---
trie_version: 0.1.0
source: tests/test_cli_agent_commands.py
file_fingerprint: f4c1ec49454e9b150600316f2dfa0b408465afb412a7320c7536823b88cbf7bc
last_synced_at: '2026-05-18T22:48:48Z'
description: 'Tests for the agent-facing CLI subcommands: `trie grep`, `trie read`,
  `trie trace`.'
defines:
- kind: class
  qualified_name: tests/test_cli_agent_commands:FakeClient
  lines: 43-57
- kind: method
  qualified_name: tests/test_cli_agent_commands:FakeClient.generate
  lines: 47-54
- kind: method
  qualified_name: tests/test_cli_agent_commands:FakeClient.count_tokens
  lines: 56-57
- kind: function
  qualified_name: tests/test_cli_agent_commands:populated_project
  lines: 61-93
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_grep_with_name_returns_human_readable_table
  lines: 101-113
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_grep_with_json_is_byte_equivalent_to_mcp_envelope
  lines: 116-145
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_grep_predicate_json_overrides_via_flags
  lines: 148-171
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_grep_invalid_predicate_json_exits_2
  lines: 174-184
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_grep_no_matches_shows_fallback_envelope
  lines: 187-199
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_grep_with_no_flags_exits_with_invalid_argument
  lines: 202-223
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_grep_text_match_fallback_renders_candidates
  lines: 226-238
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_read_known_qname_prints_prose_and_neighbours
  lines: 246-258
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_read_unknown_qname_exits_1_with_suggestion
  lines: 261-273
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_read_json_emits_envelope
  lines: 276-288
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_trace_callers_renders_topology
  lines: 296-308
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_trace_json_shape_matches_mcp
  lines: 311-333
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_trace_unknown_qname_exits_1
  lines: 336-343
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_trace_invalid_direction_exits_1
  lines: 346-355
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_grep_without_trie_toml_exits_1_with_clean_error
  lines: 363-373
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_read_without_trie_toml_exits_1
  lines: 376-382
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_trace_without_trie_toml_exits_1
  lines: 385-391
incoming_refs: 0
outgoing_refs: 6
---
<!-- trie:section symbol=tests/test_cli_agent_commands:FakeClient fingerprint=57cb0d9af6bb40fa692b1e07a745ebc033aa599c53105b31098873c4ee475f36 body_fp=c586a59ff7ac1ee8d6255eeefe8ff7ccdcca1e084ce42536bb2d25440373ab3f source_ref=8f2353097fd37581bdc7a99a316a16fdca4ea9e8 -->
## `FakeClient(model_id: str = "fake/test", body: str = "## generated\n\nGenerated description.\n")`

Stub LLM client returning fixed text for use in fixture-level sync calls.

- `body`: the exact Markdown string returned by every `generate` call.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cli_agent_commands:FakeClient.generate fingerprint=a28c91031810d416f079e2d7a57f5ed7651bd8c3315cf78d1ec869c3b812915e body_fp=30ce9124ebb65e6f596b9729b0e56e75c16b28875fd59126d557d9d63703e744 source_ref=8f2353097fd37581bdc7a99a316a16fdca4ea9e8 -->
## `FakeClient.generate(self, _req: GenerationRequest) -> GenerationResponse`

Return a hardcoded `GenerationResponse` with `self.body` as text, ignoring the request.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cli_agent_commands:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=0cc8e4c60852ed2343ba12efc7686b2f040b2c6b012d45e134249772b72c93f1 source_ref=8f2353097fd37581bdc7a99a316a16fdca4ea9e8 -->
## `count_tokens(self, _req: GenerationRequest) -> int`

Return a fixed token count of 100 for any request.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cli_agent_commands:populated_project fingerprint=b5db4105294b249e057601fb6357b88650bc0c7a1b1d3573458f847b457673dc body_fp=aba0c8e72c7597e02883a67d7d841c8906b9aaaaa2f73c3ed93ca3d502d386e4 source_ref=8f2353097fd37581bdc7a99a316a16fdca4ea9e8 -->
## `populated_project(tmp_path: Path) -> Path`

Build a two-file project with scanned graph and synced triefacts under `tmp_path`.

- Returns `tmp_path` after writing `trie.toml`, `lib.py`, `app.py`, scanning, and syncing both files with `FakeClient`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_with_name_returns_human_readable_table fingerprint=ceec71ef4ae8ab9dc6b463b4e086f20ff34717425879326053e4192406f8d74e body_fp=c385faa85f974f7cb825f07ab99dc24b4464d28ba814c810e1f660f910ac9583 source_ref=8f2353097fd37581bdc7a99a316a16fdca4ea9e8 -->
## `test_grep_with_name_returns_human_readable_table(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie grep --name slugify` without `--json` renders a Rich table containing the symbol's qname and one-liner.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_with_json_is_byte_equivalent_to_mcp_envelope fingerprint=fd27bdb9ab6125b23dd77bd49513fbb7a7494243f50e9bafa33ccd3b581547f9 body_fp=e4f00206844e13d7a90346ee72ec7de8e5c807a54135a72313f5f7e428ac1131 source_ref=8f2353097fd37581bdc7a99a316a16fdca4ea9e8 -->
## `test_grep_with_json_is_byte_equivalent_to_mcp_envelope(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie grep --json` produces a structurally valid MCP `grep` envelope with the expected hit fields.

- `populated_project`: fixture providing a synced two-file project at a temp path.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_predicate_json_overrides_via_flags fingerprint=79c5d2628d08dc80b9bd6eb493e147c9e85e1e70332ab1a09244ca9062a5c569 body_fp=a6d88944629f32460dfba392a85bfcb8d69d6169c7f2fe0252031085b4ae3f34 source_ref=8f2353097fd37581bdc7a99a316a16fdca4ea9e8 -->
## `test_grep_predicate_json_overrides_via_flags(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify that `--predicate` JSON and additional CLI flags combine correctly to filter grep results.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_invalid_predicate_json_exits_2 fingerprint=759099aaa7ff8a970783fe1c5d39d184b5690d06e8512053c3f5251cbb4f40dc body_fp=56898061764a4153c5a1c4e3a6cccc172a189dfd21525c32a414b941fb411a14 source_ref=8f2353097fd37581bdc7a99a316a16fdca4ea9e8 -->
## `test_grep_invalid_predicate_json_exits_2(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that malformed JSON in `--predicate` exits with code 2 and emits "not valid JSON".
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_no_matches_shows_fallback_envelope fingerprint=60206eb0f994a8b178b3bc8ee290427d7110a4c3e7d5e67b1d20a0ac53b47f1f body_fp=0052f4add81197bc79708d2ed848b28558bf33e6b2abbc5dd675ec67605b9007 source_ref=8f2353097fd37581bdc7a99a316a16fdca4ea9e8 -->
## `test_grep_no_matches_shows_fallback_envelope(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie grep --name` with no matching symbol exits 0 and renders a `text_match_empty` fallback envelope.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_text_match_fallback_renders_candidates fingerprint=87da0a6f67a8bf9736cf56bc6cbc7184e64472382cc2c34902fb6e2210fbc308 body_fp=44eba6e9e134855d387ebaa782c5afc93cf37b99cb6ce28ff70d21c636ddc17a source_ref=8f2353097fd37581bdc7a99a316a16fdca4ea9e8 -->
## `test_grep_text_match_fallback_renders_candidates(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie grep --name <text>` renders a candidate table when the query matches a symbol's body but not its name.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cli_agent_commands:test_read_known_qname_prints_prose_and_neighbours fingerprint=86adc7ba3e51042f0d573c5335c91041c1831526afd830ae2258a43c4edaa71f body_fp=f6f734a01a0463edf246222d8708bcbe40dfcb3d7e72e398e779f5c7b838d042 source_ref=8f2353097fd37581bdc7a99a316a16fdca4ea9e8 -->
## `test_read_known_qname_prints_prose_and_neighbours(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie read <qname>` outputs the symbol's prose body and its caller's qname.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cli_agent_commands:test_read_unknown_qname_exits_1_with_suggestion fingerprint=7cd18ff86b8641d73abf355721a190d506e7f8e5b284dca0ffe0a2555e6771a8 body_fp=d899feb012df757d04aec456de1fb5d743fb94989c662cede82c7e1738ef1614 source_ref=8f2353097fd37581bdc7a99a316a16fdca4ea9e8 -->
## `test_read_unknown_qname_exits_1_with_suggestion(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie read` with a misspelled qname exits 1 and prints the MCP envelope's suggestion.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cli_agent_commands:test_read_json_emits_envelope fingerprint=25b624dddcbc27e4aebdc236a8ff3844594190666ad1c86eea4ca9f7319e473a body_fp=c66923a611142dd4d8d6cd391795cb8817a5c34e2e368a659edc218ab517d309 source_ref=8f2353097fd37581bdc7a99a316a16fdca4ea9e8 -->
## `test_read_json_emits_envelope(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie read <qname> --json` emits a structured MCP-equivalent envelope with `qname`, `prose`, `callers`, and `callees`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cli_agent_commands:test_trace_callers_renders_topology fingerprint=e3024c73193838b4b73e014afc26d5406537704d7faa7650b922c10ffc3ed96d body_fp=a11b18fbe8f0c3c77f3d99706371411dd82b8989ff5fbac7446f88e13add787e source_ref=8f2353097fd37581bdc7a99a316a16fdca4ea9e8 -->
## `test_trace_callers_renders_topology(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie trace --direction callers` renders the root symbol and its callers in human-readable output.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cli_agent_commands:test_trace_json_shape_matches_mcp fingerprint=37ba15dd22c955d0f2e08198cf147fa0b727373366b0aed681970b8fa0cb4f36 body_fp=12ef7e048fd62830b6dc749ba953c502b85317595b17c9a50f99b44410499d4c source_ref=8f2353097fd37581bdc7a99a316a16fdca4ea9e8 -->
## `test_trace_json_shape_matches_mcp(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie trace --json` emits a root/nodes/edges envelope identical in shape to the MCP `trace` tool.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cli_agent_commands:test_trace_unknown_qname_exits_1 fingerprint=41e7adebd8254e71dbd4a61e666624407824c5f8b731cbecbaa32d59745f66da body_fp=d120d344b5915f8654f36f0fb33a66d962347f8ab9f65f4736956bd6e1fbd736 source_ref=8f2353097fd37581bdc7a99a316a16fdca4ea9e8 -->
## `test_trace_unknown_qname_exits_1(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie trace` exits 1 with a `not_found` error when given an unrecognised qname.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cli_agent_commands:test_trace_invalid_direction_exits_1 fingerprint=9eba8f0d0997a6fc3413f24b13fb4ec96c6ce6098692e496d14968c5591b9406 body_fp=8fa22ed85556ce0620746c4ecb277f16ae11934c390b2bed6d798e8ff01335cf source_ref=8f2353097fd37581bdc7a99a316a16fdca4ea9e8 -->
## `test_trace_invalid_direction_exits_1(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that an unsupported `--direction` value produces an `invalid_argument` envelope and exits 1.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_without_trie_toml_exits_1_with_clean_error fingerprint=7ae44aa39d88737da05fb452d0f77c60d500554b9e98acc9ac44df14b3285517 body_fp=0c5e3d8537bc6af3b1bb6a34b29fbfc72a40120c0c65c09075d8bb08a7502a63 source_ref=8f2353097fd37581bdc7a99a316a16fdca4ea9e8 -->
## `test_grep_without_trie_toml_exits_1_with_clean_error(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie grep` exits 1 with a clean `trie.toml` error when no config file exists.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cli_agent_commands:test_read_without_trie_toml_exits_1 fingerprint=c2e555d1c7bc5d2c145c9095f3da8575f9ca6d382c78e10517f32f8a9933b3a8 body_fp=6881305aad6a1c9067f00c872d40410f2d827553f196dafbf7a3c279814798df source_ref=8f2353097fd37581bdc7a99a316a16fdca4ea9e8 -->
## `test_read_without_trie_toml_exits_1(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert `trie read` exits 1 with a `trie.toml` message when no config file exists.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cli_agent_commands:test_trace_without_trie_toml_exits_1 fingerprint=e215ddf739c940699fec8f589a5a2d21ef060f7b7e362f9538939d1e6ed41c25 body_fp=9e5eb64757d03a1dc994b0078bcd4572d57f743f5b6f7c2a0f4e4453be06b117 source_ref=8f2353097fd37581bdc7a99a316a16fdca4ea9e8 -->
## `test_trace_without_trie_toml_exits_1(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert `trie trace` exits 1 with a `trie.toml` message when no config file exists.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_with_no_flags_exits_with_invalid_argument fingerprint=1fa4926a1140b7863c3c9783481b4a3b5b1de3c07e6319aa0d30e0206993e799 body_fp=a1198db29d0848e8cf532be35e954140d244d857f58c76b375cf78ad0e266f7f source_ref=3adab019d9e144c5db17f26244278c46468d7a08 -->
## `test_grep_with_no_flags_exits_with_invalid_argument(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie grep` with no filter flags exits 1 with an `invalid_argument` envelope naming a usable filter.

- Exit code 1 signals a tool error, not a CLI usage error (exit 2).
- Output must contain `name_contains` or `scope_prefix` as a hint.
<!-- trie:end -->