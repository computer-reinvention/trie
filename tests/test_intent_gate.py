from __future__ import annotations

import subprocess
from pathlib import Path

from trie.config import Config
from trie.graph.store import Store
from trie.intent_gate import evaluate, touched_symbols
from trie.parse.python import extract_symbols


def _repo(tmp_path: Path) -> tuple[Config, Path]:
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.email", "t@t"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.name", "t"], cwd=tmp_path, check=True)
    (tmp_path / "trie.toml").write_text("[trie]\nversion = '0.0.0'\n")
    (tmp_path / "mod.py").write_text(
        "import os\n\n\ndef alpha():\n    return 1\n\n\ndef beta():\n    return 2\n"
    )
    subprocess.run(["git", "add", "-A"], cwd=tmp_path, check=True, capture_output=True)
    subprocess.run(
        ["git", "commit", "-q", "-m", "init"], cwd=tmp_path, check=True, capture_output=True
    )
    return Config.from_dict({}), tmp_path


def test_touched_symbols_semantic_changes_only(tmp_path: Path) -> None:
    config, repo = _repo(tmp_path)

    # Formatting-only change: same normalized body, must not gate.
    (repo / "mod.py").write_text(
        "import os\n\n\ndef alpha():\n    return 1\n\n\ndef beta():\n\n    return 2\n"
    )
    assert touched_symbols(repo, config) == []

    # Real change to alpha; beta untouched; gamma added; module imports shuffled.
    (repo / "mod.py").write_text(
        "import sys\n\n\ndef alpha():\n    return 42\n\n\ndef beta():\n    return 2\n\n\ndef gamma():\n    return 3\n"
    )
    touched = touched_symbols(repo, config)
    by_qname = {t.qname: t.status for t in touched}
    assert by_qname == {"mod:alpha": "modified", "mod:gamma": "added"}
    # __module__ (import shuffle) exempt; beta exempt.
    assert not any(t.qname.endswith(":__module__") for t in touched)


def test_touched_symbols_sees_untracked_files_and_removals(tmp_path: Path) -> None:
    config, repo = _repo(tmp_path)

    # Brand-new untracked module must gate (git diff HEAD alone misses it).
    (repo / "fresh.py").write_text("def newcomer():\n    return True\n")
    # Remove beta from the tracked module.
    (repo / "mod.py").write_text("import os\n\n\ndef alpha():\n    return 1\n")

    by_qname = {t.qname: t.status for t in touched_symbols(repo, config)}
    assert by_qname["fresh:newcomer"] == "added"
    assert by_qname["mod:beta"] == "removed"


def test_evaluate_coverage_from_pending_and_session_log(tmp_path: Path) -> None:
    config, repo = _repo(tmp_path)
    (repo / "mod.py").write_text(
        "import os\n\n\ndef alpha():\n    return 42\n\n\ndef beta():\n    return 99\n"
    )

    db = repo / ".trie" / "graph.db"
    db.parent.mkdir(exist_ok=True)
    store = Store(db)
    try:
        store.upsert_file(path="mod.py", fingerprint="fp")
        store.replace_file_symbols("mod.py", extract_symbols(repo / "mod.py", repo))

        # Nothing covered yet: both symbols uncovered.
        report = evaluate(repo, config, store)
        assert {t.qname for t in report.uncovered} == {"mod:alpha", "mod:beta"}
        assert not report.ok

        # Pending patch note covers alpha.
        store.add_patch("mod:alpha", note="alpha does 42 now", reason="", session_id="s1")
        report = evaluate(repo, config, store)
        assert {t.qname for t in report.uncovered} == {"mod:beta"}

        # A sealed (applied) row covers beta the same as a staged one.
        store.add_patch("mod:beta", "beta 99", "", "s1")
        store.mark_patches_applied("session")
        report = evaluate(repo, config, store)
        assert report.ok, f"expected full coverage, got {report.uncovered}"
    finally:
        store.close()


