---
trie_version: 0.1.2
source: trie/audit.py
file_fingerprint: 6194dc36fc197b2fb708a63c0fa8c3e760530bc85f60257d98c76740e250dd43
last_synced_at: '2026-05-24T00:18:07Z'
description: Post-hoc analysis of `debug.jsonl` telemetry logs.
defines:
- kind: module
  qualified_name: trie/audit:__module__
  lines: 1-945
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
  lines: 185-270
- kind: method
  qualified_name: trie/audit:AuditSummary.from_log
  lines: 212-232
- kind: method
  qualified_name: trie/audit:AuditSummary.to_dict
  lines: 234-270
- kind: function
  qualified_name: trie/audit:_stats_to_dict
  lines: 273-293
- kind: function
  qualified_name: trie/audit:_summarise
  lines: 301-365
- kind: function
  qualified_name: trie/audit:_mcp_stats
  lines: 368-448
- kind: constant
  qualified_name: trie/audit:_pricing_cache
  lines: 453-453
- kind: function
  qualified_name: trie/audit:_pricing_for
  lines: 456-469
- kind: function
  qualified_name: trie/audit:_sync_stats
  lines: 472-555
- kind: function
  qualified_name: trie/audit:_retry_stats
  lines: 558-569
- kind: function
  qualified_name: trie/audit:_cli_invocations
  lines: 572-577
- kind: function
  qualified_name: trie/audit:_span
  lines: 580-597
- kind: function
  qualified_name: trie/audit:render
  lines: 605-623
- kind: function
  qualified_name: trie/audit:render_comparison
  lines: 626-646
- kind: function
  qualified_name: trie/audit:_render_header
  lines: 652-667
- kind: function
  qualified_name: trie/audit:_render_mcp
  lines: 670-672
- kind: function
  qualified_name: trie/audit:_render_cli_calls
  lines: 675-683
- kind: function
  qualified_name: trie/audit:_render_tool_calls
  lines: 686-760
- kind: function
  qualified_name: trie/audit:_render_sync
  lines: 763-788
- kind: function
  qualified_name: trie/audit:_render_retries
  lines: 791-799
- kind: function
  qualified_name: trie/audit:_render_cli
  lines: 802-806
- kind: function
  qualified_name: trie/audit:_render_compare_header
  lines: 812-817
- kind: function
  qualified_name: trie/audit:_render_compare_mcp
  lines: 820-826
- kind: function
  qualified_name: trie/audit:_render_compare_cli_calls
  lines: 829-840
- kind: function
  qualified_name: trie/audit:_render_compare_tool_calls
  lines: 843-874
- kind: function
  qualified_name: trie/audit:_render_compare_sync
  lines: 877-901
- kind: function
  qualified_name: trie/audit:_render_compare_retries
  lines: 904-911
- kind: function
  qualified_name: trie/audit:_delta
  lines: 917-921
- kind: function
  qualified_name: trie/audit:_delta_money
  lines: 924-928
- kind: function
  qualified_name: trie/audit:_err_cell
  lines: 931-934
- kind: function
  qualified_name: trie/audit:_fmt_seconds
  lines: 937-944
incoming_refs: 33
outgoing_refs: 2
---
<!-- trie:section symbol=trie/audit:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=463c46f50931e512e302225826dce6a7e416e5361d15982154f2eae8a103ef6a source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `trie/audit.py`

Ingest one or two `debug.jsonl` telemetry logs and produce a structured, renderable audit summary.

- `AuditSummary.from_log`: entry point for single-run ingestion
- `render` / `render_comparison`: Rich console output, single or side-by-side
- `McpCallStats`, `SyncStats`, `RetryStats`: per-section aggregates
- `to_dict`: JSON-serialisable view for `--json` or scripted consumers
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:Event fingerprint=4f541f8d3d2bb0b895f2767d53ef25779e2040966277f1c1f2f2d70115027c1b body_fp=caedccd8b328e55613769eb102ebd38e26e156c0956d68b8b333d6b0cfe0f2f7 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `Event(ts: str, event: str, fields: dict[str, Any])`

Frozen dataclass representing one decoded JSONL telemetry line.

