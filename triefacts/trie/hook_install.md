---
trie_version: 0.2.0
source: trie/hook_install.py
file_fingerprint: 235e0b5653036800a56d1513388fb87c0d0a21a022b026452ffab0ae82d2b9f6
last_synced_at: '2026-07-29T17:54:58Z'
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
- kind: class
  qualified_name: trie/hook_install:HookApplyResult
  lines: 44-56
- kind: class
  qualified_name: trie/hook_install:HookSupportFile
  lines: 60-71
- kind: class
  qualified_name: trie/hook_install:HookTarget
  lines: 75-97
- kind: constant
  qualified_name: trie/hook_install:_OPENCODE_PLUGIN_FILENAME
  lines: 105-105
- kind: function
  qualified_name: trie/hook_install:_render_opencode_plugin
  lines: 108-165
- kind: function
  qualified_name: trie/hook_install:_render_opencode_package_json
  lines: 168-197
- kind: constant
  qualified_name: trie/hook_install:TARGETS
  lines: 206-280
- kind: class
  qualified_name: trie/hook_install:HookInstallPlan
  lines: 289-295
- kind: function
  qualified_name: trie/hook_install:install
  lines: 298-348
- kind: function
  qualified_name: trie/hook_install:apply_one
  lines: 351-437
- kind: function
  qualified_name: trie/hook_install:_apply_support_files
  lines: 440-468
incoming_refs: 17
outgoing_refs: 1
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
<!-- trie:section symbol=trie/hook_install:HookInstallError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=c1fbc4900a97c73d0a9fd64636a130f16e882d7ff13c941538a344de2fb4e451 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 role=agent-integration -->
Raised when hook installation fails due to invalid target names or configuration errors.
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:HookApplyResult fingerprint=d59e0db810a8f40ec1fa7957cfd958de8ecc47599cb7e029e28289ff8599c846 body_fp=6b5ead41e2614596abfe1b009752f13b088fb3fe1e557f25637c48d049f3aeec source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 role=agent-integration -->
Represents the outcome of installing a turn-boundary hook for a single agent target.

- `action`: One of "created", "updated", "skipped", "preview", "error", or "needs_manual_setup"
- `path`: File path where the hook was installed, or None for manual setup cases
- `detail`: Human-readable notes about the operation or manual setup instructions
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:HookSupportFile fingerprint=f2b9c5f661daad56cefaee809effd0b86de91e09d125e5ec53b64645ec4b297c body_fp=6f7f4f0b7b9f06357b581ed1c3654f61f3ed98d7aa5a319799fff3e939b6d031 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 role=agent-integration -->
Represents a secondary file written alongside the primary hook plugin file.

- `relative_path`: Path components relative to project root where the support file should be written
- `render_contents`: Function that generates the file contents given the project root path
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:HookTarget fingerprint=6f8d90568ee48ee5845d4626975f5a865d71f5e8b79f084815089f8681ef3e12 body_fp=5da567e15b3792a24db4d15c44f309eeedda89123ee88caa2e3b709743f7f5e7 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 role=agent-integration -->
Static configuration describing an agent's turn-boundary hook installation requirements.

- `relative_path`: when None, the target requires manual setup instead of automation
- `render_contents`: when None, indicates no automated hook installer is available  
- `support_files`: ancillary files written alongside the primary hook file
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:_OPENCODE_PLUGIN_FILENAME fingerprint=7442e6e578a889b0767a95dd3881ed665d3e6834945f3fa54cb3a7c6aceb8925 body_fp=eb365a6e1177a9dea9e870261354332bde8897c6def370567736635558763811 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 role=agent-integration -->
Filename constant for the opencode plugin that triggers trie refresh on agent turn boundaries.
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:_render_opencode_plugin fingerprint=91eee9cdd5ef96f9e80cbb0ea6c7cc7accb1989968c9a04882982fda69d2f9d0 body_fp=f2af4f3dfb93dfb1b10f8c6f466530ab22dd81d1aa258773cb860fba454a5b9f source_ref=f7496ac380664c8c8c5e1faeaf56b98c2f230b69 role=io -->
Generates TypeScript plugin source code for opencode to automatically run `trie sync --graph-only --after-turn` on idle sessions.

- Returns complete plugin file content as string
- Plugin listens for `session.status` with idle type to trigger sync
- Uses `quiet()` to suppress stdout/stderr from flooding opencode TUI
- Swallows errors to prevent plugin failures from disrupting opencode sessions
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:_render_opencode_package_json fingerprint=f27176a9598f9a874b8858a56a2f9b2bf6bcbbc273719242e1c3adcaa000bf2a body_fp=297c53978f575c6ddf646b23def63095f2a43cd13d013fe5bfb442bb9a87860a source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 role=agent-integration -->
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
<!-- trie:section symbol=trie/hook_install:HookInstallPlan fingerprint=baa3478a6300ba11090a4751af386c60014082cfdacfed5157e780649ad9373d body_fp=d824b2f8d23b1e38e27e81a4cab6d35eaa6b24f144702c8a899038df74c98f0d source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 role=agent-integration -->
Holds the outcome of a multi-target hook installation operation.

- `target_names`: agent names the operation was applied to
- `results`: one `HookApplyResult` per target with creation/update status
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:install fingerprint=5fe181bd36c946a52447bddaed8d61ca578458f4d5caa90b8d33b766f90fffec body_fp=6c3c0147ea1bd064927582b17721795a505982f2f84f60218d54e292b9467ca9 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 role=agent-integration -->
Apply turn-boundary hooks for specified agent targets, auto-detecting agents when no targets given.

- Raises `HookInstallError` for unknown target names
- Auto-detection reuses MCP install detection logic to find installed agents
- Agents without automated support return `needs_manual_setup` results with instructions
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:apply_one fingerprint=05838fb0e3219a8d8d7aa3e2f615755e3e98b784efa6949ae5fd585a87f6adaf body_fp=5130a15d874431f0b261bf90779cc1029e3a159f0f059214dc211405fe0d7993 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 role=agent-integration -->
Install or preview a turn-boundary hook for a single target agent.

- Returns `needs_manual_setup` when target lacks automated hook support
- Writes support files (like package.json) even when main hook is unchanged
- Creates parent directories as needed before writing hook file
- Returns `skipped` when existing file matches generated contents exactly
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:_apply_support_files fingerprint=db30752fe89cf626824026104a5750b0cb0ffeeacd5ddb86cdd79d485feee1f0 body_fp=9e29ab36eb03653be6b648b55b5bd0c42cf1e4b5f879b9a881f59324a657e753 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 role=agent-integration -->
Writes hook support files with create/update/skip semantics, returning status notes per file.

- Swallows OSError exceptions to avoid masking successful primary hook installs
- Returns human-readable status messages for each file processed
<!-- trie:end -->