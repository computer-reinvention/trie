---
trie_version: 0.1.9
source: app/src/agm/propagation.ts
file_fingerprint: a736dd0249dc01fe7af549f7db8f721cc1311f7f749ffcf3929081ddb682a2e0
last_synced_at: '2026-06-17T16:35:55Z'
defines:
- kind: interface
  qualified_name: app/src/agm/propagation:TypedAdjacency
  lines: 16-19
- kind: function
  qualified_name: app/src/agm/propagation:buildTypedAdjacency
  lines: 22-35
- kind: constant
  qualified_name: app/src/agm/propagation:HUB_OUT_DEGREE
  lines: 40-40
- kind: function
  qualified_name: app/src/agm/propagation:propagate
  lines: 44-69
incoming_refs: 3
outgoing_refs: 0
---
<!-- trie:section symbol=app/src/agm/propagation:TypedAdjacency fingerprint=ef9de483b42b24b3cc02ead095934236dc870aa31b0d31bf366271702a6251c0 body_fp=afe31c41c612030ddf25694c3e3244d187283a04b9ffc4a4caeb4b929a1f6b09 source_ref=4fe7710629a6a7f85c25a0bcd14bba5ef37a043b role=model -->
Holds a directed typed adjacency map used as input to `propagate`.

- `out`: maps each source qname to its outgoing neighbour/edge-kind pairs.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/propagation:buildTypedAdjacency fingerprint=5ae92dceded87cf14bd28af5e608fd5b56a51fad1f0e6e242b56add8f488e5bb body_fp=13db423da4e66b1d846afbfa95cc2e52a20b390f1dfee3f7eb3d4ce2894f5937 source_ref=4fe7710629a6a7f85c25a0bcd14bba5ef37a043b role=util -->
Build a directed `TypedAdjacency` from a flat typed-edge list, grouping edges by source `qname` into an outbound adjacency map.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/propagation:HUB_OUT_DEGREE fingerprint=3b9f6dc2d89df139dec7fcda30bb46becf92b5bc97b0a4605dca346a6f485281 body_fp=e9647387b7c8b38435c7d8b4572d2f69e0f9236fa438b3aa0654f5cad652507d source_ref=4fe7710629a6a7f85c25a0bcd14bba5ef37a043b role=config -->
Out-degree threshold above which a source node is skipped during propagation to prevent attention smearing across high-fan-out hubs.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/propagation:propagate fingerprint=0d8a78cd89a3122e7acd7ec59e3d42df3ab3cc916b98b825acdbf487abe00468 body_fp=994ac0b532d715f558716d7fa000a7fadefd048b76b3a57a08932599a7eeef3c source_ref=4fe7710629a6a7f85c25a0bcd14bba5ef37a043b role=domain -->
Compute transient propagated heat for one hop across `adj`, returning a map of neighbour qname → added heat.

- `liveMass` — qname → raw live mass; sources with mass ≤ 0 or out-degree > 40 are skipped.
- `adj` — directed typed adjacency used to find neighbours.
- Returns accumulated gain per neighbour, excluding source nodes; never persisted.
<!-- trie:end -->