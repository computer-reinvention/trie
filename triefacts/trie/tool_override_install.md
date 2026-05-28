---
trie_version: 0.1.5
source: trie/tool_override_install.py
file_fingerprint: cf20a2f7b92f6a86f71b576ebacd67f79a073cd62eed7d433fb16b055a72c738
last_synced_at: '2026-05-28T14:27:17Z'
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
<!-- trie:section symbol=trie/tool_override_install:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=6b4ac288d16a333f4d9d4479d5fcfc8d4f416cf4515026f9efe7cf3d624b51d4 source_ref=658149b8ddacc94108782566ea27b58af04ee820 -->
## `trie/tool_override_install`

Replace an agent's built-in tools with trie wrappers by writing override files into the project root.

- `TARGETS`: registry of `ToolOverrideTarget` entries keyed by harness slug (`"opencode"`, `"claude-code"`, etc.)
- opencode: overrides `grep` and `read`, adds `trace` and 8 extended tools under `.opencode/tools/`
- claude-code: installs a `PreToolUse` advisory hook under `.claude/hooks/`; all other harnesses return `needs_manual_setup`
- `Action`: literal set of per-file outcomes — `"created"`, `"updated"`, `"skipped"`, `"preview"`, `"error"`, `"needs_manual_setup"`
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:Action fingerprint=6d5466b453e0912edae50fab1848c782530de9137450b5c33b3682dc80488f21 body_fp=6b65b8f074e125f4b5401efe85c4c999b76090020c367c758490d8a1465f3bae source_ref=658149b8ddacc94108782566ea27b58af04ee820 -->
## `Action = Literal["created", "updated", "skipped", "preview", "error", "needs_manual_setup"]`

Type alias for the outcome of a single file or target install operation.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:ToolOverrideInstallError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=41af9937735bcb59bbad70e486ac45768dace73d6176816e23ddb2df743e8763 source_ref=658149b8ddacc94108782566ea27b58af04ee820 -->
## `ToolOverrideInstallError`

Raised by `install` when target names are missing or unknown.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:FileToWrite fingerprint=d1463a335d153224df4e0fbe524be20b78d6d8091a383d10a9790a3b0e2a7bc7 body_fp=a4917e24f8abcbcc1b60bf31c502db2dcb06443285c59f2da9b0f1a7bf16c454 source_ref=658149b8ddacc94108782566ea27b58af04ee820 -->
## `FileToWrite(relative_path, render, description)`

Describe one file an override target needs written to disk.

- `relative_path`: path segments joined against the project root at write time.
- `render`: called with the project root to produce the file's text content.
- `description`: short human-readable label used in install reports.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:ToolOverrideApplyResult fingerprint=7cddfb44189be40c0f69532eed1cb7932f69fa3fd6d833f65a5666f956fb18e4 body_fp=b46703ce950e5dc79dd5bf21624227aa4efa3ac74612cf5339ef187559ebf85e source_ref=658149b8ddacc94108782566ea27b58af04ee820 -->
## `ToolOverrideApplyResult`

Immutable outcome of installing override files for one agent target.

- `action`: rolls up per-file results; precedence is `error` > `created`/`updated` > `skipped`.
- `files`: per-file breakdown for CLI reporting.
- `detail`: human-readable note, populated on `needs_manual_setup` or errors.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:ToolOverrideFileResult fingerprint=95c3d41b7de9da2d5f20aaa8a72438d7c4bcf3c67de66f8868b3e533a58b4243 body_fp=cb382c923ce2fe407d9e833e08b36d66e1323a708f716e2bcca45d7d8e9208e2 source_ref=658149b8ddacc94108782566ea27b58af04ee820 -->
## `ToolOverrideFileResult`

Per-file outcome inside a `ToolOverrideApplyResult.files` list.

