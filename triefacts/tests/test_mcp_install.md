---
trie_version: 0.1.5
source: tests/test_mcp_install.py
file_fingerprint: 29be6cb897bb91f1cc5fb997df8e2fe3a95fc94825c147f3ee09245c304d5545
last_synced_at: '2026-06-06T13:21:53Z'
defines:
- kind: module
  qualified_name: tests/test_mcp_install:__module__
  lines: 1-734
- kind: function
  qualified_name: tests/test_mcp_install:project
  lines: 20-37
- kind: function
  qualified_name: tests/test_mcp_install:test_snippet_uses_serve_subcommand
  lines: 43-47
- kind: function
  qualified_name: tests/test_mcp_install:test_install_claude_code_creates_file
  lines: 53-68
- kind: function
  qualified_name: tests/test_mcp_install:test_install_preserves_other_servers
  lines: 71-85
- kind: function
  qualified_name: tests/test_mcp_install:test_install_idempotent_when_unchanged
  lines: 88-105
- kind: function
  qualified_name: tests/test_mcp_install:test_install_errors_on_unknown_target
  lines: 108-117
- kind: function
  qualified_name: tests/test_mcp_install:test_install_print_only_writes_no_file
  lines: 123-133
- kind: function
  qualified_name: tests/test_mcp_install:test_install_dry_run_writes_no_file
  lines: 136-146
- kind: function
  qualified_name: tests/test_mcp_install:test_install_opencode_creates_project_config
  lines: 152-174
- kind: function
  qualified_name: tests/test_mcp_install:test_install_opencode_user_scope_lands_in_config_dir
  lines: 177-196
- kind: function
  qualified_name: tests/test_mcp_install:test_install_opencode_preserves_existing_mcp_servers
  lines: 199-225
- kind: function
  qualified_name: tests/test_mcp_install:test_install_opencode_idempotent_when_unchanged
  lines: 228-245
- kind: function
  qualified_name: tests/test_mcp_install:test_install_vscode_uses_servers_key
  lines: 251-266
- kind: function
  qualified_name: tests/test_mcp_install:test_install_errors_on_invalid_json
  lines: 272-282
- kind: function
  qualified_name: tests/test_mcp_install:test_install_user_scope_writes_to_user_path
  lines: 288-307
- kind: function
  qualified_name: tests/test_mcp_install:test_install_skips_target_without_scope
  lines: 310-321
- kind: function
  qualified_name: tests/test_mcp_install:test_detect_returns_false_in_clean_environment
  lines: 327-334
- kind: function
  qualified_name: tests/test_mcp_install:test_install_auto_detect_errors_when_nothing_found
  lines: 337-351
- kind: function
  qualified_name: tests/test_mcp_install:test_install_all_runs_every_target_in_print_mode
  lines: 357-374
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_install_print_only
  lines: 380-386
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_install_writes_file
  lines: 389-395
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_install_unknown_target
  lines: 398-403
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_install_target_and_all_mutex
  lines: 406-411
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_serve_dispatches_to_run_stdio
  lines: 414-426
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_no_subcommand_prints_help
  lines: 429-447
- kind: function
  qualified_name: tests/test_mcp_install:test_uninstall_removes_trie_entry
  lines: 457-489
- kind: function
  qualified_name: tests/test_mcp_install:test_uninstall_preserves_other_servers
  lines: 492-526
- kind: function
  qualified_name: tests/test_mcp_install:test_uninstall_when_not_installed_is_skipped
  lines: 529-543
- kind: function
  qualified_name: tests/test_mcp_install:test_uninstall_when_config_has_no_trie_key_is_skipped
  lines: 546-571
- kind: function
  qualified_name: tests/test_mcp_install:test_uninstall_dry_run_does_not_modify_file
  lines: 574-597
- kind: function
  qualified_name: tests/test_mcp_install:test_uninstall_print_only_does_not_modify_file
  lines: 600-623
- kind: function
  qualified_name: tests/test_mcp_install:test_uninstall_all_targets
  lines: 626-656
- kind: function
  qualified_name: tests/test_mcp_install:test_uninstall_unknown_target_raises
  lines: 659-670
- kind: function
  qualified_name: tests/test_mcp_install:test_uninstall_invalid_json_returns_error
  lines: 673-690
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_uninstall_round_trips
  lines: 696-710
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_uninstall_rejects_target_and_all_together
  lines: 713-722
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_help_lists_uninstall
  lines: 725-733
incoming_refs: 0
outgoing_refs: 45
---
<!-- trie:section symbol=tests/test_mcp_install:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=f3ba8b193c3bc167fe88b8b7ccb2dbf3a5dd7805b8f071b8ba3950dd88b759fa source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=test-infrastructure -->
Tests MCP installation and uninstallation functionality across different AI coding agents and scopes.

