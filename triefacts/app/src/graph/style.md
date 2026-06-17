---
trie_version: 0.1.9
source: app/src/graph/style.ts
file_fingerprint: 8ea12c44163db99a4e5742198f2fcbdda69ed158cc684c2a4e8a0d7c4f573fcd
last_synced_at: '2026-06-17T16:39:26Z'
defines:
- kind: constant
  qualified_name: app/src/graph/style:ROLE_COLORS
  lines: 7-20
- kind: function
  qualified_name: app/src/graph/style:roleColor
  lines: 22-29
- kind: function
  qualified_name: app/src/graph/style:subsystemColor
  lines: 32-36
- kind: function
  qualified_name: app/src/graph/style:depthColor
  lines: 41-48
- kind: function
  qualified_name: app/src/graph/style:depthBand
  lines: 51-56
- kind: function
  qualified_name: app/src/graph/style:nodeRadius
  lines: 59-64
- kind: interface
  qualified_name: app/src/graph/style:ClassMarker
  lines: 67-72
- kind: function
  qualified_name: app/src/graph/style:classMarker
  lines: 74-87
- kind: constant
  qualified_name: app/src/graph/style:ACTIVITY
  lines: 91-100
- kind: function
  qualified_name: app/src/graph/style:activityDash
  lines: 104-117
- kind: function
  qualified_name: app/src/graph/style:drawHalo
  lines: 121-136
- kind: function
  qualified_name: app/src/graph/style:activityColor
  lines: 139-154
- kind: constant
  qualified_name: app/src/graph/style:AGGREGATE_COLOR
  lines: 157-157
- kind: constant
  qualified_name: app/src/graph/style:AGGREGATE_BORDER
  lines: 158-158
incoming_refs: 20
outgoing_refs: 2
---
<!-- trie:section symbol=app/src/graph/style:ROLE_COLORS fingerprint=265a0371d713c6c4b77a2b2d1dc1c3f7db656366533341e6c149e880ba375a7a body_fp=b7f69517e8ed5f9647f9daa9f80d3756823dcf50de95e9057461ed941200be30 source_ref=20da6398cd946374e05261ed83146ba0ee12407b role=config -->
Maps each standard role name (plus `"untagged"`) to a curated hex color used for node fill in the system graph.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/style:roleColor fingerprint=a1ef0bfcd1429ebf55c7676b84cc3703ab31ec5f043ac10dc36458573cc24071 body_fp=08dceac18f30be625a4b4b04608f0bc2fca5a316d345961db16211d24786c7c2 source_ref=20da6398cd946374e05261ed83146ba0ee12407b role=util -->
Return a CSS color string for a given role, using curated colors from `ROLE_COLORS` or a deterministic HSL hash for unknown roles.

- `role`: falls back to `"untagged"` if falsy.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/style:subsystemColor fingerprint=f5c5c5b9788450cde7bd5a08e10bce565e8add860faff69e88190bb8a700d038 body_fp=a98044699605607a750b777b00b17a25e107901d8f01637193bad83ffd394559 source_ref=20da6398cd946374e05261ed83146ba0ee12407b role=util -->
Derive a deterministic HSL color from a subsystem name by hashing its characters.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/style:depthColor fingerprint=e1f8110cc71b6a07f46800005afbd35594a7a5a6d6cc811e100916d9b81b98a4 body_fp=93808552c449cd581edf03e5c913d4f9cbe4a6ce46b602dd387dd52ad9066b78 source_ref=20da6398cd946374e05261ed83146ba0ee12407b role=util -->
Convert a normalized call-depth position into an HSL color sweeping amber-to-violet.

- `t`: clamped to `[0, 1]`; `0` = entry (warm amber), `1` = foundation (cool violet).
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/style:depthBand fingerprint=2ac201024d95c9ca2e1625a78b3081c92dd941130315faabe5cf007fd1addc1d body_fp=70a6a82bdf1d28f21798ec7c49a2d9bf64b437744d82b4b4651c2e9691ef1a95 source_ref=20da6398cd946374e05261ed83146ba0ee12407b role=util -->
Map a normalised call-depth value `t` to one of four discrete band labels for legend display.

- `t`: clamped `[0, 1]` representing relative call-flow depth
- Returns `"entry"` | `"interface"` | `"logic"` | `"foundation"`
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/style:nodeRadius fingerprint=4a107e7b0d9d7a4a6edafdb6eae6146f1e4aa99cac944ee505a2d5a58dd90817 body_fp=acb1a7adfc8bc68561409496772a5255f0f3f86feebbc76ac07a95474dfe6e99 source_ref=20da6398cd946374e05261ed83146ba0ee12407b role=util -->
Compute node radius in pixels from salience and `NodeClass`, scaling hubs and doors up by fixed multipliers.

