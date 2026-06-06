---
trie_version: 0.1.5
source: tests/test_incremental.py
file_fingerprint: 8a62f0c285b7cf16d1f3454e2c33a8a96493c90320181c04e3e3749cd1ff2819
last_synced_at: '2026-06-06T13:44:30Z'
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
<!-- trie:section symbol=tests/test_incremental:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=4711276e90fe1ac84ee08ae4fc2167af651d31569ad2df9aa93671424122ed8e source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test-infrastructure -->
Tests incremental synchronization functionality that updates only changed files and their dependents.

- `project` fixture creates a temporary project with lib.py and app.py files
- `_initial_sync()` helper bootstraps initial triefacts for both files
- Tests verify cascade behavior when lib.py changes trigger app.py regeneration
- Tests verify budget constraints, CLI routing, and progress callbacks
- Tests verify worklist computation for planning without side effects
- Tests verify orphan triefact detection when source files are deleted
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=417935d1c34a8cc18e5741c536af59d3c110c7a5cd5782a88324cb472f8ffe8f source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e -->
Tests for incremental synchronization functionality including cascade detection, budget limits, CLI routing, and worklist computation.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:project fingerprint=4e084006f178a9857caa68e57d59fa178c9ea3c6baac1bde21faa670adc80dea body_fp=78dedd416b7d04f53522878d73355c91cee1fec2624727c184b109ffd4d22b14 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test-infrastructure -->
Creates a temporary project directory with trie configuration and two interdependent Python files for testing incremental sync behavior.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:project fingerprint=4e084006f178a9857caa68e57d59fa178c9ea3c6baac1bde21faa670adc80dea body_fp=0a7f998b9e356c6636b56be0a4becbde817462c8e4686f69b691fd2f59d687b5 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e -->
Pytest fixture that creates a temporary project directory with trie config, lib.py, and app.py for testing incremental sync functionality.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:_initial_sync fingerprint=19f828a287e74e17fb5815cd69f3830e5f4503b2184e00c8d3630d3a0be01605 body_fp=652189108852e3eef5b85b093a5138f0a08233347a1bc82891a5ee1201032bd3 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test-infrastructure -->
Syncs both lib.py and app.py in the test project to establish baseline triefacts.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:_initial_sync fingerprint=19f828a287e74e17fb5815cd69f3830e5f4503b2184e00c8d3630d3a0be01605 body_fp=b8237898c7df8997ac4e60b90a66d1c55589da63ca6c580aafb37cc0fff70739 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e -->
Creates initial triefacts for lib.py and app.py using fake client responses.

- Uses FakeTrieClient with hardcoded "v1" output bodies for consistent test setup
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_no_op_when_clean fingerprint=88fcf5a07320e6e6a6898d8ec818ea05472e9c1fe359a9487c5d3555f6c3b0e2 body_fp=e0d6392da412ee7fba08cf4e175b24f799b230d7ee7fdbead4a27cea9c71ef48 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test -->
Verifies incremental sync performs no work when all triefacts are current.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_no_op_when_clean fingerprint=88fcf5a07320e6e6a6898d8ec818ea05472e9c1fe359a9487c5d3555f6c3b0e2 body_fp=6c01919ce1b25bdd3c1aa8f5db307edc25ab0c009dbc39d72d544d86820a46bb source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e -->
Verifies incremental sync performs no work when all triefacts are up-to-date with source files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_resyncs_directly_changed_file fingerprint=b85bcd905c8ae3f2c0d017f024aa870a61d8a4833413467123ba8c15408719b8 body_fp=c76e89412ad4bcd6cf6b6c0647dc9968ec82664d358bf8b5276d4c196aa9c19a source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test -->
Tests that `run_incremental` detects and resyncs a file when its source code changes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_resyncs_directly_changed_file fingerprint=b85bcd905c8ae3f2c0d017f024aa870a61d8a4833413467123ba8c15408719b8 body_fp=e0383cd3ce88298cd282897dfbe4e46311810f3cad3faeb661f2a19dcae922bd source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e -->
Tests that `run_incremental` resyncs a file when its source content changes directly.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_cascades_to_callers fingerprint=1a95fb6afc0cf2e0f53dfc94ad563bf7b0d8f80435e30dc35159d35975602d6e body_fp=30d97e26c38a36a7fd8b651775a6d9852093429278e8e14b2fa8300fbe0a958f source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test -->
Tests that incremental sync propagates changes to dependent files via cascade mechanism.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_cascades_to_callers fingerprint=1a95fb6afc0cf2e0f53dfc94ad563bf7b0d8f80435e30dc35159d35975602d6e body_fp=a299156928eab9352ed085b1726c47b3e3717148fec57f74e26dbf1889d2cb2c source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e -->
Tests that modifying a file triggers cascaded regeneration of its dependents via incremental sync.

