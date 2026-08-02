---
trie_version: 0.3.0
source: tests/test_tool_override_install.py
file_fingerprint: 7f72a3893c05a4534513c675230f30973b227ccd5314ba6a786f74432e4563ee
last_synced_at: '2026-08-02T21:19:24Z'
description: 'Tests for `trie.tool_override_install`: replacing agent built-in tools with trie wrappers.'
defines:
- kind: module
  qualified_name: tests/test_tool_override_install:__module__
  lines: 1-991
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_install_creates_override_files
  lines: 39-74
  signature: 'def test_opencode_install_creates_override_files(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_grep_override_routes_to_trie_grep
  lines: 77-92
  signature: 'def test_opencode_grep_override_routes_to_trie_grep(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_files_carry_generated_notice
  lines: 95-108
  signature: 'def test_opencode_files_carry_generated_notice(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_rendered_files_have_balanced_backticks_per_line
  lines: 111-144
  signature: 'def test_opencode_rendered_files_have_balanced_backticks_per_line(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_dispatches_on_qname_path_or_show_source
  lines: 152-174
  signature: 'def test_opencode_read_override_dispatches_on_qname_path_or_show_source(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_advertises_show_source_arg
  lines: 177-190
  signature: 'def test_opencode_read_override_advertises_show_source_arg(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_qname_detection_excludes_urls_and_drives
  lines: 193-211
  signature: 'def test_opencode_read_override_qname_detection_excludes_urls_and_drives(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_emits_telemetry_from_typescript
  lines: 214-244
  signature: 'def test_opencode_read_override_emits_telemetry_from_typescript(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_appends_telemetry_atomically
  lines: 247-264
  signature: 'def test_opencode_read_override_appends_telemetry_atomically(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_handles_absolute_paths
  lines: 267-288
  signature: 'def test_opencode_read_override_handles_absolute_paths(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_advertises_full_arg
  lines: 291-307
  signature: 'def test_opencode_read_override_advertises_full_arg(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_emits_compact_renderer
  lines: 310-329
  signature: 'def test_opencode_read_override_emits_compact_renderer(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_full_mode_trims_for_agent
  lines: 332-354
  signature: 'def test_opencode_read_override_full_mode_trims_for_agent(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_trie_read_obsolete_file_removed_on_apply
  lines: 357-382
  signature: 'def test_opencode_trie_read_obsolete_file_removed_on_apply(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_trie_trace_obsolete_file_removed_on_apply
  lines: 385-408
  signature: 'def test_opencode_trie_trace_obsolete_file_removed_on_apply(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_obsolete_cleanup_is_noop_on_fresh_install
  lines: 411-426
  signature: 'def test_opencode_obsolete_cleanup_is_noop_on_fresh_install(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_install_is_idempotent_on_identical_content
  lines: 434-459
  signature: 'def test_opencode_install_is_idempotent_on_identical_content(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_install_updates_on_drift
  lines: 462-487
  signature: 'def test_opencode_install_updates_on_drift(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_tool_override_install:test_claude_code_install_creates_advisory_hook
  lines: 495-522
  signature: 'def test_claude_code_install_creates_advisory_hook(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_tool_override_install:test_claude_code_hook_does_not_deny_grep
  lines: 525-539
  signature: 'def test_claude_code_hook_does_not_deny_grep(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_tool_override_install:test_unsupported_harnesses_emit_needs_manual_setup
  lines: 551-569
  signature: 'def test_unsupported_harnesses_emit_needs_manual_setup(tmp_path: Path, slug: str)'
- kind: function
  qualified_name: tests/test_tool_override_install:test_install_for_opencode_and_claude_code_in_one_pass
  lines: 577-590
  signature: 'def test_install_for_opencode_and_claude_code_in_one_pass(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_tool_override_install:test_print_only_does_not_write_anything
  lines: 598-619
  signature: 'def test_print_only_does_not_write_anything(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_tool_override_install:test_dry_run_does_not_write_when_file_already_correct
  lines: 622-642
  signature: 'def test_dry_run_does_not_write_when_file_already_correct(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_tool_override_install:test_install_with_empty_target_names_raises
  lines: 650-657
  signature: 'def test_install_with_empty_target_names_raises(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_tool_override_install:test_install_with_unknown_target_raises
  lines: 660-674
  signature: 'def test_install_with_unknown_target_raises(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_tool_override_install:test_apply_one_uses_needs_manual_setup_for_targets_with_no_files
  lines: 677-686
  signature: def test_apply_one_uses_needs_manual_setup_for_targets_with_no_files()
