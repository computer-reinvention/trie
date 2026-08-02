---
trie_version: 0.3.0
source: trie/tool_override_install.py
file_fingerprint: f5ef399d38092408a1ae896f14372c88fbc929620a099f6735eb50bc92352123
last_synced_at: '2026-08-02T21:19:12Z'
description: 'Tool-override installation: replace an agent''s built-in tools with trie wrappers.'
defines:
- kind: module
  qualified_name: trie/tool_override_install:__module__
  lines: 1-2279
- kind: constant
  qualified_name: trie/tool_override_install:Action
  lines: 49-49
- kind: class
  qualified_name: trie/tool_override_install:ToolOverrideInstallError
  lines: 52-53
  signature: class ToolOverrideInstallError(Exception)
- kind: class
  qualified_name: trie/tool_override_install:FileToWrite
  lines: 57-68
  signature: class FileToWrite
- kind: class
  qualified_name: trie/tool_override_install:ToolOverrideApplyResult
  lines: 72-85
  signature: class ToolOverrideApplyResult
- kind: class
  qualified_name: trie/tool_override_install:ToolOverrideFileResult
  lines: 89-96
  signature: class ToolOverrideFileResult
- kind: class
  qualified_name: trie/tool_override_install:ToolOverrideTarget
  lines: 100-124
  signature: class ToolOverrideTarget
- kind: constant
  qualified_name: trie/tool_override_install:_GENERATED_HEADER
  lines: 132-137
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_grep_override
  lines: 140-244
  signature: 'def _render_opencode_grep_override(_project_root: Path) -> str'
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_read_override
  lines: 247-1014
  signature: 'def _render_opencode_read_override(_project_root: Path) -> str'
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_trace
  lines: 1017-1086
  signature: 'def _render_opencode_trace(_project_root: Path) -> str'
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_grep_str
  lines: 1094-1127
  signature: 'def _render_opencode_grep_str(_project_root: Path) -> str'
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_grep_entry_points
  lines: 1130-1162
  signature: 'def _render_opencode_grep_entry_points(_project_root: Path) -> str'
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_grep_symbol
  lines: 1165-1197
  signature: 'def _render_opencode_grep_symbol(_project_root: Path) -> str'
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_grep_symbol_neighbours
  lines: 1200-1233
  signature: 'def _render_opencode_grep_symbol_neighbours(_project_root: Path) -> str'
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_explain_symbol
  lines: 1236-1269
  signature: 'def _render_opencode_explain_symbol(_project_root: Path) -> str'
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_explain_symbol_refs
  lines: 1272-1304
  signature: 'def _render_opencode_explain_symbol_refs(_project_root: Path) -> str'
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_trace_flow
  lines: 1307-1343
  signature: 'def _render_opencode_trace_flow(_project_root: Path) -> str'
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_explain_flow
  lines: 1346-1382
  signature: 'def _render_opencode_explain_flow(_project_root: Path) -> str'
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_patch
  lines: 1390-1438
  signature: 'def _render_opencode_patch(_project_root: Path) -> str'
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_patch_drop
  lines: 1441-1482
  signature: 'def _render_opencode_patch_drop(_project_root: Path) -> str'
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_patch_list
  lines: 1485-1512
  signature: 'def _render_opencode_patch_list(_project_root: Path) -> str'
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_patch_apply
  lines: 1515-1559
  signature: 'def _render_opencode_patch_apply(_project_root: Path) -> str'
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_create_symbol
  lines: 1562-1619
  signature: 'def _render_opencode_create_symbol(_project_root: Path) -> str'
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_rename_symbol
  lines: 1622-1664
  signature: 'def _render_opencode_rename_symbol(_project_root: Path) -> str'
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_delete_symbol
  lines: 1667-1708
  signature: 'def _render_opencode_delete_symbol(_project_root: Path) -> str'
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_batch_patch
  lines: 1711-1765
  signature: 'def _render_opencode_batch_patch(_project_root: Path) -> str'
