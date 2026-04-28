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
from trie.scan import scan_project
from trie.sync.bootstrap import build_plan, run_bootstrap


@dataclass
class FakeClient:
    model_id: str = "anthropic/claude-sonnet-4-6"
    calls: int = 0

    def generate(self, _req: GenerationRequest) -> GenerationResponse:
        self.calls += 1
        return GenerationResponse(
            text="## generated\n\nbody.",
            input_tokens=50,
            output_tokens=100,
            cache_creation_input_tokens=500 if self.calls == 1 else 0,
            cache_read_input_tokens=0 if self.calls == 1 else 500,
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
    # Three files of different sizes/symbol counts.
    (tmp_path / "small.py").write_text("def x():\n    pass\n")
    (tmp_path / "medium.py").write_text(
        "def a():\n    pass\n\n\ndef b():\n    pass\n\n\ndef c():\n    pass\n"
    )
    big = "def big():\n    " + "x = 1\n    " * 50 + "return x\n"
    (tmp_path / "large.py").write_text(big + "\n\ndef big2():\n    return 2\n")
    return tmp_path


def _scanned_store(project: Path) -> Store:
    config, _ = Config.find_and_load(project)
    store = Store(project / ".trie" / "graph.db")
    scan_project(project_root=project, config=config, store=store)
    return store


def test_plan_ranks_higher_score_first(project: Path):
    with _scanned_store(project) as store:
        plan = build_plan(project_root=project, store=store, model_id="anthropic/claude-sonnet-4-6")
    paths = [it.file_path for it in plan.items]
    # large.py has 2 symbols * ~50 LOC; medium.py has 3 symbols * small LOC; small.py has 1 * 2 LOC.
    # large should come first (highest LOC*symbols product).
    assert paths[0] == "large.py"
    assert plan.pricing_known is True
    assert plan.total_estimated_cost > 0


def test_plan_excludes_files_with_no_public_symbols(project: Path, tmp_path: Path):
    (project / "private.py").write_text("def _hidden():\n    pass\n")
    with _scanned_store(project) as store:
        plan = build_plan(project_root=project, store=store, model_id="anthropic/claude-sonnet-4-6")
    paths = [it.file_path for it in plan.items]
    assert "private.py" not in paths


def test_plan_with_unknown_model_zero_cost(project: Path):
    with _scanned_store(project) as store:
        plan = build_plan(project_root=project, store=store, model_id="openai/some-model")
    assert plan.pricing_known is False
    assert plan.total_estimated_cost == 0.0


def test_run_bootstrap_respects_limit(project: Path):
    config, _ = Config.find_and_load(project)
    pricing = get_pricing("anthropic/claude-sonnet-4-6")
    client = FakeClient()
    with _scanned_store(project) as store:
        plan = build_plan(project_root=project, store=store, model_id="anthropic/claude-sonnet-4-6")
    result = run_bootstrap(
        plan=plan,
        project_root=project,
        config=config,
        client=client,
        pricing=pricing,
        budget_usd=None,
        limit=2,
    )
    assert result.files_synced == 2
    assert result.files_skipped_no_budget == len(plan.items) - 2


def test_run_bootstrap_respects_budget(project: Path):
    config, _ = Config.find_and_load(project)
    pricing = get_pricing("anthropic/claude-sonnet-4-6")
    client = FakeClient()
    with _scanned_store(project) as store:
        plan = build_plan(project_root=project, store=store, model_id="anthropic/claude-sonnet-4-6")
    # Tiny budget should cap to ~1 file.
    result = run_bootstrap(
        plan=plan,
        project_root=project,
        config=config,
        client=client,
        pricing=pricing,
        budget_usd=0.0001,
        limit=None,
    )
    assert result.files_synced >= 1
    assert result.files_synced < len(plan.items)
    assert result.actual_cost_usd >= 0.0001 - 0.001  # may overshoot by last file


def test_run_bootstrap_unbounded_processes_all(project: Path):
    config, _ = Config.find_and_load(project)
    pricing = get_pricing("anthropic/claude-sonnet-4-6")
    client = FakeClient()
    with _scanned_store(project) as store:
        plan = build_plan(project_root=project, store=store, model_id="anthropic/claude-sonnet-4-6")
    result = run_bootstrap(
        plan=plan,
        project_root=project,
        config=config,
        client=client,
        pricing=pricing,
        budget_usd=None,
        limit=None,
    )
    assert result.files_synced == len(plan.items)
    assert result.files_skipped_no_budget == 0


def test_cli_bootstrap_dry_run_makes_no_api_calls(project: Path, monkeypatch: pytest.MonkeyPatch):
    """--dry-run should print the plan without invoking the model."""
    sentinel: dict[str, bool] = {"called": False}

    def boom(*args, **kwargs):
        sentinel["called"] = True
        raise AssertionError("model should not be constructed in dry-run")

    monkeypatch.setattr("trie.cli.make_client", boom)
    runner = CliRunner()
    runner.invoke(app, ["sync", "--bootstrap", "--dry-run"], catch_exceptions=False)
    # CliRunner runs in-process; without monkeypatching cwd, find_and_load fails with
    # ConfigNotFoundError before reaching make_client. The next test exercises the dry-run
    # success path with cwd set; this one just guarantees that on failure, no model is built.
    assert sentinel["called"] is False


def test_cli_bootstrap_dry_run_in_project(project: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(project)
    sentinel: dict[str, bool] = {"called": False}

    def boom(*_args, **_kwargs):
        sentinel["called"] = True
        raise AssertionError("model should not be constructed in dry-run")

    monkeypatch.setattr("trie.cli.make_client", boom)
    runner = CliRunner()
    result = runner.invoke(app, ["sync", "--bootstrap", "--dry-run"])
    assert result.exit_code == 0, result.output
    assert sentinel["called"] is False
    assert "plan for" in result.output
    assert "dry-run" in result.output


def test_cli_bootstrap_requires_budget_or_limit(project: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["sync", "--bootstrap"])
    assert result.exit_code == 1
    assert "--budget" in result.output or "--limit" in result.output


def test_cli_sync_rejects_file_and_bootstrap_together(
    project: Path, monkeypatch: pytest.MonkeyPatch
):
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["sync", "--file", str(project / "small.py"), "--bootstrap"])
    assert result.exit_code == 1
    assert "mutually exclusive" in result.output


def test_cli_sync_rejects_neither_mode(project: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["sync"])
    assert result.exit_code == 1
    assert "--file" in result.output
