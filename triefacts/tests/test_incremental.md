---
trie_version: 0.3.0
source: tests/test_incremental.py
file_fingerprint: bad396edee2107b9efad99d69ba1a48db0c8273204896390e18b0e4aa52e19c9
last_synced_at: '2026-08-02T21:18:58Z'
defines:
- kind: module
  qualified_name: tests/test_incremental:__module__
  lines: 1-410
- kind: function
  qualified_name: tests/test_incremental:project
  lines: 19-32
  signature: 'def project(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_incremental:_initial_sync
  lines: 35-48
  signature: 'def _initial_sync(project: Path) -> None'
- kind: function
  qualified_name: tests/test_incremental:test_incremental_no_op_when_clean
  lines: 51-65
  signature: 'def test_incremental_no_op_when_clean(project: Path)'
- kind: function
  qualified_name: tests/test_incremental:test_incremental_resyncs_directly_changed_file
  lines: 68-86
  signature: 'def test_incremental_resyncs_directly_changed_file(project: Path)'
- kind: function
  qualified_name: tests/test_incremental:test_incremental_cascades_to_callers
  lines: 89-110
  signature: 'def test_incremental_cascades_to_callers(project: Path)'
- kind: function
  qualified_name: tests/test_incremental:test_incremental_respects_budget
  lines: 113-131
  signature: 'def test_incremental_respects_budget(project: Path)'
- kind: function
  qualified_name: tests/test_incremental:test_incremental_dispatched_via_cli
  lines: 134-164
  signature: 'def test_incremental_dispatched_via_cli(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_incremental:test_incremental_clean_via_cli
  lines: 167-179
  signature: 'def test_incremental_clean_via_cli(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_incremental:test_incremental_with_no_changes_yields_empty
  lines: 182-196
  signature: 'def test_incremental_with_no_changes_yields_empty(project: Path)'
- kind: function
  qualified_name: tests/test_incremental:test_incremental_handles_missing_triefact
  lines: 199-214
  signature: 'def test_incremental_handles_missing_triefact(project: Path)'
- kind: function
  qualified_name: tests/test_incremental:test_triefact_regenerated_only_for_affected_symbols_v01_limitation
  lines: 217-243
  signature: 'def test_triefact_regenerated_only_for_affected_symbols_v01_limitation(project: Path)'
- kind: function
  qualified_name: tests/test_incremental:test_run_incremental_invokes_progress_callback
  lines: 246-298
  signature: 'def test_run_incremental_invokes_progress_callback(project: Path)'
- kind: function
  qualified_name: tests/test_incremental:test_compute_incremental_worklist_empty_when_clean
  lines: 301-310
  signature: 'def test_compute_incremental_worklist_empty_when_clean(project: Path)'
- kind: function
  qualified_name: tests/test_incremental:test_compute_incremental_worklist_includes_cascade
  lines: 313-324
  signature: 'def test_compute_incremental_worklist_includes_cascade(project: Path)'
- kind: function
  qualified_name: tests/test_incremental:test_compute_incremental_worklist_is_read_only
  lines: 327-339
  signature: 'def test_compute_incremental_worklist_is_read_only(project: Path)'
- kind: function
  qualified_name: tests/test_incremental:test_compute_incremental_worklist_reports_orphans
  lines: 342-354
  signature: 'def test_compute_incremental_worklist_reports_orphans(project: Path)'
- kind: function
  qualified_name: tests/test_incremental:test_cli_plan_incremental_on_clean_tree_reports_noop
  lines: 357-373
  signature: 'def test_cli_plan_incremental_on_clean_tree_reports_noop( project: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_incremental:test_cli_plan_incremental_on_drift_lists_only_affected
  lines: 376-392
  signature: 'def test_cli_plan_incremental_on_drift_lists_only_affected( project: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_incremental:test_cli_plan_all_forces_full_bootstrap_view
  lines: 395-409
  signature: 'def test_cli_plan_all_forces_full_bootstrap_view(project: Path, monkeypatch: pytest.MonkeyPatch)'
incoming_refs: 0
outgoing_refs: 83
---
<!-- trie:section symbol=tests/test_incremental:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=417935d1c34a8cc18e5741c536af59d3c110c7a5cd5782a88324cb472f8ffe8f source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test-infrastructure -->
Tests for incremental synchronization functionality including cascade detection, budget limits, CLI routing, and worklist computation.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:project fingerprint=4e084006f178a9857caa68e57d59fa178c9ea3c6baac1bde21faa670adc80dea body_fp=efd3ecca7dd51d108b1299d74d4cf0d45be7c5d988880b3841825c2c5d1cf31d source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test-infrastructure -->
## `def project(tmp_path: Path) -> Path`

Pytest fixture that creates a temporary project directory with trie config, lib.py, and app.py for testing incremental sync functionality.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:_initial_sync fingerprint=19f828a287e74e17fb5815cd69f3830e5f4503b2184e00c8d3630d3a0be01605 body_fp=4d5e73be5199ab2dc70e8c75d7ab51456cad46ef33b703f203a1a0891279feb3 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test-infrastructure -->
## `def _initial_sync(project: Path) -> None`

