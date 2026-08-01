---
trie_version: 0.2.1
source: tests/test_audit.py
file_fingerprint: 3b93436d7a1eacb3ad160ec6ff447e4a925164865470ab188b00773ee8e8532a
last_synced_at: '2026-08-01T01:52:54Z'
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
outgoing_refs: 60
---
<!-- trie:section symbol=tests/test_audit:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=07a4dbed295fba97fe68715029a31e6fb405ccd2b7c55ccc291f2068e36f256e source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Comprehensive test suite for JSONL audit summary ingestion, rendering and CLI functionality.

- Tests event parsing, aggregation by tool/surface (MCP vs CLI), cost calculation, and graceful handling of malformed data
- Validates renderer output includes key metrics without asserting exact formatting
- Covers CLI commands for single logs, comparisons, JSON output, and error handling
- Exercises both full provider-prefixed and legacy bare model names for cost estimation
- Includes fast-path `_summarise` tests bypassing file I/O for fixture-based scenarios
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:FULL_MODEL fingerprint=ff1e35768cf136d376f0ea56a2898853998578f19d1f3d483d687562d9caf7e2 body_fp=8962d318eec374d834287f1b8b344f3739a2bb2e4a3ab5be5408c36c6716fbfc source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Full model identifier with provider prefix used in audit tests to exercise new full-prefix path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:BARE_MODEL fingerprint=b4adc561ff544880ff4d1080888606d88266fcf67c4a3a7a5a8c746f837b6009 body_fp=5b0f8c1acb19ea033cec7f1d91f8779ac2ed41cda68eded6fc84f0b4579b2da9 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Legacy bare model name constant for testing audit cost calculation with older log formats.

- Used in tests that verify audit can calculate costs for logs that predate the `full_model_id` convention
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:ANTHROPIC_MODEL fingerprint=44b085589a51447c608dba58dc112c8b95ef64bdf829ad7bb15248e2a566b787 body_fp=95dbf7bd09bb0ac679e078afecd50f2836213a5704838b0921089b60f6fb50b0 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Constants alias for the full Anthropic model ID used in audit tests that need the standard format.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:_write_log fingerprint=a49508ce8be7dce58721d370cb6b7acb6cc781d292b1e5962eb6c44d3ccb8278 body_fp=edeb21c0f3ce8e1a725c10ddff4c6fa64c6391818019ea129e5da55deb7235b7 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Write test data records to a JSONL file, creating zero-byte file for empty record list.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:_ts fingerprint=a22cf186c33161d9a1c3fe2c563c1b03f88d44ea52576190d5f961cfb38aaf3a body_fp=8839d31bbd6a6c2c8e05522ffe66461ffb5e17711defa4e92e13fb59a2111f53 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Generates ISO timestamp strings for test ordering with monotonic seconds increments.

- Returns timestamps in format "2026-05-16T10:00:{i:02d}.000000Z"
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_event_from_json_parses_well_formed_line fingerprint=44a73a735655a5b51b438004f04ecb9592f6f4329b944689803de4455dacb601 body_fp=f18ee1793a2836e734b8e1427609639200c2a2bce4f6651fb2c791994a619ae6 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Verifies that Event.from_json successfully parses a well-formed JSONL line with timestamp, event type, and custom fields.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_event_from_json_returns_none_on_empty_and_garbage fingerprint=a327dd89a1c14a919a90bcf43a686e7ee3d15adf0ea3379d916f41fa952ad812 body_fp=803e632ca5e6a7a1f4d41c13eb89cea1ffb1b9b14f69b07eba49330890c40178 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Verifies that Event.from_json returns None for empty input, malformed JSON, missing required fields, and non-object root types.

- Tests empty strings, whitespace, and invalid JSON syntax
- Checks that missing or invalid `event` field returns None
- Confirms arrays and strings as root values return None
- Validates that `ts` field has a default value when omitted
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_from_log_raises_when_file_missing fingerprint=acaf8175631acb18e813cc186c908b2718df5051d5dd709a191422dd8ff83ac2 body_fp=bb6a8f730250429ad7b6bfd6fee0c577c5d43c25bcf8e38b06ad1a44183b34ce source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=monitoring-telemetry -->
Verifies AuditSummary.from_log raises FileNotFoundError when the specified log file does not exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_from_log_empty_file_yields_empty_summary fingerprint=7a9c7b54c7f993208b60945afadd8147f60b8144ff766301db64b6c4d99ec046 body_fp=d5b2dd1c5f8568497889e28c09e24d49e145b62ae4806393382301afb8de01b9 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Tests that `AuditSummary.from_log` correctly processes an empty JSONL file.

