---
trie_version: 0.1.9
source: app/src/components/ContextMenu/index.tsx
file_fingerprint: 114e15e65bb9554d81890c0b429be011e2119808351093118390e1a6a89b3892
last_synced_at: '2026-06-17T16:37:21Z'
defines:
- kind: function
  qualified_name: app/src/components/ContextMenu/index:ContextMenu
  lines: 10-79
incoming_refs: 1
outgoing_refs: 1
---
<!-- trie:section symbol=app/src/components/ContextMenu/index:ContextMenu fingerprint=864b3a56b0260c247e888a5f0a0896aaada39417a4b35e782a34c3bce68f0219 body_fp=23b8f1cc695dd8ab8a74cb5b868964fe2afd55bea954389e4703dd0719cb69bd source_ref=878d77c5bc3af6244dc04dbd1d3560356859affd role=api -->
Render the app-wide context menu portal, clamped to the viewport, dismissing on outside click, Escape, scroll, or resize.

- Items with `label === "-"` render as a horizontal divider.
- Items with `danger: true` render in the danger colour with a tinted hover state.
- Disabled items suppress `onSelect` and receive a muted, non-interactive style.
<!-- trie:end -->