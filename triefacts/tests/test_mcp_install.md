---
trie_version: 0.1.2
source: tests/test_mcp_install.py
file_fingerprint: 79bfe15932eef28fd8a138aaf00bbdaf80ddd609c19f3439b21c6d503939860b
last_synced_at: '2026-05-21T16:21:48Z'
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
<!-- trie:section symbol=tests/test_mcp_install:project fingerprint=9635d698397eed755ba54f18855a451e5f737f90ab053c81317de51f20a18b4a body_fp=ae09ec600ba8e89e4c44445846e66135344fc4e14a18a9d6fa2dc8e49187f6c0 source_ref=0e5674937bf238506b1820b0bed47b1faea9c679 -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that writes a minimal `trie.toml` into a temp directory and returns it as the project root.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_snippet_uses_serve_subcommand fingerprint=64e9dd207621028e9aaaa81e3e2f4ff89f8d2e8def334be47eea06f9eb38a9a0 body_fp=a81e29cf884f3c61bc7516e098e86b24fbfcc7e73107606bf7173bca3afa8181 source_ref=1d6bef4bb47a3a1c329ab858e8cb8116db3bbb57 -->
## `test_snippet_uses_serve_subcommand(project: Path)`

Assert that `trie_server_snippet` returns a snippet with command `"trie"`, args `["mcp", "serve"]`, and correct `cwd`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_claude_code_creates_file fingerprint=901f2a4de5c763742d248d63f1efe2f94fe89ae5a4547c2d4a1ffbfdd4757c24 body_fp=18a814b1e146e6f882af8d950cd393f209993d91c009d7965ce1fad455472863 source_ref=1d6bef4bb47a3a1c329ab858e8cb8116db3bbb57 -->
## `test_install_claude_code_creates_file(project: Path)`

Assert that installing the `claude-code` target creates `.mcp.json` with a valid `trie` server entry.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_preserves_other_servers fingerprint=d7e5f3a30a59855914ceb6300c7973d65f4f9f3052e3289d40988a7fa7a4c2d7 body_fp=028629911c54b8df8d789ff4f59f83c6b896782f52cbae19152a6218620851fd source_ref=1d6bef4bb47a3a1c329ab858e8cb8116db3bbb57 -->
## `test_install_preserves_other_servers(project: Path)`

Assert that installing the `claude-code` target into an existing `.mcp.json` merges entries without removing pre-existing servers.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_idempotent_when_unchanged fingerprint=24e0cb1f0131366a118dcb75e676778cb66f4dbd891bf4436d2bc8bd96146a02 body_fp=b7367bf9997a498d67934da5f629e4cc26fe4619f2110196e75960d4e5be66f5 source_ref=1d6bef4bb47a3a1c329ab858e8cb8116db3bbb57 -->
## `test_install_idempotent_when_unchanged(project: Path)`

Assert that a second `install` call for the same target returns `"skipped"` when the config is already up to date.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_errors_on_unknown_target fingerprint=c1f6d21c077c44f6ca31b1a618e33f1f64a8e4a8b7c7ee59b8de7d502eca0470 body_fp=3818615400f569daab2782acdf8d83f9bfabaf0de300a905172ed62a378c1e94 source_ref=1d6bef4bb47a3a1c329ab858e8cb8116db3bbb57 -->
## `test_install_errors_on_unknown_target(project: Path)`

Assert that `install` raises `MCPInstallError` with "unknown target" when given an unrecognised target name.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_print_only_writes_no_file fingerprint=5f34d3623185276dc469ed875c75be469cd1bfc224527482601d004f1214bb4f body_fp=bec1377b990e1b84e5721fc6c6a0f09a78d40bef3270a86a45ec78d6978dd42d source_ref=1d6bef4bb47a3a1c329ab858e8cb8116db3bbb57 -->
## `test_install_print_only_writes_no_file(project: Path)`

