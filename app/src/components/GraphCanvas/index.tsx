import { useCallback, useEffect, useMemo, useRef, useState } from "react"
import ForceGraph2D, { type ForceGraphMethods } from "react-force-graph-2d"
import { forceCollide } from "d3-force"
import { useGraphStore } from "@/store/graphStore"
import { useAppStore } from "@/store/appStore"
import { buildSymbolMenu } from "@/agm/symbolMenu"
import { useSettingsStore } from "@/store/settingsStore"
import { usePatchesStore } from "@/store/patchesStore"
import { openContextMenu } from "@/store/contextMenuStore"
import { componentView, memberSubgroup } from "@/graph/doi"
import { nodeRadius, classMarker, ACTIVITY, depthColor, activityColor } from "@/graph/style"
import { GraphAnimator } from "@/graph/animator"
import { SearchPalette } from "./SearchPalette"
import { ExpandedPanel } from "./ExpandedPanel"
import { AgentActivityCards } from "./AgentActivityCards"
import { ChoreographyOverlay } from "./ChoreographyOverlay"
import { useConductor, replayTurn } from "@/graph/conductor"
import { useTrieCommandStore } from "@/store/trieCommandStore"
import { useTrieConfigStore } from "@/store/trieConfigStore"
import { useTabsStore, TRIE_TAB_ID } from "@/store/tabsStore"
import type { SystemModelNode } from "@/api/types"

interface GraphCanvasProps {
  className?: string
}

type FGNode =
  | {
      kind: "component"
      id: string
      label: string
      count: number
      color: string
      val: number
      expanded?: boolean
      order: number
      // runtime position (force-graph mutates these)
      x?: number
      y?: number
      fx?: number
      fy?: number
    }
  | {
      kind: "symbol"
      id: string
      node: SystemModelNode
      color: string
      val: number
      group: string
      order: number
      x?: number
      y?: number
      fx?: number
      fy?: number
    }
  | {
      kind: "aggregate"
      id: string
      label: string
      count: number
      color: string
      val: number
      group: string
      order: number
      x?: number
      y?: number
      fx?: number
      fy?: number
    }

interface FGLink {
  source: string
  target: string
  weight: number
  kind?: "flow" | "member" | "call"
}

