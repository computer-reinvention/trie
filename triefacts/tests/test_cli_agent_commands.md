---
trie_version: 0.1.5
source: tests/test_cli_agent_commands.py
file_fingerprint: fef25557f7b280380a6b5ea4ab80ed6f418425db203edaa4c82f85fdd674b811
last_synced_at: '2026-06-06T13:15:48Z'
description: 'Tests for the agent-facing CLI subcommands: `trie grep`, `trie read`,
  `trie trace`.'
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
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_grep_with_name_returns_human_readable_table
  lines: 87-99
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_grep_with_json_is_byte_equivalent_to_mcp_envelope
  lines: 102-131
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_grep_predicate_json_overrides_via_flags
  lines: 134-157
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_grep_invalid_predicate_json_exits_2
  lines: 160-170
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_grep_no_matches_shows_fallback_envelope
  lines: 173-185
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_grep_with_no_flags_exits_with_invalid_argument
  lines: 188-209
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_grep_text_match_fallback_renders_candidates
  lines: 212-224
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_read_known_qname_prints_prose_and_neighbours
  lines: 232-244
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_read_unknown_qname_exits_1_with_suggestion
  lines: 247-259
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_read_json_emits_envelope
  lines: 262-274
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_trace_callers_renders_topology
  lines: 282-294
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_trace_json_shape_matches_mcp
  lines: 297-319
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_trace_unknown_qname_exits_1
  lines: 322-329
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_trace_invalid_direction_exits_1
  lines: 332-341
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_grep_without_trie_toml_exits_1_with_clean_error
  lines: 349-359
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_read_without_trie_toml_exits_1
  lines: 362-368
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_trace_without_trie_toml_exits_1
  lines: 371-377
- kind: function
  qualified_name: tests/test_cli_agent_commands:_read_jsonl_events
  lines: 385-391
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_grep_emits_cli_call_event_not_mcp_call
  lines: 394-420
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_read_and_trace_also_emit_cli_call_events
  lines: 423-447
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_cli_call_event_carries_duration_and_result_fields
  lines: 450-473
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_patch_list_empty
  lines: 479-484
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_patch_create_and_list
  lines: 487-500
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_patch_create_unknown_symbol
  lines: 503-508
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_patch_preview
  lines: 511-520
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_patch_preview_empty
  lines: 523-528
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_patch_drop_by_qname
  lines: 531-543
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_patch_drop_all
  lines: 546-555
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_patch_drop_no_args
  lines: 558-563
- kind: function
  qualified_name: tests/test_cli_agent_commands:test_patch_help
  lines: 566-575
incoming_refs: 0
outgoing_refs: 33
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
<!-- trie:section symbol=tests/test_cli_agent_commands:populated_project fingerprint=90e67f6eefd8a9cde4344dfea79f23fc3bf21395b4fa03572516d408a220e7b4 body_fp=a96d47548c3b3f45a3b540f4b710016922f460bdd30fc1b70cdc29220286ab11 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
Creates a temporary project with `lib.py` and `app.py` files, scans them into the graph, and syncs triefacts using fake LLM responses.

- Returns the temporary project root directory with complete graph database
- Sets up `trie.toml` configuration and two Python modules with import relationship
- Uses `FakeTrieClient` to simulate triefact generation for both files
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_with_name_returns_human_readable_table fingerprint=ceec71ef4ae8ab9dc6b463b4e086f20ff34717425879326053e4192406f8d74e body_fp=c8e0295512b9c20d490d8d26ca7a1f0258712be3630d07b252399f36d6a80aef source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
Verifies `trie grep --name` outputs a human-readable Rich table containing the matching symbol's qname and one-liner description.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_with_json_is_byte_equivalent_to_mcp_envelope fingerprint=fd27bdb9ab6125b23dd77bd49513fbb7a7494243f50e9bafa33ccd3b581547f9 body_fp=375e6c80883e54b5df8163d03641bfc8bfb4fea8b0f96888c305a9010fd7dc6c source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
Verifies `trie grep --json` outputs the same MCP envelope structure as the wire protocol.

