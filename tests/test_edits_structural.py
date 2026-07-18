from __future__ import annotations

from pathlib import Path

import pytest

from trie.config import Config
from trie.edits.backends import FakeBackend
from trie.edits.backends.fake import _MARKER
from trie.edits.pipeline import stage_and_commit
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
    (src / "gamma.py").write_text(
        'def gamma_fn() -> int:\n    """Deepest callee."""\n    return 100\n'
    )
    (tmp_path / "trie.toml").write_text(PROJECT_TOML)
    (tmp_path / ".gitignore").write_text(".trie/\n__pycache__/\n")

    config, _ = Config.find_and_load(tmp_path)
    with Store(tmp_path / ".trie" / "graph.db") as store:
        scan_project(project_root=tmp_path, config=config, store=store)
        sync_single_file(
            tmp_path / "src/gamma.py",
            project_root=tmp_path,
            config=config,
            client=FakeTriefactClient(),
            store=store,
        )
    return tmp_path


@pytest.fixture
def class_project(tmp_path: Path) -> Path:
    """A project with a class (for method-create tests)."""
    src = tmp_path / "src"
    src.mkdir()
    (src / "__init__.py").write_text("")
    (src / "box.py").write_text(
        "class Box:\n"
        '    """A box."""\n'
        "\n"
        "    def __init__(self, w: int, h: int) -> None:\n"
        "        self.w = w\n"
        "        self.h = h\n"
        "\n"
        "    def area(self) -> int:\n"
        '        """Area."""\n'
        "        return self.w * self.h\n"
    )
    (tmp_path / "trie.toml").write_text(PROJECT_TOML)
    (tmp_path / ".gitignore").write_text(".trie/\n__pycache__/\n")
    config, _ = Config.find_and_load(tmp_path)
    with Store(tmp_path / ".trie" / "graph.db") as store:
        scan_project(project_root=tmp_path, config=config, store=store)
        sync_single_file(
            tmp_path / "src/box.py",
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


class TestDelete:
    def test_delete_removes_symbol_source(self, project: Path):
        cfg = _config(project)
        with Store(project / ".trie" / "graph.db") as store:
            store.add_delete_patch("src/gamma:gamma_fn", "obsolete", "s1")
            report = stage_and_commit(store, cfg, FakeBackend(), project)
            detail_after = store.get_symbol_detail("src/gamma:gamma_fn")
        assert report.ok
        assert report.committed
        text = (project / "src/gamma.py").read_text()
        assert "gamma_fn" not in text
        # absorbed by re-scan: symbol gone from the graph
        assert detail_after is None
        assert any(a.op == "delete" for a in report.applied)


class TestRename:
    def test_rename_updates_definition(self, project: Path):
        cfg = _config(project)
        with Store(project / ".trie" / "graph.db") as store:
            store.add_rename_patch("src/gamma:gamma_fn", "deepest", "clarity", "s1")
            report = stage_and_commit(store, cfg, FakeBackend(), project)
            renamed = store.get_symbol_detail("src/gamma:deepest")
            old = store.get_symbol_detail("src/gamma:gamma_fn")
        assert report.ok
        text = (project / "src/gamma.py").read_text()
        assert "def deepest()" in text
        assert "def gamma_fn()" not in text
        assert renamed is not None
        assert old is None

    def test_rename_invalid_identifier_refused(self, project: Path):
        cfg = _config(project)
        before = (project / "src/gamma.py").read_text()
        with Store(project / ".trie" / "graph.db") as store:
            store.add_rename_patch("src/gamma:gamma_fn", "1bad", "x", "s1")
            report = stage_and_commit(store, cfg, FakeBackend(), project)
        assert not report.ok
        assert report.blocking_unresolved
        u = report.blocking_unresolved[0]
        assert u.repatch is not None and u.repatch["tool"] == "rename_symbol"
        # refused → source untouched
        assert (project / "src/gamma.py").read_text() == before


class TestCreate:
    def test_create_adds_new_symbol(self, project: Path):
        cfg = _config(project)
        with Store(project / ".trie" / "graph.db") as store:
            store.add_create_patch(
                target_file="src/gamma.py",
                target_qname="src/gamma:helper",
                note="a helper that returns 7",
                reason="needed by gamma",
                session_id="s1",
            )
            report = stage_and_commit(store, cfg, FakeBackend("passthrough"), project)
            created = store.get_symbol_detail("src/gamma:helper")
            remaining = store.get_create_patches_grouped()
        assert report.ok
        assert report.committed
        text = (project / "src/gamma.py").read_text()
        assert "def helper()" in text
        assert created is not None  # absorbed by re-scan
        assert remaining == {}  # create patch dropped
        assert any(a.op == "create" for a in report.applied)

    def test_create_unreferenced_surfaces_orphan_advisory(self, project: Path):
        cfg = _config(project)
        with Store(project / ".trie" / "graph.db") as store:
            store.add_create_patch(
                target_file="src/gamma.py",
                target_qname="src/gamma:helper",
                note="a helper",
                reason="r",
                session_id="s1",
            )
            report = stage_and_commit(store, cfg, FakeBackend("passthrough"), project)
        assert report.committed
        # nothing calls the new helper → advisory (non-blocking) orphan_create item
        orphan = [u for u in report.unresolved if u.code == "orphan_create"]
        assert orphan and orphan[0].qname == "src/gamma:helper"
        assert not orphan[0].blocking

    def test_create_in_missing_file_creates_new_file(self, project: Path):
        # True new-file creation: a create patch targeting a not-yet-existing
        # file scaffolds that file (Fix 3b), rather than failing file_not_found.
        cfg = _config(project)
        with Store(project / ".trie" / "graph.db") as store:
            store.add_create_patch(
                target_file="src/nope.py",
                target_qname="src/nope:thing",
                note="x",
                reason="y",
                session_id="s1",
            )
            report = stage_and_commit(store, cfg, FakeBackend("passthrough"), project)
        # The new file exists on disk with the generated symbol.
        new_file = project / "src" / "nope.py"
        assert new_file.is_file()
        assert "def thing" in new_file.read_text()
        # No blocking file_not_found; the create applied (orphan-create advisory
        # is acceptable since nothing references the new symbol yet).
        assert not any(u.code == "file_not_found" and u.blocking for u in report.unresolved)

    def test_create_in_missing_nested_dir_creates_dirs(self, project: Path):
        # New file in a not-yet-existing subdirectory: parents are created.
        cfg = _config(project)
        with Store(project / ".trie" / "graph.db") as store:
            store.add_create_patch(
                target_file="src/new_pkg/mod.py",
                target_qname="src/new_pkg/mod:helper",
                note="x",
                reason="y",
                session_id="s1",
            )
            stage_and_commit(store, cfg, FakeBackend("passthrough"), project)
        created = project / "src" / "new_pkg" / "mod.py"
        assert created.is_file()
        assert "def helper" in created.read_text()

    def test_create_method_into_class(self, class_project: Path):
        # A create whose qname is `Module:Class.method` lands INSIDE the class.
        cfg = _config(class_project)
        with Store(class_project / ".trie" / "graph.db") as store:
            store.add_create_patch(
                target_file="src/box.py",
                target_qname="src/box:Box.volume",
                note="volume method",
                reason="needed",
                session_id="s1",
            )
            report = stage_and_commit(store, cfg, FakeBackend("passthrough"), class_project)
        assert report.committed
        text = (class_project / "src/box.py").read_text()
        # New method present AND indented as a class member (not at file scope).
        assert "def volume" in text
        for line in text.splitlines():
            if "def volume" in line:
                assert line.startswith("    "), f"method not indented into class: {line!r}"

    def test_modify_and_create_method_same_file(self, class_project: Path):
        # Same-file batch: modify an existing method AND create a new one in the
        # same class. Both must land and the file must compile (Python gate).
        cfg = _config(class_project)
        with Store(class_project / ".trie" / "graph.db") as store:
            store.add_patch("src/box:Box.area", "append a marker line", "x", "s1")
            store.add_create_patch(
                target_file="src/box.py",
                target_qname="src/box:Box.perimeter",
                note="perimeter method",
                reason="needed",
                session_id="s1",
            )
            report = stage_and_commit(
                store,
                cfg,
                FakeBackend("append", per_qname={}),
                class_project,
                session_note="add area marker + perimeter method",
            )
        assert report.committed, report.error
        text = (class_project / "src/box.py").read_text()
        # The created method landed...
        assert "def perimeter" in text
        # ...AND the modified method's marker landed...
        assert _MARKER.strip() in text
        # ...and the file is still valid Python.
        import ast

        ast.parse(text)

    def test_create_broken_source_unresolved(self, project: Path):
        cfg = _config(project)
        before = (project / "src/gamma.py").read_text()
        with Store(project / ".trie" / "graph.db") as store:
            store.add_create_patch(
                target_file="src/gamma.py",
                target_qname="src/gamma:helper",
                note="x",
                reason="y",
                session_id="s1",
            )
            report = stage_and_commit(store, cfg, FakeBackend("broken"), project)
        assert not report.ok
        assert any(u.stage in ("compile", "generate") for u in report.unresolved)
        assert (project / "src/gamma.py").read_text() == before


class TestSameFileMultiLane:
    """Regression: modify/rename/create on the SAME file must not clobber each other.

    Each StagedChange carries a full-file after_file_bytes; commit writes one blob
    per file. The create lane must stack on the modify/structural lane's result so
    all changes for a file share the final bytes (the bug: create computed its own
    after_bytes from the original, overwriting the modify edits).
    """

    def test_modify_and_create_same_file_both_land(self, project: Path):
        cfg = _config(project)
        with Store(project / ".trie" / "graph.db") as store:
            store.add_patch("src/gamma:gamma_fn", "tweak", "r", "s1")
            store.add_create_patch(
                target_file="src/gamma.py",
                target_qname="src/gamma:helper",
                note="a helper",
                reason="r",
                session_id="s1",
            )
            report = stage_and_commit(
                store,
                cfg,
                FakeBackend("append"),
                project,
                session_note="modify gamma_fn and add helper",
            )
        assert report.ok and report.committed
        text = (project / "src/gamma.py").read_text()
        # both the modify (append marker) and the create must be present
        assert "trie-fake-edit" in text  # modify landed
        assert "def helper()" in text  # create landed

    def test_rename_and_create_same_file_both_land(self, project: Path):
        cfg = _config(project)
        with Store(project / ".trie" / "graph.db") as store:
            store.add_rename_patch("src/gamma:gamma_fn", "deepest", "clarity", "s1")
            store.add_create_patch(
                target_file="src/gamma.py",
                target_qname="src/gamma:helper",
                note="a helper",
                reason="r",
                session_id="s1",
            )
            report = stage_and_commit(
                store,
                cfg,
                FakeBackend("append"),
                project,
                session_note="rename gamma_fn and add helper",
            )
        assert report.ok and report.committed
        text = (project / "src/gamma.py").read_text()
        assert "def deepest()" in text  # rename landed
        assert "def helper()" in text  # create landed
        assert "def gamma_fn()" not in text


@pytest.fixture
def two_file_project(tmp_path: Path) -> Path:
    """callee.py defines target(); caller.py's use_it() calls it."""
    src = tmp_path / "src"
    src.mkdir()
    (src / "__init__.py").write_text("")
    (src / "callee.py").write_text('def target() -> int:\n    """A callee."""\n    return 5\n')
    (src / "caller.py").write_text(
        "from src.callee import target\n\n\ndef use_it() -> int:\n    return target() + 1\n"
    )
    (tmp_path / "trie.toml").write_text(PROJECT_TOML)
    (tmp_path / ".gitignore").write_text(".trie/\n__pycache__/\n")
    config, _ = Config.find_and_load(tmp_path)
    with Store(tmp_path / ".trie" / "graph.db") as store:
        scan_project(project_root=tmp_path, config=config, store=store)
        for f in ("callee.py", "caller.py"):
            sync_single_file(
                tmp_path / "src" / f,
                project_root=tmp_path,
                config=config,
                client=FakeTriefactClient(),
                store=store,
            )
    return tmp_path


class TestStructuralCascade:
    """delete/rename must cascade to callers (callers definitely affected, no gate)."""

    def test_delete_cascades_to_caller(self, two_file_project: Path):
        cfg = _config(two_file_project)
        with Store(two_file_project / ".trie" / "graph.db") as store:
            # confirm the edge exists first
            assert "src/caller:use_it" in store.references_in("src/callee:target")
            store.add_delete_patch("src/callee:target", "obsolete", "s1")
            report = stage_and_commit(
                store,
                cfg,
                FakeBackend("append"),
                two_file_project,
                session_note="delete target and fix its caller",
            )
        # the caller must have been queued as a cascade edit (append marker proves it)
        caller_text = (two_file_project / "src/caller.py").read_text()
        assert "trie-fake-edit" in caller_text
        assert any(a.qname == "src/caller:use_it" for a in report.applied)
        assert any(a.op == "delete" for a in report.applied)
        # the now-broken import of the deleted symbol must be removed
        assert "import target" not in caller_text

    def test_rename_cascades_to_caller(self, two_file_project: Path):
        cfg = _config(two_file_project)
        with Store(two_file_project / ".trie" / "graph.db") as store:
            store.add_rename_patch("src/callee:target", "renamed_target", "clarity", "s1")
            report = stage_and_commit(
                store,
                cfg,
                FakeBackend("append"),
                two_file_project,
                session_note="rename target and update its caller",
            )
        # def renamed; caller queued as cascade edit
        assert "def renamed_target()" in (two_file_project / "src/callee.py").read_text()
        caller_text = (two_file_project / "src/caller.py").read_text()
        assert "trie-fake-edit" in caller_text
        assert any(a.qname == "src/caller:use_it" for a in report.applied)
        # the import line must be updated to the new name
        assert "import renamed_target" in caller_text
        assert "import target" not in caller_text.replace("renamed_target", "")