- Tests install/uninstall operations for Claude Code, VS Code, OpenCode, and other targets
- Verifies configuration file management, JSON preservation, and idempotent operations  
- Covers CLI commands, error handling, dry-run modes, and auto-detection
- Tests both project-scope and user-scope installation patterns
- Validates round-trip install/uninstall cycles preserve other MCP servers
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:project fingerprint=ec0dcdc7ce6b4eb60414b372c10e3ddd78937efff6c97a9c42895523ab41b485 body_fp=4b6d05aaedb8e0324a98f5e1dae4521711f4e48a175b00ca2901aa0e252bd63f source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=test-infrastructure -->
Creates a temporary project directory with a pre-configured `trie.toml` file for testing MCP installation functionality.

- **tmp_path**: pytest's temporary directory fixture
- **yields**: path to the temporary project directory containing the config file
- **cleanup**: removes any leaked `.mcp.json` or `.claude` files from current/home directories
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_snippet_uses_serve_subcommand fingerprint=64e9dd207621028e9aaaa81e3e2f4ff89f8d2e8def334be47eea06f9eb38a9a0 body_fp=a2f2af6bf970d6a4487cab5c0254071c21a5092facbd090e3e8cc0deffc6c7db source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=test-infrastructure -->
Verifies that `trie_server_snippet` generates correct MCP server configuration with command "trie", args ["mcp", "serve"], and project directory as cwd.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_claude_code_creates_file fingerprint=901f2a4de5c763742d248d63f1efe2f94fe89ae5a4547c2d4a1ffbfdd4757c24 body_fp=fc6caf9a1dd5f6e41a06be9a304d841244f386b821b232b10286221a7bda3a5e source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
Tests that installing trie for claude-code target creates .mcp.json with correct server configuration.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_preserves_other_servers fingerprint=d7e5f3a30a59855914ceb6300c7973d65f4f9f3052e3289d40988a7fa7a4c2d7 body_fp=b1051516debfe2b85237b5b04603db55a748135ac98db6464161c5c290ef821d source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
Verifies that MCP install preserves existing server configurations alongside the new trie entry.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_idempotent_when_unchanged fingerprint=24e0cb1f0131366a118dcb75e676778cb66f4dbd891bf4436d2bc8bd96146a02 body_fp=9f4e07cdf0fcac20c86ae42d0bc545a6549502d9ca8669cbb8aeef9985b42902 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
Verifies that installing the same target twice returns a "skipped" action when no changes are needed.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_errors_on_unknown_target fingerprint=c1f6d21c077c44f6ca31b1a618e33f1f64a8e4a8b7c7ee59b8de7d502eca0470 body_fp=f67f2dd1fa67a28c6d7e38d4b79a8105181e19a8c2f402db97e4604b55ffb0dc source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=test-infrastructure -->
Verifies that `install()` raises `MCPInstallError` when given an unrecognized target name.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_print_only_writes_no_file fingerprint=5f34d3623185276dc469ed875c75be469cd1bfc224527482601d004f1214bb4f body_fp=a6c77860308c6906b4dec8f9eff1536d2928e681914c4ad830cd2db424711435 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
Verifies that install with print_only=True returns a preview action without creating configuration files.

- Calls install with print_only=True and confirms no .mcp.json file is written to disk
- Asserts the result action is "preview" rather than "created" or "updated"
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_dry_run_writes_no_file fingerprint=f2b938546f453a63eb32e6747656f09e095bf8bdacefe51e84b35372b7939bff body_fp=67d962834a8b0f2b2be569ffb80be16aeb6c6d5da7ab9957da25a6266d591871 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
Verifies that install with `dry_run=True` returns a preview action without creating any files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_opencode_creates_project_config fingerprint=056d1ec0c7977353f4a8cffaff32482702b1f93b8e3613017f92191c1adefcab body_fp=ea554a5af0ae3243d360c0aee0137c853163099f7e7479e5e27788d18ea35bd8 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
Tests that installing the opencode target creates `opencode.json` with trie MCP server configuration under `mcp.trie` key.

- Verifies opencode uses `mcp` key instead of `mcpServers` 
- Checks trie entry has `type: "local"` and `enabled: true`
- Confirms `cwd` field is absent from opencode configuration format
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_opencode_user_scope_lands_in_config_dir fingerprint=1d03ac3f2f3d2cc7e111ab61962771718ea315388c6e26ef4d5b5b913234a4e6 body_fp=73e34c44797eebbeb74ee124f3c230196aa7d808b3f68dbcf9801651b2db20a1 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
Tests that user-scope opencode installation creates config file at `~/.config/opencode/opencode.json`.

- Mocks HOME directory to sandbox the test
- Verifies config file lands in the standard opencode user config location
- Confirms the MCP entry has `type: "local"` as expected for opencode format
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_opencode_preserves_existing_mcp_servers fingerprint=a5ebe471b22cc0b8e89250528323be69aa94350d8b75831d9e4a84d9c001f615 body_fp=6809f40675f0374b0f1ebb1af5aa6ad5edb02a7161551fb8cf77a4bc3bbd2077 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
Tests that `install` for opencode target preserves existing MCP servers when updating configuration.

