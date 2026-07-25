---
trie_version: 0.1.9
source: tests/test_session_diff.py
file_fingerprint: a12acf1dbda509370ed1466a588a538d6a70db18d45155a3c59366ededf1e98d
last_synced_at: '2026-07-25T11:36:21Z'
description: Tests for the session log archive and the `trie diff` evidence collection/prompt
  assembly.
defines:
- kind: module
  qualified_name: tests/test_session_diff:__module__
  lines: 1-713
- kind: function
  qualified_name: tests/test_session_diff:test_pending_intent_roundtrip
  lines: 24-62
- kind: function
  qualified_name: tests/test_session_diff:test_pending_intent_flattens_multiline_notes
  lines: 65-83
- kind: function
  qualified_name: tests/test_session_diff:test_build_narrative_prompt_sections_and_truncation
  lines: 86-133
- kind: function
  qualified_name: tests/test_session_diff:test_collect_session_diff_gathers_all_evidence
  lines: 136-212
- kind: function
  qualified_name: tests/test_session_diff:test_collect_session_diff_includes_new_triefacts
  lines: 215-263
- kind: function
  qualified_name: tests/test_session_diff:test_synthesize_narrative_uses_cache_prefix
  lines: 266-330
- kind: function
  qualified_name: tests/test_session_diff:test_render_digest_section_shape
  lines: 333-475
- kind: function
  qualified_name: tests/test_session_diff:test_write_digest_files_symlink_and_prune
  lines: 478-539
- kind: function
  qualified_name: tests/test_session_diff:test_one_line_flattens_and_truncates
  lines: 542-569
- kind: function
  qualified_name: tests/test_session_diff:test_collect_symbol_deltas_before_after
  lines: 572-634
- kind: function
  qualified_name: tests/test_session_diff:test_merge_applied_by_symbol_first_note_wins
  lines: 637-658
- kind: function
  qualified_name: tests/test_session_diff:test_symbol_and_file_history_from_digest_archive
  lines: 661-712