- Modifies lib.py after initial sync, verifies both lib.py and app.py are regenerated
- Validates cascade counts: 1 directly stale, 1 cascaded file
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_respects_budget fingerprint=04bdeeb4d89158444a5e2992e804a6d9579264e9f628bd719f996fbadaeb14d6 body_fp=665f4061e59633d0b1227742ca1f8b8fecf87d69bb970be4644c33e01b6a54a3 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test -->
Tests that run_incremental honors budget limits and skips files when cost exceeds the budget threshold.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_respects_budget fingerprint=04bdeeb4d89158444a5e2992e804a6d9579264e9f628bd719f996fbadaeb14d6 body_fp=a0c7d4d412e745b7c1f54ea00fe73ab21eb87fc843a99053c9c4c4618622a870 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e -->
Tests that run_incremental stops processing files when budget is exhausted.

- Sets up a project with stale files that would cascade
- Runs incremental sync with a tiny budget (0.0001 USD)
- Verifies some files sync but others are skipped due to budget constraints
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_dispatched_via_cli fingerprint=4a90404380aa80415fd81dced526cdff5bf9d212639a159913dc18ea05ba6992 body_fp=c0639d793a8e3234414b06d929ca2b65e6b4d0a390287501ade5a6dfb6940bcf source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=cli-interface -->
Verifies that `trie sync` CLI command routes through incremental sync functionality and properly regenerates triefacts.

- Sets up project with changes to trigger incremental sync
- Mocks the LLM client to inject identifiable output
- Validates CLI output indicates sync and cascade operations
- Confirms regenerated triefacts contain the mocked client output
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_dispatched_via_cli fingerprint=4a90404380aa80415fd81dced526cdff5bf9d212639a159913dc18ea05ba6992 body_fp=f3ce1c7425dcb1ff80975a982255b188355060a66254944bfa7c04a5e42d8ed0 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e -->
Tests that `trie sync` CLI command routes through incremental sync and regenerates cascaded triefacts.

- Modifies source file to trigger incremental sync
- Mocks client to inject identifiable output content 
- Verifies both directly changed and cascaded files get regenerated with expected content
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_clean_via_cli fingerprint=1e718e0f925df852f5addd2cb488022f865c67a55380d521ca0b4965c38d3cf6 body_fp=c4e3d045bb530d5f3951b24a23f2258ae736f9dc552d9110d9b9c1e6953552c6 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test-infrastructure -->
Verifies `trie sync` on an unchanged project reports the tree as coherent without performing any LLM work.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_clean_via_cli fingerprint=1e718e0f925df852f5addd2cb488022f865c67a55380d521ca0b4965c38d3cf6 body_fp=fe94fff094bd169495fdf11fffa15be11f582348ad78d7cc8f4dcb6c9a3429b1 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e -->
Verifies that `trie sync` reports "coherent" when no files need updating.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_with_no_changes_yields_empty fingerprint=846cbe05b5e0e137dd212f80c02a87f499be74cb900023d6bab72d309145b92e body_fp=9c7a619715460ab6b9b9a262427b315f50fd80f1916d959b30b8ba16ce1509c7 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test -->
Verifies that incremental sync performs no operations when triefacts exist and source files are unchanged.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_with_no_changes_yields_empty fingerprint=846cbe05b5e0e137dd212f80c02a87f499be74cb900023d6bab72d309145b92e body_fp=87f408c36a19c2270b149df1cbbe094629abf63cc781b1bc4c82568b023b4dea source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e -->
Tests that incremental sync performs no operations when source files and triefacts are unchanged.

- Verifies `directly_stale_count` is 0
- Verifies `cascaded_count` is 0  
- Verifies `files_synced` is 0
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_handles_missing_triefact fingerprint=879a299f4eb31e0d2b869bea257c5b3b21131e22e4ad5bcc3fb53163484f21fb body_fp=a284c02088b68f961f7a4dd9e0136affd5601b9121ad07fded3b74a941b523c4 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test -->
Tests that incremental sync treats all files as directly stale when no triefacts exist yet.

