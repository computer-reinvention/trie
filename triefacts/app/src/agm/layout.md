---
trie_version: 0.1.9
source: app/src/agm/layout.ts
file_fingerprint: 931cb3c54bf2cce1baefa852e2995b8043ad3848ec6016fea011310a282250a0
last_synced_at: '2026-06-17T16:37:20Z'
defines:
- kind: constant
  qualified_name: app/src/agm/layout:R_MIN
  lines: 24-24
- kind: constant
  qualified_name: app/src/agm/layout:R_MAX
  lines: 26-26
- kind: function
  qualified_name: app/src/agm/layout:radiusForMass
  lines: 31-35
- kind: function
  qualified_name: app/src/agm/layout:roleBaseAngle
  lines: 39-44
- kind: constant
  qualified_name: app/src/agm/layout:ROLE_RING_RADIUS
  lines: 51-51
- kind: function
  qualified_name: app/src/agm/layout:roleAnchor
  lines: 56-59
- kind: function
  qualified_name: app/src/agm/layout:symbolAngle
  lines: 65-82
- kind: interface
  qualified_name: app/src/agm/layout:PolarPlacement
  lines: 84-90
- kind: function
  qualified_name: app/src/agm/layout:placeSymbol
  lines: 95-112
- kind: constant
  qualified_name: app/src/agm/layout:SPEED_FLOOR
  lines: 119-119
- kind: constant
  qualified_name: app/src/agm/layout:SPEED_CEIL
  lines: 120-120
- kind: function
  qualified_name: app/src/agm/layout:ease
  lines: 126-146
- kind: interface
  qualified_name: app/src/agm/layout:RoleCluster
  lines: 157-163
- kind: function
  qualified_name: app/src/agm/layout:applyClusterCohesion
  lines: 171-189
- kind: function
  qualified_name: app/src/agm/layout:applyAnchorCohesion
  lines: 198-250
- kind: constant
  qualified_name: app/src/agm/layout:CLUSTER_ARC_PER_MEMBER
  lines: 255-255
- kind: constant
  qualified_name: app/src/agm/layout:CLUSTER_ARC_MAX
  lines: 256-256
- kind: function
  qualified_name: app/src/agm/layout:tightenRolesToFit
  lines: 269-315
- kind: interface
  qualified_name: app/src/agm/layout:BudgetResult
  lines: 322-326
- kind: function
  qualified_name: app/src/agm/layout:applyVisibleBudget
  lines: 328-355
- kind: function
  qualified_name: app/src/agm/layout:computeRoleClusters
  lines: 360-389
- kind: interface
  qualified_name: app/src/agm/layout:Sized
  lines: 408-419
- kind: function
  qualified_name: app/src/agm/layout:overlapXY
  lines: 422-427
- kind: function
  qualified_name: app/src/agm/layout:hasNoOverlaps
  lines: 430-438
- kind: function
  qualified_name: app/src/agm/layout:deOverlap
  lines: 441-487
- kind: function
  qualified_name: app/src/agm/layout:separate
  lines: 494-530
- kind: function
  qualified_name: app/src/agm/layout:hashName
  lines: 534-538
- kind: function
  qualified_name: app/src/agm/layout:pullBack
  lines: 542-560
- kind: function
  qualified_name: app/src/agm/layout:clearAt
  lines: 562-572
- kind: function
  qualified_name: app/src/agm/layout:fanOut
  lines: 574-578
- kind: interface
  qualified_name: app/src/agm/layout:LayoutInput
  lines: 595-609
- kind: interface
  qualified_name: app/src/agm/layout:RegionLabel
  lines: 611-615
- kind: interface
  qualified_name: app/src/agm/layout:LayoutResult
  lines: 617-622
- kind: function
  qualified_name: app/src/agm/layout:separateClusters
  lines: 628-690
- kind: function
  qualified_name: app/src/agm/layout:translateCluster
  lines: 692-703
- kind: function
  qualified_name: app/src/agm/layout:syncPlacements
  lines: 706-717
- kind: function
  qualified_name: app/src/agm/layout:resolveLayout
  lines: 719-792
- kind: function
  qualified_name: app/src/agm/layout:regionLabelBoxes
  lines: 797-839
