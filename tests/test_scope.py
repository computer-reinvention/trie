from __future__ import annotations

from pathlib import Path

from trie.config import Scope
from trie.scope import discover_files


def _touch(p: Path, content: str = "") -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content)


def test_basic_include(tmp_path: Path):
    _touch(tmp_path / "foo.py")
    _touch(tmp_path / "bar.txt")
    _touch(tmp_path / "src" / "deep.py")
    files = discover_files(tmp_path, Scope(include=["**/*.py"], exclude=[]))
    rel = sorted(p.relative_to(tmp_path).as_posix() for p in files)
    assert rel == ["foo.py", "src/deep.py"]


def test_exclude_directory(tmp_path: Path):
    _touch(tmp_path / "src" / "main.py")
    _touch(tmp_path / "tests" / "test_main.py")
    _touch(tmp_path / "tests" / "helpers" / "fixtures.py")
    files = discover_files(
        tmp_path,
        Scope(include=["**/*.py"], exclude=["**/tests/**"]),
    )
    rel = [p.relative_to(tmp_path).as_posix() for p in files]
    assert rel == ["src/main.py"]


def test_exclude_specific_file(tmp_path: Path):
    _touch(tmp_path / "a.py")
    _touch(tmp_path / "b.py")
    files = discover_files(
        tmp_path,
        Scope(include=["**/*.py"], exclude=["b.py"]),
    )
    rel = [p.relative_to(tmp_path).as_posix() for p in files]
    assert rel == ["a.py"]


def test_multiple_includes_unioned(tmp_path: Path):
    _touch(tmp_path / "a.py")
    _touch(tmp_path / "b.pyi")
    _touch(tmp_path / "c.txt")
    files = discover_files(
        tmp_path,
        Scope(include=["**/*.py", "**/*.pyi"], exclude=[]),
    )
    rel = sorted(p.relative_to(tmp_path).as_posix() for p in files)
    assert rel == ["a.py", "b.pyi"]


def test_default_excludes_skip_pycache_and_venv(tmp_path: Path):
    _touch(tmp_path / "src" / "main.py")
    _touch(tmp_path / "src" / "__pycache__" / "main.cpython-311.pyc")
    _touch(tmp_path / "src" / "__pycache__" / "main.py")  # someone wrote a .py here
    _touch(tmp_path / ".venv" / "lib" / "stuff.py")
    files = discover_files(tmp_path, Scope())  # default Scope has these excludes
    rel = sorted(p.relative_to(tmp_path).as_posix() for p in files)
    assert rel == ["src/main.py"]


def test_no_matches_returns_empty(tmp_path: Path):
    _touch(tmp_path / "README.md")
    files = discover_files(tmp_path, Scope(include=["**/*.py"], exclude=[]))
    assert files == []


def test_returns_sorted(tmp_path: Path):
    _touch(tmp_path / "z.py")
    _touch(tmp_path / "a.py")
    _touch(tmp_path / "m.py")
    files = discover_files(tmp_path, Scope(include=["**/*.py"], exclude=[]))
    rel = [p.relative_to(tmp_path).as_posix() for p in files]
    assert rel == sorted(rel)
