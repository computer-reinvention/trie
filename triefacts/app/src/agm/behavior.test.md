---
trie_version: 0.1.9
source: app/src/agm/behavior.test.ts
file_fingerprint: 9b1d40cd5fd9e4492fa41bcdf9144df9286c2cc474736842977de6bf2db7e442
last_synced_at: '2026-06-17T16:35:47Z'
defines:
- kind: module
  qualified_name: app/src/agm/behavior.test:__module__
  lines: 1-165
- kind: constant
  qualified_name: app/src/agm/behavior.test:ROLES
  lines: 13-13
- kind: constant
  qualified_name: app/src/agm/behavior.test:roleOf
  lines: 14-20
- kind: function
  qualified_name: app/src/agm/behavior.test:place
  lines: 22-41
- kind: function
  qualified_name: app/src/agm/behavior.test:radius
  lines: 43-43
- kind: function
  qualified_name: app/src/agm/behavior.test:byQ
  lines: 44-44
- kind: function
  qualified_name: app/src/agm/behavior.test:centreGap
  lines: 157-164
incoming_refs: 0
outgoing_refs: 7
---
<!-- trie:section symbol=app/src/agm/behavior.test:__module__ fingerprint=36a9a6f4fe303270dec2f8a6110aea5dfec470824aafcc582c5667008ea6974a body_fp=f17fec7cc11627ff51ed9cf0998e811b422f13956d0490665e40b36c69b0cb6d source_ref=1069d6d7d27aea740f677adf3ea62b8252b2e303 role=test -->
Behavioural integration tests verifying composed `AttentionModel` + layout dynamics across a simulated login-bug investigation scenario.

- Covers seven assertions: hottest symbol nearest centre, decay drift, perimeter entry, same-role clustering, role rollup dominance, idle cooling, and focus convergence gap.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/behavior.test:ROLES fingerprint=882b0147cad107fddfd377a527a8317f31f19a94f378e68e454a69415d7c0a33 body_fp=29bd41050e8ed396d480cf56efd731a23f94157132202d03909b22bc4dbeacba source_ref=1069d6d7d27aea740f677adf3ea62b8252b2e303 role=test -->
Fixed ordered list of role names passed to `placeSymbol` as the `roles` dimension across all behavioural tests.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/behavior.test:roleOf fingerprint=b0ebfd063de9df2255d23c4af0300fc78e1d06be5eb7b0c73455faf42d0cda61 body_fp=bdf615df1c1e327beb482fc989f4e61698153e1a7db122fd7769efa762a0c8c7 source_ref=1069d6d7d27aea740f677adf3ea62b8252b2e303 role=test -->
Maps each fully-qualified test symbol name to its role string, used as the shared role lookup across all test scenarios.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/behavior.test:place fingerprint=71891827d095a68aca6a6e2fe15a48af647025e9f0a6716dc467145b421f1b39 body_fp=fb7234c7648490f52f5fde16843c4ebeddba163f021ab1417d27763bfd5d9a4e source_ref=1069d6d7d27aea740f677adf3ea62b8252b2e303 role=test -->
Snapshot the `AttentionModel` at `now`, compute polar placements for all symbols, apply cluster cohesion, and return the placement array.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/behavior.test:radius fingerprint=9c4848e0ec899c7c81cbf5b01f6e44f60ec3a62d689e67db72b67b1f24fceee2 body_fp=2e5f9bd5194714211780a015ace1378bf410ff899276fc6cd66a7ad6567c167f source_ref=1069d6d7d27aea740f677adf3ea62b8252b2e303 role=util -->
Compute the Euclidean distance from the origin for a `PolarPlacement` point.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/behavior.test:byQ fingerprint=a1de7b323f8dda7de497ec63149072b064697e13f8ca3804005bfab8cd9d1fe4 body_fp=0b6024325324135a0085cc6316e354bb7c08ee8c53e15ccc5466f39c5554af40 source_ref=1069d6d7d27aea740f677adf3ea62b8252b2e303 role=util -->
Index a `PolarPlacement` array by `qname` for O(1) lookup in test assertions.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/behavior.test:centreGap fingerprint=bac38785e5ee4ffd65c7839fab3a8f7ebb54c3e5e0daf943bb05e7e5122138b5 body_fp=da2c3e81e96394c90c733ab6cd0b92017130a86adb6c284567fbb5664b59e1cd source_ref=1069d6d7d27aea740f677adf3ea62b8252b2e303 role=test -->
Compute the radius gap between the single nearest-centre placement and the mean radius of all others.

- Returns `0` when fewer than two placements are provided.
- Large return value indicates a converged, single-focus layout; near-zero indicates scattered attention.
<!-- trie:end -->