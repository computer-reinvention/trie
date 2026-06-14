---
trie_version: 0.1.5
source: trie/tool_override_install.py
file_fingerprint: cf20a2f7b92f6a86f71b576ebacd67f79a073cd62eed7d433fb16b055a72c738
last_synced_at: '2026-06-03T20:38:51Z'
description: 'Tool-override installation: replace an agent''s built-in tools with
  trie wrappers.'
defines:
- kind: module
  qualified_name: trie/tool_override_install:__module__
  lines: 1-1992
- kind: constant
  qualified_name: trie/tool_override_install:Action
  lines: 39-39
- kind: class
  qualified_name: trie/tool_override_install:ToolOverrideInstallError
  lines: 42-43
- kind: class
  qualified_name: trie/tool_override_install:FileToWrite
  lines: 47-58
- kind: class
  qualified_name: trie/tool_override_install:ToolOverrideApplyResult
  lines: 62-75
- kind: class
  qualified_name: trie/tool_override_install:ToolOverrideFileResult
  lines: 79-86
- kind: class
  qualified_name: trie/tool_override_install:ToolOverrideTarget
  lines: 90-114
- kind: constant
  qualified_name: trie/tool_override_install:_GENERATED_HEADER
  lines: 122-127
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_grep_override
  lines: 130-232
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_read_override
  lines: 235-971
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_trace
  lines: 974-1043
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_grep_str
  lines: 1051-1084
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_grep_entry_points
  lines: 1087-1119
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_grep_symbol
  lines: 1122-1154
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_grep_symbol_neighbours
  lines: 1157-1190
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_explain_symbol
  lines: 1193-1226
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_explain_symbol_refs
  lines: 1229-1261
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_trace_flow
  lines: 1264-1300
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_explain_flow
  lines: 1303-1339
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_patch
  lines: 1347-1392
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_patch_drop
  lines: 1395-1436
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_patch_list
  lines: 1439-1466
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_patch_apply
  lines: 1469-1505
- kind: function
  qualified_name: trie/tool_override_install:_render_claude_code_hooks_json
  lines: 1513-1569
- kind: constant
  qualified_name: trie/tool_override_install:TARGETS
  lines: 1578-1751
- kind: class
  qualified_name: trie/tool_override_install:ToolOverrideInstallPlan
  lines: 1760-1766
- kind: function
  qualified_name: trie/tool_override_install:install
  lines: 1769-1808
- kind: function
  qualified_name: trie/tool_override_install:apply_one
  lines: 1811-1868
- kind: function
  qualified_name: trie/tool_override_install:_remove_obsolete
  lines: 1871-1924
- kind: function
  qualified_name: trie/tool_override_install:_apply_file
  lines: 1927-1991
incoming_refs: 33
outgoing_refs: 0
---
<!-- trie:section symbol=trie/tool_override_install:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=4e6de758272688556670f60a4f9a81c71c6939abcb78cf111e99d093fbce4312 source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
Tool-override installation: replaces an agent's built-in tools with trie wrappers to make trie usage unavoidable.

- **opencode**: drop-in override files for grep/read, adds trace, grep_str, grep_entry_points, grep_symbol, grep_symbol_neighbours, explain_symbol, explain_symbol_refs, trace_flow, explain_flow, plus patch tools
- **Claude Code**: PreToolUse advisory hook that nudges toward mcp__trie__grep when agent reaches for built-in Grep
- **Other harnesses**: need_manual_setup instructions since no override mechanism exists
- Generated files carry auto-generated notices; deleting a file opts out of that override
- Companion to mcp_install (makes trie available) and hook_install (makes it automatic)
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:Action fingerprint=6d5466b453e0912edae50fab1848c782530de9137450b5c33b3682dc80488f21 body_fp=6c70c0a2c4334d66b609fcf1895be84b88d86f0815ea6d2112df98ced0fe0908 source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
Type alias for tool override installation outcome statuses.

- `created` — new file written
- `updated` — existing file overwritten with new content
- `skipped` — existing file unchanged (same content)
- `preview` — shows what would happen without writing
- `error` — write operation failed
- `needs_manual_setup` — target has no automated override mechanism
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:ToolOverrideInstallError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=c93f07c74fc9114314e7a965c12ddcb1082c94e42f503b7ff39a695971a93fe8 source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
Exception raised by ToolOverrideInstallError operations when installation or validation fails.

