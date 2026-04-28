from __future__ import annotations

from pathlib import Path

import pytest

from trie.graph.store import SCHEMA_VERSION, FileRecord, Store
from trie.parse.python import extract_symbols


@pytest.fixture
def store(tmp_path: Path) -> Store:
    s = Store(tmp_path / ".trie" / "graph.db")
    yield s
    s.close()


def test_schema_version_recorded(store: Store):
    row = store._conn.execute("SELECT version FROM schema_version").fetchone()
    assert row[0] == SCHEMA_VERSION


def test_upsert_and_get_file(store: Store):
    assert store.get_file("src/foo.py") is None
    store.upsert_file(path="src/foo.py", fingerprint="abc", now=1000)
    rec = store.get_file("src/foo.py")
    assert rec == FileRecord(path="src/foo.py", fingerprint="abc", last_scanned_at=1000)


def test_upsert_overwrites_existing(store: Store):
    store.upsert_file(path="src/foo.py", fingerprint="v1", now=1000)
    store.upsert_file(path="src/foo.py", fingerprint="v2", now=2000)
    rec = store.get_file("src/foo.py")
    assert rec is not None
    assert rec.fingerprint == "v2"
    assert rec.last_scanned_at == 2000


def test_list_files_sorted(store: Store):
    store.upsert_file(path="b.py", fingerprint="b")
    store.upsert_file(path="a.py", fingerprint="a")
    paths = [f.path for f in store.list_files()]
    assert paths == ["a.py", "b.py"]


def test_delete_file_cascades_symbols(store: Store, tmp_path: Path):
    src = tmp_path / "foo.py"
    src.write_text("def foo():\n    pass\n")
    syms = extract_symbols(src)

    store.upsert_file(path="foo.py", fingerprint="x")
    store.replace_file_symbols("foo.py", syms)
    assert store.count_symbols(file_path="foo.py") == 1

    store.delete_file("foo.py")
    assert store.count_symbols(file_path="foo.py") == 0


def test_replace_file_symbols_replaces_atomically(store: Store, tmp_path: Path):
    src_a = tmp_path / "a.py"
    src_a.write_text("def first():\n    pass\n")
    syms_v1 = extract_symbols(src_a)

    store.upsert_file(path="a.py", fingerprint="v1")
    store.replace_file_symbols("a.py", syms_v1)
    assert store.count_symbols(file_path="a.py") == 1

    src_a.write_text("def first():\n    pass\n\ndef second():\n    pass\n")
    syms_v2 = extract_symbols(src_a)
    store.replace_file_symbols("a.py", syms_v2)
    assert store.count_symbols(file_path="a.py") == 2

    # Unique constraint not violated by repeated upsert
    store.replace_file_symbols("a.py", syms_v2)
    assert store.count_symbols(file_path="a.py") == 2


def test_count_symbols_public_only(store: Store, tmp_path: Path):
    src = tmp_path / "x.py"
    src.write_text(
        "def public():\n    pass\n\n\n"
        "def _private():\n    pass\n\n\n"
        "class _Hidden:\n    def method(self):\n        pass\n"
    )
    syms = extract_symbols(src)
    store.upsert_file(path="x.py", fingerprint="x")
    store.replace_file_symbols("x.py", syms)
    assert store.count_symbols(file_path="x.py", public_only=True) == 1


def test_file_stats(store: Store, tmp_path: Path):
    src_a = tmp_path / "a.py"
    src_a.write_text(
        "def alpha():\n    pass\n\n\ndef _hidden():\n    pass\n\n\n"
        "class Public:\n    def m(self):\n        pass\n"
    )
    src_b = tmp_path / "b.py"
    src_b.write_text("# empty\n")  # no symbols

    store.upsert_file(path="a.py", fingerprint="a")
    store.replace_file_symbols("a.py", extract_symbols(src_a))
    store.upsert_file(path="b.py", fingerprint="b")
    store.replace_file_symbols("b.py", extract_symbols(src_b))

    stats = {s.path: s for s in store.file_stats()}
    assert stats["a.py"].total_symbols == 4  # alpha, _hidden, Public, Public.m
    assert stats["a.py"].public_symbols == 3
    assert stats["b.py"].total_symbols == 0
    assert stats["b.py"].public_symbols == 0


def test_context_manager_closes(tmp_path: Path):
    db = tmp_path / ".trie" / "graph.db"
    with Store(db) as s:
        s.upsert_file(path="x.py", fingerprint="x")
    # Re-opening should still see the data
    with Store(db) as s2:
        assert s2.get_file("x.py") is not None


def test_transaction_rolls_back_on_error(store: Store):
    store.upsert_file(path="x.py", fingerprint="v1")
    with pytest.raises(RuntimeError, match="boom"), store.transaction() as conn:
        conn.execute("UPDATE files SET fingerprint = 'v2' WHERE path = 'x.py'")
        raise RuntimeError("boom")
    rec = store.get_file("x.py")
    assert rec is not None
    assert rec.fingerprint == "v1"
