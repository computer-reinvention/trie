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

import { useEffect, useRef, useState } from "react"
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
  applyAnchorCohesion,
  applyVisibleBudget,
  resolveLayout,
  type PolarPlacement,
  R_MAX,
} from "@/agm/layout"
import { displayMass } from "@/agm/weights"
import { isSyntheticQname, isSyntheticFileQname, syntheticFilePath } from "@/api/types"
import { syntheticRole, syntheticLabel } from "@/agm/synthetic"
import { tierFor, ATTENTION_EDGE_COLOR, isDeliberateKind } from "@/agm/style"

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
const PILL_PERCENTILE = 0.1 // top 10%

// Footprint (world px) a dot reserves during target-spread — small so the
// exploration net packs tightly rather than being spaced like labels.
const DOT_FOOTPRINT = 16

// Auto-fit: the fraction of the smaller canvas half-dimension the drawn field's
// outer radius should occupy, so the map fills the canvas rather than huddling
// near the centre. < 1 leaves a margin for pill labels + region headings.
const FIT_TARGET_FILL = 0.82
// Clamp the auto-fit scale so a single hot node near R_MIN doesn't zoom to
// absurd levels and a huge field doesn't shrink to nothing.
const FIT_SCALE_MIN = 0.5
const FIT_SCALE_MAX = 2.2
// Easing rate for the fit scale (per frame) — slow so zoom-to-fit is a gentle
// settle, never a lurch when a new node enters/leaves.
const FIT_EASE = 0.06

// Relative-heat floor below which a node draws NO spoke (unless hovered). Cold
// peripheral nodes contributed most of the old starburst; suppressing their
// spokes keeps the field calm and the warm spokes legible.
const SPOKE_REL_FLOOR = 0.12

// Region-halo sizing (world px). Capped + member-count driven so regions stay
// tight discs instead of ballooning into overlapping blobs when members spread.
const HALO_MIN_R = 46 // smallest halo (a 2-member region)
const HALO_PER_MEMBER = 16 // sqrt(count) * this grows the halo gently
const HALO_MAX_R = 150 // hard cap — no halo ever bigger than this
const HALO_NODE_MARGIN = 26 // breathing room past the outermost member's centre
// so its pill/dot sits comfortably INSIDE the halo, not on the edge
const HALO_GAP = 24 // min visual gap kept between two adjacent region halos
const HALO_LABEL_GAP = 12 // gap between a halo's top edge and its region heading
// A role only reads as a REGION (halo + heading) once it holds a meaningful
// SHARE of the symbols currently on screen — relative, not an absolute count, so
// the map adapts to how busy it is. A role with this fraction (or more) of all
// visible members gets a halo; sparser roles just show their symbols as pills/
// dots. Floored at 2 so a halo never wraps a single symbol.
const HALO_MIN_MEMBER_FRACTION = 0.08 // ≥8% of on-screen members

