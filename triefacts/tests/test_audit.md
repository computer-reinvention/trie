---
trie_version: 0.1.5
source: tests/test_audit.py
file_fingerprint: 3b93436d7a1eacb3ad160ec6ff447e4a925164865470ab188b00773ee8e8532a
last_synced_at: '2026-05-23T23:21:48Z'
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
<!-- trie:section symbol=tests/test_audit:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=02e1ff02db52a025d6464ec4b2739acab9a0a56b717c52855cda78eedf69b9d1 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `tests/test_audit`

Test suite for JSONL audit ingestion and rendering contracts.

- Covers `Event` parsing, `AuditSummary` aggregation (MCP, CLI, sync, retries, span), cost computation, renderer smoke tests, and CLI command behaviour.
- Malformed/blank lines must degrade to `parse.lines_malformed`, never crash.
- Both `FULL_MODEL` and `BARE_MODEL` forms are exercised to validate cost fallback for legacy logs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:FULL_MODEL fingerprint=ff1e35768cf136d376f0ea56a2898853998578f19d1f3d483d687562d9caf7e2 body_fp=f717bd4150999eaff0634d4c24e329a34842fa9a2c7a65153ebde9e53ac1f0f9 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `FULL_MODEL = "anthropic/claude-sonnet-4-6"`

Model ID string using the full provider-prefixed path, exercising post-fix audit cost resolution.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:BARE_MODEL fingerprint=b4adc561ff544880ff4d1080888606d88266fcf67c4a3a7a5a8c746f837b6009 body_fp=6579f8cf0dde26b02ab552484eb0eb533dc567961de0fc3a64fd2d5f9d395696 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `BARE_MODEL = "claude-sonnet-4-6"`

Legacy bare model name used to test cost estimation fallback for older debug logs lacking the provider prefix.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:ANTHROPIC_MODEL fingerprint=44b085589a51447c608dba58dc112c8b95ef64bdf829ad7bb15248e2a566b787 body_fp=0f86947748beb773a54835c3a7a61d6a19502b1812f3e649dae6cf9502066823 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `ANTHROPIC_MODEL = FULL_MODEL`

Alias for `FULL_MODEL`; tests needing the legacy bare-name shape override this locally.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:_write_log fingerprint=a49508ce8be7dce58721d370cb6b7acb6cc781d292b1e5962eb6c44d3ccb8278 body_fp=a58de9990f2591af80f06763559eed84277386a78688e82fb284763ae3f9fcf9 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `_write_log(path: Path, records: list[dict]) -> None`

Write `records` as JSONL to `path`; an empty list produces a zero-byte file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:_ts fingerprint=a22cf186c33161d9a1c3fe2c563c1b03f88d44ea52576190d5f961cfb38aaf3a body_fp=501e6124bfa9adc32c56f5ecc0bfe1cdf1ec9fb4b6bf2e4fbeaf24451494516f source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `_ts(i: int) -> str`

Generate a monotonically increasing ISO-8601 timestamp string from an integer second offset.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_event_from_json_parses_well_formed_line fingerprint=44a73a735655a5b51b438004f04ecb9592f6f4329b944689803de4455dacb601 body_fp=3b1a7eafeb06d9ccc782a7e0efcb5c0ac23fff01e53606f590ba02cd9cf1b8f3 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_event_from_json_parses_well_formed_line()`

Verify that `Event.from_json` correctly parses a valid JSONL line into `event`, `ts`, and `fields`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_event_from_json_returns_none_on_empty_and_garbage fingerprint=a327dd89a1c14a919a90bcf43a686e7ee3d15adf0ea3379d916f41fa952ad812 body_fp=fb06ae8df2e8a7e6fcd8457ec86ffc25d748fae8e42bf13cb05fe26210737308 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_event_from_json_returns_none_on_empty_and_garbage()`

Verify `Event.from_json` returns `None` for blank input, invalid JSON, non-object roots, and missing required fields.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_from_log_raises_when_file_missing fingerprint=acaf8175631acb18e813cc186c908b2718df5051d5dd709a191422dd8ff83ac2 body_fp=6fe397ab899999cb3f53a467800eef679f1c248b0d0ed7f4cf815c00b94fb111 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_from_log_raises_when_file_missing(tmp_path: Path)`

Assert that `AuditSummary.from_log` raises `FileNotFoundError` for a non-existent path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_from_log_empty_file_yields_empty_summary fingerprint=7a9c7b54c7f993208b60945afadd8147f60b8144ff766301db64b6c4d99ec046 body_fp=6383245e3c9f46e602eb406b3fa6e8fadb27949a6381cb6e4ec7e837a714a163 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_from_log_empty_file_yields_empty_summary(tmp_path: Path)`

