---
trie_version: 0.1.0
source: tests/test_mcp_install.py
file_fingerprint: 86998d7b7de324f0550cda292e4bea1559cc9ccfc7acbbcbea2f5eb75fd0866f
last_synced_at: '2026-05-16T11:03:39Z'
defines:
- kind: function
  qualified_name: tests/test_mcp_install:project
  lines: 19-28
- kind: function
  qualified_name: tests/test_mcp_install:test_snippet_uses_serve_subcommand
  lines: 34-38
- kind: function
  qualified_name: tests/test_mcp_install:test_install_claude_code_creates_file
  lines: 44-59
- kind: function
  qualified_name: tests/test_mcp_install:test_install_preserves_other_servers
  lines: 62-76
- kind: function
  qualified_name: tests/test_mcp_install:test_install_idempotent_when_unchanged
  lines: 79-96
- kind: function
  qualified_name: tests/test_mcp_install:test_install_errors_on_unknown_target
  lines: 99-108
- kind: function
  qualified_name: tests/test_mcp_install:test_install_print_only_writes_no_file
  lines: 114-124
- kind: function
  qualified_name: tests/test_mcp_install:test_install_dry_run_writes_no_file
  lines: 127-137
- kind: function
  qualified_name: tests/test_mcp_install:test_install_opencode_creates_project_config
  lines: 143-165
- kind: function
  qualified_name: tests/test_mcp_install:test_install_opencode_user_scope_lands_in_config_dir
  lines: 168-187
- kind: function
  qualified_name: tests/test_mcp_install:test_install_opencode_preserves_existing_mcp_servers
  lines: 190-216
- kind: function
  qualified_name: tests/test_mcp_install:test_install_opencode_idempotent_when_unchanged
  lines: 219-236
- kind: function
  qualified_name: tests/test_mcp_install:test_install_vscode_uses_servers_key
  lines: 242-257
- kind: function
  qualified_name: tests/test_mcp_install:test_install_errors_on_invalid_json
  lines: 263-273
- kind: function
  qualified_name: tests/test_mcp_install:test_install_user_scope_writes_to_user_path
  lines: 279-298
- kind: function
  qualified_name: tests/test_mcp_install:test_install_skips_target_without_scope
  lines: 301-312
- kind: function
  qualified_name: tests/test_mcp_install:test_detect_returns_false_in_clean_environment
  lines: 318-325
- kind: function
  qualified_name: tests/test_mcp_install:test_install_auto_detect_errors_when_nothing_found
  lines: 328-342
- kind: function
  qualified_name: tests/test_mcp_install:test_install_all_runs_every_target_in_print_mode
  lines: 348-365
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_install_print_only
  lines: 371-377
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_install_writes_file
  lines: 380-386
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_install_unknown_target
  lines: 389-394
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_install_target_and_all_mutex
  lines: 397-402
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_serve_dispatches_to_run_stdio
  lines: 405-417
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_no_subcommand_prints_help
  lines: 420-438
incoming_refs: 0
outgoing_refs: 19
---
<!-- trie:section symbol=tests/test_mcp_install:project fingerprint=9635d698397eed755ba54f18855a451e5f737f90ab053c81317de51f20a18b4a body_fp=ae09ec600ba8e89e4c44445846e66135344fc4e14a18a9d6fa2dc8e49187f6c0 source_ref=0e5674937bf238506b1820b0bed47b1faea9c679 -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that writes a minimal `trie.toml` into a temp directory and returns it as the project root.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_snippet_uses_serve_subcommand fingerprint=64e9dd207621028e9aaaa81e3e2f4ff89f8d2e8def334be47eea06f9eb38a9a0 body_fp=a81e29cf884f3c61bc7516e098e86b24fbfcc7e73107606bf7173bca3afa8181 source_ref=0e5674937bf238506b1820b0bed47b1faea9c679 -->
## `test_snippet_uses_serve_subcommand(project: Path)`

Assert that `trie_server_snippet` returns a snippet with command `"trie"`, args `["mcp", "serve"]`, and correct `cwd`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_claude_code_creates_file fingerprint=901f2a4de5c763742d248d63f1efe2f94fe89ae5a4547c2d4a1ffbfdd4757c24 body_fp=18a814b1e146e6f882af8d950cd393f209993d91c009d7965ce1fad455472863 source_ref=0e5674937bf238506b1820b0bed47b1faea9c679 -->
## `test_install_claude_code_creates_file(project: Path)`

