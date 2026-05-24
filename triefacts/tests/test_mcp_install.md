---
trie_version: 0.1.2
source: tests/test_mcp_install.py
file_fingerprint: 79bfe15932eef28fd8a138aaf00bbdaf80ddd609c19f3439b21c6d503939860b
last_synced_at: '2026-05-23T23:23:12Z'
defines:
- kind: module
  qualified_name: tests/test_mcp_install:__module__
  lines: 1-726
- kind: function
  qualified_name: tests/test_mcp_install:project
  lines: 20-29
- kind: function
  qualified_name: tests/test_mcp_install:test_snippet_uses_serve_subcommand
  lines: 35-39
- kind: function
  qualified_name: tests/test_mcp_install:test_install_claude_code_creates_file
  lines: 45-60
- kind: function
  qualified_name: tests/test_mcp_install:test_install_preserves_other_servers
  lines: 63-77
- kind: function
  qualified_name: tests/test_mcp_install:test_install_idempotent_when_unchanged
  lines: 80-97
- kind: function
  qualified_name: tests/test_mcp_install:test_install_errors_on_unknown_target
  lines: 100-109
- kind: function
  qualified_name: tests/test_mcp_install:test_install_print_only_writes_no_file
  lines: 115-125
- kind: function
  qualified_name: tests/test_mcp_install:test_install_dry_run_writes_no_file
  lines: 128-138
- kind: function
  qualified_name: tests/test_mcp_install:test_install_opencode_creates_project_config
  lines: 144-166
- kind: function
  qualified_name: tests/test_mcp_install:test_install_opencode_user_scope_lands_in_config_dir
  lines: 169-188
- kind: function
  qualified_name: tests/test_mcp_install:test_install_opencode_preserves_existing_mcp_servers
  lines: 191-217
- kind: function
  qualified_name: tests/test_mcp_install:test_install_opencode_idempotent_when_unchanged
  lines: 220-237
- kind: function
  qualified_name: tests/test_mcp_install:test_install_vscode_uses_servers_key
  lines: 243-258
- kind: function
  qualified_name: tests/test_mcp_install:test_install_errors_on_invalid_json
  lines: 264-274
- kind: function
  qualified_name: tests/test_mcp_install:test_install_user_scope_writes_to_user_path
  lines: 280-299
- kind: function
  qualified_name: tests/test_mcp_install:test_install_skips_target_without_scope
  lines: 302-313
- kind: function
  qualified_name: tests/test_mcp_install:test_detect_returns_false_in_clean_environment
  lines: 319-326
- kind: function
  qualified_name: tests/test_mcp_install:test_install_auto_detect_errors_when_nothing_found
  lines: 329-343
- kind: function
  qualified_name: tests/test_mcp_install:test_install_all_runs_every_target_in_print_mode
  lines: 349-366
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_install_print_only
  lines: 372-378
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_install_writes_file
  lines: 381-387
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_install_unknown_target
  lines: 390-395
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_install_target_and_all_mutex
  lines: 398-403
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_serve_dispatches_to_run_stdio
  lines: 406-418
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_no_subcommand_prints_help
  lines: 421-439
- kind: function
  qualified_name: tests/test_mcp_install:test_uninstall_removes_trie_entry
  lines: 449-481
- kind: function
  qualified_name: tests/test_mcp_install:test_uninstall_preserves_other_servers
  lines: 484-518
- kind: function
  qualified_name: tests/test_mcp_install:test_uninstall_when_not_installed_is_skipped
  lines: 521-535
- kind: function
  qualified_name: tests/test_mcp_install:test_uninstall_when_config_has_no_trie_key_is_skipped
  lines: 538-563
- kind: function
  qualified_name: tests/test_mcp_install:test_uninstall_dry_run_does_not_modify_file
  lines: 566-589
- kind: function
  qualified_name: tests/test_mcp_install:test_uninstall_print_only_does_not_modify_file
  lines: 592-615
- kind: function
  qualified_name: tests/test_mcp_install:test_uninstall_all_targets
  lines: 618-648
- kind: function
  qualified_name: tests/test_mcp_install:test_uninstall_unknown_target_raises
  lines: 651-662
- kind: function
  qualified_name: tests/test_mcp_install:test_uninstall_invalid_json_returns_error
  lines: 665-682
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_uninstall_round_trips
  lines: 688-702
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_uninstall_rejects_target_and_all_together
  lines: 705-714
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_help_lists_uninstall
  lines: 717-725
