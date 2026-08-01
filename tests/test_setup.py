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
        '[trie]\nversion = "0.1.2"\n'
        '[scope]\ninclude = ["**/*.py"]\nexclude = []\n'
        '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
        '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
        'cascade = "anthropic/claude-sonnet-4-6"\n'
        "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
    )
    yield tmp_path
    # Cleanup any residue that may have leaked outside tmp_path
    for p in (Path.cwd(), Path.home()):
        (p / ".mcp.json").unlink(missing_ok=True)
        claude = p / ".claude"
        if claude.exists():
            import shutil

            shutil.rmtree(claude, ignore_errors=True)


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
    # Key wiring: the plugin listens for `session.status` with idle status
    # (the new non-deprecated event) and runs the graph-only sync.
    assert "session.status" in contents
    assert '"idle"' in contents
    assert "trie sync --graph-only --after-turn" in contents
    # The plugin MUST default-export a PluginModule shape with `id`. opencode's
    # v1 loader (`readV1Plugin`) requires path plugins to carry an `id`, and
    # the legacy named-export path is being phased out.
    assert "export default" in contents
    assert '"trie-refresh"' in contents
    # The package.json baseline must land alongside the plugin to pre-empt
    # opencode's `@opencode-ai/plugin@local` resolution failure.
    pkg_json = project / ".opencode" / "package.json"
    assert pkg_json.exists()
    data = json.loads(pkg_json.read_text())
    assert data["dependencies"]["@opencode-ai/plugin"]


def test_opencode_hook_writes_package_json_to_unblock_bun_install(project: Path):
    """opencode runs `bun install` against `.opencode/` at startup; without a
    baseline `package.json`, an older opencode build could leave the directory
    pinned to `@opencode-ai/plugin@local` which then fails to resolve and
    silently breaks every prompt (anomalyco/opencode#28286). We ship a known-
    good baseline pointing at the `"latest"` tag — opencode's arborist will
    overwrite the version with the running opencode version on first install,
    which is a real published version and resolves cleanly.
    """
    install(
        target_names=["opencode"],
        install_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    pkg_json = project / ".opencode" / "package.json"
    assert pkg_json.exists()
    data = json.loads(pkg_json.read_text())
    assert data["dependencies"]["@opencode-ai/plugin"] == "latest"


def test_opencode_hook_package_json_is_idempotent(project: Path):
    """A second run with the same support file content reports nothing
    surprising — the package.json contents are stable and we don't keep
    rewriting them."""
    install(
        target_names=["opencode"],
        install_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    pkg_path = project / ".opencode" / "package.json"
    before = pkg_path.read_text()
    install(
        target_names=["opencode"],
        install_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    assert pkg_path.read_text() == before


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
    assert "session.status" in plugin_path.read_text()


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
    assert "session.status" in plan.results[0].contents
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
    assert "trie sync --graph-only" in result.detail


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
    assert "trie sync --graph-only" in result.detail


# ---------------------------------------------------------------------------
# CLI: `trie setup` end-to-end
# ---------------------------------------------------------------------------


def test_cli_setup_opencode_writes_hook_and_overrides_by_default(
    project: Path, monkeypatch: pytest.MonkeyPatch
):
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["setup", "--target", "opencode"])
    assert result.exit_code == 0, result.output

    # MCP config NOT written by default.
    assert not (project / "opencode.json").exists()

    # Hook plugin written.
    hook_path = project / ".opencode" / "plugins" / "trie-refresh.ts"
    assert hook_path.exists()
    assert "session.status" in hook_path.read_text()
    # And the package.json baseline that lets `@opencode-ai/plugin` resolve.
    assert (project / ".opencode" / "package.json").exists()


def test_cli_setup_opencode_with_mcp_writes_mcp(project: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["setup", "--target", "opencode", "--with-mcp"])
    assert result.exit_code == 0, result.output

    # MCP config written when --with-mcp is passed.
    mcp_path = project / "opencode.json"
    assert mcp_path.exists()
    mcp_data = json.loads(mcp_path.read_text())
    assert "trie" in mcp_data["mcp"]

    # Hook plugin also written.
    hook_path = project / ".opencode" / "plugins" / "trie-refresh.ts"
    assert hook_path.exists()
    assert "session.status" in hook_path.read_text()
    assert (project / ".opencode" / "package.json").exists()


def test_cli_setup_claude_code_warns_about_hook(project: Path, monkeypatch: pytest.MonkeyPatch):
    """Agents without hook automation: hook warns. Exit code stays 0 because
    manual-setup isn't a failure. MCP is NOT written by default."""
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["setup", "--target", "claude-code"])
    assert result.exit_code == 0, result.output

    assert not (project / ".mcp.json").exists()
    assert "manual setup required" in result.output


def test_cli_setup_claude_code_with_mcp_writes_mcp_and_warns_about_hook(
    project: Path, monkeypatch: pytest.MonkeyPatch
):
    """With --with-mcp: MCP succeeds, hook warns. Exit code stays 0."""
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["setup", "--target", "claude-code", "--with-mcp"])
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
    assert "session.status" in result.output


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

    # Capture hook file content (MCP is not written by default).
    hook_before = (project / ".opencode" / "plugins" / "trie-refresh.ts").read_text()

    second = runner.invoke(app, ["setup", "--target", "opencode"])
    assert second.exit_code == 0, second.output

    assert (project / ".opencode" / "plugins" / "trie-refresh.ts").read_text() == hook_before


