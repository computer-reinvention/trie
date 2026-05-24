---
trie_version: 0.1.2
source: tests/test_cli_agent_commands.py
file_fingerprint: c8b0fe3d831eba8a48b9e521c6ccf3fcadf924d81628bd3b9d09aff196a67fd9
last_synced_at: '2026-05-23T23:45:19Z'
description: 'Tests for the agent-facing CLI subcommands: `trie grep`, `trie read`,
  `trie trace`.'
defines:
- kind: module
  qualified_name: tests/test_cli_agent_commands:__module__
  lines: 1-488
- kind: constant
  qualified_name: tests/test_cli_agent_commands:PROJECT_TOML
  lines: 32-39
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
- kind: function
  qualified_name: tests/test_cli_agent_commands:_read_jsonl_events
  lines: 399-405
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_grep_emits_cli_call_event_not_mcp_call
  lines: 408-434
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_read_and_trace_also_emit_cli_call_events
  lines: 437-461
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_cli_call_event_carries_duration_and_result_fields
  lines: 464-487
incoming_refs: 0
outgoing_refs: 26
---
<!-- trie:section symbol=tests/test_cli_agent_commands:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=66f04576c3a67474b50e6d0f5c37020c298d61571c056d3aa695f1c00042b341 source_ref=aceb4b04b98c59585615632c08ce045a85c337dc -->
## `tests/test_cli_agent_commands`

Integration tests for the agent-facing CLI subcommands `trie grep`, `trie read`, and `trie trace`.

- Verifies `--json` output is structurally equivalent to MCP tool envelopes.
- Covers exit codes: 0 (success), 1 (tool error / missing config), 2 (bad CLI input).
- Asserts CLI invocations emit `cli_call` telemetry events, never `mcp_call`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:PROJECT_TOML fingerprint=e9c7735b60c9b4e2a539d27c21376b8f0df51a16c1349855a9eec287b1183875 body_fp=d1d45a91d6cf78fc5da0e1233fcc418ecf7bc97b8b3859a16e0fdc22b2009241 source_ref=aceb4b04b98c59585615632c08ce045a85c337dc -->
## `PROJECT_TOML: str`

TOML string used to create `trie.toml` in test fixtures.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:FakeClient fingerprint=57cb0d9af6bb40fa692b1e07a745ebc033aa599c53105b31098873c4ee475f36 body_fp=c82a331b4b3964278d9f27969162752c22e8780c6549f01fb2806f4c1f83f226 source_ref=aceb4b04b98c59585615632c08ce045a85c337dc -->
## `FakeClient`

Stub AI client for tests; returns a fixed `body` string from `generate` and a constant token count from `count_tokens`.

- `body`: the Markdown text returned as `GenerationResponse.text`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:FakeClient.generate fingerprint=a28c91031810d416f079e2d7a57f5ed7651bd8c3315cf78d1ec869c3b812915e body_fp=d60ebc8693003167dacec6df491f967b98de2b104dd4b791a0167f7d78c093f2 source_ref=aceb4b04b98c59585615632c08ce045a85c337dc -->
## `FakeClient.generate(self, _req: GenerationRequest) -> GenerationResponse`

Return a hardcoded `GenerationResponse` using `FakeClient.body` as the generated text.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=77d3b6347ca7e880748f4deac8ccf865d4c9661ed1e5f1c6dd3979573067d702 source_ref=aceb4b04b98c59585615632c08ce045a85c337dc -->
## `FakeClient.count_tokens(self, _req: GenerationRequest) -> int`

Always return 100 from `FakeClient` without calling a real model.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:populated_project fingerprint=b5db4105294b249e057601fb6357b88650bc0c7a1b1d3573458f847b457673dc body_fp=251d66bf231a0b0cb0f6e533529cfec3db8aa88f1ca286a8825383359f039209 source_ref=aceb4b04b98c59585615632c08ce045a85c337dc -->
## `populated_project(tmp_path: Path) -> Path`

Create a temporary project with `lib.py` and `app.py` scanned, synced, and stored in a graph database.

