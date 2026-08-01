---
trie_version: 0.2.1
source: tests/test_setup.py
file_fingerprint: bf7bd7ecba61a41429fe5ecdcfc7e8b60408e37c1c60f6ba215a16f351aba87b
last_synced_at: '2026-08-01T09:20:27Z'
description: End-to-end tests for `trie setup` and the underlying hook installer.
defines:
- kind: module
  qualified_name: tests/test_setup:__module__
  lines: 1-543
- kind: function
  qualified_name: tests/test_setup:project
  lines: 34-53
- kind: function
  qualified_name: tests/test_setup:test_opencode_hook_creates_plugin_file
  lines: 61-91
- kind: function
  qualified_name: tests/test_setup:test_opencode_hook_writes_package_json_to_unblock_bun_install
  lines: 94-113
- kind: function
  qualified_name: tests/test_setup:test_opencode_hook_package_json_is_idempotent
  lines: 116-136
- kind: function
  qualified_name: tests/test_setup:test_opencode_hook_is_idempotent
  lines: 139-156
- kind: function
  qualified_name: tests/test_setup:test_opencode_hook_updates_when_contents_changed
  lines: 159-174
- kind: function
  qualified_name: tests/test_setup:test_print_only_writes_no_files
  lines: 177-189
- kind: function
  qualified_name: tests/test_setup:test_dry_run_writes_no_files
  lines: 192-201
- kind: function
  qualified_name: tests/test_setup:test_claude_code_hook_is_manual_setup
  lines: 204-218
- kind: function
  qualified_name: tests/test_setup:test_unknown_target_raises
  lines: 221-229
- kind: function
  qualified_name: tests/test_setup:test_install_all_covers_every_target
  lines: 232-241
- kind: function
  qualified_name: tests/test_setup:test_apply_one_returns_needs_manual_setup_for_render_none
  lines: 249-257
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_opencode_writes_hook_and_overrides_by_default
  lines: 265-281
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_opencode_with_mcp_writes_mcp
  lines: 284-300
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_claude_code_warns_about_hook
  lines: 303-312
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_claude_code_with_mcp_writes_mcp_and_warns_about_hook
  lines: 315-325
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_print_only_writes_nothing
  lines: 328-336
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_target_and_all_mutex
  lines: 339-344
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_invalid_scope
  lines: 347-352
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_idempotent_second_run
  lines: 355-369
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_installs_overrides_by_default
  lines: 382-394
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_no_overrides_flag_skips_overrides
  lines: 397-412
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_print_only_previews_overrides_without_writing
  lines: 415-430
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_claude_code_creates_advisory_hook_by_default
  lines: 433-448
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_override_idempotent_on_second_run
  lines: 451-469
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_prompts_when_multiple_agents_detected
  lines: 477-500
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_non_interactive_does_not_prompt
  lines: 503-515
- kind: function
  qualified_name: tests/test_setup:test_prompt_select_targets_parses_numbers_slugs_and_all
  lines: 518-542
incoming_refs: 0
outgoing_refs: 32
---
<!-- trie:section symbol=tests/test_setup:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=505cf6b84ffd8cbab0e5da27d0bb66f9bf3079743f2e4f7deb3391e3dae31d72 source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
End-to-end tests for `trie setup` command and the underlying hook installer.

- Tests hook installation for opencode (automated) and claude-code (manual setup required)
- Verifies idempotent behavior when re-running setup commands
- Tests CLI flags like `--print-only`, `--dry-run`, `--with-mcp`, `--no-overrides`
- Validates MCP configuration file generation and tool override installation
- Ensures proper error handling for invalid targets and mutually exclusive options
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:project fingerprint=7238db83261cb205b8f74f43a46da638bec089b0562445564e88a022fa35d30f body_fp=71d5a039142e505d420a8c98444a40f26348660f69f2d4dff190caee76289699 source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
Creates minimal trie project with config file for setup tests and cleans up artifacts.

- Creates `trie.toml` with basic configuration sections required by `Config.find_and_load`
- Cleans up any `.mcp.json` or `.claude` files that may leak outside the temp directory
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_opencode_hook_creates_plugin_file fingerprint=263c709706992b9491a35aa03163b7818a05fb6dc20ddb36359d49e34eca7d26 body_fp=a6a1697a5b1e0bc70b2ee765f432abe06caf78d8ee8ed5b10315765cff624dcd source_ref=7b00d0c0c6dd33c1043e6364acdaf4a8a35bd5d6 role=test -->
Verifies that `install()` creates a TypeScript plugin file for opencode that listens for session idle status and triggers a graph-only sync.

