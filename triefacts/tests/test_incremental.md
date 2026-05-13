---
trie_version: 0.1.0
source: tests/test_incremental.py
file_fingerprint: ef5b6fc086e0ace26a386b6560803d21d876401c23cd23f8ea530347a8733e57
last_synced_at: '2026-05-12T18:19:14Z'
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
<!-- trie:section symbol=tests/test_incremental:FakeClient fingerprint=dd2ce5cbac0a663e75372124f682811a08d99ca2d34d2c8147be3fb275b44790 body_fp=378192a30b81cfa26c8c40b4fa9a44e019943567b6bb4c6a935c5d0e5d928b80 -->
## `FakeClient(model_id: str = "anthropic/claude-sonnet-4-6", body: str = "## generated\n\nbody.", calls: int = 0)`

Stub LLM client that returns a fixed response body and tracks call count.

- `body`: literal text returned as `GenerationResponse.text` on every `generate` call.
- `calls`: incremented on each `generate` invocation; inspect to assert LLM usage.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:FakeClient.generate fingerprint=e5b2ba5644c34f4b6310cb1886861a5822e5463319ee71045769565cc6e6d011 body_fp=a171fd062c6c098726dc98cf0a3f53d774deaca67308afd1fa71dfba56eac47c -->
## `generate(self, _req: GenerationRequest) -> GenerationResponse`

Increment call counter and return a fixed `GenerationResponse` with preset token counts and `self.body` as text.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=4943a054b4305ed8d78ecd405a3e69181c6f078c7039059b20c474a5eca001f1 -->
## `count_tokens(_req: GenerationRequest) -> int`

Return a fixed token count of 100 for any generation request.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:project fingerprint=4e084006f178a9857caa68e57d59fa178c9ea3c6baac1bde21faa670adc80dea body_fp=70c22f8b03dff93fa3f49e94cf98a2a9fd5b62843bf49beba4a6ee894b68d52b -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal two-file Python project with a `trie.toml` config under `tmp_path`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_no_op_when_clean fingerprint=29350c3d31a93ea4618bd8d27979b13ff32b6c3315b6063f470262dc9e0e2997 body_fp=8b516c1d6d0ba4c07afb71bc2468e8c38bc16cee294b691d3fe257b8d360f766 -->
## `test_incremental_no_op_when_clean(project: Path)`

Assert that `run_incremental` performs zero syncs and zero LLM calls when all triefacts are up to date.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_resyncs_directly_changed_file fingerprint=d78da037adbd34418a5bd6828ccd8e99f7cfd48180cf2d168bc39d3ffa737584 body_fp=8455f11bbd1f35f8aa6b166a04b8eeeabefe8e2ab1dc1b52b7976219e0b47d24 -->
## `test_incremental_resyncs_directly_changed_file(project: Path)`

Assert that modifying a source file marks its triefact stale and causes `run_incremental` to regenerate it.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_cascades_to_callers fingerprint=3d4d1a6c94c9bdad3d047e5b4165a21d4500c811616151c63b2657be706a714a body_fp=16cf77ffb273ffc8ef0fc6b6a4cb59b8dc49c31de1a65eb0b146f924a4e61449 -->
## `test_incremental_cascades_to_callers(project: Path)`

Assert that editing `lib.py` triggers cascade re-sync of `app.py` and correct stale/cascaded counts.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_respects_budget fingerprint=5a5621ee7a68c0bc5e8dcc317152897211eea4fc4c1bbc28b26b2f75ec2d0a73 body_fp=903ce210627f73b2e40a443636a0cba68efe5ca67f4bb52d218fadb90c54e2fa -->
## `test_incremental_respects_budget(project: Path)`

Verify that `run_incremental` skips files when the USD budget is exhausted mid-run.

- `budget_usd=0.0001`: intentionally tiny to force at least one skip after the first file.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_dispatched_via_cli fingerprint=76f88c12f569dd525ddcf02390e59164963d312a9c3a52ae5f0e880b916c8103 body_fp=ae9f6c3639cc8b51793945990592b203f3e05f29ed797180c2213f64241b452c -->
## `test_incremental_dispatched_via_cli(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify that `trie sync` CLI routes through `run_incremental` and regenerates both `lib.py` and `app.py` triefacts.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_clean_via_cli fingerprint=ec121dfcf3dfa2e20573a1207e05298b58a48f6463f2a003536e3e55f5262ac7 body_fp=6d53f0b5e55db8b67704f707b31a11f2a33238328ef022293d2aa88c283a7ffe -->
## `test_incremental_clean_via_cli(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify that `trie sync` on an already-coherent project exits successfully and reports "coherent".
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_with_no_changes_yields_empty fingerprint=8e45eeea8ec2dffaa97779e35aee757c4d2d1602b8547896940b24d88e0bfc80 body_fp=3fe9700aa030e636db0a2f7090f2b3b65b6deb46ae2c611aad3e9117261d4994 -->
## `test_incremental_with_no_changes_yields_empty(project: Path)`