incoming_refs: 11
outgoing_refs: 0
---
<!-- trie:section symbol=app/src/agm/layout:R_MIN fingerprint=18df7992d572e157ca76d0d239257eb49b438f93daa326fc655819351683df4f body_fp=87a357745ad829e4ca5d4c6e45bdcd17931bd0bbfb3df4ecc1b894bbd8fa1089 source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=config -->
Minimum orbit radius (world units) at which the hottest symbols sit — reserved clear of the centre crosshair.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:R_MAX fingerprint=9aa034fed94341736dfe49aacd1392c3662edcd8f7ab1bc1e1c8900bb5c85df5 body_fp=cda85811c12281e69dc331e310fb94078631e30ae8ade49435cdd2342c017e91 source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=config -->
World-unit radius of the perimeter where cold and newly-discovered symbols are placed.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:radiusForMass fingerprint=ec7ac4b94143ab2d7f696904a4483ea04758bec2a9195cddc16198773df7fd86 body_fp=8f07809d9d73f502075cee02d8926500a71ee8c832b71104e42ab937e1cb0f0b source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=domain -->
Map a log-compressed display mass to a world-unit radius between `R_MIN` and `R_MAX`.

- `displayMass` — already log-compressed relevance score for the symbol.
- `maxDisplay` — display mass of the current hottest symbol; used to normalise so the hottest always reaches `R_MIN`.
- Returns `R_MAX` when either argument is ≤ 0 (cold/unknown symbols start at the perimeter).
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:roleBaseAngle fingerprint=eaa39c68e5110e069330acbfc3de6e1bba1fa6a673b62c93c5b78685aeaacb3e body_fp=b4579a7fca61f02e4b4ce4fe310d714f87f2b469e32df271d5a1539cee3e0a99 source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=domain -->
Return the deterministic base angle (radians) for `role` by dividing the circle evenly among alphabetically-sorted unique roles, offset by −π/2 so index 0 sits at the top.

- `roles` — full list of active roles; deduplicated and sorted internally.
- Returns angle in `[−π/2, 3π/2)` anchored at 12-o'clock for the first role.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:ROLE_RING_RADIUS fingerprint=b27721769c0204b8b4514f4cf97463deb10209cefb0b03584e5571e443d21ef7 body_fp=5f85d5f80aee3ac309c3c32704e6431c7d842a154a0645b2e5faee188550cf8c source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=config -->
World-unit radius at which every role anchor is placed, computed as the midpoint between `R_MIN` and `R_MAX`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:roleAnchor fingerprint=c2230f1b8127db97f499989a4fb97615c93a5dff32a7ebcc6439e74c87205781 body_fp=0624be2a2a7c648dbf1dfbfd3c9fd334c917127e24dd17acc4b79caab03dde72 source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=domain -->
Return the Cartesian anchor point for a role on the role ring, derived from its stable base angle.

- `radius` — defaults to `ROLE_RING_RADIUS`; pass a custom value to place the anchor on a different ring.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:symbolAngle fingerprint=66cf503d8825940b76ce9a59939010205b6393fe251b1860406c212c6f91f22a body_fp=aada802c15679f3e9b6490526770fc9c376ca076c8156ace9392b2c34cc26915 source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=domain -->
Compute the stable polar angle (radians) for a symbol, combining its role's base bearing, a qname-derived jitter, and a historical-mass pull toward the role's arc centre.

- `arc`: total angular spread allotted to a role's members; default `0.9` rad.
- `historicalMass`: higher values tighten the symbol angularly toward the role centre (saturates at 5).
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:PolarPlacement fingerprint=39ee36ab80d9d160e376ebbc97cd39151ef2b80f7ca0e475d7eaf3dce815a963 body_fp=8686e125a2731e4da79c1550f2f7efc338fe7a61f49f3cf1bbd3261f799d8554 source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=model -->
Holds the computed polar target position for a single symbol on the AGM canvas.

- `radius` — distance from canvas origin (world units); encodes live relevance
- `angle` — stable bearing (radians); encodes role + per-symbol jitter
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:placeSymbol fingerprint=2f2ed3f6ea81d10ca83788e377f78c4dc0d811be3855987b9d78fad331ea0e8b body_fp=46b0196311cb424e742579a36953133e96be80104c48e8d726b64a9c1aa90949 source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=domain -->
Compute the target `PolarPlacement` for one symbol by combining `symbolAngle` and `radiusForMass` into Cartesian coordinates.

