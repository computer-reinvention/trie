---
trie_version: 0.1.0
source: tests/test_bootstrap.py
file_fingerprint: b7e820e3e92550cf0c2ee3689408f86431e536626e3b4d2036416c795fdcc811
last_synced_at: '2026-05-12T18:21:10Z'
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
<!-- trie:section symbol=tests/test_bootstrap:FakeClient fingerprint=ceebf20d768a48a04e09bf88002e0bd6342f4f5d5f4aaa6f137763c496e80a99 body_fp=b701574e7c70cbbe4f33416192d0ef360b1ba2de503ae7461eee3060a1439081 -->
## `FakeClient(model_id: str = "anthropic/claude-sonnet-4-6", calls: int = 0)`

Stub LLM client that records call count and returns fixed token/cache responses.

- `generate`: increments `calls`; alternates cache-creation vs cache-read tokens on first vs subsequent calls.
- `count_tokens`: always returns `100`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:FakeClient.generate fingerprint=0ec0ae0f8e2a0f963b8fce2f3ad02a0c976b2d5a22a7ce046b9d55c8c9687d30 body_fp=f1505137c4869c541c2a9ea61888ed907038d062f4c425f56f6dc6c9be4c0f33 -->
## `generate(self, _req: GenerationRequest) -> GenerationResponse`

Return a synthetic `GenerationResponse`, alternating between cache-creation and cache-read token counts on successive calls.

- `calls`: incremented on each invocation to toggle cache token fields.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=0cc8e4c60852ed2343ba12efc7686b2f040b2c6b012d45e134249772b72c93f1 -->
## `count_tokens(self, _req: GenerationRequest) -> int`

Return a fixed token count of 100 for any request.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:project fingerprint=d5b12d48473fa51307a94d93e57a02093f21289d05d6fad7419855f2579e4068 body_fp=d0e4b2c5797370ac38726f21d75d5d0070c830d1c222f9e572e6b0bf8c8c3bad -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal trie project tree with a `trie.toml` and three Python source files of varying sizes.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_plan_ranks_higher_score_first fingerprint=971668a5894eb518048310526504c351c58b5e22ec45f05a1b7253959aba477f body_fp=1bf7135ead9a99c75fc04e9d32e4b6b28f755a6d597847c9fa6b2775b728e22f -->
## `test_plan_ranks_higher_score_first(project: Path)`

Assert that `build_plan` orders files by descending LOC×symbol-count score, pricing is known, and estimated cost is positive.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_plan_excludes_files_with_no_public_symbols fingerprint=1b3def771af61667125275913a5e4e30ae77069eb12659adf48c36ae58704f50 body_fp=03003eb66597ae8b00b5c85fb96bd19f92a3ceb378df4a1a041b85f090ea378a -->
## `test_plan_excludes_files_with_no_public_symbols(project: Path, tmp_path: Path)`

Assert that `build_plan` omits files whose only symbols are private (underscore-prefixed).
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_plan_with_unknown_model_zero_cost fingerprint=9cb25e13e4a98b51e03583f7d0300be59ea8cecf99b02408f98582488b3299c5 body_fp=9f4a2fe01c51fea7333ec621d9c9ed082db2be7706561bfc7e613a1cb2ba3135 -->
## `test_plan_with_unknown_model_zero_cost(project: Path)`

Assert that `build_plan` sets `pricing_known=False` and `total_estimated_cost=0.0` for unrecognised model IDs.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_plan_only_files_restricts_worklist fingerprint=1e790399a7417b3db08abac3e4c578a011ce29851fd16e568690708bc1c58f40 body_fp=02d882e95b8a1017f476344be6c20a1b65bc85e563576bb89717104f78caa23a -->
## `test_plan_only_files_restricts_worklist(project: Path)`

Verify that `only_files` limits `build_plan` output to exactly the specified file set.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_plan_only_files_empty_yields_empty_plan fingerprint=5424dcad92c82bf1eda8fb269944d30a867a399394de6d341b41e5faa2d00908 body_fp=2f9254cbe2c1881d28704ba1c2c61d6ec9d727c57f2609ec1dbe9bde0de20dd5 -->
## `test_plan_only_files_empty_yields_empty_plan(project: Path)`

Assert that passing an empty set to `only_files` produces a plan with no items and zero estimated cost.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_run_bootstrap_respects_limit fingerprint=7de8861ef77af322d07b4952145ffdf148a821f4ec4706ce27e6e011ffa57a76 body_fp=535a26c477d8e95c9df927a3e6ce0ece81b6814e214a94221485ddab64b7e369 -->
## `test_run_bootstrap_respects_limit(project: Path)`

