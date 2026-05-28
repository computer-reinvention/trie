from __future__ import annotations

from pathlib import Path

import pytest
from typer.testing import CliRunner

from tests.fake_client import FakeTrieClient
from trie.cli import app
from trie.config import Config
from trie.cost import get_pricing
from trie.graph.store import Store
from trie.scan import scan_project
from trie.sync.bootstrap import build_plan, run_bootstrap


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
        plan = build_plan(
            project_root=project,
            store=store,
            model_id="anthropic/claude-sonnet-4-6",
            client=FakeTrieClient(
                model_id="anthropic/claude-sonnet-4-6",
                output_body="## generated\n\nbody.",
                input_tokens=50,
                output_tokens=100,
                cache_creation_input_tokens=500,
            ),
        )
    paths = [it.file_path for it in plan.items]
    # large.py has 2 symbols * ~50 LOC; medium.py has 3 symbols * small LOC; small.py has 1 * 2 LOC.
    # large should come first (highest LOC*symbols product).
    assert paths[0] == "large.py"
    assert plan.pricing_known is True
    assert plan.total_estimated_cost > 0


def test_plan_excludes_files_with_no_documentable_symbols(project: Path, tmp_path: Path):
    """Files with zero parser-surfaced symbols drop out of the plan.

    Under symbol-level sync, the leading-underscore "private" convention is
    *not* a filter — `_hidden` would be documented. The parser surfaces
    functions, classes, methods, module-level constants (`NAME = value`),
    and a `__module__` synthetic symbol for files with module-level
    behaviour. Only files that don't have ANY of those land outside the
    plan — e.g. a pure-imports file with no constants, no defs, no
    module-level expression statements beyond the imports.
    """
    # imports-only file: no constants, no defs, no top-level expressions.
    # The parser surfaces nothing for this, so it's excluded from the plan.
    (project / "imports_only.py").write_text("import os\nfrom typing import Any\n")
    # A file with just a constant — gets a `constant` symbol now, so it IS
    # in the plan even though there are no functions or classes.
    (project / "constants_only.py").write_text("CONSTANT = 1\nMAX_RETRIES = 5\n")
    # A file with only private (`_hidden`) defs is still documented under
    # symbol-level sync — the underscore is descriptive metadata, not a
    # filter.
    (project / "private.py").write_text("def _hidden():\n    pass\n")
    with _scanned_store(project) as store:
        plan = build_plan(
            project_root=project,
            store=store,
            model_id="anthropic/claude-sonnet-4-6",
            client=FakeTrieClient(
                model_id="anthropic/claude-sonnet-4-6",
                output_body="## generated\n\nbody.",
                input_tokens=50,
                output_tokens=100,
                cache_creation_input_tokens=500,
            ),
        )
    paths = [it.file_path for it in plan.items]
    # `private.py` is documented — its `_hidden` symbol is a real, parser-surfaced def.
    assert "private.py" in paths
    # `constants_only.py` is documented — module-level NAME = value is a
    # `constant` symbol under the expanded parser.
    assert "constants_only.py" in paths
    # `imports_only.py` has nothing the parser surfaces; the plan skips it.
    assert "imports_only.py" not in paths


def test_plan_with_unknown_model_zero_cost(project: Path):
    with _scanned_store(project) as store:
        plan = build_plan(
            project_root=project,
            store=store,
            model_id="openai/some-model",
            client=FakeTrieClient(
                model_id="anthropic/claude-sonnet-4-6",
                output_body="## generated\n\nbody.",
                input_tokens=50,
                output_tokens=100,
                cache_creation_input_tokens=500,
            ),  # never queried since pricing is unknown
        )
    assert plan.pricing_known is False
    assert plan.total_estimated_cost == 0.0


def test_plan_only_files_restricts_worklist(project: Path):
    """`only_files` is the seam `trie plan` uses on established projects to scope the
    cost estimate to the incremental worklist instead of the whole tree."""
    with _scanned_store(project) as store:
        plan = build_plan(
            project_root=project,
            store=store,
            model_id="anthropic/claude-sonnet-4-6",
            client=FakeTrieClient(
                model_id="anthropic/claude-sonnet-4-6",
                output_body="## generated\n\nbody.",
                input_tokens=50,
                output_tokens=100,
                cache_creation_input_tokens=500,
            ),
            only_files={"medium.py"},
        )
    paths = [it.file_path for it in plan.items]
    assert paths == ["medium.py"]


