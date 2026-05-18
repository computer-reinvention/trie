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
from dataclasses import dataclass
from pathlib import Path

import pytest
from typer.testing import CliRunner

from trie.cli import app
from trie.config import Config
from trie.models import GenerationRequest, GenerationResponse
from trie.scan import scan_project
from trie.sync.single_file import sync_single_file

PROJECT_TOML = (
    '[trie]\nversion = "0.1.0"\n'
    '[scope]\ninclude = ["**/*.py"]\nexclude = ["**/__pycache__/**"]\n'
    '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
    '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
    'cascade = "anthropic/claude-sonnet-4-6"\n'
    "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
)


@dataclass
class FakeClient:
    model_id: str = "fake/test"
    body: str = "## generated\n\nGenerated description.\n"

    def generate(self, _req: GenerationRequest) -> GenerationResponse:
        return GenerationResponse(
            text=self.body,
            input_tokens=10,
            output_tokens=20,
            cache_creation_input_tokens=0,
            cache_read_input_tokens=0,
        )

    def count_tokens(self, _req: GenerationRequest) -> int:
        return 100


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
            client=FakeClient(body="## slugify\n\nLowercase text and dash-separate words.\n"),
            store=store,
        )
        sync_single_file(
            tmp_path / "app.py",
            project_root=tmp_path,
            config=config,
            client=FakeClient(body="## make_url\n\nBuild a /posts/<slug> URL from a title.\n"),
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
