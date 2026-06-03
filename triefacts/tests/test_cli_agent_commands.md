---
trie_version: 0.1.5
source: tests/test_cli_agent_commands.py
file_fingerprint: fef25557f7b280380a6b5ea4ab80ed6f418425db203edaa4c82f85fdd674b811
last_synced_at: '2026-06-03T21:18:24Z'
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
<!-- trie:section symbol=tests/test_cli_agent_commands:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=6467d1a8b8d57dc724b6f00ab529a5df4ef3b965fe67fde03370079f9a2ff35c source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
Tests CLI agent commands (`trie grep`, `trie read`, `trie trace`) ensuring JSON output matches MCP tool surface.

- `populated_project` fixture: creates temporary project with synced Python files and triefacts
- Tests verify CLI commands produce byte-equivalent JSON to MCP tools when using `--json` flag
- Validates human-readable default output renders Rich tables and prose bodies
- Checks error handling: exit code 1 for tool errors, exit code 2 for malformed predicates
- Ensures CLI calls emit `cli_call` telemetry events instead of `mcp_call` events
- Covers patch management commands: create, list, preview, drop operations
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:PROJECT_TOML fingerprint=ea44d5615a2611cc14e40b5b84f8141a4679269bc80e3914e4fef0417f24d38b body_fp=89c7bef820cb948a388f3b7884af9fcdb82f6b66a2cf95b0fd5f32366cb13429 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
TOML configuration string used to create test projects with minimal trie settings.

- Includes basic scope, triefacts, models, and cascade configuration
- Uses Claude Sonnet 4.6 for all LLM operations in tests
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:populated_project fingerprint=90e67f6eefd8a9cde4344dfea79f23fc3bf21395b4fa03572516d408a220e7b4 body_fp=be078986266dedf21d614164d7c8fb25ccf3916d95f412ee5076367540608293 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
## populated_project

Pytest fixture that creates a minimal test project with two Python files, scans them into the graph, and syncs triefacts.

- Returns the tmp_path containing the configured project with graph database and triefacts
- Creates lib.py with slugify function and app.py with make_url function  
- Uses FakeTrieClient to generate mock triefact documentation for both files
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_with_name_returns_human_readable_table fingerprint=ceec71ef4ae8ab9dc6b463b4e086f20ff34717425879326053e4192406f8d74e body_fp=9d15656e9517bd24c097b721340a31f40107fbcf804d590adf9fa75d6e6fd645 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
Tests that `trie grep --name` outputs a human-readable Rich table with symbol qnames and one-liners.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_with_json_is_byte_equivalent_to_mcp_envelope fingerprint=fd27bdb9ab6125b23dd77bd49513fbb7a7494243f50e9bafa33ccd3b581547f9 body_fp=0553dc59a5f10fad4898249203366f38aa0ed8f39391a41e3e3e76e370c33a01 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
Verifies that `trie grep --json` output matches the MCP tool envelope structure, ensuring CLI and MCP surfaces are interchangeable for agents.

- Asserts structural shape rather than byte equality to avoid timestamp brittleness
- Validates presence of required fields: qname, signature, file_pointer, one_liner, is_public, kind, inbound_count, outbound_count
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_predicate_json_overrides_via_flags fingerprint=79c5d2628d08dc80b9bd6eb493e147c9e85e1e70332ab1a09244ca9062a5c569 body_fp=d5f3f518438aa77537e9dc543a2ed514757582859011dd431b5bce4edc07f7ea source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
Tests that `trie grep --predicate` accepts JSON blob and individual flags layer additional filters on top.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_invalid_predicate_json_exits_2 fingerprint=759099aaa7ff8a970783fe1c5d39d184b5690d06e8512053c3f5251cbb4f40dc body_fp=5ca45c1946fc825fe18c3bd8cb1afd8ed31e9ddea611b89d0efaefaa15eb37ca source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
Verifies that malformed JSON in `--predicate` flag produces exit code 2 to distinguish usage errors from tool errors.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_no_matches_shows_fallback_envelope fingerprint=60206eb0f994a8b178b3bc8ee290427d7110a4c3e7d5e67b1d20a0ac53b47f1f body_fp=3b09ed7f42a0f745ab48e70271c355de3c10f89bc95457adaf0738a6dd72e55a source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
Verifies that `trie grep` with no symbol matches returns exit code 0 and displays a fallback envelope explaining the empty result.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_with_no_flags_exits_with_invalid_argument fingerprint=1fa4926a1140b7863c3c9783481b4a3b5b1de3c07e6319aa0d30e0206993e799 body_fp=90f8b48f04d231542b087219961d9b0d12c5e1d5faa411beb933e7e48a9a95cd source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
Verifies that `trie grep` without filter flags exits with code 1 and provides filter suggestions to prevent noisy empty results.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_text_match_fallback_renders_candidates fingerprint=87da0a6f67a8bf9736cf56bc6cbc7184e64472382cc2c34902fb6e2210fbc308 body_fp=42f0e547b62cf63829ea47b7bad7ffb56930c51046e9a8905a47f04227e55f59 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
Tests that `trie grep` renders text-match fallback candidates when the query appears in symbol bodies but not names.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_read_known_qname_prints_prose_and_neighbours fingerprint=86adc7ba3e51042f0d573c5335c91041c1831526afd830ae2258a43c4edaa71f body_fp=fc083fd8f5252d6d7dac1e41162e7ea4e90f938eddb8d0e00079aa17b513eac1 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
Tests that `trie read` command outputs human-readable prose and neighbor summaries for a known qname.

