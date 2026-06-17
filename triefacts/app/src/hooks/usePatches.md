---
trie_version: 0.1.9
source: app/src/hooks/usePatches.ts
file_fingerprint: 15561c64e780362f1e16fe067a09e0f1e060b7977a8349dd5e2732cc177ce1c5
last_synced_at: '2026-06-17T16:39:27Z'
defines:
- kind: constant
  qualified_name: app/src/hooks/usePatches:POLL_MS
  lines: 7-7
- kind: function
  qualified_name: app/src/hooks/usePatches:usePatches
  lines: 11-72
incoming_refs: 1
outgoing_refs: 4
---
<!-- trie:section symbol=app/src/hooks/usePatches:POLL_MS fingerprint=328f3d2c78ca254c9fd7191be100d65691525d62c2d4707e2cc13b5a13a45ebd body_fp=b3e0e3d4b2728e136ec0b457d2ec3fe577531198ab2685f208f4885f2057624b source_ref=17a5ec69051d8893080c1f5c014d08aaa4a0b8bb role=config -->
Polling interval in milliseconds between successive patch-list fetches.
<!-- trie:end -->
<!-- trie:section symbol=app/src/hooks/usePatches:usePatches fingerprint=ef660dd3cfc80672018424005192f77519a2e8e0d8c55c9247295717e052fa39 body_fp=b8431239613d6e6a571c65380bf21d958ffef558fac7d9dc8c26b6042b954e64 source_ref=17a5ec69051d8893080c1f5c014d08aaa4a0b8bb role=orchestration -->
React hook that polls pending patches every 2500 ms and returns `refresh`, `drop`, and `apply` actions.

- `refresh` — fetches current patches from `graphClient` and updates `patchesStore`; errors are silently swallowed.
- `drop(qname?)` — drops a patch by qualified name (or all if omitted), then refreshes immediately.
- `apply()` — applies all pending patches, propagates any error message to the store, and returns the `ApplyReport` or `null` on failure.
- Polling only runs while `appStore.serversReady` is `true`; the effect cleans up the timer on teardown.
<!-- trie:end -->