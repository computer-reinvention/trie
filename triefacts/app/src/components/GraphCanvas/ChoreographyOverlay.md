---
trie_version: 0.1.9
source: app/src/components/GraphCanvas/ChoreographyOverlay.tsx
file_fingerprint: dba6fcc33dc94e5c4e526e1ee20594fea3dc36cda87eeee3092a28976aa6b8f0
last_synced_at: '2026-06-17T16:38:00Z'
defines:
- kind: interface
  qualified_name: app/src/components/GraphCanvas/ChoreographyOverlay:Props
  lines: 12-18
- kind: function
  qualified_name: app/src/components/GraphCanvas/ChoreographyOverlay:ChoreographyOverlay
  lines: 20-172
incoming_refs: 1
outgoing_refs: 3
---
<!-- trie:section symbol=app/src/components/GraphCanvas/ChoreographyOverlay:Props fingerprint=c179594b0fbd5f6f5a7a68532578330a560ab3ef52af0683388000669764dd0d body_fp=5490e0e66fc648da777056d1f40c68039a9d821a2c0387a04a171cab7edec4c2 source_ref=73654aa6176584e8ce1995bba71530ce737b6e9a role=model -->
Props for `ChoreographyOverlay`; defines the canvas dimensions and data sources needed to paint transient FX.

- `fgRef` — ref to the force-graph instance; used to call `graph2ScreenCoords`
- `componentPos` — maps group/subsystem key to graph-space `{x, y}` anchor point
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/GraphCanvas/ChoreographyOverlay:ChoreographyOverlay fingerprint=afedd053fc614c6b41122883ca9737365484932488da035234a91128438b33a6 body_fp=fca53c7c8782fcfb702b6f005d6b0f7aa1532466100a7fd20f895e6e29b2e47c source_ref=73654aa6176584e8ce1995bba71530ce737b6e9a role=api -->
Render a pointer-events-none canvas overlay that drives a per-frame rAF loop painting ripples, comets, and breadcrumbs sourced from the Conductor store.

- `fgRef` — ref to the force-graph instance; used to call `graph2ScreenCoords` for camera-aware positioning.
- `componentPos` — pre-computed graph-space positions keyed by role/subsystem group name.
- Repaints are skipped when no live FX are active and the camera transform signature is unchanged.
- Ripple dash pattern is set via `activityDash(r.state)` to encode agent state without relying solely on colour.
- Comets with combined axis distance < 6 px are discarded as invisible (same component bubble).
<!-- trie:end -->