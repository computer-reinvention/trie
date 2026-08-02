---
trie_version: 0.3.0
source: tests/test_cli_agent_commands.py
file_fingerprint: fef25557f7b280380a6b5ea4ab80ed6f418425db203edaa4c82f85fdd674b811
last_synced_at: '2026-06-06T13:15:48Z'
description: 'Tests for the agent-facing CLI subcommands: `trie grep`, `trie read`, `trie trace`.'
defines:
- kind: module
  qualified_name: tests/test_cli_agent_commands:__module__
  lines: 1-576
- kind: constant
  qualified_name: tests/test_cli_agent_commands:PROJECT_TOML
  lines: 31-39
- kind: function
  qualified_name: tests/test_cli_agent_commands:populated_project
  lines: 43-79
  signature: 'def populated_project(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_grep_with_name_returns_human_readable_table
  lines: 87-99
  signature: 'def test_grep_with_name_returns_human_readable_table( populated_project: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_grep_with_json_is_byte_equivalent_to_mcp_envelope
  lines: 102-131
  signature: 'def test_grep_with_json_is_byte_equivalent_to_mcp_envelope( populated_project: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_grep_predicate_json_overrides_via_flags
  lines: 134-157
  signature: 'def test_grep_predicate_json_overrides_via_flags( populated_project: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_grep_invalid_predicate_json_exits_2
  lines: 160-170
  signature: 'def test_grep_invalid_predicate_json_exits_2( populated_project: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_grep_no_matches_shows_fallback_envelope
  lines: 173-185
  signature: 'def test_grep_no_matches_shows_fallback_envelope( populated_project: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_grep_with_no_flags_exits_with_invalid_argument
  lines: 188-209
  signature: 'def test_grep_with_no_flags_exits_with_invalid_argument( populated_project: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_grep_text_match_fallback_renders_candidates
  lines: 212-224
  signature: 'def test_grep_text_match_fallback_renders_candidates( populated_project: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_read_known_qname_prints_prose_and_neighbours
  lines: 232-244
  signature: 'def test_read_known_qname_prints_prose_and_neighbours( populated_project: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_read_unknown_qname_exits_1_with_suggestion
  lines: 247-259
  signature: 'def test_read_unknown_qname_exits_1_with_suggestion( populated_project: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_read_json_emits_envelope
  lines: 262-274
  signature: 'def test_read_json_emits_envelope(populated_project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_trace_callers_renders_topology
  lines: 282-294
  signature: 'def test_trace_callers_renders_topology(populated_project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_trace_json_shape_matches_mcp
  lines: 297-319
  signature: 'def test_trace_json_shape_matches_mcp(populated_project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_trace_unknown_qname_exits_1
  lines: 322-329
  signature: 'def test_trace_unknown_qname_exits_1(populated_project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_trace_invalid_direction_exits_1
  lines: 332-341
  signature: 'def test_trace_invalid_direction_exits_1(populated_project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_grep_without_trie_toml_exits_1_with_clean_error
  lines: 349-359
  signature: 'def test_grep_without_trie_toml_exits_1_with_clean_error( tmp_path: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_read_without_trie_toml_exits_1
  lines: 362-368
  signature: 'def test_read_without_trie_toml_exits_1(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_trace_without_trie_toml_exits_1
  lines: 371-377
  signature: 'def test_trace_without_trie_toml_exits_1(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_cli_agent_commands:_read_jsonl_events
  lines: 385-391
  signature: 'def _read_jsonl_events(path: Path) -> list[dict]'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_grep_emits_cli_call_event_not_mcp_call
  lines: 394-420
  signature: 'def test_grep_emits_cli_call_event_not_mcp_call( populated_project: Path, monkeypatch: pytest.MonkeyPatch, tmp_path: Path )'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_read_and_trace_also_emit_cli_call_events
  lines: 423-447
  signature: 'def test_read_and_trace_also_emit_cli_call_events( populated_project: Path, monkeypatch: pytest.MonkeyPatch, tmp_path: Path )'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_cli_call_event_carries_duration_and_result_fields
  lines: 450-473
  signature: 'def test_cli_call_event_carries_duration_and_result_fields( populated_project: Path, monkeypatch: pytest.MonkeyPatch, tmp_path: Path )'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_patch_list_empty
  lines: 479-484
  signature: 'def test_patch_list_empty(populated_project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_patch_create_and_list
  lines: 487-500
  signature: 'def test_patch_create_and_list(populated_project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_patch_create_unknown_symbol
  lines: 503-508
  signature: 'def test_patch_create_unknown_symbol(populated_project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_patch_preview
  lines: 511-520
  signature: 'def test_patch_preview(populated_project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_patch_preview_empty
  lines: 523-528
  signature: 'def test_patch_preview_empty(populated_project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_patch_drop_by_qname
  lines: 531-543
  signature: 'def test_patch_drop_by_qname(populated_project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_patch_drop_all
  lines: 546-555
  signature: 'def test_patch_drop_all(populated_project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_patch_drop_no_args
  lines: 558-563
  signature: 'def test_patch_drop_no_args(populated_project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_patch_help
  lines: 566-575
  signature: 'def test_patch_help(populated_project: Path, monkeypatch: pytest.MonkeyPatch)'
