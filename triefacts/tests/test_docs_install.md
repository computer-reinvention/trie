---
trie_version: 0.1.5
source: tests/test_docs_install.py
file_fingerprint: 612d52ed0d41bd1438627a21efab404e22edca595ae18169882a7c75b143b312
last_synced_at: '2026-06-06T13:17:04Z'
description: 'Tests for `trie.docs_install`: project-local agent documentation install.'
defines:
- kind: module
  qualified_name: tests/test_docs_install:__module__
  lines: 1-421
- kind: function
  qualified_name: tests/test_docs_install:test_install_creates_trie_md_at_project_root
  lines: 39-56
- kind: function
  qualified_name: tests/test_docs_install:test_install_trie_md_is_idempotent_on_identical_content
  lines: 59-69
- kind: function
  qualified_name: tests/test_docs_install:test_install_trie_md_updates_on_drift
  lines: 72-83
- kind: function
  qualified_name: tests/test_docs_install:test_install_skips_pointer_when_agent_files_absent
  lines: 91-102
- kind: function
  qualified_name: tests/test_docs_install:test_install_appends_pointer_to_existing_agents_md
  lines: 105-119
- kind: function
  qualified_name: tests/test_docs_install:test_install_appends_pointer_to_existing_claude_md
  lines: 122-130
- kind: function
  qualified_name: tests/test_docs_install:test_install_handles_both_agents_and_claude_files
  lines: 133-145
- kind: function
  qualified_name: tests/test_docs_install:test_install_pointer_is_idempotent
  lines: 148-155
- kind: function
  qualified_name: tests/test_docs_install:test_install_refreshes_stale_pointer_block_in_place
  lines: 158-177
- kind: function
  qualified_name: tests/test_docs_install:test_print_only_does_not_write_anything
  lines: 185-195
- kind: function
  qualified_name: tests/test_docs_install:test_dry_run_does_not_write_when_file_already_correct
  lines: 198-207
- kind: function
  qualified_name: tests/test_docs_install:test_splice_appends_when_marker_absent
  lines: 215-225
- kind: function
  qualified_name: tests/test_docs_install:test_splice_replaces_when_marker_present
  lines: 228-239
- kind: function
  qualified_name: tests/test_docs_install:test_splice_handles_empty_input
  lines: 242-246
- kind: function
  qualified_name: tests/test_docs_install:test_agent_doc_files_covers_known_conventions
  lines: 254-258
- kind: function
  qualified_name: tests/test_docs_install:test_install_with_no_target_renders_bare_tool_names
  lines: 266-280
- kind: function
  qualified_name: tests/test_docs_install:test_install_for_claude_code_uses_mcp_double_underscore_prefix
  lines: 283-304
- kind: function
  qualified_name: tests/test_docs_install:test_install_for_opencode_uses_bare_tool_names
  lines: 307-322
- kind: function
  qualified_name: tests/test_docs_install:test_install_unknown_target_falls_back_to_bare_names
  lines: 325-338
- kind: function
  qualified_name: tests/test_docs_install:test_install_pointer_block_uses_target_specific_names
  lines: 341-356
- kind: function
  qualified_name: tests/test_docs_install:test_install_multiple_targets_renders_primary_in_body_and_footer_for_rest
  lines: 359-379
- kind: function
  qualified_name: tests/test_docs_install:test_install_single_target_omits_multi_target_footer
  lines: 382-394
- kind: function
  qualified_name: tests/test_docs_install:test_install_re_render_on_target_change_is_an_update
  lines: 397-420
incoming_refs: 0
outgoing_refs: 49
---
<!-- trie:section symbol=tests/test_docs_install:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=3ed7cf662be97aecc713973592ba7d08076c370863fa70e35521e2f4e78beb60 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test-infrastructure -->
Tests for `trie.docs_install` module covering TRIE.md materialisation, pointer block injection into AGENTS.md/CLAUDE.md, idempotency, dry-run behavior, and target-specific tool name rendering.

