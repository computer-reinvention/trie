"""Tests for the session log archive and the `trie diff` evidence collection/prompt assembly."""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

try:
    import pytest  # type: ignore[import-not-found]
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


def test_collect_session_diff_gathers_all_evidence(tmp_path: Path, mocker) -> None:  # type: ignore[no-untyped-def]
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

        # --- Assert: `since` parameter is forwarded to read_entries ---
        # A future timestamp should exclude the already-recorded entry
        import time

        future_ts = time.time() + 3600

        from trie import session_log as _session_log

        original_read_entries = _session_log.read_entries
        captured_since = []

        def capturing_read_entries(project_root, *, session_id=None, since=None):  # type: ignore[no-untyped-def]
            captured_since.append(since)
            return original_read_entries(project_root, session_id=session_id, since=since)

        mocker.patch.object(_session_log, "read_entries", side_effect=capturing_read_entries)
        data_since = collect_session_diff(
            tmp_path, config, store, session_id=None, base="HEAD", since=future_ts
        )

        # Confirm since was forwarded
        assert captured_since == [future_ts]
        # No applied entries should exist after a future timestamp
        assert data_since.applied == []

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


def test_collect_session_diff_since_filters_applied(tmp_path: Path) -> None:
    import shutil

    from trie.session_diff import collect_session_diff as _collect_session_diff

    if not shutil.which("git"):
        if pytest is not None:
            pytest.skip("git not available")
        return

    # Set up a minimal git repo so triefact diff doesn't fail
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.email", "t@t"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.name", "t"], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-q", "--allow-empty", "-m", "init"], cwd=tmp_path, check=True)

    # Set up session log with two entries at explicit, distinct timestamps
    record_applied(
        tmp_path,
        [
            {
                "session_id": "s1",
                "qname": "pkg.early",
                "op": "modify",
                "notes": [],
                "reasons": [],
                "ts": 100.0,
            }
        ],
    )
    record_applied(
        tmp_path,
        [
            {
                "session_id": "s1",
                "qname": "pkg.late",
                "op": "modify",
                "notes": [],
                "reasons": [],
                "ts": 200.0,
            }
        ],
    )

    # Build a minimal Store
    db_dir = tmp_path / ".trie"
    db_dir.mkdir(parents=True, exist_ok=True)
    db_path = db_dir / "graph.db"
    config = Config.from_dict({})
    store = Store(db_path)
    try:
        # Sanity check: both entries recorded
        all_entries = read_entries(tmp_path)
        assert len(all_entries) == 2

        # since=150.0 is between early (100.0) and late (200.0) — only the late entry should appear
        data_filtered = _collect_session_diff(tmp_path, config, store, since=150.0, base="HEAD")
        applied_qnames_filtered = [e["qname"] for e in data_filtered.applied]
        assert "pkg.late" in applied_qnames_filtered
        assert "pkg.early" not in applied_qnames_filtered

        # since=None — both entries should appear
        data_all = _collect_session_diff(tmp_path, config, store, since=None, base="HEAD")
        applied_qnames_all = [e["qname"] for e in data_all.applied]
        assert "pkg.early" in applied_qnames_all
        assert "pkg.late" in applied_qnames_all
    finally:
        store.close()


