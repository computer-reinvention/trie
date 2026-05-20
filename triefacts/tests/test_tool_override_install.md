---
trie_version: 0.1.2
source: tests/test_tool_override_install.py
file_fingerprint: 346fad9b9250a9d6a0398ad25390458f163590878239a13322828d0fa1dd5c94
last_synced_at: '2026-05-20T13:54:54Z'
description: 'Tests for `trie.tool_override_install`: replacing agent built-in tools
  with trie wrappers.'
defines:
- kind: module
  qualified_name: tests/test_tool_override_install:__module__
  lines: 1-645
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_install_creates_three_override_files
  lines: 39-60
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_grep_override_routes_to_trie_grep
  lines: 63-77
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_files_carry_generated_notice
  lines: 80-93
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_rendered_files_have_balanced_backticks_per_line
  lines: 96-129
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_dispatches_on_qname_path_or_show_source
  lines: 137-158
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_advertises_show_source_arg
  lines: 161-174
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_qname_detection_excludes_urls_and_drives
  lines: 177-195
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_emits_telemetry_from_typescript
  lines: 198-228
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_appends_telemetry_atomically
  lines: 231-248
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_handles_absolute_paths
  lines: 251-272
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_advertises_full_arg
  lines: 275-291
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_emits_compact_renderer
  lines: 294-313
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_full_mode_trims_for_agent
  lines: 316-338
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_trie_read_obsolete_file_removed_on_apply
  lines: 341-366
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_obsolete_cleanup_is_noop_on_fresh_install
  lines: 369-384
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_install_is_idempotent_on_identical_content
  lines: 392-417
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_install_updates_on_drift
  lines: 420-445
- kind: function
  qualified_name: tests/test_tool_override_install:test_claude_code_install_creates_advisory_hook
  lines: 453-480
- kind: function
  qualified_name: tests/test_tool_override_install:test_claude_code_hook_does_not_deny_grep
  lines: 483-497
- kind: function
  qualified_name: tests/test_tool_override_install:test_unsupported_harnesses_emit_needs_manual_setup
  lines: 509-527
- kind: function
  qualified_name: tests/test_tool_override_install:test_install_for_opencode_and_claude_code_in_one_pass
  lines: 535-548
- kind: function
  qualified_name: tests/test_tool_override_install:test_print_only_does_not_write_anything
  lines: 556-577
- kind: function
  qualified_name: tests/test_tool_override_install:test_dry_run_does_not_write_when_file_already_correct
  lines: 580-600
- kind: function
  qualified_name: tests/test_tool_override_install:test_install_with_empty_target_names_raises
  lines: 608-615
- kind: function
  qualified_name: tests/test_tool_override_install:test_install_with_unknown_target_raises
  lines: 618-632
- kind: function
  qualified_name: tests/test_tool_override_install:test_apply_one_uses_needs_manual_setup_for_targets_with_no_files
  lines: 635-644
incoming_refs: 0
outgoing_refs: 29
---
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_install_creates_three_override_files fingerprint=311a913081b132222ae5933948bfc573701ad85a62aeaea33e46eb3141571d36 body_fp=738af83cbeb707dcda25021772677ed76f88d66c6495cbfc619a109956a3cfc4 source_ref=54386ad27ee9ad47292dd0874f810771cab61305 -->
## `test_opencode_install_creates_three_override_files(tmp_path: Path)`

Assert that `install` for `"opencode"` creates exactly `grep.ts`, `read.ts`, and `trie_trace.ts` under `.opencode/tools/` on disk.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_grep_override_routes_to_trie_grep fingerprint=9b92fd6651c9482e1e72bd7ff09a21b279bb5082bbfc5c07aedfef80081bedc5 body_fp=d2f8fb18c439b5742c7894737bbfb700197d2389d17b59bfad7bfacf35c8c397 source_ref=54386ad27ee9ad47292dd0874f810771cab61305 -->
## `test_opencode_grep_override_routes_to_trie_grep(tmp_path: Path)`