- Verifies exit code 0 and presence of qname, prose body content, and caller references in output
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_read_unknown_qname_exits_1_with_suggestion fingerprint=7cd18ff86b8641d73abf355721a190d506e7f8e5b284dca0ffe0a2555e6771a8 body_fp=a3b0364962ef79ef90bed3903a615080b7d831a854da461e75d5d0cc5addad4a source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
Tests that `trie read` with an unknown qname exits with code 1 and displays helpful suggestions.

- Uses typo "lib:slugfy" to trigger not_found error from tool method
- Verifies exit code 1 for script-detectable failure
- Asserts output contains either close match "slugify" or grep command suggestion
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_read_json_emits_envelope fingerprint=25b624dddcbc27e4aebdc236a8ff3844594190666ad1c86eea4ca9f7319e473a body_fp=a6615ff75a34f31cef543252e2356f170d1e4e25749aabebb9beaf21ed873f4f source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
Verifies that `trie read --json` produces the full MCP envelope structure with qname, prose, callers, and callees fields.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_trace_callers_renders_topology fingerprint=e3024c73193838b4b73e014afc26d5406537704d7faa7650b922c10ffc3ed96d body_fp=890da90d4c9b052b4249bb48eb294ec9657aa3c4cfe290a40da85e3cd915de3a source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
Verifies that `trie trace` with `--direction callers` renders human-readable topology output including root, nodes, and directional edges.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_trace_json_shape_matches_mcp fingerprint=37ba15dd22c955d0f2e08198cf147fa0b727373366b0aed681970b8fa0cb4f36 body_fp=b16d3c6adb271a7e18ee9f8f4748c35fb0e5c4b5c031c7f864b8916b7289a8f2 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
Validates that `trie trace --json` output has the same root/nodes/edges structure as the MCP trace tool.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_trace_unknown_qname_exits_1 fingerprint=41e7adebd8254e71dbd4a61e666624407824c5f8b731cbecbaa32d59745f66da body_fp=8ffbcbb4928a1894334f656e4ba093f98b8d954b9a945cad401381069d9f8599 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
Verifies `trie trace` exits with code 1 and structured error for unknown qnames.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_trace_invalid_direction_exits_1 fingerprint=9eba8f0d0997a6fc3413f24b13fb4ec96c6ce6098692e496d14968c5591b9406 body_fp=fc178faacdc46174e95a3aee560595b2424097a95b21e2dc984c37c976f0f7a1 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
Verifies that `trie trace` with invalid `--direction` exits 1 with invalid_argument error rather than Typer usage error.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_without_trie_toml_exits_1_with_clean_error fingerprint=7ae44aa39d88737da05fb452d0f77c60d500554b9e98acc9ac44df14b3285517 body_fp=f8b8bf0d2eba102448fc5f3c70575e689bfe86865227ef54fe13dd561ae7adc4 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
Verifies that `trie grep` exits cleanly with error code 1 when no trie.toml is found in the working directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_read_without_trie_toml_exits_1 fingerprint=c2e555d1c7bc5d2c145c9095f3da8575f9ca6d382c78e10517f32f8a9933b3a8 body_fp=cf1396ad17242aa7c12aeaa6d3b012ec13357cd4efbf680e12a8b7d0453b52dd source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
## test_read_without_trie_toml_exits_1

Verifies that `trie read` exits with code 1 when no trie.toml config file exists in the working directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_trace_without_trie_toml_exits_1 fingerprint=e215ddf739c940699fec8f589a5a2d21ef060f7b7e362f9538939d1e6ed41c25 body_fp=e3c778cd7cf2829f96cbaed799080e332ed36714e2b5ce2b0b76b3921218f02c source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
Verifies that `trie trace` exits with code 1 when no trie.toml is found in the working directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:_read_jsonl_events fingerprint=125817628eb1f7fc15e2a61035b6350edd8094f965da770e92e1a44a6c4c4177 body_fp=417b2c157e1a94c1eff3798ed26129bf94a7f13165e906852e55233d96dc1bb1 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
Parse a JSONL file into a list of dictionaries, skipping empty lines.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_grep_emits_cli_call_event_not_mcp_call fingerprint=2c8f3798fc6d1622c87a523234e10d289743d7e2c64c7db1c89ffa8ffbb08344 body_fp=3f599804bbba2a85efa4d9bf638b5a2402a92a9968199245550673a27ed7788a source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
Verify `trie grep` emits `cli_call` telemetry events instead of `mcp_call` events to distinguish CLI from MCP usage in audit logs.