def test_render_digest_section_shape() -> None:
    from trie.session_diff import SessionDiff, render_digest_section

    multiline_note = "# heading inside note\n1. item one\n2. item two\nActual first sentence."

    data = SessionDiff(
        triefact_diff="",
        applied=[
            {
                "op": "modify",
                "qname": "m:f",
                "notes": [multiline_note, "Follow-up clarification."],
                "churn": 5,
            },
            {
                "op": "create",
                "qname": "m:new_sym",
                "notes": ["Fresh symbol created."],
                "churn": 3,
            },
        ],
        pending=[
            {
                "op": "create",
                "qname": "m:pending_sym",
                "note": "Not yet applied.",
                "reason": "",
            }
        ],
    )

    deltas = [
        {
            "qname": "m:f",
            "status": "changed",
            "before": "Old meaning.",
            "after": "New meaning.",
        },
        {
            "qname": "m:new_sym",
            "status": "added",
            "after": "Fresh symbol.",
        },
    ]

    output = render_digest_section(
        data,
        title="Ship the widget",
        date_str="2026-07-24",
        parent_short="abc123def456",
        narrative="## Bad H2\nBody.",
        deltas=deltas,
    )

    # Header shape
    assert output.startswith("## Ship the widget — 2026-07-24 (parent abc123def456)"), (
        f"Header not found at start; got: {output[:120]!r}"
    )

    # Narrative demotion: '## Bad H2' becomes '### Bad H2'
    assert "### Bad H2" in output, "H2 inside narrative should be demoted to ### Bad H2"
    assert (
        "## Bad H2"
        not in output.split("## Ship the widget — 2026-07-24 (parent abc123def456)", 1)[
            1
        ].splitlines()[0]
    ), "Raw '## Bad H2' should not appear after demotion"
    # More thorough: no line '## Bad H2' anywhere in output
    for line in output.splitlines():
        assert line.strip() != "## Bad H2", f"Undemotion line found: {line!r}"

    # Changes section
    assert "### Changes" in output, "### Changes section missing"
    assert '~ m:f — "Old meaning." → "New meaning."' in output, "Changed symbol delta line missing"
    assert "+ m:new_sym" in output, "Added symbol line missing"

    # follow-ups suffix for doubly-noted symbol
    assert "(+1 follow-up" in output or "follow-up" in output, (
        "Follow-ups suffix missing for doubly-noted symbol"
    )

    # Markdown injection guarantee: every line is either a renderer heading or does not start with '#'
    renderer_heading_prefixes = ("## ", "### ")
    for line in output.splitlines():
        if line.startswith("#"):
            assert any(line.startswith(p) for p in renderer_heading_prefixes), (
                f"Raw '#' line leaked into output (injection): {line!r}"
            )

    # Raw '# heading inside note' must never appear as a '#'-prefixed line
    for line in output.splitlines():
        assert line.rstrip() != "# heading inside note", (
            "Raw '# heading' from note text leaked into output"
        )

    # Forbidden old-format artifacts
    assert "(reason:" not in output, "Old '(reason:' format must not appear"
    assert "### Intent" not in output, "Old ### Intent section must not appear"
    assert "### Applied" not in output, "Old ### Applied section must not appear"
    assert "### Triefact changes" not in output, "Old ### Triefact changes must not appear"

    # Staged (not applied) section
    assert "### Staged (not applied)" in output, "### Staged (not applied) section missing"
    # pending entry appears on one line
    pending_lines = [ln for ln in output.splitlines() if "m:pending_sym" in ln]
    assert len(pending_lines) == 1, (
        f"Pending symbol should appear on exactly one line; got: {pending_lines}"
    )

    # max_changes=1: exactly one change bullet plus '… and N more'
    output_limited = render_digest_section(
        data,
        title="Ship the widget",
        date_str="2026-07-24",
        parent_short="abc123def456",
        narrative="## Bad H2\nBody.",
        deltas=deltas,
        max_changes=1,
    )
    # Only the Changes section counts: bullets after '### Changes', before the next '###'
    changes_body = output_limited.split("### Changes", 1)[1].split("###", 1)[0]
    bullets = [ln for ln in changes_body.splitlines() if ln.startswith("- ")]
    symbol_bullets = [ln for ln in bullets if not ln.startswith("- … and")]
    overflow = [ln for ln in bullets if ln.startswith("- … and")]
    assert len(symbol_bullets) == 1, (
        f"With max_changes=1 expected exactly 1 change bullet; got {symbol_bullets}"
    )
    assert len(overflow) == 1, f"Expected one overflow marker line; got {bullets}"
    assert any("more" in ln for ln in output_limited.splitlines()), (
        "'… and N more' line missing when max_changes=1"
    )


