---
trie_version: 0.1.9
source: trie/sync/bootstrap.py
file_fingerprint: 3bc374880d5785934f4c89da315b1c63c82799a144cfe4b9844418ca0524acc4
last_synced_at: '2026-07-29T03:04:12Z'
defines:
- kind: module
  qualified_name: trie/sync/bootstrap:__module__
  lines: 1-215
- kind: class
  qualified_name: trie/sync/bootstrap:PlanItem
  lines: 24-28
- kind: class
  qualified_name: trie/sync/bootstrap:BootstrapPlan
  lines: 32-35
- kind: class
  qualified_name: trie/sync/bootstrap:BootstrapResult
  lines: 39-46
- kind: function
  qualified_name: trie/sync/bootstrap:build_plan
  lines: 49-135
- kind: function
  qualified_name: trie/sync/bootstrap:run_bootstrap
  lines: 138-214
incoming_refs: 18
outgoing_refs: 16
---
<!-- trie:section symbol=trie/sync/bootstrap:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=2d310a23ea477f2ab385c5eabd894da122826cd687143831bcc27ebad0cf62c8 source_ref=a9697e77ed2f518a87a84d4b0dd7da51d2d4623a role=documentation-sync -->
Provides batch documentation generation planning and execution for multiple Python files.

- **PlanItem**: represents a single file with cost estimates and priority scoring
- **BootstrapPlan**: complete worklist with total cost estimates for batch execution
- **BootstrapResult**: execution results including actual costs and sync outcomes
- **build_plan()**: ranks files by LOC × symbol count and generates accurate cost estimates
- **run_bootstrap()**: executes the worklist with budget/limit controls and progress tracking
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/bootstrap:PlanItem fingerprint=3ad4199e6663a1036afc1e755b38c0280155f590812857853ea08cca37b49294 body_fp=c976ad461650efdd68fe3f3c938f6bf49d269be213bc8a282ebcefae3b2374fe source_ref=a9697e77ed2f518a87a84d4b0dd7da51d2d4623a role=documentation-sync -->
Represents a file in the bootstrap plan with its priority score and cost estimate.

- `file_path`: relative to project source root
- `score`: prioritization value calculated as LOC × symbol count
- `estimated`: detailed cost breakdown from FileEstimate
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/bootstrap:BootstrapPlan fingerprint=4aaf47574b31c065099c6ea2ffd0ebc1af1247d496cb0f5d7affc57237016198 body_fp=d9e3f8a3ea723d0026a2a523d6b9619fbe3a525d82b9cdd98e2d2173e4371a36 source_ref=a9697e77ed2f518a87a84d4b0dd7da51d2d4623a role=documentation-sync -->
Represents a ranked worklist of files to sync with cost estimates.

- `items`: ranked by score (descending), then by file path
- `pricing_known`: false when model pricing unavailable, making cost estimates zero
- `total_estimated_cost`: sum of all item cost estimates in USD
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/bootstrap:BootstrapResult fingerprint=1f3ac61615c5ec3114ca93134c52f14f7107ed01005898274148e16a790861cd body_fp=562e4ae4aaa8bb34ef56ee7d06e8aa5f22a6ab02005d3858a634c317ef0910e3 source_ref=6fc0e2ec51a63066191561d40114cf8ce9ec15ec role=model -->
Holds the outcome of a bootstrap run, tracking files processed and associated costs.

- `files_skipped_no_budget`: files skipped due to budget or limit constraints
- `sync_results`: detailed results from each file that was actually processed
- `file_errors`: `(rel_path, error)` pairs for files whose generation raised an exception
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/bootstrap:build_plan fingerprint=639d2e91a91763f78e779d228bd86933d3afdd6d622048322fc763f83a59f463 body_fp=5eaec87f0272b7ed482e79ec419592b6125725bc99a92b6ca894eba5ba4f10f2 source_ref=b80e775bf813db8e4b4937c29c968d95eb993902 role=domain -->
Ranks files by LOC × documented symbol count and produces per-file cost estimates for documentation generation.

- `only_files`: Restricts plan to specified source-relative paths
- `regen_count_by_file`: Maps file paths to symbol counts; absence means regen all symbols
- Returns items sorted by score (descending) then file path
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/bootstrap:run_bootstrap fingerprint=016f16dbcde5466224d6943611254b47a158e272b18a71a61df640feae56baa4 body_fp=a08063cf82953adf74ef0c76bbdbcd6f1c0c1b3bcbf8df7280fca253ee2e0388 source_ref=6fc0e2ec51a63066191561d40114cf8ce9ec15ec role=orchestration -->
Executes planned file syncs in parallel waves using a scheduler for budget and limit constraints.

- Configures global inflight request limit for concurrent processing
- Creates tasks for existing files, delegates execution to run_waves scheduler
- Returns actual vs estimated costs, per-file sync results, and per-file generation errors
<!-- trie:end -->