Assert that the rendered `grep.ts` override shells out to `trie grep --json` via `Bun.spawn`.

- Checks spawn command string, not full file equality, allowing template evolution.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_files_carry_generated_notice fingerprint=1ed4d58adc054245f9c7dee187d956a8dafd22a56e3756934931e69dea854d51 body_fp=2ef89e767c43d69f1969000a12999acf912a85903b07291f1f2f907715919def source_ref=54386ad27ee9ad47292dd0874f810771cab61305 -->
## `test_opencode_files_carry_generated_notice(tmp_path: Path)`

Assert all three opencode override files contain the auto-generated header and "Do not hand-edit" notice.
<!-- trie:end -->



<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_install_is_idempotent_on_identical_content fingerprint=87fc921b24fd75af74ee18291121a61336a1480d8b0b133629f017c95411a5fd body_fp=441d0d41588f01e2add6b3576bcc27fa4e20495dd4b40b11bbcb3784d478771b source_ref=54386ad27ee9ad47292dd0874f810771cab61305 -->
## `test_opencode_install_is_idempotent_on_identical_content(tmp_path: Path)`

Assert that a second `install` call with unchanged files reports `skipped` for every file; non-obsolete files carry "same contents" detail, obsolete-cleanup results carry "nothing to clean up".
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_install_updates_on_drift fingerprint=1598b027eb6c27bf0e21de5bea19063974caf4a976a86c98938412a210e0b5a3 body_fp=984b8039637ed58cb39eee6dd3c8efbb66aeb7bc6f3f5780467c28837580d314 source_ref=48efd2b1af048b57c2891527546aedf621ea84ae -->
## `test_opencode_install_updates_on_drift(tmp_path: Path)`

Verify that a hand-edited or stale generated file is overwritten on the next install, reporting `updated`.

- `tmp_path`: pytest-provided temporary directory used as `project_root`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:test_claude_code_install_creates_advisory_hook fingerprint=001f1ffd25598478bcd3b656b515e9b5491e5d2c8d41899e6ddbad20f3a76c36 body_fp=3f3259add28f53856fd95772944bf2295e6cb81cdc0d0f4729d14ffbe6032c23 source_ref=48efd2b1af048b57c2891527546aedf621ea84ae -->
## `test_claude_code_install_creates_advisory_hook(tmp_path: Path)`

Assert that Claude Code install writes a valid `PreToolUse` hook JSON file steering the agent toward `mcp__trie__grep`.

- `tmp_path`: pytest-provided temporary directory used as project root.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:test_claude_code_hook_does_not_deny_grep fingerprint=b0917350ef7add9adf24564bb8f967df64c94de5affe02776d3be2f57ce39bcf body_fp=c897ae84dda3140d5724e36c810ada8a35f9982534e8f6f86b7b4f59351ea1c8 source_ref=48efd2b1af048b57c2891527546aedf621ea84ae -->
## `test_claude_code_hook_does_not_deny_grep(tmp_path: Path)`

Assert the Claude Code hook file contains no `permissionDecision: deny` directive, ensuring the hook remains advisory-only.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:test_unsupported_harnesses_emit_needs_manual_setup fingerprint=252d564de8cef912137183a246a83c8734777cfbd60c0a79917aab425762c512 body_fp=60395974de519b16e12f02a3cb6a8e98256869d8ad69ae2954d6400b59ab8428 source_ref=48efd2b1af048b57c2891527546aedf621ea84ae -->
## `test_unsupported_harnesses_emit_needs_manual_setup(tmp_path: Path, slug: str)`

Assert that harnesses with no tool-override mechanism emit `needs_manual_setup` and write no files.