Creates initial triefacts for lib.py and app.py using fake client responses.

- Uses FakeTrieClient with hardcoded "v1" output bodies for consistent test setup
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_no_op_when_clean fingerprint=88fcf5a07320e6e6a6898d8ec818ea05472e9c1fe359a9487c5d3555f6c3b0e2 body_fp=e9058c6203d39f754e4d431cb47db671c46393de5b07c1d9be5cddd03faca8bd source_ref=ec7f4e12c47a48489c3b7caabf845c630c79820a role=test -->
## `def test_incremental_no_op_when_clean(project: Path)`

Verifies incremental sync performs no work when all triefacts are up-to-date with source files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_resyncs_directly_changed_file fingerprint=b85bcd905c8ae3f2c0d017f024aa870a61d8a4833413467123ba8c15408719b8 body_fp=b9d1171cb9f8ecd4184a5c15019625e746db7172e53713277f34bca2e9931c0f source_ref=ec7f4e12c47a48489c3b7caabf845c630c79820a role=test -->
## `def test_incremental_resyncs_directly_changed_file(project: Path)`

Tests that `run_incremental` resyncs a file when its source content changes directly.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_cascades_to_callers fingerprint=1a95fb6afc0cf2e0f53dfc94ad563bf7b0d8f80435e30dc35159d35975602d6e body_fp=1f15454accbf366b7ca774463392df78a8b038cfe1525d40a3c302ef0a9516f7 source_ref=ec7f4e12c47a48489c3b7caabf845c630c79820a role=test -->
## `def test_incremental_cascades_to_callers(project: Path)`

Tests that modifying a file triggers cascaded regeneration of its dependents via incremental sync.

- Modifies lib.py after initial sync, verifies both lib.py and app.py are regenerated
- Validates cascade counts: 1 directly stale, 1 cascaded file
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_respects_budget fingerprint=04bdeeb4d89158444a5e2992e804a6d9579264e9f628bd719f996fbadaeb14d6 body_fp=ae136766f2a8a29a2b868e9718e27c83bdedd9fda455afb35c37687e7ccd8019 source_ref=ec7f4e12c47a48489c3b7caabf845c630c79820a role=test -->
## `def test_incremental_respects_budget(project: Path)`

Tests that run_incremental stops processing files when budget is exhausted.

- Sets up a project with stale files that would cascade
- Runs incremental sync with a tiny budget (0.0001 USD)
- Verifies some files sync but others are skipped due to budget constraints
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_dispatched_via_cli fingerprint=9166ca2cd40c05e603996f370d8ab49d5e23c8a147b3bfec4319387ef13cb0cb body_fp=c0cbb779aa2283da1ca261daf8bfc8a2d296d22f8e1c439c4fb9e09037bd55dd source_ref=61df5f6491a30ba7946712fc68a758ec64651250 role=test-infrastructure -->
## `def test_incremental_dispatched_via_cli(project: Path, monkeypatch: pytest.MonkeyPatch)`

Tests that `trie sync` CLI command routes through incremental sync and regenerates cascaded triefacts.

- Modifies source file to trigger incremental sync
- Mocks client to inject identifiable output content 
- Verifies both directly changed and cascaded files get regenerated with expected content
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_clean_via_cli fingerprint=1e718e0f925df852f5addd2cb488022f865c67a55380d521ca0b4965c38d3cf6 body_fp=62d17be03b80fe381bfff2434f9edfec5306e47c5a2b2292311d0f4576430595 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test-infrastructure -->
## `def test_incremental_clean_via_cli(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verifies that `trie sync` reports "coherent" when no files need updating.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_with_no_changes_yields_empty fingerprint=846cbe05b5e0e137dd212f80c02a87f499be74cb900023d6bab72d309145b92e body_fp=465e2bbdea04459d82f216ec2100fcf746cef6a16c6dc575190f101c20ec4428 source_ref=ec7f4e12c47a48489c3b7caabf845c630c79820a role=test -->
## `def test_incremental_with_no_changes_yields_empty(project: Path)`

Tests that incremental sync performs no operations when source files and triefacts are unchanged.

- Verifies `directly_stale_count` is 0
- Verifies `cascaded_count` is 0  
- Verifies `files_synced` is 0
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_handles_missing_triefact fingerprint=879a299f4eb31e0d2b869bea257c5b3b21131e22e4ad5bcc3fb53163484f21fb body_fp=d013ebfec36eda72bde026b7276c18dbd30da98bfa7fe18195f68ed585e58f76 source_ref=ec7f4e12c47a48489c3b7caabf845c630c79820a role=test -->
## `def test_incremental_handles_missing_triefact(project: Path)`

Test that verifies run_incremental handles projects with no existing triefacts by marking all files with public symbols as directly stale.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_triefact_regenerated_only_for_affected_symbols_v01_limitation fingerprint=0a9e2046dc131c3000bfe9fa03a00508cb967fa052fcf4e88d29b8fbdefcde50 body_fp=18f178790d3882eb2a6b7233964cadaf340be546e1cfac4f5bb3955801440f3a source_ref=ec7f4e12c47a48489c3b7caabf845c630c79820a role=test -->
## `def test_triefact_regenerated_only_for_affected_symbols_v01_limitation(project: Path)`