- Sets `TRIE_DEBUG` environment variable to capture telemetry to a temporary file
- Asserts presence of `cli_call` event and absence of MCP-specific events
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_read_and_trace_also_emit_cli_call_events fingerprint=2555d2ce32fdcaeb3949422c08eb0431136ddb0de27b6d41f1efcb1ca0f16932 body_fp=2f7ff8961601cb4dd9a1f13d00418dac42715d01229f5f6fb9163e34902c8123 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
Verifies `trie read` and `trie trace` commands emit `cli_call` telemetry events instead of `mcp_call` events.

- Sets TRIE_DEBUG environment variable to capture telemetry in temporary file
- Invokes both read and trace commands via CliRunner
- Asserts both commands emit `cli_call` events and no `mcp_call` events
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_cli_call_event_carries_duration_and_result_fields fingerprint=8bce6b8bf33876350ff2cc7019b5bf67715c081f34bf9c6124f2bf72d7f63572 body_fp=177ae7f6443729bf4f64497e9b6b1c7e3c8c3a37956e3758cde77ae37ec9f7cc source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
## test_cli_call_event_carries_duration_and_result_fields

Verifies that `cli_call` telemetry events include operational fields for audit summary computation.

- Tests that `duration_ms`, `result_kind`, `result_count`, and `response_bytes` fields are present
- Enables telemetry via `TRIE_DEBUG` environment variable and validates event structure
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_patch_list_empty fingerprint=bbcc0fb6395c895b950ebb9b9a1a4f0a52a9df3617cb617589512b803738ce23 body_fp=a6678aa6aba90323f90f33056adf19e17512e52dfaa51cb6bd5b79715a2c036c source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
Verifies that `trie patch list` shows "no pending patches" when no patches exist in the project.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_patch_create_and_list fingerprint=b669d758dc85686efcf4b77523d214120ab2387a7cc08f4c603559339679bb0d body_fp=99ede58b5c4e3252fb1f309363561e6a075df4359a33c7cd2c9bbf4e954ddcf3 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
Verifies patch creation workflow returns success output and subsequent list command shows the created patch.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_patch_create_unknown_symbol fingerprint=1d749f1e6d207fe88059f0df21a061551acc207809069338c86b7061a439122c body_fp=085e77e0411e1b5d38995dd13a57f04514db4d80043842915c101eab6836d9cb source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
Verifies that `patch create` with an unknown symbol qname exits with code 1 and displays a "not found" error message.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_patch_preview fingerprint=387cf8a08c89463e48c5ef0292e5f65cf4bb47b2e852f6666645a4b4b54ec248 body_fp=1711f75d27c551b94de863c4dde15109d730bc8652ad4afe0f6e7ae3f85db6cc source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
## test_patch_preview

Verifies `trie patch preview` displays pending patches after creating one for lib:slugify.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_patch_preview_empty fingerprint=4a4adb1e2c4354c41f42fbd9263899a957590931d66f3b4f06ec8df4c7d99848 body_fp=e0417b490504306ee5f328e4bb9a81e274bf7e2a456a07686ed7d3847ced0b79 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
Tests that `patch preview` with no pending patches displays "no pending patches" message and exits successfully.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_patch_drop_by_qname fingerprint=7a7cefdc90bc2b5d31b2a1db268922b8e11d144284005c654e255a7defae877e body_fp=707a636833e866040716b0455073dcb8532eebaf5696ec3b1df1440be734219c source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
Tests that `trie patch drop --qname <symbol>` removes a specific pending patch from the queue.

- Creates a patch for lib:slugify, verifies it appears in the list
- Drops the patch by qname and confirms the queue is empty afterward
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_patch_drop_all fingerprint=aecc0899edea290cf374f5a791edc2e7e3486b8c17322890ddc6fd6aaa15516d body_fp=67d7dc46e1adcb08fee88ff2f953b827e6c03a3afbf36111cb91b529c18e49f0 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
Verifies that `trie patch drop --all` successfully removes all pending patches from the queue.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_patch_drop_no_args fingerprint=57a9a7dec5dd7b64521914f3b2db1dd3634960a1120e8302acf91af939c95bee body_fp=2f6cb3a11b985e0708d6cdbf799b5ef35b3b1f30fbca33d7b2da42113c5eab1c source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
Tests that `trie patch drop` without arguments exits with code 1 and error message.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_cli_agent_commands:test_patch_help fingerprint=5ab2f593844c63dd8a2e16cee02cb45fb8496135884638863ecba10eb16eb068 body_fp=d184ca9a049a866a5fc7c880bb927820f0367a963f9c95800209e92be898aee0 source_ref=840ee489c600b096f9737e17c451b7b4fa1a3abe -->
Verifies `trie patch --help` displays expected subcommands in help output.

- Checks exit code 0 and presence of create, apply, preview, list, drop commands
<!-- trie:end -->