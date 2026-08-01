---
trie_version: 0.2.1
source: trie/mcp_install.py
file_fingerprint: 1b76508578d1b191c74c9ccb0d95ffa57d07baa3e851daaf34b177682dd8a68d
last_synced_at: '2026-08-01T09:20:20Z'
defines:
- kind: module
  qualified_name: trie/mcp_install:__module__
  lines: 1-529
- kind: constant
  qualified_name: trie/mcp_install:Scope
  lines: 11-11
- kind: constant
  qualified_name: trie/mcp_install:Action
  lines: 12-12
- kind: constant
  qualified_name: trie/mcp_install:SnippetFactory
  lines: 14-14
- kind: class
  qualified_name: trie/mcp_install:MCPInstallError
  lines: 17-18
- kind: class
  qualified_name: trie/mcp_install:ApplyResult
  lines: 22-27
- kind: function
  qualified_name: trie/mcp_install:_claude_style_snippet
  lines: 30-39
- kind: function
  qualified_name: trie/mcp_install:_opencode_style_snippet
  lines: 42-55
- kind: class
  qualified_name: trie/mcp_install:MCPTarget
  lines: 59-116
- kind: method
  qualified_name: trie/mcp_install:MCPTarget.supports
  lines: 89-92
- kind: method
  qualified_name: trie/mcp_install:MCPTarget.config_path
  lines: 94-107
- kind: method
  qualified_name: trie/mcp_install:MCPTarget.detect
  lines: 109-112
- kind: method
  qualified_name: trie/mcp_install:MCPTarget.snippet
  lines: 114-116
- kind: function
  qualified_name: trie/mcp_install:trie_server_snippet
  lines: 119-123
- kind: function
  qualified_name: trie/mcp_install:_claude_desktop_user_path
  lines: 126-131
- kind: constant
  qualified_name: trie/mcp_install:TARGETS
  lines: 135-209
- kind: function
  qualified_name: trie/mcp_install:detected_target_slugs
  lines: 212-226
- kind: class
  qualified_name: trie/mcp_install:InstallPlan
  lines: 230-235
- kind: function
  qualified_name: trie/mcp_install:install
  lines: 238-285
- kind: function
  qualified_name: trie/mcp_install:_apply_one
  lines: 288-360
- kind: class
  qualified_name: trie/mcp_install:UninstallPlan
  lines: 370-382
- kind: function
  qualified_name: trie/mcp_install:uninstall
  lines: 385-447
- kind: function
  qualified_name: trie/mcp_install:_uninstall_one
  lines: 450-528
incoming_refs: 56
outgoing_refs: 0
---
<!-- trie:section symbol=trie/mcp_install:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=8baeeb0f357dad4074a9114249ef07894c4af0ca9fa85cea42ce3d3eca47217d source_ref=6b04051d96622258266e38c4d8fc0905613a34ce role=agent-integration -->
Manages MCP (Model Context Protocol) server registration for trie across various AI coding agents and IDEs.

- Supports both project-scope (`.mcp.json`, `.cursor/mcp.json`) and user-scope (`~/.claude.json`) installations
- Handles agent-specific config formats (Claude, Cursor, Windsurf, VS Code, opencode, etc.)
- Auto-detects installed agents via config paths and binary presence
- Provides install/uninstall operations with dry-run and preview modes
- Generates agent-appropriate JSON snippets with correct command structure and working directory
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:Scope fingerprint=d12ea4ff19e63ba188c524bde1d23431cddd8bb548648d958a80898366b86958 body_fp=b735450f778e32676ff6e4b5e5e1b3046b66fd22139daad35998b997573f40ce source_ref=6b04051d96622258266e38c4d8fc0905613a34ce role=agent-integration -->
Type alias defining installation scope options for MCP server registration.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:Action fingerprint=1c60756f67dd341e644d4277839371345319686f7c9ddcef385cf46f6e8cc4a5 body_fp=eae66fe0d7dd26ee745d45c0b3100bfa0f0e514b3bd7dbf841ada548532ac232 source_ref=6b04051d96622258266e38c4d8fc0905613a34ce role=agent-integration -->
Type alias defining possible outcomes when applying MCP server configuration changes.

