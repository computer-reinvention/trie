---
trie_version: 0.1.5
source: tests/test_bootstrap.py
file_fingerprint: e41001506f52f7ceea533071df38f0121ff20078c519ed1189d3f8fd3ea3489b
last_synced_at: '2026-05-28T15:04:22Z'
defines:
- kind: module
  qualified_name: tests/test_bootstrap:__module__
  lines: 1-453
- kind: function
  qualified_name: tests/test_bootstrap:project
  lines: 18-34
- kind: function
  qualified_name: tests/test_bootstrap:_scanned_store
  lines: 37-41
- kind: function
  qualified_name: tests/test_bootstrap:test_plan_ranks_higher_score_first
  lines: 44-63
- kind: function
  qualified_name: tests/test_bootstrap:test_plan_excludes_files_with_no_documentable_symbols
  lines: 66-107
- kind: function
  qualified_name: tests/test_bootstrap:test_plan_with_unknown_model_zero_cost
  lines: 110-125
- kind: function
  qualified_name: tests/test_bootstrap:test_plan_only_files_restricts_worklist
  lines: 128-146
- kind: function
  qualified_name: tests/test_bootstrap:test_plan_only_files_empty_yields_empty_plan
  lines: 149-165
- kind: function
  qualified_name: tests/test_bootstrap:test_run_bootstrap_respects_limit
  lines: 168-201
- kind: function
  qualified_name: tests/test_bootstrap:test_run_bootstrap_respects_budget
  lines: 204-239
- kind: function
  qualified_name: tests/test_bootstrap:test_run_bootstrap_unbounded_processes_all
  lines: 242-275
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_plan_makes_no_message_calls
  lines: 278-293
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_plan_outside_project_errors
  lines: 296-309
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_first_run_sync_requires_budget_or_limit_non_interactive
  lines: 312-331
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_first_run_sync_with_limit_succeeds
  lines: 334-350
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_sync_all_forces_full_pass
  lines: 353-374
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_sync_rejects_file_and_all_together
  lines: 377-382
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_sync_with_no_config_errors
  lines: 385-391
- kind: function
  qualified_name: tests/test_bootstrap:test_run_bootstrap_invokes_progress_callback
  lines: 394-452
incoming_refs: 0
outgoing_refs: 44
---
<!-- trie:section symbol=tests/test_bootstrap:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=e630b9cb8e2680065d055b7dca9ade95e635eef0774e5a5c0a7209a7676129e3 source_ref=04a669302ff19f1e43c1d31e0f7c26035a7a0f63 -->
## `tests/test_bootstrap`

Integration tests for `build_plan` and `run_bootstrap`, plus CLI-level tests for `trie plan` and `trie sync`.

- `FakeClient`: stub LLM client returning fixed token counts and toggling cache hit/miss on second call.
- `project`: pytest fixture providing a `tmp_path` with a valid `trie.toml` and three `.py` files of varying size.
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
<!-- trie:section symbol=tests/test_bootstrap:test_plan_ranks_higher_score_first fingerprint=40427304095c2846dbbff8a2f455aab1384b43952e2733e744132d43eefba518 body_fp=a209965b13e2d89cc9adf70f2104d7f42051e1cee59ef4f183510e9b173e1bcc source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af -->
## `test_plan_ranks_higher_score_first(project: Path)`

Assert that `build_plan` orders items by descending LOC×symbol-count score and reports a positive estimated cost.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_plan_excludes_files_with_no_documentable_symbols fingerprint=2e21e8749c7579b6c606c86a2a9988b1169322c0ee9f9422d76e47f4ee7b71c2 body_fp=f9c8bd01a021e58358967f22a9ec211f01cf29deee5e5be15d3fdf05fc9289fe source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af -->
## `test_plan_excludes_files_with_no_documentable_symbols(project: Path, tmp_path: Path)`

Assert that `build_plan` omits files with no parser-surfaced symbols while including files with constants or underscore-prefixed defs.

- `imports_only.py`: excluded — only import statements, no surfaced symbols.
- `constants_only.py`: included — module-level assignments produce `constant` symbols.
- `private.py`: included — leading-underscore defs are not filtered.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_plan_with_unknown_model_zero_cost fingerprint=4f3e6cae5f4d17263391af3c3ffbb57f366fa56666a272dd7bafd479a388c68e body_fp=fa934eefc950aaedf6bf5d57cbfe29c5676fe694f720411a99dec91878eef564 source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af -->
## `test_plan_with_unknown_model_zero_cost(project: Path)`

Assert that `build_plan` sets `pricing_known=False` and `total_estimated_cost=0.0` when the model has no pricing data.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_plan_only_files_restricts_worklist fingerprint=e321d8979a7335532ee65e02cd7ab534224347d76d55b2a11cc341ce5f022b59 body_fp=d64f09646f0d18f609b90c0b6dabe08ea68d067f6bef8a159e490e9b87aa1d6a source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af -->
## `test_plan_only_files_restricts_worklist(project: Path)`

Assert that `build_plan` with `only_files={"medium.py"}` produces a plan containing exactly that one file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_plan_only_files_empty_yields_empty_plan fingerprint=7d6eb63549e31de9fdea6f9528084eda6ecd794da18fa169e9cf51865b8eb8ca body_fp=c3788d201f03cae17a7a705243122fd0d44b7a68fd368184a3414ed8d33d2b7a source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af -->
## `test_plan_only_files_empty_yields_empty_plan(project: Path)`