- Uses structural assertions on JSON shape rather than byte-for-byte comparison to avoid timestamp brittleness
- Confirms presence of required MCP envelope fields: qname, signature, file_pointer, one_liner, is_public, kind, inbound_count, outbound_count
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_predicate_json_overrides_via_flags fingerprint=79c5d2628d08dc80b9bd6eb493e147c9e85e1e70332ab1a09244ca9062a5c569 body_fp=afe128e54b7e67e58f7e092ebe8a5dd240b670be785bc94b3104e033239ff224 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
Tests that `--predicate` JSON is layered with command-line flags for agent workflow compatibility.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_invalid_predicate_json_exits_2 fingerprint=759099aaa7ff8a970783fe1c5d39d184b5690d06e8512053c3f5251cbb4f40dc body_fp=4ee7b3479edb4de514d306da3d15c97355b251c40015ee00c08e6ec3d6a5fb05 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
Verifies that malformed JSON in `--predicate` flag exits with code 2 to distinguish usage errors from tool errors.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_no_matches_shows_fallback_envelope fingerprint=60206eb0f994a8b178b3bc8ee290427d7110a4c3e7d5e67b1d20a0ac53b47f1f body_fp=447d24dfd6320418ba11c6486d8c180ab9f5c1ad2bf7d9fc6a0b81e4bf93e01f source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
Tests that `trie grep` with no symbol matches returns a fallback envelope explaining the empty result.

- Verifies exit code 0 (empty results are not errors)
- Checks output contains "text_match_empty" indicating fallback behavior
- Ensures human-readable output explains why no hits were found
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_with_no_flags_exits_with_invalid_argument fingerprint=1fa4926a1140b7863c3c9783481b4a3b5b1de3c07e6319aa0d30e0206993e799 body_fp=ac6f3e3a9adf628a4a152c1aad0450a185d27dfff0c934826b1bc98878cb820b source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
Verifies that `trie grep` with no filter flags exits 1 with an `invalid_argument` error and usage suggestions.

- Prevents the "noisy empty grep" footgun by rejecting empty predicates
- Exit code 1 indicates tool-level error (vs exit code 2 for CLI usage errors)
- Output must contain suggested filters like `name_contains` or `scope_prefix`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_text_match_fallback_renders_candidates fingerprint=87da0a6f67a8bf9736cf56bc6cbc7184e64472382cc2c34902fb6e2210fbc308 body_fp=705389af550225b414a6da6fe6fd45ca98ddcf2a6edbdfad2fef238c615ed21f source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
Tests that `trie grep` renders candidate symbols when search text appears in symbol bodies but not names.

- Searches for "replace" which exists in lib:slugify's body content
- Verifies fallback text_match behavior surfaces candidate symbols in output
- Ensures lib:slugify appears as a candidate despite name mismatch
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_read_known_qname_prints_prose_and_neighbours fingerprint=86adc7ba3e51042f0d573c5335c91041c1831526afd830ae2258a43c4edaa71f body_fp=6321b486b1c42fbbcd7487e5313457015aedab386febd4f4e1485a228451144b source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## test_read_known_qname_prints_prose_and_neighbours

Verifies `trie read` command outputs symbol prose body and caller/callee summaries in human-readable format.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_read_unknown_qname_exits_1_with_suggestion fingerprint=7cd18ff86b8641d73abf355721a190d506e7f8e5b284dca0ffe0a2555e6771a8 body_fp=a76e3ee91abe42ff62ef898cac7c8a91395b87670a53b76eec6c6b28a96951cd source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
Verifies that `trie read` with a typo in the qname exits with code 1 and includes helpful suggestions in the output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_read_json_emits_envelope fingerprint=25b624dddcbc27e4aebdc236a8ff3844594190666ad1c86eea4ca9f7319e473a body_fp=1c1544924902016a7932f198390a05cacdd7258de973a5ba77587ffa5b374053 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## test_read_json_emits_envelope

Verifies that `trie read --json` outputs the same MCP envelope structure as the wire protocol.

- Asserts parsed JSON contains `qname`, `prose`, `callers`, and `callees` fields
- Validates that caller qnames include expected symbols from the test project
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_trace_callers_renders_topology fingerprint=e3024c73193838b4b73e014afc26d5406537704d7faa7650b922c10ffc3ed96d body_fp=040f7721989f51fc23d1188eafda89e370c96237c7c32c1a1b445447ac7ecede source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## test_trace_callers_renders_topology

