---
trie_version: 0.1.2
source: tests/test_setup.py
file_fingerprint: 4007b65150fb6a76d61d6bee3ea71991be335e0471d9c249a6b989f7c0fba376
last_synced_at: '2026-05-20T13:54:49Z'
description: End-to-end tests for `trie setup` and the underlying hook installer.
defines:
- kind: module
  qualified_name: tests/test_setup:__module__
  lines: 1-436
- kind: function
  qualified_name: tests/test_setup:project
  lines: 34-45
- kind: function
  qualified_name: tests/test_setup:test_opencode_hook_creates_plugin_file
  lines: 53-83
- kind: function
  qualified_name: tests/test_setup:test_opencode_hook_writes_package_json_to_unblock_bun_install
  lines: 86-105
- kind: function
  qualified_name: tests/test_setup:test_opencode_hook_package_json_is_idempotent
  lines: 108-128
- kind: function
  qualified_name: tests/test_setup:test_opencode_hook_is_idempotent
  lines: 131-148
- kind: function
  qualified_name: tests/test_setup:test_opencode_hook_updates_when_contents_changed
  lines: 151-166
- kind: function
  qualified_name: tests/test_setup:test_print_only_writes_no_files
  lines: 169-181
- kind: function
  qualified_name: tests/test_setup:test_dry_run_writes_no_files
  lines: 184-193
- kind: function
  qualified_name: tests/test_setup:test_claude_code_hook_is_manual_setup
  lines: 196-210
- kind: function
  qualified_name: tests/test_setup:test_unknown_target_raises
  lines: 213-221
- kind: function
  qualified_name: tests/test_setup:test_install_all_covers_every_target
  lines: 224-233
- kind: function
  qualified_name: tests/test_setup:test_apply_one_returns_needs_manual_setup_for_render_none
  lines: 241-249
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_opencode_writes_both_files
  lines: 257-274
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_claude_code_does_mcp_and_warns_about_hook
  lines: 277-288
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_print_only_writes_nothing
  lines: 291-299
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_target_and_all_mutex
  lines: 302-307
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_invalid_scope
  lines: 310-315
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_idempotent_second_run
  lines: 318-334
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_installs_overrides_by_default
  lines: 347-359
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_no_overrides_flag_skips_overrides
  lines: 362-378
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_print_only_previews_overrides_without_writing
  lines: 381-396
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_claude_code_creates_advisory_hook_by_default
  lines: 399-414
- kind: function
  qualified_name: tests/test_setup:test_cli_setup_override_idempotent_on_second_run
  lines: 417-435
incoming_refs: 0
outgoing_refs: 26
---
<!-- trie:section symbol=tests/test_setup:project fingerprint=1f83c1fd82d36d3db04107648fc45b8a7541a7d15408974e22c21bda26a413b5 body_fp=ad646ff0bf22ebca2cb69d0e9f0ee1edbb6a6d7703170f9588696f6619e2a7e7 source_ref=eae88ef26c089f711012aa225c1debacb734217c -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal `trie.toml` in a temp directory and returns its path.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_setup:test_opencode_hook_creates_plugin_file fingerprint=fc94d480e290261b1fe2896b887d8b2dad458d4ad585c77f7a6e67594d0f2a0b body_fp=79abe08f92ae6a3fab1e08c1c75dc51cf9a6feb0e2755c1d2d36fc62505e1d53 source_ref=9ab1903672c6e8c734747e2990ed26be4fc16a93 -->
## `test_opencode_hook_creates_plugin_file(project: Path)`

Verify that `install` for the `opencode` target creates the plugin file with correct wiring on disk.

- `project`: tmp directory with a valid `trie.toml`; file must not pre-exist.
- Asserts plugin uses `session.status`/`"idle"` event, `export default` with `"trie-refresh"` id, and a `package.json` baseline with `@opencode-ai/plugin` dependency.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_setup:test_opencode_hook_is_idempotent fingerprint=990c68bf415c67aada411639b45df589b73ff3095d81a16c682c41c8bb03e798 body_fp=bba7f33cfca4ce1433bb7363de92868978589c4de3daef254b5239ffcf87a299 source_ref=eae88ef26c089f711012aa225c1debacb734217c -->
## `test_opencode_hook_is_idempotent(project: Path)`

