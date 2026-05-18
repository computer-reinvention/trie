from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pytest
from typer.testing import CliRunner

from trie.cli import app
from trie.config import Config
from trie.cost import get_pricing
from trie.graph.store import Store
from trie.models import GenerationRequest, GenerationResponse
from trie.sync.incremental import compute_incremental_worklist, run_incremental
from trie.sync.single_file import sync_single_file
from trie.sync.writer import TriefactFile


@dataclass
class FakeClient:
    model_id: str = "anthropic/claude-sonnet-4-6"
    body: str = "## generated\n\nbody."
    calls: int = 0

    def generate(self, _req: GenerationRequest) -> GenerationResponse:
        self.calls += 1
        return GenerationResponse(
            text=self.body,
            input_tokens=50,
            output_tokens=100,
            cache_creation_input_tokens=0,
            cache_read_input_tokens=0,
        )

    def count_tokens(self, _req: GenerationRequest) -> int:
        return 100


@pytest.fixture
def project(tmp_path: Path) -> Path:
    (tmp_path / "trie.toml").write_text(
        '[trie]\nversion = "0.1.1"\n'
        '[scope]\ninclude = ["**/*.py"]\nexclude = ["**/__pycache__/**"]\n'
        '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
        '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
        'cascade = "anthropic/claude-sonnet-4-6"\n'
        "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
    )
    (tmp_path / "lib.py").write_text("def helper():\n    return 1\n")
    (tmp_path / "app.py").write_text(
        "from lib import helper\n\n\ndef run():\n    return helper()\n"
    )
    return tmp_path


def _initial_sync(project: Path) -> None:
    config, _ = Config.find_and_load(project)
    sync_single_file(
        project / "lib.py",
        project_root=project,
        config=config,
        client=FakeClient(body="## v1 lib\n\nbody."),
    )
    sync_single_file(
        project / "app.py",
        project_root=project,
        config=config,
        client=FakeClient(body="## v1 app\n\nbody."),
    )


def test_incremental_no_op_when_clean(project: Path):
    _initial_sync(project)
    config, _ = Config.find_and_load(project)
    pricing = get_pricing("anthropic/claude-sonnet-4-6")
    client = FakeClient()
    with Store(project / ".trie" / "graph.db") as store:
        result = run_incremental(
            project_root=project,
            config=config,
            store=store,
            client=client,
            pricing=pricing,
        )
    assert result.files_synced == 0
    assert client.calls == 0


def test_incremental_resyncs_directly_changed_file(project: Path):
    _initial_sync(project)
    # Modify lib.py — its triefact becomes stale
    (project / "lib.py").write_text("def helper():\n    return 999\n")

    config, _ = Config.find_and_load(project)
    pricing = get_pricing("anthropic/claude-sonnet-4-6")
    client = FakeClient(body="## v2 lib\n\nbody.")
    with Store(project / ".trie" / "graph.db") as store:
        result = run_incremental(
            project_root=project,
            config=config,
            store=store,
            client=client,
            pricing=pricing,
        )
    assert result.files_synced >= 1
    synced_files = {sr.source_path.name for sr in result.sync_results}
    assert "lib.py" in synced_files


def test_incremental_cascades_to_callers(project: Path):
    """Editing lib.py should cause app.py's triefact to regenerate too (because app.run uses lib.helper)."""
    _initial_sync(project)
    (project / "lib.py").write_text("def helper():\n    return 999\n")

    config, _ = Config.find_and_load(project)
    pricing = get_pricing("anthropic/claude-sonnet-4-6")
    client = FakeClient(body="## v2\n\nbody.")
    with Store(project / ".trie" / "graph.db") as store:
        result = run_incremental(
            project_root=project,
            config=config,
            store=store,
            client=client,
            pricing=pricing,
        )

    synced_files = {sr.source_path.name for sr in result.sync_results}
    assert "lib.py" in synced_files
    assert "app.py" in synced_files  # cascade pulled it in
    assert result.directly_stale_count == 1
    assert result.cascaded_count == 1


def test_incremental_respects_budget(project: Path):
    _initial_sync(project)
    (project / "lib.py").write_text("def helper():\n    return 999\n")

    config, _ = Config.find_and_load(project)
    pricing = get_pricing("anthropic/claude-sonnet-4-6")
    client = FakeClient()
    with Store(project / ".trie" / "graph.db") as store:
        result = run_incremental(
            project_root=project,
            config=config,
            store=store,
            client=client,
            pricing=pricing,
            budget_usd=0.0001,
        )
    # First file may complete, but the second should be skipped.
    assert result.files_synced >= 1
    assert result.files_skipped_no_budget >= 1


