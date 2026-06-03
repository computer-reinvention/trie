---
trie_version: 0.1.5
source: tests/test_audit.py
file_fingerprint: 3b93436d7a1eacb3ad160ec6ff447e4a925164865470ab188b00773ee8e8532a
last_synced_at: '2026-06-03T20:41:02Z'
description: 'Audit summary: JSONL ingestion + rendering.'
defines:
- kind: module
  qualified_name: tests/test_audit:__module__
  lines: 1-1007
- kind: constant
  qualified_name: tests/test_audit:FULL_MODEL
  lines: 42-42
- kind: constant
  qualified_name: tests/test_audit:BARE_MODEL
  lines: 43-43
- kind: constant
  qualified_name: tests/test_audit:ANTHROPIC_MODEL
  lines: 44-44
- kind: function
  qualified_name: tests/test_audit:_write_log
  lines: 47-51
- kind: function
  qualified_name: tests/test_audit:_ts
  lines: 54-56
- kind: function
  qualified_name: tests/test_audit:test_event_from_json_parses_well_formed_line
  lines: 64-70
- kind: function
  qualified_name: tests/test_audit:test_event_from_json_returns_none_on_empty_and_garbage
  lines: 73-82
- kind: function
  qualified_name: tests/test_audit:test_from_log_raises_when_file_missing
  lines: 90-92
- kind: function
  qualified_name: tests/test_audit:test_from_log_empty_file_yields_empty_summary
  lines: 95-108
- kind: function
  qualified_name: tests/test_audit:test_from_log_counts_malformed_lines
  lines: 111-124
- kind: function
  qualified_name: tests/test_audit:test_from_log_computes_span
  lines: 127-140
- kind: function
  qualified_name: tests/test_audit:test_mcp_call_buckets_per_tool
  lines: 148-236
- kind: function
  qualified_name: tests/test_audit:test_read_empty_prose_counts_as_empty_result
  lines: 239-268
- kind: function
  qualified_name: tests/test_audit:test_mcp_calls_without_capture_args_still_count
  lines: 271-291
- kind: function
  qualified_name: tests/test_audit:test_cli_call_aggregation_buckets_per_tool
  lines: 304-369
- kind: function
  qualified_name: tests/test_audit:test_cli_call_and_mcp_call_are_separate_streams
  lines: 372-404
- kind: function
  qualified_name: tests/test_audit:test_to_dict_carries_cli_section
  lines: 407-443
- kind: function
  qualified_name: tests/test_audit:test_read_mode_breakdown_aggregates_from_cli_call_events
  lines: 446-516
- kind: function
  qualified_name: tests/test_audit:test_read_events_without_mode_field_count_as_qname
  lines: 519-543
- kind: function
  qualified_name: tests/test_audit:test_sync_aggregation_totals_and_cost
  lines: 551-603
- kind: function
  qualified_name: tests/test_audit:test_sync_with_legacy_bare_model_name_still_costs
  lines: 606-628
- kind: function
  qualified_name: tests/test_audit:test_sync_with_unknown_model_records_zero_cost
  lines: 631-650
- kind: function
  qualified_name: tests/test_audit:test_retries_grouped_by_reason
  lines: 658-687
- kind: function
  qualified_name: tests/test_audit:test_zero_retries_when_no_events
  lines: 690-693
- kind: function
  qualified_name: tests/test_audit:test_cli_invocations_counted
  lines: 701-713
- kind: function
  qualified_name: tests/test_audit:_render_to_string
  lines: 721-726
- kind: function
  qualified_name: tests/test_audit:test_render_single_summary_includes_counts
  lines: 729-759
- kind: function
  qualified_name: tests/test_audit:test_render_empty_log_does_not_crash
  lines: 762-767
- kind: function
  qualified_name: tests/test_audit:test_render_comparison_includes_both_paths
  lines: 770-818
- kind: function
  qualified_name: tests/test_audit:test_render_comparison_includes_cli_call_diff
  lines: 821-880
- kind: function
  qualified_name: tests/test_audit:test_cli_audit_help_lists_log_option
  lines: 888-892
- kind: function
  qualified_name: tests/test_audit:test_cli_audit_runs_against_explicit_log
  lines: 895-900
- kind: function
  qualified_name: tests/test_audit:test_cli_audit_json_output
  lines: 903-923
- kind: function
  qualified_name: tests/test_audit:test_cli_audit_compare_two_logs
  lines: 926-962
- kind: function
  qualified_name: tests/test_audit:test_cli_audit_missing_log_exits_nonzero
  lines: 965-968
