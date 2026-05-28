---
trie_version: 0.1.5
source: tests/test_tool_override_install.py
file_fingerprint: 70443976502e772d6583cdcb2efc6b6b18b2bdec426c108020010d44ad3f3536
last_synced_at: '2026-05-28T14:28:04Z'
description: 'Tests for `trie.tool_override_install`: replacing agent built-in tools
  with trie wrappers.'
defines:
- kind: module
  qualified_name: tests/test_tool_override_install:__module__
  lines: 1-687
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_install_creates_override_files
  lines: 39-74
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_grep_override_routes_to_trie_grep
  lines: 77-92
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_files_carry_generated_notice
  lines: 95-108
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_rendered_files_have_balanced_backticks_per_line
  lines: 111-144
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_dispatches_on_qname_path_or_show_source
  lines: 152-174
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_advertises_show_source_arg
  lines: 177-190
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_qname_detection_excludes_urls_and_drives
  lines: 193-211
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_emits_telemetry_from_typescript
  lines: 214-244
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_appends_telemetry_atomically
  lines: 247-264
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_handles_absolute_paths
  lines: 267-288
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_advertises_full_arg
  lines: 291-307
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_emits_compact_renderer
  lines: 310-329
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_full_mode_trims_for_agent
  lines: 332-354
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_trie_read_obsolete_file_removed_on_apply
  lines: 357-382
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_trie_trace_obsolete_file_removed_on_apply
  lines: 385-408
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_obsolete_cleanup_is_noop_on_fresh_install
  lines: 411-426
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_install_is_idempotent_on_identical_content
  lines: 434-459
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_install_updates_on_drift
  lines: 462-487
- kind: function
  qualified_name: tests/test_tool_override_install:test_claude_code_install_creates_advisory_hook
  lines: 495-522
- kind: function
  qualified_name: tests/test_tool_override_install:test_claude_code_hook_does_not_deny_grep
  lines: 525-539
- kind: function
  qualified_name: tests/test_tool_override_install:test_unsupported_harnesses_emit_needs_manual_setup
  lines: 551-569
- kind: function
  qualified_name: tests/test_tool_override_install:test_install_for_opencode_and_claude_code_in_one_pass
  lines: 577-590
- kind: function
  qualified_name: tests/test_tool_override_install:test_print_only_does_not_write_anything
  lines: 598-619
- kind: function
  qualified_name: tests/test_tool_override_install:test_dry_run_does_not_write_when_file_already_correct
  lines: 622-642
- kind: function
  qualified_name: tests/test_tool_override_install:test_install_with_empty_target_names_raises
  lines: 650-657
- kind: function
  qualified_name: tests/test_tool_override_install:test_install_with_unknown_target_raises
  lines: 660-674
- kind: function
  qualified_name: tests/test_tool_override_install:test_apply_one_uses_needs_manual_setup_for_targets_with_no_files
  lines: 677-686
incoming_refs: 0
outgoing_refs: 30
---
<!-- trie:section symbol=tests/test_tool_override_install:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=33e2cc955db5a24024a56aee2aa95bb65c5644ebe23624a33ef974bb94a0142f source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 -->
## `tests/test_tool_override_install`

Integration tests for `trie.tool_override_install`, covering file generation, idempotency, dry-run safety, and error handling across all registered agent harnesses.

- `opencode`: verifies three override files plus eight extended tools are written under `.opencode/tools/`
- `claude-code`: verifies one advisory `PreToolUse` hook file is written under `.claude/hooks/`
- Other harnesses: verifies `needs_manual_setup` is returned with no files written
- Idempotency: second run returns `skipped`; drifted content returns `updated`
- `print_only` / `dry_run`: assert no disk writes occur
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_install_creates_override_files fingerprint=a76f5ca0678b5f670b5e59832755d9e6d80531e6d259acbd2b2596c1bc5c98e6 body_fp=09a4777afd8a0f5726027db35516856cb9ad20774875a0daafc6f0d15b80b4a6 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 -->
## `test_opencode_install_creates_override_files(tmp_path: Path)`

Assert that a single `install` pass for `opencode` creates all 11 expected `.ts` files under `.opencode/tools/` on disk.

- Verifies 3 original tools: `grep.ts`, `read.ts`, `trace.ts`.
- Verifies 8 extended tools: `grep_str`, `grep_entry_points`, `grep_symbol`, `grep_symbol_neighbours`, `explain_symbol`, `explain_symbol_refs`, `trace_flow`, `explain_flow`.
- Checks `result.action == "created"` and each path physically exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_grep_override_routes_to_trie_grep fingerprint=bbea07bffaf1433c02906416587d0a3e71ec2c83fa56a0b8271f44f15358bcad body_fp=87715fd91ee4a037a78f9a47986434a2d814a1a5092ab98941460af288cf8b63 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 -->
## `test_opencode_grep_override_routes_to_trie_grep(tmp_path: Path)`

