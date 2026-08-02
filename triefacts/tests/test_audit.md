---
trie_version: 0.3.0
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
  signature: 'def _write_log(path: Path, records: list[dict]) -> None'
- kind: function
  qualified_name: tests/test_audit:_ts
  lines: 54-56
  signature: 'def _ts(i: int) -> str'
- kind: function
  qualified_name: tests/test_audit:test_event_from_json_parses_well_formed_line
  lines: 64-70
  signature: def test_event_from_json_parses_well_formed_line()
- kind: function
  qualified_name: tests/test_audit:test_event_from_json_returns_none_on_empty_and_garbage
  lines: 73-82
  signature: def test_event_from_json_returns_none_on_empty_and_garbage()
- kind: function
  qualified_name: tests/test_audit:test_from_log_raises_when_file_missing
  lines: 90-92
  signature: 'def test_from_log_raises_when_file_missing(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_audit:test_from_log_empty_file_yields_empty_summary
  lines: 95-108
  signature: 'def test_from_log_empty_file_yields_empty_summary(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_audit:test_from_log_counts_malformed_lines
  lines: 111-124
  signature: 'def test_from_log_counts_malformed_lines(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_audit:test_from_log_computes_span
  lines: 127-140
  signature: 'def test_from_log_computes_span(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_audit:test_mcp_call_buckets_per_tool
  lines: 148-236
  signature: 'def test_mcp_call_buckets_per_tool(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_audit:test_read_empty_prose_counts_as_empty_result
  lines: 239-268
  signature: 'def test_read_empty_prose_counts_as_empty_result(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_audit:test_mcp_calls_without_capture_args_still_count
  lines: 271-291
  signature: 'def test_mcp_calls_without_capture_args_still_count(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_audit:test_cli_call_aggregation_buckets_per_tool
  lines: 304-369
  signature: 'def test_cli_call_aggregation_buckets_per_tool(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_audit:test_cli_call_and_mcp_call_are_separate_streams
  lines: 372-404
  signature: 'def test_cli_call_and_mcp_call_are_separate_streams(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_audit:test_to_dict_carries_cli_section
  lines: 407-443
  signature: 'def test_to_dict_carries_cli_section(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_audit:test_read_mode_breakdown_aggregates_from_cli_call_events
  lines: 446-516
  signature: 'def test_read_mode_breakdown_aggregates_from_cli_call_events(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_audit:test_read_events_without_mode_field_count_as_qname
  lines: 519-543
  signature: 'def test_read_events_without_mode_field_count_as_qname(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_audit:test_sync_aggregation_totals_and_cost
  lines: 551-603
  signature: 'def test_sync_aggregation_totals_and_cost(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_audit:test_sync_with_legacy_bare_model_name_still_costs
  lines: 606-628
  signature: 'def test_sync_with_legacy_bare_model_name_still_costs(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_audit:test_sync_with_unknown_model_records_zero_cost
  lines: 631-650
  signature: 'def test_sync_with_unknown_model_records_zero_cost(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_audit:test_retries_grouped_by_reason
  lines: 658-687
  signature: 'def test_retries_grouped_by_reason(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_audit:test_zero_retries_when_no_events
  lines: 690-693
  signature: 'def test_zero_retries_when_no_events(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_audit:test_cli_invocations_counted
  lines: 701-713
  signature: 'def test_cli_invocations_counted(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_audit:_render_to_string
  lines: 721-726
  signature: def _render_to_string(fn, *args) -> str
- kind: function
  qualified_name: tests/test_audit:test_render_single_summary_includes_counts
  lines: 729-759
  signature: 'def test_render_single_summary_includes_counts(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_audit:test_render_empty_log_does_not_crash
  lines: 762-767
  signature: 'def test_render_empty_log_does_not_crash(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_audit:test_render_comparison_includes_both_paths
  lines: 770-818
  signature: 'def test_render_comparison_includes_both_paths(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_audit:test_render_comparison_includes_cli_call_diff
  lines: 821-880
  signature: 'def test_render_comparison_includes_cli_call_diff(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_audit:test_cli_audit_help_lists_log_option
  lines: 888-892
  signature: def test_cli_audit_help_lists_log_option()
