---
trie_version: 0.1.5
source: tests/test_setup.py
file_fingerprint: 86cb254cd0c4339624942317ede1168fc28a3822bebae8ce1273c7ec7f5852c1
last_synced_at: '2026-05-28T01:37:35Z'
description: End-to-end tests for `trie setup` and the underlying hook installer.
defines:
- kind: module
  qualified_name: tests/test_setup:__module__
  lines: 1-470
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
incoming_refs: 0
outgoing_refs: 28
---
<!-- trie:section symbol=tests/test_setup:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=3d9123c15ea1bce7f754ad9181a5c24014eedc63b0a3089b7f34d09e24190b6d source_ref=a8893a5db1e60d129df684efdfac7292f52592a8 -->
## `tests/test_setup`

End-to-end tests for `trie setup` CLI and the `hook_install` module.

- `project` fixture: tmp dir with minimal `trie.toml` satisfying `Config.find_and_load`
- Covers: file creation, idempotency, `--print-only`/`--dry-run`, manual-setup targets, CLI flags, tool-override install
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:project fingerprint=7238db83261cb205b8f74f43a46da638bec089b0562445564e88a022fa35d30f body_fp=59675e01c77c385fc42e67cf14473477431a4f2ac9f47710bc7e2c6e284c10e4 source_ref=ee8a95ecaf3f1e7f45f08a83c627670aaa27deb4 -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal `trie.toml` in a temp directory, yields it as the project root, and cleans up any `.mcp.json` or `.claude/` artifacts that leaked into `cwd` or home.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_opencode_hook_creates_plugin_file fingerprint=fc94d480e290261b1fe2896b887d8b2dad458d4ad585c77f7a6e67594d0f2a0b body_fp=85c4df03f27a5fe8cfeae2657297d2b493aec26f085e933a51ed60cc90648cbe source_ref=a8893a5db1e60d129df684efdfac7292f52592a8 -->
## `test_opencode_hook_creates_plugin_file(project: Path)`

Verify that `install` for the `opencode` target writes a valid `trie-refresh.ts` plugin and a `package.json` baseline.

- Asserts `action == "created"` and file exists at `.opencode/plugins/trie-refresh.ts`.
- Checks plugin uses `session.status`/`"idle"` event and `trie refresh --after-turn`.
- Checks plugin has `export default` with `"trie-refresh"` id (v1 loader requirement).
- Checks `.opencode/package.json` exists with `@opencode-ai/plugin` dependency.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_opencode_hook_writes_package_json_to_unblock_bun_install fingerprint=150974fe71aa8f4eec1092d0f7e58e0c3a57a1466717becd48df75f5138a2fe1 body_fp=f03f9310848da0b47c4118c9092cf38c860ddc11e5d36bbfc47516915302f48f source_ref=a8893a5db1e60d129df684efdfac7292f52592a8 -->
## `test_opencode_hook_writes_package_json_to_unblock_bun_install(project: Path)`

Assert that `install` writes `.opencode/package.json` with `@opencode-ai/plugin` pinned to `"latest"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_opencode_hook_package_json_is_idempotent fingerprint=7b393b32f63bb44b824d36e8aa3788c0150b480f0506a6403216f88a96f0f2e1 body_fp=8c8f8cc8a492264bec2a6a477e3a9c9c24daf7c5c48e6a6c329b13ae49e9e9cf source_ref=a8893a5db1e60d129df684efdfac7292f52592a8 -->
## `test_opencode_hook_package_json_is_idempotent(project: Path)`

Assert that a second `install` call leaves `.opencode/package.json` byte-for-byte unchanged.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_opencode_hook_is_idempotent fingerprint=990c68bf415c67aada411639b45df589b73ff3095d81a16c682c41c8bb03e798 body_fp=da41d74adbd4a91326ed47cdbc9b56c5120a3d770782bd433d9acc3f11159096 source_ref=a8893a5db1e60d129df684efdfac7292f52592a8 -->
## `test_opencode_hook_is_idempotent(project: Path)`

Assert that a second `install` call for `opencode` reports `"skipped"` when the plugin file already matches.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_opencode_hook_updates_when_contents_changed fingerprint=16c13d1ad1551ecdb8e569a7f01c798765f464f0fac1ac0c5d706b8987d29bc5 body_fp=9692757d8c087393512c49b95541b52321aa0ff0ab325c4fe9e3ca05e3cb4161 source_ref=a8893a5db1e60d129df684efdfac7292f52592a8 -->
## `test_opencode_hook_updates_when_contents_changed(project: Path)`

Assert that `install` overwrites a stale or hand-edited `trie-refresh.ts` plugin file with correct contents, reporting action `"updated"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_print_only_writes_no_files fingerprint=f4ff1972983e259adbd54ea679d5a6967b4d0507c47cc401ab2b6a2c3cf0e3c0 body_fp=042ba869d9437bd744eb1d5dfd65ff25198c2569e662ef24edd01c3865b01dbc source_ref=a8893a5db1e60d129df684efdfac7292f52592a8 -->
## `test_print_only_writes_no_files(project: Path)`