def test_upsert_digest_prepend_replace_trim() -> None:
    from trie.session_diff import DIGEST_HEADER, upsert_digest

    section_a = "## Some title A — 2024-01-01 (parent aaaa)\n\nContent for section A.\n"
    section_b = "## Some title B — 2024-01-02 (parent bbbb)\n\nContent for section B.\n"
    section_b2 = "## Some title B2 — 2024-01-02 (parent bbbb)\n\nReplaced content for section B2.\n"
    section_c = "## Some title C — 2024-01-03 (parent cccc)\n\nContent for section C.\n"

    # 1. Fresh file: result starts with DIGEST_HEADER and contains section_a
    result1 = upsert_digest("", section_a, base_short="aaaa")
    assert result1.startswith(DIGEST_HEADER), (
        f"Expected result to start with DIGEST_HEADER, got: {result1[:80]!r}"
    )
    assert "Content for section A." in result1

    # 2. Prepend: section_b with base 'bbbb' appears BEFORE section_a in the output
    result2 = upsert_digest(result1, section_b, base_short="bbbb")
    pos_b = result2.index("Content for section B.")
    pos_a = result2.index("Content for section A.")
    assert pos_b < pos_a, "section_b should appear before section_a after prepend"
    assert "Content for section A." in result2
    assert "Content for section B." in result2

    # 3. Replace on same base 'bbbb': section_b2 replaces section_b, section_a remains
    result3 = upsert_digest(result2, section_b2, base_short="bbbb")
    assert "Replaced content for section B2." in result3, (
        "New body for base bbbb should appear in output"
    )
    assert "Content for section B." not in result3, (
        "Old body for base bbbb should be removed after replace"
    )
    assert "Content for section A." in result3, (
        "section_a should still be present after replace of bbbb"
    )

    # 4. Trim: with max_entries=2, adding a third distinct base keeps only 2 newest
    result4 = upsert_digest(result3, section_c, base_short="cccc", max_entries=2)
    # section_c (newest) and section_b2 (second newest) should be present
    assert "Content for section C." in result4, "Newest section_c should be present"
    assert "Replaced content for section B2." in result4, (
        "Second-newest section_b2 should be present"
    )
    # section_a (oldest) should have been trimmed
    assert "Content for section A." not in result4, (
        "Oldest section_a should be trimmed when max_entries=2"
    )

    # 5. Regression: narrative body containing a '## Inner heading' line must NOT
    #    be mis-parsed as an entry boundary, causing a phantom entry or a broken
    #    same-base replace.
    #
    #    Build a section for base 'cccc' whose body legitimately contains an inner
    #    '## ' line (as an LLM narrative might produce before heading demotion).
    section_cccc_with_inner = (
        "## Some title cccc — 2024-01-03 (parent cccc)\n\n"
        "Narrative before inner heading.\n\n"
        "## Inner heading that is narrative, not an entry\n\n"
        "More narrative text after inner heading.\n"
    )
    # Start from a two-entry digest: aaaa + bbbb2
    base_digest = upsert_digest("", section_a, base_short="aaaa")
    base_digest = upsert_digest(base_digest, section_b2, base_short="bbbb")

    # Insert the tricky cccc entry (with the inner ## heading in its body)
    with_inner = upsert_digest(base_digest, section_cccc_with_inner, base_short="cccc")

    # Now replace cccc with a clean new body
    section_cccc_replacement = (
        "## Some title cccc2 — 2024-01-03 (parent cccc)\n\nClean replacement for cccc.\n"
    )
    replaced = upsert_digest(with_inner, section_cccc_replacement, base_short="cccc")

    # The replacement body must be present
    assert "Clean replacement for cccc." in replaced, (
        "Replacement body for base cccc should be present"
    )
    # The old narrative text (both before and after the inner heading) must be gone
    assert "Narrative before inner heading." not in replaced, (
        "Old narrative text before inner heading should be removed on replace"
    )
    assert "## Inner heading that is narrative, not an entry" not in replaced, (
        "Inner '## ' heading line in old narrative body should be removed on replace"
    )
    assert "More narrative text after inner heading." not in replaced, (
        "Old narrative text after inner heading should be removed on replace"
    )
    # Other entries must survive intact
    assert "Content for section A." in replaced, "section_a should survive the cccc replacement"
    assert "Replaced content for section B2." in replaced, (
        "section_b2 should survive the cccc replacement"
    )
    # The replacement must appear exactly once (no phantom duplicate)
    assert replaced.count("Clean replacement for cccc.") == 1, (
        "Replacement body should appear exactly once — no phantom duplicates"
    )


