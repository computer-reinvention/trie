---
trie_version: 0.1.2
source: tests/test_audit.py
file_fingerprint: 3b93436d7a1eacb3ad160ec6ff447e4a925164865470ab188b00773ee8e8532a
last_synced_at: '2026-05-19T15:19:17Z'
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
<!-- trie:section symbol=tests/test_audit:_write_log fingerprint=a49508ce8be7dce58721d370cb6b7acb6cc781d292b1e5962eb6c44d3ccb8278 body_fp=08ed690e43e8bb6e3ac012401caafee8453a888205fd3ff3f84303b9eb4d9e52 source_ref=1016ef16cd8f0c58806f1645f82b8759c5077b48 -->
## `_write_log(path: Path, records: list[dict]) -> None`

Write records as JSONL to `path`; an empty list produces a zero-byte file.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:_ts fingerprint=a22cf186c33161d9a1c3fe2c563c1b03f88d44ea52576190d5f961cfb38aaf3a body_fp=65eff3f48ffcf7b5a4b898a54f9433dce888ed54aac480f4aa2d33acb911b30e source_ref=1016ef16cd8f0c58806f1645f82b8759c5077b48 -->
## `_ts(i: int) -> str`

Return a zero-padded ISO-8601 timestamp string for use as a monotonic ordering key in tests.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_event_from_json_parses_well_formed_line fingerprint=44a73a735655a5b51b438004f04ecb9592f6f4329b944689803de4455dacb601 body_fp=2ec5142882ae3c2debb8425150a646a09a264684caf195144417f9da6ed13e97 source_ref=1016ef16cd8f0c58806f1645f82b8759c5077b48 -->
## `test_event_from_json_parses_well_formed_line()`

Verify that `Event.from_json` correctly parses a well-formed JSONL line into `event`, `ts`, and `fields`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_event_from_json_returns_none_on_empty_and_garbage fingerprint=a327dd89a1c14a919a90bcf43a686e7ee3d15adf0ea3379d916f41fa952ad812 body_fp=3c013d01deb44adedbccc3c61cb865623e55033e156cd5f2aa672cb2ed894df2 source_ref=1016ef16cd8f0c58806f1645f82b8759c5077b48 -->
## `test_event_from_json_returns_none_on_empty_and_garbage()`

Verify `Event.from_json` returns `None` for empty strings, whitespace, invalid JSON, non-object roots, and missing required fields.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_from_log_raises_when_file_missing fingerprint=acaf8175631acb18e813cc186c908b2718df5051d5dd709a191422dd8ff83ac2 body_fp=6fe397ab899999cb3f53a467800eef679f1c248b0d0ed7f4cf815c00b94fb111 source_ref=1016ef16cd8f0c58806f1645f82b8759c5077b48 -->
## `test_from_log_raises_when_file_missing(tmp_path: Path)`

Assert that `AuditSummary.from_log` raises `FileNotFoundError` for a non-existent path.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_from_log_empty_file_yields_empty_summary fingerprint=7a9c7b54c7f993208b60945afadd8147f60b8144ff766301db64b6c4d99ec046 body_fp=06b032059b95bae064372fd8ad21a2d4a914be1b1d387360b6e5a6ea68a3677f source_ref=cb94ee99a2944523034daac6d7b1884723dd84ec -->
## `test_from_log_empty_file_yields_empty_summary(tmp_path: Path)`

Assert that parsing a zero-byte JSONL file produces an `AuditSummary` with all counters at zero/None, including an empty `cli` bucket.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_from_log_counts_malformed_lines fingerprint=987feaff79fa266aca1552d0a1fa731fc0f28230d77dd418cf153ab2cc1f0412 body_fp=0e0013d76fe2a4a6953d4b888e5d0a4e75e34ec367d883c2f126e4a6c0897215 source_ref=1016ef16cd8f0c58806f1645f82b8759c5077b48 -->
## `test_from_log_counts_malformed_lines(tmp_path: Path)`

Verify that invalid JSON and blank lines increment `lines_malformed` without raising.

