---
trie_version: 0.1.0
source: trie/mcp_install.py
file_fingerprint: 56228de014b2f19f9f9eec8251ccab7ad10bb8e6567965a22c8a5551ab2e9210
last_synced_at: '2026-05-18T13:26:17Z'
defines:
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
- kind: class
  qualified_name: trie/mcp_install:InstallPlan
  lines: 213-218
- kind: function
  qualified_name: trie/mcp_install:install
  lines: 221-268
- kind: function
  qualified_name: trie/mcp_install:_apply_one
  lines: 271-343
incoming_refs: 23
outgoing_refs: 0
---
<!-- trie:section symbol=trie/mcp_install:MCPInstallError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=050f6cc2d8f14a693693a9be4f79ee7bbd4aaf1d6c651837debdd37f83a634a4 source_ref=e7fbffcaf68e6e36cbeb989e0bd314b39f586cda -->
## `MCPInstallError`

Signal an unrecoverable error during MCP install operations.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_install:ApplyResult fingerprint=837f4beba3d4bf388af0b76bb1c1cd73522d4e781b191c72e0ff3a0d22bb56f8 body_fp=5127f15d3535765df4e6114d7cde1acc90e4741243ebe85c6d7c929cdb381937 source_ref=e7fbffcaf68e6e36cbeb989e0bd314b39f586cda -->
## `ApplyResult(target, action, path, snippet, detail="")`

Frozen dataclass recording the outcome of a single MCP config install attempt.

- `action`: one of `"created"`, `"updated"`, `"skipped"`, `"preview"`, `"error"`
- `path`: config file path; `None` if the target was skipped before path resolution
- `snippet`: the JSON fragment written or that would have been written
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_install:MCPTarget fingerprint=070d4c0ad55ae4ecd4f770fbcbbe6d66e3c83e34765d033cbaeae11990b2565b body_fp=d593163a56b67f8ec4ff8562f79326a043018bedb0006f1a4c4675a8b57de2f7 source_ref=ea97a5335fa14a0f02bd9dd07e89a2745ea03a45 -->
## `MCPTarget(name, display_name, snippet_key, snippet_factory, project_rel_path, user_path_str, detect_paths_str, detect_binaries, tool_name_format, notes)`

Frozen dataclass describing a coding agent or IDE that hosts MCP servers via a JSON config file.

- `snippet_key`: JSON key under which server entries are nested; defaults to `"mcpServers"`.
- `snippet_factory`: callable producing the per-target JSON snippet; defaults to Claude-style schema.
- `project_rel_path`: path segments joined to project root for project-scope config.
- `user_path_str`: `~`-expandable string for user-scope config path.
- `detect_paths_str`: any existing path triggers auto-detection as installed.
- `detect_binaries`: any `PATH`-resolvable binary triggers auto-detection as installed.
- `tool_name_format`: format string with `{tool}` placeholder for how the harness exposes MCP tool names; defaults to bare `{tool}`.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_install:MCPTarget.supports fingerprint=79787e5e066fab97ba91f8b46938abb196bdba7a02388d1f6440a7065809f7ac body_fp=6747b22e71524d13d1c9e667bcef5c34ee1e3e882184f1351699ead7ea5749cc source_ref=e7fbffcaf68e6e36cbeb989e0bd314b39f586cda -->
## `supports(self, scope: Scope) -> bool`

Return whether this target supports the given install scope.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_install:MCPTarget.config_path fingerprint=729c7dfaf00b1c7b4844734927972034ff00ab63cecf6d305583e60774525f10 body_fp=afba24dece56749aeb2ad858a4055db3810ee9d5fe60fc28225ec61dc3489abd source_ref=e7fbffcaf68e6e36cbeb989e0bd314b39f586cda -->
## `config_path(self, project_root: Path, scope: Scope) -> Path`

Resolve and return the absolute config file path for the given scope.

- Raises `MCPInstallError` if the target doesn't support the requested scope.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_install:MCPTarget.detect fingerprint=35d47b088004403ab404b5527c337ad0ed667df17158764920d9b1c82547c4c1 body_fp=409eb232432b0a3860e66d5dd2bf9e0b1989ec6da5f398b9d6a505d2623f9940 source_ref=e7fbffcaf68e6e36cbeb989e0bd314b39f586cda -->
## `detect(self) -> bool`

Return `True` if the target is present on the current system via known config paths or binaries.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_install:trie_server_snippet fingerprint=14b918f3e0d1bc9c66c0d49dfbc76270c39ecd16011d07500a29bcb9d7feda79 body_fp=06c5f97423e57b4b5fedac11ea6e4caec56af635df5494593de670edde1bbd54 source_ref=d60cd5a0e4c46ef692c36bd100823726f9396960 -->
## `trie_server_snippet(project_root: Path) -> dict`