def test_one_line_flattens_and_truncates():
    from trie.session_diff import _one_line

    # (1) multi-line text returns only the first non-empty line content
    assert _one_line("hello\nworld\nfoo") == "hello"

    # (2) whitespace runs collapse to single spaces
    assert _one_line("foo   bar\tbaz") == "foo bar baz"

    # (3) text with an early sentence boundary cuts at the sentence
    result = _one_line("Fix the bug. More details follow here.")
    assert result == "Fix the bug."

    # (4) a 400-char single sentence truncates to max_chars with trailing '…'
    long_text = "x" * 400
    result = _one_line(long_text)
    assert result.endswith("…")
    assert len(result) <= 200  # default max_chars

    # (5) result never contains a newline even for pathological inputs
    pathological = "\n\n# raw heading\ncode"
    result = _one_line(pathological)
    assert "\n" not in result
    assert result == "# raw heading"

    # (6) empty/whitespace-only input returns ''
    assert _one_line("") == ""
    assert _one_line("   \n\t\n  ") == ""


def test_collect_symbol_deltas_before_after(tmp_path):
    import shutil
    import subprocess as sp

    if not shutil.which("git"):
        if pytest is not None:
            pytest.skip("git not available")
        return

    from trie.config import Config
    from trie.session_diff import collect_symbol_deltas
    from trie.sync.writer import TriefactFile

    repo = tmp_path
    sp.run(["git", "init", "-q"], cwd=repo, check=True)
    sp.run(["git", "config", "user.email", "t@t"], cwd=repo, check=True)
    sp.run(["git", "config", "user.name", "t"], cwd=repo, check=True)

    triefacts_dir = repo / "triefacts"
    triefacts_dir.mkdir()
    mod_file = triefacts_dir / "mod.md"

    # Initial triefact with two sections, committed at HEAD
    tf = TriefactFile.empty()
    tf.upsert_section(qualified_name="m:f", fingerprint="fp-f1", body="Old meaning of f.")
    tf.upsert_section(qualified_name="m:g", fingerprint="fp-g1", body="Stable meaning of g.")
    mod_file.write_text(tf.render())

    sp.run(["git", "add", "-A"], cwd=repo, check=True, capture_output=True)
    sp.run(["git", "commit", "-q", "-m", "initial"], cwd=repo, check=True, capture_output=True)

    # Working tree: change f's meaning, leave g byte-identical, add h
    tf2 = TriefactFile.parse(mod_file.read_text())
    tf2.upsert_section(qualified_name="m:f", fingerprint="fp-f2", body="New meaning of f.")
    tf2.upsert_section(qualified_name="m:h", fingerprint="fp-h1", body="Brand new h.")
    mod_file.write_text(tf2.render())

    config = Config.from_dict({})
    deltas = collect_symbol_deltas(repo, config, base="HEAD")

    changed_f = [d for d in deltas if d.get("qname") == "m:f" and d.get("status") == "changed"]
    added_h = [d for d in deltas if d.get("qname") == "m:h" and d.get("status") == "added"]
    rows_g = [d for d in deltas if d.get("qname") == "m:g"]

    assert len(changed_f) == 1, f"Expected one 'changed' row for m:f, got: {deltas}"
    assert "Old meaning" in changed_f[0].get("before", "")
    assert "New meaning" in changed_f[0].get("after", "")
    assert len(added_h) == 1, f"Expected one 'added' row for m:h, got: {deltas}"
    assert rows_g == [], f"Expected no row for churn-gated m:g, got: {rows_g}"


def test_merge_applied_by_symbol_first_note_wins():
    from trie.session_diff import merge_applied_by_symbol

    entries = [
        {"qname": "m:x", "op": "create", "notes": ["Make x."]},
        {"qname": "m:x", "op": "modify", "notes": ["Fix bug in x."]},
        {"qname": "m:y", "op": "modify", "notes": ["Tweak y."]},
    ]

    result = merge_applied_by_symbol(entries)

    assert [row["qname"] for row in result] == ["m:x", "m:y"]

    x_row = result[0]
    assert x_row["op"] == "create"
    assert x_row["note"] == "Make x."
    assert x_row["followups"] == 1

    y_row = result[1]
    assert y_row["op"] == "modify"
    assert y_row["note"] == "Tweak y."
    assert y_row["followups"] == 0