- kind: function
  qualified_name: tests/test_audit:test_cli_audit_runs_against_explicit_log
  lines: 895-900
  signature: 'def test_cli_audit_runs_against_explicit_log(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_audit:test_cli_audit_json_output
  lines: 903-923
  signature: 'def test_cli_audit_json_output(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_audit:test_cli_audit_compare_two_logs
  lines: 926-962
  signature: 'def test_cli_audit_compare_two_logs(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_audit:test_cli_audit_missing_log_exits_nonzero
  lines: 965-968
  signature: 'def test_cli_audit_missing_log_exits_nonzero(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_audit:test_summarise_directly_with_event_list
  lines: 976-1006
  signature: def test_summarise_directly_with_event_list()
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
<!-- trie:section symbol=tests/test_audit:_write_log fingerprint=a49508ce8be7dce58721d370cb6b7acb6cc781d292b1e5962eb6c44d3ccb8278 body_fp=ddd4371066335f509f84f62e24642e3ef558dc12334b609ddac33c5476411450 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
## `def _write_log(path: Path, records: list[dict]) -> None`

Write test data records to a JSONL file, creating zero-byte file for empty record list.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:_ts fingerprint=a22cf186c33161d9a1c3fe2c563c1b03f88d44ea52576190d5f961cfb38aaf3a body_fp=d38ed80e3fc29ff81051b80bccb9daa692f4e98a9d09dfd215d6ad1b171108e6 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
## `def _ts(i: int) -> str`

Generates ISO timestamp strings for test ordering with monotonic seconds increments.

- Returns timestamps in format "2026-05-16T10:00:{i:02d}.000000Z"
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_event_from_json_parses_well_formed_line fingerprint=44a73a735655a5b51b438004f04ecb9592f6f4329b944689803de4455dacb601 body_fp=938953e55c6b458a981b9971a5499599d429e832fe5267248157fdd3e6fe1a24 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
## `def test_event_from_json_parses_well_formed_line()`

Verifies that Event.from_json successfully parses a well-formed JSONL line with timestamp, event type, and custom fields.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_event_from_json_returns_none_on_empty_and_garbage fingerprint=a327dd89a1c14a919a90bcf43a686e7ee3d15adf0ea3379d916f41fa952ad812 body_fp=bcd2f79afee30ea07d3a9377658d4ec9784670cdd34eca10279ff18a2188ba9b source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
## `def test_event_from_json_returns_none_on_empty_and_garbage()`

Verifies that Event.from_json returns None for empty input, malformed JSON, missing required fields, and non-object root types.

- Tests empty strings, whitespace, and invalid JSON syntax
- Checks that missing or invalid `event` field returns None
- Confirms arrays and strings as root values return None
- Validates that `ts` field has a default value when omitted
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_from_log_raises_when_file_missing fingerprint=acaf8175631acb18e813cc186c908b2718df5051d5dd709a191422dd8ff83ac2 body_fp=b47efae67b87f6b91285cfa66199b7d75b8a27aa0ad1e7b57252bd903f99a17c source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=monitoring-telemetry -->
## `def test_from_log_raises_when_file_missing(tmp_path: Path)`

Verifies AuditSummary.from_log raises FileNotFoundError when the specified log file does not exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_from_log_empty_file_yields_empty_summary fingerprint=7a9c7b54c7f993208b60945afadd8147f60b8144ff766301db64b6c4d99ec046 body_fp=c8dfa4e80ea615ef9fe982a9a19d06b89a864e1271e3982b04126feedc4afec4 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
## `def test_from_log_empty_file_yields_empty_summary(tmp_path: Path)`

Tests that `AuditSummary.from_log` correctly processes an empty JSONL file.

