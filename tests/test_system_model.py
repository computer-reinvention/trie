from __future__ import annotations

from pathlib import Path

import pytest

from trie.config import Config
from trie.graph.store import Store
from trie.graph.system_model import build_system_model, system_model_to_dict
from trie.scan import scan_project


@pytest.fixture
def project(tmp_path: Path) -> Path:
    """A small project exercising every skeleton class.

    - `main` is a Typer command (decorator) -> door
    - `run_external` reaches out via subprocess + boundary='exit' -> exit
    - `core` / `helper` are plain internal functions
    - `CONFIG` is referenced by nothing and references nothing -> orphan
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
    return tmp_path


def _scanned_store(project: Path) -> Store:
    config, _ = Config.find_and_load(project)
    store = Store(project / ".trie" / "graph.db")
    scan_project(project_root=project, config=config, store=store)
    return store


def test_decorator_marks_door(project: Path):
    store = _scanned_store(project)
    model = build_system_model(store, project_root=project)
    by_q = {n.qname: n for n in model.nodes}
    assert by_q["app:main"].cls == "door"
    store.close()


def test_pyproject_scripts_recognized(project: Path):
    # main is also the pyproject [project.scripts] target — door either way.
    store = _scanned_store(project)
    model = build_system_model(store, project_root=project)
    assert "app:main" in {n.qname for n in model.nodes if n.cls == "door"}
    store.close()


def test_exit_boundary_classifies_exit(project: Path):
    store = _scanned_store(project)
    sid = store._conn.execute(
        "SELECT id FROM symbols WHERE qualified_name = 'app:run_external'"
    ).fetchone()[0]
    store._conn.execute(
        "INSERT INTO triefact_sections "
        "(triefact_path, symbol_id, section_fingerprint, one_liner, role, boundary, last_generated_at) "
        "VALUES (?, ?, ?, ?, ?, ?, ?)",
        ("t.md", sid, "fp", "runs ls", "io", "exit", 0),
    )
    store._conn.commit()
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
    # CONFIG is referenced by nothing and references nothing.
    assert by_q["app:CONFIG"].cls == "orphan"
    store.close()


def test_salience_orders_doors_above_helpers(project: Path):
    store = _scanned_store(project)
    model = build_system_model(store, project_root=project)
    by_q = {n.qname: n for n in model.nodes}
    assert by_q["app:main"].salience > by_q["app:helper"].salience
    store.close()


def test_role_flow_aggregation(project: Path):
    store = _scanned_store(project)
    # tag main as 'cli' and run_external as 'io' so a cross-role edge exists
    for qname, role in (("app:main", "cli"), ("app:run_external", "io")):
        sid = store._conn.execute(
            "SELECT id FROM symbols WHERE qualified_name = ?", (qname,)
        ).fetchone()[0]
        store._conn.execute(
            "INSERT INTO triefact_sections "
            "(triefact_path, symbol_id, section_fingerprint, one_liner, role, boundary, last_generated_at) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            ("t.md", sid, "fp", "", role, "internal", 0),
        )
    store._conn.commit()
    model = build_system_model(store, project_root=project)
    flows = {(f.source, f.target): f.weight for f in model.role_flows}
    # main (cli) -> run_external (io) is a cross-role call edge
    assert flows.get(("cli", "io"), 0) >= 1
    store.close()


def test_serialization_shape(project: Path):
    store = _scanned_store(project)
    d = system_model_to_dict(build_system_model(store, project_root=project))
    assert set(d.keys()) == {"nodes", "roles", "role_flows", "landmarks"}
    assert all("cls" in n and "salience" in n for n in d["nodes"])
    store.close()
