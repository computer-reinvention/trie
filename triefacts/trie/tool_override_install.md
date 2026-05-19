---
trie_version: 0.1.1
source: trie/tool_override_install.py
file_fingerprint: be574b484bf3e3264a150a9a224b25a025f66642e2db6e4b1f0cfda690dc7e8a
last_synced_at: '2026-05-19T15:19:42Z'
description: 'Tool-override installation: replace an agent''s built-in tools with
  trie wrappers.'
defines:
- kind: module
  qualified_name: trie/tool_override_install:__module__
  lines: 1-1462
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
  qualified_name: trie/tool_override_install:_render_opencode_trie_trace
  lines: 974-1042
- kind: function
  qualified_name: trie/tool_override_install:_render_claude_code_hooks_json
  lines: 1050-1106
- kind: constant
  qualified_name: trie/tool_override_install:TARGETS
  lines: 1115-1221
- kind: class
  qualified_name: trie/tool_override_install:ToolOverrideInstallPlan
  lines: 1230-1236
- kind: function
  qualified_name: trie/tool_override_install:install
  lines: 1239-1278
- kind: function
  qualified_name: trie/tool_override_install:apply_one
  lines: 1281-1338
- kind: function
  qualified_name: trie/tool_override_install:_remove_obsolete
  lines: 1341-1394
- kind: function
  qualified_name: trie/tool_override_install:_apply_file
  lines: 1397-1461
incoming_refs: 31
outgoing_refs: 0
---
<!-- trie:section symbol=trie/tool_override_install:ToolOverrideInstallError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=af02c768a0f5c0ca53ba008c51d793424e58fbb39a024793393d42518cd258dd source_ref=22af55fe3c92536b808294dbfad114aa433c76ee -->
## `ToolOverrideInstallError`

Raised when tool-override installation fails due to invalid input or configuration.
<!-- trie:end -->

<!-- trie:section symbol=trie/tool_override_install:FileToWrite fingerprint=383a49688caede199d9b7e9b5c07440b2af24a2a5077a4866f0b1560b845b1da body_fp=59e422c89b6290d8070b194d823d394ce66109763885c4abab4e8abd4e46e43b source_ref=cd49f981cf93dad430cf7f0808a344171fe6573a -->
## `FileToWrite`

Describe one file an override target must write to disk, with its render function and human-readable label.

- `relative_path`: tuple of path segments joined at write time
- `render`: called with `project_root`; returns the file's full text content
<!-- trie:end -->

<!-- trie:section symbol=trie/tool_override_install:ToolOverrideApplyResult fingerprint=7cddfb44189be40c0f69532eed1cb7932f69fa3fd6d833f65a5666f956fb18e4 body_fp=d44db69f394daa7095a6a8d0a196a58fa4acc23e31a10be91bb04e95ae9b9098 source_ref=22af55fe3c92536b808294dbfad114aa433c76ee -->
## `ToolOverrideApplyResult`

Holds the outcome of installing all override files for one target.

- `action`: summarises across files — `"error"` if any errored, `"skipped"` if all skipped, else highest-energy change.
- `files`: per-file results for CLI reporting.
- `detail`: populated on `"error"` or `"needs_manual_setup"` outcomes.
<!-- trie:end -->

<!-- trie:section symbol=trie/tool_override_install:ToolOverrideFileResult fingerprint=95c3d41b7de9da2d5f20aaa8a72438d7c4bcf3c67de66f8868b3e533a58b4243 body_fp=096cd8aad342052cc7c2cef27735c85b6ea3defc7d8fe042e1953eb1edbcb2d1 source_ref=22af55fe3c92536b808294dbfad114aa433c76ee -->
## `ToolOverrideFileResult`

Per-file outcome inside a `ToolOverrideApplyResult.files` list.

- `action`: one of `created`, `updated`, `skipped`, `preview`, `error`, `needs_manual_setup`
- `path`: resolved `Path` on disk, or `None` if unavailable
- `detail`: error message, preview contents, or skip reason
<!-- trie:end -->

<!-- trie:section symbol=trie/tool_override_install:ToolOverrideTarget fingerprint=b964401eaed7403ce2d98e9a483745ee19a1868524d0784dc5a3f5dc20b794fc body_fp=4583e9304b6a6b94b4db57f43b79147f475a6e7ddfe543b48d873b97a194fe55 source_ref=cd49f981cf93dad430cf7f0808a344171fe6573a -->
## `ToolOverrideTarget`

Describe one agent's tool-override surface and the files needed to activate it.

- `files`: empty tuple means no automated path; `apply_one` returns `needs_manual_setup`.
- `obsolete_files`: paths deleted on apply if present; missing files are silently skipped.
- `manual_instructions`: shown to the user when `files` is empty.
- `summary`: one-line consent prompt shown before writing any files.
<!-- trie:end -->

<!-- trie:section symbol=trie/tool_override_install:_render_opencode_grep_override fingerprint=d4fe781eb2476743b45b91913cd2af575d6c596c783b14cb4838b22252517ad7 body_fp=f10f1a38d56df00d70428acde6e05742f0c3d7bbf574dc9ab035e38f6ba61c49 source_ref=22af55fe3c92536b808294dbfad114aa433c76ee -->
## `_render_opencode_grep_override(_project_root: Path) -> str`