Assert that installing the `claude-code` target creates `.mcp.json` with a valid `trie` server entry.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_preserves_other_servers fingerprint=d7e5f3a30a59855914ceb6300c7973d65f4f9f3052e3289d40988a7fa7a4c2d7 body_fp=028629911c54b8df8d789ff4f59f83c6b896782f52cbae19152a6218620851fd source_ref=0e5674937bf238506b1820b0bed47b1faea9c679 -->
## `test_install_preserves_other_servers(project: Path)`

Assert that installing the `claude-code` target into an existing `.mcp.json` merges entries without removing pre-existing servers.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_idempotent_when_unchanged fingerprint=24e0cb1f0131366a118dcb75e676778cb66f4dbd891bf4436d2bc8bd96146a02 body_fp=b7367bf9997a498d67934da5f629e4cc26fe4619f2110196e75960d4e5be66f5 source_ref=0e5674937bf238506b1820b0bed47b1faea9c679 -->
## `test_install_idempotent_when_unchanged(project: Path)`

Assert that a second `install` call for the same target returns `"skipped"` when the config is already up to date.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_errors_on_unknown_target fingerprint=c1f6d21c077c44f6ca31b1a618e33f1f64a8e4a8b7c7ee59b8de7d502eca0470 body_fp=3818615400f569daab2782acdf8d83f9bfabaf0de300a905172ed62a378c1e94 source_ref=0e5674937bf238506b1820b0bed47b1faea9c679 -->
## `test_install_errors_on_unknown_target(project: Path)`

Assert that `install` raises `MCPInstallError` with "unknown target" when given an unrecognised target name.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_print_only_writes_no_file fingerprint=5f34d3623185276dc469ed875c75be469cd1bfc224527482601d004f1214bb4f body_fp=bec1377b990e1b84e5721fc6c6a0f09a78d40bef3270a86a45ec78d6978dd42d source_ref=0e5674937bf238506b1820b0bed47b1faea9c679 -->
## `test_install_print_only_writes_no_file(project: Path)`

Assert that `print_only=True` returns a `"preview"` action and writes no file to disk.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_dry_run_writes_no_file fingerprint=f2b938546f453a63eb32e6747656f09e095bf8bdacefe51e84b35372b7939bff body_fp=c2589f43a38a67a0d617d144a20a64efe59269d5d396c459a3093735d0d9d4e8 source_ref=0e5674937bf238506b1820b0bed47b1faea9c679 -->
## `test_install_dry_run_writes_no_file(project: Path)`

Assert that `dry_run=True` returns a `"preview"` action without writing any file to disk.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_vscode_uses_servers_key fingerprint=12064f01b3a79dc6f332cfc0dde7fb01c28f9c76ed47588c834127f5f5f74b0f body_fp=3c9ed3839456207db01948076bae439959a1e6b5f959b9026744f8a8344020d3 source_ref=0e5674937bf238506b1820b0bed47b1faea9c679 -->
## `test_install_vscode_uses_servers_key(project: Path)`

Assert that a VS Code project-scope install writes config under `"servers"`, not `"mcpServers"`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_errors_on_invalid_json fingerprint=b219580693bbb91025df19bade8031d5b11a5ea8cb7cb36b20c1645e7cd0842e body_fp=fd902f9fa9e634691e0b901717ffc7acca3d3c4beb1a5fd72366efd3b5664612 source_ref=0e5674937bf238506b1820b0bed47b1faea9c679 -->
## `test_install_errors_on_invalid_json(project: Path)`

Assert that installing into a config file containing malformed JSON records an `"error"` action rather than raising an exception.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_user_scope_writes_to_user_path fingerprint=5f342f1684d327798ed976f2305c907845b83d5f576644da55e91fe72e5f3c04 body_fp=594dcee05c789fb7821728bb1f37f72c1780a1846657f05d9afabf627682a050 source_ref=0e5674937bf238506b1820b0bed47b1faea9c679 -->
## `test_install_user_scope_writes_to_user_path(project: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that a user-scope install writes `~/.claude.json` under a redirected `HOME`, keeping the test sandboxed.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_skips_target_without_scope fingerprint=42874c537fdf9644872091b02f75cded37910b56a8300572544c3bd9f315d386 body_fp=9607952b6f9aa02e65d52beb96140a73ce463315282c8c8ab2080c084adac29a source_ref=0e5674937bf238506b1820b0bed47b1faea9c679 -->
## `test_install_skips_target_without_scope(project: Path)`