- kind: function
  qualified_name: tests/test_audit:test_summarise_directly_with_event_list
  lines: 976-1006
incoming_refs: 0
outgoing_refs: 35
---
<!-- trie:section symbol=tests/test_audit:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=6aada8c1eb25c7bae67a4184a0827ba62b4a52cf228f9227ed4339dd41586674 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Tests for audit summary JSONL ingestion and rendering functionality.

- Validates event parsing, aggregation, cost calculation, and rendering across MCP/CLI surfaces
- Tests malformed line handling, span computation, and CLI command integration
- Covers both single summary and comparison rendering modes
- Includes end-to-end CLI tests with JSON output and error handling
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:FULL_MODEL fingerprint=ff1e35768cf136d376f0ea56a2898853998578f19d1f3d483d687562d9caf7e2 body_fp=aa2d8e7b7a8feca2c57161701244cded72336e54cd5a0b7391eb5d12c42ec1c4 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Defines a full model identifier with provider prefix for testing audit cost calculations on new-format model names.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:BARE_MODEL fingerprint=b4adc561ff544880ff4d1080888606d88266fcf67c4a3a7a5a8c746f837b6009 body_fp=b022799ce5d83246566996c5dd52858a72657dd307f752d818f332b0480f6297 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Legacy bare model name used to test backward compatibility with older debug.jsonl logs.

- Value: "claude-sonnet-4-6" without provider prefix
- Used in tests verifying audit can cost models from logs before `full_model_id` was implemented
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:ANTHROPIC_MODEL fingerprint=44b085589a51447c608dba58dc112c8b95ef64bdf829ad7bb15248e2a566b787 body_fp=c01aecac963334f402cf4fdcebe7423317cbf68170ebf3ac60ad89458bbbada7 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Alias for FULL_MODEL used in tests that require the new full-prefix model ID format.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:_write_log fingerprint=a49508ce8be7dce58721d370cb6b7acb6cc781d292b1e5962eb6c44d3ccb8278 body_fp=b038eadc061e35d6ec68ddb26e1fd2b160b95944dad94038907b05785fcfed16 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Writes a list of dictionaries to a file as JSONL format, creating an empty file if the list is empty.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:_ts fingerprint=a22cf186c33161d9a1c3fe2c563c1b03f88d44ea52576190d5f961cfb38aaf3a body_fp=6e5da36964bf4d85238863204e48587d354c63f93da64e57159e974213f1df19 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Generates monotonic ISO timestamp strings for test ordering by formatting seconds as zero-padded integers.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_event_from_json_parses_well_formed_line fingerprint=44a73a735655a5b51b438004f04ecb9592f6f4329b944689803de4455dacb601 body_fp=f8fa9808347b9490518933dada183839df195919c6f365e430ce856732ac7ab3 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Tests that Event.from_json parses a well-formed JSONL line into an Event object with correct timestamp, event type, and field dictionary.

- Returns Event with event="scan", ts="2026-05-16T10:00:00.000000Z", fields={"files_seen": 12}
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_event_from_json_returns_none_on_empty_and_garbage fingerprint=a327dd89a1c14a919a90bcf43a686e7ee3d15adf0ea3379d916f41fa952ad812 body_fp=a39b640b2627f86732d6d1847666f43325acf729cffd722e7596cd5103e000b2 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Tests that Event.from_json returns None for invalid inputs including empty strings, non-JSON text, and malformed JSON structures.

- Tests empty/whitespace strings, garbage text, missing required fields, and non-object JSON types
- Confirms that missing `ts` field defaults to empty string when `event` field is present
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_from_log_raises_when_file_missing fingerprint=acaf8175631acb18e813cc186c908b2718df5051d5dd709a191422dd8ff83ac2 body_fp=ecb46c5bf0580e9cd3110eae4495d623acdc12f0013f8bc62aad6f958c55bbba source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Verifies that `AuditSummary.from_log()` raises `FileNotFoundError` when attempting to load a non-existent log file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_from_log_empty_file_yields_empty_summary fingerprint=7a9c7b54c7f993208b60945afadd8147f60b8144ff766301db64b6c4d99ec046 body_fp=c7ff96e1b4e73cc51a99d8363757aebf69d25a9bc9e4abbb39ba5171764afed5 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Verifies that `AuditSummary.from_log` produces empty buckets when ingesting a zero-byte JSONL file.

