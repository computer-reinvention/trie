---
trie_version: 0.1.9
source: app/src/components/ConnectionBanner/index.tsx
file_fingerprint: b88562c589c725f0d65a187f62692a4a70a2b53bc00b6c1e7dc7a28ce821ace3
last_synced_at: '2026-06-17T16:37:17Z'
defines:
- kind: function
  qualified_name: app/src/components/ConnectionBanner/index:trie
  lines: 5-5
- kind: function
  qualified_name: app/src/components/ConnectionBanner/index:ConnectionBanner
  lines: 13-80
incoming_refs: 1
outgoing_refs: 1
---
<!-- trie:section symbol=app/src/components/ConnectionBanner/index:trie fingerprint=d81964481f895264e77431f65c590a5ffe9eef7a7a98fcfddb6a40ac89d33cf5 body_fp=41c51d01e1acac970a1f50be976afe2aec2cd84189da9c6cafc023513fce5f49 source_ref=a8cd6fe405ab2acc629e8f34d0d4955b2bf7c3c3 role=util -->
Return the `trie` property from the global `window` object as an untyped accessor.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/ConnectionBanner/index:ConnectionBanner fingerprint=49188d251b957ebdff9aa6beb67338f3afcbd53f67ff6eab875d803a1cf23bf7 body_fp=2bacc8d737a0ed00ef9e0d2f2a2d163f466e71c0de5e2b587d5ae8caf2c57d3c source_ref=a8cd6fe405ab2acc629e8f34d0d4955b2bf7c3c3 role=api -->
Render a connection-status banner that reflects opencode backend health: nothing when live/connecting, a warning chip when degraded, or a full blocking crash bar with a restart button when crashed.

- `status === "degraded"`: renders a pulsing chip with `lastError` as tooltip.
- `status === "crashed"`: renders a top bar showing `lastError` and optional `exitCode`, with a Restart button that calls `window.trie.opencodeConfig.restart()`.
- `restarting`: disables the Restart button while the restart call is in flight.
<!-- trie:end -->