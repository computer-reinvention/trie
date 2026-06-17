---
trie_version: 0.1.9
source: app/src/components/AGMCanvas/index.tsx
file_fingerprint: 3b8e8a8bf54e58340469af4598a005f8f2d1c70a5b33c6bdc99e296b1379f1ee
last_synced_at: '2026-06-17T16:38:08Z'
defines:
- kind: function
  qualified_name: app/src/components/AGMCanvas/index:isAgentRunning
  lines: 24-28
- kind: constant
  qualified_name: app/src/components/AGMCanvas/index:RADIAL_COLOR
  lines: 44-44
- kind: interface
  qualified_name: app/src/components/AGMCanvas/index:AGMCanvasProps
  lines: 49-51
- kind: interface
  qualified_name: app/src/components/AGMCanvas/index:Target
  lines: 55-63
- kind: interface
  qualified_name: app/src/components/AGMCanvas/index:Drawn
  lines: 70-84
- kind: constant
  qualified_name: app/src/components/AGMCanvas/index:VISIBLE_BUDGET
  lines: 88-88
- kind: constant
  qualified_name: app/src/components/AGMCanvas/index:MAX_DISPLAY_EASE
  lines: 93-93
- kind: constant
  qualified_name: app/src/components/AGMCanvas/index:MIN_GAP
  lines: 96-96
- kind: constant
  qualified_name: app/src/components/AGMCanvas/index:MODEL_TICK_MS
  lines: 103-103
- kind: constant
  qualified_name: app/src/components/AGMCanvas/index:APPEAR_EASE
  lines: 107-107
- kind: constant
  qualified_name: app/src/components/AGMCanvas/index:FADE_EASE
  lines: 108-108
- kind: constant
  qualified_name: app/src/components/AGMCanvas/index:JOURNEY_RATE
  lines: 112-112
- kind: constant
  qualified_name: app/src/components/AGMCanvas/index:PILL_PERCENTILE
  lines: 117-117
- kind: constant
  qualified_name: app/src/components/AGMCanvas/index:DOT_FOOTPRINT
  lines: 121-121
- kind: constant
  qualified_name: app/src/components/AGMCanvas/index:FIT_TARGET_FILL
  lines: 126-126
- kind: constant
  qualified_name: app/src/components/AGMCanvas/index:FIT_SCALE_MIN
  lines: 129-129
- kind: constant
  qualified_name: app/src/components/AGMCanvas/index:FIT_SCALE_MAX
  lines: 130-130
- kind: constant
  qualified_name: app/src/components/AGMCanvas/index:FIT_EASE
  lines: 133-133
- kind: constant
  qualified_name: app/src/components/AGMCanvas/index:SPOKE_REL_FLOOR
  lines: 138-138
- kind: constant
  qualified_name: app/src/components/AGMCanvas/index:HALO_MIN_R
  lines: 142-142
- kind: constant
  qualified_name: app/src/components/AGMCanvas/index:HALO_PER_MEMBER
  lines: 143-143
- kind: constant
  qualified_name: app/src/components/AGMCanvas/index:HALO_MAX_R
  lines: 144-144
- kind: constant
  qualified_name: app/src/components/AGMCanvas/index:HALO_NODE_MARGIN
  lines: 145-145
- kind: constant
  qualified_name: app/src/components/AGMCanvas/index:HALO_GAP
  lines: 147-147
- kind: constant
  qualified_name: app/src/components/AGMCanvas/index:HALO_LABEL_GAP
  lines: 148-148
- kind: constant
  qualified_name: app/src/components/AGMCanvas/index:HALO_MIN_MEMBER_FRACTION
  lines: 154-154
- kind: constant
  qualified_name: app/src/components/AGMCanvas/index:SYNTHETIC_MASS_CAP
  lines: 160-160
- kind: interface
  qualified_name: app/src/components/AGMCanvas/index:TooltipData
  lines: 163-176
- kind: function
  qualified_name: app/src/components/AGMCanvas/index:intentReason
  lines: 179-194
- kind: function
  qualified_name: app/src/components/AGMCanvas/index:AGMCanvas
  lines: 196-1292
- kind: function
  qualified_name: app/src/components/AGMCanvas/index:labelFor
  lines: 1297-1299
- kind: function
  qualified_name: app/src/components/AGMCanvas/index:smoothstep
  lines: 1303-1306
- kind: function
  qualified_name: app/src/components/AGMCanvas/index:advanceJourney
  lines: 1311-1324