Assert that the rendered `grep.ts` spawns `trie grep` via `Bun.spawn` and omits `--json`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_files_carry_generated_notice fingerprint=931d1963484293165d869cff6a475b7e1d05914d8997dda1eaf105ae35b037c2 body_fp=1b5c93f6b0a29bc1370013030c55d96f8c86a54bda3b0a2152e3f726bb118a5e source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 -->
## `test_opencode_files_carry_generated_notice(tmp_path: Path)`

Assert that every opencode override file contains the "Auto-generated by `trie setup`" and "Do not hand-edit" header strings.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_rendered_files_have_balanced_backticks_per_line fingerprint=c22887ae666f1fc4d321d98ed8f41a4dfc374393f6e4860b7221b77820fca28c body_fp=ac18cc1880d9732f3796c8cefa417027b92c2bdb2d05b637b387ed50175df4e5 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 -->
## `test_opencode_rendered_files_have_balanced_backticks_per_line(tmp_path: Path)`

Assert that every `//` comment line in each rendered `.ts` file has an even backtick count, preventing stray JS template literals from breaking bun's parser.

- Guards against Python-side `\n` expansion splitting a single-line comment across two lines.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_dispatches_on_qname_path_or_show_source fingerprint=5384e61804c60a7be83e0410d6ad2d4ddc1952c652578811a894ea1bb18859e4 body_fp=bc118228affa7411e056a538e4767ddd0428b5191afc615ad7d95f74c520b47d source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 -->
## `test_opencode_read_override_dispatches_on_qname_path_or_show_source(tmp_path: Path)`

Assert that the rendered `read.ts` contains dispatch markers for all three modes: qname→`trie read`, path→triefact lookup, and `show_source`→raw source.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_advertises_show_source_arg fingerprint=d377a5b4a375cac89dd0bf1a263a6901952e353291915687374f1447324c8283 body_fp=569e40f909bea4923415a1153a4e39c66c8175a8a09b7d27bdf9ed3e73693101 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 -->
## `test_opencode_read_override_advertises_show_source_arg(tmp_path: Path)`

Assert that `read.ts`'s args schema exposes `show_source`, `offset`, and `limit` escape-hatch parameters.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_qname_detection_excludes_urls_and_drives fingerprint=a31e56fc088c1052530734293a7a78524443e45fac5d3e70153bda3a342a1916 body_fp=f7c47cbeadf11e9d0156ff9ae739f342ee0be6c3244e00912ff14317a91b45a0 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 -->
## `test_opencode_read_override_qname_detection_excludes_urls_and_drives(tmp_path: Path)`

Assert that `read.ts`'s `looksLikeQname` helper explicitly excludes URL schemes (`://`) and Windows drive prefixes (`[A-Za-z]:`).
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_emits_telemetry_from_typescript fingerprint=7f8c4fed8e631923f71efea317df78da8411d4c17e61bd0e528cb429666e563b body_fp=667222a8df3d84e0e48c3a56e8a99824faf6a4e61737b4e5a9fe6802eda1d078 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 -->
## `test_opencode_read_override_emits_telemetry_from_typescript(tmp_path: Path)`

Assert that the rendered `read.ts` embeds TypeScript-side telemetry helpers for the three in-process dispatch paths invisible to Python.

- Checks for `emitTelemetry`, `resolveTelemetryConfig`, `extractTomlSection` function names.
- Verifies `"cli_call"` event name, `"read"` tool name, `mode` field, and `TRIE_DEBUG` env var handling.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_appends_telemetry_atomically fingerprint=4392ac7d6c58ee986401da04b6a844b5e514681cd33a94fed47d3360195fa4f2 body_fp=81e7ca3e16f1b842faf5858fc166c74381da1e5d105944935fda55a1aecbc600 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 -->
## `test_opencode_read_override_appends_telemetry_atomically(tmp_path: Path)`

Assert that `read.ts` uses `appendFile` for telemetry writes, not read-modify-write, preventing log-file races under concurrent opencode sessions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_handles_absolute_paths fingerprint=331fc83490b3d1f8cf59065f4c0128e7d3321e595ed45c4912a282848cf2c585 body_fp=87b30f8ab5dd84e4ba825018870a429f91cff8ecd9bf14859368f27d1f5f20e3 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 -->
## `test_opencode_read_override_handles_absolute_paths(tmp_path: Path)`

Assert that the rendered `read.ts` wrapper uses `isAbsolute(path)` to skip joining absolute paths onto `cwd`, preventing ENOENT on agent-supplied absolute paths.

