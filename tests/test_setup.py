"""End-to-end tests for `trie setup` and the underlying hook installer.

Contract under test:

  - `hook_install.install` writes a plugin file for opencode and returns a
    `needs_manual_setup` result for agents we know about but can't automate.
  - Existing identical hook files are detected as idempotent (`skipped`).
  - `--print-only` / `--dry-run` never write files.
  - `trie setup` invokes both MCP install and hook install for the same set
    of targets in a single pass.
  - The CLI surfaces a unified report and exits non-zero only on real errors
    (manual-setup notices don't fail the run).
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from typer.testing import CliRunner

from trie.cli import app
from trie.hook_install import (
    TARGETS,
    HookApplyResult,
    HookInstallError,
    apply_one,
    install,
)


@pytest.fixture
def project(tmp_path: Path) -> Path:
    """Minimal valid trie project. `trie setup` only needs trie.toml to
    resolve project_root via `Config.find_and_load`."""
    (tmp_path / "trie.toml").write_text(
        '[trie]\nversion = "0.1.0"\n'
        '[scope]\ninclude = ["**/*.py"]\nexclude = []\n'
        '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
        '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
        'cascade = "anthropic/claude-sonnet-4-6"\n'
        "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
    )
    return tmp_path


# ---------------------------------------------------------------------------
# Hook install: opencode (automatable) + others (manual)
# ---------------------------------------------------------------------------


def test_opencode_hook_creates_plugin_file(project: Path):
    plan = install(
        target_names=["opencode"],
        install_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    assert len(plan.results) == 1
    result = plan.results[0]
    assert result.action == "created"
    expected_path = project / ".opencode" / "plugins" / "trie-refresh.ts"
    assert result.path == expected_path
    assert expected_path.exists()
    contents = expected_path.read_text()
    # Key wiring: the plugin listens for session.idle and runs trie refresh.
    assert "session.idle" in contents
    assert "trie refresh --after-turn" in contents


def test_opencode_hook_is_idempotent(project: Path):
    """Two runs in a row: the second is `skipped` because the file already
    contains exactly what we'd write."""
    install(
        target_names=["opencode"],
        install_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    second = install(
        target_names=["opencode"],
        install_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    assert second.results[0].action == "skipped"


def test_opencode_hook_updates_when_contents_changed(project: Path):
    """A hand-edited plugin file gets overwritten on the next run. We trade
    user-edit preservation for guaranteed-correct hook semantics — the file
    header says don't hand-edit."""
    plugin_path = project / ".opencode" / "plugins" / "trie-refresh.ts"
    plugin_path.parent.mkdir(parents=True, exist_ok=True)
    plugin_path.write_text("// stale content\n")
    plan = install(
        target_names=["opencode"],
        install_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    assert plan.results[0].action == "updated"
    assert "session.idle" in plugin_path.read_text()


def test_print_only_writes_no_files(project: Path):
    plan = install(
        target_names=["opencode"],
        install_all=False,
        print_only=True,
        dry_run=False,
        project_root=project,
    )
    assert plan.results[0].action == "preview"
    # Contents are still returned so the caller can render them.
    assert "session.idle" in plan.results[0].contents
    # But nothing landed on disk.
    assert not (project / ".opencode").exists()


def test_dry_run_writes_no_files(project: Path):
    plan = install(
        target_names=["opencode"],
        install_all=False,
        print_only=False,
        dry_run=True,
        project_root=project,
    )
    assert plan.results[0].action == "preview"
    assert not (project / ".opencode").exists()


def test_claude_code_hook_is_manual_setup(project: Path):
    """Agents we know about but can't automate produce a clear instructions
    payload rather than failing or writing a stub file."""
    plan = install(
        target_names=["claude-code"],
        install_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    result = plan.results[0]
    assert result.action == "needs_manual_setup"
    assert result.path is None
    # Instructions actually mention how to wire it.
    assert "trie refresh" in result.detail


def test_unknown_target_raises(project: Path):
    with pytest.raises(HookInstallError, match="unknown hook target"):
        install(
            target_names=["bogus"],
            install_all=False,
            print_only=False,
            dry_run=False,
            project_root=project,
        )


def test_install_all_covers_every_target(project: Path):
    plan = install(
        target_names=None,
        install_all=True,
        print_only=True,
        dry_run=False,
        project_root=project,
    )
    target_set = {r.target for r in plan.results}
    assert target_set == set(TARGETS)


# ---------------------------------------------------------------------------
# apply_one direct surface (used by the registry; tests give a focused signal)
# ---------------------------------------------------------------------------


def test_apply_one_returns_needs_manual_setup_for_render_none(project: Path):
    """A HookTarget with `render_contents=None` always produces a manual-setup
    notice regardless of print/dry-run flags."""
    target = TARGETS["cursor"]  # has no render_contents
    result = apply_one(target, project, print_only=False, dry_run=False)
    assert isinstance(result, HookApplyResult)
    assert result.action == "needs_manual_setup"
    assert result.path is None
    assert "trie refresh" in result.detail


# ---------------------------------------------------------------------------
# CLI: `trie setup` end-to-end
# ---------------------------------------------------------------------------


def test_cli_setup_opencode_writes_both_files(project: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["setup", "--target", "opencode"])
    assert result.exit_code == 0, result.output

    # MCP config written.
    mcp_path = project / "opencode.json"
    assert mcp_path.exists()
    mcp_data = json.loads(mcp_path.read_text())
    assert "trie" in mcp_data["mcp"]

    # Hook plugin written.
    hook_path = project / ".opencode" / "plugins" / "trie-refresh.ts"
    assert hook_path.exists()
    assert "session.idle" in hook_path.read_text()


def test_cli_setup_claude_code_does_mcp_and_warns_about_hook(
    project: Path, monkeypatch: pytest.MonkeyPatch
):
    """Agents without hook automation: MCP succeeds, hook warns. Exit code
    stays 0 because manual-setup isn't a failure."""
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["setup", "--target", "claude-code"])
    assert result.exit_code == 0, result.output

    assert (project / ".mcp.json").exists()
    assert "manual setup required" in result.output


def test_cli_setup_print_only_writes_nothing(project: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["setup", "--target", "opencode", "--print-only"])
    assert result.exit_code == 0, result.output
    assert not (project / "opencode.json").exists()
    assert not (project / ".opencode").exists()
    # But the preview text should reach the user.
    assert "session.idle" in result.output


def test_cli_setup_target_and_all_mutex(project: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["setup", "--target", "opencode", "--all"])
    assert result.exit_code == 1
    assert "mutually exclusive" in result.output


def test_cli_setup_invalid_scope(project: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["setup", "--target", "opencode", "--scope", "global"])
    assert result.exit_code == 1
    assert "scope" in result.output.lower()


def test_cli_setup_idempotent_second_run(project: Path, monkeypatch: pytest.MonkeyPatch):
    """Re-running setup against an already-set-up project should not change
    files and should report skipped/skipped per target."""
    monkeypatch.chdir(project)
    runner = CliRunner()
    first = runner.invoke(app, ["setup", "--target", "opencode"])
    assert first.exit_code == 0, first.output

    # Capture both file contents.
    mcp_before = (project / "opencode.json").read_text()
    hook_before = (project / ".opencode" / "plugins" / "trie-refresh.ts").read_text()

    second = runner.invoke(app, ["setup", "--target", "opencode"])
    assert second.exit_code == 0, second.output

    assert (project / "opencode.json").read_text() == mcp_before
    assert (project / ".opencode" / "plugins" / "trie-refresh.ts").read_text() == hook_before


# ---------------------------------------------------------------------------
# CLI: `trie setup` tool-override flag behaviour
# ---------------------------------------------------------------------------


def test_cli_setup_override_builtins_writes_override_files(
    project: Path, monkeypatch: pytest.MonkeyPatch
):
    """`--override-builtins` skips the interactive prompt and lands the
    override files. This is the path users hit when they've decided
    'yes, override' and don't want to be asked again."""
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["setup", "--target", "opencode", "--override-builtins"])
    assert result.exit_code == 0, result.output

    # All three opencode override files landed.
    assert (project / ".opencode" / "tools" / "grep.ts").exists()
    assert (project / ".opencode" / "tools" / "trie_read.ts").exists()
    assert (project / ".opencode" / "tools" / "trie_trace.ts").exists()


def test_cli_setup_no_override_builtins_skips_overrides(
    project: Path, monkeypatch: pytest.MonkeyPatch
):
    """`--no-override-builtins` is the explicit opt-out, useful in CI and
    scripted setup. No override files land; no prompt fires."""
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["setup", "--target", "opencode", "--no-override-builtins"])
    assert result.exit_code == 0, result.output
    # MCP + hook + docs still ran; only overrides were skipped.
    assert (project / "opencode.json").exists()
    assert (project / ".opencode" / "plugins" / "trie-refresh.ts").exists()
    # But no override files.
    assert not (project / ".opencode" / "tools" / "grep.ts").exists()
    assert not (project / ".opencode" / "tools" / "trie_read.ts").exists()
    assert not (project / ".opencode" / "tools" / "trie_trace.ts").exists()


def test_cli_setup_non_interactive_skips_overrides_silently(
    project: Path, monkeypatch: pytest.MonkeyPatch
):
    """Without an explicit flag, in a non-TTY environment (CliRunner),
    the setup must not prompt and must not install overrides. The user
    sees a one-line 'skipped' notice so they know overrides exist as a
    feature; nothing breaks for unattended setup runs."""
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["setup", "--target", "opencode"])
    assert result.exit_code == 0, result.output
    # The skip notice surfaces so users discover the feature exists.
    assert "non-interactive" in result.output or "Tool overrides skipped" in result.output
    # No override files written.
    assert not (project / ".opencode" / "tools" / "grep.ts").exists()


