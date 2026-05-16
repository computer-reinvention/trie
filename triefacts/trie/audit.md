---
trie_version: 0.1.0
source: trie/audit.py
file_fingerprint: ac484a4249aa545e89271b9bbbb864349b737e55e544991da4f46a938d804213
last_synced_at: '2026-05-16T11:22:56Z'
description: Post-hoc analysis of `debug.jsonl` telemetry logs.
defines:
- kind: class
  qualified_name: trie/audit:Event
  lines: 50-82
- kind: method
  qualified_name: trie/audit:Event.from_json
  lines: 64-82
- kind: class
  qualified_name: trie/audit:McpCallStats
  lines: 91-115
- kind: method
  qualified_name: trie/audit:McpCallStats.avg_duration_ms
  lines: 110-111
- kind: method
  qualified_name: trie/audit:McpCallStats.avg_response_bytes
  lines: 114-115
- kind: class
  qualified_name: trie/audit:SyncStats
  lines: 119-141
- kind: class
  qualified_name: trie/audit:RetryStats
  lines: 145-150
- kind: class
  qualified_name: trie/audit:ParseStats
  lines: 154-159
- kind: class
  qualified_name: trie/audit:AuditSummary
  lines: 168-255
- kind: method
  qualified_name: trie/audit:AuditSummary.from_log
  lines: 187-207
- kind: method
  qualified_name: trie/audit:AuditSummary.to_dict
  lines: 209-255
- kind: function
  qualified_name: trie/audit:_summarise
  lines: 263-315
- kind: function
  qualified_name: trie/audit:_mcp_stats
  lines: 318-374
- kind: function
  qualified_name: trie/audit:_pricing_for
  lines: 382-395
- kind: function
  qualified_name: trie/audit:_sync_stats
  lines: 398-481
- kind: function
  qualified_name: trie/audit:_retry_stats
  lines: 484-495
- kind: function
  qualified_name: trie/audit:_cli_invocations
  lines: 498-503
- kind: function
  qualified_name: trie/audit:_span
  lines: 506-523
- kind: function
  qualified_name: trie/audit:render
  lines: 531-547
- kind: function
  qualified_name: trie/audit:render_comparison
  lines: 550-564
- kind: function
  qualified_name: trie/audit:_render_header
  lines: 570-585
- kind: function
  qualified_name: trie/audit:_render_mcp
  lines: 588-630
- kind: function
  qualified_name: trie/audit:_render_sync
  lines: 633-658
- kind: function
  qualified_name: trie/audit:_render_retries
  lines: 661-669
- kind: function
  qualified_name: trie/audit:_render_cli
  lines: 672-676
- kind: function
  qualified_name: trie/audit:_render_compare_header
  lines: 682-687
- kind: function
  qualified_name: trie/audit:_render_compare_mcp
  lines: 690-713
- kind: function
  qualified_name: trie/audit:_render_compare_sync
  lines: 716-740
- kind: function
  qualified_name: trie/audit:_render_compare_retries
  lines: 743-750
- kind: function
  qualified_name: trie/audit:_delta
  lines: 756-760
- kind: function
  qualified_name: trie/audit:_delta_money
  lines: 763-767
- kind: function
  qualified_name: trie/audit:_err_cell
  lines: 770-773
- kind: function
  qualified_name: trie/audit:_fmt_seconds
  lines: 776-783
incoming_refs: 26
outgoing_refs: 2
---
<!-- trie:section symbol=trie/audit:Event fingerprint=4f541f8d3d2bb0b895f2767d53ef25779e2040966277f1c1f2f2d70115027c1b body_fp=fa776520acbdf5c8ef67f03907747776acbb5c6a809dcfec2a2a4d702f70da81 source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `Event(ts: str, event: str, fields: dict[str, Any])`

Frozen dataclass representing one decoded JSONL telemetry line.

