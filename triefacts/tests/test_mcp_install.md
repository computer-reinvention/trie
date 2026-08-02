---
trie_version: 0.3.0
source: tests/test_mcp_install.py
file_fingerprint: 8399ac3e31ad74a55ffb80c970128fb056d906ad47665b8d66ffb7e7e8db5322
last_synced_at: '2026-08-01T09:20:23Z'
defines:
- kind: module
  qualified_name: tests/test_mcp_install:__module__
  lines: 1-762
- kind: function
  qualified_name: tests/test_mcp_install:project
  lines: 20-37
  signature: 'def project(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_mcp_install:test_snippet_uses_serve_subcommand
  lines: 43-47
  signature: 'def test_snippet_uses_serve_subcommand(project: Path)'
- kind: function
  qualified_name: tests/test_mcp_install:test_install_claude_code_creates_file
  lines: 53-68
  signature: 'def test_install_claude_code_creates_file(project: Path)'
- kind: function
  qualified_name: tests/test_mcp_install:test_install_preserves_other_servers
  lines: 71-85
  signature: 'def test_install_preserves_other_servers(project: Path)'
- kind: function
  qualified_name: tests/test_mcp_install:test_install_idempotent_when_unchanged
  lines: 88-105
  signature: 'def test_install_idempotent_when_unchanged(project: Path)'
- kind: function
  qualified_name: tests/test_mcp_install:test_install_errors_on_unknown_target
  lines: 108-117
  signature: 'def test_install_errors_on_unknown_target(project: Path)'
- kind: function
  qualified_name: tests/test_mcp_install:test_install_print_only_writes_no_file
  lines: 123-133
  signature: 'def test_install_print_only_writes_no_file(project: Path)'
- kind: function
  qualified_name: tests/test_mcp_install:test_install_dry_run_writes_no_file
  lines: 136-146
  signature: 'def test_install_dry_run_writes_no_file(project: Path)'
- kind: function
  qualified_name: tests/test_mcp_install:test_install_opencode_creates_project_config
  lines: 152-174
  signature: 'def test_install_opencode_creates_project_config(project: Path)'
- kind: function
  qualified_name: tests/test_mcp_install:test_install_opencode_user_scope_lands_in_config_dir
  lines: 177-196
  signature: 'def test_install_opencode_user_scope_lands_in_config_dir( project: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_mcp_install:test_install_opencode_preserves_existing_mcp_servers
  lines: 199-225
  signature: 'def test_install_opencode_preserves_existing_mcp_servers(project: Path)'
- kind: function
  qualified_name: tests/test_mcp_install:test_install_opencode_idempotent_when_unchanged
  lines: 228-245
  signature: 'def test_install_opencode_idempotent_when_unchanged(project: Path)'
- kind: function
  qualified_name: tests/test_mcp_install:test_install_vscode_uses_servers_key
  lines: 251-266
  signature: 'def test_install_vscode_uses_servers_key(project: Path)'
- kind: function
  qualified_name: tests/test_mcp_install:test_install_errors_on_invalid_json
  lines: 272-282
  signature: 'def test_install_errors_on_invalid_json(project: Path)'
- kind: function
  qualified_name: tests/test_mcp_install:test_install_user_scope_writes_to_user_path
  lines: 288-307
  signature: 'def test_install_user_scope_writes_to_user_path( project: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_mcp_install:test_install_skips_target_without_scope
  lines: 310-321
  signature: 'def test_install_skips_target_without_scope(project: Path)'
- kind: function
  qualified_name: tests/test_mcp_install:test_detect_returns_false_in_clean_environment
  lines: 327-334
  signature: 'def test_detect_returns_false_in_clean_environment(monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_mcp_install:test_detected_target_slugs_empty_on_clean_environment
  lines: 337-344
  signature: 'def test_detected_target_slugs_empty_on_clean_environment(monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_mcp_install:test_detected_target_slugs_reports_installed_in_registry_order
  lines: 347-362
  signature: 'def test_detected_target_slugs_reports_installed_in_registry_order( monkeypatch: pytest.MonkeyPatch, )'
