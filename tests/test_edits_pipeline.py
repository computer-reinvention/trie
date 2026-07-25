from __future__ import annotations

from pathlib import Path

import pytest

from trie.config import Config
from trie.edits.backends import FakeBackend
from trie.edits.pipeline import stage, stage_and_commit
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
    """Returns a deterministic SectionBody for prose generation during sync."""

    full_model_id = "fake/fake"

    def run(self, output_type, system_prompt, user_prompt, *, max_tokens=1024, cache_prefix=None):
        from trie.models import Usage

        return ModelResult(
            output=SectionBody(body="fake prose.", role="util", boundary="internal"),
            usage=Usage(input_tokens=1, output_tokens=1),
        )


@pytest.fixture
def project(tmp_path: Path) -> Path:
    src = tmp_path / "src"
    src.mkdir()
    (src / "__init__.py").write_text("")
    (src / "alpha.py").write_text(
        "from src.beta import beta_fn\n\n\n"
        "def alpha_fn() -> int:\n"
        '    """Top-level entry."""\n'
        "    return beta_fn() + 1\n"
    )
    (src / "beta.py").write_text(
        "from src.gamma import gamma_fn\n\n\n"
        "def beta_fn() -> int:\n"
        '    """Middle layer."""\n'
        "    return gamma_fn() + 10\n"
    )
    (src / "gamma.py").write_text(
        'def gamma_fn() -> int:\n    """Deepest callee."""\n    return 100\n'
    )
    (tmp_path / "trie.toml").write_text(PROJECT_TOML)
    (tmp_path / ".gitignore").write_text(".trie/\n__pycache__/\n")

    config, _ = Config.find_and_load(tmp_path)
    with Store(tmp_path / ".trie" / "graph.db") as store:
        scan_project(project_root=tmp_path, config=config, store=store)
        c = FakeTriefactClient()
        for f in ("alpha.py", "beta.py", "gamma.py"):
            sync_single_file(
                tmp_path / "src" / f, project_root=tmp_path, config=config, client=c, store=store
            )
    return tmp_path


def _config(project: Path) -> Config:
    cfg, _ = Config.find_and_load(project)
    cfg.edits.lsp_backends = []  # no LSP in unit tests
    return cfg


class TestStageNoWrites:
    def test_stage_does_not_touch_source(self, project: Path):
        cfg = _config(project)
        before = (project / "src/gamma.py").read_text()
        with Store(project / ".trie" / "graph.db") as store:
            store.add_patch("src/gamma:gamma_fn", "return 200 instead", "spec", "s1")
            report, staged = stage(store, cfg, FakeBackend("append"), project)
        assert report.ok
        assert len(staged) == 1
        # stage must NOT write the real tree
        assert (project / "src/gamma.py").read_text() == before

    def test_empty_patches_clean_report(self, project: Path):
        cfg = _config(project)
        with Store(project / ".trie" / "graph.db") as store:
            report, staged = stage(store, cfg, FakeBackend(), project)
        assert report.ok
        assert staged == []
        assert report.requested == 0


class TestCommitApplies:
    def test_commit_writes_and_drops_patches(self, project: Path):
        cfg = _config(project)
        with Store(project / ".trie" / "graph.db") as store:
            store.add_patch("src/gamma:gamma_fn", "cosmetic", "nit", "s1")
            report = stage_and_commit(store, cfg, FakeBackend("append"), project)
            remaining = store.get_patches_for_qname("src/gamma:gamma_fn")
        assert report.ok
        assert report.committed
        assert "trie-fake-edit" in (project / "src/gamma.py").read_text()
        assert remaining == []
        d = report.to_dict()
        assert d["totals"]["applied"] == 1
        # gamma_fn has a caller (beta_fn) → surfaced as a NON-blocking second-order
        # cascade advisory; it must not block the commit nor flip ok.
        assert report.blocking_unresolved == []
        assert all(not u.blocking for u in report.unresolved)
        assert any(
            u.code == "second_order_cascade" and u.qname == "src/beta:beta_fn"
            for u in report.unresolved
        )

    def test_passthrough_is_noop_but_commits(self, project: Path):
        cfg = _config(project)
        before = (project / "src/gamma.py").read_text()
        with Store(project / ".trie" / "graph.db") as store:
            store.add_patch("src/gamma:gamma_fn", "no real change", "nit", "s1")
            report = stage_and_commit(store, cfg, FakeBackend("passthrough"), project)
        assert report.ok
        assert (project / "src/gamma.py").read_text() == before


class TestCompileGate:
    def test_broken_generation_goes_to_unresolved(self, project: Path):
        cfg = _config(project)
        before = (project / "src/gamma.py").read_text()
        with Store(project / ".trie" / "graph.db") as store:
            store.add_patch("src/gamma:gamma_fn", "break it", "test", "s1")
            report = stage_and_commit(store, cfg, FakeBackend("broken"), project)
            remaining = store.get_patches_for_qname("src/gamma:gamma_fn")
        assert not report.ok
        assert not report.committed
        blocking = report.blocking_unresolved
        assert len(blocking) >= 1
        u = blocking[0]
        assert u.code == "syntax_error_after_retry_cap"
        assert u.repatch is not None and u.repatch["tool"] == "patch"
        # all_or_nothing: source untouched, patch preserved for retry
        assert (project / "src/gamma.py").read_text() == before
        assert len(remaining) == 1

    def test_backend_failure_goes_to_unresolved(self, project: Path):
        cfg = _config(project)
        with Store(project / ".trie" / "graph.db") as store:
            store.add_patch("src/gamma:gamma_fn", "x", "y", "s1")
            report = stage_and_commit(store, cfg, FakeBackend("fail"), project)
        assert not report.ok
        assert report.blocking_unresolved[0].code == "backend_failed"


