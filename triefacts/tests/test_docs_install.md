---
trie_version: 0.3.0
source: tests/test_docs_install.py
file_fingerprint: a6c0c9184c84d1fa0f87ff4208203e20262cdf4498c7c8c555ac494d56a88c0a
last_synced_at: '2026-08-01T09:20:24Z'
description: 'Tests for `trie.docs_install`: project-local agent documentation install.'
defines:
- kind: module
  qualified_name: tests/test_docs_install:__module__
  lines: 1-457
- kind: function
  qualified_name: tests/test_docs_install:test_install_creates_trie_md_at_project_root
  lines: 39-56
  signature: 'def test_install_creates_trie_md_at_project_root(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_docs_install:test_install_trie_md_is_idempotent_on_identical_content
  lines: 59-69
  signature: 'def test_install_trie_md_is_idempotent_on_identical_content(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_docs_install:test_install_trie_md_updates_on_drift
  lines: 72-83
  signature: 'def test_install_trie_md_updates_on_drift(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_docs_install:test_install_skips_pointer_when_agent_files_absent
  lines: 91-102
  signature: 'def test_install_skips_pointer_when_agent_files_absent(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_docs_install:test_install_appends_pointer_to_existing_agents_md
  lines: 105-119
  signature: 'def test_install_appends_pointer_to_existing_agents_md(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_docs_install:test_install_appends_pointer_to_existing_claude_md
  lines: 122-130
  signature: 'def test_install_appends_pointer_to_existing_claude_md(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_docs_install:test_install_handles_both_agents_and_claude_files
  lines: 133-145
  signature: 'def test_install_handles_both_agents_and_claude_files(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_docs_install:test_install_pointer_is_idempotent
  lines: 148-155
  signature: 'def test_install_pointer_is_idempotent(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_docs_install:test_install_refreshes_stale_pointer_block_in_place
  lines: 158-177
  signature: 'def test_install_refreshes_stale_pointer_block_in_place(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_docs_install:test_print_only_does_not_write_anything
  lines: 185-195
  signature: 'def test_print_only_does_not_write_anything(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_docs_install:test_dry_run_does_not_write_when_file_already_correct
  lines: 198-207
  signature: 'def test_dry_run_does_not_write_when_file_already_correct(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_docs_install:test_splice_appends_when_marker_absent
  lines: 215-225
  signature: 'def test_splice_appends_when_marker_absent(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_docs_install:test_splice_replaces_when_marker_present
  lines: 228-239
  signature: def test_splice_replaces_when_marker_present()
- kind: function
  qualified_name: tests/test_docs_install:test_splice_handles_empty_input
  lines: 242-246
  signature: def test_splice_handles_empty_input()
- kind: function
  qualified_name: tests/test_docs_install:test_agent_doc_files_covers_known_conventions
  lines: 254-258
  signature: def test_agent_doc_files_covers_known_conventions()
- kind: function
  qualified_name: tests/test_docs_install:test_install_with_no_target_renders_bare_tool_names
  lines: 266-280
  signature: 'def test_install_with_no_target_renders_bare_tool_names(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_docs_install:test_install_for_claude_code_uses_mcp_double_underscore_prefix
  lines: 283-304
  signature: 'def test_install_for_claude_code_uses_mcp_double_underscore_prefix(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_docs_install:test_install_for_opencode_uses_bare_tool_names
  lines: 307-322
  signature: 'def test_install_for_opencode_uses_bare_tool_names(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_docs_install:test_install_unknown_target_falls_back_to_bare_names
  lines: 325-338
  signature: 'def test_install_unknown_target_falls_back_to_bare_names(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_docs_install:test_install_pointer_block_uses_target_specific_names
  lines: 341-356
  signature: 'def test_install_pointer_block_uses_target_specific_names(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_docs_install:test_install_multiple_targets_renders_primary_in_body_and_footer_for_rest
  lines: 359-381
  signature: 'def test_install_multiple_targets_renders_primary_in_body_and_footer_for_rest( tmp_path: Path, )'
