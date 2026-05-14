"""Tests for the MCP tool surface: `locate`, `explain`, `walk`.

The tools are exercised via TrieTools directly — that's the same code path FastMCP
invokes when a real agent calls a tool, but without the JSON-RPC overhead. Driving the
full stdio transport is integration-test territory.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pytest

from trie.config import Config
from trie.mcp_server import TrieTools
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
    "[mcp]\nlocate_max_limit = 50\nwalk_max_depth = 5\nwalk_hub_threshold = 20\n"
    "walk_max_nodes = 200\n"
)


@dataclass
class FakeClient:
    """Stand-in for ModelClient. Returns a fixed body and bogus token counts."""

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
def project(tmp_path: Path) -> Path:
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
    return tmp_path


@pytest.fixture
def populated_project(project: Path) -> Path:
    """Project with scan + sync run, so the MCP tools have data to query."""
    config, _ = Config.find_and_load(project)
    from trie.graph.store import Store

    with Store(project / ".trie" / "graph.db") as store:
        scan_project(project_root=project, config=config, store=store)
        sync_single_file(
            project / "lib.py",
            project_root=project,
            config=config,
            client=FakeClient(body="## slugify\n\nLowercase text and dash-separate words.\n"),
            store=store,
        )
        sync_single_file(
            project / "app.py",
            project_root=project,
            config=config,
            client=FakeClient(body="## make_url\n\nBuild a /posts/<slug> URL from a title.\n"),
            store=store,
        )
    return project


@pytest.fixture
def tools(populated_project: Path):
    t = TrieTools(populated_project)
    yield t
    t.close()


# --- locate ---------------------------------------------------------------


def test_locate_name_contains_returns_matches(tools: TrieTools):
    hits = tools.locate({"name_contains": "slug"})
    qnames = {h["qname"] for h in hits}
    assert "lib:slugify" in qnames


def test_locate_returns_one_liner_from_section_body(tools: TrieTools):
    hits = tools.locate({"name_contains": "slugify"})
    assert hits, "expected at least one hit"
    h = hits[0]
    assert "Lowercase" in h["one_liner"]
    # Sentence is truncated to first '.'
    assert h["one_liner"].endswith("words") or h["one_liner"].endswith("words.")


def test_locate_returns_file_pointer(tools: TrieTools):
    hits = tools.locate({"name_contains": "make_url"})
    assert hits[0]["file_pointer"].endswith("app.py:4")


def test_locate_kind_filter(tools: TrieTools):
    # Both fixtures define only functions; class filter should return nothing.
    hits = tools.locate({"name_contains": "slug", "kind": "class"})
    assert hits == []


def test_locate_invalid_kind_returns_error(tools: TrieTools):
    result = tools.locate({"kind": "macro"})
    assert isinstance(result, dict) and "error" in result
    assert result["error"]["code"] == "invalid_argument"


def test_locate_scope_prefix_filter(tools: TrieTools):
    hits = tools.locate({"scope_prefix": "lib"})
    file_paths = {h["file_pointer"].split(":")[0] for h in hits}
    assert all(p.startswith("lib") for p in file_paths)


def test_locate_scope_exclude_filter(tools: TrieTools):
    hits = tools.locate({"scope_exclude": ["app"]})
    file_paths = {h["file_pointer"].split(":")[0] for h in hits}
    assert "app.py" not in file_paths


def test_locate_inbound_count_predicate(tools: TrieTools):
    # slugify has one inbound edge from make_url.
    hits = tools.locate({"inbound_count": {"min": 1}})
    qnames = {h["qname"] for h in hits}
    assert "lib:slugify" in qnames
    assert "app:make_url" not in qnames  # make_url has no callers


def test_locate_rank_by_inbound_count(tools: TrieTools):
    hits = tools.locate({"name_contains": ""}, rank_by="inbound_count", limit=5)
    # First hit should have the highest inbound_count.
    assert hits[0]["inbound_count"] >= hits[-1]["inbound_count"]


def test_locate_limit_respected(tools: TrieTools):
    hits = tools.locate({"name_contains": ""}, limit=1)
    assert len(hits) == 1


def test_locate_unknown_predicate_field_silently_ignored(tools: TrieTools):
    # Extra fields don't break the call — we just ignore them.
    hits = tools.locate({"name_contains": "slug", "totally_made_up_field": True})
    assert hits  # match still works


def test_locate_invalid_predicate_returns_error(tools: TrieTools):
    result = tools.locate("not an object")  # type: ignore[arg-type]
    assert isinstance(result, dict) and "error" in result
    assert result["error"]["code"] == "invalid_argument"


# --- explain --------------------------------------------------------------


def test_explain_returns_prose_and_neighbours(tools: TrieTools):
    out = tools.explain("lib:slugify")
    assert out["qname"] == "lib:slugify"
    assert "Lowercase" in out["prose"]
    # make_url is the caller of slugify
    caller_qnames = {c["qname"] for c in out["callers"]}
    assert "app:make_url" in caller_qnames
    assert out["callees"] == []  # slugify references no other in-scope symbols


def test_explain_source_pointer_shape(tools: TrieTools):
    out = tools.explain("lib:slugify")
    assert out["source_pointer"].startswith("lib.py:")
    assert "-" in out["source_pointer"]  # "start-end"


def test_explain_neighbour_carries_one_liner(tools: TrieTools):
    out = tools.explain("lib:slugify")
    caller = next(c for c in out["callers"] if c["qname"] == "app:make_url")
    assert "Build a /posts" in caller["one_liner"]


def test_explain_unknown_qname_returns_not_found(tools: TrieTools):
    result = tools.explain("nonexistent:missing")
    assert "error" in result
    assert result["error"]["code"] == "not_found"


def test_explain_fuzzy_suggestion_for_typo(tools: TrieTools):
    result = tools.explain("lib:slugfy")  # typo
    assert "error" in result
    suggestion = result["error"].get("suggestion", "")
    # Either suggests the qname directly, or guides to locate(). Both forms include
    # something to act on.
    assert "slugify" in suggestion or "locate(" in suggestion


# --- walk -----------------------------------------------------------------


def test_walk_callers_returns_topology(tools: TrieTools):
    out = tools.walk("lib:slugify", direction="callers", depth=2)
    assert out["root"]["qname"] == "lib:slugify"
    assert "app:make_url" in out["nodes"]
    # Edge from caller to callee, tagged "in" relative to root.
    edges = out["edges"]
    assert any(e["from"] == "app:make_url" and e["to"] == "lib:slugify" for e in edges)


def test_walk_callees_returns_outbound(tools: TrieTools):
    out = tools.walk("app:make_url", direction="callees", depth=1)
    assert "lib:slugify" in out["nodes"]
    assert any(e["from"] == "app:make_url" and e["to"] == "lib:slugify" for e in out["edges"])


def test_walk_both_directions(tools: TrieTools):
    out = tools.walk("lib:slugify", direction="both", depth=1)
    # Should include the caller side.
    assert "app:make_url" in out["nodes"]
    directions = {e["direction"] for e in out["edges"]}
    assert "in" in directions


def test_walk_invalid_direction_returns_error(tools: TrieTools):
    result = tools.walk("lib:slugify", direction="sideways")
    assert "error" in result
    assert result["error"]["code"] == "invalid_argument"


def test_walk_unknown_qname_returns_not_found(tools: TrieTools):
    result = tools.walk("nonexistent:foo", direction="callers")
    assert "error" in result
    assert result["error"]["code"] == "not_found"


def test_walk_depth_zero_returns_only_root(tools: TrieTools):
    out = tools.walk("lib:slugify", direction="callers", depth=0)
    assert list(out["nodes"].keys()) == ["lib:slugify"]
    assert out["edges"] == []


def test_walk_depth_clamp_adds_note(tools: TrieTools):
    # walk_max_depth defaults to 5; ask for more and expect a note.
    out = tools.walk("lib:slugify", direction="callers", depth=99)
    assert "notes" in out
    assert any("clamped" in n for n in out["notes"])


# --- server construction --------------------------------------------------


def test_build_server_registers_three_verbs(populated_project: Path):
    """Verify build_server returns a FastMCP with the new tool names registered."""
    from trie.mcp_server import build_server

    server, t = build_server(populated_project)
    try:
        names = {tool.name for tool in server._tool_manager.list_tools()}
        assert names == {"locate", "explain", "walk"}
    finally:
        t.close()
