---
trie_version: 0.2.1
source: trie/audit.py
file_fingerprint: 208d789eb2ce515f8bf241ee25c699c8f7f5f367b0680fbce6464d4264e62b0a
last_synced_at: '2026-08-01T01:52:05Z'
description: Post-hoc analysis of `debug.jsonl` telemetry logs.
defines:
- kind: module
  qualified_name: trie/audit:__module__
  lines: 1-955
- kind: class
  qualified_name: trie/audit:Event
  lines: 50-82
- kind: method
  qualified_name: trie/audit:Event.from_json
  lines: 64-82
- kind: class
  qualified_name: trie/audit:McpCallStats
  lines: 91-132
- kind: method
  qualified_name: trie/audit:McpCallStats.avg_duration_ms
  lines: 127-128
- kind: method
  qualified_name: trie/audit:McpCallStats.avg_response_bytes
  lines: 131-132
- kind: class
  qualified_name: trie/audit:SyncStats
  lines: 136-158
- kind: class
  qualified_name: trie/audit:RetryStats
  lines: 162-167
- kind: class
  qualified_name: trie/audit:ParseStats
  lines: 171-176
- kind: class
  qualified_name: trie/audit:AuditSummary
  lines: 185-280
- kind: method
  qualified_name: trie/audit:AuditSummary.from_log
  lines: 212-242
- kind: method
  qualified_name: trie/audit:AuditSummary.to_dict
  lines: 244-280
- kind: function
  qualified_name: trie/audit:_stats_to_dict
  lines: 283-303
- kind: function
  qualified_name: trie/audit:_summarise
  lines: 311-375
- kind: function
  qualified_name: trie/audit:_mcp_stats
  lines: 378-458
- kind: constant
  qualified_name: trie/audit:_pricing_cache
  lines: 463-463
- kind: function
  qualified_name: trie/audit:_pricing_for
  lines: 466-479
- kind: function
  qualified_name: trie/audit:_sync_stats
  lines: 482-565
- kind: function
  qualified_name: trie/audit:_retry_stats
  lines: 568-579
- kind: function
  qualified_name: trie/audit:_cli_invocations
  lines: 582-587
- kind: function
  qualified_name: trie/audit:_span
  lines: 590-607
- kind: function
  qualified_name: trie/audit:render
  lines: 615-633
- kind: function
  qualified_name: trie/audit:render_comparison
  lines: 636-656
- kind: function
  qualified_name: trie/audit:_render_header
  lines: 662-677
- kind: function
  qualified_name: trie/audit:_render_mcp
  lines: 680-682
- kind: function
  qualified_name: trie/audit:_render_cli_calls
  lines: 685-693
- kind: function
  qualified_name: trie/audit:_render_tool_calls
  lines: 696-770
- kind: function
  qualified_name: trie/audit:_render_sync
  lines: 773-798
- kind: function
  qualified_name: trie/audit:_render_retries
  lines: 801-809
- kind: function
  qualified_name: trie/audit:_render_cli
  lines: 812-816
- kind: function
  qualified_name: trie/audit:_render_compare_header
  lines: 822-827
- kind: function
  qualified_name: trie/audit:_render_compare_mcp
  lines: 830-836
- kind: function
  qualified_name: trie/audit:_render_compare_cli_calls
  lines: 839-850
- kind: function
  qualified_name: trie/audit:_render_compare_tool_calls
  lines: 853-884
- kind: function
  qualified_name: trie/audit:_render_compare_sync
  lines: 887-911
- kind: function
  qualified_name: trie/audit:_render_compare_retries
  lines: 914-921
- kind: function
  qualified_name: trie/audit:_delta
  lines: 927-931
- kind: function
  qualified_name: trie/audit:_delta_money
  lines: 934-938
- kind: function
  qualified_name: trie/audit:_err_cell
  lines: 941-944
- kind: function
  qualified_name: trie/audit:_fmt_seconds
  lines: 947-954
incoming_refs: 60
outgoing_refs: 2
---
<!-- trie:section symbol=trie/audit:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=27ebf0972c553a8e38353e847ea285cfce2940715ead823ebfedde5c349e1aeb source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Post-hoc analysis of `debug.jsonl` telemetry logs to produce scriptable summaries.

