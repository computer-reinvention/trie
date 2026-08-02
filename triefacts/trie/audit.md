---
trie_version: 0.3.0
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
  signature: class Event
- kind: method
  qualified_name: trie/audit:Event.from_json
  lines: 64-82
  signature: 'def from_json(cls, line: str) -> Event | None'
- kind: class
  qualified_name: trie/audit:McpCallStats
  lines: 91-132
  signature: class McpCallStats
- kind: method
  qualified_name: trie/audit:McpCallStats.avg_duration_ms
  lines: 127-128
  signature: def avg_duration_ms(self) -> float
- kind: method
  qualified_name: trie/audit:McpCallStats.avg_response_bytes
  lines: 131-132
  signature: def avg_response_bytes(self) -> float
- kind: class
  qualified_name: trie/audit:SyncStats
  lines: 136-158
  signature: class SyncStats
- kind: class
  qualified_name: trie/audit:RetryStats
  lines: 162-167
  signature: class RetryStats
- kind: class
  qualified_name: trie/audit:ParseStats
  lines: 171-176
  signature: class ParseStats
- kind: class
  qualified_name: trie/audit:AuditSummary
  lines: 185-280
  signature: class AuditSummary
- kind: method
  qualified_name: trie/audit:AuditSummary.from_log
  lines: 212-242
  signature: 'def from_log(cls, path: Path, *, tail_bytes: int | None = None) -> AuditSummary'
- kind: method
  qualified_name: trie/audit:AuditSummary.to_dict
  lines: 244-280
  signature: def to_dict(self) -> dict[str, Any]
- kind: function
  qualified_name: trie/audit:_stats_to_dict
  lines: 283-303
  signature: 'def _stats_to_dict(stats_by_tool: dict[str, McpCallStats]) -> dict[str, dict[str, Any]]'
- kind: function
  qualified_name: trie/audit:_summarise
  lines: 311-375
  signature: 'def _summarise( events: Iterable[Event], *, log_path: Path, lines_total: int, lines_parsed: int, ) -> AuditSummary'
- kind: function
  qualified_name: trie/audit:_mcp_stats
  lines: 378-458
  signature: 'def _mcp_stats(tool: str, events: list[Event]) -> McpCallStats'
- kind: constant
  qualified_name: trie/audit:_pricing_cache
  lines: 463-463
- kind: function
  qualified_name: trie/audit:_pricing_for
  lines: 466-479
  signature: 'def _pricing_for(model_id: str) -> ModelPricing | None'
- kind: function
  qualified_name: trie/audit:_sync_stats
  lines: 482-565
  signature: 'def _sync_stats(events: list[Event]) -> SyncStats'
- kind: function
  qualified_name: trie/audit:_retry_stats
  lines: 568-579
  signature: 'def _retry_stats(events: list[Event]) -> RetryStats'
- kind: function
  qualified_name: trie/audit:_cli_invocations
  lines: 582-587
  signature: 'def _cli_invocations(events: list[Event]) -> tuple[tuple[str, int], ...]'
- kind: function
  qualified_name: trie/audit:_span
  lines: 590-607
  signature: 'def _span(timestamps: list[str]) -> tuple[str | None, str | None, float | None]'
- kind: function
  qualified_name: trie/audit:render
  lines: 615-633
  signature: 'def render(summary: AuditSummary, console: Console) -> None'
- kind: function
  qualified_name: trie/audit:render_comparison
  lines: 636-656
  signature: 'def render_comparison(baseline: AuditSummary, candidate: AuditSummary, console: Console) -> None'
- kind: function
  qualified_name: trie/audit:_render_header
  lines: 662-677
  signature: 'def _render_header(s: AuditSummary, console: Console) -> None'
- kind: function
  qualified_name: trie/audit:_render_mcp
  lines: 680-682
  signature: 'def _render_mcp(mcp: dict[str, McpCallStats], console: Console) -> None'
- kind: function
  qualified_name: trie/audit:_render_cli_calls
  lines: 685-693
  signature: 'def _render_cli_calls(cli: dict[str, McpCallStats], console: Console) -> None'
