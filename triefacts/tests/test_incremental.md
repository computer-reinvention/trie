---
trie_version: 0.1.0
source: tests/test_incremental.py
file_fingerprint: ef5b6fc086e0ace26a386b6560803d21d876401c23cd23f8ea530347a8733e57
last_synced_at: '2026-05-14T18:56:32Z'
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
<!-- trie:section symbol=tests/test_incremental:FakeClient fingerprint=dd2ce5cbac0a663e75372124f682811a08d99ca2d34d2c8147be3fb275b44790 body_fp=c79b0232a2c54c14c14093f07a782b24a027224ab407efab43345e485ef228a4 -->
## `FakeClient(model_id: str = "anthropic/claude-sonnet-4-6", body: str = "## generated\n\nbody.", calls: int = 0)`

Stub LLM client for tests that records call count and returns fixed token counts.

- `body`: text returned verbatim as `GenerationResponse.text`
- `calls`: incremented on each `generate` invocation
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:FakeClient.generate fingerprint=e5b2ba5644c34f4b6310cb1886861a5822e5463319ee71045769565cc6e6d011 body_fp=ab50d7ff8ffc0a1b77cfa3ca9f11f74845aa4d71ccd6154d815af4fe7b4438d9 -->
## `generate(self, _req: GenerationRequest) -> GenerationResponse`

Increment the call counter and return a fixed `GenerationResponse` with preset token counts.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=9d067b772e73f67b1bb1b8cb6fc3a256c95035c670c6695fa426a36018030c0b -->
## `count_tokens(_req: GenerationRequest) -> int`

Return a fixed token count of 100 for any request.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:project fingerprint=4e084006f178a9857caa68e57d59fa178c9ea3c6baac1bde21faa670adc80dea body_fp=ebe2fd9fbc241423786f005764e1c0bcb4f5207d069d07f73d5fc6e8cce4ab92 -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal two-file project with a `trie.toml` config under `tmp_path` and returns the project root.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_no_op_when_clean fingerprint=29350c3d31a93ea4618bd8d27979b13ff32b6c3315b6063f470262dc9e0e2997 body_fp=bfb57c2e47aa7737ec472946c185cd4af2afa3ac53cc30ea99ad435b014c5dab -->
## `test_incremental_no_op_when_clean(project: Path)`

Assert that `run_incremental` syncs zero files and makes zero LLM calls when all triefacts are current.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_resyncs_directly_changed_file fingerprint=d78da037adbd34418a5bd6828ccd8e99f7cfd48180cf2d168bc39d3ffa737584 body_fp=8455f11bbd1f35f8aa6b166a04b8eeeabefe8e2ab1dc1b52b7976219e0b47d24 -->
## `test_incremental_resyncs_directly_changed_file(project: Path)`

Assert that modifying a source file marks its triefact stale and causes `run_incremental` to regenerate it.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_cascades_to_callers fingerprint=3d4d1a6c94c9bdad3d047e5b4165a21d4500c811616151c63b2657be706a714a body_fp=95df55b3c173147aac3a79255a14126af7c15f48c3203bd53990625099784580 -->
## `test_incremental_cascades_to_callers(project: Path)`

Verify that editing `lib.py` triggers cascade regeneration of `app.py` and increments the correct stale/cascaded counters.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_respects_budget fingerprint=5a5621ee7a68c0bc5e8dcc317152897211eea4fc4c1bbc28b26b2f75ec2d0a73 body_fp=38ce41eb43a2d973cdd6083c45569cbb6dc0fed866bf5689cee8bb1a4b46df9f -->
## `test_incremental_respects_budget(project: Path)`

Assert that `run_incremental` skips files once the USD budget is exhausted.

- `budget_usd=0.0001`: tiny cap forces at least one file to be skipped.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_dispatched_via_cli fingerprint=76f88c12f569dd525ddcf02390e59164963d312a9c3a52ae5f0e880b916c8103 body_fp=59ac09af875154511990b7793a1380ab53761ccb3709cfd144bcd8269d066524 -->
## `test_incremental_dispatched_via_cli(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify that `trie sync` CLI routes through `run_incremental` and regenerates both lib and app triefacts.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_clean_via_cli fingerprint=ec121dfcf3dfa2e20573a1207e05298b58a48f6463f2a003536e3e55f5262ac7 body_fp=d897860031b4e840e8f0d37289cf4e1699cbd3c348c4a319e14a02507196e858 -->
## `test_incremental_clean_via_cli(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify that `trie sync` on an already-coherent project exits cleanly and reports "coherent".
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_with_no_changes_yields_empty fingerprint=8e45eeea8ec2dffaa97779e35aee757c4d2d1602b8547896940b24d88e0bfc80 body_fp=3fe9700aa030e636db0a2f7090f2b3b65b6deb46ae2c611aad3e9117261d4994 -->
## `test_incremental_with_no_changes_yields_empty(project: Path)`