Ingests telemetry from `trie sync`, `trie verify`, the MCP server, and model calls to analyze agent behavior. Provides focused summaries of:

- MCP tool usage by name with error counts and top queried qnames
- Sync activity including file count, symbols generated, tokens, and cost per model
- Retry behavior from rate-limiting, overloading, or timeouts
- CLI invocation counts for run shape visibility

Core classes include `AuditSummary` for single-run analysis via `from_log()`, and rendering functions for console output or side-by-side comparisons. Construction splits pure data pipeline from Rich-based renderer for testability.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:Event fingerprint=4f541f8d3d2bb0b895f2767d53ef25779e2040966277f1c1f2f2d70115027c1b body_fp=e435a5ece36d649ce8899f3bfe7870cdc8dfb15d1eddd00be3cca760ec97ed38 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Decodes one JSONL telemetry line into structured fields with timestamp and event type.

- `ts`: ISO timestamp string from telemetry emission
- `event`: Event type discriminator (e.g. "mcp_call", "sync_file")
- `fields`: All other JSON fields as flat dict for event-specific data
- `from_json()`: Parses JSONL line, returns None on malformed input to avoid crashes
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:Event.from_json fingerprint=a703f11e700aba5f7cc3f9ce0851ddc30910d7abf7a0e0e29a5d9094d7405cc8 body_fp=bd34c3c7436f0c1ddca45eb4988c3f0a78b3ada2036f56c9eef8d9aec6ea9e85 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Parses a JSONL telemetry line into an Event instance, returning None for malformed input to allow graceful error handling.

- Returns None for empty lines, JSON decode errors, non-dict objects, or missing required fields
- Extracts `ts` and `event` as top-level attributes, remaining fields stored in `fields` dict
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:McpCallStats fingerprint=167844760f03506f9f69113b943ea12a1520d48faa456d95d921ed477da74071 body_fp=277b1d25bc2cfbf541817882ab11f65ce2c395277146bf862862582cbdf13f71 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Aggregates statistics for one MCP tool invocation (grep/read/trace).

- `not_found_count`: tool-specific failures indicating agent passed invalid qname
- `empty_result_count`: tool returned no useful content despite success
- `fallback_kinds`: grep-specific breakdown of empty result causes  
- `modes`: read-specific dispatch branch tracking (qname/triefact/source/show_source)
- `top_qnames`: five most frequently requested symbol names
- `avg_duration_ms`: computed from total_duration_ms divided by count
- `avg_response_bytes`: computed from total_response_bytes divided by count
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:McpCallStats.avg_duration_ms fingerprint=84f86f6d52648051332f475bb2db0b3a1f00d72b9f17d5ae50742db4fa421a55 body_fp=28ebb75cb15d4936d0eaaeedb580af9d3c9a5d12b8a6b3255bef75e64fce8256 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
McpCallStats property returns average call duration in milliseconds, avoiding division by zero.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:McpCallStats.avg_response_bytes fingerprint=011d16cbf949693061e94de7dc3a2c520500347177086267b464f530e60d5b02 body_fp=a1639e0e491f6ba3eaf0eef1fda23e934cd3bf29f92a59b4f987c8318c198413 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Returns the average response size in bytes per MCP tool call, or 0.0 if no calls were made.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:SyncStats fingerprint=28cf1d88eb4a0e5a0951850dc3573d868f2eae7668870af42456d93313e285dc body_fp=57c55aea5ee091329a91e73f6cba94a5e28e59cb0bbe7f4ec5aae6dccee19ddb source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Aggregates every `sync_file` event in the log with derived cost calculations.

- `cold_count`: number of cold regeneration operations
- `diff_aware_count`: number of diff-aware regeneration operations
- `cost_usd`: computed via `estimate_actual_cost` against per-model pricing table
- `by_model`: per-model breakdown of file runs and token counts
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:RetryStats fingerprint=67878b92223cb78412169667fbf2f4e8901268f7ca09538b21d07e6467e73d6b body_fp=e5bb3536357ab31a41bd5c542bfa0846b8adeb473f04fc5ad117187662ff2146 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Aggregates `model_call_retry` events to track client backoff frequency and delay patterns.

