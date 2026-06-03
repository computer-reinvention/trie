import { useEffect, useMemo, useRef } from "react"
import ForceGraph2D, { type ForceGraphMethods } from "react-force-graph-2d"
import { useGraphStore } from "@/store/graphStore"
import { useAppStore } from "@/store/appStore"
import { componentView } from "@/graph/doi"
import { roleColor, subsystemColor } from "@/graph/style"

interface GraphCanvasProps {
  className?: string
}

// L0 component node shape for force-graph.
interface CompNode {
  id: string
  label: string
  count: number
  doorCount: number
  hubCount: number
  color: string
  val: number // force-graph node "value" -> area
}

interface CompLink {
  source: string
  target: string
  weight: number
}

export function GraphCanvas({ className }: GraphCanvasProps) {
  const { model, axis } = useGraphStore()
  const { graphLoading, graphLoadingMessage } = useAppStore()
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const fgRef = useRef<ForceGraphMethods<any, any> | undefined>(undefined)
  const containerRef = useRef<HTMLDivElement>(null)

  // Build the L0 component graph (the opening frame): one node per role/subsystem
  // group + thresholded flows. ~11-26 nodes — a readable architecture diagram.
  const data = useMemo(() => {
    if (!model) return { nodes: [] as CompNode[], links: [] as CompLink[] }
    const view = componentView(model, axis)
    const colorOf = axis === "role" ? roleColor : subsystemColor
    const maxCount = Math.max(1, ...view.groups.map((g) => g.count))
    const nodes: CompNode[] = view.groups.map((g) => ({
      id: g.key,
      label: g.key.split("/").pop() ?? g.key,
      count: g.count,
      doorCount: g.doorCount,
      hubCount: g.hubCount,
      color: colorOf(g.key),
      // area ~ member count (sqrt so big groups don't dominate absurdly)
      val: 4 + 20 * Math.sqrt(g.count / maxCount),
    }))
    const present = new Set(nodes.map((n) => n.id))
    const links: CompLink[] = view.flows
      .filter((f) => present.has(f.source) && present.has(f.target))
      .map((f) => ({ source: f.source, target: f.target, weight: f.weight }))
    return { nodes, links }
  }, [model, axis])

  // First-load reveal + gentle settle: zoom to fit once the engine warms.
  useEffect(() => {
    if (!data.nodes.length || !fgRef.current) return
    const fg = fgRef.current
    // a touch of charge so groups separate; link distance scaled by weight
    fg.d3Force("charge")?.strength(-300)
    const t = setTimeout(() => fg.zoomToFit(800, 60), 200)
    return () => clearTimeout(t)
  }, [data])

  const maxWeight = useMemo(
    () => Math.max(1, ...data.links.map((l) => l.weight)),
    [data.links],
  )

  return (
    <div ref={containerRef} className={`relative flex-1 bg-slate-950 ${className ?? ""}`}>
      {data.nodes.length > 0 && (
        <ForceGraph2D
          ref={fgRef}
          graphData={data}
          backgroundColor="#020617"
          nodeRelSize={1}
          nodeVal={(n) => (n as CompNode).val}
          cooldownTicks={120}
          warmupTicks={20}
          d3VelocityDecay={0.3}
          linkColor={() => "rgba(148,163,184,0.25)"}
          linkWidth={(l) => 0.5 + 3 * ((l as CompLink).weight / maxWeight)}
          linkDirectionalParticles={0}
          linkCurvature={0.12}
          nodeCanvasObject={(node, ctx, globalScale) => {
            const n = node as CompNode & { x: number; y: number }
            const r = n.val
            // soft halo
            ctx.beginPath()
            ctx.arc(n.x, n.y, r, 0, 2 * Math.PI)
            ctx.fillStyle = n.color
            ctx.globalAlpha = 0.9
            ctx.fill()
            ctx.globalAlpha = 1
            // label — always shown at L0 (few nodes)
            const fontSize = Math.max(11, 13 / globalScale)
            ctx.font = `${fontSize}px ui-sans-serif, system-ui, sans-serif`
            ctx.textAlign = "center"
            ctx.textBaseline = "middle"
            ctx.fillStyle = "#e2e8f0"
            ctx.fillText(n.label, n.x, n.y + r + fontSize)
            // count badge inside
            ctx.fillStyle = "rgba(2,6,23,0.85)"
            ctx.font = `${Math.max(9, 10 / globalScale)}px ui-monospace, monospace`
            ctx.fillText(String(n.count), n.x, n.y)
          }}
          nodePointerAreaPaint={(node, color, ctx) => {
            const n = node as CompNode & { x: number; y: number }
            ctx.fillStyle = color
            ctx.beginPath()
            ctx.arc(n.x, n.y, n.val, 0, 2 * Math.PI)
            ctx.fill()
          }}
        />
      )}

      {/* Loading overlay */}
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
