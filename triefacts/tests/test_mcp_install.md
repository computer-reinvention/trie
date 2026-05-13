---
trie_version: 0.1.0
source: tests/test_mcp_install.py
file_fingerprint: 185cb2e15fa149dd3eadd42decf008cb10ef4e4447cdaf95772914d9c51dff97
last_synced_at: '2026-05-12T18:20:09Z'
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
  qualified_name: tests/test_mcp_install:test_install_vscode_uses_servers_key
  lines: 143-158
- kind: function
  qualified_name: tests/test_mcp_install:test_install_errors_on_invalid_json
  lines: 164-174
- kind: function
  qualified_name: tests/test_mcp_install:test_install_user_scope_writes_to_user_path
  lines: 180-199
- kind: function
  qualified_name: tests/test_mcp_install:test_install_skips_target_without_scope
  lines: 202-213
- kind: function
  qualified_name: tests/test_mcp_install:test_detect_returns_false_in_clean_environment
  lines: 219-226
- kind: function
  qualified_name: tests/test_mcp_install:test_install_auto_detect_errors_when_nothing_found
  lines: 229-243
- kind: function
  qualified_name: tests/test_mcp_install:test_install_all_runs_every_target_in_print_mode
  lines: 249-264
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_install_print_only
  lines: 270-276
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_install_writes_file
  lines: 279-285
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_install_unknown_target
  lines: 288-293
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_install_target_and_all_mutex
  lines: 296-301
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_serve_dispatches_to_run_stdio
  lines: 304-316
- kind: function
  qualified_name: tests/test_mcp_install:test_cli_mcp_no_subcommand_runs_serve
  lines: 319-332
incoming_refs: 0
outgoing_refs: 15
---
<!-- trie:section symbol=tests/test_mcp_install:project fingerprint=9635d698397eed755ba54f18855a451e5f737f90ab053c81317de51f20a18b4a body_fp=97558e7606dfae8de95eb6909a584192855b3697f2a1196102e4169fb66c6bfb -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that writes a minimal `trie.toml` into `tmp_path` and returns it as the project root.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_snippet_uses_serve_subcommand fingerprint=64e9dd207621028e9aaaa81e3e2f4ff89f8d2e8def334be47eea06f9eb38a9a0 body_fp=a81e29cf884f3c61bc7516e098e86b24fbfcc7e73107606bf7173bca3afa8181 -->
## `test_snippet_uses_serve_subcommand(project: Path)`

Assert that `trie_server_snippet` returns a snippet with command `"trie"`, args `["mcp", "serve"]`, and correct `cwd`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_claude_code_creates_file fingerprint=901f2a4de5c763742d248d63f1efe2f94fe89ae5a4547c2d4a1ffbfdd4757c24 body_fp=e632cc4793a5ad74bd26b3167d56069a29b12c4cc8801895065cc686b1d93b2c -->
## `test_install_claude_code_creates_file(project: Path)`

Assert that installing the `claude-code` target creates `.mcp.json` with the correct `trie` server entry.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_preserves_other_servers fingerprint=d7e5f3a30a59855914ceb6300c7973d65f4f9f3052e3289d40988a7fa7a4c2d7 body_fp=556988107d1ec741890dd856333d047b788aba7d65de7329fcc27d0830fc5743 -->
## `test_install_preserves_other_servers(project: Path)`

Verify that installing the `trie` server into an existing `.mcp.json` retains pre-existing server entries and marks the result as `"updated"`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_idempotent_when_unchanged fingerprint=24e0cb1f0131366a118dcb75e676778cb66f4dbd891bf4436d2bc8bd96146a02 body_fp=7ff91425acfeba52da75a70f24ebab8783eb1987fc879f55c4f9b0a0f71b00a0 -->
## `test_install_idempotent_when_unchanged(project: Path)`

Assert that a second identical install on an unchanged target returns `action == "skipped"`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_errors_on_unknown_target fingerprint=c1f6d21c077c44f6ca31b1a618e33f1f64a8e4a8b7c7ee59b8de7d502eca0470 body_fp=7f0fdaac27c6209731b5224ae41b115e650b0440b2f53bea0124a8006c337a57 -->
## `test_install_errors_on_unknown_target(project: Path)`

Assert that `install` raises `MCPInstallError` matching "unknown target" for an unrecognised target name.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_print_only_writes_no_file fingerprint=5f34d3623185276dc469ed875c75be469cd1bfc224527482601d004f1214bb4f body_fp=3365ca3a0a36ee3bf46cb4ba991ff83a7aca531095daf2161946ca419a1cfe78 -->
## `test_install_print_only_writes_no_file(project: Path)`

Assert that `print_only=True` produces a `"preview"` action and writes no file to disk.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_dry_run_writes_no_file fingerprint=f2b938546f453a63eb32e6747656f09e095bf8bdacefe51e84b35372b7939bff body_fp=e71def27926745022d772072fcbbb1bd156dd01846b918392f24cd11fa0fef18 -->
## `test_install_dry_run_writes_no_file(project: Path)`

Assert that `dry_run=True` produces a `"preview"` action without writing any file to disk.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_vscode_uses_servers_key fingerprint=12064f01b3a79dc6f332cfc0dde7fb01c28f9c76ed47588c834127f5f5f74b0f body_fp=3c9ed3839456207db01948076bae439959a1e6b5f959b9026744f8a8344020d3 -->
## `test_install_vscode_uses_servers_key(project: Path)`

