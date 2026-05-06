from __future__ import annotations

import json
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

Scope = Literal["project", "user"]
Action = Literal["created", "updated", "skipped", "preview", "error"]


class MCPInstallError(Exception):
    pass


@dataclass(frozen=True)
class ApplyResult:
    target: str
    action: Action
    path: Path | None
    snippet: dict
    detail: str = ""


@dataclass(frozen=True)
class MCPTarget:
    """Static description of a coding agent / IDE that hosts MCP servers via JSON
    config. The shape is intentionally narrow: targets that don't fit (e.g. Zed,
    which embeds MCP config in a TOML/settings.json) would need their own adapter."""

    name: str  # short slug used as --target value
    display_name: str
    snippet_key: str = "mcpServers"
    project_rel_path: tuple[str, ...] | None = None  # relative to project root
    user_path_str: str | None = None  # passed to Path then expanduser-ed
    detect_paths_str: tuple[str, ...] = ()  # any of these existing → installed
    detect_binaries: tuple[str, ...] = ()  # any of these on PATH → installed
    notes: str = ""

    def supports(self, scope: Scope) -> bool:
        if scope == "project":
            return self.project_rel_path is not None
        return self.user_path_str is not None

    def config_path(self, project_root: Path, scope: Scope) -> Path:
        if scope == "project":
            if self.project_rel_path is None:
                raise MCPInstallError(
                    f"{self.display_name} does not support project-scope install. "
                    "Re-run with --scope user."
                )
            return project_root.joinpath(*self.project_rel_path)
        if self.user_path_str is None:
            raise MCPInstallError(
                f"{self.display_name} does not support user-scope install. "
                "Re-run with --scope project."
            )
        return Path(self.user_path_str).expanduser()

    def detect(self) -> bool:
        if any(Path(s).expanduser().exists() for s in self.detect_paths_str):
            return True
        return any(shutil.which(b) is not None for b in self.detect_binaries)


def trie_server_snippet(project_root: Path) -> dict:
    """The JSON value registered under each target's `mcpServers` (or equivalent) map."""
    return {
        "command": "trie",
        "args": ["mcp", "serve"],
        "cwd": str(project_root.resolve()),
    }


def _claude_desktop_user_path() -> str:
    if sys.platform == "darwin":
        return "~/Library/Application Support/Claude/claude_desktop_config.json"
    if sys.platform == "win32":
        return "~/AppData/Roaming/Claude/claude_desktop_config.json"
    return "~/.config/Claude/claude_desktop_config.json"


# Ordered registry — auto-detect iterates in this order, picks all that match.
TARGETS: dict[str, MCPTarget] = {
    "claude-code": MCPTarget(
        name="claude-code",
        display_name="Claude Code",
        project_rel_path=(".mcp.json",),
        user_path_str="~/.claude.json",
        detect_paths_str=("~/.claude.json", "~/.claude"),
        detect_binaries=("claude",),
    ),
    "claude-desktop": MCPTarget(
        name="claude-desktop",
        display_name="Claude Desktop",
        user_path_str=_claude_desktop_user_path(),
        detect_paths_str=(_claude_desktop_user_path(),),
    ),
    "cursor": MCPTarget(
        name="cursor",
        display_name="Cursor",
        project_rel_path=(".cursor", "mcp.json"),
        user_path_str="~/.cursor/mcp.json",
        detect_paths_str=("~/.cursor",),
        detect_binaries=("cursor",),
    ),
    "windsurf": MCPTarget(
        name="windsurf",
        display_name="Windsurf",
        user_path_str="~/.codeium/windsurf/mcp_config.json",
        detect_paths_str=("~/.codeium/windsurf",),
        detect_binaries=("windsurf",),
    ),
    "vscode": MCPTarget(
        name="vscode",
        display_name="VS Code",
        snippet_key="servers",  # VS Code's workspace mcp.json uses `servers`, not `mcpServers`.
        project_rel_path=(".vscode", "mcp.json"),
        detect_binaries=("code",),
        notes="VS Code reads workspace MCP config from .vscode/mcp.json (project scope only).",
    ),
    "codex": MCPTarget(
        name="codex",
        display_name="Codex CLI",
        user_path_str="~/.codex/config.json",
        detect_paths_str=("~/.codex",),
        detect_binaries=("codex",),
        notes="Codex CLI MCP config path may evolve; verify after install.",
    ),
}


@dataclass
class InstallPlan:
    target_names: list[str]
    scope: Scope
    print_only: bool
    dry_run: bool
    results: list[ApplyResult] = field(default_factory=list)


def install(
    *,
    target_names: list[str] | None,
    scope: Scope,
    install_all: bool,
    print_only: bool,
    dry_run: bool,
    project_root: Path,
) -> InstallPlan:
    """Apply (or preview) the trie MCP server registration to one or more targets."""
    if install_all:
        chosen = list(TARGETS.values())
    elif target_names:
        chosen = []
        for name in target_names:
            if name not in TARGETS:
                raise MCPInstallError(f"unknown target: {name!r}. Known: {', '.join(TARGETS)}")
            chosen.append(TARGETS[name])
    else:
        # Auto-detect.
        chosen = [t for t in TARGETS.values() if t.detect()]
        if not chosen:
            raise MCPInstallError(
                "no agents detected on this system. Pass --target NAME or --all "
                f"(known: {', '.join(TARGETS)})."
            )

    plan = InstallPlan(
        target_names=[t.name for t in chosen],
        scope=scope,
        print_only=print_only,
        dry_run=dry_run,
    )

    for target in chosen:
        if not target.supports(scope):
            plan.results.append(
                ApplyResult(
                    target=target.name,
                    action="skipped",
                    path=None,
                    snippet={},
                    detail=f"does not support {scope} scope",
                )
            )
            continue
        plan.results.append(_apply_one(target, project_root, scope, print_only, dry_run))
    return plan


def _apply_one(
    target: MCPTarget,
    project_root: Path,
    scope: Scope,
    print_only: bool,
    dry_run: bool,
) -> ApplyResult:
    snippet = trie_server_snippet(project_root)
    config_path = target.config_path(project_root, scope)

    if print_only:
        return ApplyResult(
            target=target.name,
            action="preview",
            path=config_path,
            snippet={target.snippet_key: {"trie": snippet}},
        )

    existed_before = config_path.exists()
    if existed_before:
        raw = config_path.read_text()
        try:
            data = json.loads(raw) if raw.strip() else {}
        except json.JSONDecodeError as exc:
            return ApplyResult(
                target=target.name,
                action="error",
                path=config_path,
                snippet=snippet,
                detail=f"existing config is not valid JSON: {exc}",
            )
        if not isinstance(data, dict):
            return ApplyResult(
                target=target.name,
                action="error",
                path=config_path,
                snippet=snippet,
                detail="existing config root is not a JSON object",
            )
    else:
        data = {}

    servers = data.setdefault(target.snippet_key, {})
    if not isinstance(servers, dict):
        return ApplyResult(
            target=target.name,
            action="error",
            path=config_path,
            snippet=snippet,
            detail=f"existing `{target.snippet_key}` is not a JSON object",
        )

    if servers.get("trie") == snippet:
        return ApplyResult(
            target=target.name,
            action="skipped",
            path=config_path,
            snippet=snippet,
            detail="trie server already registered with the same command",
        )

    if dry_run:
        return ApplyResult(target=target.name, action="preview", path=config_path, snippet=snippet)

    servers["trie"] = snippet
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(json.dumps(data, indent=2) + "\n")
    return ApplyResult(
        target=target.name,
        action="updated" if existed_before else "created",
        path=config_path,
        snippet=snippet,
    )