- `fields`: all emitter-supplied fields beyond `ts` and `event`, keyed by name
- `from_json`: returns `None` for empty, malformed, or structurally invalid lines
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:Event.from_json fingerprint=a703f11e700aba5f7cc3f9ce0851ddc30910d7abf7a0e0e29a5d9094d7405cc8 body_fp=09b25f83ab5311ff89ea51a69b963571dbede662e8f4aa850cf998d63c2cdaae source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `Event.from_json(cls, line: str) -> Event | None`

Parse one JSONL line into an `Event`, returning `None` for empty, malformed, or non-dict lines.
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:McpCallStats fingerprint=8bbb011cf0ef07208fd9b0ca0f78a9c1f33b3af1cfd49fdc4a64ec1cc19f7e14 body_fp=adbfda6954cfa987e226bd4d3b395c993a039de137d3ed1f575b5094cda1ca8a source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `McpCallStats(tool, count, error_count, not_found_count, empty_result_count, total_duration_ms, total_response_bytes, top_qnames)`

Frozen aggregate statistics for one MCP tool across all calls in a log.

- `not_found_count`: calls where the tool returned `error_code == "not_found"`
- `empty_result_count`: tool-specific zero-result outcomes (no matches, empty body, single node)
- `top_qnames`: up to 5 most-requested qnames, as `(qname, count)` pairs
- `avg_duration_ms`: derived; zero when `count == 0`
- `avg_response_bytes`: derived; zero when `count == 0`
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:McpCallStats.avg_duration_ms fingerprint=84f86f6d52648051332f475bb2db0b3a1f00d72b9f17d5ae50742db4fa421a55 body_fp=5833f82410c19720ad2b5330a67d10992f3eaafafc4b4a851e4ca2e190a9596e source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `avg_duration_ms(self) -> float`

Return mean duration in milliseconds across all calls, or `0.0` if count is zero.
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:McpCallStats.avg_response_bytes fingerprint=011d16cbf949693061e94de7dc3a2c520500347177086267b464f530e60d5b02 body_fp=21f7325a5137594e5cb97a0d0677961acab9408ccd81e7054d8cbf106cbbc521 source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `avg_response_bytes(self) -> float`

Return mean response size in bytes across all calls, or 0.0 if count is zero.
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:SyncStats fingerprint=28cf1d88eb4a0e5a0951850dc3573d868f2eae7668870af42456d93313e285dc body_fp=30cbdb2ab2ebb36273d1f63645d510ef409f06c451361f68eb09c319626cbe29 source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `SyncStats`

Aggregate token, cost, and file-level counters from all `sync_file` events in a log.

- `cost_usd`: derived via `estimate_actual_cost`; zero when model has no pricing entry.
- `by_model`: per-model breakdown of runs and token counts, keyed by model id.
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:RetryStats fingerprint=67878b92223cb78412169667fbf2f4e8901268f7ca09538b21d07e6467e73d6b body_fp=08049b82334c02421167256fb2fb2bb4e0d164b0b9e923ff336de211db07cb8a source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `RetryStats(total=0, by_reason={}, total_delay_seconds=0.0)`

Aggregate `model_call_retry` events recording backoff frequency, reason breakdown, and cumulative delay.
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:ParseStats fingerprint=7b0640a9557a90cdb8287f36e1894dc529c70ddff0f77ec612cc5e5224a15f84 body_fp=fa6f25f6f1b0c8983a99c0bbd2d254470d77d61a6ea48e32fd28631b224b207f source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `ParseStats(lines_total: int = 0, lines_parsed: int = 0, lines_malformed: int = 0)`

Count of JSONL lines read, successfully parsed, and skipped due to malformation.
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:AuditSummary fingerprint=b17c11f1ccd5c8944f55d0f0c0b2e5c9f14363119c1fa3f8f70f974ef989a3a7 body_fp=cda2a3ace957742b29aae46d2a4f72d428b5a564e8a7567874daef354aabe409 source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `AuditSummary`

Compressed telemetry view for one run, built via `AuditSummary.from_log(path)`.

