---
trie_version: 0.1.0
source: tests/test_incremental.py
file_fingerprint: ef5b6fc086e0ace26a386b6560803d21d876401c23cd23f8ea530347a8733e57
last_synced_at: '2026-05-14T17:16:34Z'
defines:
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
  lines: 181-188
- kind: function
  qualified_name: tests/test_incremental:test_incremental_with_no_changes_yields_empty
  lines: 191-205
- kind: function
  qualified_name: tests/test_incremental:test_incremental_handles_missing_triefact
  lines: 208-223
- kind: function
  qualified_name: tests/test_incremental:test_triefact_regenerated_only_for_affected_symbols_v01_limitation
  lines: 226-252
- kind: function
  qualified_name: tests/test_incremental:test_run_incremental_invokes_progress_callback
  lines: 255-297
- kind: function
  qualified_name: tests/test_incremental:test_compute_incremental_worklist_empty_when_clean
  lines: 300-309
- kind: function
  qualified_name: tests/test_incremental:test_compute_incremental_worklist_includes_cascade
  lines: 312-323
- kind: function
  qualified_name: tests/test_incremental:test_compute_incremental_worklist_is_read_only
  lines: 326-338
- kind: function
  qualified_name: tests/test_incremental:test_compute_incremental_worklist_reports_orphans
  lines: 341-353
- kind: function
  qualified_name: tests/test_incremental:test_cli_plan_incremental_on_clean_tree_reports_noop
  lines: 356-369
- kind: function
  qualified_name: tests/test_incremental:test_cli_plan_incremental_on_drift_lists_only_affected
  lines: 372-385
- kind: function
  qualified_name: tests/test_incremental:test_cli_plan_all_forces_full_bootstrap_view
  lines: 388-398
incoming_refs: 0
outgoing_refs: 51
---
<!-- trie:section symbol=tests/test_incremental:FakeClient fingerprint=dd2ce5cbac0a663e75372124f682811a08d99ca2d34d2c8147be3fb275b44790 body_fp=b681423d1a59dfe226ce5fbea054a27d577b08f45e6df4e1d44819e2407dd836 -->
## `FakeClient(model_id="anthropic/claude-sonnet-4-6", body="## generated\n\nbody.", calls=0)`

Stub LLM client that returns a fixed response body and counts `generate` invocations.

- `body`: literal text returned as `GenerationResponse.text` on every call.
- `calls`: incremented each time `generate` is invoked; inspect to assert call counts.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:FakeClient.generate fingerprint=e5b2ba5644c34f4b6310cb1886861a5822e5463319ee71045769565cc6e6d011 body_fp=ab50d7ff8ffc0a1b77cfa3ca9f11f74845aa4d71ccd6154d815af4fe7b4438d9 -->
## `generate(self, _req: GenerationRequest) -> GenerationResponse`

Increment the call counter and return a fixed `GenerationResponse` with preset token counts.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=4943a054b4305ed8d78ecd405a3e69181c6f078c7039059b20c474a5eca001f1 -->
## `count_tokens(_req: GenerationRequest) -> int`

Return a fixed token count of 100 for any generation request.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:project fingerprint=4e084006f178a9857caa68e57d59fa178c9ea3c6baac1bde21faa670adc80dea body_fp=168e8182c3b79c51b771775d0874b624ec50256c778100be90072ea2d96fe0af -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal two-file Python project with a `trie.toml` config under `tmp_path`.

- Returns `tmp_path` containing `trie.toml`, `lib.py`, and `app.py`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_no_op_when_clean fingerprint=29350c3d31a93ea4618bd8d27979b13ff32b6c3315b6063f470262dc9e0e2997 body_fp=f32029c9ca721b28e600e517fbc11edda093b5884fbc5fd7c9d6ca1e6cfa52fb -->
## `test_incremental_no_op_when_clean(project: Path)`

Assert that `run_incremental` skips all files and makes no LLM calls when triefacts are already up to date.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_resyncs_directly_changed_file fingerprint=d78da037adbd34418a5bd6828ccd8e99f7cfd48180cf2d168bc39d3ffa737584 body_fp=8455f11bbd1f35f8aa6b166a04b8eeeabefe8e2ab1dc1b52b7976219e0b47d24 -->
## `test_incremental_resyncs_directly_changed_file(project: Path)`

Assert that modifying a source file marks its triefact stale and causes `run_incremental` to regenerate it.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_cascades_to_callers fingerprint=3d4d1a6c94c9bdad3d047e5b4165a21d4500c811616151c63b2657be706a714a body_fp=7eff6054a6e9da2eaabc925157bbc8fecf681f40a46664ad1bd11de289bde79d -->
## `test_incremental_cascades_to_callers(project: Path)`

Assert that modifying `lib.py` causes `run_incremental` to regenerate both `lib.py` directly and `app.py` via cascade.

- `directly_stale_count`: expected 1 (only `lib.py` changed on disk).
- `cascaded_count`: expected 1 (`app.py` pulled in because it imports `lib.helper`).
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_respects_budget fingerprint=5a5621ee7a68c0bc5e8dcc317152897211eea4fc4c1bbc28b26b2f75ec2d0a73 body_fp=30559917f61c664a8d4d0c7a7aedd57c5d94d0ff44fbf85b8ca06db8ab6f8e47 -->
## `test_incremental_respects_budget(project: Path)`

Verify that `run_incremental` stops syncing files once a tight USD budget is exhausted.

