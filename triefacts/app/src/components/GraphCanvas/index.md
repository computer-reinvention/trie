---
trie_version: 0.1.9
source: app/src/components/GraphCanvas/index.tsx
file_fingerprint: 3298e6dab61553c1dbbe5a529b1460f1be64a008bd088cbc5998b9c81fb30458
last_synced_at: '2026-06-17T16:38:24Z'
defines:
- kind: interface
  qualified_name: app/src/components/GraphCanvas/index:GraphCanvasProps
  lines: 23-25
- kind: type
  qualified_name: app/src/components/GraphCanvas/index:FGNode
  lines: 27-69
- kind: interface
  qualified_name: app/src/components/GraphCanvas/index:FGLink
  lines: 71-76
- kind: function
  qualified_name: app/src/components/GraphCanvas/index:GraphCanvas
  lines: 78-697
- kind: function
  qualified_name: app/src/components/GraphCanvas/index:EmptyGraphState
  lines: 702-745
- kind: function
  qualified_name: app/src/components/GraphCanvas/index:ToolHud
  lines: 749-768
- kind: function
  qualified_name: app/src/components/GraphCanvas/index:ReplayControl
  lines: 771-785
- kind: interface
  qualified_name: app/src/components/GraphCanvas/index:PaintOpts
  lines: 789-800
- kind: function
  qualified_name: app/src/components/GraphCanvas/index:paintNode
  lines: 802-999
incoming_refs: 1
outgoing_refs: 25
---
<!-- trie:section symbol=app/src/components/GraphCanvas/index:GraphCanvasProps fingerprint=2a2664eb3f32d82858ccc6e12270671a8b11f58fcc410edbd124687b2c531e7b body_fp=c32c0b6a796637e075d0395af71736a77ca062d2d40fc7d1a55f67d5827d51fa source_ref=9b45d68ec4b6794a58ffb4acd64d38b1fad11d17 role=model -->
Props for the `GraphCanvas` component.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/GraphCanvas/index:FGNode fingerprint=93fbbd19d48a8cf2cf0a8c577347be86398bd906689115d37f252a7ee50ff659 body_fp=0a153e0123a5a4aacdc9c77d505730731976d3eb36348670d74d8d4f12eb2bcf source_ref=9b45d68ec4b6794a58ffb4acd64d38b1fad11d17 role=model -->
Discriminated union for the three node variants rendered by `ForceGraph2D` in `GraphCanvas`.

- `kind: "component"` — role/subsystem bubble; `val` sets radius; `fx`/`fy` are fixed layout positions mutated by the force engine.
- `kind: "symbol"` — individual `SystemModelNode`; `group` is the owning role/subsystem key.
- `kind: "aggregate"` — collapsed overflow placeholder; `group` identifies its parent component.
- `order` — normalised depth (0–1) used to assign layer position and color.
- `x`/`y` — runtime coordinates written by the force simulation; optional until the first tick.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/GraphCanvas/index:FGLink fingerprint=91711283a7e7a414520faf8bc87f6e28bad04af249f65f3cfcbf6088f6d85d57 body_fp=4bfe29d557a994580fe5e569b76979854066be0b98e9f056d84bb79d1b86a51e source_ref=9b45d68ec4b6794a58ffb4acd64d38b1fad11d17 role=model -->
Describes an edge in the force-graph, connecting two nodes with an optional semantic kind.

- `weight`: relative strength used to scale link width
- `kind`: `"flow"` adds curvature and arrows; `"member"` and `"call"` use thinner, dimmer strokes
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/GraphCanvas/index:GraphCanvas fingerprint=4558afeca3d36eb813e9039293cad1b63dc45c84cdf45422684bddd23e2f87f1 body_fp=4f16d493dc74b238aa6af72ff18e471143a7626c175bf9cb1ad605692547c21e source_ref=9b45d68ec4b6794a58ffb4acd64d38b1fad11d17 role=api -->
Render the L0 system-map force graph, wiring together layout, animation, agent-camera, hover tooltips, and all canvas overlays.