Assert that passing an empty `only_files` set to `build_plan` produces a plan with no items and zero estimated cost.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_run_bootstrap_respects_limit fingerprint=70e8a39ca994df819ddab758a7970a484a4a829705884b7c8a1da2baba89db85 body_fp=c21c18d979b5afceb8a7b20ab8024c84ea164b398af34937841cfac3b902e832 source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af -->
## `test_run_bootstrap_respects_limit(project: Path)`

Assert that `run_bootstrap` syncs exactly `limit` files and skips the remainder.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_run_bootstrap_respects_budget fingerprint=6bc46da02f86461edf7e62e32814bfe6803a56c903f9dcec80cc0ec35c7c0d77 body_fp=f6033f836f21f68bfedf39491847cd122701e4b245795480391e8ee3ae9cdef2 source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af -->
## `test_run_bootstrap_respects_budget(project: Path)`

Assert that `run_bootstrap` stops processing files once a USD budget is exhausted, syncing fewer than all plan items.

- `budget_usd=0.0001`: intentionally tiny to cap at roughly one file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_run_bootstrap_unbounded_processes_all fingerprint=90ebb573108d7fee2f9ca755f3fcdf07aebcfc48833a37c5f4dfd4a58ccdb5aa body_fp=b5a7465162860080ad222b2b838a25cf4e99f115fe0ce96f2448977c846b8eee source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af -->
## `test_run_bootstrap_unbounded_processes_all(project: Path)`

Assert that `run_bootstrap` with no `budget_usd` and no `limit` syncs every file in the plan and skips none.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_cli_plan_makes_no_message_calls fingerprint=9d4cfe2a695823505ed77e7907401858b9d536e4525b17b195940e5c3ef894d6 body_fp=6e93932c50308d25697766f1161e23d8d4155dfa92cbc703779e5537a8996489 source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af -->
## `test_cli_plan_makes_no_message_calls(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie plan` exits successfully and never invokes the client's `generate` method.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_cli_plan_outside_project_errors fingerprint=68f003153534954db66fa1f239582223794f2233a90e3e18933617e113148631 body_fp=7fef420ff4f52812715e828e528b0d42e76b0e3b7ca8618dc6f6cbed07b33b57 source_ref=04a669302ff19f1e43c1d31e0f7c26035a7a0f63 -->
## `test_cli_plan_outside_project_errors(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert `trie plan` exits with code 1 and never constructs a client when no `trie.toml` is found.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_cli_first_run_sync_requires_budget_or_limit_non_interactive fingerprint=3203da00447e4dae9e3392907d2eca1f2e8fdc283d4b487d4ed4c7621a8170c4 body_fp=e065127e3f3ef9b4c35600b05a07433974426774de4e18e508315ac1ec152c91 source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af -->
## `test_cli_first_run_sync_requires_budget_or_limit_non_interactive(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync` on a fresh project without `--budget` or `--limit` exits with code 1.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_cli_first_run_sync_with_limit_succeeds fingerprint=30d5fb7b4638eff469fb867a0a6db79c186dd48a7ec39ae4494b6285d7f29e96 body_fp=21fc0fe3008993ebd7e8024db88f12c5d947f7f684d32980e624fe82a1779218 source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af -->
## `test_cli_first_run_sync_with_limit_succeeds(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync --limit 1` exits successfully on a fresh project with no existing triefacts.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_cli_sync_all_forces_full_pass fingerprint=0d485ec94b24e3e505dc72552b946b9c9ae455c9a7cff4f2fd43ff056f9ce848 body_fp=9e4d2c837fc8fdef9face73cbbcde96bb10b8ac1b2244f3453b577baf40f1ac0 source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af -->
## `test_cli_sync_all_forces_full_pass(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verify that `trie sync --all` triggers the full bootstrap path even when triefacts already exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_cli_sync_rejects_file_and_all_together fingerprint=01e55c9bfae3ee3f4a73b7419afbdbbac4c84a28c5e67be6c163ed78e93b93ec body_fp=49e51cb23ebd5ca9f608527d79f608883957b2635fb14da74cd9e09532e97e5a source_ref=04a669302ff19f1e43c1d31e0f7c26035a7a0f63 -->
## `test_cli_sync_rejects_file_and_all_together(project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync --file <path> --all` exits with code 1 and reports mutual exclusivity.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_cli_sync_with_no_config_errors fingerprint=cd5d41cc3092e94d8b52e820f690b72a42c756589e877899f50dba42c729deff body_fp=fc8bce5d88b93b46c9889a3130e4cdf84995ecc18ab82bf634bca7a5be4e9483 source_ref=04a669302ff19f1e43c1d31e0f7c26035a7a0f63 -->
## `test_cli_sync_with_no_config_errors(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that `trie sync` in a directory without `trie.toml` exits with code 1 and mentions `trie.toml` in output.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_run_bootstrap_invokes_progress_callback fingerprint=1f93d29683e957631e6cb7cb511d4c724d6e4363b4b53c22948fc6e41deb0edd body_fp=deca56c65e29c629e6d527173ccabb56df169f481146c005b1a86e17e60bbcac source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af -->
## `test_run_bootstrap_invokes_progress_callback(project: Path)`

Verify that `run_bootstrap` calls `on_start`/`on_done` for each processed file and `on_skip` with `"limit reached"` for files cut by the `limit` cap.
<!-- trie:end -->