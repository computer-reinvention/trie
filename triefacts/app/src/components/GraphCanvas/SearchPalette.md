---
trie_version: 0.1.9
source: app/src/components/GraphCanvas/SearchPalette.tsx
file_fingerprint: 66b19e3c4f886b832c00e3f4b003019050f9af186e165edb5a1c0c8050bfcfb7
last_synced_at: '2026-06-17T16:37:52Z'
defines:
- kind: function
  qualified_name: app/src/components/GraphCanvas/SearchPalette:SearchPalette
  lines: 9-107
incoming_refs: 1
outgoing_refs: 3
---
<!-- trie:section symbol=app/src/components/GraphCanvas/SearchPalette:SearchPalette fingerprint=b0a55f50eaf95c0f33be922407fcc4efff2718864b5f0d5b354b1d272a60e2f9 body_fp=9713cfa5640bda399aabe39a6a40c49b7e3a26872ae8c933809e3603c7f0b552 source_ref=f4a8a70c884571d5dc8fed099f95567bb6234cd8 role=api -->
Render a Cmd+P search palette that filters graph nodes by name/qname and jumps focus to the selected symbol on the canvas.

- Toggles open/closed via `Cmd+P` / `Ctrl+P`; returns `null` when closed.
- Results are filtered against `model.nodes`, sorted by descending `salience`, capped at 20.
- `jump` expands the owning component and dispatches `trie:node-selected` before closing.
<!-- trie:end -->