---
trie_version: 0.2.1
source: tests/test_tool_override_install.py
file_fingerprint: 7265e090e0647ecab5b36a2f5a1169c946a528630b32364864e0fc6a4c3c03de
last_synced_at: '2026-08-01T00:20:38Z'
description: 'Tests for `trie.tool_override_install`: replacing agent built-in tools
  with trie wrappers.'
defines:
- kind: module
  qualified_name: tests/test_tool_override_install:__module__
  lines: 1-702
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_install_creates_override_files
  lines: 39-74
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_grep_override_routes_to_trie_grep
  lines: 77-92
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_files_carry_generated_notice
  lines: 95-108
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_rendered_files_have_balanced_backticks_per_line
  lines: 111-144
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_dispatches_on_qname_path_or_show_source
  lines: 152-174
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_advertises_show_source_arg
  lines: 177-190
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_qname_detection_excludes_urls_and_drives
  lines: 193-211
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_emits_telemetry_from_typescript
  lines: 214-244
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_appends_telemetry_atomically
  lines: 247-264
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_handles_absolute_paths
  lines: 267-288
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_advertises_full_arg
  lines: 291-307
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_emits_compact_renderer
  lines: 310-329
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_read_override_full_mode_trims_for_agent
  lines: 332-354
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_trie_read_obsolete_file_removed_on_apply
  lines: 357-382
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_trie_trace_obsolete_file_removed_on_apply
  lines: 385-408
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_obsolete_cleanup_is_noop_on_fresh_install
  lines: 411-426
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_install_is_idempotent_on_identical_content
  lines: 434-459
- kind: function
  qualified_name: tests/test_tool_override_install:test_opencode_install_updates_on_drift
  lines: 462-487
- kind: function
  qualified_name: tests/test_tool_override_install:test_claude_code_install_creates_advisory_hook
  lines: 495-522
- kind: function
  qualified_name: tests/test_tool_override_install:test_claude_code_hook_does_not_deny_grep
  lines: 525-539
- kind: function
  qualified_name: tests/test_tool_override_install:test_unsupported_harnesses_emit_needs_manual_setup
  lines: 551-569
- kind: function
  qualified_name: tests/test_tool_override_install:test_install_for_opencode_and_claude_code_in_one_pass
  lines: 577-590
- kind: function
  qualified_name: tests/test_tool_override_install:test_print_only_does_not_write_anything
  lines: 598-619
- kind: function
  qualified_name: tests/test_tool_override_install:test_dry_run_does_not_write_when_file_already_correct
  lines: 622-642
- kind: function
  qualified_name: tests/test_tool_override_install:test_install_with_empty_target_names_raises
  lines: 650-657
- kind: function
  qualified_name: tests/test_tool_override_install:test_install_with_unknown_target_raises
  lines: 660-674
- kind: function
  qualified_name: tests/test_tool_override_install:test_apply_one_uses_needs_manual_setup_for_targets_with_no_files
  lines: 677-686
- kind: function
  qualified_name: tests/test_tool_override_install:test_rendered_tools_relay_both_streams_on_failure
  lines: 689-701
incoming_refs: 0
outgoing_refs: 31
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
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_install_creates_override_files fingerprint=a76f5ca0678b5f670b5e59832755d9e6d80531e6d259acbd2b2596c1bc5c98e6 body_fp=72eb7c743d87ae416f2d1fd714ffd49501470822e9b40d57ab40e5e09e22acf5 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=agent-integration -->
Verifies that opencode tool override install writes 11 TypeScript files to `.opencode/tools/`.

- Asserts presence of 3 original tools: `grep.ts`, `read.ts`, `trace.ts`
- Asserts presence of 8 extended tools: various grep/explain/trace variants
- Confirms all written files exist on disk after installation
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_grep_override_routes_to_trie_grep fingerprint=bbea07bffaf1433c02906416587d0a3e71ec2c83fa56a0b8271f44f15358bcad body_fp=ae8e058afcf08fde3d7bb72270917fde2039b7ee50aec6ee4d3638d868ec2f45 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
Verifies that opencode's generated `grep.ts` override file contains the correct shell command to route agent grep calls to the trie CLI.

- Checks for `Bun.spawn(["trie"` and `"grep"` in the generated TypeScript file
- Ensures plain-text output mode (no `--json` flag present)
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_files_carry_generated_notice fingerprint=931d1963484293165d869cff6a475b7e1d05914d8997dda1eaf105ae35b037c2 body_fp=afea41a107efb867b3015a4641ceeb3925cbc43ea629efc53b2296dfe1e35255 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
Verifies that opencode tool override files contain warning headers identifying them as auto-generated artifacts.

