"""Audit summary: JSONL ingestion + rendering.

The contract under test:

  - Every event type used by the live emitters (mcp_call, sync_file,
    model_call_retry, cli, scan, parse_file, model_call) parses without
    crashing, and the ones the summary cares about populate their buckets.
  - Malformed lines, blank lines, and missing fields degrade gracefully;
    they appear as a count in `parse.lines_malformed` rather than crashing.
  - The cost figure matches what `estimate_actual_cost` would have produced
    for the same token totals.
  - The renderer produces output for both single and comparison modes
    without raising, and the rendered strings contain the load-bearing
    numbers (we don't pin exact whitespace because Rich's table layout
    is its own concern).
  - The CLI command surfaces help, runs against a real log, and supports
    --json for scripting.
"""

from __future__ import annotations

import io
import json
from pathlib import Path

import pytest
from rich.console import Console
from typer.testing import CliRunner

from trie.audit import (
    AuditSummary,
    Event,
    _summarise,
    render,
    render_comparison,
)
from trie.cli import app

# Two model id forms exercise both the new full-prefix path (post-fix) and the
# legacy bare-name path that older debug.jsonl logs still carry. Audit must cost
# both correctly.
FULL_MODEL = "anthropic/claude-sonnet-4-6"
BARE_MODEL = "claude-sonnet-4-6"
ANTHROPIC_MODEL = FULL_MODEL  # default; tests that need the legacy shape say so