- `salience`: normalized value producing a base radius in the range 3–12
- `cls`: `"hub"` → ×1.35, `"door"` → ×1.2, all others → base unchanged
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/style:ClassMarker fingerprint=c1cf7529103799ae3eb258d5cebe6b0f5ca1ebb8becbb6143a094776a62a3895 body_fp=2c81ea11afaa91ff50f581c64276f41c19ad2e6925d9d11fe88c74e5ca47ca81 source_ref=20da6398cd946374e05261ed83146ba0ee12407b role=model -->
Describes the visual decoration applied to a graph node based on its boundary class.

- `ring`: present on `door` nodes; amber ring color.
- `halo`: present on `hub` nodes; set to the node's role color.
- `shape`: `"diamond"` for `bedrock` nodes, `"circle"` otherwise.
- `chevron`: `true` on `exit` nodes to indicate outward direction.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/style:classMarker fingerprint=823a803c706f06313184b4b7ebd15651195064f5f5729ac57ae4a97ba93c2c07 body_fp=b76be7094f6e8e9f35acfc4425df5e27f22d36eaa8a2dea2615e61ab7d44ebeb source_ref=20da6398cd946374e05261ed83146ba0ee12407b role=util -->
Map a `NodeClass` value to its `ClassMarker` decoration descriptor, using `color` as the halo tint for hub nodes.

- `cls`: determines shape, ring, halo, and chevron fields of the returned marker
- `color`: passed through as `halo` only when `cls === "hub"`
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/style:ACTIVITY fingerprint=2601313a58e51e19c3a7a29fbba9ed60b61c653d2b2c0613d565ec475127bc51 body_fp=15e2386b76ed10ed02378b7543a3a8b6a43b36250c28614850349fa0cced6693 source_ref=20da6398cd946374e05261ed83146ba0ee12407b role=config -->
CVD-safe color palette mapping agent activity states to dark-theme glow hex values.

- `read`: blue — read, explain, or trace target
- `scan`: teal — grep or search operations
- `write`: amber — write or edit operations
- `patch`: orange — staged patch
- `cascade`: violet — cascade wavefront propagation
- `stale`: slate — stale state
- `error`: rose — error state
- `heat`: red — residual edit warmth
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/style:activityDash fingerprint=76ca4ec021c6a9db95e2c801c0a337f61a0e3ffcaf43f304d8ff425fd9b3466e body_fp=95837d5cc8c595fff393b25a0f1c81380f8e19f792134b6ee4d70e012190122b source_ref=20da6398cd946374e05261ed83146ba0ee12407b role=util -->
Return a canvas dash pattern for a given agent `state`, encoding state redundantly with line style for CVD/monochrome legibility.

- `state`: one of `"scanning"`, `"cascade"`, `"stale"`, `"error"`, or any other value (solid)
- Returns `[]` (solid) for read/write states; non-empty patterns otherwise
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/style:drawHalo fingerprint=45824a023bb6f382d7b7f26114a33fe775d1e64e9c3802562e7623f94b2e58aa body_fp=225a49271f61dcf06cf364142646d9bb7dba80ed2baec3adebf5e7703a8c2b70 source_ref=20da6398cd946374e05261ed83146ba0ee12407b role=io -->
Draw a filled, semi-transparent circular glow at `(x, y)` onto a canvas context.

- `alpha` — clamped to `[0, 1]` before applying as `globalAlpha`
- `ctx` state is saved and restored; no side-effects on surrounding draw calls
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/style:activityColor fingerprint=a1f911e9876924ddde50ecd3e00ab1032b7ed4623616664261fba04439a555f9 body_fp=479d821b2febcfab96941d78fed57f7dee5383bfc2dfc5d3eb53abf3340cf287 source_ref=20da6398cd946374e05261ed83146ba0ee12407b role=util -->
Map an agent `state` string to its corresponding `ACTIVITY` color constant.

- `state`: one of `"writing"`, `"scanning"`, `"cascade"`, `"stale"`, `"error"`; defaults to `ACTIVITY.read`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/style:AGGREGATE_COLOR fingerprint=a377dc99c1a5a74c6cbc4490bee428c96436ab9e08a9c9ece58d0f8fb44e8925 body_fp=b0280c4a79bfb1a9bc56f6625b612b930c2dbc0d5014195e76d5432cf8dbdaf3 source_ref=20da6398cd946374e05261ed83146ba0ee12407b role=config -->
Fill color for aggregate "+N" bubble overlays on the graph canvas.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/style:AGGREGATE_BORDER fingerprint=fca168e3e598462d0bc2eea1160219641f11b03696fdb5bc03eca6e25ce6e758 body_fp=0f76e9df8eb5d4af31b4cb024c119870a69e52492550724aaa6c1b479ba27eb8 source_ref=20da6398cd946374e05261ed83146ba0ee12407b role=config -->
Border color (`#334155`) for aggregate "+N" bubble overlays on the graph canvas.
<!-- trie:end -->