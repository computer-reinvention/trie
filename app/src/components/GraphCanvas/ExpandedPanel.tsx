import { useEffect, useMemo, useRef, useState } from "react"
import ForceGraph2D, { type ForceGraphMethods } from "react-force-graph-2d"
import { forceCollide } from "d3-force"
import { useGraphStore } from "@/store/graphStore"
import { depthColor, classMarker, nodeRadius } from "@/graph/style"
import type { SystemModelNode } from "@/api/types"

// A bounded, scrollable sub-graph panel that opens when a role/subsystem is
// expanded. It shows the focused group's members as a REAL network (their call
// interdependencies as edges) plus their connections OUT to the rest of the
// system (peripheral "outside" nodes). Drilling a member with internal
// structure replaces the panel contents in place (a drill stack with a
// breadcrumb back path).

interface PanelNode {
  id: string
  node?: SystemModelNode
  outside?: boolean // a peripheral system node this group connects to
  color: string
  val: number
  fx?: number
  fy?: number
  x?: number
  y?: number
}
interface PanelLink {
  source: string
  target: string
  outside?: boolean
}

// A drill frame: what the panel is currently showing.
interface Frame {
  key: string // group key or symbol qname
  label: string
  // predicate to pick member symbols for this frame
  members: SystemModelNode[]
}

