from __future__ import annotations

import json
import shutil
import sys
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

Scope = Literal["project", "user"]
Action = Literal["created", "updated", "removed", "skipped", "preview", "error"]

SnippetFactory = Callable[[Path], dict]


class MCPInstallError(Exception):
    pass


@dataclass(frozen=True)
class ApplyResult:
    target: str
    action: Action
    path: Path | None
    snippet: dict
    detail: str = ""


def _claude_style_snippet(project_root: Path) -> dict:
    """Snippet shape used by Claude Code, Claude Desktop, Cursor, Windsurf, Codex, and
    VS Code: a `command` string, a list of `args`, and an explicit `cwd` so the spawned
    `trie mcp serve` resolves the correct project root regardless of where the agent
    was launched from."""
    return {
        "command": "trie",
        "args": ["mcp", "serve"],
        "cwd": str(project_root.resolve()),
    }


def _opencode_style_snippet(project_root: Path) -> dict:
    """Snippet shape used by opencode (`type: "local"` with `command` as a single array).

    Unlike Claude, opencode's MCP config doesn't accept a `cwd` field. The server still
    needs to find the right `trie.toml`, so we prepend `--directory` to the command —
    `trie` itself doesn't honour that flag, but the SDK launches the process from the
    project root by default, so omission is acceptable for project-scope installs. For
    user-scope, the agent's own cwd is what trie scopes against."""
    _ = project_root  # cwd is implicit in opencode's spawn semantics
    return {
        "type": "local",
        "command": ["trie", "mcp", "serve"],
        "enabled": True,
    }


@dataclass(frozen=True)
class MCPTarget:
    """Static description of a coding agent / IDE that hosts MCP servers via JSON
    config. The shape is intentionally narrow: targets that don't fit (e.g. Zed,
    which embeds MCP config in a TOML/settings.json) would need their own adapter.

    `snippet_factory` produces the JSON value registered under `snippet_key.trie`.
    The default factory matches the Claude-style schema (`command` + `args` + `cwd`);
    opencode supplies `_opencode_style_snippet` because its schema differs.

    `tool_name_format` is how this harness names MCP tools when the agent sees them.
    The format string takes one `{tool}` placeholder; the trie server itself
    registers tools as `grep`, `read`, and `trace`, but each harness prefixes or
    mangles those names before showing them to the model. We need the rendered
    name to bake into TRIE.md so the doc tells the agent what name to actually
    call. Known formats live in the registry below; unknown harnesses default
    to bare `{tool}` (no prefix), which is the safe fallback — the agent will
    still find the tool via tab-completion / tool listing even when the doc
    name doesn't match exactly."""

    name: str  # short slug used as --target value
    display_name: str
    snippet_key: str = "mcpServers"
    snippet_factory: SnippetFactory = field(default=_claude_style_snippet)
    project_rel_path: tuple[str, ...] | None = None  # relative to project root
    user_path_str: str | None = None  # passed to Path then expanduser-ed
    detect_paths_str: tuple[str, ...] = ()  # any of these existing → installed
    detect_binaries: tuple[str, ...] = ()  # any of these on PATH → installed
    tool_name_format: str = "{tool}"  # how this harness names MCP tools
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

    def snippet(self, project_root: Path) -> dict:
        """Build the JSON value registered for this target under `snippet_key.trie`."""
        return self.snippet_factory(project_root)