- Checks for "Auto-generated by `trie setup" and "Do not hand-edit" markers in each file
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_rendered_files_have_balanced_backticks_per_line fingerprint=c22887ae666f1fc4d321d98ed8f41a4dfc374393f6e4860b7221b77820fca28c body_fp=ee0f5380afece166746869ce4fcfd0d27d6ed66ea6edc4c1c81c49145d29c998 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=agent-integration -->
Validates rendered TypeScript files have even backtick counts in comment lines to prevent template literal parsing errors.

- Prevents a regression where Python `\n` escapes in TS comments split lines and break bun's parser
- Checks all comment lines (starting with `//`) have zero or even backtick counts
- Guards against stray template literals that would silently kill opencode tool registration
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_dispatches_on_qname_path_or_show_source fingerprint=5384e61804c60a7be83e0410d6ad2d4ddc1952c652578811a894ea1bb18859e4 body_fp=ef3be1d51a55d292d92125cd792f6cdf91b144647cff4d1ea55144ad6e865c88 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
Verifies opencode read.ts override contains dispatch logic for three modes: qname routing to trie CLI, triefact lookup by path, and raw source via show_source.

- Installs opencode target and reads generated read.ts file content
- Asserts qname dispatch markers: looksLikeQname function and "read" command without --json
- Asserts triefact mode markers: readTriefact function and triefacts reference
- Asserts show_source mode markers: show_source parameter and readSourceFile function
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_advertises_show_source_arg fingerprint=d377a5b4a375cac89dd0bf1a263a6901952e353291915687374f1447324c8283 body_fp=c3ebb8744b3a54cc17aa1111146620db6fc3f69bd078936bbcb627bcdf1747f9 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
Verifies that opencode's read.ts override exposes show_source, offset, and limit arguments in its schema for raw source fallback.

- `show_source`: escape hatch to bypass triefact lookup and return raw file content
- `offset`, `limit`: line range parameters for the raw source mode
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_qname_detection_excludes_urls_and_drives fingerprint=a31e56fc088c1052530734293a7a78524443e45fac5d3e70153bda3a342a1916 body_fp=4167794636b5cf799ae98061480668e85e30a24c037f5fe09e3e4b5086242b51 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
Verifies that opencode's `read.ts` override correctly excludes URLs and Windows drive paths from qname detection.

- Checks that `looksLikeQname` function distinguishes qualified names from URLs (`://`) and Windows drives (`[A-Za-z]:`)
- Prevents false positives where colon-containing paths get misrouted to `trie read` instead of file system access
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_emits_telemetry_from_typescript fingerprint=7f8c4fed8e631923f71efea317df78da8411d4c17e61bd0e528cb429666e563b body_fp=3a49ce4391705fcf7bad1494c2bdcf8246ee0345ab74490e708b3a9e87c5e8cb source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
Validates that opencode's `read.ts` override embeds TypeScript-side telemetry for in-process dispatch modes.

- Checks rendered template contains telemetry helpers: `emitTelemetry`, `resolveTelemetryConfig`, `extractTomlSection`
- Verifies baked-in event structure includes `cli_call` event name, `read` tool name, and `mode` field
- Ensures TRIE_DEBUG environment variable support matches Python implementation
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_appends_telemetry_atomically fingerprint=4392ac7d6c58ee986401da04b6a844b5e514681cd33a94fed47d3360195fa4f2 body_fp=32532a8be6f1f06818b95407daa72313669b6df5867fdb87e386c2e4a826e9db source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=agent-integration -->
Tests that opencode's read.ts override uses atomic append-mode I/O for telemetry logging.

- Verifies `appendFile` is imported and used from `node:fs/promises`
- Ensures no read-then-write pattern that could create race conditions
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_handles_absolute_paths fingerprint=331fc83490b3d1f8cf59065f4c0128e7d3321e595ed45c4912a282848cf2c585 body_fp=0f61ea7bb3220a8578f0fd4d091b59e19436edd2e12de9020142827c840786fe source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=agent-integration -->
Tests that the opencode read.ts override correctly handles absolute paths without breaking Node.js path resolution.

- Verifies `resolveAbsolutePath` helper exists and uses `isAbsolute(path)` branching logic
- Checks that absolute paths bypass cwd joining to prevent path mangling
- Confirms `projectRelativePath` helper handles absolute paths within project tree
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_advertises_full_arg fingerprint=005cdc6c3d94967f1d1afa9f90580144130596b3eae9e920da25a090a43812dd body_fp=75d07d20614191c68241ef5462ba054afbdb5bc66b696af8f649b5a4ae8a1489 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
Verifies opencode's read.ts override includes a `full` parameter to escape compact mode defaults.