incoming_refs: 0
outgoing_refs: 35
---
<!-- trie:section symbol=tests/test_cli_agent_commands:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=9074e81e653a51caec1cddc98d63f2cb531b27dd95cca0cc10099d5d101999cd source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
Tests for agent-facing CLI commands (`trie grep`, `trie read`, `trie trace`) that mirror MCP tool surface.

- Verifies `--json` output byte-equivalent to MCP server responses
- Confirms default output renders human-readable Rich formatting
- Tests error handling: exit code 1 for tool errors, exit code 2 for predicate-parse errors
- Validates telemetry emits `cli_call` events (not `mcp_call`) for audit trail distinction
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:PROJECT_TOML fingerprint=ea44d5615a2611cc14e40b5b84f8141a4679269bc80e3914e4fef0417f24d38b body_fp=ebe8f69b29597eb802710c17ab446209bc2324556c54e813fb8f9df82761aa0d source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
TOML configuration string used by test fixtures to create a minimal trie project setup.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:populated_project fingerprint=90e67f6eefd8a9cde4344dfea79f23fc3bf21395b4fa03572516d408a220e7b4 body_fp=5ff5fcfeb7f5fdc7e5e0dcd94e096c4274b56e9dbd9269e7da5fa6724a6188cb source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def populated_project(tmp_path: Path) -> Path`

Creates a temporary project with `lib.py` and `app.py` files, scans them into the graph, and syncs triefacts using fake LLM responses.

- Returns the temporary project root directory with complete graph database
- Sets up `trie.toml` configuration and two Python modules with import relationship
- Uses `FakeTrieClient` to simulate triefact generation for both files
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_with_name_returns_human_readable_table fingerprint=ceec71ef4ae8ab9dc6b463b4e086f20ff34717425879326053e4192406f8d74e body_fp=21d243e450993c76e722c9018b310542fb468247e82e608091df2a13b3db174f source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def test_grep_with_name_returns_human_readable_table( populated_project: Path, monkeypatch: pytest.MonkeyPatch )`

Verifies `trie grep --name` outputs a human-readable Rich table containing the matching symbol's qname and one-liner description.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_with_json_is_byte_equivalent_to_mcp_envelope fingerprint=fd27bdb9ab6125b23dd77bd49513fbb7a7494243f50e9bafa33ccd3b581547f9 body_fp=a475af529cdb5af929c2fe96605a0fc1e205a7ac4c70a27a95af973e5caf80ca source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def test_grep_with_json_is_byte_equivalent_to_mcp_envelope( populated_project: Path, monkeypatch: pytest.MonkeyPatch )`

Verifies `trie grep --json` outputs the same MCP envelope structure as the wire protocol.

- Uses structural assertions on JSON shape rather than byte-for-byte comparison to avoid timestamp brittleness
- Confirms presence of required MCP envelope fields: qname, signature, file_pointer, one_liner, is_public, kind, inbound_count, outbound_count
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_predicate_json_overrides_via_flags fingerprint=79c5d2628d08dc80b9bd6eb493e147c9e85e1e70332ab1a09244ca9062a5c569 body_fp=90e03b23dd12186bb0b1e893e3f5149473cea89f460748b73a86897ddea3b0f3 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def test_grep_predicate_json_overrides_via_flags( populated_project: Path, monkeypatch: pytest.MonkeyPatch )`

Tests that `--predicate` JSON is layered with command-line flags for agent workflow compatibility.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_invalid_predicate_json_exits_2 fingerprint=759099aaa7ff8a970783fe1c5d39d184b5690d06e8512053c3f5251cbb4f40dc body_fp=27a05d125aa620de4425c7853f6d5311abfbce8d7bfcacb11ad045a7461ef090 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def test_grep_invalid_predicate_json_exits_2( populated_project: Path, monkeypatch: pytest.MonkeyPatch )`