- kind: function
  qualified_name: tests/test_tool_override_install:test_rendered_tools_relay_both_streams_on_failure
  lines: 689-701
  signature: 'def test_rendered_tools_relay_both_streams_on_failure(tmp_path: Path)'
- kind: constant
  qualified_name: tests/test_tool_override_install:_REGEX_START_CHARS
  lines: 721-721
- kind: function
  qualified_name: tests/test_tool_override_install:_first_raw_newline_in_quoted_string
  lines: 724-880
  signature: 'def _first_raw_newline_in_quoted_string(source: str) -> tuple[int, str] | None'
- kind: function
  qualified_name: tests/test_tool_override_install:_rendered_opencode_ts_files
  lines: 883-890
  signature: 'def _rendered_opencode_ts_files(project_root: Path) -> dict[str, str]'
- kind: function
  qualified_name: tests/test_tool_override_install:test_rendered_ts_overrides_have_no_unterminated_string_literals
  lines: 893-913
  signature: 'def test_rendered_ts_overrides_have_no_unterminated_string_literals(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_tool_override_install:test_scanner_flags_a_known_unterminated_string_literal
  lines: 916-942
  signature: def test_scanner_flags_a_known_unterminated_string_literal()
- kind: function
  qualified_name: tests/test_tool_override_install:test_rendered_ts_overrides_parse_under_js_runtime
  lines: 946-990
  signature: 'def test_rendered_ts_overrides_parse_under_js_runtime(tmp_path: Path, runtime: str)'
incoming_refs: 0
outgoing_refs: 32
---
<!-- trie:section symbol=tests/test_tool_override_install:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=3cb993b151f9ea2ea7ddf3774547435bafb8e0eb9c5f593eded0bd55ef057cb4 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
Tests for `trie.tool_override_install` functionality that replaces agent built-in tools with trie wrappers.

- Verifies opencode gets three override files (grep.ts, read.ts, trace.ts) plus eight extended tools under `.opencode/tools/`
- Confirms Claude Code receives advisory hook file at `.claude/hooks/trie-tools.json` for mcp__trie__grep nudging
- Validates other harnesses emit `needs_manual_setup` with target-specific instructions
- Tests idempotency: identical content returns `skipped`, drifted content returns `updated`
- Ensures `--print-only` and `--dry-run` never write files to disk
- Guards against TypeScript syntax errors from unbalanced backticks in rendered comment lines
- Verifies read.ts override dispatches between qname routing, triefact lookup, and show_source fallback
- Confirms obsolete file cleanup (trie_read.ts, trie_trace.ts) during migration
- Tests compact mode rendering with frontmatter stripping and sentinel removal
- Validates telemetry emission from TypeScript wrappers for audit visibility
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_install_creates_override_files fingerprint=a76f5ca0678b5f670b5e59832755d9e6d80531e6d259acbd2b2596c1bc5c98e6 body_fp=8768cf123dfa741bd5c7e3ae3425ef5e2c4dbfd01b55188da2ee5c992ac6bcb6 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=agent-integration -->
## `def test_opencode_install_creates_override_files(tmp_path: Path)`

Verifies that opencode tool override install writes 11 TypeScript files to `.opencode/tools/`.

- Asserts presence of 3 original tools: `grep.ts`, `read.ts`, `trace.ts`
- Asserts presence of 8 extended tools: various grep/explain/trace variants
- Confirms all written files exist on disk after installation
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_grep_override_routes_to_trie_grep fingerprint=bbea07bffaf1433c02906416587d0a3e71ec2c83fa56a0b8271f44f15358bcad body_fp=59024082ec683e960514e130cfb2ba905e107e01aba3afedf0fe6d7a7f3e3168 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
## `def test_opencode_grep_override_routes_to_trie_grep(tmp_path: Path)`

Verifies that opencode's generated `grep.ts` override file contains the correct shell command to route agent grep calls to the trie CLI.

