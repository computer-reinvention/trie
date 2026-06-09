---
trie_version: 0.1.5
source: tests/test_incremental.py
file_fingerprint: 8a62f0c285b7cf16d1f3454e2c33a8a96493c90320181c04e3e3749cd1ff2819
last_synced_at: '2026-06-07T05:47:14Z'
defines:
- kind: module
  qualified_name: tests/test_incremental:__module__
  lines: 1-405
- kind: function
  qualified_name: tests/test_incremental:project
  lines: 19-32
- kind: function
  qualified_name: tests/test_incremental:_initial_sync
  lines: 35-48
- kind: function
  qualified_name: tests/test_incremental:test_incremental_no_op_when_clean
  lines: 51-65
- kind: function
  qualified_name: tests/test_incremental:test_incremental_resyncs_directly_changed_file
  lines: 68-86
- kind: function
  qualified_name: tests/test_incremental:test_incremental_cascades_to_callers
  lines: 89-110
- kind: function
  qualified_name: tests/test_incremental:test_incremental_respects_budget
  lines: 113-131
- kind: function
  qualified_name: tests/test_incremental:test_incremental_dispatched_via_cli
  lines: 134-159
- kind: function
  qualified_name: tests/test_incremental:test_incremental_clean_via_cli
  lines: 162-174
- kind: function
  qualified_name: tests/test_incremental:test_incremental_with_no_changes_yields_empty
  lines: 177-191
- kind: function
  qualified_name: tests/test_incremental:test_incremental_handles_missing_triefact
  lines: 194-209
- kind: function
  qualified_name: tests/test_incremental:test_triefact_regenerated_only_for_affected_symbols_v01_limitation
  lines: 212-238
- kind: function
  qualified_name: tests/test_incremental:test_run_incremental_invokes_progress_callback
  lines: 241-293
- kind: function
  qualified_name: tests/test_incremental:test_compute_incremental_worklist_empty_when_clean
  lines: 296-305
- kind: function
  qualified_name: tests/test_incremental:test_compute_incremental_worklist_includes_cascade
  lines: 308-319
- kind: function
  qualified_name: tests/test_incremental:test_compute_incremental_worklist_is_read_only
  lines: 322-334
- kind: function
  qualified_name: tests/test_incremental:test_compute_incremental_worklist_reports_orphans
  lines: 337-349
- kind: function
  qualified_name: tests/test_incremental:test_cli_plan_incremental_on_clean_tree_reports_noop
  lines: 352-368
- kind: function
  qualified_name: tests/test_incremental:test_cli_plan_incremental_on_drift_lists_only_affected
  lines: 371-387
- kind: function
  qualified_name: tests/test_incremental:test_cli_plan_all_forces_full_bootstrap_view
  lines: 390-404
incoming_refs: 0
outgoing_refs: 67
---
<!-- trie:section symbol=tests/test_incremental:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=417935d1c34a8cc18e5741c536af59d3c110c7a5cd5782a88324cb472f8ffe8f source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test-infrastructure -->
Tests for incremental synchronization functionality including cascade detection, budget limits, CLI routing, and worklist computation.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:project fingerprint=4e084006f178a9857caa68e57d59fa178c9ea3c6baac1bde21faa670adc80dea body_fp=0a7f998b9e356c6636b56be0a4becbde817462c8e4686f69b691fd2f59d687b5 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test-infrastructure -->
Pytest fixture that creates a temporary project directory with trie config, lib.py, and app.py for testing incremental sync functionality.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:_initial_sync fingerprint=19f828a287e74e17fb5815cd69f3830e5f4503b2184e00c8d3630d3a0be01605 body_fp=b8237898c7df8997ac4e60b90a66d1c55589da63ca6c580aafb37cc0fff70739 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test-infrastructure -->
Creates initial triefacts for lib.py and app.py using fake client responses.

- Uses FakeTrieClient with hardcoded "v1" output bodies for consistent test setup
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_no_op_when_clean fingerprint=88fcf5a07320e6e6a6898d8ec818ea05472e9c1fe359a9487c5d3555f6c3b0e2 body_fp=6c01919ce1b25bdd3c1aa8f5db307edc25ab0c009dbc39d72d544d86820a46bb source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test -->
Verifies incremental sync performs no work when all triefacts are up-to-date with source files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_resyncs_directly_changed_file fingerprint=b85bcd905c8ae3f2c0d017f024aa870a61d8a4833413467123ba8c15408719b8 body_fp=e0383cd3ce88298cd282897dfbe4e46311810f3cad3faeb661f2a19dcae922bd source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test -->
Tests that `run_incremental` resyncs a file when its source content changes directly.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_cascades_to_callers fingerprint=1a95fb6afc0cf2e0f53dfc94ad563bf7b0d8f80435e30dc35159d35975602d6e body_fp=a299156928eab9352ed085b1726c47b3e3717148fec57f74e26dbf1889d2cb2c source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test -->
Tests that modifying a file triggers cascaded regeneration of its dependents via incremental sync.

- Modifies lib.py after initial sync, verifies both lib.py and app.py are regenerated
- Validates cascade counts: 1 directly stale, 1 cascaded file
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_respects_budget fingerprint=04bdeeb4d89158444a5e2992e804a6d9579264e9f628bd719f996fbadaeb14d6 body_fp=a0c7d4d412e745b7c1f54ea00fe73ab21eb87fc843a99053c9c4c4618622a870 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test -->
Tests that run_incremental stops processing files when budget is exhausted.