- Creates empty file and verifies all summary fields contain zero/empty values
- Confirms both MCP and CLI buckets are empty dictionaries
- Validates span timing fields are None when no events exist
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_from_log_counts_malformed_lines fingerprint=987feaff79fa266aca1552d0a1fa731fc0f28230d77dd418cf153ab2cc1f0412 body_fp=e47624b89fd519003c507cb96fd8cf2c9a1611ca5fec81bd5554ae7b5dc3f859 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
## `def test_from_log_counts_malformed_lines(tmp_path: Path)`

Verifies AuditSummary counts malformed and blank lines as parse failures rather than crashing.

- Creates JSONL with 2 valid events and 2 malformed lines (invalid JSON + blank)
- Asserts parse counts: 4 total, 2 parsed, 2 malformed
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_from_log_computes_span fingerprint=40dad95519eb3182c54e4aaefd2cbaee945088f9065d0adfb4b61b4428e92a54 body_fp=5e608ac9d4814a0209fa93fe62db3ede49eedd22a0534176fe5520ed5f0b0b32 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
## `def test_from_log_computes_span(tmp_path: Path)`

Verifies that AuditSummary.from_log correctly computes time span from earliest to latest event timestamp.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_mcp_call_buckets_per_tool fingerprint=d71df265f3618b55c6e5b8501dccde19387072e462ad4afcf7b8a8f60330d146 body_fp=a4f44da4a433bdc759b095799b26b885d49f6b7cf0aea1b59f29fe0da4383baa source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
## `def test_mcp_call_buckets_per_tool(tmp_path: Path)`

Tests that audit aggregates mcp_call events correctly per tool with accurate statistics.

- Creates JSONL with grep, read, and trace calls having various results and error conditions
- Verifies tool-specific buckets contain correct counts, error rates, and duration averages
- Confirms empty results, not_found errors, and qname extraction work as expected
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_read_empty_prose_counts_as_empty_result fingerprint=8d063b6bd968a17964e60624c799bc9d41769f0cd20cac8a0416745a4eec7b58 body_fp=904561684c54af9350d632904bac2b333e24a4c8d5252dadfe3e4bd6b6882fea source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
## `def test_read_empty_prose_counts_as_empty_result(tmp_path: Path)`

Tests that read calls with zero prose characters count as empty results rather than errors.

- Creates mock log with one zero-prose read and one normal read
- Verifies empty_result_count equals 1 to distinguish sync gaps from actual errors
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_mcp_calls_without_capture_args_still_count fingerprint=5f02e9f8ce0df07156bac5d496b1b76e742a0ebd2a0fbec017af6cbf3d0bf787 body_fp=38a499bf376501ae75a183fb634666dc48c0c9dc7fb9282e8569a2f03f559077 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=monitoring-telemetry -->
## `def test_mcp_calls_without_capture_args_still_count(tmp_path: Path)`

Tests that MCP calls without `args` field (when capture_args is disabled) still get counted in aggregation stats.

- Creates JSONL log with MCP read event missing `args` field
- Verifies call count increments normally but `top_qnames` remains empty
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_call_aggregation_buckets_per_tool fingerprint=9173ee008fb26aeb11a2ab9b499f0c944df0963b36fd9edbb6d2ea474b657519 body_fp=ffc9df30759a2f0b0900356628be4afd2761c7ad87e56eab6a281c2ccdb1337b source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
## `def test_cli_call_aggregation_buckets_per_tool(tmp_path: Path)`

Tests that CLI tool calls aggregate correctly into separate buckets by tool type (grep, read, trace).
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_call_and_mcp_call_are_separate_streams fingerprint=2066288cbb5d2b0b96a62cd7b0b160a49830bdf1aa4b274efff01523a67a203c body_fp=2f8e79b5876b7e083da4df8dd22b28eb4e1a6f49fa89033518703879d77c8364 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
## `def test_cli_call_and_mcp_call_are_separate_streams(tmp_path: Path)`

