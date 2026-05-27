---
trie_version: 0.1.2
source: tests/test_docs_install.py
file_fingerprint: 612d52ed0d41bd1438627a21efab404e22edca595ae18169882a7c75b143b312
last_synced_at: '2026-05-23T23:47:07Z'
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
<!-- trie:section symbol=tests/test_docs_install:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=be31889d9307a928b431c85ec2179a0b7fc02cc64dd301737f5ad47822fb1334 source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `tests/test_docs_install`

Test suite for `trie.docs_install`, verifying `install()` contracts.

- **TRIE.md**: created, idempotency, drift-detection, and dry-run behaviour.
- **Pointer blocks**: appended to existing `AGENTS.md`/`CLAUDE.md`, idempotent, stale-block replacement, absent files not materialised.
- **Tool-name rendering**: bare, `mcp__trie__<tool>`, `trie_<tool>`, unknown-slug fallback, multi-target footer.
- **`_splice_pointer_block`**: unit-tested for append, replace, and empty-input cases.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_creates_trie_md_at_project_root fingerprint=3bf0b6ba7aa8e85d0365130e62db162887b6ef7f9c00019abee9ee2b354708e6 body_fp=85dfe1d6468f3dbd553417296a5a343a7904b48d4dbcd57e28210c63297e7fcf source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_install_creates_trie_md_at_project_root(tmp_path: Path)`

Assert that `install` writes a non-empty `TRIE.md` with the generated-file notice and reports `action == "created"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_trie_md_is_idempotent_on_identical_content fingerprint=9a9ced828f73aac923952bd22feb3a1b00633950073a88be0eaa407d8bd6383a body_fp=b68bd84a55bfe23995ccdfe5df63b774dfd1c4d416eb64294ca5c51fe6a84e44 source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_install_trie_md_is_idempotent_on_identical_content(tmp_path: Path)`

Verify that a second `install` call on an unchanged project root reports `skipped` with an "up to date" detail.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_trie_md_updates_on_drift fingerprint=2db466ed1d7ad9b8890e976dce1c128679f8b06880d9ea46651be09068d0e8de body_fp=356b274859d5ad0095c97042f0bf8d4e56dfdb0cd2644dc5d063b45411b52e78 source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_install_trie_md_updates_on_drift(tmp_path: Path)`

Verify that `install` rewrites `TRIE.md` and reports `"updated"` when on-disk content has drifted from the bundled doc.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_skips_pointer_when_agent_files_absent fingerprint=7f41b7e6e78039766b719d39cacd7a94043104007a0eb7e9b9d464b8cacce730 body_fp=3fd0d087d4779edb62e173f1bf3059f58344a75d3726facbff0d9fc81cad0c7d source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_install_skips_pointer_when_agent_files_absent(tmp_path: Path)`

Assert that `install` never materialises `AGENTS.md` or `CLAUDE.md` when they don't already exist, and only `TRIE_DOC_FILENAME` appears in the plan.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_appends_pointer_to_existing_agents_md fingerprint=299c35faddd0533c804727020a8a5c4911e058caa4bd573295a8f420d24c27ba body_fp=ab15f782186a615437cfb5f0906d7406b2e8cd05a38ce62efcdf7d8d14c1c24f source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_install_appends_pointer_to_existing_agents_md(tmp_path: Path)`

Assert that `install` appends a marker-fenced pointer block to a pre-existing `AGENTS.md`, preserving original content.

- Verifies user content survives verbatim above the injected block.
- Verifies `POINTER_MARKER`, `POINTER_END_MARKER`, and `POINTER_LINE` all appear in the result.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_appends_pointer_to_existing_claude_md fingerprint=33c41b878ca918e62a18bf211e33173f97c94618941ed4c6ca61daee1e3f700b body_fp=a9b9808a0a0fe0d351e09fb6111c2a86a20dbbd4ad34371dfeb1ee02df8cc92a source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_install_appends_pointer_to_existing_claude_md(tmp_path: Path)`

Assert that `install` splices a pointer block into an existing `CLAUDE.md`, preserving its content.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_handles_both_agents_and_claude_files fingerprint=3bb04dd002b2bd3364369312b092f78c214dfb7aab18010e1e452d6adf0440f3 body_fp=7001740c063683d0ae75b073ab6e9ce8bf1eba0e23be6f670eaf80be61b2a8c6 source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_install_handles_both_agents_and_claude_files(tmp_path: Path)`

