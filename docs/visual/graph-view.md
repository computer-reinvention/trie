# The Desktop Graph View — architecture & extension guide

This document explains how the trie desktop app's graph view is built and how to
extend it: add a node decoration, a new live-activity type, an overlay, a data
endpoint, or a new tab. Read this before touching `app/src/components/GraphCanvas/*`.

The graph view is the heart of the desktop app: a zoomable "model of the system"
that shows the codebase as role/subsystem **components** at the top level (L0),
drills into **symbols** on demand, and animates what the agent is doing in real
time (reads, greps, edits) plus what edits are staged (patches).

---

## 1. The two-level model

The canvas never draws all symbols at once. It shows two levels:

- **L0 — component map** (`GraphCanvas`, `index.tsx`): one bubble per group on
  the current axis (`role` or `subsystem`), laid out top-down by call-flow depth.
  This is always visible. Bubbles carry counts, glow with live agent activity,
  and show pending-patch rings.
- **L1/L2 — expanded sub-graph** (`ExpandedPanel`, `ExpandedPanel.tsx`): when a
  component is expanded, a bounded overlay panel renders that group's **symbols**
  as a real call-network (with drill-into-class/subsystem frames). Individual
  symbol pulses, comets, notes, selection and patch badges live here.

> Key consequence: **symbol-level decoration only shows inside the ExpandedPanel.**
> The L0 map shows symbol activity _rolled up_ to the owning component bubble.
> If you add per-symbol visuals, add the L0 rollup too (see §6.1).

The bounded visible-set math (DOI = salience − k·distance(focus), budgeted) lives
in `app/src/graph/doi.ts` and is pure/headless-testable. `componentView(model,
axis)` produces the L0 groups + flows; `selectVisible(...)` picks the bounded
symbol set for an expanded frame.

---

## 2. File map

### Components — `app/src/components/GraphCanvas/`

- `index.tsx` — **GraphCanvas**: the L0 `ForceGraph2D`, layout, camera, hover
  tooltip, `paintNode` (canvas painter), live-activity rollups, patch pips/rings.
- `ExpandedPanel.tsx` — the drill-in sub-graph: symbol network, agent-activity
  overlays (pulse rings, comets, persistent touched rings, note popups, patch
  badges), per-frame easing, soft-pan-to-attention.
- `AgentActivityCards.tsx` — HTML popup cards anchored to L0 bubbles showing the
  tool-output snippet that focused each touched symbol (camera-tracked, fading).
- `Legend.tsx` — axis switch (roles/subsystems), call-depth key, group list with
  click-to-isolate, members-by selector, show-tests toggle.
- `SearchPalette.tsx` — ⌘-style symbol search.

### Editor host — `app/src/components/Editor/`

- `index.tsx` — tab host. Permanent tabs: **graph** (`GRAPH_TAB_ID`) and
  **patches** (`PATCHES_TAB_ID`); file tabs are dynamic. Each tab is mounted once
  and shown/hidden (graph keeps its layout/zoom alive).
- `TabStrip.tsx` — the tab bar (graph icon, patches tab with count badge, file
  tabs with src/tf pills + close).
- `PatchesPanel.tsx` — the patch review surface (list of patched symbols, apply,
  ApplyReport).
- `SourceView.tsx` / `TriefactView.tsx` / `FileTabContent.tsx` — file tabs.

### State — `app/src/store/`

- `graphStore.ts` — **the graph's brain.** Immutable `model` + derived
  `nodesByQname`/`adjacency`; view state (`axis`, `focusedExpansion`,
  `pinnedExpansions`, `selectedQname`, `isolatedGroup`); live runtime
  (`runtime` per-node activity/agentState/heat, `activeFlows` edge comets,
  `trail`, `lastTouched`, `notes`); actions (`setModel`, `revealSymbol`,
  `expandComponent`, `setNodeAgentState`, `bumpActivity`, `flowAlong`,
  `pushTrail`, `setNote`, `clearTrail`, `decayActivityAndHeat`).
- `patchesStore.ts` — pending patches + derived `patchedQnames` set + apply
  progress.
- `tabsStore.ts` — tabs (graph/patches/file) + active tab.
- `agentStore.ts` — multi-session chat transcript (separate from the graph).
- `activityStore.ts` — cross-process writer status + stale set (sync/refresh).
- `settingsStore.ts` — VS Code-style settings (`graph.followAgent`, etc.).
- `appStore.ts` — project/servers/model; `contextMenuStore.ts` — shared menu.

### Graph helpers — `app/src/graph/`

- `doi.ts` — visible-set selection, `componentView`, `buildAdjacency`,
  member sub-grouping. Pure, no React/canvas.
- `style.ts` — all colors + shapes: `ACTIVITY` (read/scan/write/heat), `roleColor`,
  `depthColor`, `classMarker`, `nodeRadius`. **Add new activity colors here.**
