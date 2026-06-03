import { useCallback, useEffect, useMemo, useRef } from "react"
import ForceGraph2D, { type ForceGraphMethods } from "react-force-graph-2d"
import { useGraphStore } from "@/store/graphStore"
import { useAppStore } from "@/store/appStore"
import { componentView } from "@/graph/doi"
import { roleColor, subsystemColor, nodeRadius, classMarker, ACTIVITY } from "@/graph/style"
import { GraphAnimator } from "@/graph/animator"
import { SearchPalette } from "./SearchPalette"
import { Legend } from "./Legend"
import type { SystemModelNode } from "@/api/types"

interface GraphCanvasProps {
  className?: string
}

// A force-graph node is either a real symbol, an L0 component, or a "+N" bubble.
type FGNode =
  | { kind: "component"; id: string; label: string; count: number; color: string; val: number; expanded?: boolean; order?: number }
  | { kind: "symbol"; id: string; node: SystemModelNode; color: string; val: number }
  | { kind: "aggregate"; id: string; label: string; count: number; color: string; val: number }

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

  // Is the agent currently traversing this link? (either direction)
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const linkIsActive = useCallback((l: any) => {
    const flows = useGraphStore.getState().activeFlows
    if (!flows.size) return false
    const s = typeof l.source === "object" ? l.source.id : l.source
    const t = typeof l.target === "object" ? l.target.id : l.target
    return flows.has(`${s}|${t}`) || flows.has(`${t}|${s}`)
  }, [])

  // Build the graph data. The L0 component graph is ALWAYS the backbone; when
  // components are expanded, their member symbols bloom OUT of the parent
  // component node (linked to it) — expand-in-place, never a view swap.
  const data = useMemo(() => {
    if (!model) return { nodes: [] as FGNode[], links: [] as FGLink[] }

    const view = componentView(model, axis)
    const expanded = new Set<string>(pinnedExpansions)
    if (focusedExpansion) expanded.add(focusedExpansion)
    const groupByKey = new Map(view.groups.map((g) => [g.key, g]))

    const nodes: FGNode[] = []
    const links: FGLink[] = []

    // 1) component backbone — UNIFORM size (size shouldn't mislead); count is
    //    shown as text. order = left(entry)->right(foundation) by call depth.
    const COMP_R = 13
    for (const g of view.groups) {
      const isExpanded = expanded.has(g.key)
      nodes.push({
        kind: "component",
        id: g.key,
        label: g.key.split("/").pop() ?? g.key,
        count: g.count,
        color: colorOf(g.key),
        val: COMP_R,
        expanded: isExpanded,
        order: g.order,
      })
    }
    const presentComp = new Set(view.groups.map((g) => g.key))
    for (const f of view.flows) {
      if (presentComp.has(f.source) && presentComp.has(f.target)) {
        links.push({ source: f.source, target: f.target, weight: f.weight, kind: "flow" })
      }
    }

    // 2) members of expanded components, linked to their parent component node.
    //    Emphasis depends on the group's CHARACTER: entry-facing groups lead
    //    with their doors; foundational groups lead with their most-depended-on.
    if (expanded.size > 0) {
      const groupKey = (n: (typeof visible.nodes)[number]) =>
        axis === "role" ? n.role || "untagged" : n.subsystem
      const isLead = (n: (typeof visible.nodes)[number], character: string) => {
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
        nodes.push({
          kind: "symbol",
          id: n.qname,
          node: n,
          color: colorOf(gk),
          // lead symbols for the group's character render larger (emphasis)
          val: nodeRadius(n.salience, n.cls) * (lead ? 1.5 : 0.85),
        })
        // tether member -> its component anchor (containment)
        links.push({ source: gk, target: n.qname, weight: 0, kind: "member" })
      }
      // aggregates ("+N") for the folded tail of each expanded component
      for (const agg of visible.aggregates) {
        if (!expanded.has(agg.key)) continue
        nodes.push({
          kind: "aggregate",
          id: agg.id,
          label: `+${agg.count}`,
          count: agg.count,
          color: colorOf(agg.key),
          val: 6 + 8 * Math.sqrt(agg.count / 50),
        })
        links.push({ source: agg.key, target: agg.id, weight: 0, kind: "member" })
      }
      // real call edges among shown members (so structure is visible)
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
  }, [model, axis, visible, colorOf, focusedExpansion, pinnedExpansions])

  useEffect(() => {
    if (!data.nodes.length || !fgRef.current) return
    const fg = fgRef.current
    const expanded = focusedExpansion !== null || pinnedExpansions.size > 0
    // sparse + readable: strong repulsion so role labels never overlap
    fg.d3Force("charge")?.strength(expanded ? -220 : -900)
    // member tethers short (cluster around parent), flow edges long (spread roles)
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const linkForce = fg.d3Force("link") as any
    if (linkForce?.distance) {
      linkForce.distance((l: FGLink) =>
        l.kind === "member" ? 34 : l.kind === "call" ? 48 : 220,
      )
    }

    // Left->right ordering: pin each component's x by its call-flow order
    // (0=entry on the left, 1=foundation on the right). y stays force-driven.
    // Members of expanded groups float free (fx cleared).
    const COL_SPAN = 1100
    for (const n of data.nodes as Array<FGNode & { fx?: number; x?: number }>) {
      if (n.kind === "component" && typeof n.order === "number") {
        n.fx = (n.order - 0.5) * COL_SPAN
      } else {
        // ensure prior pins don't stick to reused symbol objects
        delete (n as { fx?: number }).fx
      }
    }

    // register nodes for the reveal animation (new ones born at 0)
    const anim = animatorRef.current
    const present = new Set<string>()
    for (const n of data.nodes) {
      present.add(n.id)
      anim.ensure(n.id, true)
    }
    anim.prune(present)
    fg.d3ReheatSimulation?.()
    const t = setTimeout(() => fg.zoomToFit(800, 80), 250)
    return () => clearTimeout(t)
  }, [data, focusedExpansion, pinnedExpansions])

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

  const anyExpanded = focusedExpansion !== null || pinnedExpansions.size > 0

  return (
    <div className={`relative flex-1 bg-slate-950 ${className ?? ""}`}>
      {/* breadcrumb / level affordance */}
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
            const lk = l as unknown as {
              kind?: string
              source: string | { id: string }
              target: string | { id: string }
            }
            const s = typeof lk.source === "object" ? lk.source.id : lk.source
            const t = typeof lk.target === "object" ? lk.target.id : lk.target
            if (highlightSet) {
              return highlightSet.has(s) && highlightSet.has(t)
                ? "rgba(148,163,184,0.6)"
                : "rgba(148,163,184,0.04)"
            }
            if (lk.kind === "member") return "rgba(100,116,139,0.18)" // faint tether
            if (lk.kind === "call") return "rgba(148,163,184,0.22)"
            return "rgba(148,163,184,0.38)" // role->role flow: most prominent
          }}
          linkWidth={(l) => {
            const lk = l as FGLink
            if (lk.kind === "member") return 0.5
            if (lk.kind === "call") return 0.6
            return 0.6 + 3.5 * (lk.weight / maxWeight) // flow scaled by call volume
          }}
          linkCurvature={(l) => ((l as FGLink).kind === "flow" ? 0.18 : 0)}
          linkDirectionalArrowLength={(l) => ((l as FGLink).kind === "flow" ? 4 : 0)}
          linkDirectionalArrowRelPos={0.9}
          linkDirectionalParticles={(l) => (linkIsActive(l) ? 4 : 0)}
          linkDirectionalParticleWidth={2.5}
          linkDirectionalParticleColor={() => ACTIVITY.read}
          linkDirectionalParticleSpeed={0.01}
          nodeCanvasObject={(node, ctx, globalScale) => {
            const n = node as FGNode & { x: number; y: number }
            const groupOf =
              n.kind === "symbol"
                ? axis === "role"
                  ? n.node.role || "untagged"
                  : n.node.subsystem
                : n.kind === "component"
                  ? n.id
                  : n.id.replace(/^\+agg:[^:]+:/, "")
            const isolatedDim = isolatedGroup ? groupOf !== isolatedGroup : false
            const hoverDim = highlightSet ? !highlightSet.has(n.id) : false
            const dimmed = isolatedDim || hoverDim
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
    const expanded = n.expanded
    // uniform dot; expanded = hollow "opened container"
    ctx.beginPath()
    ctx.arc(n.x, n.y, r, 0, 2 * Math.PI)
    if (expanded) {
      ctx.fillStyle = n.color
      ctx.globalAlpha = 0.18
      ctx.fill()
      ctx.globalAlpha = dimmed ? 0.18 : 1
      ctx.strokeStyle = n.color
      ctx.lineWidth = 2.5 / globalScale
      ctx.stroke()
    } else {
      ctx.fillStyle = n.color
      ctx.globalAlpha = dimmed ? 0.18 : 0.95
      ctx.fill()
    }
    ctx.globalAlpha = dimmed ? 0.25 : 1
    // role label below the dot (never overlapping it), count under that
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
