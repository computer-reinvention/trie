---
trie_version: 0.3.0
source: trie/sync/bootstrap.py
file_fingerprint: 3bc374880d5785934f4c89da315b1c63c82799a144cfe4b9844418ca0524acc4
last_synced_at: '2026-08-02T21:19:47Z'
defines:
- kind: module
  qualified_name: trie/sync/bootstrap:__module__
  lines: 1-215
- kind: class
  qualified_name: trie/sync/bootstrap:PlanItem
  lines: 24-28
  signature: class PlanItem
- kind: class
  qualified_name: trie/sync/bootstrap:BootstrapPlan
  lines: 32-35
  signature: class BootstrapPlan
- kind: class
  qualified_name: trie/sync/bootstrap:BootstrapResult
  lines: 39-46
  signature: class BootstrapResult
- kind: function
  qualified_name: trie/sync/bootstrap:build_plan
  lines: 49-135
  signature: 'def build_plan( *, project_root: Path, store: Store, model_id: str, client: TrieClient, only_files: Iterable[str] | None = None, regen_count_by_file: dict[str, int] | None = None, ) -> BootstrapPlan'
- kind: function
  qualified_name: trie/sync/bootstrap:run_bootstrap
  lines: 138-214
  signature: 'def run_bootstrap( *, plan: BootstrapPlan, project_root: Path, config: Config, client: TrieClient, pricing: ModelPricing | None, budget_usd: float | None, limit: int | None, progress: ProgressCallback | None = None, store: Store | None = None, ) -> BootstrapResult'
incoming_refs: 18
outgoing_refs: 17
---
<!-- trie:section symbol=trie/sync/bootstrap:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=2d310a23ea477f2ab385c5eabd894da122826cd687143831bcc27ebad0cf62c8 source_ref=a9697e77ed2f518a87a84d4b0dd7da51d2d4623a role=documentation-sync -->
Provides batch documentation generation planning and execution for multiple Python files.

- **PlanItem**: represents a single file with cost estimates and priority scoring
- **BootstrapPlan**: complete worklist with total cost estimates for batch execution
- **BootstrapResult**: execution results including actual costs and sync outcomes
- **build_plan()**: ranks files by LOC × symbol count and generates accurate cost estimates
- **run_bootstrap()**: executes the worklist with budget/limit controls and progress tracking
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/bootstrap:PlanItem fingerprint=3ad4199e6663a1036afc1e755b38c0280155f590812857853ea08cca37b49294 body_fp=7e95a22813fba0bd847be375291c48108138e113b68e3aac6e880f5f349ffb0e source_ref=a9697e77ed2f518a87a84d4b0dd7da51d2d4623a role=documentation-sync -->
## `class PlanItem`

Represents a file in the bootstrap plan with its priority score and cost estimate.

- `file_path`: relative to project source root
- `score`: prioritization value calculated as LOC × symbol count
- `estimated`: detailed cost breakdown from FileEstimate
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/bootstrap:BootstrapPlan fingerprint=4aaf47574b31c065099c6ea2ffd0ebc1af1247d496cb0f5d7affc57237016198 body_fp=ecc25aace6601e15c62d5362d85d94fa04edc87c797c8017e810c3dc94431172 source_ref=a9697e77ed2f518a87a84d4b0dd7da51d2d4623a role=documentation-sync -->
## `class BootstrapPlan`

Represents a ranked worklist of files to sync with cost estimates.

- `items`: ranked by score (descending), then by file path
- `pricing_known`: false when model pricing unavailable, making cost estimates zero
- `total_estimated_cost`: sum of all item cost estimates in USD
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/bootstrap:BootstrapResult fingerprint=1f3ac61615c5ec3114ca93134c52f14f7107ed01005898274148e16a790861cd body_fp=cf6b7ae117456f3b99384c3e72241378013fc32e832c905e268afd41138aae5c source_ref=6fc0e2ec51a63066191561d40114cf8ce9ec15ec role=model -->
## `class BootstrapResult`

Holds the outcome of a bootstrap run, tracking files processed and associated costs.

- `files_skipped_no_budget`: files skipped due to budget or limit constraints
- `sync_results`: detailed results from each file that was actually processed
- `file_errors`: `(rel_path, error)` pairs for files whose generation raised an exception
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/bootstrap:build_plan fingerprint=639d2e91a91763f78e779d228bd86933d3afdd6d622048322fc763f83a59f463 body_fp=749f23f8532126fa7d10a1912c0947514eb864d8e3973c854e79eace8a6c01ed source_ref=6fc0e2ec51a63066191561d40114cf8ce9ec15ec role=domain -->
## `def build_plan( *, project_root: Path, store: Store, model_id: str, client: TrieClient, only_files: Iterable[str] | None = None, regen_count_by_file: dict[str, int] | None = None, ) -> BootstrapPlan`

Ranks files by LOC × documented symbol count and produces per-file cost estimates for documentation generation.

- `only_files`: Restricts plan to specified source-relative paths
- `regen_count_by_file`: Maps file paths to symbol counts; absence means regen all symbols
- Returns items sorted by score (descending) then file path
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/bootstrap:run_bootstrap fingerprint=016f16dbcde5466224d6943611254b47a158e272b18a71a61df640feae56baa4 body_fp=81da44adbc7e8becbb36d32bfc2e376c52b4b4095560282d456190a1f016c805 source_ref=6fc0e2ec51a63066191561d40114cf8ce9ec15ec role=orchestration -->
## `def run_bootstrap( *, plan: BootstrapPlan, project_root: Path, config: Config, client: TrieClient, pricing: ModelPricing | None, budget_usd: float | None, limit: int | None, progress: ProgressCallback | None = None, store: Store | None = None, ) -> BootstrapResult`

Executes planned file syncs in parallel waves using a scheduler for budget and limit constraints.

- Configures global inflight request limit for concurrent processing
- Creates tasks for existing files, delegates execution to run_waves scheduler
- Returns actual vs estimated costs, per-file sync results, and per-file generation errors
<!-- trie:end -->