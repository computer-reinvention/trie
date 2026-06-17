---
trie_version: 0.1.9
source: app/src/store/agmStore.ts
file_fingerprint: db757be7889535c36c2cdd6a10e41a6f91f262e314a9e67bc275bb60cf556e58
last_synced_at: '2026-06-17T16:40:15Z'
defines:
- kind: interface
  qualified_name: app/src/store/agmStore:AGMState
  lines: 28-66
- kind: constant
  qualified_name: app/src/store/agmStore:useAGMStore
  lines: 68-188
incoming_refs: 5
outgoing_refs: 17
---
<!-- trie:section symbol=app/src/store/agmStore:AGMState fingerprint=d5f9db192b517f01d6aec81ec832d5b4f11f425b867df526304a83c600d66619 body_fp=ce549b801774a37455a2ed4dd7502518c0b4c12fb75cb02be4703abd0f94cf26 source_ref=6617fd21ab5e5d8f6897ba7f343c4dc4c651b7ab role=model -->
Zustand store shape combining AGM engine instances, loaded topology maps, derived canvas snapshots, and action methods.

- `adjacency` — typed adjacency structure for propagation; `null` until `setModel` runs
- `roles` — sorted unique role list used for stable angular placement in gravity layout
- `historicalByQname` — decayed per-symbol historical mass seeded from `SystemModel`
- `edgesByQname` — typed out-edges per qname, consumed by canvas to draw repo spring edges
- `propagated` — live mass after graph propagation; rewritten on every `recompute` call
- `roleMass` — display-weight mass aggregated per role; rewritten on every `recompute` call
- `lastRecompute` — Unix timestamp (seconds) of the most recent `recompute` invocation
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/agmStore:useAGMStore fingerprint=19db424c5745897d25f1ab5de2f6088e1d493fe9068c3cf5826e782eb7383e76 body_fp=24f1fde366edc7ab70b0651f45c5fea022529565163a5219ee2b345056880d74 source_ref=6617fd21ab5e5d8f6897ba7f343c4dc4c651b7ab role=orchestration -->
Zustand store wiring `AttentionModel`, `AttentionGraph`, `InvestigationRegistry`, and propagation into a single reactive slice for the AGM canvas.

- `setModel` — loads topology and edges, preserves live attention state across refreshes
- `resetSession` — clears live mass, graph trail, and investigations; retains historical geography
- `ingest` — records a single attention event into the `AttentionModel`
- `ingestTrace` — reinforces a call chain in the graph and ingests each node as a `"trace"` event
- `setInvestigation` — upserts an investigation and activates it in the graph when status is `"active"`
- `addNegativeEvidence` — applies negative evidence to a node and records it against the active investigation
- `onRename` / `onDelete` / `onCreate` — forward symbol lifecycle events to `AttentionModel`
- `recompute` — prunes decay, snapshots mass, propagates live mass through adjacency, updates role mass and investigation; called each rAF tick
- `massByQname`, `propagated`, `roleMass` — derived snapshots written by `recompute`, read by the canvas
<!-- trie:end -->