- Creates empty log file and confirms all summary fields initialize to zero/empty/None values
- Tests both MCP and CLI surfaces return empty dictionaries for per-tool stats
- Validates span tracking fields are None when no timestamped events exist
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_from_log_counts_malformed_lines fingerprint=987feaff79fa266aca1552d0a1fa731fc0f28230d77dd418cf153ab2cc1f0412 body_fp=ff52e79e77c582ad9022ee7568067958883ac1e19ae4a903faf9617e7a1328ee source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Verifies that AuditSummary.from_log correctly counts malformed JSONL lines as unparseable rather than crashing.

- Creates a mixed JSONL file with 2 valid JSON events, 1 invalid JSON line, and 1 blank line
- Asserts that parse statistics correctly track 4 total lines, 2 parsed, and 2 malformed
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_from_log_computes_span fingerprint=40dad95519eb3182c54e4aaefd2cbaee945088f9065d0adfb4b61b4428e92a54 body_fp=44a9a9ddb76e199801cbe52fc2863f3135fe8b3268ac7d6ac5b42ea5a203cb1d source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Verifies that AuditSummary.from_log correctly computes time span from earliest to latest event timestamps.

- Creates log with events at timestamps 0, 15, and 30 seconds
- Asserts span_start matches earliest timestamp (0)
- Asserts span_end matches latest timestamp (30) 
- Asserts span_duration_seconds equals 30.0
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_mcp_call_buckets_per_tool fingerprint=d71df265f3618b55c6e5b8501dccde19387072e462ad4afcf7b8a8f60330d146 body_fp=570b2a27fcc700d3738b872aa9335346940bdd7db6338ee247c1a0621d4676b9 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Verifies AuditSummary correctly aggregates mcp_call events by tool type and computes per-tool statistics.

- Creates JSONL with mixed grep/read/trace calls including errors and empty results
- Asserts grep stats: 3 calls total, 1 error, 1 empty result, correct average duration  
- Asserts read stats: 2 calls, 1 error, 1 not_found, qname extraction works
- Asserts trace stats: 1 call counted as empty result when nodes_count==1
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_read_empty_prose_counts_as_empty_result fingerprint=8d063b6bd968a17964e60624c799bc9d41769f0cd20cac8a0416745a4eec7b58 body_fp=5b70f4b514ec0bd6511dcbaf0cd8d20aeebc9e4c8727bfce97d0b7df4a5999fb source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Verifies that MCP read calls with `prose_chars=0` count as empty results rather than errors.

- Creates two read events: one with zero prose chars, one with 200 prose chars
- Asserts the summary correctly identifies one empty result, distinguishing sync gaps from actual failures
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_mcp_calls_without_capture_args_still_count fingerprint=5f02e9f8ce0df07156bac5d496b1b76e742a0ebd2a0fbec017af6cbf3d0bf787 body_fp=0607be090b37edc0ce08574ebbed8e8f61905461ae0a523a439874591dc2471f source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Verifies AuditSummary handles mcp_call events without args field gracefully.

- Events without `args` field still increment call counts
- `top_qnames` returns empty tuple when qname extraction fails
- Call statistics remain accurate despite missing metadata
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_call_aggregation_buckets_per_tool fingerprint=9173ee008fb26aeb11a2ab9b499f0c944df0963b36fd9edbb6d2ea474b657519 body_fp=79a6db81a477147dc8c855fe2cab03bb5aaec6f8a7adf7ff54bf07faddb829a5 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Tests that CLI call events are grouped into separate tool buckets in `summary.cli` with per-tool statistics.

- Creates mixed `cli_call` events across grep, read, and trace tools
- Verifies tool-specific counts and empty result detection work correctly
- Confirms qname extraction works for CLI read calls
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_call_and_mcp_call_are_separate_streams fingerprint=2066288cbb5d2b0b96a62cd7b0b160a49830bdf1aa4b274efff01523a67a203c body_fp=7ae7bab8516d497237626b1df284d5e8fcb4315b5243be6d729703310a6778f1 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Verifies that MCP and CLI call events populate separate statistics buckets in the audit summary.

- Creates a log with one `mcp_call` grep event and one `cli_call` grep event
- Asserts each surface shows exactly one call without cross-contamination
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_to_dict_carries_cli_section fingerprint=4169576f5cf154f67c1b7b72d029a29a767cf9ccd66b92bdf2d347dc95a226ce body_fp=bb89c3d02778c9760a55c473ddd50c02a8659d8c4637913c0fee71cfd2f2c8c3 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Verifies that `AuditSummary.to_dict()` includes CLI call statistics in the serialized output.