- `slug`: one of `claude-desktop`, `cursor`, `windsurf`, `vscode`, `codex`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:test_install_for_opencode_and_claude_code_in_one_pass fingerprint=e5a91b31de3c5d2716c71642ee28352e70962a865fe3310f85e696ab6d40c562 body_fp=975e82bba20d4dd4f674043aa04fcacb1d17de3019bdf2bda5435c63d3eb1ed1 source_ref=48efd2b1af048b57c2891527546aedf621ea84ae -->
## `test_install_for_opencode_and_claude_code_in_one_pass(tmp_path: Path)`

Verify that a single `install` call with both `"opencode"` and `"claude-code"` targets writes all expected files in one pass.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:test_print_only_does_not_write_anything fingerprint=195068d913203efa2f7a33563f5b2d88d92ce6ddea2f47b5768362fab4701a4b body_fp=9a18a0591097373da8a8611d47f4b7859cb9a8deab7a2aada9ba41f9aae48af1 source_ref=54386ad27ee9ad47292dd0874f810771cab61305 -->
## `test_print_only_does_not_write_anything(tmp_path: Path)`

Assert that `print_only=True` writes no files; new-file results are `preview` with rendered contents in `detail`; obsolete-cleanup results for absent files are `skipped`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:test_dry_run_does_not_write_when_file_already_correct fingerprint=97dd083d6cfe5d0fce2cf74184a64b3a1581bdb594a76cf69b3fe2c183f8370c body_fp=8ef34a599d2c7fe04872f1645ea0e97c963f50ce7884b704d7a3297371018d9d source_ref=48efd2b1af048b57c2891527546aedf621ea84ae -->
## `test_dry_run_does_not_write_when_file_already_correct(tmp_path: Path)`

Verify that `--dry-run` reports `skipped` when on-disk content already matches what would be written.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:test_install_with_empty_target_names_raises fingerprint=de0258da2c32f2c009bcd96277b319ba9b02d3ed14cff07f8674efeaf77483ba body_fp=8aedf20e612278c1dc5648ee69815273594156bf5c5de561b94d32b73ba62029 source_ref=48efd2b1af048b57c2891527546aedf621ea84ae -->
## `test_install_with_empty_target_names_raises(tmp_path: Path)`

Assert that `install` raises `ToolOverrideInstallError` for both empty-list and `None` target names.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:test_install_with_unknown_target_raises fingerprint=572c2b692bcbb73e70155902d114481a3ce552681a94400872b8619403e3456e body_fp=62fa64c50501dd155c397b8fd26cbb8371ce5a1ec0011d389d9d10dde80eba0c source_ref=48efd2b1af048b57c2891527546aedf621ea84ae -->
## `test_install_with_unknown_target_raises(tmp_path: Path)`

Assert `install` raises `ToolOverrideInstallError` for an unrecognised target name, with the bad name and at least one valid target in the message.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:test_apply_one_uses_needs_manual_setup_for_targets_with_no_files fingerprint=f33b7ea65004cd19d365772957c29eacf6c1e64c4485bb643ac88dc9fb8692c1 body_fp=297e05fa5e33414bd5ef3675049d6d5a27ea967d46482b8e1a321d7740d7345d source_ref=48efd2b1af048b57c2891527546aedf621ea84ae -->
## `test_apply_one_uses_needs_manual_setup_for_targets_with_no_files()`

Assert `apply_one` returns `needs_manual_setup` for a target with no files, writing nothing to disk.

- Uses `cursor` as the representative no-files target.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_dispatches_on_qname_path_or_show_source fingerprint=4322f9dae672938db27ec89fe5f9bca99aeee684b1fda63ade3688d232d451c7 body_fp=63db6c788cb9c2d69742ced192c2e739c9473ce48fda5c85854fa377f2684708 source_ref=54386ad27ee9ad47292dd0874f810771cab61305 -->
## `test_opencode_read_override_dispatches_on_qname_path_or_show_source(tmp_path: Path)`

