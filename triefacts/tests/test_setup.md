---
trie_version: 0.3.0
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
  signature: 'def project(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_setup:test_opencode_hook_creates_plugin_file
  lines: 61-91
  signature: 'def test_opencode_hook_creates_plugin_file(project: Path)'
- kind: function
  qualified_name: tests/test_setup:test_opencode_hook_writes_package_json_to_unblock_bun_install
  lines: 94-113
  signature: 'def test_opencode_hook_writes_package_json_to_unblock_bun_install(project: Path)'
- kind: function
  qualified_name: tests/test_setup:test_opencode_hook_package_json_is_idempotent
  lines: 116-136
  signature: 'def test_opencode_hook_package_json_is_idempotent(project: Path)'
- kind: function
  qualified_name: tests/test_setup:test_opencode_hook_is_idempotent
  lines: 139-156
  signature: 'def test_opencode_hook_is_idempotent(project: Path)'
- kind: function
  qualified_name: tests/test_setup:test_opencode_hook_updates_when_contents_changed
  lines: 159-174
  signature: 'def test_opencode_hook_updates_when_contents_changed(project: Path)'
- kind: function
  qualified_name: tests/test_setup:test_print_only_writes_no_files
  lines: 177-189
  signature: 'def test_print_only_writes_no_files(project: Path)'
- kind: function
  qualified_name: tests/test_setup:test_dry_run_writes_no_files
  lines: 192-201
  signature: 'def test_dry_run_writes_no_files(project: Path)'
- kind: function
  qualified_name: tests/test_setup:test_claude_code_hook_is_manual_setup
  lines: 204-218
  signature: 'def test_claude_code_hook_is_manual_setup(project: Path)'
- kind: function
  qualified_name: tests/test_setup:test_unknown_target_raises
  lines: 221-229
  signature: 'def test_unknown_target_raises(project: Path)'
- kind: function
  qualified_name: tests/test_setup:test_install_all_covers_every_target
  lines: 232-241
  signature: 'def test_install_all_covers_every_target(project: Path)'
- kind: function
  qualified_name: tests/test_setup:test_apply_one_returns_needs_manual_setup_for_render_none
  lines: 249-257
  signature: 'def test_apply_one_returns_needs_manual_setup_for_render_none(project: Path)'
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_opencode_writes_hook_and_overrides_by_default
  lines: 265-281
  signature: 'def test_cli_setup_opencode_writes_hook_and_overrides_by_default( project: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_opencode_with_mcp_writes_mcp
  lines: 284-300
  signature: 'def test_cli_setup_opencode_with_mcp_writes_mcp(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_claude_code_warns_about_hook
  lines: 303-312
  signature: 'def test_cli_setup_claude_code_warns_about_hook(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_claude_code_with_mcp_writes_mcp_and_warns_about_hook
  lines: 315-325
  signature: 'def test_cli_setup_claude_code_with_mcp_writes_mcp_and_warns_about_hook( project: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_print_only_writes_nothing
  lines: 328-336
  signature: 'def test_cli_setup_print_only_writes_nothing(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_target_and_all_mutex
  lines: 339-344
  signature: 'def test_cli_setup_target_and_all_mutex(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_invalid_scope
  lines: 347-352
  signature: 'def test_cli_setup_invalid_scope(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_idempotent_second_run
  lines: 355-369
  signature: 'def test_cli_setup_idempotent_second_run(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_installs_overrides_by_default
  lines: 382-394
  signature: 'def test_cli_setup_installs_overrides_by_default(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_no_overrides_flag_skips_overrides
  lines: 397-412
  signature: 'def test_cli_setup_no_overrides_flag_skips_overrides( project: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_print_only_previews_overrides_without_writing
  lines: 415-430
  signature: 'def test_cli_setup_print_only_previews_overrides_without_writing( project: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_claude_code_creates_advisory_hook_by_default
  lines: 433-448
  signature: 'def test_cli_setup_claude_code_creates_advisory_hook_by_default( project: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_override_idempotent_on_second_run
  lines: 451-469
  signature: 'def test_cli_setup_override_idempotent_on_second_run( project: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_prompts_when_multiple_agents_detected
  lines: 477-500
  signature: 'def test_cli_setup_prompts_when_multiple_agents_detected( project: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_non_interactive_does_not_prompt
  lines: 503-515
  signature: 'def test_cli_setup_non_interactive_does_not_prompt(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_setup:test_prompt_select_targets_parses_numbers_slugs_and_all
  lines: 518-542
  signature: 'def test_prompt_select_targets_parses_numbers_slugs_and_all(monkeypatch: pytest.MonkeyPatch)'
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
<!-- trie:section symbol=tests/test_setup:project fingerprint=7238db83261cb205b8f74f43a46da638bec089b0562445564e88a022fa35d30f body_fp=d0e12c030d853ce665c2868e63e6ccbfc5975101753e585c975a35dcf0da0dd9 source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
## `def project(tmp_path: Path) -> Path`