- `action`: one of `"created"`, `"updated"`, `"skipped"`, `"preview"`, `"error"`, `"needs_manual_setup"`
- `path`: absolute path on disk; `None` when not yet resolved
- `detail`: human-readable elaboration, e.g. error message or preview contents
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:ToolOverrideTarget fingerprint=b964401eaed7403ce2d98e9a483745ee19a1868524d0784dc5a3f5dc20b794fc body_fp=35ea20bdc77dde28e3b68bbfd068b55dfd6bb2d12de86641eaa832bbdabd7d74 source_ref=658149b8ddacc94108782566ea27b58af04ee820 -->
## `ToolOverrideTarget`

Immutable descriptor for one agent's tool-override surface, consumed by `apply_one`.

- `files`: override files to write; empty means no automatable path → `needs_manual_setup`.
- `obsolete_files`: path tuples deleted on apply to clean up stale files from prior installs.
- `manual_instructions`: shown to the user when `files` is empty.
- `summary`: one-line consent prompt shown during `trie setup`.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_GENERATED_HEADER fingerprint=9dee807c69fc07fab72c6209e764e2323da49f8dcd319a9c54481dbecbb5889a body_fp=79ccf434b6fc0d443be86752b6ffe2730340b8800ae5220bd2f77f10e8ea1c45 source_ref=658149b8ddacc94108782566ea27b58af04ee820 -->
## `_GENERATED_HEADER`

TypeScript file header prepended to every generated `.opencode/tools/*.ts` override file.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_grep_override fingerprint=ae1bb9a2dfb2e20aa6ee58d36a1acc2044aada27b0475972e707f9af1f84c2ec body_fp=96a7a8061b16f277332aa117703cb6845106e0f33242897221d8b927ea4033b2 source_ref=658149b8ddacc94108782566ea27b58af04ee820 -->
## `_render_opencode_grep_override(_project_root: Path) -> str`

Render the `.opencode/tools/grep.ts` file that replaces opencode's built-in `grep` with a symbol-aware trie wrapper.

- Returns TypeScript source; filename collision causes opencode to prefer this tool over its built-in.
- `pattern` maps to `name_contains`; falls back to ripgrep over source bodies on no symbol match.
- `path` maps to `scope_prefix`; `include` is unsupported (scope is config-driven).
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_read_override fingerprint=ffe463adc332d1f0f88803fa18b58ae49c3b0e654de8c52d6130ffd38a1cfc29 body_fp=acf64de65b9b685677b305883d40709ac2d348503ea0c69b026b93914b09f3c4 source_ref=658149b8ddacc94108782566ea27b58af04ee820 -->
## `_render_opencode_read_override(_project_root: Path) -> str`

Render `.opencode/tools/read.ts`, a triefact-first override of opencode's built-in `read` tool.

- **qname path**: detects `path/to/file:Name` shape, shells out to `trie read <qname>`.
- **triefact path**: loads `triefacts/<stem>.md`; returns compact symbol manifest by default or agent-trimmed full prose when `full: true`.
- **source fallthrough**: used when `show_source: true`, `offset`/`limit` present, or no triefact exists.
- Emits `cli_call` telemetry events for in-process paths (qname path delegates emission to the `trie` subprocess).
- Non-default `triefacts.root` silently falls through to source.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_trace fingerprint=33f21409112cc93e5bd7b1ea55ec2806b431a24243d780acd9aa0425eb300959 body_fp=bd347a8ad1190d6da4f9c908c9adca864091c149602eaeb4f0538c017ab3a1ff source_ref=658149b8ddacc94108782566ea27b58af04ee820 -->
## `_render_opencode_trace(_project_root: Path) -> str`

Render `.opencode/tools/trace.ts`, a purely additive custom tool that exposes `trie trace` as a bare `trace` tool in opencode.