- kind: function
  qualified_name: app/src/components/AGMCanvas/index:drawCrosshair
  lines: 1328-1340
- kind: function
  qualified_name: app/src/components/AGMCanvas/index:drawDot
  lines: 1344-1352
- kind: function
  qualified_name: app/src/components/AGMCanvas/index:drawSymbolPill
  lines: 1357-1394
- kind: function
  qualified_name: app/src/components/AGMCanvas/index:drawRegionLabel
  lines: 1399-1433
incoming_refs: 1
outgoing_refs: 24
---
<!-- trie:section symbol=app/src/components/AGMCanvas/index:isAgentRunning fingerprint=0747ec6bd56a370e2a0b1afc01571bfc7d465ec65d108608ce65692bd94cc8f3 body_fp=43634f04b225e3192f6864f6353f5a32027211f8beef238f8b1b95452f69f027 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=util -->
Return `true` if the currently active agent session has its `running` flag set.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:RADIAL_COLOR fingerprint=524ae44739b31b569ca830b2f093bca15714bb9fae3ceebbaafc760c2fb34acf body_fp=ab9eb8fe53a2350f82a61b536e2d913801c9fc5619e5fe4b1d54873360eb39ea source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=config -->
Slate hex colour applied to radial spokes drawn from the attention origin to each node.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:AGMCanvasProps fingerprint=d7f9e4da3e0b89f0bc287255056098c9282c2230976464a699b5297437585362 body_fp=bb69214252cf3acfe923bad7f51d9783343a53916571601a5a2f4cb3e808ffa2 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=model -->
Props for `AGMCanvas`; accepts an optional `className` to forward to the container `div`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:Target fingerprint=e56189c590b7a77d22f2f1cc6e86f8146ab5b6b4cbad161e15028e50ea36b018 body_fp=e524648dcfc8709f9a34948bee9954b49b895b2f29ae7192ce9ba759baeaa1d5 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=model -->
Model-computed placement target holding where a symbol wants to be; the render loop eases `Drawn` nodes toward these.

- `mass`: display mass (normalised, post-cap)
- `angle`: bearing used to position perimeter entry point
- `kind`: dominant intent, drives dot / pill / trace render style
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:Drawn fingerprint=cf23e8c2c093b85d8c874a5a964c7ca186792c6c021310d41245cdb47ab6c717 body_fp=b89e23ba3f3b9d2870c7fea1f6664c027b52aed96265a140b966bdb033efefe0 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=model -->
Animated render state for a single symbol on the AGMCanvas, tracking its smoothstep journey from spawn to target position.