- kind: function
  qualified_name: tests/test_mcp_install:test_install_auto_detect_errors_when_nothing_found
  lines: 365-379
  signature: 'def test_install_auto_detect_errors_when_nothing_found( project: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_mcp_install:test_install_all_runs_every_target_in_print_mode
  lines: 385-402
  signature: 'def test_install_all_runs_every_target_in_print_mode(project: Path)'
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_install_print_only
  lines: 408-414
  signature: 'def test_cli_mcp_install_print_only(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_install_writes_file
  lines: 417-423
  signature: 'def test_cli_mcp_install_writes_file(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_install_unknown_target
  lines: 426-431
  signature: 'def test_cli_mcp_install_unknown_target(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_install_target_and_all_mutex
  lines: 434-439
  signature: 'def test_cli_mcp_install_target_and_all_mutex(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_serve_dispatches_to_run_stdio
  lines: 442-454
  signature: 'def test_cli_mcp_serve_dispatches_to_run_stdio(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_no_subcommand_prints_help
  lines: 457-475
  signature: 'def test_cli_mcp_no_subcommand_prints_help(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_mcp_install:test_uninstall_removes_trie_entry
  lines: 485-517
  signature: 'def test_uninstall_removes_trie_entry(project: Path)'
- kind: function
  qualified_name: tests/test_mcp_install:test_uninstall_preserves_other_servers
  lines: 520-554
  signature: 'def test_uninstall_preserves_other_servers(project: Path)'
- kind: function
  qualified_name: tests/test_mcp_install:test_uninstall_when_not_installed_is_skipped
  lines: 557-571
  signature: 'def test_uninstall_when_not_installed_is_skipped(project: Path)'
- kind: function
  qualified_name: tests/test_mcp_install:test_uninstall_when_config_has_no_trie_key_is_skipped
  lines: 574-599
  signature: 'def test_uninstall_when_config_has_no_trie_key_is_skipped(project: Path)'
- kind: function
  qualified_name: tests/test_mcp_install:test_uninstall_dry_run_does_not_modify_file
  lines: 602-625
  signature: 'def test_uninstall_dry_run_does_not_modify_file(project: Path)'
- kind: function
  qualified_name: tests/test_mcp_install:test_uninstall_print_only_does_not_modify_file
  lines: 628-651
  signature: 'def test_uninstall_print_only_does_not_modify_file(project: Path)'
- kind: function
  qualified_name: tests/test_mcp_install:test_uninstall_all_targets
  lines: 654-684
  signature: 'def test_uninstall_all_targets(project: Path)'
- kind: function
  qualified_name: tests/test_mcp_install:test_uninstall_unknown_target_raises
  lines: 687-698
  signature: def test_uninstall_unknown_target_raises()
- kind: function
  qualified_name: tests/test_mcp_install:test_uninstall_invalid_json_returns_error
  lines: 701-718
  signature: 'def test_uninstall_invalid_json_returns_error(project: Path)'
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_uninstall_round_trips
  lines: 724-738
  signature: 'def test_cli_mcp_uninstall_round_trips(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_uninstall_rejects_target_and_all_together
  lines: 741-750
  signature: 'def test_cli_mcp_uninstall_rejects_target_and_all_together( project: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_help_lists_uninstall
  lines: 753-761
  signature: 'def test_cli_mcp_help_lists_uninstall(project: Path, monkeypatch: pytest.MonkeyPatch)'
incoming_refs: 0
outgoing_refs: 49
---
<!-- trie:section symbol=tests/test_mcp_install:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=747a97780bb1505eb138bdc4cf2d7bae011ace0fb3b41d24ee8fcae769a4012c source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
Comprehensive test suite for MCP installation and uninstallation functionality across different AI agent targets.

- Tests installation for Claude Code, opencode, VS Code, and other AI agents
- Validates configuration file creation, updates, and preservation of existing servers  
- Covers project and user scope installations with proper path resolution
- Tests CLI commands for install/uninstall with various flags and error conditions
- Verifies dry-run, print-only, and auto-detection modes work correctly
- Ensures idempotent operations and proper error handling for malformed configs
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:project fingerprint=ec0dcdc7ce6b4eb60414b372c10e3ddd78937efff6c97a9c42895523ab41b485 body_fp=628b8779551c3a3bbdba8a9b8b53f5fa173e92c6ced438e6687817b75110f4de source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=test-infrastructure -->
## `def project(tmp_path: Path) -> Path`