- `displayMass` / `maxDisplay`: normalised relevance used to derive radius via `radiusForMass`.
- `historicalMass`: passed to `symbolAngle` to anchor the stable bearing.
- Returns a `PolarPlacement` with `x`, `y`, `radius`, and `angle`; the renderer eases toward this each frame.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:SPEED_FLOOR fingerprint=2140917ab613b7f5c09a5973c2f921f12f53b14dd824af8710b1250c84afe293 body_fp=781a4154fb4703af2eb958ca91a7b59ea600c9f47a2494c48053e81098017884 source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=config -->
Minimum easing step in world px/frame; movements below this threshold snap directly to the target to prevent an infinite crawl.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:SPEED_CEIL fingerprint=0c10766053c5811ab22c6a81356d62428de10616d5d55edbf4eb9ae7ce1dc84f body_fp=6371a28d03f571be086e8d397d397c871a92588b2942dde7e6ab2d9e4bfe0f9a source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=config -->
Maximum easing step applied by `ease`: 12 px/frame, preventing a large target jump from producing a visible lurch.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:ease fingerprint=20e3420d8131a5456d6910c993164c5ef73a3dd94a0a066a64cd8d182b998806 body_fp=cb19f7d7660d24d32477d7675d86bb1f8014415757a39a888a59b40569f8f09a source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=util -->
Advance `cur` one frame toward `target` using proportional easing clamped to `[SPEED_FLOOR, SPEED_CEIL]`, snapping to target when the gap is already within the floor.

- `alpha`: proportional step fraction per frame; default `0.16`
- `dist`: Manhattan distance remaining after the step, for rest detection; `0` when snapped
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:RoleCluster fingerprint=4cdc23b67248ef1b5a95698800e1f181fb154901a8bab8b6438319550b5bf784 body_fp=423872ace6a548d11792553b9a1f89c0c6d5982ad97138266dd130947109c5f2 source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=model -->
Describes the computed centroid and spread of one role's active symbol cluster.

- `maxRadiusFromCentroid` — furthest member distance from centroid; used to size the halo and offset the pill tag.
- `count` — includes single-member roles; callers gate halo rendering on `count >= 2`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:applyClusterCohesion fingerprint=df20d34cd8c87766e4b3d429d8a2f296b272ad787570119f9ec9833e152b4cc7 body_fp=6c7794d8f5d5676d57dfad92c30fee061025a35f98247fcbdbec9274533a2896 source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=domain -->
Mutate each placement toward its role's centroid, scaling cohesion by historical mass so frequently-visited symbols cluster tighter.

- `baseCohesion` — floor cohesion fraction applied even with zero history
- `histBoost` — additional cohesion added linearly up to `historicalMass == 5`
- Skips roles with fewer than 2 members (lone symbols are unaffected)
- Returns the same `placements` array, mutated in place
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:applyAnchorCohesion fingerprint=16038681257766f11290426971e12885d644aaecfc1f4729dac5a5ed76f79cc9 body_fp=44ecbecf051c4fef18659f5da1a149cdda51f18707c3d4ca01af16fdb2b38adf source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=domain -->
Pull each multi-member role's placements toward that role's fixed `ROLE_RING_RADIUS` anchor, then fan members angularly around the anchor bearing to prevent coincidence.