- `created` — new configuration file was written
- `updated` — existing configuration file was modified  
- `removed` — trie entry was deleted from configuration
- `skipped` — no changes made (already configured or unsupported)
- `preview` — dry-run mode, shows what would happen
- `error` — operation failed due to invalid JSON or other issues
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:SnippetFactory fingerprint=93c2a5173f07fcf25ba5724d0f0ae74f5ec427a1b364965f613ba2a6d9d59eb3 body_fp=1770c035c7d8a969ec42c511b0acd7e13edbede7233b4ac6c99b38fb4ec2001f source_ref=6b04051d96622258266e38c4d8fc0905613a34ce role=agent-integration -->
Type alias for functions that generate MCP server JSON configuration snippets from project paths.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:MCPInstallError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=cb654b652bbfa0d25ab1f78fae662d59e00925448076f92f9b3662e2c0127fe5 source_ref=6b04051d96622258266e38c4d8fc0905613a34ce role=agent-integration -->
Exception raised when MCP server installation or uninstallation fails.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:ApplyResult fingerprint=837f4beba3d4bf388af0b76bb1c1cd73522d4e781b191c72e0ff3a0d22bb56f8 body_fp=f7d34816629307a7127713f774fcca6c334fa1a5a502cbf556ad106cfbdac33f source_ref=6b04051d96622258266e38c4d8fc0905613a34ce role=agent-integration -->
Represents the outcome of applying MCP server configuration to a single target.

- `target`: name of the MCP target (e.g., "claude-desktop")
- `action`: what happened - "created", "updated", "removed", "skipped", "preview", or "error"
- `path`: config file path that was modified, or None if operation was skipped
- `snippet`: JSON configuration that was added/removed/would be applied
- `detail`: optional human-readable explanation for skipped/error actions
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:_claude_style_snippet fingerprint=57f6465b6c54d4d2fbbaab06e3cc4fab6e782ad55e0c53e3bbea72c053aba9cc body_fp=09945046473aabab3798bd06b031dbec3b7ba7c9ae2202f3c3f7078aa5066fd0 source_ref=6b04051d96622258266e38c4d8fc0905613a34ce role=agent-integration -->
Generates MCP server configuration snippet for Claude-style agents with explicit working directory.

- Returns dict with `command`, `args`, and `cwd` fields for spawning `trie mcp serve`
- Used by Claude Code, Claude Desktop, Cursor, Windsurf, Codex, and VS Code
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:_opencode_style_snippet fingerprint=882e5910393a9e41e24e4c42cc0bd620bd10b9177bed1c9cb47d6980a480a003 body_fp=5e39edbed9bb09a5f8e049810df7af95928ca418b8cad51d1a8b8a0eb1d3efe7 source_ref=6b04051d96622258266e38c4d8fc0905613a34ce role=agent-integration -->
Creates opencode-specific MCP server configuration snippet with `type: "local"` schema.

- Returns dict with `type`, `command` array, and `enabled` fields
- Omits `cwd` field since opencode doesn't support it (relies on implicit project root spawning)
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:MCPTarget fingerprint=070d4c0ad55ae4ecd4f770fbcbbe6d66e3c83e34765d033cbaeae11990b2565b body_fp=c750c3ae356762bfe23dc1d50f03b36b5f0604ca4b789515e3804fac915345aa source_ref=6b04051d96622258266e38c4d8fc0905613a34ce role=agent-integration -->
Represents a coding agent or IDE that can host MCP servers through JSON configuration files.

- `supports(scope)`: returns whether this target supports project or user scope installation
- `config_path(project_root, scope)`: resolves the target's JSON config file path for the given scope
- `detect()`: returns True if this target is installed by checking filesystem paths and binaries
- `snippet(project_root)`: generates the JSON configuration snippet for registering trie's MCP server
- `snippet_factory`: callable that produces the JSON structure (defaults to Claude-style format)
- `tool_name_format`: format string for how this target names MCP tools (e.g. "mcp__trie__{tool}")
- `snippet_key`: JSON key under which MCP servers are registered (defaults to "mcpServers")
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:MCPTarget.supports fingerprint=79787e5e066fab97ba91f8b46938abb196bdba7a02388d1f6440a7065809f7ac body_fp=73dacb4c9dd357cc9d7867e72e39be123ff86ce7a7feba7a10d2a6f62dcb211e source_ref=6b04051d96622258266e38c4d8fc0905613a34ce role=agent-integration -->
Returns True if MCPTarget supports the given installation scope.