- kind: function
  qualified_name: tests/test_docs_install:test_install_prefers_override_target_for_body_regardless_of_order
  lines: 384-415
  signature: 'def test_install_prefers_override_target_for_body_regardless_of_order(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_docs_install:test_install_single_target_omits_multi_target_footer
  lines: 418-430
  signature: 'def test_install_single_target_omits_multi_target_footer(tmp_path: Path)'
- kind: function
  qualified_name: tests/test_docs_install:test_install_re_render_on_target_change_is_an_update
  lines: 433-456
  signature: 'def test_install_re_render_on_target_change_is_an_update(tmp_path: Path)'
incoming_refs: 0
outgoing_refs: 51
---
<!-- trie:section symbol=tests/test_docs_install:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=979a2a513c2e3dac97af37a8ecfe5bfa16220224016adc3aaaf5edd7e2126fa2 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test-infrastructure -->
Tests for the `trie.docs_install` module, covering TRIE.md creation, pointer block splicing into AGENTS.md/CLAUDE.md, idempotency behavior, dry-run modes, and target-specific tool name rendering.

- Tests verify that `install()` creates TRIE.md with bundled content and generated-file notice
- Tests confirm pointer blocks are added to existing AGENTS.md/CLAUDE.md files but missing files aren't created
- Tests validate idempotent behavior where repeated installs skip unchanged files
- Tests check that stale pointer blocks are refreshed in-place while preserving surrounding content
- Tests ensure `--print-only` and `--dry-run` modes never write files
- Tests verify target-specific tool name rendering (bare names vs mcp__trie__ prefixes)
- Tests cover multi-target scenarios with footer disambiguation
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_creates_trie_md_at_project_root fingerprint=1ca777c40bf216d807d7f5704fbd185369a54c3b665fda9e05e8e3059e8709cf body_fp=b89234d25debda862f6172e50934876e2f0634b1fa4c75f831d735949f57f903 source_ref=987e7c5525420b87f12a6d301d18b4284b76f1c1 role=test -->
## `def test_install_creates_trie_md_at_project_root(tmp_path: Path)`

Verifies that `install` creates TRIE.md at project root with bundled content and generated-file notice.

- Checks file exists with non-empty body containing "Generated by `trie setup`" marker
- Validates bundled documentation was loaded by checking for "Using Trie" title
- Confirms install plan reports "created" action for the file
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_trie_md_is_idempotent_on_identical_content fingerprint=9a9ced828f73aac923952bd22feb3a1b00633950073a88be0eaa407d8bd6383a body_fp=53b92a75a86cdc6d25c8548d4f314b601a7d9442cb78eb113d9374de360cd771 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test -->
## `def test_install_trie_md_is_idempotent_on_identical_content(tmp_path: Path)`

Verifies that running `install` twice on the same project returns `skipped` action when TRIE.md is unchanged.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_trie_md_updates_on_drift fingerprint=7cb9eea5a1569961f77f8e766cb7907a7559ad850560aa17215a5aa3c01e363c body_fp=066b29bac3de31721308bbabd3cff884d25b0001edd02fd62f8ffd55013e8510 source_ref=987e7c5525420b87f12a6d301d18b4284b76f1c1 role=test -->
## `def test_install_trie_md_updates_on_drift(tmp_path: Path)`

Tests that `install` rewrites TRIE.md when the on-disk file has been modified since the last installation.

- Creates temporary project directory, installs TRIE.md, corrupts the file content, then verifies reinstall updates the file
- Validates the install result shows "updated" action and restores original bundled documentation content
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_skips_pointer_when_agent_files_absent fingerprint=7f41b7e6e78039766b719d39cacd7a94043104007a0eb7e9b9d464b8cacce730 body_fp=322d696ac1c2bf230570d4601b8c13a6b5e990bf935ed1a2c3cf82545366eddb source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test -->
## `def test_install_skips_pointer_when_agent_files_absent(tmp_path: Path)`