Verifies that malformed JSON in `--predicate` flag exits with code 2 to distinguish usage errors from tool errors.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_no_matches_shows_fallback_envelope fingerprint=60206eb0f994a8b178b3bc8ee290427d7110a4c3e7d5e67b1d20a0ac53b47f1f body_fp=bca43f7dc290c7a4fe6093d2b518217a0f42625de97a4c7172e93cc423628d8d source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def test_grep_no_matches_shows_fallback_envelope( populated_project: Path, monkeypatch: pytest.MonkeyPatch )`

Tests that `trie grep` with no symbol matches returns a fallback envelope explaining the empty result.

- Verifies exit code 0 (empty results are not errors)
- Checks output contains "text_match_empty" indicating fallback behavior
- Ensures human-readable output explains why no hits were found
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_with_no_flags_exits_with_invalid_argument fingerprint=1fa4926a1140b7863c3c9783481b4a3b5b1de3c07e6319aa0d30e0206993e799 body_fp=2619ed4ffa380b85b28e624475bb61f71301a296c202d87e4db2c413163899d8 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def test_grep_with_no_flags_exits_with_invalid_argument( populated_project: Path, monkeypatch: pytest.MonkeyPatch )`

Verifies that `trie grep` with no filter flags exits 1 with an `invalid_argument` error and usage suggestions.

- Prevents the "noisy empty grep" footgun by rejecting empty predicates
- Exit code 1 indicates tool-level error (vs exit code 2 for CLI usage errors)
- Output must contain suggested filters like `name_contains` or `scope_prefix`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_text_match_fallback_renders_candidates fingerprint=87da0a6f67a8bf9736cf56bc6cbc7184e64472382cc2c34902fb6e2210fbc308 body_fp=47c84429a870ed307fae6aa4ab9ea5ceb8b0029d8bb17f907fc3ae445af6804f source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def test_grep_text_match_fallback_renders_candidates( populated_project: Path, monkeypatch: pytest.MonkeyPatch )`

Tests that `trie grep` renders candidate symbols when search text appears in symbol bodies but not names.

- Searches for "replace" which exists in lib:slugify's body content
- Verifies fallback text_match behavior surfaces candidate symbols in output
- Ensures lib:slugify appears as a candidate despite name mismatch
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_read_known_qname_prints_prose_and_neighbours fingerprint=86adc7ba3e51042f0d573c5335c91041c1831526afd830ae2258a43c4edaa71f body_fp=89120a40ff2db7b121360d020126c7e3fa7db484ce4b369c87235c0751eda13d source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def test_read_known_qname_prints_prose_and_neighbours( populated_project: Path, monkeypatch: pytest.MonkeyPatch )`

Verifies `trie read` command outputs symbol prose body and caller/callee summaries in human-readable format.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_read_unknown_qname_exits_1_with_suggestion fingerprint=7cd18ff86b8641d73abf355721a190d506e7f8e5b284dca0ffe0a2555e6771a8 body_fp=10b3e730c2ef35f4c032868c143ee2707e64d18c4da64285d32ade513dbcd5a0 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def test_read_unknown_qname_exits_1_with_suggestion( populated_project: Path, monkeypatch: pytest.MonkeyPatch )`

Verifies that `trie read` with a typo in the qname exits with code 1 and includes helpful suggestions in the output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_read_json_emits_envelope fingerprint=25b624dddcbc27e4aebdc236a8ff3844594190666ad1c86eea4ca9f7319e473a body_fp=ade4700e05ea39dce3f2a79baf48978a6844eaae22cd6628480327d196daafb9 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def test_read_json_emits_envelope(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Verifies that `trie read --json` outputs the same MCP envelope structure as the wire protocol.

- Asserts parsed JSON contains `qname`, `prose`, `callers`, and `callees` fields
- Validates that caller qnames include expected symbols from the test project
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_trace_callers_renders_topology fingerprint=e3024c73193838b4b73e014afc26d5406537704d7faa7650b922c10ffc3ed96d body_fp=b29094fea4d314014ab1921f5f3ef42eb14148b0e18f27b2c222f4e6369cca66 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def test_trace_callers_renders_topology(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Tests that `trie trace` with callers direction produces human-readable topology output showing root, nodes, and directed edges with clear arrow indicators.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_trace_json_shape_matches_mcp fingerprint=37ba15dd22c955d0f2e08198cf147fa0b727373366b0aed681970b8fa0cb4f36 body_fp=fbef7eace08e39c01f4d05616b3ee8c8dd3278109ce0b371a0f47612f1bad753 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def test_trace_json_shape_matches_mcp(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Verifies `trie trace --json` output has the same root/nodes/edges structure as MCP trace tool responses.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_trace_unknown_qname_exits_1 fingerprint=41e7adebd8254e71dbd4a61e666624407824c5f8b731cbecbaa32d59745f66da body_fp=bce210742fb8ccdaa9e93634dbc5f996f964e60604e7902e2eeb5ad3e1ae8e46 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def test_trace_unknown_qname_exits_1(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Tests that `trie trace` with unknown qname exits 1 with structured not_found error.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_trace_invalid_direction_exits_1 fingerprint=9eba8f0d0997a6fc3413f24b13fb4ec96c6ce6098692e496d14968c5591b9406 body_fp=6a53a59543a3d4e6cd1bec987fe19b4c946386407a8acd33efb720bbac0c5365 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def test_trace_invalid_direction_exits_1(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Verifies that `trie trace` with invalid `--direction` returns exit code 1 and invalid_argument error envelope.

- Tests tool-level validation of direction parameter rather than CLI-level usage error
- Ensures CLI honors tool method's validation response without second-guessing
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_without_trie_toml_exits_1_with_clean_error fingerprint=7ae44aa39d88737da05fb452d0f77c60d500554b9e98acc9ac44df14b3285517 body_fp=068c00074b3e1164536cf8db756b279383b102b0e01dc62460aaefda3a5be1d4 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def test_grep_without_trie_toml_exits_1_with_clean_error( tmp_path: Path, monkeypatch: pytest.MonkeyPatch )`