Return the Claude-style JSON snippet registering the trie MCP server; back-compat shim delegating to `_claude_style_snippet`.

- `project_root`: resolved and used as the `cwd` field in the snippet.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_install:InstallPlan fingerprint=ecc90c2f83f83361a51cb15674f47023de506a19ced5a467dee265684790fbd2 body_fp=bf8fcf40285417d374357b849f46e0daabdc45be21fc04bdf41c5e7299263708 source_ref=e7fbffcaf68e6e36cbeb989e0bd314b39f586cda -->
## `InstallPlan`

Mutable dataclass accumulating the parameters and results of a single install run.

- `results`: populated in-place by `install()` as each target is processed.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_install:install fingerprint=88d64464dd2519b9a322945e0ce28b65ba0b2f78d430d356aa107f17d1aa522b body_fp=f0e1f8b707c161b11a7c1f1f3867d93532af6cbc3f3cbfb098332ca58cb9b933 source_ref=e7fbffcaf68e6e36cbeb989e0bd314b39f586cda -->
## `install(*, target_names: list[str] | None, scope: Scope, install_all: bool, print_only: bool, dry_run: bool, project_root: Path) -> InstallPlan`

Apply or preview trie MCP server registration to one or more agent/IDE targets.

- `target_names`: explicit target slugs; ignored when `install_all` is true.
- `install_all`: registers against every entry in `TARGETS`.
- `print_only`: returns preview results without touching the filesystem.
- `dry_run`: reads existing config but skips writes; returns preview results.
- Raises `MCPInstallError` if an unknown target name is given or no agents are auto-detected.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_install:_claude_desktop_user_path fingerprint=1e2381f94ff68e010d0f1b97646bfd14095e971daa570304a0facb2146a41f36 body_fp=8ded51c9e23ce5755c95c0b6978ae6d85baccea27fe29eaf662c839f59ac895d source_ref=e7fbffcaf68e6e36cbeb989e0bd314b39f586cda -->
## `_claude_desktop_user_path() -> str`

Return the platform-appropriate Claude Desktop config file path string.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_install:_apply_one fingerprint=b330a19107e0ccfb094bcb236edd4027f88df7a11d39129bc66efb466a925414 body_fp=3bdad29756dfcd6a690b018c6d0c63ec9fffd66410fa1f1d6dbffe16a8b3bf4a source_ref=d60cd5a0e4c46ef692c36bd100823726f9396960 -->
## `_apply_one(target: MCPTarget, project_root: Path, scope: Scope, print_only: bool, dry_run: bool) -> ApplyResult`

Read, merge, and write the trie MCP server entry into a single target's JSON config file.

- `print_only`: returns a preview result without reading or writing any file.
- `dry_run`: reads and validates the config but skips writing; returns preview.
- Returns `"skipped"` if the entry already matches; `"created"` or `"updated"` on success; `"error"` on invalid JSON.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_install:_claude_style_snippet fingerprint=57f6465b6c54d4d2fbbaab06e3cc4fab6e782ad55e0c53e3bbea72c053aba9cc body_fp=64860855c22bec9d420675acf4a676af1012713265cb3546d0484ee206c39609 source_ref=d60cd5a0e4c46ef692c36bd100823726f9396960 -->
## `_claude_style_snippet(project_root: Path) -> dict`

Build the MCP server snippet dict for Claude Code, Desktop, Cursor, Windsurf, Codex, and VS Code.

- `cwd`: set to the resolved `project_root` so the spawned process finds the correct project.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_install:_opencode_style_snippet fingerprint=882e5910393a9e41e24e4c42cc0bd620bd10b9177bed1c9cb47d6980a480a003 body_fp=e2fc712c819a88d6c43eef26f12a9394f13c3170838db97a482c71593e030a30 source_ref=d60cd5a0e4c46ef692c36bd100823726f9396960 -->
## `_opencode_style_snippet(project_root: Path) -> dict`

Build the opencode-style MCP snippet with `type: "local"` and a command array.

- `project_root`: accepted but unused; opencode infers cwd from its own spawn semantics.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_install:MCPTarget.snippet fingerprint=a4c3ce181119b0a706a42a416fa07184eeea2f71c67a53dafa00410ff59420df body_fp=ea2d6a12e3a2a101b424062fd4f6cbcc216e659e950cf67af623fd36902dab1f source_ref=d60cd5a0e4c46ef692c36bd100823726f9396960 -->
## `snippet(self, project_root: Path) -> dict`

Build the JSON value registered for this target under `snippet_key.trie`.
<!-- trie:end -->