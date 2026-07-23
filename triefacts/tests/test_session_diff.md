---
trie_version: 0.1.9
source: tests/test_session_diff.py
file_fingerprint: 7495d6e73759db7769206f85f50aff97edfc896e54e687166e43715570bdb69f
last_synced_at: '2026-07-20T23:25:34Z'
description: Tests for the session log archive and the `trie diff` evidence collection/prompt
  assembly.
defines:
- kind: module
  qualified_name: tests/test_session_diff:__module__
  lines: 1-301
- kind: function
  qualified_name: tests/test_session_diff:test_record_and_read_entries_roundtrip
  lines: 20-57
- kind: function
  qualified_name: tests/test_session_diff:test_record_applied_empty_and_missing_log
  lines: 60-63
- kind: function
  qualified_name: tests/test_session_diff:test_build_narrative_prompt_sections_and_truncation
  lines: 66-113
- kind: function
  qualified_name: tests/test_session_diff:test_collect_session_diff_gathers_all_evidence
  lines: 116-198
- kind: function
  qualified_name: tests/test_session_diff:test_collect_session_diff_includes_new_triefacts
  lines: 201-240
- kind: function
  qualified_name: tests/test_session_diff:test_synthesize_narrative_uses_cache_prefix
  lines: 243-300
incoming_refs: 0
outgoing_refs: 17
---
<!-- trie:section symbol=tests/test_session_diff:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=f8eebe79984e843049fdfbacdbe7e9a4d44a0f4bdd19324c14477bf14afd185b source_ref=77eeca2410531f4fea3afc8dc004b3087f592ed5 role=test -->
Tests for session log archive and `trie diff` evidence collection and prompt assembly.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_build_narrative_prompt_sections_and_truncation fingerprint=6446fd1cae84e737cb1b09ef79389e50b0648ad9f14d949905a4d413dd3c5263 body_fp=3faa4bd644f96a5fa15fed548664fe0c6a7fc87b9930d1bb2e0e5b27b5375f09 source_ref=77eeca2410531f4fea3afc8dc004b3087f592ed5 role=test -->
Verify `build_narrative_prompt` emits correct sections, formats entries, truncates diffs, and handles the empty-`SessionDiff` case.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_collect_session_diff_gathers_all_evidence fingerprint=71736ade6faaa73705f9e4d3048b95dd7c0709ececd227fbbd81e2105cc8184c body_fp=4c8c8dfae495946f2ac8d3a0ee8a02ebd1ec74a6e0222b2b6f151737f8c07fdf source_ref=77eeca2410531f4fea3afc8dc004b3087f592ed5 role=test -->
Integration test for `collect_session_diff`: verifies triefact git diff, applied log entries, pending patches, session ID aggregation, and session-scoped filtering against a real git repo and store.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_collect_session_diff_includes_new_triefacts fingerprint=c1dda275e06f1699121174755cf14bc12ae6299da25da2214574cef9301ccdf2 body_fp=a93e284f4e09f5d7e5c867569563703080c77fbdb14e84b700706674b750b5ba -->
This test verifies that `collect_session_diff` correctly detects and includes newly created (untracked) triefact files in the `triefact_diff` field of the returned `SessionDiff`. It sets up a temporary git repository with an initial committed triefact, then adds a new untracked triefact file simulating one created during a session, and asserts that both the file's prose content and its filename appear in the diff result.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_record_and_read_entries_roundtrip fingerprint=c7e3db1153bff00b722213cbc7f566535a487dcac244203b9d5c0bb775e38d72 body_fp=8e4dae497157ec4a1c53f6ef650c551065a32498b11fdc5c2796f07deed00e97 source_ref=77eeca2410531f4fea3afc8dc004b3087f592ed5 role=test -->
Verify that `record_applied` writes entries readable by `read_entries`, session filtering works, and corrupt log lines are silently skipped.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_record_applied_empty_and_missing_log fingerprint=efc1090ce789e94dae0ed8c06180da043b2076a88688360f3a2ffde98cdca236 body_fp=a898c1b6d78aa9f131d096932df5487e0da026a5d5a6c8a8c40105c71f6dddc4 source_ref=77eeca2410531f4fea3afc8dc004b3087f592ed5 role=test -->
Assert that `record_applied` with an empty list creates no log file and `read_entries` returns an empty list.
<!-- trie:end -->
