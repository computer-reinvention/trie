---
trie_version: 0.2.1
source: tests/test_session_diff.py
file_fingerprint: 24a101193c53d84945804a72c9b6df41fa0c8eccc0fbb07f6f7e2a532951d5b4
last_synced_at: '2026-08-02T20:43:30Z'
description: Tests for the session log archive and the `trie diff` evidence collection/prompt
  assembly.
defines:
- kind: module
  qualified_name: tests/test_session_diff:__module__
  lines: 1-777
- kind: function
  qualified_name: tests/test_session_diff:test_intent_lifecycle_in_the_patches_table
  lines: 23-48
- kind: function
  qualified_name: tests/test_session_diff:test_build_narrative_prompt_sections_and_truncation
  lines: 51-98
- kind: function
  qualified_name: tests/test_session_diff:test_collect_session_diff_gathers_all_evidence
  lines: 101-175
- kind: function
  qualified_name: tests/test_session_diff:test_collect_session_diff_includes_new_triefacts
  lines: 178-226
- kind: function
  qualified_name: tests/test_session_diff:test_synthesize_narrative_uses_cache_prefix
  lines: 229-317
- kind: function
  qualified_name: tests/test_session_diff:test_session_narrative_as_markdown_formatting
  lines: 320-349
- kind: function
  qualified_name: tests/test_session_diff:test_render_digest_section_shape
  lines: 352-494
- kind: function
  qualified_name: tests/test_session_diff:test_write_digest_files_symlink_and_prune
  lines: 497-558
- kind: function
  qualified_name: tests/test_session_diff:test_one_line_flattens_and_truncates
  lines: 561-588
- kind: function
  qualified_name: tests/test_session_diff:test_first_line_preserves_full_intent_without_truncation
  lines: 591-605
- kind: function
  qualified_name: tests/test_session_diff:test_change_bullets_record_full_intent_no_ellipsis
  lines: 608-633
- kind: function
  qualified_name: tests/test_session_diff:test_collect_symbol_deltas_before_after
  lines: 636-698
- kind: function
  qualified_name: tests/test_session_diff:test_merge_applied_by_symbol_first_note_wins
  lines: 701-722
- kind: function
  qualified_name: tests/test_session_diff:test_symbol_and_file_history_from_digest_archive
  lines: 725-776
