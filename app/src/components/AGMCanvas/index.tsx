// AGMCanvas — cognitive-state projection (NOT a graph view).
//
// The canvas centre is a FIXED crosshair: the "current attention origin". The
// world deforms around it; the camera never pans or follows. Each touched symbol
// is placed in polar coordinates:
//   radius = f(live mass)   — near centre = hot now, drifts outward as it cools
//   angle  = f(historical mass + role) — stable geography (learnable bearings)
//
// Nothing disappears mid-investigation: a cooled symbol becomes peripheral, not
// hidden. New discoveries enter from the perimeter and move inward. Repository
// edges are faint springs (tension/structure); attention edges are bright,
// temporary reasoning paths. Roles are influence (anchor labels), not boxes.
//
// All placement math lives in agm/layout.ts and is unit-tested; this file only
// eases drawn positions toward those targets and paints.

import { useEffect, useMemo, useRef, useState } from "react"
import { useAGMStore } from "@/store/agmStore"
import { useAgentStore } from "@/store/agentStore"
import { useAppStore } from "@/store/appStore"
import type { NodeMass } from "@/agm/attentionModel"

// Is the active agent session mid-turn? Drives whether the sim keeps ticking.
function isAgentRunning(): boolean {
  const a = useAgentStore.getState()
  const id = a.activeId
  return !!(id && a.sessions[id]?.running)
}
import {
  placeSymbol,
  applyClusterCohesion,
  applyVisibleBudget,
  spreadTargets,
  type PolarPlacement,
  R_MAX,
} from "@/agm/layout"
import { displayMass } from "@/agm/weights"
import { tierFor, ATTENTION_EDGE_COLOR } from "@/agm/style"

// Radial spoke colour (centre → node). Slightly warmer/brighter than the old
// repo-edge slate so the spokes read at low opacity.
const RADIAL_COLOR = "#475569"
import { openContextMenu } from "@/store/contextMenuStore"
import { buildSymbolMenu } from "@/agm/symbolMenu"
import { graphClient } from "@/api/graphClient"

interface AGMCanvasProps {
  className?: string
}

// A target produced by the MODEL (recomputed on tool calls / decay), holding
// where a symbol wants to be. The render loop eases drawn nodes toward these.
interface Target {
  qname: string
  role: string
  x: number
  y: number
  mass: number // display mass
  angle: number // bearing (for perimeter entry)
  kind: NodeMass["kind"] // dominant intent → render style (dot / pill / trace)
}

// A drawn node. Position is animated along a JOURNEY from (sx,sy) to (tx,ty)
// using an ease-in-out (smoothstep) curve on progress `p` — slow start, faster
// middle, slow end (Bézier-like), so motion is never jarring. When the target
// changes, the current position becomes the new start and `p` resets. `appear`
// 0→1 drives the entry fade+scale; `leaving` triggers the exit. Nothing instant.
interface Drawn {
  qname: string
  role: string
  x: number // current rendered position
  y: number
  sx: number // journey start
  sy: number
  tx: number // journey target
  ty: number
  p: number // progress 0→1 along the journey
  mass: number
  kind: NodeMass["kind"] // render style
  appear: number // 0 (just spawned) → 1 (fully present)
  leaving: boolean // true once it left the target set; fades out then is dropped
}

// Max symbols rendered at once (PRD: 20–100 visible). The rest fold into a
// per-role "+N" peripheral count so the centre never becomes an unreadable pile.
const VISIBLE_BUDGET = 60

// How fast the normalization denominator (maxDisplay) chases its instantaneous
// value. Easing it prevents "whiplash": one new hottest symbol would otherwise
// instantly rescale every node's radius. ~0.12/frame ≈ settles in ~0.4s.
const MAX_DISPLAY_EASE = 0.12

// Minimum gap (world px) enforced between pill footprints by the de-overlap pass.
const MIN_GAP = 8

// Two clocks. The MODEL clock is event-driven (tool calls ingest attention) plus
// a slow decay tick; it recomputes TARGETS at most this often. The RENDER clock
// is the rAF frame loop, which only eases drawn nodes toward those targets per
// the physics laws (speed floor/ceiling, fade in/out). Targets stay fixed
// between recomputes so the frame loop reliably settles — no per-frame thrash.
const MODEL_TICK_MS = 250

// Entry/exit fade rate (per frame). appear eases 0→1 on spawn; a leaving node
// fades 1→0 then is removed. Keeps every entrance/exit pleasing, never instant.
const APPEAR_EASE = 0.08
const FADE_EASE = 0.06

// Journey progress per frame. Position interpolates start→target via smoothstep
// (slow-start, fast-middle, slow-end). 0.04/frame ≈ ~0.4s end-to-end at 60fps.
const JOURNEY_RATE = 0.04

// Fraction of nodes (by attention rank) that render as NAME PILLS. The rest are
// small dots (hover to reveal the name). Keeps the field calm — only the symbols
// that genuinely matter get a label.
const PILL_PERCENTILE = 0.2 // top 20%

// Footprint (world px) a dot reserves during target-spread — small so the
// exploration net packs tightly rather than being spaced like labels.
const DOT_FOOTPRINT = 16

// Rich hover tooltip (codelens-style): what the symbol is + WHY it's on the map.
interface TooltipData {
  x: number
  y: number
  qname: string
  name: string
  role: string
  oneLiner: string
  reason: string // "grepped (exploration)" / "read" / "traced" / …
  reasonColor: string
  liveMass: number
  historicalMass: number
  inbound?: number
  outbound?: number
}