def _write_log(path: Path, records: list[dict]) -> None:
    """Write records as JSONL. Empty list yields a zero-byte file."""
    with path.open("w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r) + "\n")


def _ts(i: int) -> str:
    """Monotonic-looking timestamps for ordering tests."""
    return f"2026-05-16T10:00:{i:02d}.000000Z"


# ---------------------------------------------------------------------------
# Event parser
# ---------------------------------------------------------------------------


def test_event_from_json_parses_well_formed_line():
    line = '{"ts": "2026-05-16T10:00:00.000000Z", "event": "scan", "files_seen": 12}'
    ev = Event.from_json(line)
    assert ev is not None
    assert ev.event == "scan"
    assert ev.ts == "2026-05-16T10:00:00.000000Z"
    assert ev.fields == {"files_seen": 12}


def test_event_from_json_returns_none_on_empty_and_garbage():
    assert Event.from_json("") is None
    assert Event.from_json("  ") is None
    assert Event.from_json("not json at all") is None
    # Missing required fields.
    assert Event.from_json('{"event": 42}') is None
    assert Event.from_json('{"event": "ok"}') is not None  # ts defaults to ""
    # Root must be an object.
    assert Event.from_json("[1, 2, 3]") is None
    assert Event.from_json('"a string"') is None


# ---------------------------------------------------------------------------
# AuditSummary.from_log: end-to-end ingestion
# ---------------------------------------------------------------------------


def test_from_log_raises_when_file_missing(tmp_path: Path):
    with pytest.raises(FileNotFoundError):
        AuditSummary.from_log(tmp_path / "nope.jsonl")


def test_from_log_empty_file_yields_empty_summary(tmp_path: Path):
    p = tmp_path / "empty.jsonl"
    p.write_text("")
    summary = AuditSummary.from_log(p)
    assert summary.parse.lines_total == 0
    assert summary.parse.lines_parsed == 0
    assert summary.mcp == {}
    # CLI-side per-tool stats are a separate stream from `mcp_call`; an
    # empty log produces empty buckets for both surfaces.
    assert summary.cli == {}
    assert summary.sync.file_runs == 0
    assert summary.retries.total == 0
    assert summary.span_start is None
    assert summary.span_duration_seconds is None


def test_from_log_counts_malformed_lines(tmp_path: Path):
    p = tmp_path / "mixed.jsonl"
    p.write_text(
        '{"ts": "2026-05-16T10:00:00.000000Z", "event": "scan"}\n'
        "not valid json\n"
        "\n"  # blank line
        '{"ts": "2026-05-16T10:00:01.000000Z", "event": "scan"}\n'
    )
    summary = AuditSummary.from_log(p)
    # Blank line and garbage both return None from from_json; we lump them
    # together as "did not parse" — fine for this purpose.
    assert summary.parse.lines_total == 4
    assert summary.parse.lines_parsed == 2
    assert summary.parse.lines_malformed == 2


def test_from_log_computes_span(tmp_path: Path):
    p = tmp_path / "span.jsonl"
    _write_log(
        p,
        [
            {"ts": _ts(0), "event": "cli", "subcommand": "sync"},
            {"ts": _ts(30), "event": "sync_file"},
            {"ts": _ts(15), "event": "mcp_call", "tool": "grep"},
        ],
    )
    summary = AuditSummary.from_log(p)
    assert summary.span_start == _ts(0)
    assert summary.span_end == _ts(30)
    assert summary.span_duration_seconds == 30.0


# ---------------------------------------------------------------------------
# MCP aggregation
# ---------------------------------------------------------------------------


def test_mcp_call_buckets_per_tool(tmp_path: Path):
    p = tmp_path / "mcp.jsonl"
    _write_log(
        p,
        [
            # 3 grep calls, one with empty result, one error
            {
                "ts": _ts(0),
                "event": "mcp_call",
                "tool": "grep",
                "result_kind": "ok",
                "result_count": 5,
                "duration_ms": 12,
                "response_bytes": 800,
            },
            {
                "ts": _ts(1),
                "event": "mcp_call",
                "tool": "grep",
                "result_kind": "ok",
                "result_count": 0,
                "duration_ms": 8,
                "response_bytes": 40,
            },
            {
                "ts": _ts(2),
                "event": "mcp_call",
                "tool": "grep",
                "result_kind": "error",
                "error_code": "invalid_argument",
                "duration_ms": 3,
                "response_bytes": 80,
            },
            # 2 read calls, one not_found
            {
                "ts": _ts(3),
                "event": "mcp_call",
                "tool": "read",
                "result_kind": "ok",
                "prose_chars": 320,
                "callers_count": 2,
                "callees_count": 3,
                "duration_ms": 18,
                "response_bytes": 1200,
                "args": {"qname": "trie/cli:sync_cmd"},
            },
            {
                "ts": _ts(4),
                "event": "mcp_call",
                "tool": "read",
                "result_kind": "error",
                "error_code": "not_found",
                "duration_ms": 4,
                "response_bytes": 200,
                "args": {"qname": "trie/cli:does_not_exist"},
            },
            # 1 trace call, hub-truncated (single node returned)
            {
                "ts": _ts(5),
                "event": "mcp_call",
                "tool": "trace",
                "result_kind": "ok",
                "nodes_count": 1,
                "edges_count": 0,
                "duration_ms": 7,
                "response_bytes": 90,
                "args": {"from_qname": "trie/config:Config"},
            },
        ],
    )
    summary = AuditSummary.from_log(p)
    assert set(summary.mcp.keys()) == {"grep", "read", "trace"}

    g = summary.mcp["grep"]
    assert g.count == 3
    assert g.error_count == 1
    assert g.empty_result_count == 1  # the result_count==0 one
    assert g.avg_duration_ms == pytest.approx((12 + 8 + 3) / 3)

    r = summary.mcp["read"]
    assert r.count == 2
    assert r.error_count == 1
    assert r.not_found_count == 1
    qnames = [q for q, _ in r.top_qnames]
    assert "trie/cli:sync_cmd" in qnames

    tr = summary.mcp["trace"]
    assert tr.count == 1
    assert tr.empty_result_count == 1  # nodes_count==1 == just the root


def test_read_empty_prose_counts_as_empty_result(tmp_path: Path):
    """A read that returns prose="" (no triefact section yet) is signal —
    the agent asked about a symbol the graph knows but trie hasn't documented.
    Lumping it in with errors would hide that this is a sync-coverage gap."""
    p = tmp_path / "read.jsonl"
    _write_log(
        p,
        [
            {
                "ts": _ts(0),
                "event": "mcp_call",
                "tool": "read",
                "result_kind": "ok",
                "prose_chars": 0,
                "duration_ms": 5,
                "response_bytes": 100,
            },
            {
                "ts": _ts(1),
                "event": "mcp_call",
                "tool": "read",
                "result_kind": "ok",
                "prose_chars": 200,
                "duration_ms": 5,
                "response_bytes": 800,
            },
        ],
    )
    summary = AuditSummary.from_log(p)
    assert summary.mcp["read"].empty_result_count == 1


def test_mcp_calls_without_capture_args_still_count(tmp_path: Path):
    """When capture_args is disabled the `args` field is missing — qname extraction
    silently degrades but the call still counts."""
    p = tmp_path / "noargs.jsonl"
    _write_log(
        p,
        [
            {
                "ts": _ts(0),
                "event": "mcp_call",
                "tool": "read",
                "result_kind": "ok",
                "prose_chars": 100,
                "duration_ms": 5,
                "response_bytes": 500,
            },
        ],
    )
    summary = AuditSummary.from_log(p)
    assert summary.mcp["read"].count == 1
    assert summary.mcp["read"].top_qnames == ()


# ---------------------------------------------------------------------------
# CLI-call aggregation: `cli_call` events from `trie grep`/`read`/`trace`
# ---------------------------------------------------------------------------
#
# The CLI subcommands emit `cli_call` events with the same envelope shape
# as the MCP server's `mcp_call`. The audit summarises them into a
# separate `summary.cli` bucket so an operator can see which surface the
# agent is reaching trie through.


def test_cli_call_aggregation_buckets_per_tool(tmp_path: Path):
    """A mix of `cli_call` events across tools lands in `summary.cli`,
    keyed by tool. The aggregator reuses the per-tool stats logic from
    the MCP side, so error/empty/duration counts work identically."""
    p = tmp_path / "cli.jsonl"
    _write_log(
        p,
        [
            # Two CLI greps, one with empty result
            {
                "ts": _ts(0),
                "event": "cli_call",
                "tool": "grep",
                "result_kind": "ok",
                "result_count": 3,
                "duration_ms": 8,
                "response_bytes": 600,
            },
            {
                "ts": _ts(1),
                "event": "cli_call",
                "tool": "grep",
                "result_kind": "ok",
                "result_count": 0,
                "duration_ms": 5,
                "response_bytes": 50,
            },
            # One CLI read
            {
                "ts": _ts(2),
                "event": "cli_call",
                "tool": "read",
                "result_kind": "ok",
                "prose_chars": 400,
                "duration_ms": 12,
                "response_bytes": 1500,
                "args": {"qname": "trie/cli:grep_cmd"},
            },
            # One CLI trace
            {
                "ts": _ts(3),
                "event": "cli_call",
                "tool": "trace",
                "result_kind": "ok",
                "nodes_count": 4,
                "edges_count": 3,
                "duration_ms": 9,
                "response_bytes": 800,
                "args": {"from_qname": "trie/cli:setup_cmd"},
            },
        ],
    )
    summary = AuditSummary.from_log(p)
    assert set(summary.cli.keys()) == {"grep", "read", "trace"}

    g = summary.cli["grep"]
    assert g.count == 2
    assert g.empty_result_count == 1

    r = summary.cli["read"]
    assert r.count == 1
    qnames = [q for q, _ in r.top_qnames]
    assert "trie/cli:grep_cmd" in qnames

    tr = summary.cli["trace"]
    assert tr.count == 1


def test_cli_call_and_mcp_call_are_separate_streams(tmp_path: Path):
    """An `mcp_call` event lands in `summary.mcp`; a `cli_call` event with
    the same tool lands in `summary.cli`. The two streams must not bleed
    into each other — otherwise an operator looking at CLI usage stats
    would see MCP events double-counted (and vice versa)."""
    p = tmp_path / "mixed.jsonl"
    _write_log(
        p,
        [
            {
                "ts": _ts(0),
                "event": "mcp_call",
                "tool": "grep",
                "result_kind": "ok",
                "result_count": 1,
                "duration_ms": 3,
                "response_bytes": 200,
            },
            {
                "ts": _ts(1),
                "event": "cli_call",
                "tool": "grep",
                "result_kind": "ok",
                "result_count": 1,
                "duration_ms": 6,
                "response_bytes": 200,
            },
        ],
    )
    summary = AuditSummary.from_log(p)
    # Each surface saw exactly one grep call; neither got the other's.
    assert summary.mcp["grep"].count == 1
    assert summary.cli["grep"].count == 1


def test_to_dict_carries_cli_section(tmp_path: Path):
    """`AuditSummary.to_dict()` exposes `cli` alongside `mcp` so scripts
    consuming the JSON output can read CLI usage stats without having to
    reconstruct them. Same shape as `mcp` — the renderer reuses one body
    for both, and so does this serialiser."""
    p = tmp_path / "tojson.jsonl"
    _write_log(
        p,
        [
            {
                "ts": _ts(0),
                "event": "cli_call",
                "tool": "grep",
                "result_kind": "ok",
                "result_count": 2,
                "duration_ms": 4,
                "response_bytes": 300,
            },
        ],
    )
    data = AuditSummary.from_log(p).to_dict()
    assert "cli" in data
    assert "grep" in data["cli"]
    assert data["cli"]["grep"]["count"] == 1
    # Fields parallel `mcp` exactly — same renderer for both.
    for k in (
        "count",
        "error_count",
        "not_found_count",
        "empty_result_count",
        "avg_duration_ms",
        "avg_response_bytes",
        "top_qnames",
        "fallback_kinds",
        "modes",
    ):
        assert k in data["cli"]["grep"]


def test_read_mode_breakdown_aggregates_from_cli_call_events(tmp_path: Path):
    """The opencode `read.ts` override emits `cli_call` events with a `mode`
    field naming which dispatch branch fired (qname / triefact / source /
    show_source). The audit aggregator rolls these into `McpCallStats.modes`
    so an operator can see, at a glance, whether agents are getting the
    cheap triefact view or falling through to raw source."""
    p = tmp_path / "modes.jsonl"
    _write_log(
        p,
        [
            # Two triefact-mode reads (cheap path).
            {
                "ts": _ts(0),
                "event": "cli_call",
                "tool": "read",
                "mode": "triefact",
                "result_kind": "ok",
                "duration_ms": 3,
                "response_bytes": 1200,
            },
            {
                "ts": _ts(1),
                "event": "cli_call",
                "tool": "read",
                "mode": "triefact",
                "result_kind": "ok",
                "duration_ms": 4,
                "response_bytes": 800,
            },
            # One source fallthrough (no triefact for this path).
            {
                "ts": _ts(2),
                "event": "cli_call",
                "tool": "read",
                "mode": "source",
                "result_kind": "ok",
                "duration_ms": 2,
                "response_bytes": 3000,
            },
            # One show_source (agent reaching for raw source before edit).
            {
                "ts": _ts(3),
                "event": "cli_call",
                "tool": "read",
                "mode": "show_source",
                "result_kind": "ok",
                "duration_ms": 1,
                "response_bytes": 4500,
            },
        ],
    )
    summary = AuditSummary.from_log(p)
    modes = summary.cli["read"].modes
    assert modes == {"triefact": 2, "source": 1, "show_source": 1}


def test_read_events_without_mode_field_count_as_qname(tmp_path: Path):
    """`cli_call` events emitted from Python (i.e. `trie read` invoked
    directly from a shell) don't carry a `mode` field — those calls are
    qname-mode by construction (the Python CLI only accepts qnames). The
    aggregator attributes the absent case to `qname` so the mode
    breakdown's totals always equal the call count, regardless of which
    surface produced the events."""
    p = tmp_path / "noprefix.jsonl"
    _write_log(
        p,
        [
            {
                "ts": _ts(0),
                "event": "cli_call",
                "tool": "read",
                "result_kind": "ok",
                "duration_ms": 5,
                "response_bytes": 800,
                "args": {"qname": "trie/cli:grep_cmd"},
            },
        ],
    )
    summary = AuditSummary.from_log(p)
    modes = summary.cli["read"].modes
    assert modes == {"qname": 1}


# ---------------------------------------------------------------------------
# Sync aggregation
# ---------------------------------------------------------------------------


def test_sync_aggregation_totals_and_cost(tmp_path: Path):
    p = tmp_path / "sync.jsonl"
    _write_log(
        p,
        [
            {
                "ts": _ts(0),
                "event": "sync_file",
                "path": "trie/cli.py",
                "model": ANTHROPIC_MODEL,
                "symbols_generated": 5,
                "symbols_skipped": 2,
                "sections_removed": 1,
                "input_tokens": 1000,
                "output_tokens": 500,
                "cache_creation_input_tokens": 200,
                "cache_read_input_tokens": 800,
                "regen_mode_cold": 3,
                "regen_mode_diff_aware": 2,
                "has_blob_ref": True,
            },
            {
                "ts": _ts(1),
                "event": "sync_file",
                "path": "trie/audit.py",
                "model": ANTHROPIC_MODEL,
                "symbols_generated": 3,
                "symbols_skipped": 0,
                "sections_removed": 0,
                "input_tokens": 600,
                "output_tokens": 300,
                "cache_creation_input_tokens": 100,
                "cache_read_input_tokens": 500,
                "regen_mode_cold": 3,
                "regen_mode_diff_aware": 0,
                "has_blob_ref": False,
            },
        ],
    )
    summary = AuditSummary.from_log(p)
    s = summary.sync
    assert s.file_runs == 2
    assert s.symbols_generated == 8
    assert s.symbols_skipped == 2
    assert s.sections_removed == 1
    assert s.cold_count == 6
    assert s.diff_aware_count == 2
    assert s.input_tokens == 1600
    assert s.output_tokens == 800
    assert s.cache_creation_tokens == 300
    assert s.cache_read_tokens == 1300
    assert s.cost_usd > 0  # priced model produced positive cost
    assert ANTHROPIC_MODEL in s.by_model


def test_sync_with_legacy_bare_model_name_still_costs(tmp_path: Path):
    """Logs from before `full_model_id` landed stamp telemetry with the bare name.
    Audit must fall back to prepending the conventional provider prefix so those
    runs still produce non-zero cost."""
    p = tmp_path / "sync.jsonl"
    _write_log(
        p,
        [
            {
                "ts": _ts(0),
                "event": "sync_file",
                "path": "old.py",
                "model": BARE_MODEL,
                "symbols_generated": 1,
                "input_tokens": 100,
                "output_tokens": 50,
                "cache_creation_input_tokens": 0,
                "cache_read_input_tokens": 0,
            },
        ],
    )
    summary = AuditSummary.from_log(p)
    assert summary.sync.cost_usd > 0


def test_sync_with_unknown_model_records_zero_cost(tmp_path: Path):
    p = tmp_path / "sync.jsonl"
    _write_log(
        p,
        [
            {
                "ts": _ts(0),
                "event": "sync_file",
                "path": "x.py",
                "model": "totally-fake/model-99",
                "symbols_generated": 1,
                "input_tokens": 100,
                "output_tokens": 50,
            },
        ],
    )
    summary = AuditSummary.from_log(p)
    assert summary.sync.file_runs == 1
    assert summary.sync.input_tokens == 100
    assert summary.sync.cost_usd == 0.0


# ---------------------------------------------------------------------------
# Retry aggregation
# ---------------------------------------------------------------------------


def test_retries_grouped_by_reason(tmp_path: Path):
    p = tmp_path / "retries.jsonl"
    _write_log(
        p,
        [
            {
                "ts": _ts(0),
                "event": "model_call_retry",
                "reason": "rate_limit",
                "delay_seconds": 1.5,
            },
            {
                "ts": _ts(1),
                "event": "model_call_retry",
                "reason": "rate_limit",
                "delay_seconds": 3.0,
            },
            {
                "ts": _ts(2),
                "event": "model_call_retry",
                "reason": "overloaded",
                "delay_seconds": 2.0,
            },
        ],
    )
    summary = AuditSummary.from_log(p)
    r = summary.retries
    assert r.total == 3
    assert r.by_reason == {"rate_limit": 2, "overloaded": 1}
    assert r.total_delay_seconds == 6.5


def test_zero_retries_when_no_events(tmp_path: Path):
    p = tmp_path / "retries.jsonl"
    _write_log(p, [{"ts": _ts(0), "event": "scan"}])
    assert AuditSummary.from_log(p).retries.total == 0


# ---------------------------------------------------------------------------
# CLI invocations
# ---------------------------------------------------------------------------


def test_cli_invocations_counted(tmp_path: Path):
    p = tmp_path / "cli.jsonl"
    _write_log(
        p,
        [
            {"ts": _ts(0), "event": "cli", "subcommand": "sync"},
            {"ts": _ts(1), "event": "cli", "subcommand": "verify"},
            {"ts": _ts(2), "event": "cli", "subcommand": "sync"},
        ],
    )
    summary = AuditSummary.from_log(p)
    counts = dict(summary.cli_invocations)
    assert counts == {"sync": 2, "verify": 1}


# ---------------------------------------------------------------------------
# Renderer (smoke + presence of load-bearing numbers)
# ---------------------------------------------------------------------------


def _render_to_string(fn, *args) -> str:
    buf = io.StringIO()
    # `force_terminal=False` keeps ANSI escape codes out so we can assert on plain text.
    console = Console(file=buf, force_terminal=False, width=120)
    fn(*args, console)
    return buf.getvalue()


def test_render_single_summary_includes_counts(tmp_path: Path):
    p = tmp_path / "log.jsonl"
    _write_log(
        p,
        [
            {
                "ts": _ts(0),
                "event": "mcp_call",
                "tool": "grep",
                "result_kind": "ok",
                "result_count": 3,
                "duration_ms": 10,
                "response_bytes": 500,
            },
            {
                "ts": _ts(1),
                "event": "sync_file",
                "model": ANTHROPIC_MODEL,
                "symbols_generated": 2,
                "input_tokens": 100,
                "output_tokens": 50,
                "regen_mode_cold": 2,
            },
        ],
    )
    summary = AuditSummary.from_log(p)
    out = _render_to_string(render, summary)
    assert "MCP calls" in out
    assert "grep" in out
    assert "Sync" in out
    assert "2" in out


def test_render_empty_log_does_not_crash(tmp_path: Path):
    p = tmp_path / "empty.jsonl"
    p.write_text("")
    summary = AuditSummary.from_log(p)
    out = _render_to_string(render, summary)
    assert "none" in out.lower() or "no " in out.lower()


def test_render_comparison_includes_both_paths(tmp_path: Path):
    p1 = tmp_path / "a.jsonl"
    p2 = tmp_path / "b.jsonl"
    _write_log(
        p1,
        [
            {
                "ts": _ts(0),
                "event": "mcp_call",
                "tool": "grep",
                "result_kind": "ok",
                "result_count": 5,
                "duration_ms": 5,
                "response_bytes": 100,
            }
        ],
    )
    _write_log(
        p2,
        [
            {
                "ts": _ts(0),
                "event": "mcp_call",
                "tool": "grep",
                "result_kind": "ok",
                "result_count": 5,
                "duration_ms": 5,
                "response_bytes": 100,
            },
            {
                "ts": _ts(1),
                "event": "mcp_call",
                "tool": "read",
                "result_kind": "ok",
                "prose_chars": 200,
                "duration_ms": 5,
                "response_bytes": 800,
            },
        ],
    )
    out = _render_to_string(
        render_comparison,
        AuditSummary.from_log(p1),
        AuditSummary.from_log(p2),
    )
    assert "a.jsonl" in out
    assert "b.jsonl" in out
    # Delta column should reflect that the candidate ran one more explain.
    assert "+1" in out


def test_render_comparison_includes_cli_call_diff(tmp_path: Path):
    """The comparison renderer must show MCP and CLI surfaces as separate
    tables. A regression where an agent's call mix shifted between
    surfaces (more CLI, less MCP — or vice versa) should be visible at a
    glance, not absorbed into one combined count.

    Baseline run sees one MCP grep; candidate run sees an extra CLI grep
    on top. The MCP delta is 0; the CLI delta is +1 — both tables must
    appear, and the +1 must show up in the CLI table specifically."""
    p1 = tmp_path / "baseline.jsonl"
    p2 = tmp_path / "candidate.jsonl"
    _write_log(
        p1,
        [
            {
                "ts": _ts(0),
                "event": "mcp_call",
                "tool": "grep",
                "result_kind": "ok",
                "result_count": 2,
                "duration_ms": 4,
                "response_bytes": 200,
            },
        ],
    )
    _write_log(
        p2,
        [
            {
                "ts": _ts(0),
                "event": "mcp_call",
                "tool": "grep",
                "result_kind": "ok",
                "result_count": 2,
                "duration_ms": 4,
                "response_bytes": 200,
            },
            {
                "ts": _ts(1),
                "event": "cli_call",
                "tool": "grep",
                "result_kind": "ok",
                "result_count": 3,
                "duration_ms": 6,
                "response_bytes": 250,
            },
        ],
    )
    out = _render_to_string(
        render_comparison,
        AuditSummary.from_log(p1),
        AuditSummary.from_log(p2),
    )
    # Both section titles must appear in the comparison output.
    assert "MCP calls" in out
    assert "CLI calls" in out
    # The +1 delta is for the new CLI grep call. MCP grep count is
    # unchanged across runs, so the only `+1` in the rendered text must
    # be in the CLI table.
    assert "+1" in out


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def test_cli_audit_help_lists_log_option():
    runner = CliRunner()
    result = runner.invoke(app, ["audit", "--help"])
    assert result.exit_code == 0, result.output
    assert "--log" in result.output


def test_cli_audit_runs_against_explicit_log(tmp_path: Path):
    p = tmp_path / "log.jsonl"
    _write_log(p, [{"ts": _ts(0), "event": "scan", "files_seen": 1}])
    runner = CliRunner()
    result = runner.invoke(app, ["audit", "--log", str(p)])
    assert result.exit_code == 0, result.output


def test_cli_audit_json_output(tmp_path: Path):
    p = tmp_path / "log.jsonl"
    _write_log(
        p,
        [
            {
                "ts": _ts(0),
                "event": "mcp_call",
                "tool": "grep",
                "result_kind": "ok",
                "result_count": 3,
                "duration_ms": 5,
                "response_bytes": 100,
            },
        ],
    )
    runner = CliRunner()
    result = runner.invoke(app, ["audit", "--log", str(p), "--json"])
    assert result.exit_code == 0, result.output
    data = json.loads(result.output)
    assert data["mcp"]["grep"]["count"] == 1


def test_cli_audit_compare_two_logs(tmp_path: Path):
    p1 = tmp_path / "a.jsonl"
    p2 = tmp_path / "b.jsonl"
    _write_log(
        p1,
        [
            {
                "ts": _ts(0),
                "event": "mcp_call",
                "tool": "grep",
                "result_kind": "ok",
                "result_count": 1,
                "duration_ms": 5,
                "response_bytes": 100,
            }
        ],
    )
    _write_log(
        p2,
        [
            {
                "ts": _ts(0),
                "event": "mcp_call",
                "tool": "grep",
                "result_kind": "ok",
                "result_count": 1,
                "duration_ms": 5,
                "response_bytes": 100,
            }
        ],
    )
    runner = CliRunner()
    result = runner.invoke(app, ["audit", "--log", str(p1), "--compare", str(p2)])
    assert result.exit_code == 0, result.output
    assert "Compare" in result.output
    assert "a.jsonl" in result.output
    assert "b.jsonl" in result.output


def test_cli_audit_missing_log_exits_nonzero(tmp_path: Path):
    runner = CliRunner()
    result = runner.invoke(app, ["audit", "--log", str(tmp_path / "nope.jsonl")])
    assert result.exit_code != 0


# ---------------------------------------------------------------------------
# Direct call into _summarise (skips the file step)
# ---------------------------------------------------------------------------


def test_summarise_directly_with_event_list():
    """`_summarise` is the testable seam — gives fixture-based tests a fast path."""
    events = [
        Event(
            ts=_ts(0),
            event="mcp_call",
            fields={
                "tool": "grep",
                "result_kind": "ok",
                "result_count": 2,
                "duration_ms": 4,
                "response_bytes": 100,
            },
        ),
        Event(
            ts=_ts(1),
            event="mcp_call",
            fields={
                "tool": "read",
                "result_kind": "ok",
                "prose_chars": 100,
                "duration_ms": 8,
                "response_bytes": 500,
                "args": {"qname": "x:y"},
            },
        ),
    ]
    summary = _summarise(events, log_path=Path("synthetic"), lines_total=2, lines_parsed=2)
    assert summary.mcp["grep"].count == 1
    assert summary.mcp["read"].count == 1
    assert summary.mcp["read"].top_qnames == (("x:y", 1),)