- Checks for `Bun.spawn(["trie"` and `"grep"` in the generated TypeScript file
- Ensures plain-text output mode (no `--json` flag present)
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_files_carry_generated_notice fingerprint=931d1963484293165d869cff6a475b7e1d05914d8997dda1eaf105ae35b037c2 body_fp=89df223ce7594d37fa7a54a142d1ad2a516c5825cfcd92b77dd00b450e1e99b6 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
## `def test_opencode_files_carry_generated_notice(tmp_path: Path)`

Verifies that opencode tool override files contain warning headers identifying them as auto-generated artifacts.

- Checks for "Auto-generated by `trie setup" and "Do not hand-edit" markers in each file
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_rendered_files_have_balanced_backticks_per_line fingerprint=c22887ae666f1fc4d321d98ed8f41a4dfc374393f6e4860b7221b77820fca28c body_fp=d7eea3f4ceb2387ea8953214e7c1d1766f8d22e27f928ef93d1ac5b970af7902 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=agent-integration -->
## `def test_opencode_rendered_files_have_balanced_backticks_per_line(tmp_path: Path)`

Validates rendered TypeScript files have even backtick counts in comment lines to prevent template literal parsing errors.

- Prevents a regression where Python `\n` escapes in TS comments split lines and break bun's parser
- Checks all comment lines (starting with `//`) have zero or even backtick counts
- Guards against stray template literals that would silently kill opencode tool registration
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_dispatches_on_qname_path_or_show_source fingerprint=5384e61804c60a7be83e0410d6ad2d4ddc1952c652578811a894ea1bb18859e4 body_fp=a3ebf963f65ac5aca8c631f8f9adc49175d647b26c884b45f2b73e40343fc1fb source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
## `def test_opencode_read_override_dispatches_on_qname_path_or_show_source(tmp_path: Path)`

Verifies opencode read.ts override contains dispatch logic for three modes: qname routing to trie CLI, triefact lookup by path, and raw source via show_source.

- Installs opencode target and reads generated read.ts file content
- Asserts qname dispatch markers: looksLikeQname function and "read" command without --json
- Asserts triefact mode markers: readTriefact function and triefacts reference
- Asserts show_source mode markers: show_source parameter and readSourceFile function
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_advertises_show_source_arg fingerprint=d377a5b4a375cac89dd0bf1a263a6901952e353291915687374f1447324c8283 body_fp=fea19947fc3decb0bd48d749ed6a743ccc70b5a757fda918d7819bf84961e816 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
## `def test_opencode_read_override_advertises_show_source_arg(tmp_path: Path)`

Verifies that opencode's read.ts override exposes show_source, offset, and limit arguments in its schema for raw source fallback.

- `show_source`: escape hatch to bypass triefact lookup and return raw file content
- `offset`, `limit`: line range parameters for the raw source mode
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_qname_detection_excludes_urls_and_drives fingerprint=a31e56fc088c1052530734293a7a78524443e45fac5d3e70153bda3a342a1916 body_fp=3a9c8d491c6dea0f291ef5f89c949f236619b9faae53c8177b427c626909a9b2 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
## `def test_opencode_read_override_qname_detection_excludes_urls_and_drives(tmp_path: Path)`

Verifies that opencode's `read.ts` override correctly excludes URLs and Windows drive paths from qname detection.

- Checks that `looksLikeQname` function distinguishes qualified names from URLs (`://`) and Windows drives (`[A-Za-z]:`)
- Prevents false positives where colon-containing paths get misrouted to `trie read` instead of file system access
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_emits_telemetry_from_typescript fingerprint=7f8c4fed8e631923f71efea317df78da8411d4c17e61bd0e528cb429666e563b body_fp=197a252763ecb68512b841b8f4f3bb8d8cd70a49db4395cb71d287baf29e7572 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
## `def test_opencode_read_override_emits_telemetry_from_typescript(tmp_path: Path)`

Validates that opencode's `read.ts` override embeds TypeScript-side telemetry for in-process dispatch modes.

