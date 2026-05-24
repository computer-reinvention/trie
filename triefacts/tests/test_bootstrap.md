---
trie_version: 0.1.2
source: tests/test_bootstrap.py
file_fingerprint: e5591c507fcc5cb637c3842a9f56816b1abffd56c88bdf226e350a15f229dcdf
last_synced_at: '2026-05-23T23:48:01Z'
defines:
- kind: module
  qualified_name: tests/test_bootstrap:__module__
  lines: 1-362
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
  lines: 80-115
- kind: function
  qualified_name: tests/test_bootstrap:test_plan_with_unknown_model_zero_cost
  lines: 118-127
- kind: function
  qualified_name: tests/test_bootstrap:test_plan_only_files_restricts_worklist
  lines: 130-142
- kind: function
  qualified_name: tests/test_bootstrap:test_plan_only_files_empty_yields_empty_plan
  lines: 145-155
- kind: function
  qualified_name: tests/test_bootstrap:test_run_bootstrap_respects_limit
  lines: 158-179
- kind: function
  qualified_name: tests/test_bootstrap:test_run_bootstrap_respects_budget
  lines: 182-205
- kind: function
  qualified_name: tests/test_bootstrap:test_run_bootstrap_unbounded_processes_all
  lines: 208-229
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_plan_makes_no_message_calls
  lines: 232-241
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_plan_outside_project_errors
  lines: 244-257
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_first_run_sync_requires_budget_or_limit_non_interactive
  lines: 260-270
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_first_run_sync_with_limit_succeeds
  lines: 273-280
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_sync_all_forces_full_pass
  lines: 283-295
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_sync_rejects_file_and_all_together
  lines: 298-303
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_sync_with_no_config_errors
  lines: 306-312
- kind: function
  qualified_name: tests/test_bootstrap:test_run_bootstrap_invokes_progress_callback
  lines: 315-361
incoming_refs: 0
outgoing_refs: 34
---
<!-- trie:section symbol=tests/test_bootstrap:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=e630b9cb8e2680065d055b7dca9ade95e635eef0774e5a5c0a7209a7676129e3 source_ref=04a669302ff19f1e43c1d31e0f7c26035a7a0f63 -->
## `tests/test_bootstrap`

Integration tests for `build_plan` and `run_bootstrap`, plus CLI-level tests for `trie plan` and `trie sync`.

- `FakeClient`: stub LLM client returning fixed token counts and toggling cache hit/miss on second call.
- `project`: pytest fixture providing a `tmp_path` with a valid `trie.toml` and three `.py` files of varying size.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:FakeClient fingerprint=ceebf20d768a48a04e09bf88002e0bd6342f4f5d5f4aaa6f137763c496e80a99 body_fp=155ff9e876dfa86578f0aa190c4cca5acc5dae333c9fe6dc79ffa4c135e9c8c1 source_ref=04a669302ff19f1e43c1d31e0f7c26035a7a0f63 -->
## `FakeClient`

Test double for an LLM client that tracks `generate` call count and returns a fixed `GenerationResponse`.

- `calls`: incremented on each `generate` invocation; used to toggle cache token fields.
- First `generate` call sets `cache_creation_input_tokens=500`; subsequent calls set `cache_read_input_tokens=500`.
- `count_tokens`: always returns `100` without network I/O.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:FakeClient.generate fingerprint=0ec0ae0f8e2a0f963b8fce2f3ad02a0c976b2d5a22a7ce046b9d55c8c9687d30 body_fp=9d23f38a2354f66b8d6029b0e0c3c7c1659eacf781d07dcf50ecf759e6f8f4ae source_ref=04a669302ff19f1e43c1d31e0f7c26035a7a0f63 -->
## `FakeClient.generate(self, _req: GenerationRequest) -> GenerationResponse`

Increment `FakeClient.calls` and return a fixed `GenerationResponse`, simulating cache-creation on call 1 and cache-read on subsequent calls.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=698f7944e4c721c392db1b12412d045778464b705ef0cd93e058707001dc8ab1 source_ref=04a669302ff19f1e43c1d31e0f7c26035a7a0f63 -->
## `FakeClient.count_tokens(self, _req: GenerationRequest) -> int`

Always return 100 from `FakeClient`, simulating a token-count probe without a real API call.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:project fingerprint=d5b12d48473fa51307a94d93e57a02093f21289d05d6fad7419855f2579e4068 body_fp=e03ccc5bde877a147f3aeb0f9712dedf8b0387921d1eb28431b8aa42b617cf6d source_ref=04a669302ff19f1e43c1d31e0f7c26035a7a0f63 -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal trie project with `trie.toml` and three Python files of varying size/symbol count.