# ---------------------------------------------------------------------------
# CLI: `trie setup` tool-override behaviour
# ---------------------------------------------------------------------------
#
# Tool overrides install by default; `--no-overrides` is the only flag for
# the user to opt out. Idempotency comes from the underlying installer:
# re-running `setup` reports each file as `skipped` when content matches,
# `updated` when it drifted, `created` when missing.


def test_cli_setup_installs_overrides_by_default(project: Path, monkeypatch: pytest.MonkeyPatch):
    """Bare `trie setup --target opencode` installs the override files
    without any opt-in flag or prompt. The user gets hook + docs + overrides
    in one invocation; MCP requires --with-mcp."""
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["setup", "--target", "opencode"])
    assert result.exit_code == 0, result.output

    # All three opencode override files landed.
    assert (project / ".opencode" / "tools" / "grep.ts").exists()
    assert (project / ".opencode" / "tools" / "read.ts").exists()
    assert (project / ".opencode" / "tools" / "trace.ts").exists()


def test_cli_setup_no_overrides_flag_skips_overrides(
    project: Path, monkeypatch: pytest.MonkeyPatch
):
    """`--no-overrides` skips the tool-override step. Hook + docs still run;
    MCP is still skipped by default; only `.opencode/tools/` stays empty."""
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["setup", "--target", "opencode", "--no-overrides"])
    assert result.exit_code == 0, result.output
    # Hook + docs still ran; MCP was not written (no --with-mcp).
    assert not (project / "opencode.json").exists()
    assert (project / ".opencode" / "plugins" / "trie-refresh.ts").exists()
    # But no override files.
    assert not (project / ".opencode" / "tools" / "grep.ts").exists()
    assert not (project / ".opencode" / "tools" / "read.ts").exists()
    assert not (project / ".opencode" / "tools" / "trace.ts").exists()


def test_cli_setup_print_only_previews_overrides_without_writing(
    project: Path, monkeypatch: pytest.MonkeyPatch
):
    """`--print-only` shows every file the override step *would* write so
    the user can audit before committing. Disk untouched. Per-file preview
    lines appear in the report so the user knows which files are involved."""
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["setup", "--target", "opencode", "--print-only"])
    assert result.exit_code == 0, result.output
    # The per-file preview lines must appear in the report.
    assert "grep.ts" in result.output
    assert "read.ts" in result.output
    assert "trace.ts" in result.output
    # But the disk is untouched.
    assert not (project / ".opencode" / "tools").exists()


def test_cli_setup_claude_code_creates_advisory_hook_by_default(
    project: Path, monkeypatch: pytest.MonkeyPatch
):
    """For Claude Code, the override path writes a PreToolUse hook file
    (the only available steering mechanism). Same default-on behaviour as
    opencode: no flag needed. The hook references `mcp__trie__grep` so the
    agent gets nudged toward the trie tool every time it reaches for
    built-in Grep."""
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["setup", "--target", "claude-code"])
    assert result.exit_code == 0, result.output

    hook_path = project / ".claude" / "hooks" / "trie-tools.json"
    assert hook_path.exists()
    assert "mcp__trie__grep" in hook_path.read_text()


