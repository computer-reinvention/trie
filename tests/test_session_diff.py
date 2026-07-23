"""Tests for the session log archive and the `trie diff` evidence collection/prompt assembly."""

from __future__ import annotations

import subprocess
from pathlib import Path

try:
    import pytest
except ImportError:  # pragma: no cover
    pytest = None  # type: ignore[assignment]

from trie.config import Config
from trie.graph.store import Store
from trie.parse.python import extract_symbols
from trie.session_diff import SessionDiff, build_narrative_prompt, collect_session_diff
from trie.session_log import log_path, read_entries, record_applied


def test_record_and_read_entries_roundtrip(tmp_path: Path) -> None:
    record_applied(
        tmp_path,
        [
            {
                "session_id": "s1",
                "qname": "a/b:f",
                "op": "modify",
                "notes": ["add flag"],
                "reasons": [],
            },
            {
                "session_id": "s2",
                "qname": "a/b:g",
                "op": "create",
                "notes": ["new helper"],
                "reasons": ["needed by f"],
            },
        ],
    )

    assert log_path(tmp_path).exists()

    all_entries = read_entries(tmp_path)
    assert len(all_entries) == 2
    assert all(isinstance(e["ts"], float) for e in all_entries)
    assert all_entries[0]["qname"] == "a/b:f"
    assert all_entries[1]["qname"] == "a/b:g"

    s1_entries = read_entries(tmp_path, session_id="s1")
    assert len(s1_entries) == 1
    assert s1_entries[0]["qname"] == "a/b:f"

    with log_path(tmp_path).open("a") as fh:
        fh.write("not json\n")

    entries_after_corrupt = read_entries(tmp_path)
    assert len(entries_after_corrupt) == 2


def test_record_applied_empty_and_missing_log(tmp_path: Path) -> None:
    record_applied(tmp_path, [])
    assert not log_path(tmp_path).exists()
    assert read_entries(tmp_path) == []


def test_build_narrative_prompt_sections_and_truncation() -> None:
    data = SessionDiff(
        triefact_diff="x" * 500,
        applied=[
            {
                "session_id": "s1",
                "session_note": "add session diff feature",
                "qname": "a/b:f",
                "op": "modify",
                "notes": ["do thing"],
                "reasons": ["why"],
            }
        ],
        pending=[
            {
                "qname": "a/b:g",
                "op": "create",
                "note": "new helper",
                "reason": "",
                "session_id": "s1",
            }
        ],
        base="HEAD",
    )

    prompt = build_narrative_prompt(data, max_diff_chars=100)

    assert "## Session intents" in prompt
    assert "add session diff feature" in prompt

    assert "## Applied patch notes" in prompt
    assert "[modify] a/b:f" in prompt
    assert "do thing" in prompt
    assert "(reason: why)" in prompt

    assert "## Pending patch notes" in prompt
    assert "[create] a/b:g" in prompt

    assert "x" * 100 in prompt
    assert "x" * 101 not in prompt
    assert "truncated" in prompt

    # Empty case
    empty = SessionDiff()
    assert empty.is_empty() is True
    empty_prompt = build_narrative_prompt(empty)
    assert "(none)" in empty_prompt
    assert "(no triefact changes)" in empty_prompt


def test_collect_session_diff_gathers_all_evidence(tmp_path: Path) -> None:
    import shutil

    if not shutil.which("git"):
        if pytest is not None:
            pytest.skip("git not available")
        return

    # --- Arrange: initialise git repo ---
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.email", "t@t"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.name", "t"], cwd=tmp_path, check=True)

    triefacts_dir = tmp_path / "triefacts"
    triefacts_dir.mkdir(parents=True)
    mod_md = triefacts_dir / "mod.md"
    mod_md.write_text("old prose\n")

    subprocess.run(["git", "add", "-A"], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "init"], cwd=tmp_path, check=True)

    # Uncommitted working-tree change
    mod_md.write_text("new prose\n")

    # --- Arrange: session log ---
    record_applied(
        tmp_path,
        [{"session_id": "s1", "qname": "m:f", "op": "modify", "notes": ["n1"], "reasons": []}],
    )

    # --- Arrange: store with pending patches ---
    db_path = tmp_path / ".trie" / "graph.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)
    store = Store(db_path)
    try:
        src_py = tmp_path / "m.py"
        src_py.write_text("def f():\n    return 1\n")
        store.upsert_file(path="m.py", fingerprint="fp")
        store.replace_file_symbols("m.py", extract_symbols(src_py, tmp_path))
        store.add_patch("m:f", note="pending note", reason="r", session_id="s1")
        store.add_create_patch(
            target_file="m.py",
            target_qname="m:new",
            note="make new",
            reason="",
            session_id="s1",
        )

        # --- Arrange: config ---
        config = Config.from_dict({})

        # --- Act ---
        data = collect_session_diff(tmp_path, config, store, session_id=None, base="HEAD")

        # --- Assert: triefact diff ---
        assert "old prose" in data.triefact_diff
        assert "new prose" in data.triefact_diff

        # --- Assert: applied entries ---
        assert len(data.applied) == 1
        assert data.applied[0]["qname"] == "m:f"

        # --- Assert: pending patches ---
        pending_qnames = {row["qname"] for row in data.pending}
        pending_ops = {row["qname"]: row["op"] for row in data.pending}
        pending_notes = {row["qname"]: row["note"] for row in data.pending}
        assert "m:f" in pending_qnames
        assert pending_ops["m:f"] == "modify"
        assert pending_notes["m:f"] == "pending note"
        assert "m:new" in pending_qnames
        assert pending_ops["m:new"] == "create"
        assert pending_notes["m:new"] == "make new"

        # --- Assert: session ids ---
        assert data.session_ids() == ["s1"]

        # --- Assert: filtering by a different session_id yields empty lists ---
        data_other = collect_session_diff(tmp_path, config, store, session_id="other", base="HEAD")
        assert data_other.applied == []
        assert data_other.pending == []

    finally:
        store.close()


