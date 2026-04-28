from __future__ import annotations

from pathlib import Path

import pytest

from trie.config import Config
from trie.graph.store import Store
from trie.scan import scan_project


@pytest.fixture
def project(tmp_path: Path) -> Path:
    """A project root with a fresh trie.toml and stub source tree."""
    (tmp_path / "trie.toml").write_text(
        '[trie]\nversion = "0.1.0"\n'
        '[scope]\ninclude = ["**/*.py"]\nexclude = ["**/__pycache__/**"]\n'
        '[docs]\nroot = "docs"\nsource_root = "."\n'
        '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
        'cascade = "anthropic/claude-sonnet-4-6"\n'
        "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
    )
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "alpha.py").write_text("def alpha():\n    return 1\n")
    (tmp_path / "src" / "beta.py").write_text(
        "def beta_a():\n    pass\n\n\ndef beta_b():\n    pass\n"
    )
    return tmp_path


def _scan(project: Path) -> tuple[Store, object]:
    config, _ = Config.find_and_load(project)
    store = Store(project / ".trie" / "graph.db")
    result = scan_project(project_root=project, config=config, store=store)
    return store, result


def test_first_scan_marks_all_new(project: Path):
    store, result = _scan(project)
    try:
        assert result.files_total == 2
        assert result.files_new == 2
        assert result.files_updated == 0
        assert result.files_unchanged == 0
        assert result.symbols_total == 3  # alpha, beta_a, beta_b
        # All files have stored fingerprints + symbols
        files = {f.path for f in store.list_files()}
        assert files == {"src/alpha.py", "src/beta.py"}
    finally:
        store.close()


def test_rescan_unchanged_skips_parse(project: Path):
    s1, _ = _scan(project)
    s1.close()
    s2, result = _scan(project)
    try:
        assert result.files_unchanged == 2
        assert result.files_new == 0
        assert result.files_updated == 0
        assert result.symbols_total == 3
    finally:
        s2.close()


def test_modified_file_is_updated(project: Path):
    s1, _ = _scan(project)
    s1.close()

    (project / "src" / "alpha.py").write_text(
        "def alpha():\n    return 1\n\n\ndef alpha2():\n    return 2\n"
    )

    s2, result = _scan(project)
    try:
        assert result.files_updated == 1
        assert result.files_unchanged == 1
        assert result.files_new == 0
        assert s2.count_symbols(file_path="src/alpha.py") == 2
    finally:
        s2.close()


def test_added_file_is_new(project: Path):
    s1, _ = _scan(project)
    s1.close()

    (project / "src" / "gamma.py").write_text("def gamma():\n    pass\n")

    s2, result = _scan(project)
    try:
        assert result.files_new == 1
        assert result.files_unchanged == 2
        assert result.files_total == 3
    finally:
        s2.close()


def test_removed_file_is_cleaned_up(project: Path):
    s1, _ = _scan(project)
    s1.close()

    (project / "src" / "alpha.py").unlink()

    s2, result = _scan(project)
    try:
        assert result.files_removed == 1
        assert result.files_total == 1
        assert s2.get_file("src/alpha.py") is None
        assert s2.count_symbols(file_path="src/alpha.py") == 0
    finally:
        s2.close()


def test_excluded_file_treated_as_removed(project: Path):
    s1, _ = _scan(project)
    s1.close()

    # Tighten scope: now alpha.py is excluded
    (project / "trie.toml").write_text(
        '[trie]\nversion = "0.1.0"\n'
        '[scope]\ninclude = ["**/*.py"]\nexclude = ["src/alpha.py"]\n'
        '[docs]\nroot = "docs"\nsource_root = "."\n'
        '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
        'cascade = "anthropic/claude-sonnet-4-6"\n'
        "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
    )

    s2, result = _scan(project)
    try:
        assert result.files_removed == 1
        assert s2.get_file("src/alpha.py") is None
    finally:
        s2.close()
