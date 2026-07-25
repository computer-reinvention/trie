---
trie_version: 0.1.9
source: tests/test_edits_pipeline.py
file_fingerprint: 50ddfb20d295e8396ece5f98dcbf719d13b91b115d6325bf82aded6883674c9f
last_synced_at: '2026-07-25T11:48:31Z'
description: 'Spec for the slimmed patch pipeline: an intent store, not a code generator.'
defines:
- kind: module
  qualified_name: tests/test_edits_pipeline:__module__
  lines: 1-119
- kind: class
  qualified_name: tests/test_edits_pipeline:TestSessionNoteQuality
  lines: 14-20
- kind: method
  qualified_name: tests/test_edits_pipeline:TestSessionNoteQuality.test_rejects_short_and_boilerplate
  lines: 15-17
- kind: method
  qualified_name: tests/test_edits_pipeline:TestSessionNoteQuality.test_accepts_real_note
  lines: 19-20
- kind: function
  qualified_name: tests/test_edits_pipeline:_project
  lines: 23-40
- kind: function
  qualified_name: tests/test_edits_pipeline:test_record_intent_archives_notes_without_generation
  lines: 43-83
- kind: function
  qualified_name: tests/test_edits_pipeline:test_record_intent_preserves_structural_ops
  lines: 86-95
- kind: function
  qualified_name: tests/test_edits_pipeline:test_single_symbol_needs_no_session_note
  lines: 98-105
- kind: function
  qualified_name: tests/test_edits_pipeline:test_preview_patches_reports_pending_and_blast_radius
  lines: 108-118
incoming_refs: 0
outgoing_refs: 10
---
<!-- trie:section symbol=tests/test_edits_pipeline:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=779d3118d360be3e6cc31619bc506e3cfef98d30e9e27ade7938a41986fc4d11 source_ref=e0282d34035b65bdf7e8d362970ae8d5376a0584 role=test -->
Tests the edits pipeline functionality including staging, committing, and import fixup operations.

- PROJECT_TOML: configuration template defining trie project structure and model settings
- FakeTriefactClient: mock client returning deterministic SectionBody for sync operations
- project: pytest fixture creating temporary project with three-module dependency chain
- TestStageNoWrites: verifies staging operations don't modify source files
- TestCommitApplies: tests successful patch application and database cleanup
- TestCompileGate: ensures broken code generation is handled as unresolved errors
- TestAtomicity: validates all-or-nothing vs per-item commit modes
- TestImportFixup: tests import statement modification for structural changes
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:TestSessionNoteQuality fingerprint=a1ee057368bb1848f6f5a7a57f527c47a73c50cbfe0bb89131eeaf2b9adde649 body_fp=f8e6aab983c57c580a8ef2736ad905c86c4c7917e87c5096dbcacb81da517e58 source_ref=216da440140e9e9a0724eb58e004820fb538cdc8 role=test -->
Test class verifying `session_note_ok` rejects short/boilerplate strings and accepts well-formed notes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:TestSessionNoteQuality.test_rejects_short_and_boilerplate fingerprint=f1ff85e1b2f4b669cbe3d859ec7e562130f6fe90704eb9ad52998bda45f01501 body_fp=261d6d940e793ea5566d1f911055c6debf3e22435507e2997d1ee7eb271ed5f1 source_ref=216da440140e9e9a0724eb58e004820fb538cdc8 role=test -->
Assert that `TestSessionNoteQuality` rejects empty, punctuation-only, and common boilerplate strings via `session_note_ok`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:TestSessionNoteQuality.test_accepts_real_note fingerprint=4c02801f05c17a36b7c5d0750a8178d9807d344a55eb578f05a7b7708e01c85e body_fp=ba19b23ad1d4576694f8bfbcc99b28cd38e0f8032bf8d920c69ad41ad0619de6 source_ref=216da440140e9e9a0724eb58e004820fb538cdc8 role=test -->
Assert that `TestSessionNoteQuality` accepts a well-formed, descriptive session note via `session_note_ok`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:_project fingerprint=4b2b2f609afd05dc7a9c18f084ecb10caa49ae961a11408bb965edd03ab1b2ec body_fp=e986fc3c2079c41ff89c85e1da61dbf07d3a0c1f290fc42ba2ac561f26575b73 source_ref=216da440140e9e9a0724eb58e004820fb538cdc8 role=test -->
Build a minimal in-`tmp_path` git repo with a two-symbol `m.py`, a populated `Store`, and a `g→f` call edge for blast-radius tests.

- Returns a `(Config, Store)` tuple ready for pipeline test use.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:test_record_intent_archives_notes_without_generation fingerprint=86ece2c32493b092669f06f97b0a2b5abb4db34c0bb9bc491f1a05cad0e6651b body_fp=398692cb6b32310b59a9de6e8d932b1a01b634a81f69d093de3b4203c0c85e5b source_ref=97ea987c78febe85ff2c0d057f9bf07443d659ed role=test -->
Verify that `record_intent` seals patches in-store with the session note, leaves source files unmodified without generating code, and that consuming applied patches empties the store tables.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:test_record_intent_preserves_structural_ops fingerprint=f12e109f06dbbe243aaa11eb4d62d1828b4f734d41e9881e84fc9e43a58a69ad body_fp=f8f3cffd60109e59be6ead1b8cf9fc63d797a8a29f94bb0442b13ffc8766cdc9 source_ref=97ea987c78febe85ff2c0d057f9bf07443d659ed role=test -->
Verify that `record_intent` archives a `delete`-kind patch without requiring a session note and seals it with the correct kind in the store.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:test_single_symbol_needs_no_session_note fingerprint=7e06b4b7d7dd1a429364f560a6fe63f89833872fe544bdbf22eca4ec403bb181 body_fp=46343806dd31be8d9de4c43548a50e6452ed52eb2b733e3d0a5bc9b875886271 source_ref=216da440140e9e9a0724eb58e004820fb538cdc8 role=test -->
Assert that `record_intent` succeeds with an empty session note when only one symbol is queued.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:test_preview_patches_reports_pending_and_blast_radius fingerprint=a55df979069a8411b96cb8fafcfcae33e49683e77fcf8dee8bc4bbddd9b13ddc body_fp=7b741b03e1283cbc7169204ddf965f315d25212e11986fbf034092437fb65cdc source_ref=216da440140e9e9a0724eb58e004820fb538cdc8 role=test -->
Verify that `preview_patches` returns the pending symbol list and includes callers (`m:g`) in the cascade blast radius.
<!-- trie:end -->