Assert that a second `install` call for opencode returns `action == "skipped"` when the file already matches expected contents.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_setup:test_opencode_hook_updates_when_contents_changed fingerprint=16c13d1ad1551ecdb8e569a7f01c798765f464f0fac1ac0c5d706b8987d29bc5 body_fp=0fde6ed32f5750c7455f2d004987b3824d9447b3e49adf7bbf0b18d03ecd6bdc source_ref=9ab1903672c6e8c734747e2990ed26be4fc16a93 -->
## `test_opencode_hook_updates_when_contents_changed(project: Path)`

Assert that a stale plugin file is overwritten and the action is `"updated"`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_setup:test_print_only_writes_no_files fingerprint=f4ff1972983e259adbd54ea679d5a6967b4d0507c47cc401ab2b6a2c3cf0e3c0 body_fp=ccda917f491b32feb0485ac1560abba3c6b5cd82225284a4610d55e65efba113 source_ref=9ab1903672c6e8c734747e2990ed26be4fc16a93 -->
## `test_print_only_writes_no_files(project: Path)`

Assert that `print_only=True` returns a `"preview"` action with contents but writes no files to disk.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_setup:test_dry_run_writes_no_files fingerprint=a143c463520454fbd073ae45f77963a03b5ba91f65e6ac4691022307e2caaf32 body_fp=61ea96b75fcb209598ebada72361dd0d4f2b8405e3d7f680d3fac5ea352a77a6 source_ref=eae88ef26c089f711012aa225c1debacb734217c -->
## `test_dry_run_writes_no_files(project: Path)`

Assert that `dry_run=True` produces a `"preview"` action and writes no files to disk.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_setup:test_claude_code_hook_is_manual_setup fingerprint=a8ace2daa3934f5c10dd65a38b09bbac037bbf420577839aab85faebe680da5f body_fp=c8b19be06d2a027719218331195a56d8c7a4e0cc6a904c66471ef355c06e6e5d source_ref=eae88ef26c089f711012aa225c1debacb734217c -->
## `test_claude_code_hook_is_manual_setup(project: Path)`

Assert that `install` for `claude-code` returns `needs_manual_setup` with `trie refresh` instructions instead of writing a file.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_setup:test_unknown_target_raises fingerprint=b996901d4154a592929d95841b43d8430c072ac3d703a97266a8b5c4234ad90b body_fp=1c7937d3e4f81df3fdb899af55ea007c6be87501d4cb42e0a8df44d353ea03d8 source_ref=eae88ef26c089f711012aa225c1debacb734217c -->
## `test_unknown_target_raises(project: Path)`

Assert that `install` raises `HookInstallError` when given an unrecognised target name.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_setup:test_install_all_covers_every_target fingerprint=65b44f9f93cdc70987d9b72ed2f8154b496d4438c69b5b08bfdaed8142fff5a6 body_fp=2c77fd73181789d07d9d2fbbe138908e52c553fceac278f6f96660ec9eac32d1 source_ref=eae88ef26c089f711012aa225c1debacb734217c -->
## `test_install_all_covers_every_target(project: Path)`

Verify that `install_all=True` produces results for every registered target in `TARGETS`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_setup:test_apply_one_returns_needs_manual_setup_for_render_none fingerprint=90abc01ee67a98b22e5174ecbf38accc7f8eb7650f4914d15cc4e7b6842010c0 body_fp=1b5b0c2bea9893796b84f4d7d6e8d8a9e77d74ac637ce3a16a50f6f620817466 source_ref=eae88ef26c089f711012aa225c1debacb734217c -->
## `test_apply_one_returns_needs_manual_setup_for_render_none(project: Path)`

Assert that `apply_one` returns a `needs_manual_setup` result for any `HookTarget` with no `render_contents`.

