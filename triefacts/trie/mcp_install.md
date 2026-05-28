---
trie_version: 0.1.5
source: trie/mcp_install.py
file_fingerprint: 3274caf171669677e3e1cfd8c02be982d8b17c3daac2299cea7bf1cd9eda9a84
last_synced_at: '2026-05-23T23:46:34Z'
defines:
- kind: module
  qualified_name: trie/mcp_install:__module__
  lines: 1-512
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
- kind: class
  qualified_name: trie/mcp_install:InstallPlan
  lines: 213-218
- kind: function
  qualified_name: trie/mcp_install:install
  lines: 221-268
- kind: function
  qualified_name: trie/mcp_install:_apply_one
  lines: 271-343
- kind: class
  qualified_name: trie/mcp_install:UninstallPlan
  lines: 353-365
- kind: function
  qualified_name: trie/mcp_install:uninstall
  lines: 368-430
- kind: function
  qualified_name: trie/mcp_install:_uninstall_one
  lines: 433-511
incoming_refs: 48
outgoing_refs: 0
---
<!-- trie:section symbol=trie/mcp_install:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=97ffd6420b97e40340851e1c10ff56bb5e1185289d4a046736cf9959ebbaa9b2 source_ref=6b04051d96622258266e38c4d8fc0905613a34ce -->
## `mcp_install`

Install, preview, and remove trie MCP server registrations across multiple coding-agent JSON config files.

- `TARGETS`: ordered registry of all supported agents/IDEs
- `install` / `uninstall`: primary entry points; return `InstallPlan` / `UninstallPlan`
- `Scope`: `"project"` or `"user"`
- `Action`: outcome tag on each `ApplyResult`
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:Scope fingerprint=d12ea4ff19e63ba188c524bde1d23431cddd8bb548648d958a80898366b86958 body_fp=c0f393ea10cb194c007c868c3d36124e56c90a516afea283cf71f7939e2c4352 source_ref=6b04051d96622258266e38c4d8fc0905613a34ce -->
## `Scope = Literal["project", "user"]`

Type alias for the two install scopes: per-project config file or per-user config file.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:Action fingerprint=1c60756f67dd341e644d4277839371345319686f7c9ddcef385cf46f6e8cc4a5 body_fp=24e6bbb1b3c56eefa35e62e662031a296c0807e577606cc053eaff71d813a79b source_ref=6b04051d96622258266e38c4d8fc0905613a34ce -->
## `Action = Literal["created", "updated", "removed", "skipped", "preview", "error"]`

Type alias for the outcome of a single MCP config apply or uninstall operation.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:SnippetFactory fingerprint=93c2a5173f07fcf25ba5724d0f0ae74f5ec427a1b364965f613ba2a6d9d59eb3 body_fp=1f3b22e5b09989bade1a4c80030aedf856227b5c700ae2f297f392d53cd946cb source_ref=6b04051d96622258266e38c4d8fc0905613a34ce -->
## `SnippetFactory = Callable[[Path], dict]`

Type alias for a function that accepts a project root `Path` and returns a JSON-serialisable `dict` snippet.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:MCPInstallError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=d4f6753cd736f49680e13d922b2886a142fcce454dbe337e8df20802873439eb source_ref=6b04051d96622258266e38c4d8fc0905613a34ce -->
## `MCPInstallError`

Raised for unrecoverable errors during MCP install or uninstall operations.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:ApplyResult fingerprint=837f4beba3d4bf388af0b76bb1c1cd73522d4e781b191c72e0ff3a0d22bb56f8 body_fp=3db10bc3c64e34100838d48a0ba1804bfd1afcbf6826ce8dc37f09941b14771a source_ref=6b04051d96622258266e38c4d8fc0905613a34ce -->
## `ApplyResult(target, action, path, snippet, detail="")`

Immutable record describing the outcome of a single MCP config apply or uninstall operation.

- `target`: short slug identifying the agent (e.g. `"claude-code"`)
- `action`: one of `created`, `updated`, `removed`, `skipped`, `preview`, `error`
- `path`: config file path, or `None` when the target was skipped before path resolution
- `snippet`: the JSON value written or that would be written under `snippet_key.trie`
- `detail`: human-readable explanation, populated for `skipped` and `error` actions
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:_claude_style_snippet fingerprint=57f6465b6c54d4d2fbbaab06e3cc4fab6e782ad55e0c53e3bbea72c053aba9cc body_fp=0dfd4cccc8f6d9a417fd0f66f0226a3028ccdf223059275dd324c03e7f55a7d5 source_ref=6b04051d96622258266e38c4d8fc0905613a34ce -->
## `_claude_style_snippet(project_root: Path) -> dict`

Build a Claude-style MCP server config dict with `command`, `args`, and resolved `cwd`.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:_opencode_style_snippet fingerprint=882e5910393a9e41e24e4c42cc0bd620bd10b9177bed1c9cb47d6980a480a003 body_fp=dbda96970dafcb52ef73a6df1f189c7c087e0315a3f4f43e9fa05cd88347cfe1 source_ref=6b04051d96622258266e38c4d8fc0905613a34ce -->
## `_opencode_style_snippet(project_root: Path) -> dict`