Creates temporary project directory with trie.toml configuration file and cleans up MCP installation artifacts after test completion.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_snippet_uses_serve_subcommand fingerprint=64e9dd207621028e9aaaa81e3e2f4ff89f8d2e8def334be47eea06f9eb38a9a0 body_fp=453217746849e66c082fc8327a7f037d6a97bb5c326a760a80f4509ca2b2942e source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
## `def test_snippet_uses_serve_subcommand(project: Path)`

Tests that `trie_server_snippet` generates command configuration with "trie" command, ["mcp", "serve"] args, and resolved project path as working directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_claude_code_creates_file fingerprint=901f2a4de5c763742d248d63f1efe2f94fe89ae5a4547c2d4a1ffbfdd4757c24 body_fp=520df2010796823dfe2e912b720d4ce4ed7a04c8f3c27707fb64e1fc5d69d440 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
## `def test_install_claude_code_creates_file(project: Path)`

Tests that installing the claude-code target creates a `.mcp.json` file with proper trie server configuration.

- Verifies plan contains one result with "created" action
- Confirms file written to project root with correct path
- Validates JSON structure contains trie entry under mcpServers with correct args
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_preserves_other_servers fingerprint=d7e5f3a30a59855914ceb6300c7973d65f4f9f3052e3289d40988a7fa7a4c2d7 body_fp=783e0957c9531e80711f5ec92db6821e8dcf1dcecf2d790ed1fd2b602e34ef5a source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
## `def test_install_preserves_other_servers(project: Path)`

Tests that installing trie preserves existing MCP servers in the configuration file.

- Creates a `.mcp.json` file with an existing "other" server entry
- Installs trie for claude-code target
- Verifies both "trie" and "other" servers remain in the configuration
- Confirms the operation is recorded as "updated" rather than "created"
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_idempotent_when_unchanged fingerprint=24e0cb1f0131366a118dcb75e676778cb66f4dbd891bf4436d2bc8bd96146a02 body_fp=5371e7966089b74aa43af408cb0a3b6f142b99d12e3eb12d6e4b0879418087a1 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=test-infrastructure -->
## `def test_install_idempotent_when_unchanged(project: Path)`

Verifies that running install twice for the same target produces a "skipped" action on the second run.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_errors_on_unknown_target fingerprint=c1f6d21c077c44f6ca31b1a618e33f1f64a8e4a8b7c7ee59b8de7d502eca0470 body_fp=4736ff62e9e17633282a371112ef9a1717df01c768aee80516a0ec77c0212c42 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
## `def test_install_errors_on_unknown_target(project: Path)`

Verifies that install raises MCPInstallError when given an unknown target name.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_print_only_writes_no_file fingerprint=5f34d3623185276dc469ed875c75be469cd1bfc224527482601d004f1214bb4f body_fp=cf7e9aa19f6a090dc874a27d110a8cf887763fc397bdfa8fb2a3628da9f23b3d source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=test-infrastructure -->
## `def test_install_print_only_writes_no_file(project: Path)`

Verifies install with print_only=True shows preview action without creating config file.

- Tests that `print_only=True` prevents file system writes while still returning a plan
- Confirms the action is marked as "preview" rather than "created"
- Ensures `.mcp.json` remains non-existent after the install operation
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_dry_run_writes_no_file fingerprint=f2b938546f453a63eb32e6747656f09e095bf8bdacefe51e84b35372b7939bff body_fp=cbfce1af6b61475b8d1c402d89ff6e6fd1ffdfa794628784c97b6984edca5897 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=test-infrastructure -->
## `def test_install_dry_run_writes_no_file(project: Path)`

