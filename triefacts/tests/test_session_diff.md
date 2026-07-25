---
trie_version: 0.1.9
source: tests/test_session_diff.py
file_fingerprint: aebe04e68ba9cb3727e9bf46fc598eb9c3b84d760be4d92b1fc3b4153878e4ca
last_synced_at: '2026-07-25T01:02:08Z'
description: Tests for the session log archive and the `trie diff` evidence collection/prompt
  assembly.
defines:
- kind: module
  qualified_name: tests/test_session_diff:__module__
  lines: 1-727
- kind: function
  qualified_name: tests/test_session_diff:test_record_and_read_entries_roundtrip
  lines: 24-61
- kind: function
  qualified_name: tests/test_session_diff:test_record_applied_empty_and_missing_log
  lines: 64-67
- kind: function
  qualified_name: tests/test_session_diff:test_build_narrative_prompt_sections_and_truncation
  lines: 70-117
- kind: function
  qualified_name: tests/test_session_diff:test_collect_session_diff_gathers_all_evidence
  lines: 120-227
- kind: function
  qualified_name: tests/test_session_diff:test_collect_session_diff_includes_new_triefacts
  lines: 230-278
- kind: function
  qualified_name: tests/test_session_diff:test_synthesize_narrative_uses_cache_prefix
  lines: 281-340
- kind: function
  qualified_name: tests/test_session_diff:test_collect_session_diff_since_filters_applied
  lines: 343-410
- kind: function
  qualified_name: tests/test_session_diff:test_render_digest_section_shape
  lines: 413-543
- kind: function
  qualified_name: tests/test_session_diff:test_write_digest_files_symlink_and_prune
  lines: 546-607
- kind: function
  qualified_name: tests/test_session_diff:test_one_line_flattens_and_truncates
  lines: 610-637
- kind: function
  qualified_name: tests/test_session_diff:test_collect_symbol_deltas_before_after
  lines: 640-702
- kind: function
  qualified_name: tests/test_session_diff:test_merge_applied_by_symbol_first_note_wins
  lines: 705-726
incoming_refs: 0
outgoing_refs: 25
---
<!-- trie:section symbol=tests/test_session_diff:__module__ fingerprint=efba484e3aa652464eff4bb42149f2f8ad21e69db80743152ed50083f36a38f2 body_fp=1104a778ce390fa56813958cd8c63c2c3c38548adf128fd9b73f2b057fbc791e source_ref=17faca7a18030ef384494b789fa37a1b8d11cd20 role=test -->
Test module for session log archive and `trie diff` evidence collection and prompt assembly.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_record_and_read_entries_roundtrip fingerprint=c7e3db1153bff00b722213cbc7f566535a487dcac244203b9d5c0bb775e38d72 body_fp=e0ccd0fda856441a96913ef6ecf68c719a5f4ad2f81c2312a824b3bb56795293 source_ref=c981fd16a4af08aa07186b13567aabbfcb9a0871 role=test -->
Verify that `record_applied` persists entries readable by `read_entries`, session filtering works, and corrupt log lines are silently skipped.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_record_applied_empty_and_missing_log fingerprint=efc1090ce789e94dae0ed8c06180da043b2076a88688360f3a2ffde98cdca236 body_fp=f735588b4fc4b13f98602ea2d491b7f39f14751facf275001d90c1b2bef9d4a1 source_ref=c981fd16a4af08aa07186b13567aabbfcb9a0871 role=test -->
Verify that `record_applied` with an empty list creates no log file and `read_entries` returns an empty list.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_build_narrative_prompt_sections_and_truncation fingerprint=6446fd1cae84e737cb1b09ef79389e50b0648ad9f14d949905a4d413dd3c5263 body_fp=eea9a0dcc6b45f3e2fc0e3ad348aafecd880e63dd17c26c8eff4c60b49cca4c2 source_ref=f916af535b126787e42e039ab713e9d460879f00 role=test -->
Verify `build_narrative_prompt` emits correct sections, formats applied/pending entries, truncates `triefact_diff` to `max_diff_chars`, and handles an empty `SessionDiff`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_collect_session_diff_gathers_all_evidence fingerprint=54fe703e6478eef4a305c53c647c2d5374348f6c10de5bff50f5810fce7a06ea body_fp=9c7182427ae7c876f2cf56b1f9de326c15a3fb32f2bca413083d1d9a599d1889 source_ref=c981fd16a4af08aa07186b13567aabbfcb9a0871 role=test -->
Test `collect_session_diff` against a real git repo, verifying triefact diff content, applied/pending patch assembly, session-id filtering, and `since` timestamp forwarding.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_collect_session_diff_includes_new_triefacts fingerprint=1c8f6b894cfb45576c6cdcf42ce71b213efaf3a7e307fcb041108fc82401e0af body_fp=7cfc1ad6e85ed5c97ed11f5b9323ac777fb66f15a8f60024b089842cfce18b6c source_ref=f916af535b126787e42e039ab713e9d460879f00 role=test -->
Verify that `collect_session_diff` includes untracked new triefact files in `triefact_diff`, not only modified tracked files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_synthesize_narrative_uses_cache_prefix fingerprint=3113936385b8e907635ec1cc07bc23f9af2f841653adac1596f60d2559caaf85 body_fp=e86c163a4104695f2ea87721079357be8a9a69c45de450c623ca09c09cee010a source_ref=f916af535b126787e42e039ab713e9d460879f00 role=test -->
Verify that `synthesize_narrative` passes the triefact diff as `cache_prefix` when the client supports it, and falls back to embedding it in the user prompt when the client lacks `cache_prefix`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_collect_session_diff_since_filters_applied fingerprint=b8ad21187f0eed1369e497ac9b88cb62c894ddac513da36a098c170d0ffcfb7f body_fp=09b8b6feab2de3dcc762b79fe352bda9af2ba3b5238603bae54f6436ceec6f9f source_ref=c981fd16a4af08aa07186b13567aabbfcb9a0871 role=test -->
Verify that `collect_session_diff` filters applied session log entries by the `since` timestamp, excluding entries older than the cutoff while retaining newer ones.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_render_digest_section_shape fingerprint=ce6e87b909a2e788f61327f21e9292f2470b06f81fc09d7ac35c79f85cfdd36d body_fp=b86e5fb0cd2f50c47b7fc4135264f2494231f9a983ad9e9f540c7b47ae44618e source_ref=f916af535b126787e42e039ab713e9d460879f00 role=test -->
Verify `render_digest_section` output structure: header shape, H2-heading demotion in narratives, `### Changes` delta bullets, follow-up suffix, markdown-injection prevention, forbidden old-format artifacts, `### Staged (not applied)` section, and `max_changes` overflow truncation.
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