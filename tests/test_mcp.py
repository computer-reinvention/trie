"""Tests for the MCP tool functions.

The tools are exercised via TrieTools directly — that's the same code path FastMCP
invokes when a real agent calls a tool, but without the JSON-RPC overhead. Driving the
full stdio transport is integration-test territory and lives in M5 smoke tests.
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


@dataclass
class FakeClient:
    model_id: str = "fake/test"
    body: str = "## generated\n\nbody."

    def generate(self, _req: GenerationRequest) -> GenerationResponse:
        return GenerationResponse(
            text=self.body,
            input_tokens=10,
            output_tokens=20,
            cache_creation_input_tokens=0,
            cache_read_input_tokens=0,
        )


@pytest.fixture
def project(tmp_path: Path) -> Path:
    (tmp_path / "trie.toml").write_text(
        '[trie]\nversion = "0.1.0"\n'
        '[scope]\ninclude = ["**/*.py"]\nexclude = ["**/__pycache__/**"]\n'
        '[docs]\nroot = "docs"\nsource_root = "."\n'
        '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
        'cascade = "anthropic/claude-sonnet-4-6"\n'
        "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
    )
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
        client=FakeClient(body="## lib doc\n\nslugify body."),
    )
    sync_single_file(
        project / "app.py",
        project_root=project,
        config=config,
        client=FakeClient(body="## app doc\n\nmake_url body."),
    )
    return project


@pytest.fixture
def tools(populated_project: Path):
    t = TrieTools(populated_project)
    yield t
    t.close()


# --- get_doc ---


def test_get_doc_returns_markdown_for_source_path(tools: TrieTools):
    doc = tools.get_doc("lib.py")
    assert "lib doc" in doc
    assert "slugify body" in doc


def test_get_doc_accepts_md_path(tools: TrieTools):
    doc = tools.get_doc("lib.md")
    assert "lib doc" in doc


def test_get_doc_returns_notice_when_missing(tools: TrieTools):
    msg = tools.get_doc("nonexistent.py")
    assert "No trie doc" in msg
    assert "trie sync" in msg


# --- find_symbol ---


def test_find_symbol_substring_match(tools: TrieTools):
    hits = tools.find_symbol("slug")
    qnames = {h["qualified_name"] for h in hits}
    assert "lib:slugify" in qnames


def test_find_symbol_returns_metadata(tools: TrieTools):
    hits = tools.find_symbol("make_url")
    assert len(hits) == 1
    h = hits[0]
    assert h["qualified_name"] == "app:make_url"
    assert h["kind"] == "function"
    assert h["file_path"] == "app.py"
    assert h["start_line"] >= 1
    assert "make_url" in (h["signature"] or "")
    assert h["is_public"] is True


def test_find_symbol_empty_query_returns_some(tools: TrieTools):
    # Empty pattern matches everything (LIKE '%%' is universal)
    hits = tools.find_symbol("", limit=10)
    assert len(hits) >= 2  # slugify + make_url at minimum


def test_find_symbol_limit_respected(tools: TrieTools):
    hits = tools.find_symbol("", limit=1)
    assert len(hits) == 1


def test_find_symbol_unknown_returns_empty(tools: TrieTools):
    hits = tools.find_symbol("definitely_not_a_real_symbol_xyz")
    assert hits == []


# --- references_to / references_from ---


def test_references_to_finds_callers(tools: TrieTools):
    refs = tools.references_to("lib:slugify")
    qnames = {r["src_qname"] for r in refs}
    assert "app:make_url" in qnames
    assert refs[0]["confidence"] == "tree_sitter_import"
    assert refs[0]["file_path"] == "app.py"


def test_references_from_finds_callees(tools: TrieTools):
    refs = tools.references_from("app:make_url")
    targets = {r["target_qname"] for r in refs}
    assert "lib:slugify" in targets


def test_references_to_for_unreferenced_symbol(tools: TrieTools):
    """make_url is not called by anyone in this fixture."""
    refs = tools.references_to("app:make_url")
    assert refs == []


def test_references_to_unknown_symbol(tools: TrieTools):
    refs = tools.references_to("nonexistent:foo")
    assert refs == []


# --- server construction ---


def test_build_server_registers_tools(populated_project: Path):
    """Verify build_server returns a working FastMCP with tools registered."""
    from trie.mcp_server import build_server

    server, tools = build_server(populated_project)
    try:
        # FastMCP exposes tools via list_tools() — async, but we can introspect the
        # internal manager to assert registration without running an event loop.
        names = {tool.name for tool in server._tool_manager.list_tools()}
        assert names == {"get_doc", "find_symbol", "references_to", "references_from"}
    finally:
        tools.close()