Assert that `print_only=True` returns a `"preview"` action and writes no file to disk.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_dry_run_writes_no_file fingerprint=f2b938546f453a63eb32e6747656f09e095bf8bdacefe51e84b35372b7939bff body_fp=c2589f43a38a67a0d617d144a20a64efe59269d5d396c459a3093735d0d9d4e8 source_ref=1d6bef4bb47a3a1c329ab858e8cb8116db3bbb57 -->
## `test_install_dry_run_writes_no_file(project: Path)`

Assert that `dry_run=True` returns a `"preview"` action without writing any file to disk.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_vscode_uses_servers_key fingerprint=12064f01b3a79dc6f332cfc0dde7fb01c28f9c76ed47588c834127f5f5f74b0f body_fp=3c9ed3839456207db01948076bae439959a1e6b5f959b9026744f8a8344020d3 source_ref=1d6bef4bb47a3a1c329ab858e8cb8116db3bbb57 -->
## `test_install_vscode_uses_servers_key(project: Path)`

Assert that a VS Code project-scope install writes config under `"servers"`, not `"mcpServers"`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_errors_on_invalid_json fingerprint=b219580693bbb91025df19bade8031d5b11a5ea8cb7cb36b20c1645e7cd0842e body_fp=fd902f9fa9e634691e0b901717ffc7acca3d3c4beb1a5fd72366efd3b5664612 source_ref=1d6bef4bb47a3a1c329ab858e8cb8116db3bbb57 -->
## `test_install_errors_on_invalid_json(project: Path)`

Assert that installing into a config file containing malformed JSON records an `"error"` action rather than raising an exception.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_user_scope_writes_to_user_path fingerprint=5f342f1684d327798ed976f2305c907845b83d5f576644da55e91fe72e5f3c04 body_fp=594dcee05c789fb7821728bb1f37f72c1780a1846657f05d9afabf627682a050 source_ref=1d6bef4bb47a3a1c329ab858e8cb8116db3bbb57 -->
## `test_install_user_scope_writes_to_user_path(project: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that a user-scope install writes `~/.claude.json` under a redirected `HOME`, keeping the test sandboxed.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_skips_target_without_scope fingerprint=42874c537fdf9644872091b02f75cded37910b56a8300572544c3bd9f315d386 body_fp=9607952b6f9aa02e65d52beb96140a73ce463315282c8c8ab2080c084adac29a source_ref=1d6bef4bb47a3a1c329ab858e8cb8116db3bbb57 -->
## `test_install_skips_target_without_scope(project: Path)`

Assert that installing a user-scope-only target (VS Code) with `scope="user"` produces a `"skipped"` result mentioning `"scope"`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_detect_returns_false_in_clean_environment fingerprint=1c0deba75e86080d128799ac73240d8e3081589f4472276776630717eba7c462 body_fp=0783995171a410e08c8f2fcca920e3dbdb17169a76feb62a166748c190c2f83a source_ref=1d6bef4bb47a3a1c329ab858e8cb8116db3bbb57 -->
## `test_detect_returns_false_in_clean_environment(monkeypatch: pytest.MonkeyPatch)`

Assert that every `TARGETS` entry returns `False` from `detect()` when `HOME` and `PATH` point to non-existent locations.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_auto_detect_errors_when_nothing_found fingerprint=f729e5cb0970771d53976e18bfd16e7348a9a236597bc29dfa71ac580a755a70 body_fp=f6e3802d177b5e97acdc6b4ab956bb36a69d360943b951f1e80308f6fe2c2ea2 source_ref=1d6bef4bb47a3a1c329ab858e8cb8116db3bbb57 -->
## `test_install_auto_detect_errors_when_nothing_found(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert `install` raises `MCPInstallError` matching "no agents detected" when auto-detect finds no targets.

- Redirects `HOME` and `PATH` to non-existent locations to suppress all detection.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_all_runs_every_target_in_print_mode fingerprint=b0fda18ed4da73efc289339a12ccb0257ce9b572056669f413bce3f958cecab2 body_fp=292f8c8fa1a99f605ba2b8254366b84565eb138e58b3e58851dd6ee4bf3f2cdf source_ref=1d6bef4bb47a3a1c329ab858e8cb8116db3bbb57 -->
## `test_install_all_runs_every_target_in_print_mode(project: Path)`