- `sx/sy` — journey start, reset each time the target moves
- `tx/ty` — current journey target (world px)
- `p` — smoothstep progress `0→1`; resets to 0 when target changes
- `appear` — entry/exit alpha driver: `0` on spawn, eases to `1`; counts down to `0` on exit before the node is dropped
- `leaving` — set once the node leaves the target set; triggers perimeter-exit animation
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:VISIBLE_BUDGET fingerprint=18251a71d97e32d8a6d123e16ac85a58b8f3d805bfe909b8ab4b26efa12bdd0d body_fp=e450130df0bf1e7073afdd72fa60da02cb123ae20619d03630c659ebfd81ed11 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=config -->
Maximum number of symbols rendered simultaneously; excess symbols fold into per-role "+N" peripheral counts.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:MAX_DISPLAY_EASE fingerprint=433ecdb2dd6f128f4a20acb0690bd334cdad8eadb9dd21ad2a3d1c94768e23c5 body_fp=cc84515b5cb8654b351015121e6560fffe9efe48c69f1ef92828b136dc68c316 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=config -->
Per-frame easing rate at which `smoothedMaxRef` chases the instantaneous `maxDisplayRef`, preventing sudden rescaling of all node radii when a new hottest symbol appears.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:MIN_GAP fingerprint=10c55d5cfb93b1908afc5a23b3ebfdfe1dd5d344a5590919fdde48d3b13eb855 body_fp=ff150d409e4862265aba8b06aa79548e40b1c5482db067cab07e2734fb46e217 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=config -->
Minimum gap in world pixels enforced between pill footprints by the de-overlap pass.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:MODEL_TICK_MS fingerprint=8cf4802f2708a2a7594f98368b18bb3461a3abf952a8249eb8df83d90fda7eb0 body_fp=7e2137e4890bbfe9df3f9ba98a0c0310343480a834803e731bbbff1b748347f2 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=config -->
Minimum milliseconds between model-clock recomputes of layout targets during an active agent turn.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:APPEAR_EASE fingerprint=2685e1c1ac827d32432ea40a605767e5ebd13bb9728bb80da4dfb1c18f533844 body_fp=ea13300719388c75981432b806b9944fad63233363dc428995203ab2c3f3fd09 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=config -->
Per-frame increment applied to a drawn node's `appear` field as it fades in (0→1) on spawn.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:FADE_EASE fingerprint=42e3a94e4de8312625027faf917fc256a66aaf321935bbda9fb3ef5e1f5ffb47 body_fp=195cbeba2892c70a7f8521ff7be597ffd51ec0db5425405018ca8d04c31f1d02 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=config -->
Per-frame opacity decrement applied to leaving nodes until `appear` reaches 0 and the node is dropped.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:JOURNEY_RATE fingerprint=df07fac11259241059cea6f8f3b6a366c09d775ab5d9a199d9dec6c123f8a889 body_fp=0095126ff1d2cf87056dbc821e955ab89a5c3baeb7366357db4fc1ba8da402dc source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=config -->
Per-frame progress increment applied to each node's start→target journey; at 60 fps, a full traversal completes in ~0.4 s.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:PILL_PERCENTILE fingerprint=8be72254e76b4a7a100e011ec2b26a7532be0e9c38d20507d55def06205589ad body_fp=bf416f691d46953fb80613c3c26593023ffa43b6f0011e4bd9b6d504c65a05e7 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=config -->
Fraction of visible nodes (by attention mass) that render as named pills; the top 10% get labels, the rest render as anonymous dots.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:DOT_FOOTPRINT fingerprint=3581e6c7e3e3fdb06d0107f2bfa02d33b75f63d236ae6289fe55aaeff0a58c60 body_fp=4587b72eff4db10269298167a7b7188dd936ae94012682ed6c0aa33598893f44 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=config -->
World-space pixel radius a dot reserves during target-spread, keeping the exploration net compact rather than spaced like pill labels.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:FIT_TARGET_FILL fingerprint=93596d5b11325bcb49d6f991d711ae483be876f05c943e42adae623d9b7ee6ed body_fp=38934d65d2a6b499d8a167b805d35452e36bd763e48dcd3497aa67672dd22085 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=config -->
Fraction of the smaller canvas half-dimension the drawn field's outer radius should fill during auto-fit scaling.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:FIT_SCALE_MIN fingerprint=095d179bd76284b46dd00b94fcfc2410f73d108936a06680d28b3fd0b0b13b8e body_fp=44dc35405bac4b563a659127e53ee4da7dd6452030b604a7d5abc45bc5e2b51d source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=config -->
Minimum allowed value for the auto-fit scale, preventing a single near-centre node from zooming the canvas to an unusable level.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:FIT_SCALE_MAX fingerprint=e4f14d6851b5f08d65f93d9bc5a1edc758a5067da07ef5b86c0e034e9e82f9fc body_fp=ec09209b06b8679fa4aeff4c53b8639f21a1dba03e5052f69d0441ee8a44bfbf source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=config -->
Upper clamp on the auto-fit scale, preventing a sparse field from zooming to an unusable level.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:FIT_EASE fingerprint=a5f36f5d21683850d1f77441bb790a35e992d26f179883fc6596425a5c569f44 body_fp=184bd8d4165dee8c07a8cb6c99ad51a7c07587a508cb2fa8b61a9a7d514f478b source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=config -->
Per-frame easing rate applied to `fitScaleRef` so zoom-to-fit settles gradually rather than lurching when nodes enter or leave.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:SPOKE_REL_FLOOR fingerprint=31a881c58e1248ae8eabe42ec39417c6b51d30743f80f3c73f4e729385558a4b body_fp=ec1b8e3afb4804c15ea28b5f0ae715dc4e11051fedfab00cbc9797ea25ef7d72 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=config -->
Relative-heat floor (0.12) below which a non-hovered, non-pill node draws no radial spoke, suppressing cold peripheral spokes to keep the warm ones legible.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:HALO_MIN_R fingerprint=f4441fa8932ef45bbe0990d2b1bcb3edb089cbcb67f826158f12344e1b3d9d8e body_fp=00c6397581c553f512543769e3683d086f5d19574c2a2f66fe87b16d39b20237 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=config -->
Minimum halo radius (world px) applied to a 2-member region.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:HALO_PER_MEMBER fingerprint=0229a9877a6170db8818060bb153a095daf221141a6706d5ee002e783cb403b3 body_fp=7e77ef07757cef28a61303e6ed87a3638683008dcf9c3be96d5a091596d47e45 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=config -->
Multiplier applied to `sqrt(memberCount)` when computing a region halo's radius, growing it gently with cluster size.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:HALO_MAX_R fingerprint=7bc6e41dff11700057f22ff684a0cf418e225b8bd5ce19d2af5a89950728cc88 body_fp=d29f1a704457afa6ae5d921b13254fd239967bea8e77b26ba9105eb633e0e4a5 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=config -->
Hard cap (world px) on region halo radius; no halo ever exceeds this value.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:HALO_NODE_MARGIN fingerprint=4627c0c85cb40ac908661ae8cf49cecb5f6f3a02b28c829279a8a65b941d0030 body_fp=e110887470ecf9d20c0faa968a63c3d5cab579425f72fe8b1a9cd2cb07b12fb0 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=config -->
Minimum world-px padding added beyond the outermost member's centre when computing a region halo radius, so member pills sit comfortably inside rather than on the halo edge.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:HALO_GAP fingerprint=d0ce1580cfe47fe9500abeafd5753787c4c7e8847b6cc967ea0e95a8d36d1a3f body_fp=b1561b95b2ff0138ce5e652e9b041ff0153dc884adedcbbfa40aeb59a012fc19 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=config -->
Minimum visual gap (world px) maintained between two adjacent region halos during radius capping.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:HALO_LABEL_GAP fingerprint=bd790c588cf2b2cd34701bdc4893696570f5b14c81228f15c3b1e825dab96da8 body_fp=d1e2e621f8cda6be7fa26ff83a6b4a2b6762c1c081911c248df9569f45cd63ea source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=config -->
World-px gap between a region halo's top edge and its region heading label.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:HALO_MIN_MEMBER_FRACTION fingerprint=06dce0ac8016033860a2eda295d370b7cf659bdcb2202b458a8cf37c3cd118cd body_fp=3d81f5142db7305d50342ef822f553d8ca04bf0ff3d24e8d07cfde1e00b5c791 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=config -->
Minimum share of on-screen members a role must hold (≥ 8%) to render as a halo region; floored at 2 members so a halo never wraps a single symbol.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:SYNTHETIC_MASS_CAP fingerprint=c5fb079be78de7829e3a333f579a57cba8ab5a7bb16582dc9f98ec24f14c7bdb body_fp=2ffbfd769e3f4c28052ae8a857640ac2faaae15446136b706112a0e073bb6845 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=config -->
Caps a lumped-surface synthetic node's display mass to this fraction of the hottest real node, preventing plumbing nodes (Filesystem/Bash/Web) from dominating the map centre.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:TooltipData fingerprint=3443f1bf2aebf694ad48936996876d87d84418940ba46094392d9fa5972b8559 body_fp=9101bf49fdaa7704aadce9dc00c17c2b6724ce88220a4c54b80278b1b17e79d8 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=model -->
Shape of the codelens-style hover tooltip shown over a hovered canvas symbol.