Verifies that dry-run install returns preview action and writes no config file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_opencode_creates_project_config fingerprint=056d1ec0c7977353f4a8cffaff32482702b1f93b8e3613017f92191c1adefcab body_fp=2caca9c402820b219ae01d5fb32be0e01f2a823a35bc96a029cf45b0ca30d469 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
## `def test_install_opencode_creates_project_config(project: Path)`

Tests that installing trie for opencode target creates `opencode.json` with correct structure under `mcp.trie` key.

- Creates `opencode.json` at project root (not `.mcp.json`)
- Uses `mcp` top-level key instead of `mcpServers`
- Sets `type: "local"`, `enabled: true`, and `command` array format
- Omits `cwd` field per opencode's snippet requirements
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_opencode_user_scope_lands_in_config_dir fingerprint=1d03ac3f2f3d2cc7e111ab61962771718ea315388c6e26ef4d5b5b913234a4e6 body_fp=e835c74baa9cbd33dac722ae879e22fa7862280f7df6f4449324fee165ac3d02 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
## `def test_install_opencode_user_scope_lands_in_config_dir( project: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch )`

Tests that opencode user-scope install creates configuration at `~/.config/opencode/opencode.json`.

- Creates fake home directory and patches environment to isolate test
- Verifies install plan creates file at expected user config path
- Confirms generated configuration contains correct MCP server entry with local type
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_opencode_preserves_existing_mcp_servers fingerprint=a5ebe471b22cc0b8e89250528323be69aa94350d8b75831d9e4a84d9c001f615 body_fp=5bdc0b2951d787043051ae5b3f3e58574f8dbd019b8809f22740092cb65adfca source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
## `def test_install_opencode_preserves_existing_mcp_servers(project: Path)`

Verifies that installing trie to opencode.json preserves existing MCP servers and top-level keys.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_opencode_idempotent_when_unchanged fingerprint=4feb7ef3e18d0c41903e35f54d8c15fbe57b3e201600c0b55870bcf0c8f811d8 body_fp=2b3d644a838d760de72b7780dcce08a5970b37c26041acb8b626d5ddb5e37de2 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
## `def test_install_opencode_idempotent_when_unchanged(project: Path)`

Verifies that installing opencode MCP integration twice produces a skipped action on the second run.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_vscode_uses_servers_key fingerprint=12064f01b3a79dc6f332cfc0dde7fb01c28f9c76ed47588c834127f5f5f74b0f body_fp=761c8723b68f5c891c6ad6913c774a9a1a1705c1d42383ca28261ff1ab3c2361 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
## `def test_install_vscode_uses_servers_key(project: Path)`

Verifies that installing trie for VS Code creates a config file using `servers` key instead of `mcpServers`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_errors_on_invalid_json fingerprint=b219580693bbb91025df19bade8031d5b11a5ea8cb7cb36b20c1645e7cd0842e body_fp=a696d32236816483588ea3af56ee8cf608e240ceda0a853178722d91e332671b source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
## `def test_install_errors_on_invalid_json(project: Path)`

Tests that `install` returns an error result when the target config file contains invalid JSON.

- Creates malformed JSON in `.mcp.json` before calling `install`
- Verifies the plan result has `action == "error"` rather than crashing
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_user_scope_writes_to_user_path fingerprint=5f342f1684d327798ed976f2305c907845b83d5f576644da55e91fe72e5f3c04 body_fp=d21c368787bef2fd79af286b4364e9c04c542306134488d4c91da50691e54075 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=test-infrastructure -->
## `def test_install_user_scope_writes_to_user_path( project: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch )`

Tests that user-scope install creates config file under HOME directory.

- Sets fake HOME directory to keep test sandboxed
- Verifies user-scope install writes to `~/.claude.json` instead of project directory
- Confirms trie server entry is properly added to user config
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_skips_target_without_scope fingerprint=42874c537fdf9644872091b02f75cded37910b56a8300572544c3bd9f315d386 body_fp=56b62ec4e77263012b641288596107b8d2fcd3b0e7f88e68c54d310994bc8550 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
## `def test_install_skips_target_without_scope(project: Path)`

