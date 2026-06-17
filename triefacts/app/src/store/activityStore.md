---
trie_version: 0.1.9
source: app/src/store/activityStore.ts
file_fingerprint: 7df1e55be9c404baea0f602bac5677d2bc43b7d89434f60b9656250f703f9d1a
last_synced_at: '2026-06-17T16:39:57Z'
defines:
- kind: interface
  qualified_name: app/src/store/activityStore:ActivityStore
  lines: 9-15
- kind: constant
  qualified_name: app/src/store/activityStore:useActivityStore
  lines: 17-23
incoming_refs: 2
outgoing_refs: 3
---
<!-- trie:section symbol=app/src/store/activityStore:ActivityStore fingerprint=923440703f5ba1073165e77655d1e62728b7726c010feb1a3d36e5ad4a7f45e2 body_fp=86a24d051050320713878fc70d9b5eb458235bbd4a4933c63d321d065e3569cf source_ref=db357f7de1897221d5a12bff4d6ae6d279487213 role=model -->
Zustand store shape tracking the current activity poll result and its metadata.

- `status`: current activity status from the last poll, or `null` if not yet fetched.
- `pending`: pending activity details from the last poll, or `null` if absent.
- `lastPolledAt`: wall-clock ms of the last successful poll; used to detect polling failure.
- `setActivity`: updates `status`, `pending`, and `lastPolledAt` from a fresh `ActivityResult`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/activityStore:useActivityStore fingerprint=aac1ce79bf9abfd3b3371be9355da9222532b2dc93666d3bc3dda3fdc733c032 body_fp=e7bc9b617361e25b399782fca21fa25824431e5d1cb22339805a90e8a4bfedcd source_ref=db357f7de1897221d5a12bff4d6ae6d279487213 role=model -->
Zustand store holding the latest polled activity state for the current trie writer session.

- `lastPolledAt`: wall-clock ms of last successful poll; zero until first poll completes.
- `setActivity`: writes `status`, `pending`, and `lastPolledAt` from a fresh `ActivityResult`.
<!-- trie:end -->