Render the `.opencode/tools/grep.ts` file that replaces opencode's built-in `grep` with a trie-backed symbol search tool.
<!-- trie:end -->



<!-- trie:section symbol=trie/tool_override_install:_render_opencode_trie_trace fingerprint=3bc12307a5afa6daeb4daab60835363783b9d4fc1fa7de70dd3e60b306bb21df body_fp=900b76cc9fbdd0f0af2903b8b6a3260db104fe173331813ff3daab255d7d6d62 source_ref=cd49f981cf93dad430cf7f0808a344171fe6573a -->
## `_render_opencode_trie_trace(_project_root: Path) -> str`

Render `.opencode/tools/trie_trace.ts`, adding `trie_trace` as a new agent tool for call-graph traversal.
<!-- trie:end -->

<!-- trie:section symbol=trie/tool_override_install:_render_claude_code_hooks_json fingerprint=2b004e51b57a5be1e5d0181eb5239d9e0484ae53fc4b78e3acda4c59131e21ed body_fp=2c2db52cd3cddb7e36276c6e9e96b47c06e2ffff1818d6dffe1d05f4176562ed source_ref=22af55fe3c92536b808294dbfad114aa433c76ee -->
## `_render_claude_code_hooks_json(_project_root: Path) -> str`

Render `.claude/hooks/trie-tools.json`, a `PreToolUse` advisory hook that nudges Claude toward `mcp__trie__grep` when it reaches for built-in `Grep`.

- Does not block the built-in call; emits a `systemMessage` only.
- Output is a JSON string with a trailing newline.
<!-- trie:end -->

<!-- trie:section symbol=trie/tool_override_install:ToolOverrideInstallPlan fingerprint=83ec1a61df42535b35c8b51fedbfbfc45086f0e5962ba7c40558117b34de29df body_fp=2dc2be28cbeaeb67793f4a6fd0e29bc3f45a0607effdb4951babad3ce1ec6862 source_ref=22af55fe3c92536b808294dbfad114aa433c76ee -->
## `ToolOverrideInstallPlan`

Aggregate result of a full `install` call across one or more targets.
<!-- trie:end -->

<!-- trie:section symbol=trie/tool_override_install:install fingerprint=d1450ff3c792844aaa780cfdb60ec25d3403dafdee9b932957ea583841beaf10 body_fp=23720cff65117d87bf3627951850ba81fbb5754821a946a49ae741f61ca34f2b source_ref=22af55fe3c92536b808294dbfad114aa433c76ee -->
## `install(*, target_names: list[str] | None, print_only: bool, dry_run: bool, project_root: Path) -> ToolOverrideInstallPlan`

Apply tool-override files for one or more explicitly named targets, raising `ToolOverrideInstallError` on unknown names or empty input.

- `target_names`: required; no implicit "all targets" expansion.
- `print_only`: renders content without writing; results carry `"preview"` action.
- `dry_run`: checks disk state without writing; results carry `"preview"` action.
<!-- trie:end -->

<!-- trie:section symbol=trie/tool_override_install:apply_one fingerprint=ba92586faae5c98a3f4a5228889bd4a297381515308bc99e0afaba467e97047f body_fp=89da4427ac742c3537afdcf56ca20d69844309df3338e622642d69ce3d5be52e source_ref=cd49f981cf93dad430cf7f0808a344171fe6573a -->
## `apply_one(target: ToolOverrideTarget, project_root: Path, print_only: bool, dry_run: bool, *, scope: Scope = "project") -> ToolOverrideApplyResult`

Install or preview every override file for one `ToolOverrideTarget`, returning a per-file and aggregate result.

- `scope`: accepted for API symmetry; currently unused.
- Returns `needs_manual_setup` immediately if `target.files` is empty.
- After writing new files, removes any paths listed in `target.obsolete_files` via `_remove_obsolete`.
- Top-level `action` summarises file results by precedence: `error` > `created` > `updated` > `preview` > `skipped`.
<!-- trie:end -->

<!-- trie:section symbol=trie/tool_override_install:_apply_file fingerprint=a55304ab263ea6f60e2d442ead639c43d89f3b54e65dda158b61cb687f3febf3 body_fp=7fada6f6e3c8f7958eae3b3a33a4e89c55e80ca45e9ef83dbb20be3d8b6a0283 source_ref=22af55fe3c92536b808294dbfad114aa433c76ee -->
## `_apply_file(spec: FileToWrite, project_root: Path, print_only: bool, dry_run: bool) -> ToolOverrideFileResult`

Materialise one override file on disk with idempotency, dry-run, and print-only guards.

- `spec` — provides the target path segments, renderer, and description.
- Returns `skipped` if file exists with identical contents; `preview` if `print_only` or `dry_run`; `error` on unreadable existing file; else `created` or `updated`.
<!-- trie:end -->