Tests that `trie trace` with callers direction produces human-readable topology output showing root, nodes, and directed edges with clear arrow indicators.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_trace_json_shape_matches_mcp fingerprint=37ba15dd22c955d0f2e08198cf147fa0b727373366b0aed681970b8fa0cb4f36 body_fp=fe5e36db561609ccfcdb4ab4d1139ecc0b33fc07c57ca2070dd0a94194fbf2a7 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
Verifies `trie trace --json` output has the same root/nodes/edges structure as MCP trace tool responses.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_trace_unknown_qname_exits_1 fingerprint=41e7adebd8254e71dbd4a61e666624407824c5f8b731cbecbaa32d59745f66da body_fp=4bdc24c4a55997e15eefc09829131c1dc0a1412d3b8c00845e15b7ec66289266 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
Tests that `trie trace` with unknown qname exits 1 with structured not_found error.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_trace_invalid_direction_exits_1 fingerprint=9eba8f0d0997a6fc3413f24b13fb4ec96c6ce6098692e496d14968c5591b9406 body_fp=794fcfff2b812cc845a9ef62845117f5a52152f36b6910a3b8968bb0d3f71d7c source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
Verifies that `trie trace` with invalid `--direction` returns exit code 1 and invalid_argument error envelope.

- Tests tool-level validation of direction parameter rather than CLI-level usage error
- Ensures CLI honors tool method's validation response without second-guessing
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_without_trie_toml_exits_1_with_clean_error fingerprint=7ae44aa39d88737da05fb452d0f77c60d500554b9e98acc9ac44df14b3285517 body_fp=59e1323ad0f09cb2b51dfe531db8bc65e23bc53f9234d6a1bda430f17e6ac45b source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
Verifies `trie grep` exits 1 with clean error when run without trie.toml configuration file.

- Tests that missing trie.toml produces user-friendly error message rather than stack trace
- Confirms exit code 1 for script-detectable failure condition
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_read_without_trie_toml_exits_1 fingerprint=c2e555d1c7bc5d2c145c9095f3da8575f9ca6d382c78e10517f32f8a9933b3a8 body_fp=ba9aae046a1ab80eb1d0cf1917b1388f4cbac9a6efc1c5c6261a61664c0407e7 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
Tests that `trie read` exits with code 1 and mentions "trie.toml" when run outside a configured project directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_trace_without_trie_toml_exits_1 fingerprint=e215ddf739c940699fec8f589a5a2d21ef060f7b7e362f9538939d1e6ed41c25 body_fp=f69c83177f1f30e5fc2f3c7fc568adecaa86fc32952e782dfc1bc6a1a6898464 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
Verifies that `trie trace` exits with code 1 and shows a clean error when no `trie.toml` is found.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:_read_jsonl_events fingerprint=125817628eb1f7fc15e2a61035b6350edd8094f965da770e92e1a44a6c4c4177 body_fp=ef4e11948c62d2955013ed7274508426369d4d08915043e4e4ecac7ae69e2e3b source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
Parses a JSONL file into a list of dictionaries, skipping empty lines.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_emits_cli_call_event_not_mcp_call fingerprint=2c8f3798fc6d1622c87a523234e10d289743d7e2c64c7db1c89ffa8ffbb08344 body_fp=9bff6c115f24133b65da5e2ff193ba445e8c331061c940e660ec157568528c45 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=monitoring-telemetry -->
Verifies that `trie grep` invocation emits `cli_call` telemetry events instead of `mcp_call` events.

- Sets `TRIE_DEBUG` to capture telemetry in a temporary JSONL file
- Executes `trie grep --name slugify` command via CliRunner  
- Asserts `cli_call` event is present and `mcp_call`/`mcp_server_start` are absent
- Ensures telemetry distinguishes CLI usage from MCP server usage for audit purposes
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_read_and_trace_also_emit_cli_call_events fingerprint=2555d2ce32fdcaeb3949422c08eb0431136ddb0de27b6d41f1efcb1ca0f16932 body_fp=e74dd660335afacbefff7148fcabfed77c307576ea12cb73145882fe16abffbe source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## test_read_and_trace_also_emit_cli_call_events

Verifies that `trie read` and `trie trace` CLI commands emit `cli_call` telemetry events, not `mcp_call` events.

