---
trie_version: 0.1.0
source: trie/sync/bootstrap.py
file_fingerprint: 58be95f926987e7fd99407998fa1c1f20eeaef04ecd696fbc43c0a50d961c964
last_synced_at: '2026-05-14T19:44:57Z'
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

<!-- trie:section symbol=trie/sync/bootstrap:BootstrapResult fingerprint=3f3fd17f4bf3bb39691a228e43cfd2570d8f5faf3fec4a81808e46a8a00268f5 body_fp=6381a8c026e5ec7efd2b56703b75695312cdceb219aa98c99368f5a693007f6a source_ref=b583bb2faaee7145d066e7c3b4ea1688f30fec3e -->
## `BootstrapResult`

Immutable record of a completed bootstrap run's outcome and cost.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/bootstrap:build_plan fingerprint=08ab28078e22b0e8cbda5b286c321381af5000a1042cf0aa9c11563e38acf475 body_fp=44d566a367ce4cadbc071f61bccb01ac7300d2efe9af47eb7969ed37c4fd1a94 source_ref=b583bb2faaee7145d066e7c3b4ea1688f30fec3e -->
## `build_plan(*, project_root: Path, store: Store, model_id: str, client: ModelClient, only_files: Iterable[str] | None = None) -> BootstrapPlan`

Rank all files with public symbols by `LOC × public_symbol_count` and produce per-file cost estimates.

- `only_files`: restrict plan to these source-relative paths; skips all others
- `pricing_known`: `False` when model pricing is unavailable; cost estimates are zeroed
- Files with zero public symbols or missing from disk are silently excluded
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/bootstrap:run_bootstrap fingerprint=2c937a218d06abcc2c1e95a2902e01bf7fe41c2028ce38edb61c84e611636b2f body_fp=c1553ced5e1eace0953d1a6ee67ae81352e0a15e5a981be07ed9452be58680e9 source_ref=b583bb2faaee7145d066e7c3b4ea1688f30fec3e -->
## `run_bootstrap(*, plan: BootstrapPlan, project_root: Path, config: Config, client: ModelClient, pricing: ModelPricing | None, budget_usd: float | None, limit: int | None, progress: ProgressCallback | None = None, store: Store | None = None) -> BootstrapResult`

Execute the ranked worklist, generating triefacts for each file until budget or limit is exhausted.

- `budget_usd`: stops after cost meets or exceeds threshold; final file may overshoot by its own cost.
- `limit`: caps the number of files successfully synced, not items iterated.
- `pricing`: when `None`, actual cost tracking is disabled and `actual_cost_usd` returns 0.
- `progress`: defaults to a no-op callback when omitted.
<!-- trie:end -->