- Checks rendered template contains telemetry helpers: `emitTelemetry`, `resolveTelemetryConfig`, `extractTomlSection`
- Verifies baked-in event structure includes `cli_call` event name, `read` tool name, and `mode` field
- Ensures TRIE_DEBUG environment variable support matches Python implementation
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_appends_telemetry_atomically fingerprint=4392ac7d6c58ee986401da04b6a844b5e514681cd33a94fed47d3360195fa4f2 body_fp=190f86a1e8d8e5aaf17101a773f4fa1dc13a4df365f253b16a7af694c326603d source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=agent-integration -->
## `def test_opencode_read_override_appends_telemetry_atomically(tmp_path: Path)`

Tests that opencode's read.ts override uses atomic append-mode I/O for telemetry logging.

- Verifies `appendFile` is imported and used from `node:fs/promises`
- Ensures no read-then-write pattern that could create race conditions
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_handles_absolute_paths fingerprint=331fc83490b3d1f8cf59065f4c0128e7d3321e595ed45c4912a282848cf2c585 body_fp=5e1dfc7b1525cf11a198c290ae84983f6e50a99c72e6bc36144da9f2ccd48c3e source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=agent-integration -->
## `def test_opencode_read_override_handles_absolute_paths(tmp_path: Path)`

Tests that the opencode read.ts override correctly handles absolute paths without breaking Node.js path resolution.

- Verifies `resolveAbsolutePath` helper exists and uses `isAbsolute(path)` branching logic
- Checks that absolute paths bypass cwd joining to prevent path mangling
- Confirms `projectRelativePath` helper handles absolute paths within project tree
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_advertises_full_arg fingerprint=005cdc6c3d94967f1d1afa9f90580144130596b3eae9e920da25a090a43812dd body_fp=cbc50ac2b6df1234882e4729b4089815f4b39b2c9840d0070174ee8bad7ae298 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
## `def test_opencode_read_override_advertises_full_arg(tmp_path: Path)`

Verifies opencode's read.ts override includes a `full` parameter to escape compact mode defaults.

- Checks for `full: tool.schema` in the generated TypeScript
- Ensures the description mentions "compact" so agents understand the default behavior
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_emits_compact_renderer fingerprint=5695f91271e789440ef43b5a770758ef6502837591c372a78ebe8aa3c93de99a body_fp=fccdd55e8476113992c9c53dba814fb74a85e6109dbc5835bf3b00d9d6c14835 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
## `def test_opencode_read_override_emits_compact_renderer(tmp_path: Path)`

Verifies opencode's read.ts override includes compact rendering helpers and telemetry mode tags.

- Checks for presence of `renderCompact`, `parseFrontMatter`, and `extractSections` functions
- Validates telemetry mode tags `triefact_compact` and `triefact_full` are emitted
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_full_mode_trims_for_agent fingerprint=d16eec00436dccc69af73d191648d1d6ccfaa708532d5301f331e513bd01bf08 body_fp=a044b0dd434092f11bfea7297b1c9d0c33cdd888331c3aed1f127959f2b7b986 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
## `def test_opencode_read_override_full_mode_trims_for_agent(tmp_path: Path)`

Verifies that opencode's `read.ts` override strips internal metadata from triefacts in full mode.

- Checks for `renderForAgent`, `stripSentinels`, and `renderFrontMatterForAgent` helper functions
- Ensures full mode calls `renderForAgent(triefact)` instead of returning raw triefact
- Prevents regression where full mode leaked raw `.md` with frontmatter and sentinels
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_trie_read_obsolete_file_removed_on_apply fingerprint=9b1d5f8b5a30c80327e621908e7e53850a244638429671af0c96104d234129fb body_fp=8f76a4e393f0c789dca3f80d4c5a91d5a3f8a1f11c31bb8ae0c39eff684b333a source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=agent-integration -->
## `def test_opencode_trie_read_obsolete_file_removed_on_apply(tmp_path: Path)`

Tests that trie setup automatically removes obsolete `trie_read.ts` files when applying opencode tool overrides.

- Creates a stale `trie_read.ts` file then verifies setup removes it during installation
- Asserts cleanup action appears in plan results with "removed obsolete" description  
- Validates new `read.ts` override subsumes the old separate tool's functionality
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_trie_trace_obsolete_file_removed_on_apply fingerprint=1e6177df323fce1c409ce9b59f17140642922fad4f84cf0e0083388b293e4581 body_fp=b99d0dba6f2ad34be0a2631f0c00be37cf8df41b563032af7de69d8472d72661 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=agent-integration -->
## `def test_opencode_trie_trace_obsolete_file_removed_on_apply(tmp_path: Path)`