Assert that installing a user-scope-only target (VS Code) with `scope="user"` produces a `"skipped"` result mentioning `"scope"`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_detect_returns_false_in_clean_environment fingerprint=1c0deba75e86080d128799ac73240d8e3081589f4472276776630717eba7c462 body_fp=0783995171a410e08c8f2fcca920e3dbdb17169a76feb62a166748c190c2f83a source_ref=0e5674937bf238506b1820b0bed47b1faea9c679 -->
## `test_detect_returns_false_in_clean_environment(monkeypatch: pytest.MonkeyPatch)`

Assert that every `TARGETS` entry returns `False` from `detect()` when `HOME` and `PATH` point to non-existent locations.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_auto_detect_errors_when_nothing_found fingerprint=f729e5cb0970771d53976e18bfd16e7348a9a236597bc29dfa71ac580a755a70 body_fp=f6e3802d177b5e97acdc6b4ab956bb36a69d360943b951f1e80308f6fe2c2ea2 source_ref=0e5674937bf238506b1820b0bed47b1faea9c679 -->
## `test_install_auto_detect_errors_when_nothing_found(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert `install` raises `MCPInstallError` matching "no agents detected" when auto-detect finds no targets.

- Redirects `HOME` and `PATH` to non-existent locations to suppress all detection.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_all_runs_every_target_in_print_mode fingerprint=b0fda18ed4da73efc289339a12ccb0257ce9b572056669f413bce3f958cecab2 body_fp=292f8c8fa1a99f605ba2b8254366b84565eb138e58b3e58851dd6ee4bf3f2cdf source_ref=7fe9c5365e5d687b3a41f594c3f7556635ef1989 -->
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



<!-- trie:section symbol=tests/test_mcp_install:test_install_opencode_creates_project_config fingerprint=056d1ec0c7977353f4a8cffaff32482702b1f93b8e3613017f92191c1adefcab body_fp=d1cd03c84510c694651f3ff43e12677055423393181fc5825356f31aad60fdad source_ref=7fe9c5365e5d687b3a41f594c3f7556635ef1989 -->
## `test_install_opencode_creates_project_config(project: Path)`

Assert that installing the `opencode` target at project scope creates `opencode.json` with the correct `mcp.trie` snippet shape.

- `type` must be `"local"`, `command` must be `["trie", "mcp", "serve"]`, `enabled` must be `True`.
- `cwd` must be absent from the snippet; `mcpServers` key must not appear at the top level.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_opencode_user_scope_lands_in_config_dir fingerprint=1d03ac3f2f3d2cc7e111ab61962771718ea315388c6e26ef4d5b5b913234a4e6 body_fp=ed4ba128770806b39a36a80369eb89421815c95711021280454ecd5dc87b1d39 source_ref=7fe9c5365e5d687b3a41f594c3f7556635ef1989 -->
## `test_install_opencode_user_scope_lands_in_config_dir(project: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert user-scope opencode install writes to `~/.config/opencode/opencode.json` with correct snippet shape.

- `monkeypatch`: redirects `HOME` to a sandboxed temp directory to avoid touching the real filesystem.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_opencode_preserves_existing_mcp_servers fingerprint=a5ebe471b22cc0b8e89250528323be69aa94350d8b75831d9e4a84d9c001f615 body_fp=675a46580b01da6135620a796d9d0a60d04fe5b4f1b99d7d5e84c2e24463296c source_ref=7fe9c5365e5d687b3a41f594c3f7556635ef1989 -->
## `test_install_opencode_preserves_existing_mcp_servers(project: Path)`

Assert that installing the `opencode` target merges `trie` into an existing `opencode.json` without removing other MCP entries or top-level keys.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_opencode_idempotent_when_unchanged fingerprint=4feb7ef3e18d0c41903e35f54d8c15fbe57b3e201600c0b55870bcf0c8f811d8 body_fp=f33f6092742514251e22730dd1d1c8e87fe4aa8aefe6947742335ad5a64e238d source_ref=7fe9c5365e5d687b3a41f594c3f7556635ef1989 -->
## `test_install_opencode_idempotent_when_unchanged(project: Path)`

Assert that a second `install` call for `opencode` with identical config produces a `"skipped"` action.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_no_subcommand_prints_help fingerprint=81a7825c6ac3f78de339c25c6d9c267e2f68655c15bbb250a598119a1b2e1863 body_fp=5db9770ac1db659588822b63ef4a31ee7deb999131ca2c1394d6b5e7d4409d4c source_ref=7fe9c5365e5d687b3a41f594c3f7556635ef1989 -->
## `test_cli_mcp_no_subcommand_prints_help(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie mcp` with no subcommand prints help, exits with code 2, and never starts the stdio server.
<!-- trie:end -->