- Subclasses standard `Exception` with no additional behavior
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:FileToWrite fingerprint=d1463a335d153224df4e0fbe524be20b78d6d8091a383d10a9790a3b0e2a7bc7 body_fp=b3bf167fb599067e3e42f7706f923441a97bfa58403eefc184627345ca5c8d3b source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
Describes one file an override target needs on disk for tool override installation.

- `relative_path`: file location as path segments tuple
- `render`: callable that generates file contents given project root
- `description`: human-readable label for install reports
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:ToolOverrideApplyResult fingerprint=7cddfb44189be40c0f69532eed1cb7932f69fa3fd6d833f65a5666f956fb18e4 body_fp=c7a954b95d7701ea39b26ddbc8262d5d738d0510b107fbc4de74b919296ca41f source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
Encapsulates the result of installing tool override files for a single target.

- `action`: Summarized outcome across all files - "error" if any failed, "skipped" if all unchanged, otherwise "created" or "updated" reflecting the highest-energy change
- `files`: Per-file results for granular CLI reporting of which overrides were applied or skipped
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:ToolOverrideFileResult fingerprint=95c3d41b7de9da2d5f20aaa8a72438d7c4bcf3c67de66f8868b3e533a58b4243 body_fp=e499a34ab835b5a18e70fb5945425d7426feb46d8c95b70607998149ee8335e3 source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
## ToolOverrideFileResult(relative_path, action, path, description, detail="")

Per-file outcome inside a target's apply result.

- `action`: Action taken on the file - "created", "updated", "skipped", "preview", or "error"
- `path`: Absolute path where file was processed, or None for virtual operations
- `detail`: Additional context about the action taken or error encountered
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:ToolOverrideTarget fingerprint=b964401eaed7403ce2d98e9a483745ee19a1868524d0784dc5a3f5dc20b794fc body_fp=5eea55495f5f88b865d34c635abb5d9f8c279145138d533972a85b80ab47b1c7 source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
Describes an agent's tool-override surface and installation requirements.

- `files`: Override files to write; empty list means no automatable path exists
- `obsolete_files`: Paths to delete from prior trie setup versions during apply
- `manual_instructions`: Guidance shown when no automated override is available
- `summary`: One-line description of what installing actually does for consent prompts
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_GENERATED_HEADER fingerprint=9dee807c69fc07fab72c6209e764e2323da49f8dcd319a9c54481dbecbb5889a body_fp=1cb2c4b662f77e7586b2d356fccd30b1c00b0a6f9f64be757a5e90465db1c1d4 source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
Standard TypeScript header comment injected into all generated opencode tool override files.

- Contains warning against manual editing and instructions for opting out
- References opencode.ai custom-tools documentation
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_grep_override fingerprint=ae1bb9a2dfb2e20aa6ee58d36a1acc2044aada27b0475972e707f9af1f84c2ec body_fp=effa9eadec1298bbf56a76a7ed95c0c3721dde375a55de9b6fe4183c9f9e12bc source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
Generates the TypeScript source for opencode's `grep.ts` tool override that replaces the built-in grep with symbol-aware search via `trie grep`.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_read_override fingerprint=ffe463adc332d1f0f88803fa18b58ae49c3b0e654de8c52d6130ffd38a1cfc29 body_fp=f55d7a489f1e10ac416cd3ea564d6eb021fd49b18c3e1ee4ef05a3fb707264d1 source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
Generates TypeScript code for `.opencode/tools/read.ts` that overrides opencode's built-in `read` tool with trie-aware dispatch.

The override routes requests based on argument shape:
- **Qname paths** (contain `:`, not URL/drive): route to `trie read <qname>`
- **File paths with triefacts**: return compact view (symbol metadata + intros) by default, or agent-trimmed full view with `full: true`
- **Source fallthrough**: raw file bytes when `show_source: true`, no triefact exists, or `offset`/`limit` specified

