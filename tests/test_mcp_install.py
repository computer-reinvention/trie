from __future__ import annotations

import json
from pathlib import Path

import pytest
from typer.testing import CliRunner

from trie.cli import app
from trie.mcp_install import (
    TARGETS,
    MCPInstallError,
    install,
    trie_server_snippet,
)


@pytest.fixture
def project(tmp_path: Path) -> Path:
    (tmp_path / "trie.toml").write_text(
        '[trie]\nversion = "0.1.0"\n'
        '[scope]\ninclude = ["**/*.py"]\nexclude = []\n'
        '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
        '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
        'cascade = "anthropic/claude-sonnet-4-6"\n'
        "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
    )
    return tmp_path


# --- snippet shape ---


def test_snippet_uses_serve_subcommand(project: Path):
    snip = trie_server_snippet(project)
    assert snip["command"] == "trie"
    assert snip["args"] == ["mcp", "serve"]
    assert snip["cwd"] == str(project.resolve())


# --- per-target apply: Claude Code (project scope) ---


def test_install_claude_code_creates_file(project: Path):
    plan = install(
        target_names=["claude-code"],
        scope="project",
        install_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    assert len(plan.results) == 1
    r = plan.results[0]
    assert r.action == "created"
    assert r.path == project / ".mcp.json"
    data = json.loads(r.path.read_text())
    assert "trie" in data["mcpServers"]
    assert data["mcpServers"]["trie"]["args"] == ["mcp", "serve"]


def test_install_preserves_other_servers(project: Path):
    existing = {"mcpServers": {"other": {"command": "x", "args": []}}}
    (project / ".mcp.json").write_text(json.dumps(existing))
    plan = install(
        target_names=["claude-code"],
        scope="project",
        install_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    assert plan.results[0].action == "updated"
    data = json.loads((project / ".mcp.json").read_text())
    assert "trie" in data["mcpServers"]
    assert "other" in data["mcpServers"]


def test_install_idempotent_when_unchanged(project: Path):
    install(
        target_names=["claude-code"],
        scope="project",
        install_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    second = install(
        target_names=["claude-code"],
        scope="project",
        install_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    assert second.results[0].action == "skipped"


def test_install_errors_on_unknown_target(project: Path):
    with pytest.raises(MCPInstallError, match="unknown target"):
        install(
            target_names=["bogus"],
            scope="project",
            install_all=False,
            print_only=False,
            dry_run=False,
            project_root=project,
        )


# --- print-only / dry-run ---


def test_install_print_only_writes_no_file(project: Path):
    plan = install(
        target_names=["claude-code"],
        scope="project",
        install_all=False,
        print_only=True,
        dry_run=False,
        project_root=project,
    )
    assert plan.results[0].action == "preview"
    assert not (project / ".mcp.json").exists()


def test_install_dry_run_writes_no_file(project: Path):
    plan = install(
        target_names=["claude-code"],
        scope="project",
        install_all=False,
        print_only=False,
        dry_run=True,
        project_root=project,
    )
    assert plan.results[0].action == "preview"
    assert not (project / ".mcp.json").exists()


# --- VS Code uses `servers`, not `mcpServers` ---


def test_install_vscode_uses_servers_key(project: Path):
    plan = install(
        target_names=["vscode"],
        scope="project",
        install_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    r = plan.results[0]
    assert r.action == "created"
    data = json.loads(r.path.read_text())
    assert "servers" in data
    assert "trie" in data["servers"]
    # And not the other key.
    assert "mcpServers" not in data


# --- malformed config handling ---


def test_install_errors_on_invalid_json(project: Path):
    (project / ".mcp.json").write_text("{not valid json")
    plan = install(
        target_names=["claude-code"],
        scope="project",
        install_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    assert plan.results[0].action == "error"


# --- scope handling ---


def test_install_user_scope_writes_to_user_path(
    project: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    """User-scope install resolves under HOME — redirect HOME so the test stays sandboxed."""
    fake_home = tmp_path / "fakehome"
    fake_home.mkdir()
    monkeypatch.setenv("HOME", str(fake_home))
    plan = install(
        target_names=["claude-code"],
        scope="user",
        install_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    r = plan.results[0]
    assert r.action == "created"
    assert r.path == fake_home / ".claude.json"
    data = json.loads(r.path.read_text())
    assert "trie" in data["mcpServers"]


def test_install_skips_target_without_scope(project: Path):
    """VS Code only supports project scope; --scope user must skip with a clear note."""
    plan = install(
        target_names=["vscode"],
        scope="user",
        install_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    assert plan.results[0].action == "skipped"
    assert "scope" in plan.results[0].detail


# --- detect / auto-detect ---


def test_detect_returns_false_in_clean_environment(monkeypatch: pytest.MonkeyPatch):
    """With every detect path remapped to a non-existent dir and PATH cleared, no
    target should detect as installed."""
    fake_home = Path("/tmp/trie_test_no_such_home_2026")
    monkeypatch.setenv("HOME", str(fake_home))
    monkeypatch.setenv("PATH", "/no/such/path")
    for t in TARGETS.values():
        assert t.detect() is False, f"{t.name} should not detect on clean fixture"


def test_install_auto_detect_errors_when_nothing_found(
    project: Path, monkeypatch: pytest.MonkeyPatch
):
    fake_home = Path("/tmp/trie_test_no_such_home_2026_b")
    monkeypatch.setenv("HOME", str(fake_home))
    monkeypatch.setenv("PATH", "/no/such/path")
    with pytest.raises(MCPInstallError, match="no agents detected"):
        install(
            target_names=None,
            scope="project",
            install_all=False,
            print_only=False,
            dry_run=False,
            project_root=project,
        )


# --- --all ---


def test_install_all_runs_every_target_in_print_mode(project: Path):
    plan = install(
        target_names=None,
        scope="project",
        install_all=True,
        print_only=True,
        dry_run=False,
        project_root=project,
    )
    assert {r.target for r in plan.results} == set(TARGETS)
    # VS Code supports project scope; user-scope-only targets get skipped here.
    actions = {r.target: r.action for r in plan.results}
    assert actions["claude-code"] == "preview"
    assert actions["vscode"] == "preview"
    assert actions["claude-desktop"] == "skipped"  # user-scope only
    assert actions["windsurf"] == "skipped"  # user-scope only


# --- CLI ---


def test_cli_mcp_install_print_only(project: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["mcp", "install", "--target", "claude-code", "--print-only"])
    assert result.exit_code == 0, result.output
    assert "Claude Code" in result.output
    assert "mcp" in result.output and "serve" in result.output


def test_cli_mcp_install_writes_file(project: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["mcp", "install", "--target", "claude-code"])
    assert result.exit_code == 0, result.output
    assert (project / ".mcp.json").exists()
    assert "created" in result.output or "Claude Code" in result.output


def test_cli_mcp_install_unknown_target(project: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["mcp", "install", "--target", "bogus"])
    assert result.exit_code == 1
    assert "unknown target" in result.output


def test_cli_mcp_install_target_and_all_mutex(project: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["mcp", "install", "--target", "claude-code", "--all"])
    assert result.exit_code == 1
    assert "mutually exclusive" in result.output


def test_cli_mcp_serve_dispatches_to_run_stdio(project: Path, monkeypatch: pytest.MonkeyPatch):
    """`trie mcp serve` should call run_stdio with the resolved project root."""
    monkeypatch.chdir(project)
    captured: dict[str, Path] = {}

    def fake_run_stdio(root: Path) -> None:
        captured["root"] = root

    monkeypatch.setattr("trie.cli.run_mcp_stdio", fake_run_stdio)
    runner = CliRunner()
    result = runner.invoke(app, ["mcp", "serve"])
    assert result.exit_code == 0, result.output
    assert captured["root"].resolve() == project.resolve()


def test_cli_mcp_no_subcommand_runs_serve(project: Path, monkeypatch: pytest.MonkeyPatch):
    """Back-compat: `trie mcp` (no subcommand) still starts the server, so existing
    snippets that reference just `trie mcp` keep working."""
    monkeypatch.chdir(project)
    captured: dict[str, Path] = {}

    def fake_run_stdio(root: Path) -> None:
        captured["root"] = root

    monkeypatch.setattr("trie.cli.run_mcp_stdio", fake_run_stdio)
    runner = CliRunner()
    result = runner.invoke(app, ["mcp"])
    assert result.exit_code == 0, result.output
    assert captured["root"].resolve() == project.resolve()