- kind: function
  qualified_name: trie/tool_override_install:_render_claude_code_hooks_json
  lines: 1773-1829
  signature: 'def _render_claude_code_hooks_json(_project_root: Path) -> str'
- kind: constant
  qualified_name: trie/tool_override_install:TARGETS
  lines: 1838-2038
- kind: class
  qualified_name: trie/tool_override_install:ToolOverrideInstallPlan
  lines: 2047-2053
  signature: class ToolOverrideInstallPlan
- kind: function
  qualified_name: trie/tool_override_install:install
  lines: 2056-2095
  signature: 'def install( *, target_names: list[str] | None, print_only: bool, dry_run: bool, project_root: Path, ) -> ToolOverrideInstallPlan'
- kind: function
  qualified_name: trie/tool_override_install:apply_one
  lines: 2098-2155
  signature: 'def apply_one( target: ToolOverrideTarget, project_root: Path, print_only: bool, dry_run: bool, *, scope: Scope = "project", ) -> ToolOverrideApplyResult'
- kind: function
  qualified_name: trie/tool_override_install:_remove_obsolete
  lines: 2158-2211
  signature: 'def _remove_obsolete( relative_path: tuple[str, ...], project_root: Path, print_only: bool, dry_run: bool, ) -> ToolOverrideFileResult'
- kind: function
  qualified_name: trie/tool_override_install:_apply_file
  lines: 2214-2278
  signature: 'def _apply_file( spec: FileToWrite, project_root: Path, print_only: bool, dry_run: bool, ) -> ToolOverrideFileResult'
incoming_refs: 35
outgoing_refs: 0
---
<!-- trie:section symbol=trie/tool_override_install:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=4e6de758272688556670f60a4f9a81c71c6939abcb78cf111e99d093fbce4312 source_ref=6967f23962876ba37085c9375bb9b409583814a1 role=orchestration -->
Tool-override installation: replaces an agent's built-in tools with trie wrappers to make trie usage unavoidable.

- **opencode**: drop-in override files for grep/read, adds trace, grep_str, grep_entry_points, grep_symbol, grep_symbol_neighbours, explain_symbol, explain_symbol_refs, trace_flow, explain_flow, plus patch tools
- **Claude Code**: PreToolUse advisory hook that nudges toward mcp__trie__grep when agent reaches for built-in Grep
- **Other harnesses**: need_manual_setup instructions since no override mechanism exists
- Generated files carry auto-generated notices; deleting a file opts out of that override
- Companion to mcp_install (makes trie available) and hook_install (makes it automatic)
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:Action fingerprint=6d5466b453e0912edae50fab1848c782530de9137450b5c33b3682dc80488f21 body_fp=6c70c0a2c4334d66b609fcf1895be84b88d86f0815ea6d2112df98ced0fe0908 source_ref=6967f23962876ba37085c9375bb9b409583814a1 role=model -->
Type alias for tool override installation outcome statuses.

- `created` — new file written
- `updated` — existing file overwritten with new content
- `skipped` — existing file unchanged (same content)
- `preview` — shows what would happen without writing
- `error` — write operation failed
- `needs_manual_setup` — target has no automated override mechanism
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:ToolOverrideInstallError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=313bc3f0ee50338b03a75a3b17cd23f8e17ece0f2c85d7a4308b72078d7479bb source_ref=6967f23962876ba37085c9375bb9b409583814a1 role=model -->
## `class ToolOverrideInstallError(Exception)`

Exception raised by ToolOverrideInstallError operations when installation or validation fails.

- Subclasses standard `Exception` with no additional behavior
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:FileToWrite fingerprint=d1463a335d153224df4e0fbe524be20b78d6d8091a383d10a9790a3b0e2a7bc7 body_fp=473901eb4da518e75c748b7ff82ea5d63b95b848276c4d5ed1ddf5042ab69b13 source_ref=6967f23962876ba37085c9375bb9b409583814a1 role=model -->
## `class FileToWrite`

