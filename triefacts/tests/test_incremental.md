---
trie_version: 0.1.5
source: tests/test_incremental.py
file_fingerprint: 73fcc52dfe76dd02f4f58619694ab3b389f654684b8097432f313d18b1cb764a
last_synced_at: '2026-05-28T01:39:44Z'
defines:
- kind: module
  qualified_name: tests/test_incremental:__module__
  lines: 1-402
- kind: class
  qualified_name: tests/test_incremental:FakeClient
  lines: 20-36
- kind: method
  qualified_name: tests/test_incremental:FakeClient.generate
  lines: 25-33
- kind: method
  qualified_name: tests/test_incremental:FakeClient.count_tokens
  lines: 35-36
- kind: function
  qualified_name: tests/test_incremental:project
  lines: 40-53
- kind: function
  qualified_name: tests/test_incremental:_initial_sync
  lines: 56-69
- kind: function
  qualified_name: tests/test_incremental:test_incremental_no_op_when_clean
  lines: 72-86
- kind: function
  qualified_name: tests/test_incremental:test_incremental_resyncs_directly_changed_file
  lines: 89-107
- kind: function
  qualified_name: tests/test_incremental:test_incremental_cascades_to_callers
  lines: 110-131
- kind: function
  qualified_name: tests/test_incremental:test_incremental_respects_budget
  lines: 134-152
- kind: function
  qualified_name: tests/test_incremental:test_incremental_dispatched_via_cli
  lines: 155-178
- kind: function
  qualified_name: tests/test_incremental:test_incremental_clean_via_cli
  lines: 181-191
- kind: function
  qualified_name: tests/test_incremental:test_incremental_with_no_changes_yields_empty
  lines: 194-208
- kind: function
  qualified_name: tests/test_incremental:test_incremental_handles_missing_triefact
  lines: 211-226
- kind: function
  qualified_name: tests/test_incremental:test_triefact_regenerated_only_for_affected_symbols_v01_limitation
  lines: 229-255
- kind: function
  qualified_name: tests/test_incremental:test_run_incremental_invokes_progress_callback
  lines: 258-300
- kind: function
  qualified_name: tests/test_incremental:test_compute_incremental_worklist_empty_when_clean
  lines: 303-312
- kind: function
  qualified_name: tests/test_incremental:test_compute_incremental_worklist_includes_cascade
  lines: 315-326
- kind: function
  qualified_name: tests/test_incremental:test_compute_incremental_worklist_is_read_only
  lines: 329-341
- kind: function
  qualified_name: tests/test_incremental:test_compute_incremental_worklist_reports_orphans
  lines: 344-356
- kind: function
  qualified_name: tests/test_incremental:test_cli_plan_incremental_on_clean_tree_reports_noop
  lines: 359-372
- kind: function
  qualified_name: tests/test_incremental:test_cli_plan_incremental_on_drift_lists_only_affected
  lines: 375-388
- kind: function
  qualified_name: tests/test_incremental:test_cli_plan_all_forces_full_bootstrap_view
  lines: 391-401
incoming_refs: 0
outgoing_refs: 56
---
<!-- trie:section symbol=tests/test_incremental:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=cbd0208bd1a5e20ff12cb76dba063241750c2fa827bde432ba6a4dc120ee3b98 source_ref=f81ee936e7bc6c01e0ab2b744f93acfa2cd45c96 -->
## `tests/test_incremental`

Integration tests for incremental sync, cascade worklist computation, and related CLI commands.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:FakeClient fingerprint=dd2ce5cbac0a663e75372124f682811a08d99ca2d34d2c8147be3fb275b44790 body_fp=eeb0a2e216c5dcb08a2dd7d214139e43a9332657ff47525afce8afc55ca430bb source_ref=f81ee936e7bc6c01e0ab2b744f93acfa2cd45c96 -->
## `FakeClient`

Stub LLM client for tests that records call counts and returns fixed `GenerationResponse` values.

- `body`: markdown text returned by every `generate` call.
- `calls`: incremented on each `generate` invocation; inspect to assert LLM usage.
- `count_tokens`: always returns `100`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:FakeClient.generate fingerprint=e5b2ba5644c34f4b6310cb1886861a5822e5463319ee71045769565cc6e6d011 body_fp=749006a3b630691ca9c8e4acb6f2dae52812809cbef469fe49cb00a469a4d1f5 source_ref=f81ee936e7bc6c01e0ab2b744f93acfa2cd45c96 -->
## `FakeClient.generate(self, _req: GenerationRequest) -> GenerationResponse`

