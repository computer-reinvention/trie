---
trie_version: 0.1.9
source: app/src/store/graphStore.ts
file_fingerprint: be73e9737c5dd90480214cef28f85720bbba4a5d4b81ab33219eca3f2183d765
last_synced_at: '2026-06-17T16:40:33Z'
defines:
- kind: interface
  qualified_name: app/src/store/graphStore:NodeRuntime
  lines: 13-20
- kind: type
  qualified_name: app/src/store/graphStore:ViewLevel
  lines: 23-23
- kind: type
  qualified_name: app/src/store/graphStore:MemberGrouping
  lines: 26-26
- kind: interface
  qualified_name: app/src/store/graphStore:GraphStore
  lines: 28-106
- kind: constant
  qualified_name: app/src/store/graphStore:DEFAULT_RUNTIME
  lines: 108-108
- kind: function
  qualified_name: app/src/store/graphStore:emptyVisible
  lines: 110-112
- kind: constant
  qualified_name: app/src/store/graphStore:useGraphStore
  lines: 114-385
incoming_refs: 20
outgoing_refs: 12
---
<!-- trie:section symbol=app/src/store/graphStore:NodeRuntime fingerprint=22cd76ea8b124f61fb84f7a3e3ee9969bb0119791de41e864cf831a1f14a24ec body_fp=fcfa949b439888cc950c48e4c29ba6ce9d06a90990d7dd031e8b171935d8b50e source_ref=c07836488aa95dacb9afac30d13c2593b304cb2e role=model -->
Per-node live runtime state keyed by qname, held separately from the immutable model to avoid triggering model rebuilds.

- `activity`: transient intensity `0..1` driven by SSE; read by the animator for pulse/glow effects
- `heat`: edit-heat `0..1` that decays over time (~minutes)
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/graphStore:ViewLevel fingerprint=4516349dd91fcfd150cdeaf67102960bb2e725fda3f127d41e5c0a75e7b9f415 body_fp=f43ea12a55db87e39f04d72ff2ffc0122ac9f3281f01f22a20edb09f3648161f source_ref=c07836488aa95dacb9afac30d13c2593b304cb2e role=model -->
Union type encoding the three zoom levels of the graph canvas view.

- `"components"` — L0, shows collapsed component nodes
- `"landmarks"` — L1, an expanded component revealing its landmark symbols
- `"neighborhood"` — L2, a single symbol's call neighbourhood
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/graphStore:MemberGrouping fingerprint=2e1496f9d714082dd84c0e62f937b17aee4255a584a71813bfd96766c0a2c7b0 body_fp=511b7c34b7c225b618d70b841ebcbe553d65b5e1e90d97175cbcc568c37fcfb0 source_ref=c07836488aa95dacb9afac30d13c2593b304cb2e role=model -->
Union type controlling how members inside an expanded container are sub-grouped.

- `"subsystem"` — group by subsystem membership
- `"class"` — group by the member's own class
- `"owningClass"` — group by the class that owns the member
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/graphStore:GraphStore fingerprint=ce624ff59bf4576ff5ee81cbf0d08427c1a8a3d0a379e80cdf618cab9ff30a35 body_fp=596b87128ac30202e3aed0dc05d6f15e5e0871ee7f8234e1a22e2b1063b328c3 source_ref=c07836488aa95dacb9afac30d13c2593b304cb2e role=model -->
Zustand store shape combining immutable graph model, view state, live per-node runtime, and all mutating actions.

- `model` / `nodesByQname` / `adjacency` / `regime` — set once by `setModel`; treated as immutable thereafter
- `focusedExpansion` — single transient expanded component key; replaced (not stacked) on each `expandComponent` call
- `pinnedExpansions` — user-pinned expansions that survive transient collapse
- `focus` — qnames fed to the DOI algorithm to bias salience toward selected/agent-active symbols
- `isolatedGroup` — when non-null, dims all legend groups except this one on the active axis
- `activeFlows` — edge keys (`"from|to"`) mapped to expiry timestamps (ms); drives comet particles
- `trail` — capped at 24 entries, most-recent last; drives breadcrumb and trail highlight
- `lastTouched` — most-recent agent symbol + intent; drives the canvas caption
- `notes` — per-symbol popup text from agent tool output, timestamped
- `visible` — derived; always recomputed via `recomputeVisible` after state changes that affect salience
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/graphStore:DEFAULT_RUNTIME fingerprint=0d37b761741b2d8fa45bd3d73b867e2cee78b04b14c3e5277749d0d708172272 body_fp=82cd4b010f8447f2d2d1bcb26070a942f13d32d51424b1ebd431f1ead2f64c8f source_ref=c07836488aa95dacb9afac30d13c2593b304cb2e role=model -->
Fallback `NodeRuntime` value used when a node has no entry in the runtime map.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/graphStore:emptyVisible fingerprint=4cff2f7c67ae62d58043c1cbbcf7e9a82b7e39d26185cd70bce362b8f6916597 body_fp=3823cff7823fd97cccaa69758c6eee0bada50c0c0c1e12fedf3122734c0d61e2 source_ref=c07836488aa95dacb9afac30d13c2593b304cb2e role=util -->
Return a zero-state `VisibleSet` with empty `nodes` and `aggregates` arrays.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/graphStore:useGraphStore fingerprint=d996ae2b6f3fa58543cb56e383be618f4d8080d069601d33b3152440006c21f1 body_fp=0765ef0ac65f470f375f713ae4e577b93a373f59cc6dfe53a653497f256d71ae source_ref=c07836488aa95dacb9afac30d13c2593b304cb2e role=orchestration -->
Zustand store holding the full graph view state: immutable model, derived visibility, per-node runtime, agent trail, and all mutation actions.

- `setModel` — loads a new `SystemModel`, rebuilds adjacency/regime, resets runtime and view state
- `recomputeVisible` — recomputes `visible` via `selectVisible` using current axis, focus, and expanded groups
- `expandComponent` — sets exactly one transient expansion, replacing any prior unpinned one; advances level to `"landmarks"`
- `collapseTransient` — clears transient expansion; drops to `"components"` unless pinned expansions remain
- `revealSymbol` — expands the owning group and selects the node; returns `false` if qname absent from model
- `revealFile` — focuses all file symbols, expands the most-salient non-module symbol's component; returns `false` if file has no nodes
- `pushTrail` — appends qname to trail (max 24, no adjacent duplicate) and updates `lastTouched`
- `flowAlong` — registers a timed active-flow edge and bumps destination activity by 0.6
- `decayActivityAndHeat` — exponentially decays activity (~500 ms half-life) and heat (~120 s half-life); expires stale flow entries
- `bumpActivity` — clamps activity to 1 after adding `amount` (default 1)
- `setFileActivity` / `setFileAgentState` — apply a value to every node whose `file_path` matches the given path
<!-- trie:end -->