Tests that install skips targets when scope is unsupported, verifying VS Code user-scope installation returns "skipped" action with scope-related detail message.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_detect_returns_false_in_clean_environment fingerprint=1c0deba75e86080d128799ac73240d8e3081589f4472276776630717eba7c462 body_fp=97d39006d3e8a470fd7e27b8f1c27fb7601b3ba58ba275f1d6479b8303389acd source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=test-infrastructure -->
## `def test_detect_returns_false_in_clean_environment(monkeypatch: pytest.MonkeyPatch)`

Verifies that target detection returns false when environment paths are redirected to non-existent directories.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_detected_target_slugs_empty_on_clean_environment fingerprint=cfbefa760a9a500cb256056f97002ab110c310f9dfcb61f87dd702512b2c6aaf body_fp=79daab5ba171a4fd75b5b33899758c952d7d500f7f32e8efcb7d79a4b0608239 source_ref=2c8417d0479305ff3cadb92e6ebff569af46dcff role=test -->
## `def test_detected_target_slugs_empty_on_clean_environment(monkeypatch: pytest.MonkeyPatch)`

Assert that `detected_target_slugs` returns an empty list when HOME and PATH point to non-existent locations.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_detected_target_slugs_reports_installed_in_registry_order fingerprint=31e3decb80e20da737fb34a68c5854aadd1939afb814df09b8351fbab433a257 body_fp=44a27908325e12260ce2300b6ab403a05831fd49c9f8083a2f730c3825349048 source_ref=2c8417d0479305ff3cadb92e6ebff569af46dcff role=test -->
## `def test_detected_target_slugs_reports_installed_in_registry_order( monkeypatch: pytest.MonkeyPatch, )`

Verify `detected_target_slugs` returns slugs in registry definition order when multiple targets detect as installed.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_auto_detect_errors_when_nothing_found fingerprint=f729e5cb0970771d53976e18bfd16e7348a9a236597bc29dfa71ac580a755a70 body_fp=7d0b633b2602ff333de6c31177dbeb851d24edb585d01da9a6fa7fd6ff22b464 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
## `def test_install_auto_detect_errors_when_nothing_found( project: Path, monkeypatch: pytest.MonkeyPatch )`

Verifies that `install` raises `MCPInstallError` when auto-detection finds no supported agents in a clean environment.

- Sets fake HOME and empty PATH to simulate environment with no detectable agents
- Calls `install` with `target_names=None` to trigger auto-detection
- Expects `MCPInstallError` with "no agents detected" message
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_all_runs_every_target_in_print_mode fingerprint=b0fda18ed4da73efc289339a12ccb0257ce9b572056669f413bce3f958cecab2 body_fp=d0ce25ae1b740ff902c642bc75b3b2d230a66f527170c344b310c561da1cf254 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
## `def test_install_all_runs_every_target_in_print_mode(project: Path)`

Verifies that `install_all=True` executes against all targets in the registry.

- When combined with `print_only=True`, project-scope targets return "preview" action
- User-scope-only targets return "skipped" action due to scope mismatch
- Validates the plan covers all registered targets without actually writing files
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_install_print_only fingerprint=ff72c235cd8c0a7bd68d24714747272e35a04b8f4dda60b434f7d23c379ca3c9 body_fp=eea0f986b71b695d4ce8a7fb1793c88c635fba0fb4d052da79c528039b44d3d3 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=test-infrastructure -->
## `def test_cli_mcp_install_print_only(project: Path, monkeypatch: pytest.MonkeyPatch)`

Tests that `trie mcp install --print-only` outputs preview information without creating files.

- Verifies CLI exits successfully with target name and serve command in output
- Confirms no actual installation occurs when print-only flag is used
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_install_writes_file fingerprint=cf6045c64a03c2ac5c3023e6a4e3030a819ceecc932e3e4b6a7fd007d299dd70 body_fp=4ee53e02ceed5946b18d8cb7da03afb7ef1172b12bc08c4608fd1071746047f9 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=test-infrastructure -->
## `def test_cli_mcp_install_writes_file(project: Path, monkeypatch: pytest.MonkeyPatch)`