class TestAtomicity:
    def test_all_or_nothing_blocks_on_any_failure(self, project: Path):
        cfg = _config(project)
        a_before = (project / "src/alpha.py").read_text()
        with Store(project / ".trie" / "graph.db") as store:
            store.add_patch("src/alpha:alpha_fn", "ok change", "x", "s1")
            store.add_patch("src/gamma:gamma_fn", "break", "y", "s1")
            backend = FakeBackend("append", per_qname={"src/gamma:gamma_fn": "broken"})
            report = stage_and_commit(
                store,
                cfg,
                backend,
                project,
                commit_mode="all_or_nothing",
                session_note="touch alpha and gamma together",
            )
        assert not report.committed
        # alpha (which would have passed) is NOT written under all_or_nothing
        assert (project / "src/alpha.py").read_text() == a_before

    def test_per_item_commits_the_good_one(self, project: Path):
        cfg = _config(project)
        with Store(project / ".trie" / "graph.db") as store:
            store.add_patch("src/alpha:alpha_fn", "ok change", "x", "s1")
            store.add_patch("src/gamma:gamma_fn", "break", "y", "s1")
            backend = FakeBackend("append", per_qname={"src/gamma:gamma_fn": "broken"})
            report = stage_and_commit(
                store,
                cfg,
                backend,
                project,
                commit_mode="per_item",
                session_note="touch alpha and gamma together",
            )
        assert report.committed
        assert "trie-fake-edit" in (project / "src/alpha.py").read_text()
        # gamma failed → in unresolved
        assert any(u.qname == "src/gamma:gamma_fn" for u in report.unresolved)


class TestImportFixup:
    def test_drop_deleted_import(self):
        from trie.edits.pipeline import _fix_imports_for_structural

        src = "from m import a, b, c\n\n\ndef f():\n    return a + c\n"
        out = _fix_imports_for_structural(src, deleted_names={"b"}, renamed={})
        assert "from m import a, c" in out
        assert "b" not in out.split("\n")[0]

    def test_remove_line_when_all_deleted(self):
        from trie.edits.pipeline import _fix_imports_for_structural

        src = "from m import only\n\n\ndef f():\n    pass\n"
        out = _fix_imports_for_structural(src, deleted_names={"only"}, renamed={})
        assert "import only" not in out

    def test_rename_import_preserves_alias(self):
        from trie.edits.pipeline import _fix_imports_for_structural

        src = "from m import old as o, keep\n"
        out = _fix_imports_for_structural(src, deleted_names=set(), renamed={"old": "new"})
        assert "new as o" in out
        assert "keep" in out

    def test_star_and_paren_imports_untouched(self):
        from trie.edits.pipeline import _fix_imports_for_structural

        src = "from m import *\nfrom n import (a, b)\n"
        out = _fix_imports_for_structural(src, deleted_names={"a"}, renamed={})
        assert out == src  # too varied to touch safely

    def test_noop_when_no_targets(self):
        from trie.edits.pipeline import _fix_imports_for_structural

        src = "from m import a\n"
        assert _fix_imports_for_structural(src, deleted_names=set(), renamed={}) == src


def test_record_intent_archives_notes_without_generation(tmp_path):
    """The default apply backend: notes -> session log, queue cleared, no code."""
    import subprocess

    from trie.config import Config
    from trie.edits.pipeline import record_intent
    from trie.graph.store import Store
    from trie.parse.python import extract_symbols
    from trie.session_log import read_entries

    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    (tmp_path / "m.py").write_text("def f():\n    return 1\n\n\ndef g():\n    return 2\n")
    src_before = (tmp_path / "m.py").read_text()

    config = Config.from_dict({})
    store = Store(tmp_path / ".trie" / "graph.db")
    try:
        store.upsert_file(path="m.py", fingerprint="fp")
        store.replace_file_symbols("m.py", extract_symbols(tmp_path / "m.py", tmp_path))
        store.add_patch("m:f", note="f returns one", reason="spec", session_id="s1")
        store.add_create_patch(
            target_file="m.py", target_qname="m:new", note="add new", reason="", session_id="s1"
        )

        # Multi-symbol without a session note: refused.
        refused = record_intent(store, config, tmp_path, session_note="")
        assert refused["ok"] is False and refused["error"] == "session_note_required"

        result = record_intent(store, config, tmp_path, session_note="ship the m module")
        assert result["ok"] is True and result["mode"] == "record"
        assert result["recorded"] == 2
        assert set(result["symbols"]) == {"m:f", "m:new"}

        # Archived to the session log with the session note attached.
        rows = read_entries(tmp_path)
        assert {r["qname"]: r["op"] for r in rows} == {"m:f": "modify", "m:new": "create"}
        assert all(r["session_note"] == "ship the m module" for r in rows)

        # Queue cleared; source untouched (no generation).
        assert store.get_patched_qnames() == []
        assert store.get_create_patches_grouped() == {}
        assert (tmp_path / "m.py").read_text() == src_before

        # Empty queue re-run is a no-op success.
        again = record_intent(store, config, tmp_path, session_note="")
        assert again["ok"] is True and again["recorded"] == 0
    finally:
        store.close()