- `cohesion` — blend fraction toward the anchor (0–1); default 0.72 keeps cluster centre stable while preserving individual relevance radii.
- `roleList` — defines angular ordering of roles; pass active roles for even on-screen spread.
- Lone symbols (role count < 2) are skipped entirely.
- Mutates `placements` in place and returns the same array.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:CLUSTER_ARC_PER_MEMBER fingerprint=dcf493c9143d71cfd7027f9d2c019afdd4cc1a9230633880395ba579ddeeb360 body_fp=4347765dfed4b906cf960ca5c1bb7f503f64761aa319fecbd2b97ba97094e34f source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=config -->
Angular spread step (radians) added per cluster member in `applyAnchorCohesion`; multiplied by `(count - 1)` then capped at `CLUSTER_ARC_MAX`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:CLUSTER_ARC_MAX fingerprint=6392be2fbef383b991a93428a4428fde1d9108ea9dcccf86527975f506eb3963 body_fp=353a827fe7a4bfda3d4c531c5eb36757c449adbc002b1dd004b3cb8122d86a13 source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=config -->
Maximum total angular spread (radians) of a role cluster's member fan in `applyAnchorCohesion`, capping `CLUSTER_ARC_PER_MEMBER * (count - 1)` so large clusters don't wrap the ring.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:tightenRolesToFit fingerprint=8d27904dc3e96e44a5c36fc1388e2460b34dccb437657919f8d53ed59d0fcf50 body_fp=aeb074facf295abf5efd4f48688b8ec9596df20fc4ca4a52336927f48f883f6c source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=domain -->
Scale each halo-eligible role's members toward their centroid so the cluster's covering radius fits within half the distance to the nearest neighbouring halo, minus `gap` and `nodeMargin`.

- `opts.minCount` — roles with fewer members are skipped entirely.
- `opts.gap` — clearance subtracted from the half-distance budget before clamping.
- `opts.minRadius` — floor on the budget; cluster is never squeezed below this covering radius.
- `opts.nodeMargin` — additional margin subtracted from the budget alongside `gap`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:BudgetResult fingerprint=536d33d57ce6db2b2a12ce99e2ad1e45574c6a0bcd71e89c76ce49d19cd99364 body_fp=136205ae8706acea9d0a23349fa697a9758a152f1072e1fcc663e8fdfeb5d069 source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=model -->
Return type of `applyVisibleBudget`; splits placements into visible and folded sets.

- `kept` — placements within the display budget (including all pinned symbols)
- `foldedByRole` — count of folded-out symbols per role tag
- `foldedTotal` — total count of folded-out symbols across all roles
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:applyVisibleBudget fingerprint=344503e2cee25dacf521bc77d79f7febc92caf129b1453e568052f29d6e27a1f body_fp=1c6248af6f06d860ec06c268f1eb63e311d7bce787322a048208235f92915209 source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=domain -->
Trim `placements` to a `budget`-sized visible set, keeping all pinned symbols and the hottest non-pinned symbols by display mass; returns folded counts per role for overflow indicators.

- `budget`: max visible placements; default 60; bypassed if `placements.length <= budget`.
- `pinned`: qnames exempt from folding; always included in `kept` regardless of budget room.
- `foldedByRole`: count of folded placements grouped by role tag (`"untagged"` if unmapped).
- `foldedTotal`: total count of placements dropped from view.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:computeRoleClusters fingerprint=31fe0f392f5f4bb3e30d597eadbc9852c8370354a5e0ff12b89029f2035f6a16 body_fp=f41e7ed72fc7ab88c52a5012629d95589e1f2df153a83bf0de4ab7ef366a13d8 source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=domain -->
Compute the centroid and max spread of each role's members across `placements`, returning one `RoleCluster` per role.

- Roles with a single member still produce an entry; callers decide whether to render a halo.
- `maxRadiusFromCentroid` is the furthest member distance from the centroid, used for halo sizing.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:Sized fingerprint=324030268797398387c203bf8caa6b26b0622e76650c69e77757ecdc733371ec body_fp=f02c02270518ded8b20818792a6f2fb34bf9fc96418ce55a4c421f7d747a8711 source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=model -->
Represents a node footprint for overlap resolution, holding position, axis-aligned half-extents, and optional pin state.

- `hw` / `hh`: half-width and half-height of the bounding box in world units.
- `fixed`: when `true`, `deOverlap` never moves this node; other nodes yield to it instead.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:overlapXY fingerprint=df98dc7bdd184d33e7db48bb0f632f35af5466f6dfadf20486587d0ec88483f8 body_fp=5acbf42f859b17fd0ec4fff09897d387bfb4d1f0a4f46d64dd37cf072f6bbef9 source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=util -->
Compute the signed overlap on each axis between two `Sized` nodes, including `pad` clearance; positive values indicate actual overlap.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:hasNoOverlaps fingerprint=47a2356d0f28fadae597c74882258f0c923df57f8071e0e9d962f6b3372f16a8 body_fp=e0e856afa0b96a5851d917836deffdf3f9ff597d18413cc2705c559d04d7c2bd source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=util -->
Return `true` iff no two `Sized` nodes in `nodes` have overlapping axis-aligned footprints, using `pad` as the minimum clearance gap.

