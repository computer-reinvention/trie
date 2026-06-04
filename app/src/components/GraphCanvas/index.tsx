import { useCallback, useEffect, useMemo, useRef, useState } from "react"
import ForceGraph2D, { type ForceGraphMethods } from "react-force-graph-2d"
import { forceCollide } from "d3-force"
import { useGraphStore } from "@/store/graphStore"
import { useAppStore } from "@/store/appStore"
import { componentView, memberSubgroup } from "@/graph/doi"
import { nodeRadius, classMarker, ACTIVITY, depthColor } from "@/graph/style"
import { GraphAnimator } from "@/graph/animator"
import { SearchPalette } from "./SearchPalette"
import { ExpandedPanel } from "./ExpandedPanel"
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
  const { graphLoading, graphLoadingMessage } = useAppStore()
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const fgRef = useRef<ForceGraphMethods<any, any> | undefined>(undefined)
  const animatorRef = useRef(new GraphAnimator())
  // live screen position of the focused role node, so the sub-graph panel can
  // anchor to it (act like a graph node, panning/zooming with the canvas).
  const [anchor, setAnchor] = useState<{ x: number; y: number } | null>(null)

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
    const flows = useGraphStore.getState().activeFlows
    if (!flows.size) return false
    const s = typeof l.source === "object" ? l.source.id : l.source
    const t = typeof l.target === "object" ? l.target.id : l.target
    return flows.has(`${s}|${t}`) || flows.has(`${t}|${s}`)
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
    (node: any) => {
      const n = node as FGNode
      if (n.kind === "component") togglePin(n.id)
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
    <div className={`relative flex-1 bg-slate-950 ${className ?? ""}`}>
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
      <ExpandedPanel anchor={anchor} />
      {data.nodes.length > 0 && (
        <ForceGraph2D
          ref={fgRef}
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
            for (const fgn of data.nodes) {
              if (fgn.kind !== "symbol") {
                anim.ensure(fgn.id)
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
          linkColor={(l) => {
            const lk = l as unknown as {
              kind?: string
              source: string | { id: string }
              target: string | { id: string }
            }
            const s = typeof lk.source === "object" ? lk.source.id : lk.source
            const t = typeof lk.target === "object" ? lk.target.id : lk.target
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
        <div className="absolute inset-0 bg-slate-950/80 flex flex-col items-center justify-center gap-3 z-10">
          <div className="w-8 h-8 border-2 border-slate-600 border-t-indigo-400 rounded-full animate-spin" />
          <p className="text-slate-400 text-sm">{graphLoadingMessage || "Loading…"}</p>
        </div>
      )}
      {!graphLoading && data.nodes.length === 0 && (
        <div className="absolute inset-0 flex items-center justify-center">
          <p className="text-slate-600 text-sm">No system model loaded.</p>
        </div>
      )}
    </div>
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
}

function paintNode(
  n: FGNode & { x: number; y: number },
  ctx: CanvasRenderingContext2D,
  globalScale: number,
  opts: PaintOpts,
): void {
  const { dimmed, selected, reveal, pulse, emphasis, agentState, heat, showLabel: wantLabel } = opts
  const scale = (0.4 + 0.6 * reveal) * (1 + 0.25 * emphasis)
  const r = n.val * scale
  ctx.save()
  ctx.globalAlpha = dimmed ? 0.15 : reveal

  if (pulse > 0.01 && n.kind === "symbol") {
    const ringColor = agentState === "writing" ? ACTIVITY.write : ACTIVITY.read
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
