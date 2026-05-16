---
trie_version: 0.1.0
source: tests/test_bootstrap.py
file_fingerprint: 1b3cc4748e30ace4478f8a8eae2c8b18e47b0d8d1a129e149b03b7403080f397
last_synced_at: '2026-05-16T10:51:08Z'
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
  qualified_name: tests/test_bootstrap:_scanned_store
  lines: 57-61
- kind: function
  qualified_name: tests/test_bootstrap:test_plan_ranks_higher_score_first
  lines: 64-77
- kind: function
  qualified_name: tests/test_bootstrap:test_plan_excludes_files_with_no_documentable_symbols
  lines: 80-101
- kind: function
  qualified_name: tests/test_bootstrap:test_plan_with_unknown_model_zero_cost
  lines: 104-113
- kind: function
  qualified_name: tests/test_bootstrap:test_plan_only_files_restricts_worklist
  lines: 116-128
- kind: function
  qualified_name: tests/test_bootstrap:test_plan_only_files_empty_yields_empty_plan
  lines: 131-141
- kind: function
  qualified_name: tests/test_bootstrap:test_run_bootstrap_respects_limit
  lines: 144-165
- kind: function
  qualified_name: tests/test_bootstrap:test_run_bootstrap_respects_budget
  lines: 168-191
- kind: function
  qualified_name: tests/test_bootstrap:test_run_bootstrap_unbounded_processes_all
  lines: 194-215
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_plan_makes_no_message_calls
  lines: 218-227
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_plan_outside_project_errors
  lines: 230-243
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_first_run_sync_requires_budget_or_limit_non_interactive
  lines: 246-256
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_first_run_sync_with_limit_succeeds
  lines: 259-266
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_sync_all_forces_full_pass
  lines: 269-281
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_sync_rejects_file_and_all_together
  lines: 284-289
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_sync_with_no_config_errors
  lines: 292-298
- kind: function
  qualified_name: tests/test_bootstrap:test_run_bootstrap_invokes_progress_callback
  lines: 301-347
incoming_refs: 0
outgoing_refs: 27
---
<!-- trie:section symbol=tests/test_bootstrap:FakeClient fingerprint=ceebf20d768a48a04e09bf88002e0bd6342f4f5d5f4aaa6f137763c496e80a99 body_fp=daf058e1b67a18e9cd6b974b1d0813763e23b80f2f21f3711df3bd2b872a3ef9 source_ref=295b134de94b596d598954dbd34017d13b93f383 -->
## `FakeClient(model_id: str = "anthropic/claude-sonnet-4-6", calls: int = 0)`

Stub LLM client that records call counts and returns fixed token/cost responses for bootstrap tests.

- `generate`: increments `calls`; alternates between cache-creation and cache-read token counts.
- `count_tokens`: always returns 100 without incrementing `calls`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:FakeClient.generate fingerprint=0ec0ae0f8e2a0f963b8fce2f3ad02a0c976b2d5a22a7ce046b9d55c8c9687d30 body_fp=31805384e22771545ffe97300d042048cfa0cd56d7b9f2983e6b59491cf8c47b source_ref=295b134de94b596d598954dbd34017d13b93f383 -->
## `generate(self, _req: GenerationRequest) -> GenerationResponse`

Return a synthetic `GenerationResponse`, alternating cache-creation and cache-read tokens on first vs. subsequent calls.

- `calls`: incremented each invocation to toggle cache token fields.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=9d067b772e73f67b1bb1b8cb6fc3a256c95035c670c6695fa426a36018030c0b source_ref=295b134de94b596d598954dbd34017d13b93f383 -->
## `count_tokens(_req: GenerationRequest) -> int`

Return a fixed token count of 100 for any request.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:project fingerprint=d5b12d48473fa51307a94d93e57a02093f21289d05d6fad7419855f2579e4068 body_fp=eec260563cea725971a62cdef59be814a2e803086b23fb9f4a285af78aff36d1 source_ref=295b134de94b596d598954dbd34017d13b93f383 -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal trie project with `trie.toml` and three Python source files of varying size/symbol count.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_plan_ranks_higher_score_first fingerprint=971668a5894eb518048310526504c351c58b5e22ec45f05a1b7253959aba477f body_fp=a233c134172fc91cf9225e415aff3bb9e649162a36fb4e7562bc51832119dd59 source_ref=295b134de94b596d598954dbd34017d13b93f383 -->
## `test_plan_ranks_higher_score_first(project: Path)`

