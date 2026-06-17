---
trie_version: 0.1.9
source: app/src/agm/stress.test.ts
file_fingerprint: 68c161d1d889ac3fae68fbe8a8f253d71ae1c74a0627cbfeaba1d693b2c44272
last_synced_at: '2026-06-17T16:35:57Z'
defines:
- kind: module
  qualified_name: app/src/agm/stress.test:__module__
  lines: 1-191
- kind: constant
  qualified_name: app/src/agm/stress.test:TYPES
  lines: 12-12
- kind: function
  qualified_name: app/src/agm/stress.test:finite
  lines: 14-16
incoming_refs: 0
outgoing_refs: 1
---
<!-- trie:section symbol=app/src/agm/stress.test:__module__ fingerprint=02fa7bdc651e00602c53e63dd2a39bc4b29c7e5f442dc4426b9ea59fb3684eb6 body_fp=8c4845c2e0eadfb51a3af4788139bfae7f83ddb0a9fd173f118cd0fad521507f source_ref=3f41055c1b96130a73ff377420ddfc9aa727ae4b role=test -->
Stress and edge-case test suite asserting AGM engine invariants: no NaN, no negative mass, bounded propagation, correct lifecycle on rename/delete/create, hub guard, and decay correctness.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/stress.test:TYPES fingerprint=046ca8e4374a59422346859c007389b6b0241ea9678cfa9eda74037a28cec6d5 body_fp=6ede79d0d6c12b8a79610b02bdea557b15cefafbf2eba4ffccf5cc1b9f6d6ffa source_ref=3f41055c1b96130a73ff377420ddfc9aa727ae4b role=test -->
Module-level constant listing all four `AttentionEventType` values used to cycle event types in stress tests.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/stress.test:finite fingerprint=1fdd570d646854bbdc3d68063c2bc4774e81e284da024cc3f5e52cd71ea36c0f body_fp=9fbfe82fbf454693697c6938e23e42a774c78f3e8c7c9ecc4bc04aa292b8e348 source_ref=3f41055c1b96130a73ff377420ddfc9aa727ae4b role=util -->
Return `true` if `n` is a finite number, delegating to `Number.isFinite`.
<!-- trie:end -->