- Creates a single `cli_call` event log and checks that the resulting dictionary contains a `cli` section
- Validates that all expected fields are present in the CLI statistics, mirroring the MCP section structure
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_read_mode_breakdown_aggregates_from_cli_call_events fingerprint=7846b4cf97a29f5409f0866aa00fcb3f57fde1d1ddd38c31343b55d47c288bff body_fp=cdac1f875b0e6fbf00f33f48c5334dd33d33d6facd1caddcb632c97f7da41a9d source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Tests that `cli_call` events with `mode` fields are correctly aggregated into `McpCallStats.modes` breakdown.

- Creates JSONL with five `cli_call` read events across different modes
- Verifies `summary.cli["read"].modes` counts each mode type correctly
- Ensures operators can distinguish cheap triefact views from expensive source fallbacks
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_read_events_without_mode_field_count_as_qname fingerprint=239e047d3a3191b56c46c4400027a51f3630bff20b5ea2ab1ffebdcda1c9a5eb body_fp=8121a6d83b92d21d2f95b4c96530eebb6a134edcebe6753ecee7785bfaf702c8 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Tests that cli_call events without mode field are counted as qname mode by the audit aggregator.

- Verifies events from Python CLI (which only accepts qnames) get properly categorized
- Ensures mode breakdown totals match call counts regardless of event source
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_sync_aggregation_totals_and_cost fingerprint=dfed249ef4bc999064cdb424a8f6aa695dc868332633b0334360e84d5eb1610d body_fp=4ec03a260bca000c31d9543632d6206566ed6b2b0c93c1087767b0e7f68888db source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Verifies AuditSummary correctly aggregates sync_file event totals and computes cost.

- Creates two sync_file events with token usage and generation counts
- Asserts aggregated totals match sum of individual events
- Verifies positive cost calculation for priced model
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_sync_with_legacy_bare_model_name_still_costs fingerprint=19898e184915fb26dfae5e642b70bd752549860d5c03b2755117b5aa82bbad84 body_fp=2eff2f096e1a67b642ad3bb915ae38e0ca9958a53bec8943adb1fb7d7537df3a source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Verifies that AuditSummary correctly prices sync_file events with legacy bare model names by applying provider prefix fallback.

- Creates a sync_file event using `BARE_MODEL` (legacy format without provider prefix)
- Asserts the summary produces non-zero cost despite the bare model name
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_sync_with_unknown_model_records_zero_cost fingerprint=ec9a55613a3b6739103cafb44d946a4d3deccb2e5b1ea0893898e87c469177c5 body_fp=3d1c0454e4d2f85d9694dc8aaa1c886d409ee1eabf2b4f9633327d0ec10b6e5f source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Verifies that `AuditSummary` records zero cost when sync events contain unknown model identifiers.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_retries_grouped_by_reason fingerprint=87a990082b97658c25c4a4469a4716d6096f8fd968f8812fc0676cfbaa3a22f0 body_fp=918211b2f2374624756798bc48c09a6bfc6bd66ea2763f64a8ee36c93f2ccf78 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Verifies that `AuditSummary.from_log` correctly aggregates model retry events by reason and calculates total delays.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_zero_retries_when_no_events fingerprint=b03fe825bbcaefc0331179f700f7c9993419081cbeca61fd371d8afc38595415 body_fp=54ad691580042f7804e9d65c63f0e0049bbcacb4f8f5aab16f3fc30a6fac67ce source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Verifies that AuditSummary reports zero retries when the log contains no retry events.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_invocations_counted fingerprint=bd6aeaf1d02bf5e62edc832cb0483789c7683f42ba3025638ba6d6e304e3cf90 body_fp=fe6db10cbd68fca920a4bb5762e8b9a3cb17045157fb51892599ed380efba78c source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Tests that CLI subcommand invocations are counted correctly by parsing "cli" events from JSONL.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:_render_to_string fingerprint=a7b633e28363b8b05b2a1fbcb14505272df321ce9637266f07dd810f3aa74bdc body_fp=22b06814d9135737135812a05629f26c0c9a14426ddf49e5a985c1de6e49705d source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Captures output from rich console rendering functions as plain text strings for testing.

- `fn`: render function to invoke with console argument
- Returns: rendered output with ANSI escape codes stripped
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_render_single_summary_includes_counts fingerprint=9df6bd18ba5368b9da29768e39fef43adc284fec13eaa91d72f6c6bc39b68231 body_fp=372890a69ef506eaee22eb3f5bb9924354b4262c3b85fd7232bdac698f08d9ce source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Verifies that `render` produces output containing expected section headings and key statistics when rendering a populated audit summary.