Increment `FakeClient.calls` and return a fixed `GenerationResponse` using `self.body`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=5e0527e7f832a52c41aeb4c40f33e070049f0a913d35731eb156be433a163c38 source_ref=f81ee936e7bc6c01e0ab2b744f93acfa2cd45c96 -->
## `FakeClient.count_tokens(self, _req: GenerationRequest) -> int`

Always return 100 from `FakeClient`, ignoring the request.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:project fingerprint=4e084006f178a9857caa68e57d59fa178c9ea3c6baac1bde21faa670adc80dea body_fp=feb539da8c48d37dd340972b8e166c25fb5589f48c09473d5928b9556589ba44 source_ref=f81ee936e7bc6c01e0ab2b744f93acfa2cd45c96 -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal two-file project (`lib.py`, `app.py`) with a `trie.toml` config in a temporary directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:_initial_sync fingerprint=26e91fbfaf35286067bf8b736a60ae24749de7c391b5f08c3d758862a8c71c34 body_fp=a0278c92c8af75e26ffc5c007fd65e416c30c8eca07b8b894bdb085fb23e6fcb source_ref=f81ee936e7bc6c01e0ab2b744f93acfa2cd45c96 -->
## `_initial_sync(project: Path) -> None`

Seed `project` with v1 triefacts for `lib.py` and `app.py` using `FakeClient`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_no_op_when_clean fingerprint=29350c3d31a93ea4618bd8d27979b13ff32b6c3315b6063f470262dc9e0e2997 body_fp=3debe33dedd47caea43d9bcca4d0806221b4840481b386d4b552c69369b5aff8 source_ref=f81ee936e7bc6c01e0ab2b744f93acfa2cd45c96 -->
## `test_incremental_no_op_when_clean(project: Path)`

Assert that `run_incremental` performs zero LLM calls and syncs zero files when triefacts are already up to date.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_resyncs_directly_changed_file fingerprint=d78da037adbd34418a5bd6828ccd8e99f7cfd48180cf2d168bc39d3ffa737584 body_fp=8455f11bbd1f35f8aa6b166a04b8eeeabefe8e2ab1dc1b52b7976219e0b47d24 source_ref=f81ee936e7bc6c01e0ab2b744f93acfa2cd45c96 -->
## `test_incremental_resyncs_directly_changed_file(project: Path)`

Assert that modifying a source file marks its triefact stale and causes `run_incremental` to regenerate it.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_cascades_to_callers fingerprint=3d4d1a6c94c9bdad3d047e5b4165a21d4500c811616151c63b2657be706a714a body_fp=f7355927c7023b776bd577d246b172ae2c987f755809fba9a85aa41e9df2d7da source_ref=f81ee936e7bc6c01e0ab2b744f93acfa2cd45c96 -->
## `test_incremental_cascades_to_callers(project: Path)`

Assert that modifying `lib.py` causes both `lib.py` (direct) and `app.py` (cascade) to be regenerated by `run_incremental`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_respects_budget fingerprint=5a5621ee7a68c0bc5e8dcc317152897211eea4fc4c1bbc28b26b2f75ec2d0a73 body_fp=4da2f894dfa0d181d90ae7ab7ffda628889ce8039bba81ae2f449313c5730b81 source_ref=f81ee936e7bc6c01e0ab2b744f93acfa2cd45c96 -->
## `test_incremental_respects_budget(project: Path)`

Verify that `run_incremental` skips files once a tight USD budget is exhausted.

