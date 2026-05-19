---
trie_version: 0.1.1
source: tests/test_incremental.py
file_fingerprint: 29c8b8ef8ec9a5308f42db7ff2b4864b8f5d4fe5b9340b949d0f1d826d4d61f3
last_synced_at: '2026-05-19T10:38:12Z'
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
<!-- trie:section symbol=tests/test_incremental:FakeClient fingerprint=dd2ce5cbac0a663e75372124f682811a08d99ca2d34d2c8147be3fb275b44790 body_fp=0c2506996518995494b4a7de01bb236daf07f9119d037edfe92acf6aba8cff17 source_ref=cccb1012c6337a0910e535398f2041ab87ed321a -->
## `FakeClient(model_id: str = "anthropic/claude-sonnet-4-6", body: str = "## generated\n\nbody.", calls: int = 0)`

Stub LLM client that records call counts and returns fixed token counts and body text.

- `body`: returned verbatim as `GenerationResponse.text`
- `calls`: incremented on each `generate` invocation; inspect to assert LLM usage
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:FakeClient.generate fingerprint=e5b2ba5644c34f4b6310cb1886861a5822e5463319ee71045769565cc6e6d011 body_fp=d28c6bbc372e357ba5eafe24048d336804c0e7b2829d1edb0c33f83a10d061c4 source_ref=634fbeecb09b136114605fc4deac4b2a8647db8c -->
## `generate(self, _req: GenerationRequest) -> GenerationResponse`

Increment call counter and return a fixed `GenerationResponse` with preset token counts.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=9d067b772e73f67b1bb1b8cb6fc3a256c95035c670c6695fa426a36018030c0b source_ref=634fbeecb09b136114605fc4deac4b2a8647db8c -->
## `count_tokens(_req: GenerationRequest) -> int`

Return a fixed token count of 100 for any request.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:project fingerprint=4e084006f178a9857caa68e57d59fa178c9ea3c6baac1bde21faa670adc80dea body_fp=432e50a625de57bf7d8f2b709dbd537c324824c1c7c425638d4afbfd43da5681 source_ref=634fbeecb09b136114605fc4deac4b2a8647db8c -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal two-file Python project with a valid `trie.toml` config under `tmp_path`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_no_op_when_clean fingerprint=29350c3d31a93ea4618bd8d27979b13ff32b6c3315b6063f470262dc9e0e2997 body_fp=8dfeaa738270a7941fdcfced2dbfd6230cc9711fdd10338348911be246b1cb10 source_ref=634fbeecb09b136114605fc4deac4b2a8647db8c -->
## `test_incremental_no_op_when_clean(project: Path)`

Assert that `run_incremental` performs zero syncs and zero LLM calls when triefacts are already up to date.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_resyncs_directly_changed_file fingerprint=d78da037adbd34418a5bd6828ccd8e99f7cfd48180cf2d168bc39d3ffa737584 body_fp=17b9e5aa4f731304deba4ca7a6fd680186737e0a0eb0cd16dc6e62fbaa3bb824 source_ref=634fbeecb09b136114605fc4deac4b2a8647db8c -->
## `test_incremental_resyncs_directly_changed_file(project: Path)`

Assert that modifying a source file marks its triefact stale and triggers re-sync.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_cascades_to_callers fingerprint=3d4d1a6c94c9bdad3d047e5b4165a21d4500c811616151c63b2657be706a714a body_fp=cf6572cd6fb0fc9f5f7faed887bb351179538a2bfd05555c6fb157ace30b8bb5 source_ref=634fbeecb09b136114605fc4deac4b2a8647db8c -->
## `test_incremental_cascades_to_callers(project: Path)`

Assert that editing `lib.py` triggers cascade regeneration of `app.py` via the caller graph.

- `directly_stale_count` must equal 1; `cascaded_count` must equal 1.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_respects_budget fingerprint=5a5621ee7a68c0bc5e8dcc317152897211eea4fc4c1bbc28b26b2f75ec2d0a73 body_fp=5833f4d8769e4214163a3e86b3f3dd5230a6885356c508af1c2c6c050685f054 source_ref=634fbeecb09b136114605fc4deac4b2a8647db8c -->
## `test_incremental_respects_budget(project: Path)`