- Checks plugin contains "session.status", "idle", and "trie sync --graph-only --after-turn"
- Verifies plugin uses default export with "trie-refresh" id
- Confirms accompanying package.json with @opencode-ai/plugin dependency is created
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_opencode_hook_writes_package_json_to_unblock_bun_install fingerprint=150974fe71aa8f4eec1092d0f7e58e0c3a57a1466717becd48df75f5138a2fe1 body_fp=92c46bb0dbbd9c5e16c2d81670e77b8b6f0864a22fa6ba958a53ed964b21c02a source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
Tests that opencode hook installation writes package.json with latest @opencode-ai/plugin to prevent bun install failures.

- Verifies package.json exists at project/.opencode/package.json after install
- Confirms @opencode-ai/plugin dependency points to "latest" version
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_opencode_hook_package_json_is_idempotent fingerprint=7b393b32f63bb44b824d36e8aa3788c0150b480f0506a6403216f88a96f0f2e1 body_fp=91d95b59d0baf54785f4fddf8e9b1ee00ab7257151d11b7aa1af619e7e58d510 source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
Verifies that consecutive hook installs for opencode do not rewrite the package.json file when content is unchanged.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_opencode_hook_is_idempotent fingerprint=990c68bf415c67aada411639b45df589b73ff3095d81a16c682c41c8bb03e798 body_fp=42f53033603358afaf495c6dac2cbfec7b767ea46832100d5589a91e41dddaeb source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
Tests that running opencode hook install twice produces a "skipped" action on the second run when content is unchanged.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_opencode_hook_updates_when_contents_changed fingerprint=16c13d1ad1551ecdb8e569a7f01c798765f464f0fac1ac0c5d706b8987d29bc5 body_fp=2418861c2b3ede6cab280b339fafc2fea66883d9385c615ce466b83d28610e0a source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
Tests that hook installer overwrites modified plugin files with correct content.

Creates a stale plugin file, runs the installer, and verifies the file gets updated with proper hook semantics.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_print_only_writes_no_files fingerprint=f4ff1972983e259adbd54ea679d5a6967b4d0507c47cc401ab2b6a2c3cf0e3c0 body_fp=543263db61bc3c4be039353db5b7fdd8bb7947f62a62f2448f77c9061a1342f3 source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
Verifies that `install` with `print_only=True` returns preview results without writing files to disk.

- Checks that result action is "preview" and contains expected contents
- Confirms no `.opencode` directory is created on filesystem
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_dry_run_writes_no_files fingerprint=a143c463520454fbd073ae45f77963a03b5ba91f65e6ac4691022307e2caaf32 body_fp=bf45b7235dcc6edf563904b7a7a4a69f1dd0fa6132ae25fb1de4f05f2ce06665 source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
Verifies that `install` with `dry_run=True` produces preview results without creating filesystem directories.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_claude_code_hook_is_manual_setup fingerprint=6720c09ddc813966e1fcd82a0038e335e18d736a64f2f6245314c6a1a594faf4 body_fp=f4b9fb138aaaac8c58dedea0af6c8c6f73ac30a34d71164a154c235d6bcfa3de source_ref=7b00d0c0c6dd33c1043e6364acdaf4a8a35bd5d6 role=test -->
Tests that `install` returns `needs_manual_setup` for claude-code targets instead of creating files.