- Creates empty file and verifies all summary fields contain zero/empty values
- Confirms both MCP and CLI buckets are empty dictionaries
- Validates span timing fields are None when no events exist
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_from_log_counts_malformed_lines fingerprint=987feaff79fa266aca1552d0a1fa731fc0f28230d77dd418cf153ab2cc1f0412 body_fp=644fae49c76d09f1a45768e88878a45d03a8121e6dc330ff2b583c14c77dcf53 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Verifies AuditSummary counts malformed and blank lines as parse failures rather than crashing.

- Creates JSONL with 2 valid events and 2 malformed lines (invalid JSON + blank)
- Asserts parse counts: 4 total, 2 parsed, 2 malformed
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_from_log_computes_span fingerprint=40dad95519eb3182c54e4aaefd2cbaee945088f9065d0adfb4b61b4428e92a54 body_fp=3fc6ec196b91802b2d141af68e17fd2c741dbfda249dccd3fcc7637aca176944 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Verifies that AuditSummary.from_log correctly computes time span from earliest to latest event timestamp.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_mcp_call_buckets_per_tool fingerprint=d71df265f3618b55c6e5b8501dccde19387072e462ad4afcf7b8a8f60330d146 body_fp=0e0344d37a1a59dda2f5dd824132ce7f602c8ee9c22a36414926125d5817ee13 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Tests that audit aggregates mcp_call events correctly per tool with accurate statistics.

- Creates JSONL with grep, read, and trace calls having various results and error conditions
- Verifies tool-specific buckets contain correct counts, error rates, and duration averages
- Confirms empty results, not_found errors, and qname extraction work as expected
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_read_empty_prose_counts_as_empty_result fingerprint=8d063b6bd968a17964e60624c799bc9d41769f0cd20cac8a0416745a4eec7b58 body_fp=beb0c45a7a2f444752f40bfa6b41c1899df7b6d883b5728062867d50fbbe0281 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Tests that read calls with zero prose characters count as empty results rather than errors.

- Creates mock log with one zero-prose read and one normal read
- Verifies empty_result_count equals 1 to distinguish sync gaps from actual errors
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_mcp_calls_without_capture_args_still_count fingerprint=5f02e9f8ce0df07156bac5d496b1b76e742a0ebd2a0fbec017af6cbf3d0bf787 body_fp=b917f5fc07809329e26f34c1d54c885a96c1fa4027f54360b59d4c2213045025 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=monitoring-telemetry -->
Tests that MCP calls without `args` field (when capture_args is disabled) still get counted in aggregation stats.

- Creates JSONL log with MCP read event missing `args` field
- Verifies call count increments normally but `top_qnames` remains empty
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_call_aggregation_buckets_per_tool fingerprint=9173ee008fb26aeb11a2ab9b499f0c944df0963b36fd9edbb6d2ea474b657519 body_fp=bf859310a5ee7f307af993d0ced3179e51588738da73ddca3bd92c6d8968762b source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Tests that CLI tool calls aggregate correctly into separate buckets by tool type (grep, read, trace).
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_call_and_mcp_call_are_separate_streams fingerprint=2066288cbb5d2b0b96a62cd7b0b160a49830bdf1aa4b274efff01523a67a203c body_fp=1913acfed3daa0fda2dd41f96c59105b7682fed374265bca442df5b282a37f07 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Tests that `mcp_call` and `cli_call` events are aggregated into separate buckets to prevent double-counting of tool usage across surfaces.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_to_dict_carries_cli_section fingerprint=4169576f5cf154f67c1b7b72d029a29a767cf9ccd66b92bdf2d347dc95a226ce body_fp=93e5d8f710fef7d8f9e9c83c64b316dd0a3bb26cc37db80b1ec061b9d4b33440 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Tests that AuditSummary.to_dict() includes CLI call stats in the JSON output alongside MCP stats.

- Creates a CLI grep call event and verifies the resulting dictionary contains a "cli" section
- Confirms all expected field keys are present in the CLI stats, mirroring the MCP structure
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_read_mode_breakdown_aggregates_from_cli_call_events fingerprint=7846b4cf97a29f5409f0866aa00fcb3f57fde1d1ddd38c31343b55d47c288bff body_fp=ae07025340a0d6ad7cbee7f804a9812929714049eaad84ae3a7d1da939f9c4a6 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=monitoring-telemetry -->
Tests that `cli_call` events with `mode` field aggregate into `McpCallStats.modes` breakdown.

