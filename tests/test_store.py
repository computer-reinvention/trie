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
    # Under symbol-level sync, `public_symbols` is a legacy field name; the value
    # equals `total_symbols` because every parser-surfaced symbol is documented.
    assert stats["a.py"].public_symbols == 4
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


# --- patch ops ---


def test_patches_table_exists(store: Store):
    """Patches schema is created by SCHEMA_SQL."""
    table_count = store._conn.execute(
        "SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='patches'"
    ).fetchone()[0]
    assert table_count == 1


def test_add_patch_creates_row(store: Store, tmp_path: Path):
    src = tmp_path / "a.py"
    src.write_text("def greet():\n    return 'hello'\n")
    syms = extract_symbols(src)
    store.upsert_file(path="a.py", fingerprint="x")
    store.replace_file_symbols("a.py", syms)

    pid = store.add_patch("a:greet", "change return value", "test", "sess1")
    assert isinstance(pid, int) and pid > 0


def test_add_patch_unknown_qname_raises(store: Store):
    with pytest.raises(KeyError):
        store.add_patch("nonexistent:foo", "note", "reason", "sess1")


def test_get_patches_for_qname(store: Store, tmp_path: Path):
    src = tmp_path / "a.py"
    src.write_text("def greet():\n    return 'hello'\n")
    syms = extract_symbols(src)
    store.upsert_file(path="a.py", fingerprint="x")
    store.replace_file_symbols("a.py", syms)

    store.add_patch("a:greet", "note1", "reason1", "sess1")
    store.add_patch("a:greet", "note2", "reason2", "sess1")

    patches = store.get_patches_for_qname("a:greet")
    assert len(patches) == 2
    assert patches[0]["note"] == "note1"
    assert patches[1]["note"] == "note2"


def test_get_patches_for_unknown_qname_returns_empty(store: Store):
    assert store.get_patches_for_qname("no/such:sym") == []


def test_get_all_patches_grouped(store: Store, tmp_path: Path):
    src = tmp_path / "a.py"
    src.write_text("def greet():\n    return 'hello'\n\ndef farewell():\n    return 'bye'\n")
    syms = extract_symbols(src)
    store.upsert_file(path="a.py", fingerprint="x")
    store.replace_file_symbols("a.py", syms)

    store.add_patch("a:greet", "note1", "r1", "s1")
    store.add_patch("a:farewell", "note2", "r2", "s1")

    grouped = store.get_all_patches_grouped()
    assert len(grouped) == 2
    all_notes = [p["note"] for plist in grouped.values() for p in plist]
    assert set(all_notes) == {"note1", "note2"}


def test_patch_count_for_symbol(store: Store, tmp_path: Path):
    src = tmp_path / "a.py"
    src.write_text("def greet():\n    return 'hello'\n")
    syms = extract_symbols(src)
    store.upsert_file(path="a.py", fingerprint="x")
    store.replace_file_symbols("a.py", syms)

    store.add_patch("a:greet", "n1", "r1", "s1")
    sym_id = store._conn.execute(
        "SELECT id FROM symbols WHERE qualified_name = ?", ("a:greet",)
    ).fetchone()[0]
    assert store.patch_count_for_symbol(sym_id) == 1


def test_delete_patches_by_qname(store: Store, tmp_path: Path):
    src = tmp_path / "a.py"
    src.write_text("def greet():\n    return 'hello'\n")
    syms = extract_symbols(src)
    store.upsert_file(path="a.py", fingerprint="x")
    store.replace_file_symbols("a.py", syms)

    store.add_patch("a:greet", "n1", "r1", "s1")
    assert len(store.get_patches_for_qname("a:greet")) == 1
    store.delete_patches(qname="a:greet")
    assert len(store.get_patches_for_qname("a:greet")) == 0


def test_delete_patches_all(store: Store, tmp_path: Path):
    src = tmp_path / "a.py"
    src.write_text("def greet():\n    return 'hello'\n")
    syms = extract_symbols(src)
    store.upsert_file(path="a.py", fingerprint="x")
    store.replace_file_symbols("a.py", syms)

    store.add_patch("a:greet", "n1", "r1", "s1")
    count = store.delete_patches(all=True)
    assert count >= 1
    assert len(store.get_patches_for_qname("a:greet")) == 0


def test_delete_patches_by_session(store: Store, tmp_path: Path):
    src = tmp_path / "a.py"
    src.write_text("def greet():\n    return 'hello'\n")
    syms = extract_symbols(src)
    store.upsert_file(path="a.py", fingerprint="x")
    store.replace_file_symbols("a.py", syms)

    store.add_patch("a:greet", "n1", "r1", "ses_x")
    store.add_patch("a:greet", "n2", "r2", "ses_y")
    assert len(store.get_patches_for_qname("a:greet")) == 2
    store.delete_patches(session_id="ses_x")
    patches = store.get_patches_for_qname("a:greet")
    assert len(patches) == 1
    assert patches[0]["session_id"] == "ses_y"


def test_get_patched_qnames(store: Store, tmp_path: Path):
    src = tmp_path / "a.py"
    src.write_text("def greet():\n    return 'hello'\n")
    syms = extract_symbols(src)
    store.upsert_file(path="a.py", fingerprint="x")
    store.replace_file_symbols("a.py", syms)

    assert store.get_patched_qnames() == []
    store.add_patch("a:greet", "n1", "r1", "s1")
    assert store.get_patched_qnames() == ["a:greet"]