- Creates existing opencode.json with context7 server and schema URL
- Verifies install action is "updated" rather than "created"
- Confirms both trie and context7 servers exist in final config
- Ensures non-mcp keys like $schema survive the update
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_opencode_idempotent_when_unchanged fingerprint=4feb7ef3e18d0c41903e35f54d8c15fbe57b3e201600c0b55870bcf0c8f811d8 body_fp=2c19c751bad793804b7127a7100fdcd6426bcb81e401e646b78523b3aef38a3e source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
Tests that opencode installation is idempotent by installing twice and verifying the second installation returns "skipped" action.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_vscode_uses_servers_key fingerprint=12064f01b3a79dc6f332cfc0dde7fb01c28f9c76ed47588c834127f5f5f74b0f body_fp=2a95fca61e9e21e90b922fb71d230fdd362e810115a733a3d17173569df5c205 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=test-infrastructure -->
Tests that VS Code MCP installation uses `servers` key instead of `mcpServers` in configuration JSON.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_errors_on_invalid_json fingerprint=b219580693bbb91025df19bade8031d5b11a5ea8cb7cb36b20c1645e7cd0842e body_fp=018353d5ae5d7aa09764fe8e9788061d43d38014ab028e357936588120852f59 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
Verifies install handles malformed JSON in existing config files by returning an error action.

- Creates invalid JSON in `.mcp.json` before attempting installation
- Confirms install plan returns "error" action rather than crashing
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_user_scope_writes_to_user_path fingerprint=5f342f1684d327798ed976f2305c907845b83d5f576644da55e91fe72e5f3c04 body_fp=ed899013cf6f0e4c47339e25d1b09b17606edbbed59e06ea4252c295e331532b source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
Tests that user-scope install writes to the user's home directory configuration file.

• Redirects HOME to a temporary directory to sandbox the test
• Verifies the installation creates `.claude.json` in the fake home directory
• Confirms the generated config contains the trie MCP server entry
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_skips_target_without_scope fingerprint=42874c537fdf9644872091b02f75cded37910b56a8300572544c3bd9f315d386 body_fp=de060cdd290d090bc5305ed3641b343c18d162677b2dd9b94e09d7cfeeda1e7f source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
Tests that install skips targets that don't support the requested scope with appropriate detail.

- Tests VS Code target with user scope (unsupported) gets "skipped" action
- Verifies result detail mentions "scope" to explain why it was skipped
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_detect_returns_false_in_clean_environment fingerprint=1c0deba75e86080d128799ac73240d8e3081589f4472276776630717eba7c462 body_fp=e8eafdc18c902703ce0449cbf5b56c32ec413b8111de1d3024dfb65d31f50133 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
Tests that all MCP targets return `False` from their `detect()` method when run in a clean environment with no installations present.

- Redirects `HOME` and `PATH` to non-existent directories to simulate clean system
- Asserts `detect()` returns `False` for every target in the registry
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_auto_detect_errors_when_nothing_found fingerprint=f729e5cb0970771d53976e18bfd16e7348a9a236597bc29dfa71ac580a755a70 body_fp=763a1573bda83e7fc7ac5124c585657f44bef4b6d94169d31417071410c2f67e source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=test-infrastructure -->
Tests that auto-detection raises MCPInstallError when no agent targets are found in clean environment.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_all_runs_every_target_in_print_mode fingerprint=b0fda18ed4da73efc289339a12ccb0257ce9b572056669f413bce3f958cecab2 body_fp=26743cb50a6b2a677e4c540da21ff8c6def8642e2dc91c5aabc9cbdf3e701194 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
Verifies that `install_all=True` with `print_only=True` attempts every target, previewing project-scope targets and skipping user-scope-only targets.

- Returns preview action for claude-code, vscode, opencode targets
- Returns skipped action for claude-desktop, windsurf (user-scope only)
- Confirms all registered targets are processed
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_install_print_only fingerprint=ff72c235cd8c0a7bd68d24714747272e35a04b8f4dda60b434f7d23c379ca3c9 body_fp=a8cda1f42ef3c218f637c07715257db3fbd486a8521ae62d7a9069471cf755fb source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=test-infrastructure -->
Tests that `trie mcp install --print-only` exits successfully and outputs preview content without creating files.