- Returns `tmp_path` with `trie.toml`, source files, and a populated `.trie/graph.db`.
- `lib:slugify` and `app:make_url` are both synced with `FakeClient`-generated triefacts.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_with_name_returns_human_readable_table fingerprint=ceec71ef4ae8ab9dc6b463b4e086f20ff34717425879326053e4192406f8d74e body_fp=16e3787524516fc27aa290d498b207b91128682aff3abd834afa27b49795c0e3 source_ref=aceb4b04b98c59585615632c08ce045a85c337dc -->
## `test_grep_with_name_returns_human_readable_table(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie grep --name slugify` without `--json` renders a Rich table containing the qname and one-liner.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_with_json_is_byte_equivalent_to_mcp_envelope fingerprint=fd27bdb9ab6125b23dd77bd49513fbb7a7494243f50e9bafa33ccd3b581547f9 body_fp=34963d40d3a65b91703eef6a292c814df12fce6376422e15f5d3464c53d92a67 source_ref=aceb4b04b98c59585615632c08ce045a85c337dc -->
## `test_grep_with_json_is_byte_equivalent_to_mcp_envelope(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie grep --json` returns a `hits` envelope with the same fields an MCP `grep` call would produce.

- Checks for `qname`, `signature`, `file_pointer`, `one_liner`, `is_public`, `kind`, `inbound_count`, `outbound_count` on every hit.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_predicate_json_overrides_via_flags fingerprint=79c5d2628d08dc80b9bd6eb493e147c9e85e1e70332ab1a09244ca9062a5c569 body_fp=4e9f5d1e6ac268f2e0db2c8ad0e41d8dba11586ae6e5269796f6389d8adf0462 source_ref=aceb4b04b98c59585615632c08ce045a85c337dc -->
## `test_grep_predicate_json_overrides_via_flags(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify that `--predicate` JSON and individual flag filters compose correctly on `trie grep`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_invalid_predicate_json_exits_2 fingerprint=759099aaa7ff8a970783fe1c5d39d184b5690d06e8512053c3f5251cbb4f40dc body_fp=ebcbc32b3470077b6ee095d7d9477d60fca38ed555ea25e94a2ebc6cd3e11df0 source_ref=aceb4b04b98c59585615632c08ce045a85c337dc -->
## `test_grep_invalid_predicate_json_exits_2(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that malformed JSON passed to `--predicate` exits with code 2, distinct from tool-side errors (exit 1).
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_no_matches_shows_fallback_envelope fingerprint=60206eb0f994a8b178b3bc8ee290427d7110a4c3e7d5e67b1d20a0ac53b47f1f body_fp=4270dc432feaacef00294c1a99c12687079916075a10d1637e53d1b5bb0d2759 source_ref=aceb4b04b98c59585615632c08ce045a85c337dc -->
## `test_grep_no_matches_shows_fallback_envelope(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie grep --name` with no symbol matches exits 0 and renders a `text_match_empty` fallback envelope.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_with_no_flags_exits_with_invalid_argument fingerprint=1fa4926a1140b7863c3c9783481b4a3b5b1de3c07e6319aa0d30e0206993e799 body_fp=878bd6e3fc52dcad53ceb1c607f4891d5f3021c6e7f52e87a745988bafcf71c9 source_ref=aceb4b04b98c59585615632c08ce045a85c337dc -->
## `test_grep_with_no_flags_exits_with_invalid_argument(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie grep` with no filter flags exits 1 with an `invalid_argument` envelope naming usable filters.