- Verifies both `lib.py` and `app.py` get synced when starting from scratch
- Confirms `directly_stale_count` is 2 (no cascade double-counting)
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_handles_missing_triefact fingerprint=879a299f4eb31e0d2b869bea257c5b3b21131e22e4ad5bcc3fb53163484f21fb body_fp=e9e9d6da3a448ff73ca5ec4f7c552642c61ab25fbf22772f07b341ed312c8fc8 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e -->
Test that verifies run_incremental handles projects with no existing triefacts by marking all files with public symbols as directly stale.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_triefact_regenerated_only_for_affected_symbols_v01_limitation fingerprint=0a9e2046dc131c3000bfe9fa03a00508cb967fa052fcf4e88d29b8fbdefcde50 body_fp=3608baa4424dc0b852a2b3709176fbd615d39b7b802f6ff278cd43187d936852 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test -->
Documents that incremental sync regenerates entire files rather than individual symbols when changes occur.

- Modifies only lib.py and verifies both lib.md and app.md are regenerated due to cascade
- Confirms v0.1 limitation: whole-file regeneration instead of per-symbol granularity
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_triefact_regenerated_only_for_affected_symbols_v01_limitation fingerprint=0a9e2046dc131c3000bfe9fa03a00508cb967fa052fcf4e88d29b8fbdefcde50 body_fp=ee08654dc4ddfd02e418838bd8f40b9851f11dcd8074c0ec1cc47390fb6c4339 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e -->
Documents that v0.1 incremental sync regenerates entire files rather than individual symbol sections.

- Tests that modifying one symbol causes the whole file's triefact to regenerate
- Verifies cascade behavior pulls in dependent files completely
- Confirms both lib.py and app.py triefacts contain their expected symbol sections after sync
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_run_incremental_invokes_progress_callback fingerprint=412274a40568b9a4b7ab6ef350db630f15eb17287688711580021655266352ed body_fp=3197bb9acd235558901b6a7c6f4063a0b0b555d14656ce9527340a0645d8b7b7 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test -->
Verifies that `run_incremental` streams per-file progress events to the provided callback during cascade-driven re-sync.

- Creates test project with lib.py and app.py files, syncs both initially
- Modifies lib.py to trigger cascade to app.py 
- Uses custom Recorder class to capture on_start and on_done callback invocations
- Asserts both files appear in captured progress events
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_run_incremental_invokes_progress_callback fingerprint=412274a40568b9a4b7ab6ef350db630f15eb17287688711580021655266352ed body_fp=ad623ec5972dd2af67befb4a116c21fe08ac66f16bfebb2ab0b38f7c2b934fca source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e -->
Tests that `run_incremental` invokes progress callbacks during cascade-driven file synchronization.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_empty_when_clean fingerprint=cee10449e37638cbcb7584f41c7a16959603fbd74fc37e487f6c4431acef61cd body_fp=3426d263139065383fb981161cfeb821a597a9707b23effab2b578bf4e4c5ecc source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test -->
Verifies `compute_incremental_worklist` returns empty worklist when project triefacts are coherent with source files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_empty_when_clean fingerprint=cee10449e37638cbcb7584f41c7a16959603fbd74fc37e487f6c4431acef61cd body_fp=3642e88b1aee3377b22e576960a0e363f443f9310804eaa2de372dedc41ab1b3 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e -->
Verifies that `compute_incremental_worklist` returns empty lists when the project state is coherent with existing triefacts.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_includes_cascade fingerprint=19c15c1b29c078331a336f622e363b66959f8716f801ca6fe7080644d95a55c2 body_fp=db70c7244aac5ba8e5b26f524aa4f3fdfe70747944121e14a55fd0586ef8f569 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test -->
Verifies that compute_incremental_worklist includes both directly modified files and cascade-affected dependencies.

- Modifies lib.py to make it directly stale
- Confirms lib.py appears in directly_stale list 
- Confirms app.py appears in cascaded_files (depends on lib.py)
- Verifies both files are included in affected_files
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_includes_cascade fingerprint=19c15c1b29c078331a336f622e363b66959f8716f801ca6fe7080644d95a55c2 body_fp=d0cad7b7945571a3dff45cf8740c6285ba374020a6c804096678f5f5241adfd1 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e -->
Tests that editing lib.py includes both lib.py (direct) and app.py (cascade) in the incremental worklist without LLM calls.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_is_read_only fingerprint=b52fe57285334a3855e29c7336c6bcbc9cc95bfb04a5a962c757fce08ac63a67 body_fp=ba03f18eccb8a06c893778b7c5d2cc7daa0ae22300fccd684aa3ad445b11a4bf source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test -->
Verifies that `compute_incremental_worklist` does not mutate triefact files when determining work needed.