Tests that CLI `trie mcp install --target claude-code` creates `.mcp.json` file and reports success.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_install_unknown_target fingerprint=bce0de12746a6f9f01ff2afd0109dd69569e194e6dc4fc6a0207b585541fee36 body_fp=a77c42f4b90b9ce26eea0192cc52cb5e42be02d75010437f2823a53ffae912b2 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
## `def test_cli_mcp_install_unknown_target(project: Path, monkeypatch: pytest.MonkeyPatch)`

Tests that CLI install command rejects unknown target with exit code 1 and error message.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_install_target_and_all_mutex fingerprint=faca422a774e99a77e55dd846f767a61a0b152766c074a084428d5341d7478f8 body_fp=4b75194d967098e43326e26994fc3b83ea1b2d38184b242d471bff8f0f81699a source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
## `def test_cli_mcp_install_target_and_all_mutex(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verifies that CLI `mcp install` with both `--target` and `--all` flags exits with error code 1 and reports mutual exclusion.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_serve_dispatches_to_run_stdio fingerprint=dc419e9badf8868cb08692fc7c528c6d5b50a9b9dd57c5b724a65a1e645d0c0a body_fp=ee12443a34f5dfe779c59119c210bc501c6d0699fd30fe0bb16a6dc187d2782e source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=test-infrastructure -->
## `def test_cli_mcp_serve_dispatches_to_run_stdio(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verifies that the CLI command `trie mcp serve` calls `run_mcp_stdio` with the resolved project root path.

- Uses monkeypatch to capture the root argument passed to the mocked function
- Asserts successful exit code and correct path resolution
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_no_subcommand_prints_help fingerprint=81a7825c6ac3f78de339c25c6d9c267e2f68655c15bbb250a598119a1b2e1863 body_fp=f3be32e646892ade1d88caf16067981b745ff2b3828c9c8b0d412d6b93cd88cd source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=test-infrastructure -->
## `def test_cli_mcp_no_subcommand_prints_help(project: Path, monkeypatch: pytest.MonkeyPatch)`

Tests that `trie mcp` without subcommands prints help and exits with code 2.

- Mocks `run_mcp_stdio` to verify the server is not started
- Validates help output contains "serve" and "install" subcommands
- Ensures the CLI follows typer's `no_args_is_help` pattern instead of silently starting server
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_removes_trie_entry fingerprint=971ab5611ba1b9b03cc9a128e906cda48f702598abb239b594b68f6d32e1713b body_fp=cb91f1f0e1317ee62232430bed6b602241e3b33849b7f6047d4f8c32ec690809 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
## `def test_uninstall_removes_trie_entry(project: Path)`

Tests that uninstalling removes the trie entry from MCP server configuration while preserving the file structure.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_preserves_other_servers fingerprint=ae273311161d194d8e53473c92efd25ced9713851f0545a9b918c1daa365b628 body_fp=dc6e8a3225e47bb8e5c0ad7a8a0ae3b0210c05263577b3a18fbd1b36c0782eb7 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
## `def test_uninstall_preserves_other_servers(project: Path)`

Tests that `uninstall` removes only the `trie` entry while preserving other MCP servers and unrelated config keys.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_when_not_installed_is_skipped fingerprint=9dedbf216b46a3053f2635c7775ffed45f83087a930b42a000441d970863c7ab body_fp=1314b02625839a43d48b5ba38d4071e8cab4abbd15a24afee6ca8e09b5cc606d source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
## `def test_uninstall_when_not_installed_is_skipped(project: Path)`

Tests that uninstalling from a non-existent config file returns "skipped" action with descriptive detail.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_when_config_has_no_trie_key_is_skipped fingerprint=28657ea793254d5f844f6f8be2888077b3a56faf9e93fb1a78d258a92e67916e body_fp=87b06aa9b44432ca9d7b193f6d515af5627a72e49a39201debff674b9a67b3a1 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
## `def test_uninstall_when_config_has_no_trie_key_is_skipped(project: Path)`

Tests uninstall when config file has no trie entry returns skipped action without modifying file.

