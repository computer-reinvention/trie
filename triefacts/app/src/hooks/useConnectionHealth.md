---
trie_version: 0.1.9
source: app/src/hooks/useConnectionHealth.ts
file_fingerprint: d6b99b4e060bca065c9b84219ac5335609d9a17b713ad72220fdbf39d343b4fd
last_synced_at: '2026-06-17T16:39:14Z'
defines:
- kind: function
  qualified_name: app/src/hooks/useConnectionHealth:trie
  lines: 5-5
- kind: function
  qualified_name: app/src/hooks/useConnectionHealth:useConnectionHealth
  lines: 15-46
incoming_refs: 1
outgoing_refs: 1
---
<!-- trie:section symbol=app/src/hooks/useConnectionHealth:trie fingerprint=d81964481f895264e77431f65c590a5ffe9eef7a7a98fcfddb6a40ac89d33cf5 body_fp=31ae442bb2fd3bce4ca1b88cdd74d02e53a678bdb55c842e72955f30253d0cde source_ref=832b8c1d86317e3a8dedc42a2f09f32d2013b0c8 role=util -->
Retrieve the `trie` preload bridge object injected onto `window` by the Electron main process.
<!-- trie:end -->
<!-- trie:section symbol=app/src/hooks/useConnectionHealth:useConnectionHealth fingerprint=d5585fe2d007676bf632e43a16c9595ba3b094c2895ab9cd5568ad56398b5de0 body_fp=058a9308ee9d2d2d8e5372f6cf873d35ba0673aab6bf012777c9e1692dbec074 source_ref=832b8c1d86317e3a8dedc42a2f09f32d2013b0c8 role=orchestration -->
Subscribe once on mount to main-process health signals (process exit, stderr, SSE errors) and forward them into `useConnectionStore`.

- Unexpected exits (no `info.expected`) call `setCrashed`; expected teardowns are silently ignored.
- Stderr lines call `noteError`; SSE stream drops call `setDegraded` (transient, not a crash).
- Returns cleanup callbacks so hot-reload does not stack duplicate listeners.
<!-- trie:end -->