- Creates log with mcp_call and sync_file events containing specific counts
- Asserts rendered output contains "MCP calls", "grep", "Sync" section markers and numeric values
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_render_empty_log_does_not_crash fingerprint=5cf202e5e064141630a0f007d069e00512d3f4ae177aa7979d36f030b4b4a337 body_fp=ed551a9915b6bb1f0e3a438972efed30f77142f0655c03c550176d4821f9a6a2 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Verifies that rendering an empty audit log produces output without raising exceptions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_render_comparison_includes_both_paths fingerprint=06969b33c19c1ef5fdc076f8cd9f13ec312712f6180328118dda042592445321 body_fp=24b7f608888133faed324cb1d4e2059470864c04db4409853c4c42448b1b0075 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Tests that render_comparison displays both log filenames and delta counts when comparing audit summaries.

- Creates two JSONL logs with different MCP call counts (p1 has 1 grep, p2 has 1 grep + 1 read)
- Verifies rendered output contains both filenames "a.jsonl" and "b.jsonl"
- Confirms delta column shows "+1" reflecting the additional read call in p2
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_render_comparison_includes_cli_call_diff fingerprint=8f671d41f58ef1b6381d0a7f96c2b0bd82ae69a85673a012940589d463ccd028 body_fp=a178e2e328a1e23d964195f053a5d481842a548f8f71e106919c188d3b0c8c72 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Tests that audit comparison renderer displays MCP and CLI call surfaces as separate tables with correct deltas.

- Sets up two JSONL logs: baseline with one MCP grep call, candidate with same MCP call plus one CLI grep call
- Verifies rendered comparison output contains both "MCP calls" and "CLI calls" section headers
- Confirms "+1" delta appears only in CLI table (not absorbed into combined count)
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_audit_help_lists_log_option fingerprint=b5b79bb7880bf3f0c12b233a264c4d1060f77f1458cd607ac62a33b11e1e9a98 body_fp=eae1c46a68d5dde291a729974c02f272c1bf8b82e058448853371d79a5847d7c source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Verifies that the audit CLI command displays --log option in its help text.

- Invokes `trie audit --help` via CliRunner
- Confirms exit code is 0 and "--log" appears in help output
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_audit_runs_against_explicit_log fingerprint=3a2fc0a8689698cda13d3a658b4ef902333dd0a09c67d2b75b00584d9acdf8cb body_fp=f2a37a317e8733160c7deb86fbc91f7a7ea74e10b369f181c5aa6871cc856795 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Tests that the CLI audit command accepts an explicit log file path and runs successfully.

- Creates a minimal JSONL log with one scan event
- Verifies the command exits with status 0
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_audit_json_output fingerprint=1ebb633d9c86847eb818d78b992ff9c4d7a2bb2c919cca9d19efa0c6ee2e4b18 body_fp=ec0cffe0a2bb551374a5b8d71649a5a42e3687902be2320393f01f793940ba26 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Verifies `trie audit --json` outputs valid JSON with MCP tool call statistics.

- Creates a log with one grep call, invokes audit with `--json` flag, parses output JSON
- Confirms grep call count appears correctly in `mcp.grep.count` field
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_audit_compare_two_logs fingerprint=d789e6c8f87f7553aa544b19dfecdbfa46c8a87a734a44c6586252791f872daa body_fp=5883e55b651c04c824080f3cb492c0404a7eb35aa4010d2af8478c49216a48bc source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Verifies the CLI audit command's comparison mode renders output with both log file paths visible.

- Creates two identical JSONL logs containing single mcp_call events
- Invokes `trie audit --log a.jsonl --compare b.jsonl` via CliRunner
- Asserts successful exit code and presence of comparison markers in output
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_audit_missing_log_exits_nonzero fingerprint=960f50e897c51b014da29ce985a928538142159c5389629c917635569d710dbe body_fp=9bf8fd950b54792b16c751e69143e83ef2575e0f7d5d531de35463ba6cd57cd1 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Verifies the CLI audit command returns non-zero exit code when given a nonexistent log file path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_summarise_directly_with_event_list fingerprint=5a50e6ff212176e95879a868884ee2fd952cb70d899925a4581956158416ec1d body_fp=51d6a8ee0ef40fcd8a3f561b1c02da6d85f580c0629ce5863531fcb6cf411652 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
Tests the `_summarise` function directly with synthetic Event objects to verify audit aggregation logic.

- Bypasses file I/O by providing pre-constructed Event instances
- Verifies MCP tool call counts and qname tracking work correctly
- Serves as a fast unit test alternative to full JSONL file processing
<!-- trie:end -->