def test_incremental_dispatched_via_cli(project: Path, monkeypatch: pytest.MonkeyPatch):
    """Verify `trie sync` (no flags) routes through run_incremental."""
    _initial_sync(project)
    (project / "lib.py").write_text("def helper():\n    return 999\n")
    monkeypatch.chdir(project)

    captured: dict = {}

    def fake_make_client(model_id: str, **_kwargs):
        captured["model_id"] = model_id
        return FakeClient(body="## via_cli\n\nbody.", model_id=model_id)

    monkeypatch.setattr("trie.cli.make_client", fake_make_client)

    runner = CliRunner()
    cli_result = runner.invoke(app, ["sync"])
    assert cli_result.exit_code == 0, cli_result.output
    assert "synced" in cli_result.output
    assert "cascade" in cli_result.output
    # Verify the lib.py and app.py triefacts got regenerated with the v2 body
    lib_triefact = (project / "triefacts" / "lib.md").read_text()
    app_triefact = (project / "triefacts" / "app.md").read_text()
    assert "via_cli" in lib_triefact
    assert "via_cli" in app_triefact


def test_incremental_clean_via_cli(project: Path, monkeypatch: pytest.MonkeyPatch):
    _initial_sync(project)
    monkeypatch.chdir(project)
    monkeypatch.setattr(
        "trie.cli.make_client",
        lambda model_id, **_kw: FakeClient(model_id=model_id),
    )
    runner = CliRunner()
    cli_result = runner.invoke(app, ["sync"])
    assert cli_result.exit_code == 0
    assert "coherent" in cli_result.output


def test_incremental_with_no_changes_yields_empty(project: Path):
    """If no files changed and triefacts already exist, incremental should be a no-op."""
    _initial_sync(project)
    config, _ = Config.find_and_load(project)
    with Store(project / ".trie" / "graph.db") as store:
        result = run_incremental(
            project_root=project,
            config=config,
            store=store,
            client=FakeClient(),
            pricing=get_pricing("anthropic/claude-sonnet-4-6"),
        )
    assert result.directly_stale_count == 0
    assert result.cascaded_count == 0
    assert result.files_synced == 0


def test_incremental_handles_missing_triefact(project: Path):
    """No triefacts at all → directly_stale should include all files with public symbols, cascade adds none beyond."""
    config, _ = Config.find_and_load(project)
    pricing = get_pricing("anthropic/claude-sonnet-4-6")
    with Store(project / ".trie" / "graph.db") as store:
        result = run_incremental(
            project_root=project,
            config=config,
            store=store,
            client=FakeClient(),
            pricing=pricing,
        )
    synced_files = {sr.source_path.name for sr in result.sync_results}
    assert {"lib.py", "app.py"}.issubset(synced_files)
    # Both files were directly stale (no triefact); cascade should NOT additionally count them.
    assert result.directly_stale_count == 2


def test_triefact_regenerated_only_for_affected_symbols_v01_limitation(project: Path):
    """v0.1 regenerates the WHOLE file's symbols, not just stale sections — document this.

    M4 cascade refines this in spirit (only affected files regenerate), but per-symbol
    granularity within a file is still v0.2 work.
    """
    _initial_sync(project)
    config, _ = Config.find_and_load(project)
    # Only modify lib.py
    (project / "lib.py").write_text("def helper():\n    return 42\n")

    with Store(project / ".trie" / "graph.db") as store:
        run_incremental(
            project_root=project,
            config=config,
            store=store,
            client=FakeClient(body="## v2\n\nbody."),
            pricing=get_pricing("anthropic/claude-sonnet-4-6"),
        )

    # Both lib.md and app.md should have been touched (cascade brought app.py in).
    lib_text = (project / "triefacts" / "lib.md").read_text()
    app_text = (project / "triefacts" / "app.md").read_text()
    lib_triefact = TriefactFile.parse(lib_text)
    app_triefact = TriefactFile.parse(app_text)
    assert "lib:helper" in lib_triefact.section_qnames()
    assert "app:run" in app_triefact.section_qnames()


def test_run_incremental_invokes_progress_callback(project: Path):
    """Cascade-driven re-sync streams per-file events to the progress callback."""

    config, _ = Config.find_and_load(project)
    db_path = project / ".trie" / "graph.db"

    # Bootstrap both files first so we have a non-empty triefacts tree.
    with Store(db_path) as store:
        from trie.scan import scan_project as _scan

        _scan(project_root=project, config=config, store=store)
    sync_single_file(project / "lib.py", project_root=project, config=config, client=FakeClient())
    sync_single_file(project / "app.py", project_root=project, config=config, client=FakeClient())

    # Mutate lib.py so the cascade kicks in.
    (project / "lib.py").write_text("def helper():\n    return 'CHANGED'\n")

    starts: list[tuple[str, int, int]] = []
    dones: list[str] = []

    class Recorder:
        def on_start(self, rel_path, idx, total):
            starts.append((rel_path, idx, total))

        def on_done(self, rel_path, result, running_cost_usd):
            dones.append(rel_path)

        def on_skip(self, rel_path, reason):
            pass

    with Store(db_path) as store:
        run_incremental(
            project_root=project,
            config=config,
            store=store,
            client=FakeClient(body="## v2\n\nbody."),
            pricing=get_pricing("anthropic/claude-sonnet-4-6"),
            progress=Recorder(),
        )

    # At least lib.py and app.py should have streamed through the callback.
    assert {rel for rel, _, _ in starts} >= {"lib.py", "app.py"}
    assert {rel for rel in dones} >= {"lib.py", "app.py"}