- `fields`: all emitter-supplied keys except `ts` and `event`, which are promoted to top-level attributes.

## `Event.from_json(line: str) -> Event | None`

Parse one JSONL line into an `Event`, returning `None` on empty, malformed, or non-dict input.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:Event.from_json fingerprint=a703f11e700aba5f7cc3f9ce0851ddc30910d7abf7a0e0e29a5d9094d7405cc8 body_fp=84ab795f3db4f7ee30b2f73c7ae165bb6f5006b33e1f52e4704ee81c2da0c264 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `Event.from_json(cls, line: str) -> Event | None`

Parse one JSONL line into an `Event`, returning `None` for empty, malformed, or non-dict lines.

- Returns `None` instead of raising on any parse failure, including truncated writes.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:McpCallStats fingerprint=167844760f03506f9f69113b943ea12a1520d48faa456d95d921ed477da74071 body_fp=60fff5dfd38b65e810638b21ea426b6209ed5e58ad3f8aabbed78e6d453fd993 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `McpCallStats`

Aggregate call statistics for one MCP/CLI tool (`grep`, `read`, or `trace`).

- `not_found_count`: calls where the tool returned `error_code == "not_found"`.
- `empty_result_count`: tool-specific "returned nothing useful" signal (zero hits for grep, ≤1 node for trace, zero prose chars for read).
- `top_qnames`: up to 5 most-requested qnames; populated for `read` and `trace` only.
- `fallback_kinds`: grep-only; counts of fallback discriminator values (`none`, `text_match`, `text_match_empty`).
- `modes`: read-only; dispatch branch counts (`qname`, `triefact`, `source`, `show_source`).
- `avg_duration_ms`: mean call latency; 0.0 when `count` is zero.
- `avg_response_bytes`: mean response size; 0.0 when `count` is zero.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:McpCallStats.avg_duration_ms fingerprint=84f86f6d52648051332f475bb2db0b3a1f00d72b9f17d5ae50742db4fa421a55 body_fp=9c7d65d2c90da8dfb19b952496d7ecb6433f85251226c91a33150a21dba6d6fb source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `McpCallStats.avg_duration_ms`

Mean call duration in milliseconds across all `McpCallStats` events for this tool.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:McpCallStats.avg_response_bytes fingerprint=011d16cbf949693061e94de7dc3a2c520500347177086267b464f530e60d5b02 body_fp=ce192ee9ebee031a0ca995cec1ef5aae21cf2aaa126aba47294cdcf97f7b77ec source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `McpCallStats.avg_response_bytes`

Mean response size in bytes across all calls for this `McpCallStats` tool; `0.0` when count is zero.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:SyncStats fingerprint=28cf1d88eb4a0e5a0951850dc3573d868f2eae7668870af42456d93313e285dc body_fp=ca7d1e4ccd2a160052d5a6d3a9789bfa0a64f31c54aae05ad3bb9dd4158a458b source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `SyncStats`

Aggregate all `sync_file` events from a log into token totals, symbol counts, and derived USD cost.

- `cost_usd`: sum of `estimate_actual_cost` across all events; zero for models with no pricing entry.
- `by_model`: per-model dict with keys `file_runs`, `input_tokens`, `output_tokens`, `cache_creation_tokens`, `cache_read_tokens`.
- `cold_count`: number of events with `regen_mode_cold` set.
- `diff_aware_count`: number of events with `regen_mode_diff_aware` set.
- `symbols_skipped`: symbols passed through without regeneration.
- `sections_removed`: triefact sections deleted during sync runs.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:RetryStats fingerprint=67878b92223cb78412169667fbf2f4e8901268f7ca09538b21d07e6467e73d6b body_fp=d553dc3c6cdf81164aa5f249ef21d9547fc7cacecbca56cde828445486a52320 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `RetryStats`

Aggregate counts of `model_call_retry` events across a log run.

- `by_reason`: maps retry reason strings (e.g. `rate_limit`, `overloaded`) to occurrence counts.
- `total_delay_seconds`: cumulative backoff time across all retries.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:ParseStats fingerprint=7b0640a9557a90cdb8287f36e1894dc529c70ddff0f77ec612cc5e5224a15f84 body_fp=be09a8bf2143c1d3e6f549b0a59e953fb5b6b65276f79ffde39e453a1f5d64cd source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `ParseStats`