- Creates log with mixed read modes: two `triefact_compact`, one each of `triefact_full`, `source`, `show_source`
- Verifies audit summary correctly counts each mode in `summary.cli["read"].modes`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_read_events_without_mode_field_count_as_qname fingerprint=239e047d3a3191b56c46c4400027a51f3630bff20b5ea2ab1ffebdcda1c9a5eb body_fp=e78e00b0c2b0e061a1def175d72e3a722a2e077cb0083a5daa1f9fd13202f3ae source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Verifies that `cli_call` events missing a `mode` field are classified as qname mode.

- Tests that CLI calls from Python shells without mode data count toward qname breakdown
- Ensures mode totals equal call count regardless of event source surface
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_sync_aggregation_totals_and_cost fingerprint=dfed249ef4bc999064cdb424a8f6aa695dc868332633b0334360e84d5eb1610d body_fp=da8b12aa805df716bdc0ba6bfcde4163fd407c90b5e46c9e266d0898de0b0c04 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Verifies that AuditSummary aggregates sync_file events into correct totals and computes cost.

- Creates two sync_file events with different token counts and regeneration modes
- Asserts aggregated counts match sum across events (symbols, tokens, cache usage)
- Verifies cost calculation produces positive value for known model
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_sync_with_legacy_bare_model_name_still_costs fingerprint=19898e184915fb26dfae5e642b70bd752549860d5c03b2755117b5aa82bbad84 body_fp=ecc12219deb125bfe12ee965d24bef90724cc19c8e67b89dc195bae7dd68ac36 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=monitoring-telemetry -->
Verifies that AuditSummary correctly computes non-zero cost for sync events with legacy bare model names.

- Uses BARE_MODEL constant (legacy format) instead of full provider prefix
- Asserts cost calculation falls back to prepending conventional provider prefix
- Ensures backward compatibility with logs from before full_model_id feature
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_sync_with_unknown_model_records_zero_cost fingerprint=ec9a55613a3b6739103cafb44d946a4d3deccb2e5b1ea0893898e87c469177c5 body_fp=ddce3c42740db8ace099346f903f81695243a5429bbd66654aba281beed5a067 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Tests that sync events with unknown model IDs record zero cost while preserving other metrics.

- Creates a sync_file event with an unrecognized model name
- Verifies file_runs and token counts are tracked normally
- Asserts cost_usd equals 0.0 when model pricing is unavailable
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_retries_grouped_by_reason fingerprint=87a990082b97658c25c4a4469a4716d6096f8fd968f8812fc0676cfbaa3a22f0 body_fp=4853f88bdcf57659a7d5f4c2dcc01f4174c388063d17a7d17bca281e71226c2e source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Tests that retry events are aggregated by reason and total counts/delays computed correctly.

- Verifies `total` equals count of all retry events
- Verifies `by_reason` groups retry counts by failure type
- Verifies `total_delay_seconds` sums all delay durations
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_zero_retries_when_no_events fingerprint=b03fe825bbcaefc0331179f700f7c9993419081cbeca61fd371d8afc38595415 body_fp=022459de5b0ae855e0c6c00f899ccd5e0496a1b9735094428e9472f50c4c1f31 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Verifies that AuditSummary correctly reports zero retries when the log contains no model_call_retry events.

- Creates a log file with only a scan event (no retry events)
- Asserts that retries.total equals 0
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_invocations_counted fingerprint=bd6aeaf1d02bf5e62edc832cb0483789c7683f42ba3025638ba6d6e304e3cf90 body_fp=84eb943c7b56f8cc714b2c6db5f9fc4e12faa15c0773a07b255e0b290eb0fb69 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Tests that AuditSummary.cli_invocations correctly aggregates CLI subcommand counts from "cli" events.

- Creates JSONL with sync/verify invocations and verifies count tallies match expected totals
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:_render_to_string fingerprint=a7b633e28363b8b05b2a1fbcb14505272df321ce9637266f07dd810f3aa74bdc body_fp=045f38559e9e5d781484be8c8161bda2862ff7b87e132993fb9da4d5ba397a87 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Captures render function output as plain text string by redirecting to StringIO buffer.

