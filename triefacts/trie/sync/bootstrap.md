---
trie_version: 0.1.0
source: trie/sync/bootstrap.py
file_fingerprint: 58be95f926987e7fd99407998fa1c1f20eeaef04ecd696fbc43c0a50d961c964
last_synced_at: '2026-05-14T17:28:05Z'
defines:
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
  lines: 46-114
- kind: function
  qualified_name: trie/sync/bootstrap:run_bootstrap
  lines: 117-186
incoming_refs: 16
outgoing_refs: 12
---
<!-- trie:section symbol=trie/sync/bootstrap:PlanItem fingerprint=3ad4199e6663a1036afc1e755b38c0280155f590812857853ea08cca37b49294 body_fp=e4427040d7aa7582332231974276dadf14a818bd74e1c70fca228e7f36fe3b47 -->
## `PlanItem`

Immutable record representing one file's entry in a bootstrap plan.

- `score`: `LOC × public_symbol_count`, used for ranking
- `estimated`: per-file token and cost breakdown
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/bootstrap:BootstrapPlan fingerprint=4aaf47574b31c065099c6ea2ffd0ebc1af1247d496cb0f5d7affc57237016198 body_fp=1cf14b2a51b71c7d394c0e04e0b7eb73dbefc587992d3bc9a8729c8e447675a7 -->
## `BootstrapPlan(items: list[PlanItem], pricing_known: bool, total_estimated_cost: float)`

Frozen dataclass holding the ranked worklist and aggregate cost estimate produced by `build_plan`.

- `pricing_known`: `False` when no pricing data exists for the model; costs will be zero.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/bootstrap:BootstrapResult fingerprint=3f3fd17f4bf3bb39691a228e43cfd2570d8f5faf3fec4a81808e46a8a00268f5 body_fp=e98a2ef0099eb2aa396b20f0c2beb441716a5d911ef80e57115a6e2a136de97a -->
## `BootstrapResult`

Frozen dataclass holding aggregate outcomes from a completed bootstrap run.

- `files_skipped_no_budget`: count of files skipped due to budget or limit exhaustion.
- `actual_cost_usd`: sum of per-file costs computed from real token usage.
- `estimated_cost_usd`: sum of pre-run cost estimates from the plan.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/bootstrap:build_plan fingerprint=08ab28078e22b0e8cbda5b286c321381af5000a1042cf0aa9c11563e38acf475 body_fp=5f218dd4f633f6eb5036dac86fccdd3d8c1feba6953f0cd7732ff43956492d92 -->
## `build_plan(*, project_root: Path, store: Store, model_id: str, client: ModelClient, only_files: Iterable[str] | None = None) -> BootstrapPlan`

Rank files by `LOC × public_symbol_count` and produce per-file cost estimates, excluding files with no public symbols.

- `only_files`: restrict plan to these source-relative paths; `None` means all files in the store.
- `pricing_known`: `False` when model pricing is unavailable; cost fields default to `0.0`.
- Token counts are fetched via `client.count_tokens` (free API call) for accurate estimates.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/bootstrap:run_bootstrap fingerprint=2c937a218d06abcc2c1e95a2902e01bf7fe41c2028ce38edb61c84e611636b2f body_fp=f53e1afff88bc43555b244a1e7da87c4fe1c6e03ea8849f8384c6bdcf126efd7 -->
## `run_bootstrap(*, plan: BootstrapPlan, project_root: Path, config: Config, client: ModelClient, pricing: ModelPricing | None, budget_usd: float | None, limit: int | None, progress: ProgressCallback | None = None, store: Store | None = None) -> BootstrapResult`

Execute a bootstrap plan, generating triefacts for each file until budget or limit is exhausted.

- `budget_usd`: stops accepting new files once cumulative actual cost meets or exceeds this value.
- `limit`: stops after this many files are successfully synced.
- `pricing`: if `None`, actual cost tracking is skipped and reported as `0.0`.
- Cost is checked **after** each file completes; final file may overshoot budget.
<!-- trie:end -->