- Validates TRIE.md creation at project root with generated-file notice
- Tests pointer block appending/updating in existing agent documentation files  
- Verifies idempotent behavior when content already matches canonical form
- Covers print-only/dry-run modes that preview changes without writing files
- Tests tool name substitution for different MCP harnesses (claude-code, opencode)
- Includes direct tests of internal `_splice_pointer_block` function
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_creates_trie_md_at_project_root fingerprint=3bf0b6ba7aa8e85d0365130e62db162887b6ef7f9c00019abee9ee2b354708e6 body_fp=30c8a4655867992c696ba7eb54645072f252f990760188d34d9ba8b2c98d2d0e source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test-infrastructure -->
Verifies that `install()` creates `TRIE.md` at project root with generated-file notice and bundled documentation content.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_trie_md_is_idempotent_on_identical_content fingerprint=9a9ced828f73aac923952bd22feb3a1b00633950073a88be0eaa407d8bd6383a body_fp=c5668e80abf45fb68f2cfb8d0d4673bdb431341b2a1ca9f30e5565395b6764b1 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test-infrastructure -->
Verifies that `install` correctly skips writing TRIE.md when content hasn't changed between runs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_trie_md_updates_on_drift fingerprint=2db466ed1d7ad9b8890e976dce1c128679f8b06880d9ea46651be09068d0e8de body_fp=e51d245eafd6e4b19c600891e7e8092ed94b53ffce2be19871acb677c1d40221 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=agent-integration -->
Verifies install rewrites TRIE.md when content drifts from bundled documentation template.

- Creates initial TRIE.md, corrupts it with invalid content, then confirms second install updates file
- Asserts result action is "updated" and final content matches bundled body with "Using trie" text
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_skips_pointer_when_agent_files_absent fingerprint=7f41b7e6e78039766b719d39cacd7a94043104007a0eb7e9b9d464b8cacce730 body_fp=42cf96c1a8a1216c40e909e34bbfdafd273c3d7628874268862ff62f0213b823 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=agent-integration -->
Tests that install skips creating AGENTS.md/CLAUDE.md when they don't exist, only writing TRIE.md.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_appends_pointer_to_existing_agents_md fingerprint=299c35faddd0533c804727020a8a5c4911e058caa4bd573295a8f420d24c27ba body_fp=812ca8ff80787c90e30164bf9b239017522d162cc4250d36e45dec9b1d5a4851 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test-infrastructure -->
Tests that `install` appends a pointer block to existing AGENTS.md while preserving user content.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_appends_pointer_to_existing_claude_md fingerprint=33c41b878ca918e62a18bf211e33173f97c94618941ed4c6ca61daee1e3f700b body_fp=7337d5807f3c504aaf01c04a2c0d0d054edc0e685d3bb5cf87edc0ef5c5e1278 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=agent-integration -->
Verifies that install() appends a pointer block to existing CLAUDE.md files.

- Creates CLAUDE.md with initial content, runs install(), then confirms the pointer markers and TRIE.md reference are present
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_handles_both_agents_and_claude_files fingerprint=3bb04dd002b2bd3364369312b092f78c214dfb7aab18010e1e452d6adf0440f3 body_fp=f6aa14147c723d8ca9f294537c58293dd0a5339b69381e09c4aa9d73d6e3abb9 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test-infrastructure -->
Verifies that install adds pointer blocks to both AGENTS.md and CLAUDE.md when both files exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_pointer_is_idempotent fingerprint=d46e62d8582e4ca22291dd24a293f1fa124e7be6fc98f4e7179dcadfb94c4b13 body_fp=65dfdc873337862bfd749462a309cfa10f7325dc737e26ef36d6d50d65f18739 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test-infrastructure -->
Tests that repeated installs on identical AGENTS.md pointer blocks report "skipped" action.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_refreshes_stale_pointer_block_in_place fingerprint=936883fe669313ace022a049ab843aabd7f9618989175708bd378611e602acfd body_fp=72ff1383e601cf34ebba5ca0e275a593038551d220867366b260eb7b10b00e5d source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=agent-integration -->
Tests that `install` replaces stale pointer blocks in-place while preserving surrounding user content.