- `exit_code == 1`: tool-level error, not CLI usage error (which would be 2).
- Output must contain `name_contains` or `scope_prefix` as a next-step hint.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_text_match_fallback_renders_candidates fingerprint=87da0a6f67a8bf9736cf56bc6cbc7184e64472382cc2c34902fb6e2210fbc308 body_fp=d62526728d0fab8492ef5954b1853667880b1507096a051a16a65a20ab1d0ff1 source_ref=aceb4b04b98c59585615632c08ce045a85c337dc -->
## `test_grep_text_match_fallback_renders_candidates(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie grep --name` with a body-only match triggers the text-match fallback and renders candidate symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_read_known_qname_prints_prose_and_neighbours fingerprint=86adc7ba3e51042f0d573c5335c91041c1831526afd830ae2258a43c4edaa71f body_fp=73c95ec4a9815e8a2bf411355e026f11b7de5959338a8dc2c6ae61c54e6a0cca source_ref=aceb4b04b98c59585615632c08ce045a85c337dc -->
## `test_read_known_qname_prints_prose_and_neighbours(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie read lib:slugify` outputs the qname, prose body, and caller `app:make_url`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_read_unknown_qname_exits_1_with_suggestion fingerprint=7cd18ff86b8641d73abf355721a190d506e7f8e5b284dca0ffe0a2555e6771a8 body_fp=c00992d128476bff20c990172147fb2128b346c357187b2875b8c4a2341955b8 source_ref=aceb4b04b98c59585615632c08ce045a85c337dc -->
## `test_read_unknown_qname_exits_1_with_suggestion(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie read` with an unknown qname exits 1 and prints a corrective suggestion.

- Invokes `read lib:slugfy` (deliberate typo of `lib:slugify`).
- Expects `not_found` in output and either the close match or `grep(` hint.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_read_json_emits_envelope fingerprint=25b624dddcbc27e4aebdc236a8ff3844594190666ad1c86eea4ca9f7319e473a body_fp=833d7068af60fc729b084d90088f5e343522a601d558dcb0cf3cd9c17490f50c source_ref=aceb4b04b98c59585615632c08ce045a85c337dc -->
## `test_read_json_emits_envelope(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie read --json` emits a complete MCP `read` envelope with `qname`, `prose`, `callers`, and `callees`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_trace_callers_renders_topology fingerprint=e3024c73193838b4b73e014afc26d5406537704d7faa7650b922c10ffc3ed96d body_fp=130f96199a40da35d03a1fc97a4e6bb4122963357414593c670db825c770f234 source_ref=aceb4b04b98c59585615632c08ce045a85c337dc -->
## `test_trace_callers_renders_topology(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie trace --direction callers` human output includes the root symbol and its caller.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_trace_json_shape_matches_mcp fingerprint=37ba15dd22c955d0f2e08198cf147fa0b727373366b0aed681970b8fa0cb4f36 body_fp=6cbff11cbaf2a6c54a95295be54b0ff083fe08adb2123bd636694e08a2897246 source_ref=aceb4b04b98c59585615632c08ce045a85c337dc -->
## `test_trace_json_shape_matches_mcp(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie trace --json` emits the same `root`/`nodes`/`edges` envelope shape as the MCP `trace` tool.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_trace_unknown_qname_exits_1 fingerprint=41e7adebd8254e71dbd4a61e666624407824c5f8b731cbecbaa32d59745f66da body_fp=85e5f0071721b4c16b247fb8ef6567123a08960241e5102698b2ff243b0161e2 source_ref=aceb4b04b98c59585615632c08ce045a85c337dc -->
## `test_trace_unknown_qname_exits_1(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie trace` exits 1 with a `not_found` envelope when given an unknown qname.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_trace_invalid_direction_exits_1 fingerprint=9eba8f0d0997a6fc3413f24b13fb4ec96c6ce6098692e496d14968c5591b9406 body_fp=847dd1724bc3c1705769ced78cf14b520bd3d1034b61fc2f665fbd4a266d2005 source_ref=aceb4b04b98c59585615632c08ce045a85c337dc -->
## `test_trace_invalid_direction_exits_1(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that an unsupported `--direction` value produces an `invalid_argument` envelope with exit code 1.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_without_trie_toml_exits_1_with_clean_error fingerprint=7ae44aa39d88737da05fb452d0f77c60d500554b9e98acc9ac44df14b3285517 body_fp=9eef9f06c7fdfe09bc5df59687b9a28fd8d9235134ba1bc2fa06ebce04209178 source_ref=aceb4b04b98c59585615632c08ce045a85c337dc -->
## `test_grep_without_trie_toml_exits_1_with_clean_error(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert `trie grep` exits 1 with a clean `trie.toml` error when no config file exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_read_without_trie_toml_exits_1 fingerprint=c2e555d1c7bc5d2c145c9095f3da8575f9ca6d382c78e10517f32f8a9933b3a8 body_fp=7dd51bf86ca809cc8e81790a25de3e5bc76a3eb5e04bcabfca6ddbcdcbfc27c7 source_ref=aceb4b04b98c59585615632c08ce045a85c337dc -->
## `test_read_without_trie_toml_exits_1(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert `trie read` exits 1 with a `trie.toml` error message when no config file exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_trace_without_trie_toml_exits_1 fingerprint=e215ddf739c940699fec8f589a5a2d21ef060f7b7e362f9538939d1e6ed41c25 body_fp=7ed2439474bbab3af1f92f40704142bb1a1e9341bbc65047f331afa34438e17c source_ref=aceb4b04b98c59585615632c08ce045a85c337dc -->
## `test_trace_without_trie_toml_exits_1(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert `trie trace` exits 1 with a clean `trie.toml` error when no config file is present.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:_read_jsonl_events fingerprint=125817628eb1f7fc15e2a61035b6350edd8094f965da770e92e1a44a6c4c4177 body_fp=c021fbd1f1088f32254f92c016f5e0b901b1e57f4ad2c39e5776dcf8d7342fb1 source_ref=aceb4b04b98c59585615632c08ce045a85c337dc -->
## `_read_jsonl_events(path: Path) -> list[dict]`

