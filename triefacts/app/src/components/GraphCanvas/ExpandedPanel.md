---
trie_version: 0.1.9
source: app/src/components/GraphCanvas/ExpandedPanel.tsx
file_fingerprint: 22276bd35b65e41351129c4c5545910657d631c40ac25180331752e072dcfc2e
last_synced_at: '2026-06-17T16:38:09Z'
defines:
- kind: interface
  qualified_name: app/src/components/GraphCanvas/ExpandedPanel:PanelNode
  lines: 16-27
- kind: interface
  qualified_name: app/src/components/GraphCanvas/ExpandedPanel:PanelLink
  lines: 28-32
- kind: interface
  qualified_name: app/src/components/GraphCanvas/ExpandedPanel:Frame
  lines: 35-40
- kind: interface
  qualified_name: app/src/components/GraphCanvas/ExpandedPanel:ExpandedPanelProps
  lines: 42-44
- kind: function
  qualified_name: app/src/components/GraphCanvas/ExpandedPanel:ExpandedPanel
  lines: 46-647
- kind: function
  qualified_name: app/src/components/GraphCanvas/ExpandedPanel:ownerOf
  lines: 652-657
- kind: function
  qualified_name: app/src/components/GraphCanvas/ExpandedPanel:ownerClassOf
  lines: 660-662
incoming_refs: 1
outgoing_refs: 11
---
<!-- trie:section symbol=app/src/components/GraphCanvas/ExpandedPanel:PanelNode fingerprint=96aa1c24ea73980ed1154479d4e3d32a2af76d1883f234eb8885d4716a85b60f body_fp=8572e88408ef6902deae61449ac2cad8adae7235825f07a31ebba479c8022ff7 source_ref=1ed1c3b0a906576ce88fd5d44e0d8f0680208314 role=model -->
Node shape used by the `ExpandedPanel` force-graph, extending ForceGraph2D's node with rendering and layout fields.

- `outside`: marks a peripheral system node connected to the group but not a member
- `val`: visual radius, derived from salience/cls via `nodeRadius`
- `folded`: count of child symbols collapsed into this node (e.g. class methods)
- `fx`/`fy`: pinned coordinates set after engine stop to freeze layout
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/GraphCanvas/ExpandedPanel:PanelLink fingerprint=5ba20ba7c96d2e2a680cafb61c817615e3869f4af04068f9ebd5c1b2bdf03624 body_fp=67aa6eefc5de8352bc501c540e882244401f88a65fad21ecd2f6fa9a9c3ba246 source_ref=1ed1c3b0a906576ce88fd5d44e0d8f0680208314 role=model -->
Represents a directed edge in the `ExpandedPanel` sub-graph.

- `outside`: marks edges connecting a frame member to a peripheral system node outside the group.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/GraphCanvas/ExpandedPanel:Frame fingerprint=ed3d86919f64bff5b2f13e973824a1e0cbceb4236bae03fd6789e91e5a98e493 body_fp=c9602fe2b0653bacf3e371d73e967f82de976b960f53d6451d7749c8024b47e7 source_ref=1ed1c3b0a906576ce88fd5d44e0d8f0680208314 role=model -->
Represents one level in the `ExpandedPanel` drill stack, capturing the group or symbol currently displayed.

- `key`: group key (role/subsystem name) or symbol qname identifying this frame.
- `members`: the `SystemModelNode` instances visible at this drill level.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/GraphCanvas/ExpandedPanel:ExpandedPanelProps fingerprint=de2a9877f72d1e8f57ea4845ce9cac9b104e851e439f5c1e79ea00f8ff80e4f9 body_fp=1bcc76e49976c220fd63327e79a106c539955c921df18592d369cd6440402242 source_ref=1ed1c3b0a906576ce88fd5d44e0d8f0680208314 role=model -->
Props for `ExpandedPanel`; supplies the screen-space anchor point used to position the sub-graph panel.

- `anchor`: pixel coordinates of the role node, or `null` before the first layout frame.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/GraphCanvas/ExpandedPanel:ExpandedPanel fingerprint=0790bde0bcbd7cef5f629345b7889b5aaf126ae6f02cb4f78848cb9b02ed4c9c body_fp=ad1704f186cb40740c797ee13b3433259c12d9f3f31e3fa3fa11a50cbae09def source_ref=1ed1c3b0a906576ce88fd5d44e0d8f0680208314 role=api -->
Render a floating 560×440 force-graph panel showing the members of the currently focused role/subsystem group and their call-interdependency edges, with drilldown navigation, agent-activity overlays, and a hover tooltip.

- `anchor` — screen coordinates of the role node; panel is clamped to the viewport below it.
- Returns `null` when no `focusedExpansion` is active or the drill stack is empty.
- Drill stack is reset whenever `focusedExpansion` or `axis` changes; clicking a member with children pushes a new frame, breadcrumb allows popping back.
- Minor symbols (`inbound_count ≤ 1`, non-landmark) and methods whose owner class is already visible are folded; clicking a folded owner drills into it.
- Up to 24 highest-degree external neighbours are shown as dimmed peripheral nodes.
- Force layout runs 60 warmup ticks then freezes (all nodes pinned); soft-pans to `lastTouched`/`selectedQname` without re-running simulation.
- Per-node pulse values are eased per frame toward `runtime.activity`; rendered as breathing halos colour-coded by agent state (read/scan/write).
- Agent tool-output notes appear as word-wrapped canvas popups above nodes, fading out after 6 s.
- Escape key calls `collapseTransient()`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/GraphCanvas/ExpandedPanel:ownerOf fingerprint=5154bed0c8337a6521eae8d36993093a198ec14ff1c8bb4811093082d0636339 body_fp=1863a5fbb372eeee86b426c9ee36a46d2f6f7c2540654202a180a5503a93ded4 source_ref=1ed1c3b0a906576ce88fd5d44e0d8f0680208314 role=util -->
Return the parent qname for a dotted symbol (e.g. `mod:A.b.c` → `mod:A.b`), or `null` for top-level symbols.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/GraphCanvas/ExpandedPanel:ownerClassOf fingerprint=b1b2990157737b1665f330a6e1fab37f5625cef9331feddef3f1cde6eab41e7a body_fp=bc59a66f8c477eeac606ce05d40a5f4d98e0494cf9e3d60db60982b73d15e228 source_ref=1ed1c3b0a906576ce88fd5d44e0d8f0680208314 role=util -->
Return the owning class qname for a method symbol by delegating to `ownerOf`.
<!-- trie:end -->