Describes one file an override target needs on disk for tool override installation.

- `relative_path`: file location as path segments tuple
- `render`: callable that generates file contents given project root
- `description`: human-readable label for install reports
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:ToolOverrideApplyResult fingerprint=7cddfb44189be40c0f69532eed1cb7932f69fa3fd6d833f65a5666f956fb18e4 body_fp=ee72a97308b0f954aba4b05d641309e9805631c4bd9a649b72790620ecf23697 source_ref=6967f23962876ba37085c9375bb9b409583814a1 role=model -->
## `class ToolOverrideApplyResult`

Encapsulates the result of installing tool override files for a single target.

- `action`: Summarized outcome across all files - "error" if any failed, "skipped" if all unchanged, otherwise "created" or "updated" reflecting the highest-energy change
- `files`: Per-file results for granular CLI reporting of which overrides were applied or skipped
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:ToolOverrideFileResult fingerprint=95c3d41b7de9da2d5f20aaa8a72438d7c4bcf3c67de66f8868b3e533a58b4243 body_fp=f4d1f0237e206f46af7532ef83159f676015587b95e528f3343fbf5b712bca1b source_ref=6967f23962876ba37085c9375bb9b409583814a1 role=model -->
## `class ToolOverrideFileResult`

Per-file outcome inside a target's apply result.

- `action`: Action taken on the file - "created", "updated", "skipped", "preview", or "error"
- `path`: Absolute path where file was processed, or None for virtual operations
- `detail`: Additional context about the action taken or error encountered
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:ToolOverrideTarget fingerprint=b964401eaed7403ce2d98e9a483745ee19a1868524d0784dc5a3f5dc20b794fc body_fp=73d1e9c19ad2caac262ccd92043ae9e3855a610759bb5e2e8fa998c68bc94deb source_ref=6967f23962876ba37085c9375bb9b409583814a1 role=model -->
## `class ToolOverrideTarget`

Describes an agent's tool-override surface and installation requirements.

- `files`: Override files to write; empty list means no automatable path exists
- `obsolete_files`: Paths to delete from prior trie setup versions during apply
- `manual_instructions`: Guidance shown when no automated override is available
- `summary`: One-line description of what installing actually does for consent prompts
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_GENERATED_HEADER fingerprint=9dee807c69fc07fab72c6209e764e2323da49f8dcd319a9c54481dbecbb5889a body_fp=1cb2c4b662f77e7586b2d356fccd30b1c00b0a6f9f64be757a5e90465db1c1d4 source_ref=6967f23962876ba37085c9375bb9b409583814a1 role=config -->
Standard TypeScript header comment injected into all generated opencode tool override files.

- Contains warning against manual editing and instructions for opting out
- References opencode.ai custom-tools documentation
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_grep_override fingerprint=486df3280b6418cf66318d5682f29bfafd8e00d78e9aa311b4f0f3fdbaf564ff body_fp=cad891db8c7039f9b7f67d5f118545cb6ae21ea84d798bfb3d368f252f1b3624 source_ref=ac5d9bf06782e0f9333fe020a4e73cca9a867fc6 role=io -->
## `def _render_opencode_grep_override(_project_root: Path) -> str`

Generates the TypeScript source for opencode's `grep.ts` tool override that replaces the built-in grep with symbol-aware search via `trie grep`.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_read_override fingerprint=421d562a7998dbe841f8e323c311b28b6f19d152cdbdc4f444a8eafd74ece182 body_fp=96d2e8cddfdc28548ba8b33093b9c1c04b8f60e7ac2b20fdb7debcecf5de374a source_ref=3a601e00b82ebd8a91dec91bf2edd78df42f870f role=io -->
## `def _render_opencode_read_override(_project_root: Path) -> str`