- `lines_total` counts all four raw lines; `lines_parsed` counts only the two valid ones.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_from_log_computes_span fingerprint=40dad95519eb3182c54e4aaefd2cbaee945088f9065d0adfb4b61b4428e92a54 body_fp=f13f0f4c5170488110a85907dd0021dab8aa68d7e1bd86f0da9f5b9ba883130c source_ref=ee7d0fdea4864e7b19aa3bc740e8dfc57f4281cd -->
## `test_from_log_computes_span(tmp_path: Path)`

Verify that `AuditSummary.from_log` derives correct `span_start`, `span_end`, and `span_duration_seconds` from out-of-order timestamps.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_mcp_call_buckets_per_tool fingerprint=d71df265f3618b55c6e5b8501dccde19387072e462ad4afcf7b8a8f60330d146 body_fp=4072254d6716dc072efd2edc362027f40de4d7c56b635bf65a94a652de68a195 source_ref=ee7d0fdea4864e7b19aa3bc740e8dfc57f4281cd -->
## `test_mcp_call_buckets_per_tool(tmp_path: Path)`

Verify MCP tool aggregation buckets counts, errors, empty results, durations, and qnames per distinct tool.

- `grep`: 3 calls, 1 error, 1 empty (`result_count==0`)
- `read`: 2 calls, 1 error, 1 `not_found`, top qname recorded
- `trace`: 1 call, counted as empty when `nodes_count==1`
<!-- trie:end -->



<!-- trie:section symbol=tests/test_audit:test_mcp_calls_without_capture_args_still_count fingerprint=5f02e9f8ce0df07156bac5d496b1b76e742a0ebd2a0fbec017af6cbf3d0bf787 body_fp=039103e2d879b2df81dc310a702da0d88f053a719b058f42d5d737ff01dac45a source_ref=ee7d0fdea4864e7b19aa3bc740e8dfc57f4281cd -->
## `test_mcp_calls_without_capture_args_still_count(tmp_path: Path)`

Verify that an `mcp_call` event missing the `args` field still increments the call count with an empty `top_qnames`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_sync_aggregation_totals_and_cost fingerprint=dfed249ef4bc999064cdb424a8f6aa695dc868332633b0334360e84d5eb1610d body_fp=b49eb1e3dc69610f8480d045e15dbc7799b5f71af8ba8f60214a2bc22c417570 source_ref=1016ef16cd8f0c58806f1645f82b8759c5077b48 -->
## `test_sync_aggregation_totals_and_cost(tmp_path: Path)`

Verify that two `sync_file` events are correctly aggregated into totals for tokens, counts, modes, cost, and per-model bucketing.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_sync_with_legacy_bare_model_name_still_costs fingerprint=19898e184915fb26dfae5e642b70bd752549860d5c03b2755117b5aa82bbad84 body_fp=72805edb7276437dd87ab36fcb3463a6a1b76cd8dad9e94e373028cb743a6e9a source_ref=1016ef16cd8f0c58806f1645f82b8759c5077b48 -->
## `test_sync_with_legacy_bare_model_name_still_costs(tmp_path: Path)`

Verify that a bare model name (without provider prefix) in older log files still produces a non-zero cost.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_sync_with_unknown_model_records_zero_cost fingerprint=ec9a55613a3b6739103cafb44d946a4d3deccb2e5b1ea0893898e87c469177c5 body_fp=cedd331b591560a2c9b5e958b427f806ef4dcd3a8fff0318d8e575b29c99941d source_ref=1016ef16cd8f0c58806f1645f82b8759c5077b48 -->
## `test_sync_with_unknown_model_records_zero_cost(tmp_path: Path)`

Assert that a `sync_file` event with an unrecognised model ID records zero cost while still counting tokens and file runs.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_retries_grouped_by_reason fingerprint=87a990082b97658c25c4a4469a4716d6096f8fd968f8812fc0676cfbaa3a22f0 body_fp=a258b15efebba5d3ad02c12e8c0a4af3e325028be3f55a4e89816dc3d9c44dd4 source_ref=1016ef16cd8f0c58806f1645f82b8759c5077b48 -->
## `test_retries_grouped_by_reason(tmp_path: Path)`