- Sets up a project with stale files that would cascade
- Runs incremental sync with a tiny budget (0.0001 USD)
- Verifies some files sync but others are skipped due to budget constraints
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_dispatched_via_cli fingerprint=4a90404380aa80415fd81dced526cdff5bf9d212639a159913dc18ea05ba6992 body_fp=f3ce1c7425dcb1ff80975a982255b188355060a66254944bfa7c04a5e42d8ed0 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test-infrastructure -->
Tests that `trie sync` CLI command routes through incremental sync and regenerates cascaded triefacts.

- Modifies source file to trigger incremental sync
- Mocks client to inject identifiable output content 
- Verifies both directly changed and cascaded files get regenerated with expected content
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_clean_via_cli fingerprint=1e718e0f925df852f5addd2cb488022f865c67a55380d521ca0b4965c38d3cf6 body_fp=fe94fff094bd169495fdf11fffa15be11f582348ad78d7cc8f4dcb6c9a3429b1 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test-infrastructure -->
Verifies that `trie sync` reports "coherent" when no files need updating.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_with_no_changes_yields_empty fingerprint=846cbe05b5e0e137dd212f80c02a87f499be74cb900023d6bab72d309145b92e body_fp=87f408c36a19c2270b149df1cbbe094629abf63cc781b1bc4c82568b023b4dea source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test -->
Tests that incremental sync performs no operations when source files and triefacts are unchanged.

- Verifies `directly_stale_count` is 0
- Verifies `cascaded_count` is 0  
- Verifies `files_synced` is 0
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_handles_missing_triefact fingerprint=879a299f4eb31e0d2b869bea257c5b3b21131e22e4ad5bcc3fb53163484f21fb body_fp=e9e9d6da3a448ff73ca5ec4f7c552642c61ab25fbf22772f07b341ed312c8fc8 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test -->
Test that verifies run_incremental handles projects with no existing triefacts by marking all files with public symbols as directly stale.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_triefact_regenerated_only_for_affected_symbols_v01_limitation fingerprint=0a9e2046dc131c3000bfe9fa03a00508cb967fa052fcf4e88d29b8fbdefcde50 body_fp=ee08654dc4ddfd02e418838bd8f40b9851f11dcd8074c0ec1cc47390fb6c4339 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test -->
Documents that v0.1 incremental sync regenerates entire files rather than individual symbol sections.

- Tests that modifying one symbol causes the whole file's triefact to regenerate
- Verifies cascade behavior pulls in dependent files completely
- Confirms both lib.py and app.py triefacts contain their expected symbol sections after sync
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_run_incremental_invokes_progress_callback fingerprint=412274a40568b9a4b7ab6ef350db630f15eb17287688711580021655266352ed body_fp=ad623ec5972dd2af67befb4a116c21fe08ac66f16bfebb2ab0b38f7c2b934fca source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test -->
Tests that `run_incremental` invokes progress callbacks during cascade-driven file synchronization.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_empty_when_clean fingerprint=cee10449e37638cbcb7584f41c7a16959603fbd74fc37e487f6c4431acef61cd body_fp=3642e88b1aee3377b22e576960a0e363f443f9310804eaa2de372dedc41ab1b3 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test -->
Verifies that `compute_incremental_worklist` returns empty lists when the project state is coherent with existing triefacts.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_includes_cascade fingerprint=19c15c1b29c078331a336f622e363b66959f8716f801ca6fe7080644d95a55c2 body_fp=d0cad7b7945571a3dff45cf8740c6285ba374020a6c804096678f5f5241adfd1 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test -->
Tests that editing lib.py includes both lib.py (direct) and app.py (cascade) in the incremental worklist without LLM calls.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_is_read_only fingerprint=b52fe57285334a3855e29c7336c6bcbc9cc95bfb04a5a962c757fce08ac63a67 body_fp=d2c5cf2c93a02f5e7ca00c1185ffc0e3b655da990de62b3608fcc68354ad8734 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test -->
Verifies that `compute_incremental_worklist` does not modify triefact files when analyzing project changes.

- Captures triefact directory state before and after worklist computation
- Modifies source file to trigger stale detection
- Asserts triefact files remain unchanged after analysis
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_reports_orphans fingerprint=485e1297b791feffbf91b27b19055ae1493474b073d92853ea881e5c40bfad3c body_fp=12bdf4154caeffc47c16d28385b159a3cb06db35a503ef7690f79675e3953015 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test -->
Tests that `compute_incremental_worklist` detects orphaned triefacts when source files are deleted without removing them from disk.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_cli_plan_incremental_on_clean_tree_reports_noop fingerprint=4db390236c0ccf4b0a6740b4884f58820085d76652e2c109d278c69e7638a4d9 body_fp=dae6a4d5c108230dee741b1b7c4d339a9752eb88fbbc8748b3a633218e48c627 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test-infrastructure -->
Verifies that `trie plan` on a coherent established project reports no-op rather than full-bootstrap costs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_cli_plan_incremental_on_drift_lists_only_affected fingerprint=8af4a0d4196163c1948a984c33f635d05f98b0f37378f54703608740eb844080 body_fp=c8975da251c6e35eb1fae0ef16db600a2408c1b161ce43dcf667ebfe3699d21b source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test-infrastructure -->
Tests that `trie plan` on an established project with file changes shows only incremental sync costs rather than full bootstrap costs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_cli_plan_all_forces_full_bootstrap_view fingerprint=4b275d51edf24baed79b45e27f8bf548affa56b8c67ab6f014a8b1f227e37ede body_fp=81e2a4ce5c3b91722bfb9f3ddfe63330a252a07d229b813e0c68d5735c240955 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=cli-interface -->
Verifies `trie plan --all` displays full bootstrap costs on established projects instead of incremental planning.
<!-- trie:end -->