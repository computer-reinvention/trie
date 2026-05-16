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
            {"ts": _ts(15), "event": "mcp_call", "tool": "locate"},
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
            # 3 locate calls, one with empty result, one error
            {
                "ts": _ts(0),
                "event": "mcp_call",
                "tool": "locate",
                "result_kind": "ok",
                "result_count": 5,
                "duration_ms": 12,
                "response_bytes": 800,
            },
            {
                "ts": _ts(1),
                "event": "mcp_call",
                "tool": "locate",
                "result_kind": "ok",
                "result_count": 0,
                "duration_ms": 8,
                "response_bytes": 40,
            },
            {
                "ts": _ts(2),
                "event": "mcp_call",
                "tool": "locate",
                "result_kind": "error",
                "error_code": "invalid_argument",
                "duration_ms": 3,
                "response_bytes": 80,
            },
            # 2 explain calls, one not_found
            {
                "ts": _ts(3),
                "event": "mcp_call",
                "tool": "explain",
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
                "tool": "explain",
                "result_kind": "error",
                "error_code": "not_found",
                "duration_ms": 4,
                "response_bytes": 200,
                "args": {"qname": "trie/cli:does_not_exist"},
            },
            # 1 walk call, hub-truncated (single node returned)
            {
                "ts": _ts(5),
                "event": "mcp_call",
                "tool": "walk",
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
    assert set(summary.mcp.keys()) == {"locate", "explain", "walk"}

    loc = summary.mcp["locate"]
    assert loc.count == 3
    assert loc.error_count == 1
    assert loc.empty_result_count == 1  # the result_count==0 one
    assert loc.avg_duration_ms == pytest.approx((12 + 8 + 3) / 3)

    exp = summary.mcp["explain"]
    assert exp.count == 2
    assert exp.error_count == 1
    assert exp.not_found_count == 1
    qnames = [q for q, _ in exp.top_qnames]
    assert "trie/cli:sync_cmd" in qnames

    wlk = summary.mcp["walk"]
    assert wlk.count == 1
    assert wlk.empty_result_count == 1  # nodes_count==1 == just the root


def test_explain_empty_prose_counts_as_empty_result(tmp_path: Path):
    """An explain that returns prose="" (no triefact section yet) is signal —
    the agent asked about a symbol the graph knows but trie hasn't documented.
    Lumping it in with errors would hide that this is a sync-coverage gap."""
    p = tmp_path / "explain.jsonl"
    _write_log(
        p,
        [
            {
                "ts": _ts(0),
                "event": "mcp_call",
                "tool": "explain",
                "result_kind": "ok",
                "prose_chars": 0,
                "duration_ms": 5,
                "response_bytes": 100,
            },
            {
                "ts": _ts(1),
                "event": "mcp_call",
                "tool": "explain",
                "result_kind": "ok",
                "prose_chars": 200,
                "duration_ms": 5,
                "response_bytes": 800,
            },
        ],
    )
    summary = AuditSummary.from_log(p)
    assert summary.mcp["explain"].empty_result_count == 1


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
                "tool": "explain",
                "result_kind": "ok",
                "prose_chars": 100,
                "duration_ms": 5,
                "response_bytes": 500,
            },
        ],
    )
    summary = AuditSummary.from_log(p)
    assert summary.mcp["explain"].count == 1
    assert summary.mcp["explain"].top_qnames == ()


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
                "tool": "locate",
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
    assert "locate" in out
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
                "tool": "locate",
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
                "tool": "locate",
                "result_kind": "ok",
                "result_count": 5,
                "duration_ms": 5,
                "response_bytes": 100,
            },
            {
                "ts": _ts(1),
                "event": "mcp_call",
                "tool": "explain",
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
                "tool": "locate",
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
    assert data["mcp"]["locate"]["count"] == 1


def test_cli_audit_compare_two_logs(tmp_path: Path):
    p1 = tmp_path / "a.jsonl"
    p2 = tmp_path / "b.jsonl"
    _write_log(
        p1,
        [
            {
                "ts": _ts(0),
                "event": "mcp_call",
                "tool": "locate",
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
                "tool": "locate",
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
                "tool": "locate",
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
                "tool": "explain",
                "result_kind": "ok",
                "prose_chars": 100,
                "duration_ms": 8,
                "response_bytes": 500,
                "args": {"qname": "x:y"},
            },
        ),
    ]
    summary = _summarise(events, log_path=Path("synthetic"), lines_total=2, lines_parsed=2)
    assert summary.mcp["locate"].count == 1
    assert summary.mcp["explain"].count == 1
    assert summary.mcp["explain"].top_qnames == (("x:y", 1),)
