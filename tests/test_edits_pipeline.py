"""Spec for the slimmed patch pipeline: an intent store, not a code generator."""

from __future__ import annotations

import subprocess
from pathlib import Path

from trie.config import Config
from trie.edits.pipeline import preview_patches, record_intent, session_note_ok
from trie.graph.store import Store
from trie.parse.python import extract_symbols


class TestSessionNoteQuality:
    def test_rejects_short_and_boilerplate(self):
        for junk in ("", ".", "fix", "wip", "update", "short"):
            assert not session_note_ok(junk), f"{junk!r} must not satisfy the gate"

    def test_accepts_real_note(self):
        assert session_note_ok("Rework the digest window so boundary rows never leak.")


def _project(tmp_path: Path) -> tuple[Config, Store]:
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    (tmp_path / "m.py").write_text("def f():\n    return 1\n\n\ndef g():\n    return f()\n")
    config = Config.from_dict({})
    store = Store(tmp_path / ".trie" / "graph.db")
    store.upsert_file(path="m.py", fingerprint="fp")
    store.replace_file_symbols("m.py", extract_symbols(tmp_path / "m.py", tmp_path))
    # g calls f — one edge for the preview blast radius.
    ids = {
        row[0]: row[1]
        for row in store._conn.execute("SELECT qualified_name, id FROM symbols").fetchall()
    }
    store._conn.execute(
        "INSERT INTO edges (src_symbol_id, dst_symbol_id, kind) VALUES (?, ?, 'call')",
        (ids["m:g"], ids["m:f"]),
    )
    store._conn.commit()
    return config, store


def test_record_intent_archives_notes_without_generation(tmp_path: Path) -> None:
    config, store = _project(tmp_path)
    src_before = (tmp_path / "m.py").read_text()
    try:
        store.add_patch("m:f", note="f returns one", reason="spec", session_id="s1")
        store.add_create_patch(
            target_file="m.py", target_qname="m:new", note="add new", reason="", session_id="s1"
        )

        # Multi-symbol without a REAL session note: refused (quality-gated).
        refused = record_intent(store, config, tmp_path, session_note="fix")
        assert refused["ok"] is False and refused["error"] == "session_note_required"

        result = record_intent(store, config, tmp_path, session_note="ship the m module rework")
        assert result["ok"] is True and result["mode"] == "record"
        assert result["recorded"] == 2
        assert set(result["symbols"]) == {"m:f", "m:new"}

        # Sealed in place: rows stay in the qname-keyed table, stamped with
        # the session note, until the digest write consumes them.
        sealed = store.get_all_patches_grouped(applied=True)
        assert set(sealed) == {"m:f"}
        assert sealed["m:f"][0]["session_note"] == "ship the m module rework"
        creates = store.get_create_patches_grouped(applied=True)
        assert [c["target_qname"] for rows_ in creates.values() for c in rows_] == ["m:new"]

        # Nothing left UNSEALED; source byte-identical (no generation, ever).
        assert store.get_patched_qnames(applied=False) == []
        assert store.get_create_patches_grouped(applied=False) == {}
        assert (tmp_path / "m.py").read_text() == src_before

        # Consumption (what the digest write does) empties the tables.
        store.delete_applied_patches()
        assert store.get_patched_qnames() == []
        assert store.get_create_patches_grouped() == {}

        # Empty queue re-run is a no-op success.
        again = record_intent(store, config, tmp_path, session_note="")
        assert again["ok"] is True and again["recorded"] == 0
    finally:
        store.close()


def test_record_intent_preserves_structural_ops(tmp_path: Path) -> None:
    config, store = _project(tmp_path)
    try:
        store.add_patch("m:f", "f is superseded", "", "s1", kind="delete")
        result = record_intent(store, config, tmp_path, session_note="")
        assert result["ok"] is True and result["recorded"] == 1
        sealed = store.get_all_patches_grouped(applied=True)
        assert sealed["m:f"][0]["kind"] == "delete"
    finally:
        store.close()


def test_single_symbol_needs_no_session_note(tmp_path: Path) -> None:
    config, store = _project(tmp_path)
    try:
        store.add_patch("m:f", note="only one symbol", reason="", session_id="s1")
        result = record_intent(store, config, tmp_path, session_note="")
        assert result["ok"] is True and result["recorded"] == 1
    finally:
        store.close()


def test_preview_patches_reports_pending_and_blast_radius(tmp_path: Path) -> None:
    config, store = _project(tmp_path)
    try:
        store.add_patch("m:f", note="change f", reason="", session_id="s1")
        out = preview_patches(store, config)
        assert out["patched_list"] == ["m:f"]
        assert out["total_patches"] == 1
        # g calls f, so the review blast radius pulls it in.
        assert "m:g" in out["cascade_list"]
    finally:
        store.close()
