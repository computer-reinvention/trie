---
trie_version: 0.3.0
source: tests/test_bootstrap.py
file_fingerprint: 2a28fdd6921642cebe5f76ec6a76802fcc99f3f3e03db137209908c06e9e16a6
last_synced_at: '2026-07-25T01:37:04Z'
defines:
- kind: module
  qualified_name: tests/test_bootstrap:__module__
  lines: 1-453
- kind: function
  qualified_name: tests/test_bootstrap:project
  lines: 18-34
  signature: 'def project(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_bootstrap:_scanned_store
  lines: 37-41
  signature: 'def _scanned_store(project: Path) -> Store'
- kind: function
  qualified_name: tests/test_bootstrap:test_plan_ranks_higher_score_first
  lines: 44-63
  signature: 'def test_plan_ranks_higher_score_first(project: Path)'
- kind: function
  qualified_name: tests/test_bootstrap:test_plan_excludes_files_with_no_documentable_symbols
  lines: 66-107
  signature: 'def test_plan_excludes_files_with_no_documentable_symbols(project: Path, tmp_path: Path)'
- kind: function
  qualified_name: tests/test_bootstrap:test_plan_with_unknown_model_zero_cost
  lines: 110-125
  signature: 'def test_plan_with_unknown_model_zero_cost(project: Path)'
- kind: function
  qualified_name: tests/test_bootstrap:test_plan_only_files_restricts_worklist
  lines: 128-146
  signature: 'def test_plan_only_files_restricts_worklist(project: Path)'
- kind: function
  qualified_name: tests/test_bootstrap:test_plan_only_files_empty_yields_empty_plan
  lines: 149-165
  signature: 'def test_plan_only_files_empty_yields_empty_plan(project: Path)'
- kind: function
  qualified_name: tests/test_bootstrap:test_run_bootstrap_respects_limit
  lines: 168-201
  signature: 'def test_run_bootstrap_respects_limit(project: Path)'
- kind: function
  qualified_name: tests/test_bootstrap:test_run_bootstrap_respects_budget
  lines: 204-239
  signature: 'def test_run_bootstrap_respects_budget(project: Path)'
- kind: function
  qualified_name: tests/test_bootstrap:test_run_bootstrap_unbounded_processes_all
  lines: 242-275
  signature: 'def test_run_bootstrap_unbounded_processes_all(project: Path)'
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_plan_makes_no_message_calls
  lines: 278-293
  signature: 'def test_cli_plan_makes_no_message_calls(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_plan_outside_project_errors
  lines: 296-309
  signature: 'def test_cli_plan_outside_project_errors(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_first_run_sync_requires_budget_or_limit_non_interactive
  lines: 312-331
  signature: 'def test_cli_first_run_sync_requires_budget_or_limit_non_interactive( project: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_first_run_sync_with_limit_succeeds
  lines: 334-350
  signature: 'def test_cli_first_run_sync_with_limit_succeeds(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_sync_all_forces_full_pass
  lines: 353-374
  signature: 'def test_cli_sync_all_forces_full_pass(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_sync_rejects_file_and_all_together
  lines: 377-382
  signature: 'def test_cli_sync_rejects_file_and_all_together(project: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_bootstrap:test_cli_sync_with_no_config_errors
  lines: 385-391
  signature: 'def test_cli_sync_with_no_config_errors(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)'
- kind: function
  qualified_name: tests/test_bootstrap:test_run_bootstrap_invokes_progress_callback
  lines: 394-452
  signature: 'def test_run_bootstrap_invokes_progress_callback(project: Path)'
incoming_refs: 0
outgoing_refs: 49
---
<!-- trie:section symbol=tests/test_bootstrap:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=9cc35dd3b719aebe784f8157204a3e69eeffd00264ad9956539678c87278c390 source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af role=test-infrastructure -->
Tests for the bootstrap sync workflow, including plan building, execution limits, cost estimation, and CLI integration.

- `project` fixture creates a test project with small/medium/large Python files and trie.toml config
- `test_plan_ranks_higher_score_first` verifies files are prioritized by LOC * symbol count product
- `test_plan_excludes_files_with_no_documentable_symbols` confirms imports-only files are skipped
- `test_plan_with_unknown_model_zero_cost` handles unknown model pricing gracefully
- `test_plan_only_files_*` tests scope restriction for incremental updates
- `test_run_bootstrap_respects_*` validates budget and limit enforcement
- `test_cli_*` exercises command-line interface error handling and workflow detection
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:project fingerprint=d5b12d48473fa51307a94d93e57a02093f21289d05d6fad7419855f2579e4068 body_fp=b173f0879b8b54225f70fee65c40a856442d0ba724805c67e6c1caf55c278cf4 source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af role=test-infrastructure -->
## `def project(tmp_path: Path) -> Path`

Creates a temporary trie project with configuration file and three Python test files of varying sizes.

