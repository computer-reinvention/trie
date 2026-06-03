import { useCallback, useEffect, useMemo, useRef } from "react"
import ForceGraph2D, { type ForceGraphMethods } from "react-force-graph-2d"
import { useGraphStore } from "@/store/graphStore"
import { useAppStore } from "@/store/appStore"
import { componentView } from "@/graph/doi"
import { roleColor, subsystemColor, nodeRadius, classMarker, ACTIVITY } from "@/graph/style"
import { GraphAnimator } from "@/graph/animator"
import { SearchPalette } from "./SearchPalette"
import type { SystemModelNode } from "@/api/types"

interface GraphCanvasProps {
  className?: string
}

// A force-graph node is either a real symbol, an L0 component, or a "+N" bubble.
type FGNode =
  | { kind: "component"; id: string; label: string; count: number; color: string; val: number }
  | { kind: "symbol"; id: string; node: SystemModelNode; color: string; val: number }
  | { kind: "aggregate"; id: string; label: string; count: number; color: string; val: number }

interface FGLink {
  source: string
  target: string
  weight: number
}

export function GraphCanvas({ className }: GraphCanvasProps) {
  const { model, axis, level, visible, hoveredId, adjacency, selectedQname } = useGraphStore()
  const expandComponent = useGraphStore((s) => s.expandComponent)
  const togglePin = useGraphStore((s) => s.togglePin)
  const selectNode = useGraphStore((s) => s.selectNode)
  const setHovered = useGraphStore((s) => s.setHovered)
  const collapseTransient = useGraphStore((s) => s.collapseTransient)
  const { graphLoading, graphLoadingMessage } = useAppStore()
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const fgRef = useRef<ForceGraphMethods<any, any> | undefined>(undefined)
  const animatorRef = useRef(new GraphAnimator())

  const colorOf = axis === "role" ? roleColor : subsystemColor

  // Neighbours of the hovered node (for the spotlight: highlight + dim the rest).
  const highlightSet = useMemo(() => {
    if (!hoveredId) return null
    const s = new Set<string>([hoveredId])
    const nbrs = adjacency?.neighbours.get(hoveredId)
    if (nbrs) for (const w of nbrs) s.add(w)
    return s
  }, [hoveredId, adjacency])

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const onNodeClick = useCallback(
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (node: any) => {
      const n = node as FGNode
      if (n.kind === "component") {
        expandComponent(n.id)
      } else if (n.kind === "aggregate") {
        // expanding an aggregate: drill into its group (raises local detail)
        expandComponent(n.id.replace(/^\+agg:[^:]+:/, ""))
      } else if (n.kind === "symbol") {
        selectNode(n.id)
        window.dispatchEvent(
          new CustomEvent("trie:node-selected", { detail: { qname: n.id } }),
        )
        if (fgRef.current) {
          const p = node as { x: number; y: number }
          fgRef.current.centerAt(p.x, p.y, 600)
        }
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
    (node: any) => {
      setHovered(node ? (node as FGNode).id : null)
    },
    [setHovered],
  )

  // Build the graph data for the current level. L0 = component diagram; deeper
  // levels = the DOI-bounded symbol set + "+N" aggregate bubbles.
  const data = useMemo(() => {
    if (!model) return { nodes: [] as FGNode[], links: [] as FGLink[] }

    if (level === "components") {
      const view = componentView(model, axis)
      const maxCount = Math.max(1, ...view.groups.map((g) => g.count))
      const nodes: FGNode[] = view.groups.map((g) => ({
        kind: "component",
        id: g.key,
        label: g.key.split("/").pop() ?? g.key,
        count: g.count,
        color: colorOf(g.key),
        val: 4 + 20 * Math.sqrt(g.count / maxCount),
      }))
      const present = new Set(nodes.map((n) => n.id))
      const links: FGLink[] = view.flows
        .filter((f) => present.has(f.source) && present.has(f.target))
        .map((f) => ({ source: f.source, target: f.target, weight: f.weight }))
      return { nodes, links }
    }

    // L1/L2 — DOI visible symbol set + aggregates.
    const nodes: FGNode[] = visible.nodes.map((n) => ({
      kind: "symbol",
      id: n.qname,
      node: n,
      color: colorOf(axis === "role" ? n.role || "untagged" : n.subsystem),
      val: nodeRadius(n.salience, n.cls),
    }))
    for (const agg of visible.aggregates) {
      nodes.push({
        kind: "aggregate",
        id: agg.id,
        label: `+${agg.count} ${agg.key.split("/").pop() ?? agg.key}`,
        count: agg.count,
        color: colorOf(agg.key),
        val: 6 + 10 * Math.sqrt(agg.count / 50),
      })
    }
    // edges among visible symbols only (tapered caller->callee drawn in paint)
    const shownIds = new Set(visible.nodes.map((n) => n.qname))
    const links: FGLink[] = []
    const seen = new Set<string>()
    for (const n of visible.nodes) {
      const nbrs = useGraphStore.getState().adjacency?.neighbours.get(n.qname)
      if (!nbrs) continue
      for (const w of nbrs) {
        if (shownIds.has(w)) {
          const id = n.qname < w ? `${n.qname}|${w}` : `${w}|${n.qname}`
          if (!seen.has(id)) {
            seen.add(id)
            links.push({ source: n.qname, target: w, weight: 1 })
          }
        }
      }
    }
    return { nodes, links }
  }, [model, axis, level, visible, colorOf])

  useEffect(() => {
    if (!data.nodes.length || !fgRef.current) return
    const fg = fgRef.current
    fg.d3Force("charge")?.strength(level === "components" ? -300 : -120)
    // register nodes for the reveal animation (new ones born at 0)
    const anim = animatorRef.current
    const present = new Set<string>()
    for (const n of data.nodes) {
      present.add(n.id)
      anim.ensure(n.id, true)
    }
    anim.prune(present)
    const t = setTimeout(() => fg.zoomToFit(800, 60), 200)
    return () => clearTimeout(t)
  }, [data, level])

  // decay activity (fast) + heat (slow) on a rAF loop so pulses fade and edit
  // warmth cools even when the sim is frozen.
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

  const { focusedExpansion, pinnedExpansions } = useGraphStore()

  return (
    <div className={`relative flex-1 bg-slate-950 ${className ?? ""}`}>
      {/* breadcrumb / level affordance */}
      {level !== "components" && (
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
      {data.nodes.length > 0 && (
        <ForceGraph2D
          ref={fgRef}
          graphData={data}
          backgroundColor="#020617"
          nodeRelSize={1}
          nodeVal={(n) => (n as FGNode).val}
          cooldownTicks={120}
          warmupTicks={20}
          d3VelocityDecay={0.3}
          autoPauseRedraw={false}
          onRenderFramePre={() => {
            // The animation heart: advance springs + sync targets from store
            // runtime once per frame, before nodes paint.
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
          }}
          onNodeClick={onNodeClick}
          onNodeRightClick={onNodeRightClick}
          onNodeHover={onNodeHover}
          onBackgroundClick={onBackgroundClick}
          linkColor={(l) => {
            const lk = l as unknown as { source: { id: string }; target: { id: string } }
            if (highlightSet) {
              const s = typeof lk.source === "object" ? lk.source.id : (lk.source as unknown as string)
              const t = typeof lk.target === "object" ? lk.target.id : (lk.target as unknown as string)
              return highlightSet.has(s) && highlightSet.has(t)
                ? "rgba(148,163,184,0.55)"
                : "rgba(148,163,184,0.06)"
            }
            return "rgba(148,163,184,0.22)"
          }}
          linkWidth={(l) => 0.5 + 2.5 * ((l as FGLink).weight / maxWeight)}
          linkCurvature={0.12}
          nodeCanvasObject={(node, ctx, globalScale) => {
            const n = node as FGNode & { x: number; y: number }
            const dimmed = highlightSet ? !highlightSet.has(n.id) : false
            const anim = animatorRef.current.get(n.id)
            const rt = n.kind === "symbol" ? useGraphStore.getState().runtime.get(n.id) : undefined
            paintNode(n, ctx, globalScale, {
              dimmed,
              selected: n.id === selectedQname,
              reveal: anim?.reveal.current ?? 1,
              pulse: anim?.pulse.current ?? 0,
              emphasis: anim?.emphasis.current ?? 0,
              agentState: rt?.agentState ?? "idle",
              heat: rt?.heat ?? 0,
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
}

function paintNode(
  n: FGNode & { x: number; y: number },
  ctx: CanvasRenderingContext2D,
  globalScale: number,
  opts: PaintOpts,
): void {
  const { dimmed, selected, reveal, pulse, emphasis, agentState, heat } = opts
  // reveal: scale + fade in on first appearance; emphasis: grow on hover/select
  const scale = (0.4 + 0.6 * reveal) * (1 + 0.25 * emphasis)
  const r = n.val * scale
  ctx.save()
  ctx.globalAlpha = dimmed ? 0.18 : reveal

  // sonar pulse ring (agent reading/writing) — expands outward and fades
  if (pulse > 0.01 && n.kind === "symbol") {
    const ringColor = agentState === "writing" ? ACTIVITY.write : ACTIVITY.read
    ctx.beginPath()
    ctx.arc(n.x, n.y, r + (4 + 18 * (1 - pulse)) / globalScale, 0, 2 * Math.PI)
    ctx.strokeStyle = ringColor
    ctx.globalAlpha = (dimmed ? 0.18 : 1) * pulse * 0.7
    ctx.lineWidth = 2 / globalScale
    ctx.stroke()
    ctx.globalAlpha = dimmed ? 0.18 : reveal
  }

  // residual edit heat — a warm glow that lingers
  if (heat > 0.02 && n.kind === "symbol") {
    ctx.beginPath()
    ctx.arc(n.x, n.y, r * 2.2, 0, 2 * Math.PI)
    ctx.fillStyle = ACTIVITY.heat
    ctx.globalAlpha = (dimmed ? 0.1 : 0.22) * heat
    ctx.fill()
    ctx.globalAlpha = dimmed ? 0.18 : reveal
  }

  if (selected && n.kind === "symbol") {
    ctx.beginPath()
    ctx.arc(n.x, n.y, r + 4 / globalScale, 0, 2 * Math.PI)
    ctx.strokeStyle = "#a3e635"
    ctx.lineWidth = 2 / globalScale
    ctx.stroke()
  }

  if (n.kind === "aggregate") {
    // "+N" bubble: dashed, hollow — clearly a fold-out, not a real symbol
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
    ctx.beginPath()
    ctx.arc(n.x, n.y, r, 0, 2 * Math.PI)
    ctx.fillStyle = n.color
    ctx.globalAlpha = 0.9
    ctx.fill()
    ctx.globalAlpha = 1
    const fs = Math.max(11, 13 / globalScale)
    ctx.font = `${fs}px ui-sans-serif, system-ui, sans-serif`
    ctx.textAlign = "center"
    ctx.textBaseline = "middle"
    ctx.fillStyle = "#e2e8f0"
    ctx.fillText(n.label, n.x, n.y + r + fs)
    ctx.fillStyle = "rgba(2,6,23,0.85)"
    ctx.font = `${Math.max(9, 10 / globalScale)}px ui-monospace, monospace`
    ctx.fillText(String(n.count), n.x, n.y)
    ctx.restore()
    return
  }

  // symbol node
  const sym = n.node
  const marker = classMarker(sym.cls, n.color)

  // halo for hubs
  if (marker.halo) {
    ctx.beginPath()
    ctx.arc(n.x, n.y, r * 1.8, 0, 2 * Math.PI)
    ctx.fillStyle = marker.halo
    ctx.globalAlpha = 0.12
    ctx.fill()
    ctx.globalAlpha = 1
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

  // door ring
  if (marker.ring) {
    ctx.beginPath()
    ctx.arc(n.x, n.y, r + 2 / globalScale, 0, 2 * Math.PI)
    ctx.strokeStyle = marker.ring
    ctx.lineWidth = 1.5 / globalScale
    ctx.stroke()
  }

  // LOD labels: hubs/doors at mid zoom, everything when zoomed in
  const showLabel =
    globalScale >= 2 || ((sym.cls === "hub" || sym.cls === "door") && globalScale >= 0.8)
  if (showLabel) {
    const fs = Math.max(8, 11 / globalScale)
    ctx.font = `${fs}px ui-sans-serif, system-ui, sans-serif`
    ctx.textAlign = "center"
    ctx.textBaseline = "middle"
    ctx.fillStyle = "#cbd5e1"
    ctx.fillText(sym.name, n.x, n.y + r + fs)
  }
  ctx.restore()
}
