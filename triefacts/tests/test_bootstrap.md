---
trie_version: 0.1.0
source: tests/test_bootstrap.py
file_fingerprint: b7e820e3e92550cf0c2ee3689408f86431e536626e3b4d2036416c795fdcc811
last_synced_at: '2026-05-14T17:18:22Z'
defines:
- kind: class
  qualified_name: tests/test_bootstrap:FakeClient
  lines: 19-34
- kind: method
  qualified_name: tests/test_bootstrap:FakeClient.generate
  lines: 23-31
- kind: method
  qualified_name: tests/test_bootstrap:FakeClient.count_tokens
  lines: 33-34
- kind: function
  qualified_name: tests/test_bootstrap:project
  lines: 38-54
- kind: function
  qualified_name: tests/test_bootstrap:test_plan_ranks_higher_score_first
  lines: 64-77
- kind: function
  qualified_name: tests/test_bootstrap:test_plan_excludes_files_with_no_public_symbols
  lines: 80-90
- kind: function
  qualified_name: tests/test_bootstrap:test_plan_with_unknown_model_zero_cost
  lines: 93-102
- kind: function
  qualified_name: tests/test_bootstrap:test_plan_only_files_restricts_worklist
  lines: 105-117
- kind: function
  qualified_name: tests/test_bootstrap:test_plan_only_files_empty_yields_empty_plan
  lines: 120-130
- kind: function
  qualified_name: tests/test_bootstrap:test_run_bootstrap_respects_limit
  lines: 133-154
- kind: function
  qualified_name: tests/test_bootstrap:test_run_bootstrap_respects_budget
  lines: 157-180
- kind: function
  qualified_name: tests/test_bootstrap:test_run_bootstrap_unbounded_processes_all
  lines: 183-204
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_plan_makes_no_message_calls
  lines: 207-216
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_plan_outside_project_errors
  lines: 219-232
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_first_run_sync_requires_budget_or_limit_non_interactive
  lines: 235-245
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_first_run_sync_with_limit_succeeds
  lines: 248-255
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_sync_all_forces_full_pass
  lines: 258-270
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_sync_rejects_file_and_all_together
  lines: 273-278
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_sync_with_no_config_errors
  lines: 281-287
- kind: function
  qualified_name: tests/test_bootstrap:test_run_bootstrap_invokes_progress_callback
  lines: 290-336
incoming_refs: 0
outgoing_refs: 27
---
<!-- trie:section symbol=tests/test_bootstrap:FakeClient fingerprint=ceebf20d768a48a04e09bf88002e0bd6342f4f5d5f4aaa6f137763c496e80a99 body_fp=d3ddf47b748ac243843e718bcda5e333699fe9af0225d6bb5911eb8c870fe09d -->
## `FakeClient(model_id: str = "anthropic/claude-sonnet-4-6", calls: int = 0)`

Stub LLM client that returns fixed token counts and alternates cache creation/read tokens across calls.

- `generate`: increments `calls`; first call simulates cache creation, subsequent calls simulate cache reads.
- `count_tokens`: always returns `100`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:FakeClient.generate fingerprint=0ec0ae0f8e2a0f963b8fce2f3ad02a0c976b2d5a22a7ce046b9d55c8c9687d30 body_fp=6142ad45b5c14aa20c796fbe1a39816fb213e1b39f9059677111164a81ec7918 -->
## `generate(self, _req: GenerationRequest) -> GenerationResponse`

Return a fixed `GenerationResponse`, toggling cache creation/read tokens between first and subsequent calls.

- `calls`: incremented each invocation to track call count.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=a8a8c0b325c425618e3e7394f09962fff89b9aa04c714b490d2cddb1ecc24f9e -->
## `count_tokens(self, _req: GenerationRequest) -> int`

