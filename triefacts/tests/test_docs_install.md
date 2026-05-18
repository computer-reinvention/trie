---
trie_version: 0.1.1
source: tests/test_docs_install.py
file_fingerprint: de7c98fcfd2eb93c13bf961ba554fc35110ea849b4c8bee8c44aa552998c9fdd
last_synced_at: '2026-05-18T13:25:57Z'
description: 'Tests for `trie.docs_install`: project-local agent documentation install.'
defines:
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
  qualified_name: tests/test_docs_install:test_install_for_opencode_uses_single_underscore_prefix
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
outgoing_refs: 22
---
<!-- trie:section symbol=tests/test_docs_install:test_install_creates_trie_md_at_project_root fingerprint=3bf0b6ba7aa8e85d0365130e62db162887b6ef7f9c00019abee9ee2b354708e6 body_fp=7a3ec4a01bfac7fa1aeac2365ea0c119b64382e53bbdf2d7b9da3d0d1d28faa2 source_ref=9f9ea6168a5dc67017db28037388a765414ee32e -->
## `test_install_creates_trie_md_at_project_root(tmp_path: Path)`

Assert that `install` writes a non-empty `TRIE.md` with a generated-file notice and reports action `"created"`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_docs_install:test_install_trie_md_is_idempotent_on_identical_content fingerprint=9a9ced828f73aac923952bd22feb3a1b00633950073a88be0eaa407d8bd6383a body_fp=459e45158cc8012c09907c28f1dc34e3303c307dbdd7fbd125f2c4823447a88a source_ref=9f9ea6168a5dc67017db28037388a765414ee32e -->
## `test_install_trie_md_is_idempotent_on_identical_content(tmp_path: Path)`

Assert that a second `install` call reports `skipped` when `TRIE.md` already matches the canonical content.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_docs_install:test_install_trie_md_updates_on_drift fingerprint=2db466ed1d7ad9b8890e976dce1c128679f8b06880d9ea46651be09068d0e8de body_fp=3338e41401904f057896b3a2a82d13f9eae51ef9a8141d75dd7a9873b436843e source_ref=9f9ea6168a5dc67017db28037388a765414ee32e -->
## `test_install_trie_md_updates_on_drift(tmp_path: Path)`

Assert that `install` overwrites a modified `TRIE.md` and restores its canonical content.

- `action` is `"updated"` when on-disk content differs from the bundled doc.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_docs_install:test_install_skips_pointer_when_agent_files_absent fingerprint=7f41b7e6e78039766b719d39cacd7a94043104007a0eb7e9b9d464b8cacce730 body_fp=c80e25c7df55031330935224f7a807fb1aedbc0734b70cad00a7a864ef6a9d47 source_ref=9f9ea6168a5dc67017db28037388a765414ee32e -->
## `test_install_skips_pointer_when_agent_files_absent(tmp_path: Path)`

Assert that `install` does not create `AGENTS.md` or `CLAUDE.md` when neither exists, and only `TRIE.md` appears in the plan results.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_docs_install:test_install_appends_pointer_to_existing_agents_md fingerprint=299c35faddd0533c804727020a8a5c4911e058caa4bd573295a8f420d24c27ba body_fp=7ff6f9b4b2103b0fc69ef3a3bc3eb429f12568762a4e4302c7f12f5d38353d6f source_ref=9f9ea6168a5dc67017db28037388a765414ee32e -->
## `test_install_appends_pointer_to_existing_agents_md(tmp_path: Path)`

Assert that `install` appends a marker-fenced pointer block to a pre-existing `AGENTS.md` without disturbing existing content.

- Verifies `POINTER_MARKER`, `POINTER_END_MARKER`, and `POINTER_LINE` are all present after install.
- Confirms original user text is preserved verbatim.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_docs_install:test_install_appends_pointer_to_existing_claude_md fingerprint=33c41b878ca918e62a18bf211e33173f97c94618941ed4c6ca61daee1e3f700b body_fp=6e159e8d15feddf1b3b36a53b2663713d1f0f9cd63490d2f7caafffe68f6de30 source_ref=9f9ea6168a5dc67017db28037388a765414ee32e -->
## `test_install_appends_pointer_to_existing_claude_md(tmp_path: Path)`

Verify that `install` appends a pointer block to a pre-existing `CLAUDE.md`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_docs_install:test_install_handles_both_agents_and_claude_files fingerprint=3bb04dd002b2bd3364369312b092f78c214dfb7aab18010e1e452d6adf0440f3 body_fp=bcb7e9bc4cf95e7733edb12c09c5c1e0368667cd3316f36186c08b61963c5da3 source_ref=9f9ea6168a5dc67017db28037388a765414ee32e -->
## `test_install_handles_both_agents_and_claude_files(tmp_path: Path)`

