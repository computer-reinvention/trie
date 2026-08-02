---
trie_version: 0.3.0
source: trie/hook_install.py
file_fingerprint: 235e0b5653036800a56d1513388fb87c0d0a21a022b026452ffab0ae82d2b9f6
last_synced_at: '2026-08-01T09:20:35Z'
description: Turn-boundary hook installation for coding agents.
defines:
- kind: module
  qualified_name: trie/hook_install:__module__
  lines: 1-469
- kind: constant
  qualified_name: trie/hook_install:Action
  lines: 36-36
- kind: class
  qualified_name: trie/hook_install:HookInstallError
  lines: 39-40
  signature: class HookInstallError(Exception)
- kind: class
  qualified_name: trie/hook_install:HookApplyResult
  lines: 44-56
  signature: class HookApplyResult
- kind: class
  qualified_name: trie/hook_install:HookSupportFile
  lines: 60-71
  signature: class HookSupportFile
- kind: class
  qualified_name: trie/hook_install:HookTarget
  lines: 75-97
  signature: class HookTarget
- kind: constant
  qualified_name: trie/hook_install:_OPENCODE_PLUGIN_FILENAME
  lines: 105-105
- kind: function
  qualified_name: trie/hook_install:_render_opencode_plugin
  lines: 108-165
  signature: 'def _render_opencode_plugin(_project_root: Path) -> str'
- kind: function
  qualified_name: trie/hook_install:_render_opencode_package_json
  lines: 168-197
  signature: 'def _render_opencode_package_json(_project_root: Path) -> str'
- kind: constant
  qualified_name: trie/hook_install:TARGETS
  lines: 206-280
- kind: class
  qualified_name: trie/hook_install:HookInstallPlan
  lines: 289-295
  signature: class HookInstallPlan
- kind: function
  qualified_name: trie/hook_install:install
  lines: 298-348
  signature: 'def install( *, target_names: list[str] | None, install_all: bool, print_only: bool, dry_run: bool, project_root: Path, ) -> HookInstallPlan'
- kind: function
  qualified_name: trie/hook_install:apply_one
  lines: 351-437
  signature: 'def apply_one( target: HookTarget, project_root: Path, print_only: bool, dry_run: bool, *, scope: Scope = "project", ) -> HookApplyResult'
- kind: function
  qualified_name: trie/hook_install:_apply_support_files
  lines: 440-468
  signature: 'def _apply_support_files( files: tuple[HookSupportFile, ...], project_root: Path, ) -> list[str]'
incoming_refs: 17
outgoing_refs: 2
---
<!-- trie:section symbol=trie/hook_install:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=21ee9d447b947371dbc665d0c8e007fa0ce70a727b8ff219daf9a1aba308f600 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 role=agent-integration -->
Installs turn-boundary hooks that automatically run `trie refresh` when coding agents finish sessions.

- Supports automated installation for opencode via TypeScript plugins
- Returns manual setup instructions for agents without hook APIs (Claude, Cursor, etc.)
- Mirrors `mcp_install` structure for unified reporting in `trie setup`
- Handles idempotency and dry-run/preview modes like MCP installation
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:Action fingerprint=6d5466b453e0912edae50fab1848c782530de9137450b5c33b3682dc80488f21 body_fp=83a58f4f37da94b3698c78d6cc6ecca58f7387a2754aa81174bf1383dcbcf0dd source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 role=agent-integration -->
Type alias for hook install operation outcomes.

• **created**: Hook file was written for the first time
• **updated**: Hook file existed and was overwritten with new contents
• **skipped**: Hook file already exists with identical contents
• **preview**: Contents shown without writing (dry-run or print-only mode)
• **error**: Operation failed due to filesystem or other error
• **needs_manual_setup**: Target known but lacks automated installation
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:HookInstallError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=ac8d7ba3ec39fd04151755dbd2a2aed0868769654c0f3f0bb78cffd4a976f1aa source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 role=agent-integration -->
## `class HookInstallError(Exception)`

Raised when hook installation fails due to invalid target names or configuration errors.
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:HookApplyResult fingerprint=d59e0db810a8f40ec1fa7957cfd958de8ecc47599cb7e029e28289ff8599c846 body_fp=9feb04678eb1d9f3c50729c70dfecc0a476682b3c66f4730fc37f7db5b7e5e6e source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 role=agent-integration -->
## `class HookApplyResult`

Represents the outcome of installing a turn-boundary hook for a single agent target.

- `action`: One of "created", "updated", "skipped", "preview", "error", or "needs_manual_setup"
- `path`: File path where the hook was installed, or None for manual setup cases
- `detail`: Human-readable notes about the operation or manual setup instructions
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:HookSupportFile fingerprint=f2b9c5f661daad56cefaee809effd0b86de91e09d125e5ec53b64645ec4b297c body_fp=6d19dcc3112f3700e44228857b2154c1f06e5da65f5d36c642dafa59f2173387 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 role=agent-integration -->
## `class HookSupportFile`

Represents a secondary file written alongside the primary hook plugin file.

- `relative_path`: Path components relative to project root where the support file should be written
- `render_contents`: Function that generates the file contents given the project root path
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:HookTarget fingerprint=6f8d90568ee48ee5845d4626975f5a865d71f5e8b79f084815089f8681ef3e12 body_fp=df56a86edd27c614bcd02fa48ddca72aa84c7539526fd3df60532f9a8f245a91 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 role=agent-integration -->
## `class HookTarget`

