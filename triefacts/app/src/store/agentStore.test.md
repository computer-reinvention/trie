---
trie_version: 0.1.9
source: app/src/store/agentStore.test.ts
file_fingerprint: 1109eb732b7504eb154d8b0472ec938eb05c41e2fbcfc144b9277d3213e7fcb5
last_synced_at: '2026-06-17T16:40:04Z'
defines:
- kind: module
  qualified_name: app/src/store/agentStore.test:__module__
  lines: 1-58
- kind: function
  qualified_name: app/src/store/agentStore.test:reset
  lines: 5-5
- kind: function
  qualified_name: app/src/store/agentStore.test:toolPart
  lines: 7-14
incoming_refs: 0
outgoing_refs: 2
---
<!-- trie:section symbol=app/src/store/agentStore.test:__module__ fingerprint=d8c4f637f438d32c8a5a7424facc8db4e68f55a01490fe68633be2e46d7c101a body_fp=c45e8808c748622ec651f11b7cf37b6cfad7c31f7df7042108463a09bc4e544a source_ref=9678f3b42ca725454c60f4eeca657afdb662299c role=test -->
Tests `agentStore` child/sub-agent session behaviour using Vitest and `useAgentStore`.

- Verifies child sessions are stored but excluded from switcher `order`
- Verifies child sessions never become `activeId`
- Verifies `setSessions` filters children from `order`
- Verifies `applyPartUpdated` and `setRunning` auto-register unknown sessions without adding them to `order`
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/agentStore.test:reset fingerprint=4c6f225f897697a4ece39a8b7336b2dd1d51a6517ad05a7ebc5e1c40b65f8a9c body_fp=f25979e1a9809a67b320aac4b5078e0ca9f8abedde29eeebc792816055bacc26 source_ref=9678f3b42ca725454c60f4eeca657afdb662299c role=test -->
Reset `useAgentStore` to its empty initial state before each test.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/agentStore.test:toolPart fingerprint=1e9e1a2db6992c7ab5712f7ded1a0d491af729b02c2b370edd3b1bd801615263 body_fp=a0dccdc7254b1a4cb76ea972ec6924bdc4d65d0f930d53b04c834dc2bfc5a37d source_ref=9678f3b42ca725454c60f4eeca657afdb662299c role=test -->
Create a completed `tool`-type `OpencodePart` fixture with the given `id` used as both `id` and `callID`.
<!-- trie:end -->