- `from_log`: single-pass JSONL ingestion; raises `FileNotFoundError` if path absent.
- `to_dict`: returns JSON-serialisable dict for `--json` output or test assertions.
- `mcp`: keyed by tool name (`locate`/`explain`/`walk`).
- `cli_invocations`: subcommand counts as a sorted tuple of `(name, count)` pairs.
- `span_duration_seconds`: `None` if timestamps are absent or unparseable.
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:AuditSummary.from_log fingerprint=8fe7c2361cf7c16c905a99b261122cde88a56e973ad2461fd1a45a330fa26408 body_fp=8704593df78fa9e73e84415eb3df74f96447881479af549e8609d6a62eee79e1 source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `AuditSummary.from_log(cls, path: Path) -> AuditSummary`

Parse a JSONL telemetry log in a single pass, tolerating malformed lines, and return a populated `AuditSummary`.

- `path`: must exist; raises `FileNotFoundError` otherwise.
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:AuditSummary.to_dict fingerprint=78d3dfc88e53c9fbebde56bfba4c863dab7c588ccdb29f6ce3552970d682d541 body_fp=3f770d7baec29e723afae0ad031ab008f26fc0da9f2d7e12c1dd03a26b1a773d source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `to_dict(self) -> dict[str, Any]`

Serialize the summary to a JSON-friendly dict for `--json` output or structural assertions in tests.
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:_summarise fingerprint=30ac0aadb46b11f12857866dd2cfe21b3d5d8c3439f4dd95d8394205efea99b1 body_fp=b6765309f65b64e6d5ac40d7fbeec45734554b34d3eb85316b27fd995cf36da2 source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `_summarise(events: Iterable[Event], *, log_path: Path, lines_total: int, lines_parsed: int) -> AuditSummary`

Bucket a pre-parsed event list into an `AuditSummary` in a single pass.

- `events`: synthetic or file-sourced; not re-read from disk.
- `lines_total` / `lines_parsed`: forwarded into `ParseStats`; malformed count is derived as the difference.
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:_mcp_stats fingerprint=9960260d539da484dfc8d12b9fd52e4b3a07c6511cc586ffa04ea9eeaaa23861 body_fp=3fde8a6f59a1fb4b09431e6f837b7bfc52281ed7487d43c3691cd36d694d246b source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `_mcp_stats(tool: str, events: list[Event]) -> McpCallStats`

Build aggregate per-tool statistics from raw MCP call events.

- `top_qnames`: top-5 qnames for `explain`/`walk`; empty for `locate`
- `empty_result_count`: tool-specific logic — zero results for `locate`, ≤1 node for `walk`, zero prose chars for `explain`
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:_pricing_for fingerprint=81bc5640eca955efcad34e67471ba90c6f7f0fafea2861b567f92ccef61b922a body_fp=90a76c85c42b6065f880bef239d8d4a45b47bd3357b926d1d36f6fc2741aff19 source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `_pricing_for(model_id: str) -> ModelPricing | None`

Look up cached pricing for a model, falling back to `anthropic/` prefix for bare model names.

- Returns `None` when no pricing entry exists for the model.
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:_sync_stats fingerprint=bd0946bd0a48c1e3b58ef1d5233c5265fb3aa18bccac0be13c57ba9c2bdadd25 body_fp=240ebc3cf4e0046f5f129604ace03e4d9dca8ad649c79dfa2b63a8a7aaa87d13 source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `_sync_stats(events: list[Event]) -> SyncStats`

Roll every `sync_file` event into a `SyncStats` aggregate with per-model token breakdown and computed USD cost.

- `cost_usd`: summed via `estimate_actual_cost`; models without pricing contribute zero
- `by_model`: keyed by model id string, tracks file runs and token counts per model
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:_retry_stats fingerprint=c99848ca78c758eb1dab4f2006736de48377634aac3653eae3bf49ddd4ec72c1 body_fp=4736a95cfc1a55e71bee667dc029be2af4c9c9e84fd893f5c8dc13e1f64f5ab6 source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `_retry_stats(events: list[Event]) -> RetryStats`

