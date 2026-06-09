from __future__ import annotations

from pathlib import Path

import pytest

from trie import activity
from trie.config import Config
from trie.edits.backends import FakeBackend
from trie.edits.pipeline import stage_and_commit
from trie.edits.report import session_note_ok
from trie.graph.store import Store
from trie.models import ModelResult, SectionBody
from trie.scan import scan_project
from trie.sync.single_file import sync_single_file

PROJECT_TOML = (
    '[trie]\nversion = "0.1.2"\n'
    '[scope]\ninclude = ["src/**/*.py"]\nexclude = ["**/__pycache__/**"]\n'
    '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
    '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
    'cascade = "anthropic/claude-sonnet-4-6"\n'
    'edits = "anthropic/claude-sonnet-4-6"\n'
    "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
)


class FakeTriefactClient:
    full_model_id = "fake/fake"

    def run(self, output_type, system_prompt, user_prompt, *, max_tokens=1024, cache_prefix=None):
        from pydantic_ai.usage import Usage

        return ModelResult(
            output=SectionBody(body="fake prose.", role="util", boundary="internal"),
            usage=Usage(input_tokens=1, output_tokens=1),
        )


@pytest.fixture
def project(tmp_path: Path) -> Path:
    src = tmp_path / "src"
    src.mkdir()
    (src / "__init__.py").write_text("")
    (src / "m.py").write_text("def a() -> int:\n    return 1\n\n\ndef b() -> int:\n    return 2\n")
    (tmp_path / "trie.toml").write_text(PROJECT_TOML)
    (tmp_path / ".gitignore").write_text(".trie/\n")
    config, _ = Config.find_and_load(tmp_path)
    with Store(tmp_path / ".trie" / "graph.db") as store:
        scan_project(project_root=tmp_path, config=config, store=store)
        sync_single_file(
            tmp_path / "src/m.py",
            project_root=tmp_path,
            config=config,
            client=FakeTriefactClient(),
            store=store,
        )
    return tmp_path


def _config(project: Path) -> Config:
    cfg, _ = Config.find_and_load(project)
    cfg.edits.lsp_backends = []
    return cfg


class TestSessionNoteValidator:
    def test_rejects_short_and_boilerplate(self):
        assert not session_note_ok("")
        assert not session_note_ok("   ")
        assert not session_note_ok("fix")
        assert not session_note_ok("update")
        assert not session_note_ok(".")
        assert not session_note_ok("too short")  # < 12 chars

    def test_accepts_real_note(self):
        assert session_note_ok("bump return values across module m")


class TestGate:
    def test_single_symbol_needs_no_note(self, project: Path):
        cfg = _config(project)
        with Store(project / ".trie" / "graph.db") as store:
            store.add_patch("src/m:a", "change", "r", "s1")
            report = stage_and_commit(store, cfg, FakeBackend("append"), project)
        assert report.ok and report.committed

    def test_multi_symbol_requires_note(self, project: Path):
        cfg = _config(project)
        with Store(project / ".trie" / "graph.db") as store:
            store.add_patch("src/m:a", "change", "r", "s1")
            store.add_patch("src/m:b", "change", "r", "s1")
            report = stage_and_commit(store, cfg, FakeBackend("append"), project)
        assert not report.ok
        assert not report.committed
        assert report.error == "session_note_required"
        u = report.unresolved[0]
        assert u.code == "session_note_required"
        # repatch carries a truthful synthesized draft
        assert u.repatch is not None
        assert u.repatch["tool"] == "commit"
        assert len(u.repatch["args"]["session_note"]) >= 1

    def test_multi_symbol_with_note_commits(self, project: Path):
        cfg = _config(project)
        with Store(project / ".trie" / "graph.db") as store:
            store.add_patch("src/m:a", "change", "r", "s1")
            store.add_patch("src/m:b", "change", "r", "s1")
            report = stage_and_commit(
                store,
                cfg,
                FakeBackend("append"),
                project,
                session_note="bump both return values to new spec",
            )
        assert report.ok and report.committed


class TestMetaHelpers:
    def test_set_get_clear_meta(self, tmp_path: Path):
        # touch the activity db via set
        activity.set_meta(tmp_path, "cli_session_id", "abc123")
        assert activity.get_meta(tmp_path, "cli_session_id") == "abc123"
        activity.clear_meta(tmp_path, "cli_session_id")
        assert activity.get_meta(tmp_path, "cli_session_id") is None

    def test_get_meta_missing_db_returns_none(self, tmp_path: Path):
        assert activity.get_meta(tmp_path / "nonexistent", "k") is None
