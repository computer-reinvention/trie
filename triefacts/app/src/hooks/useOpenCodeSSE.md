---
trie_version: 0.1.9
source: app/src/hooks/useOpenCodeSSE.ts
file_fingerprint: 2ecd26e83d01e4d5b7409cb49112736ff6edfe2790fb22d5d6a1b0b5fd17579b
last_synced_at: '2026-06-17T16:39:21Z'
defines:
- kind: function
  qualified_name: app/src/hooks/useOpenCodeSSE:useOpenCodeSSE
  lines: 38-356
incoming_refs: 1
outgoing_refs: 20
---
<!-- trie:section symbol=app/src/hooks/useOpenCodeSSE:useOpenCodeSSE fingerprint=f930fcd58a493cf4c535aae1f8eb1202ccaa592a2bc19604aa72910fade10515 body_fp=ec7dfae3a85ba76cfdf623b1d95f4580a2bc4c6974c734991b12b21ef1ceed7a source_ref=b6555c87e5c21f13e1ad2080e6e1845d8943e7c5 role=orchestration -->
Subscribe to the opencode `/event` SSE bus and bridge all agent events to the transcript store, live graph choreography, and AGM attention model.

- `opencodePort` — skips setup entirely when falsy; re-subscribes when the port changes
- Handles `message.part.updated`, `message.part.delta`, `message.updated`, `session.status/updated/idle/error`, `file.edited`, `permission.asked/replied`
- Tool parts trigger node colour changes (read=blue, scan=violet, write=amber), comet flow animations along real call-graph edges, and AGM attention ingestion
- Grep scan hits are weighted at 0.25 (capped at 8) to prevent broad searches from dominating the canvas
- Written symbols are pinned in the AGM model for the session lifetime
- `patch` completion triggers `ghostCascade`; `patch_apply` start triggers `playCascade` for all staged patches
- Off-graph tools (bash/fetch/shell) surface as a HUD chip rather than graph nodes
- Cleans up by calling `trie.sseUnsubscribe()` and removing the event listener on unmount or port change
<!-- trie:end -->