Assert that `run_incremental` is a no-op when all triefacts are already up-to-date.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_handles_missing_triefact fingerprint=0e6264b2ea320f5d589407ae325cc58bfc5bc679de330cbc6e9aee9be1b43084 body_fp=c479ac52c458968d2cb55085192f5dc388642ebf24ce017784f0053ade872d59 -->
## `test_incremental_handles_missing_triefact(project: Path)`

Assert that with no pre-existing triefacts, all files with public symbols are directly stale and cascade count adds none beyond them.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_triefact_regenerated_only_for_affected_symbols_v01_limitation fingerprint=fca40f95e94fbb526a9d921e5072f7ab01b4f633a3f0a2247c780f42a2a55c7e body_fp=2e1f49fd2ecac94991c8ec1026727c5c0a817d82dcbbb22928cafb723747fb48 -->
## `test_triefact_regenerated_only_for_affected_symbols_v01_limitation(project: Path)`

Assert that v0.1 regenerates all symbols in a file, not just stale ones, and that cascade pulls `app.py` in when only `lib.py` changes.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_run_incremental_invokes_progress_callback fingerprint=c838ad91126bcd1ccca97818090a36de1d353cf655f16ea0db3fb242fb106ec6 body_fp=8aab10207f4ba7aaf24da4faa165b86f9716c4d4375390d1bfde5af7180e11f6 -->
## `test_run_incremental_invokes_progress_callback(project: Path)`

Verify that `run_incremental` streams `on_start` and `on_done` events for every affected file via the `progress` callback.

- `starts`: collects `(rel_path, idx, total)` tuples from `on_start`.
- `dones`: collects `rel_path` strings from `on_done`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_empty_when_clean fingerprint=cee10449e37638cbcb7584f41c7a16959603fbd74fc37e487f6c4431acef61cd body_fp=0c1a46ee567f526f2d9d0f108bf8d5f9223904375698dd30f182ab5491a61b62 -->
## `test_compute_incremental_worklist_empty_when_clean(project: Path)`

Assert that a fully synced, unmodified project yields an empty incremental worklist.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_includes_cascade fingerprint=19c15c1b29c078331a336f622e363b66959f8716f801ca6fe7080644d95a55c2 body_fp=65f729865f50f959243f905382d239c746de3db8d8ac3fcac893da44523e9074 -->
## `test_compute_incremental_worklist_includes_cascade(project: Path)`

Assert that editing `lib.py` places it in `directly_stale` and `app.py` in `cascaded_files` without performing any LLM calls.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_is_read_only fingerprint=b52fe57285334a3855e29c7336c6bcbc9cc95bfb04a5a962c757fce08ac63a67 body_fp=8c2f8398f4889e1bb4172925ced64dadc8b04eee53fd4cbaf4061328660ba15b -->
## `test_compute_incremental_worklist_is_read_only(project: Path)`

Assert that `compute_incremental_worklist` leaves all triefact files unmodified on disk.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_reports_orphans fingerprint=485e1297b791feffbf91b27b19055ae1493474b073d92853ea881e5c40bfad3c body_fp=3c42ab0d1fd3287dcd0f690bf0a9aed232e815e835f4b5a55daad52d5b93600c -->
## `test_compute_incremental_worklist_reports_orphans(project: Path)`

Assert that deleting a source file causes its triefact to appear in `worklist.orphan_triefacts` without being deleted from disk.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_cli_plan_incremental_on_clean_tree_reports_noop fingerprint=c5f369e80b62fb9b6394580e4fd6528bf01fd7fde46152fc5cff2b4e9addb870 body_fp=8402558e3d0e8d56e071d5977847844571ba5dedf14fe31e17081b18b5fa100f -->
## `test_cli_plan_incremental_on_clean_tree_reports_noop(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie plan` on a coherent, fully-synced project reports no-op without showing a full-bootstrap cost header.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_cli_plan_incremental_on_drift_lists_only_affected fingerprint=94665fe3e49bf70c830e7f50939f03dc26b64afeec6ae732c2548a49c5968a9b body_fp=8799f6686b714fc22ee60014e4401a80dbd228396e0f560a2b76db935965668c -->
## `test_cli_plan_incremental_on_drift_lists_only_affected(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie plan` on a project with drift shows incremental cost, not full-bootstrap cost.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_cli_plan_all_forces_full_bootstrap_view fingerprint=fd9b83493d1cf2bb3617946a5a9511d4a89d3fef2f3edcb6c60253ce01b034ed body_fp=4b3cf35803072a258ea5cb8f476ef170537e0dbb204e15c9958b27ffeb9622df -->
## `test_cli_plan_all_forces_full_bootstrap_view(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie plan --all` outputs the full-bootstrap cost view, not the incremental plan.
<!-- trie:end -->