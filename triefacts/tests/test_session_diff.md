---
trie_version: 0.1.9
source: tests/test_session_diff.py
file_fingerprint: 2380be4883819136e11925166b585db5160793a73a92b860f3b9c018ee48e179
last_synced_at: '2026-07-23T16:52:11Z'
description: Tests for the session log archive and the `trie diff` evidence collection/prompt
  assembly.
defines:
- kind: module
  qualified_name: tests/test_session_diff:__module__
  lines: 1-543
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
  lines: 413-494
- kind: function
  qualified_name: tests/test_session_diff:test_upsert_digest_prepend_replace_trim
  lines: 497-542
incoming_refs: 0
outgoing_refs: 24
---
<!-- trie:section symbol=tests/test_session_diff:__module__ fingerprint=efba484e3aa652464eff4bb42149f2f8ad21e69db80743152ed50083f36a38f2 body_fp=1104a778ce390fa56813958cd8c63c2c3c38548adf128fd9b73f2b057fbc791e source_ref=17faca7a18030ef384494b789fa37a1b8d11cd20 role=test -->
Test module for session log archive and `trie diff` evidence collection and prompt assembly.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_record_and_read_entries_roundtrip fingerprint=c7e3db1153bff00b722213cbc7f566535a487dcac244203b9d5c0bb775e38d72 body_fp=8e4dae497157ec4a1c53f6ef650c551065a32498b11fdc5c2796f07deed00e97 source_ref=77eeca2410531f4fea3afc8dc004b3087f592ed5 role=test -->
Verify that `record_applied` writes entries readable by `read_entries`, session filtering works, and corrupt log lines are silently skipped.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_record_applied_empty_and_missing_log fingerprint=efc1090ce789e94dae0ed8c06180da043b2076a88688360f3a2ffde98cdca236 body_fp=a898c1b6d78aa9f131d096932df5487e0da026a5d5a6c8a8c40105c71f6dddc4 source_ref=77eeca2410531f4fea3afc8dc004b3087f592ed5 role=test -->
Assert that `record_applied` with an empty list creates no log file and `read_entries` returns an empty list.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_build_narrative_prompt_sections_and_truncation fingerprint=6446fd1cae84e737cb1b09ef79389e50b0648ad9f14d949905a4d413dd3c5263 body_fp=3faa4bd644f96a5fa15fed548664fe0c6a7fc87b9930d1bb2e0e5b27b5375f09 source_ref=77eeca2410531f4fea3afc8dc004b3087f592ed5 role=test -->
Verify `build_narrative_prompt` emits correct sections, formats entries, truncates diffs, and handles the empty-`SessionDiff` case.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_collect_session_diff_gathers_all_evidence fingerprint=54fe703e6478eef4a305c53c647c2d5374348f6c10de5bff50f5810fce7a06ea body_fp=9570f7e786b7b60eb43e3a38c9d17ad6e46ce73f7f7e99ba12e12f1284654bed role=monitoring-telemetry -->
Integration test for `collect_session_diff` that verifies the full evidence-gathering pipeline against a real git repository and store: it checks that triefact file diffs are captured, applied session-log entries are returned, pending modify and create patches are included with correct metadata, `session_ids()` aggregation works, session-scoped filtering (via `session_id`) correctly excludes unrelated entries, and — critically — that the `since` parameter (a float Unix timestamp) is forwarded to `read_entries` and correctly narrows the set of applied entries returned, using pytest-mock's `mocker` fixture to intercept and inspect the call.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_collect_session_diff_includes_new_triefacts fingerprint=1c8f6b894cfb45576c6cdcf42ce71b213efaf3a7e307fcb041108fc82401e0af body_fp=7cfc1ad6e85ed5c97ed11f5b9323ac777fb66f15a8f60024b089842cfce18b6c source_ref=17faca7a18030ef384494b789fa37a1b8d11cd20 role=test -->
Verify that `collect_session_diff` includes untracked new triefact files in `triefact_diff`, not only modified tracked files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_synthesize_narrative_uses_cache_prefix fingerprint=3113936385b8e907635ec1cc07bc23f9af2f841653adac1596f60d2559caaf85 body_fp=e86c163a4104695f2ea87721079357be8a9a69c45de450c623ca09c09cee010a source_ref=17faca7a18030ef384494b789fa37a1b8d11cd20 role=test -->
Verify that `synthesize_narrative` passes the triefact diff as `cache_prefix` when the client supports it, and falls back to embedding it in the user prompt when the client lacks `cache_prefix`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_collect_session_diff_since_filters_applied fingerprint=b8ad21187f0eed1369e497ac9b88cb62c894ddac513da36a098c170d0ffcfb7f body_fp=09b8b6feab2de3dcc762b79fe352bda9af2ba3b5238603bae54f6436ceec6f9f source_ref=17faca7a18030ef384494b789fa37a1b8d11cd20 role=test -->
Verify that `collect_session_diff` filters applied session log entries by the `since` timestamp, excluding entries older than the cutoff while retaining newer ones.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_render_digest_section_shape fingerprint=375b31e5d64792260c021ac9eed41a1aae876462f0295dd45e0c1914f0ddd250 body_fp=ff0b4a26fc25101710f73c1290ba1996191be384a5b71b110e5f54cbe728e446 source_ref=17faca7a18030ef384494b789fa37a1b8d11cd20 role=test -->
Verify that `render_digest_section` produces a correctly structured Markdown digest with header, narrative, intent, applied, pending, and triefact-change sections, and omits the narrative paragraph when `narrative` is empty.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_session_diff:test_upsert_digest_prepend_replace_trim fingerprint=1a5d2ded3951ca273be4c36b88c343b0345d023a4af8732a1ef7896c85e47eea body_fp=ecd57fd1db8a38e832e85c4ef97d9832621d710a0b924a6821b13171d9e83c52 source_ref=17faca7a18030ef384494b789fa37a1b8d11cd20 role=test -->
Verify `upsert_digest` correctly prepends new sections, replaces existing sections with the same `base_short`, and trims oldest entries when `max_entries` is exceeded.
<!-- trie:end -->