Immutable counts of how many JSONL lines were attempted, successfully decoded, and rejected.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:AuditSummary fingerprint=7ac89756751d2fb08be28cc28ab609ee6112219b0fc7389b2a0dd5c25a5e20a6 body_fp=5ecf9021e0f34ae2c2c671cda309c8b63f4cbbdb4a2b02ac50f8c679fc9abcf2 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `AuditSummary`

Frozen dataclass holding one run's compressed telemetry view; construct via `AuditSummary.from_log(path)`.

- `mcp`: per-tool `McpCallStats` for `mcp_call` events from the MCP server.
- `cli`: per-tool `McpCallStats` for `cli_call` events from CLI subcommands.
- `span_start` / `span_end`: earliest and latest event timestamps in the log.
- `cli_invocations`: ranked `(subcommand, count)` pairs from `cli` events.
- `from_log(path)`: classmethod; single-pass JSONL ingestion, raises `FileNotFoundError` if `path` absent.
- `to_dict()`: returns JSON-serialisable dict; used by `--json` output and tests.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:AuditSummary.from_log fingerprint=8fe7c2361cf7c16c905a99b261122cde88a56e973ad2461fd1a45a330fa26408 body_fp=31540b275d6926dea900e6cc627fb8b6710916fc38cf037540611dffb46fa190 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `AuditSummary.from_log(path: Path) -> AuditSummary`

Build an `AuditSummary` by reading and parsing a JSONL telemetry log in a single pass.

- `path`: must exist; raises `FileNotFoundError` otherwise.
- Malformed lines are silently skipped and counted in `parse.lines_malformed`.
- Pricing lookups are memoised at module level across calls.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:AuditSummary.to_dict fingerprint=1dc447ee86ac36c9170a03669d6f96e8c9e85bb02a7983d703345227311924d7 body_fp=dfd5e06702af4e9a876eef8ec120a8af14b4d7fd261ce786d2d4be8b030ec406 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `AuditSummary.to_dict() -> dict[str, Any]`

Serialize an `AuditSummary` to a JSON-compatible dict for `--json` output and structural assertions in tests.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_stats_to_dict fingerprint=25ef2bd8764316d4065079ea9bc1e7b1c80dfb88a029e38f4ae20b7fa1f647a3 body_fp=e3becbf6b48ff43d236f55a9ffe614f515f1384a64d19f34577fba11b5fb907f source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `_stats_to_dict(stats_by_tool: dict[str, McpCallStats]) -> dict[str, dict[str, Any]]`

Serialise a `{tool: McpCallStats}` mapping to a JSON-friendly dict for `AuditSummary.to_dict()`.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_summarise fingerprint=db36977352ddc32e4f323c1f0633a80c46be598613801ede35273742c66ed32f body_fp=88d98949d30afe2648037221ef7639665118d101d575883c080e1c04166331b7 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `_summarise(events: Iterable[Event], *, log_path: Path, lines_total: int, lines_parsed: int) -> AuditSummary`

Walk an event list once, bucket by event type, and return a complete `AuditSummary`.

- `events`: pre-parsed `Event` objects; accepts any iterable so test fixtures can bypass filesystem I/O.
- `lines_total` / `lines_parsed`: forwarded directly into `ParseStats`; malformed count is derived as their difference.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_mcp_stats fingerprint=57b447f7ffcaeae22e1c1db744b9df072b73cfc0f814f69412e4c6883455f4ea body_fp=191e210b2d48f50a85d1977e6c214e5bcba69aff6fa3fedce1e842d863c975aa source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `_mcp_stats(tool: str, events: list[Event]) -> McpCallStats`

Aggregate a list of same-tool events into a `McpCallStats`, with tool-specific empty-result detection, fallback kind counts, and top-5 qnames.