def trie_server_snippet(project_root: Path) -> dict:
    """Back-compat shim. New callers should prefer `MCPTarget.snippet(project_root)`
    because different agents expect different shapes. Kept as the Claude-style default
    so existing tests and any external imports continue to work."""
    return _claude_style_snippet(project_root)


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
        # Claude Code namespaces MCP tools as `mcp__<server>__<tool>`. Confirmed
        # from the docs at docs.claude.com/en/docs/claude-code/permissions
        # (the MCP permission-rule example uses `mcp__puppeteer__puppeteer_navigate`).
        tool_name_format="mcp__trie__{tool}",
    ),
    "claude-desktop": MCPTarget(
        name="claude-desktop",
        display_name="Claude Desktop",
        user_path_str=_claude_desktop_user_path(),
        detect_paths_str=(_claude_desktop_user_path(),),
        # Same naming convention as Claude Code (same MCP host implementation).
        tool_name_format="mcp__trie__{tool}",
    ),
    "cursor": MCPTarget(
        name="cursor",
        display_name="Cursor",
        project_rel_path=(".cursor", "mcp.json"),
        user_path_str="~/.cursor/mcp.json",
        detect_paths_str=("~/.cursor",),
        detect_binaries=("cursor",),
        # TODO: confirm Cursor's MCP tool naming convention; defaulting to
        # bare `{tool}` until verified. Agents will still discover the tools
        # via tool listing — the doc just won't show the exact rendered name.
    ),
    "windsurf": MCPTarget(
        name="windsurf",
        display_name="Windsurf",
        user_path_str="~/.codeium/windsurf/mcp_config.json",
        detect_paths_str=("~/.codeium/windsurf",),
        detect_binaries=("windsurf",),
        # TODO: confirm Windsurf's MCP tool naming convention.
    ),
    "vscode": MCPTarget(
        name="vscode",
        display_name="VS Code",
        snippet_key="servers",  # VS Code's workspace mcp.json uses `servers`, not `mcpServers`.
        project_rel_path=(".vscode", "mcp.json"),
        detect_binaries=("code",),
        notes="VS Code reads workspace MCP config from .vscode/mcp.json (project scope only).",
        # TODO: confirm VS Code's MCP tool naming convention (likely depends on
        # which AI extension is reading the config — Copilot Chat vs others).
    ),
    "codex": MCPTarget(
        name="codex",
        display_name="Codex CLI",
        user_path_str="~/.codex/config.json",
        detect_paths_str=("~/.codex",),
        detect_binaries=("codex",),
        notes="Codex CLI MCP config path may evolve; verify after install.",
        # TODO: confirm Codex CLI's MCP tool naming convention.
    ),
    "opencode": MCPTarget(
        name="opencode",
        display_name="opencode",
        # opencode uses `mcp` (not `mcpServers`) under both project and user configs.
        snippet_key="mcp",
        snippet_factory=_opencode_style_snippet,
        project_rel_path=("opencode.json",),
        user_path_str="~/.config/opencode/opencode.json",
        detect_paths_str=("~/.config/opencode", "~/.local/share/opencode"),
        detect_binaries=("opencode",),
        # opencode prefixes MCP tools with `<server-name>_<tool>`. Confirmed
        # from opencode.ai/docs/mcp-servers: "MCP server tools are registered
        # with server name as prefix" (example: `mymcpservername_*`).
        tool_name_format="trie_{tool}",
    ),
}


def detected_target_slugs() -> list[str]:
    """Return the slugs of every registered harness detected on this system.

    Single source of truth for auto-detection so `trie setup`, the hook
    installer, and the MCP installer all agree on which agents are "present".
    Order follows the `TARGETS` registry.

    Detection is deliberately machine-global (an agent's presence is a property
    of the workstation, e.g. `~/.claude.json` or a binary on PATH), not of the
    current repo — see `MCPTarget.detect`. Because a workstation can have
    several agents installed at once, callers that must pick ONE (like the docs
    body, or an interactive `trie setup`) should disambiguate rather than
    assume the first detected slug is the intended one.
    """
    return [slug for slug, target in TARGETS.items() if target.detect()]


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
    snippet = target.snippet(project_root)
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


# ---------------------------------------------------------------------------
# Uninstall: inverse of `install`. Drops the `trie` key from each target's
# config and leaves everything else alone.
# ---------------------------------------------------------------------------