- kind: function
  qualified_name: trie/audit:_render_tool_calls
  lines: 696-770
  signature: 'def _render_tool_calls( by_tool: dict[str, McpCallStats], console: Console, *, title: str, empty_label: str, ) -> None'
- kind: function
  qualified_name: trie/audit:_render_sync
  lines: 773-798
  signature: 'def _render_sync(s: SyncStats, console: Console) -> None'
- kind: function
  qualified_name: trie/audit:_render_retries
  lines: 801-809
  signature: 'def _render_retries(s: RetryStats, console: Console) -> None'
- kind: function
  qualified_name: trie/audit:_render_cli
  lines: 812-816
  signature: 'def _render_cli(invocations: tuple[tuple[str, int], ...], console: Console) -> None'
- kind: function
  qualified_name: trie/audit:_render_compare_header
  lines: 822-827
  signature: 'def _render_compare_header( baseline: AuditSummary, candidate: AuditSummary, console: Console ) -> None'
- kind: function
  qualified_name: trie/audit:_render_compare_mcp
  lines: 830-836
  signature: 'def _render_compare_mcp( baseline: dict[str, McpCallStats], candidate: dict[str, McpCallStats], console: Console, ) -> None'
- kind: function
  qualified_name: trie/audit:_render_compare_cli_calls
  lines: 839-850
  signature: 'def _render_compare_cli_calls( baseline: dict[str, McpCallStats], candidate: dict[str, McpCallStats], console: Console, ) -> None'
- kind: function
  qualified_name: trie/audit:_render_compare_tool_calls
  lines: 853-884
  signature: 'def _render_compare_tool_calls( baseline: dict[str, McpCallStats], candidate: dict[str, McpCallStats], console: Console, *, title: str, ) -> None'
- kind: function
  qualified_name: trie/audit:_render_compare_sync
  lines: 887-911
  signature: 'def _render_compare_sync(b: SyncStats, c: SyncStats, console: Console) -> None'
- kind: function
  qualified_name: trie/audit:_render_compare_retries
  lines: 914-921
  signature: 'def _render_compare_retries(b: RetryStats, c: RetryStats, console: Console) -> None'
- kind: function
  qualified_name: trie/audit:_delta
  lines: 927-931
  signature: 'def _delta(b: int, c: int) -> str'
- kind: function
  qualified_name: trie/audit:_delta_money
  lines: 934-938
  signature: 'def _delta_money(b: float, c: float) -> str'
- kind: function
  qualified_name: trie/audit:_err_cell
  lines: 941-944
  signature: 'def _err_cell(n: int) -> str'
- kind: function
  qualified_name: trie/audit:_fmt_seconds
  lines: 947-954
  signature: 'def _fmt_seconds(s: float | None) -> str'
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
<!-- trie:section symbol=trie/audit:Event fingerprint=4f541f8d3d2bb0b895f2767d53ef25779e2040966277f1c1f2f2d70115027c1b body_fp=2959e363df05d0b776d7d7f107a726542ecf5592d991f49a1d987ecde5c3556c source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `class Event`

Decodes one JSONL telemetry line into structured fields with timestamp and event type.