Assert that `build_plan` orders files by descending LOC×symbol-count score, with pricing populated.
<!-- trie:end -->



<!-- trie:section symbol=tests/test_bootstrap:test_plan_with_unknown_model_zero_cost fingerprint=9cb25e13e4a98b51e03583f7d0300be59ea8cecf99b02408f98582488b3299c5 body_fp=1ed5391b8839797f01507d031ebead435f8f9cf03ca9918b8389df4220dd805b source_ref=295b134de94b596d598954dbd34017d13b93f383 -->
## `test_plan_with_unknown_model_zero_cost(project: Path)`

Assert that `build_plan` with an unrecognised model sets `pricing_known=False` and `total_estimated_cost==0.0`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_plan_only_files_restricts_worklist fingerprint=1e790399a7417b3db08abac3e4c578a011ce29851fd16e568690708bc1c58f40 body_fp=c5c89408a2c7ba0af89d3ba189d8232da8057e08518a22e93bd264ed5dd8b1eb source_ref=295b134de94b596d598954dbd34017d13b93f383 -->
## `test_plan_only_files_restricts_worklist(project: Path)`

Verify that `only_files` restricts `build_plan` output to exactly the specified file paths.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_plan_only_files_empty_yields_empty_plan fingerprint=5424dcad92c82bf1eda8fb269944d30a867a399394de6d341b41e5faa2d00908 body_fp=c3788d201f03cae17a7a705243122fd0d44b7a68fd368184a3414ed8d33d2b7a source_ref=295b134de94b596d598954dbd34017d13b93f383 -->
## `test_plan_only_files_empty_yields_empty_plan(project: Path)`

Assert that passing an empty `only_files` set to `build_plan` produces a plan with no items and zero estimated cost.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_run_bootstrap_respects_limit fingerprint=7de8861ef77af322d07b4952145ffdf148a821f4ec4706ce27e6e011ffa57a76 body_fp=aa38696556b523bdef5608923cc8b87d962e3d129af63134c27e0916e3939041 source_ref=295b134de94b596d598954dbd34017d13b93f383 -->
## `test_run_bootstrap_respects_limit(project: Path)`

Verify that `run_bootstrap` stops after processing exactly `limit` files and records the remainder as budget-skipped.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_run_bootstrap_respects_budget fingerprint=212829569c689d43cbb5a59833c28923a364e80704d7be3c66f6924e5ef0435f body_fp=811136ef71df2a18fa61e7ba8e64fabc81280f8f9fe58ac65298b1b56dfd9c12 source_ref=295b134de94b596d598954dbd34017d13b93f383 -->
## `test_run_bootstrap_respects_budget(project: Path)`

Assert that a tiny `budget_usd` caps generation to fewer than all files but at least one.

- `budget_usd=0.0001`: intentionally small to trigger mid-run budget exhaustion.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_run_bootstrap_unbounded_processes_all fingerprint=872b56bed5737b6a766200f7e71b75e8437693aae7e0a70cf5aa69d9ff1cd742 body_fp=0a4ea326aae1ee08b7a234bbf0a497e46c21bf69dc95b396b85134240b71981a source_ref=295b134de94b596d598954dbd34017d13b93f383 -->
## `test_run_bootstrap_unbounded_processes_all(project: Path)`

Verify that `run_bootstrap` with no budget or limit processes every file in the plan.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_cli_plan_makes_no_message_calls fingerprint=d225090e9f287c90f59210995c95d3e449567bdc5d4ccc428a9130c0960f7330 body_fp=8572c3397f8a53cab709e707c22ee072b9c642c11dad83fff02b8acf841a733d source_ref=c5f2a27d17af1fac1345ecf2d272264e44780d76 -->
## `test_cli_plan_makes_no_message_calls(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie plan` calls `count_tokens` but never calls `generate` on the injected client.

