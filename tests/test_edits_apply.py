from __future__ import annotations

from pathlib import Path

from trie.edits.apply import (
    _compile_check,
    _expand_callers,
    preview_patches,
)
from trie.graph.store import Store


class TestExpandCallers:
    """BFS through caller edges."""

    class FakeRow:
        def fetchone(self):
            return None

    class FakeConn:
        def execute(self, sql, params):
            return TestExpandCallers.FakeRow()

    def test_empty_seeds(self):
        store = type("FakeStore", (), {})()
        store.references_in = lambda qn: []
        store._conn = self.FakeConn()
        result = _expand_callers([], store, cascade_depth=1, hub_threshold=20)
        assert result == set()

    def test_seeds_not_in_store(self):
        store = type("FakeStore2", (), {})()
        store.references_in = lambda qn: []
        store._conn = self.FakeConn()
        result = _expand_callers(["missing:foo"], store, cascade_depth=1, hub_threshold=20)
        assert result == set()


class TestCompileCheck:
    def test_valid_python(self):
        assert _compile_check("def foo():\n    return 1\n") is True

    def test_syntax_error(self):
        assert _compile_check("def foo(:\n") is False

    def test_empty_source(self):
        assert _compile_check("") is True


class TestPreviewPatches:
    def test_no_patches(self, tmp_path: Path):
        store = Store(tmp_path / ".trie" / "graph.db")
        from trie.config import Config

        config = Config()
        result = preview_patches(store, config)
        assert result["total_patches"] == 0
        assert result["patched_symbols"] == 0
        store.close()