- `top_qnames`: populated for `read` (`qname` arg) and `trace` (`from_qname` arg); empty for `grep`.
- `empty_result_count`: detected via `result_count==0` (grep), `nodes_count<=1` (trace), or `prose_chars==0` (read).
- `modes`: `read`-only; absent `mode` field attributed to `"qname"` so counts sum to total.
- `fallback_kinds`: `grep`-only; counts `fallback_kind` discriminator values from empty-result calls.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_pricing_cache fingerprint=51486f7a90f088344ba57f7648af229ce4381d3ddb72cd85ba6458417ea304c6 body_fp=16013bed2f7708d45a001413d5f10c78252885d6af42f3d5b5701711455ccf7e source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `_pricing_cache: dict[str, ModelPricing | None] = {}`

Module-level memoisation table mapping model IDs to their `ModelPricing` entries, shared across `from_log` calls.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_pricing_for fingerprint=81bc5640eca955efcad34e67471ba90c6f7f0fafea2861b567f92ccef61b922a body_fp=e96e63ff2fa4b68df2ec35f43afda748f057e6a9f8638543ca6055551e05ee6e source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `_pricing_for(model_id: str) -> ModelPricing | None`

Look up and memoize pricing for a model ID, accepting both `provider/model` and bare model formats.

- Falls back to `anthropic/<model_id>` when no slash is present and the direct lookup fails.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_sync_stats fingerprint=bd0946bd0a48c1e3b58ef1d5233c5265fb3aa18bccac0be13c57ba9c2bdadd25 body_fp=beb74a6281863e794ea9f15e66104bfd9a2b1cd3478e9d796618b3a0906dde48 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `_sync_stats(events: list[Event]) -> SyncStats`

Aggregate all `sync_file` events into a `SyncStats` with token totals, cost, and per-model breakdown.

- Models without a pricing entry contribute zero cost but still appear in `by_model`.
- Cost uses `estimate_actual_cost` with memoised pricing, matching what the live `sync` command reports.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_retry_stats fingerprint=c99848ca78c758eb1dab4f2006736de48377634aac3653eae3bf49ddd4ec72c1 body_fp=3785c0a5ae55171b6cc77ac05956c4870d597ad7e290682cd7f83fc645040e14 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `_retry_stats(events: list[Event]) -> RetryStats`

Aggregate `model_call_retry` events into a `RetryStats` by reason and total delay.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_cli_invocations fingerprint=3ee3208f853f5da73a48967394afe7e736b1a8f9a4eee71547f1fb17952bab59 body_fp=c30b6dc48c449b0ebbb2fb01ef21f6390f3bd8b9d7da15ab22a1fb647cfd9950 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `_cli_invocations(events: list[Event]) -> tuple[tuple[str, int], ...]`

Count `cli` events by subcommand and return all entries sorted by frequency descending.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_span fingerprint=06219108afd96504879d771b07d5dcfa0ccf1aac6d7a32802b7eaea42148b7c3 body_fp=ef003038b7f2aed0a20bcf7b3cf64724a6b67c94ee6fe2ad7a967fb12c5953ec source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `_span(timestamps: list[str]) -> tuple[str | None, str | None, float | None]`

Return the earliest timestamp, latest timestamp, and elapsed seconds from a list of RFC3339 strings.

- Duration is `None` if any timestamp fails `fromisoformat` parsing.
- Returns `(None, None, None)` for an empty input list.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:render fingerprint=be28e4dbcb60339d6dc207338b8bfa0b7d6fa027eba5ecb557a6bd4b263710cc body_fp=3114aa1072815e2aafc8489541b12b9c0290022768eb5afe626543444a8d3d21 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `render(summary: AuditSummary, console: Console) -> None`

Print one `AuditSummary` as six Rich sections: header, MCP calls, CLI calls, sync, retries, CLI invocations.

- Empty sections print a placeholder instead of being silently omitted.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:render_comparison fingerprint=f17366612143d3d6815f816050c207b26b065fe5f93ce1438b29cf9a99eb50fb body_fp=8cd5fdc7fcdad98e53f7e9ea682a422b9d47481409734011f237d1da1e2ccb27 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `render_comparison(baseline: AuditSummary, candidate: AuditSummary, console: Console) -> None`

Print a side-by-side Rich comparison of two `AuditSummary` runs with per-metric deltas.