Assert that `install` writes a pointer block into both `AGENTS.md` and `CLAUDE.md` when both exist, reporting each in the plan.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_pointer_is_idempotent fingerprint=d46e62d8582e4ca22291dd24a293f1fa124e7be6fc98f4e7179dcadfb94c4b13 body_fp=d01afe27d840ccb1c5b552bd2f83c9cfd19ccc0067069ac10194148ed4e20ab5 source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_install_pointer_is_idempotent(tmp_path: Path)`

Verify that a second `install` reports `skipped` for `AGENTS.md` when the pointer block is already present and unchanged.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_refreshes_stale_pointer_block_in_place fingerprint=936883fe669313ace022a049ab843aabd7f9618989175708bd378611e602acfd body_fp=e791b4897de9489655c7c6b531cf58505eb34215d61bf1cab6555da82b1e66d7 source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_install_refreshes_stale_pointer_block_in_place(tmp_path: Path)`

Verify that `install` replaces only the marker-fenced block in AGENTS.md, preserving surrounding user content.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_print_only_does_not_write_anything fingerprint=3d616c1d20ceaa9d4fb90f483515a2b069d4d393d8ab2789057083e4e6953001 body_fp=c39445001c9c35496422939f2b7d2c16e456bd4ecb107bef6e3a01cf59e17ff6 source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_print_only_does_not_write_anything(tmp_path: Path)`

Assert that `install(print_only=True)` writes no files and returns only `"preview"` actions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_dry_run_does_not_write_when_file_already_correct fingerprint=cf475c6d30538c0bf4597946a389e4a90cf7c8e796d457084a3ca0162180475f body_fp=cf820fffc878b6f003df4dfc2c80c200f7cd5cf98ff2e7196be34431b6fa1804 source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_dry_run_does_not_write_when_file_already_correct(tmp_path: Path)`

Assert that `install` with `dry_run=True` reports `skipped` when on-disk content already matches the canonical write.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_splice_appends_when_marker_absent fingerprint=205b8edad0c258f4bbe09a41ebbe06c14452a736cd557df2ed59dd752db87aa2 body_fp=1fbe2434c56517964036c91855f00ed5c31793e2ad14e89dbdc5b8d73b72a1b3 source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_splice_appends_when_marker_absent(tmp_path: Path)`

Verify `_splice_pointer_block` appends the pointer block with a blank-line separator when no marker exists in the input.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_splice_replaces_when_marker_present fingerprint=cb17cac81bcfab095b782d945f82fb285ef15e5283112c5d4ff29c72929208b7 body_fp=0794d952062d0cf3bd08a5edf7a318c6e75a936553e1838c5acfb45f4238003b source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_splice_replaces_when_marker_present()`

Verify `_splice_pointer_block` rewrites only the marked block, preserving surrounding content and producing no duplicate marker pairs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_splice_handles_empty_input fingerprint=30701c07c06462fd811f4af402b6f22d730ef0ef27b4ea2b11b6b97a6c67aa9a body_fp=a2648f3aeaa7985ae3e0675009d50525f3b26da4d5fe9e43054c03a1f2bd3324 source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_splice_handles_empty_input()`

Verify that `_splice_pointer_block` on an empty string produces output starting with `POINTER_MARKER` and no spurious leading blank line.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_agent_doc_files_covers_known_conventions fingerprint=4d9b70824755d5d8b83a37286588a8d52c99d0f08a3bb8cc31f58d3bac55e121 body_fp=050990893344edf5c486a8cdd2b4fdf1adf4b8f284a147f160d426baf5335ab2 source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_agent_doc_files_covers_known_conventions()`