Tests that `mcp_call` and `cli_call` events are aggregated into separate buckets to prevent double-counting of tool usage across surfaces.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_to_dict_carries_cli_section fingerprint=4169576f5cf154f67c1b7b72d029a29a767cf9ccd66b92bdf2d347dc95a226ce body_fp=efb097b0f89abf6c330a2c1c6633b40ea2c39dd8c8a8c400fc0cbd8a6f5f3d72 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
## `def test_to_dict_carries_cli_section(tmp_path: Path)`

Tests that AuditSummary.to_dict() includes CLI call stats in the JSON output alongside MCP stats.

- Creates a CLI grep call event and verifies the resulting dictionary contains a "cli" section
- Confirms all expected field keys are present in the CLI stats, mirroring the MCP structure
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_read_mode_breakdown_aggregates_from_cli_call_events fingerprint=7846b4cf97a29f5409f0866aa00fcb3f57fde1d1ddd38c31343b55d47c288bff body_fp=8b70e15db33c9e7cf50b679bf70e87941a33c9ad665c2d0006f8fad2efff9912 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=monitoring-telemetry -->
## `def test_read_mode_breakdown_aggregates_from_cli_call_events(tmp_path: Path)`

Tests that `cli_call` events with `mode` field aggregate into `McpCallStats.modes` breakdown.

- Creates log with mixed read modes: two `triefact_compact`, one each of `triefact_full`, `source`, `show_source`
- Verifies audit summary correctly counts each mode in `summary.cli["read"].modes`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_read_events_without_mode_field_count_as_qname fingerprint=239e047d3a3191b56c46c4400027a51f3630bff20b5ea2ab1ffebdcda1c9a5eb body_fp=c47ddd6596fea7066cc47f2ef15ea4e90b6881e008a68ba8349f5e6cfe3e96d0 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
## `def test_read_events_without_mode_field_count_as_qname(tmp_path: Path)`

Verifies that `cli_call` events missing a `mode` field are classified as qname mode.

- Tests that CLI calls from Python shells without mode data count toward qname breakdown
- Ensures mode totals equal call count regardless of event source surface
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_sync_aggregation_totals_and_cost fingerprint=dfed249ef4bc999064cdb424a8f6aa695dc868332633b0334360e84d5eb1610d body_fp=17e6416a17b467c2ab629f0c7f9873da9a6be47d6b6d504ac37d74553621c981 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
## `def test_sync_aggregation_totals_and_cost(tmp_path: Path)`

Verifies that AuditSummary aggregates sync_file events into correct totals and computes cost.

- Creates two sync_file events with different token counts and regeneration modes
- Asserts aggregated counts match sum across events (symbols, tokens, cache usage)
- Verifies cost calculation produces positive value for known model
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_sync_with_legacy_bare_model_name_still_costs fingerprint=19898e184915fb26dfae5e642b70bd752549860d5c03b2755117b5aa82bbad84 body_fp=4e40dedd8933bcd8eb37ab34d2cd702be90ea58017d750f41b15e0e090091414 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=monitoring-telemetry -->
## `def test_sync_with_legacy_bare_model_name_still_costs(tmp_path: Path)`

Verifies that AuditSummary correctly computes non-zero cost for sync events with legacy bare model names.

- Uses BARE_MODEL constant (legacy format) instead of full provider prefix
- Asserts cost calculation falls back to prepending conventional provider prefix
- Ensures backward compatibility with logs from before full_model_id feature
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_sync_with_unknown_model_records_zero_cost fingerprint=ec9a55613a3b6739103cafb44d946a4d3deccb2e5b1ea0893898e87c469177c5 body_fp=4111a6e18da2b127ee49e2e4ed14ee6bb0ca29df24b51b045ef77710e35f90dd source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
## `def test_sync_with_unknown_model_records_zero_cost(tmp_path: Path)`