- Creates AGENTS.md with user content above and below an outdated pointer block
- Verifies `install` updates only the marker-delimited section
- Confirms user content on both sides remains untouched
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_print_only_does_not_write_anything fingerprint=3d616c1d20ceaa9d4fb90f483515a2b069d4d393d8ab2789057083e4e6953001 body_fp=43b7d086f516a1366518c26cae23d416f9d20726e9fd894a5156615560db455d source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=agent-integration -->
Verifies that `install` with `print_only=True` performs no filesystem writes while returning preview actions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_dry_run_does_not_write_when_file_already_correct fingerprint=cf475c6d30538c0bf4597946a389e4a90cf7c8e796d457084a3ca0162180475f body_fp=80855999aba483994cdf07c128341ea6e3bfb9907bce53cafc0be65d2d688592 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=agent-integration -->
Verifies that `install` with `dry_run=True` reports `skipped` for unchanged files rather than `preview`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_splice_appends_when_marker_absent fingerprint=205b8edad0c258f4bbe09a41ebbe06c14452a736cd557df2ed59dd752db87aa2 body_fp=906d7a211856d69ab6ad0dffe4c5328be26d1505309f6255d86af820a015c16d source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test-infrastructure -->
Tests that `_splice_pointer_block` appends a pointer block with blank-line separator when no existing marker is found.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_splice_replaces_when_marker_present fingerprint=cb17cac81bcfab095b782d945f82fb285ef15e5283112c5d4ff29c72929208b7 body_fp=83985500aa640287393d80dc6abdf390082382d2e861d25f8c8a5be2f873aa26 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test-infrastructure -->
Verifies that `_splice_pointer_block` replaces existing marker blocks in place without duplicating markers.

- Tests that old content between markers is removed
- Ensures only one marker pair exists after replacement
- Confirms surrounding content is preserved unchanged
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_splice_handles_empty_input fingerprint=30701c07c06462fd811f4af402b6f22d730ef0ef27b4ea2b11b6b97a6c67aa9a body_fp=3fcc836eefe11dc830185a0aff2c328e5b5678214dce9db3d112d2e90d590224 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=agent-integration -->
Verifies `_splice_pointer_block` handles empty input by adding only the pointer block without extra blank lines.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_agent_doc_files_covers_known_conventions fingerprint=4d9b70824755d5d8b83a37286588a8d52c99d0f08a3bb8cc31f58d3bac55e121 body_fp=15c50b6089324c383f939ca053740472691d53fb31c6816fbf7d9650c94ef47c source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test-infrastructure -->
Verifies that AGENT_DOC_FILES contains exactly ("AGENTS.md", "CLAUDE.md") as supported conventions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_with_no_target_renders_bare_tool_names fingerprint=fb44134da3aa120acd2c8813e1479bd3500b11ea95a551ea66697bec3e04cb5a body_fp=2f451f4b06e8d3b8c4967f8fdb00fe9aa90fbb4df322e93ea2b3034f35410b89 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test-infrastructure -->
Verifies that install() renders bare tool names when no target is specified.

- Tests that placeholder tokens `«grep»`, `«read»`, `«trace»` are fully substituted
- Confirms bare names `grep`, `read`, `trace` appear in generated TRIE.md
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_for_claude_code_uses_mcp_double_underscore_prefix fingerprint=2629d7ed16832df3abd883531d6329f54001eb1c060921162a08394c53fbfbb4 body_fp=dd7e1aec323f1e70759d27114329215b7a65f3ff85f2b4f64b0b21613fa5e855 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=agent-integration -->
Verifies that install() with target_names=["claude-code"] renders MCP-prefixed tool names in TRIE.md body.

- Expects tool names formatted as `mcp__trie__<tool>` for Claude Code's MCP namespace convention
- Asserts placeholder tokens `«grep»` are fully substituted out of rendered documentation
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_for_opencode_uses_bare_tool_names fingerprint=a29cc89ae0deac1cada85e8f6f38f7866374a9887c407b5294e0f055d3bdeaa1 body_fp=3eb8b8070d1b35400150f45f1f2a796a4fc8e926cc4d7b3fe08f8f81feadfa81 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test-infrastructure -->
Verifies `install` renders bare tool names in TRIE.md when target is "opencode".
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_unknown_target_falls_back_to_bare_names fingerprint=8dc34e858b445570e9f034ad3c01247ba1aafcc6cf8bacfca76855fcdc499d65 body_fp=21321d6a76505e232293d736b89a8eac674f0dfa00c7ca61f95b139e24b974d7 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test-infrastructure -->
Tests that unknown target names fall back to bare tool names without errors.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_pointer_block_uses_target_specific_names fingerprint=36f1eed4451bda0e06df74720cd065d70d775a68ed604a9a92a35e0bc2cad263 body_fp=d18eab8b61044d59debde6d0536bf5a2b9291c4231db3582610d19e672e1ceee source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test-infrastructure -->
Verifies that pointer blocks in agent documentation files use target-specific tool names matching the agent's actual tool list.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_multiple_targets_renders_primary_in_body_and_footer_for_rest fingerprint=1c8049e6eb9d914828abe22ff389d3c1627c1bff5993f0f3a49b0b5b35959688 body_fp=722073c9923de8c72f9df414422b14ff1ee632fda6cbed8c582832b4e5f7dfd6 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=agent-integration -->
Tests that multiple target harnesses render primary target tool names in body and secondary targets in footer.