def test_cli_setup_override_idempotent_on_second_run(
    project: Path, monkeypatch: pytest.MonkeyPatch
):
    """Second run of `setup` reports skipped for every override file when
    content hasn't drifted. Same idempotency contract as MCP install and
    hook install — `trie setup` is safe to re-run as the install path AND
    as a reinstall path."""
    monkeypatch.chdir(project)
    runner = CliRunner()
    first = runner.invoke(app, ["setup", "--target", "opencode"])
    assert first.exit_code == 0, first.output
    grep_before = (project / ".opencode" / "tools" / "grep.ts").read_text()

    second = runner.invoke(app, ["setup", "--target", "opencode"])
    assert second.exit_code == 0, second.output
    # File unchanged.
    assert (project / ".opencode" / "tools" / "grep.ts").read_text() == grep_before
    # And the report mentions skipped for the override files.
    assert "skipped" in second.output


# ---------------------------------------------------------------------------
# Multiple detected agents: disambiguation prompt
# ---------------------------------------------------------------------------


def test_cli_setup_prompts_when_multiple_agents_detected(
    project: Path, monkeypatch: pytest.MonkeyPatch
):
    """When no --target is given and several agents are installed on the
    machine, setup must ASK rather than silently wire all of them (which would
    set up a globally-installed agent the user doesn't use in this repo). We
    force both claude-code and opencode to 'detect', make the session look
    interactive, and answer the prompt with 'opencode' — only opencode should
    get wired."""
    monkeypatch.chdir(project)
    monkeypatch.setattr(
        "trie.mcp_install.detected_target_slugs", lambda: ["claude-code", "opencode"]
    )
    monkeypatch.setattr("trie.cli._is_interactive", lambda: True)

    runner = CliRunner()
    result = runner.invoke(app, ["setup"], input="opencode\n")
    assert result.exit_code == 0, result.output
    # The prompt was shown.
    assert "Multiple coding agents detected" in result.output
    # opencode got wired (its hook plugin exists) …
    assert (project / ".opencode" / "plugins" / "trie-refresh.ts").exists()
    # … and claude-code did NOT (no advisory hook file).
    assert not (project / ".claude" / "hooks" / "trie-tools.json").exists()


def test_cli_setup_non_interactive_does_not_prompt(project: Path, monkeypatch: pytest.MonkeyPatch):
    """Non-interactive (no tty): setup must NOT block on a prompt. It falls
    back to wiring all detected agents so scripts and CI keep working. Here
    only opencode detects, so it should be set up with no prompt shown."""
    monkeypatch.chdir(project)
    monkeypatch.setattr("trie.mcp_install.detected_target_slugs", lambda: ["opencode"])
    monkeypatch.setattr("trie.cli._is_interactive", lambda: False)

    runner = CliRunner()
    result = runner.invoke(app, ["setup"])
    assert result.exit_code == 0, result.output
    assert "Multiple coding agents detected" not in result.output
    assert (project / ".opencode" / "plugins" / "trie-refresh.ts").exists()


def test_prompt_select_targets_parses_numbers_slugs_and_all(monkeypatch: pytest.MonkeyPatch):
    """`_prompt_select_targets` accepts a comma-separated mix of list numbers
    and slugs, dedupes, preserves detection order, and honours 'all'. Empty
    input takes the recommended default (the lone override target)."""
    from trie import cli as cli_mod
    from trie.reporter import Reporter

    reporter = Reporter()
    detected = ["claude-code", "opencode"]

    # Number selection: "2" -> opencode.
    monkeypatch.setattr(cli_mod.typer, "prompt", lambda *a, **k: "2")
    assert cli_mod._prompt_select_targets(reporter, detected) == ["opencode"]

    # Slug selection with whitespace and dupes -> ordered, deduped.
    monkeypatch.setattr(cli_mod.typer, "prompt", lambda *a, **k: "opencode, opencode, claude-code")
    assert cli_mod._prompt_select_targets(reporter, detected) == ["claude-code", "opencode"]

    # 'all' -> everything detected.
    monkeypatch.setattr(cli_mod.typer, "prompt", lambda *a, **k: "all")
    assert cli_mod._prompt_select_targets(reporter, detected) == ["claude-code", "opencode"]

    # Empty input -> recommended default (single override target present).
    monkeypatch.setattr(cli_mod.typer, "prompt", lambda *a, **k: "")
    assert cli_mod._prompt_select_targets(reporter, detected) == ["opencode"]
