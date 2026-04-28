from __future__ import annotations

from pathlib import Path

from trie.config import Config
from trie.sync.reconcile import find_orphan_docs, remove_orphan_docs


def _setup(tmp_path: Path) -> Path:
    (tmp_path / "trie.toml").write_text(
        '[trie]\nversion = "0.1.0"\n'
        '[scope]\ninclude = ["**/*.py"]\nexclude = ["**/__pycache__/**"]\n'
        '[docs]\nroot = "docs"\nsource_root = "."\n'
        '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
        'cascade = "anthropic/claude-sonnet-4-6"\n'
        "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
    )
    return tmp_path


def test_no_orphans_when_sources_exist(tmp_path: Path):
    project = _setup(tmp_path)
    (project / "lib.py").write_text("def x():\n    pass\n")
    (project / "docs").mkdir()
    (project / "docs" / "lib.md").write_text(
        "---\ntrie_version: 0.1.0\nsource: lib.py\nfile_fingerprint: abc\n---\nbody\n"
    )
    config, _ = Config.find_and_load(project)
    assert find_orphan_docs(project_root=project, config=config) == []


def test_orphan_when_source_deleted(tmp_path: Path):
    project = _setup(tmp_path)
    (project / "docs").mkdir()
    (project / "docs" / "removed.md").write_text(
        "---\ntrie_version: 0.1.0\nsource: removed.py\nfile_fingerprint: abc\n---\nbody\n"
    )
    config, _ = Config.find_and_load(project)
    orphans = find_orphan_docs(project_root=project, config=config)
    assert len(orphans) == 1
    assert orphans[0].name == "removed.md"


def test_user_authored_doc_left_alone(tmp_path: Path):
    project = _setup(tmp_path)
    (project / "docs").mkdir()
    # No trie_version front-matter — this is user-owned
    (project / "docs" / "architecture.md").write_text("# Architecture\n\nHand-written.\n")
    config, _ = Config.find_and_load(project)
    assert find_orphan_docs(project_root=project, config=config) == []


def test_remove_actually_deletes(tmp_path: Path):
    project = _setup(tmp_path)
    (project / "docs").mkdir()
    doc = project / "docs" / "removed.md"
    doc.write_text(
        "---\ntrie_version: 0.1.0\nsource: removed.py\nfile_fingerprint: abc\n---\nbody\n"
    )
    config, _ = Config.find_and_load(project)
    removed = remove_orphan_docs(project_root=project, config=config)
    assert len(removed) == 1
    assert not doc.exists()


def test_no_docs_dir_returns_empty(tmp_path: Path):
    project = _setup(tmp_path)
    config, _ = Config.find_and_load(project)
    assert find_orphan_docs(project_root=project, config=config) == []


def test_excluded_source_treated_as_orphan(tmp_path: Path):
    """If a source is excluded by scope, its doc becomes orphan."""
    project = _setup(tmp_path)
    (project / "lib.py").write_text("def x():\n    pass\n")
    (project / "docs").mkdir()
    (project / "docs" / "lib.md").write_text(
        "---\ntrie_version: 0.1.0\nsource: lib.py\nfile_fingerprint: abc\n---\nbody\n"
    )
    # Tighten scope to exclude lib.py
    (project / "trie.toml").write_text(
        '[trie]\nversion = "0.1.0"\n'
        '[scope]\ninclude = ["**/*.py"]\nexclude = ["lib.py"]\n'
        '[docs]\nroot = "docs"\nsource_root = "."\n'
        '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
        'cascade = "anthropic/claude-sonnet-4-6"\n'
        "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
    )
    config, _ = Config.find_and_load(project)
    orphans = find_orphan_docs(project_root=project, config=config)
    assert len(orphans) == 1
