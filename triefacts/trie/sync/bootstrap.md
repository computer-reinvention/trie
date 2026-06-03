---
trie_version: 0.1.5
source: trie/sync/bootstrap.py
file_fingerprint: ed84fc3396904355438b749b7c6e76594aa6592f4f35f8df92abc98a667fff89
last_synced_at: '2026-06-03T21:15:25Z'
defines:
- kind: module
  qualified_name: trie/sync/bootstrap:__module__
  lines: 1-205
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
  lines: 46-132
- kind: function
  qualified_name: trie/sync/bootstrap:run_bootstrap
  lines: 135-204
incoming_refs: 16
outgoing_refs: 13
---
<!-- trie:section symbol=trie/sync/bootstrap:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=2d310a23ea477f2ab385c5eabd894da122826cd687143831bcc27ebad0cf62c8 source_ref=a9697e77ed2f518a87a84d4b0dd7da51d2d4623a -->
Provides batch documentation generation planning and execution for multiple Python files.

- **PlanItem**: represents a single file with cost estimates and priority scoring
- **BootstrapPlan**: complete worklist with total cost estimates for batch execution
- **BootstrapResult**: execution results including actual costs and sync outcomes
- **build_plan()**: ranks files by LOC × symbol count and generates accurate cost estimates
- **run_bootstrap()**: executes the worklist with budget/limit controls and progress tracking
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/bootstrap:PlanItem fingerprint=3ad4199e6663a1036afc1e755b38c0280155f590812857853ea08cca37b49294 body_fp=c976ad461650efdd68fe3f3c938f6bf49d269be213bc8a282ebcefae3b2374fe source_ref=a9697e77ed2f518a87a84d4b0dd7da51d2d4623a -->
Represents a file in the bootstrap plan with its priority score and cost estimate.

- `file_path`: relative to project source root
- `score`: prioritization value calculated as LOC × symbol count
- `estimated`: detailed cost breakdown from FileEstimate
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/bootstrap:BootstrapPlan fingerprint=4aaf47574b31c065099c6ea2ffd0ebc1af1247d496cb0f5d7affc57237016198 body_fp=d9e3f8a3ea723d0026a2a523d6b9619fbe3a525d82b9cdd98e2d2173e4371a36 source_ref=a9697e77ed2f518a87a84d4b0dd7da51d2d4623a -->
Represents a ranked worklist of files to sync with cost estimates.

- `items`: ranked by score (descending), then by file path
- `pricing_known`: false when model pricing unavailable, making cost estimates zero
- `total_estimated_cost`: sum of all item cost estimates in USD
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/bootstrap:BootstrapResult fingerprint=3f3fd17f4bf3bb39691a228e43cfd2570d8f5faf3fec4a81808e46a8a00268f5 body_fp=f0132e66ba35b1cd486a3e5458feb1da04024660f80e9705e58cab8c3378129a source_ref=a9697e77ed2f518a87a84d4b0dd7da51d2d4623a -->
Holds the outcome of a bootstrap run, tracking files processed and associated costs.

- `files_skipped_no_budget`: files skipped due to budget or limit constraints
- `sync_results`: detailed results from each file that was actually processed
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/bootstrap:build_plan fingerprint=639d2e91a91763f78e779d228bd86933d3afdd6d622048322fc763f83a59f463 body_fp=5eaec87f0272b7ed482e79ec419592b6125725bc99a92b6ca894eba5ba4f10f2 source_ref=a9697e77ed2f518a87a84d4b0dd7da51d2d4623a -->
Ranks files by LOC × documented symbol count and produces per-file cost estimates for documentation generation.

- `only_files`: Restricts plan to specified source-relative paths
- `regen_count_by_file`: Maps file paths to symbol counts; absence means regen all symbols
- Returns items sorted by score (descending) then file path
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/bootstrap:run_bootstrap fingerprint=2c937a218d06abcc2c1e95a2902e01bf7fe41c2028ce38edb61c84e611636b2f body_fp=0607ecd16388cb936d8864f50a0f06e0088a80c4521a88db162a4210e09351eb source_ref=a9697e77ed2f518a87a84d4b0dd7da51d2d4623a -->
Executes planned file syncs with budget and limit constraints, stopping when either is reached.

- Cost checked after each file completes, may overshoot budget by final file cost
- Files skipped if source missing, limit reached, or budget exceeded
- Returns actual vs estimated costs and per-file sync results
<!-- trie:end -->