Tests that obsolete `trie_trace.ts` is removed when re-running opencode tool override installation.

- Creates stale `.opencode/tools/trie_trace.ts` file to simulate prior installation
- Verifies file is deleted and cleanup result shows "updated" action with "removed obsolete" description
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_obsolete_cleanup_is_noop_on_fresh_install fingerprint=04ec87c8983682f3c5d287e359bb0d00e26fb2b3059928626ca6aa13c0d16dd4 body_fp=4689f58cc9c4aa0d9ca42ddbfcddab55cf3e70c0e30de29a68035f00480e975e source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=agent-integration -->
## `def test_opencode_obsolete_cleanup_is_noop_on_fresh_install(tmp_path: Path)`

Verifies that first-time opencode installs skip cleanup of non-existent obsolete files without errors.

- Asserts cleanup results report "skipped" action with "nothing to clean up" detail
- Guards against errors when attempting to remove files that were never created
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_install_is_idempotent_on_identical_content fingerprint=87fc921b24fd75af74ee18291121a61336a1480d8b0b133629f017c95411a5fd body_fp=8fb46496440379cf9f1e95c5eb184c9f7b5120b79eaf166ed7f34648dbefeb6c source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
## `def test_opencode_install_is_idempotent_on_identical_content(tmp_path: Path)`

Tests that `install()` skips file writes when content hasn't changed.

- Runs install twice on same project, verifies second run reports `skipped` for all files
- Non-obsolete files must report "same contents" in detail field
- Validates idempotency behavior that makes `trie setup` safe to run repeatedly
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_install_updates_on_drift fingerprint=1598b027eb6c27bf0e21de5bea19063974caf4a976a86c98938412a210e0b5a3 body_fp=24ed2fcbbbb002a57f34b680bae1cd8bb1d59e997362e9df034d19a2ceea92d8 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
## `def test_opencode_install_updates_on_drift(tmp_path: Path)`

Verifies that opencode install detects and overwrites manually-edited generated files to prevent stale routing.

- Runs initial install, manually edits `grep.ts`, then runs second install
- Asserts second install reports `updated` action and restores auto-generated content
- Guards against stale wrapper files silently routing agents to wrong destinations
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_claude_code_install_creates_advisory_hook fingerprint=001f1ffd25598478bcd3b656b515e9b5491e5d2c8d41899e6ddbad20f3a76c36 body_fp=d9de9ba00271987b72cf513866f9ca281be60f18ec87a55e06371317577234bd source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
## `def test_claude_code_install_creates_advisory_hook(tmp_path: Path)`

Tests that Claude Code install creates the advisory hook file at `.claude/hooks/trie-tools.json` with correct PreToolUse structure.

- Verifies hook file exists and contains proper JSON schema for Claude Code
- Asserts hook targets built-in "Grep" tool with exact string match
- Confirms hook command contains "systemMessage" and references "mcp__trie__grep"
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_claude_code_hook_does_not_deny_grep fingerprint=b0917350ef7add9adf24564bb8f967df64c94de5affe02776d3be2f57ce39bcf body_fp=b8261c5a567693fc9741b348c36e2024ae90ae9bae09ce40801c1ae2db94ee3b source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=agent-integration -->
## `def test_claude_code_hook_does_not_deny_grep(tmp_path: Path)`

Verifies that Claude Code's trie tools hook remains advisory-only and does not block built-in Grep usage.

- Ensures rendered hook JSON contains no `permissionDecision` or `"deny"` strings
- Guards against accidental conversion from advisory to blocking behavior
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_unsupported_harnesses_emit_needs_manual_setup fingerprint=252d564de8cef912137183a246a83c8734777cfbd60c0a79917aab425762c512 body_fp=7e8c895e254bea5a087ea4346062e3dd234046073a1203f2f54c6ca4a40fcd0f source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
## `def test_unsupported_harnesses_emit_needs_manual_setup(tmp_path: Path, slug: str)`

Verifies unsupported harnesses return `needs_manual_setup` with instructions instead of silently skipping.

