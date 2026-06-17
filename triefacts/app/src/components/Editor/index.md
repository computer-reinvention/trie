---
trie_version: 0.1.9
source: app/src/components/Editor/index.tsx
file_fingerprint: 28e336f65799a0f2841c36ebab083a9e5f9770f9da527dbc015f2b7a54aefd2e
last_synced_at: '2026-06-17T16:37:28Z'
defines:
- kind: function
  qualified_name: app/src/components/Editor/index:Editor
  lines: 21-93
incoming_refs: 1
outgoing_refs: 11
---
<!-- trie:section symbol=app/src/components/Editor/index:Editor fingerprint=2c9a2a94e5928d6b4d71033afde170dae17b6ff7056ad34ffc938ed5f30032f7 body_fp=de579baf41d4c0d926ea0c21beca85fb6565fad2df6bd8fce784c07c29ac2bff source_ref=21e22683ff164d1efbb2dba9d2d6def46b87d0de role=api -->
Render the central editor area: a `TabStrip` above a stacked content region where all permanent panels (`AGMCanvas`, `GraphCanvas`, `PatchesPanel`, `TriePanel`) stay mounted and file tabs mount lazily.

- All permanent panels use CSS `visibility`/`zIndex` toggling to stay alive across tab switches, preserving layout, zoom, and live streams.
- File tabs (`tab.kind === "file"`) are mounted once opened and hidden when inactive.
<!-- trie:end -->