- `by_reason`: breakdown of retry counts by reason (rate-limit, overloaded, timeout)
- `total_delay_seconds`: cumulative backoff time across all retries
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:ParseStats fingerprint=7b0640a9557a90cdb8287f36e1894dc529c70ddff0f77ec612cc5e5224a15f84 body_fp=4182d8cc84a5ea15fc17adfcf8c73acd3fc745729478efaf2e4d9bbbce9fc348 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Tracks JSONL parsing statistics for audit log ingestion.

- `lines_total`: Total lines read from the telemetry log file
- `lines_parsed`: Successfully decoded JSONL events 
- `lines_malformed`: Lines that failed JSON parsing or validation
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:AuditSummary fingerprint=41e3a4f551fb822aa8bc6dc38a73bee21e3f19f81193b45a2b7fef8446a269d6 body_fp=a104088cf71a29a9c60c856efaa9d5b563d0d28c13347df55c9c43c5a475da27 source_ref=dcd19d40dcef6d59dc6598f56f1fb68bb12fe211 role=model -->
Frozen dataclass aggregating telemetry statistics from a debug.jsonl log file.

- `log_path`: Source telemetry file
- `parse`: Line counts and malformed entries from JSONL ingestion
- `span_start`/`span_end`/`span_duration_seconds`: First and last timestamps plus duration
- `mcp`: Tool usage stats from MCP server calls (grep/read/trace)
- `cli`: Tool usage stats from CLI commands (trie grep/read/trace)
- `sync`: File processing, token usage, and cost aggregates from sync operations
- `retries`: Model API backoff events and delay totals
- `cli_invocations`: Subcommand usage counts

The `AuditSummary.from_log` classmethod accepts an optional `tail_bytes` keyword argument to read only the trailing window of the log file; `None` reads everything. The `to_dict` method produces JSON-serializable output for `trie audit --json`.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:AuditSummary.from_log fingerprint=ad10e237f96f6924ed42244d3b7a5b266cca613d217136bff4d820a2c7feb012 body_fp=c16e7326aee5932f356ebc049521e5d631f4bf5569c62a9edd2a8e6c3cf685c2 source_ref=dcd19d40dcef6d59dc6598f56f1fb68bb12fe211 role=persistence -->
Parses JSONL telemetry log into AuditSummary, tolerating malformed lines and memoizing pricing lookups.

- `tail_bytes`: when set, seeks to the trailing window of the file, discarding the partial first line; `None` reads everything
- Raises `FileNotFoundError` if path doesn't exist
- Skips unparseable lines rather than crashing, counting them as malformed
- Returns complete summary with parse stats and aggregated telemetry data
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:AuditSummary.to_dict fingerprint=1dc447ee86ac36c9170a03669d6f96e8c9e85bb02a7983d703345227311924d7 body_fp=2768fc0c5e28a76a77500ac394ba6e45a04b73c6c2ffc142eedb760691c1ae08 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Converts AuditSummary to JSON-serializable dictionary for `--json` output and structural tests.

- Flattens all nested dataclass fields into plain dict/list/primitive structure
- Converts Path objects to strings for JSON compatibility
- Preserves all statistical data and metadata for programmatic consumption
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_stats_to_dict fingerprint=25ef2bd8764316d4065079ea9bc1e7b1c80dfb88a029e38f4ae20b7fa1f647a3 body_fp=09fc523f1fc9a5b63f87a74c33fbef27e4519bdaa278b15fed1b209b5d6534c0 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Serialises a `{tool: McpCallStats}` mapping to JSON-compatible dict format for `AuditSummary.to_dict()`.

- Converts tuple fields to lists and preserves dict fields as dicts
- Used by both MCP and CLI sections for consistent JSON output structure
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_summarise fingerprint=db36977352ddc32e4f323c1f0633a80c46be598613801ede35273742c66ed32f body_fp=27744cb5a00da092aa4c18bca25d2eac8febdbd554052018c44d2046129f0ec6 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Walks event list once and buckets events by type into aggregated statistics.

