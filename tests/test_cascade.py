from __future__ import annotations

from pathlib import Path

import pytest

from trie.config import Config
from trie.graph.store import Store
from trie.scan import scan_project
from trie.sync.cascade import compute_cascade


@pytest.fixture
def project(tmp_path: Path) -> Path:
    (tmp_path / "trie.toml").write_text(
        '[trie]\nversion = "0.1.2"\n'
        '[scope]\ninclude = ["**/*.py"]\nexclude = ["**/__pycache__/**"]\n'
        '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
        '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
        'cascade = "anthropic/claude-sonnet-4-6"\n'
        "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
    )
    # lib.helper is the leaf
    (tmp_path / "lib.py").write_text("def helper():\n    return 1\n")
    # mid imports lib.helper and exposes mid.compute
    (tmp_path / "mid.py").write_text(
        "from lib import helper\n\n\ndef compute():\n    return helper() + 1\n"
    )
    # app imports mid.compute
    (tmp_path / "app.py").write_text(
        "from mid import compute\n\n\ndef main():\n    return compute()\n"
    )
    return tmp_path


def _store(project: Path) -> Store:
    config, _ = Config.find_and_load(project)
    s = Store(project / ".trie" / "graph.db")
    scan_project(project_root=project, config=config, store=s)
    return s


def test_cascade_returns_seed_when_empty(tmp_path: Path):
    s = Store(tmp_path / ".trie" / "graph.db")
    try:
        r = compute_cascade(changed_files=[], store=s)
        assert r.affected_files == []
    finally:
        s.close()


def test_cascade_includes_changed_files(project: Path):
    with _store(project) as s:
        r = compute_cascade(changed_files=["lib.py"], store=s)
        assert "lib.py" in r.affected_files


def test_cascade_depth_one_pulls_direct_callers(project: Path):
    """Editing lib.py should pull in mid.py (mid:compute calls lib:helper)."""
    with _store(project) as s:
        r = compute_cascade(changed_files=["lib.py"], store=s, depth=1)
        assert "mid.py" in r.affected_files
        assert "mid.py" in r.cascaded_from_change
        # depth=1 should NOT pull in app.py (it references mid.compute, not lib.helper)
        assert "app.py" not in r.affected_files


def test_cascade_depth_two_walks_two_hops(project: Path):
    """Depth 2 from lib.py: lib -> mid -> app."""
    with _store(project) as s:
        r = compute_cascade(changed_files=["lib.py"], store=s, depth=2)
        assert {"lib.py", "mid.py", "app.py"}.issubset(set(r.affected_files))


def test_cascade_depth_zero_only_returns_seed(project: Path):
    with _store(project) as s:
        r = compute_cascade(changed_files=["lib.py"], store=s, depth=0)
        assert r.affected_files == ["lib.py"]
        assert r.cascaded_from_change == set()


def test_cascade_hub_threshold_blocks_expansion(tmp_path: Path):
    (tmp_path / "trie.toml").write_text(
        '[trie]\nversion = "0.1.2"\n'
        '[scope]\ninclude = ["**/*.py"]\nexclude = ["**/__pycache__/**"]\n'
        '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
        '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
        'cascade = "anthropic/claude-sonnet-4-6"\n'
        "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
    )
    # `utils.utility` is referenced from many callers
    (tmp_path / "utils.py").write_text("def utility():\n    return 1\n")
    for i in range(5):
        (tmp_path / f"caller_{i}.py").write_text(
            f"from utils import utility\n\n\ndef call_{i}():\n    return utility()\n"
        )

    with _store(tmp_path) as s:
        # Permissive threshold: hub expands, all callers come along
        permissive = compute_cascade(
            changed_files=["utils.py"], store=s, depth=1, hub_threshold=100
        )
        assert len({f for f in permissive.affected_files if f.startswith("caller_")}) == 5

        # Strict threshold: hub does NOT expand
        strict = compute_cascade(changed_files=["utils.py"], store=s, depth=1, hub_threshold=2)
        # utils.py is still present (it's the seed) but no callers were pulled in.
        assert "utils.py" in strict.affected_files
        assert not any(f.startswith("caller_") for f in strict.affected_files)


def test_cascade_files_sorted(project: Path):
    with _store(project) as s:
        r = compute_cascade(changed_files=["lib.py"], store=s, depth=2)
        assert r.affected_files == sorted(r.affected_files)


def test_cascade_no_inbound_edges(tmp_path: Path):
    (tmp_path / "trie.toml").write_text(
        '[trie]\nversion = "0.1.2"\n'
        '[scope]\ninclude = ["**/*.py"]\nexclude = ["**/__pycache__/**"]\n'
        '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
        '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
        'cascade = "anthropic/claude-sonnet-4-6"\n'
        "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
    )
    (tmp_path / "isolated.py").write_text("def x():\n    return 1\n")
    with _store(tmp_path) as s:
        r = compute_cascade(changed_files=["isolated.py"], store=s)
        assert r.affected_files == ["isolated.py"]
        assert r.cascaded_from_change == set()