def test_plan_only_files_empty_yields_empty_plan(project: Path):
    with _scanned_store(project) as store:
        plan = build_plan(
            project_root=project,
            store=store,
            model_id="anthropic/claude-sonnet-4-6",
            client=FakeTrieClient(
                model_id="anthropic/claude-sonnet-4-6",
                output_body="## generated\n\nbody.",
                input_tokens=50,
                output_tokens=100,
                cache_creation_input_tokens=500,
            ),
            only_files=set(),
        )
    assert plan.items == []
    assert plan.total_estimated_cost == 0.0


def test_run_bootstrap_respects_limit(project: Path):
    config, _ = Config.find_and_load(project)
    pricing = get_pricing("anthropic/claude-sonnet-4-6")
    client = FakeTrieClient(
        model_id="anthropic/claude-sonnet-4-6",
        output_body="## generated\n\nbody.",
        input_tokens=50,
        output_tokens=100,
        cache_creation_input_tokens=500,
    )
    with _scanned_store(project) as store:
        plan = build_plan(
            project_root=project,
            store=store,
            model_id="anthropic/claude-sonnet-4-6",
            client=FakeTrieClient(
                model_id="anthropic/claude-sonnet-4-6",
                output_body="## generated\n\nbody.",
                input_tokens=50,
                output_tokens=100,
                cache_creation_input_tokens=500,
            ),
        )
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
    client = FakeTrieClient(
        model_id="anthropic/claude-sonnet-4-6",
        output_body="## generated\n\nbody.",
        input_tokens=50,
        output_tokens=100,
        cache_creation_input_tokens=500,
    )
    with _scanned_store(project) as store:
        plan = build_plan(
            project_root=project,
            store=store,
            model_id="anthropic/claude-sonnet-4-6",
            client=FakeTrieClient(
                model_id="anthropic/claude-sonnet-4-6",
                output_body="## generated\n\nbody.",
                input_tokens=50,
                output_tokens=100,
                cache_creation_input_tokens=500,
            ),
        )
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
    client = FakeTrieClient(
        model_id="anthropic/claude-sonnet-4-6",
        output_body="## generated\n\nbody.",
        input_tokens=50,
        output_tokens=100,
        cache_creation_input_tokens=500,
    )
    with _scanned_store(project) as store:
        plan = build_plan(
            project_root=project,
            store=store,
            model_id="anthropic/claude-sonnet-4-6",
            client=FakeTrieClient(
                model_id="anthropic/claude-sonnet-4-6",
                output_body="## generated\n\nbody.",
                input_tokens=50,
                output_tokens=100,
                cache_creation_input_tokens=500,
            ),
        )
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


def test_cli_plan_makes_no_message_calls(project: Path, monkeypatch: pytest.MonkeyPatch):
    """`trie plan` may call count_tokens (free) but must never call generate."""
    monkeypatch.chdir(project)
    fake = FakeTrieClient(
        model_id="anthropic/claude-sonnet-4-6",
        output_body="## generated\n\nbody.",
        input_tokens=50,
        output_tokens=100,
        cache_creation_input_tokens=500,
    )
    monkeypatch.setattr("trie.cli.make_client", lambda _model_id, **_kw: fake)
    runner = CliRunner()
    result = runner.invoke(app, ["plan"])
    assert result.exit_code == 0, result.output
    assert fake.calls == 0  # generate never invoked
    assert "plan for" in result.output