- `events`: Stream of parsed telemetry events to categorize
- `log_path`: Source file path for the summary metadata
- `lines_total`: Total lines read from log file
- `lines_parsed`: Successfully parsed lines count
- Returns `AuditSummary` with per-tool MCP/CLI stats, sync metrics, retry counts, and time span
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_mcp_stats fingerprint=57b447f7ffcaeae22e1c1db744b9df072b73cfc0f814f69412e4c6883455f4ea body_fp=8ca7e321636eadde1cb9f02c064526081da576e11c023e2a4a49c01490064e2a source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Aggregates telemetry events for one MCP tool into comprehensive usage statistics.

- `tool`: Tool name being analyzed (grep/read/trace)
- `events`: List of telemetry events from that tool
- `top_qnames`: Top 5 most-queried symbols (read/trace only, empty for grep)
- `fallback_kinds`: Breakdown of grep's fallback types when returning empty results
- `modes`: Read tool's dispatch mode breakdown (qname/triefact/source/show_source)
- `empty_result_count`: Tool-specific empty result detection (grep: 0 hits, trace: ≤1 nodes, read: 0 prose_chars)
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_pricing_cache fingerprint=51486f7a90f088344ba57f7648af229ce4381d3ddb72cd85ba6458417ea304c6 body_fp=366db4e44e1c444c658af91188977e481849e56f2d04cd3617451c00e42286bd source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Module-level cache for model pricing lookups to avoid re-traversing the pricing table on back-to-back `from_log` calls.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_pricing_for fingerprint=81bc5640eca955efcad34e67471ba90c6f7f0fafea2861b567f92ccef61b922a body_fp=a655580652aa68de1d371da277c295f6055c8fef35b190c87f628459335d4c78 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Looks up model pricing with backward compatibility for bare model names.

- Tries exact model_id first, then prepends "anthropic/" if not found and no provider prefix exists
- Caches results in module-level `_pricing_cache` to avoid repeated lookups
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_sync_stats fingerprint=bd0946bd0a48c1e3b58ef1d5233c5265fb3aa18bccac0be13c57ba9c2bdadd25 body_fp=588532f3fca736f89206efa5c78e2d5837fe05e2019d4114c325be59bfa5e6a3 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Aggregates sync_file events into SyncStats with token counts, cost estimation, and per-model breakdown.

- cost_usd: computed via estimate_actual_cost using same pricing logic as live sync command
- by_model: tracks file_runs and token totals per model, surfacing models without pricing entries
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_retry_stats fingerprint=c99848ca78c758eb1dab4f2006736de48377634aac3653eae3bf49ddd4ec72c1 body_fp=932a7c26f3f0d6cf362c5b4eb73d078a0ded907efb6a4518aa370fa3bb8307f1 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Aggregates retry events into total count, reasons breakdown, and cumulative delay seconds.

- Extracts `reason` field from each event, defaulting to "unknown" if absent
- Sums `delay_seconds` fields across all retry events, rounding to 3 decimal places
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_cli_invocations fingerprint=3ee3208f853f5da73a48967394afe7e736b1a8f9a4eee71547f1fb17952bab59 body_fp=fbdf89f7788bcc789361206ae3db71ee7fe477edb0135c78fe1509e147d4ad0d source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Counts CLI subcommand invocations from `cli` events and returns them as frequency-ordered tuples.

- Extracts `subcommand` field from each event, defaulting to "(unknown)" for missing values
- Returns most common subcommands first as (subcommand, count) pairs
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_span fingerprint=06219108afd96504879d771b07d5dcfa0ccf1aac6d7a32802b7eaea42148b7c3 body_fp=8a43ab050971096e935476e6462d2ef9560744271e6e05a07eb8dee2f8fffb62 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Computes the earliest and latest timestamps from a telemetry log plus their time delta in seconds.

- Returns (None, None, None) when timestamps list is empty
- Drops malformed timestamps from span calculation rather than failing
- Parses RFC3339 format by converting 'Z' suffix to '+00:00' for datetime.fromisoformat
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:render fingerprint=be28e4dbcb60339d6dc207338b8bfa0b7d6fa027eba5ecb557a6bd4b263710cc body_fp=01b07f8f414873f8a5002c6c50c1111fc3e87bb7f2d45ba006a16c82c943b109 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Renders a single AuditSummary as five Rich console sections with spacing between each.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:render_comparison fingerprint=f17366612143d3d6815f816050c207b26b065fe5f93ce1438b29cf9a99eb50fb body_fp=d43758994c00647c934f0a860be32bdb4324892d27d8cbd45f394df4c3570740 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Renders side-by-side comparison of two audit summaries with deltas.