Assert that `read.ts` contains dispatch markers for all three call modes: qname→`trie read`, path→triefact lookup, and `show_source`→raw source fallback.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_advertises_show_source_arg fingerprint=d377a5b4a375cac89dd0bf1a263a6901952e353291915687374f1447324c8283 body_fp=57f66cff63966e017bcf49ab38013ab7717a93bc2caa0f068de7d767a6099270 source_ref=54386ad27ee9ad47292dd0874f810771cab61305 -->
## `test_opencode_read_override_advertises_show_source_arg(tmp_path: Path)`

Assert that the rendered `read.ts` schema includes `show_source`, `offset`, and `limit` arguments.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_qname_detection_excludes_urls_and_drives fingerprint=a31e56fc088c1052530734293a7a78524443e45fac5d3e70153bda3a342a1916 body_fp=7dc38a4f3311ea07fae5bdb7a5ffd31d41f38b18543968171a53619d7d8e8456 source_ref=54386ad27ee9ad47292dd0874f810771cab61305 -->
## `test_opencode_read_override_qname_detection_excludes_urls_and_drives(tmp_path: Path)`

Assert that `read.ts`'s `looksLikeQname` regex rejects URLs (`://`) and Windows drive paths (`[A-Za-z]:\`).
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_emits_telemetry_from_typescript fingerprint=7f8c4fed8e631923f71efea317df78da8411d4c17e61bd0e528cb429666e563b body_fp=ce5d26c89676d7a1de0d9a5e5b2b5e28ac57981db43dc6d2c1bfd50c8bad299f source_ref=54386ad27ee9ad47292dd0874f810771cab61305 -->
## `test_opencode_read_override_emits_telemetry_from_typescript(tmp_path: Path)`

Assert that the rendered `read.ts` contains TS-side telemetry plumbing for non-qname dispatch paths.

- Checks for `emitTelemetry`, `resolveTelemetryConfig`, `extractTomlSection` helper names.
- Verifies `"cli_call"` event name, `"read"` tool name, and `mode` field are present.
- Confirms `TRIE_DEBUG` env var is honoured in the rendered template.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_appends_telemetry_atomically fingerprint=4392ac7d6c58ee986401da04b6a844b5e514681cd33a94fed47d3360195fa4f2 body_fp=96448435d9dcf49ea7ebc4e4560ca851ff2925924cebedb667e7db48219d1dc2 source_ref=54386ad27ee9ad47292dd0874f810771cab61305 -->
## `test_opencode_read_override_appends_telemetry_atomically(tmp_path: Path)`

Assert that the rendered `read.ts` uses `appendFile` from `node:fs/promises` for telemetry writes, not a read-modify-write pattern.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_trie_read_obsolete_file_removed_on_apply fingerprint=9b1d5f8b5a30c80327e621908e7e53850a244638429671af0c96104d234129fb body_fp=b4db4fbc574a92d55392bb6903aee33e8f155279a8af7c765692c7bf34f2a3c5 source_ref=54386ad27ee9ad47292dd0874f810771cab61305 -->
## `test_opencode_trie_read_obsolete_file_removed_on_apply(tmp_path: Path)`

Verify that re-running install removes the obsolete `trie_read.ts` file superseded by the new `read.ts` override.

- `tmp_path`: fresh temp directory pre-seeded with a stale `trie_read.ts` file.
- Asserts the stale file is deleted and its cleanup result has action `"updated"` with `"removed obsolete"` in the description.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_obsolete_cleanup_is_noop_on_fresh_install fingerprint=04ec87c8983682f3c5d287e359bb0d00e26fb2b3059928626ca6aa13c0d16dd4 body_fp=bdabe8fc37911d3ca52d41d6b386e5a9baf855a7c498d526dc04cd1ac6d5ebcb source_ref=54386ad27ee9ad47292dd0874f810771cab61305 -->
## `test_opencode_obsolete_cleanup_is_noop_on_fresh_install(tmp_path: Path)`

Assert that obsolete-file cleanup on a clean project reports `skipped` with "nothing to clean up" and does not error.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=87a32003d5858b95154070db9afb9e072ea310d69f06685ac24f94421b6d5034 source_ref=54386ad27ee9ad47292dd0874f810771cab61305 -->
## `tests/test_tool_override_install`

