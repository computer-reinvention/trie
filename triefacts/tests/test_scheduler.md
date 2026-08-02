---
trie_version: 0.3.0
source: tests/test_scheduler.py
file_fingerprint: 3901e6f9692033cf9b9caef42545c389dc13594086a02657233d1c0450fc2ee9
last_synced_at: '2026-08-02T21:19:27Z'
description: Tests for the wave-based file scheduler (trie/sync/scheduler.py).
defines:
- kind: module
  qualified_name: tests/test_scheduler:__module__
  lines: 1-181
- kind: function
  qualified_name: tests/test_scheduler:_result
  lines: 13-23
  signature: 'def _result(rel: str) -> FileSyncResult'
- kind: function
  qualified_name: tests/test_scheduler:test_unbounded_run_processes_all_files
  lines: 26-31
  signature: def test_unbounded_run_processes_all_files()
- kind: function
  qualified_name: tests/test_scheduler:test_files_actually_run_in_parallel
  lines: 34-52
  signature: def test_files_actually_run_in_parallel()
- kind: function
  qualified_name: tests/test_scheduler:test_none_result_counts_as_skip
  lines: 55-63
  signature: def test_none_result_counts_as_skip()
- kind: function
  qualified_name: tests/test_scheduler:test_exception_in_one_file_does_not_sink_wave
  lines: 66-78
  signature: def test_exception_in_one_file_does_not_sink_wave()
- kind: function
  qualified_name: tests/test_scheduler:test_all_files_erroring_is_not_a_silent_success
  lines: 81-94
  signature: def test_all_files_erroring_is_not_a_silent_success()
- kind: function
  qualified_name: tests/test_scheduler:test_limit_caps_and_reports_skips
  lines: 97-116
  signature: def test_limit_caps_and_reports_skips()
- kind: function
  qualified_name: tests/test_scheduler:test_budget_caps_run
  lines: 119-129
  signature: def test_budget_caps_run()
- kind: function
  qualified_name: tests/test_scheduler:test_depth_banded_ordering_band0_before_band1
  lines: 132-152
  signature: def test_depth_banded_ordering_band0_before_band1()
- kind: function
  qualified_name: tests/test_scheduler:test_global_inflight_semaphore_caps_concurrency
  lines: 155-180
  signature: def test_global_inflight_semaphore_caps_concurrency()
incoming_refs: 0
outgoing_refs: 23
---
<!-- trie:section symbol=tests/test_scheduler:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=a55feab9fddb09dc00f6570ef7eae5f4addd2d1e6a0580ef7dfc0d4162c7e964 source_ref=49d06a80c655d6743830a8fe1d3623699c10a995 role=test -->
Tests for the wave-based file scheduler functionality in `trie.sync.scheduler`.

- `_result()`: Creates a mock `FileSyncResult` for testing with standard token counts
- `test_unbounded_run_processes_all_files()`: Verifies all tasks complete when no limits are set
- `test_files_actually_run_in_parallel()`: Confirms genuine parallelism with multiple workers
- `test_none_result_counts_as_skip()`: Tests that None returns are counted as skips
- `test_exception_in_one_file_does_not_sink_wave()`: Ensures exceptions in one file don't stop others
- `test_limit_caps_and_reports_skips()`: Validates file count limiting and skip reporting
- `test_budget_caps_run()`: Tests USD budget enforcement stops execution when exceeded
- `test_depth_banded_ordering_band0_before_band1()`: Verifies hop-0 files complete before hop-1 files start
- `test_global_inflight_semaphore_caps_concurrency()`: Tests global concurrency limiting via semaphore
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scheduler:_result fingerprint=89f80e8e00dcf9a76d0fa92151f1f4ff417c496ac55f25033392f78559088950 body_fp=0c7c65f4b795fc3e6bfd097aa7a60d0a9d28e2d8323996f9d797e6f78ac88193 source_ref=305d54f16a70c75809170cdbff2cb12756d99675 role=test -->
## `def _result(rel: str) -> FileSyncResult`

Creates a FileSyncResult with fixed test values for the given relative path.

- `rel`: relative file path to use for source_path basename
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scheduler:test_unbounded_run_processes_all_files fingerprint=b871992e406fb67bac54cbd5c141c46937cc30c7a958dcca13c0a37dd3c1c03f body_fp=adef07fd32f454b304f75d60f4f80f6391f67956ad0c2d0305cb3e220e126ee0 source_ref=2d0a6dfc259f5e05467859318304860c4dd2bbc5 role=test -->
## `def test_unbounded_run_processes_all_files()`