Documents that v0.1 incremental sync regenerates entire files rather than individual symbol sections.

- Tests that modifying one symbol causes the whole file's triefact to regenerate
- Verifies cascade behavior pulls in dependent files completely
- Confirms both lib.py and app.py triefacts contain their expected symbol sections after sync
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_run_incremental_invokes_progress_callback fingerprint=dc90828a0e0cffc2947784db90416e10b45b9a867ed7a3909f97fa62790db52d body_fp=68dbfecf329b9158a55e4fcf75e84973384dd1fb85557ce5374ff7a31d57e97c source_ref=ec7f4e12c47a48489c3b7caabf845c630c79820a role=test -->
## `def test_run_incremental_invokes_progress_callback(project: Path)`

Tests that `run_incremental` invokes progress callback methods during cascade-driven file synchronization.

- Creates a test project with two files where one imports from the other
- Modifies the imported file to trigger cascade synchronization 
- Uses a custom `Recorder` class to capture `on_start` and `on_done` callback invocations
- Verifies both directly affected and cascaded files stream through the progress callbacks
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_empty_when_clean fingerprint=cee10449e37638cbcb7584f41c7a16959603fbd74fc37e487f6c4431acef61cd body_fp=de81e8ec5fa064ecbce7b4dbd62ec703f8ef95926669eb686756ebd8dfe1d188 source_ref=ec7f4e12c47a48489c3b7caabf845c630c79820a role=test -->
## `def test_compute_incremental_worklist_empty_when_clean(project: Path)`

Verifies that `compute_incremental_worklist` returns empty lists when the project state is coherent with existing triefacts.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_includes_cascade fingerprint=19c15c1b29c078331a336f622e363b66959f8716f801ca6fe7080644d95a55c2 body_fp=de597c793524c7de7ff6d517ccc91e0ee2725c94e9a215c03054f664b64f8f03 source_ref=ec7f4e12c47a48489c3b7caabf845c630c79820a role=test -->
## `def test_compute_incremental_worklist_includes_cascade(project: Path)`

Tests that editing lib.py includes both lib.py (direct) and app.py (cascade) in the incremental worklist without LLM calls.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_is_read_only fingerprint=b52fe57285334a3855e29c7336c6bcbc9cc95bfb04a5a962c757fce08ac63a67 body_fp=385ba29584d4e934502fc5a488802bf24d5d07a5dacdb0692a1cd85b58b261d8 source_ref=ec7f4e12c47a48489c3b7caabf845c630c79820a role=test -->
## `def test_compute_incremental_worklist_is_read_only(project: Path)`

Verifies that `compute_incremental_worklist` does not modify triefact files when analyzing project changes.

- Captures triefact directory state before and after worklist computation
- Modifies source file to trigger stale detection
- Asserts triefact files remain unchanged after analysis
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_reports_orphans fingerprint=485e1297b791feffbf91b27b19055ae1493474b073d92853ea881e5c40bfad3c body_fp=c89c46578613d7f0f7f7abd49473523a51fec4bb56dc136e0556e592ba9b0f67 source_ref=ec7f4e12c47a48489c3b7caabf845c630c79820a role=test -->
## `def test_compute_incremental_worklist_reports_orphans(project: Path)`

Tests that `compute_incremental_worklist` detects orphaned triefacts when source files are deleted without removing them from disk.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_cli_plan_incremental_on_clean_tree_reports_noop fingerprint=4db390236c0ccf4b0a6740b4884f58820085d76652e2c109d278c69e7638a4d9 body_fp=96371d19715f411fed78ea1e46f6ccc3985afba1f16467da4172797127c2be6d source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test-infrastructure -->
## `def test_cli_plan_incremental_on_clean_tree_reports_noop( project: Path, monkeypatch: pytest.MonkeyPatch )`

Verifies that `trie plan` on a coherent established project reports no-op rather than full-bootstrap costs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_cli_plan_incremental_on_drift_lists_only_affected fingerprint=8af4a0d4196163c1948a984c33f635d05f98b0f37378f54703608740eb844080 body_fp=b6e976bb3401060d813c9f9a5a66bc657ccc50aeee4e9cdbdc8f9a8d3be415cd source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=test-infrastructure -->
## `def test_cli_plan_incremental_on_drift_lists_only_affected( project: Path, monkeypatch: pytest.MonkeyPatch )`

Tests that `trie plan` on an established project with file changes shows only incremental sync costs rather than full bootstrap costs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_cli_plan_all_forces_full_bootstrap_view fingerprint=4b275d51edf24baed79b45e27f8bf548affa56b8c67ab6f014a8b1f227e37ede body_fp=4022b0ae8c4636d5219d5cab1919c657d4dc485b5c9bdd8ce7ba527e13fb5cee source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e role=cli-interface -->
## `def test_cli_plan_all_forces_full_bootstrap_view(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verifies `trie plan --all` displays full bootstrap costs on established projects instead of incremental planning.
<!-- trie:end -->