- `className` — optional CSS class applied to the outermost container div.
- Builds a deterministic top-down layered layout of component (role/subsystem) bubbles with fixed positions; member detail is delegated to `ExpandedPanel`.
- Left-clicks on a component bubble call `expandComponent`; right-clicks toggle pin; left-clicks on symbol nodes select and dispatch `trie:node-selected`.
- Agent-following camera behaviour is gated by the `motion.camera` setting (`off` | `edge-only` | `cinematic`).
- Hover over a component bubble shows a tooltip with pending patches (amber) and agent activity notes (read/scan/write) for symbols inside that group.
- Activity and heat decay runs on every animation frame via `requestAnimationFrame`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/GraphCanvas/index:EmptyGraphState fingerprint=0bdc4f401e52a9feafc3d5bd8daee3c92c96ae33a2b4868c1aa7dec4bfec4e79 body_fp=e41809ce20f34cca6602eb65c49d37af34df7990da201d4a669a0c2ba0d37077 source_ref=9b45d68ec4b6794a58ffb4acd64d38b1fad11d17 role=api -->
Render a full-screen placeholder when the graph has no nodes, offering a button to run `init` or `refresh` depending on whether `trie.toml` exists.

- Button is hidden until `trieConfigStore.loaded` is true, preventing premature action.
- Dispatches the chosen command via `trieCommandStore.run` and switches to the trie tab.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/GraphCanvas/index:ToolHud fingerprint=3806563650556238c594460f679abc74a2dc8cbf94d76f085471933698e26d46 body_fp=3f593bc02063342d38bfc00cd81faf0a6619c56196e435b30417d03bfdb01ce2 source_ref=9b45d68ec4b6794a58ffb4acd64d38b1fad11d17 role=ui -->
Render a transient bottom-centre HUD pill showing the active non-symbol tool (e.g. bash/fetch) name and output text, auto-hiding 3.5 s after the last update.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/GraphCanvas/index:ReplayControl fingerprint=bb39352646d2211fe29cf77418233ca624ce0ab6fd1524f94bbb16af847ebc8b body_fp=ea9c23826d83a12c559d9b078a87d707ece04a29709af45333d903cb0109914d source_ref=9b45d68ec4b6794a58ffb4acd64d38b1fad11d17 role=api -->
Render a replay-turn button that triggers `replayTurn()` and disables itself while replay is in progress; returns `null` when the cue log is empty.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/GraphCanvas/index:PaintOpts fingerprint=403fea17ccabe2d8533a12686a7adf3693ece5182ba4c4e3c03ba022a64e6747 body_fp=f1a0496522bfb0a6902243e0f7f1bf0130886a3dd6663597393ab6af89686473 source_ref=9b45d68ec4b6794a58ffb4acd64d38b1fad11d17 role=model -->
Options passed to `paintNode` controlling per-frame visual state of a canvas node.

- `reveal`: opacity/scale factor for enter animation; `0`=hidden, `1`=fully visible.
- `pulse`: normalised activity intensity `0–1`; drives the animated ring radius.
- `emphasis`: hover/selection scale boost `0–1`.
- `heat`: residual write-heat halo intensity `0–1`.
- `touchedGroup`: marks a component bubble as accessed this agent turn.
- `patchedCount`: number of pending-patch symbols inside a component bubble.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/GraphCanvas/index:paintNode fingerprint=5087d4c4df849a765b3cc34fbcd4053d7817bb40775d0d2c84b24c9271f6313a body_fp=4fab0ff8cccab0282bf6fa9e0879bcd42d2ca63c787af9e6e727f04422a9c38f source_ref=9b45d68ec4b6794a58ffb4acd64d38b1fad11d17 role=util -->
Paint a single `FGNode` onto the force-graph canvas, dispatching across `component`, `aggregate`, and `symbol` node kinds with activity rings, heat halos, selection strokes, patch badges, and on-demand labels.

- `opts.pulse` — drives animated activity ring/glow radius and opacity.
- `opts.heat` — renders a diffuse heat halo for recently-written symbols.
- `opts.reveal` — fade-in scalar applied to `globalAlpha` and node scale.
- `opts.emphasis` — scales the node up slightly when hovered or selected.
- `opts.touchedGroup` — draws a persistent "touched this turn" ring on component nodes.
- `opts.patchedCount` — renders an amber dashed ring plus a numeric pip on component nodes with staged patches.
- `opts.showLabel` — overrides label suppression; labels also appear when `globalScale >= 2.6`.
<!-- trie:end -->