def test_get_symbol_detail_includes_patches(store: Store, tmp_path: Path):
    src = tmp_path / "a.py"
    src.write_text("def greet():\n    return 'hello'\n")
    syms = extract_symbols(src)
    store.upsert_file(path="a.py", fingerprint="x")
    store.replace_file_symbols("a.py", syms)

    detail = store.get_symbol_detail("a:greet")
    assert detail is not None
    assert detail.pending_patches == []
    assert detail.pending_patch_count == 0

    store.add_patch("a:greet", "my note", "my reason", "s1")
    detail2 = store.get_symbol_detail("a:greet")
    assert detail2 is not None
    assert len(detail2.pending_patches) == 1
    assert detail2.pending_patches[0]["note"] == "my note"
    assert detail2.pending_patch_count == 1


def test_grep_symbols_includes_patch_count(store: Store, tmp_path: Path):
    from trie.graph.store import GrepPredicate

    src = tmp_path / "a.py"
    src.write_text("def greet():\n    return 'hello'\n")
    syms = extract_symbols(src)
    store.upsert_file(path="a.py", fingerprint="x")
    store.replace_file_symbols("a.py", syms)

    store.add_patch("a:greet", "n1", "r1", "s1")
    hits = store.grep_symbols(GrepPredicate(name_contains="greet"))
    assert len(hits) == 1
    assert hits[0].pending_patch_count == 1


def test_patches_cascaded_on_symbol_delete(store: Store, tmp_path: Path):
    src = tmp_path / "a.py"
    src.write_text("def greet():\n    return 'hello'\n")
    syms = extract_symbols(src)
    store.upsert_file(path="a.py", fingerprint="x")
    store.replace_file_symbols("a.py", syms)

    store.add_patch("a:greet", "n1", "r1", "s1")
    store.replace_file_symbols("a.py", [])  # Remove the symbol
    remaining = store.get_patches_for_qname("a:greet")
    assert remaining == []


# --- WS6: structural patch kinds + create_patches ---------------------------


def _seed_greet(store: Store, tmp_path: Path) -> None:
    src = tmp_path / "a.py"
    src.write_text("def greet():\n    return 'hello'\n")
    store.upsert_file(path="a.py", fingerprint="x")
    store.replace_file_symbols("a.py", extract_symbols(src))


def test_add_patch_defaults_to_modify_kind(store: Store, tmp_path: Path):
    _seed_greet(store, tmp_path)
    store.add_patch("a:greet", "n", "r", "s1")
    p = store.get_patches_for_qname("a:greet")[0]
    assert p["kind"] == "modify"
    assert p["rename_to"] is None


def test_add_delete_patch(store: Store, tmp_path: Path):
    _seed_greet(store, tmp_path)
    store.add_delete_patch("a:greet", "obsolete", "s1")
    p = store.get_patches_for_qname("a:greet")[0]
    assert p["kind"] == "delete"


def test_add_rename_patch_carries_new_name(store: Store, tmp_path: Path):
    _seed_greet(store, tmp_path)
    store.add_rename_patch("a:greet", "salute", "clarity", "s1")
    p = store.get_patches_for_qname("a:greet")[0]
    assert p["kind"] == "rename"
    assert p["rename_to"] == "salute"


def test_delete_and_rename_patches_require_existing_symbol(store: Store):
    with pytest.raises(KeyError):
        store.add_delete_patch("nope:x", "r", "s1")
    with pytest.raises(KeyError):
        store.add_rename_patch("nope:x", "y", "r", "s1")


def test_grouped_patches_include_kind(store: Store, tmp_path: Path):
    _seed_greet(store, tmp_path)
    store.add_rename_patch("a:greet", "salute", "r", "s1")
    grouped = store.get_all_patches_grouped()
    rows = next(iter(grouped.values()))
    assert rows[0]["kind"] == "rename"
    assert rows[0]["rename_to"] == "salute"


def test_add_and_group_create_patches(store: Store):
    store.add_create_patch(
        target_file="a.py",
        target_qname="a:new_fn",
        note="a brand new helper",
        reason="needed",
        session_id="s1",
        anchor_qname="a:greet",
    )
    grouped = store.get_create_patches_grouped()
    assert "a.py" in grouped
    cp = grouped["a.py"][0]
    assert cp["target_qname"] == "a:new_fn"
    assert cp["anchor_qname"] == "a:greet"
    assert cp["note"] == "a brand new helper"


def test_delete_create_patches_by_target(store: Store):
    store.add_create_patch(
        target_file="a.py", target_qname="a:x", note="n", reason="r", session_id="s1"
    )
    store.add_create_patch(
        target_file="a.py", target_qname="a:y", note="n", reason="r", session_id="s1"
    )
    assert store.delete_create_patches(target_qname="a:x") == 1
    grouped = store.get_create_patches_grouped()
    assert [c["target_qname"] for c in grouped.get("a.py", [])] == ["a:y"]


def test_delete_create_patches_by_session_and_all(store: Store):
    store.add_create_patch(
        target_file="a.py", target_qname="a:x", note="n", reason="r", session_id="s1"
    )
    store.add_create_patch(
        target_file="b.py", target_qname="b:z", note="n", reason="r", session_id="s2"
    )
    assert store.delete_create_patches(session_id="s1") == 1
    assert store.delete_create_patches(all=True) == 1
    assert store.get_create_patches_grouped() == {}
