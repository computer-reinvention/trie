---
trie_version: 0.3.0
source: tests/test_edits_pipeline.py
file_fingerprint: 50ddfb20d295e8396ece5f98dcbf719d13b91b115d6325bf82aded6883674c9f
last_synced_at: '2026-07-29T23:18:11Z'
description: 'Spec for the slimmed patch pipeline: an intent store, not a code generator.'
defines:
- kind: module
  qualified_name: tests/test_edits_pipeline:__module__
  lines: 1-119
- kind: class
  qualified_name: tests/test_edits_pipeline:TestSessionNoteQuality
  lines: 14-20
  signature: class TestSessionNoteQuality
- kind: method
  qualified_name: tests/test_edits_pipeline:TestSessionNoteQuality.test_rejects_short_and_boilerplate
  lines: 15-17
  signature: def test_rejects_short_and_boilerplate(self)
- kind: method
  qualified_name: tests/test_edits_pipeline:TestSessionNoteQuality.test_accepts_real_note
  lines: 19-20
  signature: def test_accepts_real_note(self)
- kind: function
  qualified_name: tests/test_edits_pipeline:_project
  lines: 23-40
  signature: 'def _project(tmp_path: Path) -> tuple[Config, Store]'
- kind: function
  qualified_name: tests/test_edits_pipeline:test_record_intent_archives_notes_without_generation
  lines: 43-83
  signature: 'def test_record_intent_archives_notes_without_generation(tmp_path: Path) -> None'
- kind: function
  qualified_name: tests/test_edits_pipeline:test_record_intent_preserves_structural_ops
  lines: 86-95
  signature: 'def test_record_intent_preserves_structural_ops(tmp_path: Path) -> None'
- kind: function
  qualified_name: tests/test_edits_pipeline:test_single_symbol_needs_no_session_note
  lines: 98-105
  signature: 'def test_single_symbol_needs_no_session_note(tmp_path: Path) -> None'
- kind: function
  qualified_name: tests/test_edits_pipeline:test_preview_patches_reports_pending_and_blast_radius
  lines: 108-118
  signature: 'def test_preview_patches_reports_pending_and_blast_radius(tmp_path: Path) -> None'
incoming_refs: 0
outgoing_refs: 11
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
<!-- trie:section symbol=tests/test_edits_pipeline:TestSessionNoteQuality fingerprint=a1ee057368bb1848f6f5a7a57f527c47a73c50cbfe0bb89131eeaf2b9adde649 body_fp=0f306bd15fd88c5d51d3809d14e0fb2a773e390190d80dce4c26d2dc6d735cfc source_ref=97ea987c78febe85ff2c0d057f9bf07443d659ed role=test -->
## `class TestSessionNoteQuality`

Test class verifying `session_note_ok` rejects short/boilerplate strings and accepts well-formed notes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:TestSessionNoteQuality.test_rejects_short_and_boilerplate fingerprint=f1ff85e1b2f4b669cbe3d859ec7e562130f6fe90704eb9ad52998bda45f01501 body_fp=0f048eae7e9aa463cda4bdc140f97096f09e74b892201b708d42a1c8f54759a8 source_ref=97ea987c78febe85ff2c0d057f9bf07443d659ed role=test -->
## `def test_rejects_short_and_boilerplate(self)`

Assert that `TestSessionNoteQuality` rejects empty, punctuation-only, and common boilerplate strings via `session_note_ok`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:TestSessionNoteQuality.test_accepts_real_note fingerprint=4c02801f05c17a36b7c5d0750a8178d9807d344a55eb578f05a7b7708e01c85e body_fp=1195d51a7e18ec81e69c8f38ed525dd7ce99d350b60ea7e3702da0008636380e source_ref=97ea987c78febe85ff2c0d057f9bf07443d659ed role=test -->
## `def test_accepts_real_note(self)`

Assert that `TestSessionNoteQuality` accepts a well-formed, descriptive session note via `session_note_ok`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:_project fingerprint=4b2b2f609afd05dc7a9c18f084ecb10caa49ae961a11408bb965edd03ab1b2ec body_fp=0e2d82caf7c275d776db7f1ad203fcfba3c552e7dc39bf422c87d4a5b41ae67a source_ref=97ea987c78febe85ff2c0d057f9bf07443d659ed role=test -->
## `def _project(tmp_path: Path) -> tuple[Config, Store]`

Build a minimal in-`tmp_path` git repo with a two-symbol `m.py`, a populated `Store`, and a `g→f` call edge for blast-radius tests.

- Returns a `(Config, Store)` tuple ready for pipeline test use.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:test_record_intent_archives_notes_without_generation fingerprint=86ece2c32493b092669f06f97b0a2b5abb4db34c0bb9bc491f1a05cad0e6651b body_fp=3a1bf801aaeaf20647e6687fd3f5c430366793128aecb8bfc2ba5a557c342e0d source_ref=97ea987c78febe85ff2c0d057f9bf07443d659ed role=test -->
## `def test_record_intent_archives_notes_without_generation(tmp_path: Path) -> None`

Verify that `record_intent` seals patches in-store with the session note, leaves source files unmodified without generating code, and that consuming applied patches empties the store tables.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:test_record_intent_preserves_structural_ops fingerprint=f12e109f06dbbe243aaa11eb4d62d1828b4f734d41e9881e84fc9e43a58a69ad body_fp=9791fd4b0ed8402f07ed4129f46d2ad21e5534b4749f4e0080634d926a42455a source_ref=97ea987c78febe85ff2c0d057f9bf07443d659ed role=test -->
## `def test_record_intent_preserves_structural_ops(tmp_path: Path) -> None`

Verify that `record_intent` archives a `delete`-kind patch without requiring a session note and seals it with the correct kind in the store.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:test_single_symbol_needs_no_session_note fingerprint=7e06b4b7d7dd1a429364f560a6fe63f89833872fe544bdbf22eca4ec403bb181 body_fp=0dd835fa7effd93f202769bf18ec295e914d70d085c49c6d1f4c15e7621c755e source_ref=97ea987c78febe85ff2c0d057f9bf07443d659ed role=test -->
## `def test_single_symbol_needs_no_session_note(tmp_path: Path) -> None`

Assert that `record_intent` succeeds with an empty session note when only one symbol is queued.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_pipeline:test_preview_patches_reports_pending_and_blast_radius fingerprint=a55df979069a8411b96cb8fafcfcae33e49683e77fcf8dee8bc4bbddd9b13ddc body_fp=8c2b63f5dd6745c51e0569b7516f845ef98e6b642cda7e5ead06f5bd89c97b95 source_ref=97ea987c78febe85ff2c0d057f9bf07443d659ed role=test -->
## `def test_preview_patches_reports_pending_and_blast_radius(tmp_path: Path) -> None`

Verify that `preview_patches` returns the pending symbol list and includes callers (`m:g`) in the cascade blast radius.
<!-- trie:end -->