Generates TypeScript code for `.opencode/tools/read.ts` that overrides opencode's built-in `read` tool with trie-aware dispatch.

The override routes requests based on argument shape:
- **Qname paths** (contain `:`, not URL/drive): route to `trie read <qname>`
- **File paths with triefacts**: return compact view (symbol metadata + intros) by default, or agent-trimmed full view with `full: true`
- **Source fallthrough**: raw file bytes when `show_source: true`, no triefact exists, or `offset`/`limit` specified

The generated tool includes TypeScript telemetry emission to mirror Python's `cli_call` events, TOML config parsing, triefact frontmatter parsing (including an optional `signature` field per `defines` entry), and compact/full rendering modes that strip trie's internal machinery while preserving agent-relevant metadata. Compact mode prefers the frontmatter `signature` key over the section-body heading; `quoteYamlScalar` also quotes values containing `: ` or ` #` sequences (to handle annotated signatures).
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_trace fingerprint=174ad0a50e042d045578a0a16872a87c8a0776fdb8d0a619c8e84e194d562784 body_fp=dac105f2a350d1b98d7b3365f3c0fd0f034320408724d68f03fe76d1968c9d02 source_ref=ac5d9bf06782e0f9333fe020a4e73cca9a867fc6 role=io -->
## `def _render_opencode_trace(_project_root: Path) -> str`

Generate TypeScript tool override for opencode's `trace` command that shells out to `trie trace`.

The function renders `.opencode/tools/trace.ts` as a custom tool that exposes `trie trace` functionality to opencode agents. Since this is purely additive (no built-in collision), it creates a clean `trace` tool name without prefixes. The generated tool accepts a qualified symbol name, optional direction (callers/callees/both), and optional depth, then spawns a `trie trace` subprocess and returns the plain text output.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_grep_str fingerprint=f5f3bac0e07e83cb60c4f3605da6a9b7dafb2e575ca1cf8a3c2cd0b8aeeb736b body_fp=e2e444539e974cf474df9ab92dad0ab8df4fd900dc6b655c70c744e7a1267235 source_ref=ac5d9bf06782e0f9333fe020a4e73cca9a867fc6 role=io -->
## `def _render_opencode_grep_str(_project_root: Path) -> str`

Renders the TypeScript source for `.opencode/tools/grep_str.ts`, which wraps `trie grep-str` as an opencode custom tool.

- Returns TypeScript implementing a tool that searches source bodies with regex and attributes matches to enclosing symbols
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_grep_entry_points fingerprint=f5f3bac0e07e83cb60c4f3605da6a9b7dafb2e575ca1cf8a3c2cd0b8aeeb736b body_fp=4eb97cd200294091d0798115f5d3873635d238ddce469c27badbc3fb9851539b source_ref=ac5d9bf06782e0f9333fe020a4e73cca9a867fc6 role=io -->
## `def _render_opencode_grep_entry_points(_project_root: Path) -> str`

Generates TypeScript tool definition for opencode's `grep_entry_points` tool that shells out to `trie grep-entry-points`.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_grep_symbol fingerprint=f5f3bac0e07e83cb60c4f3605da6a9b7dafb2e575ca1cf8a3c2cd0b8aeeb736b body_fp=94b909cbda7c09a96e3796692f03d369fb1d02908591e6df629ac42bd8526d77 source_ref=ac5d9bf06782e0f9333fe020a4e73cca9a867fc6 role=io -->
## `def _render_opencode_grep_symbol(_project_root: Path) -> str`

Generates opencode tool override for fuzzy symbol name lookup via `trie grep-symbol`.

