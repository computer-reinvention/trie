from __future__ import annotations

from pathlib import Path

import pytest

from trie.config import Config
from trie.graph.store import Store
from trie.graph.system_model import (
    build_system_model,
    build_system_model_cached,
    system_model_to_dict,
)
from trie.scan import scan_project


@pytest.fixture
def project(tmp_path: Path) -> Path:
    """A small project exercising every skeleton class.

    - `main` is a Typer command (decorator) + pyproject script -> door
    - `run_external` reaches out via subprocess (boundary='exit') -> exit
    - `core` / `helper` are plain internal functions
    - `CONFIG` is referenced by nothing and references nothing -> orphan
    - a tests/ file exercises test exclusion
    """
    (tmp_path / "pyproject.toml").write_text(
        '[project]\nname = "demo"\n[project.scripts]\ndemo = "app:main"\n'
    )
    (tmp_path / "trie.toml").write_text('[triefacts]\nroot = "triefacts"\nsource_root = "."\n')
    (tmp_path / "app.py").write_text(
        "import subprocess\n"
        "import typer\n"
        "\n"
        "CONFIG = {}\n"
        "\n"
        "app = typer.Typer()\n"
        "\n"
        "def helper(x):\n"
        "    return x + 1\n"
        "\n"
        "def core(x):\n"
        "    return helper(x) * 2\n"
        "\n"
        "def run_external():\n"
        '    subprocess.run(["ls"])\n'
        "\n"
        "@app.command()\n"
        "def main():\n"
        "    core(1)\n"
        "    run_external()\n"
    )
    tests_dir = tmp_path / "tests"
    tests_dir.mkdir()
    (tests_dir / "test_app.py").write_text(
        "from app import core\n\n\ndef test_core():\n    assert core(1) == 4\n"
    )
    return tmp_path


def _scanned_store(project: Path) -> Store:
    config, _ = Config.find_and_load(project)
    store = Store(project / ".trie" / "graph.db")
    scan_project(project_root=project, config=config, store=store)
    return store


def _tag(store: Store, qname: str, *, role: str = "", boundary: str = "internal") -> None:
    sid = store._conn.execute(
        "SELECT id FROM symbols WHERE qualified_name = ?", (qname,)
    ).fetchone()[0]
    store._conn.execute(
        "INSERT INTO triefact_sections "
        "(triefact_path, symbol_id, section_fingerprint, one_liner, role, boundary, last_generated_at) "
        "VALUES (?, ?, ?, ?, ?, ?, ?)",
        ("t.md", sid, "fp", "", role, boundary, 0),
    )
    store._conn.commit()


def test_decorator_marks_door(project: Path):
    store = _scanned_store(project)
    model = build_system_model(store, project_root=project)
    by_q = {n.qname: n for n in model.nodes}
    assert by_q["app:main"].cls == "door"
    store.close()


def test_pyproject_scripts_recognized(project: Path):
    store = _scanned_store(project)
    model = build_system_model(store, project_root=project)
    assert "app:main" in {n.qname for n in model.nodes if n.cls == "door"}
    store.close()


def test_exit_boundary_classifies_exit(project: Path):
    store = _scanned_store(project)
    _tag(store, "app:run_external", role="io", boundary="exit")
    model = build_system_model(store, project_root=project)
    by_q = {n.qname: n for n in model.nodes}
    assert by_q["app:run_external"].cls == "exit"
    store.close()


def test_depth_propagates_from_doors(project: Path):
    store = _scanned_store(project)
    model = build_system_model(store, project_root=project)
    by_q = {n.qname: n for n in model.nodes}
    assert by_q["app:main"].depth == 0
    assert by_q["app:core"].depth == 1
    assert by_q["app:helper"].depth == 2
    store.close()


def test_orphan_detection(project: Path):
    store = _scanned_store(project)
    model = build_system_model(store, project_root=project)
    by_q = {n.qname: n for n in model.nodes}
    assert by_q["app:CONFIG"].cls == "orphan"
    store.close()


def test_salience_orders_doors_above_helpers(project: Path):
    store = _scanned_store(project)
    model = build_system_model(store, project_root=project)
    by_q = {n.qname: n for n in model.nodes}
    assert by_q["app:main"].salience > by_q["app:helper"].salience
    store.close()