// Human reason + colour for why a node is lit, from its dominant intent.
function intentReason(kind: NodeMass["kind"]): { label: string; color: string } {
  switch (kind) {
    case "grep":
      return { label: "found while exploring (grep)", color: "#2dd4bf" }
    case "read":
      return { label: "read by the agent", color: "#3b82f6" }
    case "trace":
      return { label: "traced — part of the reasoning path", color: "#a78bfa" }
    case "write":
      return { label: "edited by the agent", color: "#f59e0b" }
    case "historical":
      return { label: "historically attended (returns here)", color: "#94a3b8" }
    default:
      return { label: "attended", color: "#94a3b8" }
  }
}

export function AGMCanvas({ className }: AGMCanvasProps) {
  const canvasRef = useRef<HTMLCanvasElement | null>(null)
  // user zoom only (no pan / no follow — the centre is fixed at (0,0)).
  const zoomRef = useRef(1)
  const drawnRef = useRef<Map<string, Drawn>>(new Map())
  const targetsRef = useRef<Map<string, Target>>(new Map())
  const hoverRef = useRef<string | null>(null) // qname under the cursor (for dot tooltip)
  const edgeHoverRef = useRef<string | null>(null) // key of the hovered edge (spoke/attention)
  const pillThresholdRef = useRef(Infinity) // mass cutoff for name pills (top %)
  const [tooltip, setTooltipState] = useState<TooltipData | null>(null)
  const tooltipRef = useRef<TooltipData | null>(null)
  const setTooltip = (t: TooltipData | null) => {
    tooltipRef.current = t
    setTooltipState(t)
  }
  const maxDisplayRef = useRef(0) // current normalization denominator (target)
  const smoothedMaxRef = useRef(0) // eased denominator used for rendering
  const lastModelTickRef = useRef(0)
  const rafRef = useRef<number | null>(null)

  const systemModel = useAGMStore((s) => s.systemModel)
  const hasAttention = useAGMStore((s) => s.massByQname.size > 0)

  useEffect(() => {
    if (!systemModel) return
    kick()
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [systemModel])

  const kick = () => {
    if (rafRef.current == null) rafRef.current = requestAnimationFrame(loop)
  }

  // --- frozen-layout snapshot (per opencode session) -------------------------
  // Save the current drawn layout so a restarted editor / re-opened chat shows
  // the attention map as it was, frozen (no decay replay).
  const saveSnapshot = (sessionId: string) => {
    const projectDir = useAppStore.getState().projectDir
    if (!projectDir || !sessionId) return
    const drawn = drawnRef.current
    if (drawn.size === 0) return
    const pinned = useAGMStore.getState().model.pinnedSet()
    const nodes = [...drawn.values()].map((n) => ({
      qname: n.qname,
      role: n.role,
      x: n.x,
      y: n.y,
      mass: n.mass,
      kind: n.kind,
      pinned: pinned.has(n.qname),
    }))
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    ;(window as any).trie?.agmSnapshotSet?.(projectDir, sessionId, { nodes })
  }

  // Restore a session's frozen layout into drawnRef (appear=1, p=1 → static).
  const restoreSnapshot = async (sessionId: string) => {
    const projectDir = useAppStore.getState().projectDir
    if (!projectDir || !sessionId) return
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const snap = await (window as any).trie?.agmSnapshotGet?.(projectDir, sessionId)
    const nodes = snap?.nodes as
      | Array<{ qname: string; role: string; x: number; y: number; mass: number; kind: NodeMass["kind"]; pinned?: boolean }>
      | undefined
    if (!nodes || nodes.length === 0) return
    const drawn = drawnRef.current
    const targets = targetsRef.current
    drawn.clear()
    targets.clear()
    const model = useAGMStore.getState().model
    let maxMass = 0
    for (const n of nodes) {
      drawn.set(n.qname, {
        qname: n.qname,
        role: n.role,
        x: n.x,
        y: n.y,
        sx: n.x,
        sy: n.y,
        tx: n.x,
        ty: n.y,
        p: 1,
        mass: n.mass,
        kind: n.kind,
        appear: 1,
        leaving: false,
      })
      // Seed a matching frozen target so the loop keeps these nodes (otherwise
      // the empty model would fade them out). Angle is derived from position.
      targets.set(n.qname, {
        qname: n.qname,
        role: n.role,
        x: n.x,
        y: n.y,
        mass: n.mass,
        angle: Math.atan2(n.y, n.x),
        kind: n.kind,
      })
      if (n.pinned) model.pin(n.qname)
      if (n.mass > maxMass) maxMass = n.mass
    }
    // restore the normalization denominator so radii/pills render correctly
    smoothedMaxRef.current = maxMass
    maxDisplayRef.current = maxMass
    kick()
  }

  // A tool call (ingest) bumps lastRecompute → recompute targets immediately so
  // the new attention is reflected, then let the frame loop animate to it.
  useEffect(() => {
    const unsub = useAGMStore.subscribe((s, prev) => {
      if (s.lastRecompute !== prev.lastRecompute) {
        recomputeTargets()
        kick()
      }
    })
    return unsub
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  // Persist the frozen layout when a turn ends, and restore a session's snapshot
  // when the active chat changes (so a restarted editor / switched chat shows its
  // attention map). Tracks the active session's running flag across updates.
  useEffect(() => {
    let prevActive = useAgentStore.getState().activeId
    let prevRunning = prevActive
      ? (useAgentStore.getState().sessions[prevActive]?.running ?? false)
      : false
    // restore the initial active session on mount
    if (prevActive) void restoreSnapshot(prevActive)
    const unsub = useAgentStore.subscribe((s) => {
      const active = s.activeId
      const running = active ? (s.sessions[active]?.running ?? false) : false
      // turn just ended on the active session → save its snapshot
      if (active && prevRunning && !running) saveSnapshot(active)
      // active session changed → save the old one, restore the new one
      if (active !== prevActive) {
        if (prevActive) saveSnapshot(prevActive)
        if (active) void restoreSnapshot(active)
      }
      prevActive = active
      prevRunning = running
    })
    return unsub
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  // ---- MODEL clock: recompute TARGETS (where every symbol wants to be). Runs
  // on each tool call and on a slow decay tick — NOT every frame. -------------
  const recomputeTargets = () => {
    const store = useAGMStore.getState()
    const now = Date.now() / 1000
    store.recompute(now)

    const mass = store.massByQname
    const prop = store.propagated
    const roleByQ = store.roleByQname
    const histByQ = store.historicalByQname
    const roles = store.roles

    const active = new Set<string>(mass.keys())
    for (const [q, v] of prop) if (v > 0) active.add(q)

    let instantMax = 0
    for (const q of active) {
      const m = mass.get(q)
      const propAdd = prop.get(q) ?? 0
      const d = m ? m.display : propAdd > 0 ? displayMass(propAdd) : 0
      if (d > instantMax) instantMax = d
    }
    maxDisplayRef.current = instantMax

    const activeRoleByQ = new Map<string, string>()
    const massForBudget = new Map<string, number>()
    const placements = []
    for (const q of active) {
      const m = mass.get(q)
      const propAdd = prop.get(q) ?? 0
      const d = m ? m.display : propAdd > 0 ? displayMass(propAdd) : 0
      const role = roleByQ.get(q) || "untagged"
      activeRoleByQ.set(q, role)
      massForBudget.set(q, d)
      placements.push(
        placeSymbol({
          qname: q,
          role,
          roles,
          displayMass: d,
          maxDisplay: instantMax,
          historicalMass: histByQ.get(q) ?? 0,
        }),
      )
    }
    applyClusterCohesion(placements, activeRoleByQ, histByQ)
    const budget = applyVisibleBudget(
      placements,
      massForBudget,
      activeRoleByQ,
      VISIBLE_BUDGET,
      useAGMStore.getState().model.pinnedSet(),
    )

    // Pill-vs-dot threshold (top PILL_PERCENTILE by mass): pills reserve their
    // full measured width when spreading; dots reserve a tight footprint so the
    // faint exploration net stays compact instead of being spaced like labels.
    const keptMasses = budget.kept
      .map((p) => massForBudget.get(p.qname) ?? 0)
      .filter((v) => v > 0)
      .sort((a, b) => a - b)
    const pillThreshold =
      keptMasses.length > 0
        ? (keptMasses[Math.floor(keptMasses.length * (1 - PILL_PERCENTILE))] ?? Infinity)
        : Infinity
    pillThresholdRef.current = pillThreshold
    const widthFor = (qname: string): number => {
      const m = massForBudget.get(qname) ?? 0
      return m >= pillThreshold ? pillWidth(qname) : DOT_FOOTPRINT
    }
    spreadTargets(budget.kept, widthFor)

    const targets = new Map<string, Target>()
    for (const p of budget.kept) {
      // dominant intent → render kind; propagated-only nodes (no direct event)
      // render as faint grep-style dots (inferred, not directly attended).
      const kind = mass.get(p.qname)?.kind ?? "grep"
      targets.set(p.qname, {
        qname: p.qname,
        role: activeRoleByQ.get(p.qname) || "untagged",
        x: p.x,
        y: p.y,
        mass: massForBudget.get(p.qname) ?? 0,
        angle: p.angle,
        kind,
      })
    }
    targetsRef.current = targets
  }

  // ---- RENDER clock: ease drawn nodes toward targets; animate entry/exit. ----
  const loop = () => {
    const canvas = canvasRef.current
    if (!canvas) {
      rafRef.current = null
      return
    }
    const nowMs = performance.now()
    // Slow decay tick: refresh targets occasionally so cooling symbols drift out
    // smoothly. ONLY while the agent turn is running — when the turn ends the
    // simulation FREEZES (targets stop moving, the loop settles to rest and
    // stops). This gives a stable "frozen photograph" of the finished turn.
    if (isAgentRunning() && nowMs - lastModelTickRef.current > MODEL_TICK_MS) {
      lastModelTickRef.current = nowMs
      recomputeTargets()
    }

    const drawn = drawnRef.current
    const targets = targetsRef.current

    // Ease the rendering denominator toward the model's value (no snap-rescale).
    const want = maxDisplayRef.current
    const prevMax = smoothedMaxRef.current
    smoothedMaxRef.current =
      want > prevMax ? prevMax + (want - prevMax) * MAX_DISPLAY_EASE : want
    const maxDisplay = smoothedMaxRef.current

    let motion = 0

    // Spawn drawn nodes for any new target — entering from the perimeter at the
    // symbol's bearing, with appear=0 so it fades+scales in (never instant).
    for (const [q, t] of targets) {
      let node = drawn.get(q)
      if (!node) {
        const ex = Math.cos(t.angle) * R_MAX
        const ey = Math.sin(t.angle) * R_MAX
        node = {
          qname: q,
          role: t.role,
          x: ex,
          y: ey,
          sx: ex,
          sy: ey,
          tx: t.x,
          ty: t.y,
          p: 0,
          mass: t.mass,
          kind: t.kind,
          appear: 0,
          leaving: false,
        }
        drawn.set(q, node)
      }
      node.kind = t.kind
      node.leaving = false
      node.role = t.role
      node.mass = t.mass
      // Re-anchor the journey if the target moved meaningfully (new tool call /
      // decay shift): start from where we are now, restart the ease-in-out.
      if (Math.hypot(t.x - node.tx, t.y - node.ty) > 1) {
        node.sx = node.x
        node.sy = node.y
        node.tx = t.x
        node.ty = t.y
        node.p = 0
      }
      motion += advanceJourney(node)
      // entry fade/scale eases in
      if (node.appear < 1) {
        node.appear = Math.min(1, node.appear + APPEAR_EASE)
        motion += 1
      }
    }

    // Nodes no longer targeted: mark leaving, retarget to the perimeter (so the
    // exit travels on the same smooth curve), fade out, then drop. Never a pop.
    for (const [q, node] of drawn) {
      if (targets.has(q)) continue
      const r = Math.hypot(node.x, node.y) || 1e-6
      const ox = (node.x / r) * R_MAX
      const oy = (node.y / r) * R_MAX
      if (!node.leaving) {
        node.leaving = true
        node.sx = node.x
        node.sy = node.y
        node.tx = ox
        node.ty = oy
        node.p = 0
      }
      motion += advanceJourney(node)
      node.appear = Math.max(0, node.appear - FADE_EASE)
      motion += 1
      if (node.appear <= 0) drawn.delete(q)
    }

    draw(maxDisplay)

    if (motion < 0.5 && drawn.size === 0 && targets.size === 0) {
      rafRef.current = null
      return
    }
    rafRef.current = requestAnimationFrame(loop)
  }

  // Build the rich codelens tooltip for a hovered symbol: what it is + why it's
  // on the map (its dominant intent) + its live/historical mass + graph degree.
  const buildTooltip = (qname: string, x: number, y: number): TooltipData => {
    const s = useAGMStore.getState()
    const node = s.nodesByQname.get(qname)
    const m = s.massByQname.get(qname)
    const drawn = drawnRef.current.get(qname)
    const kind = m?.kind ?? drawn?.kind ?? "historical"
    const reason = intentReason(kind)
    return {
      x,
      y,
      qname,
      name: node?.name ?? qname.split(":").pop() ?? qname,
      role: node?.role || "untagged",
      oneLiner: node?.one_liner ?? "",
      reason: reason.label,
      reasonColor: reason.color,
      liveMass: m?.live ?? 0,
      historicalMass: s.historicalByQname.get(qname) ?? 0,
      inbound: node?.inbound_count,
      outbound: node?.outbound_count,
    }
  }

  // Pill width (world px) for a qname — measured once with the pill font, cached
  // for the frame. Feeds spreadTargets so target spacing matches what's drawn.
  const pillWidthCache = new Map<string, number>()
  const pillWidth = (qname: string): number => {
    const cached = pillWidthCache.get(qname)
    if (cached != null) return cached
    const ctx = canvasRef.current?.getContext("2d")
    if (!ctx) return 80
    ctx.font = "11px ui-sans-serif, system-ui"
    const label = qname.split(":").pop() ?? qname
    const w = ctx.measureText(label).width + 14 + MIN_GAP // padX*2 + min gap
    pillWidthCache.set(qname, w)
    return w
  }

  // Find the qname of the node under a world-space point. Uses a generous
  // circular radius so even small dots are easy to hover / right-click; the
  // nearest qualifying node wins.
  const hitTest = (wx: number, wy: number): string | null => {
    const drawn = drawnRef.current
    const HIT_R = 14
    let best: string | null = null
    let bestD = Infinity
    for (const node of drawn.values()) {
      if (node.appear <= 0.05) continue
      const d = Math.hypot(wx - node.x, wy - node.y)
      if (d <= HIT_R && d < bestD) {
        bestD = d
        best = node.qname
      }
    }
    if (best) {
      edgeHoverRef.current = null
      return best
    }
    // No node hit → test edges. A hovered edge highlights AND behaves like its
    // symbol: a radial spoke resolves to its node; an attention (trace) edge
    // resolves to the endpoint nearest the cursor. Sets edgeHoverRef so draw()
    // can light the specific edge.
    const edge = hitEdge(wx, wy)
    edgeHoverRef.current = edge?.key ?? null
    return edge?.qname ?? null
  }

  // Distance from point (px,py) to segment (ax,ay)-(bx,by).
  const distToSeg = (
    px: number,
    py: number,
    ax: number,
    ay: number,
    bx: number,
    by: number,
  ): number => {
    const dx = bx - ax
    const dy = by - ay
    const len2 = dx * dx + dy * dy || 1e-6
    let t = ((px - ax) * dx + (py - ay) * dy) / len2
    t = Math.max(0, Math.min(1, t))
    return Math.hypot(px - (ax + dx * t), py - (ay + dy * t))
  }

  // Find the edge under the cursor: radial spokes (centre→node) and attention
  // (trace) edges. Returns the edge key (for highlight) + the symbol it behaves
  // as. Attention edges win ties (they're more meaningful than spokes).
  const hitEdge = (wx: number, wy: number): { key: string; qname: string } | null => {
    const drawn = drawnRef.current
    const HIT_W = 6 // world px tolerance around a line
    let best: { key: string; qname: string } | null = null
    let bestD = HIT_W
    // attention/trace edges first (priority)
    const store = useAGMStore.getState()
    const now = store.lastRecompute || Date.now() / 1000
    for (const ae of store.graph.liveEdges(now)) {
      const a = drawn.get(ae.from)
      const b = drawn.get(ae.to)
      if (!a || !b) continue
      const d = distToSeg(wx, wy, a.x, a.y, b.x, b.y)
      if (d < bestD) {
        bestD = d
        // behave as the endpoint nearest the cursor
        const near = Math.hypot(wx - a.x, wy - a.y) <= Math.hypot(wx - b.x, wy - b.y) ? a : b
        best = { key: `ae:${ae.from}|${ae.to}`, qname: near.qname }
      }
    }
    if (best) return best
    // radial spokes
    for (const node of drawn.values()) {
      if (node.appear <= 0.05) continue
      const d = distToSeg(wx, wy, 0, 0, node.x, node.y)
      if (d < bestD) {
        bestD = d
        best = { key: `sp:${node.qname}`, qname: node.qname }
      }
    }
    return best
  }

  // Blast radius: light up the cascade set as attention so the user sees what
  // would regenerate if this symbol changed.
  const revealBlastRadius = (qname: string) => {
    graphClient
      .blastRadius(qname)
      .then((res) => {
        const agm = useAGMStore.getState()
        const now = Date.now() / 1000
        for (const c of res.cascade ?? []) agm.ingest(c.qname, "grep", now)
        agm.ingest(qname, "read", now)
        agm.recompute(now)
      })
      .catch(() => {})
  }

  // Attention stats: a quick inspector (alert for now — host can replace with a
  // panel). Pulls live + historical mass and node metadata.
  const showStats = (qname: string) => {
    const s = useAGMStore.getState()
    const node = s.nodesByQname.get(qname)
    const m = s.massByQname.get(qname)
    const hist = s.historicalByQname.get(qname) ?? 0
    const lines = [
      qname,
      `role: ${node?.role ?? "—"}`,
      `live mass (display): ${(m?.display ?? 0).toFixed(2)}`,
      `historical mass: ${hist.toFixed(1)}`,
      `inbound: ${node?.inbound_count ?? "—"}  outbound: ${node?.outbound_count ?? "—"}`,
    ]
    window.alert(lines.join("\n"))
  }

  const draw = (maxDisplay: number) => {
    const canvas = canvasRef.current
    if (!canvas) return
    const ctx = canvas.getContext("2d")
    if (!ctx) return
    const dpr = window.devicePixelRatio || 1
    const w = canvas.clientWidth
    const h = canvas.clientHeight
    if (canvas.width !== w * dpr || canvas.height !== h * dpr) {
      canvas.width = w * dpr
      canvas.height = h * dpr
    }
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0)
    ctx.clearRect(0, 0, w, h)

    // Fixed coordinate system: centre of the canvas is (0,0). Only zoom scales.
    const k = zoomRef.current
    ctx.save()
    ctx.translate(w / 2, h / 2)
    ctx.scale(k, k)

    const store = useAGMStore.getState()
    const drawn = drawnRef.current
    const roles = store.roles

    // --- the crosshair: current attention origin (always present) ---
    drawCrosshair(ctx)

    // --- role clusters: centroid + bounds of each role's visible nodes. A role
    // is an emergent REGION (not a single node), so we draw a faint enclosing
    // halo behind its members and a distinct region heading — making it obvious
    // the label names the whole area, not one symbol.
    interface ClusterAcc {
      sx: number
      sy: number
      n: number
      minX: number
      minY: number
      maxX: number
      maxY: number
    }
    const clusterAcc = new Map<string, ClusterAcc>()
    for (const n of drawn.values()) {
      if (n.mass <= 0) continue
      let a = clusterAcc.get(n.role)
      if (!a) {
        a = { sx: 0, sy: 0, n: 0, minX: n.x, minY: n.y, maxX: n.x, maxY: n.y }
        clusterAcc.set(n.role, a)
      }
      a.sx += n.x
      a.sy += n.y
      a.n += 1
      a.minX = Math.min(a.minX, n.x)
      a.minY = Math.min(a.minY, n.y)
      a.maxX = Math.max(a.maxX, n.x)
      a.maxY = Math.max(a.maxY, n.y)
    }

    // Region halos — drawn FIRST (behind everything) so members sit on top.
    for (const [, a] of clusterAcc) {
      if (a.n < 2) continue
      const cx = a.sx / a.n
      const cy = a.sy / a.n
      // radius covering the members + padding
      const rr =
        Math.max(Math.hypot(a.maxX - a.minX, a.maxY - a.minY) / 2, 40) + 34
      ctx.beginPath()
      ctx.arc(cx, cy, rr, 0, Math.PI * 2)
      ctx.fillStyle = "#1e293b"
      ctx.globalAlpha = 0.18
      ctx.fill()
      ctx.strokeStyle = "#334155"
      ctx.globalAlpha = 0.35
      ctx.setLineDash([4, 4])
      ctx.lineWidth = 1
      ctx.stroke()
      ctx.setLineDash([])
      ctx.globalAlpha = 1
    }

    // --- radial spokes from the centre to each node ---
    // Inter-symbol repo edges are disabled; instead every node draws a spoke to
    // the attention origin, reinforcing "distance from centre = relevance".
    // Opacity scales with the node's relevance (hot symbols → stronger spokes,
    // faint symbols → faint spokes); the hovered node's spoke is highlighted.
    const hoveredQ = hoverRef.current
    const hoveredEdge = edgeHoverRef.current
    for (const node of drawn.values()) {
      const a = smoothstep(node.appear)
      if (a <= 0) continue
      const rel = maxDisplay > 0 ? Math.min(1, node.mass / maxDisplay) : 0
      // a spoke highlights when its node is hovered OR the spoke itself is hovered
      const isHover = node.qname === hoveredQ || hoveredEdge === `sp:${node.qname}`
      ctx.beginPath()
      ctx.moveTo(0, 0)
      ctx.lineTo(node.x, node.y)
      if (isHover) {
        ctx.strokeStyle = "#cbd5e1"
        ctx.globalAlpha = 0.7 * a
        ctx.lineWidth = 1.75
      } else {
        ctx.strokeStyle = RADIAL_COLOR
        // base 0.08 (faint symbols) → up to ~0.4 (hot symbols)
        ctx.globalAlpha = (0.08 + 0.32 * rel) * a
        ctx.lineWidth = 1
      }
      ctx.stroke()
      ctx.globalAlpha = 1
      ctx.lineWidth = 1
    }

    // --- attention edges (trace constellations): bright reasoning paths ---
    // An edge highlights when it is hovered, OR when either endpoint is hovered
    // (the edge "acts like the symbol").
    const now = store.lastRecompute || Date.now() / 1000
    for (const ae of store.graph.liveEdges(now)) {
      const a = drawn.get(ae.from)
      const b = drawn.get(ae.to)
      if (!a || !b) continue
      const isHover =
        hoveredEdge === `ae:${ae.from}|${ae.to}` ||
        hoveredQ === ae.from ||
        hoveredQ === ae.to
      ctx.beginPath()
      ctx.moveTo(a.x, a.y)
      ctx.lineTo(b.x, b.y)
      if (isHover) {
        ctx.strokeStyle = "#e9d5ff" // brighter violet-white
        ctx.globalAlpha = 0.95
        ctx.lineWidth = 2.5
      } else {
        ctx.strokeStyle = ATTENTION_EDGE_COLOR
        ctx.globalAlpha = Math.min(0.85, 0.4 + ae.heat * 0.15)
        ctx.lineWidth = 1.75
      }
      ctx.stroke()
      ctx.globalAlpha = 1
      ctx.lineWidth = 1
    }

    // --- symbols: only the TOP percentile by attention render as NAME PILLS;
    // everyone else is a small DOT (name revealed on hover). Distance from centre
    // encodes relevance; opacity reinforces it. Monochrome, no role colours.
    const sorted = [...drawn.values()].sort((a, b) => a.mass - b.mass)
    // Pill-vs-dot threshold computed in recomputeTargets (top PILL_PERCENTILE),
    // so spread + render agree on who is a pill.
    const pillThreshold = pillThresholdRef.current
    const hovered = hoverRef.current
    const pinned = store.model.pinnedSet()
    for (const node of sorted) {
      const m = node.mass
      const rel = maxDisplay > 0 ? Math.min(1, m / maxDisplay) : 0
      const a = smoothstep(node.appear)
      const scale = 0.6 + 0.4 * a
      const isHover = node.qname === hovered
      const isPinned = pinned.has(node.qname)
      // top-percentile, pinned (edited), or hovered → name pill; rest → dot.
      if ((m > 0 && m >= pillThreshold) || isPinned || isHover) {
        const label = node.qname.split(":").pop() ?? node.qname
        const opacity = (0.28 + 0.72 * rel) * a
        const hot = isPinned || (m > 0 && tierFor(m, maxDisplay) === "dominant")
        drawSymbolPill(ctx, label, node.x, node.y, opacity, hot, scale)
      } else {
        drawDot(ctx, node.x, node.y, rel, a)
      }
    }

    // --- role REGION headings: a distinct label for the whole area (not a pill
    // like a symbol). Uppercase + letter-spaced + an underline, placed above the
    // region halo, so it obviously names the region, not a node.
    for (const [role, a] of clusterAcc) {
      if (a.n < 2) continue
      const cx = a.sx / a.n
      drawRegionLabel(ctx, role, cx, a.minY - 22)
    }

    ctx.restore()
  }

  // --- zoom only (centre stays fixed; no pan, no camera follow) ---
  useEffect(() => {
    const canvas = canvasRef.current
    if (!canvas) return
    const onWheel = (e: WheelEvent) => {
      e.preventDefault()
      const factor = Math.exp(-e.deltaY * 0.001)
      zoomRef.current = Math.min(4, Math.max(0.25, zoomRef.current * factor))
      kick()
    }
    // Right-click a symbol → context menu. Hit-test by inverting the draw
    // transform (centre-origin, no pan, zoom only) and finding the nearest pill.
    const onContext = (e: MouseEvent) => {
      const rect = canvas.getBoundingClientRect()
      const k = zoomRef.current
      const wx = (e.clientX - rect.left - rect.width / 2) / k
      const wy = (e.clientY - rect.top - rect.height / 2) / k
      const hit = hitTest(wx, wy)
      if (!hit) return // let the background menu (or nothing) handle it
      e.preventDefault()
      const node = useAGMStore.getState().nodesByQname?.get(hit)
      openContextMenu(
        e,
        buildSymbolMenu({
          qname: hit,
          filePath: node?.file_path,
          signature: node?.one_liner ?? null, // system model carries one_liner, not signature
          onShowBlastRadius: revealBlastRadius,
          onShowStats: showStats,
        }),
      )
    }
    // Hover → reveal the symbol under the cursor (a dot shows its name as a
    // tooltip + temporarily renders as a pill). Throttled to actual changes.
    const onMove = (e: MouseEvent) => {
      const rect = canvas.getBoundingClientRect()
      const k = zoomRef.current
      const wx = (e.clientX - rect.left - rect.width / 2) / k
      const wy = (e.clientY - rect.top - rect.height / 2) / k
      const prevEdge = edgeHoverRef.current
      const hit = hitTest(wx, wy) // also updates edgeHoverRef
      const px = e.clientX - rect.left
      const py = e.clientY - rect.top
      if (hit !== hoverRef.current || edgeHoverRef.current !== prevEdge) {
        hoverRef.current = hit
        setTooltip(hit ? buildTooltip(hit, px, py) : null)
        kick()
      } else if (hit && tooltipRef.current) {
        setTooltip(buildTooltip(hit, px, py))
      }
    }
    const onLeave = () => {
      if (hoverRef.current || edgeHoverRef.current) {
        hoverRef.current = null
        edgeHoverRef.current = null
        setTooltip(null)
        kick()
      }
    }
    canvas.addEventListener("wheel", onWheel, { passive: false })
    canvas.addEventListener("contextmenu", onContext)
    canvas.addEventListener("mousemove", onMove)
    canvas.addEventListener("mouseleave", onLeave)
    return () => {
      canvas.removeEventListener("wheel", onWheel)
      canvas.removeEventListener("contextmenu", onContext)
      canvas.removeEventListener("mousemove", onMove)
      canvas.removeEventListener("mouseleave", onLeave)
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  useEffect(() => {
    kick()
    return () => {
      if (rafRef.current != null) cancelAnimationFrame(rafRef.current)
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  const showIdleHint = useMemo(() => !hasAttention, [hasAttention])

  return (
    <div className={className} style={{ position: "relative" }}>
      <canvas ref={canvasRef} style={{ width: "100%", height: "100%", display: "block" }} />
      {showIdleHint && (
        <div
          style={{
            position: "absolute",
            inset: 0,
            display: "flex",
            alignItems: "flex-end",
            justifyContent: "center",
            paddingBottom: "18%", // keep clear of the centre crosshair
            color: "#3f4a5a",
            fontSize: 13,
            pointerEvents: "none",
          }}
        >
          No attention yet — the map fills in as the agent works.
        </div>
      )}
      {tooltip && (
        <div
          style={{
            position: "absolute",
            left: Math.min(tooltip.x + 14, 100000),
            top: tooltip.y + 14,
            maxWidth: 340,
            padding: "8px 10px",
            borderRadius: 7,
            background: "#0b1220f2",
            border: "1px solid #334155",
            boxShadow: "0 6px 20px #0008",
            color: "#e2e8f0",
            fontSize: 12,
            fontFamily: "ui-sans-serif, system-ui",
            pointerEvents: "none",
            zIndex: 10,
          }}
        >
          {/* reason pill — why this symbol is on the map */}
          <div
            style={{
              display: "inline-block",
              fontSize: 10,
              fontWeight: 600,
              color: tooltip.reasonColor,
              border: `1px solid ${tooltip.reasonColor}55`,
              background: `${tooltip.reasonColor}1a`,
              borderRadius: 4,
              padding: "1px 6px",
              marginBottom: 6,
            }}
          >
            {tooltip.reason}
          </div>
          {/* symbol name (mono) */}
          <div
            style={{
              fontFamily: "ui-monospace, monospace",
              fontSize: 12,
              color: "#f1f5f9",
              wordBreak: "break-all",
            }}
          >
            {tooltip.name}
            <span style={{ color: "#64748b" }}> · {tooltip.role}</span>
          </div>
          {/* one-liner (codelens) */}
          {tooltip.oneLiner && (
            <div style={{ color: "#94a3b8", marginTop: 4, lineHeight: 1.35 }}>
              {tooltip.oneLiner}
            </div>
          )}
          {/* mass + degree */}
          <div
            style={{
              display: "flex",
              gap: 12,
              marginTop: 6,
              fontSize: 10.5,
              color: "#64748b",
              fontFamily: "ui-monospace, monospace",
            }}
          >
            <span>live {tooltip.liveMass.toFixed(1)}</span>
            <span>hist {tooltip.historicalMass.toFixed(1)}</span>
            {tooltip.inbound != null && (
              <span>
                ↓{tooltip.inbound} ↑{tooltip.outbound}
              </span>
            )}
          </div>
          {/* full qname, dim */}
          <div
            style={{
              marginTop: 5,
              fontSize: 9.5,
              color: "#475569",
              fontFamily: "ui-monospace, monospace",
              wordBreak: "break-all",
            }}
          >
            {tooltip.qname}
          </div>
        </div>
      )}
    </div>
  )
}

// Ease-in-out curve (slow start, fast middle, slow end) — Hermite smoothstep.
// Used for entry/exit fade+scale so nothing pops; the appearance "breathes" in.
function smoothstep(t: number): number {
  const x = Math.max(0, Math.min(1, t))
  return x * x * (3 - 2 * x)
}

// Advance a node's journey by one frame: bump progress and set its position to
// the smoothstep-interpolated point start→target (slow-start, slow-end). Returns
// the per-frame displacement so the loop can detect rest. At p=1 it's a no-op.
function advanceJourney(node: Drawn): number {
  if (node.p >= 1) {
    node.x = node.tx
    node.y = node.ty
    return 0
  }
  const px = node.x
  const py = node.y
  node.p = Math.min(1, node.p + JOURNEY_RATE)
  const e = smoothstep(node.p)
  node.x = node.sx + (node.tx - node.sx) * e
  node.y = node.sy + (node.ty - node.sy) * e
  return Math.abs(node.x - px) + Math.abs(node.y - py)
}

// The fixed centre crosshair — the current attention origin. Nothing else ever
// occupies the exact centre; this is the coordinate system's (0,0).
function drawCrosshair(ctx: CanvasRenderingContext2D) {
  const s = 7
  ctx.strokeStyle = "#475569"
  ctx.globalAlpha = 0.8
  ctx.lineWidth = 1
  ctx.beginPath()
  ctx.moveTo(-s, 0)
  ctx.lineTo(s, 0)
  ctx.moveTo(0, -s)
  ctx.lineTo(0, s)
  ctx.stroke()
  ctx.globalAlpha = 1
}

// A small monochrome dot for a low-attention symbol (name revealed on hover).
// Radius scales subtly with relevance; opacity carries heat + the entry fade.
function drawDot(ctx: CanvasRenderingContext2D, cx: number, cy: number, rel: number, appear: number) {
  const r = (2.2 + rel * 2.6) * (0.6 + 0.4 * appear)
  ctx.beginPath()
  ctx.arc(cx, cy, r, 0, Math.PI * 2)
  ctx.fillStyle = "#94a3b8"
  ctx.globalAlpha = (0.3 + 0.5 * rel) * appear
  ctx.fill()
  ctx.globalAlpha = 1
}

// A monochrome symbol pill: the symbol's short name in a subtle rounded chip.
// Heat reads through opacity (passed in) + a brighter text for the hottest.
// No role colour — the whole map is grayscale, distance encodes relevance.
function drawSymbolPill(
  ctx: CanvasRenderingContext2D,
  label: string,
  cx: number,
  cy: number,
  opacity: number,
  hot: boolean,
  scale = 1,
) {
  ctx.font = `${hot ? "600 " : ""}11px ui-sans-serif, system-ui`
  ctx.textAlign = "center"
  ctx.textBaseline = "middle"
  const padX = 7
  const tw = ctx.measureText(label).width
  const w = (tw + padX * 2) * scale
  const h = 17 * scale
  const x = cx - w / 2
  const y = cy - h / 2
  const r = h / 2
  ctx.beginPath()
  ctx.moveTo(x + r, y)
  ctx.arcTo(x + w, y, x + w, y + h, r)
  ctx.arcTo(x + w, y + h, x, y + h, r)
  ctx.arcTo(x, y + h, x, y, r)
  ctx.arcTo(x, y, x + w, y, r)
  ctx.closePath()
  // chip background: brighter (less transparent) for hotter symbols
  ctx.fillStyle = hot ? "#33415560" : "#1e293b"
  ctx.globalAlpha = opacity
  ctx.fill()
  ctx.globalAlpha = 1
  // text: white-ish, dimmed by opacity
  ctx.fillStyle = hot ? "#f1f5f9" : "#cbd5e1"
  ctx.globalAlpha = opacity
  ctx.fillText(label, cx, cy)
  ctx.globalAlpha = 1
  ctx.textBaseline = "alphabetic"
}

// A role REGION heading — visually distinct from a symbol pill so it obviously
// names the whole area: uppercase, letter-spaced, muted, with a short underline.
// No rounded chip (that's the symbol-pill look).
function drawRegionLabel(ctx: CanvasRenderingContext2D, role: string, cx: number, cy: number) {
  const text = role.toUpperCase()
  ctx.font = "600 10px ui-sans-serif, system-ui"
  ctx.textAlign = "center"
  ctx.textBaseline = "middle"
  ctx.fillStyle = "#94a3b8"
  // letter-spacing (canvas has no native tracking pre-2023; draw char by char)
  const spacing = 2
  const widths = [...text].map((c) => ctx.measureText(c).width)
  const total = widths.reduce((s, w) => s + w + spacing, 0) - spacing
  let x = cx - total / 2
  for (let i = 0; i < text.length; i++) {
    ctx.fillText(text[i], x + widths[i] / 2, cy)
    x += widths[i] + spacing
  }
  // underline spanning the label width
  ctx.strokeStyle = "#475569"
  ctx.globalAlpha = 0.7
  ctx.lineWidth = 1
  ctx.beginPath()
  ctx.moveTo(cx - total / 2, cy + 9)
  ctx.lineTo(cx + total / 2, cy + 9)
  ctx.stroke()
  ctx.globalAlpha = 1
  ctx.textBaseline = "alphabetic"
}