def test_cli_setup_print_only_previews_overrides_without_writing(
    project: Path, monkeypatch: pytest.MonkeyPatch
):
    """`--print-only` is opt-in for the override step: we *show* what
    would be written so the user can audit it, but we don't ask and we
    don't write. Crucially the user must see *which files* the override
    would land, not just a generic 'override: preview' line."""
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["setup", "--target", "opencode", "--print-only"])
    assert result.exit_code == 0, result.output
    # The per-file preview lines must appear in the report.
    assert "grep.ts" in result.output
    assert "trie_read.ts" in result.output
    assert "trie_trace.ts" in result.output
    # But the disk is untouched.
    assert not (project / ".opencode" / "tools").exists()


def test_cli_setup_claude_code_override_creates_advisory_hook(
    project: Path, monkeypatch: pytest.MonkeyPatch
):
    """For Claude Code, the override path writes a PreToolUse hook file
    (the only available steering mechanism). The hook references
    `mcp__trie__grep` so the agent gets nudged toward the trie tool
    every time it reaches for built-in Grep."""
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["setup", "--target", "claude-code", "--override-builtins"])
    assert result.exit_code == 0, result.output

    hook_path = project / ".claude" / "hooks" / "trie-tools.json"
    assert hook_path.exists()
    assert "mcp__trie__grep" in hook_path.read_text()


def test_cli_setup_override_idempotent_on_second_run(
    project: Path, monkeypatch: pytest.MonkeyPatch
):
    """Second run with `--override-builtins` reports skipped for every
    override file. Same idempotency contract as MCP install and hook
    install — `trie setup` is safe to re-run."""
    monkeypatch.chdir(project)
    runner = CliRunner()
    first = runner.invoke(app, ["setup", "--target", "opencode", "--override-builtins"])
    assert first.exit_code == 0, first.output
    grep_before = (project / ".opencode" / "tools" / "grep.ts").read_text()

    second = runner.invoke(app, ["setup", "--target", "opencode", "--override-builtins"])
    assert second.exit_code == 0, second.output
    # File unchanged.
    assert (project / ".opencode" / "tools" / "grep.ts").read_text() == grep_before
    # And the report mentions skipped for the override files.
    assert "skipped" in second.output