- `pad`: minimum gap between footprints in world units; defaults to `4`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:deOverlap fingerprint=6dbcbb0a2471a58980bad42879b10ce5d2892e71bba3c86d516df6217ca41573 body_fp=10034744e381377ae3498c17ec5d0479f558b75b11575a4fd71459d5e98d114a source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=domain -->
Resolve all overlaps among `nodes` in place, guaranteeing `hasNoOverlaps()` on return.

- `nodes` — mutated in place; `fixed` nodes are never moved.
- `opts.pad` — minimum gap between footprints; defaults to `4`.
- Each pass calls `separate` on every overlapping pair then `pullBack` toward each node's original polar target.
- Falls back to radial `fanOut` for up to 200 guards if 400 passes do not converge.
- Returns the same `nodes` array.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:separate fingerprint=d5a1abeee8ccb2248ffaef8684370148c6fedecfd4e0c9d29dc3b9822084965c body_fp=74258c0bc91580e645ce681951b41340ee3b41c804267a346a34ec6dcd0f9153 source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=util -->
Push two overlapping `Sized` nodes apart along the minimum-translation axis, respecting `fixed` pins and biasing separation tangentially to preserve radius.

- `ox`, `oy`: pre-computed overlap extents on each axis (from `overlapXY`).
- Both `fixed`: no-op; one `fixed`: movable absorbs the full displacement; both movable: split evenly.
- Near-coincident pair (centres within 1e-6): uses `hashName` to derive a deterministic separation angle.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:hashName fingerprint=657b05e98052c22d7c78cbfe147247729092b8513a6148f7c3b36614ff17d708 body_fp=18cb5140dbf0ba0f21e7f9563d0e4f761b5f460f908bfed339b2ddc7480a6daf source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=util -->
Compute a deterministic 32-bit hash of a string using a polynomial roll with base 31.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:pullBack fingerprint=cd7cc6ee44a28a629ebf11efea3ef92f6c8cb8b0c8e8002c61901ca220f3499e body_fp=1fc04216b2bd4d15a91f2b08b62f39698801c5d7e858442e3bad1905c675b554 source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=util -->
Pull node `i` toward its target position `(tgx, tgy)` by the largest overlap-free fraction, found via 12-iteration binary search.

- Skips nodes where `fixed` is true; anchors never move toward a target.
- Mutates `nodes[i].x` and `nodes[i].y` in place.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:clearAt fingerprint=9737858accebdefd759da70ed3aa19a7627c9bd5a4894e39ccbb5a787b0ffe41 body_fp=9ebc01b4c52a6959c5399ecae3bf705cee4b1e8eec7d072fbf2d160258b1de5e source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=util -->
Return `true` if placing node `i` at `(cx, cy)` produces no axis-aligned overlap with any other node in `nodes`, respecting `pad` clearance.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:fanOut fingerprint=20292724ff2bbe4e5608aeed08ba80680cf63dbc9933decb9b6ee87b8443f2ad body_fp=70f74081c9c63fda62a09272dcf855692b96061e876c1bb3ba4bfa735d01d7db source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=util -->
Push a `Sized` node radially outward from the origin by `amount` world units.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:LayoutInput fingerprint=70d98ba7cbec7d4a784a24b78a8a2e7a7cdd7fa9fe6a926f09e320389a7b8395 body_fp=4d235fc398f29fa50849330bf69941457e337c0e3c6595fc4ba1caf0ea187a21 source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=model -->
Input contract for `resolveLayout`, bundling all placement data and measurement callbacks needed to produce non-overlapping canvas positions.

