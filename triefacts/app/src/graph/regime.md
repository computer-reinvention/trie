---
trie_version: 0.1.9
source: app/src/graph/regime.ts
file_fingerprint: b1b31150d6a058e0119c085cb9dadf3fb460ec75aa8914b2359f1fd29ef3621d
last_synced_at: '2026-06-17T16:38:59Z'
defines:
- kind: type
  qualified_name: app/src/graph/regime:Regime
  lines: 11-11
- kind: interface
  qualified_name: app/src/graph/regime:RegimeConfig
  lines: 13-22
- kind: function
  qualified_name: app/src/graph/regime:regimeFor
  lines: 26-41
- kind: function
  qualified_name: app/src/graph/regime:regimeForModel
  lines: 43-45
incoming_refs: 2
outgoing_refs: 1
---
<!-- trie:section symbol=app/src/graph/regime:Regime fingerprint=8321c504de5a341d86766526e7a9dfdea2fd4aa0140a3da45d7e3b6adc65581e body_fp=37b58c0c6d118cca67af58eada2ba6ddf558ab078cbf90fbf843c40081a4bae5 source_ref=1f3d96a654955307d57f3c4b02667abd43208806 role=model -->
Union type enumerating the four project-size scale regimes that drive graph aggregation behaviour.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/regime:RegimeConfig fingerprint=3d172c48743c5167fc5fbe96795809373b169af058d64ddc4721cdceafa5684c body_fp=4f73080b5e807ce8fb85691a0f5b2f026312a3254aace4be2194d89e0e5d3426 source_ref=1f3d96a654955307d57f3c4b02667abd43208806 role=model -->
Configuration bundle describing rendering constraints for a scale regime.

- `budget`: hard cap on real nodes drawn at L2; prevents overwhelm regardless of project size.
- `salienceFloor`: nodes below this threshold collapse into a "+N" summary at L1.
- `defaultAxis`: `"subsystem"` only for huge projects where role groupings become unnavigable blobs.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/regime:regimeFor fingerprint=d5d89a334f8f8af413373ba827fd0d359a8d84e0924c21d7dc3b78e8171c7fae body_fp=1eb722c617d3fd55afce09e796c1eae2e46d9a49eedd29fdf134973f28fb23a2 source_ref=1f3d96a654955307d57f3c4b02667abd43208806 role=domain -->
Map a production node count to a `RegimeConfig` by bucketing into `tiny` (≤150), `medium` (≤3000), `large` (≤10000), or `huge`.

- `productionNodeCount` — count of non-test nodes; determines which regime and `salienceFloor` apply.
- Returns `defaultAxis: "subsystem"` only for `huge`; all smaller regimes use `"role"`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/regime:regimeForModel fingerprint=174e39b286b165103191bbb3beba566ac59c5ccd5449793441259d8ee01af47a body_fp=5e0c31f870e617be4980430c7b595490bba00518fd338432dd9ec6c8210826e1 source_ref=1f3d96a654955307d57f3c4b02667abd43208806 role=util -->
Derive a `RegimeConfig` from a `SystemModel` by delegating to `regimeFor` with the model's production node count.
<!-- trie:end -->