Aggregate `model_call_retry` events into total count, per-reason breakdown, and summed backoff delay.
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:_cli_invocations fingerprint=3ee3208f853f5da73a48967394afe7e736b1a8f9a4eee71547f1fb17952bab59 body_fp=2f9ecfb406a74d46410d2ab112c371520f8c9428bf6aac5f868e1fa4e70d3129 source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `_cli_invocations(events: list[Event]) -> tuple[tuple[str, int], ...]`

Count CLI subcommand invocations from `cli` events, returning all subcommands sorted by frequency.
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:_span fingerprint=06219108afd96504879d771b07d5dcfa0ccf1aac6d7a32802b7eaea42148b7c3 body_fp=825c140d310922515ddd202e07dc537a55fedbe4cdc8c9a9dc00b506b7f4744b source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `_span(timestamps: list[str]) -> tuple[str | None, str | None, float | None]`

Return the earliest timestamp, latest timestamp, and duration in seconds from a list of RFC3339 strings.

- Returns `(None, None, None)` when `timestamps` is empty.
- Returns `(start, end, None)` when timestamps are present but unparseable.
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:render fingerprint=6ccf5ffa07f19d23bca8120c8ce61d512da9d2abc09c1222cdfedfc64d109cf5 body_fp=a43d23f6dec4d316138c17f16ef3bdc49081ba2ea63dbfcfd8478fb5f7df7596 source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `render(summary: AuditSummary, console: Console) -> None`

Print one `AuditSummary` as four Rich sections: header, MCP calls, sync stats, and retries.

- Empty sections print a placeholder rather than being silently omitted.
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:render_comparison fingerprint=33c6ffc23a1c792792b99d3ec221eeb327a55a6878b1a676305381a70c3ed838 body_fp=3df54e82f0312e8e3a0044bc8c86081d8171631a0359e088e218f8fc29ddf4ac source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `render_comparison(baseline: AuditSummary, candidate: AuditSummary, console: Console) -> None`

Render two audit summaries side-by-side with per-metric deltas to a Rich console.

- `baseline`: reference run (typically `without_trie`); shown in the left column.
- `candidate`: evaluated run (`with_trie`); deltas reported relative to baseline.
- Missing sections render as `--` rather than being silently omitted.
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:_render_header fingerprint=028de2583de75b8da4d67b66301b1c96b959a81bd4d63e86f9fb5c9e004f8f93 body_fp=4b27abfa96a6b9cec4923b325ad4230e68b658c24921a22c36bde53ecc67d68f source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `_render_header(s: AuditSummary, console: Console) -> None`

Print the log path, time span, and parse-line counts to the console.
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:_render_mcp fingerprint=c5fe7d2dc3e6919b3ae9f23bb3676067479576db9b301732c9785b6554f7385b body_fp=6645170113ba350e72f792fc0343f6f3f5d94ab3f90f85916c8b4cef1fe66901 source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `_render_mcp(mcp: dict[str, McpCallStats], console: Console) -> None`

Render a Rich table of MCP tool call statistics for `locate`, `explain`, and `walk`.

- `mcp`: empty dict prints a "none" placeholder instead of a table.
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:_render_sync fingerprint=f52f1b1727ea65ecbb99e76d18a16787eceffb3e6d9053e8b4ce403868cbe012 body_fp=15aebf67f4d4572fc6dab758c5ea761813787e36a5601f32450418a883d6763e source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `_render_sync(s: SyncStats, console: Console) -> None`

Render a `SyncStats` instance as a compact Rich key-value table, including a per-model breakdown when multiple models are present.
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:_render_retries fingerprint=a1e2b8663c11620776005312a803cfffcf1ae91cca4e48c8128c189fae731c25 body_fp=65d3dcd923bf73bbd1e312510ad54779435e7619caa915cdeeb1b4a0430eeb31 source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `_render_retries(s: RetryStats, console: Console) -> None`

Render retry backoff summary; prints green "none" when zero, yellow count with per-reason breakdown and total delay when nonzero.
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:_render_cli fingerprint=795aa283d5cd30e94e9b96ed812cf35ec66ed522b88ff2838f5c64cfe7b98c96 body_fp=3673f97b21df78bdaba048344ac7e89f33392ab3d76ee31018a5e452b7d7bac7 source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `_render_cli(invocations: tuple[tuple[str, int], ...], console: Console) -> None`