Assert that a VS Code project-scope install writes config under `"servers"`, not `"mcpServers"`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_errors_on_invalid_json fingerprint=b219580693bbb91025df19bade8031d5b11a5ea8cb7cb36b20c1645e7cd0842e body_fp=b3d156ae399c46b65f34cae9671fc7e4ab6be329891f4db565391881a7b56175 -->
## `test_install_errors_on_invalid_json(project: Path)`

Assert that `install` returns an `"error"` action when the target config file contains malformed JSON.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_user_scope_writes_to_user_path fingerprint=5f342f1684d327798ed976f2305c907845b83d5f576644da55e91fe72e5f3c04 body_fp=c3f785662218ad641e950204c2c60a85a1d3ecde7587f5348fe1a9921ae7dee6 -->
## `test_install_user_scope_writes_to_user_path(project: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that a user-scope install writes to `~/.claude.json` under a redirected `HOME`.

- `monkeypatch`: redirects `HOME` to a sandboxed directory to avoid touching the real home.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_skips_target_without_scope fingerprint=42874c537fdf9644872091b02f75cded37910b56a8300572544c3bd9f315d386 body_fp=c475227f1a8f5ee518a729ffca8b8ac24d1faaf01d03b327ffc694e1eea32d6f -->
## `test_install_skips_target_without_scope(project: Path)`

Assert that installing a scope-incompatible target (VS Code, project-only) with `scope="user"` produces a `"skipped"` result with `"scope"` in the detail message.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_detect_returns_false_in_clean_environment fingerprint=1c0deba75e86080d128799ac73240d8e3081589f4472276776630717eba7c462 body_fp=1faf953398e7130480c93790d0c13d0c26d4cc1993aca562b70b1e06de5b256c -->
## `test_detect_returns_false_in_clean_environment(monkeypatch: pytest.MonkeyPatch)`

Assert that every registered `TARGETS` entry returns `False` from `detect()` when `HOME` and `PATH` point to non-existent locations.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_auto_detect_errors_when_nothing_found fingerprint=f729e5cb0970771d53976e18bfd16e7348a9a236597bc29dfa71ac580a755a70 body_fp=5402f3479ee9729b3168c73711186c29e71601f1af3f5dc94866ff1714b90f33 -->
## `test_install_auto_detect_errors_when_nothing_found(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert `install` raises `MCPInstallError` matching "no agents detected" when auto-detect finds nothing.

- Redirects `HOME` and `PATH` to non-existent paths to suppress all agent detection.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_install_all_runs_every_target_in_print_mode fingerprint=34698c279db160b45ff5a07c148efb263e5deacecc3f46de20426de713de0179 body_fp=d41e220c6cdeeab1e6d6d92d47d09fb646ae71baa0194784fc80c9bb699aa49c -->
## `test_install_all_runs_every_target_in_print_mode(project: Path)`

Assert that `install_all=True` with `print_only=True` emits one result per target, previewing supported scopes and skipping user-scope-only targets.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_install_print_only fingerprint=ff72c235cd8c0a7bd68d24714747272e35a04b8f4dda60b434f7d23c379ca3c9 body_fp=f179440ddf3c33531cf2925bcc8d86e394f910e8445386cae4b63aea651f24fb -->
## `test_cli_mcp_install_print_only(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie mcp install --target claude-code --print-only` exits 0 and prints the snippet without writing any file.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_install_writes_file fingerprint=cf6045c64a03c2ac5c3023e6a4e3030a819ceecc932e3e4b6a7fd007d299dd70 body_fp=358089be101c23f1704a60b0b2f5e99aa4c356f042d5e5d5eaeab04656cdc258 -->
## `test_cli_mcp_install_writes_file(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify that `trie mcp install --target claude-code` creates `.mcp.json` and exits 0.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_install_unknown_target fingerprint=bce0de12746a6f9f01ff2afd0109dd69569e194e6dc4fc6a0207b585541fee36 body_fp=e922ee99d90c0485355eeba505354ba97356ccc55ea9e1c2c5d59de18cac324d -->
## `test_cli_mcp_install_unknown_target(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert the CLI exits with code 1 and reports "unknown target" for an unrecognised `--target` value.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_install_target_and_all_mutex fingerprint=faca422a774e99a77e55dd846f767a61a0b152766c074a084428d5341d7478f8 body_fp=7254f7dd0bd817d5a9fea749504f3e117f3c489eb177d71c0086f2cddf1d2cb9 -->
## `test_cli_mcp_install_target_and_all_mutex(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that passing both `--target` and `--all` to `trie mcp install` exits with code 1 and reports mutual exclusivity.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_serve_dispatches_to_run_stdio fingerprint=dc419e9badf8868cb08692fc7c528c6d5b50a9b9dd57c5b724a65a1e645d0c0a body_fp=f63d344d804718e8fa68880b36c6a8cbf8d363ca23721ce16cb803cc7cdf00b2 -->
## `test_cli_mcp_serve_dispatches_to_run_stdio(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify that `trie mcp serve` invokes `run_mcp_stdio` with the resolved project root.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp_install:test_cli_mcp_no_subcommand_runs_serve fingerprint=1684a89b2d1ae28d0118412fb9c20e562c61d2b9dad00525e7c0cb7d8cd138a8 body_fp=a21dd89fa77ffeb34525fa429eec72ec26774e325e8d3ce5c92164ea896ba142 -->
## `test_cli_mcp_no_subcommand_runs_serve(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify that `trie mcp` with no subcommand invokes `run_mcp_stdio` for backward compatibility with existing snippets.
<!-- trie:end -->