- `animator.ts` — `GraphAnimator`: per-node spring channels (`pulse`, `reveal`,
  `emphasis`); state sets targets, animator eases current, paint draws current.
- `agentChoreography.ts` — `choreographFor(toolPart)`: maps an opencode tool part
  to `{reads, scans, writes, files, flows}` symbol sets. **Add new agent tools here.**
- `regime.ts` — budget/salience-floor tuning per model size.

### API — `app/src/api/`

- `graphClient.ts` — typed client for the `/desktop/graph/*` HTTP endpoints
  (routed through the Electron IPC proxy; renderer can't reach 127.0.0.1).
- `types.ts` — every wire shape (SystemModel, SymbolHit, patches, ApplyReport,
  opencode messages, desktop SSE events). **Add new shapes here.**
- `opencodeClient.ts` — session/message/permission HTTP for the chat.

### Hooks — `app/src/hooks/`

- `useGraphPopulation.ts` — fetches `system-model` + `all-edges` → `setModel`.
- `useOpenCodeSSE.ts` — subscribes the raw `/event` bus stream, maps bus events
  to transcript + **graph choreography** (the live animation driver).
- `usePatches.ts` — polls `/desktop/graph/patches`; exposes drop/apply.
- `useActivityPoll.ts` — polls `/desktop/graph/activity` (sync/refresh glow).
- `useSessions.ts` — chat session lifecycle.

### Backend (opencode submodule)

`opencode/packages/opencode/src/server/routes/instance/httpapi/`

- `groups/desktop.ts` — endpoint declarations (paths + schemas).
- `handlers/desktop.ts` — handlers; most proxy a trie MCP tool via
  `callTrieTool(tools, "<tool>", args)`. `mapBusEvent` is the SSE event mapper
  (currently unused by the app, which consumes raw `/event` directly).

The trie MCP tools the endpoints proxy live in `trie/mcp_server.py`
(`summary`, `all_symbols`, `all_edges`, `system_model`, `symbols_by_file`,
`file_triefact`, `activity`, `patch_list`, `patch_drop`, `patch_apply`, …).

---

## 3. Data flow

### Initial population

1. Electron spawns the bundled `opencode-server` in the project dir and emits
   `ipc:servers-ready` with the port.
2. `App.tsx` → `setGraphClientBase(port)` → `useGraphPopulation` waits for the
   trie MCP to connect, then `graphClient.systemModel()` + `allEdges()` →
   `graphStore.setModel(model, edges)`.
3. `GraphCanvas` renders the L0 component map from the model.

### Live agent activity (the animation)

1. `useOpenCodeSSE` subscribes `http://127.0.0.1:<port>/event` via the IPC SSE
   proxy (`trie.sseSubscribe`).
2. On `message.part.updated` with a **tool** part → `choreographFor(part)` →
   sets `runtime` agentState + `bumpActivity`, `pushTrail`, `setNote`, and
   `flowAlong` for connected/traced edges.
3. `GraphCanvas.onRenderFramePre` eases component-bubble pulses from rolled-up
   activity; `ExpandedPanel` eases per-symbol pulses. `decayActivityAndHeat`
   (rAF loop) fades activity; `notes`/`trail` persist until the next user turn
   (`clearTrail` fires in `useSessions.send`).

### Patches

1. `usePatches` polls `graphClient.patches()` → `patchesStore.setPatches` →
   derives `patchedQnames`.
2. `PatchesPanel` lists them; `GraphCanvas` draws amber ring + count pip on
   bubbles containing patched symbols; `ExpandedPanel` draws an amber dashed
   ring on each patched symbol; hover tooltips explain them.

---

## 4. Rendering model (canvas)

Both `ForceGraph2D` instances paint nodes with `nodeCanvasObject` and run
`onRenderFramePre` each frame (with `autoPauseRedraw={false}` so animation keeps
ticking after the force sim settles). Layout is **fixed** (`fx/fy` pinned); forces
are effectively off — positions are deterministic.

- L0 painter: `paintNode(n, ctx, scale, opts)` in `index.tsx`. `opts` carries
  `pulse`, `agentState`, `touchedGroup`, `patchedCount`, etc.
- Sub-graph painter: inline `nodeCanvasObject` in `ExpandedPanel.tsx`.

Coordinate conversion for HTML overlays: `fgRef.current.graph2ScreenCoords(x, y)`.
Component graph-space positions are memoized as `componentPos` in `index.tsx`.

---

## 5. Conventions

- **Everything is keyed by `qname`** (qualified name). Resolve a node via
  `graphStore.nodesByQname.get(qname)`; its group is
  `axis === "role" ? node.role || "untagged" : node.subsystem`.
- **State sets targets; the animator eases; paint draws.** Don't snap values in
  paint — push to `runtime`/animator and let the spring/decay handle motion.
- **Live state is transient and store-driven.** Read it in paint via
  `useGraphStore.getState()` / `usePatchesStore.getState()` (not via hooks) so the
  canvas isn't re-rendered per frame.
- **Persisted-for-the-turn vs decaying:** `runtime.activity` decays fast (pulse);
  `notes` + `trail` persist until `clearTrail` (next user message). Use `notes`
  for "what did the agent touch this turn", `activity` for "is it live now".
- **Colors come from `graph/style.ts`.** Don't hardcode hex in components.

---

## 6. Extension recipes

### 6.1 Add a new per-symbol decoration (ring/badge)

1. Source the data into a store (e.g. extend `graphStore` runtime or a new store)
   keyed by qname.
2. Draw it in `ExpandedPanel.tsx`'s `nodeCanvasObject` (read via `getState()`).
3. **Roll it up to L0:** in `index.tsx` `onRenderFramePre`, aggregate the per-symbol
   data to its group into a `Ref<Map<group, …>>`, pass a flag/count through
   `paintNode`'s `opts` (extend `PaintOpts`), and draw on the component branch.
   (See `patchedGroupCountRef` + `patchedCount`, or `touchedGroupsRef` +
   `touchedGroup` for the exact pattern.)

### 6.2 Add a new live-activity type/color

1. Add the state to `AgentState` in `api/types.ts`.
2. Add its color to `ACTIVITY` in `graph/style.ts`.
3. Handle it in `paintNode` (L0 ring color) and `ExpandedPanel` (`activityColor`).
4. Emit it from `agentChoreography.ts` / `useOpenCodeSSE.ts`.

### 6.3 Teach the graph a new agent tool

Edit `choreographFor` in `graph/agentChoreography.ts`: match the tool name
(prefix-stripped via `bareTool`), pull the symbol(s) from `part.state.input`
and/or parse `part.state.output`, and return them in `reads`/`scans`/`writes`/
`flows`. The SSE hook does the rest.

### 6.4 Add an HTML overlay anchored to the graph

Model it on `AgentActivityCards.tsx`: take `fgRef` + `componentPos` + `width/height`,
run a rAF to re-read `graph2ScreenCoords` while the data is fresh, render absolutely
positioned cards inside the `GraphCanvas` container (`pointer-events-none`).

### 6.5 Add a new desktop data endpoint

1. **Backend (submodule):** add a path to `DesktopPaths` + an `HttpApiEndpoint`
   in `groups/desktop.ts`; add a handler in `handlers/desktop.ts` (usually
   `callTrieTool(tools, "<mcp_tool>", args)`) and wire it in the `.handle(...)`
   chain. The MCP tool must exist in `trie/mcp_server.py` and be registered in
   `build_server`.
2. **Rebuild the bundled server:** `cd app && npm run build:resources` (compiles
   the submodule into `app/resources/opencode-server`).
3. **Frontend:** add the type to `api/types.ts`, a method to `api/graphClient.ts`,
   and consume it (store + poll/hook + component).

### 6.6 Add a new tab

1. Add an id + `kind` + tab interface to `tabsStore.ts`; include it in the
   permanent `tabs` array (or open dynamically), and guard it in `close`.
2. Render its button in `Editor/TabStrip.tsx`.
3. Render its content (mounted-hidden) in `Editor/index.tsx`.

### 6.7 Adjust the agent-following camera

The gentle follow lives in `index.tsx` (effect on `lastTouched`): it pans only
when the active component drifts near the viewport edge. Gate via the
`graph.followAgent` setting. There is intentionally **no** auto-zoom/auto-drill.

---

## 7. Gotchas

- **L0 shows components, not symbols.** Per-symbol effects are invisible on the
  main map unless rolled up to the bubble (§6.1).
- **Canvas keeps redrawing** only with `autoPauseRedraw={false}`; time-based fades
  (notes, decay) rely on it.
- **Read live state via `getState()` in paint**, never via a hook in the paint
  callback — hooks there would thrash React.
- **Backend changes need `npm run build:resources`** to land in the packaged app;
  the submodule is compiled into a standalone binary.
- **`graph2ScreenCoords` requires `fgRef.current`** — guard for null on first frame.
- The desktop app consumes the **raw `/event` SSE stream** and maps bus events
  client-side (`useOpenCodeSSE`); the server-side `mapBusEvent` in `desktop.ts`
  is kept additive but is not the app's source of truth.

---

## 8. Verify after changes

```bash
cd app && npm run typecheck          # app TS
cd app && npm run build              # renderer build
cd app && npm run build:resources    # only if the submodule changed
cd app && npm run pack               # package .app for manual testing
```

For backend endpoint changes also typecheck the submodule:
`cd opencode/packages/opencode && bun typecheck` (a known pre-existing baseline of
effect-beta errors in `httpapi/handlers/desktop.ts` + `server.ts` is expected;
don't add _new_ error categories).