export function ExpandedPanel() {
  const model = useGraphStore((s) => s.model)
  const axis = useGraphStore((s) => s.axis)
  const adjacency = useGraphStore((s) => s.adjacency)
  const focusedExpansion = useGraphStore((s) => s.focusedExpansion)
  const collapseTransient = useGraphStore((s) => s.collapseTransient)
  const selectNode = useGraphStore((s) => s.selectNode)
  const nodesByQname = useGraphStore((s) => s.nodesByQname)

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const fgRef = useRef<ForceGraphMethods<any, any> | undefined>(undefined)
  const [stack, setStack] = useState<Frame[]>([])

  // (re)initialize the drill stack when the focused expansion changes.
  useEffect(() => {
    if (!model || !focusedExpansion) {
      setStack([])
      return
    }
    const groupKey = (n: SystemModelNode) =>
      axis === "role" ? n.role || "untagged" : n.subsystem
    const members = model.nodes.filter((n) => !n.is_test && groupKey(n) === focusedExpansion)
    setStack([{ key: focusedExpansion, label: focusedExpansion, members }])
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [focusedExpansion, model, axis])

  const frame = stack[stack.length - 1]

  const maxDepth = useMemo(() => {
    if (!model) return 1
    let m = 1
    for (const n of model.nodes) if (n.depth > m) m = n.depth
    return m
  }, [model])

  // Build the sub-graph for the current frame: member nodes + member<->member
  // call edges + a ring of "outside" nodes (other groups/symbols the members
  // call or are called by), so interdependence and external connections show.
  const graph = useMemo(() => {
    if (!frame || !adjacency) return { nodes: [] as PanelNode[], links: [] as PanelLink[] }
    const memberIds = new Set(frame.members.map((m) => m.qname))
    const nodes: PanelNode[] = frame.members.map((n) => ({
      id: n.qname,
      node: n,
      color: depthColor(n.depth >= 0 ? n.depth / maxDepth : 0.5),
      val: Math.max(3, Math.min(10, nodeRadius(n.salience, n.cls))),
    }))
    const links: PanelLink[] = []
    const seen = new Set<string>()
    const outsideDeg = new Map<string, number>()

    for (const m of frame.members) {
      const nbrs = adjacency.neighbours.get(m.qname)
      if (!nbrs) continue
      for (const w of nbrs) {
        if (memberIds.has(w)) {
          // internal interdependence edge
          const id = m.qname < w ? `${m.qname}|${w}` : `${w}|${m.qname}`
          if (!seen.has(id)) {
            seen.add(id)
            links.push({ source: m.qname, target: w })
          }
        } else {
          // external connection — accumulate so we show the most-connected ones
          outsideDeg.set(w, (outsideDeg.get(w) ?? 0) + 1)
        }
      }
    }

    // add the top external connections as peripheral nodes
    const outside = [...outsideDeg.entries()].sort((a, b) => b[1] - a[1]).slice(0, 24)
    for (const [qn] of outside) {
      const ext = nodesByQname.get(qn)
      nodes.push({
        id: qn,
        node: ext,
        outside: true,
        color: "#475569",
        val: 4,
      })
      // link each member that touches this external node
      for (const m of frame.members) {
        if (adjacency.neighbours.get(m.qname)?.has(qn)) {
          links.push({ source: m.qname, target: qn, outside: true })
        }
      }
    }
    return { nodes, links }
  }, [frame, adjacency, maxDepth, nodesByQname])

  useEffect(() => {
    if (!fgRef.current) return
    const fg = fgRef.current
    fg.d3Force("charge")?.strength(-90)
    fg.d3Force(
      "collide",
      forceCollide<PanelNode>()
        .radius((n) => n.val + 8)
        .strength(1),
    )
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const link = fg.d3Force("link") as any
    link?.distance?.((l: PanelLink) => (l.outside ? 90 : 40))
    const t = setTimeout(() => fg.zoomToFit(500, 30), 250)
    return () => clearTimeout(t)
  }, [graph])

  if (!focusedExpansion || !frame) return null

  // drill into a member that has its own internal structure (a class with
  // methods, or a subsystem) — replaces panel contents in place.
  const drillInto = (n: SystemModelNode) => {
    // members whose owning class is this node, or whose subsystem is this node
    const children = (model?.nodes ?? []).filter(
      (m) =>
        !m.is_test &&
        m.qname !== n.qname &&
        (ownerClassOf(m.qname) === n.qname || m.subsystem === n.qname),
    )
    if (children.length === 0) {
      // leaf — select it in the system instead of drilling
      selectNode(n.qname)
      window.dispatchEvent(new CustomEvent("trie:node-selected", { detail: { qname: n.qname } }))
      return
    }
    setStack((s) => [...s, { key: n.qname, label: n.name, members: children }])
  }

  const popTo = (idx: number) => setStack((s) => s.slice(0, idx + 1))

  return (
    <div className="absolute top-4 left-1/2 -translate-x-1/2 z-20 w-[640px] max-w-[80%] bg-[#0b1220] border border-slate-600 rounded-xl shadow-2xl flex flex-col overflow-hidden">
      {/* header: depth breadcrumb (entrypoint > cli > ...) + close */}
      <div
        className="flex items-center gap-1.5 px-3 py-2 border-b border-slate-800"
        style={{ borderTop: `3px solid ${depthColor(0.3)}` }}
      >
        <span className="text-slate-500 text-xs uppercase tracking-wide mr-1">depth</span>
        {stack.map((f, i) => (
          <span key={f.key} className="flex items-center gap-1.5 min-w-0">
            {i > 0 && <span className="text-slate-600">›</span>}
            <button
              className={`font-mono text-sm truncate ${
                i === stack.length - 1
                  ? "text-slate-100 font-semibold"
                  : "text-slate-400 hover:text-slate-200"
              }`}
              onClick={() => popTo(i)}
              title="Go to this level"
            >
              {f.label.split("/").pop()}
            </button>
          </span>
        ))}
        <span className="text-slate-600 text-xs ml-2">· {frame.members.length} symbols</span>
        <button
          className="ml-auto text-slate-500 hover:text-slate-200 text-sm"
          onClick={() => collapseTransient()}
          title="Close (Esc)"
        >
          ×
        </button>
      </div>

      {/* the bounded, scrollable sub-graph */}
      <div className="h-[420px] max-h-[60vh] overflow-hidden relative bg-[#0b1220]">
        {graph.nodes.length > 0 ? (
          <ForceGraph2D
            ref={fgRef}
            width={640}
            height={420}
            graphData={graph}
            backgroundColor="#0b1220"
            nodeRelSize={1}
            nodeVal={(n) => (n as PanelNode).val}
            cooldownTicks={120}
            linkColor={(l) => ((l as PanelLink).outside ? "rgba(100,116,139,0.25)" : "rgba(148,163,184,0.45)")}
            linkWidth={(l) => ((l as PanelLink).outside ? 0.5 : 1)}
            linkDirectionalArrowLength={3}
            linkDirectionalArrowRelPos={0.9}
            onNodeClick={(node) => {
              const n = node as PanelNode
              if (n.node && !n.outside) drillInto(n.node)
              else if (n.node) {
                selectNode(n.id)
                window.dispatchEvent(new CustomEvent("trie:node-selected", { detail: { qname: n.id } }))
              }
            }}
            nodeCanvasObject={(node, ctx, scale) => {
              const n = node as PanelNode & { x: number; y: number }
              const r = n.val
              if (n.outside) {
                ctx.beginPath()
                ctx.arc(n.x, n.y, r, 0, 2 * Math.PI)
                ctx.fillStyle = n.color
                ctx.globalAlpha = 0.6
                ctx.fill()
                ctx.globalAlpha = 1
                return
              }
              const marker = n.node ? classMarker(n.node.cls, n.color) : { shape: "circle" as const }
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
                ctx.arc(n.x, n.y, r + 2 / scale, 0, 2 * Math.PI)
                ctx.strokeStyle = marker.ring
                ctx.lineWidth = 1.5 / scale
                ctx.stroke()
              }
              // label visible when zoomed in or few nodes
              if (scale >= 1.2 || graph.nodes.length <= 30) {
                const fs = Math.max(8, 10 / scale)
                ctx.font = `${fs}px ui-sans-serif, system-ui, sans-serif`
                ctx.textAlign = "center"
                ctx.textBaseline = "top"
                ctx.fillStyle = "#cbd5e1"
                ctx.fillText(n.node?.name ?? n.id, n.x, n.y + r + 2 / scale)
              }
            }}
            nodePointerAreaPaint={(node, color, ctx) => {
              const n = node as PanelNode & { x: number; y: number }
              ctx.fillStyle = color
              ctx.beginPath()
              ctx.arc(n.x, n.y, n.val + 3, 0, 2 * Math.PI)
              ctx.fill()
            }}
          />
        ) : (
          <div className="flex items-center justify-center h-full text-slate-600 text-sm">
            No internal structure.
          </div>
        )}
        {/* legend hint */}
        <div className="absolute bottom-2 left-2 text-[10px] text-slate-600 flex items-center gap-3">
          <span className="flex items-center gap-1">
            <span className="w-2 h-2 rounded-full bg-slate-200/70" /> member
          </span>
          <span className="flex items-center gap-1">
            <span className="w-2 h-2 rounded-full bg-slate-600" /> outside connection
          </span>
          <span>click a member to drill in</span>
        </div>
      </div>
    </div>
  )
}

// owning class qname for a method, else null
function ownerClassOf(qname: string): string | null {
  if (!qname.includes(":")) return null
  const [mod, local] = qname.split(":")
  if (!local.includes(".")) return null
  return `${mod}:${local.slice(0, local.lastIndexOf("."))}`
}