Assert that `install_all=True` with `print_only=True` covers every target, previewing project-scope targets and skipping user-scope-only ones.

- `claude-desktop` and `windsurf` expect `"skipped"` as user-scope-only targets.
- `claude-code`, `vscode`, and `opencode` expect `"preview"` as project-scope-compatible targets.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_install_print_only fingerprint=ff72c235cd8c0a7bd68d24714747272e35a04b8f4dda60b434f7d23c379ca3c9 body_fp=f179440ddf3c33531cf2925bcc8d86e394f910e8445386cae4b63aea651f24fb source_ref=0e5674937bf238506b1820b0bed47b1faea9c679 -->
## `test_cli_mcp_install_print_only(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie mcp install --target claude-code --print-only` exits 0 and prints the snippet without writing any file.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_install_writes_file fingerprint=cf6045c64a03c2ac5c3023e6a4e3030a819ceecc932e3e4b6a7fd007d299dd70 body_fp=8909e5f4accc0ed35d24a5df10193613e624090ef3e2b68f1d3f40376b19737a source_ref=0e5674937bf238506b1820b0bed47b1faea9c679 -->
## `test_cli_mcp_install_writes_file(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify that `trie mcp install --target claude-code` creates `.mcp.json` and exits with code 0.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_install_unknown_target fingerprint=bce0de12746a6f9f01ff2afd0109dd69569e194e6dc4fc6a0207b585541fee36 body_fp=97a9741854089f151ad7aa9807cd40a64a26e8e43244bbf9b1094d3d5f1dfd2c source_ref=0e5674937bf238506b1820b0bed47b1faea9c679 -->
## `test_cli_mcp_install_unknown_target(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie mcp install --target bogus` exits with code 1 and prints "unknown target".
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_install_target_and_all_mutex fingerprint=faca422a774e99a77e55dd846f767a61a0b152766c074a084428d5341d7478f8 body_fp=7254f7dd0bd817d5a9fea749504f3e117f3c489eb177d71c0086f2cddf1d2cb9 source_ref=0e5674937bf238506b1820b0bed47b1faea9c679 -->
## `test_cli_mcp_install_target_and_all_mutex(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that passing both `--target` and `--all` to `trie mcp install` exits with code 1 and reports mutual exclusivity.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_serve_dispatches_to_run_stdio fingerprint=dc419e9badf8868cb08692fc7c528c6d5b50a9b9dd57c5b724a65a1e645d0c0a body_fp=a4123213fa207b4c9b04e6293d6cf9cdeb25c88cf65d3386c04c97c97abca60f source_ref=0e5674937bf238506b1820b0bed47b1faea9c679 -->
## `test_cli_mcp_serve_dispatches_to_run_stdio(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie mcp serve` invokes `run_mcp_stdio` with the resolved project root.
<!-- trie:end -->



<!-- trie:section symbol=tests/test_mcp_install:test_install_opencode_creates_project_config fingerprint=056d1ec0c7977353f4a8cffaff32482702b1f93b8e3613017f92191c1adefcab body_fp=d1cd03c84510c694651f3ff43e12677055423393181fc5825356f31aad60fdad source_ref=1d6bef4bb47a3a1c329ab858e8cb8116db3bbb57 -->
## `test_install_opencode_creates_project_config(project: Path)`

Assert that installing the `opencode` target at project scope creates `opencode.json` with the correct `mcp.trie` snippet shape.

- `type` must be `"local"`, `command` must be `["trie", "mcp", "serve"]`, `enabled` must be `True`.
- `cwd` must be absent from the snippet; `mcpServers` key must not appear at the top level.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_opencode_user_scope_lands_in_config_dir fingerprint=1d03ac3f2f3d2cc7e111ab61962771718ea315388c6e26ef4d5b5b913234a4e6 body_fp=ed4ba128770806b39a36a80369eb89421815c95711021280454ecd5dc87b1d39 source_ref=1d6bef4bb47a3a1c329ab858e8cb8116db3bbb57 -->
## `test_install_opencode_user_scope_lands_in_config_dir(project: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert user-scope opencode install writes to `~/.config/opencode/opencode.json` with correct snippet shape.