@dataclass
class UninstallPlan:
    """Aggregate result of an `uninstall` call across one or more targets.

    Mirrors `InstallPlan` field-for-field; kept as a separate type so the
    install / uninstall sides can diverge in the future without breaking
    each other's callers and so call sites read clearly when grepped.
    """

    target_names: list[str]
    scope: Scope
    print_only: bool
    dry_run: bool
    results: list[ApplyResult] = field(default_factory=list)


def uninstall(
    *,
    target_names: list[str] | None,
    scope: Scope,
    uninstall_all: bool,
    print_only: bool,
    dry_run: bool,
    project_root: Path,
) -> UninstallPlan:
    """Remove the trie MCP server registration from one or more targets.

    The inverse of `install`. For each target:

      - file missing → `skipped` with detail "no config file at <path>"
      - file present, no `trie` key under `snippet_key` → `skipped` with
        detail "trie not registered in this config"
      - file present, `trie` key present → remove it; report `removed`.
        If removing leaves `snippet_key` empty, drop the key too so the
        config file stays tidy. We never delete the file itself —
        agents own that file; we only own the `trie` entry inside it.

    Auto-detect mirrors `install`: `target.detect()` decides which
    targets are candidates when neither `--target` nor `--all` is given.
    Targets that are detected but have no `trie` entry just come back
    `skipped` — the "no-op uninstall" case.
    """
    if uninstall_all:
        chosen = list(TARGETS.values())
    elif target_names:
        chosen = []
        for name in target_names:
            if name not in TARGETS:
                raise MCPInstallError(f"unknown target: {name!r}. Known: {', '.join(TARGETS)}")
            chosen.append(TARGETS[name])
    else:
        chosen = [t for t in TARGETS.values() if t.detect()]
        if not chosen:
            raise MCPInstallError(
                "no agents detected on this system. Pass --target NAME or --all "
                f"(known: {', '.join(TARGETS)})."
            )

    plan = UninstallPlan(
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
        plan.results.append(_uninstall_one(target, project_root, scope, print_only, dry_run))
    return plan


def _uninstall_one(
    target: MCPTarget,
    project_root: Path,
    scope: Scope,
    print_only: bool,
    dry_run: bool,
) -> ApplyResult:
    """Remove the `trie` entry from one target's config file.

    Same parse-and-merge dance as `_apply_one` in reverse: read JSON,
    delete the `trie` key under `snippet_key`, drop `snippet_key` if it
    becomes empty, write back. We never touch other servers under the
    same key — those are the agent's other MCP integrations and out of
    scope for trie's uninstall.
    """
    config_path = target.config_path(project_root, scope)

    if not config_path.exists():
        return ApplyResult(
            target=target.name,
            action="skipped",
            path=config_path,
            snippet={},
            detail=f"no config file at {config_path}",
        )

    raw = config_path.read_text()
    try:
        data = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError as exc:
        return ApplyResult(
            target=target.name,
            action="error",
            path=config_path,
            snippet={},
            detail=f"existing config is not valid JSON: {exc}",
        )
    if not isinstance(data, dict):
        return ApplyResult(
            target=target.name,
            action="error",
            path=config_path,
            snippet={},
            detail="existing config root is not a JSON object",
        )

    servers = data.get(target.snippet_key)
    if not isinstance(servers, dict) or "trie" not in servers:
        return ApplyResult(
            target=target.name,
            action="skipped",
            path=config_path,
            snippet={},
            detail="trie not registered in this config",
        )

    removed_snippet = servers["trie"]

    if print_only or dry_run:
        return ApplyResult(
            target=target.name,
            action="preview",
            path=config_path,
            snippet=removed_snippet,
            detail="would remove the trie entry",
        )

    del servers["trie"]
    if not servers:
        # Don't leave an empty `mcpServers: {}` behind — drop the key.
        del data[target.snippet_key]

    config_path.write_text(json.dumps(data, indent=2) + "\n")
    return ApplyResult(
        target=target.name,
        action="removed",
        path=config_path,
        snippet=removed_snippet,
    )