Tests that `install` skips pointer block injection when neither AGENTS.md nor CLAUDE.md exist at project root.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_appends_pointer_to_existing_agents_md fingerprint=299c35faddd0533c804727020a8a5c4911e058caa4bd573295a8f420d24c27ba body_fp=57b9b4a41791ce070b27187ea2a2b0ec1eb9e81e83e9e34a7f7e3dae141cc519 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test -->
## `def test_install_appends_pointer_to_existing_agents_md(tmp_path: Path)`

Tests that `install()` appends a pointer block to existing AGENTS.md files while preserving user content.

- Verifies pointer markers and TRIE.md reference are added
- Confirms user content remains unchanged
- Validates pointer uses local path for offline compatibility
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_appends_pointer_to_existing_claude_md fingerprint=33c41b878ca918e62a18bf211e33173f97c94618941ed4c6ca61daee1e3f700b body_fp=8cde8113785dfc08177e003468ae89fc699f49897f050b7e1045d2c92700bdb4 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test -->
## `def test_install_appends_pointer_to_existing_claude_md(tmp_path: Path)`

Tests that `install()` adds a pointer block to existing CLAUDE.md files.

- Verifies CLAUDE.md receives the same pointer treatment as AGENTS.md
- Checks that pointer markers and TRIE.md references are properly inserted
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_handles_both_agents_and_claude_files fingerprint=3bb04dd002b2bd3364369312b092f78c214dfb7aab18010e1e452d6adf0440f3 body_fp=67fac7fd573ff726655c721900d4c37816d0ee6cd2563a0d1b038cfcef54a094 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test -->
## `def test_install_handles_both_agents_and_claude_files(tmp_path: Path)`

Verifies install() adds pointer blocks to both AGENTS.md and CLAUDE.md when both files exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_pointer_is_idempotent fingerprint=d46e62d8582e4ca22291dd24a293f1fa124e7be6fc98f4e7179dcadfb94c4b13 body_fp=46a3576e06ef90ee92774fc8c47fd853d5af6c920c7d0e1f3b06484710ca56d0 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test -->
## `def test_install_pointer_is_idempotent(tmp_path: Path)`

Tests that running install twice produces `skipped` result for existing pointer blocks.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_refreshes_stale_pointer_block_in_place fingerprint=936883fe669313ace022a049ab843aabd7f9618989175708bd378611e602acfd body_fp=fc8441a6e15ff152c2781ae2390f84344f5a0aecf28d6c729336a0404c71d878 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test -->
## `def test_install_refreshes_stale_pointer_block_in_place(tmp_path: Path)`

Tests that install replaces only the marker-delimited pointer block in existing agent documentation files.

- Creates AGENTS.md with user content surrounding a stale pointer block
- Verifies install preserves user content while updating only the pointer block content
- Confirms old pointer text is removed and new POINTER_LINE is inserted
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_print_only_does_not_write_anything fingerprint=3d616c1d20ceaa9d4fb90f483515a2b069d4d393d8ab2789057083e4e6953001 body_fp=5291104ab3bc2a1872f563a336a74e5bf28464d039412616d3c9e8b5ea07ce33 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test -->
## `def test_print_only_does_not_write_anything(tmp_path: Path)`

Tests that `install` with `print_only=True` generates a plan without writing any files to disk.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_dry_run_does_not_write_when_file_already_correct fingerprint=cf475c6d30538c0bf4597946a389e4a90cf7c8e796d457084a3ca0162180475f body_fp=42ee0b93ca231b3a534b46326ef559ffb4a91ab133a937f16219e3338481d388 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test -->
## `def test_dry_run_does_not_write_when_file_already_correct(tmp_path: Path)`

