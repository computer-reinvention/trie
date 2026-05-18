---
trie_version: 0.1.1
source: trie/tool_override_install.py
file_fingerprint: 5fefd857cd00895510189932de8df8c6539a951520ae6a70b9617ac9ee098965
last_synced_at: '2026-05-18T14:18:27Z'
description: 'Tool-override installation: replace an agent''s built-in tools with
  trie wrappers.'
defines:
- kind: class
  qualified_name: trie/tool_override_install:ToolOverrideInstallError
  lines: 41-42
- kind: class
  qualified_name: trie/tool_override_install:FileToWrite
  lines: 46-57
- kind: class
  qualified_name: trie/tool_override_install:ToolOverrideApplyResult
  lines: 61-74
- kind: class
  qualified_name: trie/tool_override_install:ToolOverrideFileResult
  lines: 78-85
- kind: class
  qualified_name: trie/tool_override_install:ToolOverrideTarget
  lines: 89-104
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_grep_override
  lines: 120-222
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_trie_read
  lines: 225-282
- kind: function
  qualified_name: trie/tool_override_install:_render_opencode_trie_trace
  lines: 285-350
- kind: function
  qualified_name: trie/tool_override_install:_render_claude_code_hooks_json
  lines: 358-414
- kind: class
  qualified_name: trie/tool_override_install:ToolOverrideInstallPlan
  lines: 527-533
- kind: function
  qualified_name: trie/tool_override_install:install
  lines: 536-575
- kind: function
  qualified_name: trie/tool_override_install:apply_one
  lines: 578-629
- kind: function
  qualified_name: trie/tool_override_install:_apply_file
  lines: 632-696
incoming_refs: 20
outgoing_refs: 0
---
<!-- trie:section symbol=trie/tool_override_install:ToolOverrideInstallError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=af02c768a0f5c0ca53ba008c51d793424e58fbb39a024793393d42518cd258dd source_ref=22af55fe3c92536b808294dbfad114aa433c76ee -->
## `ToolOverrideInstallError`

Raised when tool-override installation fails due to invalid input or configuration.
<!-- trie:end -->

<!-- trie:section symbol=trie/tool_override_install:FileToWrite fingerprint=f7c57b82436fde2c1d02d512b099998ef105eb27562833196a7acad6903a5b65 body_fp=59e422c89b6290d8070b194d823d394ce66109763885c4abab4e8abd4e46e43b source_ref=22af55fe3c92536b808294dbfad114aa433c76ee -->
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

<!-- trie:section symbol=trie/tool_override_install:ToolOverrideTarget fingerprint=f4feb904f003fafb2fd9adf58654fca5ff7a4a57b7fb5dd006f64c7d9341a4b0 body_fp=4e3d89ed5853f1b8bf6d09633f3cb282d5c04111b40969e85d6415bc21fc82ba source_ref=22af55fe3c92536b808294dbfad114aa433c76ee -->
## `ToolOverrideTarget`

Describe one agent's tool-override surface and the files needed to activate it.

- `files`: empty tuple means no automated path; `apply_one` returns `needs_manual_setup`.
- `manual_instructions`: shown to the user when `files` is empty.
- `summary`: one-line consent prompt shown before writing any files.
<!-- trie:end -->

<!-- trie:section symbol=trie/tool_override_install:_render_opencode_grep_override fingerprint=d4fe781eb2476743b45b91913cd2af575d6c596c783b14cb4838b22252517ad7 body_fp=f10f1a38d56df00d70428acde6e05742f0c3d7bbf574dc9ab035e38f6ba61c49 source_ref=22af55fe3c92536b808294dbfad114aa433c76ee -->
## `_render_opencode_grep_override(_project_root: Path) -> str`

Render the `.opencode/tools/grep.ts` file that replaces opencode's built-in `grep` with a trie-backed symbol search tool.
<!-- trie:end -->

<!-- trie:section symbol=trie/tool_override_install:_render_opencode_trie_read fingerprint=d37b70bf8b64d7960cf0536e262dc8692ee16e690ee700068fbf35cdd29ba8df body_fp=6fef1dc9e50477dc99e1b88297cbea75389950ef2ca060852bb82da97acdaad9 source_ref=22af55fe3c92536b808294dbfad114aa433c76ee -->
## `_render_opencode_trie_read(_project_root: Path) -> str`

Render `.opencode/tools/trie_read.ts`, adding a `trie_read` tool that looks up a symbol by qname without overriding the built-in `read`.
<!-- trie:end -->

<!-- trie:section symbol=trie/tool_override_install:_render_opencode_trie_trace fingerprint=537940b2a83e32c563b3263704f8fe98cb28be21ba268625e929926f7b789762 body_fp=900b76cc9fbdd0f0af2903b8b6a3260db104fe173331813ff3daab255d7d6d62 source_ref=22af55fe3c92536b808294dbfad114aa433c76ee -->
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

<!-- trie:section symbol=trie/tool_override_install:apply_one fingerprint=118729e955cec82c8b85f59fb3f259c880349b005b459d8eb99a7297c0037cb7 body_fp=45efa2494f0b2cb8dc7b3002a9a8409b59f2619c60d02d39e37f3641395b160f source_ref=22af55fe3c92536b808294dbfad114aa433c76ee -->
## `apply_one(target: ToolOverrideTarget, project_root: Path, print_only: bool, dry_run: bool, *, scope: Scope = "project") -> ToolOverrideApplyResult`

Install or preview every override file for one `ToolOverrideTarget`, returning a per-file and aggregate result.

- `scope`: accepted for API symmetry; currently unused.
- Returns `needs_manual_setup` immediately if `target.files` is empty.
- Top-level `action` summarises file results by precedence: `error` > `created` > `updated` > `preview` > `skipped`.
<!-- trie:end -->

<!-- trie:section symbol=trie/tool_override_install:_apply_file fingerprint=a55304ab263ea6f60e2d442ead639c43d89f3b54e65dda158b61cb687f3febf3 body_fp=7fada6f6e3c8f7958eae3b3a33a4e89c55e80ca45e9ef83dbb20be3d8b6a0283 source_ref=22af55fe3c92536b808294dbfad114aa433c76ee -->
## `_apply_file(spec: FileToWrite, project_root: Path, print_only: bool, dry_run: bool) -> ToolOverrideFileResult`

Materialise one override file on disk with idempotency, dry-run, and print-only guards.

- `spec` — provides the target path segments, renderer, and description.
- Returns `skipped` if file exists with identical contents; `preview` if `print_only` or `dry_run`; `error` on unreadable existing file; else `created` or `updated`.
<!-- trie:end -->