- Creates TRIE.md with claude-code tool names in main content
- Verifies opencode tool names appear in footer section
- Ensures multi-target footer section is present with secondary aliases
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_single_target_omits_multi_target_footer fingerprint=48e4895b63d616d714fe313ed1185b050e760f6dfb0aa64e9a73d6081ff375ae body_fp=c8929f17d141d935910e487496b377947f1f6f7ad3ea77bded9c352eee9661cb source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=test-infrastructure -->
Verifies that install() with a single target omits the multi-target footer from TRIE.md.

- Creates test with `target_names=["opencode"]`
- Asserts footer text "Tool names under other installed harnesses" is absent
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_re_render_on_target_change_is_an_update fingerprint=e2be5e875fe2c7e81504d6cdd617417a1d724b944d2092315ea56323dcc5fd1d body_fp=b05c2ea8e432cf10e7df34450106ef5e36b147c32ac168f730b3c8b6fe7a5d52 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 role=agent-integration -->
Verifies that changing target names between install runs triggers TRIE.md rewrite with updated tool references.

- First install with "opencode" target, second with "claude-code" target produces "updated" action
- Confirms old tool names removed and new MCP-prefixed names present in final content
<!-- trie:end -->

<!-- trie:section symbol=tests/test_docs_install:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=979a2a513c2e3dac97af37a8ecfe5bfa16220224016adc3aaaf5edd7e2126fa2 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Tests for the `trie.docs_install` module, covering TRIE.md creation, pointer block splicing into AGENTS.md/CLAUDE.md, idempotency behavior, dry-run modes, and target-specific tool name rendering.

- Tests verify that `install()` creates TRIE.md with bundled content and generated-file notice
- Tests confirm pointer blocks are added to existing AGENTS.md/CLAUDE.md files but missing files aren't created
- Tests validate idempotent behavior where repeated installs skip unchanged files
- Tests check that stale pointer blocks are refreshed in-place while preserving surrounding content
- Tests ensure `--print-only` and `--dry-run` modes never write files
- Tests verify target-specific tool name rendering (bare names vs mcp__trie__ prefixes)
- Tests cover multi-target scenarios with footer disambiguation
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_creates_trie_md_at_project_root fingerprint=3bf0b6ba7aa8e85d0365130e62db162887b6ef7f9c00019abee9ee2b354708e6 body_fp=849e7010cf61f61c08df0fc894b27302b8ef4510151bf5e577bf29991ba09e6a source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Verifies that `install` creates TRIE.md at project root with bundled content and generated-file notice.

- Checks file exists with non-empty body containing "Generated by `trie setup`" marker
- Validates bundled documentation was loaded by checking for "Using trie" title
- Confirms install plan reports "created" action for the file
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_trie_md_is_idempotent_on_identical_content fingerprint=9a9ced828f73aac923952bd22feb3a1b00633950073a88be0eaa407d8bd6383a body_fp=d05eb486556ad4f084dedbdfde9a25060166815e726e41498c62cc45407809f5 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Verifies that running `install` twice on the same project returns `skipped` action when TRIE.md is unchanged.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_trie_md_updates_on_drift fingerprint=2db466ed1d7ad9b8890e976dce1c128679f8b06880d9ea46651be09068d0e8de body_fp=a15cd795a3f8e52f72d7cb0afbf458ba15f2ca2ba811e413a8021688369c025f source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Tests that `install` rewrites TRIE.md when the on-disk file has been modified since the last installation.

- Creates temporary project directory, installs TRIE.md, corrupts the file content, then verifies reinstall updates the file
- Validates the install result shows "updated" action and restores original bundled documentation content
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_skips_pointer_when_agent_files_absent fingerprint=7f41b7e6e78039766b719d39cacd7a94043104007a0eb7e9b9d464b8cacce730 body_fp=e20cffe1f4b7e6684c003f7b8aa8c3810e023284b8a83cd5506afa95714a9ca8 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Tests that `install` skips pointer block injection when neither AGENTS.md nor CLAUDE.md exist at project root.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_appends_pointer_to_existing_agents_md fingerprint=299c35faddd0533c804727020a8a5c4911e058caa4bd573295a8f420d24c27ba body_fp=87305cd6322f8a0ef3cbc62bfb463083f9520314363d3e0c770262fca634e15d source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Tests that `install()` appends a pointer block to existing AGENTS.md files while preserving user content.