Return a fixed token count of 100 for any generation request.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:project fingerprint=d5b12d48473fa51307a94d93e57a02093f21289d05d6fad7419855f2579e4068 body_fp=1caf16f868c0355486ce721743748e2aeaceb71cf3fd467f66105abc330ec5e2 -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal trie project with config and three Python source files of varying size.

- `tmp_path`: pytest-provided temporary directory used as the project root.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_plan_ranks_higher_score_first fingerprint=971668a5894eb518048310526504c351c58b5e22ec45f05a1b7253959aba477f body_fp=4d72f2624f2c2901f190ee59f4810c2a6557bdd64a3c1261dc5b8725cad98edd -->
## `test_plan_ranks_higher_score_first(project: Path)`

Assert that `build_plan` orders files by descending LOC×symbol-count score, with `large.py` ranked first.

- `plan.pricing_known` must be `True` and `total_estimated_cost` positive.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_plan_excludes_files_with_no_public_symbols fingerprint=1b3def771af61667125275913a5e4e30ae77069eb12659adf48c36ae58704f50 body_fp=03003eb66597ae8b00b5c85fb96bd19f92a3ceb378df4a1a041b85f090ea378a -->
## `test_plan_excludes_files_with_no_public_symbols(project: Path, tmp_path: Path)`

Assert that `build_plan` omits files whose only symbols are private (underscore-prefixed).
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_plan_with_unknown_model_zero_cost fingerprint=9cb25e13e4a98b51e03583f7d0300be59ea8cecf99b02408f98582488b3299c5 body_fp=5691a77dd79cdf119cdb25f016894e4757bc279aecc078cacc9f081ea659d695 -->
## `test_plan_with_unknown_model_zero_cost(project: Path)`

Assert that `build_plan` with an unrecognised model sets `pricing_known=False` and `total_estimated_cost=0.0`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_plan_only_files_restricts_worklist fingerprint=1e790399a7417b3db08abac3e4c578a011ce29851fd16e568690708bc1c58f40 body_fp=02d882e95b8a1017f476344be6c20a1b65bc85e563576bb89717104f78caa23a -->
## `test_plan_only_files_restricts_worklist(project: Path)`

Verify that `only_files` limits `build_plan` output to exactly the specified file set.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_plan_only_files_empty_yields_empty_plan fingerprint=5424dcad92c82bf1eda8fb269944d30a867a399394de6d341b41e5faa2d00908 body_fp=050c7c413bd605ba9192ae9896f32660490599f1b134ac46176a084884efa627 -->
## `test_plan_only_files_empty_yields_empty_plan(project: Path)`

Assert that passing an empty `only_files` set to `build_plan` produces a plan with no items and zero cost.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_run_bootstrap_respects_limit fingerprint=7de8861ef77af322d07b4952145ffdf148a821f4ec4706ce27e6e011ffa57a76 body_fp=51f45bbfdc41d8b368222d128bdba746c7c017fe5f2162ef10dd729f8d6e1759 -->
## `test_run_bootstrap_respects_limit(project: Path)`

Verify that `run_bootstrap` processes exactly `limit` files and marks the remainder as budget-skipped.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_run_bootstrap_respects_budget fingerprint=212829569c689d43cbb5a59833c28923a364e80704d7be3c66f6924e5ef0435f body_fp=09621b026c4e780e25bafea7cf1ebb1d8e117ec87eb4768d9c738d4d12004b74 -->
## `test_run_bootstrap_respects_budget(project: Path)`

Verify that a tiny `budget_usd` caps bootstrap to fewer than all files while processing at least one.

- `budget_usd=0.0001`: intentionally small to trigger early budget exhaustion.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_run_bootstrap_unbounded_processes_all fingerprint=872b56bed5737b6a766200f7e71b75e8437693aae7e0a70cf5aa69d9ff1cd742 body_fp=0a4ea326aae1ee08b7a234bbf0a497e46c21bf69dc95b396b85134240b71981a -->
## `test_run_bootstrap_unbounded_processes_all(project: Path)`