Build the opencode-style MCP snippet with `type: "local"` and `command` as an array.

- `project_root`: accepted but unused; opencode infers cwd from its own spawn semantics.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:MCPTarget fingerprint=070d4c0ad55ae4ecd4f770fbcbbe6d66e3c83e34765d033cbaeae11990b2565b body_fp=66578a5d918aa80d11844b9c6e1d9833952caabc81c4d1a8604b7a74ca2e6592 source_ref=6b04051d96622258266e38c4d8fc0905613a34ce -->
## `MCPTarget`

Frozen dataclass describing one coding agent/IDE target for MCP server registration via JSON config.

- `name`: short slug used as `--target` value on the CLI
- `snippet_key`: top-level JSON key under which `trie` is registered (default `"mcpServers"`)
- `snippet_factory`: callable producing the JSON value; defaults to Claude-style schema
- `project_rel_path`: path segments relative to project root; `None` means no project-scope support
- `user_path_str`: `~`-prefixed string expanded to the user-scope config path
- `detect_paths_str`: any existing path triggers auto-detection
- `detect_binaries`: any binary found on `PATH` triggers auto-detection
- `tool_name_format`: `{tool}` format string rendering how the agent exposes MCP tool names
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:MCPTarget.supports fingerprint=79787e5e066fab97ba91f8b46938abb196bdba7a02388d1f6440a7065809f7ac body_fp=2b89103aa4e24aefd1ad6157e86f72365d550a95ba1dceab4930721750b2dca7 source_ref=6b04051d96622258266e38c4d8fc0905613a34ce -->
## `MCPTarget.supports(self, scope: Scope) -> bool`

Return whether this `MCPTarget` has a config path defined for the given scope.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:MCPTarget.config_path fingerprint=729c7dfaf00b1c7b4844734927972034ff00ab63cecf6d305583e60774525f10 body_fp=59f311c4c6e77b9f7698e5aba864a12955f56113292173627cb92f00c953c0e5 source_ref=6b04051d96622258266e38c4d8fc0905613a34ce -->
## `MCPTarget.config_path(self, project_root: Path, scope: Scope) -> Path`

Resolve the absolute config file path for this `MCPTarget` given a scope.

- Raises `MCPInstallError` if the target doesn't support the requested scope.
- `"project"` scope: joins `project_rel_path` onto `project_root`.
- `"user"` scope: expands `user_path_str` via `Path.expanduser()`.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:MCPTarget.detect fingerprint=35d47b088004403ab404b5527c337ad0ed667df17158764920d9b1c82547c4c1 body_fp=44db36bdc22933edf0cbbdf5b54aa4ab265dee5c991dbbb91202b49a8989cea6 source_ref=6b04051d96622258266e38c4d8fc0905613a34ce -->
## `MCPTarget.detect(self) -> bool`

Return `True` if any configured detection path exists or any configured binary is on `PATH`.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:MCPTarget.snippet fingerprint=a4c3ce181119b0a706a42a416fa07184eeea2f71c67a53dafa00410ff59420df body_fp=1fe5aa440691ea24fc1f94a7c0db8a4a0f09475574493d15fe138c9d0fe8035a source_ref=6b04051d96622258266e38c4d8fc0905613a34ce -->
## `MCPTarget.snippet(self, project_root: Path) -> dict`

Invoke the `MCPTarget`'s `snippet_factory` to build the JSON value registered under `snippet_key["trie"]`.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:trie_server_snippet fingerprint=14b918f3e0d1bc9c66c0d49dfbc76270c39ecd16011d07500a29bcb9d7feda79 body_fp=2e351c59837b25e4975cd65de4edca8d260072cbae88ee1e22c71c0828adf16d source_ref=6b04051d96622258266e38c4d8fc0905613a34ce -->
## `trie_server_snippet(project_root: Path) -> dict`

Return a Claude-style MCP snippet; back-compat shim delegating to `_claude_style_snippet`.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:_claude_desktop_user_path fingerprint=1e2381f94ff68e010d0f1b97646bfd14095e971daa570304a0facb2146a41f36 body_fp=4b9b1cafbf71a3deb8394aa9e125b255e570eb754391be28399e78f469d355f1 source_ref=6b04051d96622258266e38c4d8fc0905613a34ce -->
## `_claude_desktop_user_path() -> str`

Return the platform-appropriate path string for the Claude Desktop config file.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:TARGETS fingerprint=e37d304acf66777b8a68a405b3940e6e2c8d3735c94b1fb39613dcef2fefd31d body_fp=9089b3a17d3603984dabe4cd94696d77ddba6f0524ce25557759398bae658a2c source_ref=6b04051d96622258266e38c4d8fc0905613a34ce -->
## `TARGETS: dict[str, MCPTarget]`

Ordered registry of all supported MCP host targets, keyed by slug name.

