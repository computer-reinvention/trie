---
trie_version: 0.1.5
source: tests/test_scheduler.py
file_fingerprint: 996cffc379cbf2b09d756831e8d699e44934bb777172329c9ad78b324ae69fe6
last_synced_at: '2026-06-06T13:43:35Z'
description: Tests for the wave-based file scheduler (trie/sync/scheduler.py).
defines:
- kind: module
  qualified_name: tests/test_scheduler:__module__
  lines: 1-162
- kind: function
  qualified_name: tests/test_scheduler:_result
  lines: 13-23
- kind: function
  qualified_name: tests/test_scheduler:test_unbounded_run_processes_all_files
  lines: 26-31
- kind: function
  qualified_name: tests/test_scheduler:test_files_actually_run_in_parallel
  lines: 34-52
- kind: function
  qualified_name: tests/test_scheduler:test_none_result_counts_as_skip
  lines: 55-63
- kind: function
  qualified_name: tests/test_scheduler:test_exception_in_one_file_does_not_sink_wave
  lines: 66-75
- kind: function
  qualified_name: tests/test_scheduler:test_limit_caps_and_reports_skips
  lines: 78-97
- kind: function
  qualified_name: tests/test_scheduler:test_budget_caps_run
  lines: 100-110
- kind: function
  qualified_name: tests/test_scheduler:test_depth_banded_ordering_band0_before_band1
  lines: 113-133
- kind: function
  qualified_name: tests/test_scheduler:test_global_inflight_semaphore_caps_concurrency
  lines: 136-161
incoming_refs: 0
outgoing_refs: 18
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
<!-- trie:section symbol=tests/test_scheduler:_result fingerprint=89f80e8e00dcf9a76d0fa92151f1f4ff417c496ac55f25033392f78559088950 body_fp=099db3d388016955af7988368e55adce9d1e87d10b20ba903202f1cf77471f8c source_ref=49d06a80c655d6743830a8fe1d3623699c10a995 role=test -->
Creates a mock `FileSyncResult` with fixed token counts and paths derived from the given relative path.

- `rel`: relative file path used to construct source and triefact paths
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scheduler:test_unbounded_run_processes_all_files fingerprint=b871992e406fb67bac54cbd5c141c46937cc30c7a958dcca13c0a37dd3c1c03f body_fp=1c44992e4a7154f8a047868f75711d6f8ed7d2b846c5d6d095163889e38639a6 source_ref=49d06a80c655d6743830a8fe1d3623699c10a995 role=test -->
Verifies that run_waves processes all tasks when no limits are applied.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scheduler:test_files_actually_run_in_parallel fingerprint=c00a235372651b34fd99d1669e4854e75d789e53cb4671a474bc42ed17a06583 body_fp=d9e9638a2ed6aad5cfe92f0391d32981f50a3b2063bd33d6ae246d6d758bb805 source_ref=49d06a80c655d6743830a8fe1d3623699c10a995 role=test -->
Verifies that `run_waves` actually executes file processing tasks in parallel with multiple workers.

- Uses thread-safe counters to track maximum concurrent task execution
- Introduces artificial delay via `time.sleep(0.02)` to ensure overlap detection
- Asserts at least 2 tasks run concurrently when `file_workers=4`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scheduler:test_none_result_counts_as_skip fingerprint=8834bf3bc0f18a1776ebdb715c86f5cba189c8921f243fa1d06d009714bf34e2 body_fp=3262f0b67d061d0e51352f9c1ef778451c7c49275f739c6f8b62e1bdac9c1535 source_ref=49d06a80c655d6743830a8fe1d3623699c10a995 role=test -->
Verifies that when `process_file` returns `None` for a task, the scheduler counts it as a skip rather than a result.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scheduler:test_exception_in_one_file_does_not_sink_wave fingerprint=e9d1ea60163d3d68ff7ffecbd6d8bc4d63af16f9ec0e238fe46a8d90f17f7a44 body_fp=5f7a3b24c133623f4d4c727b7252aab30d48bd88d13ec0bb3357de758ee0763c source_ref=49d06a80c655d6743830a8fe1d3623699c10a995 role=test -->
Verifies that run_waves continues processing remaining files when one file raises an exception during processing.

- Creates three tasks where the middle one throws RuntimeError
- Asserts two successful results and one skip counted
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scheduler:test_limit_caps_and_reports_skips fingerprint=55776da5871d6bc11e8adf3417d86de532d304aab694935e8c85b62275c12397 body_fp=d6abcec11c618bc2e6dcabe24b306b013b7a4f2f1363cdc42fcd3e7797cf6ef8 source_ref=49d06a80c655d6743830a8fe1d3623699c10a995 role=test -->
Verifies that run_waves respects the limit parameter and correctly reports skip reasons.

- Creates 5 tasks but sets limit=2 to process only 2 files
- Uses progress callback to capture skip reasons
- Confirms 3 files are skipped with "limit reached" reason
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scheduler:test_budget_caps_run fingerprint=9195ae4d2271a335d0cf51e8698b2b892f666a628fea04d2b00bd7917bfb1a96 body_fp=d9663d31aa8ae76deec465c6dfff930eebeae94e34b0e67d60d77beb5055b9b5 source_ref=49d06a80c655d6743830a8fe1d3623699c10a995 role=test -->
Tests that run_waves stops processing files when budget limit is exceeded and reports skipped count correctly.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scheduler:test_depth_banded_ordering_band0_before_band1 fingerprint=188b7355e75ff9c114a88db424d8c410bd587bfdba3124b333363833fe5222b0 body_fp=4f8d1d3ebdc488ea7fa06471fca8f5d330659d1247cc0bd523de61e928889015 source_ref=49d06a80c655d6743830a8fe1d3623699c10a995 role=test -->
Tests that run_waves processes tasks in hop-based waves, completing all hop-0 files before starting hop-1 files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_scheduler:test_global_inflight_semaphore_caps_concurrency fingerprint=bbc8853c4d1ade6dea9d414693db4a674786a49819917e418fa7a3ed8a38c3c9 body_fp=ac6eb49950b375f13978b0a12d8f4502b14d2965c01c7bb0a34a473f96acf481 source_ref=49d06a80c655d6743830a8fe1d3623699c10a995 role=test -->
Tests that the global inflight semaphore correctly limits concurrent holders to the configured maximum.
<!-- trie:end -->