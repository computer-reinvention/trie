---
trie_version: 0.1.5
source: tests/test_incremental.py
file_fingerprint: 8a62f0c285b7cf16d1f3454e2c33a8a96493c90320181c04e3e3749cd1ff2819
last_synced_at: '2026-05-28T15:04:29Z'
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
<!-- trie:section symbol=tests/test_incremental:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=cbd0208bd1a5e20ff12cb76dba063241750c2fa827bde432ba6a4dc120ee3b98 source_ref=f81ee936e7bc6c01e0ab2b744f93acfa2cd45c96 -->
## `tests/test_incremental`

Integration tests for incremental sync, cascade worklist computation, and related CLI commands.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:project fingerprint=4e084006f178a9857caa68e57d59fa178c9ea3c6baac1bde21faa670adc80dea body_fp=feb539da8c48d37dd340972b8e166c25fb5589f48c09473d5928b9556589ba44 source_ref=f81ee936e7bc6c01e0ab2b744f93acfa2cd45c96 -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal two-file project (`lib.py`, `app.py`) with a `trie.toml` config in a temporary directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:_initial_sync fingerprint=19f828a287e74e17fb5815cd69f3830e5f4503b2184e00c8d3630d3a0be01605 body_fp=a0278c92c8af75e26ffc5c007fd65e416c30c8eca07b8b894bdb085fb23e6fcb source_ref=17efc5900983b25f09743e7d3cf11646ba6932b5 -->
## `_initial_sync(project: Path) -> None`

Seed `project` with v1 triefacts for `lib.py` and `app.py` using `FakeClient`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_no_op_when_clean fingerprint=88fcf5a07320e6e6a6898d8ec818ea05472e9c1fe359a9487c5d3555f6c3b0e2 body_fp=3debe33dedd47caea43d9bcca4d0806221b4840481b386d4b552c69369b5aff8 source_ref=17efc5900983b25f09743e7d3cf11646ba6932b5 -->
## `test_incremental_no_op_when_clean(project: Path)`

Assert that `run_incremental` performs zero LLM calls and syncs zero files when triefacts are already up to date.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_resyncs_directly_changed_file fingerprint=b85bcd905c8ae3f2c0d017f024aa870a61d8a4833413467123ba8c15408719b8 body_fp=8455f11bbd1f35f8aa6b166a04b8eeeabefe8e2ab1dc1b52b7976219e0b47d24 source_ref=17efc5900983b25f09743e7d3cf11646ba6932b5 -->
## `test_incremental_resyncs_directly_changed_file(project: Path)`

Assert that modifying a source file marks its triefact stale and causes `run_incremental` to regenerate it.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_cascades_to_callers fingerprint=1a95fb6afc0cf2e0f53dfc94ad563bf7b0d8f80435e30dc35159d35975602d6e body_fp=f7355927c7023b776bd577d246b172ae2c987f755809fba9a85aa41e9df2d7da source_ref=17efc5900983b25f09743e7d3cf11646ba6932b5 -->
## `test_incremental_cascades_to_callers(project: Path)`

Assert that modifying `lib.py` causes both `lib.py` (direct) and `app.py` (cascade) to be regenerated by `run_incremental`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_respects_budget fingerprint=04bdeeb4d89158444a5e2992e804a6d9579264e9f628bd719f996fbadaeb14d6 body_fp=4da2f894dfa0d181d90ae7ab7ffda628889ce8039bba81ae2f449313c5730b81 source_ref=17efc5900983b25f09743e7d3cf11646ba6932b5 -->
## `test_incremental_respects_budget(project: Path)`

Verify that `run_incremental` skips files once a tight USD budget is exhausted.

- `budget_usd=0.0001`: intentionally tiny to force at least one skip after the first file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_dispatched_via_cli fingerprint=4a90404380aa80415fd81dced526cdff5bf9d212639a159913dc18ea05ba6992 body_fp=7037e04d356d21fb7d5dcb2ec28ab019eca34acc452ca12567ad07c14d33e3cb source_ref=17efc5900983b25f09743e7d3cf11646ba6932b5 -->
## `test_incremental_dispatched_via_cli(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify `trie sync` CLI routes through `run_incremental` and regenerates stale triefacts via cascade.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_clean_via_cli fingerprint=1e718e0f925df852f5addd2cb488022f865c67a55380d521ca0b4965c38d3cf6 body_fp=0e1b1dde46def8082f42449dd9883f24ec56c6d796e27e658000425e0e5c2020 source_ref=17efc5900983b25f09743e7d3cf11646ba6932b5 -->
## `test_incremental_clean_via_cli(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync` on an already-coherent project exits cleanly and reports "coherent".
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_with_no_changes_yields_empty fingerprint=846cbe05b5e0e137dd212f80c02a87f499be74cb900023d6bab72d309145b92e body_fp=6346ef078a148a84a0f088aafa09ca4206e7f4cc919a731dd12bb297b5980b42 source_ref=17efc5900983b25f09743e7d3cf11646ba6932b5 -->
## `test_incremental_with_no_changes_yields_empty(project: Path)`