- Verifies pointer markers and TRIE.md reference are added
- Confirms user content remains unchanged
- Validates pointer uses local path for offline compatibility
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_appends_pointer_to_existing_claude_md fingerprint=33c41b878ca918e62a18bf211e33173f97c94618941ed4c6ca61daee1e3f700b body_fp=bc5d3e686286ef84019ce7b90d18f33627f1f9599a6f01e5c572806808ab7945 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Tests that `install()` adds a pointer block to existing CLAUDE.md files.

- Verifies CLAUDE.md receives the same pointer treatment as AGENTS.md
- Checks that pointer markers and TRIE.md references are properly inserted
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_handles_both_agents_and_claude_files fingerprint=3bb04dd002b2bd3364369312b092f78c214dfb7aab18010e1e452d6adf0440f3 body_fp=122dbe1337f592c5a9cd7d05ae56df04811f62fcfc0eb4201d9d5b0b78561fca source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Verifies install() adds pointer blocks to both AGENTS.md and CLAUDE.md when both files exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_pointer_is_idempotent fingerprint=d46e62d8582e4ca22291dd24a293f1fa124e7be6fc98f4e7179dcadfb94c4b13 body_fp=762a512c5c59cab8d3df227cdc638355536fbdd12e3ff3b3bf92a0f7e5c02713 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Tests that running install twice produces `skipped` result for existing pointer blocks.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_refreshes_stale_pointer_block_in_place fingerprint=936883fe669313ace022a049ab843aabd7f9618989175708bd378611e602acfd body_fp=026c9bb5b453eb1dadd0aec4b55653e13d97c437c652efca1b4022dcac39ac29 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Tests that install replaces only the marker-delimited pointer block in existing agent documentation files.

- Creates AGENTS.md with user content surrounding a stale pointer block
- Verifies install preserves user content while updating only the pointer block content
- Confirms old pointer text is removed and new POINTER_LINE is inserted
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_print_only_does_not_write_anything fingerprint=3d616c1d20ceaa9d4fb90f483515a2b069d4d393d8ab2789057083e4e6953001 body_fp=a31ac0378ac1c8ebf1de2f8a505ae98f1d08adca4f94a53089d3a562a58f1a73 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Tests that `install` with `print_only=True` generates a plan without writing any files to disk.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_dry_run_does_not_write_when_file_already_correct fingerprint=cf475c6d30538c0bf4597946a389e4a90cf7c8e796d457084a3ca0162180475f body_fp=c6cb670ab668813f221b8de728dbada9bb0d27d8192ce478392a8dcb458daa41 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Verifies dry-run mode reports `skipped` when target files match expected content without writing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_splice_appends_when_marker_absent fingerprint=205b8edad0c258f4bbe09a41ebbe06c14452a736cd557df2ed59dd752db87aa2 body_fp=0df63c7dca5fdb58093b8ced032c05f23eb679f0f0bd9551085550df522acfb5 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Tests that `_splice_pointer_block` appends pointer markers when none exist, preserving original content and avoiding extra blank lines.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_splice_replaces_when_marker_present fingerprint=cb17cac81bcfab095b782d945f82fb285ef15e5283112c5d4ff29c72929208b7 body_fp=7db26b971ea2315c3c295a8c4a79251f229db15fb3bd13566bf849b45dbcf276 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Verifies `_splice_pointer_block` replaces content between existing markers without duplication.