Verifies that `run_waves` processes all tasks when no limits are imposed.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scheduler:test_files_actually_run_in_parallel fingerprint=c00a235372651b34fd99d1669e4854e75d789e53cb4671a474bc42ed17a06583 body_fp=081aa8810d924e19b7b998187233f256b4a5cb81f2fedd3daf7772b16e15d886 source_ref=305d54f16a70c75809170cdbff2cb12756d99675 role=test -->
## `def test_files_actually_run_in_parallel()`

Verifies that `run_waves` executes file processing tasks in parallel using multiple worker threads.

- Uses a mock processor that tracks concurrent execution count via threading lock
- Asserts at least 2 tasks ran simultaneously to confirm genuine parallelism
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scheduler:test_none_result_counts_as_skip fingerprint=8834bf3bc0f18a1776ebdb715c86f5cba189c8921f243fa1d06d009714bf34e2 body_fp=14047af9bd100d036b256eea0028caa132eb5d11728660b348cb8c9458c99dde source_ref=2d0a6dfc259f5e05467859318304860c4dd2bbc5 role=test -->
## `def test_none_result_counts_as_skip()`

Tests that files returning None from process_file are counted as skipped rather than processed.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scheduler:test_exception_in_one_file_does_not_sink_wave fingerprint=397d99f38378f6a4911f73206fa077712b9996de4929b29ea1dc56024692eb25 body_fp=742e759d8e0365bd8036623343c041428467a12ef74febb29d1781ad2aa4857d source_ref=305d54f16a70c75809170cdbff2cb12756d99675 role=test -->
## `def test_exception_in_one_file_does_not_sink_wave()`

Verifies that `run_waves` continues processing other tasks when one task's processor function raises an exception.

- Creates three tasks where the middle one triggers a RuntimeError
- Confirms two successful results are recorded, the error is stored in `sched.errors`, and `skipped_other` remains 0
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scheduler:test_all_files_erroring_is_not_a_silent_success fingerprint=9582e4bde37e1b76e988f328d43744e474f8d9def63f50c752fdafc71ebc1730 body_fp=f878ea919caa33649f817205e8a30ef9977afc0c40b2a20e77775b7571aaa1e4 source_ref=305d54f16a70c75809170cdbff2cb12756d99675 role=test -->
## `def test_all_files_erroring_is_not_a_silent_success()`

Regression test asserting that all-file errors populate `errors`, not `skipped_other`, so callers cannot silently interpret a total failure as "nothing to do".
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scheduler:test_limit_caps_and_reports_skips fingerprint=e24eaabaf0a2811872cadfa157bb69f7e1ff97cbc74e4910af35bcd1be867741 body_fp=84fd87354320a1006ac3eaa9fe6fe226ce1a51183f67152fa1d45afba2c39c85 source_ref=2d0a6dfc259f5e05467859318304860c4dd2bbc5 role=test -->
## `def test_limit_caps_and_reports_skips()`

Tests that run_waves respects file limit and reports skip reasons via progress callback.

- Creates 5 tasks but limits execution to 2 files
- Verifies 3 files are skipped with "limit reached" reason
- Uses custom progress recorder to capture skip notifications
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scheduler:test_budget_caps_run fingerprint=9195ae4d2271a335d0cf51e8698b2b892f666a628fea04d2b00bd7917bfb1a96 body_fp=fb6c16ec2e8c51e9c45b9dbd35f6969d48ebb9d9bd95379dce1242889e144ff6 source_ref=2d0a6dfc259f5e05467859318304860c4dd2bbc5 role=test -->
## `def test_budget_caps_run()`

Tests that run_waves stops processing files when budget is exceeded after first file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scheduler:test_depth_banded_ordering_band0_before_band1 fingerprint=188b7355e75ff9c114a88db424d8c410bd587bfdba3124b333363833fe5222b0 body_fp=802fdf1b7f2e8fdf700845e41d543eaa5f247f4fa489f700cbb2c96b356a5529 source_ref=305d54f16a70c75809170cdbff2cb12756d99675 role=test -->
## `def test_depth_banded_ordering_band0_before_band1()`

Tests that `run_waves` processes hop-0 files completely before starting any hop-1 files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scheduler:test_global_inflight_semaphore_caps_concurrency fingerprint=bbc8853c4d1ade6dea9d414693db4a674786a49819917e418fa7a3ed8a38c3c9 body_fp=280172ed391cd2e6f13c9f9ceff23a4131c3dc7a2d77fc40f57633f214e01a75 source_ref=305d54f16a70c75809170cdbff2cb12756d99675 role=test -->
## `def test_global_inflight_semaphore_caps_concurrency()`

Verify that `configure_inflight_limit(2)` prevents more than 2 threads from holding `_inflight_slot` concurrently across 8 competing threads.
<!-- trie:end -->