- `project`: fixture providing a minimal trie project root.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_setup:test_cli_setup_opencode_writes_both_files fingerprint=248b29b548d5689c673c4e1bb49ca3795c4fbaeb7caf6b5b5b49bf63f54921b8 body_fp=939a78df660e8553136e94583cb653cb9394a2616ef4eceb38370f7629f2d147 source_ref=9ab1903672c6e8c734747e2990ed26be4fc16a93 -->
## `test_cli_setup_opencode_writes_both_files(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify `trie setup --target opencode` writes the MCP config, hook plugin, and `package.json` baseline files.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_setup:test_cli_setup_claude_code_does_mcp_and_warns_about_hook fingerprint=51526b5cf3bd1dce60b48f4f40eb26eee596f61f0622ea4d8945beca74259a68 body_fp=51a92e55a8928d7e667947cdc30735b7fcdf3d6b49f55dccc3a45ab667434858 source_ref=eae88ef26c089f711012aa225c1debacb734217c -->
## `test_cli_setup_claude_code_does_mcp_and_warns_about_hook(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify that `trie setup --target claude-code` writes MCP config and emits a manual-setup warning without failing.

- `project`: tmp directory containing a minimal `trie.toml`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_setup:test_cli_setup_print_only_writes_nothing fingerprint=0ae794aaa478e7f364ff59256049d6077fa8dd1b4b65f356984718fd8902fd56 body_fp=d2a61bee3557799b082574e5d86f605f4b9a4de3a9d45b52341b567db5b2789f source_ref=9ab1903672c6e8c734747e2990ed26be4fc16a93 -->
## `test_cli_setup_print_only_writes_nothing(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie setup --print-only` writes no files but prints preview content including `session.status`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_setup:test_cli_setup_target_and_all_mutex fingerprint=5b719a0905f62f2b711acb341172ce5f2aeb84e6c1814917e8213465d811d8d6 body_fp=008989d375ff5cc9ec78acbbae8a3eb5792d5b883d3d4f8822fe7d3fd806e02f source_ref=eae88ef26c089f711012aa225c1debacb734217c -->
## `test_cli_setup_target_and_all_mutex(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that passing `--target` and `--all` together exits with code 1 and reports mutual exclusivity.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_setup:test_cli_setup_invalid_scope fingerprint=0ae4df086b2c9d0f965e0c4788fd03182fca2adf1cf4ab29fe7a0d6e296eb426 body_fp=4b6d43fd7dfc55baea60d83513fe4dc3adf151d42b8ca3cacb9572c230ebd250 source_ref=eae88ef26c089f711012aa225c1debacb734217c -->
## `test_cli_setup_invalid_scope(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie setup` exits with code 1 and mentions "scope" when given an unsupported `--scope` value.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_setup:test_cli_setup_idempotent_second_run fingerprint=6786ef89771693ca5d491db1b534d622da55d95415f845c57a6126c441fdbd64 body_fp=52a5830570d3bdaa1d89c7ce5b8068f69c52d27e579870237465e95f220862d0 source_ref=eae88ef26c089f711012aa225c1debacb734217c -->
## `test_cli_setup_idempotent_second_run(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that re-running `trie setup opencode` leaves MCP and hook files byte-identical.
<!-- trie:end -->







<!-- trie:section symbol=tests/test_setup:test_cli_setup_print_only_previews_overrides_without_writing fingerprint=b1ebb850f2e5e3fc8e38f0ea33e3f01a120ba0cf72ada1eea7fe5434b290adca body_fp=aa6ef5ba4eec29945c18ef46756df8f3c0ef62f5ea52b75337a575aca37d69b2 source_ref=83d461b20e1178bd609db26de2df4ee987163495 -->
## `test_cli_setup_print_only_previews_overrides_without_writing(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert `--print-only` shows all three override filenames in output without writing any files to disk.

- `project`: temporary directory with a minimal `trie.toml`.
<!-- trie:end -->