- Tests that old pointer content is removed and replaced with current pointer
- Ensures only one marker pair exists after replacement
- Confirms surrounding user content remains intact
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_splice_handles_empty_input fingerprint=30701c07c06462fd811f4af402b6f22d730ef0ef27b4ea2b11b6b97a6c67aa9a body_fp=dc41d02651adea088d595047faba115f05da112908de7494626ef632fce3dcd5 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Tests that `_splice_pointer_block` handles empty input by returning only the pointer block without leading blank lines.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_agent_doc_files_covers_known_conventions fingerprint=4d9b70824755d5d8b83a37286588a8d52c99d0f08a3bb8cc31f58d3bac55e121 body_fp=301d93426110729d3af38dcfd52f62c0e60fc7d93accd13d08e15b04fbc90a02 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Asserts AGENT_DOC_FILES equals the expected tuple of agent documentation filenames.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_with_no_target_renders_bare_tool_names fingerprint=fb44134da3aa120acd2c8813e1479bd3500b11ea95a551ea66697bec3e04cb5a body_fp=7c0c596e83d7fde5bfa57b68cd886a388a721e25ade79d1dde69654041ff550e source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Verifies that install with no target parameter renders bare tool names in TRIE.md without harness prefixes.

- Checks placeholder tokens are completely substituted out 
- Confirms `grep`, `read`, `trace` appear as bare tool names in documentation
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_for_claude_code_uses_mcp_double_underscore_prefix fingerprint=2629d7ed16832df3abd883531d6329f54001eb1c060921162a08394c53fbfbb4 body_fp=dd5ed68a4016c1ee83dac710d261a10c672c7e1ce62336735e7506ecca6021c8 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Verifies that `install` with `target_names=["claude-code"]` renders tool names as `mcp__trie__<tool>` in TRIE.md body.

- Checks for `mcp__trie__grep`, `mcp__trie__read`, and `mcp__trie__trace` in generated content
- Ensures placeholder tokens like `«grep»` are fully substituted out
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_for_opencode_uses_bare_tool_names fingerprint=a29cc89ae0deac1cada85e8f6f38f7866374a9887c407b5294e0f055d3bdeaa1 body_fp=5640f7d6c88f8d98b9eba78553427be79d56690109e89120ac7ab1f029b2d7bf source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Tests that `install` with `opencode` target uses bare tool names in generated TRIE.md content.

- Verifies that prefixed names like `trie_grep` are not present
- Confirms bare names `grep`, `read`, `trace` appear in the documentation
- Ensures template tokens like `«grep»` are properly substituted
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_unknown_target_falls_back_to_bare_names fingerprint=8dc34e858b445570e9f034ad3c01247ba1aafcc6cf8bacfca76855fcdc499d65 body_fp=0263c22f9d290d2b4018196d0c15db631191c2560274a89e7c54e7be2fb81739 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Verifies install with unknown target name falls back to bare tool names and doesn't crash.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_pointer_block_uses_target_specific_names fingerprint=36f1eed4451bda0e06df74720cd065d70d775a68ed604a9a92a35e0bc2cad263 body_fp=666581e8fa35b79eb790cfd426ae176e5c5674845ecb7f33e7655ed64a69ec6d source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Tests that install writes target-specific tool names in AGENTS.md pointer blocks.

- Creates AGENTS.md and runs install with claude-code target
- Verifies pointer block contains mcp__trie__ prefixed tool names matching agent's tool list
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_multiple_targets_renders_primary_in_body_and_footer_for_rest fingerprint=1c8049e6eb9d914828abe22ff389d3c1627c1bff5993f0f3a49b0b5b35959688 body_fp=4c88430f85528f441ce3ce183a877aafae3c60c870602d3faf491a1dcb8c2b00 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Tests that install with multiple targets renders primary target names in body and secondary targets in footer.

- Verifies first target (claude-code) tool names appear in main TRIE.md content
- Confirms footer section lists alternative tool names for other harnesses
- Ensures single TRIE.md handles multi-agent scenarios without confusion
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_single_target_omits_multi_target_footer fingerprint=48e4895b63d616d714fe313ed1185b050e760f6dfb0aa64e9a73d6081ff375ae body_fp=429d3092b99bdd551ff5f34368b3d3191e5e81af4e41f47d127c60db6136a367 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Verifies that `install` omits the multi-target footer when only one target is specified.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_re_render_on_target_change_is_an_update fingerprint=e2be5e875fe2c7e81504d6cdd617417a1d724b944d2092315ea56323dcc5fd1d body_fp=c9f3d7c34f5d7d525b0f0880e5eeb030822ae6e2691332afff5ce56ffbf76554 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Verifies that changing target names between installs triggers an update action, not a skip.

- Runs install twice with different target_names to ensure TRIE.md gets rewritten with new tool names
- Confirms second install returns "updated" action rather than "skipped"
- Validates old tool names are replaced with target-specific prefixed names
<!-- trie:end -->