- `baseline`: reference run (typically `without_trie`); deltas are relative to this.
- `candidate`: run under evaluation; delta shown as `±N` beside each candidate value.
- MCP and CLI call counts rendered in separate tables; missing sections show `--`.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_header fingerprint=028de2583de75b8da4d67b66301b1c96b959a81bd4d63e86f9fb5c9e004f8f93 body_fp=5d4309f23cd372d836139d2a5ab7758dfc4e9b99420480625742a16b73342d71 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `_render_header(s: AuditSummary, console: Console) -> None`

Print log path, time span, and parse line counts for one `AuditSummary`.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_mcp fingerprint=c0e81898fe6b14b8ef60f335fa5a4cb3f9b4fc8d2c88133cba432ec5d07b3621 body_fp=4e76621c1dc9671e1c20b13d62b74c66b7db0564fe682e533b00c5f7164381b9 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `_render_mcp(mcp: dict[str, McpCallStats], console: Console) -> None`

Render the MCP-server-side tool-calls section by delegating to `_render_tool_calls`.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_cli_calls fingerprint=8bd6fe144f4be60808e5abf46703d5eed976f4f65e6bfcaff396beb6ae9c0b15 body_fp=e56daff8796d6fc0bf4a8451b7b7197defb76819ae88009267b18b4247958322 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `_render_cli_calls(cli: dict[str, McpCallStats], console: Console) -> None`

Render the CLI-side tool calls section (`trie grep`/`read`/`trace`) using the shared `_render_tool_calls` layout.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_tool_calls fingerprint=4ad4fb44c2beb8d9919d1631dccedc2baea4455d9614ca54e225539ccb1f032a body_fp=469424137d2fcad071e5611d70879ef5022ee4974709fef5a040056e494df16e source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `_render_tool_calls(by_tool: dict[str, McpCallStats], console: Console, *, title: str, empty_label: str) -> None`

Render a Rich table of per-tool call stats, plus grep fallback and read mode breakdowns, to `console`.

- `by_tool`: tool-name-keyed stats; always emits rows for `grep`/`read`/`trace` even when absent.
- `empty_label`: heading text printed when `by_tool` is empty.
- `title`: Rich table title shown when data is present.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_sync fingerprint=f52f1b1727ea65ecbb99e76d18a16787eceffb3e6d9053e8b4ce403868cbe012 body_fp=5f9abca429401d861c0100a551e639edc2cb6a91d4249a9ea17830419ac38ed3 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `_render_sync(s: SyncStats, console: Console) -> None`

Render a `SyncStats` block to `console` as a two-column Rich table, with a per-model breakdown appended when more than one model was seen.

- Prints a `no sync_file events` placeholder when `s.file_runs == 0`.
- Per-model breakdown is only shown when `len(s.by_model) > 1`.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_retries fingerprint=a1e2b8663c11620776005312a803cfffcf1ae91cca4e48c8128c189fae731c25 body_fp=839225c46859f5eadf8f824a9ab75461d910c53db6fa07cdb3cb6c644bb975dd source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `_render_retries(s: RetryStats, console: Console) -> None`

Print the retries section: green "none" when zero, otherwise total count, per-reason breakdown, and cumulative backoff seconds.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_cli fingerprint=795aa283d5cd30e94e9b96ed812cf35ec66ed522b88ff2838f5c64cfe7b98c96 body_fp=32461a03ec44bd434270d8fe8b8781ff1f76ba5c067231835123d510d39cd4fa source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `_render_cli(invocations: tuple[tuple[str, int], ...], console: Console) -> None`

Print a single "CLI: subcommand xN, …" line; silently skips if there are no invocations.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_compare_header fingerprint=213ee3d022bcb9f7ab2bcb6bc12bbe61671beefaca19ce6e29ded0f691c30947 body_fp=7a4bfbeeda657a67fdc9b3a77b3cec49147fc672e11d7e2a69893552bbfb1b3c source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `_render_compare_header(baseline: AuditSummary, candidate: AuditSummary, console: Console) -> None`

Print the "Compare" heading and both log paths to `console`.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_compare_mcp fingerprint=e464f8232966c1c44fb7eb6343af84a6625170c06b7cdd14468d6eb93a4481fc body_fp=36cbd248f861ab1f6929863fde1a7d764abc71a98a010d23442858e006d8ba16 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `_render_compare_mcp(baseline: dict[str, McpCallStats], candidate: dict[str, McpCallStats], console: Console) -> None`