- Tests each harness slug: claude-desktop, cursor, windsurf, vscode, codex
- Confirms no files written to disk when automation isn't possible
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_install_for_opencode_and_claude_code_in_one_pass fingerprint=e5a91b31de3c5d2716c71642ee28352e70962a865fe3310f85e696ab6d40c562 body_fp=1b54f2d617c4f8b6f56d998242528b073f62ee75924077ae9f7a1a001890b3a8 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
## `def test_install_for_opencode_and_claude_code_in_one_pass(tmp_path: Path)`

Tests that `install()` can process multiple targets in a single call, verifying both opencode and claude-code files are written independently.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_print_only_does_not_write_anything fingerprint=195068d913203efa2f7a33563f5b2d88d92ce6ddea2f47b5768362fab4701a4b body_fp=61c8f7cdbe938a0ba00cf1e9b41a4615433b08b34716471a2aa43f81909404ef source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
## `def test_print_only_does_not_write_anything(tmp_path: Path)`

Verifies that `--print-only` mode prevents disk writes and returns preview results with rendered file contents.

- Confirms `.opencode` directory is never created during preview
- Validates write operations report `preview` action with content in `detail`
- Distinguishes between preview-eligible file writes and skipped obsolete cleanups
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_dry_run_does_not_write_when_file_already_correct fingerprint=97dd083d6cfe5d0fce2cf74184a64b3a1581bdb594a76cf69b3fe2c183f8370c body_fp=a59e00dd53f31d613b03b17b0b7ff6aec01e03b35ef1aa5c7b61130eac1ce6b4 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
## `def test_dry_run_does_not_write_when_file_already_correct(tmp_path: Path)`

Verifies that `--dry-run` returns `skipped` when files already match expected content.

- Creates files with first install, then runs second install with `dry_run=True`
- Asserts second install reports `skipped` action since no changes needed
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_install_with_empty_target_names_raises fingerprint=de0258da2c32f2c009bcd96277b319ba9b02d3ed14cff07f8674efeaf77483ba body_fp=dea9355928f3393889b8b9d46863d64158bc5852a113fa195484089182ef4912 source_ref=221ce3a4983305c9d20743562130f96880bc751a role=test -->
## `def test_install_with_empty_target_names_raises(tmp_path: Path)`

Tests that `install` raises `ToolOverrideInstallError` when called with empty or null target names.

- Verifies both `[]` and `None` as invalid inputs trigger the exception
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_install_with_unknown_target_raises fingerprint=572c2b692bcbb73e70155902d114481a3ce552681a94400872b8619403e3456e body_fp=1d50e9d32c83e8871502a00768c4faefd80d832b31ad2d05c78d4a72cf026638 source_ref=221ce3a4983305c9d20743562130f96880bc751a role=test -->
## `def test_install_with_unknown_target_raises(tmp_path: Path)`

Verifies `install()` raises `ToolOverrideInstallError` for unknown target names.

- Checks error message includes the invalid target name
- Verifies error message lists valid options for fixing typos
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_apply_one_uses_needs_manual_setup_for_targets_with_no_files fingerprint=f33b7ea65004cd19d365772957c29eacf6c1e64c4485bb643ac88dc9fb8692c1 body_fp=19ea794246c008930e641dfe173be85303d0333aa892a2d2f519d74190731aaf source_ref=221ce3a4983305c9d20743562130f96880bc751a role=test -->
## `def test_apply_one_uses_needs_manual_setup_for_targets_with_no_files()`

Tests that `apply_one` returns `needs_manual_setup` for targets with empty file tuples.

- Verifies harnesses with only manual instructions return appropriate action without disk writes
- Ensures consistent behavior with `hook_install.apply_one` for similar target shapes
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_rendered_tools_relay_both_streams_on_failure fingerprint=5545acc4b20798092b016b8c47735b01af594ea2289600b95613073bdf8e1bfb body_fp=c1fa42fea4a1b1c07b638098099a2b22779a9f9e5135228f9128895e893e63c6 source_ref=221ce3a4983305c9d20743562130f96880bc751a role=test -->
## `def test_rendered_tools_relay_both_streams_on_failure(tmp_path: Path)`

