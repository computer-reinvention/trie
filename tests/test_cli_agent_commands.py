"""Tests for the agent-facing CLI subcommands: `trie grep`, `trie read`, `trie trace`.

These commands are the CLI mirror of the MCP tool surface. The contract under test:

  - Each command calls the same `TrieTools` method the MCP server registers, so
    the `--json` output is byte-equivalent to what an agent would see via MCP.
  - The default (no `--json`) output is human-readable Rich-formatted text.
  - Error envelopes from the tool methods produce exit code 1 and a clear
    diagnostic on stderr/stdout; predicate-parse errors exit code 2.
  - Missing `trie.toml` produces a clean error, not a stack trace.

The fixture builds a tiny project mirroring `tests/test_mcp.py` so the two
suites exercise the same data and identical assertions can be made about both
surfaces.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from typer.testing import CliRunner

from tests.fake_client import FakeTrieClient
from trie.cli import app
from trie.config import Config
from trie.scan import scan_project
from trie.sync.single_file import sync_single_file

PROJECT_TOML = (
    '[trie]\nversion = "0.1.2"\n'
    '[scope]\ninclude = ["**/*.py"]\nexclude = ["**/__pycache__/**"]\n'
    '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
    '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
    'cascade = "anthropic/claude-sonnet-4-6"\n'
    'edits = "anthropic/claude-sonnet-4-6"\n'
    "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
)


@pytest.fixture
def populated_project(tmp_path: Path) -> Path:
    """Tiny project with two Python files synced into the graph + triefact tree."""
    (tmp_path / "trie.toml").write_text(PROJECT_TOML)
    (tmp_path / "lib.py").write_text(
        "def slugify(text: str) -> str:\n"
        '    """Lowercase + dash-separate."""\n'
        '    return text.lower().replace(" ", "-")\n'
    )
    (tmp_path / "app.py").write_text(
        "from lib import slugify\n\n\n"
        "def make_url(title: str) -> str:\n"
        '    return "/posts/" + slugify(title)\n'
    )
    config, _ = Config.find_and_load(tmp_path)
    from trie.graph.store import Store

    with Store(tmp_path / ".trie" / "graph.db") as store:
        scan_project(project_root=tmp_path, config=config, store=store)
        sync_single_file(
            tmp_path / "lib.py",
            project_root=tmp_path,
            config=config,
            client=FakeTrieClient(
                output_body="## slugify\n\nLowercase text and dash-separate words.\n"
            ),
            store=store,
        )
        sync_single_file(
            tmp_path / "app.py",
            project_root=tmp_path,
            config=config,
            client=FakeTrieClient(
                output_body="## make_url\n\nBuild a /posts/<slug> URL from a title.\n"
            ),
            store=store,
        )
    return tmp_path


# ---------------------------------------------------------------------------
# trie grep
# ---------------------------------------------------------------------------


def test_grep_with_name_returns_human_readable_table(
    populated_project: Path, monkeypatch: pytest.MonkeyPatch
):
    """Default output (no --json) renders a Rich table with the hit's qname and
    one-liner. The first asserted content is the qname so we know the lookup
    actually found the symbol."""
    monkeypatch.chdir(populated_project)
    runner = CliRunner()
    result = runner.invoke(app, ["grep", "--name", "slugify"])
    assert result.exit_code == 0, result.output
    assert "lib:slugify" in result.output
    # The one-liner pulled from the synced triefact body should appear.
    assert "Lowercase" in result.output


def test_grep_with_json_is_byte_equivalent_to_mcp_envelope(
    populated_project: Path, monkeypatch: pytest.MonkeyPatch
):
    """`--json` dumps the same envelope the MCP `grep` tool would return. This
    is the contract that lets an agent use either surface interchangeably.

    We assert structural shape (hits array, first hit's keys) rather than
    full byte equality with a literal expected JSON, because timestamps and
    other metadata could otherwise make the test brittle.
    """
    monkeypatch.chdir(populated_project)
    runner = CliRunner()
    result = runner.invoke(app, ["grep", "--name", "slugify", "--json"])
    assert result.exit_code == 0, result.output
    parsed = json.loads(result.output)
    assert "hits" in parsed
    assert any(h["qname"] == "lib:slugify" for h in parsed["hits"])
    # Every hit carries the standard MCP envelope fields.
    first = parsed["hits"][0]
    for required_field in (
        "qname",
        "signature",
        "file_pointer",
        "one_liner",
        "is_public",
        "kind",
        "inbound_count",
        "outbound_count",
    ):
        assert required_field in first


def test_grep_predicate_json_overrides_via_flags(
    populated_project: Path, monkeypatch: pytest.MonkeyPatch
):
    """`--predicate` accepts a JSON blob (matching the MCP shape); individual
    flags layer on top. This is the path an agent would use when it has a
    pre-built predicate but wants to add one more filter on the command
    line."""
    monkeypatch.chdir(populated_project)
    runner = CliRunner()
    result = runner.invoke(
        app,
        [
            "grep",
            "--predicate",
            '{"name_contains": "make_url"}',
            "--scope-prefix",
            "app",
            "--json",
        ],
    )
    assert result.exit_code == 0, result.output
    parsed = json.loads(result.output)
    qnames = [h["qname"] for h in parsed["hits"]]
    assert "app:make_url" in qnames


def test_grep_invalid_predicate_json_exits_2(
    populated_project: Path, monkeypatch: pytest.MonkeyPatch
):
    """Malformed JSON in `--predicate` is a usage error (exit 2), distinct
    from a tool-side error (exit 1). Lets shell scripts tell the two
    apart."""
    monkeypatch.chdir(populated_project)
    runner = CliRunner()
    result = runner.invoke(app, ["grep", "--predicate", "not json at all"])
    assert result.exit_code == 2
    assert "not valid JSON" in result.output


def test_grep_no_matches_shows_fallback_envelope(
    populated_project: Path, monkeypatch: pytest.MonkeyPatch
):
    """When `--name` matches no symbol, the response carries a fallback
    envelope describing what the text-search did instead. The human
    renderer should surface the fallback's kind and any note so the
    operator understands why hits was empty."""
    monkeypatch.chdir(populated_project)
    runner = CliRunner()
    result = runner.invoke(app, ["grep", "--name", "xyzzy_no_such_thing"])
    # Exit code 0 — empty hits isn't an error, it's a valid response.
    assert result.exit_code == 0, result.output
    assert "text_match_empty" in result.output


def test_grep_with_no_flags_exits_with_invalid_argument(
    populated_project: Path, monkeypatch: pytest.MonkeyPatch
):
    """`trie grep` with no filter flags must error out instead of silently
    returning the alphabetically-first N public symbols. The CLI builds an
    empty predicate when no flags are passed; `TrieTools.grep` rejects it.
    The agent (or human) sees an `invalid_argument` envelope with a
    suggestion naming usable filters.

    This is the contract that prevents the 'noisy empty grep' footgun on
    the CLI surface, matching the same enforcement on the MCP wire.
    """
    monkeypatch.chdir(populated_project)
    runner = CliRunner()
    result = runner.invoke(app, ["grep"])
    # Exit code 1 = tool returned an error envelope. (2 is for CLI-level
    # usage errors like malformed --predicate JSON, not for tool errors.)
    assert result.exit_code == 1
    assert "invalid_argument" in result.output
    # The suggestion should name at least one usable filter so the next
    # invocation is obvious.
    assert "name_contains" in result.output or "scope_prefix" in result.output


def test_grep_text_match_fallback_renders_candidates(
    populated_project: Path, monkeypatch: pytest.MonkeyPatch
):
    """When the query string is in a symbol's body but not its name, the
    fallback returns candidate enclosing symbols. The human renderer
    surfaces the candidate table so the user sees the redirected hits."""
    monkeypatch.chdir(populated_project)
    runner = CliRunner()
    # "replace" appears in lib:slugify's body but isn't a symbol name.
    result = runner.invoke(app, ["grep", "--name", "replace"])
    assert result.exit_code == 0, result.output
    assert "text_match" in result.output
    assert "lib:slugify" in result.output


# ---------------------------------------------------------------------------
# trie read
# ---------------------------------------------------------------------------


def test_read_known_qname_prints_prose_and_neighbours(
    populated_project: Path, monkeypatch: pytest.MonkeyPatch
):
    """`trie read <qname>` is the equivalent of the MCP `read` call: prose
    body plus the one-line summaries of every caller and callee. The output
    must include the qname, the prose body, and the caller (app:make_url)."""
    monkeypatch.chdir(populated_project)
    runner = CliRunner()
    result = runner.invoke(app, ["read", "lib:slugify"])
    assert result.exit_code == 0, result.output
    assert "lib:slugify" in result.output
    assert "Lowercase" in result.output  # prose body
    assert "app:make_url" in result.output  # caller


def test_read_unknown_qname_exits_1_with_suggestion(
    populated_project: Path, monkeypatch: pytest.MonkeyPatch
):
    """A not_found error from the tool method exits 1 (script-detectable)
    and prints the suggestion the MCP envelope carries so the user has a
    next step."""
    monkeypatch.chdir(populated_project)
    runner = CliRunner()
    result = runner.invoke(app, ["read", "lib:slugfy"])  # typo
    assert result.exit_code == 1
    assert "not_found" in result.output
    # The suggestion either names the close match or points at grep().
    assert "slugify" in result.output or "grep(" in result.output


def test_read_json_emits_envelope(populated_project: Path, monkeypatch: pytest.MonkeyPatch):
    """`--json` produces the full MCP `read` envelope so an agent calling
    the CLI gets the same structured response as a wire call."""
    monkeypatch.chdir(populated_project)
    runner = CliRunner()
    result = runner.invoke(app, ["read", "lib:slugify", "--json"])
    assert result.exit_code == 0, result.output
    parsed = json.loads(result.output)
    assert parsed["qname"] == "lib:slugify"
    assert "prose" in parsed
    assert "callers" in parsed and "callees" in parsed
    caller_qnames = {c["qname"] for c in parsed["callers"]}
    assert "app:make_url" in caller_qnames


# ---------------------------------------------------------------------------
# trie trace
# ---------------------------------------------------------------------------


def test_trace_callers_renders_topology(populated_project: Path, monkeypatch: pytest.MonkeyPatch):
    """Default output names the root, lists nodes, and prints the directed
    edges. The arrow direction (← vs →) tells the operator at a glance
    which way the edge points relative to the root."""
    monkeypatch.chdir(populated_project)
    runner = CliRunner()
    result = runner.invoke(
        app,
        ["trace", "lib:slugify", "--direction", "callers", "--depth", "2"],
    )
    assert result.exit_code == 0, result.output
    assert "lib:slugify" in result.output
    assert "app:make_url" in result.output


def test_trace_json_shape_matches_mcp(populated_project: Path, monkeypatch: pytest.MonkeyPatch):
    """The `--json` envelope must have the same root/nodes/edges shape as
    the MCP `trace` tool. This is what makes the CLI a drop-in alternative
    for an agent that prefers shelling out."""
    monkeypatch.chdir(populated_project)
    runner = CliRunner()
    result = runner.invoke(
        app,
        [
            "trace",
            "app:make_url",
            "--direction",
            "callees",
            "--depth",
            "1",
            "--json",
        ],
    )
    assert result.exit_code == 0, result.output
    parsed = json.loads(result.output)
    assert parsed["root"]["qname"] == "app:make_url"
    assert "lib:slugify" in parsed["nodes"]
    assert any(e["from"] == "app:make_url" and e["to"] == "lib:slugify" for e in parsed["edges"])


def test_trace_unknown_qname_exits_1(populated_project: Path, monkeypatch: pytest.MonkeyPatch):
    """Same not_found contract as `trie read` — unknown qnames exit 1 with
    a structured error so scripts can branch on it."""
    monkeypatch.chdir(populated_project)
    runner = CliRunner()
    result = runner.invoke(app, ["trace", "nonexistent:foo"])
    assert result.exit_code == 1
    assert "not_found" in result.output


def test_trace_invalid_direction_exits_1(populated_project: Path, monkeypatch: pytest.MonkeyPatch):
    """Passing an unsupported `--direction` produces an invalid_argument
    envelope (exit 1), not a Typer-level usage error. The tool method
    validates the direction string, and the CLI surface honours that
    answer rather than second-guessing."""
    monkeypatch.chdir(populated_project)
    runner = CliRunner()
    result = runner.invoke(app, ["trace", "lib:slugify", "--direction", "sideways"])
    assert result.exit_code == 1
    assert "invalid_argument" in result.output


# ---------------------------------------------------------------------------
# No trie.toml in the working directory
# ---------------------------------------------------------------------------


def test_grep_without_trie_toml_exits_1_with_clean_error(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    """Running an agent command in a directory without trie.toml prints a
    clear error and exits 1 — no stack trace. Same fail-mode as the other
    commands that depend on a configured project."""
    monkeypatch.chdir(tmp_path)
    runner = CliRunner()
    result = runner.invoke(app, ["grep", "--name", "anything"])
    assert result.exit_code == 1
    assert "trie.toml" in result.output


def test_read_without_trie_toml_exits_1(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    """Symmetric with `trie grep`: no config means a clean failure."""
    monkeypatch.chdir(tmp_path)
    runner = CliRunner()
    result = runner.invoke(app, ["read", "some:qname"])
    assert result.exit_code == 1
    assert "trie.toml" in result.output


def test_trace_without_trie_toml_exits_1(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    """Same fail-mode for `trie trace`."""
    monkeypatch.chdir(tmp_path)
    runner = CliRunner()
    result = runner.invoke(app, ["trace", "some:qname"])
    assert result.exit_code == 1
    assert "trie.toml" in result.output


# ---------------------------------------------------------------------------
# Telemetry: CLI calls emit `cli_call` events (not `mcp_call`)
# ---------------------------------------------------------------------------


def _read_jsonl_events(path: Path) -> list[dict]:
    """Read a JSONL file and return one parsed dict per non-empty line."""
    out: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            out.append(json.loads(line))
    return out


def test_grep_emits_cli_call_event_not_mcp_call(
    populated_project: Path, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
):
    """A successful `trie grep` invocation must emit a `cli_call` event (not
    a `mcp_call` event). This is the contract that lets `trie audit`
    distinguish CLI usage from MCP-server usage — without it, audit
    aggregates the CLI calls into the MCP bucket and operators can't tell
    which surface the agent is actually using.

    Verified by setting `TRIE_DEBUG=<tmp>/log.jsonl` so telemetry lands in
    a tmp file we can read back, then asserting on the event names that
    actually fired."""
    log_path = tmp_path / "telem.jsonl"
    monkeypatch.setenv("TRIE_DEBUG", str(log_path))
    monkeypatch.chdir(populated_project)

    runner = CliRunner()
    result = runner.invoke(app, ["grep", "--name", "slugify"])
    assert result.exit_code == 0, result.output

    assert log_path.exists()
    events = _read_jsonl_events(log_path)
    event_names = {e["event"] for e in events}
    assert "cli_call" in event_names
    # The MCP-only event names must NOT fire for a CLI invocation.
    assert "mcp_call" not in event_names
    assert "mcp_server_start" not in event_names


def test_read_and_trace_also_emit_cli_call_events(
    populated_project: Path, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
):
    """Symmetric coverage for `trie read` and `trie trace`. Both reach the
    same `TrieTools` methods as `grep`, and both should emit `cli_call`
    events when invoked via the CLI."""
    log_path = tmp_path / "telem.jsonl"
    monkeypatch.setenv("TRIE_DEBUG", str(log_path))
    monkeypatch.chdir(populated_project)

    runner = CliRunner()
    read_result = runner.invoke(app, ["read", "lib:slugify"])
    assert read_result.exit_code == 0, read_result.output
    trace_result = runner.invoke(
        app, ["trace", "lib:slugify", "--direction", "callers", "--depth", "1"]
    )
    assert trace_result.exit_code == 0, trace_result.output

    events = _read_jsonl_events(log_path)
    cli_call_tools = {e["tool"] for e in events if e["event"] == "cli_call"}
    # Both tools represented; no mcp_call events.
    assert "read" in cli_call_tools
    assert "trace" in cli_call_tools
    mcp_call_events = [e for e in events if e["event"] == "mcp_call"]
    assert mcp_call_events == []


def test_cli_call_event_carries_duration_and_result_fields(
    populated_project: Path, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
):
    """`cli_call` events carry the same operational fields the MCP path
    emits: `duration_ms` (from `telemetry.timed`), `result_kind`,
    `result_count` for grep, `response_bytes`. Without these the audit
    summary can't compute avg duration / error rate per CLI tool."""
    log_path = tmp_path / "telem.jsonl"
    monkeypatch.setenv("TRIE_DEBUG", str(log_path))
    monkeypatch.chdir(populated_project)

    runner = CliRunner()
    result = runner.invoke(app, ["grep", "--name", "slugify"])
    assert result.exit_code == 0, result.output

    events = _read_jsonl_events(log_path)
    cli_calls = [e for e in events if e["event"] == "cli_call"]
    assert len(cli_calls) == 1
    ev = cli_calls[0]
    assert ev["tool"] == "grep"
    assert "duration_ms" in ev
    assert ev["result_kind"] == "ok"
    assert "result_count" in ev
    assert "response_bytes" in ev


# ── trie patch CLI tests ──────────────────────────────────────────────


def test_patch_list_empty(populated_project: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(populated_project)
    runner = CliRunner()
    result = runner.invoke(app, ["patch", "list"])
    assert result.exit_code == 0
    assert "no pending patches" in result.output


def test_patch_create_and_list(populated_project: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(populated_project)
    runner = CliRunner()

    result = runner.invoke(
        app, ["patch", "create", "lib:slugify", "--note", "add unicode support", "--reason", "i18n"]
    )
    assert result.exit_code == 0
    assert "patch #" in result.output
    assert "posted" in result.output

    list_result = runner.invoke(app, ["patch", "list"])
    assert list_result.exit_code == 0
    assert "lib:slugify" in list_result.output


def test_patch_create_unknown_symbol(populated_project: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(populated_project)
    runner = CliRunner()
    result = runner.invoke(app, ["patch", "create", "nosuch:foo", "--note", "x", "--reason", "y"])
    assert result.exit_code == 1
    assert "not found" in result.output


def test_patch_preview(populated_project: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(populated_project)
    runner = CliRunner()

    runner.invoke(
        app, ["patch", "create", "lib:slugify", "--note", "add unicode", "--reason", "i18n"]
    )
    result = runner.invoke(app, ["patch", "preview"])
    assert result.exit_code == 0
    assert "lib:slugify" in result.output


def test_patch_preview_empty(populated_project: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(populated_project)
    runner = CliRunner()
    result = runner.invoke(app, ["patch", "preview"])
    assert result.exit_code == 0
    assert "no pending patches" in result.output


def test_patch_drop_by_qname(populated_project: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(populated_project)
    runner = CliRunner()

    runner.invoke(app, ["patch", "create", "lib:slugify", "--note", "x", "--reason", "y"])
    list1 = runner.invoke(app, ["patch", "list"])
    assert "lib:slugify" in list1.output

    drop = runner.invoke(app, ["patch", "drop", "--qname", "lib:slugify"])
    assert drop.exit_code == 0

    list2 = runner.invoke(app, ["patch", "list"])
    assert "no pending patches" in list2.output


def test_patch_drop_all(populated_project: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(populated_project)
    runner = CliRunner()

    runner.invoke(app, ["patch", "create", "lib:slugify", "--note", "x", "--reason", "y"])
    drop = runner.invoke(app, ["patch", "drop", "--all"])
    assert drop.exit_code == 0

    list2 = runner.invoke(app, ["patch", "list"])
    assert "no pending patches" in list2.output


def test_patch_drop_no_args(populated_project: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(populated_project)
    runner = CliRunner()
    result = runner.invoke(app, ["patch", "drop"])
    assert result.exit_code == 1
    assert "specify" in result.output


def test_patch_help(populated_project: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(populated_project)
    runner = CliRunner()
    result = runner.invoke(app, ["patch", "--help"])
    assert result.exit_code == 0
    assert "create" in result.output
    assert "apply" in result.output
    assert "preview" in result.output
    assert "list" in result.output
    assert "drop" in result.output