Tests that sync events with unknown model IDs record zero cost while preserving other metrics.

- Creates a sync_file event with an unrecognized model name
- Verifies file_runs and token counts are tracked normally
- Asserts cost_usd equals 0.0 when model pricing is unavailable
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_retries_grouped_by_reason fingerprint=87a990082b97658c25c4a4469a4716d6096f8fd968f8812fc0676cfbaa3a22f0 body_fp=5ff408dc94eca520cce082f8b2f66aabfa173b0101de24a776ef0d237acf73a7 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
## `def test_retries_grouped_by_reason(tmp_path: Path)`

Tests that retry events are aggregated by reason and total counts/delays computed correctly.

- Verifies `total` equals count of all retry events
- Verifies `by_reason` groups retry counts by failure type
- Verifies `total_delay_seconds` sums all delay durations
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_zero_retries_when_no_events fingerprint=b03fe825bbcaefc0331179f700f7c9993419081cbeca61fd371d8afc38595415 body_fp=9ba64378e806dadf20b6d2e439042b870a3779ee5f86cf7757f20247e3c874d2 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
## `def test_zero_retries_when_no_events(tmp_path: Path)`

Verifies that AuditSummary correctly reports zero retries when the log contains no model_call_retry events.

- Creates a log file with only a scan event (no retry events)
- Asserts that retries.total equals 0
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_invocations_counted fingerprint=bd6aeaf1d02bf5e62edc832cb0483789c7683f42ba3025638ba6d6e304e3cf90 body_fp=ffa199ab1375485ee924ab7ae389227c67fc53ee96edef24f6bd09419f47cc99 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
## `def test_cli_invocations_counted(tmp_path: Path)`

Tests that AuditSummary.cli_invocations correctly aggregates CLI subcommand counts from "cli" events.

- Creates JSONL with sync/verify invocations and verifies count tallies match expected totals
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:_render_to_string fingerprint=a7b633e28363b8b05b2a1fbcb14505272df321ce9637266f07dd810f3aa74bdc body_fp=3de8645c9078ce0d04ecaacfcdfe5f92d81788ae53aaf80b7d95bbc37da38c5c source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
## `def _render_to_string(fn, *args) -> str`

Captures render function output as plain text string by redirecting to StringIO buffer.

- Sets `force_terminal=False` to strip ANSI escape codes for testing
- Uses fixed width of 120 characters for consistent output
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_render_single_summary_includes_counts fingerprint=9df6bd18ba5368b9da29768e39fef43adc284fec13eaa91d72f6c6bc39b68231 body_fp=2427458ae3811b63e8ae3ed4e9a46a22ec8d30bce40c63fe831fc3b0f351704a source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
## `def test_render_single_summary_includes_counts(tmp_path: Path)`

Verifies that `render` produces output containing key section headers and numeric data from the audit summary.

- Creates a test log with one MCP call and one sync event
- Renders the summary to a string buffer and checks for presence of expected content
- Asserts that rendered output includes "MCP calls", tool name, "Sync" section, and numeric values
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_render_empty_log_does_not_crash fingerprint=5cf202e5e064141630a0f007d069e00512d3f4ae177aa7979d36f030b4b4a337 body_fp=ef831df71b36b4ff7132c53a8ed3abb12ae486dde5e9454aa6bae139e908c6fe source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
## `def test_render_empty_log_does_not_crash(tmp_path: Path)`

Verifies the render function handles empty audit logs gracefully without raising exceptions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_render_comparison_includes_both_paths fingerprint=06969b33c19c1ef5fdc076f8cd9f13ec312712f6180328118dda042592445321 body_fp=ae9b8e65f95b1f8a2045c0132e7a51701b97d835ed24c86eb656b41415f5b6a7 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test -->
## `def test_render_comparison_includes_both_paths(tmp_path: Path)`

Tests that `render_comparison` displays both log filenames and correctly shows deltas between runs.