incoming_refs: 0
outgoing_refs: 22
---
<!-- trie:section symbol=tests/test_session_diff:__module__ fingerprint=efba484e3aa652464eff4bb42149f2f8ad21e69db80743152ed50083f36a38f2 body_fp=1104a778ce390fa56813958cd8c63c2c3c38548adf128fd9b73f2b057fbc791e source_ref=17faca7a18030ef384494b789fa37a1b8d11cd20 role=test -->
Test module for session log archive and `trie diff` evidence collection and prompt assembly.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_pending_intent_roundtrip fingerprint=6681624fa2fe930bae3753def916c5ebddd34b872fbbb3fbfb0bbd95db70261f body_fp=9bd1f28f33cb9f92a70b3bdc7f7cce74986e49a08345f39d35d2f9f71b16095e source_ref=6f97b6fdd7ee1e1b25a6a61330c44c4c5230bae9 role=test -->
Verify that `append_intent`, `read_intent`, and `consume_intent` correctly write, parse, and delete the `.pending.md` file across two appended batches.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_pending_intent_flattens_multiline_notes fingerprint=57693e3ee76cd5a6dabf18022c0c4cca17440b6153e841a7ba8d85a96701cd5f body_fp=c482cf2a73f1645645a894f76b16ba4f541c245082c16860498dae1f40696396 source_ref=6f97b6fdd7ee1e1b25a6a61330c44c4c5230bae9 role=test -->
Verify that multiline note strings are collapsed to a single line and that no body line starts with `#` after writing pending intent.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_build_narrative_prompt_sections_and_truncation fingerprint=6446fd1cae84e737cb1b09ef79389e50b0648ad9f14d949905a4d413dd3c5263 body_fp=eea9a0dcc6b45f3e2fc0e3ad348aafecd880e63dd17c26c8eff4c60b49cca4c2 source_ref=d975eae36aecf24fcccb49ac5032cd7a805d1e02 role=test -->
Verify `build_narrative_prompt` emits correct sections, formats applied/pending entries, truncates `triefact_diff` to `max_diff_chars`, and handles an empty `SessionDiff`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_collect_session_diff_gathers_all_evidence fingerprint=46a4d44aa3b1e3f1d4f921e0c6c2ec2db59c04b3b756b4e02d0aa3b3bdaebea3 body_fp=9998e4986e5dcdd77c0158784f3084040c7373e750c12ccf914f2e0ba5e727f8 source_ref=6f97b6fdd7ee1e1b25a6a61330c44c4c5230bae9 role=test -->
Test `collect_session_diff` against a real git repo, verifying triefact diff content and applied/pending patch assembly via `append_intent` and store patches.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_collect_session_diff_includes_new_triefacts fingerprint=1c8f6b894cfb45576c6cdcf42ce71b213efaf3a7e307fcb041108fc82401e0af body_fp=7cfc1ad6e85ed5c97ed11f5b9323ac777fb66f15a8f60024b089842cfce18b6c source_ref=d975eae36aecf24fcccb49ac5032cd7a805d1e02 role=test -->
Verify that `collect_session_diff` includes untracked new triefact files in `triefact_diff`, not only modified tracked files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_synthesize_narrative_uses_cache_prefix fingerprint=4e3948647dcaca3e817614b7a09851a35a6f20ee9b139ed861ee7b4442cb7de2 body_fp=ba6a3b5193f2743db024f4b9c90042bdb7de6545dac14e9483d8d4ce5a7b7557 source_ref=d975eae36aecf24fcccb49ac5032cd7a805d1e02 role=test -->
Verify that `synthesize_narrative` passes the triefact diff as `cache_prefix` when the client supports it, and falls back to embedding it in the user prompt when the client lacks `cache_prefix`; also asserts `max_tokens >= 512` to guard against runaway truncation.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_render_digest_section_shape fingerprint=1baf8fbadf9592ac0616a4f6c8391dec9c91b39bc8e347722872ad1e8c9679b5 body_fp=8f6db62f45672b0bd5709d7ea6a5c774c1659a0e023e57c96d6b707f903741df source_ref=955596e075cf1ceb107ee51be2054a6a2fecab0c role=test -->
Verify `render_digest_section` output structure: header shape, H2-heading demotion in narratives, `### Changes` delta bullets, follow-up suffix, markdown-injection prevention, forbidden old-format artifacts, `### Staged (not applied)` section, and `max_changes` overflow truncation with lossless HTML-comment storage of capped-out rows.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_write_digest_files_symlink_and_prune fingerprint=a6d890f9a90cbf52aa184a2c3c03461db319557c8aef09de529333e12344c58b body_fp=ff6430b9bac25e154f23862c4dde4c660c4fc2f4970913f6c48d50fe33553295 source_ref=c981fd16a4af08aa07186b13567aabbfcb9a0871 role=test -->
Test `write_digest` for filesystem contract: timestamped file creation under `triefacts/triediffs/`, `TRIE_DIFF.md` symlink management, in-place rewrite via `reuse_file`, legacy regular-file replacement, and `max_entries` retention pruning.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_one_line_flattens_and_truncates fingerprint=2f0ba482c18eb7978c4e4724a58f3a1e674200782e5d3f29c4a862a8f082989c body_fp=b0b2db762e1f94b4d614e613fd8aca35ce2348fe5a6f7b11e5ea5bb7d4203c80 source_ref=f916af535b126787e42e039ab713e9d460879f00 role=test -->
Verify `_one_line` flattens multiline text, collapses whitespace, cuts at sentence boundaries, truncates long input to ≤200 chars with `…`, and returns `""` for empty input.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_collect_symbol_deltas_before_after fingerprint=69389e9411dc11c1f5a44e402bb7eb71dbf9d3b752658f453a85ef6061c4ea8b body_fp=6b3606b0e5e94df200f2aed93cb75263556ef5e3c312158b78cb930c3550cbe5 source_ref=c981fd16a4af08aa07186b13567aabbfcb9a0871 role=test -->
Test that `collect_symbol_deltas` returns `changed` rows with `before`/`after` prose, `added` rows for new symbols, no row for unchanged symbols, and excludes symbols from the digest archive subdirectory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_merge_applied_by_symbol_first_note_wins fingerprint=2a24c952c5e057186e3287e08d5a7ac89f95b21a54f20f7060f39b27b3fb0660 body_fp=dfc99a0c54ed5d2dc9c02a715e2846211f52df600ec1e2def897b4708396de45 source_ref=f916af535b126787e42e039ab713e9d460879f00 role=test -->
Verify that `merge_applied_by_symbol` deduplicates entries by `qname`, preserves the first `op` and `note`, and counts subsequent entries as `followups`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_symbol_and_file_history_from_digest_archive fingerprint=f6cb9edbe398a9db418796cf2bbbcd9804768fad741e7767c019a10377d42064 body_fp=647cef2ceaa6b4cb9cca7d4de753537d95098e896a2bb9bc7f363a48812c551d source_ref=d975eae36aecf24fcccb49ac5032cd7a805d1e02 role=test -->
Test `iter_digest_entries`, `symbol_history`, and `file_history` against a synthetic digest archive.

- Verifies entries are returned newest-first and unparseable files are ignored.
- Confirms overflow markers and Staged-section lines are excluded from `changes`.
- Checks exact-match semantics: substring qnames produce no results.
- Asserts `limit` parameter is honoured by `symbol_history`.
- Validates `file_history` aggregates all symbols sharing a module prefix.
<!-- trie:end -->