- Enables telemetry logging via `TRIE_DEBUG` environment variable
- Invokes both CLI commands and parses resulting JSONL telemetry log  
- Asserts that `cli_call` events exist for both "read" and "trace" tools
- Verifies no `mcp_call` events were emitted during CLI usage
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_cli_call_event_carries_duration_and_result_fields fingerprint=8bce6b8bf33876350ff2cc7019b5bf67715c081f34bf9c6124f2bf72d7f63572 body_fp=6869dbe3bc7e7917d91f48e7bdd661896cc415ea0457614088ddac42ccb47dbb source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
Verifies that CLI command invocations emit telemetry events with operational metadata fields.

- Tests that `cli_call` events include `duration_ms`, `result_kind`, `result_count`, and `response_bytes` fields
- Uses temporary directory with `TRIE_DEBUG` environment variable to capture telemetry output
- Validates event structure by parsing JSONL telemetry log and inspecting event fields
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_patch_list_empty fingerprint=bbcc0fb6395c895b950ebb9b9a1a4f0a52a9df3617cb617589512b803738ce23 body_fp=a873374721d51461716a3e8ec61a26a8bee62a3d0212cb68912e6c293d19e14e source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
Verifies that `trie patch list` returns a clean "no pending patches" message when the patch queue is empty.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_patch_create_and_list fingerprint=b669d758dc85686efcf4b77523d214120ab2387a7cc08f4c603559339679bb0d body_fp=60418863c172e272af328b8a2e2c57bb0a374d46adbcd9154a4ed65fc11b3782 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
Tests `patch create` followed by `patch list` to verify patch creation workflow.

- Creates patch for `lib:slugify` with note and reason
- Verifies patch creation output contains patch ID and confirmation
- Confirms `patch list` shows the created patch
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_patch_create_unknown_symbol fingerprint=1d749f1e6d207fe88059f0df21a061551acc207809069338c86b7061a439122c body_fp=a652851128dfb5480bb3ef4315286b2b96e7b7ec8928f9a7355aa791e7750bad source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
Verifies that `trie patch create` exits with code 1 and shows error when given unknown symbol qname.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_patch_preview fingerprint=387cf8a08c89463e48c5ef0292e5f65cf4bb47b2e852f6666645a4b4b54ec248 body_fp=98589b837e6c10ba0b1f26c3fa55730edc4cc211bbab16a49c370d332e9d6817 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
Tests that `trie patch preview` displays pending patches after one is created.

- Creates a patch for `lib:slugify` then verifies preview command shows the symbol qname
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_patch_preview_empty fingerprint=4a4adb1e2c4354c41f42fbd9263899a957590931d66f3b4f06ec8df4c7d99848 body_fp=ba4b73759abbf8d7794676c1c192f45a5c4076e477e3713f56beb93c3e660b9b source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
Verifies that `trie patch preview` displays "no pending patches" message when patch queue is empty.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_patch_drop_by_qname fingerprint=7a7cefdc90bc2b5d31b2a1db268922b8e11d144284005c654e255a7defae877e body_fp=df6a586236d84dcaa11c3a171bc003bb5917bba46e96a7b5540f339e8fe6ca16 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
## test_patch_drop_by_qname

Verifies `trie patch drop --qname <symbol>` removes a specific patch from the pending queue.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_patch_drop_all fingerprint=aecc0899edea290cf374f5a791edc2e7e3486b8c17322890ddc6fd6aaa15516d body_fp=2fad59159841c3df3b828720eabb9a25e56a9f0120f41b7bc4c133f1a4c3bf7b source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
Test that `trie patch drop --all` removes all pending patches from the queue.

- Creates a single patch then drops all patches via `--all` flag
- Verifies patch queue becomes empty after the drop operation
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_patch_drop_no_args fingerprint=57a9a7dec5dd7b64521914f3b2db1dd3634960a1120e8302acf91af939c95bee body_fp=5d3cd88cc3e0eeb237aeff1197fc830693ef6626b1d8aeaf0f6b71ec7c313f1d source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
Test that `trie patch drop` without arguments exits with code 1 and error message.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_patch_help fingerprint=5ab2f593844c63dd8a2e16cee02cb45fb8496135884638863ecba10eb16eb068 body_fp=d6e59554be15305472a3e64284048b343cf468fa320c3c5e4972467fa9e96b2e source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe role=test-infrastructure -->
Verifies that `trie patch --help` exits successfully and displays expected subcommand names in its help output.
<!-- trie:end -->

