Assert that `install` with `print_only=True` returns a `"preview"` action with contents but writes no files to disk.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_dry_run_writes_no_files fingerprint=a143c463520454fbd073ae45f77963a03b5ba91f65e6ac4691022307e2caaf32 body_fp=53d23e1514afb280388f639dc1330042b94e7b1b1b3c0cce07583bbd5822d38b source_ref=a8893a5db1e60d129df684efdfac7292f52592a8 -->
## `test_dry_run_writes_no_files(project: Path)`

Assert that `install` with `dry_run=True` returns action `"preview"` and writes no files to disk.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_claude_code_hook_is_manual_setup fingerprint=a8ace2daa3934f5c10dd65a38b09bbac037bbf420577839aab85faebe680da5f body_fp=9a613cfc093edaf0dc5b12ca8b474b8663bc5ae4035734205879d94ac5938a0b source_ref=a8893a5db1e60d129df684efdfac7292f52592a8 -->
## `test_claude_code_hook_is_manual_setup(project: Path)`

Assert that `install` returns `needs_manual_setup` (not an error or stub file) for the `claude-code` target, with `detail` containing `"trie refresh"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_unknown_target_raises fingerprint=b996901d4154a592929d95841b43d8430c072ac3d703a97266a8b5c4234ad90b body_fp=6392c2012149725cce62e97c8bf68107c4cb7394f87fec66a5778bbe48505d24 source_ref=a8893a5db1e60d129df684efdfac7292f52592a8 -->
## `test_unknown_target_raises(project: Path)`

Assert that `install` raises `HookInstallError` matching "unknown hook target" when given an unrecognised target name.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_install_all_covers_every_target fingerprint=65b44f9f93cdc70987d9b72ed2f8154b496d4438c69b5b08bfdaed8142fff5a6 body_fp=6d88fc00fb244dc77f650efa83a18da8235d39553220415d8a3212dcf5c262cb source_ref=a8893a5db1e60d129df684efdfac7292f52592a8 -->
## `test_install_all_covers_every_target(project: Path)`

Assert that `install_all=True` produces exactly one result per entry in `TARGETS`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_apply_one_returns_needs_manual_setup_for_render_none fingerprint=90abc01ee67a98b22e5174ecbf38accc7f8eb7650f4914d15cc4e7b6842010c0 body_fp=ce85ef9ee83d559e22d6d7bf66668ec77f2ad04fc5a88b0554c9547a386edb42 source_ref=a8893a5db1e60d129df684efdfac7292f52592a8 -->
## `test_apply_one_returns_needs_manual_setup_for_render_none(project: Path)`

Verify that `apply_one` returns a `needs_manual_setup` `HookApplyResult` when the target has no `render_contents`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_opencode_writes_hook_and_overrides_by_default fingerprint=572621477207cb95c3abc357b2201db81033977c79b53c7f2d85df4fa9e2301b body_fp=74e9f2639d37b1deef2df3da45803cbc55f91eea83a6aab51eb3098f31b5cac3 source_ref=a8893a5db1e60d129df684efdfac7292f52592a8 -->
## `test_cli_setup_opencode_writes_hook_and_overrides_by_default(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert `trie setup --target opencode` writes the hook plugin and `package.json` without writing MCP config.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_opencode_with_mcp_writes_mcp fingerprint=7345fdd2c5fdff0e1078271d030d8f51f5adffa6090726dbbfe5752e914b099f body_fp=b342662cd5bb9458f630031158d8ea031b455086b2cf0351557952f1491104ee source_ref=a8893a5db1e60d129df684efdfac7292f52592a8 -->
## `test_cli_setup_opencode_with_mcp_writes_mcp(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie setup --target opencode --with-mcp` writes both `opencode.json` MCP config and the hook plugin file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_claude_code_warns_about_hook fingerprint=47bccdb5ba3e9f3e7f093d38b452f268e74cb23b522780d3e427823fed4fcf60 body_fp=c41ed3cb404aa372e552a9ba57c826d4e640b9649d5b45ef0c03e43c1fc5cd66 source_ref=a8893a5db1e60d129df684efdfac7292f52592a8 -->
## `test_cli_setup_claude_code_warns_about_hook(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie setup --target claude-code` exits 0, emits a manual-setup warning, and writes no MCP config.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_claude_code_with_mcp_writes_mcp_and_warns_about_hook fingerprint=0422dee9ed6c040f17f09e839cca7e523b710314601fbe1090c581dc6c957466 body_fp=1d7d922f480d2113313b2725d34e899171262142ea22380ccdcf6b4086f8744c source_ref=a8893a5db1e60d129df684efdfac7292f52592a8 -->
## `test_cli_setup_claude_code_with_mcp_writes_mcp_and_warns_about_hook(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie setup --target claude-code --with-mcp` writes `.mcp.json`, warns about manual hook setup, and exits 0.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_print_only_writes_nothing fingerprint=0ae794aaa478e7f364ff59256049d6077fa8dd1b4b65f356984718fd8902fd56 body_fp=90b04740ee5e0283c771b34dbf0237d08c9475403ac54c40e184f60cd542c44a source_ref=a8893a5db1e60d129df684efdfac7292f52592a8 -->
## `test_cli_setup_print_only_writes_nothing(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify `trie setup --print-only` writes no files but still prints preview content to output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_target_and_all_mutex fingerprint=5b719a0905f62f2b711acb341172ce5f2aeb84e6c1814917e8213465d811d8d6 body_fp=008989d375ff5cc9ec78acbbae8a3eb5792d5b883d3d4f8822fe7d3fd806e02f source_ref=a8893a5db1e60d129df684efdfac7292f52592a8 -->
## `test_cli_setup_target_and_all_mutex(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that passing `--target` and `--all` together exits with code 1 and reports mutual exclusivity.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_invalid_scope fingerprint=0ae4df086b2c9d0f965e0c4788fd03182fca2adf1cf4ab29fe7a0d6e296eb426 body_fp=aba2bc078e35f5398dc5c35886f3a039e46c9ee2888384a66d08528c1de822a1 source_ref=a8893a5db1e60d129df684efdfac7292f52592a8 -->
## `test_cli_setup_invalid_scope(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert `trie setup` exits 1 and reports a scope error when given an unsupported `--scope` value.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_idempotent_second_run fingerprint=7c3d67f6169a8d980d23d0f443fdece2159b421050a9b0bbcfc1e32d6505411c body_fp=0dced88e31ee520fe7957b26d3b91db8c16f6b6319283f038127a149f0a7ce55 source_ref=a8893a5db1e60d129df684efdfac7292f52592a8 -->
## `test_cli_setup_idempotent_second_run(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that a second `trie setup --target opencode` invocation leaves hook files unchanged.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_installs_overrides_by_default fingerprint=e258c0885e6ad03ef7fe1c0b31f8b70c91c56d1dce2605f8e6718950a68f26dc body_fp=5530cd9ec76ec56db3d5d8e04e18955faff922e0d9ef3023cebe04f88d22eea6 source_ref=a8893a5db1e60d129df684efdfac7292f52592a8 -->
## `test_cli_setup_installs_overrides_by_default(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie setup --target opencode` writes all three tool override files without any opt-in flag.

- Verifies `grep.ts`, `read.ts`, and `trace.ts` exist under `.opencode/tools/`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_no_overrides_flag_skips_overrides fingerprint=8407ca1665d3efe3daa1a6907fcd302c1f1d4c33ce1c05f3fe318822ead89243 body_fp=9eb40bd1d57bd09c8b1681faa32a39a8c78ce2216f3972465b004a82e12920b4 source_ref=a8893a5db1e60d129df684efdfac7292f52592a8 -->
## `test_cli_setup_no_overrides_flag_skips_overrides(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `--no-overrides` prevents tool override files while hook install still runs.

- Hook plugin and MCP are unaffected; `.opencode/tools/` remains absent.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_print_only_previews_overrides_without_writing fingerprint=b2b7d3bfa3e33477b09d67e0f0ed933e298ae48f5c6bf6700facae32bba41c37 body_fp=05fa0f457f8d4b39a69742e52d814c2800e6f97f6be0afec40e941884c5ae665 source_ref=a8893a5db1e60d129df684efdfac7292f52592a8 -->
## `test_cli_setup_print_only_previews_overrides_without_writing(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `--print-only` outputs override file previews for all three opencode tools without writing any files to disk.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_claude_code_creates_advisory_hook_by_default fingerprint=22a9eac169969fc08042af9f7177daab246cabac72da267aac8b7c515ce3a647 body_fp=70ada2c65e039f43be42113f00b4ce1c7aadb5a1d4cfa9c12ee359810211f852 source_ref=a8893a5db1e60d129df684efdfac7292f52592a8 -->
## `test_cli_setup_claude_code_creates_advisory_hook_by_default(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie setup --target claude-code` writes a PreToolUse hook file referencing `mcp__trie__grep` by default.

- `hook_path`: `.claude/hooks/trie-tools.json` must exist and contain `mcp__trie__grep`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_setup:test_cli_setup_override_idempotent_on_second_run fingerprint=cf1b1f9d9fccd3a9e0b4c3cf87f6ee2ca5cc89a9f55e88d2b2228fd0ac05c34c body_fp=eead2730d42577aa637e90c9b5b09b2a6edd086ddd5f81f846c44955823f2977 source_ref=a8893a5db1e60d129df684efdfac7292f52592a8 -->
## `test_cli_setup_override_idempotent_on_second_run(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that a second `trie setup --target opencode` run skips unchanged override files and reports `skipped`.
<!-- trie:end -->