- Verifies exit code 0
- Checks output contains target name "Claude Code" and command fragments "mcp", "serve"
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_install_writes_file fingerprint=cf6045c64a03c2ac5c3023e6a4e3030a819ceecc932e3e4b6a7fd007d299dd70 body_fp=6b085e83c52b8cd5288c4c0a40ff212f444fd078b741fcbb849ab972ec74e949 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
Verifies that `trie mcp install --target claude-code` creates the `.mcp.json` configuration file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_install_unknown_target fingerprint=bce0de12746a6f9f01ff2afd0109dd69569e194e6dc4fc6a0207b585541fee36 body_fp=99a1e4c7dd45eb0b366a93d08e16a4f162dd4798663294f9524b3f022568c088 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=test-infrastructure -->
Tests that CLI `mcp install` with unknown target exits non-zero with error message.

- `project`: Test fixture providing temporary project directory with trie.toml
- `monkeypatch`: pytest fixture for modifying environment during test
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_install_target_and_all_mutex fingerprint=faca422a774e99a77e55dd846f767a61a0b152766c074a084428d5341d7478f8 body_fp=c472057163cb2ea92718feece3da89acddb4c6812ef7347a6e4df01f5b173194 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
Tests that `trie mcp install` rejects `--target` and `--all` flags when used together.

- Verifies CLI exits with code 1 and reports "mutually exclusive" error
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_serve_dispatches_to_run_stdio fingerprint=dc419e9badf8868cb08692fc7c528c6d5b50a9b9dd57c5b724a65a1e645d0c0a body_fp=013e6f3070bc2dd3d14664d26b60a9aca89e254b64072e1d9d8f2e3c1d533baf source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=test-infrastructure -->
Verifies that `trie mcp serve` CLI command correctly dispatches to `run_mcp_stdio` with resolved project root.

- Mocks `run_mcp_stdio` to capture the root path argument
- Asserts the CLI exits successfully and passes the expected project path
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_no_subcommand_prints_help fingerprint=81a7825c6ac3f78de339c25c6d9c267e2f68655c15bbb250a598119a1b2e1863 body_fp=498d59ef18f835520dd43e78dc6586a0c186a2527528da0b2f5275517b8cf6db source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=test-infrastructure -->
Tests that `trie mcp` without subcommand prints help and exits with code 2, avoiding silent server startup.

- Mocks `run_mcp_stdio` to capture if server starts unexpectedly
- Verifies help text mentions "serve" and "install" subcommands  
- Confirms server function is never called when no subcommand given
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_removes_trie_entry fingerprint=971ab5611ba1b9b03cc9a128e906cda48f702598abb239b594b68f6d32e1713b body_fp=47b5387b60f90f257121a1ebfb1304a52ac420388eb0ccb894eaaa8ac8ec9e60 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
Verifies that uninstall correctly removes the `trie` entry from MCP configuration while preserving the config file structure.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_preserves_other_servers fingerprint=ae273311161d194d8e53473c92efd25ced9713851f0545a9b918c1daa365b628 body_fp=e97a1b80840971c32a07674a9ed418fc69d7d1302e0babf39842a24809ed84e1 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=test-infrastructure -->
Tests that uninstall removes only the trie entry while preserving other MCP servers and top-level config keys.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_when_not_installed_is_skipped fingerprint=9dedbf216b46a3053f2635c7775ffed45f83087a930b42a000441d970863c7ab body_fp=862e6ea3fd33e61c52c19130021cf52c5303a012ad36cbaa5aa391301839362a source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
Verifies uninstall skips gracefully when trie was never registered for the target.

- Tests uninstall with no existing config file returns action "skipped"
- Asserts detail message mentions "no config file" for clear user feedback
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_when_config_has_no_trie_key_is_skipped fingerprint=28657ea793254d5f844f6f8be2888077b3a56faf9e93fb1a78d258a92e67916e body_fp=902aa5580325d57fa47b5b574dfcb15bed4cded2a49573f20c7a76cdd7ebb172 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=test-infrastructure -->
Tests that uninstalling trie from a config file without a trie entry skips the operation and preserves other servers.

- Creates `.mcp.json` with `other-tool` server but no `trie` entry
- Verifies uninstall returns `skipped` action with "trie not registered" detail
- Confirms the existing `other-tool` configuration remains untouched
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_dry_run_does_not_modify_file fingerprint=3b7f689c728aa757b567ae8d16269840a6712f35d0c735c68469b1dd71c1a049 body_fp=47cc9d5cad35909993a7f5c74e598a3b98534c7e7652b664b2b963dcff31b923 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
Verifies that uninstall dry-run returns preview action without modifying the config file.

- Installs trie for claude-code, captures config content, runs uninstall with dry_run=True
- Asserts result action is "preview" and file content remains byte-identical
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_print_only_does_not_modify_file fingerprint=dfca7d6660914c8fda96ef49d0f05a3754b66ddd1bbeb06c07565d776eb7c792 body_fp=afb2a4378d6fe638289a73cc284fbe255e2b983ea13bf3571dcef3f7194093e8 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
Tests that uninstall with `--print-only` flag returns preview action without modifying config file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_all_targets fingerprint=aca9ab8e631abd60e4e2777d62008c2a59f555cdae4bc4a3fb2887c202f9aaf9 body_fp=1b08ef7af089b60498cffacbb0a9f962cf2ac81f6a62e115c4e84979a2d5e5a3 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
Verifies that `uninstall` with `uninstall_all=True` walks every target in the registry and removes only previously installed ones.

