---
trie_version: 0.1.5
source: tests/test_docs_install.py
file_fingerprint: 612d52ed0d41bd1438627a21efab404e22edca595ae18169882a7c75b143b312
last_synced_at: '2026-06-03T21:18:56Z'
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
<!-- trie:section symbol=tests/test_docs_install:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=3ed7cf662be97aecc713973592ba7d08076c370863fa70e35521e2f4e78beb60 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Tests for `trie.docs_install` module covering TRIE.md materialisation, pointer block injection into AGENTS.md/CLAUDE.md, idempotency, dry-run behavior, and target-specific tool name rendering.

- Validates TRIE.md creation at project root with generated-file notice
- Tests pointer block appending/updating in existing agent documentation files  
- Verifies idempotent behavior when content already matches canonical form
- Covers print-only/dry-run modes that preview changes without writing files
- Tests tool name substitution for different MCP harnesses (claude-code, opencode)
- Includes direct tests of internal `_splice_pointer_block` function
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_creates_trie_md_at_project_root fingerprint=3bf0b6ba7aa8e85d0365130e62db162887b6ef7f9c00019abee9ee2b354708e6 body_fp=30c8a4655867992c696ba7eb54645072f252f990760188d34d9ba8b2c98d2d0e source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Verifies that `install()` creates `TRIE.md` at project root with generated-file notice and bundled documentation content.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_trie_md_is_idempotent_on_identical_content fingerprint=9a9ced828f73aac923952bd22feb3a1b00633950073a88be0eaa407d8bd6383a body_fp=c5668e80abf45fb68f2cfb8d0d4673bdb431341b2a1ca9f30e5565395b6764b1 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Verifies that `install` correctly skips writing TRIE.md when content hasn't changed between runs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_trie_md_updates_on_drift fingerprint=2db466ed1d7ad9b8890e976dce1c128679f8b06880d9ea46651be09068d0e8de body_fp=e51d245eafd6e4b19c600891e7e8092ed94b53ffce2be19871acb677c1d40221 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Verifies install rewrites TRIE.md when content drifts from bundled documentation template.

- Creates initial TRIE.md, corrupts it with invalid content, then confirms second install updates file
- Asserts result action is "updated" and final content matches bundled body with "Using trie" text
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_skips_pointer_when_agent_files_absent fingerprint=7f41b7e6e78039766b719d39cacd7a94043104007a0eb7e9b9d464b8cacce730 body_fp=42cf96c1a8a1216c40e909e34bbfdafd273c3d7628874268862ff62f0213b823 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Tests that install skips creating AGENTS.md/CLAUDE.md when they don't exist, only writing TRIE.md.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_appends_pointer_to_existing_agents_md fingerprint=299c35faddd0533c804727020a8a5c4911e058caa4bd573295a8f420d24c27ba body_fp=812ca8ff80787c90e30164bf9b239017522d162cc4250d36e45dec9b1d5a4851 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Tests that `install` appends a pointer block to existing AGENTS.md while preserving user content.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_appends_pointer_to_existing_claude_md fingerprint=33c41b878ca918e62a18bf211e33173f97c94618941ed4c6ca61daee1e3f700b body_fp=7337d5807f3c504aaf01c04a2c0d0d054edc0e685d3bb5cf87edc0ef5c5e1278 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Verifies that install() appends a pointer block to existing CLAUDE.md files.

- Creates CLAUDE.md with initial content, runs install(), then confirms the pointer markers and TRIE.md reference are present
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_handles_both_agents_and_claude_files fingerprint=3bb04dd002b2bd3364369312b092f78c214dfb7aab18010e1e452d6adf0440f3 body_fp=f6aa14147c723d8ca9f294537c58293dd0a5339b69381e09c4aa9d73d6e3abb9 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Verifies that install adds pointer blocks to both AGENTS.md and CLAUDE.md when both files exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_pointer_is_idempotent fingerprint=d46e62d8582e4ca22291dd24a293f1fa124e7be6fc98f4e7179dcadfb94c4b13 body_fp=65dfdc873337862bfd749462a309cfa10f7325dc737e26ef36d6d50d65f18739 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Tests that repeated installs on identical AGENTS.md pointer blocks report "skipped" action.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_refreshes_stale_pointer_block_in_place fingerprint=936883fe669313ace022a049ab843aabd7f9618989175708bd378611e602acfd body_fp=72ff1383e601cf34ebba5ca0e275a593038551d220867366b260eb7b10b00e5d source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Tests that `install` replaces stale pointer blocks in-place while preserving surrounding user content.

- Creates AGENTS.md with user content above and below an outdated pointer block
- Verifies `install` updates only the marker-delimited section
- Confirms user content on both sides remains untouched
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_print_only_does_not_write_anything fingerprint=3d616c1d20ceaa9d4fb90f483515a2b069d4d393d8ab2789057083e4e6953001 body_fp=43b7d086f516a1366518c26cae23d416f9d20726e9fd894a5156615560db455d source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Verifies that `install` with `print_only=True` performs no filesystem writes while returning preview actions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_dry_run_does_not_write_when_file_already_correct fingerprint=cf475c6d30538c0bf4597946a389e4a90cf7c8e796d457084a3ca0162180475f body_fp=80855999aba483994cdf07c128341ea6e3bfb9907bce53cafc0be65d2d688592 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Verifies that `install` with `dry_run=True` reports `skipped` for unchanged files rather than `preview`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_splice_appends_when_marker_absent fingerprint=205b8edad0c258f4bbe09a41ebbe06c14452a736cd557df2ed59dd752db87aa2 body_fp=906d7a211856d69ab6ad0dffe4c5328be26d1505309f6255d86af820a015c16d source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Tests that `_splice_pointer_block` appends a pointer block with blank-line separator when no existing marker is found.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_splice_replaces_when_marker_present fingerprint=cb17cac81bcfab095b782d945f82fb285ef15e5283112c5d4ff29c72929208b7 body_fp=83985500aa640287393d80dc6abdf390082382d2e861d25f8c8a5be2f873aa26 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Verifies that `_splice_pointer_block` replaces existing marker blocks in place without duplicating markers.