export function GraphCanvas({ className }: GraphCanvasProps) {
  const {
    model,
    axis,
    hoveredId,
    adjacency,
    selectedQname,
    isolatedGroup,
    focusedExpansion,
    pinnedExpansions,
  } = useGraphStore()
  const expandComponent = useGraphStore((s) => s.expandComponent)
  const togglePin = useGraphStore((s) => s.togglePin)
  const selectNode = useGraphStore((s) => s.selectNode)
  const setHovered = useGraphStore((s) => s.setHovered)
  const collapseTransient = useGraphStore((s) => s.collapseTransient)
  // the symbol currently under the agent's attention (drives the gentle camera)
  const lastTouched = useGraphStore((s) => s.lastTouched)
  const notes = useGraphStore((s) => s.notes)
  const nodesByQname = useGraphStore((s) => s.nodesByQname)
  const { graphLoading, graphLoadingMessage } = useAppStore()
  // mouse position within the canvas (for the hover-note tooltip)
  const [mouse, setMouse] = useState<{ x: number; y: number }>({ x: 0, y: 0 })
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const fgRef = useRef<ForceGraphMethods<any, any> | undefined>(undefined)
  const animatorRef = useRef(new GraphAnimator())
  // current zoom factor — fade edges out when zoomed far (legibility + perf).
  const zoomRef = useRef(1)
  // groups (role/subsystem) containing a symbol the agent touched THIS turn —
  // persists until the next turn so the component bubble stays marked.
  const touchedGroupsRef = useRef<Set<string>>(new Set())
  // count of symbols with pending patches per group, for the bubble pip.
  const patchedGroupCountRef = useRef<Map<string, number>>(new Map())
  // live screen position of the focused role node, so the sub-graph panel can
  // anchor to it (act like a graph node, panning/zooming with the canvas).
  const [anchor, setAnchor] = useState<{ x: number; y: number } | null>(null)
  // size the force graph to its container (not the window) so the input bar /
  // turn history below it stay visible.
  const containerRef = useRef<HTMLDivElement>(null)
  const [dims, setDims] = useState<{ w: number; h: number }>({ w: 0, h: 0 })

  useEffect(() => {
    const el = containerRef.current
    if (!el) return
    const ro = new ResizeObserver((entries) => {
      const cr = entries[0].contentRect
      setDims({ w: Math.round(cr.width), h: Math.round(cr.height) })
    })
    ro.observe(el)
    setDims({ w: el.clientWidth, h: el.clientHeight })
    return () => ro.disconnect()
  }, [])

  // Neighbours of the hovered node (spotlight: highlight + dim the rest).
  const highlightSet = useMemo(() => {
    if (!hoveredId) return null
    const s = new Set<string>([hoveredId])
    const nbrs = adjacency?.neighbours.get(hoveredId)
    if (nbrs) for (const w of nbrs) s.add(w)
    return s
  }, [hoveredId, adjacency])

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const linkIsActive = useCallback((l: any) => {
    const st = useGraphStore.getState()
    const flows = st.activeFlows
    if (!flows.size) return false
    const s = typeof l.source === "object" ? l.source.id : l.source
    const t = typeof l.target === "object" ? l.target.id : l.target
    // direct symbol-edge match (used inside the expanded panel)
    if (flows.has(`${s}|${t}`) || flows.has(`${t}|${s}`)) return true
    // component-level rollup: a flow whose endpoints live in these two groups
    // (on the current axis) lights the component->component backbone link.
    const groupOf = (qn: string) => {
      const n = st.nodesByQname.get(qn)
      if (!n) return null
      return st.axis === "role" ? n.role || "untagged" : n.subsystem
    }
    for (const key of flows.keys()) {
      const [from, to] = key.split("|")
      const gf = groupOf(from)
      const gt = groupOf(to)
      if (gf && gt && gf !== gt && ((gf === s && gt === t) || (gf === t && gt === s))) return true
    }
    return false
  }, [])

  // Build the graph. L0 component backbone always present; expanded roles bloom
  // their members into a bounded community region tethered to the role anchor.
  const data = useMemo(() => {
    if (!model)
      return { nodes: [] as FGNode[], links: [] as FGLink[] }

    const view = componentView(model, axis)
    const expanded = new Set<string>(pinnedExpansions)
    if (focusedExpansion) expanded.add(focusedExpansion)
    const groupByKey = new Map(view.groups.map((g) => [g.key, g]))

    const nodes: FGNode[] = []
    const links: FGLink[] = []
    const COMP_R = 16

    // Top-down LAYERED layout — the way an engineer reads a system: start at
    // entry points (top), follow the call flow down through logic, to the
    // foundations everything rests on (bottom). Roles are bucketed into discrete
    // layers by call-flow order; within a layer they're spread horizontally and
    // de-overlapped. Deterministic fixed positions (no collapse-to-a-line).
    const LAYER_GAP = 200
    const COL_GAP = 260
    // assign each group a layer index from its order (0..1) -> 0..NLAYERS-1
    const NLAYERS = 5
    const layerOf = (order: number) => Math.min(NLAYERS - 1, Math.round(order * (NLAYERS - 1)))
    const byLayer = new Map<number, typeof view.groups>()
    for (const g of view.groups) {
      const L = layerOf(g.order)
      if (!byLayer.has(L)) byLayer.set(L, [])
      byLayer.get(L)!.push(g)
    }
    const compPos = new Map<string, { x: number; y: number }>()
    for (const [L, groups] of byLayer) {
      // sort within layer by member count desc for a stable, centered spread
      const sorted = [...groups].sort((a, b) => b.count - a.count)
      const n = sorted.length
      sorted.forEach((g, i) => {
        const x = (i - (n - 1) / 2) * COL_GAP
        const y = L * LAYER_GAP
        compPos.set(g.key, { x, y })
      })
    }

    for (const g of view.groups) {
      const p = compPos.get(g.key)!
      nodes.push({
        kind: "component",
        id: g.key,
        label: g.key.split("/").pop() ?? g.key,
        count: g.count,
        color: depthColor(g.order),
        val: COMP_R,
        expanded: expanded.has(g.key),
        order: g.order,
        fx: p.x,
        fy: p.y,
      })
    }
    const presentComp = new Set(view.groups.map((g) => g.key))
    for (const f of view.flows) {
      if (presentComp.has(f.source) && presentComp.has(f.target)) {
        links.push({ source: f.source, target: f.target, weight: f.weight, kind: "flow" })
      }
    }

    // Members are NOT drawn on the main canvas anymore. Expansion opens a
    // dedicated bounded, scrollable sub-graph panel (ExpandedPanel overlay) that
    // shows the role's members as a real network with their interdependencies.
    // The main canvas stays the clean L0 system map.
    return { nodes, links }
  }, [model, axis, focusedExpansion, pinnedExpansions])

  useEffect(() => {
    if (!data.nodes.length || !fgRef.current) return
    const fg = fgRef.current

    // Everything is fixed-positioned (components in a top-down layered layout,
    // members in their containers). Forces are effectively off — we only keep a
    // gentle collide so any unpinned stragglers don't stack. The layout is
    // deterministic and stable; no collapse to a line.
    fg.d3Force("charge")?.strength(0)
    fg.d3Force(
      "collide",
      forceCollide<FGNode>()
        .radius((n) => n.val + 4)
        .strength(0.2)
        .iterations(1),
    )
    fg.d3Force("x", null)
    fg.d3Force("y", null)
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const linkForce = fg.d3Force("link") as any
    if (linkForce?.strength) linkForce.strength(0) // links don't pull; layout is fixed

    const anim = animatorRef.current
    const present = new Set<string>()
    for (const n of data.nodes) {
      present.add(n.id)
      anim.ensure(n.id, true)
    }
    anim.prune(present)
    fg.d3ReheatSimulation?.()
    const t = setTimeout(() => fg.zoomToFit(900, 90), 300)
    return () => clearTimeout(t)
  }, [data, focusedExpansion, pinnedExpansions])

  // --- gentle agent-following camera ---------------------------------------
  // Softly keep the component the agent is working in within view — a calm pan,
  // no zoom yanking, no auto-drill. The HTML activity cards (below) carry the
  // detail. Gated by the "Follow Agent in Graph" setting.
  useEffect(() => {
    if (!lastTouched) return
    const camera = useSettingsStore.getState().get<string>("motion.camera") ?? "edge-only"
    if (camera === "off") return
    const fg = fgRef.current
    if (!fg) return
    const st = useGraphStore.getState()
    const node = st.nodesByQname.get(lastTouched.qname)
    if (!node) return
    const group = axis === "role" ? node.role || "untagged" : node.subsystem
    const comp = data.nodes.find((n) => n.kind === "component" && n.id === group) as
      | (FGNode & { x?: number; y?: number })
      | undefined
    if (!comp || comp.x == null || comp.y == null) return
    const s = fg.graph2ScreenCoords(comp.x, comp.y)
    if (camera === "cinematic") {
      // follow closely (but eased)
      fg.centerAt(comp.x, comp.y, 700)
      return
    }
    // edge-only: pan only when the target drifts toward the viewport edge.
    const m = 120
    if (s.x < m || s.y < m || s.x > dims.w - m || s.y > dims.h - m) {
      fg.centerAt(comp.x, comp.y, 900)
    }
  }, [lastTouched, axis, data, dims.w, dims.h])

  // decay activity + heat on a rAF loop
  useEffect(() => {
    let raf = 0
    let last = performance.now()
    const loop = (now: number) => {
      const dt = now - last
      last = now
      useGraphStore.getState().decayActivityAndHeat(dt)
      raf = requestAnimationFrame(loop)
    }
    raf = requestAnimationFrame(loop)
    return () => cancelAnimationFrame(raf)
  }, [])

  // component (role/subsystem) bubble positions in graph space — anchors for
  // the live agent-activity cards.
  const componentPos = useMemo(() => {
    const m = new Map<string, { x: number; y: number }>()
    for (const n of data.nodes) {
      if (n.kind === "component") {
        const c = n as FGNode & { fx?: number; fy?: number; x?: number; y?: number }
        const x = c.fx ?? c.x
        const y = c.fy ?? c.y
        if (x != null && y != null) m.set(n.id, { x, y })
      }
    }
    return m
  }, [data])

  // When hovering a component bubble, the tool-output snippets for the symbols
  // the agent touched inside that group — shown as a tooltip.
  const hoveredGroupNotes = useMemo(() => {
    if (!hoveredId || !componentPos.has(hoveredId)) return []
    const out: Array<{ qname: string; name: string; text: string; state: string; ts: number }> = []
    for (const [qn, note] of notes.entries()) {
      const node = nodesByQname.get(qn)
      if (!node) continue
      const g = axis === "role" ? node.role || "untagged" : node.subsystem
      if (g === hoveredId) out.push({ qname: qn, name: node.name, ...note })
    }
    return out.sort((a, b) => b.ts - a.ts).slice(0, 6)
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [hoveredId, notes, axis, componentPos, nodesByQname])

  // Pending-patch symbols inside the hovered component bubble — explained in the
  // hover tooltip so it's clear the subsystem holds staged edits.
  const patchEntries = usePatchesStore((s) => s.patches)
  const hoveredGroupPatches = useMemo(() => {
    if (!hoveredId || !componentPos.has(hoveredId)) return []
    const out: Array<{ qname: string; name: string; count: number; origin: string }> = []
    for (const p of patchEntries) {
      const node = nodesByQname.get(p.qname)
      if (!node) continue
      const g = axis === "role" ? node.role || "untagged" : node.subsystem
      if (g === hoveredId) out.push({ qname: p.qname, name: node.name, count: p.count, origin: p.origin })
    }
    return out.slice(0, 8)
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [hoveredId, patchEntries, axis, componentPos, nodesByQname])

  const maxWeight = useMemo(() => Math.max(1, ...data.links.map((l) => l.weight)), [data.links])
  const anyExpanded = focusedExpansion !== null || pinnedExpansions.size > 0

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const onNodeClick = useCallback(
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (node: any) => {
      const n = node as FGNode
      if (n.kind === "component") {
        expandComponent(n.id)
        // center on where the community will bloom (just below the node)
        const p = node as { x: number; y: number }
        if (fgRef.current) {
          fgRef.current.centerAt(p.x, p.y + 160, 700)
          fgRef.current.zoom(1.4, 700)
        }
      } else if (n.kind === "aggregate") expandComponent(n.group)
      else if (n.kind === "symbol") {
        selectNode(n.id)
        window.dispatchEvent(new CustomEvent("trie:node-selected", { detail: { qname: n.id } }))
        if (fgRef.current) fgRef.current.centerAt((node as { x: number }).x, (node as { y: number }).y, 600)
      }
    },
    [expandComponent, selectNode],
  )

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const onNodeRightClick = useCallback(
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (node: any, event: MouseEvent) => {
      const n = node as FGNode
      if (n.kind === "component") {
        togglePin(n.id)
        return
      }
      if (n.kind === "symbol") {
        const sym = n.node
        // Shared symbol menu (same actions as the AGM canvas). Blast radius +
        // stats are AGM-specific surfaces, so they're omitted here; navigation,
        // ruled-out, investigation, ask-agent, and clipboard all apply.
        openContextMenu(event, buildSymbolMenu({ qname: sym.qname, filePath: sym.file_path }))
      }
    },
    [togglePin],
  )

  const onBackgroundClick = useCallback(() => {
    collapseTransient()
    selectNode(null)
  }, [collapseTransient, selectNode])

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const onNodeHover = useCallback(
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (node: any) => setHovered(node ? (node as FGNode).id : null),
    [setHovered],
  )

  return (
    <div
      ref={containerRef}
      className={`relative flex-1 bg-slate-950 overflow-hidden ${className ?? ""}`}
      onMouseMove={(e) => {
        const el = containerRef.current
        if (!el) return
        const r = el.getBoundingClientRect()
        setMouse({ x: e.clientX - r.left, y: e.clientY - r.top })
      }}
    >
      {(hoveredGroupNotes.length > 0 || hoveredGroupPatches.length > 0) && (
        <div
          className="absolute z-30 pointer-events-none max-w-[300px] rounded-md border border-slate-600 bg-slate-950/95 shadow-xl px-2.5 py-2"
          style={{
            left: Math.min(mouse.x + 14, (dims.w || 600) - 310),
            top: Math.min(mouse.y + 14, (dims.h || 400) - 24 - (hoveredGroupNotes.length + hoveredGroupPatches.length) * 40),
          }}
        >
          {hoveredGroupPatches.length > 0 && (
            <div className={hoveredGroupNotes.length > 0 ? "mb-2 pb-2 border-b border-slate-800" : ""}>
              <p className="text-[10px] uppercase tracking-wide text-amber-400/90 mb-1 flex items-center gap-1">
                <span className="w-1.5 h-1.5 rounded-full bg-amber-400" />
                {hoveredGroupPatches.length} pending patch
                {hoveredGroupPatches.length !== 1 ? "es" : ""} in this {axis}
              </p>
              <div className="space-y-0.5">
                {hoveredGroupPatches.map((p) => (
                  <div key={p.qname} className="flex items-center gap-1.5">
                    <span className="text-amber-300/80 text-[10px]">✎</span>
                    <span className="text-[11px] font-mono text-slate-200 truncate">{p.name}</span>
                    {p.count > 1 && <span className="text-[9px] text-slate-500">×{p.count}</span>}
                    <span className="text-[9px] text-slate-500">{p.origin}</span>
                  </div>
                ))}
              </div>
            </div>
          )}
          {hoveredGroupNotes.length > 0 && (
            <>
              <p className="text-[10px] uppercase tracking-wide text-slate-500 mb-1">
                Agent activity ({hoveredGroupNotes.length})
              </p>
              <div className="space-y-1.5">
                {hoveredGroupNotes.map((n) => {
                  const col =
                    n.state === "writing" ? ACTIVITY.write : n.state === "scanning" ? ACTIVITY.scan : ACTIVITY.read
                  const verb =
                    n.state === "writing" ? "EDITED" : n.state === "scanning" ? "FOUND" : "READ"
                  return (
                    <div key={n.qname}>
                      <div className="flex items-center gap-1.5">
                        <span className="w-1.5 h-1.5 rounded-full shrink-0" style={{ background: col }} />
                        <span
                          className="text-[9px] font-semibold uppercase tracking-wide shrink-0"
                          style={{ color: col }}
                        >
                          {verb}
                        </span>
                        <span className="text-[11px] font-mono text-slate-200 truncate">{n.name}</span>
                      </div>
                      {n.text && (
                        <p className="text-[11px] text-slate-400 leading-snug line-clamp-2 pl-3">{n.text}</p>
                      )}
                    </div>
                  )
                })}
              </div>
            </>
          )}
        </div>
      )}
      {anyExpanded && (
        <div className="absolute top-3 left-3 z-10 flex items-center gap-2 text-xs">
          <button
            className="bg-slate-800/90 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded px-2 py-1"
            onClick={() => collapseTransient()}
          >
            ← System
          </button>
          {focusedExpansion && (
            <span className="bg-slate-800/70 text-slate-300 border border-slate-700 rounded px-2 py-1 font-mono">
              {focusedExpansion}
            </span>
          )}
          {[...pinnedExpansions].map((k) => (
            <span
              key={k}
              className="bg-indigo-900/50 text-indigo-200 border border-indigo-700 rounded px-2 py-1 font-mono flex items-center gap-1"
            >
              📌 {k}
              <button className="hover:text-white" onClick={() => togglePin(k)}>
                ×
              </button>
            </span>
          ))}
        </div>
      )}
      <SearchPalette />
      <ReplayControl />
      <ToolHud />
      <ExpandedPanel anchor={anchor} />
      <ChoreographyOverlay fgRef={fgRef} componentPos={componentPos} width={dims.w} height={dims.h} />
      <AgentActivityCards fgRef={fgRef} componentPos={componentPos} width={dims.w} height={dims.h} />
      {data.nodes.length > 0 && (
        <ForceGraph2D
          ref={fgRef}
          width={dims.w || undefined}
          height={dims.h || undefined}
          graphData={data}
          backgroundColor="#020617"
          nodeRelSize={1}
          nodeVal={(n) => (n as FGNode).val}
          cooldownTicks={140}
          warmupTicks={30}
          d3VelocityDecay={0.35}
          autoPauseRedraw={false}
          onRenderFramePre={() => {
            const anim = animatorRef.current
            const st = useGraphStore.getState()
            // Roll up live symbol activity to the component (role/subsystem) it
            // belongs to, so the system-level bubbles glow when the agent is
            // working inside them even while not drilled in.
            const groupActivity = new Map<string, number>()
            if (st.runtime.size && st.model) {
              for (const node of st.model.nodes) {
                const a = st.runtime.get(node.qname)?.activity ?? 0
                if (a <= 0.01) continue
                const key = axis === "role" ? node.role || "untagged" : node.subsystem
                groupActivity.set(key, Math.max(groupActivity.get(key) ?? 0, a))
              }
            }
            // persistent "touched this turn" group set, from the notes map
            const touchedGroups = touchedGroupsRef.current
            touchedGroups.clear()
            if (st.notes.size) {
              for (const qn of st.notes.keys()) {
                const node = st.nodesByQname.get(qn)
                if (!node) continue
                touchedGroups.add(axis === "role" ? node.role || "untagged" : node.subsystem)
              }
            }
            // pending-patch count per group, for the component-bubble pip
            const patchedGroupCount = patchedGroupCountRef.current
            patchedGroupCount.clear()
            const patched = usePatchesStore.getState().patchedQnames
            if (patched.size) {
              for (const qn of patched) {
                const node = st.nodesByQname.get(qn)
                if (!node) continue
                const g = axis === "role" ? node.role || "untagged" : node.subsystem
                patchedGroupCount.set(g, (patchedGroupCount.get(g) ?? 0) + 1)
              }
            }
            for (const fgn of data.nodes) {
              if (fgn.kind !== "symbol") {
                anim.ensure(fgn.id)
                if (fgn.kind === "component") {
                  anim.setTargets(fgn.id, { pulse: groupActivity.get(fgn.id) ?? 0 })
                }
                continue
              }
              const rt = st.runtime.get(fgn.id)
              const hovered = st.hoveredId === fgn.id
              const selected = st.selectedQname === fgn.id
              anim.setTargets(fgn.id, {
                pulse: rt?.activity ?? 0,
                emphasis: hovered || selected ? 1 : 0,
              })
            }
            anim.tick(performance.now())

            // track the focused role node's screen position for the panel anchor
            const fg = fgRef.current
            if (fg && focusedExpansion) {
              const comp = data.nodes.find(
                (n) => n.kind === "component" && n.id === focusedExpansion,
              ) as (FGNode & { x?: number; y?: number }) | undefined
              if (comp && comp.x != null && comp.y != null) {
                const s = fg.graph2ScreenCoords(comp.x, comp.y)
                setAnchor((prev) =>
                  !prev || Math.abs(prev.x - s.x) > 1 || Math.abs(prev.y - s.y) > 1
                    ? { x: s.x, y: s.y }
                    : prev,
                )
              }
            }
          }}
          onNodeClick={onNodeClick}
          onNodeRightClick={onNodeRightClick}
          onNodeHover={onNodeHover}
          onBackgroundClick={onBackgroundClick}
          onZoom={(z: { k: number }) => {
            zoomRef.current = z.k
          }}
          linkColor={(l) => {
            const lk = l as unknown as {
              kind?: string
              source: string | { id: string }
              target: string | { id: string }
            }
            const s = typeof lk.source === "object" ? lk.source.id : lk.source
            const t = typeof lk.target === "object" ? lk.target.id : lk.target
            // far-zoom: fade edges so the whole-system shape reads cleanly.
            if (!highlightSet && zoomRef.current < 0.35) return "rgba(148,163,184,0.05)"
            if (highlightSet) {
              return highlightSet.has(s) && highlightSet.has(t)
                ? "rgba(203,213,225,0.6)"
                : "rgba(148,163,184,0.04)"
            }
            if (lk.kind === "member") return "rgba(100,116,139,0.12)"
            if (lk.kind === "call") return "rgba(148,163,184,0.2)"
            return "rgba(203,213,225,0.32)"
          }}
          linkWidth={(l) => {
            const lk = l as FGLink
            if (lk.kind === "member") return 0.4
            if (lk.kind === "call") return 0.6
            return 0.8 + 3.5 * (lk.weight / maxWeight)
          }}
          linkCurvature={(l) => ((l as FGLink).kind === "flow" ? 0.16 : 0)}
          linkDirectionalArrowLength={(l) => ((l as FGLink).kind === "flow" ? 4 : 0)}
          linkDirectionalArrowRelPos={0.92}
          linkDirectionalParticles={(l) => (linkIsActive(l) ? 4 : 0)}
          linkDirectionalParticleWidth={2.5}
          linkDirectionalParticleColor={() => ACTIVITY.read}
          linkDirectionalParticleSpeed={0.01}
          nodeCanvasObject={(node, ctx, globalScale) => {
            const n = node as FGNode & { x: number; y: number }
            const groupOf =
              n.kind === "symbol" ? n.group : n.kind === "component" ? n.id : n.kind === "aggregate" ? n.group : ""
            const isolatedDim = isolatedGroup ? groupOf !== isolatedGroup : false
            const hoverDim = highlightSet ? !highlightSet.has(n.id) : false
            const anim = animatorRef.current.get(n.id)
            const st = useGraphStore.getState()
            const rt = n.kind === "symbol" ? st.runtime.get(n.id) : undefined
            const hovered = st.hoveredId === n.id
            const active = (rt?.agentState ?? "idle") !== "idle" || (rt?.activity ?? 0) > 0.05
            paintNode(n, ctx, globalScale, {
              dimmed: isolatedDim || hoverDim,
              selected: n.id === selectedQname,
              reveal: anim?.reveal.current ?? 1,
              pulse: anim?.pulse.current ?? 0,
              emphasis: anim?.emphasis.current ?? 0,
              agentState: rt?.agentState ?? "idle",
              heat: rt?.heat ?? 0,
              // symbol labels only show on demand: hovered, selected, or active
              showLabel: hovered || n.id === selectedQname || active,
              touchedGroup: n.kind === "component" && touchedGroupsRef.current.has(n.id),
              patchedCount: n.kind === "component" ? (patchedGroupCountRef.current.get(n.id) ?? 0) : 0,
            })
          }}
          nodePointerAreaPaint={(node, color, ctx) => {
            const n = node as FGNode & { x: number; y: number }
            ctx.fillStyle = color
            ctx.beginPath()
            ctx.arc(n.x, n.y, n.val + 2, 0, 2 * Math.PI)
            ctx.fill()
          }}
        />
      )}

      {graphLoading && (
        <div
          className="absolute inset-0 flex flex-col items-center justify-center gap-3 z-10"
          style={{ background: "color-mix(in srgb, var(--bg-app) 80%, transparent)" }}
        >
          <div
            className="w-8 h-8 border-2 rounded-full animate-spin"
            style={{ borderColor: "var(--border-strong)", borderTopColor: "var(--accent)" }}
          />
          <p className="text-2 text-sm">{graphLoadingMessage || "Loading…"}</p>
        </div>
      )}
      {!graphLoading && data.nodes.length === 0 && <EmptyGraphState />}
    </div>
  )
}

// Shown when the system model has no nodes and nothing is loading: a fresh
// checkout / uninitialised project. Offers the one action that fixes it (run
// init / refresh) rather than leaving the user at a dead end.
function EmptyGraphState() {
  const running = useTrieCommandStore((s) => s.running)
  const run = useTrieCommandStore((s) => s.run)
  const trieExists = useTrieConfigStore((s) => s.exists)
  const trieLoaded = useTrieConfigStore((s) => s.loaded)
  // init when there's no trie.toml yet; otherwise a refresh rebuilds the graph.
  const command = trieExists ? "refresh" : "init"
  const onRun = () => {
    if (running) return
    run(command, {})
    useTabsStore.getState().activate(TRIE_TAB_ID)
  }
  return (
    <div className="absolute inset-0 flex flex-col items-center justify-center gap-3 px-8 text-center">
      <p className="text-2 text-sm">No system model yet.</p>
      <p className="text-3 text-xs max-w-xs leading-relaxed">
        {trieExists
          ? "The graph is empty — run a refresh to build it from your source."
          : "This project isn’t initialised for trie yet."}
      </p>
      {trieLoaded && (
        <button
          className="inline-flex items-center gap-1.5 rounded-md bg-accent text-white px-3.5 py-1.5 text-xs font-medium disabled:opacity-60"
          onClick={onRun}
          disabled={running}
        >
          {running ? (
            <>
              <span
                className="w-3 h-3 border-2 rounded-full animate-spin"
                style={{ borderColor: "rgba(255,255,255,0.4)", borderTopColor: "#fff" }}
              />
              Working…
            </>
          ) : trieExists ? (
            "Build graph (refresh)"
          ) : (
            "Initialize trie"
          )}
        </button>
      )}
    </div>
  )
}

// Ambient HUD for non-symbol tools (bash/shell/fetch) — keeps off-graph agent
// actions visible. Auto-hides a few seconds after the last such tool.
function ToolHud() {
  const hud = useConductor((s) => s.hud)
  const [, force] = useState(0)
  useEffect(() => {
    if (!hud) return
    const t = setTimeout(() => force((n) => n + 1), 3500)
    return () => clearTimeout(t)
  }, [hud])
  if (!hud || Date.now() - hud.ts > 3500) return null
  return (
    <div className="absolute bottom-3 left-1/2 -translate-x-1/2 z-30 flex items-center gap-2 rounded-full border border-strong surface-pop elev-2 px-3 py-1 text-xs">
      <span
        className="w-3 h-3 border-2 rounded-full animate-spin"
        style={{ borderColor: "var(--border-strong)", borderTopColor: "var(--accent)" }}
      />
      <span className="font-mono text-2">{hud.tool}</span>
      {hud.text && <span className="text-3 font-mono truncate max-w-[280px]">{hud.text}</span>}
    </div>
  )
}

// Replay transport — re-plays the recorded choreography of the last turn.
function ReplayControl() {
  const count = useConductor((s) => s.cueLog.length)
  const replaying = useConductor((s) => s.replaying)
  if (count === 0) return null
  return (
    <button
      className="absolute top-3 right-3 z-30 rounded-md border border-strong surface-pop elev-1 px-2.5 py-1 text-xs text-2 hover:surface-3 hover:text-1 transition-colors disabled:opacity-50"
      onClick={() => replayTurn()}
      disabled={replaying}
      title="Replay the agent's last turn"
    >
      {replaying ? "▶ replaying…" : "↻ replay turn"}
    </button>
  )
}

// --- canvas painting --------------------------------------------------------

interface PaintOpts {
  dimmed: boolean
  selected: boolean
  reveal: number
  pulse: number
  emphasis: number
  agentState: string
  heat: number
  showLabel: boolean
  touchedGroup?: boolean
  patchedCount?: number
}

function paintNode(
  n: FGNode & { x: number; y: number },
  ctx: CanvasRenderingContext2D,
  globalScale: number,
  opts: PaintOpts,
): void {
  const { dimmed, selected, reveal, pulse, emphasis, agentState, heat, showLabel: wantLabel, touchedGroup, patchedCount } = opts
  const scale = (0.4 + 0.6 * reveal) * (1 + 0.25 * emphasis)
  const r = n.val * scale
  ctx.save()
  ctx.globalAlpha = dimmed ? 0.15 : reveal

  if (pulse > 0.01 && n.kind === "symbol") {
    const ringColor = activityColor(agentState)
    ctx.beginPath()
    ctx.arc(n.x, n.y, r + (4 + 18 * (1 - pulse)) / globalScale, 0, 2 * Math.PI)
    ctx.strokeStyle = ringColor
    ctx.globalAlpha = (dimmed ? 0.15 : 1) * pulse * 0.7
    ctx.lineWidth = 2 / globalScale
    ctx.stroke()
    ctx.globalAlpha = dimmed ? 0.15 : reveal
  }
  if (heat > 0.02 && n.kind === "symbol") {
    ctx.beginPath()
    ctx.arc(n.x, n.y, r * 2.2, 0, 2 * Math.PI)
    ctx.fillStyle = ACTIVITY.heat
    ctx.globalAlpha = (dimmed ? 0.08 : 0.22) * heat
    ctx.fill()
    ctx.globalAlpha = dimmed ? 0.15 : reveal
  }
  if (selected && n.kind === "symbol") {
    ctx.beginPath()
    ctx.arc(n.x, n.y, r + 4 / globalScale, 0, 2 * Math.PI)
    ctx.strokeStyle = "#a3e635"
    ctx.lineWidth = 2 / globalScale
    ctx.stroke()
  }

  if (n.kind === "aggregate") {
    ctx.beginPath()
    ctx.arc(n.x, n.y, r, 0, 2 * Math.PI)
    ctx.setLineDash([3, 3])
    ctx.strokeStyle = n.color
    ctx.lineWidth = 1.5 / globalScale
    ctx.stroke()
    ctx.setLineDash([])
    const fs = Math.max(9, 11 / globalScale)
    ctx.font = `${fs}px ui-sans-serif, system-ui, sans-serif`
    ctx.textAlign = "center"
    ctx.textBaseline = "middle"
    ctx.fillStyle = "#94a3b8"
    ctx.fillText(n.label, n.x, n.y)
    ctx.restore()
    return
  }

  if (n.kind === "component") {
    // PENDING-PATCH ring — an amber halo + dashed ring marks subsystems that
    // contain symbols with staged edits, so patches are obvious at the L0 map.
    if (patchedCount && patchedCount > 0) {
      ctx.beginPath()
      ctx.arc(n.x, n.y, r + (7 + 4) / globalScale, 0, 2 * Math.PI)
      ctx.fillStyle = "#f59e0b"
      ctx.globalAlpha = dimmed ? 0.06 : 0.12
      ctx.fill()
      ctx.beginPath()
      ctx.arc(n.x, n.y, r + 6 / globalScale, 0, 2 * Math.PI)
      ctx.setLineDash([3 / globalScale, 2 / globalScale])
      ctx.strokeStyle = "#f59e0b"
      ctx.globalAlpha = dimmed ? 0.3 : 0.9
      ctx.lineWidth = 1.75 / globalScale
      ctx.stroke()
      ctx.setLineDash([])
      ctx.globalAlpha = dimmed ? 0.15 : reveal
    }
    // PERSISTENT "touched this turn" ring — stays after the live pulse fades so
    // it's clear which subsystems the agent used to answer the question.
    if (touchedGroup) {
      ctx.beginPath()
      ctx.arc(n.x, n.y, r + 5 / globalScale, 0, 2 * Math.PI)
      ctx.strokeStyle = ACTIVITY.read
      ctx.globalAlpha = dimmed ? 0.2 : 0.7
      ctx.lineWidth = 1.5 / globalScale
      ctx.stroke()
      ctx.globalAlpha = dimmed ? 0.15 : reveal
    }
    // agent-activity glow: a soft halo + ring when symbols inside this group
    // are live, so you can see WHERE the agent is at the system level.
    if (pulse > 0.02) {
      ctx.beginPath()
      ctx.arc(n.x, n.y, r + (6 + 22 * pulse) / globalScale, 0, 2 * Math.PI)
      ctx.fillStyle = ACTIVITY.read
      ctx.globalAlpha = 0.1 * pulse
      ctx.fill()
      ctx.beginPath()
      ctx.arc(n.x, n.y, r + (4 + 8 * (1 - pulse)) / globalScale, 0, 2 * Math.PI)
      ctx.strokeStyle = ACTIVITY.read
      ctx.globalAlpha = Math.min(1, 0.5 + pulse)
      ctx.lineWidth = 2 / globalScale
      ctx.stroke()
      ctx.globalAlpha = 1
    }
    const expanded = n.expanded
    ctx.beginPath()
    ctx.arc(n.x, n.y, r, 0, 2 * Math.PI)
    if (expanded) {
      // when expanded, the anchor shrinks to a faint marker (the region IS the
      // container now); draw a small hollow ring.
      ctx.strokeStyle = n.color
      ctx.globalAlpha = dimmed ? 0.15 : 0.5
      ctx.lineWidth = 2 / globalScale
      ctx.arc(n.x, n.y, r * 0.5, 0, 2 * Math.PI)
      ctx.stroke()
      ctx.restore()
      return
    }
    ctx.fillStyle = n.color
    ctx.globalAlpha = dimmed ? 0.15 : 0.95
    ctx.fill()
    ctx.globalAlpha = dimmed ? 0.25 : 1
    const fs = Math.max(12, 13 / globalScale)
    ctx.textAlign = "center"
    ctx.textBaseline = "top"
    ctx.font = `600 ${fs}px ui-sans-serif, system-ui, sans-serif`
    ctx.fillStyle = "#f1f5f9"
    ctx.fillText(n.label, n.x, n.y + r + 4 / globalScale)
    ctx.font = `${Math.max(8, 9 / globalScale)}px ui-monospace, monospace`
    ctx.fillStyle = "#64748b"
    ctx.fillText(`${n.count}`, n.x, n.y + r + 4 / globalScale + fs * 1.05)
    // pending-patch pip: amber badge with the count of patched symbols inside.
    if (patchedCount && patchedCount > 0) {
      const px = n.x + r * 0.8
      const py = n.y - r * 0.8
      const pr = 5 / globalScale
      ctx.beginPath()
      ctx.arc(px, py, pr, 0, 2 * Math.PI)
      ctx.fillStyle = "#f59e0b"
      ctx.globalAlpha = 1
      ctx.fill()
      ctx.fillStyle = "#1e1206"
      ctx.font = `600 ${Math.max(7, 8 / globalScale)}px ui-sans-serif, system-ui, sans-serif`
      ctx.textAlign = "center"
      ctx.textBaseline = "middle"
      ctx.fillText(`${patchedCount}`, px, py)
    }
    ctx.restore()
    return
  }

  // symbol node
  const sym = n.node
  const marker = classMarker(sym.cls, n.color)
  if (marker.halo) {
    ctx.beginPath()
    ctx.arc(n.x, n.y, r * 1.8, 0, 2 * Math.PI)
    ctx.fillStyle = marker.halo
    ctx.globalAlpha = (dimmed ? 0.06 : 0.12) * reveal
    ctx.fill()
    ctx.globalAlpha = dimmed ? 0.15 : reveal
  }
  ctx.beginPath()
  if (marker.shape === "diamond") {
    ctx.moveTo(n.x, n.y - r)
    ctx.lineTo(n.x + r, n.y)
    ctx.lineTo(n.x, n.y + r)
    ctx.lineTo(n.x - r, n.y)
    ctx.closePath()
  } else {
    ctx.arc(n.x, n.y, r, 0, 2 * Math.PI)
  }
  ctx.fillStyle = n.color
  ctx.fill()
  if (marker.ring) {
    ctx.beginPath()
    ctx.arc(n.x, n.y, r + 2 / globalScale, 0, 2 * Math.PI)
    ctx.strokeStyle = marker.ring
    ctx.lineWidth = 1.5 / globalScale
    ctx.stroke()
  }
  // Labels on demand only: hovered / selected / active (wantLabel), or when
  // zoomed in far enough to read without collision. Keeps the map clean.
  const showLabel = wantLabel || globalScale >= 2.6
  if (showLabel) {
    const fs = Math.max(9, 12 / globalScale)
    const text = sym.name
    ctx.font = `${fs}px ui-sans-serif, system-ui, sans-serif`
    ctx.textAlign = "center"
    ctx.textBaseline = "top"
    // legibility backdrop so the label reads over neighbours
    const tw = ctx.measureText(text).width
    const ly = n.y + r + 3 / globalScale
    ctx.fillStyle = "rgba(2,6,23,0.82)"
    ctx.fillRect(n.x - tw / 2 - 3 / globalScale, ly - 1 / globalScale, tw + 6 / globalScale, fs + 3 / globalScale)
    ctx.fillStyle = wantLabel ? "#f1f5f9" : "#cbd5e1"
    ctx.fillText(text, n.x, ly)
  }
  ctx.restore()
}