- `placements`: relevance-placed symbols, post anchor-cohesion
- `isPill`: returns true if the symbol renders as a pill chip (vs. a dot)
- `pillHalfWidth`: measured label half-width per qname, in world units
- `regionLabelHalfWidth`: measured heading half-width per role, in world units
- `haloMinCount`: minimum member count for a role to receive a halo and heading
- `haloNodeMargin`: padding from member centre to halo edge, in world units
- `haloLabelGap`: gap between halo edge and its heading box, in world units
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:RegionLabel fingerprint=7400eb0c03134cf32c40892a83665d341c676e4af7a994a3b569c6bddbb9533a body_fp=b212df3c3b4a91e49ea97619c33a52636d80977a419f5f50e53d642530199e47 source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=model -->
Holds the resolved canvas position of a single role's region heading label.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:LayoutResult fingerprint=6c737c9944c150103054a0ece55550ea074d793ab1b39b85bebd38b7d3c96ffb body_fp=21759985c88b4fb5c649ec40f5dfc620ae965dbb5b2f86aa49fc6ca32d772d95 source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=model -->
Return type of `resolveLayout`: holds final resolved node positions and region heading locations.

- `placements` — input `PolarPlacement[]` mutated in-place and also returned here
- `labels` — one `RegionLabel` per halo role, positioned at its reserved fixed box
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:separateClusters fingerprint=d4015633ca067f45315fb8026b69731c76cc0bb3f23f4bfd5fd3ce2445a9d9e9 body_fp=a1a72635753b3a5070fd7d45421932b1c425dcfaaed64df5f1f60937fdffce90 source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=domain -->
Translate overlapping role-cluster bounding discs apart as rigid groups in place, so each cluster occupies a distinct canvas region before per-node de-overlap runs.

- `opts.minCount` — roles with fewer members are skipped (not treated as clusters).
- `opts.pad` — minimum gap enforced between any two disc edges.
- Fixed `Sized` boxes are excluded from grouping and never moved.
- Coincident disc centres are split along a deterministic `hashName`-derived angle.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:translateCluster fingerprint=2b003e7c075136df5959b44924d421ac71318ce1d40dfcf43eb3d2617a1baa1b body_fp=f93149f5ddac221374e71d67123b60f7599f5e7edccd3678e5d3f49e417dfb74 source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=util -->
Translate all members of a disc cluster and its centroid by `(dx, dy)` in place.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:syncPlacements fingerprint=d33f1b913caf1492b8278ddd96006d33a0a2298efd00325e4fa134bc5e348558 body_fp=e35eb731790b7466356a9ef2095974c5d74ad0f0010312c1f1d7aedca04027ac source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=util -->
Copy resolved `x`/`y` positions from `boxes` back onto matching `placements` entries, recomputing `angle` and `radius` to stay consistent.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:resolveLayout fingerprint=6d08c8f4d434072449333e2fa322becc17b12aa881f2b5ff0ab6656e54a39e57 body_fp=76e411e2069db5907e0a220e0c8e92f5440745df7f0200621b7916cb2b7f8299 source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=orchestration -->
Compute final non-overlapping canvas positions for all symbol nodes and region-heading labels from relevance-placed `PolarPlacement` inputs.

- `input.placements` — mutated in place; resolved positions are also returned in `LayoutResult.placements`
- `input.isPill` / `input.pillHalfWidth` — determine each node's footprint size (pill vs. dot)
- `input.haloMinCount` — roles with at least this many members get a rigid cluster separation pass and a fixed heading box
- Returns `labels` — final `{role, x, y}` positions for each region heading, derived from post-separation cluster centroids
- Pipeline order: rigid cluster separation → sync centroids → place fixed heading boxes → per-node `deOverlap`; guarantees zero overlaps on return
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/layout:regionLabelBoxes fingerprint=615773de592b3d6bb168c663710d628077046e496d8df2fae7612cf845564072 body_fp=ea6f222fbfa7ee1c59e9580ea83d80a0d6c8bd602db7d784d090e1126edcca6b source_ref=56df10874d38c6265d298658124fe1b2d4e91eac role=domain -->
Build fixed `Sized` heading boxes for every role with at least `opts.minCount` members, positioned outside the role's covering halo, hemisphere-aware.

- `opts.haloMaxR` — caps the covering radius before the label is placed.
- `opts.haloNodeMargin` — padding added from member centres to halo edge.
- `opts.haloLabelGap` — gap between halo edge and label centre.
- `opts.halfWidthOf` — callback supplying measured text half-width per role.
- Returns boxes with `fixed: true`; qnames are prefixed `__label__:<role>` for later stripping.
- Label is placed below the centroid when `cy > 0`, above otherwise.
<!-- trie:end -->