Assert that `AuditSummary.from_log` on a zero-byte file produces zeroed parse counts, empty `mcp`/`cli` dicts, and `None` span fields.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_from_log_counts_malformed_lines fingerprint=987feaff79fa266aca1552d0a1fa731fc0f28230d77dd418cf153ab2cc1f0412 body_fp=6e88c59d7a276e3b3eaba2ff0aa2d807b0c384d408c0d059d60bdcf16f3cbca3 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_from_log_counts_malformed_lines(tmp_path: Path)`

Verify that blank lines and invalid JSON both increment `parse.lines_malformed` without crashing `AuditSummary.from_log`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_from_log_computes_span fingerprint=40dad95519eb3182c54e4aaefd2cbaee945088f9065d0adfb4b61b4428e92a54 body_fp=bfae83aba0f4318164adfd34e558fbaee19d44b1898fec49dc07413780374744 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_from_log_computes_span(tmp_path: Path)`

Verify that `AuditSummary.from_log` derives `span_start`, `span_end`, and `span_duration_seconds` from the min/max timestamps across all event types.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_mcp_call_buckets_per_tool fingerprint=d71df265f3618b55c6e5b8501dccde19387072e462ad4afcf7b8a8f60330d146 body_fp=9e9b60f8b5ef492dd0d953de57fda6e2af855e438a3d912d5e5ab1c44aa6438a source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_mcp_call_buckets_per_tool(tmp_path: Path)`

Verify `AuditSummary.mcp` correctly buckets per-tool counts, errors, empty results, average duration, `not_found` count, top qnames, and hub-truncated trace detection across grep, read, and trace tools.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_read_empty_prose_counts_as_empty_result fingerprint=8d063b6bd968a17964e60624c799bc9d41769f0cd20cac8a0416745a4eec7b58 body_fp=2f912e3b233268cf92fa0f66290b2c4a70f860eb6ab8a9ed11038c81cee3db27 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_read_empty_prose_counts_as_empty_result(tmp_path: Path)`

Assert that a `read` `mcp_call` returning `prose_chars=0` increments `empty_result_count`, not `error_count`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_mcp_calls_without_capture_args_still_count fingerprint=5f02e9f8ce0df07156bac5d496b1b76e742a0ebd2a0fbec017af6cbf3d0bf787 body_fp=039103e2d879b2df81dc310a702da0d88f053a719b058f42d5d737ff01dac45a source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_mcp_calls_without_capture_args_still_count(tmp_path: Path)`

Verify that an `mcp_call` event missing the `args` field still increments the call count with an empty `top_qnames`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_call_aggregation_buckets_per_tool fingerprint=9173ee008fb26aeb11a2ab9b499f0c944df0963b36fd9edbb6d2ea474b657519 body_fp=c411a5ba0cc0f68c349c4b1a2d2ea926a4f72640010958557152d338f7030316 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_cli_call_aggregation_buckets_per_tool(tmp_path: Path)`

Verify that mixed `cli_call` events are bucketed into `summary.cli` per tool with correct count, empty-result, and qname stats.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_call_and_mcp_call_are_separate_streams fingerprint=2066288cbb5d2b0b96a62cd7b0b160a49830bdf1aa4b274efff01523a67a203c body_fp=ab52c9d870bc8d8746f9bcf445325815ee7c52b34254f42851d696121dfe2dc2 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_cli_call_and_mcp_call_are_separate_streams(tmp_path: Path)`

Assert that `mcp_call` and `cli_call` events for the same tool populate `summary.mcp` and `summary.cli` independently, with no cross-contamination.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_to_dict_carries_cli_section fingerprint=4169576f5cf154f67c1b7b72d029a29a767cf9ccd66b92bdf2d347dc95a226ce body_fp=f60dae475a759011344f5e46821179acb0557e8310b52d6bdf4cd41c31128b3c source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_to_dict_carries_cli_section(tmp_path: Path)`