Verifies `trie grep` exits 1 with clean error when run without trie.toml configuration file.

- Tests that missing trie.toml produces user-friendly error message rather than stack trace
- Confirms exit code 1 for script-detectable failure condition
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_read_without_trie_toml_exits_1 fingerprint=c2e555d1c7bc5d2c145c9095f3da8575f9ca6d382c78e10517f32f8a9933b3a8 body_fp=abf0effcd3f890d8360b459919638976b5539236ba5828d4e8d27005513b2cd0 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def test_read_without_trie_toml_exits_1(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Tests that `trie read` exits with code 1 and mentions "trie.toml" when run outside a configured project directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_trace_without_trie_toml_exits_1 fingerprint=e215ddf739c940699fec8f589a5a2d21ef060f7b7e362f9538939d1e6ed41c25 body_fp=3e3a3661f6c1cb2552a977c5f44210b71a733312cb117ac453fc48fd7bd76303 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def test_trace_without_trie_toml_exits_1(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Verifies that `trie trace` exits with code 1 and shows a clean error when no `trie.toml` is found.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:_read_jsonl_events fingerprint=125817628eb1f7fc15e2a61035b6350edd8094f965da770e92e1a44a6c4c4177 body_fp=37cb5ebb1eac02ccd327281296104594ebe06ba948b3e0cf5e386bbc92e55698 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def _read_jsonl_events(path: Path) -> list[dict]`

Parses a JSONL file into a list of dictionaries, skipping empty lines.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_emits_cli_call_event_not_mcp_call fingerprint=2c8f3798fc6d1622c87a523234e10d289743d7e2c64c7db1c89ffa8ffbb08344 body_fp=f6d1799b4d9650f97391f783dfe2ba8cad2a2ba8a1db40e8f9cac41c6f72d1c5 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=monitoring-telemetry -->
## `def test_grep_emits_cli_call_event_not_mcp_call( populated_project: Path, monkeypatch: pytest.MonkeyPatch, tmp_path: Path )`

Verifies that `trie grep` invocation emits `cli_call` telemetry events instead of `mcp_call` events.

- Sets `TRIE_DEBUG` to capture telemetry in a temporary JSONL file
- Executes `trie grep --name slugify` command via CliRunner  
- Asserts `cli_call` event is present and `mcp_call`/`mcp_server_start` are absent
- Ensures telemetry distinguishes CLI usage from MCP server usage for audit purposes
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_read_and_trace_also_emit_cli_call_events fingerprint=2555d2ce32fdcaeb3949422c08eb0431136ddb0de27b6d41f1efcb1ca0f16932 body_fp=43f7e1d248f41c346f6e45729e9ee44ae47c0b74d2a6792b46be865e5f691d77 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def test_read_and_trace_also_emit_cli_call_events( populated_project: Path, monkeypatch: pytest.MonkeyPatch, tmp_path: Path )`

Verifies that `trie read` and `trie trace` CLI commands emit `cli_call` telemetry events, not `mcp_call` events.

- Enables telemetry logging via `TRIE_DEBUG` environment variable
- Invokes both CLI commands and parses resulting JSONL telemetry log  
- Asserts that `cli_call` events exist for both "read" and "trace" tools
- Verifies no `mcp_call` events were emitted during CLI usage
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_cli_call_event_carries_duration_and_result_fields fingerprint=8bce6b8bf33876350ff2cc7019b5bf67715c081f34bf9c6124f2bf72d7f63572 body_fp=cf3b2cc102a90f84c4e5a94af65707af083480f968e6adeda8f2930fc3d25e39 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def test_cli_call_event_carries_duration_and_result_fields( populated_project: Path, monkeypatch: pytest.MonkeyPatch, tmp_path: Path )`

Verifies that CLI command invocations emit telemetry events with operational metadata fields.

- Tests that `cli_call` events include `duration_ms`, `result_kind`, `result_count`, and `response_bytes` fields
- Uses temporary directory with `TRIE_DEBUG` environment variable to capture telemetry output
- Validates event structure by parsing JSONL telemetry log and inspecting event fields
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_patch_list_empty fingerprint=bbcc0fb6395c895b950ebb9b9a1a4f0a52a9df3617cb617589512b803738ce23 body_fp=74749e1900e20bdceb430f4c91e601c8a9b4daaa4e441e6f09199a3d6a25eedc source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def test_patch_list_empty(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Verifies that `trie patch list` returns a clean "no pending patches" message when the patch queue is empty.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_patch_create_and_list fingerprint=b669d758dc85686efcf4b77523d214120ab2387a7cc08f4c603559339679bb0d body_fp=30a7f423b80e72d7c52187ef3afc54243dbe83d55ad828188d114010ea8307d2 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def test_patch_create_and_list(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Tests `patch create` followed by `patch list` to verify patch creation workflow.

- Creates patch for `lib:slugify` with note and reason
- Verifies patch creation output contains patch ID and confirmation
- Confirms `patch list` shows the created patch
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_patch_create_unknown_symbol fingerprint=1d749f1e6d207fe88059f0df21a061551acc207809069338c86b7061a439122c body_fp=81c61cfe545d780fee53732ef5c308bf313d1e1a22267c4dd43cfe2393019338 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def test_patch_create_unknown_symbol(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Verifies that `trie patch create` exits with code 1 and shows error when given unknown symbol qname.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_patch_preview fingerprint=387cf8a08c89463e48c5ef0292e5f65cf4bb47b2e852f6666645a4b4b54ec248 body_fp=07469a21fe905e44c00cc11ab8bfd47a1006f9190b6edfc3781d005283cb5f01 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def test_patch_preview(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Tests that `trie patch preview` displays pending patches after one is created.

- Creates a patch for `lib:slugify` then verifies preview command shows the symbol qname
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_patch_preview_empty fingerprint=4a4adb1e2c4354c41f42fbd9263899a957590931d66f3b4f06ec8df4c7d99848 body_fp=cca5f92b039ac6a23f10a03d0c9b34b408e0e586a1008797609e4bc691de528b source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def test_patch_preview_empty(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Verifies that `trie patch preview` displays "no pending patches" message when patch queue is empty.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_patch_drop_by_qname fingerprint=7a7cefdc90bc2b5d31b2a1db268922b8e11d144284005c654e255a7defae877e body_fp=790fdf20f1c96326f4e14cf99ffdb66b8dc652baac3ac3c08aa90771dd7c023e source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def test_patch_drop_by_qname(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Verifies `trie patch drop --qname <symbol>` removes a specific patch from the pending queue.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_patch_drop_all fingerprint=aecc0899edea290cf374f5a791edc2e7e3486b8c17322890ddc6fd6aaa15516d body_fp=8dd1d795009dbbd688f43be14b6ad99aceeae68767275e3d71ddc1ad360cf90d source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def test_patch_drop_all(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Test that `trie patch drop --all` removes all pending patches from the queue.

- Creates a single patch then drops all patches via `--all` flag
- Verifies patch queue becomes empty after the drop operation
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_patch_drop_no_args fingerprint=57a9a7dec5dd7b64521914f3b2db1dd3634960a1120e8302acf91af939c95bee body_fp=375d82df010aaf9bb25ca16e4b431572d1ae19212322215253dcb968ff6aa8f0 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def test_patch_drop_no_args(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Test that `trie patch drop` without arguments exits with code 1 and error message.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_patch_help fingerprint=5ab2f593844c63dd8a2e16cee02cb45fb8496135884638863ecba10eb16eb068 body_fp=7f6be672bf62d5eea29d22b059ea57bc932b4036b3a1343605abc62d3e16dcba source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## `def test_patch_help(populated_project: Path, monkeypatch: pytest.MonkeyPatch)`

Verifies that `trie patch --help` exits successfully and displays expected subcommand names in its help output.
<!-- trie:end -->

