Assert that `run_incremental` skips files once the USD budget is exhausted.

- `budget_usd=0.0001`: tiny budget forces at least one file to be skipped.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_dispatched_via_cli fingerprint=a96b26f7d8714ef746368622e24dab2851385c5903972a766811da99fa3a7c81 body_fp=ae9f6c3639cc8b51793945990592b203f3e05f29ed797180c2213f64241b452c source_ref=cccb1012c6337a0910e535398f2041ab87ed321a -->
## `test_incremental_dispatched_via_cli(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify that `trie sync` CLI routes through `run_incremental` and regenerates both `lib.py` and `app.py` triefacts.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_clean_via_cli fingerprint=fbb297b35f04c76646bb85116f3ffa5e8b6df65ea0c56e661f2e11504ccc4c9b body_fp=6d516d3aa2ad54ba82718e89ba326aa00866f36da49298c2d07af5d537bb1cb6 source_ref=cccb1012c6337a0910e535398f2041ab87ed321a -->
## `test_incremental_clean_via_cli(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync` on an already-coherent tree exits 0 and reports "coherent".
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_with_no_changes_yields_empty fingerprint=8e45eeea8ec2dffaa97779e35aee757c4d2d1602b8547896940b24d88e0bfc80 body_fp=c771fb7318cbd33f2952936bd27597ad95cdccce5b5e1574edb34e77c29bc023 source_ref=634fbeecb09b136114605fc4deac4b2a8647db8c -->
## `test_incremental_with_no_changes_yields_empty(project: Path)`

Assert that `run_incremental` is a no-op when triefacts already exist and no source files have changed.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_handles_missing_triefact fingerprint=0e6264b2ea320f5d589407ae325cc58bfc5bc679de330cbc6e9aee9be1b43084 body_fp=980ed33e171e2cf399f991d3fad73a7d2714f3aba78c3351f0c0fb650c75a4ec source_ref=634fbeecb09b136114605fc4deac4b2a8647db8c -->
## `test_incremental_handles_missing_triefact(project: Path)`

Assert that `run_incremental` treats all files as directly stale when no triefacts exist, with zero cascade additions.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_triefact_regenerated_only_for_affected_symbols_v01_limitation fingerprint=fca40f95e94fbb526a9d921e5072f7ab01b4f633a3f0a2247c780f42a2a55c7e body_fp=c5d2b0ca0013747d223da527ea047866d740126754056a773721dc8efa771710 source_ref=634fbeecb09b136114605fc4deac4b2a8647db8c -->
## `test_triefact_regenerated_only_for_affected_symbols_v01_limitation(project: Path)`

Assert that v0.1 regenerates all symbols in an affected file, not just stale ones, and that cascade brings `app.py` in when `lib.py` changes.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_run_incremental_invokes_progress_callback fingerprint=c838ad91126bcd1ccca97818090a36de1d353cf655f16ea0db3fb242fb106ec6 body_fp=44d2e93c60c77a4fa0b88519a3a2f893856b9eabe2c6ee8ec9594dc476386aaf source_ref=634fbeecb09b136114605fc4deac4b2a8647db8c -->
## `test_run_incremental_invokes_progress_callback(project: Path)`

Verify that `run_incremental` streams `on_start` and `on_done` events for every affected file via the `progress` callback.

- `starts`: collects `(rel_path, idx, total)` tuples from `on_start` calls.
- `dones`: collects `rel_path` strings from `on_done` calls.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_empty_when_clean fingerprint=cee10449e37638cbcb7584f41c7a16959603fbd74fc37e487f6c4431acef61cd body_fp=fe701c2e4cac7c339a4b6fa9e11399d100ed00194ca6bb9806782ff453afac3e source_ref=634fbeecb09b136114605fc4deac4b2a8647db8c -->
## `test_compute_incremental_worklist_empty_when_clean(project: Path)`