Assert that `AuditSummary.to_dict()` includes a `cli` key with the same per-tool field shape as `mcp`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_read_mode_breakdown_aggregates_from_cli_call_events fingerprint=7846b4cf97a29f5409f0866aa00fcb3f57fde1d1ddd38c31343b55d47c288bff body_fp=00e8f251420a51cf2292cecc2fb3e5e8af5859163101b003d713efe0741e4f8a source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_read_mode_breakdown_aggregates_from_cli_call_events(tmp_path: Path)`

Verify that `cli_call` events carrying a `mode` field are counted into `McpCallStats.modes` keyed by dispatch branch name.

- `modes`: asserted to equal `{"triefact_compact": 2, "triefact_full": 1, "source": 1, "show_source": 1}`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_read_events_without_mode_field_count_as_qname fingerprint=239e047d3a3191b56c46c4400027a51f3630bff20b5ea2ab1ffebdcda1c9a5eb body_fp=73b54873a921fcd1ee4db8f0ca6f9484e40f7e6edb22ac6865ceb98a9e59175b source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_read_events_without_mode_field_count_as_qname(tmp_path: Path)`

Assert that `cli_call` events lacking a `mode` field are attributed to `"qname"` in `McpCallStats.modes`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_sync_aggregation_totals_and_cost fingerprint=dfed249ef4bc999064cdb424a8f6aa695dc868332633b0334360e84d5eb1610d body_fp=27d9097e33bfbc55bca5ed838406d87585d816813884d3508589c96c183a16ac source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_sync_aggregation_totals_and_cost(tmp_path: Path)`

Verify that two `sync_file` events are correctly summed across all token, symbol, regen-mode, and cost fields in `AuditSummary.sync`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_sync_with_legacy_bare_model_name_still_costs fingerprint=19898e184915fb26dfae5e642b70bd752549860d5c03b2755117b5aa82bbad84 body_fp=b05619db88249faf2ded9ba2f12a6f9f27d1dbb3d1c832f55489824b1bc14cbe source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_sync_with_legacy_bare_model_name_still_costs(tmp_path: Path)`

Assert that `AuditSummary` produces non-zero cost when a `sync_file` event carries a bare model name instead of the full provider-prefixed id.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_sync_with_unknown_model_records_zero_cost fingerprint=ec9a55613a3b6739103cafb44d946a4d3deccb2e5b1ea0893898e87c469177c5 body_fp=cedd331b591560a2c9b5e958b427f806ef4dcd3a8fff0318d8e575b29c99941d source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_sync_with_unknown_model_records_zero_cost(tmp_path: Path)`

Assert that a `sync_file` event with an unrecognised model ID records zero cost while still counting tokens and file runs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_retries_grouped_by_reason fingerprint=87a990082b97658c25c4a4469a4716d6096f8fd968f8812fc0676cfbaa3a22f0 body_fp=7bb2788361d44b37d48bc1f8b6e602e532c98b4a63f410ff74521ea07a6776ab source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_retries_grouped_by_reason(tmp_path: Path)`

Verify that `model_call_retry` events are counted by reason and summed by total delay.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_zero_retries_when_no_events fingerprint=b03fe825bbcaefc0331179f700f7c9993419081cbeca61fd371d8afc38595415 body_fp=dd75dbde842209b225b018613d6bf763375cde52dee38ce388ce7caee8559c1f source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_zero_retries_when_no_events(tmp_path: Path)`

Assert that `AuditSummary.retries.total` is zero when the log contains no `model_call_retry` events.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_invocations_counted fingerprint=bd6aeaf1d02bf5e62edc832cb0483789c7683f42ba3025638ba6d6e304e3cf90 body_fp=b2d4481a2b61ea741689cc740e7e2a4131899acdadf848b8e7b4501d817c7e64 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_cli_invocations_counted(tmp_path: Path)`

Assert that `cli` events are counted per subcommand and accumulated in `summary.cli_invocations`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:_render_to_string fingerprint=a7b633e28363b8b05b2a1fbcb14505272df321ce9637266f07dd810f3aa74bdc body_fp=ff77e27c2fd9744c8da7888b20a65365e216ee20045bad74b8d89df401d450bc source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `_render_to_string(fn, *args) -> str`

Invoke a render function with a plain-text `Console` and return the captured output as a string.