- No built-in collision; file basename `trace` is distinct from MCP-prefixed `trie_trace`.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_grep_str fingerprint=58319bb302d242e7793e07fbc486394d9929f9b77d2e5b4c7b67871c72313bbb body_fp=8b3ce12f3acab3a6f2135cda4ad1adb16b7012a85cff2fed986bde85eed3662e source_ref=658149b8ddacc94108782566ea27b58af04ee820 -->
## `_render_opencode_grep_str(_project_root: Path) -> str`

Render `.opencode/tools/grep_str.ts`, a tool that searches raw source bodies by regex and attributes matches to enclosing symbols.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_grep_entry_points fingerprint=c103f37b0731a78f4946f00df70aa0a7c59469865fa179bcc49b4f126a9be390 body_fp=4466d7fc62fb89093716b9667604179a0ceb7dd2c33a9501f911434b9c62a5ba source_ref=658149b8ddacc94108782566ea27b58af04ee820 -->
## `_render_opencode_grep_entry_points(_project_root: Path) -> str`

Render `.opencode/tools/grep_entry_points.ts`, a custom tool that shells out to `trie grep-entry-points` to find high-inbound public symbols matching a topic.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_grep_symbol fingerprint=5fe0f8a345b92f4e74ab8594f01138a2ca9465f62424c8cca778c6243f42bdcd body_fp=8669aafeb567229dca3f95a4375d7796ddce55fdd26b7bab96e3e1716a833e6d source_ref=658149b8ddacc94108782566ea27b58af04ee820 -->
## `_render_opencode_grep_symbol(_project_root: Path) -> str`

Render `.opencode/tools/grep_symbol.ts`, a fuzzy symbol-name lookup tool wrapping `trie grep-symbol`.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_grep_symbol_neighbours fingerprint=fd4dd9c1438e507552610e6b0b7208cd5eda44be46f6fe56f3ac96de1bda926b body_fp=27352294596417f6d940448b7d3bff1eeccf09b565394127205190df8912da97 source_ref=658149b8ddacc94108782566ea27b58af04ee820 -->
## `_render_opencode_grep_symbol_neighbours(_project_root: Path) -> str`

Render `.opencode/tools/grep_symbol_neighbours.ts`, which shells out to `trie grep-symbol-neighbours` for fuzzy symbol lookup plus immediate caller/callee metadata.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_explain_symbol fingerprint=3d74449df7ba7f3d9b5fa4b53a18b86d658841f1dd02f5df48c5b229f9eea361 body_fp=b74effcec2e1e175136030cac2aa18ad73c3bf37d390882d6ba678ed3325cbbd source_ref=658149b8ddacc94108782566ea27b58af04ee820 -->
## `_render_opencode_explain_symbol(_project_root: Path) -> str`

Render `.opencode/tools/explain_symbol.ts`, which shells out to `trie explain-symbol` for full symbol prose plus a caller/callee narrative.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_explain_symbol_refs fingerprint=ccf063b124b1693e10748b1ce8eab31574140cd313a5456a07f70effd3ac958d body_fp=e69ce797ef4cd16db4664b18132a04e217a92211268ebaef047c29b0c63c43ad source_ref=658149b8ddacc94108782566ea27b58af04ee820 -->
## `_render_opencode_explain_symbol_refs(_project_root: Path) -> str`

Render `.opencode/tools/explain_symbol_refs.ts`, a tool that shells out to `trie explain-symbol-refs` to narrate a symbol's callers.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_trace_flow fingerprint=27e2f63229308ef7da4fbbe00d2462f2457e8587819484054e13f589be0db140 body_fp=6ca89b9b72eb917ba7647ccb86aab7b75a40f2d60d98bc1f2832bfb75df3d918 source_ref=658149b8ddacc94108782566ea27b58af04ee820 -->
## `_render_opencode_trace_flow(_project_root: Path) -> str`