Verifies dry-run mode reports `skipped` when target files match expected content without writing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_splice_appends_when_marker_absent fingerprint=205b8edad0c258f4bbe09a41ebbe06c14452a736cd557df2ed59dd752db87aa2 body_fp=73cdf58fb1fc0d182bb11229a664051ad6e7ccb22a18c8adba4b2c2ff10ebfe4 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test -->
## `def test_splice_appends_when_marker_absent(tmp_path: Path)`

Tests that `_splice_pointer_block` appends pointer markers when none exist, preserving original content and avoiding extra blank lines.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_splice_replaces_when_marker_present fingerprint=cb17cac81bcfab095b782d945f82fb285ef15e5283112c5d4ff29c72929208b7 body_fp=fb816100eb2980a203800c35b44ab622ae9e5a378b0d3440a59baa9eee7e016b source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test -->
## `def test_splice_replaces_when_marker_present()`

Verifies `_splice_pointer_block` replaces content between existing markers without duplication.

- Tests that old pointer content is removed and replaced with current pointer
- Ensures only one marker pair exists after replacement
- Confirms surrounding user content remains intact
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_splice_handles_empty_input fingerprint=30701c07c06462fd811f4af402b6f22d730ef0ef27b4ea2b11b6b97a6c67aa9a body_fp=58dad64453879d18a2ce7f68ac37b3ec39a32176e727bbfa0005e11af4d613ad source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test -->
## `def test_splice_handles_empty_input()`

Tests that `_splice_pointer_block` handles empty input by returning only the pointer block without leading blank lines.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_agent_doc_files_covers_known_conventions fingerprint=4d9b70824755d5d8b83a37286588a8d52c99d0f08a3bb8cc31f58d3bac55e121 body_fp=303a686ea9462cbbd8da063ac31790771a01e6d47506cd6c3d4cf08ca57c7f6f source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test -->
## `def test_agent_doc_files_covers_known_conventions()`

Asserts AGENT_DOC_FILES equals the expected tuple of agent documentation filenames.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_with_no_target_renders_bare_tool_names fingerprint=fb44134da3aa120acd2c8813e1479bd3500b11ea95a551ea66697bec3e04cb5a body_fp=2279138a98438fb67f9bcd60fecaad0ea99196d6f53355a17cf940535bb00818 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test -->
## `def test_install_with_no_target_renders_bare_tool_names(tmp_path: Path)`

Verifies that install with no target parameter renders bare tool names in TRIE.md without harness prefixes.

- Checks placeholder tokens are completely substituted out 
- Confirms `grep`, `read`, `trace` appear as bare tool names in documentation
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_for_claude_code_uses_mcp_double_underscore_prefix fingerprint=2629d7ed16832df3abd883531d6329f54001eb1c060921162a08394c53fbfbb4 body_fp=e43b35426c1c544998fdf149165632e772eb9f1d81a7fa9521f898de6510c3e2 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test -->
## `def test_install_for_claude_code_uses_mcp_double_underscore_prefix(tmp_path: Path)`

Verifies that `install` with `target_names=["claude-code"]` renders tool names as `mcp__trie__<tool>` in TRIE.md body.

- Checks for `mcp__trie__grep`, `mcp__trie__read`, and `mcp__trie__trace` in generated content
- Ensures placeholder tokens like `«grep»` are fully substituted out
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_for_opencode_uses_bare_tool_names fingerprint=a29cc89ae0deac1cada85e8f6f38f7866374a9887c407b5294e0f055d3bdeaa1 body_fp=44e8983f1a4011147a5117d420ab813584345a22a9c48d80a326918419157db7 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test -->
## `def test_install_for_opencode_uses_bare_tool_names(tmp_path: Path)`

Tests that `install` with `opencode` target uses bare tool names in generated TRIE.md content.