Verify that when both `AGENTS.md` and `CLAUDE.md` exist, each receives its own pointer block and the plan reports both writes.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_docs_install:test_install_pointer_is_idempotent fingerprint=d46e62d8582e4ca22291dd24a293f1fa124e7be6fc98f4e7179dcadfb94c4b13 body_fp=4c9863d78f26ae1b816ea8ab3cccc8ab09b7c2ee0a04f435009045dc066b7582 source_ref=9f9ea6168a5dc67017db28037388a765414ee32e -->
## `test_install_pointer_is_idempotent(tmp_path: Path)`

Assert that a second `install` call reports `skipped` for `AGENTS.md` when the pointer block is already present and unchanged.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_docs_install:test_install_refreshes_stale_pointer_block_in_place fingerprint=936883fe669313ace022a049ab843aabd7f9618989175708bd378611e602acfd body_fp=75b6614e851aefa412274d3e93f35addb6fba4ac0e13dd1ed010761349b25a9c source_ref=9f9ea6168a5dc67017db28037388a765414ee32e -->
## `test_install_refreshes_stale_pointer_block_in_place(tmp_path: Path)`

Verify that `install` replaces only the stale marker-fenced block, preserving user content above and below it.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_docs_install:test_print_only_does_not_write_anything fingerprint=3d616c1d20ceaa9d4fb90f483515a2b069d4d393d8ab2789057083e4e6953001 body_fp=48601c4a6e1674c4344bc5e90831882aa1d9224d12c0a605f0298037b030aac3 source_ref=9f9ea6168a5dc67017db28037388a765414ee32e -->
## `test_print_only_does_not_write_anything(tmp_path: Path)`

Verify that `print_only=True` leaves all files unmodified and returns only `"preview"` actions.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_docs_install:test_dry_run_does_not_write_when_file_already_correct fingerprint=cf475c6d30538c0bf4597946a389e4a90cf7c8e796d457084a3ca0162180475f body_fp=4f8ad4926d4afe850b32d3c4b0e2ab411faec5aacf4e433fce28132c328a5f1b source_ref=9f9ea6168a5dc67017db28037388a765414ee32e -->
## `test_dry_run_does_not_write_when_file_already_correct(tmp_path: Path)`

Verify that `--dry-run` reports `skipped` when on-disk content already matches the canonical write, without modifying files.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_docs_install:test_splice_appends_when_marker_absent fingerprint=205b8edad0c258f4bbe09a41ebbe06c14452a736cd557df2ed59dd752db87aa2 body_fp=a7184fbdb4454d037a5957e58bc69a01cddec3c2249106b3f6506b158954c76e source_ref=9f9ea6168a5dc67017db28037388a765414ee32e -->
## `test_splice_appends_when_marker_absent(tmp_path: Path)`

Verify `_splice_pointer_block` appends a fenced pointer block when no marker exists in the input.

- Asserts no quadruple newlines accumulate on repeated calls.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_docs_install:test_splice_replaces_when_marker_present fingerprint=cb17cac81bcfab095b782d945f82fb285ef15e5283112c5d4ff29c72929208b7 body_fp=542c7d4f54dd6c051aa0cd82463fdd583bb39601e8c0d0f774d24877fd8433a9 source_ref=9f9ea6168a5dc67017db28037388a765414ee32e -->
## `test_splice_replaces_when_marker_present()`

Verify that `_splice_pointer_block` rewrites only the marker-fenced block, preserving surrounding content and never duplicating markers.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_docs_install:test_splice_handles_empty_input fingerprint=30701c07c06462fd811f4af402b6f22d730ef0ef27b4ea2b11b6b97a6c67aa9a body_fp=4e907983fa792d5ad4213a553826cb1bb00294f3a7122a6d070483e53d38edd5 source_ref=9f9ea6168a5dc67017db28037388a765414ee32e -->
## `test_splice_handles_empty_input()`

Verify that `_splice_pointer_block` on an empty string produces output beginning with `POINTER_MARKER` and no leading blank line.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_docs_install:test_agent_doc_files_covers_known_conventions fingerprint=4d9b70824755d5d8b83a37286588a8d52c99d0f08a3bb8cc31f58d3bac55e121 body_fp=c6b0ba80b70b83d299aa542850d7c4e4cb82c8218766147f693e8872c78714e4 source_ref=9f9ea6168a5dc67017db28037388a765414ee32e -->
## `test_agent_doc_files_covers_known_conventions()`