The generated tool includes TypeScript telemetry emission to mirror Python's `cli_call` events, TOML config parsing, triefact frontmatter parsing, and compact/full rendering modes that strip trie's internal machinery while preserving agent-relevant metadata.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_trace fingerprint=33f21409112cc93e5bd7b1ea55ec2806b431a24243d780acd9aa0425eb300959 body_fp=c13f027796659665154aaf4da5883c8222db475096177423eb417d158a853dc8 source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
Generate TypeScript tool override for opencode's `trace` command that shells out to `trie trace`.

The function renders `.opencode/tools/trace.ts` as a custom tool that exposes `trie trace` functionality to opencode agents. Since this is purely additive (no built-in collision), it creates a clean `trace` tool name without prefixes. The generated tool accepts a qualified symbol name, optional direction (callers/callees/both), and optional depth, then spawns a `trie trace` subprocess and returns the plain text output.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_grep_str fingerprint=58319bb302d242e7793e07fbc486394d9929f9b77d2e5b4c7b67871c72313bbb body_fp=e2e444539e974cf474df9ab92dad0ab8df4fd900dc6b655c70c744e7a1267235 source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
## `def _render_opencode_grep_str(_project_root: Path) -> str`

Renders the TypeScript source for `.opencode/tools/grep_str.ts`, which wraps `trie grep-str` as an opencode custom tool.

- Returns TypeScript implementing a tool that searches source bodies with regex and attributes matches to enclosing symbols
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_grep_entry_points fingerprint=c103f37b0731a78f4946f00df70aa0a7c59469865fa179bcc49b4f126a9be390 body_fp=b2bea9c0aafb42bce8ab8d114f538cdaf47530c9f66edfd0474ce81992c2c018 source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
Generates TypeScript tool definition for opencode's `grep_entry_points` tool that shells out to `trie grep-entry-points`.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_grep_symbol fingerprint=5fe0f8a345b92f4e74ab8594f01138a2ca9465f62424c8cca778c6243f42bdcd body_fp=af70a2b4fe2c1890a23a19b1c10f76aea0d80f7f8b21f5a1185ba70b1bc15c1d source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
Generates opencode tool override for fuzzy symbol name lookup via `trie grep-symbol`.

- Returns TypeScript tool definition that wraps `trie grep-symbol` command
- Spawns subprocess with single `sym` argument for fuzzy matching
- Handles exit codes 0/1 as success, throws error for other codes
- Used by opencode target to add `grep_symbol` tool alongside built-in overrides
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_grep_symbol_neighbours fingerprint=fd4dd9c1438e507552610e6b0b7208cd5eda44be46f6fe56f3ac96de1bda926b body_fp=930bbfa81ace896850614d5e25e9e21343ea6510e30157817857f008e8bb5b9a source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
Renders the TypeScript source for an opencode `grep-symbol-neighbours` tool that shells out to `trie grep-symbol-neighbours`.

- Returns a TypeScript tool module with a generated header and no-edit warning
- Creates a fuzzy symbol lookup tool that includes immediate callers and callees metadata
- Accepts a `sym` parameter for the symbol name or fragment to match
- Spawns `trie grep-symbol-neighbours` subprocess and returns stdout on success
- Throws errors for non-zero exit codes except 1 (structured trie errors)
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_explain_symbol fingerprint=3d74449df7ba7f3d9b5fa4b53a18b86d658841f1dd02f5df48c5b229f9eea361 body_fp=e7ed04c1f760c4c071aecb4ac44a01e6427cdb1c98f7ef35dad11fa9a5b61ecc source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
Renders the opencode tool override for `explain_symbol.ts`, which provides full prose and narrative for a symbol plus its callers/callees.

- Returns TypeScript tool definition that shells out to `trie explain-symbol`
- Accepts `sym` parameter (qname or name fragment) to identify the target symbol
- Uses Bun.spawn to execute the trie CLI with proper error handling
- Tool description emphasizes deep understanding beyond just docstrings
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_explain_symbol_refs fingerprint=ccf063b124b1693e10748b1ce8eab31574140cd313a5456a07f70effd3ac958d body_fp=4118a968cfd2c78b0693c52835d5301216c798f951b295a4b9179cefb999e78d source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
Renders the opencode tool `explain_symbol_refs.ts` that wraps `trie explain-symbol-refs`.