Creates minimal trie project with config file for setup tests and cleans up artifacts.

- Creates `trie.toml` with basic configuration sections required by `Config.find_and_load`
- Cleans up any `.mcp.json` or `.claude` files that may leak outside the temp directory
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_opencode_hook_creates_plugin_file fingerprint=263c709706992b9491a35aa03163b7818a05fb6dc20ddb36359d49e34eca7d26 body_fp=46f6813c0559c4d84124b57845c86fe84273f9c167d5a2104eb9baa93f57f2a4 source_ref=7b00d0c0c6dd33c1043e6364acdaf4a8a35bd5d6 role=test -->
## `def test_opencode_hook_creates_plugin_file(project: Path)`

Verifies that `install()` creates a TypeScript plugin file for opencode that listens for session idle status and triggers a graph-only sync.

- Checks plugin contains "session.status", "idle", and "trie sync --graph-only --after-turn"
- Verifies plugin uses default export with "trie-refresh" id
- Confirms accompanying package.json with @opencode-ai/plugin dependency is created
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_opencode_hook_writes_package_json_to_unblock_bun_install fingerprint=150974fe71aa8f4eec1092d0f7e58e0c3a57a1466717becd48df75f5138a2fe1 body_fp=bdb82e8bcf36c3870bb8418b19cb547bcb520ee2e14f4c08359da3e4ceabc628 source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
## `def test_opencode_hook_writes_package_json_to_unblock_bun_install(project: Path)`

Tests that opencode hook installation writes package.json with latest @opencode-ai/plugin to prevent bun install failures.

- Verifies package.json exists at project/.opencode/package.json after install
- Confirms @opencode-ai/plugin dependency points to "latest" version
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_opencode_hook_package_json_is_idempotent fingerprint=7b393b32f63bb44b824d36e8aa3788c0150b480f0506a6403216f88a96f0f2e1 body_fp=38975c2feeccd62715271526c94240a738116522471355ca3b06c510d0d7984b source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
## `def test_opencode_hook_package_json_is_idempotent(project: Path)`

Verifies that consecutive hook installs for opencode do not rewrite the package.json file when content is unchanged.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_opencode_hook_is_idempotent fingerprint=990c68bf415c67aada411639b45df589b73ff3095d81a16c682c41c8bb03e798 body_fp=45f6123a3c816f13b52b89cb2746dfaf0ba55b6df105c0aa204056d1ae39d4f2 source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
## `def test_opencode_hook_is_idempotent(project: Path)`

Tests that running opencode hook install twice produces a "skipped" action on the second run when content is unchanged.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_opencode_hook_updates_when_contents_changed fingerprint=16c13d1ad1551ecdb8e569a7f01c798765f464f0fac1ac0c5d706b8987d29bc5 body_fp=c9722a1d1100b4ea34c4004855f4d3cec92b63b299705b5b6519b9a79672cc21 source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
## `def test_opencode_hook_updates_when_contents_changed(project: Path)`

Tests that hook installer overwrites modified plugin files with correct content.

Creates a stale plugin file, runs the installer, and verifies the file gets updated with proper hook semantics.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_print_only_writes_no_files fingerprint=f4ff1972983e259adbd54ea679d5a6967b4d0507c47cc401ab2b6a2c3cf0e3c0 body_fp=b6cbfe4f3e9b191da5a2c55dec72d046c9d1b9cf248fba9502f0a8eeebccc918 source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
## `def test_print_only_writes_no_files(project: Path)`