- Returns TypeScript tool definition that wraps `trie grep-symbol` command
- Spawns subprocess with single `sym` argument for fuzzy matching
- Handles exit codes 0/1 as success, throws error for other codes
- Used by opencode target to add `grep_symbol` tool alongside built-in overrides
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_grep_symbol_neighbours fingerprint=f5f3bac0e07e83cb60c4f3605da6a9b7dafb2e575ca1cf8a3c2cd0b8aeeb736b body_fp=d9c9e4d1c8829ce3cf4c6ee90303966eaf17bd75d852e5e0d41e4a24657d3ad9 source_ref=ac5d9bf06782e0f9333fe020a4e73cca9a867fc6 role=io -->
## `def _render_opencode_grep_symbol_neighbours(_project_root: Path) -> str`

Renders the TypeScript source for an opencode `grep-symbol-neighbours` tool that shells out to `trie grep-symbol-neighbours`.

- Returns a TypeScript tool module with a generated header and no-edit warning
- Creates a fuzzy symbol lookup tool that includes immediate callers and callees metadata
- Accepts a `sym` parameter for the symbol name or fragment to match
- Spawns `trie grep-symbol-neighbours` subprocess and returns stdout on success
- Throws errors for non-zero exit codes except 1 (structured trie errors)
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_explain_symbol fingerprint=f5f3bac0e07e83cb60c4f3605da6a9b7dafb2e575ca1cf8a3c2cd0b8aeeb736b body_fp=2bb726fbb3e62ffd2b7571875142518d53d4f6c618125056b84076cf63eb93e0 source_ref=ac5d9bf06782e0f9333fe020a4e73cca9a867fc6 role=io -->
## `def _render_opencode_explain_symbol(_project_root: Path) -> str`

Renders the opencode tool override for `explain_symbol.ts`, which provides full prose and narrative for a symbol plus its callers/callees.

- Returns TypeScript tool definition that shells out to `trie explain-symbol`
- Accepts `sym` parameter (qname or name fragment) to identify the target symbol
- Uses Bun.spawn to execute the trie CLI with proper error handling
- Tool description emphasizes deep understanding beyond just docstrings
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_explain_symbol_refs fingerprint=f5f3bac0e07e83cb60c4f3605da6a9b7dafb2e575ca1cf8a3c2cd0b8aeeb736b body_fp=5d4ebc90795f60dfd9c83e7bf08541572f7d77f3fd63be2f2b621dcb42d53f62 source_ref=ac5d9bf06782e0f9333fe020a4e73cca9a867fc6 role=io -->
## `def _render_opencode_explain_symbol_refs(_project_root: Path) -> str`

Renders the opencode tool `explain_symbol_refs.ts` that wraps `trie explain-symbol-refs`.

