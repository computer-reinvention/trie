---
trie_version: 0.1.9
source: app/src/store/refreshStore.ts
file_fingerprint: 8f6c4b0c6849ea2c662335cb4893c3eb53af64a2205b00c733580e98b0b6ad92
last_synced_at: '2026-06-17T16:40:39Z'
defines:
- kind: type
  qualified_name: app/src/store/refreshStore:RefreshEvent
  lines: 6-21
- kind: type
  qualified_name: app/src/store/refreshStore:RefreshPhase
  lines: 23-23
- kind: interface
  qualified_name: app/src/store/refreshStore:RefreshStore
  lines: 25-41
- kind: constant
  qualified_name: app/src/store/refreshStore:initial
  lines: 43-53
- kind: constant
  qualified_name: app/src/store/refreshStore:useRefreshStore
  lines: 55-96
incoming_refs: 3
outgoing_refs: 0
---
<!-- trie:section symbol=app/src/store/refreshStore:RefreshEvent fingerprint=717643bfb01267dec5191e7cd10104ee8c8d433732ce431b5d2e27e43b015c75 body_fp=d8b9a2fb20ec0e835d9d847d58eac4b0201c267c598e01196a5f264b54626198 source_ref=f49efcf0226fb5c3f1c2256863248efb575fa498 role=model -->
Discriminated union of all JSONL events emitted by `trie refresh --json` plus process-manager lifecycle events.

- `spawned` / `phase`: lifecycle signals; `phase` carries current phase name and mode
- `start`: per-file processing begins; `idx` is 1-based position in the queue
- `done`: per-file completion; `running_cost_usd` is cumulative cost so far
- `skip`: file bypassed; `reason` explains why
- `summary`: run-level outcome; `refreshed` indicates graph changes, `cost_usd` is total
- `exit`: process exited; `stderr` is optional, only present on abnormal exit
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/refreshStore:RefreshPhase fingerprint=0cffe206f17f550efb7f31b02891b91a276e58dd3ddd65d73f082ebea672baa9 body_fp=3ee746ecbc8acb5fa6b2f1c69edfc7e6e88615a8609e153f28c920e2ac12799a source_ref=f49efcf0226fb5c3f1c2256863248efb575fa498 role=model -->
Union type representing the lifecycle phase of a `trie refresh` run.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/refreshStore:RefreshStore fingerprint=1c081339864808b4667bf9a0bb0e7d49843049dc5a8eacf7e0b4866d7ae6a57a body_fp=6b8813a95d84c2b54ac2c0e899beb4d3c33d3da2822bb0d6eac030944e4fdc01 source_ref=f49efcf0226fb5c3f1c2256863248efb575fa498 role=model -->
Zustand store shape tracking the full lifecycle of a `trie refresh` run.

- `reason`: human-readable freshness-gate code (e.g. `empty_store`, `head_moved`); null until summary received
- `current`: rel-path of the file currently being processed; null when no sync is active
- `refreshed`: true if the last run changed the graph, signalling a graph re-fetch
- `apply`: transitions state in response to a `RefreshEvent`
- `reset`: restores all fields to their initial values
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/refreshStore:initial fingerprint=9f5a3f7b6ea582af42c69b71f7089379cfa18c4896fcba705a8dc0702c0cfad7 body_fp=0e011409c94d7639c7963b745a6466c248a634411a7550994bfe919c9065405c source_ref=f49efcf0226fb5c3f1c2256863248efb575fa498 role=model -->
Default state object spread into `useRefreshStore` on creation and by `reset`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/refreshStore:useRefreshStore fingerprint=757092a52b4ffc9b51fdd47800d0d384ef44a0d5f65dfe770706090e9674813e body_fp=2385144ee3655b05fa22f9a8ed3de888f39e9664ed4ea3a3045d222b816e023f source_ref=f49efcf0226fb5c3f1c2256863248efb575fa498 role=persistence -->
Zustand store managing the lifecycle and progress state of a `trie refresh` run, updated by dispatching `RefreshEvent` values via `apply`.

- `apply`: transitions store state based on event kind; `exit` with non-zero code and no prior error sets `phase: "error"`
- `reset`: restores all fields to their initial idle values
- `refreshed`: set from the `summary` event; signals whether the graph needs re-fetching
- `runningCostUsd` on `summary`: takes the max of current and reported cost to avoid regression
<!-- trie:end -->