- `project`: temp project fixture with `trie.toml` and Python source files.
- Verifies exit code 0 and `"plan for"` in output.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_cli_plan_outside_project_errors fingerprint=68f003153534954db66fa1f239582223794f2233a90e3e18933617e113148631 body_fp=1109d277b52754dc3a974a4ae9115d49712d3d22e876d133bfbe97dee79ec79d source_ref=295b134de94b596d598954dbd34017d13b93f383 -->
## `test_cli_plan_outside_project_errors(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie plan` exits with code 1 and never constructs a client when no `trie.toml` is found.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_cli_first_run_sync_requires_budget_or_limit_non_interactive fingerprint=c176cbf44d1f8ffa33d4a17b559ffeffe7015a4b129cc030212027dd9c181d30 body_fp=83e08da9ac915f519d9efb396dae8dfecde560b7aa62146db6abb1e975fac75f source_ref=c5f2a27d17af1fac1345ecf2d272264e44780d76 -->
## `test_cli_first_run_sync_requires_budget_or_limit_non_interactive(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync` on a fresh project exits with code 1 when no `--budget` or `--limit` flag is provided.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_cli_first_run_sync_with_limit_succeeds fingerprint=9f99e521eba3b2b27410a062f94a8584e852b31e35a7a608b0e12db4102d0fba body_fp=536339d88ffbbe09c350a1a4174629982acac38b3b2ec383a4ec554662b81610 source_ref=c5f2a27d17af1fac1345ecf2d272264e44780d76 -->
## `test_cli_first_run_sync_with_limit_succeeds(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync --limit 1` succeeds on a fresh project with no existing triefacts.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_cli_sync_all_forces_full_pass fingerprint=d56ba3ef3b5d05f041df15ead42c9f087f79e118cdb43561fc1affec3453fe14 body_fp=29d1e4520c1a4be1ac857fec1fb4c04acf5d15a3c97dd03b7a5027a46d2c9258 source_ref=c5f2a27d17af1fac1345ecf2d272264e44780d76 -->
## `test_cli_sync_all_forces_full_pass(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync --all` runs the bootstrap path even when triefacts already exist.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_cli_sync_rejects_file_and_all_together fingerprint=01e55c9bfae3ee3f4a73b7419afbdbbac4c84a28c5e67be6c163ed78e93b93ec body_fp=76b2fb6638ea47134c4eeb58b47ca252a91676a6f7a9e559d8ce2804a8639643 source_ref=295b134de94b596d598954dbd34017d13b93f383 -->
## `test_cli_sync_rejects_file_and_all_together(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that passing `--file` and `--all` together exits with code 1 and reports mutual exclusivity.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_cli_sync_with_no_config_errors fingerprint=cd5d41cc3092e94d8b52e820f690b72a42c756589e877899f50dba42c729deff body_fp=ad77fa85fe213c5107488cf8422118050e8bcaed5ebcc0ec31f37771475d9da5 source_ref=295b134de94b596d598954dbd34017d13b93f383 -->
## `test_cli_sync_with_no_config_errors(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync` in a directory without `trie.toml` exits with code 1 and mentions `trie.toml`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_run_bootstrap_invokes_progress_callback fingerprint=6b44eba3f1833129fb1d37020e9e32268580ac28ad495377d1f8003868565e45 body_fp=c623bb5461c6491dd274ac73715a9f8fd352ff98a0d87a382814a33ec8567995 source_ref=295b134de94b596d598954dbd34017d13b93f383 -->
## `test_run_bootstrap_invokes_progress_callback(project: Path)`

Verify that `run_bootstrap` fires `on_start`/`on_done` for each processed file and `on_skip` with reason `"limit reached"` for files cut by `limit`.

- `starts`: asserted to equal `limit` (2) entries.
- `skips`: asserted to equal `len(plan.items) - 2`, each with reason `"limit reached"`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:_scanned_store fingerprint=be2171d309873933c9dd828dece87833bd3c117974cc17e64314491077d352a8 body_fp=b866baf8b0f0da0e2c1ed73fe582834631116b216fac7d64fa7001b5a456b868 source_ref=d81050fda19efe01c9150c2635c3b24dff5debd3 -->
## `_scanned_store(project: Path) -> Store`

Load config from `project`, initialise a graph `Store`, scan the project into it, and return the open store.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_plan_excludes_files_with_no_documentable_symbols fingerprint=726c876c56b82d65b082a64bb62bb92ccd91d87af9683b492c0958654b307c17 body_fp=caa31741df143c8479993a1a55ea8a55c9864ec5a253a285fa2e41e60fb7784b source_ref=d81050fda19efe01c9150c2635c3b24dff5debd3 -->
## `test_plan_excludes_files_with_no_documentable_symbols(project: Path, tmp_path: Path)`

Assert that `build_plan` omits files with no parser-surfaced symbols but includes files with private (`_`-prefixed) defs.

- `empty_module.py`: imports + constant only; no `def`/`class` → excluded.
- `private.py`: contains `_hidden()` def → included.
<!-- trie:end -->