- Verifies `result.action` is `"needs_manual_setup"`
- Checks `result.path` is `None` (no file created)
- Confirms instructions contain "trie sync --graph-only"
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_unknown_target_raises fingerprint=b996901d4154a592929d95841b43d8430c072ac3d703a97266a8b5c4234ad90b body_fp=68f4faba62eae81bbc6ad280689d6c77f129270fea0b868cbdaa6c24a4e6f140 source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
Verifies that `install` raises `HookInstallError` when given an unknown target name.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_install_all_covers_every_target fingerprint=65b44f9f93cdc70987d9b72ed2f8154b496d4438c69b5b08bfdaed8142fff5a6 body_fp=8f6e9f751c7de493f6cbda661db27023723b728842df46c4dd4e6e376661eb1f source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
Verifies that `install` with `install_all=True` produces results for every target in the TARGETS registry.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_apply_one_returns_needs_manual_setup_for_render_none fingerprint=edf1212d32061a4320a00b7da9003acd3cf2e3a060a72b1c4c134678a0342702 body_fp=545fe6764997c9cc3e8df6fae57483f9f1645dcf2f9375b8b4a121acc6d62a2a source_ref=7b00d0c0c6dd33c1043e6364acdaf4a8a35bd5d6 role=test -->
Verifies that `apply_one` returns a manual setup result when the target has no automated hook content.

- Uses the "cursor" target which lacks `render_contents`
- Asserts the result action is "needs_manual_setup" with no file path
- Confirms the detail contains `"trie sync --graph-only"`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_opencode_writes_hook_and_overrides_by_default fingerprint=572621477207cb95c3abc357b2201db81033977c79b53c7f2d85df4fa9e2301b body_fp=9c1b33b9b3eefe2558f39173ebb72428713b4700a1ebce967adb8fc69592acb4 source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
Verifies that `trie setup --target opencode` writes hook plugin and package.json but skips MCP config by default.

- Asserts opencode.json is NOT created without --with-mcp flag
- Verifies trie-refresh.ts plugin contains session.status event handling
- Confirms package.json baseline exists to resolve @opencode-ai/plugin dependency
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_opencode_with_mcp_writes_mcp fingerprint=7345fdd2c5fdff0e1078271d030d8f51f5adffa6090726dbbfe5752e914b099f body_fp=b377b1090a20cdbbb2eb396c62b2d4f00f1d78704272b71ef270762b10904eaa source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
Tests that `trie setup --target opencode --with-mcp` writes both MCP configuration and hook files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_claude_code_warns_about_hook fingerprint=47bccdb5ba3e9f3e7f093d38b452f268e74cb23b522780d3e427823fed4fcf60 body_fp=3189d6826b4e4e269befd3bb762a1a0ee3dc69aac1a8667f6bb9aad343d8e7e1 source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
Tests that `trie setup --target claude-code` warns about manual hook setup but exits successfully.