- `ts`: ISO timestamp string from telemetry emission
- `event`: Event type discriminator (e.g. "mcp_call", "sync_file")
- `fields`: All other JSON fields as flat dict for event-specific data
- `from_json()`: Parses JSONL line, returns None on malformed input to avoid crashes
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:Event.from_json fingerprint=a703f11e700aba5f7cc3f9ce0851ddc30910d7abf7a0e0e29a5d9094d7405cc8 body_fp=d876748ea3b7b9efa5352682391f67136d7b30a47110ae77d471ba4484adf694 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def from_json(cls, line: str) -> Event | None`

Parses a JSONL telemetry line into an Event instance, returning None for malformed input to allow graceful error handling.

- Returns None for empty lines, JSON decode errors, non-dict objects, or missing required fields
- Extracts `ts` and `event` as top-level attributes, remaining fields stored in `fields` dict
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:McpCallStats fingerprint=167844760f03506f9f69113b943ea12a1520d48faa456d95d921ed477da74071 body_fp=fd1a1cbab92236e9bc1c31705c34104c2348b88d67fda002b938d8ba8b5687ce source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `class McpCallStats`

Aggregates statistics for one MCP tool invocation (grep/read/trace).

- `not_found_count`: tool-specific failures indicating agent passed invalid qname
- `empty_result_count`: tool returned no useful content despite success
- `fallback_kinds`: grep-specific breakdown of empty result causes  
- `modes`: read-specific dispatch branch tracking (qname/triefact/source/show_source)
- `top_qnames`: five most frequently requested symbol names
- `avg_duration_ms`: computed from total_duration_ms divided by count
- `avg_response_bytes`: computed from total_response_bytes divided by count
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:McpCallStats.avg_duration_ms fingerprint=84f86f6d52648051332f475bb2db0b3a1f00d72b9f17d5ae50742db4fa421a55 body_fp=a481e1c6e7fe3445b3809d22f45433d9ccbe6981c14ea106efb24eda0d16b8a6 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def avg_duration_ms(self) -> float`

McpCallStats property returns average call duration in milliseconds, avoiding division by zero.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:McpCallStats.avg_response_bytes fingerprint=011d16cbf949693061e94de7dc3a2c520500347177086267b464f530e60d5b02 body_fp=5f83db811ec7963cdca4fee765817acecfaebbc6c53bdd0fab4691e6edea38ee source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def avg_response_bytes(self) -> float`

Returns the average response size in bytes per MCP tool call, or 0.0 if no calls were made.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:SyncStats fingerprint=28cf1d88eb4a0e5a0951850dc3573d868f2eae7668870af42456d93313e285dc body_fp=6700c98e9e043479dfd7e02298cf15882d8b7f91ffa195b1825f75b99f75fd7a source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `class SyncStats`

Aggregates every `sync_file` event in the log with derived cost calculations.

- `cold_count`: number of cold regeneration operations
- `diff_aware_count`: number of diff-aware regeneration operations
- `cost_usd`: computed via `estimate_actual_cost` against per-model pricing table
- `by_model`: per-model breakdown of file runs and token counts
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:RetryStats fingerprint=67878b92223cb78412169667fbf2f4e8901268f7ca09538b21d07e6467e73d6b body_fp=b84bbf9a5b2d27c545c35c4a8d489aaf517b1ce29c5eb8d1a50e5646b88238be source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `class RetryStats`

Aggregates `model_call_retry` events to track client backoff frequency and delay patterns.

- `by_reason`: breakdown of retry counts by reason (rate-limit, overloaded, timeout)
- `total_delay_seconds`: cumulative backoff time across all retries
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:ParseStats fingerprint=7b0640a9557a90cdb8287f36e1894dc529c70ddff0f77ec612cc5e5224a15f84 body_fp=44967892b7dd14226870d5ea2fc4e81260b08784a81bfeeaeb1fb49c0cc42688 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `class ParseStats`

Tracks JSONL parsing statistics for audit log ingestion.

- `lines_total`: Total lines read from the telemetry log file
- `lines_parsed`: Successfully decoded JSONL events 
- `lines_malformed`: Lines that failed JSON parsing or validation
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:AuditSummary fingerprint=41e3a4f551fb822aa8bc6dc38a73bee21e3f19f81193b45a2b7fef8446a269d6 body_fp=2a74ad5bf450cba1a3d548055a5375be6cdea32fa0d19ca00a1de8730b3123d1 source_ref=dcd19d40dcef6d59dc6598f56f1fb68bb12fe211 role=model -->
## `class AuditSummary`

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
<!-- trie:section symbol=trie/audit:AuditSummary.from_log fingerprint=ad10e237f96f6924ed42244d3b7a5b266cca613d217136bff4d820a2c7feb012 body_fp=9eae37e1b2c7f901c0cc3a94e434d3f4f3b6e9472f0cb33780ea5d7f6f8fe277 source_ref=dcd19d40dcef6d59dc6598f56f1fb68bb12fe211 role=persistence -->
## `def from_log(cls, path: Path, *, tail_bytes: int | None = None) -> AuditSummary`

Parses JSONL telemetry log into AuditSummary, tolerating malformed lines and memoizing pricing lookups.

- `tail_bytes`: when set, seeks to the trailing window of the file, discarding the partial first line; `None` reads everything
- Raises `FileNotFoundError` if path doesn't exist
- Skips unparseable lines rather than crashing, counting them as malformed
- Returns complete summary with parse stats and aggregated telemetry data
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:AuditSummary.to_dict fingerprint=1dc447ee86ac36c9170a03669d6f96e8c9e85bb02a7983d703345227311924d7 body_fp=17806f9a54f8dddb91a9f52a5c62d281ea8f83c3f18aaf382e18f5a2e630d99f source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def to_dict(self) -> dict[str, Any]`