- Creates `trie.toml` with bootstrap model configuration and scope settings
- Creates `small.py` with 1 function, `medium.py` with 3 functions, `large.py` with 2 large functions
- Returns the temporary project root path for use in bootstrap planning tests
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:_scanned_store fingerprint=be2171d309873933c9dd828dece87833bd3c117974cc17e64314491077d352a8 body_fp=9bd512b5f23170d705a8120146f6380c282df7f3d8001e1591ae5e681bb37447 source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af role=test-infrastructure -->
## `def _scanned_store(project: Path) -> Store`

Creates a scanned Store instance for the test project with populated symbol data.

- Returns context manager that must be used with `with` statement
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_plan_ranks_higher_score_first fingerprint=40427304095c2846dbbff8a2f455aab1384b43952e2733e744132d43eefba518 body_fp=06eaf610f12ccb2d05e1fb543d3a3303e20c91d0bfdfb23a4aeebe0f1060ffee source_ref=982d1d0e9ae7e7ac2035a589831f5c3f674a6a13 role=test -->
## `def test_plan_ranks_higher_score_first(project: Path)`

Verifies that bootstrap plan orders files by descending score based on symbol count multiplied by lines of code.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_plan_excludes_files_with_no_documentable_symbols fingerprint=2e21e8749c7579b6c606c86a2a9988b1169322c0ee9f9422d76e47f4ee7b71c2 body_fp=d22f2f87500e74d64a4f27291c03f8d99bb0932f137063369710668fe954f709 source_ref=982d1d0e9ae7e7ac2035a589831f5c3f674a6a13 role=test -->
## `def test_plan_excludes_files_with_no_documentable_symbols(project: Path, tmp_path: Path)`

Tests that build_plan excludes files with no parser-surfaced symbols from documentation plans.

- Creates imports-only file (excluded), constants-only file (included), and private-function file (included)
- Verifies that only files with documentable symbols appear in the plan
- Confirms underscore-prefixed symbols are documented, imports-only files are skipped
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_plan_with_unknown_model_zero_cost fingerprint=4f3e6cae5f4d17263391af3c3ffbb57f366fa56666a272dd7bafd479a388c68e body_fp=e0765f615d9d68d963df14fa4274eaed68a1c9e8336500694b97470b3c52599f source_ref=982d1d0e9ae7e7ac2035a589831f5c3f674a6a13 role=test -->
## `def test_plan_with_unknown_model_zero_cost(project: Path)`

Tests that `build_plan` sets zero cost and unknown pricing for unrecognized model IDs.

- Uses "openai/some-model" which lacks pricing data in the system
- Verifies `plan.pricing_known` returns `False` and `total_estimated_cost` is `0.0`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_plan_only_files_restricts_worklist fingerprint=e321d8979a7335532ee65e02cd7ab534224347d76d55b2a11cc341ce5f022b59 body_fp=348788c6d072faa9fc1506571803233dc3ee90e1aacada357c34a5db95e7caa6 source_ref=982d1d0e9ae7e7ac2035a589831f5c3f674a6a13 role=test -->
## `def test_plan_only_files_restricts_worklist(project: Path)`

Tests that `build_plan` with `only_files` parameter restricts the plan to specified files only.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_plan_only_files_empty_yields_empty_plan fingerprint=7d6eb63549e31de9fdea6f9528084eda6ecd794da18fa169e9cf51865b8eb8ca body_fp=ddfe7e7221485864cc7010f3728352adb4d68c5407f7449fcd3db426103c6f00 source_ref=982d1d0e9ae7e7ac2035a589831f5c3f674a6a13 role=test -->
## `def test_plan_only_files_empty_yields_empty_plan(project: Path)`

Tests that `build_plan` returns an empty plan when `only_files` is an empty set.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_run_bootstrap_respects_limit fingerprint=70e8a39ca994df819ddab758a7970a484a4a829705884b7c8a1da2baba89db85 body_fp=6261d3e4dc34af4cd943ca53855903a006b70fc18c3324454e0349e7c6299cc1 source_ref=982d1d0e9ae7e7ac2035a589831f5c3f674a6a13 role=test -->
## `def test_run_bootstrap_respects_limit(project: Path)`

Verifies that `run_bootstrap` stops after processing the specified `limit` of files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_run_bootstrap_respects_budget fingerprint=6bc46da02f86461edf7e62e32814bfe6803a56c903f9dcec80cc0ec35c7c0d77 body_fp=feb98d00d9fb2725cc0381d9c84633ab4454e33d7223c5c40ae156416d27990a source_ref=982d1d0e9ae7e7ac2035a589831f5c3f674a6a13 role=test -->
## `def test_run_bootstrap_respects_budget(project: Path)`

Verifies that run_bootstrap stops processing files when the USD budget is exhausted.