- `reason`: human-readable intent label (e.g. `"read"`, `"traced — part of the reasoning path"`).
- `reasonColor`: hex colour matching the intent kind, used to tint the reason pill.
- `oneLiner`: node's `one_liner` from the system model, or full path for per-file synthetics.
- `liveMass` / `historicalMass`: raw AGM mass values displayed in the tooltip footer.
- `inbound` / `outbound`: graph degree counts; absent when the node has no metadata entry.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:intentReason fingerprint=ebef1be6bec217d49c88e8f4492e43cc57587281a7e84d349bbdbc043f4a047a body_fp=27a580d127a1461e5113cc1c9d9c86f4f3f9a2bae0c433332afeb7122897bcd0 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=util -->
Map a `NodeMass` intent kind to a human-readable label and hex colour for tooltip display.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:AGMCanvas fingerprint=0d5eeb6cdaaec0d4d945cdbd975363374a08ec0121a11122a44eaa19ab4a7c2c body_fp=2ed4ad225ff6fbb1a1b8325361b43b25f2789cdcebc51aa24aed140dc7263cf2 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=api -->
React component that renders the AGM cognitive-state canvas: a polar attention map where symbol distance from a fixed crosshair encodes live relevance, animated via a dual-clock model/render loop.

- `className` — forwarded to the outer wrapper `div` for layout sizing.
- Runs two clocks: a model clock (`recomputeTargets`) triggered on tool calls and a slow decay tick; a rAF render clock (`loop`) that eases `Drawn` nodes toward `Target` positions via smoothstep journeys.
- Saves and restores per-session frozen layout snapshots via `window.trie.agmSnapshotSet/Get`; clears stale nodes on session switch.
- Symbols render as monochrome name pills (top `PILL_PERCENTILE` by mass, plus all deliberate-kind nodes) or anonymous dots; role regions render as dashed halos with uppercase headings only after a turn ends.
- Hover resolves to the nearest node or edge (spoke / attention trace) within hit tolerance; right-click opens a context menu via `buildSymbolMenu`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:labelFor fingerprint=c5716a815b68d4688c5702e798b4206c9dd0f311528beb75b88f53a395fe68c4 body_fp=3e9b6a525050b594a4a832d7377f4d54fe3779ee436cd66bfa84f519620f7871 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=util -->
Return a short display label for a qname: synthetic basename, last colon-delimited segment, or the raw qname as fallback.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:smoothstep fingerprint=9f01da352b78c372f1f3b2ef61b2d2c7136c24c798a60cd81c79c810046eddad body_fp=0d018cd6a2e0d0137db9c6d734b1ec46d2f07e0a85aba766322e813a4b800172 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=util -->
Apply Hermite ease-in-out (slow start, fast middle, slow end) to `t`, clamped to [0, 1].
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:advanceJourney fingerprint=49a4edd6ebab79cc7b23fc726e4c17334d928160b33c6a79f9dcb91158a5c666 body_fp=a21e265a68d4d1a7bac523ff0ce89cee5e1824fe61892a48752c9bd92f1e1618 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=util -->
Advance a `Drawn` node's journey by one frame, updating its position via smoothstep interpolation from start to target and returning the L1 displacement.

