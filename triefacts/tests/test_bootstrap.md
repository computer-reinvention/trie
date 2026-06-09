---
trie_version: 0.1.5
source: tests/test_bootstrap.py
file_fingerprint: e41001506f52f7ceea533071df38f0121ff20078c519ed1189d3f8fd3ea3489b
last_synced_at: '2026-06-06T13:44:20Z'
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

<!-- trie:section symbol=tests/test_bootstrap:project fingerprint=d5b12d48473fa51307a94d93e57a02093f21289d05d6fad7419855f2579e4068 body_fp=654b8ea7776bd57e3306adda677beffb1d8c545299f2faca1ee06ee3ff77e20a source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af role=test-infrastructure -->
Creates a temporary trie project with configuration file and three Python test files of varying sizes.

- Creates `trie.toml` with bootstrap model configuration and scope settings
- Creates `small.py` with 1 function, `medium.py` with 3 functions, `large.py` with 2 large functions
- Returns the temporary project root path for use in bootstrap planning tests
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:_scanned_store fingerprint=be2171d309873933c9dd828dece87833bd3c117974cc17e64314491077d352a8 body_fp=51ff4987cfb01ecd9e37818a9abed600a1881b89fad3f9a8789916abced328b8 source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af role=test-infrastructure -->
Creates a scanned Store instance for the test project with populated symbol data.

- Returns context manager that must be used with `with` statement
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_plan_ranks_higher_score_first fingerprint=40427304095c2846dbbff8a2f455aab1384b43952e2733e744132d43eefba518 body_fp=716949baaeeb3aa197ee23c1c16127d83273db0363e31020ac67a0b2214133bb source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af role=test-infrastructure -->
Verifies that bootstrap plan orders files by descending score based on symbol count multiplied by lines of code.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_plan_excludes_files_with_no_documentable_symbols fingerprint=2e21e8749c7579b6c606c86a2a9988b1169322c0ee9f9422d76e47f4ee7b71c2 body_fp=f0611423f84aaaa9efc32a2a69dea83454d79d204afde6206b4645f8eb7d2d9a source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af role=test-infrastructure -->
Tests that build_plan excludes files with no parser-surfaced symbols from documentation plans.

- Creates imports-only file (excluded), constants-only file (included), and private-function file (included)
- Verifies that only files with documentable symbols appear in the plan
- Confirms underscore-prefixed symbols are documented, imports-only files are skipped
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_plan_with_unknown_model_zero_cost fingerprint=4f3e6cae5f4d17263391af3c3ffbb57f366fa56666a272dd7bafd479a388c68e body_fp=63b6cff0dd4022f02f96c59c2816206a4bafa1edbdcf572818f942a398ed72d4 source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af role=test-infrastructure -->
Tests that `build_plan` sets zero cost and unknown pricing for unrecognized model IDs.

- Uses "openai/some-model" which lacks pricing data in the system
- Verifies `plan.pricing_known` returns `False` and `total_estimated_cost` is `0.0`
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_plan_only_files_restricts_worklist fingerprint=e321d8979a7335532ee65e02cd7ab534224347d76d55b2a11cc341ce5f022b59 body_fp=9c0a91fa1bc3eee247dcfbeb9a54534f1674e69d1d0530d5cfc6b5432adb3b7d source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af role=test-infrastructure -->
Tests that `build_plan` with `only_files` parameter restricts the plan to specified files only.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_plan_only_files_empty_yields_empty_plan fingerprint=7d6eb63549e31de9fdea6f9528084eda6ecd794da18fa169e9cf51865b8eb8ca body_fp=b87d23e9918c1d54e5975c321d31ca5f44bde18f7bac46114152eeb437f34a96 source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af role=documentation-sync -->
Tests that `build_plan` returns an empty plan when `only_files` is an empty set.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_run_bootstrap_respects_limit fingerprint=70e8a39ca994df819ddab758a7970a484a4a829705884b7c8a1da2baba89db85 body_fp=547539a47d5d8c2ffefb57ea6031539cd5717b7e1ca788d518a5642383b0f6a3 source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af role=test-infrastructure -->
Verifies that `run_bootstrap` stops after processing the specified `limit` of files.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_run_bootstrap_respects_budget fingerprint=6bc46da02f86461edf7e62e32814bfe6803a56c903f9dcec80cc0ec35c7c0d77 body_fp=c5092c97cfe540b18598a6fb4cbecb90be6467e4051cad25455039aa9ffbcae7 source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af role=test-infrastructure -->
Verifies that run_bootstrap stops processing files when the USD budget is exhausted.

