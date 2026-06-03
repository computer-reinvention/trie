import { useCallback, useEffect, useMemo, useRef } from "react"
import ForceGraph2D, { type ForceGraphMethods } from "react-force-graph-2d"
import { forceCollide, forceX, forceY } from "d3-force"
import { useGraphStore } from "@/store/graphStore"
import { useAppStore } from "@/store/appStore"
import { componentView } from "@/graph/doi"
import { nodeRadius, classMarker, ACTIVITY, depthColor } from "@/graph/style"
import { GraphAnimator } from "@/graph/animator"
import { SearchPalette } from "./SearchPalette"
import { Legend } from "./Legend"
import type { SystemModelNode } from "@/api/types"

interface GraphCanvasProps {
  className?: string
}

// Position spread for the left->right call-flow axis.
const COL_SPAN = 1600

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
    }

interface FGLink {
  source: string
  target: string
  weight: number
  kind?: "flow" | "member" | "call"
}

// Depth order per group key, for color + x-position of member nodes.
function maxDepthFor(nodes: SystemModelNode[]): number {
  let m = 1
  for (const n of nodes) if (n.depth > m) m = n.depth
  return m
}

export function GraphCanvas({ className }: GraphCanvasProps) {
  const {
    model,
    axis,
    visible,
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

  const maxDepth = useMemo(() => (model ? maxDepthFor(model.nodes) : 1), [model])

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
    if (!model) return { nodes: [] as FGNode[], links: [] as FGLink[] }

    const view = componentView(model, axis)
    const expanded = new Set<string>(pinnedExpansions)
    if (focusedExpansion) expanded.add(focusedExpansion)
    const groupByKey = new Map(view.groups.map((g) => [g.key, g]))

    const nodes: FGNode[] = []
    const links: FGLink[] = []
    const COMP_R = 14

    for (const g of view.groups) {
      nodes.push({
        kind: "component",
        id: g.key,
        label: g.key.split("/").pop() ?? g.key,
        count: g.count,
        color: depthColor(g.order),
        val: COMP_R,
        expanded: expanded.has(g.key),
        order: g.order,
      })
    }
    const presentComp = new Set(view.groups.map((g) => g.key))
    for (const f of view.flows) {
      if (presentComp.has(f.source) && presentComp.has(f.target)) {
        links.push({ source: f.source, target: f.target, weight: f.weight, kind: "flow" })
      }
    }

    if (expanded.size > 0) {
      const groupKey = (n: SystemModelNode) =>
        axis === "role" ? n.role || "untagged" : n.subsystem
      const isLead = (n: SystemModelNode, character: string) => {
        if (character === "entry") return n.cls === "door"
        if (character === "foundation") return n.cls === "bedrock" || n.cls === "hub"
        return n.cls === "hub" || n.cls === "door"
      }
      const shownIds = new Set<string>()
      for (const n of visible.nodes) {
        const gk = groupKey(n)
        if (!expanded.has(gk)) continue
        shownIds.add(n.qname)
        const character = groupByKey.get(gk)?.character ?? "mixed"
        const lead = isLead(n, character)
        const t = n.depth >= 0 ? n.depth / maxDepth : 0.5
        nodes.push({
          kind: "symbol",
          id: n.qname,
          node: n,
          color: depthColor(t),
          val: nodeRadius(n.salience, n.cls) * (lead ? 1.5 : 0.9),
          group: gk,
          order: groupByKey.get(gk)?.order ?? 0.5,
        })
        links.push({ source: gk, target: n.qname, weight: 0, kind: "member" })
      }
      for (const agg of visible.aggregates) {
        if (!expanded.has(agg.key)) continue
        nodes.push({
          kind: "aggregate",
          id: agg.id,
          label: `+${agg.count}`,
          count: agg.count,
          color: depthColor(groupByKey.get(agg.key)?.order ?? 0.5),
          val: 9,
          group: agg.key,
          order: groupByKey.get(agg.key)?.order ?? 0.5,
        })
        links.push({ source: agg.key, target: agg.id, weight: 0, kind: "member" })
      }
      const adj = useGraphStore.getState().adjacency
      const seen = new Set<string>()
      for (const n of visible.nodes) {
        if (!shownIds.has(n.qname)) continue
        const nbrs = adj?.neighbours.get(n.qname)
        if (!nbrs) continue
        for (const w of nbrs) {
          if (shownIds.has(w)) {
            const id = n.qname < w ? `${n.qname}|${w}` : `${w}|${n.qname}`
            if (!seen.has(id)) {
              seen.add(id)
              links.push({ source: n.qname, target: w, weight: 1, kind: "call" })
            }
          }
        }
      }
    }

    return { nodes, links }
  }, [model, axis, visible, focusedExpansion, pinnedExpansions, maxDepth])

  useEffect(() => {
    if (!data.nodes.length || !fgRef.current) return
    const fg = fgRef.current
    const expanded = focusedExpansion !== null || pinnedExpansions.size > 0

    // Sparsity: strong repulsion. No-overlap: collision sized to node radius +
    // generous padding (and bigger for component anchors so their labels clear).
    fg.d3Force("charge")?.strength(expanded ? -300 : -1200)
    fg.d3Force(
      "collide",
      forceCollide<FGNode>()
        .radius((n) => (n.kind === "component" ? n.val + 46 : n.val + 14))
        .strength(1)
        .iterations(3),
    )
    // Left->right by call order. Components hard-pin via fx; members pulled
    // toward their group's column so the community sits under its anchor.
    fg.d3Force(
      "x",
      forceX<FGNode>((n) => (n.order - 0.5) * COL_SPAN).strength((n) =>
        n.kind === "component" ? 1 : 0.25,
      ),
    )
    fg.d3Force("y", forceY<FGNode>(0).strength(0.04))
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const linkForce = fg.d3Force("link") as any
    if (linkForce?.distance) {
      linkForce.distance((l: FGLink) =>
        l.kind === "member" ? 60 : l.kind === "call" ? 70 : 320,
      )
    }

    for (const n of data.nodes as FGNode[]) {
      if (n.kind === "component") n.fx = (n.order - 0.5) * COL_SPAN
    }

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

  // Draw bounded community regions behind expanded groups (the "container").
  const drawRegions = useCallback(
    (ctx: CanvasRenderingContext2D) => {
      if (!anyExpanded) return
      const expanded = new Set<string>(pinnedExpansions)
      if (focusedExpansion) expanded.add(focusedExpansion)
      // gather member positions per group
      const byGroup = new Map<string, Array<{ x: number; y: number; r: number }>>()
      for (const n of data.nodes as Array<FGNode & { x?: number; y?: number }>) {
        const g =
          n.kind === "component"
            ? n.id
            : n.kind === "symbol"
              ? n.group
              : n.kind === "aggregate"
                ? n.group
                : null
        if (!g || !expanded.has(g)) continue
        if (n.x == null || n.y == null) continue
        if (!byGroup.has(g)) byGroup.set(g, [])
        byGroup.get(g)!.push({ x: n.x, y: n.y, r: n.val })
      }
      for (const [g, pts] of byGroup) {
        if (pts.length < 1) continue
        let minX = Infinity,
          minY = Infinity,
          maxX = -Infinity,
          maxY = -Infinity
        for (const p of pts) {
          minX = Math.min(minX, p.x - p.r)
          minY = Math.min(minY, p.y - p.r)
          maxX = Math.max(maxX, p.x + p.r)
          maxY = Math.max(maxY, p.y + p.r)
        }
        const pad = 26
        const x = minX - pad,
          y = minY - pad,
          w = maxX - minX + pad * 2,
          h = maxY - minY + pad * 2
        const order =
          (data.nodes.find((n) => n.kind === "component" && n.id === g) as
            | (FGNode & { order: number })
            | undefined)?.order ?? 0.5
        const col = depthColor(order)
        const radius = 22
        ctx.beginPath()
        roundRect(ctx, x, y, w, h, radius)
        ctx.fillStyle = col
        ctx.globalAlpha = 0.07
        ctx.fill()
        ctx.globalAlpha = 0.5
        ctx.lineWidth = 1.5
        ctx.strokeStyle = col
        ctx.stroke()
        ctx.globalAlpha = 1
        // group title in the container's top-left
        ctx.font = "600 13px ui-sans-serif, system-ui, sans-serif"
        ctx.textAlign = "left"
        ctx.textBaseline = "bottom"
        ctx.fillStyle = col
        ctx.fillText(g.split("/").pop() ?? g, x + 10, y + 18)
      }
    },
    [anyExpanded, data.nodes, focusedExpansion, pinnedExpansions],
  )

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const onNodeClick = useCallback(
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (node: any) => {
      const n = node as FGNode
      if (n.kind === "component") expandComponent(n.id)
      else if (n.kind === "aggregate") expandComponent(n.group)
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
      <Legend />
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
          onRenderFramePre={(ctx) => {
            drawRegions(ctx as CanvasRenderingContext2D)
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
            const rt = n.kind === "symbol" ? useGraphStore.getState().runtime.get(n.id) : undefined
            paintNode(n, ctx, globalScale, {
              dimmed: isolatedDim || hoverDim,
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

function roundRect(ctx: CanvasRenderingContext2D, x: number, y: number, w: number, h: number, r: number) {
  const rr = Math.min(r, w / 2, h / 2)
  ctx.moveTo(x + rr, y)
  ctx.arcTo(x + w, y, x + w, y + h, rr)
  ctx.arcTo(x + w, y + h, x, y + h, rr)
  ctx.arcTo(x, y + h, x, y, rr)
  ctx.arcTo(x, y, x + w, y, rr)
  ctx.closePath()
}

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
  const showLabel =
    globalScale >= 1.6 || ((sym.cls === "hub" || sym.cls === "door") && globalScale >= 0.7)
  if (showLabel) {
    const fs = Math.max(8, 11 / globalScale)
    ctx.font = `${fs}px ui-sans-serif, system-ui, sans-serif`
    ctx.textAlign = "center"
    ctx.textBaseline = "top"
    ctx.fillStyle = "#cbd5e1"
    ctx.fillText(sym.name, n.x, n.y + r + 2 / globalScale)
  }
  ctx.restore()
}