- `baseline` — reference run (typically without_trie)
- `candidate` — evaluated run (typically with_trie)
- Deltas show as `(±N)` on candidate side
- Missing sections display `--` to highlight asymmetry
- MCP and CLI calls compared separately to detect surface shifts
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_header fingerprint=028de2583de75b8da4d67b66301b1c96b959a81bd4d63e86f9fb5c9e004f8f93 body_fp=24ae037e8366bd0fe66d4c335b4573906f27b45b5c4f505f54b3aadae72f01aa source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Renders the header section of a single audit summary to the Rich console.

- Displays log file path, time span with duration, and parse statistics
- Shows malformed line count in yellow if any parsing errors occurred
- Time span appears as "(no timestamped events)" when no valid timestamps found
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_mcp fingerprint=c0e81898fe6b14b8ef60f335fa5a4cb3f9b4fc8d2c88133cba432ec5d07b3621 body_fp=e4552b489806476f2e9a866f07ad2329ac8ca650957cbd6d9217280160c039c9 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Renders the MCP-server-side calls section by delegating to `_render_tool_calls` with MCP-specific labels.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_cli_calls fingerprint=8bd6fe144f4be60808e5abf46703d5eed976f4f65e6bfcaff396beb6ae9c0b15 body_fp=0c659b222620069497b31fbd960517e6501da655b4067c7946b52f6efd75fc62 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Renders CLI-side tool call statistics as a Rich table.

- Delegates to `_render_tool_calls` with "CLI calls" title and empty label
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_tool_calls fingerprint=4ad4fb44c2beb8d9919d1631dccedc2baea4455d9614ca54e225539ccb1f032a body_fp=8ef93109734f6f108edd25d978554726e98dd3c25ac074dba9ba74c5c160021e source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Renders tool call statistics table with per-tool rows and optional fallback/mode breakdowns.

- Shows grep/read/trace rows even when zero, with placeholder dashes
- Truncates top qname display at 50 characters
- Appends grep fallback breakdown when fallback activity occurred
- Appends read mode breakdown showing dispatch path distribution
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_sync fingerprint=f52f1b1727ea65ecbb99e76d18a16787eceffb3e6d9053e8b4ce403868cbe012 body_fp=76b586fc01b0baa916fb7634d5900f9a7f693455d08f8b52ec76413d730c87e4 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Renders sync statistics as a Rich table with file runs, token counts, cost, and optional per-model breakdown.

- Displays "--" for cost when zero
- Shows comma-separated thousands for token counts
- Includes per-model breakdown when multiple models present
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_retries fingerprint=a1e2b8663c11620776005312a803cfffcf1ae91cca4e48c8128c189fae731c25 body_fp=e571100e4d742d1a8f3cc64efb174dba3efebca45d5fbb9bab60a2b28a3221e8 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Renders retry statistics showing total count, breakdown by reason, and total delay.

- Prints "none" in green when no retries occurred
- Shows retry counts by reason (429/529/timeout) and cumulative backoff time
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_cli fingerprint=795aa283d5cd30e94e9b96ed812cf35ec66ed522b88ff2838f5c64cfe7b98c96 body_fp=e05185f0405a1bc84fc77cb6a0b4762f6aaf4ab6965474508d59c5462453eb94 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Renders CLI subcommand usage counts as a compact line.

- Shows format like "sync x5, grep x2" for each subcommand and its invocation count
- Skips rendering entirely when no CLI invocations occurred
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_compare_header fingerprint=213ee3d022bcb9f7ab2bcb6bc12bbe61671beefaca19ce6e29ded0f691c30947 body_fp=0622d45c7598cece44e002b11119074264934741f6aed50e6e76415480b07f06 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Prints the header section for comparison mode, showing baseline and candidate log paths with a "Compare" title.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_compare_mcp fingerprint=e464f8232966c1c44fb7eb6343af84a6625170c06b7cdd14468d6eb93a4481fc body_fp=fec0b2b41238b45eabbcac109e3d140ffc97e67e5823398781052dcbfc648a0a source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Renders side-by-side comparison of MCP tool call statistics between baseline and candidate runs.