<!-- trie:section symbol=trie/tool_override_install:Action fingerprint=6d5466b453e0912edae50fab1848c782530de9137450b5c33b3682dc80488f21 body_fp=1922a7ee9f5f29f8c2eb06478d570b909133433d28dcbb8483bb6c97f7fead58 source_ref=cd49f981cf93dad430cf7f0808a344171fe6573a -->
## `Action = Literal["created", "updated", "skipped", "preview", "error", "needs_manual_setup"]`

Type alias for the set of possible per-file or per-target outcome verbs.
<!-- trie:end -->

<!-- trie:section symbol=trie/tool_override_install:_GENERATED_HEADER fingerprint=9dee807c69fc07fab72c6209e764e2323da49f8dcd319a9c54481dbecbb5889a body_fp=39fce4cf2c89ea6ffd1f3a2caf602eff1d020d9c2f55cb6f9628b3dc5fac9c3d source_ref=cd49f981cf93dad430cf7f0808a344171fe6573a -->
## `_GENERATED_HEADER`

Top-of-file comment block prepended to every generated `.ts` override file.
<!-- trie:end -->

<!-- trie:section symbol=trie/tool_override_install:_render_opencode_read_override fingerprint=3e4371bc634714174d7e76b9f94e76c2f5f015b3db4ac0f661f3ec3cb3d12b5f body_fp=4ec7a7bc485ebe5c1ac9089cb2d86a4a1ab83e88c64fc1d39267aa2dd612f8e7 source_ref=429ffd0e344f00bc83056230f6ecab0384be6390 -->
## `_render_opencode_read_override(_project_root: Path) -> str`

Render `.opencode/tools/read.ts`, dispatching on argument shape across four paths: qname → `trie read --json`, file path with triefact → compact view (default) or agent-trimmed full view (`full: true`), otherwise raw source bytes.

- **qname**: string containing `:` (not a URL scheme or Windows drive) routes to `trie read`
- **triefact compact** (default): renders symbol manifest with signatures and first-paragraph intros via `renderCompact`
- **triefact full** (`full: true`): strips internal frontmatter keys and section sentinels via `renderForAgent`, keeping only agent-facing keys and section bodies
- **show_source / offset / limit**: force raw file read via `readSourceFile`; absolute paths resolved verbatim, relative paths under cwd
- Accepts a `full` arg in telemetry capture; emits `cli_call` telemetry for in-process paths; skips emission on qname path to avoid double-counting with the subprocess
- `readTriefact` now handles absolute paths by stripping the cwd prefix before triefact lookup; returns `null` for paths outside the project tree
<!-- trie:end -->

<!-- trie:section symbol=trie/tool_override_install:TARGETS fingerprint=1ce974ad6b0934f36a67e1d9fec6f544b144d44c35f10f05e07f8f9b35a996dd body_fp=e10c52965d036e6bbb07bc6a857374249ea8e7aadf30e1f7f5aa371d03ea078f source_ref=cd49f981cf93dad430cf7f0808a344171fe6573a -->
## `TARGETS: dict[str, ToolOverrideTarget]`

Registry mapping target slug to its `ToolOverrideTarget` descriptor for all known agent harnesses.

- Keys must match slugs in `trie.mcp_install.TARGETS`; `install()` validates against this dict.
- Targets without an automatable override path (`claude-desktop`, `cursor`, `windsurf`, `vscode`, `codex`) have empty `files` and carry `manual_instructions` instead.
- `opencode` entry includes `obsolete_files` to drop `trie_read.ts` from prior installs.
<!-- trie:end -->

<!-- trie:section symbol=trie/tool_override_install:_remove_obsolete fingerprint=2c10eaaf6621f765d84ecc5d05ce22304e2c4d73c09fd8511dafcf9069194641 body_fp=b1adad5ee10a4acd0c89c2df84eae7af3f30604a3103748e51f6a29cb0281d93 source_ref=cd49f981cf93dad430cf7f0808a344171fe6573a -->
## `_remove_obsolete(relative_path: tuple[str, ...], project_root: Path, print_only: bool, dry_run: bool) -> ToolOverrideFileResult`

Delete an obsolete override file left by a prior `trie setup` version, or report skipped/preview if absent or in dry-run mode.

- `relative_path`: path segments joined against `project_root` to locate the file.
- Returns `action="updated"` when the file is removed, `"skipped"` when absent, `"preview"` in dry-run/print-only mode, `"error"` on `OSError`.
<!-- trie:end -->

<!-- trie:section symbol=trie/tool_override_install:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=99a1027719819282265fdafac8cb3b41fd3034267f97bcb9569e4c12eb697681 source_ref=cd49f981cf93dad430cf7f0808a344171fe6573a -->
## `tool_override_install`

Replace an agent's built-in tools with trie wrappers, making trie the default search and read path.

- `TARGETS`: registry of `ToolOverrideTarget` entries keyed by harness slug (`opencode`, `claude-code`, etc.)
- opencode: overrides `grep` and `read`, adds `trie_trace` via `.opencode/tools/*.ts`
- claude-code: installs a `PreToolUse` advisory hook nudging toward `mcp__trie__grep`
- other harnesses: return `needs_manual_setup` with human-readable instructions
<!-- trie:end -->