Render CLI subcommand invocation counts as a single `Console` line; no-ops when `invocations` is empty.
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:_render_compare_header fingerprint=213ee3d022bcb9f7ab2bcb6bc12bbe61671beefaca19ce6e29ded0f691c30947 body_fp=6a4baada5789abda24afa8b40771c5670f6406a59530a8e8b94ee2fe6861a6a8 source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `_render_compare_header(baseline: AuditSummary, candidate: AuditSummary, console: Console) -> None`

Print the "Compare" heading with both log paths to the console.
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:_render_compare_mcp fingerprint=4bea8978b700153d1b3cb4437e50dada0ed48bd0c06a28a114112a2f86a6c55f body_fp=a4e9b77faa00d50b27ce7759b21a052f779f3a2927772bdde95453556c14dc44 source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `_render_compare_mcp(baseline: dict[str, McpCallStats], candidate: dict[str, McpCallStats], console: Console) -> None`

Render a side-by-side Rich table of MCP call counts for baseline vs candidate, with a delta column.
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:_render_compare_sync fingerprint=5a67d6c4a9165c95996b28c6f58e5b64d6e6e563f0ba4421f0e0a4edc4237511 body_fp=8833ac26dfb0946eb0ebc6d7a38eee2ceac12e26cb00fbd2f5fb28570a1871d3 source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `_render_compare_sync(b: SyncStats, c: SyncStats, console: Console) -> None`

Render a side-by-side Rich table comparing sync metrics between baseline and candidate, with deltas.

- Skips output entirely when both runs have zero file runs.
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:_render_compare_retries fingerprint=67562a410e2c06a1229e5299fa48f024421177c6af554919c51dfc76510355d7 body_fp=8ec039269b530e0a7ccbca38f2c94857de0b64ed7b0406b3658be4a542adae93 source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `_render_compare_retries(b: RetryStats, c: RetryStats, console: Console) -> None`

Print a one-line retry comparison between baseline and candidate, with delta.
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:_delta fingerprint=d85999dc29db9403c37ab0a63a763ed396ce0ff337f1b0f06ac9d1b4c6af3a1b body_fp=081da7c6602dcdf122cd4db13fc4320f9c6d198b0470a6c9ae7316d007a36aec source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `_delta(b: int, c: int) -> str`

Format the integer difference `c - b` as a Rich-coloured string.

- Returns `"0"`, green `+N`, or red `-N`.
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:_delta_money fingerprint=48efc2af497d07b81c90d8dc4e078be3812a2d7adb0d8da0bf07ae4578d06124 body_fp=9ae2f7448ce6df031b4b54dce592c886457487aad5d8666858a8df8d293e2292 source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `_delta_money(b: float, c: float) -> str`

Format the monetary delta between two USD cost values as a coloured Rich string.

- Returns `"$0.0000"` when the absolute difference is below `1e-6`.
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:_err_cell fingerprint=328ffa7dd16dfd32571fa7bfb5fbd758965687c94186e1759ae361c45b2d733a body_fp=73593ff108ee1bdc4afb9978c3b781b625444785121a242f2147d409ada2806c source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `_err_cell(n: int) -> str`

Format an integer count as a yellow Rich markup string when non-zero, plain `"0"` otherwise.
<!-- trie:end -->

<!-- trie:section symbol=trie/audit:_fmt_seconds fingerprint=882fd66a371c7442b94ba88ac801dd6ac4412a1abfe22a23ee78585471dc2a2d body_fp=48deae9cd620d704339a97b1dbd9bdb325bc64553f16fb5c281e7e3f8f6186b6 source_ref=9199ba7d07a057fc5294735842b6dc55ccea55e4 -->
## `_fmt_seconds(s: float | None) -> str`

Format a duration in seconds as a human-readable string with adaptive units.

- Returns `"--"` for `None`, seconds for < 60, minutes for < 3600, else hours.
<!-- trie:end -->