<!-- trie:section symbol=tests/test_setup:test_cli_setup_override_idempotent_on_second_run fingerprint=cf1b1f9d9fccd3a9e0b4c3cf87f6ee2ca5cc89a9f55e88d2b2228fd0ac05c34c body_fp=8caf075be48efa04b0e4683a5b397781a27c040e2aa9955f432f70b1bd08da62 source_ref=83d461b20e1178bd609db26de2df4ee987163495 -->
## `test_cli_setup_override_idempotent_on_second_run(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify that re-running `trie setup` (without `--override-builtins`) skips unchanged override files and reports "skipped".
<!-- trie:end -->

<!-- trie:section symbol=tests/test_setup:test_cli_setup_installs_overrides_by_default fingerprint=356d4f89b98b08b5ad78e8145c1c4b0ca434fd5bc6b5183834d8d468756a6b62 body_fp=c739266b3cb17198298509c091616bba1c5bc25a9ebcaaf8a86bcba2ef01c789 source_ref=83d461b20e1178bd609db26de2df4ee987163495 -->
## `test_cli_setup_installs_overrides_by_default(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie setup --target opencode` installs all three opencode tool-override files without any opt-in flag.

- Checks `.opencode/tools/grep.ts`, `read.ts`, and `trie_trace.ts` all exist after invocation.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_setup:test_cli_setup_no_overrides_flag_skips_overrides fingerprint=1152208439be12d21551f9408466b790ab8560619d9c19f535fe9217e89e951b body_fp=02094ee306f9e0bbcca539f5ef0e3a5361dc8d9e8bfdd49fd3ce2ac645ebe3b5 source_ref=83d461b20e1178bd609db26de2df4ee987163495 -->
## `test_cli_setup_no_overrides_flag_skips_overrides(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify that `--no-overrides` skips `.opencode/tools/` override files while MCP, hook, and docs steps still complete.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_setup:test_cli_setup_claude_code_creates_advisory_hook_by_default fingerprint=22a9eac169969fc08042af9f7177daab246cabac72da267aac8b7c515ce3a647 body_fp=684eea9c84edfef7b8c17b4fa432e79187c110779e33c12becc15d237dd15a1e source_ref=83d461b20e1178bd609db26de2df4ee987163495 -->
## `test_cli_setup_claude_code_creates_advisory_hook_by_default(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify that `trie setup --target claude-code` writes a PreToolUse hook file referencing `mcp__trie__grep` by default, without any opt-in flag.

- `project`: temporary directory with a minimal `trie.toml`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_setup:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=a54abe81712a48ef5929396818127feb4d47ee6e411d706f516647c7740c5d4e source_ref=83d461b20e1178bd609db26de2df4ee987163495 -->
## `tests/test_setup`

End-to-end tests for `trie setup`, `hook_install.install`, and `apply_one` covering creation, idempotency, dry-run, manual-setup notices, and CLI behaviour.

- `project` fixture: minimal `trie.toml` in `tmp_path`, returned as `Path`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_setup:test_opencode_hook_writes_package_json_to_unblock_bun_install fingerprint=150974fe71aa8f4eec1092d0f7e58e0c3a57a1466717becd48df75f5138a2fe1 body_fp=2a0832f73cc542da622d728af11e073564966b03ee61fda9ee481e284ce9e36c source_ref=9ab1903672c6e8c734747e2990ed26be4fc16a93 -->
## `test_opencode_hook_writes_package_json_to_unblock_bun_install(project: Path)`

Verify that `install` writes `.opencode/package.json` with `@opencode-ai/plugin` pinned to `"latest"`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_setup:test_opencode_hook_package_json_is_idempotent fingerprint=7b393b32f63bb44b824d36e8aa3788c0150b480f0506a6403216f88a96f0f2e1 body_fp=8c8f8cc8a492264bec2a6a477e3a9c9c24daf7c5c48e6a6c329b13ae49e9e9cf source_ref=9ab1903672c6e8c734747e2990ed26be4fc16a93 -->
## `test_opencode_hook_package_json_is_idempotent(project: Path)`

Assert that a second `install` call leaves `.opencode/package.json` byte-for-byte unchanged.
<!-- trie:end -->