Verify that retry events are counted per-reason and total delay is summed correctly.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_zero_retries_when_no_events fingerprint=b03fe825bbcaefc0331179f700f7c9993419081cbeca61fd371d8afc38595415 body_fp=9ff68e01fabc7f68dfe7fe065eaeab6b03f1c3a802dcd7449c7af497873d1ff3 source_ref=1016ef16cd8f0c58806f1645f82b8759c5077b48 -->
## `test_zero_retries_when_no_events(tmp_path: Path)`

Assert that `retries.total` is zero when the log contains no `model_call_retry` events.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_cli_invocations_counted fingerprint=bd6aeaf1d02bf5e62edc832cb0483789c7683f42ba3025638ba6d6e304e3cf90 body_fp=15da3a9d641cf43abacb49d07269b3e7d82c17a4f14c45a68173bca4d0a0e6e9 source_ref=1016ef16cd8f0c58806f1645f82b8759c5077b48 -->
## `test_cli_invocations_counted(tmp_path: Path)`

Verify that `cli` events are grouped and counted per subcommand in `summary.cli_invocations`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:_render_to_string fingerprint=a7b633e28363b8b05b2a1fbcb14505272df321ce9637266f07dd810f3aa74bdc body_fp=9cf574174e458abe635f84a4cf2520926fd9efc857c7b8839133b7624f144449 source_ref=1016ef16cd8f0c58806f1645f82b8759c5077b48 -->
## `_render_to_string(fn, *args) -> str`

Invoke a render function with a plain-text Rich `Console` and return captured output.

- `fn`: callable accepting positional args followed by a `Console` instance.
- Returns ANSI-free string; `force_terminal=False` strips escape codes.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_render_single_summary_includes_counts fingerprint=9df6bd18ba5368b9da29768e39fef43adc284fec13eaa91d72f6c6bc39b68231 body_fp=bd9b11d1a19f7ee51ae3fd6245db8ed54ba979661a1e7553bd768afd363840ba source_ref=ee7d0fdea4864e7b19aa3bc740e8dfc57f4281cd -->
## `test_render_single_summary_includes_counts(tmp_path: Path)`

Assert that `render` output contains MCP tool names, section headers, and numeric counts from a two-event log.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_render_empty_log_does_not_crash fingerprint=5cf202e5e064141630a0f007d069e00512d3f4ae177aa7979d36f030b4b4a337 body_fp=418d26b3f88d83798a133c327a1ad5a9e3d38af6888cfc349487946cd7fd7918 source_ref=1016ef16cd8f0c58806f1645f82b8759c5077b48 -->
## `test_render_empty_log_does_not_crash(tmp_path: Path)`

Assert that `render` on an empty log completes without raising and produces output containing "none" or "no".
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_render_comparison_includes_both_paths fingerprint=06969b33c19c1ef5fdc076f8cd9f13ec312712f6180328118dda042592445321 body_fp=eb7cb32a7728333d74cd121c7e2910b198294350f64e8af5f183378140e5f66a source_ref=ee7d0fdea4864e7b19aa3bc740e8dfc57f4281cd -->
## `test_render_comparison_includes_both_paths(tmp_path: Path)`

Verify that `render_comparison` output names both log files and shows a `+1` delta for the extra read call in the second log.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_cli_audit_help_lists_log_option fingerprint=b5b79bb7880bf3f0c12b233a264c4d1060f77f1458cd607ac62a33b11e1e9a98 body_fp=ce662d67aeb203c994e1eae6fcf70d330f0d5f2afc672ef7947d5aab0e179611 source_ref=1016ef16cd8f0c58806f1645f82b8759c5077b48 -->
## `test_cli_audit_help_lists_log_option()`

Assert that `audit --help` exits successfully and exposes `--log` in its output.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_cli_audit_runs_against_explicit_log fingerprint=3a2fc0a8689698cda13d3a658b4ef902333dd0a09c67d2b75b00584d9acdf8cb body_fp=b0355240b41d39589ecbafb1b68a73eac22e148b8378be8ef46a7013b99e49af source_ref=1016ef16cd8f0c58806f1645f82b8759c5077b48 -->
## `test_cli_audit_runs_against_explicit_log(tmp_path: Path)`

