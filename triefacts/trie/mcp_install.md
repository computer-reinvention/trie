---
trie_version: 0.1.0
source: trie/mcp_install.py
file_fingerprint: 6c38c90552d80587396bcaa468bd5981cc31afd14a3cd6db915998f588476eab
last_synced_at: '2026-05-12T18:26:04Z'
defines:
- kind: class
  qualified_name: trie/mcp_install:MCPInstallError
  lines: 14-15
- kind: class
  qualified_name: trie/mcp_install:ApplyResult
  lines: 19-24
- kind: class
  qualified_name: trie/mcp_install:MCPTarget
  lines: 28-65
- kind: method
  qualified_name: trie/mcp_install:MCPTarget.supports
  lines: 42-45
- kind: method
  qualified_name: trie/mcp_install:MCPTarget.config_path
  lines: 47-60
- kind: method
  qualified_name: trie/mcp_install:MCPTarget.detect
  lines: 62-65
- kind: function
  qualified_name: trie/mcp_install:trie_server_snippet
  lines: 68-74
- kind: class
  qualified_name: trie/mcp_install:InstallPlan
  lines: 136-141
- kind: function
  qualified_name: trie/mcp_install:install
  lines: 144-191
incoming_refs: 17
outgoing_refs: 0
---
<!-- trie:section symbol=trie/mcp_install:MCPInstallError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=2234121157705710da1c932983ff36a8aa193ff6c804ed614518e187b7c3a426 -->
## `MCPInstallError`

Raised when MCP installation fails due to unknown targets, unsupported scopes, or missing agents.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_install:ApplyResult fingerprint=837f4beba3d4bf388af0b76bb1c1cd73522d4e781b191c72e0ff3a0d22bb56f8 body_fp=6e371f342142ca057553cf6379f8575dd1267ba750450b0618ae297e4d3059b4 -->
## `ApplyResult(target, action, path, snippet, detail="")`

Frozen dataclass recording the outcome of a single MCP config install attempt.

- `action`: one of `"created"`, `"updated"`, `"skipped"`, `"preview"`, `"error"`
- `path`: config file path, or `None` if the target was skipped before path resolution
- `snippet`: the JSON fragment written or proposed
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_install:MCPTarget fingerprint=a5f99be28366226321e202a38fd69182d4b700fc0d60c26cd9d6785037e34056 body_fp=6201c481a882a525e5f1f5e35b112e160fb902cc9aee29d87c126794de9fe128 -->
## `MCPTarget(name, display_name, snippet_key, project_rel_path, user_path_str, detect_paths_str, detect_binaries, notes)`

Frozen dataclass describing a coding agent/IDE that hosts MCP servers via a JSON config file.

- `snippet_key`: JSON object key under which MCP servers are registered; defaults to `"mcpServers"`.
- `project_rel_path`: path components relative to project root; `None` means project scope unsupported.
- `user_path_str`: raw string passed to `Path` then `expanduser`; `None` means user scope unsupported.
- `detect_paths_str`: if any exist, `detect()` returns `True`.
- `detect_binaries`: if any are on `PATH`, `detect()` returns `True`.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_install:MCPTarget.supports fingerprint=79787e5e066fab97ba91f8b46938abb196bdba7a02388d1f6440a7065809f7ac body_fp=68e2261f5e8563e3197051cc8cd266420f4d4ff913ffa31ff851006e25389cc1 -->
## `supports(self, scope: Scope) -> bool`

Return whether this target has a config path defined for the given scope.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_install:MCPTarget.config_path fingerprint=729c7dfaf00b1c7b4844734927972034ff00ab63cecf6d305583e60774525f10 body_fp=afba24dece56749aeb2ad858a4055db3810ee9d5fe60fc28225ec61dc3489abd -->
## `config_path(self, project_root: Path, scope: Scope) -> Path`

Resolve and return the absolute config file path for the given scope.

- Raises `MCPInstallError` if the target doesn't support the requested scope.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_install:MCPTarget.detect fingerprint=35d47b088004403ab404b5527c337ad0ed667df17158764920d9b1c82547c4c1 body_fp=a5004054d382c071bb9d0b8da821fd9f25f37d2d8e31e022b418d4a357a53114 -->
## `detect(self) -> bool`

Return `True` if any configured detection path exists or any detection binary is on `PATH`.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_install:trie_server_snippet fingerprint=d6267d49425cd7733da3e1ec78f5d90c02cd5558a1cce4bc04bd5bb33af5e4ce body_fp=5afdbcb8c8dc26aff1ff9aa9efb8a7ee841f6b6aa16530343d0f9534276ec28e -->
## `trie_server_snippet(project_root: Path) -> dict`

Return the JSON snippet registering the trie MCP server under a target's `mcpServers` map.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_install:InstallPlan fingerprint=ecc90c2f83f83361a51cb15674f47023de506a19ced5a467dee265684790fbd2 body_fp=6142b88ea47dcc16f858925cf855ea0d0d0e69706ad5ff3bd3f7dbf653978260 -->
## `InstallPlan(target_names, scope, print_only, dry_run, results=[])`

Mutable dataclass accumulating the configuration and outcomes of a single `install` call.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_install:install fingerprint=88d64464dd2519b9a322945e0ce28b65ba0b2f78d430d356aa107f17d1aa522b body_fp=670ee6c7151b99fab7c75d31e4120b09a8b2c050b2cb8e0a88c8078ae31c2aae -->
## `install(*, target_names: list[str] | None, scope: Scope, install_all: bool, print_only: bool, dry_run: bool, project_root: Path) -> InstallPlan`

Apply or preview trie MCP server registration to one or more detected or named targets.

- `target_names`: explicit target slugs; ignored when `install_all` is true.
- `install_all`: register against every known target regardless of detection.
- `print_only`: return preview results without reading or writing any files.
- `dry_run`: parse existing configs but skip writes; returns `"preview"` actions.
- Raises `MCPInstallError` if an unknown target name is given or none are auto-detected.
<!-- trie:end -->