Static configuration describing an agent's turn-boundary hook installation requirements.

- `relative_path`: when None, the target requires manual setup instead of automation
- `render_contents`: when None, indicates no automated hook installer is available  
- `support_files`: ancillary files written alongside the primary hook file
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:_OPENCODE_PLUGIN_FILENAME fingerprint=7442e6e578a889b0767a95dd3881ed665d3e6834945f3fa54cb3a7c6aceb8925 body_fp=eb365a6e1177a9dea9e870261354332bde8897c6def370567736635558763811 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 role=agent-integration -->
Filename constant for the opencode plugin that triggers trie refresh on agent turn boundaries.
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:_render_opencode_plugin fingerprint=91eee9cdd5ef96f9e80cbb0ea6c7cc7accb1989968c9a04882982fda69d2f9d0 body_fp=358778d04e2f7a12d7791093d8bc45cafd17c954aeaed810a9c11f7fd6e77b1f source_ref=f7496ac380664c8c8c5e1faeaf56b98c2f230b69 role=io -->
## `def _render_opencode_plugin(_project_root: Path) -> str`

Generates TypeScript plugin source code for opencode to automatically run `trie sync --graph-only --after-turn` on idle sessions.

- Returns complete plugin file content as string
- Plugin listens for `session.status` with idle type to trigger sync
- Uses `quiet()` to suppress stdout/stderr from flooding opencode TUI
- Swallows errors to prevent plugin failures from disrupting opencode sessions
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:_render_opencode_package_json fingerprint=f27176a9598f9a874b8858a56a2f9b2bf6bcbbc273719242e1c3adcaa000bf2a body_fp=1811cdc5b9a23b8260a020d9df93aac768d155b684557b7e0313b54390bbb132 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 role=agent-integration -->
## `def _render_opencode_package_json(_project_root: Path) -> str`

Renders `.opencode/package.json` pinning `@opencode-ai/plugin` to prevent opencode module resolution failures.

- Returns JSON string with `@opencode-ai/plugin: "latest"` dependency
- Prevents `ERR_MODULE_NOT_FOUND` errors when opencode auto-pins to `"local"`
- Works around opencode bugs #28286 and #27676 that break plugin imports
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:TARGETS fingerprint=794ceee835be8ac0de8e8d58d422e7c4673276bf496f622614be02f8dc9ebf9c body_fp=247db4a205edb681a13bb95c5255badfde198a176abc2fd4e7b912c49b866671 source_ref=f7496ac380664c8c8c5e1faeaf56b98c2f230b69 role=agent-integration -->
Maps agent names to their turn-boundary hook installation specifications.

- Only "opencode" supports automated hook installation with TypeScript plugin
- Other agents return manual setup instructions requiring user intervention
- All names must also exist in `mcp_install.TARGETS` for unified setup reporting
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:HookInstallPlan fingerprint=baa3478a6300ba11090a4751af386c60014082cfdacfed5157e780649ad9373d body_fp=1d13e3bbb0c542e40c611c24d38dd1cb3fcac1a651a8a9dc7d08f74fbdffc221 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 role=agent-integration -->
## `class HookInstallPlan`

Holds the outcome of a multi-target hook installation operation.

- `target_names`: agent names the operation was applied to
- `results`: one `HookApplyResult` per target with creation/update status
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:install fingerprint=5fe181bd36c946a52447bddaed8d61ca578458f4d5caa90b8d33b766f90fffec body_fp=3ca5dae431f39b6c7f180f0986de786dffa750ad0927cf1b9399781feb515e11 source_ref=f7496ac380664c8c8c5e1faeaf56b98c2f230b69 role=agent-integration -->
## `def install( *, target_names: list[str] | None, install_all: bool, print_only: bool, dry_run: bool, project_root: Path, ) -> HookInstallPlan`

Apply turn-boundary hooks for specified agent targets, auto-detecting agents when no targets given.

- Raises `HookInstallError` for unknown target names
- Auto-detection reuses MCP install detection logic to find installed agents
- Agents without automated support return `needs_manual_setup` results with instructions
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:apply_one fingerprint=05838fb0e3219a8d8d7aa3e2f615755e3e98b784efa6949ae5fd585a87f6adaf body_fp=d59865f7280ab177fed78fb763394060664fe9cf667b179b0e00b4f73d130b51 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 role=agent-integration -->
## `def apply_one( target: HookTarget, project_root: Path, print_only: bool, dry_run: bool, *, scope: Scope = "project", ) -> HookApplyResult`

Install or preview a turn-boundary hook for a single target agent.

- Returns `needs_manual_setup` when target lacks automated hook support
- Writes support files (like package.json) even when main hook is unchanged
- Creates parent directories as needed before writing hook file
- Returns `skipped` when existing file matches generated contents exactly
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:_apply_support_files fingerprint=db30752fe89cf626824026104a5750b0cb0ffeeacd5ddb86cdd79d485feee1f0 body_fp=86ed05c4af5846fc0ef371c058b1fcafe30a0140bb42d252791f1ba36a69a9c7 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 role=agent-integration -->
## `def _apply_support_files( files: tuple[HookSupportFile, ...], project_root: Path, ) -> list[str]`

Writes hook support files with create/update/skip semantics, returning status notes per file.

- Swallows OSError exceptions to avoid masking successful primary hook installs
- Returns human-readable status messages for each file processed
<!-- trie:end -->