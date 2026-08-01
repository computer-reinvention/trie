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
    uninstall,
)


@pytest.fixture
def project(tmp_path: Path) -> Path:
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


# --- opencode uses `mcp` and a `type: "local"` snippet shape ---


def test_install_opencode_creates_project_config(project: Path):
    """opencode's project config is `opencode.json` at repo root, with the snippet
    nested under `mcp.trie`."""
    plan = install(
        target_names=["opencode"],
        scope="project",
        install_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    r = plan.results[0]
    assert r.action == "created"
    assert r.path == project / "opencode.json"
    data = json.loads(r.path.read_text())
    assert "mcp" in data
    assert "mcpServers" not in data  # opencode uses a different key
    trie_entry = data["mcp"]["trie"]
    assert trie_entry["type"] == "local"
    assert trie_entry["command"] == ["trie", "mcp", "serve"]
    assert trie_entry["enabled"] is True
    # opencode snippets do not carry a `cwd` field — its absence is part of the shape.
    assert "cwd" not in trie_entry


def test_install_opencode_user_scope_lands_in_config_dir(
    project: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    """User-scope install resolves to `~/.config/opencode/opencode.json`."""
    fake_home = tmp_path / "fakehome"
    fake_home.mkdir()
    monkeypatch.setenv("HOME", str(fake_home))
    plan = install(
        target_names=["opencode"],
        scope="user",
        install_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    r = plan.results[0]
    assert r.action == "created"
    assert r.path == fake_home / ".config" / "opencode" / "opencode.json"
    data = json.loads(r.path.read_text())
    assert data["mcp"]["trie"]["type"] == "local"


def test_install_opencode_preserves_existing_mcp_servers(project: Path):
    """When opencode.json already has other MCP servers, we add `trie` alongside
    rather than clobbering them."""
    existing = {
        "$schema": "https://opencode.ai/config.json",
        "mcp": {
            "context7": {
                "type": "remote",
                "url": "https://mcp.context7.com/mcp",
            }
        },
    }
    (project / "opencode.json").write_text(json.dumps(existing))
    plan = install(
        target_names=["opencode"],
        scope="project",
        install_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    assert plan.results[0].action == "updated"
    data = json.loads((project / "opencode.json").read_text())
    assert "trie" in data["mcp"]
    assert "context7" in data["mcp"]
    # Non-mcp keys (the schema URL) survive too.
    assert data["$schema"] == "https://opencode.ai/config.json"


def test_install_opencode_idempotent_when_unchanged(project: Path):
    install(
        target_names=["opencode"],
        scope="project",
        install_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    second = install(
        target_names=["opencode"],
        scope="project",
        install_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    assert second.results[0].action == "skipped"


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


def test_detected_target_slugs_empty_on_clean_environment(monkeypatch: pytest.MonkeyPatch):
    """`detected_target_slugs` returns [] when nothing is installed."""
    from trie.mcp_install import detected_target_slugs

    fake_home = Path("/tmp/trie_test_no_such_home_2026_slugs")
    monkeypatch.setenv("HOME", str(fake_home))
    monkeypatch.setenv("PATH", "/no/such/path")
    assert detected_target_slugs() == []


def test_detected_target_slugs_reports_installed_in_registry_order(
    monkeypatch: pytest.MonkeyPatch,
):
    """When several agents detect, the helper lists their slugs in registry
    order — the single source of truth setup uses to decide whether to prompt."""
    # Force claude-code and opencode to detect, everything else not.
    # MCPTarget is frozen, so patch the class method to consult self.name.
    from trie.mcp_install import MCPTarget, detected_target_slugs

    installed = {"claude-code", "opencode"}
    monkeypatch.setattr(MCPTarget, "detect", lambda self: self.name in installed)

    slugs = detected_target_slugs()
    assert set(slugs) == installed
    # Registry order: claude-code is defined before opencode.
    assert slugs.index("claude-code") < slugs.index("opencode")


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
    # VS Code, opencode, claude-code, cursor all support project scope; user-scope-only
    # targets get skipped here.
    actions = {r.target: r.action for r in plan.results}
    assert actions["claude-code"] == "preview"
    assert actions["vscode"] == "preview"
    assert actions["opencode"] == "preview"
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


def test_cli_mcp_no_subcommand_prints_help(project: Path, monkeypatch: pytest.MonkeyPatch):
    """`trie mcp` with no subcommand must print help and exit non-zero (typer's
    standard no-args-is-help behaviour). Earlier versions silently ran the stdio
    server, which is hostile when a human types it at a terminal."""
    monkeypatch.chdir(project)
    captured: dict[str, Path] = {}

    def fake_run_stdio(root: Path) -> None:
        captured["root"] = root

    monkeypatch.setattr("trie.cli.run_mcp_stdio", fake_run_stdio)
    runner = CliRunner()
    result = runner.invoke(app, ["mcp"])
    # typer's no_args_is_help renders help and exits with code 2 (missing command).
    assert result.exit_code == 2
    assert "serve" in result.output
    assert "install" in result.output
    # And critically, the server must NOT have been started.
    assert "root" not in captured


# ---------------------------------------------------------------------------
# Uninstall: inverse of install. Drops the `trie` entry from each target's
# config file, leaving the file (and other servers under the same key)
# alone.
# ---------------------------------------------------------------------------


def test_uninstall_removes_trie_entry(project: Path):
    """Install then uninstall: the `trie` key under `mcpServers` is gone
    from the config file, but the file still exists and is valid JSON."""
    install(
        target_names=["claude-code"],
        scope="project",
        install_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    config = project / ".mcp.json"
    assert "trie" in json.loads(config.read_text())["mcpServers"]

    plan = uninstall(
        target_names=["claude-code"],
        scope="project",
        uninstall_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    assert len(plan.results) == 1
    r = plan.results[0]
    assert r.action == "removed"
    assert r.path == config
    # File still exists; trie key gone.
    assert config.exists()
    data = json.loads(config.read_text())
    # `mcpServers` was emptied → dropped entirely so the config stays tidy.
    assert "mcpServers" not in data
    # The snippet that was removed is reported back for the user's audit trail.
    assert r.snippet["args"] == ["mcp", "serve"]


def test_uninstall_preserves_other_servers(project: Path):
    """Uninstall must touch only the `trie` key. Other MCP servers
    registered alongside trie stay put. This is the load-bearing
    invariant: agents have their own integrations; uninstall must not
    nuke them."""
    config = project / ".mcp.json"
    config.write_text(
        json.dumps(
            {
                "mcpServers": {
                    "trie": {"command": "trie", "args": ["mcp", "serve"]},
                    "other-tool": {"command": "other", "args": ["serve"]},
                },
                "unrelated_top_level_key": "preserve-me",
            },
            indent=2,
        )
        + "\n"
    )

    plan = uninstall(
        target_names=["claude-code"],
        scope="project",
        uninstall_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    assert plan.results[0].action == "removed"

    data = json.loads(config.read_text())
    # `mcpServers` survives because `other-tool` is still in it.
    assert "trie" not in data["mcpServers"]
    assert "other-tool" in data["mcpServers"]
    assert data["unrelated_top_level_key"] == "preserve-me"


def test_uninstall_when_not_installed_is_skipped(project: Path):
    """Uninstalling from a target where trie was never registered: the
    config file may not even exist. Either way, the result is `skipped`
    with a detail explaining what we saw — never an error."""
    plan = uninstall(
        target_names=["claude-code"],
        scope="project",
        uninstall_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    r = plan.results[0]
    assert r.action == "skipped"
    assert "no config file" in r.detail.lower()


def test_uninstall_when_config_has_no_trie_key_is_skipped(project: Path):
    """Config file exists with other servers, but no `trie` entry. We
    must not touch the file; the result is `skipped` with a clear
    detail."""
    config = project / ".mcp.json"
    config.write_text(
        json.dumps(
            {"mcpServers": {"other-tool": {"command": "other"}}},
            indent=2,
        )
        + "\n"
    )
    plan = uninstall(
        target_names=["claude-code"],
        scope="project",
        uninstall_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    r = plan.results[0]
    assert r.action == "skipped"
    assert "trie not registered" in r.detail.lower()
    # The other server is still there, byte-for-byte.
    data = json.loads(config.read_text())
    assert data["mcpServers"]["other-tool"]["command"] == "other"


def test_uninstall_dry_run_does_not_modify_file(project: Path):
    """`--dry-run` returns a `preview` action and writes nothing."""
    install(
        target_names=["claude-code"],
        scope="project",
        install_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    config = project / ".mcp.json"
    before = config.read_text()

    plan = uninstall(
        target_names=["claude-code"],
        scope="project",
        uninstall_all=False,
        print_only=False,
        dry_run=True,
        project_root=project,
    )
    assert plan.results[0].action == "preview"
    # File is byte-identical.
    assert config.read_text() == before


def test_uninstall_print_only_does_not_modify_file(project: Path):
    """`--print-only` is the same as dry-run for uninstall: render the
    plan, write nothing."""
    install(
        target_names=["claude-code"],
        scope="project",
        install_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    config = project / ".mcp.json"
    before = config.read_text()

    plan = uninstall(
        target_names=["claude-code"],
        scope="project",
        uninstall_all=False,
        print_only=True,
        dry_run=False,
        project_root=project,
    )
    assert plan.results[0].action == "preview"
    assert config.read_text() == before


def test_uninstall_all_targets(project: Path):
    """`uninstall_all=True` walks every target in the registry. Each
    target that supports project scope and was previously registered
    comes back `removed`; the rest come back `skipped`."""
    # Install for two targets that support project scope.
    install(
        target_names=["claude-code", "opencode"],
        scope="project",
        install_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )

    plan = uninstall(
        target_names=None,
        scope="project",
        uninstall_all=True,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    # All registered targets were walked.
    assert {t for t in plan.target_names} == set(TARGETS.keys())
    # The two we installed are removed; the rest are skipped.
    by_target = {r.target: r for r in plan.results}
    assert by_target["claude-code"].action == "removed"
    assert by_target["opencode"].action == "removed"
    # Targets that don't support project scope come back skipped with the
    # scope-mismatch detail.
    assert by_target["claude-desktop"].action == "skipped"


def test_uninstall_unknown_target_raises():
    """Symmetric with install: unknown slugs raise `MCPInstallError`
    immediately, not silently skipped."""
    with pytest.raises(MCPInstallError, match="unknown target"):
        uninstall(
            target_names=["not-a-real-agent"],
            scope="project",
            uninstall_all=False,
            print_only=False,
            dry_run=False,
            project_root=Path("/tmp/anywhere"),
        )


def test_uninstall_invalid_json_returns_error(project: Path):
    """A corrupt config file produces an `error` result, not a crash.
    The file is left untouched so the user can fix it by hand."""
    config = project / ".mcp.json"
    config.write_text("{this is not valid json")
    plan = uninstall(
        target_names=["claude-code"],
        scope="project",
        uninstall_all=False,
        print_only=False,
        dry_run=False,
        project_root=project,
    )
    r = plan.results[0]
    assert r.action == "error"
    assert "not valid json" in r.detail.lower()
    # File untouched.
    assert config.read_text() == "{this is not valid json"


# --- CLI surface ---


def test_cli_mcp_uninstall_round_trips(project: Path, monkeypatch: pytest.MonkeyPatch):
    """End-to-end: `trie mcp install` then `trie mcp uninstall` returns
    the config file to a trie-free state. The CLI surface stays in sync
    with the library surface."""
    monkeypatch.chdir(project)
    runner = CliRunner()
    install_result = runner.invoke(app, ["mcp", "install", "--target", "claude-code"])
    assert install_result.exit_code == 0, install_result.output
    assert (project / ".mcp.json").exists()

    uninstall_result = runner.invoke(app, ["mcp", "uninstall", "--target", "claude-code"])
    assert uninstall_result.exit_code == 0, uninstall_result.output
    assert "removed" in uninstall_result.output.lower()
    data = json.loads((project / ".mcp.json").read_text())
    assert "mcpServers" not in data


def test_cli_mcp_uninstall_rejects_target_and_all_together(
    project: Path, monkeypatch: pytest.MonkeyPatch
):
    """`--target` and `--all` are mutually exclusive on uninstall, same
    as install."""
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["mcp", "uninstall", "--target", "claude-code", "--all"])
    assert result.exit_code == 1
    assert "mutually exclusive" in result.output


def test_cli_mcp_help_lists_uninstall(project: Path, monkeypatch: pytest.MonkeyPatch):
    """The `trie mcp` help screen must mention `uninstall` so users can
    discover the command without reading the source."""
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["mcp"])
    # no_args_is_help → exit 2 with help on stdout.
    assert result.exit_code == 2
    assert "uninstall" in result.output