- Checks for `full: tool.schema` in the generated TypeScript
- Ensures the description mentions "compact" so agents understand the default behavior
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_emits_compact_renderer fingerprint=5695f91271e789440ef43b5a770758ef6502837591c372a78ebe8aa3c93de99a body_fp=72f633c2541900c125a80290f375c0120b741bd46e114642f68c3494b732cd49 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
Verifies opencode's read.ts override includes compact rendering helpers and telemetry mode tags.

- Checks for presence of `renderCompact`, `parseFrontMatter`, and `extractSections` functions
- Validates telemetry mode tags `triefact_compact` and `triefact_full` are emitted
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_read_override_full_mode_trims_for_agent fingerprint=d16eec00436dccc69af73d191648d1d6ccfaa708532d5301f331e513bd01bf08 body_fp=0b514d273f785e660f3d1093722262d338660c3ad3786f2c4afc75b3b1d74c28 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
Verifies that opencode's `read.ts` override strips internal metadata from triefacts in full mode.

- Checks for `renderForAgent`, `stripSentinels`, and `renderFrontMatterForAgent` helper functions
- Ensures full mode calls `renderForAgent(triefact)` instead of returning raw triefact
- Prevents regression where full mode leaked raw `.md` with frontmatter and sentinels
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_trie_read_obsolete_file_removed_on_apply fingerprint=9b1d5f8b5a30c80327e621908e7e53850a244638429671af0c96104d234129fb body_fp=52c69d074c2901e52af247aeaf1d4ce6a42af11dd217a38635829df6bf057f6b source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=agent-integration -->
Tests that trie setup automatically removes obsolete `trie_read.ts` files when applying opencode tool overrides.

- Creates a stale `trie_read.ts` file then verifies setup removes it during installation
- Asserts cleanup action appears in plan results with "removed obsolete" description  
- Validates new `read.ts` override subsumes the old separate tool's functionality
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_trie_trace_obsolete_file_removed_on_apply fingerprint=1e6177df323fce1c409ce9b59f17140642922fad4f84cf0e0083388b293e4581 body_fp=ea19cb8019b51e6a15e817233c7f52ae5735324bcc3226d142dd2ed31c5f9085 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=agent-integration -->
Tests that obsolete `trie_trace.ts` is removed when re-running opencode tool override installation.

- Creates stale `.opencode/tools/trie_trace.ts` file to simulate prior installation
- Verifies file is deleted and cleanup result shows "updated" action with "removed obsolete" description
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_obsolete_cleanup_is_noop_on_fresh_install fingerprint=04ec87c8983682f3c5d287e359bb0d00e26fb2b3059928626ca6aa13c0d16dd4 body_fp=6d51e41ec6557503d78617b7533223d60b96561f3333760d888e899ea153e7d0 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=agent-integration -->
Verifies that first-time opencode installs skip cleanup of non-existent obsolete files without errors.

- Asserts cleanup results report "skipped" action with "nothing to clean up" detail
- Guards against errors when attempting to remove files that were never created
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_install_is_idempotent_on_identical_content fingerprint=87fc921b24fd75af74ee18291121a61336a1480d8b0b133629f017c95411a5fd body_fp=d520cbfd09f5a82cc5c3a17ec3137f207cd4b00490563781141c92e767cc3db9 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
Tests that `install()` skips file writes when content hasn't changed.

- Runs install twice on same project, verifies second run reports `skipped` for all files
- Non-obsolete files must report "same contents" in detail field
- Validates idempotency behavior that makes `trie setup` safe to run repeatedly
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_opencode_install_updates_on_drift fingerprint=1598b027eb6c27bf0e21de5bea19063974caf4a976a86c98938412a210e0b5a3 body_fp=8221fd54fdcc67e11764771cae52766cf1845a359d3a2064fbbe87997078aa86 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
Verifies that opencode install detects and overwrites manually-edited generated files to prevent stale routing.

- Runs initial install, manually edits `grep.ts`, then runs second install
- Asserts second install reports `updated` action and restores auto-generated content
- Guards against stale wrapper files silently routing agents to wrong destinations
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_claude_code_install_creates_advisory_hook fingerprint=001f1ffd25598478bcd3b656b515e9b5491e5d2c8d41899e6ddbad20f3a76c36 body_fp=55b7dd4917b8bd77dbb5d56eaecab746135ac2acd74f9b17c3e7f66c64f945a2 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
Tests that Claude Code install creates the advisory hook file at `.claude/hooks/trie-tools.json` with correct PreToolUse structure.