- Sets `force_terminal=False` to strip ANSI escape codes for testing
- Uses fixed width of 120 characters for consistent output
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_render_single_summary_includes_counts fingerprint=9df6bd18ba5368b9da29768e39fef43adc284fec13eaa91d72f6c6bc39b68231 body_fp=a6e8af33c2a02141ed11473125adffe86ec02ba03ac00c7c4ef92169c5834b1b source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Verifies that `render` produces output containing key section headers and numeric data from the audit summary.

- Creates a test log with one MCP call and one sync event
- Renders the summary to a string buffer and checks for presence of expected content
- Asserts that rendered output includes "MCP calls", tool name, "Sync" section, and numeric values
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_render_empty_log_does_not_crash fingerprint=5cf202e5e064141630a0f007d069e00512d3f4ae177aa7979d36f030b4b4a337 body_fp=2025c671f004643f28cb7d3ee44b1dfec65a05a9ac85b06325ac0b9d4d60bdc8 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Verifies the render function handles empty audit logs gracefully without raising exceptions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_render_comparison_includes_both_paths fingerprint=06969b33c19c1ef5fdc076f8cd9f13ec312712f6180328118dda042592445321 body_fp=1adb14fd1ff3a086671bc0a27888235909315bce4334159c4e277825cd1ca5d7 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test -->
Tests that `render_comparison` displays both log filenames and correctly shows deltas between runs.

- Creates two JSONL audit logs with different MCP call counts
- Verifies both filenames appear in the comparison output  
- Confirms delta column shows "+1" for the additional read call in the second log
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_render_comparison_includes_cli_call_diff fingerprint=8f671d41f58ef1b6381d0a7f96c2b0bd82ae69a85673a012940589d463ccd028 body_fp=b096355545616dce535480365074621526f695d9f501e0232b33607a7194b8a6 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Tests that `render_comparison` shows MCP and CLI call surfaces in separate tables with correct deltas.

- Creates baseline log with one MCP grep call and candidate log with same MCP call plus additional CLI grep call
- Verifies comparison output contains both "MCP calls" and "CLI calls" section headers
- Confirms the "+1" delta appears in CLI table specifically, not combined with MCP counts
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_audit_help_lists_log_option fingerprint=b5b79bb7880bf3f0c12b233a264c4d1060f77f1458cd607ac62a33b11e1e9a98 body_fp=34482dd8ca60f28a3d23c6e3714af1220d310fe59d3d6067649df04a83425e6e source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Tests that `audit --help` command shows the `--log` option in its help output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_audit_runs_against_explicit_log fingerprint=3a2fc0a8689698cda13d3a658b4ef902333dd0a09c67d2b75b00584d9acdf8cb body_fp=631b7f650132377d65c4ff08108832c2f9ff7f87f9b4a1c24e5122ecf2653e63 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Verifies that the audit CLI command runs successfully when given an explicit log file path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_audit_json_output fingerprint=1ebb633d9c86847eb818d78b992ff9c4d7a2bb2c919cca9d19efa0c6ee2e4b18 body_fp=a8869b133ac9d842fcab38d678d18029c145883922447884b838599a0c3e44e8 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Tests that the audit CLI command produces valid JSON output when --json flag is used.

- Creates a test log with one MCP grep call
- Verifies the JSON output parses and contains expected count data
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_audit_compare_two_logs fingerprint=d789e6c8f87f7553aa544b19dfecdbfa46c8a87a734a44c6586252791f872daa body_fp=b7bd48fc956bdfed20bb922f919f7dabd3b732f1a9712685b1de706defef7c89 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Tests that the audit CLI command supports comparing two logs via the `--compare` option.

- Creates two identical log files with single grep events
- Verifies CLI exits successfully and output contains comparison indicators
- Confirms both log filenames appear in the rendered comparison output
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_audit_missing_log_exits_nonzero fingerprint=960f50e897c51b014da29ce985a928538142159c5389629c917635569d710dbe body_fp=61f2c18dd07375dd6226def06ad84eee05c124a00cbbafdc216910afb0994000 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
Tests that the audit CLI command exits with non-zero status when the specified log file does not exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_summarise_directly_with_event_list fingerprint=5a50e6ff212176e95879a868884ee2fd952cb70d899925a4581956158416ec1d body_fp=ec3dfbcab5112db7a12315fe2343be26b44bd9e132bb8478c9d38ea88ea4e190 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test -->
Tests the direct `_summarise` function with a list of Event objects bypassing file parsing.

- Creates synthetic Event objects for `mcp_call` events with grep and read tools
- Verifies that tool counts and read qname tracking work correctly through the direct interface
- Provides a fast path for fixture-based testing without requiring JSONL file creation
<!-- trie:end -->