Verify that `run_bootstrap` processes exactly `limit` files and counts the remainder as budget-skipped.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_run_bootstrap_respects_budget fingerprint=212829569c689d43cbb5a59833c28923a364e80704d7be3c66f6924e5ef0435f body_fp=b175e317d68fe13c72b50df4b6e2e1b2e5f9221dc264ee479ffe17af305fbb51 -->
## `test_run_bootstrap_respects_budget(project: Path)`

Verify that `run_bootstrap` halts after exhausting a tiny USD budget, processing fewer files than the full plan.

- `budget_usd=0.0001`: intentionally small to cap execution to roughly one file.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_run_bootstrap_unbounded_processes_all fingerprint=872b56bed5737b6a766200f7e71b75e8437693aae7e0a70cf5aa69d9ff1cd742 body_fp=0a4ea326aae1ee08b7a234bbf0a497e46c21bf69dc95b396b85134240b71981a -->
## `test_run_bootstrap_unbounded_processes_all(project: Path)`

Verify that `run_bootstrap` with no budget or limit processes every file in the plan.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_cli_plan_makes_no_message_calls fingerprint=39b5d7917ee277414b01d873170fa14aaec8e4c4974768008976c972a3fe1d90 body_fp=5d4714c8fa6cd87f35f4b071674fb8e502dde7103627eb5050ce7f56ab4cbd0b -->
## `test_cli_plan_makes_no_message_calls(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie plan` calls `count_tokens` but never calls `generate` on the injected client.

- `project`: fixture providing a temp dir with a valid `trie.toml` and Python files.
- Verifies exit code 0 and `"plan for"` in output.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_cli_plan_outside_project_errors fingerprint=68f003153534954db66fa1f239582223794f2233a90e3e18933617e113148631 body_fp=1109d277b52754dc3a974a4ae9115d49712d3d22e876d133bfbe97dee79ec79d -->
## `test_cli_plan_outside_project_errors(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie plan` exits with code 1 and never constructs a client when no `trie.toml` is found.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_cli_first_run_sync_requires_budget_or_limit_non_interactive fingerprint=55d19f815b2c63af3d7a743a8024aada97846247c97defa75e04a6e31125da04 body_fp=bd30f73238fc7e5e01f244d272ee74ee32e486693248b053c1ecf436a7769006 -->
## `test_cli_first_run_sync_requires_budget_or_limit_non_interactive(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync` on a fresh project exits with code 1 and mentions `--budget` or `--limit` when run non-interactively.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_cli_first_run_sync_with_limit_succeeds fingerprint=a8a5f1553238f649f03c990e6347874ce8d2884edee4ee0e8ae220e9f05b62b3 body_fp=21fc0fe3008993ebd7e8024db88f12c5d947f7f684d32980e624fe82a1779218 -->
## `test_cli_first_run_sync_with_limit_succeeds(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync --limit 1` exits successfully on a fresh project with no existing triefacts.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_cli_sync_all_forces_full_pass fingerprint=625e0c9ead995e825c124add9b676a2eea7489832d1538f84841acd170ef28b2 body_fp=29d1e4520c1a4be1ac857fec1fb4c04acf5d15a3c97dd03b7a5027a46d2c9258 -->
## `test_cli_sync_all_forces_full_pass(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync --all` runs the bootstrap path even when triefacts already exist.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_cli_sync_rejects_file_and_all_together fingerprint=01e55c9bfae3ee3f4a73b7419afbdbbac4c84a28c5e67be6c163ed78e93b93ec body_fp=70fba99a945d40c3ffb7902274904e37af96bca08e523e617a562458bfd8d79a -->
## `test_cli_sync_rejects_file_and_all_together(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that passing `--file` and `--all` together causes exit code 1 with a "mutually exclusive" error message.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_cli_sync_with_no_config_errors fingerprint=cd5d41cc3092e94d8b52e820f690b72a42c756589e877899f50dba42c729deff body_fp=ad77fa85fe213c5107488cf8422118050e8bcaed5ebcc0ec31f37771475d9da5 -->
## `test_cli_sync_with_no_config_errors(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync` in a directory without `trie.toml` exits with code 1 and mentions `trie.toml`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_run_bootstrap_invokes_progress_callback fingerprint=6b44eba3f1833129fb1d37020e9e32268580ac28ad495377d1f8003868565e45 body_fp=4930870a04217ed7f77db985f5bcfa5b12f56164d24190c0bfbda51e1e05fcb5 -->
## `test_run_bootstrap_invokes_progress_callback(project: Path)`

Verify that `run_bootstrap` fires `on_start`, `on_done`, and `on_skip` callbacks for processed and skipped files respectively.

- `on_start` called once per synced file with correct total count
- `on_skip` called for remaining files with reason `"limit reached"`
<!-- trie:end -->