incoming_refs: 0
outgoing_refs: 45
---
<!-- trie:section symbol=tests/test_mcp_install:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=cbc1fe063b37f04f15cf950538ab0dcc0be9f170907458294dfeeda8155be3fe source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `tests/test_mcp_install`

Test suite for `trie.mcp_install` covering install, uninstall, CLI surface, and edge cases.

- `project` fixture: temp dir with a valid `trie.toml`; used by nearly every test.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:project fingerprint=9635d698397eed755ba54f18855a451e5f737f90ab053c81317de51f20a18b4a body_fp=1379bfc073e627515d56672678202ff5dff3e34ae1be17082dbe4b1d6ecf2991 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a `tmp_path` directory with a valid `trie.toml` and returns it as the project root.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_snippet_uses_serve_subcommand fingerprint=64e9dd207621028e9aaaa81e3e2f4ff89f8d2e8def334be47eea06f9eb38a9a0 body_fp=8066ef86e59ace6b39af7c33dae4e91793e002722011ef681b76ee1d52eee8a2 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_snippet_uses_serve_subcommand(project: Path)`

Assert that `trie_server_snippet` returns a snippet with `command="trie"`, `args=["mcp", "serve"]`, and `cwd` set to the resolved project path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_claude_code_creates_file fingerprint=901f2a4de5c763742d248d63f1efe2f94fe89ae5a4547c2d4a1ffbfdd4757c24 body_fp=dfc825b0234fba114950aed659fcaccaa919a26561eb92e64e46b30d37134b8a source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_install_claude_code_creates_file(project: Path)`

Assert that `install` with `target_names=["claude-code"]` creates `.mcp.json` containing a `trie` entry under `mcpServers` with `args == ["mcp", "serve"]`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_preserves_other_servers fingerprint=d7e5f3a30a59855914ceb6300c7973d65f4f9f3052e3289d40988a7fa7a4c2d7 body_fp=94097dd76967763b46172cda29849caf292a8c5f9b596ff21d6b89556a0f944c source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_install_preserves_other_servers(project: Path)`

Assert that installing `claude-code` merges `trie` into an existing `.mcp.json` without removing other servers.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_idempotent_when_unchanged fingerprint=24e0cb1f0131366a118dcb75e676778cb66f4dbd891bf4436d2bc8bd96146a02 body_fp=18d52d9d76be3ded3c18b93770993abe3ea66b65c70a698f26c5a94bb0cc75cb source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_install_idempotent_when_unchanged(project: Path)`

Assert that a second `install` call for an already-configured target returns `"skipped"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_errors_on_unknown_target fingerprint=c1f6d21c077c44f6ca31b1a618e33f1f64a8e4a8b7c7ee59b8de7d502eca0470 body_fp=b2dcd3ffc61d2cee920a192fd961cb360724531929a477b345e33200dded3b67 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_install_errors_on_unknown_target(project: Path)`

Assert that `install` raises `MCPInstallError` matching "unknown target" when given an unrecognised target name.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_print_only_writes_no_file fingerprint=5f34d3623185276dc469ed875c75be469cd1bfc224527482601d004f1214bb4f body_fp=48ca0b0e980ecfd38269dfc4459fc74b5edba1ed3c9150c837f95ad0e678ebbb source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_install_print_only_writes_no_file(project: Path)`

Assert that `install` with `print_only=True` returns a `"preview"` action and writes no config file to disk.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_dry_run_writes_no_file fingerprint=f2b938546f453a63eb32e6747656f09e095bf8bdacefe51e84b35372b7939bff body_fp=ffa99e5b202a4e06865d4f9a5274e6a14751b18003c40eab3465b85f437804d0 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_install_dry_run_writes_no_file(project: Path)`