- `small.py`: 1 function, 2 LOC
- `medium.py`: 3 functions, small bodies
- `large.py`: 2 functions, one with ~50 statements
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:_scanned_store fingerprint=be2171d309873933c9dd828dece87833bd3c117974cc17e64314491077d352a8 body_fp=24ac4360219361341f573e5789a1c319cf8a147e80e8db894a2301c5b074230e source_ref=04a669302ff19f1e43c1d31e0f7c26035a7a0f63 -->
## `_scanned_store(project: Path) -> Store`

Load config, initialise a `Store`, scan the project into it, and return the open store.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_plan_ranks_higher_score_first fingerprint=971668a5894eb518048310526504c351c58b5e22ec45f05a1b7253959aba477f body_fp=c2b0df2346342e77e389418010cb9a99e93f497632767cd6603edc238d226455 source_ref=04a669302ff19f1e43c1d31e0f7c26035a7a0f63 -->
## `test_plan_ranks_higher_score_first(project: Path)`

Assert that `build_plan` orders items by descending LOC×symbol-count score and sets a positive known cost.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_plan_excludes_files_with_no_documentable_symbols fingerprint=0d85118720b7198c3af34e2584b30afada2874a67a1cf2f2a427a8a70b83dba3 body_fp=bc6ab0adcc632612da362014aefa5af61c3f57b674fd853571c64523ba7165b6 source_ref=04a669302ff19f1e43c1d31e0f7c26035a7a0f63 -->
## `test_plan_excludes_files_with_no_documentable_symbols(project: Path, tmp_path: Path)`

Assert that `build_plan` omits files with no parser-surfaced symbols while including constants and underscore-prefixed defs.

- `imports_only.py`: excluded — only import statements, parser surfaces nothing.
- `constants_only.py`: included — module-level `NAME = value` yields a `constant` symbol.
- `private.py`: included — leading-underscore defs are not filtered.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_plan_with_unknown_model_zero_cost fingerprint=9cb25e13e4a98b51e03583f7d0300be59ea8cecf99b02408f98582488b3299c5 body_fp=25bc97cf54b83bd8571a46c955752b1ad21005c0415fb18a9e911d50420ffe8a source_ref=04a669302ff19f1e43c1d31e0f7c26035a7a0f63 -->
## `test_plan_with_unknown_model_zero_cost(project: Path)`

Assert that `build_plan` sets `pricing_known=False` and `total_estimated_cost=0.0` for an unrecognised model ID.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_plan_only_files_restricts_worklist fingerprint=1e790399a7417b3db08abac3e4c578a011ce29851fd16e568690708bc1c58f40 body_fp=37de3246a94296573f5c4a1bbb70cf70058a14f344b2c6dd9838cc834dcc6202 source_ref=04a669302ff19f1e43c1d31e0f7c26035a7a0f63 -->
## `test_plan_only_files_restricts_worklist(project: Path)`

Assert that `build_plan` with `only_files` returns a plan containing exactly the specified files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_plan_only_files_empty_yields_empty_plan fingerprint=5424dcad92c82bf1eda8fb269944d30a867a399394de6d341b41e5faa2d00908 body_fp=c3788d201f03cae17a7a705243122fd0d44b7a68fd368184a3414ed8d33d2b7a source_ref=04a669302ff19f1e43c1d31e0f7c26035a7a0f63 -->
## `test_plan_only_files_empty_yields_empty_plan(project: Path)`

Assert that passing an empty `only_files` set to `build_plan` produces a plan with no items and zero estimated cost.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_run_bootstrap_respects_limit fingerprint=7de8861ef77af322d07b4952145ffdf148a821f4ec4706ce27e6e011ffa57a76 body_fp=28be67ee5fa9055e04937e6c57a09f58344248774ff1357dde6502804aa14156 source_ref=04a669302ff19f1e43c1d31e0f7c26035a7a0f63 -->
## `test_run_bootstrap_respects_limit(project: Path)`

Assert that `run_bootstrap` stops after `limit=2` files and reports the remainder as skipped.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_run_bootstrap_respects_budget fingerprint=212829569c689d43cbb5a59833c28923a364e80704d7be3c66f6924e5ef0435f body_fp=06f9fa00f834c9e96c12a27988e265d807cf51c975969c2b5f9b30a2495f9bb9 source_ref=04a669302ff19f1e43c1d31e0f7c26035a7a0f63 -->
## `test_run_bootstrap_respects_budget(project: Path)`