- Checks `resolveAbsolutePath` helper exists and branches correctly.
- Checks `projectRelativePath` strips `cwd` prefix for triefact lookup on absolute paths.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_advertises_full_arg fingerprint=005cdc6c3d94967f1d1afa9f90580144130596b3eae9e920da25a090a43812dd body_fp=3cc8f138bdabdeac755fd2574cf995f6cf8f1fec24fa9b3cb1b732cbe18a0a77 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 -->
## `test_opencode_read_override_advertises_full_arg(tmp_path: Path)`

Assert that the rendered `read.ts` schema exposes a `full` argument and mentions compact mode in its description.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_emits_compact_renderer fingerprint=5695f91271e789440ef43b5a770758ef6502837591c372a78ebe8aa3c93de99a body_fp=ed25177e4b651776c74952efb394ee958cb3acf116aefc906c9ea8924a83fcc6 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 -->
## `test_opencode_read_override_emits_compact_renderer(tmp_path: Path)`

Assert that the rendered `read.ts` contains `renderCompact`, `parseFrontMatter`, `extractSections`, and both telemetry mode tags `triefact_compact` and `triefact_full`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_full_mode_trims_for_agent fingerprint=d16eec00436dccc69af73d191648d1d6ccfaa708532d5301f331e513bd01bf08 body_fp=1a04619af02628484d2b2adbf39605cc09d5ed2be95789726c3f933da201db5e source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 -->
## `test_opencode_read_override_full_mode_trims_for_agent(tmp_path: Path)`

Assert that `read.ts` full-mode routes through `renderForAgent` instead of returning raw triefact bytes.

- Checks `renderForAgent`, `stripSentinels`, and `renderFrontMatterForAgent` helpers are present in rendered TS.
- Verifies full mode invokes `renderForAgent(triefact)` and does not leak the raw `triefact` string directly.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_trie_read_obsolete_file_removed_on_apply fingerprint=9b1d5f8b5a30c80327e621908e7e53850a244638429671af0c96104d234129fb body_fp=95f837db7cdbecbb68771d3443e5eef7050100ea040c98c078daab43f03b97ed source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 -->
## `test_opencode_trie_read_obsolete_file_removed_on_apply(tmp_path: Path)`

Assert that `install` deletes the legacy `.opencode/tools/trie_read.ts` file and records the cleanup in the plan.

- `cleanup_results[0].action`: must be `"updated"` to signal a migration, not a fresh write.
- `cleanup_results[0].description`: must contain `"removed obsolete"` so the user sees what changed.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_trie_trace_obsolete_file_removed_on_apply fingerprint=1e6177df323fce1c409ce9b59f17140642922fad4f84cf0e0083388b293e4581 body_fp=ab9cf73ce41d8dc689cba2d199cd5b94403f888fde03f9031aaba19243767e08 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 -->
## `test_opencode_trie_trace_obsolete_file_removed_on_apply(tmp_path: Path)`

Assert that `install` deletes the stale `.opencode/tools/trie_trace.ts` file and records an `updated`/`"removed obsolete"` result.

- Pre-creates `trie_trace.ts` to simulate a prior install with the old prefixed filename.
- Verifies the file is gone on disk and the plan contains exactly one cleanup entry.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_obsolete_cleanup_is_noop_on_fresh_install fingerprint=04ec87c8983682f3c5d287e359bb0d00e26fb2b3059928626ca6aa13c0d16dd4 body_fp=3b4b104a317494169a5430df08d6fd2d8a371dada4647ec1aa4f67ac5d754eaa source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 -->
## `test_opencode_obsolete_cleanup_is_noop_on_fresh_install(tmp_path: Path)`

Assert that obsolete-file cleanup on a clean project reports `skipped` with "nothing to clean up" detail rather than erroring on absent files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_install_is_idempotent_on_identical_content fingerprint=87fc921b24fd75af74ee18291121a61336a1480d8b0b133629f017c95411a5fd body_fp=32025af6d3b96481288ba71313e7beea18f088c3ebce0e846afa5225b3464ee1 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 -->
## `test_opencode_install_is_idempotent_on_identical_content(tmp_path: Path)`

Assert that a second `install` call for `opencode` with unchanged files reports `skipped` for every file result.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_install_updates_on_drift fingerprint=1598b027eb6c27bf0e21de5bea19063974caf4a976a86c98938412a210e0b5a3 body_fp=0dd776f96929eed6ad5a128150d26ce21b37927faffca77dbf536608524731b0 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 -->
## `test_opencode_install_updates_on_drift(tmp_path: Path)`

Verify that a second `install` overwrites a hand-edited or stale `grep.ts` and restores trie-generated content.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_claude_code_install_creates_advisory_hook fingerprint=001f1ffd25598478bcd3b656b515e9b5491e5d2c8d41899e6ddbad20f3a76c36 body_fp=ba67e5bae763f7c2ef5eb54f9b54897883aeb9c7b24a293c2877d059e3c52ce3 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 -->
## `test_claude_code_install_creates_advisory_hook(tmp_path: Path)`