def test_class_note_covers_its_methods(tmp_path: Path) -> None:
    """A note on `mod:Klass` covers `mod:Klass.method` — intent describing a
    class naturally describes its methods, and demanding one note per method
    failed commits whose intent was already on record."""
    config, repo = _repo(tmp_path)
    (repo / "mod.py").write_text(
        "import os\n\n\ndef alpha():\n    return 1\n\n\ndef beta():\n    return 2\n\n\n"
        "class Klass:\n    def method_a(self):\n        return 'a'\n\n"
        "    def method_b(self):\n        return 'b'\n"
    )

    db = repo / ".trie" / "graph.db"
    db.parent.mkdir(exist_ok=True)
    store = Store(db)
    try:
        store.upsert_file(path="mod.py", fingerprint="fp")
        store.replace_file_symbols("mod.py", extract_symbols(repo / "mod.py", repo))

        # Uncovered: the class and both methods (alpha/beta unchanged).
        report = evaluate(repo, config, store)
        uncovered = {t.qname for t in report.uncovered}
        assert "mod:Klass" in uncovered
        assert "mod:Klass.method_a" in uncovered

        # One note on the class covers the class AND its methods.
        store.add_patch("mod:Klass", note="new Klass with a/b methods", reason="", session_id="s1")
        report = evaluate(repo, config, store)
        assert report.ok, f"expected class note to cover methods, got {report.uncovered}"

        # A method note alone does NOT cover the sibling or the class.
        store2_path = repo / ".trie" / "graph2.db"
        with Store(store2_path) as store2:
            store2.upsert_file(path="mod.py", fingerprint="fp")
            store2.replace_file_symbols("mod.py", extract_symbols(repo / "mod.py", repo))
            store2.add_patch("mod:Klass.method_a", note="only a", reason="", session_id="s1")
            report2 = evaluate(repo, config, store2)
            uncovered2 = {t.qname for t in report2.uncovered}
            assert "mod:Klass" in uncovered2
            assert "mod:Klass.method_b" in uncovered2
            assert "mod:Klass.method_a" not in uncovered2
    finally:
        store.close()


def test_record_intent_reports_uncovered_symbols(tmp_path: Path) -> None:
    """Apply-time coverage feedback: sealing notes reports the touched symbols
    that still lack notes, so the agent learns before the commit gate fails."""
    from trie.edits.pipeline import record_intent

    config, repo = _repo(tmp_path)
    (repo / "mod.py").write_text(
        "import os\n\n\ndef alpha():\n    return 42\n\n\ndef beta():\n    return 99\n"
    )

    db = repo / ".trie" / "graph.db"
    db.parent.mkdir(exist_ok=True)
    store = Store(db)
    try:
        store.upsert_file(path="mod.py", fingerprint="fp")
        store.replace_file_symbols("mod.py", extract_symbols(repo / "mod.py", repo))

        store.add_patch("mod:alpha", note="alpha does 42 now", reason="", session_id="s1")
        envelope = record_intent(store, config, repo, session_note="")
        assert envelope["ok"]
        assert envelope["uncovered"] == ["mod:beta"]
        assert "would fail the commit gate" in envelope["next"]

        # Cover beta too: the next apply reports full coverage.
        store.add_patch("mod:beta", note="beta 99", reason="", session_id="s1")
        envelope2 = record_intent(store, config, repo, session_note="")
        assert envelope2["ok"]
        assert envelope2["uncovered"] == []
    finally:
        store.close()


def test_gate_is_silent_outside_git(tmp_path: Path) -> None:
    (tmp_path / "trie.toml").write_text("[trie]\nversion = '0.0.0'\n")
    (tmp_path / "mod.py").write_text("def f():\n    return 1\n")
    config = Config.from_dict({})
    assert touched_symbols(tmp_path, config) == []


def test_record_intent_empty_queue_still_reports_uncovered(tmp_path: Path) -> None:
    """The lazy-but-correct flow must work from zero: edit → patch_apply (with
    nothing staged) → read the uncovered worklist. An empty queue used to
    early-return without coverage info, hiding the worklist until commit time."""
    from trie.edits.pipeline import record_intent

    config, repo = _repo(tmp_path)
    (repo / "mod.py").write_text(
        "import os\n\n\ndef alpha():\n    return 42\n\n\ndef beta():\n    return 2\n"
    )

    db = repo / ".trie" / "graph.db"
    db.parent.mkdir(exist_ok=True)
    store = Store(db)
    try:
        store.upsert_file(path="mod.py", fingerprint="fp")
        store.replace_file_symbols("mod.py", extract_symbols(repo / "mod.py", repo))

        envelope = record_intent(store, config, repo, session_note="")
        assert envelope["ok"]
        assert envelope["recorded"] == 0
        assert envelope["uncovered"] == ["mod:alpha"]
        assert "stage a patch note" in envelope["next"]
    finally:
        store.close()