Verify that `run_bootstrap` with no budget or limit processes every file in the plan.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_cli_plan_makes_no_message_calls fingerprint=39b5d7917ee277414b01d873170fa14aaec8e4c4974768008976c972a3fe1d90 body_fp=1861b17ec27355d836c0ef8f0369af5e8a40892c55d2001c867398c5605d9983 -->
## `test_cli_plan_makes_no_message_calls(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie plan` calls `count_tokens` but never calls `generate` on the injected client.

- `project`: fixture providing a temp dir with `trie.toml` and Python files.
- Verifies exit code 0 and `"plan for"` in output.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_cli_plan_outside_project_errors fingerprint=68f003153534954db66fa1f239582223794f2233a90e3e18933617e113148631 body_fp=1109d277b52754dc3a974a4ae9115d49712d3d22e876d133bfbe97dee79ec79d -->
## `test_cli_plan_outside_project_errors(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie plan` exits with code 1 and never constructs a client when no `trie.toml` is found.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_cli_first_run_sync_requires_budget_or_limit_non_interactive fingerprint=55d19f815b2c63af3d7a743a8024aada97846247c97defa75e04a6e31125da04 body_fp=8f6666a987a7d07e52a57ebb31f35928927eb2f5cae1e5fe4fcdd326e7b7dcd1 -->
## `test_cli_first_run_sync_requires_budget_or_limit_non_interactive(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync` on a fresh project with no triefacts exits with code 1 when neither `--budget` nor `--limit` is supplied.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_cli_first_run_sync_with_limit_succeeds fingerprint=a8a5f1553238f649f03c990e6347874ce8d2884edee4ee0e8ae220e9f05b62b3 body_fp=536339d88ffbbe09c350a1a4174629982acac38b3b2ec383a4ec554662b81610 -->
## `test_cli_first_run_sync_with_limit_succeeds(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync --limit 1` succeeds on a fresh project with no existing triefacts.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_cli_sync_all_forces_full_pass fingerprint=625e0c9ead995e825c124add9b676a2eea7489832d1538f84841acd170ef28b2 body_fp=744487785bf9cd6f62fbba14569a2feb6072ff31ba87fcf910da338ec3da27cf -->
## `test_cli_sync_all_forces_full_pass(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync --all` re-runs the bootstrap path even when triefacts already exist.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_cli_sync_rejects_file_and_all_together fingerprint=01e55c9bfae3ee3f4a73b7419afbdbbac4c84a28c5e67be6c163ed78e93b93ec body_fp=f0589a8b6e3a813a4d4361af548fb9c23a98f2b1c8d2447b07fad3e5c15760d4 -->
## `test_cli_sync_rejects_file_and_all_together(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that passing both `--file` and `--all` to `trie sync` exits with code 1 and reports mutual exclusivity.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_cli_sync_with_no_config_errors fingerprint=cd5d41cc3092e94d8b52e820f690b72a42c756589e877899f50dba42c729deff body_fp=fdc0b22395555066da3a37e56ca56e897ef32d3f23cdcf98059f73b14b31ba9c -->
## `test_cli_sync_with_no_config_errors(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert `trie sync` in a directory without `trie.toml` exits with code 1 and mentions `trie.toml`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_run_bootstrap_invokes_progress_callback fingerprint=6b44eba3f1833129fb1d37020e9e32268580ac28ad495377d1f8003868565e45 body_fp=baad64c48d20a9dc4ffcf947e3e755fb061f0b6dfa4c94de2cf37ba7bf95346e -->
## `test_run_bootstrap_invokes_progress_callback(project: Path)`

Verify that `run_bootstrap` fires `on_start`, `on_done`, and `on_skip` callbacks for processed and skipped files.

- `on_start` called once per synced file, with correct total count
- `on_skip` called for each file beyond the limit, with reason `"limit reached"`
<!-- trie:end -->