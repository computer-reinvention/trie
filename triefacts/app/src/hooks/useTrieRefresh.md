---
trie_version: 0.1.9
source: app/src/hooks/useTrieRefresh.ts
file_fingerprint: 750ec32b77b9e2b385ba5358654718963b1243382ae29d6b7682673594d79e87
last_synced_at: '2026-06-17T16:39:31Z'
defines:
- kind: function
  qualified_name: app/src/hooks/useTrieRefresh:trie
  lines: 5-5
- kind: function
  qualified_name: app/src/hooks/useTrieRefresh:useTrieRefresh
  lines: 17-38
incoming_refs: 1
outgoing_refs: 2
---
<!-- trie:section symbol=app/src/hooks/useTrieRefresh:trie fingerprint=d81964481f895264e77431f65c590a5ffe9eef7a7a98fcfddb6a40ac89d33cf5 body_fp=bd5d8dce08731ddc589fec638c46eb4b7bc33f183a7ea95522187d393bf388ff source_ref=a53177eed95a9990159de456aa272db4347cf6c1 role=util -->
Return the `trie` preload API object from `window`, typed as `any` to bypass TypeScript's DOM types.
<!-- trie:end -->
<!-- trie:section symbol=app/src/hooks/useTrieRefresh:useTrieRefresh fingerprint=755f6560a727bbf5a82e215aef41084d792b819713885ad20e735722b0063537 body_fp=d7e0066f5ab6ca7573155fc385c495f27a9b99263730f517991086aaedc99ac5 source_ref=a53177eed95a9990159de456aa272db4347cf6c1 role=api -->
React hook that subscribes to the `trie refresh --json` progress stream and calls `onRefreshed` when the graph changes or a clean exit occurs.

- `onRefreshed` — invoked on `summary` events where `refreshed` is true, or on `exit` with code `0`.
<!-- trie:end -->