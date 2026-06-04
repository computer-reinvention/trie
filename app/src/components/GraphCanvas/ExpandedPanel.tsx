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

interface ExpandedPanelProps {
  anchor: { x: number; y: number } | null
}

export function ExpandedPanel({ anchor }: ExpandedPanelProps) {
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
  const [hoveredMember, setHoveredMember] = useState<string | null>(null)

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

  // Esc closes the sub-graph.
  useEffect(() => {
    if (!focusedExpansion) return
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") collapseTransient()
    }
    window.addEventListener("keydown", onKey)
    return () => window.removeEventListener("keydown", onKey)
  }, [focusedExpansion, collapseTransient])

  const frame = stack[stack.length - 1]

  const maxDepth = useMemo(() => {
    if (!model) return 1
    let m = 1
    for (const n of model.nodes) if (n.depth > m) m = n.depth
    return m
  }, [model])

  // Minimum node sizes (note #2).
  const MIN_MEMBER_R = 5
  const MIN_OUTSIDE_R = 4

  // Build the sub-graph for the current frame: member nodes + member<->member
  // call edges + a ring of "outside" nodes. Unimportant members (called <=1
  // time) are HIDDEN unless their neighbour is the hovered member (note #5).
  const graph = useMemo(() => {
    if (!frame || !adjacency) return { nodes: [] as PanelNode[], links: [] as PanelLink[] }

    // a member is "minor" if it's depended on at most once (low inbound) and
    // isn't itself a landmark (door/hub/bedrock/exit).
    const isLandmark = (n: SystemModelNode) =>
      n.cls === "door" || n.cls === "hub" || n.cls === "bedrock" || n.cls === "exit"
    const isMinor = (n: SystemModelNode) => !isLandmark(n) && n.inbound_count <= 1

    // visible members: landmarks + non-minor always; minor only when the hovered
    // member is one of their neighbours (the "caller under focus" reveal).
    const hoveredNbrs = hoveredMember ? adjacency.neighbours.get(hoveredMember) : undefined
    const visibleMembers = frame.members.filter(
      (n) =>
        !isMinor(n) ||
        n.qname === hoveredMember ||
        (hoveredNbrs ? hoveredNbrs.has(n.qname) : false),
    )
    const memberIds = new Set(visibleMembers.map((m) => m.qname))

    const nodes: PanelNode[] = visibleMembers.map((n) => ({
      id: n.qname,
      node: n,
      color: depthColor(n.depth >= 0 ? n.depth / maxDepth : 0.5),
      val: Math.max(MIN_MEMBER_R, Math.min(11, nodeRadius(n.salience, n.cls))),
    }))
    const links: PanelLink[] = []
    const seen = new Set<string>()
    const outsideDeg = new Map<string, number>()

    for (const m of visibleMembers) {
      const nbrs = adjacency.neighbours.get(m.qname)
      if (!nbrs) continue
      for (const w of nbrs) {
        if (memberIds.has(w)) {
          const id = m.qname < w ? `${m.qname}|${w}` : `${w}|${m.qname}`
          if (!seen.has(id)) {
            seen.add(id)
            links.push({ source: m.qname, target: w })
          }
        } else {
          outsideDeg.set(w, (outsideDeg.get(w) ?? 0) + 1)
        }
      }
    }

    const outside = [...outsideDeg.entries()].sort((a, b) => b[1] - a[1]).slice(0, 24)
    for (const [qn] of outside) {
      const ext = nodesByQname.get(qn)
      nodes.push({ id: qn, node: ext, outside: true, color: "#475569", val: MIN_OUTSIDE_R })
      for (const m of visibleMembers) {
        if (adjacency.neighbours.get(m.qname)?.has(qn)) {
          links.push({ source: m.qname, target: qn, outside: true })
        }
      }
    }
    return { nodes, links }
  }, [frame, adjacency, maxDepth, nodesByQname, hoveredMember])

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

  // Position the panel AS the role node (note #1): anchored at the node's screen
  // position, opening down-right from it, clamped to the viewport. Falls back to
  // a fixed spot before the first anchor frame arrives.
  const PANEL_W = 560
  const PANEL_H = 440
  const pos = (() => {
    if (!anchor) return { left: 80, top: 80 }
    const margin = 12
    const vw = window.innerWidth
    const vh = window.innerHeight
    // center horizontally on the node, sit just below it
    let left = anchor.x - PANEL_W / 2
    let top = anchor.y + 16
    left = Math.max(margin, Math.min(left, vw - PANEL_W - margin))
    top = Math.max(margin, Math.min(top, vh - PANEL_H - margin))
    return { left, top }
  })()

  return (
    <div
      className="absolute z-20 bg-[#0b1220] border border-slate-600 rounded-xl shadow-2xl flex flex-col overflow-hidden"
      style={{ left: pos.left, top: pos.top, width: PANEL_W }}
    >
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

      {/* the bounded sub-graph (pan/zoom to navigate within the box) */}
      <div className="overflow-hidden relative bg-[#0b1220]" style={{ height: PANEL_H - 46 }}>
        {graph.nodes.length > 0 ? (
          <ForceGraph2D
            ref={fgRef}
            width={PANEL_W}
            height={PANEL_H - 46}
            graphData={graph}
            backgroundColor="#0b1220"
            nodeRelSize={1}
            nodeVal={(n) => (n as PanelNode).val}
            cooldownTicks={120}
            onNodeHover={(node) =>
              setHoveredMember(node ? (node as PanelNode).id : null)
            }
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
              } else {
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
              }
              // Labels when the area is sparse enough (note #3): show when few
              // nodes, zoomed in, hovered, or a landmark. Backdrop for legibility.
              const isLandmark =
                n.node &&
                (n.node.cls === "door" || n.node.cls === "hub" || n.node.cls === "bedrock")
              const sparse = graph.nodes.length <= 24
              const wantLabel =
                hoveredMember === n.id || sparse || scale >= 1.3 || (!n.outside && isLandmark)
              if (wantLabel) {
                const fs = Math.max(8, 10 / scale)
                const text = n.node?.name ?? n.id
                ctx.font = `${fs}px ui-sans-serif, system-ui, sans-serif`
                ctx.textAlign = "center"
                ctx.textBaseline = "top"
                const tw = ctx.measureText(text).width
                const ly = n.y + r + 2 / scale
                ctx.fillStyle = "rgba(11,18,32,0.85)"
                ctx.fillRect(n.x - tw / 2 - 2 / scale, ly, tw + 4 / scale, fs + 2 / scale)
                ctx.fillStyle = n.outside ? "#94a3b8" : "#e2e8f0"
                ctx.fillText(text, n.x, ly)
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