def test_compute_incremental_worklist_empty_when_clean(project: Path):
    """A coherent tree should produce an empty worklist (no LLM work needed)."""
    _initial_sync(project)
    config, _ = Config.find_and_load(project)
    with Store(project / ".trie" / "graph.db") as store:
        worklist = compute_incremental_worklist(project_root=project, config=config, store=store)
    assert worklist.affected_files == []
    assert worklist.directly_stale == []
    assert worklist.cascaded_files == []
    assert worklist.orphan_triefacts == []


def test_compute_incremental_worklist_includes_cascade(project: Path):
    """Editing lib.py should put both lib.py (direct) and app.py (cascade) in the worklist
    without doing any LLM work or deleting anything."""
    _initial_sync(project)
    (project / "lib.py").write_text("def helper():\n    return 999\n")

    config, _ = Config.find_and_load(project)
    with Store(project / ".trie" / "graph.db") as store:
        worklist = compute_incremental_worklist(project_root=project, config=config, store=store)
    assert "lib.py" in worklist.directly_stale
    assert "app.py" in worklist.cascaded_files
    assert set(worklist.affected_files) >= {"lib.py", "app.py"}


def test_compute_incremental_worklist_is_read_only(project: Path):
    """The worklist must not mutate the triefacts dir — `trie plan` is read-only."""
    _initial_sync(project)
    triefacts_root = project / "triefacts"
    before = {p.name: p.read_text() for p in triefacts_root.rglob("*.md")}

    (project / "lib.py").write_text("def helper():\n    return 999\n")
    config, _ = Config.find_and_load(project)
    with Store(project / ".trie" / "graph.db") as store:
        compute_incremental_worklist(project_root=project, config=config, store=store)

    after = {p.name: p.read_text() for p in triefacts_root.rglob("*.md")}
    assert before == after


def test_compute_incremental_worklist_reports_orphans(project: Path):
    """When source disappears, its triefact becomes an orphan — worklist surfaces it
    without deleting (sync handles deletion)."""
    _initial_sync(project)
    (project / "lib.py").unlink()  # orphan lib.md

    config, _ = Config.find_and_load(project)
    with Store(project / ".trie" / "graph.db") as store:
        worklist = compute_incremental_worklist(project_root=project, config=config, store=store)
    orphan_names = {p.name for p in worklist.orphan_triefacts}
    assert "lib.md" in orphan_names
    # The orphan triefact file is still on disk — worklist did not delete it.
    assert (project / "triefacts" / "lib.md").exists()


def test_cli_plan_incremental_on_clean_tree_reports_noop(
    project: Path, monkeypatch: pytest.MonkeyPatch
):
    """`trie plan` on a coherent established project should announce no-op, not list a
    bogus full-bootstrap cost."""
    _initial_sync(project)
    monkeypatch.chdir(project)
    monkeypatch.setattr("trie.cli.make_client", lambda _model_id, **_kw: FakeClient())
    runner = CliRunner()
    result = runner.invoke(app, ["plan"])
    assert result.exit_code == 0, result.output
    assert "coherent" in result.output or "no-op" in result.output
    # Critically: the full-bootstrap header must not appear.
    assert "plan for" not in result.output


def test_cli_plan_incremental_on_drift_lists_only_affected(
    project: Path, monkeypatch: pytest.MonkeyPatch
):
    """On an established project with drift, `trie plan` shows the incremental cost,
    not the cost of regenerating every in-scope file."""
    _initial_sync(project)
    (project / "lib.py").write_text("def helper():\n    return 999\n")
    monkeypatch.chdir(project)
    monkeypatch.setattr("trie.cli.make_client", lambda _model_id, **_kw: FakeClient())
    runner = CliRunner()
    result = runner.invoke(app, ["plan"])
    assert result.exit_code == 0, result.output
    assert "incremental plan for" in result.output
    assert "directly stale" in result.output


def test_cli_plan_all_forces_full_bootstrap_view(project: Path, monkeypatch: pytest.MonkeyPatch):
    """`trie plan --all` opts into the legacy full-bootstrap view on an established
    project — useful for 'what would re-bootstrapping cost?'"""
    _initial_sync(project)
    monkeypatch.chdir(project)
    monkeypatch.setattr("trie.cli.make_client", lambda _model_id, **_kw: FakeClient())
    runner = CliRunner()
    result = runner.invoke(app, ["plan", "--all"])
    assert result.exit_code == 0, result.output
    assert "plan for" in result.output
    assert "incremental plan for" not in result.output