Assert that `AGENT_DOC_FILES` is exactly `("AGENTS.md", "CLAUDE.md")`, preventing silent drift.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_with_no_target_renders_bare_tool_names fingerprint=fb44134da3aa120acd2c8813e1479bd3500b11ea95a551ea66697bec3e04cb5a body_fp=dd68a4d0d5751799e5871ce80d48ca7a461ce771dab1e138006cddcb96120fd8 source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_install_with_no_target_renders_bare_tool_names(tmp_path: Path)`

Assert that `install` with no `target_names` renders bare `grep`/`read`/`trace` tool names and eliminates all `«…»` placeholder tokens.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_for_claude_code_uses_mcp_double_underscore_prefix fingerprint=2629d7ed16832df3abd883531d6329f54001eb1c060921162a08394c53fbfbb4 body_fp=183e6f57ca5911a3b7e161f67dbca465e0b6db7a117f9700d220f7de7176f203 source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_install_for_claude_code_uses_mcp_double_underscore_prefix(tmp_path: Path)`

Assert that `install` with `target_names=["claude-code"]` renders `mcp__trie__grep/read/trace` in `TRIE.md` and leaves no `«…»` placeholder tokens.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_for_opencode_uses_single_underscore_prefix fingerprint=22926a0d8f5b42ab3687ac6b9d5ef0ea1c93b0100e80c9f6e3b363b6bc55889b body_fp=04886c183abf157ad7e59c1c8eb66064603bd00009c2ecd1fb5a445a7bfbf41f source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_install_for_opencode_uses_single_underscore_prefix(tmp_path: Path)`

Assert that `install` with `target_names=["opencode"]` renders `trie_grep`, `trie_read`, and `trie_trace` in `TRIE.md`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_unknown_target_falls_back_to_bare_names fingerprint=8dc34e858b445570e9f034ad3c01247ba1aafcc6cf8bacfca76855fcdc499d65 body_fp=4a8f20e50687f78133b144b604f8e97ed34c3386643697125b2ca9d23bc2c3b2 source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_install_unknown_target_falls_back_to_bare_names(tmp_path: Path)`

Assert that `install` uses bare tool names when `target_names` contains an unrecognised slug.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_pointer_block_uses_target_specific_names fingerprint=36f1eed4451bda0e06df74720cd065d70d775a68ed604a9a92a35e0bc2cad263 body_fp=b3df90b29fc9784bc52f9e21e67d8c99af05208a03cc33e8ad165976452736b2 source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_install_pointer_block_uses_target_specific_names(tmp_path: Path)`

Assert that the pointer block spliced into `AGENTS.md` uses target-specific tool names (e.g. `mcp__trie__grep` for `claude-code`), not bare names.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_multiple_targets_renders_primary_in_body_and_footer_for_rest fingerprint=2559dcf8d6468ade53c2ea38c8a01c2e7b4e87472da0a18d41680885a4b09c78 body_fp=3e85533eff552c81adbc8e7922eff0f027fc62ed70a3f8093aefb2acee8bf9a3 source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_install_multiple_targets_renders_primary_in_body_and_footer_for_rest(tmp_path: Path)`

Assert that with multiple targets, the first target's tool names appear in the TRIE.md body and remaining targets' aliases appear in a footer.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_single_target_omits_multi_target_footer fingerprint=48e4895b63d616d714fe313ed1185b050e760f6dfb0aa64e9a73d6081ff375ae body_fp=b828bc91858e0ad2ffeec65dd44a3010ca451f62dfba39b6fffc9aed6a07b8d7 source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_install_single_target_omits_multi_target_footer(tmp_path: Path)`

Assert that a single-target `install` omits the multi-harness tool-alias footer from `TRIE.md`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_docs_install:test_install_re_render_on_target_change_is_an_update fingerprint=e2be5e875fe2c7e81504d6cdd617417a1d724b944d2092315ea56323dcc5fd1d body_fp=778f59f4108b7b3f5e46718484b94bf708c4d6dadd351df7b57dd05891e8ccb9 source_ref=c71598498bc9ec5f3a1ba4c97c80ab82f4fb431f -->
## `test_install_re_render_on_target_change_is_an_update(tmp_path: Path)`

Assert that switching `target_names` between successive `install` calls marks TRIE.md as `updated` and rewrites tool names.
<!-- trie:end -->