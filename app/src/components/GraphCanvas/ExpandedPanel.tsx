import { useEffect, useMemo, useRef, useState } from "react"
import ForceGraph2D, { type ForceGraphMethods } from "react-force-graph-2d"
import { forceCollide } from "d3-force"
import { useGraphStore } from "@/store/graphStore"
import { depthColor, classMarker, nodeRadius, ACTIVITY } from "@/graph/style"
import type { AgentState, SystemModelNode } from "@/api/types"

// Colour for an agent state's pulse ring.
function activityColor(state: AgentState): string {
  if (state === "writing") return ACTIVITY.write
  if (state === "scanning") return ACTIVITY.scan
  return ACTIVITY.read
}

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
  folded?: number // count of members folded into this one (e.g. class methods)
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
  const selectedQname = useGraphStore((s) => s.selectedQname)
  const lastTouched = useGraphStore((s) => s.lastTouched)
  const notes = useGraphStore((s) => s.notes)

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const fgRef = useRef<ForceGraphMethods<any, any> | undefined>(undefined)
  const [stack, setStack] = useState<Frame[]>([])
  const [hoveredMember, setHoveredMember] = useState<string | null>(null)
  const [mouse, setMouse] = useState<{ x: number; y: number }>({ x: 0, y: 0 })
  // soft per-node pulse value (eased toward runtime.activity each frame)
  const pulseRef = useRef<Map<string, number>>(new Map())

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

  // Soft-pan to the member under attention (the agent's latest symbol, or a
  // manual selection) without rebuilding the panel — keeps the stage stable
  // while the agent moves between symbols in the same group.
  const panTarget = lastTouched?.qname ?? selectedQname
  useEffect(() => {
    if (!panTarget) return
    const fg = fgRef.current
    if (!fg) return
    // wait a frame so the node has coords if the layout just settled
    const t = setTimeout(() => {
      const node = (graph.nodes as Array<PanelNode & { x?: number; y?: number }>).find(
        (n) => n.id === panTarget,
      )
      if (node && node.x != null && node.y != null) fg.centerAt(node.x, node.y, 600)
    }, 120)
    return () => clearTimeout(t)
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [panTarget])

  const frame = stack[stack.length - 1]

  // info for the hovered symbol (drives the VS Code-style tooltip)
  const hoveredInfo = hoveredMember ? nodesByQname.get(hoveredMember) : undefined
  // the tool-output snippet for the hovered node, if the agent touched it
  const hoveredNote = hoveredMember ? notes.get(hoveredMember) : undefined

  const maxDepth = useMemo(() => {
    if (!model) return 1
    let m = 1
    for (const n of model.nodes) if (n.depth > m) m = n.depth
    return m
  }, [model])

  // Minimum node sizes (note #2).
  const MIN_MEMBER_R = 5
  const MIN_OUTSIDE_R = 4

  // Build the sub-graph for the current frame. STATIC: this does NOT depend on
  // hover, so hovering never rebuilds the data or re-runs the simulation.
  // Minor symbols (inbound<=1, non-landmark) and members folded into a visible
  // owner are excluded; drilling reveals folded members.
  const graph = useMemo(() => {
    if (!frame || !adjacency) return { nodes: [] as PanelNode[], links: [] as PanelLink[] }

    const isLandmark = (n: SystemModelNode) =>
      n.cls === "door" || n.cls === "hub" || n.cls === "bedrock" || n.cls === "exit"
    const isMinor = (n: SystemModelNode) => !isLandmark(n) && n.inbound_count <= 1

    const frameIds = new Set(frame.members.map((m) => m.qname))
    const ownerInFrame = (n: SystemModelNode): boolean => {
      const owner = ownerOf(n.qname)
      return !!owner && frameIds.has(owner)
    }

    const visibleMembers = frame.members.filter((n) => {
      if (ownerInFrame(n)) return false // folded into its owner
      if (isMinor(n)) return false // unimportant
      return true
    })
    const memberIds = new Set(visibleMembers.map((m) => m.qname))

    // count members folded into each visible owner (for the "contains more" cue)
    const foldedCount = new Map<string, number>()
    for (const n of frame.members) {
      if (memberIds.has(n.qname)) continue
      const owner = ownerOf(n.qname)
      if (owner && memberIds.has(owner)) {
        foldedCount.set(owner, (foldedCount.get(owner) ?? 0) + 1)
      }
    }

    const nodes: PanelNode[] = visibleMembers.map((n) => ({
      id: n.qname,
      node: n,
      color: depthColor(n.depth >= 0 ? n.depth / maxDepth : 0.5),
      val: Math.max(MIN_MEMBER_R, Math.min(11, nodeRadius(n.salience, n.cls))),
      folded: foldedCount.get(n.qname) ?? 0,
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
  }, [frame, adjacency, maxDepth, nodesByQname])

  // Configure forces once when the graph changes; the engine runs a short fixed
  // warmup then stops (cooldownTicks). onEngineStop pins every node so the
  // layout is fully STATIC afterward — no drift, no per-frame physics.
  useEffect(() => {
    if (!fgRef.current) return
    const fg = fgRef.current
    fg.d3Force("charge")?.strength(-120)
    fg.d3Force(
      "collide",
      forceCollide<PanelNode>()
        .radius((n) => n.val + 8)
        .strength(1),
    )
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const link = fg.d3Force("link") as any
    link?.distance?.((l: PanelLink) => (l.outside ? 90 : 40))
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
      <div
        className="overflow-hidden relative bg-[#0b1220]"
        style={{ height: PANEL_H - 46 }}
        onMouseMove={(e) => {
          const r = e.currentTarget.getBoundingClientRect()
          setMouse({ x: e.clientX - r.left, y: e.clientY - r.top })
        }}
      >
        {/* live "what the agent is doing" caption */}
        {lastTouched && (
          <div className="absolute top-2 left-2 z-30 flex items-center gap-1.5 bg-[#0b1220]/80 rounded px-2 py-1 pointer-events-none">
            <span
              className="w-2 h-2 rounded-full"
              style={{ background: activityColor(lastTouched.state) }}
            />
            <span className="text-[10px] font-mono text-slate-300">
              {lastTouched.state === "writing"
                ? "editing"
                : lastTouched.state === "scanning"
                  ? "searching"
                  : "reading"}{" "}
              {(nodesByQname.get(lastTouched.qname)?.name) ?? lastTouched.qname.split(":").pop()}
            </span>
          </div>
        )}
        {/* VS Code-style hover info: name + one-liner for the hovered symbol */}
        {hoveredInfo && (
          <div
            className="absolute z-30 pointer-events-none max-w-[280px] bg-[#1e1e1e] border border-slate-600 rounded shadow-xl px-2.5 py-1.5"
            style={{
              left: Math.min(mouse.x + 12, PANEL_W - 290),
              top: Math.min(mouse.y + 12, PANEL_H - 160),
            }}
          >
            <p className="text-slate-100 font-mono text-xs font-medium truncate">{hoveredInfo.name}</p>
            <p className="text-slate-500 font-mono text-[10px] truncate">
              {hoveredInfo.kind} · {hoveredInfo.file_path.split("/").pop()}
            </p>
            {hoveredInfo.one_liner ? (
              <p className="text-slate-300 text-[11px] mt-1 leading-snug">{hoveredInfo.one_liner}</p>
            ) : (
              <p className="text-slate-600 text-[11px] mt-1 italic">no description</p>
            )}
            {hoveredNote && hoveredNote.text && (
              <div
                className="mt-1.5 pt-1.5 border-t border-slate-700"
                style={{ borderColor: activityColor(hoveredNote.state) + "66" }}
              >
                <div className="flex items-center gap-1 mb-0.5">
                  <span
                    className="w-1.5 h-1.5 rounded-full"
                    style={{ background: activityColor(hoveredNote.state) }}
                  />
                  <span
                    className="text-[9px] uppercase tracking-wide"
                    style={{ color: activityColor(hoveredNote.state) }}
                  >
                    {hoveredNote.state === "writing"
                      ? "edited"
                      : hoveredNote.state === "scanning"
                        ? "found"
                        : "read"}
                  </span>
                </div>
                <p className="text-slate-300 text-[11px] leading-snug">{hoveredNote.text}</p>
              </div>
            )}
          </div>
        )}
        {graph.nodes.length > 0 ? (
          <ForceGraph2D
            ref={fgRef}
            width={PANEL_W}
            height={PANEL_H - 46}
            graphData={graph}
            backgroundColor="#0b1220"
            nodeRelSize={1}
            nodeVal={(n) => (n as PanelNode).val}
            warmupTicks={60}
            cooldownTicks={0}
            enableNodeDrag={false}
            autoPauseRedraw={false}
            onRenderFramePre={() => {
              // Ease each member's pulse toward its live agent activity so reads/
              // scans/writes breathe instead of snapping. Cheap; runs per frame.
              const rt = useGraphStore.getState().runtime
              const pulses = pulseRef.current
              for (const n of graph.nodes as PanelNode[]) {
                if (n.outside) continue
                const target = rt.get(n.id)?.activity ?? 0
                const cur = pulses.get(n.id) ?? 0
                pulses.set(n.id, cur + (target - cur) * 0.18)
              }
            }}
            linkDirectionalParticles={(l) => {
              const lk = l as PanelLink
              if (lk.outside) return 0
              const flows = useGraphStore.getState().activeFlows
              if (!flows.size) return 0
              const s = typeof lk.source === "object" ? (lk.source as { id: string }).id : lk.source
              const t = typeof lk.target === "object" ? (lk.target as { id: string }).id : lk.target
              return flows.has(`${s}|${t}`) || flows.has(`${t}|${s}`) ? 4 : 0
            }}
            linkDirectionalParticleWidth={2.5}
            linkDirectionalParticleSpeed={0.012}
            linkDirectionalParticleColor={() => ACTIVITY.read}
            onEngineStop={() => {
              const fg = fgRef.current
              if (!fg) return
              // pin every node so the layout is fully static afterward
              for (const n of graph.nodes as Array<PanelNode & { x?: number; y?: number }>) {
                if (n.x != null && n.y != null) {
                  n.fx = n.x
                  n.fy = n.y
                }
              }
              fg.zoomToFit(400, 30)
            }}
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
                // --- agent-activity overlays (under the node) ---
                const st = useGraphStore.getState()
                const rt = st.runtime.get(n.id)
                const pulse = pulseRef.current.get(n.id) ?? 0
                const touched = st.notes.get(n.id) // touched this turn (persists)
                const isSel = st.selectedQname === n.id
                // PERSISTENT "touched this turn" highlight: a solid colour ring +
                // a soft tint that stays until the next turn, so it stays obvious
                // which symbols the agent used to answer the question.
                if (touched) {
                  const tcol = activityColor(touched.state)
                  ctx.beginPath()
                  ctx.arc(n.x, n.y, r + 5 / scale, 0, 2 * Math.PI)
                  ctx.fillStyle = tcol
                  ctx.globalAlpha = 0.1
                  ctx.fill()
                  ctx.globalAlpha = 1
                  ctx.beginPath()
                  ctx.arc(n.x, n.y, r + 3 / scale, 0, 2 * Math.PI)
                  ctx.strokeStyle = tcol
                  ctx.globalAlpha = 0.85
                  ctx.lineWidth = 1.75 / scale
                  ctx.stroke()
                  ctx.globalAlpha = 1
                }
                // live pulse ring coloured by what the agent is doing
                if (pulse > 0.05) {
                  const col = activityColor(rt?.agentState ?? "reading")
                  // breathing halo
                  ctx.beginPath()
                  ctx.arc(n.x, n.y, r + (3 + 10 * pulse) / scale, 0, 2 * Math.PI)
                  ctx.fillStyle = col
                  ctx.globalAlpha = 0.12 * pulse
                  ctx.fill()
                  ctx.globalAlpha = 1
                  // crisp ring
                  ctx.beginPath()
                  ctx.arc(n.x, n.y, r + (3 + 6 * (1 - pulse)) / scale, 0, 2 * Math.PI)
                  ctx.strokeStyle = col
                  ctx.globalAlpha = Math.min(1, 0.5 + pulse)
                  ctx.lineWidth = 2 / scale
                  ctx.stroke()
                  ctx.globalAlpha = 1
                }
                // selected ring (where the agent is right now)
                if (isSel) {
                  ctx.beginPath()
                  ctx.arc(n.x, n.y, r + 4 / scale, 0, 2 * Math.PI)
                  ctx.strokeStyle = "#e2e8f0"
                  ctx.lineWidth = 1.5 / scale
                  ctx.stroke()
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
                // "contains folded members" cue: a faint concentric ring +
                // small count. Hover or click to reveal/drill into them.
                if (n.folded && n.folded > 0) {
                  ctx.beginPath()
                  ctx.arc(n.x, n.y, r + 3.5 / scale, 0, 2 * Math.PI)
                  ctx.strokeStyle = n.color
                  ctx.globalAlpha = 0.45
                  ctx.lineWidth = 1 / scale
                  ctx.stroke()
                  ctx.globalAlpha = 1
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

              // Agent note popup: a small readable snippet of the tool output
              // that focused this node, shown above it for a few seconds after
              // the agent touched it (recency-based so it survives the pulse
              // decay), fading out at the end.
              const note = n.outside ? undefined : useGraphStore.getState().notes.get(n.id)
              const noteAge = note ? Date.now() - note.ts : Infinity
              const NOTE_TTL = 6000
              if (note && note.text && noteAge < NOTE_TTL) {
                const noteFade = noteAge < NOTE_TTL - 1200 ? 1 : Math.max(0, (NOTE_TTL - noteAge) / 1200)
                const fs = Math.max(7, 8.5 / scale)
                ctx.font = `${fs}px ui-sans-serif, system-ui, sans-serif`
                const maxW = 150 / scale
                // greedy word-wrap, max 3 lines, ellipsize overflow
                const words = note.text.split(/\s+/)
                const lines: string[] = []
                let cur = ""
                for (const w of words) {
                  const test = cur ? `${cur} ${w}` : w
                  if (ctx.measureText(test).width > maxW && cur) {
                    lines.push(cur)
                    cur = w
                    if (lines.length === 3) break
                  } else {
                    cur = test
                  }
                }
                if (lines.length < 3 && cur) lines.push(cur)
                if (lines.length === 3 && cur && lines[2] !== cur) lines[2] = lines[2] + "…"
                const pad = 4 / scale
                const lineH = fs + 2 / scale
                const boxW = Math.max(...lines.map((l) => ctx.measureText(l).width)) + pad * 2
                const boxH = lines.length * lineH + pad * 2
                const bx = n.x - boxW / 2
                const by = n.y - r - 7 / scale - boxH
                const col = activityColor(note.state)
                ctx.globalAlpha = noteFade
                ctx.beginPath()
                if (ctx.roundRect) ctx.roundRect(bx, by, boxW, boxH, 3 / scale)
                else ctx.rect(bx, by, boxW, boxH)
                ctx.fillStyle = "rgba(2,6,23,0.94)"
                ctx.fill()
                ctx.strokeStyle = col
                ctx.lineWidth = 1 / scale
                ctx.stroke()
                // little pointer dot toward the node
                ctx.beginPath()
                ctx.arc(n.x, by + boxH + 2 / scale, 1.5 / scale, 0, 2 * Math.PI)
                ctx.fillStyle = col
                ctx.fill()
                // text
                ctx.fillStyle = "#e2e8f0"
                ctx.textAlign = "left"
                ctx.textBaseline = "top"
                lines.forEach((l, i) => ctx.fillText(l, bx + pad, by + pad + i * lineH))
                ctx.globalAlpha = 1
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

// Owner qname for a symbol that belongs to another (a method belongs to its
// class, a nested member to its enclosing symbol), else null. `mod:A.b.c` ->
// `mod:A.b`. Top-level `mod:A` has no owner.
function ownerOf(qname: string): string | null {
  if (!qname.includes(":")) return null
  const [mod, local] = qname.split(":")
  if (!local.includes(".")) return null
  return `${mod}:${local.slice(0, local.lastIndexOf("."))}`
}

// owning class qname for a method (used by the drill logic), else null
function ownerClassOf(qname: string): string | null {
  return ownerOf(qname)
}