Assert that `AGENT_DOC_FILES` equals exactly `("AGENTS.md", "CLAUDE.md")`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_docs_install:test_install_with_no_target_renders_bare_tool_names fingerprint=fb44134da3aa120acd2c8813e1479bd3500b11ea95a551ea66697bec3e04cb5a body_fp=894285c69ed2382dce7376eebe1473ec18e77303c909d11e8c9ea60b3d2da07d source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_install_with_no_target_renders_bare_tool_names(tmp_path: Path)`

Assert that `install` without `target_names` renders bare tool names (`grep`, `read`, `trace`) with no placeholder tokens remaining.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_docs_install:test_install_for_claude_code_uses_mcp_double_underscore_prefix fingerprint=2629d7ed16832df3abd883531d6329f54001eb1c060921162a08394c53fbfbb4 body_fp=4e67c0aebd7bab181db9709d9f0645f4a6300ef93ea411f432220cd7c893702c source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_install_for_claude_code_uses_mcp_double_underscore_prefix(tmp_path: Path)`

Assert that `install` with `target_names=["claude-code"]` renders `mcp__trie__<tool>` names in `TRIE.md`.

- `tmp_path`: pytest-provided temporary directory used as `project_root`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_docs_install:test_install_for_opencode_uses_single_underscore_prefix fingerprint=22926a0d8f5b42ab3687ac6b9d5ef0ea1c93b0100e80c9f6e3b363b6bc55889b body_fp=bf5f093cf91496f58da8ef8d5d17789e606791124ee3c3e4703ad2d31dead8a8 source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_install_for_opencode_uses_single_underscore_prefix(tmp_path: Path)`

Assert that `install` with `target_names=["opencode"]` renders tools as `trie_grep`, `trie_read`, `trie_trace` in `TRIE.md`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_docs_install:test_install_unknown_target_falls_back_to_bare_names fingerprint=8dc34e858b445570e9f034ad3c01247ba1aafcc6cf8bacfca76855fcdc499d65 body_fp=1c6aaf16cf2349bc96ce4189d8d0de6e789fbcea57d4b85401fa2fac42b6e10d source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_install_unknown_target_falls_back_to_bare_names(tmp_path: Path)`

Verify that an unrecognised `target_names` slug produces bare tool names instead of raising an error.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_docs_install:test_install_pointer_block_uses_target_specific_names fingerprint=36f1eed4451bda0e06df74720cd065d70d775a68ed604a9a92a35e0bc2cad263 body_fp=894168889fb30a8431dc52b5ef4f13f7cdce6cbbd665b8430eb17675f89f712b source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_install_pointer_block_uses_target_specific_names(tmp_path: Path)`

Assert that the pointer block spliced into `AGENTS.md` uses the target-specific tool names rather than bare names.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_docs_install:test_install_multiple_targets_renders_primary_in_body_and_footer_for_rest fingerprint=2559dcf8d6468ade53c2ea38c8a01c2e7b4e87472da0a18d41680885a4b09c78 body_fp=9eec4ff2daaa1922430e7cad033cef631956c6ea733c1aae9ffdd320f5653409 source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_install_multiple_targets_renders_primary_in_body_and_footer_for_rest(tmp_path: Path)`

Assert that the first target's tool names appear in the TRIE.md body and remaining targets' aliases appear in a footer section.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_docs_install:test_install_single_target_omits_multi_target_footer fingerprint=48e4895b63d616d714fe313ed1185b050e760f6dfb0aa64e9a73d6081ff375ae body_fp=58be81fb0823d56208e7892d00427ca615b37155e48dfcd89b4bdfc02a18830b source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_install_single_target_omits_multi_target_footer(tmp_path: Path)`

Assert that a single-target install omits the multi-harness footer from the generated `TRIE.md`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_docs_install:test_install_re_render_on_target_change_is_an_update fingerprint=e2be5e875fe2c7e81504d6cdd617417a1d724b944d2092315ea56323dcc5fd1d body_fp=61b35340f17c12b4df3a22653bee6f35bf26ddfe797746ae3805fb473b4b2695 source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_install_re_render_on_target_change_is_an_update(tmp_path: Path)`

Assert that switching `target_names` between two installs triggers an `"updated"` action and rewrites stale tool names in `TRIE.md`.
<!-- trie:end -->