- Sets tiny budget (0.0001 USD) to force early termination
- Validates files_synced is partial but at least 1
- Allows slight cost overshoot due to file-level granularity
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_run_bootstrap_unbounded_processes_all fingerprint=90ebb573108d7fee2f9ca755f3fcdf07aebcfc48833a37c5f4dfd4a58ccdb5aa body_fp=69b37a0c0d01a4e770a110329a2f10e0293162eb507953bdbac6a57039570de8 source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af role=test-infrastructure -->
Verifies run_bootstrap processes all files when no budget or limit constraints are set.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_cli_plan_makes_no_message_calls fingerprint=9d4cfe2a695823505ed77e7907401858b9d536e4525b17b195940e5c3ef894d6 body_fp=45a975f1212f0a9248d5d726e73ff6ab6df98ea2b216acd4a03609785d10c91c source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af role=test-infrastructure -->
Tests that `trie plan` CLI command calls no expensive LLM generate methods, only free token counting operations.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_cli_plan_outside_project_errors fingerprint=68f003153534954db66fa1f239582223794f2233a90e3e18933617e113148631 body_fp=573a1b260d02eee87a2f9ae95e8c5aa31c9b3bca26132fc2a88c7f4fff74aaf5 source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af role=test-infrastructure -->
Verifies that `trie plan` exits with error code 1 when run outside a project directory without trie.toml.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_cli_first_run_sync_requires_budget_or_limit_non_interactive fingerprint=3203da00447e4dae9e3392907d2eca1f2e8fdc283d4b487d4ed4c7621a8170c4 body_fp=bc7049d851624e0052dc9d12b2052f7987cb497cf9428618c7d815b0cfa4eb9d source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af role=cli-interface -->
Tests that `trie sync` on fresh projects requires --budget or --limit flags to prevent surprise costs.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_cli_first_run_sync_with_limit_succeeds fingerprint=30d5fb7b4638eff469fb867a0a6db79c186dd48a7ec39ae4494b6285d7f29e96 body_fp=5673dd4ed744a7cbaa533afba4240d6e0032fc8e3b167b2ae6034a9a0c7b38f2 source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af role=test-infrastructure -->
Tests that first-run bootstrap succeeds when --limit is provided to cap file processing.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_cli_sync_all_forces_full_pass fingerprint=0d485ec94b24e3e505dc72552b946b9c9ae455c9a7cff4f2fd43ff056f9ce848 body_fp=2c0dcc1657e05da003e6ccf0624ed94465fdbb7ec5ea5c6a2798288340792713 source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af role=test-infrastructure -->
Tests that `trie sync --all` forces bootstrap mode even when triefacts exist, overriding incremental sync detection.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_cli_sync_rejects_file_and_all_together fingerprint=01e55c9bfae3ee3f4a73b7419afbdbbac4c84a28c5e67be6c163ed78e93b93ec body_fp=d722a5b142b9ec38d4f31540509953b673cbfc020aaf7d244ca4b67c613b3bf3 source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af role=test-infrastructure -->
Verifies that `trie sync` rejects the mutually exclusive `--file` and `--all` flags.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_cli_sync_with_no_config_errors fingerprint=cd5d41cc3092e94d8b52e820f690b72a42c756589e877899f50dba42c729deff body_fp=9c1794a075985d0294c34463c95f3809a7d1e903df3e4b00117dc77a04efc0d3 source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af role=test-infrastructure -->
Verifies that `trie sync` without a trie.toml configuration file exits with error code 1.

- Confirms error message mentions "trie.toml"
<!-- trie:end -->

<!-- trie:section symbol=tests/test_bootstrap:test_run_bootstrap_invokes_progress_callback fingerprint=1f93d29683e957631e6cb7cb511d4c724d6e4363b4b53c22948fc6e41deb0edd body_fp=4e20e619152656f5021ee0ef2033bb471048c464f273d10f3f018f9c2d9faade source_ref=1f9bf5173245eaa144dd62b7047e435686fee5af role=test-infrastructure -->
Verifies run_bootstrap correctly calls progress callback methods for processed and skipped files.

- Uses custom Recorder class to capture on_start, on_done, and on_skip callback invocations
- Processes 2 files with limit=2, expects remaining files to be skipped with "limit reached" reason
- Validates callback counts and parameters match expected bootstrap execution flow
<!-- trie:end -->