// The LUMPED surface synthetics (the catch-all Filesystem/Bash/Web pills) are
// PLUMBING, not the subject of an investigation. Cap their display mass to this
// fraction of the hottest real node so they can never hold the centre / be the
// brightest node. Per-FILE synthetic nodes are exempt — they're named subjects.
const SYNTHETIC_MASS_CAP = 0.5

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
  // Auto-fit scale (eased): folds with user zoom so the drawn field fills the
  // canvas instead of huddling near the centre. 1 = no auto-scaling yet.
  const fitScaleRef = useRef(1)
  const drawnRef = useRef<Map<string, Drawn>>(new Map())
  const targetsRef = useRef<Map<string, Target>>(new Map())
  const hoverRef = useRef<string | null>(null) // qname under the cursor (for dot tooltip)
  const edgeHoverRef = useRef<string | null>(null) // key of the hovered edge (spoke/attention)
  const pillThresholdRef = useRef(Infinity) // mass cutoff for name pills (top %)
  // Region heading boxes reserved during de-overlap. draw() paints headings at
  // these EXACT positions so the painted label matches the reserved (fixed) box
  // — guaranteeing a heading never lands on a node it pushed away.
  const regionLabelsRef = useRef<Array<{ role: string; x: number; y: number }>>([])
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
  const hasLiveAttention = useAGMStore((s) => s.massByQname.size > 0)
  // A restored snapshot puts nodes on screen WITHOUT populating live mass, so
  // `hasLiveAttention` stays false. Track restore explicitly so the idle hint
  // hides whenever there's a frozen map on screen.
  const [restored, setRestored] = useState(false)
  const hasAttention = hasLiveAttention || restored

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
    const drawn = drawnRef.current
    const targets = targetsRef.current
    // No snapshot for this session → it's a fresh map. Clear any stale layout
    // left over from the previously-active session (otherwise switching from a
    // session-with-snapshot to one-without leaves ghost nodes on screen) and
    // reset the render state so the idle hint shows.
    if (!nodes || nodes.length === 0) {
      if (useAGMStore.getState().massByQname.size === 0) {
        drawn.clear()
        targets.clear()
        pillThresholdRef.current = Infinity
        smoothedMaxRef.current = 0
        maxDisplayRef.current = 0
        setRestored(false)
        kick()
      }
      return
    }
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
    // Restore the pill-vs-dot cutoff the same way recomputeTargets derives it
    // (top PILL_PERCENTILE by mass). Without this it stays Infinity and every
    // restored node renders as an anonymous dot. Deliberate-kind nodes still
    // get pills regardless via isDeliberateKind at draw time, but this surfaces
    // the hot grep/historical labels too, matching a live map.
    const restoredMasses = nodes
      .map((n) => n.mass)
      .filter((v) => v > 0)
      .sort((a, b) => a - b)
    pillThresholdRef.current =
      restoredMasses.length > 0
        ? (restoredMasses[Math.floor(restoredMasses.length * (1 - PILL_PERCENTILE))] ?? Infinity)
        : Infinity
    // Frozen map is on screen even though live mass is empty → hide idle hint.
    setRestored(true)
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
      // turn just ended on the active session → save its snapshot AND kick the
      // render loop so the region halos + headings (hidden during the turn) get
      // painted now that the sim has frozen.
      if (active && prevRunning && !running) {
        saveSnapshot(active)
        kick()
      }
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

    // Raw (uncapped) display mass for a qname from live or propagated mass.
    const rawDisplay = (q: string): number => {
      const m = mass.get(q)
      const propAdd = prop.get(q) ?? 0
      return m ? m.display : propAdd > 0 ? displayMass(propAdd) : 0
    }

    // A "lumped surface" synthetic is the catch-all Filesystem/Bash/Web/… pill —
    // pure plumbing that must never hold the centre. Per-FILE synthetic nodes
    // are now individually named real subjects, so they compete fairly like
    // symbols (a file read 10 times genuinely IS relevant).
    const isLumpedSurface = (q: string): boolean => isSyntheticQname(q) && !isSyntheticFileQname(q)

    // The normalization denominator is the hottest non-lumped node — the lumped
    // surfaces are excluded so a constant stream of misc file reads can't rescale
    // the whole map around the Filesystem pill.
    let instantMax = 0
    for (const q of active) {
      if (isLumpedSurface(q)) continue
      const d = rawDisplay(q)
      if (d > instantMax) instantMax = d
    }
    // Fallback: if ONLY lumped surfaces are active, normalise against them so the
    // map isn't blank (their cap below still applies relative to this value).
    if (instantMax <= 0) {
      for (const q of active) {
        const d = rawDisplay(q)
        if (d > instantMax) instantMax = d
      }
    }
    maxDisplayRef.current = instantMax

    // Cap a lumped-surface synthetic's display mass so it never out-shines the
    // hottest real symbol; real symbols + per-file nodes pass through unchanged.
    const cappedDisplay = (q: string): number => {
      const d = rawDisplay(q)
      if (!isLumpedSurface(q)) return d
      return Math.min(d, instantMax * SYNTHETIC_MASS_CAP)
    }

    // Even angular distribution: spread base bearings across only the roles
    // ACTUALLY on screen, not every role in the project. Passing the full role
    // list left active regions bunched wherever those few happened to fall (big
    // dead arcs between them). Using the active set fans regions evenly around
    // the circle so the canvas is used and regions don't pile up.
    // Role resolver: per-file synthetic nodes are created at ingest time and
    // aren't in the static role map, so resolve their role dynamically.
    const roleFor = (q: string): string => syntheticRole(q) ?? roleByQ.get(q) ?? "untagged"

    const activeRoles = new Set<string>()
    for (const q of active) activeRoles.add(roleFor(q))
    const roleList = activeRoles.size > 0 ? [...activeRoles] : roles

    const activeRoleByQ = new Map<string, string>()
    const massForBudget = new Map<string, number>()
    const placements = []
    for (const q of active) {
      const d = cappedDisplay(q)
      const role = roleFor(q)
      activeRoleByQ.set(q, role)
      massForBudget.set(q, d)
      placements.push(
        placeSymbol({
          qname: q,
          role,
          roles: roleList,
          displayMass: d,
          maxDisplay: instantMax,
          historicalMass: histByQ.get(q) ?? 0,
        }),
      )
    }
    applyAnchorCohesion(placements, activeRoleByQ, roleList)
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
    // A node is a NAME PILL when it was deliberately attended (read/trace/write)
    // — those keep their pill for the life of the contribution — OR when it's
    // hot enough to clear the mass cutoff (lets a hot grep/historical dot earn a
    // label). Deliberate pills reserve their measured width so spread spacing
    // matches the render and they never collide as anonymous dots.
    const isPillNode = (qname: string): boolean => {
      const kind = mass.get(qname)?.kind ?? "grep"
      if (isDeliberateKind(kind)) return true
      const m = massForBudget.get(qname) ?? 0
      return m > 0 && m >= pillThreshold
    }
    // GLOBAL, TYPE-AWARE non-overlap — delegated to the shared, pure resolveLayout
    // so the live canvas and the headless verifier run the IDENTICAL collision
    // math (no drift). It guarantees: no two node footprints overlap, and nothing
    // overlaps a region heading (headings are fixed; nodes are pushed out of
    // them). The stacking failure case is impossible — overlap resolution is law.
    const haloMinCount = Math.max(2, Math.ceil(budget.kept.length * HALO_MIN_MEMBER_FRACTION))
    const layout = resolveLayout({
      placements: budget.kept,
      roleByQname: activeRoleByQ,
      isPill: isPillNode,
      pillHalfWidth: (q) => pillWidth(q) / 2,
      regionLabelHalfWidth: regionLabelWidth,
      haloMinCount,
      pad: MIN_GAP,
      dotHalf: DOT_FOOTPRINT / 2,
      pillHalfHeight: 9,
      haloMaxR: HALO_MAX_R,
      haloNodeMargin: HALO_NODE_MARGIN,
      haloLabelGap: HALO_LABEL_GAP,
      labelHalfHeight: 8,
    })
    regionLabelsRef.current = layout.labels

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
    const synthPath = syntheticFilePath(qname)
    return {
      x,
      y,
      qname,
      name: node?.name ?? labelFor(qname),
      role: syntheticRole(qname) ?? node?.role ?? "untagged",
      // For a per-file synthetic node, surface the full path as the one-liner so
      // the tooltip says WHICH file (the pill only shows the basename).
      oneLiner: node?.one_liner ?? synthPath ?? "",
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
    const label = labelFor(qname)
    const w = ctx.measureText(label).width + 14 + MIN_GAP // padX*2 + min gap
    pillWidthCache.set(qname, w)
    return w
  }

  // Region-heading width (world px) for a role, measured with the heading font
  // (uppercase + letter-spacing), cached. Mirrors drawRegionLabel's metrics.
  const regionLabelWidthCache = new Map<string, number>()
  const regionLabelWidth = (role: string): number => {
    const cached = regionLabelWidthCache.get(role)
    if (cached != null) return cached
    const ctx = canvasRef.current?.getContext("2d")
    if (!ctx) return 80
    ctx.font = "600 10px ui-sans-serif, system-ui"
    const text = role.toUpperCase()
    const spacing = 2
    const widths = [...text].map((c) => ctx.measureText(c).width)
    const w = widths.reduce((s, cw) => s + cw + spacing, 0) - spacing
    regionLabelWidthCache.set(role, w)
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
  // as. Attention edges win ties (they're more meaningful).
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
    // radial spokes (anchored at the centre (0,0), matching draw())
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

    const store = useAGMStore.getState()
    const drawn = drawnRef.current
    const roles = store.roles

    // Region halos + headings appear only when the turn has ENDED (the sim is
    // frozen). While the agent is working the clusters are still settling, so
    // their halos would be churning noise — clustering runs regardless, only the
    // painting waits for the heaviest regions to stop moving.
    const showRegions = !isAgentRunning()

    // --- auto-fit: scale the field so it fills the canvas instead of huddling
    // near the centre. Measure the outer radius of the drawn nodes and ease the
    // fit scale toward "outer radius should occupy FIT_TARGET_FILL of the half-
    // dimension". Folds with user zoom; eased so it never lurches.
    let outerR = 0
    for (const n of drawn.values()) {
      if (n.appear <= 0.05) continue
      const r = Math.hypot(n.x, n.y)
      if (r > outerR) outerR = r
    }
    const half = Math.min(w, h) / 2
    const wantFit =
      outerR > 1
        ? Math.max(FIT_SCALE_MIN, Math.min(FIT_SCALE_MAX, (half * FIT_TARGET_FILL) / outerR))
        : fitScaleRef.current
    fitScaleRef.current += (wantFit - fitScaleRef.current) * FIT_EASE

    // Fixed coordinate system: centre of the canvas is (0,0). Only zoom + the
    // eased auto-fit scale transform the world; the centre never pans.
    const k = zoomRef.current * fitScaleRef.current
    ctx.save()
    ctx.translate(w / 2, h / 2)
    ctx.scale(k, k)

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
    // Each halo's radius is capped three ways so regions NEVER overlap into an
    // unreadable blob:
    //   1. by member count (sqrt growth, not raw extent)
    //   2. by the actual member spread (never dwarf the symbols it encloses)
    //   3. by HALF the distance to the nearest other region centroid — so two
    //      adjacent regions' halos shrink to just touch, never bleed together.
    // Relative halo threshold: a role needs at least this SHARE of all on-screen
    // members to read as a region (floored at 2 so a halo never wraps one node).
    let totalMembers = 0
    for (const [, a] of clusterAcc) totalMembers += a.n
    const haloMinMembers = Math.max(2, Math.ceil(totalMembers * HALO_MIN_MEMBER_FRACTION))
    const regionCentres = [...clusterAcc.entries()]
      .filter(([, a]) => a.n >= haloMinMembers)
      .map(([role, a]) => ({ role, cx: a.sx / a.n, cy: a.sy / a.n, acc: a, radius: 0, cover: 0 }))

    // True covering radius per region: the max distance from the region centroid
    // to ANY of its members (plus a node margin). A drawn halo must cover all its
    // members, so this is a HARD FLOOR — the cosmetic caps below can only grow a
    // halo, never shrink it below what's needed to enclose every point.
    const regionByRole = new Map(regionCentres.map((r) => [r.role, r]))
    for (const n of drawn.values()) {
      if (n.mass <= 0) continue
      const r = regionByRole.get(n.role)
      if (!r) continue
      const d = Math.hypot(n.x - r.cx, n.y - r.cy)
      if (d > r.cover) r.cover = d
    }

    for (const r of regionCentres) {
      const a = r.acc
      const countR = HALO_MIN_R + Math.sqrt(a.n) * HALO_PER_MEMBER
      // nearest neighbouring region centroid → cap at half that gap (minus a
      // small margin) so neighbouring halos can't overlap.
      let nearest = Infinity
      for (const o of regionCentres) {
        if (o === r) continue
        const d = Math.hypot(o.cx - r.cx, o.cy - r.cy)
        if (d < nearest) nearest = d
      }
      const neighbourCap = nearest === Infinity ? HALO_MAX_R : nearest / 2 - HALO_GAP / 2
      // The covering radius (+ node margin) is the FLOOR: a shown halo always
      // encloses every member. The caps only apply ABOVE that floor.
      const coverFloor = r.cover + HALO_NODE_MARGIN
      const rr = Math.max(coverFloor, Math.min(HALO_MAX_R, countR, neighbourCap))
      r.radius = rr // remember so the heading label can hug the halo edge
      // Halos (and headings) are HIDDEN while the turn runs — the clusters keep
      // moving as attention lands, so a halo mid-turn is noise. They appear only
      // once the turn ENDS (the simulation freezes), revealing the settled
      // heaviest regions. Clustering/separation still runs every frame; only the
      // painting waits. `showRegions` gates both the arc and the heading below.
      if (!showRegions) continue
      ctx.beginPath()
      ctx.arc(r.cx, r.cy, rr, 0, Math.PI * 2)
      ctx.fillStyle = "#1e293b"
      ctx.globalAlpha = 0.16
      ctx.fill()
      ctx.strokeStyle = "#334155"
      ctx.globalAlpha = 0.3
      ctx.setLineDash([4, 4])
      ctx.lineWidth = 1
      ctx.stroke()
      ctx.setLineDash([])
      ctx.globalAlpha = 1
    }

    // --- radial spokes from the ATTENTION ORIGIN (0,0) to each node ---
    // A spoke ALWAYS anchors at the centre crosshair: its whole meaning is
    // "distance from the attention origin = relevance". (Anchoring to a region
    // centroid would sever that — a floating segment says nothing about
    // relevance.) Spoke VISIBILITY mirrors the pill rule: any node that draws as
    // a name pill (deliberate read/trace/write, pinned, hovered, or hot) keeps
    // its spoke even as mass decays — so a cooled read symbol never ends up a
    // pill with no spoke. Anonymous cold dots (the grep/historical net) draw no
    // spoke, which is what calms the starburst without moving the anchor.
    const hoveredQ = hoverRef.current
    const hoveredEdge = edgeHoverRef.current
    const pillThresholdForSpokes = pillThresholdRef.current
    const pinnedForSpokes = store.model.pinnedSet()
    for (const node of drawn.values()) {
      const a = smoothstep(node.appear)
      if (a <= 0) continue
      const rel = maxDisplay > 0 ? Math.min(1, node.mass / maxDisplay) : 0
      const isHover = node.qname === hoveredQ || hoveredEdge === `sp:${node.qname}`
      const isPill =
        isDeliberateKind(node.kind) ||
        pinnedForSpokes.has(node.qname) ||
        (node.mass > 0 && node.mass >= pillThresholdForSpokes)
      // Anonymous cold dots draw no spoke unless hovered — calms the starburst.
      if (!isPill && !isHover && rel < SPOKE_REL_FLOOR) continue
      ctx.beginPath()
      ctx.moveTo(0, 0)
      ctx.lineTo(node.x, node.y)
      if (isHover) {
        ctx.strokeStyle = "#cbd5e1"
        ctx.globalAlpha = 0.7 * a
        ctx.lineWidth = 1.75
      } else {
        ctx.strokeStyle = RADIAL_COLOR
        // Named pills keep a clear spoke floor (so a cooled read symbol still
        // reads); ramps further with relevance. Dots stay faint.
        const base = isPill ? 0.32 : 0.1
        ctx.globalAlpha = Math.min(0.6, base + 0.34 * rel) * a
        ctx.lineWidth = isPill ? 1.25 : 1
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
      // A symbol shows a NAME PILL when it was deliberately attended
      // (read/trace/write — those keep their pill as mass decays, never
      // degenerating to a dot), or it's pinned/hovered, or it's hot enough to
      // clear the mass cutoff. The grep exploration net + historical seed stay
      // dots until they earn a label. (Pills are monochrome — distance, not
      // colour, encodes relevance.)
      const deliberate = isDeliberateKind(node.kind)
      if (deliberate || (m > 0 && m >= pillThreshold) || isPinned || isHover) {
        const label = labelFor(node.qname)
        const opacity = (0.28 + 0.72 * rel) * a
        const hot = isPinned || (m > 0 && tierFor(m, maxDisplay) === "dominant")
        drawSymbolPill(ctx, label, node.x, node.y, opacity, hot, scale)
      } else {
        drawDot(ctx, node.x, node.y, rel, a)
      }
    }

    // --- role REGION headings: painted at the EXACT positions reserved as fixed
    // boxes during de-overlap (regionLabelsRef), so a heading is guaranteed not
    // to land on any node — every node was pushed out of that box. Only headings
    // whose role still has a halo on screen are drawn — and, like the halos,
    // only once the turn has ended (showRegions).
    if (showRegions) {
      const haloRoles = new Set(regionCentres.map((r) => r.role))
      for (const lbl of regionLabelsRef.current) {
        if (!haloRoles.has(lbl.role)) continue
        drawRegionLabel(ctx, lbl.role, lbl.x, lbl.y, lbl.y > 0)
      }
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
    // transform (centre-origin, no pan, user-zoom × auto-fit) and finding the
    // nearest pill. Must include fitScaleRef so hits match what's painted.
    const onContext = (e: MouseEvent) => {
      const rect = canvas.getBoundingClientRect()
      const k = zoomRef.current * fitScaleRef.current
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
      const k = zoomRef.current * fitScaleRef.current
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

  const showIdleHint = !hasAttention

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

// Short display label for a symbol or synthetic node. Per-file synthetic qnames
// (agm:synthetic/file/…) show their basename; real symbols show the segment
// after the last ':'; fixed surfaces show their name.
function labelFor(qname: string): string {
  return syntheticLabel(qname) ?? qname.split(":").pop() ?? qname
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
function drawRegionLabel(
  ctx: CanvasRenderingContext2D,
  role: string,
  cx: number,
  cy: number,
  below = false,
) {
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
  // underline on the halo-facing side: BELOW the text for an above-halo label,
  // ABOVE the text for a below-halo label — so it always sits between the
  // heading and its halo.
  const uy = below ? cy - 9 : cy + 9
  ctx.strokeStyle = "#475569"
  ctx.globalAlpha = 0.7
  ctx.lineWidth = 1
  ctx.beginPath()
  ctx.moveTo(cx - total / 2, uy)
  ctx.lineTo(cx + total / 2, uy)
  ctx.stroke()
  ctx.globalAlpha = 1
  ctx.textBaseline = "alphabetic"
}