- `budget_usd=0.0001`: intentionally tiny to force at least one skip after the first file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_dispatched_via_cli fingerprint=a96b26f7d8714ef746368622e24dab2851385c5903972a766811da99fa3a7c81 body_fp=7037e04d356d21fb7d5dcb2ec28ab019eca34acc452ca12567ad07c14d33e3cb source_ref=f81ee936e7bc6c01e0ab2b744f93acfa2cd45c96 -->
## `test_incremental_dispatched_via_cli(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify `trie sync` CLI routes through `run_incremental` and regenerates stale triefacts via cascade.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_clean_via_cli fingerprint=fbb297b35f04c76646bb85116f3ffa5e8b6df65ea0c56e661f2e11504ccc4c9b body_fp=0e1b1dde46def8082f42449dd9883f24ec56c6d796e27e658000425e0e5c2020 source_ref=f81ee936e7bc6c01e0ab2b744f93acfa2cd45c96 -->
## `test_incremental_clean_via_cli(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync` on an already-coherent project exits cleanly and reports "coherent".
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_with_no_changes_yields_empty fingerprint=8e45eeea8ec2dffaa97779e35aee757c4d2d1602b8547896940b24d88e0bfc80 body_fp=6346ef078a148a84a0f088aafa09ca4206e7f4cc919a731dd12bb297b5980b42 source_ref=f81ee936e7bc6c01e0ab2b744f93acfa2cd45c96 -->
## `test_incremental_with_no_changes_yields_empty(project: Path)`

Assert that `run_incremental` produces zero stale, cascaded, or synced files when triefacts are already coherent.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_incremental_handles_missing_triefact fingerprint=0e6264b2ea320f5d589407ae325cc58bfc5bc679de330cbc6e9aee9be1b43084 body_fp=65e4167f358efd1584d145f4d87ca73866760efb7396599423c928c78884d9d1 source_ref=f81ee936e7bc6c01e0ab2b744f93acfa2cd45c96 -->
## `test_incremental_handles_missing_triefact(project: Path)`

Assert that `run_incremental` treats all in-scope files as directly stale when no triefacts exist, and cascade adds no additional count.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_triefact_regenerated_only_for_affected_symbols_v01_limitation fingerprint=fca40f95e94fbb526a9d921e5072f7ab01b4f633a3f0a2247c780f42a2a55c7e body_fp=9434172ef8c50c62c25e6aeb41827c9df7eccb3e48b450e38d616fc77ff1e6ed source_ref=f81ee936e7bc6c01e0ab2b744f93acfa2cd45c96 -->
## `test_triefact_regenerated_only_for_affected_symbols_v01_limitation(project: Path)`

Document that v0.1 regenerates all symbols in a file, not just stale sections, and verify cascade updates both `lib.md` and `app.md`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_run_incremental_invokes_progress_callback fingerprint=c838ad91126bcd1ccca97818090a36de1d353cf655f16ea0db3fb242fb106ec6 body_fp=3a6047e4221ade3c1328d0769c261a8cccc45dc77cb190f54f6c6406e32e1053 source_ref=f81ee936e7bc6c01e0ab2b744f93acfa2cd45c96 -->
## `test_run_incremental_invokes_progress_callback(project: Path)`

Assert that `run_incremental` calls `progress.on_start` and `on_done` for every file processed during a cascade-driven re-sync.
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
<!-- trie:section symbol=tests/test_incremental:test_cli_plan_incremental_on_clean_tree_reports_noop fingerprint=0ed0b5ad398f177bd0e3b1f0cddbaa78e2ada916bb9a7cf860b3421ee8467d4b body_fp=38a21366e208aaa82d1f61a50fe8173042c6e7a33045e387a26e28fe463ed58b source_ref=f81ee936e7bc6c01e0ab2b744f93acfa2cd45c96 -->
## `test_cli_plan_incremental_on_clean_tree_reports_noop(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie plan` on a coherent, fully-synced project reports no-op rather than a full-bootstrap cost.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_cli_plan_incremental_on_drift_lists_only_affected fingerprint=89ce01ff9a98093056c0f96d66c2dec5f9b6405b7d9b5881d14987ce61799c1b body_fp=6043bc8c7fc5e1e16790df014fa5fe4c73b8f6a363d1ba203d3c8fe3a80c4e3a source_ref=f81ee936e7bc6c01e0ab2b744f93acfa2cd45c96 -->
## `test_cli_plan_incremental_on_drift_lists_only_affected(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie plan` on a drifted established project outputs incremental cost, not full-bootstrap cost.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_incremental:test_cli_plan_all_forces_full_bootstrap_view fingerprint=9a51a732f41159a3ecac00479af6014c0f5002971c2177545164581720fab29c body_fp=4b3cf35803072a258ea5cb8f476ef170537e0dbb204e15c9958b27ffeb9622df source_ref=f81ee936e7bc6c01e0ab2b744f93acfa2cd45c96 -->
## `test_cli_plan_all_forces_full_bootstrap_view(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie plan --all` outputs the full-bootstrap cost view, not the incremental plan.
<!-- trie:end -->