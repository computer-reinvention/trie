---
trie_version: 0.1.0
source: trie/sync/bootstrap.py
file_fingerprint: 58be95f926987e7fd99407998fa1c1f20eeaef04ecd696fbc43c0a50d961c964
last_synced_at: '2026-05-14T18:32:38Z'
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
<!-- trie:section symbol=trie/sync/bootstrap:PlanItem fingerprint=3ad4199e6663a1036afc1e755b38c0280155f590812857853ea08cca37b49294 body_fp=0abc087000ec3fabf75f86822a7051fcfc9e3d1b4d074ce3748d2e9c60984138 -->
## `PlanItem(file_path: str, public_symbols: int, score: float, estimated: FileEstimate)`

Immutable dataclass representing one file in a bootstrap plan with its cost estimate.

- `score`: product of line count and public symbol count; drives sort order.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/bootstrap:BootstrapPlan fingerprint=4aaf47574b31c065099c6ea2ffd0ebc1af1247d496cb0f5d7affc57237016198 body_fp=7f2e47e22e7111389a9d048f1751c424e6edc1592b2a56bc5b871e294aeedd06 -->
## `BootstrapPlan(items: list[PlanItem], pricing_known: bool, total_estimated_cost: float)`

Immutable snapshot of a ranked worklist with aggregate cost estimate before execution.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/bootstrap:BootstrapResult fingerprint=3f3fd17f4bf3bb39691a228e43cfd2570d8f5faf3fec4a81808e46a8a00268f5 body_fp=24fd0b18c0dd990a9122723f0fbda7fadf25bfd732a034f1ba587f05eb1e74e8 -->
## `BootstrapResult`

Frozen dataclass holding aggregate results from a completed bootstrap run.

- `files_skipped_no_budget`: count of files skipped due to budget or limit constraints.
- `actual_cost_usd`: sum of real token costs; zero when pricing is unavailable.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/bootstrap:build_plan fingerprint=08ab28078e22b0e8cbda5b286c321381af5000a1042cf0aa9c11563e38acf475 body_fp=557365383cc5a38481b51f7fd6f05af76a5f510d107b91dfda19efae5e9cceb0 -->
## `build_plan(*, project_root: Path, store: Store, model_id: str, client: ModelClient, only_files: Iterable[str] | None = None) -> BootstrapPlan`

Rank eligible source files by `LOC × public_symbol_count` and produce per-file cost estimates.

- `only_files`: restrict plan to these source-relative paths; `None` means all files.
- Files with zero public symbols or missing from disk are silently excluded.
- Token counts are fetched via `client.count_tokens` when pricing is available; otherwise costs default to zero and `pricing_known` is `False`.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/bootstrap:run_bootstrap fingerprint=2c937a218d06abcc2c1e95a2902e01bf7fe41c2028ce38edb61c84e611636b2f body_fp=64ed45e36c9a4524e06ffc8932b03b344ced5e89ab64503fd69d184933c194c4 -->
## `run_bootstrap(*, plan: BootstrapPlan, project_root: Path, config: Config, client: ModelClient, pricing: ModelPricing | None, budget_usd: float | None, limit: int | None, progress: ProgressCallback | None = None, store: Store | None = None) -> BootstrapResult`

Execute the bootstrap worklist, calling `sync_single_file` for each plan item until budget or limit is exhausted.

- `budget_usd`: stops after actual spend reaches this value; may overshoot by one file's cost.
- `limit`: caps the number of successfully synced files, not total iterations.
- `pricing`: when `None`, actual cost is reported as `0.0`.
- `progress`: defaults to a no-op callback if omitted.
<!-- trie:end -->