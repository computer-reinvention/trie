---
trie_version: 0.1.1
source: tests/test_tool_override_install.py
file_fingerprint: 1a4334d05f21e46033563e82b5d7bba56e2ef96c0fc3077b0a8268601bb35f60
last_synced_at: '2026-05-18T14:18:08Z'
description: 'Tests for `trie.tool_override_install`: replacing agent built-in tools
  with trie wrappers.'
defines:
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_install_creates_three_override_files
  lines: 39-60
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_grep_override_routes_to_trie_grep
  lines: 63-80
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_files_carry_generated_notice
  lines: 83-96
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_trie_read_takes_qname_not_path
  lines: 99-116
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_install_is_idempotent_on_identical_content
  lines: 124-144
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_install_updates_on_drift
  lines: 147-172
- kind: function
  qualified_name: tests/test_tool_override_install:test_claude_code_install_creates_advisory_hook
  lines: 180-207
- kind: function
  qualified_name: tests/test_tool_override_install:test_claude_code_hook_does_not_deny_grep
  lines: 210-224
- kind: function
  qualified_name: tests/test_tool_override_install:test_unsupported_harnesses_emit_needs_manual_setup
  lines: 236-254
- kind: function
  qualified_name: tests/test_tool_override_install:test_install_for_opencode_and_claude_code_in_one_pass
  lines: 262-275
- kind: function
  qualified_name: tests/test_tool_override_install:test_print_only_does_not_write_anything
  lines: 283-299
- kind: function
  qualified_name: tests/test_tool_override_install:test_dry_run_does_not_write_when_file_already_correct
  lines: 302-322
- kind: function
  qualified_name: tests/test_tool_override_install:test_install_with_empty_target_names_raises
  lines: 330-337
- kind: function
  qualified_name: tests/test_tool_override_install:test_install_with_unknown_target_raises
  lines: 340-354
- kind: function
  qualified_name: tests/test_tool_override_install:test_apply_one_uses_needs_manual_setup_for_targets_with_no_files
  lines: 357-366
incoming_refs: 0
outgoing_refs: 17
---
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_install_creates_three_override_files fingerprint=a5e415f4eff2ac330724dd1ff7a46d728e0829f003db25aefaedba8523f4065c body_fp=9e1495557de05784705f322d708812045f77428dbf4a8f47fc7a3817dee95499 source_ref=48efd2b1af048b57c2891527546aedf621ea84ae -->
## `test_opencode_install_creates_three_override_files(tmp_path: Path)`

Assert that `install` for `"opencode"` creates exactly `grep.ts`, `trie_read.ts`, and `trie_trace.ts` under `.opencode/tools/` on disk.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_grep_override_routes_to_trie_grep fingerprint=4d94a3118681715d6e9b3d1be0403096cb1c9c657f6095708c67ac3f00b4592e body_fp=d2f8fb18c439b5742c7894737bbfb700197d2389d17b59bfad7bfacf35c8c397 source_ref=48efd2b1af048b57c2891527546aedf621ea84ae -->
## `test_opencode_grep_override_routes_to_trie_grep(tmp_path: Path)`

Assert that the rendered `grep.ts` override shells out to `trie grep --json` via `Bun.spawn`.

- Checks spawn command string, not full file equality, allowing template evolution.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_files_carry_generated_notice fingerprint=1449c26a6f654a66721d374d982bc1a084003e3cb2d54ccc93c481ae151d7fb9 body_fp=2ef89e767c43d69f1969000a12999acf912a85903b07291f1f2f907715919def source_ref=48efd2b1af048b57c2891527546aedf621ea84ae -->
## `test_opencode_files_carry_generated_notice(tmp_path: Path)`

Assert all three opencode override files contain the auto-generated header and "Do not hand-edit" notice.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_trie_read_takes_qname_not_path fingerprint=bdfa2ad1ce51ed9276e88ce150e61be2a80e29b9ee242c540183b4765e3b8c49 body_fp=e74133bd2c144b16f33f539d8ff30f2ba7fba4b72c181bdc42857648a87ff6b0 source_ref=48efd2b1af048b57c2891527546aedf621ea84ae -->
## `test_opencode_trie_read_takes_qname_not_path(tmp_path: Path)`

Assert that `trie_read.ts` accepts a qname parameter, not a file path, and that its description disambiguates from the built-in `read` tool.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_install_is_idempotent_on_identical_content fingerprint=68d319152b04dfadc1f9f1ab82bcacfa698d7773e9b667118ceb3a48fc447bdb body_fp=4a49aa89366ea067a68c055ba15d372079bcd5fa8bfbd81c2ef0bd7a14de6e7a source_ref=48efd2b1af048b57c2891527546aedf621ea84ae -->
## `test_opencode_install_is_idempotent_on_identical_content(tmp_path: Path)`

Assert that a second `install` call with unchanged files reports `skipped` for every file with a "same contents" detail.
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

<!-- trie:section symbol=tests/test_tool_override_install:test_print_only_does_not_write_anything fingerprint=85337d2516f65896bea397a1cc6afb878de0aaece98e1ed34d6ef5a999af70c3 body_fp=e8b2e5cf8acd2805dcef89abc0b80cc5cf9eeb45a5f558b88e529c25a02f11a0 source_ref=48efd2b1af048b57c2891527546aedf621ea84ae -->
## `test_print_only_does_not_write_anything(tmp_path: Path)`

Assert that `print_only=True` writes no files and returns `preview` action with rendered contents in each file's `detail`.
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