Verifies that `install` with `print_only=True` returns preview results without writing files to disk.

- Checks that result action is "preview" and contains expected contents
- Confirms no `.opencode` directory is created on filesystem
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_dry_run_writes_no_files fingerprint=a143c463520454fbd073ae45f77963a03b5ba91f65e6ac4691022307e2caaf32 body_fp=6f58b88d456a1924ec1f05d185b1742bdcbb5c254fde75e47bf48cdc527ab139 source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
## `def test_dry_run_writes_no_files(project: Path)`

Verifies that `install` with `dry_run=True` produces preview results without creating filesystem directories.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_claude_code_hook_is_manual_setup fingerprint=6720c09ddc813966e1fcd82a0038e335e18d736a64f2f6245314c6a1a594faf4 body_fp=ab04681efecdecbac4f93901b0a86bfd39d1d3b01eafb69072bd824d6cdbf843 source_ref=7b00d0c0c6dd33c1043e6364acdaf4a8a35bd5d6 role=test -->
## `def test_claude_code_hook_is_manual_setup(project: Path)`

Tests that `install` returns `needs_manual_setup` for claude-code targets instead of creating files.

- Verifies `result.action` is `"needs_manual_setup"`
- Checks `result.path` is `None` (no file created)
- Confirms instructions contain "trie sync --graph-only"
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_unknown_target_raises fingerprint=b996901d4154a592929d95841b43d8430c072ac3d703a97266a8b5c4234ad90b body_fp=4e6259ee3603a7eb389f3f344007c973a4f7f8e406bcfa9c40a904600ff18b6f source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
## `def test_unknown_target_raises(project: Path)`

Verifies that `install` raises `HookInstallError` when given an unknown target name.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_install_all_covers_every_target fingerprint=65b44f9f93cdc70987d9b72ed2f8154b496d4438c69b5b08bfdaed8142fff5a6 body_fp=d00ceb812276c50357faa2b3dd24b0ab016393149169bf0e1eec48079d63d93d source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
## `def test_install_all_covers_every_target(project: Path)`

Verifies that `install` with `install_all=True` produces results for every target in the TARGETS registry.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_apply_one_returns_needs_manual_setup_for_render_none fingerprint=edf1212d32061a4320a00b7da9003acd3cf2e3a060a72b1c4c134678a0342702 body_fp=e9181f47192e7786441d16d06983a8bf993eea9bd52d9729e68e2cb48eeeae04 source_ref=7b00d0c0c6dd33c1043e6364acdaf4a8a35bd5d6 role=test -->
## `def test_apply_one_returns_needs_manual_setup_for_render_none(project: Path)`

Verifies that `apply_one` returns a manual setup result when the target has no automated hook content.

- Uses the "cursor" target which lacks `render_contents`
- Asserts the result action is "needs_manual_setup" with no file path
- Confirms the detail contains `"trie sync --graph-only"`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_opencode_writes_hook_and_overrides_by_default fingerprint=572621477207cb95c3abc357b2201db81033977c79b53c7f2d85df4fa9e2301b body_fp=f996176bda982a8583c12527293906b83e424ae26c572757d278f4245fed883e source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
## `def test_cli_setup_opencode_writes_hook_and_overrides_by_default( project: Path, monkeypatch: pytest.MonkeyPatch )`

Verifies that `trie setup --target opencode` writes hook plugin and package.json but skips MCP config by default.

- Asserts opencode.json is NOT created without --with-mcp flag
- Verifies trie-refresh.ts plugin contains session.status event handling
- Confirms package.json baseline exists to resolve @opencode-ai/plugin dependency
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_opencode_with_mcp_writes_mcp fingerprint=7345fdd2c5fdff0e1078271d030d8f51f5adffa6090726dbbfe5752e914b099f body_fp=f623a190d98f16ee98a4ebf02e357166ca0d16b7b8c84b4648584cd9b742a606 source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
## `def test_cli_setup_opencode_with_mcp_writes_mcp(project: Path, monkeypatch: pytest.MonkeyPatch)`