- `fn`: callable accepting positional args followed by a `Console` instance.
- `force_terminal=False`: strips ANSI escape codes for plain-text assertions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_render_single_summary_includes_counts fingerprint=9df6bd18ba5368b9da29768e39fef43adc284fec13eaa91d72f6c6bc39b68231 body_fp=ee096524a8a9467354f2bf390a2bd240061b2cfb7c5f560fb34b2be0662386f3 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_render_single_summary_includes_counts(tmp_path: Path)`

Verify that `render` produces output containing MCP call section, tool name, sync section, and numeric counts for a mixed-event log.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_render_empty_log_does_not_crash fingerprint=5cf202e5e064141630a0f007d069e00512d3f4ae177aa7979d36f030b4b4a337 body_fp=587241dbd0d8c333d7865fa46f4e7eeac3449c1781589508756c3fc0fe4db0ea source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_render_empty_log_does_not_crash(tmp_path: Path)`

Assert that `render` completes without raising on an empty log and produces output containing "none" or "no".
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_render_comparison_includes_both_paths fingerprint=06969b33c19c1ef5fdc076f8cd9f13ec312712f6180328118dda042592445321 body_fp=5887f24453e815453fba2ef22debfae04412792a567e6e3eb88ad84542d59ad1 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_render_comparison_includes_both_paths(tmp_path: Path)`

Assert that `render_comparison` names both log files and shows a `+1` delta when the candidate log has one extra `mcp_call` tool.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_render_comparison_includes_cli_call_diff fingerprint=8f671d41f58ef1b6381d0a7f96c2b0bd82ae69a85673a012940589d463ccd028 body_fp=71b2643c65791e9c1c1e6b27c8ef3e7e63f4d3b59216fccfc6e40da3b0b23616 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_render_comparison_includes_cli_call_diff(tmp_path: Path)`

Assert that `render_comparison` renders MCP and CLI call surfaces as separate tables, with deltas scoped correctly to each surface.

- Baseline log: one `mcp_call` grep; candidate log adds one `cli_call` grep.
- Verifies both "MCP calls" and "CLI calls" headings appear and `+1` delta is present.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_audit_help_lists_log_option fingerprint=b5b79bb7880bf3f0c12b233a264c4d1060f77f1458cd607ac62a33b11e1e9a98 body_fp=ef5d94b14d28a343ef48eb1dd4638a01675ad55cb1461d77ea5ff9a73d54ce68 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_cli_audit_help_lists_log_option()`

Assert the `audit` CLI subcommand exits cleanly and advertises `--log` in its help output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_audit_runs_against_explicit_log fingerprint=3a2fc0a8689698cda13d3a658b4ef902333dd0a09c67d2b75b00584d9acdf8cb body_fp=a5e1ebacf14f424ebb45c102a562819940bbeb8e5ac2b102685d4386f1fd6746 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_cli_audit_runs_against_explicit_log(tmp_path: Path)`

Verify that `trie audit --log <path>` exits zero against a minimal real JSONL log.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_audit_json_output fingerprint=1ebb633d9c86847eb818d78b992ff9c4d7a2bb2c919cca9d19efa0c6ee2e4b18 body_fp=29ccc49db75de8ece4ac7d8a04bc646536bf31d9ebcbfdda125e2b6c7d992ab8 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_cli_audit_json_output(tmp_path: Path)`

Verify that `audit --json` exits cleanly and emits valid JSON with correct MCP tool counts.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_audit_compare_two_logs fingerprint=d789e6c8f87f7553aa544b19dfecdbfa46c8a87a734a44c6586252791f872daa body_fp=e8c80085ae46ad775878da2240a0a74415b47a67fb1df992f345890e00209ff1 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_cli_audit_compare_two_logs(tmp_path: Path)`

Verify the `audit --compare` CLI flag exits zero and names both log files in its output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_cli_audit_missing_log_exits_nonzero fingerprint=960f50e897c51b014da29ce985a928538142159c5389629c917635569d710dbe body_fp=a6734a8a5ad82a5ca50d723bdb2bb40c401f716ae540272ad17ebd3f6439e938 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_cli_audit_missing_log_exits_nonzero(tmp_path: Path)`

Assert the `audit` CLI command exits with a non-zero code when the specified log file does not exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_audit:test_summarise_directly_with_event_list fingerprint=5a50e6ff212176e95879a868884ee2fd952cb70d899925a4581956158416ec1d body_fp=01f21eefcb57647eec48968e12a967bcf081b9bfe7a6f5aa78c0f05bcdafbc50 source_ref=7b5ee3d5f7adab6f8ba5f38a4f9896e457c14fdb -->
## `test_summarise_directly_with_event_list()`

Verify that `_summarise` correctly aggregates a hand-built `Event` list into per-tool MCP buckets, including `top_qnames`.
<!-- trie:end -->