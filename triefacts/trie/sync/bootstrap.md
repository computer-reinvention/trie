---
trie_version: 0.1.2
source: trie/sync/bootstrap.py
file_fingerprint: c0f4f174435148e121708503ba60c8afc867ea101708bae16e1d220cc1fe5ade
last_synced_at: '2026-05-19T10:41:53Z'
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
outgoing_refs: 12
---
<!-- trie:section symbol=trie/sync/bootstrap:PlanItem fingerprint=3ad4199e6663a1036afc1e755b38c0280155f590812857853ea08cca37b49294 body_fp=d88f0bcdf0f255266a2628781f371e1464f82f12d71957673fdaf3dc978a22cb source_ref=b583bb2faaee7145d066e7c3b4ea1688f30fec3e -->
## `PlanItem`

Immutable record representing one file in a bootstrap plan with its cost estimate.

- `file_path`: source-root-relative path string
- `score`: `LOC × public_symbol_count`, used for ranking
- `estimated`: per-file token and cost breakdown
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/bootstrap:BootstrapPlan fingerprint=4aaf47574b31c065099c6ea2ffd0ebc1af1247d496cb0f5d7affc57237016198 body_fp=17663ac2911af33528cd8dffe9bd845d53dd16556ab97e9c5b8c9bac413b8aaa source_ref=b583bb2faaee7145d066e7c3b4ea1688f30fec3e -->
## `BootstrapPlan(items: list[PlanItem], pricing_known: bool, total_estimated_cost: float)`

Frozen dataclass holding a ranked worklist of files and aggregate cost estimates for a bootstrap run.

- `pricing_known`: `False` when model pricing is unavailable; cost fields will be zero.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/bootstrap:BootstrapResult fingerprint=3f3fd17f4bf3bb39691a228e43cfd2570d8f5faf3fec4a81808e46a8a00268f5 body_fp=6381a8c026e5ec7efd2b56703b75695312cdceb219aa98c99368f5a693007f6a source_ref=6fa7f487ae550d9e0cbd13df58df2357ddc4b78a -->
## `BootstrapResult`

Immutable record of a completed bootstrap run's outcome and cost.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/bootstrap:build_plan fingerprint=cb58508dbf1731b80ba6987d1ed9b9c6985a068b30e6e48d9d4e1fa52e119e1f body_fp=ddcb84692f36f7848a60ecc92e4a8d3c5621970d4e8815e9b4cbc07f27631819 source_ref=6fa7f487ae550d9e0cbd13df58df2357ddc4b78a -->
## `build_plan(*, project_root: Path, store: Store, model_id: str, client: ModelClient, only_files: Iterable[str] | None = None, regen_count_by_file: dict[str, int] | None = None) -> BootstrapPlan`

Rank all files with public symbols by `LOC × public_symbol_count` and produce per-file cost estimates.

- `only_files`: restrict plan to these source-relative paths; skips all others
- `regen_count_by_file`: scale per-file cost estimate to only the symbols that will hit the LLM; absent file means regen all
- `PlanItem.public_symbols`: always the file's total documented symbol count, not the regen target
- `pricing_known`: `False` when model pricing is unavailable; cost estimates are zeroed
- Files with zero public symbols or missing from disk are silently excluded
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/bootstrap:run_bootstrap fingerprint=2c937a218d06abcc2c1e95a2902e01bf7fe41c2028ce38edb61c84e611636b2f body_fp=c1553ced5e1eace0953d1a6ee67ae81352e0a15e5a981be07ed9452be58680e9 source_ref=6fa7f487ae550d9e0cbd13df58df2357ddc4b78a -->
## `run_bootstrap(*, plan: BootstrapPlan, project_root: Path, config: Config, client: ModelClient, pricing: ModelPricing | None, budget_usd: float | None, limit: int | None, progress: ProgressCallback | None = None, store: Store | None = None) -> BootstrapResult`

Execute the ranked worklist, generating triefacts for each file until budget or limit is exhausted.

- `budget_usd`: stops after cost meets or exceeds threshold; final file may overshoot by its own cost.
- `limit`: caps the number of files successfully synced, not items iterated.
- `pricing`: when `None`, actual cost tracking is disabled and `actual_cost_usd` returns 0.
- `progress`: defaults to a no-op callback when omitted.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/bootstrap:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=631cc54423e766f7b1a878b08b253359839010499bf3664253105075ddcf4e29 source_ref=6fa7f487ae550d9e0cbd13df58df2357ddc4b78a -->
## `bootstrap`

Rank, cost-estimate, and execute a batch documentation-generation run across a project's source files.

- `build_plan`: scores files by `LOC × symbol_count`, calls Anthropic token-count API for accurate estimates
- `run_bootstrap`: iterates the plan, stopping at budget or limit, accumulating real costs
- `PlanItem` / `BootstrapPlan` / `BootstrapResult`: frozen dataclasses carrying plan and execution state
<!-- trie:end -->