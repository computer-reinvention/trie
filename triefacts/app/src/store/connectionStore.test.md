---
trie_version: 0.1.9
source: app/src/store/connectionStore.test.ts
file_fingerprint: 05736922726353bd828bc5d75516dc8a693f26a0c6a4134ac8ba9a8b5eaaa0ee
last_synced_at: '2026-06-17T16:40:12Z'
defines:
- kind: module
  qualified_name: app/src/store/connectionStore.test:__module__
  lines: 1-48
- kind: function
  qualified_name: app/src/store/connectionStore.test:reset
  lines: 4-6
incoming_refs: 0
outgoing_refs: 1
---
<!-- trie:section symbol=app/src/store/connectionStore.test:__module__ fingerprint=399f38623cca9de84184faa4b4c34b5eeffece968540957f36af8ca29162584b body_fp=6176d54556d84e66428d34f2da8408199e8a23d5102b95c3b1f9c5cc0816889e source_ref=7428289454c9de5ceec5f40b6d4290e1c0c14140 role=test -->
Tests state transitions (`connecting`, `live`, `crashed`, `degraded`) of `useConnectionStore`, covering status precedence and field side-effects.

- Verifies `setCrashed` cannot be downgraded to `degraded` by a subsequent `setDegraded` call.
- Verifies `lastError` still updates even when status stays `crashed`.
- Verifies `setLive` clears `exitCode` and recovers from `degraded`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/connectionStore.test:reset fingerprint=9aad6235ac84f21c530f84c6163cf18791993d6eb8bbab19c9e7ed14c95993dc body_fp=b484c18cb29a2143cb1363c4ee559846e89ec459d74769018eba56eddecd78f0 source_ref=7428289454c9de5ceec5f40b6d4290e1c0c14140 role=test -->
Reset `useConnectionStore` to its initial `connecting` state before each test.
<!-- trie:end -->