- `budget_usd=0.0001`: intentionally tiny so at least one file is skipped.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_dispatched_via_cli fingerprint=76f88c12f569dd525ddcf02390e59164963d312a9c3a52ae5f0e880b916c8103 body_fp=4fd4587193fd46c96298615f7e1837a851a8d3baadba0514710cea69c8a93a0e -->
## `test_incremental_dispatched_via_cli(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify that `trie sync` CLI routes through `run_incremental` and regenerates triefacts for both directly-changed and cascaded files.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_clean_via_cli fingerprint=ec121dfcf3dfa2e20573a1207e05298b58a48f6463f2a003536e3e55f5262ac7 body_fp=00f042688b23434b4a128e7c1fbe371dbdd99a95ce5a8dc349fb6e41117ec2cd -->
## `test_incremental_clean_via_cli(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify that `trie sync` on an already-coherent project reports a clean/coherent status via CLI output.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_with_no_changes_yields_empty fingerprint=8e45eeea8ec2dffaa97779e35aee757c4d2d1602b8547896940b24d88e0bfc80 body_fp=949e43a6926517bd81e83b828ad3bc249c6b077a38d8ae438144529516fb1c35 -->
## `test_incremental_with_no_changes_yields_empty(project: Path)`

Assert that `run_incremental` is a no-op when all triefacts are already current.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_handles_missing_triefact fingerprint=0e6264b2ea320f5d589407ae325cc58bfc5bc679de330cbc6e9aee9be1b43084 body_fp=4090c368910a891a651170fca067f69fc49841dcb545abb0763aaef1ac0b44b1 -->
## `test_incremental_handles_missing_triefact(project: Path)`

Assert that `run_incremental` treats all files as directly stale when no triefacts exist, with zero cascade inflation.

- `directly_stale_count` must equal 2; cascade must not double-count already-stale files.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_triefact_regenerated_only_for_affected_symbols_v01_limitation fingerprint=fca40f95e94fbb526a9d921e5072f7ab01b4f633a3f0a2247c780f42a2a55c7e body_fp=452bf0e43b90a393c108f2743bb6a07c62178fa9d912c1bed1e20c748f14c330 -->
## `test_triefact_regenerated_only_for_affected_symbols_v01_limitation(project: Path)`

Assert that v0.1 regenerates all symbols in a file rather than only stale sections, with cascade pulling `app.py` in when `lib.py` changes.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_run_incremental_invokes_progress_callback fingerprint=c838ad91126bcd1ccca97818090a36de1d353cf655f16ea0db3fb242fb106ec6 body_fp=e4c929c303e9cf74f5313a4048aa70cdaa55f62c6157f15117d34c5ef4d8b46f -->
## `test_run_incremental_invokes_progress_callback(project: Path)`

Verify that `run_incremental` fires `on_start` and `on_done` callbacks for every cascade-affected file.

- `project`: tmp directory fixture with `lib.py` and `app.py` pre-bootstrapped before mutation.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_empty_when_clean fingerprint=cee10449e37638cbcb7584f41c7a16959603fbd74fc37e487f6c4431acef61cd body_fp=0d71e1c8d9dfdd0550f6e72c4078ead923d93918a327c9d1594d2d66b0e62207 -->
## `test_compute_incremental_worklist_empty_when_clean(project: Path)`

Assert that a fully synced, unmodified project produces an empty incremental worklist.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_includes_cascade fingerprint=19c15c1b29c078331a336f622e363b66959f8716f801ca6fe7080644d95a55c2 body_fp=02e59515400ee3d4bac731f853ce9c4ec2861eafc7fa4e9ea9f5ead022a8b612 -->
## `test_compute_incremental_worklist_includes_cascade(project: Path)`

Assert that editing `lib.py` places it in `directly_stale` and `app.py` in `cascaded_files` without invoking any LLM.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_is_read_only fingerprint=b52fe57285334a3855e29c7336c6bcbc9cc95bfb04a5a962c757fce08ac63a67 body_fp=8c2f8398f4889e1bb4172925ced64dadc8b04eee53fd4cbaf4061328660ba15b -->
## `test_compute_incremental_worklist_is_read_only(project: Path)`

Assert that `compute_incremental_worklist` leaves all triefact files unmodified on disk.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_reports_orphans fingerprint=485e1297b791feffbf91b27b19055ae1493474b073d92853ea881e5c40bfad3c body_fp=8074cb1e07a69f1e803ae15e05c4a934326241353a8b33ab7ebe920beb357f24 -->
## `test_compute_incremental_worklist_reports_orphans(project: Path)`

Assert that deleting a source file causes its triefact to appear in the worklist's `orphan_triefacts` without being deleted from disk.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_cli_plan_incremental_on_clean_tree_reports_noop fingerprint=c5f369e80b62fb9b6394580e4fd6528bf01fd7fde46152fc5cff2b4e9addb870 body_fp=8402558e3d0e8d56e071d5977847844571ba5dedf14fe31e17081b18b5fa100f -->
## `test_cli_plan_incremental_on_clean_tree_reports_noop(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie plan` on a coherent, fully-synced project reports no-op without showing a full-bootstrap cost header.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_cli_plan_incremental_on_drift_lists_only_affected fingerprint=94665fe3e49bf70c830e7f50939f03dc26b64afeec6ae732c2548a49c5968a9b body_fp=4924c7115769603db83d7a6a23a750d363439d2004dd327c503dd382d062d7b3 -->
## `test_cli_plan_incremental_on_drift_lists_only_affected(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie plan` on a project with drift shows incremental cost output, not full-bootstrap cost.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_cli_plan_all_forces_full_bootstrap_view fingerprint=fd9b83493d1cf2bb3617946a5a9511d4a89d3fef2f3edcb6c60253ce01b034ed body_fp=c32c7fa67cf7fb6429a2d6591cc6339997681cf035388355713050c8b97dcea4 -->
## `test_cli_plan_all_forces_full_bootstrap_view(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie plan --all` on an established project renders the full-bootstrap cost view, not the incremental plan.
<!-- trie:end -->