- Verifies that prefixed names like `trie_grep` are not present
- Confirms bare names `grep`, `read`, `trace` appear in the documentation
- Ensures template tokens like `«grep»` are properly substituted
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_unknown_target_falls_back_to_bare_names fingerprint=8dc34e858b445570e9f034ad3c01247ba1aafcc6cf8bacfca76855fcdc499d65 body_fp=51e08c8a77b28a1c9ab8dfcda6a9824816563c54bfcbf5a1ff693a08e5199f8d source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test -->
## `def test_install_unknown_target_falls_back_to_bare_names(tmp_path: Path)`

Verifies install with unknown target name falls back to bare tool names and doesn't crash.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_pointer_block_uses_target_specific_names fingerprint=36f1eed4451bda0e06df74720cd065d70d775a68ed604a9a92a35e0bc2cad263 body_fp=371e3ad31ab22a937ca0e12641a6f5446e59e0ee48379bba7563a70b2d2c60aa source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test -->
## `def test_install_pointer_block_uses_target_specific_names(tmp_path: Path)`

Tests that install writes target-specific tool names in AGENTS.md pointer blocks.

- Creates AGENTS.md and runs install with claude-code target
- Verifies pointer block contains mcp__trie__ prefixed tool names matching agent's tool list
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_multiple_targets_renders_primary_in_body_and_footer_for_rest fingerprint=f00600099a2512515bf1c05ea63e546068546374be5e36bfc0189aeb2526101a body_fp=32dbb57eb5489444b690d7cd2e095af1b15e36b6a880fef3f74de8974f5edf47 source_ref=021ab1f8d935a6154fc29488d3c5afa6a1219147 role=test -->
## `def test_install_multiple_targets_renders_primary_in_body_and_footer_for_rest( tmp_path: Path, )`

Tests that install with multiple targets renders the override harness (opencode) names in the body and secondary targets in the footer.

- Verifies override target (opencode) bare names dominate the main TRIE.md body, not MCP-prefixed names
- Confirms footer section lists alternative tool names (e.g. `mcp__trie__grep`) for other harnesses
- Ensures single TRIE.md handles multi-agent scenarios, preferring override harness regardless of detection order
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_prefers_override_target_for_body_regardless_of_order fingerprint=078484d26b2e92f06588416824d63d4e410ae40e238f71bb8cf874bf72fa02a6 body_fp=ac5e7e938bc7abc022cf22c3bff43132e49f4b735d5bad4a6972b17e54a48725 source_ref=021ab1f8d935a6154fc29488d3c5afa6a1219147 role=test -->
## `def test_install_prefers_override_target_for_body_regardless_of_order(tmp_path: Path)`

Regression test asserting that `install` always renders bare override tool names in the TRIE.md body regardless of target detection order, and that AGENTS.md pointer also uses bare names when an override harness (opencode) is present alongside a prefixed harness (claude-code).
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_single_target_omits_multi_target_footer fingerprint=48e4895b63d616d714fe313ed1185b050e760f6dfb0aa64e9a73d6081ff375ae body_fp=c7568ee80103a8bbab5790801b0641e0edf889d57354cc5e59997a0ae611c024 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test -->
## `def test_install_single_target_omits_multi_target_footer(tmp_path: Path)`

Verifies that `install` omits the multi-target footer when only one target is specified.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_re_render_on_target_change_is_an_update fingerprint=e2be5e875fe2c7e81504d6cdd617417a1d724b944d2092315ea56323dcc5fd1d body_fp=098d70d4c6741e1f6fa11f273cd680cf547e238d9ee6959a8955c0c36308ee28 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test -->
## `def test_install_re_render_on_target_change_is_an_update(tmp_path: Path)`

Verifies that changing target names between installs triggers an update action, not a skip.

- Runs install twice with different target_names to ensure TRIE.md gets rewritten with new tool names
- Confirms second install returns "updated" action rather than "skipped"
- Validates old tool names are replaced with target-specific prefixed names
<!-- trie:end -->