Assert that a coherent triefact tree produces an empty worklist with no stale, cascaded, or orphan entries.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_includes_cascade fingerprint=19c15c1b29c078331a336f622e363b66959f8716f801ca6fe7080644d95a55c2 body_fp=65f729865f50f959243f905382d239c746de3db8d8ac3fcac893da44523e9074 source_ref=634fbeecb09b136114605fc4deac4b2a8647db8c -->
## `test_compute_incremental_worklist_includes_cascade(project: Path)`

Assert that editing `lib.py` places it in `directly_stale` and `app.py` in `cascaded_files` without performing any LLM calls.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_is_read_only fingerprint=b52fe57285334a3855e29c7336c6bcbc9cc95bfb04a5a962c757fce08ac63a67 body_fp=19dabff3b0e28e413ba89b78d534d707810f091a927ef0f8efcb81b5b2d529c6 source_ref=634fbeecb09b136114605fc4deac4b2a8647db8c -->
## `test_compute_incremental_worklist_is_read_only(project: Path)`

Assert that `compute_incremental_worklist` does not modify any triefact files on disk.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_reports_orphans fingerprint=485e1297b791feffbf91b27b19055ae1493474b073d92853ea881e5c40bfad3c body_fp=9c413ea55c6abd9af2beb2dac71ae1faac274fe41618e1bdf01fc93827d3f768 source_ref=634fbeecb09b136114605fc4deac4b2a8647db8c -->
## `test_compute_incremental_worklist_reports_orphans(project: Path)`

Assert that deleting a source file surfaces its triefact as an orphan in the worklist without deleting the file from disk.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_cli_plan_incremental_on_clean_tree_reports_noop fingerprint=0ed0b5ad398f177bd0e3b1f0cddbaa78e2ada916bb9a7cf860b3421ee8467d4b body_fp=5cd48f07676178912191edef25da4e41d8d9538b1c8c2e29cb9cfd7a74f0d99f source_ref=cccb1012c6337a0910e535398f2041ab87ed321a -->
## `test_cli_plan_incremental_on_clean_tree_reports_noop(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie plan` on a coherent, fully-synced project reports a no-op without showing full-bootstrap cost output.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_cli_plan_incremental_on_drift_lists_only_affected fingerprint=89ce01ff9a98093056c0f96d66c2dec5f9b6405b7d9b5881d14987ce61799c1b body_fp=3938783b982288f42a97e40783bf720ad2968bbe8c0c1a301f16edcc7ce7f3cb source_ref=cccb1012c6337a0910e535398f2041ab87ed321a -->
## `test_cli_plan_incremental_on_drift_lists_only_affected(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie plan` on an established project with drift shows incremental cost, not full-bootstrap cost.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_cli_plan_all_forces_full_bootstrap_view fingerprint=9a51a732f41159a3ecac00479af6014c0f5002971c2177545164581720fab29c body_fp=ebb3a57122fe73aa4e1d7b96a29fe59f22cbb410764b24c110575a47d796364d source_ref=cccb1012c6337a0910e535398f2041ab87ed321a -->
## `test_cli_plan_all_forces_full_bootstrap_view(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie plan --all` displays the full-bootstrap cost view, not the incremental plan.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:_initial_sync fingerprint=26e91fbfaf35286067bf8b736a60ae24749de7c391b5f08c3d758862a8c71c34 body_fp=5c966db4c9e7c01b996ce303f54e0632b4d57b2961a546b15f4408627f55140b source_ref=634fbeecb09b136114605fc4deac4b2a8647db8c -->
## `_initial_sync(project: Path) -> None`

Sync both `lib.py` and `app.py` into the project's triefacts directory using fixed v1 body text.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=727014eb36f176856223297b6fda5102561e335e8eaf0c5ca3f7dd8747152b19 source_ref=a0117e395aa062adbf5e2b983b5664f0d36835c4 -->
## `tests/test_incremental`

Integration tests for incremental sync, cascade, CLI routing, and worklist computation.

- `FakeClient`: stub LLM client tracking call count and returning fixed bodies
- `project`: pytest fixture creating a two-file Python project with `trie.toml`
- `_initial_sync`: seeds both `lib.py` and `app.py` triefacts before each test
<!-- trie:end -->