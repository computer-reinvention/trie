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
from trie.sync.incremental import run_incremental
from trie.sync.single_file import sync_single_file
from trie.sync.writer import DocFile


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


@pytest.fixture
def project(tmp_path: Path) -> Path:
    (tmp_path / "trie.toml").write_text(
        '[trie]\nversion = "0.1.0"\n'
        '[scope]\ninclude = ["**/*.py"]\nexclude = ["**/__pycache__/**"]\n'
        '[docs]\nroot = "docs"\nsource_root = "."\n'
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
    # Modify lib.py — its doc becomes stale
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
    """Editing lib.py should cause app.py's doc to regenerate too (because app.run uses lib.helper)."""
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

    def fake_make_client(model_id: str):
        captured["model_id"] = model_id
        return FakeClient(body="## via_cli\n\nbody.", model_id=model_id)

    monkeypatch.setattr("trie.cli.make_client", fake_make_client)

    runner = CliRunner()
    cli_result = runner.invoke(app, ["sync"])
    assert cli_result.exit_code == 0, cli_result.output
    assert "synced" in cli_result.output
    assert "cascade" in cli_result.output
    # Verify the lib.py and app.py docs got regenerated with the v2 body
    lib_doc = (project / "docs" / "lib.md").read_text()
    app_doc = (project / "docs" / "app.md").read_text()
    assert "via_cli" in lib_doc
    assert "via_cli" in app_doc


def test_incremental_clean_via_cli(project: Path, monkeypatch: pytest.MonkeyPatch):
    _initial_sync(project)
    monkeypatch.chdir(project)
    monkeypatch.setattr("trie.cli.make_client", lambda model_id: FakeClient(model_id=model_id))
    runner = CliRunner()
    cli_result = runner.invoke(app, ["sync"])
    assert cli_result.exit_code == 0
    assert "coherent" in cli_result.output


def test_incremental_with_no_changes_yields_empty(project: Path):
    """If no files changed and docs already exist, incremental should be a no-op."""
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


def test_incremental_handles_missing_doc(project: Path):
    """No docs at all → directly_stale should include all files with public symbols, cascade adds none beyond."""
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
    # Both files were directly stale (no doc); cascade should NOT additionally count them.
    assert result.directly_stale_count == 2


def test_doc_regenerated_only_for_affected_symbols_v01_limitation(project: Path):
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
    lib_text = (project / "docs" / "lib.md").read_text()
    app_text = (project / "docs" / "app.md").read_text()
    lib_doc = DocFile.parse(lib_text)
    app_doc = DocFile.parse(app_text)
    assert "lib:helper" in lib_doc.section_qnames()
    assert "app:run" in app_doc.section_qnames()
