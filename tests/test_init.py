from __future__ import annotations

from pathlib import Path

import pytest
from typer.testing import CliRunner

from trie.cli import app
from trie.init import (
    GITIGNORE_LINE,
    PRE_COMMIT_HOOK_MARKER,
    InitError,
    _detect_python_project,
    _ensure_gitignore_entry,
    init_project,
    install_pre_commit_hook,
)


@pytest.fixture
def python_project(tmp_path: Path) -> Path:
    (tmp_path / "pyproject.toml").write_text("[project]\nname = 'demo'\n")
    return tmp_path


@pytest.fixture
def empty_dir(tmp_path: Path) -> Path:
    return tmp_path


# --- detection ---


def test_detect_pyproject(python_project: Path):
    assert _detect_python_project(python_project) == ["pyproject.toml"]


def test_detect_loose_py_files(empty_dir: Path):
    (empty_dir / "thing.py").write_text("x = 1\n")
    assert _detect_python_project(empty_dir) == ["*.py files"]


def test_detect_one_level_deep_py_files(empty_dir: Path):
    (empty_dir / "src").mkdir()
    (empty_dir / "src" / "thing.py").write_text("x = 1\n")
    assert _detect_python_project(empty_dir) == ["*.py files"]


def test_detect_returns_empty_for_non_python(empty_dir: Path):
    (empty_dir / "README.md").write_text("# hi")
    assert _detect_python_project(empty_dir) == []


# --- gitignore handling ---


def test_gitignore_creates_when_missing(empty_dir: Path):
    gi = empty_dir / ".gitignore"
    assert _ensure_gitignore_entry(gi, GITIGNORE_LINE) is True
    assert gi.read_text() == ".trie/\n"


def test_gitignore_appends_when_missing_line(empty_dir: Path):
    gi = empty_dir / ".gitignore"
    gi.write_text("__pycache__/\n")
    assert _ensure_gitignore_entry(gi, GITIGNORE_LINE) is True
    assert ".trie/" in gi.read_text().splitlines()


def test_gitignore_no_dup_when_already_present(empty_dir: Path):
    gi = empty_dir / ".gitignore"
    gi.write_text(".trie/\n")
    assert _ensure_gitignore_entry(gi, GITIGNORE_LINE) is False
    assert gi.read_text().count(".trie/") == 1


def test_gitignore_treats_trailing_slash_as_match(empty_dir: Path):
    gi = empty_dir / ".gitignore"
    gi.write_text(".trie\n")  # without trailing slash
    assert _ensure_gitignore_entry(gi, GITIGNORE_LINE) is False


def test_gitignore_handles_no_trailing_newline(empty_dir: Path):
    gi = empty_dir / ".gitignore"
    gi.write_text("__pycache__/")  # no trailing newline
    assert _ensure_gitignore_entry(gi, GITIGNORE_LINE) is True
    text = gi.read_text()
    assert text.endswith(".trie/\n")
    assert "__pycache__/" in text


# --- init_project ---


def test_init_happy_path(python_project: Path):
    result = init_project(python_project)
    assert result.config_written is True
    assert (python_project / "trie.toml").exists()
    assert (python_project / ".gitignore").exists()
    assert ".trie/" in (python_project / ".gitignore").read_text()
    assert "pyproject.toml" in result.detected_markers


def test_init_errors_on_non_python_without_force(empty_dir: Path):
    (empty_dir / "README.md").write_text("# hi")
    with pytest.raises(InitError, match="does not look like a Python project"):
        init_project(empty_dir)


def test_init_force_overrides_detection(empty_dir: Path):
    (empty_dir / "README.md").write_text("# hi")
    result = init_project(empty_dir, force=True)
    assert result.config_written is True


def test_init_refuses_overwrite(python_project: Path):
    init_project(python_project)
    with pytest.raises(InitError, match="already exists"):
        init_project(python_project)


def test_init_force_overwrites(python_project: Path):
    init_project(python_project)
    (python_project / "trie.toml").write_text("# tampered\n")
    init_project(python_project, force=True)
    assert "[trie]" in (python_project / "trie.toml").read_text()


# --- CLI ---


def test_cli_init_runs(python_project: Path):
    runner = CliRunner()
    result = runner.invoke(app, ["init", str(python_project)])
    assert result.exit_code == 0, result.output
    assert "wrote" in result.output
    assert (python_project / "trie.toml").exists()


def test_cli_init_errors_on_existing(python_project: Path):
    init_project(python_project)
    runner = CliRunner()
    result = runner.invoke(app, ["init", str(python_project)])
    assert result.exit_code == 1
    assert "already exists" in result.output


def test_cli_init_force_succeeds(python_project: Path):
    init_project(python_project)
    runner = CliRunner()
    result = runner.invoke(app, ["init", str(python_project), "--force"])
    assert result.exit_code == 0


# --- scan-after-init ---


def test_init_runs_scan_by_default(python_project: Path):
    (python_project / "thing.py").write_text("def hello():\n    return 1\n")
    result = init_project(python_project)
    assert result.scan_ran is True
    assert result.scan_files_total == 1
    assert result.scan_symbols_total >= 1
    assert (python_project / ".trie" / "graph.db").exists()