- Creates two JSONL audit logs with different MCP call counts
- Verifies both filenames appear in the comparison output  
- Confirms delta column shows "+1" for the additional read call in the second log
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_render_comparison_includes_cli_call_diff fingerprint=8f671d41f58ef1b6381d0a7f96c2b0bd82ae69a85673a012940589d463ccd028 body_fp=1b101425ef68209b8646c7f8d930b5bbcbeb2108eee148734946f7f0bc226fb7 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
## `def test_render_comparison_includes_cli_call_diff(tmp_path: Path)`

Tests that `render_comparison` shows MCP and CLI call surfaces in separate tables with correct deltas.

- Creates baseline log with one MCP grep call and candidate log with same MCP call plus additional CLI grep call
- Verifies comparison output contains both "MCP calls" and "CLI calls" section headers
- Confirms the "+1" delta appears in CLI table specifically, not combined with MCP counts
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_audit_help_lists_log_option fingerprint=b5b79bb7880bf3f0c12b233a264c4d1060f77f1458cd607ac62a33b11e1e9a98 body_fp=b8130ffe64c8b095fa35a582bf33441c08a1d1958d2019106aa31e40fb6b7965 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
## `def test_cli_audit_help_lists_log_option()`

Tests that `audit --help` command shows the `--log` option in its help output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_audit_runs_against_explicit_log fingerprint=3a2fc0a8689698cda13d3a658b4ef902333dd0a09c67d2b75b00584d9acdf8cb body_fp=e0746cb743f44fce1ef4259cf8c4e67be62375580250f1f6e8bc4105601a2e38 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
## `def test_cli_audit_runs_against_explicit_log(tmp_path: Path)`

Verifies that the audit CLI command runs successfully when given an explicit log file path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_audit_json_output fingerprint=1ebb633d9c86847eb818d78b992ff9c4d7a2bb2c919cca9d19efa0c6ee2e4b18 body_fp=b7df8df7d1606ebf2aecd608bcf03fc49d5d3052978de9f3405641c6ccc01c22 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
## `def test_cli_audit_json_output(tmp_path: Path)`

Tests that the audit CLI command produces valid JSON output when --json flag is used.

- Creates a test log with one MCP grep call
- Verifies the JSON output parses and contains expected count data
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_audit_compare_two_logs fingerprint=d789e6c8f87f7553aa544b19dfecdbfa46c8a87a734a44c6586252791f872daa body_fp=9397e6b92ac6e902f6d65681af58133631ee3bf7cf63dd445d6a0ccfd492ad32 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
## `def test_cli_audit_compare_two_logs(tmp_path: Path)`

Tests that the audit CLI command supports comparing two logs via the `--compare` option.

- Creates two identical log files with single grep events
- Verifies CLI exits successfully and output contains comparison indicators
- Confirms both log filenames appear in the rendered comparison output
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_audit_missing_log_exits_nonzero fingerprint=960f50e897c51b014da29ce985a928538142159c5389629c917635569d710dbe body_fp=0b20c028a56e2a453ffa316eb7c51668ddd00f8750e86f4d5adf758fcd39ccd3 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test-infrastructure -->
## `def test_cli_audit_missing_log_exits_nonzero(tmp_path: Path)`

Tests that the audit CLI command exits with non-zero status when the specified log file does not exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_summarise_directly_with_event_list fingerprint=5a50e6ff212176e95879a868884ee2fd952cb70d899925a4581956158416ec1d body_fp=76f3bdcdb3d1d5bd0ce230b8d76c0285e90f09f47428deb8ce5f880071e069fb source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb role=test -->
## `def test_summarise_directly_with_event_list()`

Tests the direct `_summarise` function with a list of Event objects bypassing file parsing.

- Creates synthetic Event objects for `mcp_call` events with grep and read tools
- Verifies that tool counts and read qname tracking work correctly through the direct interface
- Provides a fast path for fixture-based testing without requiring JSONL file creation
<!-- trie:end -->