- Sets tiny budget (0.0001 USD) to force early termination
- Validates files_synced is partial but at least 1
- Allows slight cost overshoot due to file-level granularity
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_run_bootstrap_unbounded_processes_all fingerprint=90ebb573108d7fee2f9ca755f3fcdf07aebcfc48833a37c5f4dfd4a58ccdb5aa body_fp=033a2c80f749e730bd14c4b5b0e70219af18fd34d509c5838db305cd8daa2864 source_ref=982d1d0e9ae7e7ac2035a589831f5c3f674a6a13 role=test -->
## `def test_run_bootstrap_unbounded_processes_all(project: Path)`

Verifies run_bootstrap processes all files when no budget or limit constraints are set.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_cli_plan_makes_no_message_calls fingerprint=9d4cfe2a695823505ed77e7907401858b9d536e4525b17b195940e5c3ef894d6 body_fp=7c2e439d75cef9752332a871869997bdfc3849b07a7f494dfceddc8220738f7a source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af role=test-infrastructure -->
## `def test_cli_plan_makes_no_message_calls(project: Path, monkeypatch: pytest.MonkeyPatch)`

Tests that `trie plan` CLI command calls no expensive LLM generate methods, only free token counting operations.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_cli_plan_outside_project_errors fingerprint=68f003153534954db66fa1f239582223794f2233a90e3e18933617e113148631 body_fp=acb5382338114ca0ca41eb6ed0f8ee3ed26e7c6ac521ad23680d45440216bf04 source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af role=test-infrastructure -->
## `def test_cli_plan_outside_project_errors(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Verifies that `trie plan` exits with error code 1 when run outside a project directory without trie.toml.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_cli_first_run_sync_requires_budget_or_limit_non_interactive fingerprint=3203da00447e4dae9e3392907d2eca1f2e8fdc283d4b487d4ed4c7621a8170c4 body_fp=0f6cb0e90510c53d9e357cbeaa728d3b8b82b580e63e4a93fe3be7c7a0f9b572 source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af role=cli-interface -->
## `def test_cli_first_run_sync_requires_budget_or_limit_non_interactive( project: Path, monkeypatch: pytest.MonkeyPatch )`

Tests that `trie sync` on fresh projects requires --budget or --limit flags to prevent surprise costs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_cli_first_run_sync_with_limit_succeeds fingerprint=30d5fb7b4638eff469fb867a0a6db79c186dd48a7ec39ae4494b6285d7f29e96 body_fp=60e5960af8024924ab7cca9b1cf909a81a8cde8cf6f75cb83ef78c360ca1864f source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af role=test-infrastructure -->
## `def test_cli_first_run_sync_with_limit_succeeds(project: Path, monkeypatch: pytest.MonkeyPatch)`

Tests that first-run bootstrap succeeds when --limit is provided to cap file processing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_cli_sync_all_forces_full_pass fingerprint=0d485ec94b24e3e505dc72552b946b9c9ae455c9a7cff4f2fd43ff056f9ce848 body_fp=54667e1c3aa2afd8157d367b2e05406e610daaea3e8796c19e02016cca0ffdc6 source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af role=test-infrastructure -->
## `def test_cli_sync_all_forces_full_pass(project: Path, monkeypatch: pytest.MonkeyPatch)`

Tests that `trie sync --all` forces bootstrap mode even when triefacts exist, overriding incremental sync detection.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_cli_sync_rejects_file_and_all_together fingerprint=01e55c9bfae3ee3f4a73b7419afbdbbac4c84a28c5e67be6c163ed78e93b93ec body_fp=79894b8892ec4149f3ed566b00ef6bba0cc611a04ba01c28f8195ee7cbc3df86 source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af role=test-infrastructure -->
## `def test_cli_sync_rejects_file_and_all_together(project: Path, monkeypatch: pytest.MonkeyPatch)`

Verifies that `trie sync` rejects the mutually exclusive `--file` and `--all` flags.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_cli_sync_with_no_config_errors fingerprint=cd5d41cc3092e94d8b52e820f690b72a42c756589e877899f50dba42c729deff body_fp=a0b0bb01a1975f818134d1178923914b7762bfaa13c48b2c5e2d5b8a48a50dee source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af role=test-infrastructure -->
## `def test_cli_sync_with_no_config_errors(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)`

Verifies that `trie sync` without a trie.toml configuration file exits with error code 1.

- Confirms error message mentions "trie.toml"
<!-- trie:end -->
<!-- trie:section symbol=tests/test_bootstrap:test_run_bootstrap_invokes_progress_callback fingerprint=05e290fe30d0101df97f3f76be757c1e106eda23bf0e80e1614a07511d3521fb body_fp=9cea69fb307fdcd950adec110e21ea1beb154539d180db9832321b9448a2ded9 source_ref=982d1d0e9ae7e7ac2035a589831f5c3f674a6a13 role=test -->
## `def test_run_bootstrap_invokes_progress_callback(project: Path)`

Verifies run_bootstrap correctly calls progress callback methods for processed and skipped files.

- Uses custom Recorder class to capture on_start, on_done, and on_skip callback invocations
- Processes 2 files with limit=2, expects remaining files to be skipped with "limit reached" reason
- Validates callback counts and parameters match expected bootstrap execution flow
<!-- trie:end -->