def test_cli_plan_outside_project_errors(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    """Without a trie.toml in the cwd or its parents, plan errors before constructing a client."""
    monkeypatch.chdir(tmp_path)
    sentinel: dict[str, bool] = {"called": False}

    def boom(*_args, **_kwargs):
        sentinel["called"] = True
        raise AssertionError("client should not be constructed without config")

    monkeypatch.setattr("trie.cli.make_client", boom)
    runner = CliRunner()
    result = runner.invoke(app, ["plan"])
    assert result.exit_code == 1
    assert sentinel["called"] is False


def test_cli_first_run_sync_requires_budget_or_limit_non_interactive(
    project: Path, monkeypatch: pytest.MonkeyPatch
):
    """In a fresh project (no triefacts yet), `trie sync` without --budget/--limit must
    refuse non-interactive runs to avoid surprise bills."""
    monkeypatch.chdir(project)
    monkeypatch.setattr(
        "trie.cli.make_client",
        lambda _model_id, **_kw: FakeTrieClient(
            model_id="anthropic/claude-sonnet-4-6",
            output_body="## generated\n\nbody.",
            input_tokens=50,
            output_tokens=100,
            cache_creation_input_tokens=500,
        ),
    )
    runner = CliRunner()
    result = runner.invoke(app, ["sync"])
    assert result.exit_code == 1
    assert "--budget" in result.output or "--limit" in result.output


def test_cli_first_run_sync_with_limit_succeeds(project: Path, monkeypatch: pytest.MonkeyPatch):
    """Auto-detected first-run bootstrap proceeds when a cap is set."""
    monkeypatch.chdir(project)
    monkeypatch.setattr(
        "trie.cli.make_client",
        lambda _model_id, **_kw: FakeTrieClient(
            model_id="anthropic/claude-sonnet-4-6",
            output_body="## generated\n\nbody.",
            input_tokens=50,
            output_tokens=100,
            cache_creation_input_tokens=500,
        ),
    )
    runner = CliRunner()
    result = runner.invoke(app, ["sync", "--limit", "1"])
    assert result.exit_code == 0, result.output
    assert "synced" in result.output


def test_cli_sync_all_forces_full_pass(project: Path, monkeypatch: pytest.MonkeyPatch):
    """Even when triefacts already exist, --all should re-run the bootstrap path."""
    # Pre-populate one triefact so the auto-detect would otherwise pick incremental.
    triefacts = project / "triefacts"
    triefacts.mkdir()
    (triefacts / "small.md").write_text("# placeholder\n")
    monkeypatch.chdir(project)
    monkeypatch.setattr(
        "trie.cli.make_client",
        lambda _model_id, **_kw: FakeTrieClient(
            model_id="anthropic/claude-sonnet-4-6",
            output_body="## generated\n\nbody.",
            input_tokens=50,
            output_tokens=100,
            cache_creation_input_tokens=500,
        ),
    )
    runner = CliRunner()
    result = runner.invoke(app, ["sync", "--all", "--limit", "1"])
    assert result.exit_code == 0, result.output
    # The full-pass path prints the plan header.
    assert "plan for" in result.output


def test_cli_sync_rejects_file_and_all_together(project: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["sync", "--file", str(project / "small.py"), "--all"])
    assert result.exit_code == 1
    assert "mutually exclusive" in result.output


def test_cli_sync_with_no_config_errors(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    """Bare `trie sync` without a project errors clearly."""
    monkeypatch.chdir(tmp_path)
    runner = CliRunner()
    result = runner.invoke(app, ["sync"])
    assert result.exit_code == 1
    assert "trie.toml" in result.output


def test_run_bootstrap_invokes_progress_callback(project: Path):
    """Each completed file fires on_start + on_done; skipped files fire on_skip."""

    config, _ = Config.find_and_load(project)
    pricing = get_pricing("anthropic/claude-sonnet-4-6")
    client = FakeTrieClient(
        model_id="anthropic/claude-sonnet-4-6",
        output_body="## generated\n\nbody.",
        input_tokens=50,
        output_tokens=100,
        cache_creation_input_tokens=500,
    )
    with _scanned_store(project) as store:
        plan = build_plan(
            project_root=project,
            store=store,
            model_id="anthropic/claude-sonnet-4-6",
            client=FakeTrieClient(
                model_id="anthropic/claude-sonnet-4-6",
                output_body="## generated\n\nbody.",
                input_tokens=50,
                output_tokens=100,
                cache_creation_input_tokens=500,
            ),
        )

    starts: list[tuple[str, int, int]] = []
    dones: list[tuple[str, float]] = []
    skips: list[tuple[str, str]] = []

    class Recorder:
        def on_start(self, rel_path, idx, total):
            starts.append((rel_path, idx, total))

        def on_done(self, rel_path, result, running_cost_usd):
            dones.append((rel_path, running_cost_usd))

        def on_skip(self, rel_path, reason):
            skips.append((rel_path, reason))

    run_bootstrap(
        plan=plan,
        project_root=project,
        config=config,
        client=client,
        pricing=pricing,
        budget_usd=None,
        limit=2,
        progress=Recorder(),
    )

    assert len(starts) == 2
    assert len(dones) == 2
    # Total in each on_start matches the plan size.
    total = len(plan.items)
    assert all(t == total for _, _, t in starts)
    # Skipped files are reported with a reason.
    assert len(skips) == total - 2
    assert all(reason == "limit reached" for _, reason in skips)