def test_init_no_scan_skips_graph_db(python_project: Path):
    (python_project / "thing.py").write_text("def hello():\n    return 1\n")
    result = init_project(python_project, run_scan=False)
    assert result.scan_ran is False
    assert not (python_project / ".trie" / "graph.db").exists()


# --- pre-commit hook installer ---


def test_install_hook_writes_new_pre_commit_when_git_repo(python_project: Path):
    (python_project / ".git").mkdir()
    installed, strategy, hook_path = install_pre_commit_hook(python_project)
    assert installed is True
    assert strategy == "git_hook"
    assert hook_path is not None
    text = hook_path.read_text()
    assert PRE_COMMIT_HOOK_MARKER in text
    # The hook runs lock-check before verify so a commit during a refresh/sync
    # fails fast with a clear message rather than racing the writer.
    assert "trie -q lock-check" in text
    assert "trie -q verify" in text
    # Order matters: lock-check must precede verify so the commit fails on
    # contention before spending cycles on the offline drift check.
    assert text.index("trie -q lock-check") < text.index("trie -q verify")
    # Must be executable.
    import stat

    assert hook_path.stat().st_mode & stat.S_IXUSR


def test_install_hook_appends_to_existing_pre_commit(python_project: Path):
    (python_project / ".git").mkdir()
    hooks = python_project / ".git" / "hooks"
    hooks.mkdir()
    existing = hooks / "pre-commit"
    existing.write_text("#!/bin/sh\necho running existing\n")
    installed, strategy, hook_path = install_pre_commit_hook(python_project)
    assert installed is True
    assert strategy == "git_hook"
    text = hook_path.read_text()
    assert "echo running existing" in text  # preserved
    assert PRE_COMMIT_HOOK_MARKER in text  # appended


def test_install_hook_idempotent(python_project: Path):
    (python_project / ".git").mkdir()
    install_pre_commit_hook(python_project)
    installed, strategy, _ = install_pre_commit_hook(python_project)
    assert installed is False
    assert strategy == "git_hook"


def test_install_hook_skips_when_pre_commit_framework_present(python_project: Path):
    (python_project / ".git").mkdir()
    (python_project / ".pre-commit-config.yaml").write_text("repos: []\n")
    installed, strategy, hook_path = install_pre_commit_hook(python_project)
    assert installed is False
    assert strategy == "framework"
    assert hook_path is None


def test_install_hook_skips_when_not_a_git_repo(python_project: Path):
    installed, strategy, hook_path = install_pre_commit_hook(python_project)
    assert installed is False
    assert strategy == "none"
    assert hook_path is None


# --- init_project hook integration ---


def test_init_project_install_hooks_in_git_repo(python_project: Path):
    (python_project / ".git").mkdir()
    result = init_project(python_project, install_hooks=True)
    assert result.pre_commit_installed is True
    assert result.pre_commit_strategy == "git_hook"
    assert (python_project / ".git" / "hooks" / "pre-commit").exists()


def test_init_project_default_does_not_install_hooks(python_project: Path):
    (python_project / ".git").mkdir()
    result = init_project(python_project)
    assert result.pre_commit_installed is False
    assert result.pre_commit_strategy == "skipped"


# --- CLI --install-hooks plumbing ---


def test_cli_init_install_hooks_flag_in_git_repo(python_project: Path):
    (python_project / ".git").mkdir()
    runner = CliRunner()
    result = runner.invoke(app, ["init", str(python_project), "--install-hooks"])
    assert result.exit_code == 0, result.output
    assert "installed pre-commit hook" in result.output
    assert (python_project / ".git" / "hooks" / "pre-commit").exists()


def test_cli_init_no_install_hooks_flag_skips(python_project: Path):
    (python_project / ".git").mkdir()
    runner = CliRunner()
    result = runner.invoke(app, ["init", str(python_project), "--no-install-hooks"])
    assert result.exit_code == 0, result.output
    assert not (python_project / ".git" / "hooks" / "pre-commit").exists()


def test_cli_init_framework_path_prints_snippet(python_project: Path):
    (python_project / ".git").mkdir()
    (python_project / ".pre-commit-config.yaml").write_text("repos: []\n")
    runner = CliRunner()
    result = runner.invoke(app, ["init", str(python_project), "--install-hooks"])
    assert result.exit_code == 0, result.output
    assert "trie-verify" in result.output
    assert ".pre-commit-config.yaml" in result.output


def test_cli_init_non_interactive_skips_prompt(python_project: Path):
    """CliRunner is non-interactive; without --install-hooks the prompt must not block."""
    runner = CliRunner()
    result = runner.invoke(app, ["init", str(python_project)])
    assert result.exit_code == 0, result.output


def test_cli_init_prints_scan_summary(python_project: Path):
    (python_project / "thing.py").write_text("def hello():\n    return 1\n")
    runner = CliRunner()
    result = runner.invoke(app, ["init", str(python_project)])
    assert result.exit_code == 0, result.output
    assert "scanned" in result.output
    assert "symbols" in result.output