Assert that `run_incremental` produces zero stale, cascaded, or synced files when triefacts are already coherent.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_handles_missing_triefact fingerprint=879a299f4eb31e0d2b869bea257c5b3b21131e22e4ad5bcc3fb53163484f21fb body_fp=65e4167f358efd1584d145f4d87ca73866760efb7396599423c928c78884d9d1 source_ref=17efc5900983b25f09743e7d3cf11646ba6932b5 -->
## `test_incremental_handles_missing_triefact(project: Path)`

Assert that `run_incremental` treats all in-scope files as directly stale when no triefacts exist, and cascade adds no additional count.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_triefact_regenerated_only_for_affected_symbols_v01_limitation fingerprint=0a9e2046dc131c3000bfe9fa03a00508cb967fa052fcf4e88d29b8fbdefcde50 body_fp=9434172ef8c50c62c25e6aeb41827c9df7eccb3e48b450e38d616fc77ff1e6ed source_ref=17efc5900983b25f09743e7d3cf11646ba6932b5 -->
## `test_triefact_regenerated_only_for_affected_symbols_v01_limitation(project: Path)`

Document that v0.1 regenerates all symbols in a file, not just stale sections, and verify cascade updates both `lib.md` and `app.md`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_run_incremental_invokes_progress_callback fingerprint=412274a40568b9a4b7ab6ef350db630f15eb17287688711580021655266352ed body_fp=a8e6a6d5e0aa4a59c27fabfd8850ed9721295a5f36484a60e86d6226e881b512 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e -->
## `test_run_incremental_invokes_progress_callback(project: Path)`

Verify that `run_incremental` fires `on_start` and `on_done` progress callbacks for each cascade-affected file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_empty_when_clean fingerprint=cee10449e37638cbcb7584f41c7a16959603fbd74fc37e487f6c4431acef61cd body_fp=ef8aa9806a740b314f429a71f7e602b0ed0c2edb29165462401fa0300552d2b5 source_ref=f81ee936e7bc6c01e0ab2b744f93acfa2cd45c96 -->
## `test_compute_incremental_worklist_empty_when_clean(project: Path)`

Assert that `compute_incremental_worklist` returns an empty worklist when all triefacts are up to date.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_includes_cascade fingerprint=19c15c1b29c078331a336f622e363b66959f8716f801ca6fe7080644d95a55c2 body_fp=aca2a23fb7ab09ac4f6928ca73ec055f7b724958409e376f247d35722e317c03 source_ref=f81ee936e7bc6c01e0ab2b744f93acfa2cd45c96 -->
## `test_compute_incremental_worklist_includes_cascade(project: Path)`

Assert that modifying `lib.py` places it in `directly_stale` and its caller `app.py` in `cascaded_files` without invoking any LLM or mutating triefacts.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_is_read_only fingerprint=b52fe57285334a3855e29c7336c6bcbc9cc95bfb04a5a962c757fce08ac63a67 body_fp=f0adb6f316233f284336e2e1bb2245a3810dfcf5d30429ee257e44895c44f3fd source_ref=f81ee936e7bc6c01e0ab2b744f93acfa2cd45c96 -->
## `test_compute_incremental_worklist_is_read_only(project: Path)`

Assert that `compute_incremental_worklist` leaves all triefact files unchanged after drift is introduced.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_reports_orphans fingerprint=485e1297b791feffbf91b27b19055ae1493474b073d92853ea881e5c40bfad3c body_fp=3c42ab0d1fd3287dcd0f690bf0a9aed232e815e835f4b5a55daad52d5b93600c source_ref=f81ee936e7bc6c01e0ab2b744f93acfa2cd45c96 -->
## `test_compute_incremental_worklist_reports_orphans(project: Path)`

Assert that deleting a source file causes its triefact to appear in `worklist.orphan_triefacts` without being deleted from disk.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_cli_plan_incremental_on_clean_tree_reports_noop fingerprint=4db390236c0ccf4b0a6740b4884f58820085d76652e2c109d278c69e7638a4d9 body_fp=9f3f0cff487a76e7bc31cd07b9d02dfa1e8325b498e023a66c78c2319a011da5 source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e -->
## `test_cli_plan_incremental_on_clean_tree_reports_noop(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie plan` on a coherent, fully-synced project outputs "coherent" or "no-op" and never the full-bootstrap cost header.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_cli_plan_incremental_on_drift_lists_only_affected fingerprint=8af4a0d4196163c1948a984c33f635d05f98b0f37378f54703608740eb844080 body_fp=6043bc8c7fc5e1e16790df014fa5fe4c73b8f6a363d1ba203d3c8fe3a80c4e3a source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e -->
## `test_cli_plan_incremental_on_drift_lists_only_affected(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie plan` on a drifted established project outputs incremental cost, not full-bootstrap cost.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_cli_plan_all_forces_full_bootstrap_view fingerprint=4b275d51edf24baed79b45e27f8bf548affa56b8c67ab6f014a8b1f227e37ede body_fp=ebb3a57122fe73aa4e1d7b96a29fe59f22cbb410764b24c110575a47d796364d source_ref=a2b7bc3250cdda5be24221661f9fbc536677e55e -->
## `test_cli_plan_all_forces_full_bootstrap_view(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie plan --all` displays the full-bootstrap cost view, not the incremental plan.
<!-- trie:end -->