- Verifies exit code is 0 (manual setup notices don't fail the run)
- Confirms no MCP config is written by default
- Checks that warning message about manual setup appears in output
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_claude_code_with_mcp_writes_mcp_and_warns_about_hook fingerprint=0422dee9ed6c040f17f09e839cca7e523b710314601fbe1090c581dc6c957466 body_fp=dff67546403389abad07686db357900ca6ef35a4d77abf576684b463536320ef source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=agent-integration -->
Verifies `trie setup --target claude-code --with-mcp` writes MCP config and warns about manual hook setup with exit code 0.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_print_only_writes_nothing fingerprint=0ae794aaa478e7f364ff59256049d6077fa8dd1b4b65f356984718fd8902fd56 body_fp=0c7c26439a41282d31c5e4764690a29b6ef5b1c3962dd869c1e2b04f8d8eed4f source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
Verifies `trie setup --print-only` shows preview output without creating any files or directories.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_target_and_all_mutex fingerprint=5b719a0905f62f2b711acb341172ce5f2aeb84e6c1814917e8213465d811d8d6 body_fp=71d5115441f609c7618570ac5cfb7234b9f46091c2b7cb7af8aeb7427b4d4d5b source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
Verifies that `trie setup` rejects conflicting `--target` and `--all` flags with exit code 1.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_invalid_scope fingerprint=0ae4df086b2c9d0f965e0c4788fd03182fca2adf1cf4ab29fe7a0d6e296eb426 body_fp=89e464df85cf20644466132b9c748e1c371c42f95b3a388287518fb38ce1f4ff source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
Verifies that `trie setup` rejects invalid scope values and exits with error code 1.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_idempotent_second_run fingerprint=7c3d67f6169a8d980d23d0f443fdece2159b421050a9b0bbcfc1e32d6505411c body_fp=91a3debe6f31329337dfefc770370260f9db14d35fee7bc8093c9f5a6fa58dbc source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=agent-integration -->
Verifies that running `trie setup` twice on the same project leaves files unchanged and reports skipped operations.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_installs_overrides_by_default fingerprint=e258c0885e6ad03ef7fe1c0b31f8b70c91c56d1dce2605f8e6718950a68f26dc body_fp=e52cf0deaf60907a655f73b47c85ae9e8532b8939b0ac0d32e40ddf28c64c036 source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
Verifies that `trie setup --target opencode` installs tool override files by default without requiring additional flags.

- Creates grep.ts, read.ts, and trace.ts override files in `.opencode/tools/`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_no_overrides_flag_skips_overrides fingerprint=8407ca1665d3efe3daa1a6907fcd302c1f1d4c33ce1c05f3fe318822ead89243 body_fp=94ddd9c3a804cc28b71a5aec9bc8b90f84818756f2d0df5d07f70bdb9a4cba52 source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
Tests that `trie setup --no-overrides` skips tool override installation while still writing hook and package files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_print_only_previews_overrides_without_writing fingerprint=b2b7d3bfa3e33477b09d67e0f0ed933e298ae48f5c6bf6700facae32bba41c37 body_fp=e0c7aa3c9c76858442bdbbfa1ce983846ce556c36365cf8bdf089ad2c0c20272 source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
Tests that `trie setup --print-only` shows tool override file previews without writing to disk.

- Verifies CLI includes preview content for grep.ts, read.ts, and trace.ts in output
- Confirms no files are actually created on filesystem
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_claude_code_creates_advisory_hook_by_default fingerprint=22a9eac169969fc08042af9f7177daab246cabac72da267aac8b7c515ce3a647 body_fp=8415d24900f7bbdf65ad38d9084686c0b5d597ee4cf5c11a680789bb79fc5c60 source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
Verifies that `trie setup --target claude-code` writes advisory hook file nudging agent toward trie grep tool.

- Creates `.claude/hooks/trie-tools.json` containing `mcp__trie__grep` reference
- Confirms setup succeeds without additional flags (default-on behavior)
- Tests the override installation path for Claude Code (PreToolUse hook mechanism)
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_override_idempotent_on_second_run fingerprint=cf1b1f9d9fccd3a9e0b4c3cf87f6ee2ca5cc89a9f55e88d2b2228fd0ac05c34c body_fp=098fbb0f9287e5ff57de732b76ba67af20749d3f1e0162807bce658e9ceadec2 source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
Verifies that running `trie setup --target opencode` twice reports skipped for unchanged override files.
- Tests idempotency: second run doesn't modify files when content unchanged
- Asserts "skipped" appears in CLI output for override files
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_prompts_when_multiple_agents_detected fingerprint=70761004676fd7bc2d3fb8b80428a0ac7f7944ac4169806f8798e96efe8971ab body_fp=a48e882f040df14279626d0b2efccca02e913bd84c7156a297dbe9c5483f2113 source_ref=4b6e8a038fa79aacdb6a87ebf2e4df9deba884ef role=test -->
Assert that `trie setup` shows a disambiguation prompt when multiple agents are detected and only wires the agent selected by the user.

- Patches `detected_target_slugs` to return both `claude-code` and `opencode` and `_is_interactive` to `True`.
- Supplies `"opencode\n"` as stdin input; verifies only opencode's hook plugin is written and claude-code's advisory hook is absent.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_non_interactive_does_not_prompt fingerprint=bec817eb2a78f6da3a15fbd499d440d4e720e402423ac2e2fcb17e8edc8a4330 body_fp=f9daf548aa7df3e8abe58d0620834e6ae6606fa917b94bb1f4edfc456b64c6a0 source_ref=4b6e8a038fa79aacdb6a87ebf2e4df9deba884ef role=test -->
Assert that `trie setup` in non-interactive mode wires all detected agents without displaying a selection prompt.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_prompt_select_targets_parses_numbers_slugs_and_all fingerprint=a9fb7249ea012f3de5142315892601e97ae1a9dce2b9d3edf54e61f8393fdba4 body_fp=09ad449b1e7b39a72dba832ef9e15037063a7336337bd48e1184f52f10256deb source_ref=4b6e8a038fa79aacdb6a87ebf2e4df9deba884ef role=test -->
Test that `_prompt_select_targets` correctly parses numeric indices, slug names, `"all"`, and empty input against a two-agent detected list.
<!-- trie:end -->