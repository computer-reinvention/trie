---
trie_version: 0.1.9
source: app/src/store/agentStore.ts
file_fingerprint: c65f2d431a47f0242a833f9730b47d95fb07071ee62904d7654a49ddf5aebbc2
last_synced_at: '2026-06-17T16:40:17Z'
defines:
- kind: interface
  qualified_name: app/src/store/agentStore:SessionState
  lines: 22-29
- kind: interface
  qualified_name: app/src/store/agentStore:AgentStore
  lines: 31-59
- kind: function
  qualified_name: app/src/store/agentStore:emptySession
  lines: 61-63
- kind: function
  qualified_name: app/src/store/agentStore:upsertPart
  lines: 66-72
- kind: function
  qualified_name: app/src/store/agentStore:patchMessageParts
  lines: 75-85
- kind: constant
  qualified_name: app/src/store/agentStore:useAgentStore
  lines: 87-268
- kind: function
  qualified_name: app/src/store/agentStore:useActiveSession
  lines: 271-273
incoming_refs: 8
outgoing_refs: 15
---
<!-- trie:section symbol=app/src/store/agentStore:SessionState fingerprint=6c50152e8dc28b38df82a2fe54a40972b272512b8f1b4fa1b676241abd21f068 body_fp=a1a84576fbf941f816f958fe76bcbfb598d8f1db7f8dc5e38d28976c0de67f8e source_ref=894842417c214468e995fc34e98b75c4700222cf role=model -->
Holds the full runtime state for a single opencode session.

- `permissions`: keyed by `PermissionRequest.id`
- `loaded`: `true` once message history has been fetched at least once
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/agentStore:AgentStore fingerprint=c3aa226de1097d4ed1c70048d2c240c307da31a7415285bed2f7810d41b1ec67 body_fp=8019af9b8e7aa822516d6afdfd1ebb9839b83f8fe39595bdf48b083db9d1c211 source_ref=894842417c214468e995fc34e98b75c4700222cf role=model -->
Zustand store shape for the full multi-session agent state, including session lifecycle, SSE transcript reducers, turn status, optimistic messages, and permissions.

- `sessions`: map of session id → `SessionState`
- `order`: session ids sorted most-recent first, excludes child sessions
- `activeId`: currently focused session id, or `null`
- `setSessions`: bulk-replaces session list and recomputes `order`/`activeId`
- `upsertSession`: inserts or updates one session; child sessions skip `order`
- `applyPartUpdated`: upserts a part into a message; auto-creates stub session/message if absent
- `applyTextDelta`: appends text delta to an existing text part or creates one
- `applyReasoningDelta`: appends reasoning delta to an existing reasoning part or creates one
- `applyMessageInfo`: upserts message metadata; drops optimistic `local-*` stubs on user echo
- `appendLocalUser`: inserts an optimistic user message with a `local-` prefixed id
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/agentStore:emptySession fingerprint=5a32e2ca05a663ec6e0920256d85dadac24ef5ca873b948ffd4f7916c3ca5f84 body_fp=ad9454938534450b29372ebad6ba52f91641822db6ecefe1e67da67d593e4cbb source_ref=894842417c214468e995fc34e98b75c4700222cf role=util -->
Construct a blank `SessionState` for a given `OpencodeSession` with empty messages, no permissions, and `loaded: false`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/agentStore:upsertPart fingerprint=0ce6a4a89daa4290ed2cc4934eb7c7cea752fb19617a347d3b195b7a5cd221ce body_fp=3cba27ddb331bb7b3554744ee3dd8be8208c36c87e60a890dbac7705ba13cc91 source_ref=894842417c214468e995fc34e98b75c4700222cf role=util -->
Return a new `OpencodePart` array with `part` appended or replaced by matching `id`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/agentStore:patchMessageParts fingerprint=f1288f80d34256aac156e25a07985bb0d6bf3405cd779d71e3cc5390262909f8 body_fp=71ddb24fa45ae6d654a4fa76ddbc992525fbdc549be58be2802a0b234a5c745e source_ref=894842417c214468e995fc34e98b75c4700222cf role=util -->
Apply `fn` to the parts of the message matching `messageID`, returning a new messages array.

- `fn`: transform applied to the matched message's parts array
- Returns the original array unchanged if `messageID` is not found
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/agentStore:useAgentStore fingerprint=a96325f9d380e5ce3c90465eadb59d9e5de895564dcc6691049913c9d0bfbabd body_fp=911af7e6b2accec8a0c1ded4ea751048d63c5980b22ea7a4a5b436ccbfbdd594 source_ref=894842417c214468e995fc34e98b75c4700222cf role=orchestration -->
Zustand store managing all opencode sessions, their message transcripts, running state, and per-session permission requests.

- `setSessions` — bulk-replaces session list; excludes child sessions from switcher `order`; preserves existing transcript state
- `upsertSession` — adds or updates one session; child sessions (with `parentID`) never enter `order` or become `activeId`
- `removeSession` — deletes session and promotes the next in `order` as `activeId` if removed was active
- `applyPartUpdated` — upserts a part onto a message; auto-creates stub session/message for child-session parts arriving before metadata
- `applyTextDelta` — appends delta text to an existing `text` part, or creates a new one if absent
- `applyReasoningDelta` — same as `applyTextDelta` but for `reasoning`-typed parts
- `applyMessageInfo` — upserts message metadata; strips optimistic `local-*` user stubs when server echoes the real user message
- `setRunning` — clears `error` when set to `true`; does not clear it when set to `false`
- `appendLocalUser` — inserts an optimistic user message with a `local-` prefixed id and sets `running: true`
- `addPermission` / `removePermission` — mutate the per-session `permissions` map keyed by request id
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/agentStore:useActiveSession fingerprint=33ee22d247aa9e47779bf10f3a4d99bfb955a3fa7c454c4b268fe75df95579c8 body_fp=42c9a3507094bda9e349054124532adc172f674bb2a684df47382547d5f2c31c source_ref=894842417c214468e995fc34e98b75c4700222cf role=util -->
Return the `SessionState` for the currently active session, or `null` if none is active or the session is missing.
<!-- trie:end -->