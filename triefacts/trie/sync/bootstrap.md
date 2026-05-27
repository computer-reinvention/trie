---
trie_version: 0.1.2
source: trie/sync/bootstrap.py
file_fingerprint: c0f4f174435148e121708503ba60c8afc867ea101708bae16e1d220cc1fe5ade
last_synced_at: '2026-05-24T00:25:20Z'
defines:
- kind: module
  qualified_name: trie/sync/bootstrap:__module__
  lines: 1-206
- kind: class
  qualified_name: trie/sync/bootstrap:PlanItem
  lines: 23-27
- kind: class
  qualified_name: trie/sync/bootstrap:BootstrapPlan
  lines: 31-34
- kind: class
  qualified_name: trie/sync/bootstrap:BootstrapResult
  lines: 38-43
- kind: function
  qualified_name: trie/sync/bootstrap:build_plan
  lines: 46-133
- kind: function
  qualified_name: trie/sync/bootstrap:run_bootstrap
  lines: 136-205
incoming_refs: 16
outgoing_refs: 14
---
<!-- trie:section symbol=trie/sync/bootstrap:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=2c44ad2129410e5f78f3ce0090cea7f8ed4f87735d12047f806bab3d04a258b8 source_ref=6fa7f487ae550d9e0cbd13df58df2357ddc4b78a -->
## `trie/sync/bootstrap`

Plan and execute bulk documentation generation across all files in a project.

- `build_plan`: ranks files and estimates costs before any LLM calls
- `run_bootstrap`: executes the ranked worklist respecting budget and file limits
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/bootstrap:PlanItem fingerprint=3ad4199e6663a1036afc1e755b38c0280155f590812857853ea08cca37b49294 body_fp=d96e8ac21c296d622fc3939e61541233cc83fc8de23b57dc5c96b82fc1bb6963 source_ref=6fa7f487ae550d9e0cbd13df58df2357ddc4b78a -->
## `PlanItem`

Immutable record representing one file's entry in a bootstrap plan.

- `file_path`: source-root-relative path string
- `score`: `LOC × public_symbols`, used for ranking
- `estimated`: per-file token and cost breakdown
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/bootstrap:BootstrapPlan fingerprint=4aaf47574b31c065099c6ea2ffd0ebc1af1247d496cb0f5d7affc57237016198 body_fp=d2a43a23c06a2916603c26b846f882186f58f9fc844be7114860c0b6f8c19e87 source_ref=6fa7f487ae550d9e0cbd13df58df2357ddc4b78a -->
## `BootstrapPlan`

Immutable result of `build_plan` holding a ranked worklist and aggregate cost estimate.

- `pricing_known`: `False` when the model has no registered pricing; costs will be zero.
- `total_estimated_cost`: sum of all `PlanItem.estimated.cost_usd` values.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/bootstrap:BootstrapResult fingerprint=3f3fd17f4bf3bb39691a228e43cfd2570d8f5faf3fec4a81808e46a8a00268f5 body_fp=ae9918e8aa339ba87fb99d19a09ca7aa6fd3ec23e556ef1d8ebe75c86a492bad source_ref=6fa7f487ae550d9e0cbd13df58df2357ddc4b78a -->
## `BootstrapResult`

Immutable record of a completed bootstrap run's outcomes and costs.

- `files_skipped_no_budget`: count of files skipped due to budget or limit.
- `sync_results`: per-file `FileSyncResult` for every file that was processed.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/bootstrap:build_plan fingerprint=cb58508dbf1731b80ba6987d1ed9b9c6985a068b30e6e48d9d4e1fa52e119e1f body_fp=776e6e17885155b77cf27de186537e100a45a261d4d3d227982a26b1dcbd3885 source_ref=6fa7f487ae550d9e0cbd13df58df2357ddc4b78a -->
## `build_plan(*, project_root, store, model_id, client, only_files=None, regen_count_by_file=None) -> BootstrapPlan`

Rank store files by `LOC × public_symbol_count` and produce per-file LLM cost estimates.

- `only_files`: restrict plan to these source-relative paths; absent files are silently skipped.
- `regen_count_by_file`: scale cost estimates to only the symbols that will hit the LLM; missing key means regen all.
- `PlanItem.public_symbols`: always the file's total documented symbols, not the regen target.
- Cost estimates use `client.count_tokens` (Anthropic API) when pricing is available; zero-filled otherwise.
- `BootstrapPlan.pricing_known`: false when no pricing data exists for `model_id`.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/bootstrap:run_bootstrap fingerprint=2c937a218d06abcc2c1e95a2902e01bf7fe41c2028ce38edb61c84e611636b2f body_fp=2ab1ab6b3851c9b4ad0606083cea40339bf3923c8f8bb99f96a65edb8c2d4450 source_ref=6fa7f487ae550d9e0cbd13df58df2357ddc4b78a -->
## `run_bootstrap(*, plan, project_root, config, client, pricing, budget_usd, limit, progress=None, store=None) -> BootstrapResult`

Execute a `BootstrapPlan` worklist, stopping when the file limit or USD budget is exhausted.

- `budget_usd`: cost ceiling checked *after* each file; run may overshoot by one file's cost.
- `limit`: max number of files synced; remaining items are skipped and counted.
- `pricing`: when `None`, actual cost is not tracked and `actual_cost_usd` returns `0.0`.
- `progress`: defaults to a no-op callback when omitted.
<!-- trie:end -->