Converts AuditSummary to JSON-serializable dictionary for `--json` output and structural tests.

- Flattens all nested dataclass fields into plain dict/list/primitive structure
- Converts Path objects to strings for JSON compatibility
- Preserves all statistical data and metadata for programmatic consumption
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_stats_to_dict fingerprint=25ef2bd8764316d4065079ea9bc1e7b1c80dfb88a029e38f4ae20b7fa1f647a3 body_fp=a7196a1f342ec021fe22fcaf4871cd38aff03d2b2b0fd9cc5151efbc14bc2947 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def _stats_to_dict(stats_by_tool: dict[str, McpCallStats]) -> dict[str, dict[str, Any]]`

Serialises a `{tool: McpCallStats}` mapping to JSON-compatible dict format for `AuditSummary.to_dict()`.

- Converts tuple fields to lists and preserves dict fields as dicts
- Used by both MCP and CLI sections for consistent JSON output structure
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_summarise fingerprint=db36977352ddc32e4f323c1f0633a80c46be598613801ede35273742c66ed32f body_fp=8571463b6b14c00d2defd1d06e62153f6d8f84146c00072eeab91777f3231fe1 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def _summarise( events: Iterable[Event], *, log_path: Path, lines_total: int, lines_parsed: int, ) -> AuditSummary`

Walks event list once and buckets events by type into aggregated statistics.

- `events`: Stream of parsed telemetry events to categorize
- `log_path`: Source file path for the summary metadata
- `lines_total`: Total lines read from log file
- `lines_parsed`: Successfully parsed lines count
- Returns `AuditSummary` with per-tool MCP/CLI stats, sync metrics, retry counts, and time span
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_mcp_stats fingerprint=57b447f7ffcaeae22e1c1db744b9df072b73cfc0f814f69412e4c6883455f4ea body_fp=827b80723721770cd54ee80a6db6d1bd3394110fefaece94fb9fe5f2b3d8e25a source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def _mcp_stats(tool: str, events: list[Event]) -> McpCallStats`

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
<!-- trie:section symbol=trie/audit:_pricing_for fingerprint=81bc5640eca955efcad34e67471ba90c6f7f0fafea2861b567f92ccef61b922a body_fp=1ef7561fc459ce3c62480a327875848cfd126f5ded427703353d57ccf0df9459 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def _pricing_for(model_id: str) -> ModelPricing | None`

Looks up model pricing with backward compatibility for bare model names.

- Tries exact model_id first, then prepends "anthropic/" if not found and no provider prefix exists
- Caches results in module-level `_pricing_cache` to avoid repeated lookups
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_sync_stats fingerprint=bd0946bd0a48c1e3b58ef1d5233c5265fb3aa18bccac0be13c57ba9c2bdadd25 body_fp=8329087bc9539cc5bf54af5f0779157d9d3ab8f080216f7b7f2acb4591c935c6 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def _sync_stats(events: list[Event]) -> SyncStats`

Aggregates sync_file events into SyncStats with token counts, cost estimation, and per-model breakdown.

- cost_usd: computed via estimate_actual_cost using same pricing logic as live sync command
- by_model: tracks file_runs and token totals per model, surfacing models without pricing entries
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_retry_stats fingerprint=c99848ca78c758eb1dab4f2006736de48377634aac3653eae3bf49ddd4ec72c1 body_fp=2ceab429c715aa97e79e0675c4cf1ec2d9227d3739f5b59b868d52d541a3b1e8 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def _retry_stats(events: list[Event]) -> RetryStats`

