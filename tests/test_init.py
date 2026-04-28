from __future__ import annotations

from pathlib import Path

import pytest
from typer.testing import CliRunner

from trie.cli import app
from trie.init import (
    GITIGNORE_LINE,
    InitError,
    _detect_python_project,
    _ensure_gitignore_entry,
    init_project,
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