incoming_refs: 0
outgoing_refs: 35
---
<!-- trie:section symbol=tests/test_session_diff:__module__ fingerprint=efba484e3aa652464eff4bb42149f2f8ad21e69db80743152ed50083f36a38f2 body_fp=1104a778ce390fa56813958cd8c63c2c3c38548adf128fd9b73f2b057fbc791e source_ref=c2dff8907b251d36ea66f85df0d978cec2ed679e role=test -->
Test module for session log archive and `trie diff` evidence collection and prompt assembly.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_intent_lifecycle_in_the_patches_table fingerprint=1ea69d213793fddcd179296becc22e7a8aaea1a65b8426c86689a7be06c488b2 body_fp=7dd039331350bf007080e1f52c63fdf7dd931b4dc01196360315294d6230ab6c source_ref=c2dff8907b251d36ea66f85df0d978cec2ed679e role=test -->
Verify that `Store` patch staging, sealing via `mark_patches_applied`, and consumption via `delete_applied_patches` operate correctly on the qname-keyed patches table without symbol FK requirements.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_build_narrative_prompt_sections_and_truncation fingerprint=6446fd1cae84e737cb1b09ef79389e50b0648ad9f14d949905a4d413dd3c5263 body_fp=eea9a0dcc6b45f3e2fc0e3ad348aafecd880e63dd17c26c8eff4c60b49cca4c2 source_ref=c2dff8907b251d36ea66f85df0d978cec2ed679e role=test -->
Verify `build_narrative_prompt` emits correct sections, formats applied/pending entries, truncates `triefact_diff` to `max_diff_chars`, and handles an empty `SessionDiff`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_collect_session_diff_gathers_all_evidence fingerprint=0b749d0514dc8ee9cb364b32f45f11b121d37aa4c9b946dbb3d476ef87310cba body_fp=74e0034c1ddc1559b3771623f4fe2be9d07ded645594cb03cc35c5db63b09104 source_ref=c2dff8907b251d36ea66f85df0d978cec2ed679e role=test -->
Test `collect_session_diff` against a real git repo, verifying triefact diff content and applied/pending patch assembly via sealed/unsealed store patches.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_collect_session_diff_includes_new_triefacts fingerprint=1c8f6b894cfb45576c6cdcf42ce71b213efaf3a7e307fcb041108fc82401e0af body_fp=7cfc1ad6e85ed5c97ed11f5b9323ac777fb66f15a8f60024b089842cfce18b6c source_ref=c2dff8907b251d36ea66f85df0d978cec2ed679e role=test -->
Verify that `collect_session_diff` includes untracked new triefact files in `triefact_diff`, not only modified tracked files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_synthesize_narrative_uses_cache_prefix fingerprint=adb5a4b7bc2e81d2a8d3a545f7fb1f22240f1d5854aa0bfb56d664df8b4a9b09 body_fp=c82992d91333b9aa3f4debadc41f21236ee30e6d30d2fe8602f78cc9aca4328a source_ref=c2dff8907b251d36ea66f85df0d978cec2ed679e role=test -->
Verify that `synthesize_narrative` passes the triefact diff as `cache_prefix` when the client supports it, falls back to embedding it in the user prompt otherwise, asserts `max_tokens >= 512`, uses a structured `run(output_type, ...)` interface returning `SessionNarrative`, and coerces a bare-string output into a `SessionNarrative` with an empty `one_liner`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_session_narrative_as_markdown_formatting fingerprint=1116d5d2a4cbad55e9cee216cc33aad36da26316791fe4dec82c49ad6681b566 body_fp=c562ca1179245895d10a777266f2094bef23b7cf0a0128762d3f93170bd2992e source_ref=c2dff8907b251d36ea66f85df0d978cec2ed679e role=test -->
Verify `SessionNarrative.as_markdown()` formats bold one-liner, body, and conflict blockquotes, and drops empty/whitespace fields.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_render_digest_section_shape fingerprint=1baf8fbadf9592ac0616a4f6c8391dec9c91b39bc8e347722872ad1e8c9679b5 body_fp=8f6db62f45672b0bd5709d7ea6a5c774c1659a0e023e57c96d6b707f903741df source_ref=c2dff8907b251d36ea66f85df0d978cec2ed679e role=test -->
Verify `render_digest_section` output structure: header shape, H2-heading demotion in narratives, `### Changes` delta bullets, follow-up suffix, markdown-injection prevention, forbidden old-format artifacts, `### Staged (not applied)` section, and `max_changes` overflow truncation with lossless HTML-comment storage of capped-out rows.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_write_digest_files_symlink_and_prune fingerprint=a6d890f9a90cbf52aa184a2c3c03461db319557c8aef09de529333e12344c58b body_fp=ff6430b9bac25e154f23862c4dde4c660c4fc2f4970913f6c48d50fe33553295 source_ref=c2dff8907b251d36ea66f85df0d978cec2ed679e role=test -->
Test `write_digest` for filesystem contract: timestamped file creation under `triefacts/triediffs/`, `TRIE_DIFF.md` symlink management, in-place rewrite via `reuse_file`, legacy regular-file replacement, and `max_entries` retention pruning.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_one_line_flattens_and_truncates fingerprint=2f0ba482c18eb7978c4e4724a58f3a1e674200782e5d3f29c4a862a8f082989c body_fp=b0b2db762e1f94b4d614e613fd8aca35ce2348fe5a6f7b11e5ea5bb7d4203c80 source_ref=c2dff8907b251d36ea66f85df0d978cec2ed679e role=test -->
Verify `_one_line` flattens multiline text, collapses whitespace, cuts at sentence boundaries, truncates long input to ≤200 chars with `…`, and returns `""` for empty input.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_first_line_preserves_full_intent_without_truncation fingerprint=ffab40c9bd610faa4508b1113fd374b1288bb3a1de706b7af890bd5f6fae39c2 body_fp=cac1d472acfe236c456be4d3fba47afd60d1d5d172bc7d5da276044dde4ad8c9 source_ref=88ab7199843febfd95eb072ba13dc516a3d5aa7e role=test -->
Verify that `_first_line` returns the complete first non-empty line with no sentence-boundary cut, no character cap, and no ellipsis.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_change_bullets_record_full_intent_no_ellipsis fingerprint=972a63a26e64b558119cf5b3964010d2a872cf6e3c3da6dd3c61986fee755c90 body_fp=57fbf982a9fa1a4d3edcd8c64aaf34765c54dd2e901507cb651b1ef9f09f10ba source_ref=88ab7199843febfd95eb072ba13dc516a3d5aa7e role=test -->
Assert that `render_digest_section` preserves long notes verbatim in change and staged bullets, with no ellipsis truncation in the Changes section.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_collect_symbol_deltas_before_after fingerprint=69389e9411dc11c1f5a44e402bb7eb71dbf9d3b752658f453a85ef6061c4ea8b body_fp=6b3606b0e5e94df200f2aed93cb75263556ef5e3c312158b78cb930c3550cbe5 source_ref=c2dff8907b251d36ea66f85df0d978cec2ed679e role=test -->
Test that `collect_symbol_deltas` returns `changed` rows with `before`/`after` prose, `added` rows for new symbols, no row for unchanged symbols, and excludes symbols from the digest archive subdirectory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_merge_applied_by_symbol_first_note_wins fingerprint=2a24c952c5e057186e3287e08d5a7ac89f95b21a54f20f7060f39b27b3fb0660 body_fp=dfc99a0c54ed5d2dc9c02a715e2846211f52df600ec1e2def897b4708396de45 source_ref=c2dff8907b251d36ea66f85df0d978cec2ed679e role=test -->
Verify that `merge_applied_by_symbol` deduplicates entries by `qname`, preserves the first `op` and `note`, and counts subsequent entries as `followups`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_symbol_and_file_history_from_digest_archive fingerprint=f6cb9edbe398a9db418796cf2bbbcd9804768fad741e7767c019a10377d42064 body_fp=647cef2ceaa6b4cb9cca7d4de753537d95098e896a2bb9bc7f363a48812c551d source_ref=c2dff8907b251d36ea66f85df0d978cec2ed679e role=test -->
Test `iter_digest_entries`, `symbol_history`, and `file_history` against a synthetic digest archive.

- Verifies entries are returned newest-first and unparseable files are ignored.
- Confirms overflow markers and Staged-section lines are excluded from `changes`.
- Checks exact-match semantics: substring qnames produce no results.
- Asserts `limit` parameter is honoured by `symbol_history`.
- Validates `file_history` aggregates all symbols sharing a module prefix.
<!-- trie:end -->