---
trie_version: 0.1.9
source: app/src/components/AgentPanel/index.tsx
file_fingerprint: 7537d72b72915790a8cd08a4462c8d443dc260bc43e60ea0746e3aa1d226d4c5
last_synced_at: '2026-06-17T16:37:16Z'
defines:
- kind: constant
  qualified_name: app/src/components/AgentPanel/index:PANEL_WIDTH_KEY
  lines: 20-20
- kind: constant
  qualified_name: app/src/components/AgentPanel/index:MIN_WIDTH
  lines: 21-21
- kind: constant
  qualified_name: app/src/components/AgentPanel/index:MAX_WIDTH
  lines: 22-22
- kind: constant
  qualified_name: app/src/components/AgentPanel/index:DEFAULT_WIDTH
  lines: 23-23
- kind: function
  qualified_name: app/src/components/AgentPanel/index:usePanelResize
  lines: 28-69
- kind: function
  qualified_name: app/src/components/AgentPanel/index:AgentPanel
  lines: 74-299
incoming_refs: 1
outgoing_refs: 11
---
<!-- trie:section symbol=app/src/components/AgentPanel/index:PANEL_WIDTH_KEY fingerprint=9bb8a851ab324eee9db3e67049dc5f79b93f0a773e65461f02c57242e494983a body_fp=db7cd031110fca4684cef54b44e1c6cc922893109bba5686ed7d02457207b597 source_ref=2e3a70085354b6c60f99b7ea2d8b9c2c69316ce9 role=config -->
localStorage key used to persist the agent panel's pixel width across reloads.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AgentPanel/index:MIN_WIDTH fingerprint=9f53d0614558c73f9ba5321c1c54500af10febdced998911082fd73e2bf2aa47 body_fp=11e658405fb492e133748f37817ff54a19276f686f630a5d4b123f58aecc8a16 source_ref=2e3a70085354b6c60f99b7ea2d8b9c2c69316ce9 role=config -->
Minimum pixel width the agent panel can be resized to.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AgentPanel/index:MAX_WIDTH fingerprint=efd410713a871e1198983b3a899f417f90db26da0329db775d07c778363678e3 body_fp=a16e1a85e7991b611c20a9f86dc7b98afe4d263174dc252303c23e78255cf977 source_ref=2e3a70085354b6c60f99b7ea2d8b9c2c69316ce9 role=config -->
Maximum pixel width the agent panel can be resized to.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AgentPanel/index:DEFAULT_WIDTH fingerprint=fe2e4b2a25ac4dc944b73a277cd9d3b94eeef4d45e28d5a5ee0476dc61433918 body_fp=db712d91438f0876fa3fec28ded735ff87e630bcd4d83a5412af7efff0ef3c6a source_ref=2e3a70085354b6c60f99b7ea2d8b9c2c69316ce9 role=config -->
Default pixel width applied to the agent panel when no persisted value exists in localStorage.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AgentPanel/index:usePanelResize fingerprint=f9e10dedc4bda272609239dc9c9c98e3ccfa053e3aaf8a97bc83caad33cc039d body_fp=1489704767c9effb6dc4809d08d32ed2efd4471f6a46441cbe0556cb1eac4f54 source_ref=2e3a70085354b6c60f99b7ea2d8b9c2c69316ce9 role=util -->
React hook that manages drag-to-resize state for the agent panel, persisting width to `localStorage`.

- `width` — current panel width in px, clamped between `MIN_WIDTH` (320) and `MAX_WIDTH` (720)
- `onResizeStart` — `mousedown` handler to attach to the resize handle; sets body cursor and disables text selection for the drag duration
- `resizing` — `true` while a drag is in progress
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AgentPanel/index:AgentPanel fingerprint=ac79fbacce9e9116fef64ec3856a6b7cc1d26cff371e071162ee0de96974819b body_fp=ee78dd01e6368a5970d20bdd45ee8e73ba76ef4567358d44f69fc5c45f3baa12 source_ref=2e3a70085354b6c60f99b7ea2d8b9c2c69316ce9 role=api -->
Render the fixed right-hand agent panel combining a session switcher, `Transcript`, and `Composer` into a single resizable `<aside>`.

- Session dropdown shows a filter input only when more than 6 sessions exist.
- `permissionsByCallID` indexes pending `PermissionRequest` objects by tool call ID before passing to `Transcript`.
- `resolvePermission` optimistically removes the permission from store then calls `opencodeClient.replyPermission`.
- Shows a connecting spinner in place of `Transcript`/`Composer` while `serversReady` is false.
<!-- trie:end -->