Render a side-by-side MCP-server-side per-tool call count diff table to `console`.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_compare_cli_calls fingerprint=076c6187677ec795745060548c77a5ebd5c544d30f2985c0cdf2b6887c353af0 body_fp=08bae93d0291eebd12bdb3f748585134ecee1afb97778930d61dd0c1110e9294 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `_render_compare_cli_calls(baseline: dict[str, McpCallStats], candidate: dict[str, McpCallStats], console: Console) -> None`

Render a side-by-side CLI-call count diff table for `trie grep`/`read`/`trace` between two runs.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_compare_tool_calls fingerprint=1d49933c03fa5fa08f02cfb1bcaacd1f9881267cd5b37f0659c351ae2c466f90 body_fp=e7790f138b7304a98fa85c95b9bd5fccf0609d95dfb6b6c31bdeba5a1459abc6 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `_render_compare_tool_calls(baseline, candidate, console, *, title)`

Render a baseline/candidate/Δ Rich table comparing per-tool call counts across two `McpCallStats` mappings.

- `baseline`: reference run's tool stats; missing tools count as zero.
- `candidate`: evaluated run's tool stats; missing tools count as zero.
- `title`: section heading; only difference between MCP and CLI variants.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_compare_sync fingerprint=5a67d6c4a9165c95996b28c6f58e5b64d6e6e563f0ba4421f0e0a4edc4237511 body_fp=70c4ff5f41922902972c40ed82616352030a789822484f8b77890ae21e9a45c7 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `_render_compare_sync(b: SyncStats, c: SyncStats, console: Console) -> None`

Print a side-by-side Rich table comparing two runs' sync stats with deltas.

- Silently returns when both sides have zero `file_runs`.
- Cost delta uses `_delta_money`; all other numeric deltas use `_delta`.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_render_compare_retries fingerprint=67562a410e2c06a1229e5299fa48f024421177c6af554919c51dfc76510355d7 body_fp=620260aa1406f299f9c511297ac8b78c459aa1ad8f13216b2fe7458f0b24da01 source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `_render_compare_retries(b: RetryStats, c: RetryStats, console: Console) -> None`

Print a one-line retry comparison between baseline and candidate `RetryStats` to `console`.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_delta fingerprint=d85999dc29db9403c37ab0a63a763ed396ce0ff337f1b0f06ac9d1b4c6af3a1b body_fp=1b15ce0d7295dc84f2f3a021a84e820169e181329606e6b7b8119a4292e542bb source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `_delta(b: int, c: int) -> str`

Format the signed difference between two integers as a Rich-coloured string.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_delta_money fingerprint=48efc2af497d07b81c90d8dc4e078be3812a2d7adb0d8da0bf07ae4578d06124 body_fp=eeb9c5c3aef65e14b9f31283de9c1ee76288aec5e0c652ff930fb613e3df2e9a source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `_delta_money(b: float, c: float) -> str`

Format a USD cost delta as a Rich-coloured string, green for increases, red for decreases.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_err_cell fingerprint=328ffa7dd16dfd32571fa7bfb5fbd758965687c94186e1759ae361c45b2d733a body_fp=24548d2eeeaa2336766ea8b2fc13e60ecd66945cce9b9d9ac22d0d8d73c530da source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `_err_cell(n: int) -> str`

Format an integer count as a Rich markup string, highlighting non-zero values in yellow.
<!-- trie:end -->
<!-- trie:section symbol=trie/audit:_fmt_seconds fingerprint=882fd66a371c7442b94ba88ac801dd6ac4412a1abfe22a23ee78585471dc2a2d body_fp=68cc186360f15308947a60dadbb0bf883f34f1c5fcfa7fb94e01573ec2a8511a source_ref=71d2cd65b307abdd2377641ffa5bffdd9fab4954 -->
## `_fmt_seconds(s: float | None) -> str`

Format a duration in seconds as a human-readable string with adaptive units.

- Returns `"--"` for `None`, seconds for `< 60`, minutes for `< 3600`, hours otherwise.
<!-- trie:end -->