Regression test asserting that all rendered opencode `.ts` tool templates join both `stderr` and `stdout` on failure rather than silently dropping one stream.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:_REGEX_START_CHARS fingerprint=f1c49945c596206494f991f5ce8050f110ae35d2b295bbb937d1cec93d6bb945 body_fp=09027c01e261523640328b8a3bd7d182ed1f9a5286f2cef597058495ed1f7754 source_ref=221ce3a4983305c9d20743562130f96880bc751a role=util -->
Set of punctuation characters after which a `/` token begins a JS regex literal rather than a division operator, used by `_first_raw_newline_in_quoted_string`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:_first_raw_newline_in_quoted_string fingerprint=d52a891c2f9d8964f2ddaa47292f1b1e3c7535d37b7e43fa9947a70469eb8d53 body_fp=9305dea8a68884604bda34a1edd45023d2ab6157e61bbfc2af45b410d723019f source_ref=221ce3a4983305c9d20743562130f96880bc751a role=util -->
## `def _first_raw_newline_in_quoted_string(source: str) -> tuple[int, str] | None`

Scan a JS/TS source string and return `(line_number, snippet)` for the first `'`/`"`-quoted string containing a raw newline, or `None` if all are clean.

- Handles `//`, `/* */`, `` ` `` template literals (including `${…}` interpolations), and `/regex/` literals; does not require a JS runtime.
- Returns the line number where the offending string **opened**, plus a context snippet with newlines escaped.
- A `/` is treated as a regex start only when preceded by a char in `_REGEX_START_CHARS`; quotes inside regex character classes are not mistaken for strings.
- Descends into `${…}` interpolations so a broken quoted string nested inside a template literal is still detected.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:_rendered_opencode_ts_files fingerprint=d02b2e355f4463ca429e600e2d8b1a63973e796905668ea5e1e5c27f35e78d33 body_fp=9f760396424abb4bb0a4bd8466c87c660deb2fe0627bac8d0003a82a43a7acb7 source_ref=221ce3a4983305c9d20743562130f96880bc751a role=test -->
## `def _rendered_opencode_ts_files(project_root: Path) -> dict[str, str]`

Render every opencode `.ts` override file from `TARGETS`, returning a dict keyed by filename.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_rendered_ts_overrides_have_no_unterminated_string_literals fingerprint=739b5e1c4994453876bded715f6c5df3f33eeb70e388be4f21e1e309ea101b0c body_fp=6a6969969fd545a1bb92e69e31919a288c85db7be868a41159e572c4a3b89258 source_ref=221ce3a4983305c9d20743562130f96880bc751a role=test -->
## `def test_rendered_ts_overrides_have_no_unterminated_string_literals(tmp_path: Path)`

Assert that no rendered opencode `.ts` override contains a raw newline inside a single- or double-quoted string literal, using `_first_raw_newline_in_quoted_string` as the hermetic detector.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_scanner_flags_a_known_unterminated_string_literal fingerprint=846396d6957136cfbb0c49313f0df25405f71d60a78ec669d77afe4d67330e4d body_fp=2480257d6a71c85a1250f6fd59971e13451d380bee58e599e15789caae3d45b4 source_ref=221ce3a4983305c9d20743562130f96880bc751a role=test -->
## `def test_scanner_flags_a_known_unterminated_string_literal()`

Validates `_first_raw_newline_in_quoted_string` against known-good and known-bad JS snippets, including raw newlines in `'`/`"` strings, legal `\n` escapes, backtick templates, comments, `${...}` interpolations, and regex literals containing quotes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_rendered_ts_overrides_parse_under_js_runtime fingerprint=727ca79a552fe2b1ef50d45281f3311c9ccf2dbd606ad951cf1dd1dd786d2157 body_fp=0926513d13325d2906996eb2f239bbe21765f8d9d68bf2dfcb7d772018416f72 source_ref=221ce3a4983305c9d20743562130f96880bc751a role=test -->
## `def test_rendered_ts_overrides_parse_under_js_runtime(tmp_path: Path, runtime: str)`

Verify every rendered opencode `.ts` override parses cleanly under `bun build`; skips automatically when `bun` is not on PATH.

- Stubs `@opencode-ai/plugin` locally so parsing requires no network install.
- Fails with per-file `bun` stderr when any override has a syntax error.
<!-- trie:end -->