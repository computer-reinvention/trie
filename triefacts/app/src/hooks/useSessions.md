---
trie_version: 0.1.9
source: app/src/hooks/useSessions.ts
file_fingerprint: 65b40bb710113284acffe46e8cfb7b056d649f2127acd9face0cdb5af8d4457e
last_synced_at: '2026-06-17T16:39:24Z'
defines:
- kind: function
  qualified_name: app/src/hooks/useSessions:useSessions
  lines: 20-165
incoming_refs: 1
outgoing_refs: 9
---
<!-- trie:section symbol=app/src/hooks/useSessions:useSessions fingerprint=5db92133ea10870f87403a0162eb1830f5ba41a35763004d68900e626f18c132 body_fp=3d9366fae6193a9bce848e9557fb548e6c585d2ca1c4ce41116bd056e418dde4 source_ref=6d4594bbce4a562b6f2858317e60c7089c60924f role=orchestration -->
React hook that orchestrates opencode session lifecycle: loads, prunes empty stubs, lazily fetches transcripts, and exposes session-management actions.

- `newSession` — creates a session, sets it active, resets AGM/graph live state
- `switchSession` — activates an existing session by id, resets AGM/graph live state
- `deleteSession` — deletes server-side session and removes it from store/loaded cache
- `clearEmpty` — deletes all non-active, default-titled, message-less sessions server-side
- `send` — sends a message to the active session; opens an AGM investigation and writes inline error on POST failure
- `abort` — aborts the active session's running turn and clears its running flag
<!-- trie:end -->