- `node` — mutated in place; `p`, `x`, `y` are updated each call
- Returns `0` when already at rest (`p >= 1`), otherwise the Manhattan distance moved this frame
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:drawCrosshair fingerprint=8d7601d19fea12a5059db91b524b9752f01b055fb87b9c503062115fa60e987a body_fp=9afbfb3b3a7c8b30d7a256ea5e237f18ccbfeb6fe1a91460dda9471e7a0f8074 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=util -->
Paint the fixed centre crosshair at the canvas origin `(0, 0)`, representing the current attention origin.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:drawDot fingerprint=c840d041506ea9ac983da761aa16ae4506cbd838bc417260424aff747d74cc96 body_fp=62949845d8a6db5826e1f7d1d15bd224c05cd2a5e48675a3d167490ca9414c89 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=util -->
Render a small monochrome dot for a low-attention symbol onto `ctx`, scaling radius and opacity with `rel` and `appear`.

- `rel` — normalised relevance [0–1]; drives radius (2.2–4.8 px) and opacity.
- `appear` — entry/exit fade progress [0–1]; multiplies both radius and opacity.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:drawSymbolPill fingerprint=7b6accef6c0e1b3265ee1389dc0084a41944ab72713b7a7e67abb7b303a4d349 body_fp=4c6f6029c47b09015b15bbeae578654c06aca1ffec801c16459f9d3bb63510e5 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=util -->
Draw a monochrome rounded-chip pill centred at `(cx, cy)` with `label`, scaling background and text opacity by `opacity` and boosting weight/brightness when `hot`.

- `hot`: renders bold text (`600`) and a brighter chip background (`#33415560` vs `#1e293b`)
- `scale`: uniform scale applied to width and height; defaults to `1`
- `opacity`: controls `globalAlpha` for both fill and text independently
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AGMCanvas/index:drawRegionLabel fingerprint=89f40d01d6e736e98c2c4edb684db7bd1ea9f242f5fc1e5da72adaa1af1f2200 body_fp=ad56c92b2b9f009c7cb3ebeb9fb3b517e11990cc00c70a888945a5086b77aa00 source_ref=74863921a1142db01087b73f2ab20d8820ee3db7 role=util -->
Paint a role region heading onto `ctx`: uppercase, letter-spaced, muted, with a halo-facing underline.

- `below` — when `true`, underline draws above the text (label is below the halo); default places it below.
<!-- trie:end -->