Parse every non-empty line of a JSONL file into a list of dicts.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_emits_cli_call_event_not_mcp_call fingerprint=2c8f3798fc6d1622c87a523234e10d289743d7e2c64c7db1c89ffa8ffbb08344 body_fp=2a2ea040dd2e015537a92b0acebb48bc7ad2cb1c96739c962931b63412be8016 source_ref=aceb4b04b98c59585615632c08ce045a85c337dc -->
## `test_grep_emits_cli_call_event_not_mcp_call(populated_project: Path, monkeypatch: pytest.MonkeyPatch, tmp_path: Path)`

Assert that `trie grep` emits a `cli_call` telemetry event and never `mcp_call` or `mcp_server_start`.

- `TRIE_DEBUG`: set to a tmp JSONL path to capture telemetry for inspection.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_read_and_trace_also_emit_cli_call_events fingerprint=2555d2ce32fdcaeb3949422c08eb0431136ddb0de27b6d41f1efcb1ca0f16932 body_fp=be75e41bd752bccf8fd6290ce6efc873bb47a4466e7b8cb542070e22ecb9ac59 source_ref=aceb4b04b98c59585615632c08ce045a85c337dc -->
## `test_read_and_trace_also_emit_cli_call_events(populated_project: Path, monkeypatch: pytest.MonkeyPatch, tmp_path: Path)`

Assert that `trie read` and `trie trace` each emit a `cli_call` event and zero `mcp_call` events.

- `TRIE_DEBUG`: set to a tmp JSONL path to capture telemetry output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_cli_call_event_carries_duration_and_result_fields fingerprint=8bce6b8bf33876350ff2cc7019b5bf67715c081f34bf9c6124f2bf72d7f63572 body_fp=def8db32098596980a23419e6e1ed1eb4894cab67e07efd1ded8531c0e96a937 source_ref=aceb4b04b98c59585615632c08ce045a85c337dc -->
## `test_cli_call_event_carries_duration_and_result_fields(populated_project: Path, monkeypatch: pytest.MonkeyPatch, tmp_path: Path)`

Assert that a `cli_call` telemetry event from `trie grep` includes `duration_ms`, `result_kind`, `result_count`, and `response_bytes`.
<!-- trie:end -->