- Tests that old content between markers is removed
- Ensures only one marker pair exists after replacement
- Confirms surrounding content is preserved unchanged
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_splice_handles_empty_input fingerprint=30701c07c06462fd811f4af402b6f22d730ef0ef27b4ea2b11b6b97a6c67aa9a body_fp=3fcc836eefe11dc830185a0aff2c328e5b5678214dce9db3d112d2e90d590224 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Verifies `_splice_pointer_block` handles empty input by adding only the pointer block without extra blank lines.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_agent_doc_files_covers_known_conventions fingerprint=4d9b70824755d5d8b83a37286588a8d52c99d0f08a3bb8cc31f58d3bac55e121 body_fp=15c50b6089324c383f939ca053740472691d53fb31c6816fbf7d9650c94ef47c source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Verifies that AGENT_DOC_FILES contains exactly ("AGENTS.md", "CLAUDE.md") as supported conventions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_with_no_target_renders_bare_tool_names fingerprint=fb44134da3aa120acd2c8813e1479bd3500b11ea95a551ea66697bec3e04cb5a body_fp=2f451f4b06e8d3b8c4967f8fdb00fe9aa90fbb4df322e93ea2b3034f35410b89 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Verifies that install() renders bare tool names when no target is specified.

- Tests that placeholder tokens `«grep»`, `«read»`, `«trace»` are fully substituted
- Confirms bare names `grep`, `read`, `trace` appear in generated TRIE.md
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_for_claude_code_uses_mcp_double_underscore_prefix fingerprint=2629d7ed16832df3abd883531d6329f54001eb1c060921162a08394c53fbfbb4 body_fp=dd7e1aec323f1e70759d27114329215b7a65f3ff85f2b4f64b0b21613fa5e855 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Verifies that install() with target_names=["claude-code"] renders MCP-prefixed tool names in TRIE.md body.

- Expects tool names formatted as `mcp__trie__<tool>` for Claude Code's MCP namespace convention
- Asserts placeholder tokens `«grep»` are fully substituted out of rendered documentation
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_for_opencode_uses_bare_tool_names fingerprint=a29cc89ae0deac1cada85e8f6f38f7866374a9887c407b5294e0f055d3bdeaa1 body_fp=3eb8b8070d1b35400150f45f1f2a796a4fc8e926cc4d7b3fe08f8f81feadfa81 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Verifies `install` renders bare tool names in TRIE.md when target is "opencode".
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_unknown_target_falls_back_to_bare_names fingerprint=8dc34e858b445570e9f034ad3c01247ba1aafcc6cf8bacfca76855fcdc499d65 body_fp=21321d6a76505e232293d736b89a8eac674f0dfa00c7ca61f95b139e24b974d7 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Tests that unknown target names fall back to bare tool names without errors.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_pointer_block_uses_target_specific_names fingerprint=36f1eed4451bda0e06df74720cd065d70d775a68ed604a9a92a35e0bc2cad263 body_fp=d18eab8b61044d59debde6d0536bf5a2b9291c4231db3582610d19e672e1ceee source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Verifies that pointer blocks in agent documentation files use target-specific tool names matching the agent's actual tool list.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_multiple_targets_renders_primary_in_body_and_footer_for_rest fingerprint=1c8049e6eb9d914828abe22ff389d3c1627c1bff5993f0f3a49b0b5b35959688 body_fp=722073c9923de8c72f9df414422b14ff1ee632fda6cbed8c582832b4e5f7dfd6 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Tests that multiple target harnesses render primary target tool names in body and secondary targets in footer.

- Creates TRIE.md with claude-code tool names in main content
- Verifies opencode tool names appear in footer section
- Ensures multi-target footer section is present with secondary aliases
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_single_target_omits_multi_target_footer fingerprint=48e4895b63d616d714fe313ed1185b050e760f6dfb0aa64e9a73d6081ff375ae body_fp=c8929f17d141d935910e487496b377947f1f6f7ad3ea77bded9c352eee9661cb source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Verifies that install() with a single target omits the multi-target footer from TRIE.md.

- Creates test with `target_names=["opencode"]`
- Asserts footer text "Tool names under other installed harnesses" is absent
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_re_render_on_target_change_is_an_update fingerprint=e2be5e875fe2c7e81504d6cdd617417a1d724b944d2092315ea56323dcc5fd1d body_fp=b05c2ea8e432cf10e7df34450106ef5e36b147c32ac168f730b3c8b6fe7a5d52 source_ref=9fe1a66b8400606b68b3e6d8a2b2a75352e32c94 -->
Verifies that changing target names between install runs triggers TRIE.md rewrite with updated tool references.

- First install with "opencode" target, second with "claude-code" target produces "updated" action
- Confirms old tool names removed and new MCP-prefixed names present in final content
<!-- trie:end -->