def test_collect_session_diff_includes_new_triefacts(tmp_path: Path) -> None:
    import shutil

    if not shutil.which("git"):
        if pytest is not None:
            pytest.skip("git not available")
        return

    # Initialize a git repo and make an initial commit with one triefact
    subprocess.run(["git", "init"], cwd=tmp_path, check=True, capture_output=True)
    subprocess.run(
        ["git", "config", "user.email", "test@test.com"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )
    subprocess.run(
        ["git", "config", "user.name", "Test"], cwd=tmp_path, check=True, capture_output=True
    )

    triefacts_dir = tmp_path / "triefacts"
    triefacts_dir.mkdir()

    existing_triefact = triefacts_dir / "mod.md"
    existing_triefact.write_text("existing module prose")

    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True, capture_output=True)
    subprocess.run(
        ["git", "commit", "-m", "initial"], cwd=tmp_path, check=True, capture_output=True
    )

    # Create a new untracked triefact file (simulating a file created during a session)
    new_triefact = triefacts_dir / "session_feature.md"
    new_triefact.write_text("session feature prose")

    # Build a minimal store with the correct constructor signature
    db_path = tmp_path / ".trie" / "graph.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)
    store = Store(db_path)

    config = Config.from_dict({})

    try:
        data = collect_session_diff(tmp_path, config, store, base="HEAD")

        assert "session feature prose" in data.triefact_diff
        assert "session_feature.md" in data.triefact_diff
    finally:
        store.close()


def test_synthesize_narrative_uses_cache_prefix() -> None:
    import types

    from trie.session_diff import SessionDiff as LocalSessionDiff  # type: ignore[attr-defined]
    from trie.session_diff import synthesize_narrative

    diff = LocalSessionDiff(triefact_diff="- old fact\n+ new fact\n")

    class FakeClientWithCache:
        def __init__(self) -> None:
            self.recorded_system: str | None = None
            self.recorded_user: str | None = None
            self.recorded_cache_prefix: str | None = None
            self.recorded_max_tokens: int | None = None

        def run_text(
            self,
            system_prompt: str,
            user_prompt: str,
            *,
            max_tokens: int = 1024,
            cache_prefix: str | None = None,
        ) -> object:
            self.recorded_system = system_prompt
            self.recorded_user = user_prompt
            self.recorded_cache_prefix = cache_prefix
            self.recorded_max_tokens = max_tokens
            return types.SimpleNamespace(output="narrative md")

    client_with_cache = FakeClientWithCache()
    result = synthesize_narrative(diff, client_with_cache)

    assert result == "narrative md"
    assert client_with_cache.recorded_cache_prefix is not None
    assert "## Raw triefact diff" in client_with_cache.recorded_cache_prefix
    recorded_user = client_with_cache.recorded_user or ""
    assert "## Raw triefact diff" not in recorded_user

    class FakeClientNoCache:
        def __init__(self) -> None:
            self.recorded_system: str | None = None
            self.recorded_user: str | None = None

        def run_text(
            self,
            system_prompt: str,
            user_prompt: str,
            *,
            max_tokens: int = 1024,
        ) -> object:
            self.recorded_system = system_prompt
            self.recorded_user = user_prompt
            return types.SimpleNamespace(output="narrative md")

    client_no_cache = FakeClientNoCache()
    result_fallback = synthesize_narrative(diff, client_no_cache)

    assert result_fallback == "narrative md"
    recorded_user_no_cache = client_no_cache.recorded_user or ""
    assert "## Raw triefact diff" in recorded_user_no_cache