Delegates to `_render_compare_tool_calls` with "MCP calls" title to display per-tool count differences.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_compare_cli_calls fingerprint=076c6187677ec795745060548c77a5ebd5c544d30f2985c0cdf2b6887c353af0 body_fp=2e32f48d3363e73aff9c021266b0185e57fdc86fd4b7f061ea7a32a7f049d76d source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Renders side-by-side CLI tool call comparison between baseline and candidate audit summaries.

- `baseline`: McpCallStats mapping from baseline run  
- `candidate`: McpCallStats mapping from candidate run
- `console`: Rich console for output
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_compare_tool_calls fingerprint=1d49933c03fa5fa08f02cfb1bcaacd1f9881267cd5b37f0659c351ae2c466f90 body_fp=3964af7b52c26490a3bf711ef3bef9b8be9581b808bba15bd499e4633e7bf4bd source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Renders a comparison table showing tool usage counts (grep/read/trace) between baseline and candidate runs with deltas.

- `title`: Table title distinguishing MCP vs CLI calls  
- Creates four-column table: tool name, baseline count, candidate count, delta
- Includes all tools from both runs plus standard grep/read/trace even if unused
- Delta formatted with green/red colors for positive/negative changes
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_compare_sync fingerprint=5a67d6c4a9165c95996b28c6f58e5b64d6e6e563f0ba4421f0e0a4edc4237511 body_fp=0ed6c47501218cabb4e577749f29a644887f9377ae2fe52d420f6ab71282bd6a source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Renders a side-by-side comparison table of sync metrics with baseline/candidate/delta columns.

- Returns early if both runs have zero file runs
- Displays file runs, symbols generated, cold writes, diff-aware regens, tokens, and cost
- Uses color-coded deltas via `_delta` and `_delta_money` helpers
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_compare_retries fingerprint=67562a410e2c06a1229e5299fa48f024421177c6af554919c51dfc76510355d7 body_fp=7af0543b6302787821472e9ae8fdae33219e16ac92883466af2b3c1833ac7333 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Prints retry comparison between baseline and candidate runs to console.

- Displays "none on either side" when both runs have zero retries
- Shows baseline/candidate totals with delta when either run has retries
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_delta fingerprint=d85999dc29db9403c37ab0a63a763ed396ce0ff337f1b0f06ac9d1b4c6af3a1b body_fp=ee0733fd115a04f3e2de150dbfb79b4ad7c2ea83efe36d06b17c70185f8b34f8 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Formats integer difference between baseline and candidate values with Rich color markup.

- Returns "0" for no change
- Green markup for positive deltas, red for negative
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_delta_money fingerprint=48efc2af497d07b81c90d8dc4e078be3812a2d7adb0d8da0bf07ae4578d06124 body_fp=227d5d9aae6561d3b954960f8ce2483fb812ad34cd97d90455c5358e07f71dc4 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Formats cost delta between baseline and candidate as colored Rich markup string.

- Returns "$0.0000" for differences smaller than 1e-6 to avoid noise from floating point precision
- Green markup for positive deltas (candidate more expensive), red for negative (candidate cheaper)
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_err_cell fingerprint=328ffa7dd16dfd32571fa7bfb5fbd758965687c94186e1759ae361c45b2d733a body_fp=13b68d021c0fa3303ce8668ed91f061b5a37de45fd825b34fdfe3cec937438b9 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Formats an error count for Rich table cells with yellow highlighting for non-zero values.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_fmt_seconds fingerprint=882fd66a371c7442b94ba88ac801dd6ac4412a1abfe22a23ee78585471dc2a2d body_fp=0f684130b724100f0939f40a5183d47ca40b245d6e67ef79accd976a14b64d88 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
Formats a duration in seconds as a human-readable string with appropriate units.

- Returns "--" for None values
- Uses seconds (s) for durations under 60 seconds
- Uses minutes (m) for durations under 3600 seconds
- Uses hours (h) for longer durations
<!-- trie:end -->