- Installs trie for `claude-code` and `opencode` targets, then uninstalls all targets
- Asserts that previously installed targets return `removed` action
- Asserts that targets not supporting project scope return `skipped` action
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_unknown_target_raises fingerprint=f78972ed42eae1aa73343ef43a32589addb94dc75f33b040b2ca577f4c6a966b body_fp=de1e2d75e4e873c8fdf9d139d9fac8ed41c0814b3a74d5e22f13447046f89052 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=test-infrastructure -->
Verifies `uninstall` raises `MCPInstallError` when given an unknown target name instead of silently skipping.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_invalid_json_returns_error fingerprint=9854b0b5f0d9c291141ae7c12be25d53f7de5e4f2ae39593dc5256edf94125fb body_fp=10cc788f20f2e4193e0c012dbf8690f4c39f76df47a93271d715fd3d48a0cfb5 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=agent-integration -->
Tests that uninstall gracefully handles corrupt JSON config files by returning error status without modifying the file.

- Creates invalid JSON in `.mcp.json` then calls uninstall on `claude-code` target
- Verifies result action is `error` with appropriate detail message
- Confirms the corrupt config file remains unchanged for manual repair
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_uninstall_round_trips fingerprint=2b5988bb6d4f64478fb0295c8c127b637f11125efe436a7c8b9f61842cf703c3 body_fp=4610a863298e5d1b65654829f6b614e191ef973a91445761f899c7101d7e9241 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=test-infrastructure -->
Tests that installing and uninstalling trie via CLI commands returns the config file to its original state.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_uninstall_rejects_target_and_all_together fingerprint=d6582c23d9b225cbcba13c6edde6ddd64018fc33cbf9b1b61974285e488ebf74 body_fp=7ddeea0f977510ec1a1d7e1b4eb2cfbd4311dd5bfdc7cf24cc1a7a59cf11927b source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=test-infrastructure -->
Verifies that `trie mcp uninstall` rejects the combination of `--target` and `--all` flags.

- Expects exit code 1 and "mutually exclusive" error message
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_help_lists_uninstall fingerprint=c2c2a3f26f862873bfc6dafb4114a6cfe3d0aa9173f08a8378f2c4ee13e430ef body_fp=c65432971742dbc1af12f3e64fe3c569b8e0f00108940177f960d088097f48c9 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a role=test-infrastructure -->
Verifies that `trie mcp` help screen mentions uninstall command for discoverability.