Aggregates retry events into total count, reasons breakdown, and cumulative delay seconds.

- Extracts `reason` field from each event, defaulting to "unknown" if absent
- Sums `delay_seconds` fields across all retry events, rounding to 3 decimal places
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_cli_invocations fingerprint=3ee3208f853f5da73a48967394afe7e736b1a8f9a4eee71547f1fb17952bab59 body_fp=f3ad2cbc2c765dedfbd2db84975dc3734ad7daab5f6a9474d8e1e619f347ed27 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def _cli_invocations(events: list[Event]) -> tuple[tuple[str, int], ...]`

Counts CLI subcommand invocations from `cli` events and returns them as frequency-ordered tuples.

- Extracts `subcommand` field from each event, defaulting to "(unknown)" for missing values
- Returns most common subcommands first as (subcommand, count) pairs
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_span fingerprint=06219108afd96504879d771b07d5dcfa0ccf1aac6d7a32802b7eaea42148b7c3 body_fp=773974c6054fb96b5353b41bd1a4bbe66e382c8578d814e4ff5a85889e468f06 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def _span(timestamps: list[str]) -> tuple[str | None, str | None, float | None]`

Computes the earliest and latest timestamps from a telemetry log plus their time delta in seconds.

- Returns (None, None, None) when timestamps list is empty
- Drops malformed timestamps from span calculation rather than failing
- Parses RFC3339 format by converting 'Z' suffix to '+00:00' for datetime.fromisoformat
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:render fingerprint=be28e4dbcb60339d6dc207338b8bfa0b7d6fa027eba5ecb557a6bd4b263710cc body_fp=1d609daa23504e0cfd163d22f46cbf6f167d22cfdfbe0aeba8c5694090f71113 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def render(summary: AuditSummary, console: Console) -> None`

Renders a single AuditSummary as five Rich console sections with spacing between each.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:render_comparison fingerprint=f17366612143d3d6815f816050c207b26b065fe5f93ce1438b29cf9a99eb50fb body_fp=1bf593cc3bdf9715d7f81d25595c747253421af9c7da2bc29bf2ec43f3cef4bf source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def render_comparison(baseline: AuditSummary, candidate: AuditSummary, console: Console) -> None`

Renders side-by-side comparison of two audit summaries with deltas.

- `baseline` — reference run (typically without_trie)
- `candidate` — evaluated run (typically with_trie)
- Deltas show as `(±N)` on candidate side
- Missing sections display `--` to highlight asymmetry
- MCP and CLI calls compared separately to detect surface shifts
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_header fingerprint=028de2583de75b8da4d67b66301b1c96b959a81bd4d63e86f9fb5c9e004f8f93 body_fp=d06244713b64e71fcd714d4b2f1215f89842509a6b3cd6671230b768a00806ec source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def _render_header(s: AuditSummary, console: Console) -> None`

Renders the header section of a single audit summary to the Rich console.

- Displays log file path, time span with duration, and parse statistics
- Shows malformed line count in yellow if any parsing errors occurred
- Time span appears as "(no timestamped events)" when no valid timestamps found
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_mcp fingerprint=c0e81898fe6b14b8ef60f335fa5a4cb3f9b4fc8d2c88133cba432ec5d07b3621 body_fp=820affb394051a000eb70cfd4ea5ba028921874bed792d1e9738683354bae153 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def _render_mcp(mcp: dict[str, McpCallStats], console: Console) -> None`

