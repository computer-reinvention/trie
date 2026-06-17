---
trie_version: 0.1.9
source: app/src/agm/propagation.test.ts
file_fingerprint: 528583b97414828305d11657c03fb2153dba275d40caefc0421f62d8bf00a1df
last_synced_at: '2026-06-17T16:35:40Z'
defines:
- kind: module
  qualified_name: app/src/agm/propagation.test:__module__
  lines: 1-49
incoming_refs: 0
outgoing_refs: 0
---
<!-- trie:section symbol=app/src/agm/propagation.test:__module__ fingerprint=33e2c42145fe1b7434f790ec5c952da0717b029877c381bd88c025f37bc9a635 body_fp=b91b538533e52dc4dfb3d4fe4187c21583e9a9dab07af99a707be5c1caf8482a source_ref=ec044b6de211674a0760029d29e4015271b758d9 role=test -->
Vitest suite for `buildTypedAdjacency` and `propagate`, covering edge-weight scaling, cold sources, single-hop limits, and hub suppression.

- **"spreads one weak hop"**: verifies gain equals `score × edgeWeight × PROPAGATION_FACTOR`
- **"weaker edge kinds"**: asserts `calls` (1.0) propagates more than `contains` (0.2)
- **"cold source"**: propagation from a zero-score node produces an empty result map
- **"one hop only"**: confirms nodes two hops away receive no gain
- **"skips hub sources"**: a node with ≥ 50 outgoing edges is not expanded
<!-- trie:end -->