Assert that `dry_run=True` returns a `"preview"` action without writing `.mcp.json` to disk.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_opencode_creates_project_config fingerprint=056d1ec0c7977353f4a8cffaff32482702b1f93b8e3613017f92191c1adefcab body_fp=bf2c24b609476fdfded9fa60ab4561b20d3ba2638cc75a6668211616d9b9e211 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_install_opencode_creates_project_config(project: Path)`

Assert that installing the `opencode` target at project scope creates `opencode.json` with the correct snippet shape.

- `opencode.json` uses `mcp` key, not `mcpServers`
- Snippet nested at `mcp.trie` with `type: "local"`, `command: ["trie", "mcp", "serve"]`, `enabled: true`
- No `cwd` field present in the opencode snippet
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_opencode_user_scope_lands_in_config_dir fingerprint=1d03ac3f2f3d2cc7e111ab61962771718ea315388c6e26ef4d5b5b913234a4e6 body_fp=4bc97988a38293992d7e6d9f7cf1223effe514d329fc4e53e4cca19ccd0057f2 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_install_opencode_user_scope_lands_in_config_dir(project: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that a user-scope opencode install writes to `~/.config/opencode/opencode.json` with a `local` type snippet.

- `monkeypatch`: redirects `HOME` to a sandboxed temp directory to avoid touching the real filesystem.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_opencode_preserves_existing_mcp_servers fingerprint=a5ebe471b22cc0b8e89250528323be69aa94350d8b75831d9e4a84d9c001f615 body_fp=a059ae4ce3d581a629ef36c31148de6622b5131ccd629bb12262de2072eb2ce1 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_install_opencode_preserves_existing_mcp_servers(project: Path)`

Assert that installing the opencode target merges `trie` into an existing `mcp` block without removing other servers or top-level keys.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_opencode_idempotent_when_unchanged fingerprint=4feb7ef3e18d0c41903e35f54d8c15fbe57b3e201600c0b55870bcf0c8f811d8 body_fp=00efe8b20183a56f060cddeb235cec040e475d6edc342a57a3d1790ea4014d89 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_install_opencode_idempotent_when_unchanged(project: Path)`

Assert that a second `install` call for the `opencode` target returns `skipped` when the config is already up to date.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_vscode_uses_servers_key fingerprint=12064f01b3a79dc6f332cfc0dde7fb01c28f9c76ed47588c834127f5f5f74b0f body_fp=fc02e8ffeb62f38e2a326917f71cfc94211af5a96ab27985bd019a0f22e363fd source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_install_vscode_uses_servers_key(project: Path)`

Assert that a VS Code project-scope install writes `servers` (not `mcpServers`) as the top-level key containing the `trie` entry.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_errors_on_invalid_json fingerprint=b219580693bbb91025df19bade8031d5b11a5ea8cb7cb36b20c1645e7cd0842e body_fp=37a3d8f0f2d98da05263f90f0089254d9c54e4074b9917a3458b434c1a6866d1 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_install_errors_on_invalid_json(project: Path)`

Assert that `install` returns an `error` action result when the target config file contains malformed JSON.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_user_scope_writes_to_user_path fingerprint=5f342f1684d327798ed976f2305c907845b83d5f576644da55e91fe72e5f3c04 body_fp=11f1bff25279145a6120785648bba9bd9f35d51059b61190563bbb64202d3537 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_install_user_scope_writes_to_user_path(project: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that a `user`-scope claude-code install writes `~/.claude.json` under the redirected `HOME`.

- `monkeypatch`: redirects `HOME` to a sandboxed `tmp_path` subdirectory before invoking `install`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_skips_target_without_scope fingerprint=42874c537fdf9644872091b02f75cded37910b56a8300572544c3bd9f315d386 body_fp=154998155b15e41ab24d5cbe5930c2c3949b99aed1062b91bde91b9fc6101230 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_install_skips_target_without_scope(project: Path)`

Assert that `install` skips a target and includes `"scope"` in the detail when the target doesn't support the requested scope.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_detect_returns_false_in_clean_environment fingerprint=1c0deba75e86080d128799ac73240d8e3081589f4472276776630717eba7c462 body_fp=0783995171a410e08c8f2fcca920e3dbdb17169a76feb62a166748c190c2f83a source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_detect_returns_false_in_clean_environment(monkeypatch: pytest.MonkeyPatch)`