Tests that `trie setup --target opencode --with-mcp` writes both MCP configuration and hook files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_claude_code_warns_about_hook fingerprint=47bccdb5ba3e9f3e7f093d38b452f268e74cb23b522780d3e427823fed4fcf60 body_fp=3444eb5a88383522d1f3784313e43c084d6f62d6681d8761988063d32849b454 source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
## `def test_cli_setup_claude_code_warns_about_hook(project: Path, monkeypatch: pytest.MonkeyPatch)`

Tests that `trie setup --target claude-code` warns about manual hook setup but exits successfully.

- Verifies exit code is 0 (manual setup notices don't fail the run)
- Confirms no MCP config is written by default
- Checks that warning message about manual setup appears in output
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_claude_code_with_mcp_writes_mcp_and_warns_about_hook fingerprint=0422dee9ed6c040f17f09e839cca7e523b710314601fbe1090c581dc6c957466 body_fp=7457770f5bcb713258b49b3e9eb5e92b3031ae9eb0e02e615f6c36bc153ac9fc source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=agent-integration -->
## `def test_cli_setup_claude_code_with_mcp_writes_mcp_and_warns_about_hook( project: Path, monkeypatch: pytest.MonkeyPatch )`

Verifies `trie setup --target claude-code --with-mcp` writes MCP config and warns about manual hook setup with exit code 0.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_print_only_writes_nothing fingerprint=0ae794aaa478e7f364ff59256049d6077fa8dd1b4b65f356984718fd8902fd56 body_fp=604947af2c3214414b8b030abf353eb3172eed03ae44df7e01424c91dc890713 source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
## `def test_cli_setup_print_only_writes_nothing(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verifies `trie setup --print-only` shows preview output without creating any files or directories.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_target_and_all_mutex fingerprint=5b719a0905f62f2b711acb341172ce5f2aeb84e6c1814917e8213465d811d8d6 body_fp=b286cab534a84db3a3017816cf5577f23bd9caa4b5f4e031d311a92330d700bd source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
## `def test_cli_setup_target_and_all_mutex(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verifies that `trie setup` rejects conflicting `--target` and `--all` flags with exit code 1.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_invalid_scope fingerprint=0ae4df086b2c9d0f965e0c4788fd03182fca2adf1cf4ab29fe7a0d6e296eb426 body_fp=d9123f8b76472222a55bd3ae7ff82c61b808cf2db25a736464be93b741061c06 source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
## `def test_cli_setup_invalid_scope(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verifies that `trie setup` rejects invalid scope values and exits with error code 1.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_idempotent_second_run fingerprint=7c3d67f6169a8d980d23d0f443fdece2159b421050a9b0bbcfc1e32d6505411c body_fp=d6ae17d5b82d7bdc14d52725e155c2273eebcc2413ff1c9edf4798d93d2ea035 source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=agent-integration -->
## `def test_cli_setup_idempotent_second_run(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verifies that running `trie setup` twice on the same project leaves files unchanged and reports skipped operations.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_installs_overrides_by_default fingerprint=e258c0885e6ad03ef7fe1c0b31f8b70c91c56d1dce2605f8e6718950a68f26dc body_fp=a32409ec1d0615a2a57509d8e1d1df121d982f4f9a5b509a23162542c47e855f source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
## `def test_cli_setup_installs_overrides_by_default(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verifies that `trie setup --target opencode` installs tool override files by default without requiring additional flags.

- Creates grep.ts, read.ts, and trace.ts override files in `.opencode/tools/`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_no_overrides_flag_skips_overrides fingerprint=8407ca1665d3efe3daa1a6907fcd302c1f1d4c33ce1c05f3fe318822ead89243 body_fp=baf2821262eb2cacb882ebea9a36b48c87d2dc33261dbeeb6d87c82a74c983e9 source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
## `def test_cli_setup_no_overrides_flag_skips_overrides( project: Path, monkeypatch: pytest.MonkeyPatch )`

Tests that `trie setup --no-overrides` skips tool override installation while still writing hook and package files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_print_only_previews_overrides_without_writing fingerprint=b2b7d3bfa3e33477b09d67e0f0ed933e298ae48f5c6bf6700facae32bba41c37 body_fp=9d603f61978d8c1c53c4cb73c7c902bb4976895c96bd4867e8de90c5820911f9 source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
## `def test_cli_setup_print_only_previews_overrides_without_writing( project: Path, monkeypatch: pytest.MonkeyPatch )`

Tests that `trie setup --print-only` shows tool override file previews without writing to disk.

- Verifies CLI includes preview content for grep.ts, read.ts, and trace.ts in output
- Confirms no files are actually created on filesystem
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_claude_code_creates_advisory_hook_by_default fingerprint=22a9eac169969fc08042af9f7177daab246cabac72da267aac8b7c515ce3a647 body_fp=4195bd20cb1ddf90bb598e5cd61528ad2d05321caeb6c300a2ebcb9ccca344ff source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
## `def test_cli_setup_claude_code_creates_advisory_hook_by_default( project: Path, monkeypatch: pytest.MonkeyPatch )`

Verifies that `trie setup --target claude-code` writes advisory hook file nudging agent toward trie grep tool.

- Creates `.claude/hooks/trie-tools.json` containing `mcp__trie__grep` reference
- Confirms setup succeeds without additional flags (default-on behavior)
- Tests the override installation path for Claude Code (PreToolUse hook mechanism)
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_override_idempotent_on_second_run fingerprint=cf1b1f9d9fccd3a9e0b4c3cf87f6ee2ca5cc89a9f55e88d2b2228fd0ac05c34c body_fp=9a7102028a82b45c26f17164368083aced8368a379b79b8d7d75617d700b2be9 source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 role=test-infrastructure -->
## `def test_cli_setup_override_idempotent_on_second_run( project: Path, monkeypatch: pytest.MonkeyPatch )`

Verifies that running `trie setup --target opencode` twice reports skipped for unchanged override files.
- Tests idempotency: second run doesn't modify files when content unchanged
- Asserts "skipped" appears in CLI output for override files
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_prompts_when_multiple_agents_detected fingerprint=70761004676fd7bc2d3fb8b80428a0ac7f7944ac4169806f8798e96efe8971ab body_fp=7f3c29e344619941d2990cb29aec86cf8baf360f1f9c489bb5a773f3ff93a5f7 source_ref=4b6e8a038fa79aacdb6a87ebf2e4df9deba884ef role=test -->
## `def test_cli_setup_prompts_when_multiple_agents_detected( project: Path, monkeypatch: pytest.MonkeyPatch )`

Assert that `trie setup` shows a disambiguation prompt when multiple agents are detected and only wires the agent selected by the user.

- Patches `detected_target_slugs` to return both `claude-code` and `opencode` and `_is_interactive` to `True`.
- Supplies `"opencode\n"` as stdin input; verifies only opencode's hook plugin is written and claude-code's advisory hook is absent.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_non_interactive_does_not_prompt fingerprint=bec817eb2a78f6da3a15fbd499d440d4e720e402423ac2e2fcb17e8edc8a4330 body_fp=0b9012d1a6d0e9f9b6b63a0bc582762486537331fb3ffce8e3edd48e88cfa300 source_ref=4b6e8a038fa79aacdb6a87ebf2e4df9deba884ef role=test -->
## `def test_cli_setup_non_interactive_does_not_prompt(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie setup` in non-interactive mode wires all detected agents without displaying a selection prompt.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_prompt_select_targets_parses_numbers_slugs_and_all fingerprint=a9fb7249ea012f3de5142315892601e97ae1a9dce2b9d3edf54e61f8393fdba4 body_fp=8a2dc32f0957b92712d767a297d55e1c71f3830f771c392cf0c240f08326d140 source_ref=4b6e8a038fa79aacdb6a87ebf2e4df9deba884ef role=test -->
## `def test_prompt_select_targets_parses_numbers_slugs_and_all(monkeypatch: pytest.MonkeyPatch)`

Test that `_prompt_select_targets` correctly parses numeric indices, slug names, `"all"`, and empty input against a two-agent detected list.
<!-- trie:end -->