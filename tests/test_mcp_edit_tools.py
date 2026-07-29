"""Tests for the MCP edit tool surface: patch/create/delete/rename/preview/list.

Driven via TrieTools directly (same path FastMCP invokes). commit() builds a real
LLM client so it's not exercised here; the staging tools and report wiring are.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from tests.fake_client import FakeTrieClient
from trie.config import Config
from trie.graph.store import Store
from trie.mcp_server import TrieTools
from trie.scan import scan_project
from trie.sync.single_file import sync_single_file

PROJECT_TOML = (
    '[trie]\nversion = "0.1.2"\n'
    '[scope]\ninclude = ["**/*.py"]\nexclude = ["**/__pycache__/**"]\n'
    '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
    '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
    'cascade = "anthropic/claude-sonnet-4-6"\n'
    "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
)


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
    config, _ = Config.find_and_load(tmp_path)
    with Store(tmp_path / ".trie" / "graph.db") as store:
        scan_project(project_root=tmp_path, config=config, store=store)
        for f in ("lib.py", "app.py"):
            sync_single_file(
                tmp_path / f,
                project_root=tmp_path,
                config=config,
                client=FakeTrieClient(output_body="## x\n\nprose.\n"),
                store=store,
            )
    return tmp_path


@pytest.fixture
def tools(project: Path):
    t = TrieTools(project)
    yield t
    t.close()


class TestPatchTool:
    def test_patch_with_note_returns_blast_radius(self, tools):
        r = tools.patch("lib:slugify", note="trim whitespace")
        assert "patch_id" in r
        assert r["mode"] == "note"
        assert "blast_radius" in r
        # slugify is called by make_url → appears in cascade
        assert "app:make_url" in r["blast_radius"]["cascade"]

    def test_patch_with_source_mode(self, tools):
        r = tools.patch("lib:slugify", source="def slugify(text):\n    return text\n")
        assert r["mode"] == "source"

    def test_patch_requires_exactly_one_of_note_source(self, tools):
        both = tools.patch("lib:slugify", note="x", source="y")
        assert both["error"]["code"] == "invalid_argument"
        neither = tools.patch("lib:slugify")
        assert neither["error"]["code"] == "invalid_argument"

    def test_patch_unknown_qname_has_fix(self, tools):
        r = tools.patch("lib:nope", note="x")
        assert r["error"]["code"] == "not_found"
        assert r["error"]["fix"]["tool"] == "patch"


class TestCreateTool:
    def test_create_stages_create_patch(self, tools):
        r = tools.create_symbol("lib:helper", note="a helper")
        assert "create_patch_id" in r
        assert r["target_file"] == "lib.py"
        listed = tools.patch_list()
        assert any(c["target_qname"] == "lib:helper" for c in listed["creates"])

    def test_create_existing_symbol_falls_back_to_patch(self, tools):
        # Creating a symbol that already exists is not an error: the note is
        # recorded as a patch and the result flags the graceful fallback.
        r = tools.create_symbol("lib:slugify", note="dup")
        assert "error" not in r
        assert r["op"] == "patch"
        assert r["fell_back"] is True
        assert "patch_id" in r
        listed = tools.patch_list()
        assert any(p["qname"] == "lib:slugify" for p in listed["patches"])


class TestDeleteTool:
    def test_delete_lists_dependents(self, tools):
        r = tools.delete_symbol("lib:slugify")
        assert "patch_id" in r
        assert any(d["qname"] == "app:make_url" for d in r["dependents"])

    def test_delete_unknown_errors(self, tools):
        r = tools.delete_symbol("lib:nope")
        assert r["error"]["code"] == "not_found"


class TestRenameTool:
    def test_rename_returns_references(self, tools):
        r = tools.rename_symbol("lib:slugify", "sluggify")
        assert r["new_name"] == "sluggify"
        assert "app:make_url" in r["references"]

    def test_rename_invalid_identifier(self, tools):
        r = tools.rename_symbol("lib:slugify", "1bad")
        assert r["error"]["code"] == "invalid_argument"


class TestPreviewAndList:
    def test_preview_reports_pending_and_cascade(self, tools):
        tools.patch("lib:slugify", note="change")
        pv = tools.preview()
        assert "lib:slugify" in pv["pending"]
        assert pv["ready_to_commit"] is True

    def test_preview_flags_multi_symbol_note_need(self, tools):
        tools.patch("lib:slugify", note="a")
        tools.patch("app:make_url", note="b")
        pv = tools.preview()
        assert pv["needs_session_note"] is True

    def test_patch_list_includes_kind(self, tools):
        tools.rename_symbol("lib:slugify", "sluggify")
        listed = tools.patch_list()
        entry = next(p for p in listed["patches"] if p["qname"] == "lib:slugify")
        assert entry["kind"] == "rename"


class TestActivityAndSummary:
    def test_activity_includes_patches_block(self, tools):
        tools.patch("lib:slugify", note="change")
        act = tools.activity()
        assert act["patches"]["total_patches"] == 1
        assert act["patches"]["symbol_count"] == 1
        assert act["apply"] is None

    def test_patch_summary_counts_creates(self, tools):
        tools.create_symbol("lib:helper", note="h")
        summary = tools.store.patch_summary()
        assert summary["create_count"] == 1


class TestSessionIdInjection:
    def test_env_session_id_used(self, project, monkeypatch):
        monkeypatch.setenv("TRIE_SESSION_ID", "injected123")
        t = TrieTools(project)
        try:
            assert t._session_id == "injected123"
        finally:
            t.close()
