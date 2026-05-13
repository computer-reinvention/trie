---
trie_version: 0.1.0
source: trie/sync/bootstrap.py
file_fingerprint: 58be95f926987e7fd99407998fa1c1f20eeaef04ecd696fbc43c0a50d961c964
last_synced_at: '2026-05-12T18:31:05Z'
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
<!-- trie:section symbol=trie/sync/bootstrap:PlanItem fingerprint=3ad4199e6663a1036afc1e755b38c0280155f590812857853ea08cca37b49294 body_fp=0b4420a239d6f99ad0699c0a78eb6b6b80618c8c64662484e36288af4d525a97 -->
## `PlanItem`

Immutable record representing one file in a bootstrap plan.

- `file_path`: source-root-relative path string
- `score`: `LOC × public_symbol_count`, used for ranking
- `estimated`: per-file token and cost breakdown
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/bootstrap:BootstrapPlan fingerprint=4aaf47574b31c065099c6ea2ffd0ebc1af1247d496cb0f5d7affc57237016198 body_fp=9c51fcb94ea9e520b1458bb2f6d2f2bd5b5ae856d22f9e55894cd598b4d14c47 -->
## `BootstrapPlan(items: list[PlanItem], pricing_known: bool, total_estimated_cost: float)`

Frozen dataclass holding a ranked list of files to document with aggregate cost metadata.

- `pricing_known`: `False` when model pricing is unavailable; cost fields will be zero.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/bootstrap:BootstrapResult fingerprint=3f3fd17f4bf3bb39691a228e43cfd2570d8f5faf3fec4a81808e46a8a00268f5 body_fp=a2f5233acde9923de88f6c081319c5ae04301c3a6b1f0cdfcfbbabd99486c95d -->
## `BootstrapResult`

Frozen dataclass holding aggregate outcome of a completed bootstrap run.

- `files_skipped_no_budget`: count of files skipped due to budget or limit constraints.
- `actual_cost_usd`: sum of per-file costs using real token counts; 0.0 if pricing unknown.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/bootstrap:build_plan fingerprint=08ab28078e22b0e8cbda5b286c321381af5000a1042cf0aa9c11563e38acf475 body_fp=d28160dbbf506212b3b07443fe21d39280b1f36fa0c83be177d5f7f859464df9 -->
## `build_plan(*, project_root: Path, store: Store, model_id: str, client: ModelClient, only_files: Iterable[str] | None = None) -> BootstrapPlan`

Rank all files with public symbols by `LOC × public_symbol_count` and produce per-file cost estimates.

- `only_files`: restrict plan to these source-relative paths; skips all others.
- `pricing_known`: `False` when model pricing is unavailable; cost fields are zeroed.
- Files with zero public symbols or missing from disk are silently excluded.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/bootstrap:run_bootstrap fingerprint=2c937a218d06abcc2c1e95a2902e01bf7fe41c2028ce38edb61c84e611636b2f body_fp=5fe39492f25931634532cf866ed6b394973cdf32c9157bf2928ba1103226d3a1 -->
## `run_bootstrap(*, plan: BootstrapPlan, project_root: Path, config: Config, client: ModelClient, pricing: ModelPricing | None, budget_usd: float | None, limit: int | None, progress: ProgressCallback | None = None, store: Store | None = None) -> BootstrapResult`

Execute the plan's worklist, generating triefacts for each file until budget or limit is exhausted.

- `budget_usd`: stops processing after cumulative actual cost meets or exceeds this value; may overshoot by one file's cost.
- `limit`: caps the number of successfully synced files, not total iterations.
- `pricing`: when `None`, actual cost tracking is skipped and `actual_cost_usd` remains `0.0`.
- `progress`: falls back to a no-op callback when `None`.
<!-- trie:end -->