- `"claude-code"`: project `.mcp.json`, user `~/.claude.json`, tools `mcp__trie__{tool}`
- `"claude-desktop"`: user-scope only, platform-dependent path, same tool format as claude-code
- `"cursor"`: project `.cursor/mcp.json`, user `~/.cursor/mcp.json`, tool format unconfirmed
- `"windsurf"`: user-scope only, tool format unconfirmed
- `"vscode"`: project `.vscode/mcp.json` only, uses `servers` snippet key instead of `mcpServers`
- `"codex"`: user-scope only, config path may change in future releases
- `"opencode"`: uses `mcp` snippet key and `_opencode_style_snippet`; tools prefixed `trie_{tool}`
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:InstallPlan fingerprint=ecc90c2f83f83361a51cb15674f47023de506a19ced5a467dee265684790fbd2 body_fp=e0090e299f28534e9169d8f5227b7382aeb9ee16ef2e9d347d49f08aa8da510b source_ref=6b04051d96622258266e38c4d8fc0905613a34ce -->
## `InstallPlan`

Accumulate the parameters and per-target results of a single `install` call.

- `print_only`: emit preview output without writing any files.
- `dry_run`: simulate writes; still parses existing configs.
- `results`: populated by `install` as each target is processed.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:install fingerprint=88d64464dd2519b9a322945e0ce28b65ba0b2f78d430d356aa107f17d1aa522b body_fp=5b9ef77d80e8556592250e7016a32ff9e96589660a57ec8c988ae28be7b03f3d source_ref=6b04051d96622258266e38c4d8fc0905613a34ce -->
## `install(*, target_names: list[str] | None, scope: Scope, install_all: bool, print_only: bool, dry_run: bool, project_root: Path) -> InstallPlan`

Register the trie MCP server into one or more agent config files, returning an `InstallPlan` with per-target results.

- `target_names`: explicit slugs from `TARGETS`; `None` triggers auto-detect via `MCPTarget.detect()`.
- `install_all`: overrides `target_names` and auto-detect; selects every known target.
- `print_only`: records `"preview"` actions without touching the filesystem.
- `dry_run`: simulates writes; also produces `"preview"` actions.
- Raises `MCPInstallError` if a name is unknown or no agents are detected.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:_apply_one fingerprint=b330a19107e0ccfb094bcb236edd4027f88df7a11d39129bc66efb466a925414 body_fp=202609921a4ba0d7ff4d09f39273a84725ff94f778cfff4f8c23407286c147e1 source_ref=6b04051d96622258266e38c4d8fc0905613a34ce -->
## `_apply_one(target: MCPTarget, project_root: Path, scope: Scope, print_only: bool, dry_run: bool) -> ApplyResult`

Merge the trie server snippet into one target's JSON config file, returning an `ApplyResult`.

- `print_only`: returns `preview` without reading the existing file.
- `dry_run`: reads and validates the file but skips the write, returns `preview`.
- Returns `skipped` if the identical snippet is already registered.
- Returns `error` if the config file contains invalid JSON or a non-object root/servers key.
- Returns `created` or `updated` depending on whether the config file existed before.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:UninstallPlan fingerprint=19af140e47feb1a80ad4e54e24c332499233c87da1cf175a2e7ec07ac50519b4 body_fp=be0827a53e738e17731d4f5cb8350e91c97eb82b96d950655235fc5bbd7fb2c6 source_ref=6b04051d96622258266e38c4d8fc0905613a34ce -->
## `UninstallPlan`

Aggregate result of an `uninstall` call across one or more targets.

- `results`: accumulated `ApplyResult` entries, one per processed target.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:uninstall fingerprint=f0ed02e01f9b7af425811ae3bcaa2a0e897458d2641f1b17d8f3439cdf43b6fb body_fp=633dc270e04b3763540bc8599ad679e9a13b262881c3d1d90b47a19e958d8235 source_ref=6b04051d96622258266e38c4d8fc0905613a34ce -->
## `uninstall(*, target_names, scope, uninstall_all, print_only, dry_run, project_root) -> UninstallPlan`

Remove the trie MCP server entry from one or more agent config files.

- `uninstall_all`: process every entry in `TARGETS` regardless of detection.
- `target_names`: explicit list; raises `MCPInstallError` for unknown names.
- Auto-detects targets via `MCPTarget.detect()` when both are falsy.
- `print_only` / `dry_run`: produce `"preview"` results without writing.
- Raises `MCPInstallError` if auto-detect finds no agents on the system.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_install:_uninstall_one fingerprint=3c5c7cd363ffa80b387090dd6004c96ea2578c45a32ddf8fdb53851e97e079f5 body_fp=6f045f4411cc589b820a51f0e221b3e168bac037eb1acd2cdbf87b175e022cd9 source_ref=6b04051d96622258266e38c4d8fc0905613a34ce -->
## `_uninstall_one(target: MCPTarget, project_root: Path, scope: Scope, print_only: bool, dry_run: bool) -> ApplyResult`

Remove the `trie` key from one target's JSON config, dropping `snippet_key` if it becomes empty.

- Returns `skipped` if config file is absent or `trie` is not registered.
- Returns `error` if the config file contains invalid JSON or a non-object root.
- Returns `preview` for both `print_only` and `dry_run`; never writes in either mode.
- Returns `removed` with the deleted snippet on successful write.
<!-- trie:end -->