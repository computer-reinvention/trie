"""Spec for `trie gate` — the commit guard as one command.

The hook body delegates here, and hook-less environments (CI runners) call it
explicitly, so the guard must behave identically in both worlds.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

from typer.testing import CliRunner

from trie.cli import app

runner = CliRunner()


def _repo(tmp_path: Path) -> Path:
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.email", "t@t"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.name", "t"], cwd=tmp_path, check=True)
    (tmp_path / "trie.toml").write_text('[trie]\nversion = "0.0.0"\n[diff]\nnarrative = false\n')
    return tmp_path


def test_gate_noop_without_config(tmp_path: Path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    result = runner.invoke(app, ["gate"])
    assert result.exit_code == 0
    assert "nothing to gate" in result.output


def _synced_repo(tmp_path: Path) -> Path:
    """Repo with one committed module and a *coherent* triefact for it."""
    from trie.parse.python import extract_symbols
    from trie.sync.writer import TriefactFile

    repo = _repo(tmp_path)
    src = repo / "m.py"
    src.write_text("def f():\n    return 1\n")

    [sym] = [s for s in extract_symbols(src, repo) if s.name == "f"]
    tf = TriefactFile.empty()
    tf.upsert_section(
        qualified_name=sym.qualified_name,
        fingerprint=sym.body_normalized_hash,
        body="Returns one.",
    )
    (repo / "triefacts").mkdir()
    (repo / "triefacts" / "m.md").write_text(tf.render())

    subprocess.run(["git", "add", "-A"], cwd=repo, check=True, capture_output=True)
    subprocess.run(["git", "commit", "-q", "-m", "init"], cwd=repo, check=True, capture_output=True)
    return repo


def test_gate_blocks_unsynced_source(tmp_path: Path, monkeypatch):
    """A source file with no triefact fails verify — the gate teaches the fix."""
    repo = _repo(tmp_path)
    (repo / "m.py").write_text("def f():\n    return 1\n")
    monkeypatch.chdir(repo)
    result = runner.invoke(app, ["gate", "--no-digest"])
    assert result.exit_code == 1
    assert "trie sync" in result.output


def test_gate_passes_clean_then_blocks_unexplained_change(tmp_path: Path, monkeypatch):
    repo = _synced_repo(tmp_path)
    monkeypatch.chdir(repo)

    # Coherent prose, no changes, nothing to digest -> exit 0.
    result = runner.invoke(app, ["gate"])
    assert result.exit_code == 0, result.output

    # Change the symbol without recording intent. Verify would also fire (the
    # prose is now stale), so regenerate the triefact fingerprint to isolate
    # the intent gate: the change must block with the fix instructions.
    src = repo / "m.py"
    src.write_text("def f():\n    return 42\n")
    from trie.parse.python import extract_symbols
    from trie.sync.writer import TriefactFile

    [sym] = [s for s in extract_symbols(src, repo) if s.name == "f"]
    tf = TriefactFile.parse((repo / "triefacts" / "m.md").read_text())
    tf.upsert_section(
        qualified_name=sym.qualified_name,
        fingerprint=sym.body_normalized_hash,
        body="Returns forty-two.",
    )
    (repo / "triefacts" / "m.md").write_text(tf.render())

    result = runner.invoke(app, ["gate", "--no-digest"])
    assert result.exit_code == 1
    assert "m:f" in result.output
    assert "trie patch create" in result.output

    # Record the note: the gate opens.
    result = runner.invoke(app, ["patch", "create", "m:f", "-n", "f returns 42 now"])
    # patch requires the symbol in the graph; build it via refresh-equivalent scan.
    if result.exit_code != 0:
        from trie.config import Config
        from trie.graph.store import Store
        from trie.scan import scan_project

        config, _ = Config.find_and_load(repo)
        with Store(repo / ".trie" / "graph.db") as store:
            scan_project(project_root=repo, config=config, store=store)
        result = runner.invoke(app, ["patch", "create", "m:f", "-n", "f returns 42 now"])
        assert result.exit_code == 0, result.output

    result = runner.invoke(app, ["gate", "--no-digest"])
    assert result.exit_code == 0, result.output


def test_gate_exits_2_when_writer_holds_the_lock(tmp_path: Path, monkeypatch):
    """Same-process flock re-acquire can succeed (platform-dependent), so the
    contended state is simulated at the API boundary."""
    import contextlib

    import trie.refresh_lock as refresh_lock

    repo = _repo(tmp_path)
    monkeypatch.chdir(repo)

    class _Contended:
        acquired = False

    @contextlib.contextmanager
    def fake_try_acquire(root, name=""):
        yield _Contended()

    monkeypatch.setattr(refresh_lock, "try_acquire", fake_try_acquire)
    result = runner.invoke(app, ["gate"])
    assert result.exit_code == 2
    assert "retry" in result.output.lower()


def test_gate_warns_on_self_hosting_version_skew(tmp_path: Path, monkeypatch):
    """When the project IS the trie source repo at a different version than the
    running binary, the gate warns loudly — a stale global install once shipped
    a commit whose digest was written by the previous release."""
    repo = _synced_repo(tmp_path)
    (repo / "pyproject.toml").write_text(
        '[project]\nname = "trie"\nversion = "999.0.0"\n',
    )
    monkeypatch.chdir(repo)
    result = runner.invoke(app, ["gate", "--no-digest"])
    flat = " ".join(result.output.split())
    assert "999.0.0" in flat
    assert "uv tool install --force" in flat


def test_gate_no_skew_warning_for_other_projects(tmp_path: Path, monkeypatch):
    """A non-trie project with its own pyproject must never see the warning."""
    repo = _synced_repo(tmp_path)
    (repo / "pyproject.toml").write_text(
        '[project]\nname = "someapp"\nversion = "999.0.0"\n',
    )
    monkeypatch.chdir(repo)
    result = runner.invoke(app, ["gate", "--no-digest"])
    assert "uv tool install --force" not in " ".join(result.output.split())


def test_patch_create_suggests_close_qnames_on_miss(tmp_path: Path, monkeypatch):
    """A guessed/hand-built qname gets did-you-mean candidates, not just the
    misleading --gone hint (which is for genuinely removed symbols)."""
    import subprocess as sp

    from trie.graph.store import Store
    from trie.parse.python import extract_symbols

    repo = _repo(tmp_path)
    src = repo / "pkg_init.py"
    src.write_text('__version__ = "1.0"\n')
    sp.run(["git", "add", "-A"], cwd=repo, check=True, capture_output=True)
    sp.run(["git", "commit", "-q", "-m", "init"], cwd=repo, check=True, capture_output=True)

    db = repo / ".trie" / "graph.db"
    db.parent.mkdir(exist_ok=True)
    with Store(db) as store:
        store.upsert_file(path="pkg_init.py", fingerprint="fp")
        store.replace_file_symbols("pkg_init.py", extract_symbols(src, repo))

    monkeypatch.chdir(repo)
    result = runner.invoke(app, ["patch", "create", "pkg_init:__module__", "-n", "bump"])
    flat = " ".join(result.output.split())
    assert result.exit_code == 1
    assert "did you mean" in flat
    assert "pkg_init:__version__" in flat
    # --gone is mentioned as the removal escape hatch, not the headline fix.
    assert "--gone" in flat