Assert that `run_bootstrap` stops processing files once a tiny `budget_usd` is exhausted, syncing fewer than the full plan.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_run_bootstrap_unbounded_processes_all fingerprint=872b56bed5737b6a766200f7e71b75e8437693aae7e0a70cf5aa69d9ff1cd742 body_fp=ea2ff41e55331d4b5c38741c3f19ebe3d88f07c2b871a4a2d61ca48cfb8871c5 source_ref=04a669302ff19f1e43c1d31e0f7c26035a7a0f63 -->
## `test_run_bootstrap_unbounded_processes_all(project: Path)`

Assert that `run_bootstrap` with no budget and no limit syncs every file in the plan.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_cli_plan_makes_no_message_calls fingerprint=d225090e9f287c90f59210995c95d3e449567bdc5d4ccc428a9130c0960f7330 body_fp=b4ce05115b450a61ff0f33cc09557cd0a28b4d7b5240068d3689c2b0d56210c4 source_ref=04a669302ff19f1e43c1d31e0f7c26035a7a0f63 -->
## `test_cli_plan_makes_no_message_calls(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie plan` exits successfully and never invokes `generate` on the client.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_cli_plan_outside_project_errors fingerprint=68f003153534954db66fa1f239582223794f2233a90e3e18933617e113148631 body_fp=7fef420ff4f52812715e828e528b0d42e76b0e3b7ca8618dc6f6cbed07b33b57 source_ref=04a669302ff19f1e43c1d31e0f7c26035a7a0f63 -->
## `test_cli_plan_outside_project_errors(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert `trie plan` exits with code 1 and never constructs a client when no `trie.toml` is found.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_cli_first_run_sync_requires_budget_or_limit_non_interactive fingerprint=c176cbf44d1f8ffa33d4a17b559ffeffe7015a4b129cc030212027dd9c181d30 body_fp=4d162fe3445f94d27ac3825a71addb31ca087c23528f6171df2e82d237e3a095 source_ref=04a669302ff19f1e43c1d31e0f7c26035a7a0f63 -->
## `test_cli_first_run_sync_requires_budget_or_limit_non_interactive(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync` on a fresh project without `--budget` or `--limit` exits with code 1 and prompts for a cap.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_cli_first_run_sync_with_limit_succeeds fingerprint=9f99e521eba3b2b27410a062f94a8584e852b31e35a7a608b0e12db4102d0fba body_fp=f4aace3891a8cfc9f2c9f5d1848f48747566efd5779429ef6946d4e3d83ece05 source_ref=04a669302ff19f1e43c1d31e0f7c26035a7a0f63 -->
## `test_cli_first_run_sync_with_limit_succeeds(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync --limit 1` exits successfully on a first-run project with no existing triefacts.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_cli_sync_all_forces_full_pass fingerprint=d56ba3ef3b5d05f041df15ead42c9f087f79e118cdb43561fc1affec3453fe14 body_fp=4f8269cad4f050499e615388d607bfd0dd3f48485efa32349b00c78de27d7f22 source_ref=04a669302ff19f1e43c1d31e0f7c26035a7a0f63 -->
## `test_cli_sync_all_forces_full_pass(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync --all` triggers the full bootstrap path even when triefacts already exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_cli_sync_rejects_file_and_all_together fingerprint=01e55c9bfae3ee3f4a73b7419afbdbbac4c84a28c5e67be6c163ed78e93b93ec body_fp=49e51cb23ebd5ca9f608527d79f608883957b2635fb14da74cd9e09532e97e5a source_ref=04a669302ff19f1e43c1d31e0f7c26035a7a0f63 -->
## `test_cli_sync_rejects_file_and_all_together(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync --file <path> --all` exits with code 1 and reports mutual exclusivity.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_cli_sync_with_no_config_errors fingerprint=cd5d41cc3092e94d8b52e820f690b72a42c756589e877899f50dba42c729deff body_fp=fc8bce5d88b93b46c9889a3130e4cdf84995ecc18ab82bf634bca7a5be4e9483 source_ref=04a669302ff19f1e43c1d31e0f7c26035a7a0f63 -->
## `test_cli_sync_with_no_config_errors(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync` in a directory without `trie.toml` exits with code 1 and mentions `trie.toml` in output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_run_bootstrap_invokes_progress_callback fingerprint=6b44eba3f1833129fb1d37020e9e32268580ac28ad495377d1f8003868565e45 body_fp=b3dcb4a7a30cfbee1f7b6c6dae95944c985823e6286aa35dea2cc7d12cdebd4e source_ref=04a669302ff19f1e43c1d31e0f7c26035a7a0f63 -->
## `test_run_bootstrap_invokes_progress_callback(project: Path)`

Verify that `run_bootstrap` calls `on_start`/`on_done` for each processed file and `on_skip` (with reason `"limit reached"`) for each file cut by the limit.
<!-- trie:end -->