- Verifies hook file exists and contains proper JSON schema for Claude Code
- Asserts hook targets built-in "Grep" tool with exact string match
- Confirms hook command contains "systemMessage" and references "mcp__trie__grep"
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_claude_code_hook_does_not_deny_grep fingerprint=b0917350ef7add9adf24564bb8f967df64c94de5affe02776d3be2f57ce39bcf body_fp=01095e1ed30a5bb8d4873946159f0566e6d08c9e8d52906f7bef134ba198169a source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=agent-integration -->
Verifies that Claude Code's trie tools hook remains advisory-only and does not block built-in Grep usage.

- Ensures rendered hook JSON contains no `permissionDecision` or `"deny"` strings
- Guards against accidental conversion from advisory to blocking behavior
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_unsupported_harnesses_emit_needs_manual_setup fingerprint=252d564de8cef912137183a246a83c8734777cfbd60c0a79917aab425762c512 body_fp=54fa0462bfe8a49cc91903dd2412ac1fa30e66c416d8ce686d7a24db59583ecf source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
Verifies unsupported harnesses return `needs_manual_setup` with instructions instead of silently skipping.

- Tests each harness slug: claude-desktop, cursor, windsurf, vscode, codex
- Confirms no files written to disk when automation isn't possible
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_install_for_opencode_and_claude_code_in_one_pass fingerprint=e5a91b31de3c5d2716c71642ee28352e70962a865fe3310f85e696ab6d40c562 body_fp=d464e32315b30bc07e630f8ef2e424e53b8ee7977f2e3fa18a70c609c436d3d4 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
Tests that `install()` can process multiple targets in a single call, verifying both opencode and claude-code files are written independently.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_print_only_does_not_write_anything fingerprint=195068d913203efa2f7a33563f5b2d88d92ce6ddea2f47b5768362fab4701a4b body_fp=e9aa49047873590142dc66022fbdd155db51f09b18f3d5b6eeefc4f16d2aa627 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
Verifies that `--print-only` mode prevents disk writes and returns preview results with rendered file contents.

- Confirms `.opencode` directory is never created during preview
- Validates write operations report `preview` action with content in `detail`
- Distinguishes between preview-eligible file writes and skipped obsolete cleanups
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_dry_run_does_not_write_when_file_already_correct fingerprint=97dd083d6cfe5d0fce2cf74184a64b3a1581bdb594a76cf69b3fe2c183f8370c body_fp=0fec4ac8832fb4c714bad2a7e39722d4fbc81a38e7bc6790a846fc138a32f570 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test-infrastructure -->
Verifies that `--dry-run` returns `skipped` when files already match expected content.

- Creates files with first install, then runs second install with `dry_run=True`
- Asserts second install reports `skipped` action since no changes needed
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_install_with_empty_target_names_raises fingerprint=de0258da2c32f2c009bcd96277b319ba9b02d3ed14cff07f8674efeaf77483ba body_fp=804951ad161ebcc915d375adfbb8d7aabffc0fd1e0c701fd77153f758c6823a6 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test -->
Tests that `install` raises `ToolOverrideInstallError` when called with empty or null target names.

- Verifies both `[]` and `None` as invalid inputs trigger the exception
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_install_with_unknown_target_raises fingerprint=572c2b692bcbb73e70155902d114481a3ce552681a94400872b8619403e3456e body_fp=787cd2ca6b03d2b1016d534da86a9ae319c57544ba0db1f31c8e903e3799db63 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test -->
Verifies `install()` raises `ToolOverrideInstallError` for unknown target names.

- Checks error message includes the invalid target name
- Verifies error message lists valid options for fixing typos
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_apply_one_uses_needs_manual_setup_for_targets_with_no_files fingerprint=f33b7ea65004cd19d365772957c29eacf6c1e64c4485bb643ac88dc9fb8692c1 body_fp=7aad40739435e62250b4adbbbed514620510ddc00a5437067260c9c1bfea6439 source_ref=c2731124701c9a5f3a8f683a4cc84d0be1fc6b27 role=test -->
Tests that `apply_one` returns `needs_manual_setup` for targets with empty file tuples.

- Verifies harnesses with only manual instructions return appropriate action without disk writes
- Ensures consistent behavior with `hook_install.apply_one` for similar target shapes
<!-- trie:end -->
<!-- trie:section symbol=tests/test_tool_override_install:test_rendered_tools_relay_both_streams_on_failure fingerprint=5545acc4b20798092b016b8c47735b01af594ea2289600b95613073bdf8e1bfb body_fp=48aa76b43f74ce36378b7d26f861548660a50b7c21eb06b69be60415952a6297 source_ref=25e5de83b30ad677b72d5c9c11521ac289b6e9f6 role=test -->
Regression test asserting that all rendered opencode `.ts` tool templates join both `stderr` and `stdout` on failure rather than silently dropping one stream.
<!-- trie:end -->