Render `.opencode/tools/trace_flow.ts`, a custom tool that finds shortest call chain(s) between two symbols via `trie trace-flow`.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_explain_flow fingerprint=60bc58f220fddf22d79fc3b0feb7c064f81546e80a928f6c04fd14cf7cbd70b0 body_fp=01f5f551fbab49246a34a297e08c3f91581e4ac0ec454600ce150843723ee14c source_ref=658149b8ddacc94108782566ea27b58af04ee820 -->
## `_render_opencode_explain_flow(_project_root: Path) -> str`

Render `.opencode/tools/explain_flow.ts`, an opencode custom tool that shells out to `trie explain-flow` to narrate the call chain between two symbols.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_patch fingerprint=7d3eeaa5500b89ea0b3f58626af2edecfd4e01b955c1dc949259babdde12784c body_fp=933613b24a5adc62f2121580fab979c51e77a9d5f8193512510194388f8b626c source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 -->
## `_render_opencode_patch(_project_root: Path) -> str`

Render `.opencode/tools/patch.ts`, a custom tool that posts an implementation note against a named symbol via `trie patch create`.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_patch_drop fingerprint=c5a387d3ccd119d17f820125b1767dcb772ecdab7406226b76fd4aad95c70acd body_fp=5f6597dd9d4535efe4052b3b33fec1f052769213bf6e33258f5aec399c2afbbf source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 -->
## `_render_opencode_patch_drop(_project_root: Path) -> str`

Render `.opencode/tools/patch_drop.ts`, which removes pending patches by qname or clears all.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_patch_list fingerprint=f5f3bac0e07e83cb60c4f3605da6a9b7dafb2e575ca1cf8a3c2cd0b8aeeb736b body_fp=55eb375ef31075c611be8ac30b744da9f611e2bd76e25bc05fbc7f213d53e6c7 source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 -->
## `_render_opencode_patch_list(_project_root: Path) -> str`

Render `.opencode/tools/patch_list.ts`, a custom tool that lists all pending patches grouped by symbol.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_opencode_patch_apply fingerprint=c1d3e2346fdc9369b2275316c79f709733b929a1107fac815ab6075c24603a5f body_fp=c5bb342fc643fc8b4f9d46eed1a4834fdc9850744ad108a3ac56f76dfb15afda source_ref=71f51dd9f7fe32391c5e0e222fcd7a56fe247388 -->
## `_render_opencode_patch_apply(_project_root: Path) -> str`

Render `.opencode/tools/patch_apply.ts`, a tool that runs `trie patch apply` to execute all pending patches.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_render_claude_code_hooks_json fingerprint=2b004e51b57a5be1e5d0181eb5239d9e0484ae53fc4b78e3acda4c59131e21ed body_fp=8f98a136fdaa84b7442e48d37b71a10905d9d3f89801c62c6dbf96e87044da5c source_ref=658149b8ddacc94108782566ea27b58af04ee820 -->
## `_render_claude_code_hooks_json(_project_root: Path) -> str`

Render `.claude/hooks/trie-tools.json`, a Claude Code `PreToolUse` advisory hook that nudges the model toward `mcp__trie__grep` when it invokes built-in `Grep`.

- Emits a `systemMessage` via `echo`; does not block the original `Grep` call.
- Only intercepts `Grep`; `Read` and `Glob` are left unhooked.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:TARGETS fingerprint=34ed053e3260f7d7d50751489108a97a3c33b6738a62034bd2797dbf3300480d body_fp=6ab5fd86bdbd648622596beb37697271f9ee237f36c5bfa6b2734af027d100f6 source_ref=cfb899e753d7c0d36aaf32452b674ea11e3097a3 -->
## `TARGETS: dict[str, ToolOverrideTarget]`

Registry mapping agent slug to its `ToolOverrideTarget` definition, keyed by the same names used in `mcp_install.TARGETS`.