- Returns a TypeScript tool definition with description, args schema, and execute handler
- Tool explains symbol usage by showing callers and their prose (skipping the symbol's own documentation)
- Shells out to `trie explain-symbol-refs` subprocess and returns stdout on success
- Handles exit codes 0/1 as success, throws errors for other codes
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_trace_flow fingerprint=f5f3bac0e07e83cb60c4f3605da6a9b7dafb2e575ca1cf8a3c2cd0b8aeeb736b body_fp=0cc36a1de96b7edeca7d915f73afbf04d02114a2b693f168f68063daa0393c3b source_ref=ac5d9bf06782e0f9333fe020a4e73cca9a867fc6 role=io -->
## `def _render_opencode_trace_flow(_project_root: Path) -> str`

Renders the TypeScript source for opencode's `trace_flow.ts` custom tool.

Generates a tool that wraps `trie trace-flow` to find call chains between two symbols, returning the shortest paths following callee edges or clearly stating when no path exists within search depth.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_explain_flow fingerprint=f5f3bac0e07e83cb60c4f3605da6a9b7dafb2e575ca1cf8a3c2cd0b8aeeb736b body_fp=f5dfc12747bdc88f7f6323ed5905aa38e8dcda6a4342c0c80613fc9298b682a5 source_ref=ac5d9bf06782e0f9333fe020a4e73cca9a867fc6 role=io -->
## `def _render_opencode_explain_flow(_project_root: Path) -> str`

Renders TypeScript code for an opencode `explain_flow.ts` tool that wraps `trie explain-flow`.

- Creates tool that takes two symbols and narrates execution flow with prose
- Spawns `trie explain-flow <symbol1> <symbol2>` subprocess via Bun
- Returns stdout on exit codes 0-1, throws error on other codes
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_patch fingerprint=f5f3bac0e07e83cb60c4f3605da6a9b7dafb2e575ca1cf8a3c2cd0b8aeeb736b body_fp=3e6d30fe8db510c59c6b7a430027227921eb04ff7031b849ecef17d1ff1d8a47 source_ref=ac5d9bf06782e0f9333fe020a4e73cca9a867fc6 role=io -->
## `def _render_opencode_patch(_project_root: Path) -> str`

Renders the TypeScript source for an opencode `patch.ts` tool that posts implementation notes against symbols.

- Returns complete TypeScript tool definition that calls `trie patch create`
- Accepts qname (required), note (required), and reason (optional) parameters
- Wraps trie CLI subprocess execution with error handling and result parsing
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_patch_drop fingerprint=f5f3bac0e07e83cb60c4f3605da6a9b7dafb2e575ca1cf8a3c2cd0b8aeeb736b body_fp=659a631eea752e4ec0b237dbefba5bcdca8e19b1c5b664d213cdda426291ce41 source_ref=ac5d9bf06782e0f9333fe020a4e73cca9a867fc6 role=io -->
## `def _render_opencode_patch_drop(_project_root: Path) -> str`

Renders the TypeScript for opencode's `patch_drop` tool that removes pending patches by symbol or clears all.

- Returns complete TypeScript tool definition with header and error handling
- Tool accepts either `qname` for symbol-specific removal or `all` flag for full clear
- Validates that exactly one of `qname` or `all` is provided, throws error otherwise
- Shells out to `trie patch drop` subprocess with appropriate flags
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_patch_list fingerprint=95b007327a420376dc8fdfba06848b6ddb487d7b5cce02afbd87432be35c8205 body_fp=30b4b46304e00ca528022b746ccb074ba78decf8fd46654602155b464586709a source_ref=ac5d9bf06782e0f9333fe020a4e73cca9a867fc6 role=io -->
## `def _render_opencode_patch_list(_project_root: Path) -> str`

Generate TypeScript tool for opencode that lists pending patches by symbol.

Returns a generated TypeScript tool definition that shells out to `trie patch list` and displays the symbol-grouped patches to the agent. The tool takes no arguments and formats output to show "(no pending patches)" when the command succeeds but produces no output.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_patch_apply fingerprint=f5f3bac0e07e83cb60c4f3605da6a9b7dafb2e575ca1cf8a3c2cd0b8aeeb736b body_fp=5550a85a788dd732086f3bee9c26e3b4cbf3501a4690220230657740a727dbba source_ref=ac5d9bf06782e0f9333fe020a4e73cca9a867fc6 role=io -->
## `def _render_opencode_patch_apply(_project_root: Path) -> str`

Generates TypeScript source for opencode's `patch_apply.ts` tool override.

- Returns template code that wraps `trie patch apply` subprocess calls
- Accepts only `session_note` (required for multi-symbol applies); `backend`, `commit_mode`, and `verbose` args removed
- Generated tool description clarifies that `patch apply` archives intent only — trie generates no code
- Generated tool description includes gate-coverage output: touched symbols still lacking notes are listed after apply
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_create_symbol fingerprint=f5f3bac0e07e83cb60c4f3605da6a9b7dafb2e575ca1cf8a3c2cd0b8aeeb736b body_fp=b9f72276e966e26d5ce2d0ab558074ab78b77a5dd7a53e250a59fb2a4445b0a8 source_ref=ac5d9bf06782e0f9333fe020a4e73cca9a867fc6 role=io -->
## `def _render_opencode_create_symbol(_project_root: Path) -> str`

Render the `.opencode/tools/create_symbol.ts` override file that stages creation of a new symbol via `trie patch create-symbol`.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_rename_symbol fingerprint=f5f3bac0e07e83cb60c4f3605da6a9b7dafb2e575ca1cf8a3c2cd0b8aeeb736b body_fp=9953fe573fc8b557a7d0e2a5152d516394e6bcb31e3d0a27e33e3658d298d70c source_ref=ac5d9bf06782e0f9333fe020a4e73cca9a867fc6 role=io -->
## `def _render_opencode_rename_symbol(_project_root: Path) -> str`

Render the `.opencode/tools/rename_symbol.ts` content that stages a symbol rename via `trie patch rename-symbol`.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_delete_symbol fingerprint=e04b220fcfe5b1376f33b3791796d18d76acda70c5e5cc42a408a7671fbab7c6 body_fp=e1cf6d16090991063c61f1dfdcfb5f7a7aba7b4be5b5aa2a1577d5cb35971ea5 source_ref=ac5d9bf06782e0f9333fe020a4e73cca9a867fc6 role=io -->
## `def _render_opencode_delete_symbol(_project_root: Path) -> str`

Render the `.opencode/tools/delete_symbol.ts` source string that stages deletion of an existing symbol via `trie patch delete-symbol`.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_batch_patch fingerprint=f5f3bac0e07e83cb60c4f3605da6a9b7dafb2e575ca1cf8a3c2cd0b8aeeb736b body_fp=b3dafa1e75c3693178c24aa40b2245aee43e183f2f18be64cbe55bee1166167f source_ref=ac5d9bf06782e0f9333fe020a4e73cca9a867fc6 role=io -->
## `def _render_opencode_batch_patch(_project_root: Path) -> str`

Render the `.opencode/tools/batch_patch.ts` custom tool that pipes a JSON array of patch/create items to `trie patch create-batch` via stdin.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_claude_code_hooks_json fingerprint=2b004e51b57a5be1e5d0181eb5239d9e0484ae53fc4b78e3acda4c59131e21ed body_fp=f630162e7d7fb922045111edf902333fbf795ed8b11038dad5825103abff5473 source_ref=6967f23962876ba37085c9375bb9b409583814a1 role=io -->
## `def _render_claude_code_hooks_json(_project_root: Path) -> str`

Generates JSON hook config for Claude Code that advises using trie's grep over the built-in when Claude attempts Grep calls.

- Creates a PreToolUse hook that matches built-in `Grep` tool usage
- Emits a system message nudging Claude toward `mcp__trie__grep` for symbol/structure queries
- Outputs complete JSON config with auto-generation notice and removal instructions
- Non-blocking advisory only — built-in Grep still functions, agent just sees the tip
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:TARGETS fingerprint=36657fdefdc2da6e79ef59ba09a8d595f194fc582693387897666a5b36b198b5 body_fp=43e23eb41ac5750b3b5363eaeea82ef6a3668d5939ca14de9f5d7cdeba58e131 source_ref=6967f23962876ba37085c9375bb9b409583814a1 role=config -->
Registry mapping target names to tool-override installation specs for supported agent harnesses.

- **opencode**: overrides built-in `grep`/`read`, adds 19 trie-aware tools (including `trace`, search variants, explanation tools, and patching workflow — now including `create_symbol`, `rename_symbol`, `delete_symbol`, `batch_patch`); also cleans up obsolete `patch_batch.ts` on apply
- **claude-code**: installs PreToolUse advisory hook nudging toward `mcp__trie__grep`
- **claude-desktop**, **cursor**, **windsurf**, **vscode**, **codex**: no automated override path (manual instructions only)
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:ToolOverrideInstallPlan fingerprint=83ec1a61df42535b35c8b51fedbfbfc45086f0e5962ba7c40558117b34de29df body_fp=1a74c7ac0a2aeaf2010b0cba60563372907924a379bf9cad6d1b9846039ef88a source_ref=6967f23962876ba37085c9375bb9b409583814a1 role=model -->
## `class ToolOverrideInstallPlan`

Aggregate result of a full `install` call across one or more targets.

- `target_names`: List of target names that were processed during install
- `print_only`: Whether the install was run in print-only mode (no files written)
- `dry_run`: Whether the install was run in dry-run mode (no files written)
- `results`: List of per-target apply results, empty by default
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:install fingerprint=d1450ff3c792844aaa780cfdb60ec25d3403dafdee9b932957ea583841beaf10 body_fp=e9cb8a9b4b154d4834f10823ccf789a3ab00401e2e52928a40fd8c303186e934 source_ref=6967f23962876ba37085c9375bb9b409583814a1 role=orchestration -->
## `def install( *, target_names: list[str] | None, print_only: bool, dry_run: bool, project_root: Path, ) -> ToolOverrideInstallPlan`

Apply tool-override files for one or more targets.

- `target_names`: Must be explicit; no `install_all` to prevent accidental multi-target rollout
- Raises `ToolOverrideInstallError` for unknown target names or missing target list
- Returns `ToolOverrideInstallPlan` with per-target `apply_one` results
- Symmetric with `mcp_install.install` and `hook_install.install` for flag semantics
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:apply_one fingerprint=ba92586faae5c98a3f4a5228889bd4a297381515308bc99e0afaba467e97047f body_fp=434509e5b5df60419842d115a736fcbad1d3c8c0bd951e358eb8d1ebaf4632e2 source_ref=6967f23962876ba37085c9375bb9b409583814a1 role=orchestration -->
## `def apply_one( target: ToolOverrideTarget, project_root: Path, print_only: bool, dry_run: bool, *, scope: Scope = "project", ) -> ToolOverrideApplyResult`

Installs override files for a target, rendering each file and comparing against existing contents.

- Returns `needs_manual_setup` when `target.files` is empty
- Processes each file spec via `_apply_file`, then removes obsolete files via `_remove_obsolete`
- Summarizes per-file actions into target-level action with precedence: error > created/updated > preview > skipped
- `scope` parameter accepted for API symmetry but currently unused
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_remove_obsolete fingerprint=2c10eaaf6621f765d84ecc5d05ce22304e2c4d73c09fd8511dafcf9069194641 body_fp=60d447a77640da96bd3ccd29bac6895404366dc9587853bda3b77ea343215a3e source_ref=6967f23962876ba37085c9375bb9b409583814a1 role=io -->
## `def _remove_obsolete( relative_path: tuple[str, ...], project_root: Path, print_only: bool, dry_run: bool, ) -> ToolOverrideFileResult`

Removes obsolete tool-override files that earlier trie versions installed but newer ones don't need.

- Returns `"skipped"` if the target file doesn't exist
- Returns `"preview"` when `print_only` or `dry_run` is True without touching disk
- Returns `"error"` if file deletion fails with OSError details
- Returns `"updated"` after successful removal (file state changed)
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_apply_file fingerprint=a55304ab263ea6f60e2d442ead639c43d89f3b54e65dda158b61cb687f3febf3 body_fp=1d950c416a49704d94665ab906ec17be6bd0bcb29ed95939881aec72487dfc9e source_ref=6967f23962876ba37085c9375bb9b409583814a1 role=io -->
## `def _apply_file( spec: FileToWrite, project_root: Path, print_only: bool, dry_run: bool, ) -> ToolOverrideFileResult`

Materialises one tool-override file to disk with idempotency checking and preview modes.

- Renders file contents via `spec.render()` and resolves target path under project root  
- Returns `"preview"` action for `print_only` or `dry_run` modes without writing
- Returns `"skipped"` when existing file has identical contents  
- Returns `"error"` if existing file cannot be read
- Creates parent directories and writes file, returning `"created"` or `"updated"`
<!-- trie:end -->