- Snapshots triefact directory contents before and after calling `compute_incremental_worklist`
- Modifies source file to trigger stale detection but expects no file changes
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_is_read_only fingerprint=b52fe57285334a3855e29c7336c6bcbc9cc95bfb04a5a962c757fce08ac63a67 body_fp=d2c5cf2c93a02f5e7ca00c1185ffc0e3b655da990de62b3608fcc68354ad8734 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e -->
Verifies that `compute_incremental_worklist` does not modify triefact files when analyzing project changes.

- Captures triefact directory state before and after worklist computation
- Modifies source file to trigger stale detection
- Asserts triefact files remain unchanged after analysis
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_reports_orphans fingerprint=485e1297b791feffbf91b27b19055ae1493474b073d92853ea881e5c40bfad3c body_fp=438c836d73e9500148c90a238969ea4a847ef181c559f7e51c3917cc3772f902 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test -->
Verifies that `compute_incremental_worklist` identifies orphaned triefacts when source files are deleted.

- Creates initial sync then removes `lib.py` to orphan its triefact
- Confirms orphan appears in worklist without being deleted from disk
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_reports_orphans fingerprint=485e1297b791feffbf91b27b19055ae1493474b073d92853ea881e5c40bfad3c body_fp=12bdf4154caeffc47c16d28385b159a3cb06db35a503ef7690f79675e3953015 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e -->
Tests that `compute_incremental_worklist` detects orphaned triefacts when source files are deleted without removing them from disk.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_cli_plan_incremental_on_clean_tree_reports_noop fingerprint=4db390236c0ccf4b0a6740b4884f58820085d76652e2c109d278c69e7638a4d9 body_fp=ecfe3049527cc2686b925c5b5fae476756b6e79010ca8b020eb8c7becf67a005 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test-infrastructure -->
Tests that `trie plan` on a clean project reports no-op status rather than full-bootstrap cost.

- Verifies CLI output contains "coherent" or "no-op" messaging
- Ensures "plan for" header does not appear for established projects
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_cli_plan_incremental_on_clean_tree_reports_noop fingerprint=4db390236c0ccf4b0a6740b4884f58820085d76652e2c109d278c69e7638a4d9 body_fp=dae6a4d5c108230dee741b1b7c4d339a9752eb88fbbc8748b3a633218e48c627 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e -->
Verifies that `trie plan` on a coherent established project reports no-op rather than full-bootstrap costs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_cli_plan_incremental_on_drift_lists_only_affected fingerprint=8af4a0d4196163c1948a984c33f635d05f98b0f37378f54703608740eb844080 body_fp=126c4cef52710f6c7efbf047c81ad3144cc7772a9855ae049f09f5d7a444d7c0 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test-infrastructure -->
Tests that `trie plan` on a project with file changes shows incremental cost rather than full bootstrap cost.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_cli_plan_incremental_on_drift_lists_only_affected fingerprint=8af4a0d4196163c1948a984c33f635d05f98b0f37378f54703608740eb844080 body_fp=c8975da251c6e35eb1fae0ef16db600a2408c1b161ce43dcf667ebfe3699d21b source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e -->
Tests that `trie plan` on an established project with file changes shows only incremental sync costs rather than full bootstrap costs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_cli_plan_all_forces_full_bootstrap_view fingerprint=4b275d51edf24baed79b45e27f8bf548affa56b8c67ab6f014a8b1f227e37ede body_fp=3f02dd9ce5ad441c4383e121af63aee2afccf5ae09ce34cf024ba53db83f2adc source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test-infrastructure -->
Verifies `trie plan --all` shows full-bootstrap cost view on established projects instead of incremental planning.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_cli_plan_all_forces_full_bootstrap_view fingerprint=4b275d51edf24baed79b45e27f8bf548affa56b8c67ab6f014a8b1f227e37ede body_fp=81e2a4ce5c3b91722bfb9f3ddfe63330a252a07d229b813e0c68d5735c240955 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e -->
Verifies `trie plan --all` displays full bootstrap costs on established projects instead of incremental planning.
<!-- trie:end -->