- `"opencode"`: 15 files — overrides `grep`/`read`, adds `trace` plus 8 extended tools and 4 patch tools (`patch`, `patch_drop`, `patch_list`, `patch_apply`); obsoletes `trie_read.ts`/`trie_trace.ts`.
- `"claude-code"`: 1 file — advisory `PreToolUse` hook nudging toward `mcp__trie__grep`.
- All other entries: no files; `apply_one` returns `needs_manual_setup` with `manual_instructions`.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:ToolOverrideInstallPlan fingerprint=83ec1a61df42535b35c8b51fedbfbfc45086f0e5962ba7c40558117b34de29df body_fp=3c80948ef55ed294f84915374407ec7d6200aef7bce5e24a0755db639161b82f source_ref=658149b8ddacc94108782566ea27b58af04ee820 -->
## `ToolOverrideInstallPlan`

Aggregate result of a full `install` call across one or more targets.

- `results`: per-target `ToolOverrideApplyResult` instances, populated by `install`.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:install fingerprint=d1450ff3c792844aaa780cfdb60ec25d3403dafdee9b932957ea583841beaf10 body_fp=9f0e96f443a4b3af0ff9be3cbf6b45d938d415721d1465912fe0e77bbd37db7b source_ref=658149b8ddacc94108782566ea27b58af04ee820 -->
## `install(*, target_names: list[str] | None, print_only: bool, dry_run: bool, project_root: Path) -> ToolOverrideInstallPlan`

Apply tool-override files for each named target, returning a plan with per-target results.

- `target_names`: required; raises `ToolOverrideInstallError` if empty or contains unknown names.
- `print_only`: preview content without writing to disk.
- `dry_run`: report prospective changes without writing to disk.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:apply_one fingerprint=ba92586faae5c98a3f4a5228889bd4a297381515308bc99e0afaba467e97047f body_fp=c3f4ecc6033c1c6bcd66a871a721b066b072aed69d39b992a4d9eb007ef6ef2e source_ref=658149b8ddacc94108782566ea27b58af04ee820 -->
## `apply_one(target: ToolOverrideTarget, project_root: Path, print_only: bool, dry_run: bool, *, scope: Scope = "project") -> ToolOverrideApplyResult`

Install or preview every override file for a single `ToolOverrideTarget`, cleans up obsolete files, and returns an aggregated result.

- `scope`: accepted for API symmetry but unused; files always land under the project.
- Returns `needs_manual_setup` immediately when `target.files` is empty.
- Top-level `action` reflects highest-precedence per-file outcome: `error` > `created` > `updated` > `preview` > `skipped`.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_remove_obsolete fingerprint=2c10eaaf6621f765d84ecc5d05ce22304e2c4d73c09fd8511dafcf9069194641 body_fp=894c958656cb0aae13a9c49525570b5ff9a00fd6e631947a9700c294c2fc1c34 source_ref=658149b8ddacc94108782566ea27b58af04ee820 -->
## `_remove_obsolete(relative_path: tuple[str, ...], project_root: Path, print_only: bool, dry_run: bool) -> ToolOverrideFileResult`

Delete an obsolete override file left by a prior `trie setup` version, returning a per-file result.

- `relative_path`: path segments joined under `project_root` to locate the file.
- Returns `skipped` if absent, `preview` for dry-run/print-only, `updated` on successful deletion, `error` on `OSError`.
<!-- trie:end -->
<!-- trie:section symbol=trie/tool_override_install:_apply_file fingerprint=a55304ab263ea6f60e2d442ead639c43d89f3b54e65dda158b61cb687f3febf3 body_fp=568d3600221564fd90c15df41e4d0347fbbfe9897794d19ab9fa08f88a787b5c source_ref=658149b8ddacc94108782566ea27b58af04ee820 -->
## `_apply_file(spec: FileToWrite, project_root: Path, print_only: bool, dry_run: bool) -> ToolOverrideFileResult`

Materialise one override file with idempotency: skip if unchanged, overwrite if different, preview without writing if `print_only` or `dry_run`.
<!-- trie:end -->