- Returns True for "project" scope when `project_rel_path` is configured
- Returns True for "user" scope when `user_path_str` is configured
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:MCPTarget.config_path fingerprint=729c7dfaf00b1c7b4844734927972034ff00ab63cecf6d305583e60774525f10 body_fp=cd48c27b527bf2c4a63bc9361d549e3271d4d97d6ab7bf2c2328eefc1c566ac2 source_ref=6b04051d96622258266e38c4d8fc0905613a34ce role=agent-integration -->
Returns the configuration file path for MCPTarget based on scope and project root.

- Raises MCPInstallError if the target doesn't support the requested scope
- For project scope: joins project_root with project_rel_path components
- For user scope: expands user_path_str with home directory substitution
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:MCPTarget.detect fingerprint=35d47b088004403ab404b5527c337ad0ed667df17158764920d9b1c82547c4c1 body_fp=7820b3bb6e22e4e6b951e75e7ced35986d31ca07ae71f42d15849197f67c410e source_ref=6b04051d96622258266e38c4d8fc0905613a34ce role=agent-integration -->
Returns True if MCPTarget detects this agent is installed on the system by checking filesystem paths or PATH binaries.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:MCPTarget.snippet fingerprint=a4c3ce181119b0a706a42a416fa07184eeea2f71c67a53dafa00410ff59420df body_fp=03252b475b3ec756af18d7104cd0bcca3f8a12ccb64aa26ace7a8442b0e80019 source_ref=6b04051d96622258266e38c4d8fc0905613a34ce role=agent-integration -->
MCPTarget.snippet builds the JSON value registered for this target under `snippet_key.trie` by delegating to the configured snippet factory.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:trie_server_snippet fingerprint=14b918f3e0d1bc9c66c0d49dfbc76270c39ecd16011d07500a29bcb9d7feda79 body_fp=28627a82f71993c08a939aa207a2201985734e0880fbf62a40b90ddf7a39114e source_ref=6b04051d96622258266e38c4d8fc0905613a34ce role=agent-integration -->
Returns Claude-style MCP server snippet for back-compatibility with existing callers.

- New code should use `MCPTarget.snippet()` instead for agent-specific formats
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:_claude_desktop_user_path fingerprint=1e2381f94ff68e010d0f1b97646bfd14095e971daa570304a0facb2146a41f36 body_fp=690fdf7fface4f5a515fefd134f7e00c4be8d0db42e5045f13c5c46ecd0abc41 source_ref=6b04051d96622258266e38c4d8fc0905613a34ce role=agent-integration -->
Returns platform-specific path to Claude Desktop's MCP config file.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:TARGETS fingerprint=e37d304acf66777b8a68a405b3940e6e2c8d3735c94b1fb39613dcef2fefd31d body_fp=4af8d1871f499196c4da36be6cee4052bd8b7b36c0684ca72142917335298bd5 source_ref=6b04051d96622258266e38c4d8fc0905613a34ce role=agent-integration -->
Registry of supported MCP targets, mapping agent names to configuration metadata.

- `claude-code` — Claude Code IDE with `.mcp.json` project config and tool format `mcp__trie__{tool}`
- `claude-desktop` — Claude Desktop app with platform-specific user config paths
- `cursor` — Cursor IDE with `.cursor/mcp.json` project config
- `windsurf` — Windsurf IDE with user config at `~/.codeium/windsurf/mcp_config.json`
- `vscode` — VS Code with `.vscode/mcp.json` project config using `servers` key
- `codex` — Codex CLI with user config at `~/.codex/config.json`
- `opencode` — opencode IDE with `mcp` key and tool format `trie_{tool}`
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:detected_target_slugs fingerprint=883d720ec6f4cbe213fb945a07abcc9f0d2f1064d43b48919b4706aa943cee83 body_fp=b3667ef8c1988e39fc91e189d7a194984632a20e22432df9a46b9cf29705b971 source_ref=34464ff2f5778fbeb35a0704bbe03f6c386772af role=util -->
Return slugs of all `TARGETS` entries whose `MCPTarget.detect()` returns `True` on the current machine, in registry order.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:InstallPlan fingerprint=ecc90c2f83f83361a51cb15674f47023de506a19ced5a467dee265684790fbd2 body_fp=5c24435461c914e75887f5098ddb6adfbc68e956d3402a6959044ae093d939a4 source_ref=6b04051d96622258266e38c4d8fc0905613a34ce role=agent-integration -->
Aggregate result of an `install` call across one or more targets.