Assert that `install` for `claude-code` writes a valid `PreToolUse` hook JSON file at `.claude/hooks/trie-tools.json` that matches `Grep` and emits a `systemMessage` referencing `mcp__trie__grep`.

- Verifies `result.action == "created"` and file exists on disk.
- Checks hook schema: `hooks.PreToolUse[0].matcher == "Grep"`.
- Checks handler command contains both `systemMessage` and `mcp__trie__grep`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_claude_code_hook_does_not_deny_grep fingerprint=b0917350ef7add9adf24564bb8f967df64c94de5affe02776d3be2f57ce39bcf body_fp=fb9543d469e761cdf9024fc17c4fb22185b2add3bbfbd72150576ed192f8fd8e source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 -->
## `test_claude_code_hook_does_not_deny_grep(tmp_path: Path)`

Assert that the Claude Code hook file contains no `permissionDecision: deny` rule, keeping the hook advisory-only.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_unsupported_harnesses_emit_needs_manual_setup fingerprint=252d564de8cef912137183a246a83c8734777cfbd60c0a79917aab425762c512 body_fp=de62af315a0925fa32ce3ab6fb413b8ace199935e6b179c14061df56cc333409 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 -->
## `test_unsupported_harnesses_emit_needs_manual_setup(tmp_path: Path, slug: str)`

Assert that each unsupported harness returns `needs_manual_setup` with instructions and writes no files.

- `slug`: parametrized over `claude-desktop`, `cursor`, `windsurf`, `vscode`, `codex`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_install_for_opencode_and_claude_code_in_one_pass fingerprint=e5a91b31de3c5d2716c71642ee28352e70962a865fe3310f85e696ab6d40c562 body_fp=6fee43a1300bbf4aeb6e23fd45a4e98e262a2be07a17555ec1fd9404704be9c4 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 -->
## `test_install_for_opencode_and_claude_code_in_one_pass(tmp_path: Path)`

Assert that a single `install` call with both targets writes all files for opencode and Claude Code independently in one pass.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_print_only_does_not_write_anything fingerprint=195068d913203efa2f7a33563f5b2d88d92ce6ddea2f47b5768362fab4701a4b body_fp=b8614fec4f43b9ffa6c49ae4443bac2088508221c76057a3c6fed2981497cfab source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 -->
## `test_print_only_does_not_write_anything(tmp_path: Path)`

Assert that `install` with `print_only=True` writes nothing to disk and returns `preview` results with rendered contents in `detail`.

- Non-obsolete file results: `action == "preview"` with `detail` populated.
- Obsolete-cleanup results for absent files: `action == "skipped"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_dry_run_does_not_write_when_file_already_correct fingerprint=97dd083d6cfe5d0fce2cf74184a64b3a1581bdb594a76cf69b3fe2c183f8370c body_fp=e2b9c3694231a3a2cf0c0b1b9e0c0358036bcb181c0f036ccfa705fe444dd3a1 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 -->
## `test_dry_run_does_not_write_when_file_already_correct(tmp_path: Path)`

Verify that `--dry-run` reports `skipped` when on-disk content already matches the would-be output, writing nothing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_install_with_empty_target_names_raises fingerprint=de0258da2c32f2c009bcd96277b319ba9b02d3ed14cff07f8674efeaf77483ba body_fp=3e7d3a5071bfbcfed39fc1094e26b2993fcda8be9f43751c0a5ef91fec811e93 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 -->
## `test_install_with_empty_target_names_raises(tmp_path: Path)`

Assert that `install` raises `ToolOverrideInstallError` for both empty list and `None` as `target_names`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_install_with_unknown_target_raises fingerprint=572c2b692bcbb73e70155902d114481a3ce552681a94400872b8619403e3456e body_fp=c1d3826c0152ddc355cef0f632b2f04424c694551deae8b09692fe881723c72c source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 -->
## `test_install_with_unknown_target_raises(tmp_path: Path)`

Assert that `install` raises `ToolOverrideInstallError` for an unrecognised target name, with the bad name and at least one valid harness in the message.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_apply_one_uses_needs_manual_setup_for_targets_with_no_files fingerprint=f33b7ea65004cd19d365772957c29eacf6c1e64c4485bb643ac88dc9fb8692c1 body_fp=eed1f74a60ccb9c7c0c4b57437be422175293845d8c6da08618ac629f56398ca source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 -->
## `test_apply_one_uses_needs_manual_setup_for_targets_with_no_files()`

Assert `apply_one` returns `needs_manual_setup` for a target with no files and writes nothing to disk.
<!-- trie:end -->