- Invokes CLI with no subcommand to trigger help display
- Asserts exit code 2 (typer's no-args-is-help behavior)  
- Confirms "uninstall" appears in help output
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=747a97780bb1505eb138bdc4cf2d7bae011ace0fb3b41d24ee8fcae769a4012c source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Comprehensive test suite for MCP installation and uninstallation functionality across different AI agent targets.

- Tests installation for Claude Code, opencode, VS Code, and other AI agents
- Validates configuration file creation, updates, and preservation of existing servers  
- Covers project and user scope installations with proper path resolution
- Tests CLI commands for install/uninstall with various flags and error conditions
- Verifies dry-run, print-only, and auto-detection modes work correctly
- Ensures idempotent operations and proper error handling for malformed configs
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:project fingerprint=ec0dcdc7ce6b4eb60414b372c10e3ddd78937efff6c97a9c42895523ab41b485 body_fp=0c8144475e981c1d2c871b03d5d190a97bdebcdd6dacd4a026c8018615febf93 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Creates temporary project directory with trie.toml configuration file and cleans up MCP installation artifacts after test completion.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_snippet_uses_serve_subcommand fingerprint=64e9dd207621028e9aaaa81e3e2f4ff89f8d2e8def334be47eea06f9eb38a9a0 body_fp=152c070889bbe42c44c4ab8601247396b8fad99a4df566a2ab04165237948c8f source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Tests that `trie_server_snippet` generates command configuration with "trie" command, ["mcp", "serve"] args, and resolved project path as working directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_claude_code_creates_file fingerprint=901f2a4de5c763742d248d63f1efe2f94fe89ae5a4547c2d4a1ffbfdd4757c24 body_fp=c9ca26972659e26a870f3f949836ec918d506952f60b01e581b84215071bebd9 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Tests that installing the claude-code target creates a `.mcp.json` file with proper trie server configuration.

- Verifies plan contains one result with "created" action
- Confirms file written to project root with correct path
- Validates JSON structure contains trie entry under mcpServers with correct args
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_preserves_other_servers fingerprint=d7e5f3a30a59855914ceb6300c7973d65f4f9f3052e3289d40988a7fa7a4c2d7 body_fp=92a27440812741b2b8ff321ccdc80aab2bb6fa00dbd0d820cb744c506489b89d source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Tests that installing trie preserves existing MCP servers in the configuration file.

- Creates a `.mcp.json` file with an existing "other" server entry
- Installs trie for claude-code target
- Verifies both "trie" and "other" servers remain in the configuration
- Confirms the operation is recorded as "updated" rather than "created"
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_idempotent_when_unchanged fingerprint=24e0cb1f0131366a118dcb75e676778cb66f4dbd891bf4436d2bc8bd96146a02 body_fp=45cb640b9ce722a4dbe54cbd6b5ccf395e9d0e33d37000f75caf320f9dce387b source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Verifies that running install twice for the same target produces a "skipped" action on the second run.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_errors_on_unknown_target fingerprint=c1f6d21c077c44f6ca31b1a618e33f1f64a8e4a8b7c7ee59b8de7d502eca0470 body_fp=f062923734a711ae11f86c4e8f2aaa95c58a400bdc12d949ab6187ceb046f292 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Verifies that install raises MCPInstallError when given an unknown target name.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_print_only_writes_no_file fingerprint=5f34d3623185276dc469ed875c75be469cd1bfc224527482601d004f1214bb4f body_fp=d5306d81e75fd61bdafbca30791378b760d7c55df1c5e2cc150b6cae550da9cc source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Verifies install with print_only=True shows preview action without creating config file.

- Tests that `print_only=True` prevents file system writes while still returning a plan
- Confirms the action is marked as "preview" rather than "created"
- Ensures `.mcp.json` remains non-existent after the install operation
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_dry_run_writes_no_file fingerprint=f2b938546f453a63eb32e6747656f09e095bf8bdacefe51e84b35372b7939bff body_fp=e8613d5c19691f6633c1c542f2994c48af96f3c1d8495c2cbedab6848309ffb3 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Verifies that dry-run install returns preview action and writes no config file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_opencode_creates_project_config fingerprint=056d1ec0c7977353f4a8cffaff32482702b1f93b8e3613017f92191c1adefcab body_fp=e6d19de615a5c207df0b8fb24a03b8d0b1e2072995a32c3228f60b1e98b44f84 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Tests that installing trie for opencode target creates `opencode.json` with correct structure under `mcp.trie` key.

- Creates `opencode.json` at project root (not `.mcp.json`)
- Uses `mcp` top-level key instead of `mcpServers`
- Sets `type: "local"`, `enabled: true`, and `command` array format
- Omits `cwd` field per opencode's snippet requirements
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_opencode_user_scope_lands_in_config_dir fingerprint=1d03ac3f2f3d2cc7e111ab61962771718ea315388c6e26ef4d5b5b913234a4e6 body_fp=a0d92b8e1754262b4670e07e0ba08935e532f05c22c08422f4db94d84b1defe5 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Tests that opencode user-scope install creates configuration at `~/.config/opencode/opencode.json`.

- Creates fake home directory and patches environment to isolate test
- Verifies install plan creates file at expected user config path
- Confirms generated configuration contains correct MCP server entry with local type
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_opencode_preserves_existing_mcp_servers fingerprint=a5ebe471b22cc0b8e89250528323be69aa94350d8b75831d9e4a84d9c001f615 body_fp=e8f9d8b5905ce0aff8c0515901ce2efc5292b377c7ed6c2f3c12ea0402c389da source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Verifies that installing trie to opencode.json preserves existing MCP servers and top-level keys.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_opencode_idempotent_when_unchanged fingerprint=4feb7ef3e18d0c41903e35f54d8c15fbe57b3e201600c0b55870bcf0c8f811d8 body_fp=382929c7211d26d3bce4ef05bd159e3dec711ccf9a432d33ce98f4ebbae39b07 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Verifies that installing opencode MCP integration twice produces a skipped action on the second run.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_vscode_uses_servers_key fingerprint=12064f01b3a79dc6f332cfc0dde7fb01c28f9c76ed47588c834127f5f5f74b0f body_fp=5b66af02f4226c6b2b715ca0809f58395932f4cc36f544347eb2faa348c2e4b3 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Verifies that installing trie for VS Code creates a config file using `servers` key instead of `mcpServers`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_errors_on_invalid_json fingerprint=b219580693bbb91025df19bade8031d5b11a5ea8cb7cb36b20c1645e7cd0842e body_fp=8ec7b49ab5ffe4d080d10227aaeac28795441b247ca0ad0d07d408e2c2f4be2d source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Tests that `install` returns an error result when the target config file contains invalid JSON.

- Creates malformed JSON in `.mcp.json` before calling `install`
- Verifies the plan result has `action == "error"` rather than crashing
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_user_scope_writes_to_user_path fingerprint=5f342f1684d327798ed976f2305c907845b83d5f576644da55e91fe72e5f3c04 body_fp=189b4145b0f4905fab6c063f64a724f97959918b6331b7ec44510d91a3c87c66 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Tests that user-scope install creates config file under HOME directory.

- Sets fake HOME directory to keep test sandboxed
- Verifies user-scope install writes to `~/.claude.json` instead of project directory
- Confirms trie server entry is properly added to user config
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_skips_target_without_scope fingerprint=42874c537fdf9644872091b02f75cded37910b56a8300572544c3bd9f315d386 body_fp=e65d9dabde5514a528adf3fa44750d718da810a35cad334b64a872c7b1b913ff source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Tests that install skips targets when scope is unsupported, verifying VS Code user-scope installation returns "skipped" action with scope-related detail message.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_detect_returns_false_in_clean_environment fingerprint=1c0deba75e86080d128799ac73240d8e3081589f4472276776630717eba7c462 body_fp=718a298985c098dd0a5076812606c3540906d95321cb7cbd95b3c1c3bb0e42b9 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Verifies that target detection returns false when environment paths are redirected to non-existent directories.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_auto_detect_errors_when_nothing_found fingerprint=f729e5cb0970771d53976e18bfd16e7348a9a236597bc29dfa71ac580a755a70 body_fp=86bde68143a8eb68428e95b73a2efcc538f5d3d09caf866a563a7777569363e2 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Verifies that `install` raises `MCPInstallError` when auto-detection finds no supported agents in a clean environment.

- Sets fake HOME and empty PATH to simulate environment with no detectable agents
- Calls `install` with `target_names=None` to trigger auto-detection
- Expects `MCPInstallError` with "no agents detected" message
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_all_runs_every_target_in_print_mode fingerprint=b0fda18ed4da73efc289339a12ccb0257ce9b572056669f413bce3f958cecab2 body_fp=9f28da20c5cc197edd559f35e55d1511500b582700345b3a1e0b740353d3ef26 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Verifies that `install_all=True` executes against all targets in the registry.

- When combined with `print_only=True`, project-scope targets return "preview" action
- User-scope-only targets return "skipped" action due to scope mismatch
- Validates the plan covers all registered targets without actually writing files
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_install_print_only fingerprint=ff72c235cd8c0a7bd68d24714747272e35a04b8f4dda60b434f7d23c379ca3c9 body_fp=93acbe2be3a2bf16e3710d104bdcb6d7f63461fe5ef53f3b6d17148c91e82415 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Tests that `trie mcp install --print-only` outputs preview information without creating files.

- Verifies CLI exits successfully with target name and serve command in output
- Confirms no actual installation occurs when print-only flag is used
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_install_writes_file fingerprint=cf6045c64a03c2ac5c3023e6a4e3030a819ceecc932e3e4b6a7fd007d299dd70 body_fp=13fb8a6f1aba7c91963d946771804e6352de68ba6651c5116029a83635f1a343 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Tests that CLI `trie mcp install --target claude-code` creates `.mcp.json` file and reports success.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_install_unknown_target fingerprint=bce0de12746a6f9f01ff2afd0109dd69569e194e6dc4fc6a0207b585541fee36 body_fp=fec47749e8501cc4fde7184470450da8e83838cee202ecb6f3bfeef95eee4a56 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Tests that CLI install command rejects unknown target with exit code 1 and error message.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_install_target_and_all_mutex fingerprint=faca422a774e99a77e55dd846f767a61a0b152766c074a084428d5341d7478f8 body_fp=e63a4527ba1bb32a808087c1b2e16684510965893aa9d2ae9a792de1647a6c2e source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Verifies that CLI `mcp install` with both `--target` and `--all` flags exits with error code 1 and reports mutual exclusion.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_serve_dispatches_to_run_stdio fingerprint=dc419e9badf8868cb08692fc7c528c6d5b50a9b9dd57c5b724a65a1e645d0c0a body_fp=bd8fb65f8db14443a90266c361aba662aff5bfec9ef60ad686648b255542f47b source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Verifies that the CLI command `trie mcp serve` calls `run_mcp_stdio` with the resolved project root path.

- Uses monkeypatch to capture the root argument passed to the mocked function
- Asserts successful exit code and correct path resolution
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_no_subcommand_prints_help fingerprint=81a7825c6ac3f78de339c25c6d9c267e2f68655c15bbb250a598119a1b2e1863 body_fp=c321abb314620b2cc2fd75d5b73f08ea5f0da191361cb2f3b63255a61f93814e source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Tests that `trie mcp` without subcommands prints help and exits with code 2.

- Mocks `run_mcp_stdio` to verify the server is not started
- Validates help output contains "serve" and "install" subcommands
- Ensures the CLI follows typer's `no_args_is_help` pattern instead of silently starting server
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_removes_trie_entry fingerprint=971ab5611ba1b9b03cc9a128e906cda48f702598abb239b594b68f6d32e1713b body_fp=0fab9e54039409e9c18fcd61c55bcb30fac037df7a32ae305ff88edabd903b6b source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Tests that uninstalling removes the trie entry from MCP server configuration while preserving the file structure.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_preserves_other_servers fingerprint=ae273311161d194d8e53473c92efd25ced9713851f0545a9b918c1daa365b628 body_fp=b05c2da4e458ad512617445a8cd98cb0a85ec00375cb3ce96637fddc67c10265 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Tests that `uninstall` removes only the `trie` entry while preserving other MCP servers and unrelated config keys.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_when_not_installed_is_skipped fingerprint=9dedbf216b46a3053f2635c7775ffed45f83087a930b42a000441d970863c7ab body_fp=1c771af3f8b746531cb13719248364cef904bbb040c20d4cad1f8ec7a58df5af source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Tests that uninstalling from a non-existent config file returns "skipped" action with descriptive detail.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_when_config_has_no_trie_key_is_skipped fingerprint=28657ea793254d5f844f6f8be2888077b3a56faf9e93fb1a78d258a92e67916e body_fp=8926a4954ff9f71cab2e98dd2f62f5bf83e954c92422b1ae82d9f22aa5e7b759 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Tests uninstall when config file has no trie entry returns skipped action without modifying file.

- Creates `.mcp.json` with `other-tool` server but no `trie` entry
- Verifies uninstall action is `skipped` with "trie not registered" detail
- Confirms existing server configuration remains unchanged
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_dry_run_does_not_modify_file fingerprint=3b7f689c728aa757b567ae8d16269840a6712f35d0c735c68469b1dd71c1a049 body_fp=08641d0d65e99fa7e5bdb712fbc11ff89c083b49ea32a033cd8a805e593f2068 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Verifies that uninstall with `dry_run=True` returns preview action without modifying the config file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_print_only_does_not_modify_file fingerprint=dfca7d6660914c8fda96ef49d0f05a3754b66ddd1bbeb06c07565d776eb7c792 body_fp=cf1f4ac1f56b2da8d47c9552d91ac705f5e898b1fe78de6009e157dcd5571db4 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Verifies that uninstall with `print_only=True` returns a preview action without modifying the config file.

- Sets up an installed trie configuration first
- Captures config file content before uninstall operation
- Asserts file remains byte-identical after preview-only uninstall
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_all_targets fingerprint=aca9ab8e631abd60e4e2777d62008c2a59f555cdae4bc4a3fb2887c202f9aaf9 body_fp=6a4b09d983c18200b9af845cef7e91a598276590e5f4a4805c95af89b96c5661 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Tests that uninstall with `uninstall_all=True` processes all targets, removing previously installed ones and skipping others.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_unknown_target_raises fingerprint=f78972ed42eae1aa73343ef43a32589addb94dc75f33b040b2ca577f4c6a966b body_fp=0f07a56643362915b9cecda0f1714180e8fdcfab49b4dfd9530f13f34591dfdf source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Tests that `uninstall` raises `MCPInstallError` when given unknown target names.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_invalid_json_returns_error fingerprint=9854b0b5f0d9c291141ae7c12be25d53f7de5e4f2ae39593dc5256edf94125fb body_fp=c81d81415fe74b0af0c3ca8bd0beb611ebb77ef9031af0afbc3d9f816dcba46b source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Verifies that `uninstall` returns an error result when encountering corrupt JSON configuration files instead of crashing.

- Creates malformed JSON in `.mcp.json` config file
- Confirms uninstall operation returns "error" action with descriptive detail
- Verifies corrupt config file remains untouched for manual user repair
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_uninstall_round_trips fingerprint=2b5988bb6d4f64478fb0295c8c127b637f11125efe436a7c8b9f61842cf703c3 body_fp=55cac742ee3fb9b9191e29ec3f78deb880a421604a47dc9abb7d277fb07c2178 source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Tests end-to-end CLI workflow of installing then uninstalling trie MCP server for claude-code target.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_uninstall_rejects_target_and_all_together fingerprint=d6582c23d9b225cbcba13c6edde6ddd64018fc33cbf9b1b61974285e488ebf74 body_fp=9455efca161b4fa1591a76430741522b9f270161e72a0e9223ed81895082839d source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Verifies that CLI `mcp uninstall` rejects `--target` and `--all` flags as mutually exclusive.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_help_lists_uninstall fingerprint=c2c2a3f26f862873bfc6dafb4114a6cfe3d0aa9173f08a8378f2c4ee13e430ef body_fp=c0791b69f27b060d482615167953b2efb50ee405bacf536ce989d661e9750c1a source_ref=a2a263825d8bc473d9aedf29ca944244e117391a -->
Tests that the CLI help screen for `trie mcp` includes the `uninstall` subcommand for discoverability.

- Verifies `trie mcp` exits with code 2 (no-args-is-help behavior)
- Checks "uninstall" appears in help output
<!-- trie:end -->