Verify the `audit` CLI command exits zero when given an explicit log file path.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_cli_audit_json_output fingerprint=1ebb633d9c86847eb818d78b992ff9c4d7a2bb2c919cca9d19efa0c6ee2e4b18 body_fp=c41cb36ac91d54246b90cab9bafd3e94847d399f045643870895c06f3e4fb282 source_ref=ee7d0fdea4864e7b19aa3bc740e8dfc57f4281cd -->
## `test_cli_audit_json_output(tmp_path: Path)`

Verify that `audit --json` exits cleanly and emits valid JSON with correct MCP call counts.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_cli_audit_compare_two_logs fingerprint=d789e6c8f87f7553aa544b19dfecdbfa46c8a87a734a44c6586252791f872daa body_fp=2420b98eb7eb756fdc0a73d22768c1d26542aa1e4ac196f27352509be2c31172 source_ref=ee7d0fdea4864e7b19aa3bc740e8dfc57f4281cd -->
## `test_cli_audit_compare_two_logs(tmp_path: Path)`

Verify the `audit --compare` CLI command renders a comparison table containing both log filenames and exits cleanly.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_cli_audit_missing_log_exits_nonzero fingerprint=960f50e897c51b014da29ce985a928538142159c5389629c917635569d710dbe body_fp=4741f782a50372575f911d1d9659b95051e8cd38493319f1d80a6b7d352d74b6 source_ref=1016ef16cd8f0c58806f1645f82b8759c5077b48 -->
## `test_cli_audit_missing_log_exits_nonzero(tmp_path: Path)`

Assert that the `audit` CLI exits with a non-zero code when the specified log file does not exist.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_summarise_directly_with_event_list fingerprint=5a50e6ff212176e95879a868884ee2fd952cb70d899925a4581956158416ec1d body_fp=1c80b90e4b408801feaf238a6fac6930a83fd5a2213598bbded0392519f5a307 source_ref=ee7d0fdea4864e7b19aa3bc740e8dfc57f4281cd -->
## `test_summarise_directly_with_event_list()`

Verify `_summarise` correctly buckets `mcp_call` events when called directly with a pre-built event list.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_read_empty_prose_counts_as_empty_result fingerprint=8d063b6bd968a17964e60624c799bc9d41769f0cd20cac8a0416745a4eec7b58 body_fp=0c212172a164325da528cae093a652c50b98355719be5888367b816a81edf361 source_ref=ee7d0fdea4864e7b19aa3bc740e8dfc57f4281cd -->
## `test_read_empty_prose_counts_as_empty_result(tmp_path: Path)`

Assert that a `read` MCP call returning `prose_chars=0` increments `empty_result_count`, not `error_count`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:FULL_MODEL fingerprint=ff1e35768cf136d376f0ea56a2898853998578f19d1f3d483d687562d9caf7e2 body_fp=426f39aebfa8d68f460bb27c88ca49f34d6f621735715f5a424f8d27ca470bf7 source_ref=cb94ee99a2944523034daac6d7b1884723dd84ec -->
## `FULL_MODEL = "anthropic/claude-sonnet-4-6"`

Test constant representing the full provider-prefixed model ID for cost-routing tests.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:BARE_MODEL fingerprint=b4adc561ff544880ff4d1080888606d88266fcf67c4a3a7a5a8c746f837b6009 body_fp=738f0a8ffb959a1f949cb93e8580322a5c0b50d3de32eae3d58b79cf9c317481 source_ref=cb94ee99a2944523034daac6d7b1884723dd84ec -->
## `BARE_MODEL = "claude-sonnet-4-6"`

Legacy bare model name used to test cost calculation when log entries lack the provider prefix.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:ANTHROPIC_MODEL fingerprint=44b085589a51447c608dba58dc112c8b95ef64bdf829ad7bb15248e2a566b787 body_fp=08500f0db5f7973f20d0b4360c5a30e4ff70a34120d531cbfe40e8dc3d7c0e68 source_ref=cb94ee99a2944523034daac6d7b1884723dd84ec -->
## `ANTHROPIC_MODEL = FULL_MODEL`

Alias for `FULL_MODEL` used as the default model identifier in sync test fixtures.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_cli_call_aggregation_buckets_per_tool fingerprint=9173ee008fb26aeb11a2ab9b499f0c944df0963b36fd9edbb6d2ea474b657519 body_fp=bab7eed64e14b20f5130adf779ef9ec0a8736a7cecdf36a6930db8aa50f7f075 source_ref=cb94ee99a2944523034daac6d7b1884723dd84ec -->
## `test_cli_call_aggregation_buckets_per_tool(tmp_path: Path)`