Renders the MCP-server-side calls section by delegating to `_render_tool_calls` with MCP-specific labels.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_cli_calls fingerprint=8bd6fe144f4be60808e5abf46703d5eed976f4f65e6bfcaff396beb6ae9c0b15 body_fp=45877ea14a47953d6d13f890f9f3d3ed71cdfd94bdaa9b7abeafe682c068ae05 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def _render_cli_calls(cli: dict[str, McpCallStats], console: Console) -> None`

Renders CLI-side tool call statistics as a Rich table.

- Delegates to `_render_tool_calls` with "CLI calls" title and empty label
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_tool_calls fingerprint=4ad4fb44c2beb8d9919d1631dccedc2baea4455d9614ca54e225539ccb1f032a body_fp=6a55f9876788d19832b059f9237103e95cccc25cef430b5b77ee41957f92cd63 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def _render_tool_calls( by_tool: dict[str, McpCallStats], console: Console, *, title: str, empty_label: str, ) -> None`

Renders tool call statistics table with per-tool rows and optional fallback/mode breakdowns.

- Shows grep/read/trace rows even when zero, with placeholder dashes
- Truncates top qname display at 50 characters
- Appends grep fallback breakdown when fallback activity occurred
- Appends read mode breakdown showing dispatch path distribution
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_sync fingerprint=f52f1b1727ea65ecbb99e76d18a16787eceffb3e6d9053e8b4ce403868cbe012 body_fp=2ced82e964a4526ade32ba89b26f8c9901d90eeae5b24a76e39a3cd2aad5677b source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def _render_sync(s: SyncStats, console: Console) -> None`

Renders sync statistics as a Rich table with file runs, token counts, cost, and optional per-model breakdown.

- Displays "--" for cost when zero
- Shows comma-separated thousands for token counts
- Includes per-model breakdown when multiple models present
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_retries fingerprint=a1e2b8663c11620776005312a803cfffcf1ae91cca4e48c8128c189fae731c25 body_fp=5267b1abc1973a54f4498ee03725162646ff3672bc53e839756d7de97b37ce3c source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def _render_retries(s: RetryStats, console: Console) -> None`

Renders retry statistics showing total count, breakdown by reason, and total delay.

- Prints "none" in green when no retries occurred
- Shows retry counts by reason (429/529/timeout) and cumulative backoff time
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_cli fingerprint=795aa283d5cd30e94e9b96ed812cf35ec66ed522b88ff2838f5c64cfe7b98c96 body_fp=8236f956b0895911567e48a0b3d3a7a777b6332e8420a0bd4a02fb1f8c653504 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def _render_cli(invocations: tuple[tuple[str, int], ...], console: Console) -> None`

Renders CLI subcommand usage counts as a compact line.

- Shows format like "sync x5, grep x2" for each subcommand and its invocation count
- Skips rendering entirely when no CLI invocations occurred
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_compare_header fingerprint=213ee3d022bcb9f7ab2bcb6bc12bbe61671beefaca19ce6e29ded0f691c30947 body_fp=33e897df1712bc27e5e541749dd4adbfe048fd061a6b7cbfcbc33228dd8d693a source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def _render_compare_header( baseline: AuditSummary, candidate: AuditSummary, console: Console ) -> None`

Prints the header section for comparison mode, showing baseline and candidate log paths with a "Compare" title.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_compare_mcp fingerprint=e464f8232966c1c44fb7eb6343af84a6625170c06b7cdd14468d6eb93a4481fc body_fp=3005b5fb032c57e6948f88e156c667054620c4eb331a7561094821761f096aee source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def _render_compare_mcp( baseline: dict[str, McpCallStats], candidate: dict[str, McpCallStats], console: Console, ) -> None`

Renders side-by-side comparison of MCP tool call statistics between baseline and candidate runs.

Delegates to `_render_compare_tool_calls` with "MCP calls" title to display per-tool count differences.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_compare_cli_calls fingerprint=076c6187677ec795745060548c77a5ebd5c544d30f2985c0cdf2b6887c353af0 body_fp=357e3ed622f222d825578b5b73dca8ab5038498091c356a415276f27b69c8ab9 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def _render_compare_cli_calls( baseline: dict[str, McpCallStats], candidate: dict[str, McpCallStats], console: Console, ) -> None`

Renders side-by-side CLI tool call comparison between baseline and candidate audit summaries.