- `monkeypatch`: redirects `HOME` to a sandboxed temp directory to avoid touching the real filesystem.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_opencode_preserves_existing_mcp_servers fingerprint=a5ebe471b22cc0b8e89250528323be69aa94350d8b75831d9e4a84d9c001f615 body_fp=675a46580b01da6135620a796d9d0a60d04fe5b4f1b99d7d5e84c2e24463296c source_ref=1d6bef4bb47a3a1c329ab858e8cb8116db3bbb57 -->
## `test_install_opencode_preserves_existing_mcp_servers(project: Path)`

Assert that installing the `opencode` target merges `trie` into an existing `opencode.json` without removing other MCP entries or top-level keys.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_opencode_idempotent_when_unchanged fingerprint=4feb7ef3e18d0c41903e35f54d8c15fbe57b3e201600c0b55870bcf0c8f811d8 body_fp=f33f6092742514251e22730dd1d1c8e87fe4aa8aefe6947742335ad5a64e238d source_ref=1d6bef4bb47a3a1c329ab858e8cb8116db3bbb57 -->
## `test_install_opencode_idempotent_when_unchanged(project: Path)`

Assert that a second `install` call for `opencode` with identical config produces a `"skipped"` action.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_no_subcommand_prints_help fingerprint=81a7825c6ac3f78de339c25c6d9c267e2f68655c15bbb250a598119a1b2e1863 body_fp=5db9770ac1db659588822b63ef4a31ee7deb999131ca2c1394d6b5e7d4409d4c source_ref=7fe9c5365e5d687b3a41f594c3f7556635ef1989 -->
## `test_cli_mcp_no_subcommand_prints_help(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie mcp` with no subcommand prints help, exits with code 2, and never starts the stdio server.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=4005c813074c6a647868a1eed12d50119c28a56192fe19f9ed2e4e91868f9a9f source_ref=fecdf0b15acb6369d3974e674cd692dff8469777 -->
## `tests/test_mcp_install`

Integration and unit tests for the `mcp_install` module and its CLI surface.

- Covers `install()` correctness, idempotency, dry-run, scope routing, and per-target config shapes.
- Exercises CLI commands `mcp install` and `mcp serve` via Typer's `CliRunner`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_removes_trie_entry fingerprint=971ab5611ba1b9b03cc9a128e906cda48f702598abb239b594b68f6d32e1713b body_fp=80415f11377c9f8cca19a434dd64789d16b8eaed4de2da4054e4db0d31680760 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_uninstall_removes_trie_entry(project: Path)`

Install then uninstall claude-code, asserting the `trie` key is removed from `.mcp.json` while the file remains valid JSON.

- `r.snippet["args"]` must equal `["mcp", "serve"]` — the removed snippet is returned for audit.
- `mcpServers` key dropped entirely when emptied, not left as `{}`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_preserves_other_servers fingerprint=ae273311161d194d8e53473c92efd25ced9713851f0545a9b918c1daa365b628 body_fp=70658bc801b0d8bd20e448a1dd036a30f902042c807a588f801c352efc2b9f11 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_uninstall_preserves_other_servers(project: Path)`

Verify that uninstalling trie removes only the `trie` key, leaving other MCP servers and top-level config keys intact.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_when_not_installed_is_skipped fingerprint=9dedbf216b46a3053f2635c7775ffed45f83087a930b42a000441d970863c7ab body_fp=4662bf3c558d411b88dbe7edd14336734c2ec4685da99d6fb75f45ebc62ce1be source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_uninstall_when_not_installed_is_skipped(project: Path)`