Test suite for `trie.tool_override_install`, covering tool-override installation across all supported agent harnesses.

- **opencode**: verifies three files written (`grep.ts`, `read.ts`, `trie_trace.ts`), content correctness, idempotency, drift detection, and obsolete-file cleanup
- **claude-code**: verifies advisory-only `PreToolUse` hook written to `.claude/hooks/trie-tools.json`
- **other harnesses**: verifies `needs_manual_setup` result with no files written
- **preview/dry-run**: verifies neither mode touches disk
- **error handling**: verifies empty/unknown targets raise `ToolOverrideInstallError`
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_handles_absolute_paths fingerprint=331fc83490b3d1f8cf59065f4c0128e7d3321e595ed45c4912a282848cf2c585 body_fp=b95015ee329dd28c123fd697e93c22449b558e490a20be37e16403b054fc87e0 source_ref=d3095c353e2dea491cce6acc2c63c0f3f28041d3 -->
## `test_opencode_read_override_handles_absolute_paths(tmp_path: Path)`

Assert that `read.ts` uses `isAbsolute(path)` to handle absolute paths verbatim instead of joining them onto cwd.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_advertises_full_arg fingerprint=005cdc6c3d94967f1d1afa9f90580144130596b3eae9e920da25a090a43812dd body_fp=19dcdf875157bc8be64fd1ffb9364d1b878005d3a86959d9912d6e0d4042dae4 source_ref=d3095c353e2dea491cce6acc2c63c0f3f28041d3 -->
## `test_opencode_read_override_advertises_full_arg(tmp_path: Path)`

Assert that the rendered `read.ts` wrapper exposes a `full: bool` argument so agents can opt out of compact mode.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_emits_compact_renderer fingerprint=5695f91271e789440ef43b5a770758ef6502837591c372a78ebe8aa3c93de99a body_fp=e40c5a68212829bbaed5dbd83db3712a061a30346b8faf223fdcd258cea6bf24 source_ref=d3095c353e2dea491cce6acc2c63c0f3f28041d3 -->
## `test_opencode_read_override_emits_compact_renderer(tmp_path: Path)`

Assert that the rendered `read.ts` wrapper contains compact-rendering helpers and telemetry mode tags for both compact and full paths.

- `tmp_path`: pytest fixture providing an isolated temporary directory.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_full_mode_trims_for_agent fingerprint=d16eec00436dccc69af73d191648d1d6ccfaa708532d5301f331e513bd01bf08 body_fp=3fcdc33b9f8685e84a167a0eeb48ccc4fbe8945994b79c9d9edbca9452e261c0 source_ref=d3095c353e2dea491cce6acc2c63c0f3f28041d3 -->
## `test_opencode_read_override_full_mode_trims_for_agent(tmp_path: Path)`

Assert that `full: true` mode routes through `renderForAgent`, stripping internal frontmatter keys and sentinel comments before returning content to the agent.

- Checks for `renderForAgent`, `stripSentinels`, and `renderFrontMatterForAgent` helpers.
- Verifies `result = renderForAgent(triefact)` call site exists.
- Verifies the raw `result = triefact` leak pattern is absent for full mode.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_rendered_files_have_balanced_backticks_per_line fingerprint=b10d440c635ed2b7ce7200e27f8521ed5f0d6f0882f993a7fcac8addd399ab04 body_fp=231d983706b3c3561272b29f9b51870304f72d736690c9ac90444ce072e297ef source_ref=768573ad34b38438e73a322470e24aaed565093e -->
## `test_opencode_rendered_files_have_balanced_backticks_per_line(tmp_path: Path)`

Regression-guard: assert every `//` comment line in all three rendered `.ts` files has an even backtick count.

- Odd count in a comment opens a stray JS template literal, causing bun parse failure.
- Root cause guarded against: unescaped `\n` in Python renderer splitting a single-line comment.
<!-- trie:end -->