- `target_names`: names of MCP targets that were processed
- `scope`: whether installation was project or user scoped
- `print_only`: whether this was a preview-only run
- `dry_run`: whether this was a dry run without file modifications
- `results`: list of ApplyResult objects showing what happened to each target
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:install fingerprint=88d64464dd2519b9a322945e0ce28b65ba0b2f78d430d356aa107f17d1aa522b body_fp=ce9f607d5bd02d878cb9c4bd658cbca0904ed172c0f6804a594ea5a8b37327c1 source_ref=6b04051d96622258266e38c4d8fc0905613a34ce role=agent-integration -->
Registers trie MCP server with coding agents/IDEs, applying configuration changes to JSON config files.

- `install_all`: installs to all known targets instead of auto-detecting or using target_names
- `target_names`: specific agent targets to configure; if None, auto-detects installed agents
- Returns InstallPlan with per-target results showing created/updated/skipped/error status
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:_apply_one fingerprint=b330a19107e0ccfb094bcb236edd4027f88df7a11d39129bc66efb466a925414 body_fp=7a4befc040209dbddf165dd02909070464df88f65071ff4ee4e44d4ef4156b43 source_ref=6b04051d96622258266e38c4d8fc0905613a34ce role=agent-integration -->
Apply trie MCP server registration to a single target's JSON config file.

- `print_only`: returns preview action without reading or modifying files
- `dry_run`: reads existing config but returns preview action instead of writing
- Creates parent directories if needed when writing config
- Returns error action if existing config contains invalid JSON or wrong types
- Returns skipped action if trie entry already exists with identical snippet
- Returns updated/created action based on whether config file existed before
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:UninstallPlan fingerprint=19af140e47feb1a80ad4e54e24c332499233c87da1cf175a2e7ec07ac50519b4 body_fp=a0302215560568271adc7b294f2a1fcc56b85440e1209429f51cd381a63a3fbc source_ref=6b04051d96622258266e38c4d8fc0905613a34ce role=agent-integration -->
Aggregate result of an `uninstall` call across one or more targets.

- `target_names`: List of target names processed during uninstall
- `scope`: Whether uninstall targeted project or user scope
- `print_only`: Whether this was a preview-only run without modifications
- `dry_run`: Whether this was a dry run without actual file changes
- `results`: List of `ApplyResult` instances showing outcome for each target
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:uninstall fingerprint=f0ed02e01f9b7af425811ae3bcaa2a0e897458d2641f1b17d8f3439cdf43b6fb body_fp=f79abbe2196e410b6924f9feb1e7e8907608ba5bd6bd0c7893f48affa46dc09e source_ref=6b04051d96622258266e38c4d8fc0905613a34ce role=agent-integration -->
Remove the trie MCP server registration from one or more targets.

- `uninstall_all`: when True, removes trie from all registered targets regardless of detection
- `print_only`/`dry_run`: preview mode, shows what would be removed without modifying files
- Returns `UninstallPlan` with per-target results showing "removed", "skipped", or "error" actions
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:_uninstall_one fingerprint=3c5c7cd363ffa80b387090dd6004c96ea2578c45a32ddf8fdb53851e97e079f5 body_fp=ffc79c7c40ba7f97fad6623c995557084ded5686062df066af0b14703a736119 source_ref=6b04051d96622258266e38c4d8fc0905613a34ce role=agent-integration -->
Removes the trie MCP server entry from a single target's config file, preserving other MCP registrations.

- `print_only`/`dry_run`: returns preview action without modifying files
- Handles missing files, JSON parse errors, and missing trie entries as skipped/error actions
- Cleans up empty snippet_key sections after removal
<!-- trie:end -->