def test_tests_excluded_by_default(project: Path):
    store = _scanned_store(project)
    model = build_system_model(store, project_root=project)
    prod_qnames = {n.qname for n in model.nodes}
    # the test function is not in the production node set
    assert not any(q.startswith("tests/") for q in prod_qnames)
    # but it is captured separately, flagged
    test_qnames = {n.qname for n in model.test_nodes}
    assert any("test_core" in q for q in test_qnames)
    assert all(n.cls == "test" and n.is_test for n in model.test_nodes)
    store.close()


def test_tests_do_not_pollute_door_classification(project: Path):
    # test_core has no production caller and calls core -> would be a false door
    # if tests weren't excluded. Confirm it never appears as a door.
    store = _scanned_store(project)
    model = build_system_model(store, project_root=project)
    assert not any(n.cls == "door" for n in model.test_nodes)
    store.close()


def test_module_nodes_dropped(project: Path):
    store = _scanned_store(project)
    model = build_system_model(store, project_root=project)
    assert not any(n.kind == "module" for n in model.nodes)
    store.close()


def test_blind_spot_method_not_orphan(tmp_path: Path):
    # A method with no resolved edges whose class IS connected = dynamic-dispatch
    # blind spot, classified 'internal', never 'orphan'.
    (tmp_path / "trie.toml").write_text('[triefacts]\nroot = "triefacts"\nsource_root = "."\n')
    (tmp_path / "m.py").write_text(
        "class Repo:\n"
        "    def save(self):\n"
        "        return self._helper()\n"
        "    def _helper(self):\n"
        "        return 1\n"
        "    def unwired(self):\n"  # called only via getattr-style dispatch in real code
        "        return 2\n"
        "\n"
        "def build():\n"
        "    return Repo()\n"
    )
    config, _ = Config.find_and_load(tmp_path)
    store = Store(tmp_path / ".trie" / "graph.db")
    scan_project(project_root=tmp_path, config=config, store=store)
    model = build_system_model(store, project_root=tmp_path)
    by_q = {n.qname: n for n in model.nodes}
    # Repo is connected (build() -> Repo, save -> _helper). 'unwired' has no
    # edges but its class is connected -> internal, not orphan.
    unwired = by_q["m:Repo.unwired"]
    assert unwired.cls == "internal"
    store.close()


def test_role_axis_flow_aggregation(project: Path):
    store = _scanned_store(project)
    _tag(store, "app:main", role="cli")
    _tag(store, "app:run_external", role="io")
    model = build_system_model(store, project_root=project)
    role_axis = model.axes["role"]
    flows = {(f.source, f.target): f.weight for f in role_axis.flows}
    assert flows.get(("cli", "io"), 0) >= 1
    store.close()


def test_subsystem_axis_present(project: Path):
    store = _scanned_store(project)
    model = build_system_model(store, project_root=project)
    assert "subsystem" in model.axes
    keys = {g.key for g in model.axes["subsystem"].groups}
    # app.py is its own subsystem; tests excluded so no tests/ subsystem
    assert any("app" in k for k in keys)
    assert not any(k.startswith("tests") for k in keys)
    store.close()


def test_layout_positions_assigned(project: Path):
    store = _scanned_store(project)
    model = build_system_model(store, project_root=project)
    # doors sit at depth 0 (top); deeper nodes have larger y
    by_q = {n.qname: n for n in model.nodes}
    assert by_q["app:main"].y <= by_q["app:helper"].y
    store.close()


def test_serialization_shape(project: Path):
    store = _scanned_store(project)
    d = system_model_to_dict(build_system_model(store, project_root=project))
    assert set(d.keys()) == {"nodes", "axes", "landmarks", "stats"}
    assert {"role", "subsystem"} <= set(d["axes"].keys())
    assert all("cls" in n and "salience" in n and "x" in n for n in d["nodes"])
    store.close()


def test_cache_roundtrip_and_invalidation(project: Path):
    store = _scanned_store(project)
    first = build_system_model_cached(store, project_root=project)
    cache = project / ".trie" / "system_model.json"
    assert cache.exists()
    # second call hits cache, identical result
    second = build_system_model_cached(store, project_root=project)
    assert first == second
    # include_tests returns more nodes
    with_tests = build_system_model_cached(store, project_root=project, include_tests=True)
    assert len(with_tests["nodes"]) > len(first["nodes"])
    store.close()