Assert that uninstalling from a target with no config file yields a `skipped` result with a descriptive detail.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_when_config_has_no_trie_key_is_skipped fingerprint=28657ea793254d5f844f6f8be2888077b3a56faf9e93fb1a78d258a92e67916e body_fp=17782150bdab72c1b5c1acc0334c21d2630aa79aaa2e47c2f16f7b2545078b3e source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_uninstall_when_config_has_no_trie_key_is_skipped(project: Path)`

Assert that uninstalling from a config file that contains other servers but no `trie` entry returns `skipped` and leaves the file untouched.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_dry_run_does_not_modify_file fingerprint=3b7f689c728aa757b567ae8d16269840a6712f35d0c735c68469b1dd71c1a049 body_fp=72c56f1db4850fe242d9e08b7aa1a05c2021fb1be7ab34cf4462cecb33f01285 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_uninstall_dry_run_does_not_modify_file(project: Path)`

Assert that `uninstall` with `dry_run=True` returns a `"preview"` action and leaves the config file byte-identical to its pre-call state.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_print_only_does_not_modify_file fingerprint=dfca7d6660914c8fda96ef49d0f05a3754b66ddd1bbeb06c07565d776eb7c792 body_fp=29aea948a963094d5c034710fef824eda275cdb0c46d80ca674c9071c55312e3 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_uninstall_print_only_does_not_modify_file(project: Path)`

Assert that `uninstall` with `print_only=True` returns a `preview` action and leaves the config file byte-identical to its pre-call state.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_all_targets fingerprint=aca9ab8e631abd60e4e2777d62008c2a59f555cdae4bc4a3fb2887c202f9aaf9 body_fp=c2f37e5ef274896d4e861f2e3e4d60a488f5b2cab4480fa2eaf2601ba6e96e56 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_uninstall_all_targets(project: Path)`

Verify that `uninstall_all=True` removes all previously installed targets and skips unsupported-scope targets.

- `claude-code` and `opencode` are pre-installed; both must return `"removed"`.
- `claude-desktop` supports only user scope; must return `"skipped"`.
- All keys in `TARGETS` must appear in the plan results.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_unknown_target_raises fingerprint=f78972ed42eae1aa73343ef43a32589addb94dc75f33b040b2ca577f4c6a966b body_fp=c4d843901ed2f544c4e6aba9c1aa685fd79533c3709799733855e9fc075fa3a6 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_uninstall_unknown_target_raises()`

Assert that `uninstall` raises `MCPInstallError` matching "unknown target" for an unrecognised target slug.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_uninstall_invalid_json_returns_error fingerprint=9854b0b5f0d9c291141ae7c12be25d53f7de5e4f2ae39593dc5256edf94125fb body_fp=55496de846d3b1814071df78bf6e03e6ad95121ba4e4a77cf7bc7c74b0b867ef source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_uninstall_invalid_json_returns_error(project: Path)`

Assert that a corrupt config file produces an `error` result without crashing or modifying the file.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_uninstall_round_trips fingerprint=2b5988bb6d4f64478fb0295c8c127b637f11125efe436a7c8b9f61842cf703c3 body_fp=194d326f11a3b530c47039315ff0b349f49c01c6e9f468edff45c863ed7ad88f source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_cli_mcp_uninstall_round_trips(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify that `trie mcp install` followed by `trie mcp uninstall` leaves `.mcp.json` with no `mcpServers` key.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_uninstall_rejects_target_and_all_together fingerprint=d6582c23d9b225cbcba13c6edde6ddd64018fc33cbf9b1b61974285e488ebf74 body_fp=779c35fba69b758f66d8b649ac499c50f19740eaabc15b5e99d93a2d0b9d200b source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_cli_mcp_uninstall_rejects_target_and_all_together(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie mcp uninstall --target <name> --all` exits with code 1 and reports "mutually exclusive".
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_help_lists_uninstall fingerprint=c2c2a3f26f862873bfc6dafb4114a6cfe3d0aa9173f08a8378f2c4ee13e430ef body_fp=bd3227abfb0e5ceafdf5ed8362353120cc77abfe507e9c2538468d57b28daad2 source_ref=e661d455f96b2f16fd9464529e313e3f1c9ca66f -->
## `test_cli_mcp_help_lists_uninstall(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie mcp` (no subcommand) prints help text containing `"uninstall"` and exits with code 2.
<!-- trie:end -->