Assert that every `TARGETS` entry returns `False` from `detect()` when `HOME` and `PATH` point to non-existent locations.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_auto_detect_errors_when_nothing_found fingerprint=f729e5cb0970771d53976e18bfd16e7348a9a236597bc29dfa71ac580a755a70 body_fp=038f0d5c1e3fdd2f82e1ef9abdadf11eca244ac2add3ef13ac1b007c0218890c source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_install_auto_detect_errors_when_nothing_found(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `install` raises `MCPInstallError` matching "no agents detected" when auto-detection finds no installed targets.

- Redirects `HOME` and `PATH` to non-existent paths to suppress all target detection.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_install_all_runs_every_target_in_print_mode fingerprint=b0fda18ed4da73efc289339a12ccb0257ce9b572056669f413bce3f958cecab2 body_fp=a7bd2550eda9cb8310bea6121b44e87bcfbe58c12f3db5c634057bb38cb0e6dd source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_install_all_runs_every_target_in_print_mode(project: Path)`

Assert that `install_all=True` with `print_only=True` covers every registered target, previewing project-scoped ones and skipping user-scope-only targets.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_install_print_only fingerprint=ff72c235cd8c0a7bd68d24714747272e35a04b8f4dda60b434f7d23c379ca3c9 body_fp=6d0702f8e04ff4364115c8ee24ad893f9abacec73c1c9c05cb45fad645ffa6c5 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_cli_mcp_install_print_only(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie mcp install --target claude-code --print-only` exits 0 and prints the server snippet without writing files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_install_writes_file fingerprint=cf6045c64a03c2ac5c3023e6a4e3030a819ceecc932e3e4b6a7fd007d299dd70 body_fp=6efaadfd7350ca9464ade7304a14e2e1a167e3fdb488b243a430913fe0f33903 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_cli_mcp_install_writes_file(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify that `trie mcp install --target claude-code` creates `.mcp.json` and reports success via the CLI.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_install_unknown_target fingerprint=bce0de12746a6f9f01ff2afd0109dd69569e194e6dc4fc6a0207b585541fee36 body_fp=97a9741854089f151ad7aa9807cd40a64a26e8e43244bbf9b1094d3d5f1dfd2c source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_cli_mcp_install_unknown_target(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie mcp install --target bogus` exits with code 1 and prints "unknown target".
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_install_target_and_all_mutex fingerprint=faca422a774e99a77e55dd846f767a61a0b152766c074a084428d5341d7478f8 body_fp=71fa2fa38607f3915192c6f6d6e65e09632396a2578012935b668b7d58187a16 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_cli_mcp_install_target_and_all_mutex(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that passing `--target` and `--all` together to `trie mcp install` exits with code 1 and reports mutual exclusivity.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_serve_dispatches_to_run_stdio fingerprint=dc419e9badf8868cb08692fc7c528c6d5b50a9b9dd57c5b724a65a1e645d0c0a body_fp=6957fc2f1761e23d3c4cd463ea493c54643ec73d6906d26ae8b3f28c6676c3b2 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_cli_mcp_serve_dispatches_to_run_stdio(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie mcp serve` calls `run_mcp_stdio` with the resolved project root.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_no_subcommand_prints_help fingerprint=81a7825c6ac3f78de339c25c6d9c267e2f68655c15bbb250a598119a1b2e1863 body_fp=e9c10350fb4b534bc267e71a7a582b67ecaf06aaaeadc01cc2b9aac0c171937c source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_cli_mcp_no_subcommand_prints_help(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie mcp` with no subcommand prints help, exits with code 2, and does not start the MCP stdio server.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_removes_trie_entry fingerprint=971ab5611ba1b9b03cc9a128e906cda48f702598abb239b594b68f6d32e1713b body_fp=0a3e23a5ab3d0adf829dd74a41131f48eea4ae84c778dc53a3b57fe31de5df23 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_uninstall_removes_trie_entry(project: Path)`

Install then uninstall claude-code; assert `trie` key is removed and `mcpServers` dropped from `.mcp.json`.

- Result action is `"removed"`, path is `.mcp.json`, and `r.snippet["args"]` is `["mcp", "serve"]`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_preserves_other_servers fingerprint=ae273311161d194d8e53473c92efd25ced9713851f0545a9b918c1daa365b628 body_fp=f688d2762fba158d54b9ed80033ba2b413e399bfc5dc82daf04a0013c71677ea source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_uninstall_preserves_other_servers(project: Path)`

Assert that `uninstall` removes only the `trie` key, leaving sibling MCP servers and unrelated top-level config keys intact.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_when_not_installed_is_skipped fingerprint=9dedbf216b46a3053f2635c7775ffed45f83087a930b42a000441d970863c7ab body_fp=d66a8e8c6a4e4a0f3fafc4d024557a28378e4ba7f006f2fcd299ada3e1b86f11 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_uninstall_when_not_installed_is_skipped(project: Path)`

Assert that `uninstall` returns a `skipped` result with a "no config file" detail when trie was never installed on the target.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_when_config_has_no_trie_key_is_skipped fingerprint=28657ea793254d5f844f6f8be2888077b3a56faf9e93fb1a78d258a92e67916e body_fp=f8e936266c1148e71a548fd187cee1c2bf040eae494e69b8c901dc1697c06ec0 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_uninstall_when_config_has_no_trie_key_is_skipped(project: Path)`

Assert that `uninstall` returns `skipped` and leaves the config file untouched when it exists but contains no `trie` entry.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_dry_run_does_not_modify_file fingerprint=3b7f689c728aa757b567ae8d16269840a6712f35d0c735c68469b1dd71c1a049 body_fp=d8d05ca8f8615d3df0e73133428209130e8630f089b03b1227efb98f1c9dae81 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_uninstall_dry_run_does_not_modify_file(project: Path)`

Assert that `uninstall` with `dry_run=True` returns a `preview` action and leaves the config file byte-identical.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_print_only_does_not_modify_file fingerprint=dfca7d6660914c8fda96ef49d0f05a3754b66ddd1bbeb06c07565d776eb7c792 body_fp=019e9a99cd8c7a4bd5037e9f9adf54f46b7287cbcdccd3dc94dccd5c2d8cd842 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_uninstall_print_only_does_not_modify_file(project: Path)`

Assert that `uninstall` with `print_only=True` returns a `"preview"` action and leaves the config file byte-identical.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_all_targets fingerprint=aca9ab8e631abd60e4e2777d62008c2a59f555cdae4bc4a3fb2887c202f9aaf9 body_fp=ad281b6e6905c7fcd8a51ce2d77d7ee0d3be2cb69cbef430fc42800e5f513e5a source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_uninstall_all_targets(project: Path)`

Verify that `uninstall_all=True` walks every registered target, marking previously-installed ones `removed` and scope-incompatible ones `skipped`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_unknown_target_raises fingerprint=f78972ed42eae1aa73343ef43a32589addb94dc75f33b040b2ca577f4c6a966b body_fp=51e152cf56241894d09d4e1fa45f4965bd836569592cdb1eeedd6eda6cd89895 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_uninstall_unknown_target_raises()`

Assert that `uninstall` raises `MCPInstallError` matching "unknown target" for unrecognised target slugs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_invalid_json_returns_error fingerprint=9854b0b5f0d9c291141ae7c12be25d53f7de5e4f2ae39593dc5256edf94125fb body_fp=779553436500a70b2a0bea372efcab7b7cf31f8c1c77e234990ae73b176ddd3b source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_uninstall_invalid_json_returns_error(project: Path)`

Assert that `uninstall` returns an `error` result for a corrupt config file without modifying or crashing on it.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_uninstall_round_trips fingerprint=2b5988bb6d4f64478fb0295c8c127b637f11125efe436a7c8b9f61842cf703c3 body_fp=ad3ebaa42db1dfba3a033824993421dd3e154ded7aae4767db8f6472080b1036 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_cli_mcp_uninstall_round_trips(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify that `trie mcp install` followed by `trie mcp uninstall` leaves `.mcp.json` free of any `mcpServers` key.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_uninstall_rejects_target_and_all_together fingerprint=d6582c23d9b225cbcba13c6edde6ddd64018fc33cbf9b1b61974285e488ebf74 body_fp=4f6a21ab8f47c020eb98819fe098a4d66c9dc0281b428e9dda8c3452af810867 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_cli_mcp_uninstall_rejects_target_and_all_together(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie mcp uninstall --target <name> --all` exits with code 1 and reports mutual exclusivity.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_help_lists_uninstall fingerprint=c2c2a3f26f862873bfc6dafb4114a6cfe3d0aa9173f08a8378f2c4ee13e430ef body_fp=771d18117d9a060fc71f4e7537c079a75a90efb97a4f41218bf774282aeb9273 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_cli_mcp_help_lists_uninstall(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie mcp` (no subcommand) exits with code 2 and prints `uninstall` in its help output.
<!-- trie:end -->