- Creates `.mcp.json` with `other-tool` server but no `trie` entry
- Verifies uninstall action is `skipped` with "trie not registered" detail
- Confirms existing server configuration remains unchanged
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_dry_run_does_not_modify_file fingerprint=3b7f689c728aa757b567ae8d16269840a6712f35d0c735c68469b1dd71c1a049 body_fp=912a726fda9ab4b08a0ad92ba45913a249d80795f50071450d537ea047817ca7 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
## `def test_uninstall_dry_run_does_not_modify_file(project: Path)`

Verifies that uninstall with `dry_run=True` returns preview action without modifying the config file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_print_only_does_not_modify_file fingerprint=dfca7d6660914c8fda96ef49d0f05a3754b66ddd1bbeb06c07565d776eb7c792 body_fp=0c6d219081f3985bd4ec17ab9b5673c93be6e3908ca868753109960e7a944d0c source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
## `def test_uninstall_print_only_does_not_modify_file(project: Path)`

Verifies that uninstall with `print_only=True` returns a preview action without modifying the config file.

- Sets up an installed trie configuration first
- Captures config file content before uninstall operation
- Asserts file remains byte-identical after preview-only uninstall
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_all_targets fingerprint=aca9ab8e631abd60e4e2777d62008c2a59f555cdae4bc4a3fb2887c202f9aaf9 body_fp=877c56ad9b58a65416406a48b35e1d5dbb6b8a121a8979fe79fb37b3b1766681 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
## `def test_uninstall_all_targets(project: Path)`

Tests that uninstall with `uninstall_all=True` processes all targets, removing previously installed ones and skipping others.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_unknown_target_raises fingerprint=f78972ed42eae1aa73343ef43a32589addb94dc75f33b040b2ca577f4c6a966b body_fp=15340ad392cb6173e1ac09ac4a5882a85414ba6b5bd7b229b50ec128233dd417 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
## `def test_uninstall_unknown_target_raises()`

Tests that `uninstall` raises `MCPInstallError` when given unknown target names.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_invalid_json_returns_error fingerprint=9854b0b5f0d9c291141ae7c12be25d53f7de5e4f2ae39593dc5256edf94125fb body_fp=4549485d6085b4088dd2d6d8760ec6e6cd5c6ecbb3031afdf9a604e77b3269ca source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
## `def test_uninstall_invalid_json_returns_error(project: Path)`

Verifies that `uninstall` returns an error result when encountering corrupt JSON configuration files instead of crashing.

- Creates malformed JSON in `.mcp.json` config file
- Confirms uninstall operation returns "error" action with descriptive detail
- Verifies corrupt config file remains untouched for manual user repair
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_uninstall_round_trips fingerprint=2b5988bb6d4f64478fb0295c8c127b637f11125efe436a7c8b9f61842cf703c3 body_fp=62353a06f963f29baec063ab99061278b9a0ac6cf446e0603ccb39f7080c123a source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
## `def test_cli_mcp_uninstall_round_trips(project: Path, monkeypatch: pytest.MonkeyPatch)`

Tests end-to-end CLI workflow of installing then uninstalling trie MCP server for claude-code target.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_uninstall_rejects_target_and_all_together fingerprint=d6582c23d9b225cbcba13c6edde6ddd64018fc33cbf9b1b61974285e488ebf74 body_fp=21576a67e5df5f1ad382f423f1fcb4e8770c3b76b268420ccb3ac85520790fd5 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
## `def test_cli_mcp_uninstall_rejects_target_and_all_together( project: Path, monkeypatch: pytest.MonkeyPatch )`

Verifies that CLI `mcp uninstall` rejects `--target` and `--all` flags as mutually exclusive.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_help_lists_uninstall fingerprint=c2c2a3f26f862873bfc6dafb4114a6cfe3d0aa9173f08a8378f2c4ee13e430ef body_fp=da8631d1b37f12a0292b5cf580f15c1d44d870fa0d982992d624a153e6e7e318 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
## `def test_cli_mcp_help_lists_uninstall(project: Path, monkeypatch: pytest.MonkeyPatch)`

Tests that the CLI help screen for `trie mcp` includes the `uninstall` subcommand for discoverability.

- Verifies `trie mcp` exits with code 2 (no-args-is-help behavior)
- Checks "uninstall" appears in help output
<!-- trie:end -->