Verify that mixed `cli_call` events across grep, read, and trace tools populate `summary.cli` with correct per-tool counts, empty-result tracking, and qname attribution.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_cli_call_and_mcp_call_are_separate_streams fingerprint=2066288cbb5d2b0b96a62cd7b0b160a49830bdf1aa4b274efff01523a67a203c body_fp=cb684b8c1a728066bc744603734775944308e42bf80522974d1f2460937a9fc8 source_ref=cb94ee99a2944523034daac6d7b1884723dd84ec -->
## `test_cli_call_and_mcp_call_are_separate_streams(tmp_path: Path)`

Assert that `mcp_call` and `cli_call` events with the same tool name populate `summary.mcp` and `summary.cli` independently, without cross-contamination.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_to_dict_carries_cli_section fingerprint=4169576f5cf154f67c1b7b72d029a29a767cf9ccd66b92bdf2d347dc95a226ce body_fp=97387e73f112a8cebd14912c14e083ecaed84bfde524ae35b012387fdfaeead4 source_ref=cb94ee99a2944523034daac6d7b1884723dd84ec -->
## `test_to_dict_carries_cli_section(tmp_path: Path)`

Verify that `AuditSummary.to_dict()` includes a `cli` key with per-tool stats matching the shape of the `mcp` section.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_read_mode_breakdown_aggregates_from_cli_call_events fingerprint=7846b4cf97a29f5409f0866aa00fcb3f57fde1d1ddd38c31343b55d47c288bff body_fp=599b2e5307321a05d1e0964215dab040791a6de8789ad696bb87b96b88de29d1 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_read_mode_breakdown_aggregates_from_cli_call_events(tmp_path: Path)`

Verify that `cli_call` events with a `mode` field are rolled into `McpCallStats.modes` keyed by mode name.

- Emits five `cli_call` events: two `triefact_compact`, one `triefact_full`, one `source`, one `show_source`.
- Asserts `summary.cli["read"].modes == {"triefact_compact": 2, "triefact_full": 1, "source": 1, "show_source": 1}`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_read_events_without_mode_field_count_as_qname fingerprint=239e047d3a3191b56c46c4400027a51f3630bff20b5ea2ab1ffebdcda1c9a5eb body_fp=577e94978926fc7209b0ee9e454ac0fb16d7b898fedf6b4658bd49eec2d4619a source_ref=cb94ee99a2944523034daac6d7b1884723dd84ec -->
## `test_read_events_without_mode_field_count_as_qname(tmp_path: Path)`

Assert that `cli_call` events lacking a `mode` field are attributed to `qname` in `McpCallStats.modes`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:test_render_comparison_includes_cli_call_diff fingerprint=8f671d41f58ef1b6381d0a7f96c2b0bd82ae69a85673a012940589d463ccd028 body_fp=af0f397f350732f58edaef54397f7348fdcc02254508217bcec0649bc0e97698 source_ref=cb94ee99a2944523034daac6d7b1884723dd84ec -->
## `test_render_comparison_includes_cli_call_diff(tmp_path: Path)`

Verify that `render_comparison` shows MCP and CLI call surfaces in separate tables with correct deltas.

- Baseline has one MCP grep; candidate adds one CLI grep, leaving MCP count unchanged.
- Asserts both "MCP calls" and "CLI calls" headings appear and `+1` reflects only the CLI delta.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_audit:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=bcf9eb9d1f0e2d89472329ad5241b23797e2059f0c353d3f3f77489b82a6bcd5 source_ref=cb94ee99a2944523034daac6d7b1884723dd84ec -->
## `tests/test_audit`

Test suite for JSONL audit log ingestion and rendering in `trie.audit`.

- Covers `Event.from_json`, `AuditSummary.from_log`, `_summarise`, `render`, `render_comparison`, and the `audit` CLI command.
- Verifies per-tool MCP and CLI call bucketing, sync cost, retry grouping, span computation, malformed-line degradation, and comparison delta rendering.
<!-- trie:end -->