Assert that `run_incremental` is a no-op when all triefacts are already up-to-date.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_incremental_handles_missing_triefact fingerprint=0e6264b2ea320f5d589407ae325cc58bfc5bc679de330cbc6e9aee9be1b43084 body_fp=8c46a7a10bca4dda09a7da8cca40eff79938fa97e48927eb567f10d16b015d1f -->
## `test_incremental_handles_missing_triefact(project: Path)`

Assert that `run_incremental` with no pre-existing triefacts marks all files directly stale and does not double-count via cascade.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_triefact_regenerated_only_for_affected_symbols_v01_limitation fingerprint=fca40f95e94fbb526a9d921e5072f7ab01b4f633a3f0a2247c780f42a2a55c7e body_fp=7b7d207033496003bf4b41a7e48c9a0d8bb476ae701cfccf2fa05361c64cff9c -->
## `test_triefact_regenerated_only_for_affected_symbols_v01_limitation(project: Path)`

Assert that v0.1 regenerates all symbols in an affected file, not only the changed symbol, and that cascade brings dependent files along.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_run_incremental_invokes_progress_callback fingerprint=c838ad91126bcd1ccca97818090a36de1d353cf655f16ea0db3fb242fb106ec6 body_fp=7645bdd9e7a134fe9e3c3e529799c42b6e59400c244434bb08ea5d2472e0f874 -->
## `test_run_incremental_invokes_progress_callback(project: Path)`

Verify that `run_incremental` fires `on_start` and `on_done` callbacks for every cascade-affected file.

- `starts`: collects `(rel_path, idx, total)` tuples from `on_start` calls.
- `dones`: collects `rel_path` strings from `on_done` calls.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_empty_when_clean fingerprint=cee10449e37638cbcb7584f41c7a16959603fbd74fc37e487f6c4431acef61cd body_fp=126b9fad5b457e2d02e055cb15f99d984119bc3d5974d3391ef28cdf55d4c08a -->
## `test_compute_incremental_worklist_empty_when_clean(project: Path)`

Assert that `compute_incremental_worklist` returns an empty worklist when the triefact tree is fully coherent.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_includes_cascade fingerprint=19c15c1b29c078331a336f622e363b66959f8716f801ca6fe7080644d95a55c2 body_fp=02e59515400ee3d4bac731f853ce9c4ec2861eafc7fa4e9ea9f5ead022a8b612 -->
## `test_compute_incremental_worklist_includes_cascade(project: Path)`

Assert that editing `lib.py` places it in `directly_stale` and `app.py` in `cascaded_files` without invoking any LLM.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_is_read_only fingerprint=b52fe57285334a3855e29c7336c6bcbc9cc95bfb04a5a962c757fce08ac63a67 body_fp=19dabff3b0e28e413ba89b78d534d707810f091a927ef0f8efcb81b5b2d529c6 -->
## `test_compute_incremental_worklist_is_read_only(project: Path)`

Assert that `compute_incremental_worklist` does not modify any triefact files on disk.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_compute_incremental_worklist_reports_orphans fingerprint=485e1297b791feffbf91b27b19055ae1493474b073d92853ea881e5c40bfad3c body_fp=baffb6e6189fd3aa7d74ac327c8caa00674e80307642927f7a220f4bf4d2d59a -->
## `test_compute_incremental_worklist_reports_orphans(project: Path)`

Assert that deleting a source file surfaces its triefact as an orphan without removing it from disk.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_cli_plan_incremental_on_clean_tree_reports_noop fingerprint=c5f369e80b62fb9b6394580e4fd6528bf01fd7fde46152fc5cff2b4e9addb870 body_fp=d9577d4209a2b90e11e6dd9db3be84adf366fc1af52b3ec0680c2cd5b8799dd2 -->
## `test_cli_plan_incremental_on_clean_tree_reports_noop(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie plan` on a coherent, fully-synced project outputs "coherent" or "no-op" and omits the full-bootstrap header.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_cli_plan_incremental_on_drift_lists_only_affected fingerprint=94665fe3e49bf70c830e7f50939f03dc26b64afeec6ae732c2548a49c5968a9b body_fp=d05e01eb78073976154a11b82d216a6ce53990f4a8703ca5a945f5a2e52df427 -->
## `test_cli_plan_incremental_on_drift_lists_only_affected(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie plan` on an established project with drift outputs incremental cost, not full-bootstrap cost.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_incremental:test_cli_plan_all_forces_full_bootstrap_view fingerprint=fd9b83493d1cf2bb3617946a5a9511d4a89d3fef2f3edcb6c60253ce01b034ed body_fp=4b3cf35803072a258ea5cb8f476ef170537e0dbb204e15c9958b27ffeb9622df -->
## `test_cli_plan_all_forces_full_bootstrap_view(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie plan --all` outputs the full-bootstrap cost view, not the incremental plan.
<!-- trie:end -->