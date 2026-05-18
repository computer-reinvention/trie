"""Post-hoc analysis of `debug.jsonl` telemetry logs.

`trie sync`, `trie verify`, the MCP server, and every model call already emit
JSON-Lines telemetry into a configured log (see `trie/telemetry.py`). When
running an eval (especially the `with_trie` vs `without_trie` shape we're
building for httpx), the question is no longer "is the log being written" —
it's "how did the agent actually use trie during that run, and is that
different from the baseline?"

This module ingests one or two such logs and produces a focused, scriptable
summary:

- MCP tool usage by name, with error counts and most-asked qnames
- Sync activity (file count, symbols generated, tokens, cost) per model seen
- Retry behaviour (rate-limit / overloaded / timeout) — flags when the model
  client had to back off
- CLI invocation counts so a run's shape is visible at a glance

The renderer is intentionally compact: a single Rich console block per run,
or a side-by-side table when `--compare` is given. There's no streaming, no
filtering, no "show me every event" mode — that's what `jq` is for. This is
the descriptive summary you'd otherwise eyeball.

Construction is split into a pure data pipeline (`AuditSummary.from_log`)
and a renderer that takes one or two summaries. Both halves are testable
without touching the filesystem beyond reading a fixture JSONL.
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from collections.abc import Iterable
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

from rich.console import Console
from rich.table import Table

from trie.cost import ModelPricing, estimate_actual_cost, get_pricing

# ---------------------------------------------------------------------------
# Raw event model
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Event:
    """One JSONL line decoded into its `event` discriminator plus everything else.

    `ts` and `event` are stamped automatically by `telemetry.emit`, so we
    promote them to top-level attributes. All other emitter-supplied fields
    stay in `fields` as a flat dict — different event types carry different
    payloads and the audit summary picks them out by name.
    """

    ts: str
    event: str
    fields: dict[str, Any]

    @classmethod
    def from_json(cls, line: str) -> Event | None:
        """Parse one JSONL line. Returns None on malformed lines so the caller
        can count them without crashing the whole run. Real logs sometimes end
        mid-write when a process is killed; tolerating that is more useful
        than aborting."""
        line = line.strip()
        if not line:
            return None
        try:
            data = json.loads(line)
        except json.JSONDecodeError:
            return None
        if not isinstance(data, dict):
            return None
        event = data.pop("event", None)
        ts = data.pop("ts", "")
        if not isinstance(event, str) or not isinstance(ts, str):
            return None
        return cls(ts=ts, event=event, fields=data)


# ---------------------------------------------------------------------------
# Per-section stats
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class McpCallStats:
    """Aggregate statistics for one MCP tool (grep / read / trace).

    `not_found_count` and `empty_result_count` are tool-specific failure
    flavours worth surfacing separately: a `not_found` from `read` usually
    means the agent passed a guessed-up qname; an empty `grep` result means
    the agent's predicate didn't match anything. Both are diagnostic.

    `fallback_kinds` is grep-specific: when `grep` returns empty hits it
    attaches a discriminated `fallback` envelope describing why. Audit rolls
    those discriminator values up here so eval reports can show "of K empty
    greps, M produced text_match redirects, N were text_match_empty (typos),
    etc."
    """

    tool: str
    count: int = 0
    error_count: int = 0
    not_found_count: int = 0
    empty_result_count: int = 0
    total_duration_ms: int = 0
    total_response_bytes: int = 0
    top_qnames: tuple[tuple[str, int], ...] = ()
    fallback_kinds: dict[str, int] = field(default_factory=dict)

    @property
    def avg_duration_ms(self) -> float:
        return self.total_duration_ms / self.count if self.count else 0.0

    @property
    def avg_response_bytes(self) -> float:
        return self.total_response_bytes / self.count if self.count else 0.0


@dataclass(frozen=True)
class SyncStats:
    """Aggregate of every `sync_file` event in the log, plus derived cost.

    Cost is computed via `estimate_actual_cost` against the per-model pricing
    table; when a model has no pricing entry the corresponding tokens are
    still counted but the cost contribution from that model is zero. The
    derivation lives here instead of in the renderer so callers that consume
    the summary structurally (eg. tests, scripts via --json) see the same
    number the human-facing output does.
    """

    file_runs: int = 0
    symbols_generated: int = 0
    symbols_skipped: int = 0
    sections_removed: int = 0
    cold_count: int = 0
    diff_aware_count: int = 0
    input_tokens: int = 0
    output_tokens: int = 0
    cache_creation_tokens: int = 0
    cache_read_tokens: int = 0
    cost_usd: float = 0.0
    by_model: dict[str, dict[str, int]] = field(default_factory=dict)


@dataclass(frozen=True)
class RetryStats:
    """`model_call_retry` events: how often the client backed off and why."""

    total: int = 0
    by_reason: dict[str, int] = field(default_factory=dict)
    total_delay_seconds: float = 0.0


@dataclass(frozen=True)
class ParseStats:
    """Counts surfaced as a footer line so users know how complete the read was."""

    lines_total: int = 0
    lines_parsed: int = 0
    lines_malformed: int = 0


# ---------------------------------------------------------------------------
# Top-level summary
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class AuditSummary:
    """One run's compressed telemetry view.

    Construct via `AuditSummary.from_log(path)`. The structure is stable enough
    to JSON-serialise for scripting; `to_dict()` produces a representation
    suitable for `--json` output.
    """

    log_path: Path
    parse: ParseStats
    span_start: str | None
    span_end: str | None
    span_duration_seconds: float | None
    mcp: dict[str, McpCallStats]
    sync: SyncStats
    retries: RetryStats
    cli_invocations: tuple[tuple[str, int], ...]

    @classmethod
    def from_log(cls, path: Path) -> AuditSummary:
        """Single-pass JSONL ingestion. Tolerates malformed lines and missing
        fields, on the theory that a partial summary is more useful than a
        crash. Pricing lookups are memoised so a 5k-line log doesn't pay the
        cost N times."""
        if not path.exists():
            raise FileNotFoundError(f"telemetry log not found: {path}")

        lines_total = 0
        lines_parsed = 0
        events: list[Event] = []
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                lines_total += 1
                ev = Event.from_json(line)
                if ev is None:
                    continue
                lines_parsed += 1
                events.append(ev)

        return _summarise(events, log_path=path, lines_total=lines_total, lines_parsed=lines_parsed)

    def to_dict(self) -> dict[str, Any]:
        """JSON-friendly view. Used by `trie audit --json` and by tests that
        want to assert on structure without pinning to the renderer's exact
        whitespace."""
        return {
            "log_path": str(self.log_path),
            "parse": {
                "lines_total": self.parse.lines_total,
                "lines_parsed": self.parse.lines_parsed,
                "lines_malformed": self.parse.lines_malformed,
            },
            "span_start": self.span_start,
            "span_end": self.span_end,
            "span_duration_seconds": self.span_duration_seconds,
            "mcp": {
                tool: {
                    "count": s.count,
                    "error_count": s.error_count,
                    "not_found_count": s.not_found_count,
                    "empty_result_count": s.empty_result_count,
                    "avg_duration_ms": s.avg_duration_ms,
                    "avg_response_bytes": s.avg_response_bytes,
                    "top_qnames": list(s.top_qnames),
                    "fallback_kinds": dict(s.fallback_kinds),
                }
                for tool, s in self.mcp.items()
            },
            "sync": {
                "file_runs": self.sync.file_runs,
                "symbols_generated": self.sync.symbols_generated,
                "symbols_skipped": self.sync.symbols_skipped,
                "sections_removed": self.sync.sections_removed,
                "cold_count": self.sync.cold_count,
                "diff_aware_count": self.sync.diff_aware_count,
                "input_tokens": self.sync.input_tokens,
                "output_tokens": self.sync.output_tokens,
                "cache_creation_tokens": self.sync.cache_creation_tokens,
                "cache_read_tokens": self.sync.cache_read_tokens,
                "cost_usd": self.sync.cost_usd,
                "by_model": self.sync.by_model,
            },
            "retries": {
                "total": self.retries.total,
                "by_reason": self.retries.by_reason,
                "total_delay_seconds": self.retries.total_delay_seconds,
            },
            "cli_invocations": list(self.cli_invocations),
        }


# ---------------------------------------------------------------------------
# Aggregation
# ---------------------------------------------------------------------------


def _summarise(
    events: Iterable[Event],
    *,
    log_path: Path,
    lines_total: int,
    lines_parsed: int,
) -> AuditSummary:
    """Walk the event list once and bucket each event into its aggregate.

    Kept as a free function (rather than a classmethod on AuditSummary) so
    test fixtures can hand in a synthetic event list directly without going
    through the filesystem path.
    """
    mcp_calls: dict[str, list[Event]] = defaultdict(list)
    sync_events: list[Event] = []
    retry_events: list[Event] = []
    cli_events: list[Event] = []
    timestamps: list[str] = []

    for ev in events:
        timestamps.append(ev.ts)
        if ev.event == "mcp_call":
            tool = ev.fields.get("tool")
            if isinstance(tool, str):
                mcp_calls[tool].append(ev)
        elif ev.event == "sync_file":
            sync_events.append(ev)
        elif ev.event == "model_call_retry":
            retry_events.append(ev)
        elif ev.event == "cli":
            cli_events.append(ev)

    mcp = {tool: _mcp_stats(tool, evs) for tool, evs in mcp_calls.items()}
    sync = _sync_stats(sync_events)
    retries = _retry_stats(retry_events)
    cli_invocations = _cli_invocations(cli_events)
    span_start, span_end, span_duration = _span(timestamps)

    return AuditSummary(
        log_path=log_path,
        parse=ParseStats(
            lines_total=lines_total,
            lines_parsed=lines_parsed,
            lines_malformed=lines_total - lines_parsed,
        ),
        span_start=span_start,
        span_end=span_end,
        span_duration_seconds=span_duration,
        mcp=mcp,
        sync=sync,
        retries=retries,
        cli_invocations=cli_invocations,
    )


def _mcp_stats(tool: str, events: list[Event]) -> McpCallStats:
    """Build the per-tool stats. `top_qnames` is computed differently per tool:

    - read: the `qname` argument (when capture_args is on) names the symbol asked about.
    - trace: same, via `from_qname`.
    - grep: no single qname per call — predicates are diverse — so we leave it empty.
    """
    error_count = 0
    not_found_count = 0
    empty_result_count = 0
    total_duration_ms = 0
    total_response_bytes = 0
    qname_counter: Counter[str] = Counter()
    fallback_kinds: Counter[str] = Counter()

    for ev in events:
        f = ev.fields
        if f.get("result_kind") == "error":
            error_count += 1
            if f.get("error_code") == "not_found":
                not_found_count += 1
        total_duration_ms += int(f.get("duration_ms") or 0)
        total_response_bytes += int(f.get("response_bytes") or 0)

        # Tool-specific empty-result detection. Each tool's "I returned nothing
        # useful" shape is different, and conflating them would hide the signal.
        if tool == "grep" and f.get("result_kind") == "ok" and (f.get("result_count") or 0) == 0:
            empty_result_count += 1
        if tool == "trace" and f.get("result_kind") == "ok" and (f.get("nodes_count") or 0) <= 1:
            empty_result_count += 1
        # A read call with prose_chars == 0 means the symbol exists in the
        # graph but has no triefact section yet — agent got an empty body.
        if tool == "read" and f.get("result_kind") == "ok" and (f.get("prose_chars") or 0) == 0:
            empty_result_count += 1

        # grep's fallback discriminator (one of "none", "text_match",
        # "text_match_empty"). Present only on grep calls that returned empty.
        fb_kind = f.get("fallback_kind")
        if tool == "grep" and isinstance(fb_kind, str):
            fallback_kinds[fb_kind] += 1

        # Qname extraction — only when capture_args was on at the time of emit.
        args = f.get("args") or {}
        if not isinstance(args, dict):
            args = {}
        if tool == "read":
            q = args.get("qname")
            if isinstance(q, str) and q:
                qname_counter[q] += 1
        elif tool == "trace":
            q = args.get("from_qname")
            if isinstance(q, str) and q:
                qname_counter[q] += 1

    return McpCallStats(
        tool=tool,
        count=len(events),
        error_count=error_count,
        not_found_count=not_found_count,
        empty_result_count=empty_result_count,
        total_duration_ms=total_duration_ms,
        total_response_bytes=total_response_bytes,
        top_qnames=tuple(qname_counter.most_common(5)),
        fallback_kinds=dict(fallback_kinds),
    )


# Pricing memo lives at module level so back-to-back `from_log` calls (eg.
# `--compare`) don't re-traverse the pricing table for the same model twice.
_pricing_cache: dict[str, ModelPricing | None] = {}


def _pricing_for(model_id: str) -> ModelPricing | None:
    """Look up pricing, tolerating both `"anthropic/claude-..."` and bare `"claude-..."`.

    New runs stamp telemetry with the full `provider/model` id (see
    `AnthropicClient.full_model_id`), but older logs predate that and emit just the
    bare model name. Try the as-recorded form first, then fall back to prepending
    `"anthropic/"` so historical eval logs still produce costed summaries.
    """
    if model_id not in _pricing_cache:
        pricing = get_pricing(model_id)
        if pricing is None and "/" not in model_id:
            pricing = get_pricing(f"anthropic/{model_id}")
        _pricing_cache[model_id] = pricing
    return _pricing_cache[model_id]


def _sync_stats(events: list[Event]) -> SyncStats:
    """Roll every `sync_file` event into one bucket plus a per-model breakdown.

    Cost is computed by feeding each event's token counters through the same
    `estimate_actual_cost` the live `sync` command uses, so the summary's
    cost matches what the runner reported at exit. Events emitted by models
    without a pricing entry contribute zero cost but still count toward token
    totals — surfacing the model name in `by_model` makes the gap visible.
    """
    file_runs = len(events)
    symbols_generated = 0
    symbols_skipped = 0
    sections_removed = 0
    cold_count = 0
    diff_aware_count = 0
    input_tokens = 0
    output_tokens = 0
    cache_creation_tokens = 0
    cache_read_tokens = 0
    cost_usd = 0.0
    by_model: dict[str, dict[str, int]] = defaultdict(
        lambda: {
            "file_runs": 0,
            "input_tokens": 0,
            "output_tokens": 0,
            "cache_creation_tokens": 0,
            "cache_read_tokens": 0,
        }
    )

    for ev in events:
        f = ev.fields
        sg = int(f.get("symbols_generated") or 0)
        ss = int(f.get("symbols_skipped") or 0)
        sr = int(f.get("sections_removed") or 0)
        cold = int(f.get("regen_mode_cold") or 0)
        diff = int(f.get("regen_mode_diff_aware") or 0)
        it = int(f.get("input_tokens") or 0)
        ot = int(f.get("output_tokens") or 0)
        cct = int(f.get("cache_creation_input_tokens") or 0)
        crt = int(f.get("cache_read_input_tokens") or 0)
        model = str(f.get("model") or "unknown")

        symbols_generated += sg
        symbols_skipped += ss
        sections_removed += sr
        cold_count += cold
        diff_aware_count += diff
        input_tokens += it
        output_tokens += ot
        cache_creation_tokens += cct
        cache_read_tokens += crt

        bucket = by_model[model]
        bucket["file_runs"] += 1
        bucket["input_tokens"] += it
        bucket["output_tokens"] += ot
        bucket["cache_creation_tokens"] += cct
        bucket["cache_read_tokens"] += crt

        pricing = _pricing_for(model)
        if pricing is not None and (it + ot + cct + crt) > 0:
            cost_usd += estimate_actual_cost(
                cache_creation_input_tokens=cct,
                cache_read_input_tokens=crt,
                input_tokens=it,
                output_tokens=ot,
                pricing=pricing,
            )

    return SyncStats(
        file_runs=file_runs,
        symbols_generated=symbols_generated,
        symbols_skipped=symbols_skipped,
        sections_removed=sections_removed,
        cold_count=cold_count,
        diff_aware_count=diff_aware_count,
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        cache_creation_tokens=cache_creation_tokens,
        cache_read_tokens=cache_read_tokens,
        cost_usd=cost_usd,
        by_model=dict(by_model),
    )


def _retry_stats(events: list[Event]) -> RetryStats:
    by_reason: Counter[str] = Counter()
    total_delay = 0.0
    for ev in events:
        reason = str(ev.fields.get("reason") or "unknown")
        by_reason[reason] += 1
        total_delay += float(ev.fields.get("delay_seconds") or 0.0)
    return RetryStats(
        total=len(events),
        by_reason=dict(by_reason),
        total_delay_seconds=round(total_delay, 3),
    )


def _cli_invocations(events: list[Event]) -> tuple[tuple[str, int], ...]:
    counter: Counter[str] = Counter()
    for ev in events:
        sub = str(ev.fields.get("subcommand") or "(unknown)")
        counter[sub] += 1
    return tuple(counter.most_common())


def _span(timestamps: list[str]) -> tuple[str | None, str | None, float | None]:
    """Earliest and latest timestamps in the log, plus their delta in seconds.

    Telemetry stamps timestamps as `YYYY-MM-DDTHH:MM:SS.fffZ`. We parse the
    minimal RFC3339 shape; if a single line is malformed we just drop it from
    the span computation rather than abort.
    """
    if not timestamps:
        return None, None, None
    sorted_ts = sorted(timestamps)
    start = sorted_ts[0]
    end = sorted_ts[-1]
    try:
        start_dt = datetime.fromisoformat(start.replace("Z", "+00:00"))
        end_dt = datetime.fromisoformat(end.replace("Z", "+00:00"))
        return start, end, (end_dt - start_dt).total_seconds()
    except ValueError:
        return start, end, None


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------


def render(summary: AuditSummary, console: Console) -> None:
    """Print one summary as four Rich sections: header, MCP, sync, retries.

    Output is dense by design — the whole report should fit in a terminal
    pane without scrolling. Sections with no data are still printed (with a
    "no events" placeholder) so an unexpected empty section is visible as
    a finding rather than hidden as silence.
    """
    _render_header(summary, console)
    console.print()
    _render_mcp(summary.mcp, console)
    console.print()
    _render_sync(summary.sync, console)
    console.print()
    _render_retries(summary.retries, console)
    console.print()
    _render_cli(summary.cli_invocations, console)


def render_comparison(baseline: AuditSummary, candidate: AuditSummary, console: Console) -> None:
    """Side-by-side render of two summaries with deltas.

    `baseline` is the reference run (typically `without_trie`); `candidate` is
    the run being evaluated (`with_trie`). Deltas are reported on the candidate
    side as `(±N)`. When a section is missing from one run the corresponding
    column shows `--` so the asymmetry is loud rather than papered over.
    """
    _render_compare_header(baseline, candidate, console)
    console.print()
    _render_compare_mcp(baseline.mcp, candidate.mcp, console)
    console.print()
    _render_compare_sync(baseline.sync, candidate.sync, console)
    console.print()
    _render_compare_retries(baseline.retries, candidate.retries, console)


# --- single-run renderers ---


def _render_header(s: AuditSummary, console: Console) -> None:
    console.print(f"[bold]Audit:[/bold] {s.log_path}")
    span = (
        f"{s.span_start} → {s.span_end} ({_fmt_seconds(s.span_duration_seconds)})"
        if s.span_start
        else "[dim](no timestamped events)[/dim]"
    )
    console.print(f"  span:  {span}")
    console.print(
        f"  lines: {s.parse.lines_parsed} parsed"
        + (
            f" · [yellow]{s.parse.lines_malformed} malformed[/yellow]"
            if s.parse.lines_malformed
            else ""
        )
    )


def _render_mcp(mcp: dict[str, McpCallStats], console: Console) -> None:
    if not mcp:
        console.print("[bold]MCP calls[/bold]: [dim]none[/dim]")
        return
    table = Table(title="MCP calls", title_style="bold", show_header=True, header_style="bold")
    table.add_column("tool")
    table.add_column("count", justify="right")
    table.add_column("errors", justify="right")
    table.add_column("empty", justify="right")
    table.add_column("avg ms", justify="right")
    table.add_column("avg bytes", justify="right")
    table.add_column("top qname")
    for tool in ("grep", "read", "trace"):
        stats = mcp.get(tool)
        if stats is None:
            table.add_row(tool, "0", "0", "0", "--", "--", "--")
            continue
        top = stats.top_qnames[0][0] if stats.top_qnames else "[dim]--[/dim]"
        if len(top) > 50:
            top = top[:47] + "…"
        table.add_row(
            tool,
            str(stats.count),
            _err_cell(stats.error_count),
            _err_cell(stats.empty_result_count),
            f"{stats.avg_duration_ms:.0f}",
            f"{stats.avg_response_bytes:.0f}",
            top,
        )
    # Surface any other tool names (forward-compat: if we add a fourth tool later).
    for tool, stats in mcp.items():
        if tool in ("grep", "read", "trace"):
            continue
        table.add_row(
            tool,
            str(stats.count),
            str(stats.error_count),
            "--",
            f"{stats.avg_duration_ms:.0f}",
            f"{stats.avg_response_bytes:.0f}",
            "--",
        )
    console.print(table)

    # grep fallback breakdown: one extra line when the eval saw fallback
    # activity. Tells the operator at a glance whether agents are hitting
    # typo paths (`text_match_empty`), the no-name-contains path (`none`),
    # or successfully getting redirected to body matches (`text_match`).
    grep_stats = mcp.get("grep")
    if grep_stats is not None and grep_stats.fallback_kinds:
        parts = ", ".join(f"{k}={n}" for k, n in sorted(grep_stats.fallback_kinds.items()))
        console.print(f"  [dim]grep fallback:[/dim] {parts}")


def _render_sync(s: SyncStats, console: Console) -> None:
    if s.file_runs == 0:
        console.print("[bold]Sync[/bold]: [dim]no sync_file events[/dim]")
        return
    table = Table(title="Sync", title_style="bold", show_header=False, box=None, padding=(0, 2))
    table.add_column("k", style="dim")
    table.add_column("v", justify="right")
    table.add_row("file runs", str(s.file_runs))
    table.add_row("symbols generated", str(s.symbols_generated))
    table.add_row("symbols skipped (pass-through)", str(s.symbols_skipped))
    table.add_row("sections removed", str(s.sections_removed))
    table.add_row("cold writes", str(s.cold_count))
    table.add_row("diff-aware regens", str(s.diff_aware_count))
    table.add_row("input tokens", f"{s.input_tokens:,}")
    table.add_row("output tokens", f"{s.output_tokens:,}")
    table.add_row("cache create tokens", f"{s.cache_creation_tokens:,}")
    table.add_row("cache read tokens", f"{s.cache_read_tokens:,}")
    table.add_row("cost (USD)", f"${s.cost_usd:.4f}" if s.cost_usd > 0 else "[dim]--[/dim]")
    console.print(table)
    if len(s.by_model) > 1:
        console.print("  [dim]by model:[/dim]")
        for model, b in s.by_model.items():
            console.print(
                f"    {model}: {b['file_runs']} run(s), "
                f"{b['input_tokens']:,} in / {b['output_tokens']:,} out"
            )


def _render_retries(s: RetryStats, console: Console) -> None:
    if s.total == 0:
        console.print("[bold]Retries[/bold]: [green]none[/green] (no 429/529/timeout)")
        return
    reasons = ", ".join(f"{r}={n}" for r, n in sorted(s.by_reason.items()))
    console.print(
        f"[bold]Retries[/bold]: [yellow]{s.total}[/yellow] "
        f"({reasons}; total backoff {s.total_delay_seconds:.1f}s)"
    )


def _render_cli(invocations: tuple[tuple[str, int], ...], console: Console) -> None:
    if not invocations:
        return
    parts = ", ".join(f"{sub} x{n}" for sub, n in invocations)
    console.print(f"[bold]CLI[/bold]: {parts}")


# --- comparison renderers ---


def _render_compare_header(
    baseline: AuditSummary, candidate: AuditSummary, console: Console
) -> None:
    console.print("[bold]Compare[/bold]")
    console.print(f"  baseline:  {baseline.log_path}")
    console.print(f"  candidate: {candidate.log_path}")


def _render_compare_mcp(
    baseline: dict[str, McpCallStats],
    candidate: dict[str, McpCallStats],
    console: Console,
) -> None:
    table = Table(title="MCP calls", title_style="bold", show_header=True, header_style="bold")
    table.add_column("tool")
    table.add_column("baseline", justify="right")
    table.add_column("candidate", justify="right")
    table.add_column("Δ", justify="right")

    tools = sorted({"grep", "read", "trace", *baseline.keys(), *candidate.keys()})
    for tool in tools:
        b = baseline.get(tool)
        c = candidate.get(tool)
        b_count = b.count if b else 0
        c_count = c.count if c else 0
        table.add_row(
            tool,
            str(b_count),
            str(c_count),
            _delta(b_count, c_count),
        )
    console.print(table)


def _render_compare_sync(b: SyncStats, c: SyncStats, console: Console) -> None:
    if b.file_runs == 0 and c.file_runs == 0:
        return
    table = Table(title="Sync", title_style="bold", show_header=True, header_style="bold")
    table.add_column("metric")
    table.add_column("baseline", justify="right")
    table.add_column("candidate", justify="right")
    table.add_column("Δ", justify="right")
    rows = [
        ("file runs", b.file_runs, c.file_runs),
        ("symbols generated", b.symbols_generated, c.symbols_generated),
        ("cold writes", b.cold_count, c.cold_count),
        ("diff-aware regens", b.diff_aware_count, c.diff_aware_count),
        ("input tokens", b.input_tokens, c.input_tokens),
        ("output tokens", b.output_tokens, c.output_tokens),
    ]
    for label, bv, cv in rows:
        table.add_row(label, f"{bv:,}", f"{cv:,}", _delta(bv, cv))
    table.add_row(
        "cost (USD)",
        f"${b.cost_usd:.4f}" if b.cost_usd else "--",
        f"${c.cost_usd:.4f}" if c.cost_usd else "--",
        _delta_money(b.cost_usd, c.cost_usd),
    )
    console.print(table)


def _render_compare_retries(b: RetryStats, c: RetryStats, console: Console) -> None:
    if b.total == 0 and c.total == 0:
        console.print("[bold]Retries[/bold]: [green]none on either side[/green]")
        return
    console.print(
        f"[bold]Retries[/bold]: baseline={b.total} candidate={c.total} "
        f"(Δ {_delta(b.total, c.total)})"
    )


# --- helpers ---


def _delta(b: int, c: int) -> str:
    d = c - b
    if d == 0:
        return "0"
    return f"[green]+{d}[/green]" if d > 0 else f"[red]{d}[/red]"


def _delta_money(b: float, c: float) -> str:
    d = c - b
    if abs(d) < 1e-6:
        return "$0.0000"
    return f"[green]+${d:.4f}[/green]" if d > 0 else f"[red]-${abs(d):.4f}[/red]"


def _err_cell(n: int) -> str:
    if n == 0:
        return "0"
    return f"[yellow]{n}[/yellow]"


def _fmt_seconds(s: float | None) -> str:
    if s is None:
        return "--"
    if s < 60:
        return f"{s:.1f}s"
    if s < 3600:
        return f"{s / 60:.1f}m"
    return f"{s / 3600:.2f}h"