- Returns a TypeScript tool definition with description, args schema, and execute handler
- Tool explains symbol usage by showing callers and their prose (skipping the symbol's own documentation)
- Shells out to `trie explain-symbol-refs` subprocess and returns stdout on success
- Handles exit codes 0/1 as success, throws errors for other codes
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_trace_flow fingerprint=27e2f63229308ef7da4fbbe00d2462f2457e8587819484054e13f589be0db140 body_fp=17ab203fc56a16b2a3aff2d0ae25ee9ac2ffe49a6c25453b7172764326b7d414 source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
Renders the TypeScript source for opencode's `trace_flow.ts` custom tool.

Generates a tool that wraps `trie trace-flow` to find call chains between two symbols, returning the shortest paths following callee edges or clearly stating when no path exists within search depth.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_explain_flow fingerprint=60bc58f220fddf22d79fc3b0feb7c064f81546e80a928f6c04fd14cf7cbd70b0 body_fp=febfcdeddb9f799a503c8c8cb2623db038371c1a154426f60e50ad0de2e64846 source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
Renders TypeScript code for an opencode `explain_flow.ts` tool that wraps `trie explain-flow`.

- Creates tool that takes two symbols and narrates execution flow with prose
- Spawns `trie explain-flow <symbol1> <symbol2>` subprocess via Bun
- Returns stdout on exit codes 0-1, throws error on other codes
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_patch fingerprint=7d3eeaa5500b89ea0b3f58626af2edecfd4e01b955c1dc949259babdde12784c body_fp=e1a92fe20ddfa6618f2874b6cd776bf5b348b2bf9583760d06219934041fbf4e source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
Renders the TypeScript source for an opencode `patch.ts` tool that posts implementation notes against symbols.

- Returns complete TypeScript tool definition that calls `trie patch create`
- Accepts qname (required), note (required), and reason (optional) parameters
- Wraps trie CLI subprocess execution with error handling and result parsing
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_patch_drop fingerprint=c5a387d3ccd119d17f820125b1767dcb772ecdab7406226b76fd4aad95c70acd body_fp=b0804a1b59ecab06762aff0a88c2b8dcd5449b654a713ac99971b4ab620c20fd source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
Renders the TypeScript for opencode's `patch_drop` tool that removes pending patches by symbol or clears all.

- Returns complete TypeScript tool definition with header and error handling
- Tool accepts either `qname` for symbol-specific removal or `all` flag for full clear
- Validates that exactly one of `qname` or `all` is provided, throws error otherwise
- Shells out to `trie patch drop` subprocess with appropriate flags
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_patch_list fingerprint=f5f3bac0e07e83cb60c4f3605da6a9b7dafb2e575ca1cf8a3c2cd0b8aeeb736b body_fp=67ab942a35a42493599db73943dbe287496448b92d12c3a3d8fe94e113d8d499 source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
Generate TypeScript tool for opencode that lists pending patches by symbol.

Returns a generated TypeScript tool definition that shells out to `trie patch list` and displays the symbol-grouped patches to the agent. The tool takes no arguments and formats output to show "(no pending patches)" when the command succeeds but produces no output.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_patch_apply fingerprint=c1d3e2346fdc9369b2275316c79f709733b929a1107fac815ab6075c24603a5f body_fp=ab16b23c64541244aa78a3467b3d929f629315faed5c5b1d5cc97e9b36b6e7c9 source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
Generates TypeScript source for opencode's `patch_apply.ts` tool override.

- Returns template code that wraps `trie patch apply` subprocess calls
- Includes optional `verbose` flag for detailed per-symbol output during execution
- Part of opencode's tool override suite that replaces built-in tools with trie equivalents
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_claude_code_hooks_json fingerprint=2b004e51b57a5be1e5d0181eb5239d9e0484ae53fc4b78e3acda4c59131e21ed body_fp=cf4a62f79da4db7968bb2442a49ed25ab95898bfb70b197684a4a851f62d4686 source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
Generates JSON hook config for Claude Code that advises using trie's grep over the built-in when Claude attempts Grep calls.

- Creates a PreToolUse hook that matches built-in `Grep` tool usage
- Emits a system message nudging Claude toward `mcp__trie__grep` for symbol/structure queries
- Outputs complete JSON config with auto-generation notice and removal instructions
- Non-blocking advisory only — built-in Grep still functions, agent just sees the tip
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:TARGETS fingerprint=34ed053e3260f7d7d50751489108a97a3c33b6738a62034bd2797dbf3300480d body_fp=ea071268dd8f8c598cd2795de3e27a876b46fbb4db2d8cc4f0fc659851b30848 source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
Registry mapping target names to tool-override installation specs for supported agent harnesses.

- **opencode**: overrides built-in `grep`/`read`, adds 15 trie-aware tools (including `trace`, search variants, explanation tools, and patching workflow)
- **claude-code**: installs PreToolUse advisory hook nudging toward `mcp__trie__grep`
- **claude-desktop**, **cursor**, **windsurf**, **vscode**, **codex**: no automated override path (manual instructions only)
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:ToolOverrideInstallPlan fingerprint=83ec1a61df42535b35c8b51fedbfbfc45086f0e5962ba7c40558117b34de29df body_fp=9b54f41de2bee6ee68761dadb0f2d5d24fd9e6d2091245498965c8addee29df0 source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
Aggregate result of a full `install` call across one or more targets.

- `target_names`: List of target names that were processed during install
- `print_only`: Whether the install was run in print-only mode (no files written)
- `dry_run`: Whether the install was run in dry-run mode (no files written)
- `results`: List of per-target apply results, empty by default
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:install fingerprint=d1450ff3c792844aaa780cfdb60ec25d3403dafdee9b932957ea583841beaf10 body_fp=4fe8ad91ae2aa0881aa8dd338721de76faf6a3229bcf0838398826fefcb3eb77 source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
Apply tool-override files for one or more targets.

- `target_names`: Must be explicit; no `install_all` to prevent accidental multi-target rollout
- Raises `ToolOverrideInstallError` for unknown target names or missing target list
- Returns `ToolOverrideInstallPlan` with per-target `apply_one` results
- Symmetric with `mcp_install.install` and `hook_install.install` for flag semantics
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:apply_one fingerprint=ba92586faae5c98a3f4a5228889bd4a297381515308bc99e0afaba467e97047f body_fp=1fe57b7e7ce665e72db9562c5719930b0070c12507d51406998a19644e3a92c7 source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
Installs override files for a target, rendering each file and comparing against existing contents.

- Returns `needs_manual_setup` when `target.files` is empty
- Processes each file spec via `_apply_file`, then removes obsolete files via `_remove_obsolete`
- Summarizes per-file actions into target-level action with precedence: error > created/updated > preview > skipped
- `scope` parameter accepted for API symmetry but currently unused
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_remove_obsolete fingerprint=2c10eaaf6621f765d84ecc5d05ce22304e2c4d73c09fd8511dafcf9069194641 body_fp=260f9370346af85bf019649ef080bf369698932aa9fdec26cfdb0a95ffa9800e source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
Removes obsolete tool-override files that earlier trie versions installed but newer ones don't need.

- Returns `"skipped"` if the target file doesn't exist
- Returns `"preview"` when `print_only` or `dry_run` is True without touching disk
- Returns `"error"` if file deletion fails with OSError details
- Returns `"updated"` after successful removal (file state changed)
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_apply_file fingerprint=a55304ab263ea6f60e2d442ead639c43d89f3b54e65dda158b61cb687f3febf3 body_fp=8da4569d769123b304fafe04ba95eac374eea98ed3901d743f64ae80ec0c2b12 source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 role=agent-integration -->
Materialises one tool-override file to disk with idempotency checking and preview modes.

- Renders file contents via `spec.render()` and resolves target path under project root  
- Returns `"preview"` action for `print_only` or `dry_run` modes without writing
- Returns `"skipped"` when existing file has identical contents  
- Returns `"error"` if existing file cannot be read
- Creates parent directories and writes file, returning `"created"` or `"updated"`
<!-- trie:end -->