- `baseline`: McpCallStats mapping from baseline run  
- `candidate`: McpCallStats mapping from candidate run
- `console`: Rich console for output
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_compare_tool_calls fingerprint=1d49933c03fa5fa08f02cfb1bcaacd1f9881267cd5b37f0659c351ae2c466f90 body_fp=aecaf17bca7a8c48cbf5b21f8545227262c120fa7e16478fe3a9782a923f88b8 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def _render_compare_tool_calls( baseline: dict[str, McpCallStats], candidate: dict[str, McpCallStats], console: Console, *, title: str, ) -> None`

Renders a comparison table showing tool usage counts (grep/read/trace) between baseline and candidate runs with deltas.

- `title`: Table title distinguishing MCP vs CLI calls  
- Creates four-column table: tool name, baseline count, candidate count, delta
- Includes all tools from both runs plus standard grep/read/trace even if unused
- Delta formatted with green/red colors for positive/negative changes
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_compare_sync fingerprint=5a67d6c4a9165c95996b28c6f58e5b64d6e6e563f0ba4421f0e0a4edc4237511 body_fp=2d8df12e7393aeb00be039ef6dbb474435ee1dbf481f5f408d73734cd646230a source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def _render_compare_sync(b: SyncStats, c: SyncStats, console: Console) -> None`

Renders a side-by-side comparison table of sync metrics with baseline/candidate/delta columns.

- Returns early if both runs have zero file runs
- Displays file runs, symbols generated, cold writes, diff-aware regens, tokens, and cost
- Uses color-coded deltas via `_delta` and `_delta_money` helpers
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_compare_retries fingerprint=67562a410e2c06a1229e5299fa48f024421177c6af554919c51dfc76510355d7 body_fp=f8dc9efd446661b44820c32aaae89e2623a1d1c1847d92756412093b85df1040 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def _render_compare_retries(b: RetryStats, c: RetryStats, console: Console) -> None`

Prints retry comparison between baseline and candidate runs to console.

- Displays "none on either side" when both runs have zero retries
- Shows baseline/candidate totals with delta when either run has retries
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_delta fingerprint=d85999dc29db9403c37ab0a63a763ed396ce0ff337f1b0f06ac9d1b4c6af3a1b body_fp=d0c7bcfc1aefbe02373e793a7605137a1d50f28a7ebacc9883f9fbfda0361ba8 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def _delta(b: int, c: int) -> str`

Formats integer difference between baseline and candidate values with Rich color markup.

- Returns "0" for no change
- Green markup for positive deltas, red for negative
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_delta_money fingerprint=48efc2af497d07b81c90d8dc4e078be3812a2d7adb0d8da0bf07ae4578d06124 body_fp=03ba7f2fe1066c4e14acdabaff21fb30178088af9876811f140898264468680c source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def _delta_money(b: float, c: float) -> str`

Formats cost delta between baseline and candidate as colored Rich markup string.

- Returns "$0.0000" for differences smaller than 1e-6 to avoid noise from floating point precision
- Green markup for positive deltas (candidate more expensive), red for negative (candidate cheaper)
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_err_cell fingerprint=328ffa7dd16dfd32571fa7bfb5fbd758965687c94186e1759ae361c45b2d733a body_fp=d67fe5dbc1282ba04ba114be5e29c045986b4a2f6b036144921a707d88153016 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def _err_cell(n: int) -> str`

Formats an error count for Rich table cells with yellow highlighting for non-zero values.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_fmt_seconds fingerprint=882fd66a371c7442b94ba88ac801dd6ac4412a1abfe22a23ee78585471dc2a2d body_fp=d6bd3fcd460447ceafcd6db1b0c671bc6dfe653626e722b13b0d358a686cd2bf source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 role=monitoring-telemetry -->
## `def _fmt_seconds(s: float | None) -> str`

Formats a duration in seconds as a human-readable string with appropriate units.

- Returns "--" for None values
- Uses seconds (s) for durations under 60 seconds
- Uses minutes (m) for durations under 3600 seconds
- Uses hours (h) for longer durations
<!-- trie:end -->