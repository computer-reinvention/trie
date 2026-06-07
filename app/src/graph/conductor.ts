import { create } from "zustand"
import { useGraphStore } from "@/store/graphStore"
import { useSettingsStore } from "@/store/settingsStore"
import { graphClient } from "@/api/graphClient"
import { activityColor } from "@/graph/style"
import type { AgentState } from "@/api/types"

// The Conductor — the single source of truth for the agent-activity performance
// (docs/choreography-prd.md §2). It owns:
//   - the transient FX layer (ripples, comet-tails, breadcrumbs, chevrons),
//   - governance (concurrency cap, staggering, decay),
//   - a cue log (ring buffer) that powers turn replay.
//
// Per-node *body* pulse still lives in graphStore + the canvas animator; the
// Conductor adds the higher-order, cross-surface choreography and the FX overlay
// renders from this store on one rAF.

// ---------------------------------------------------------------------------
// Motion preferences
// ---------------------------------------------------------------------------

export type MotionIntensity = "cinematic" | "restrained" | "off"
export type CameraMode = "cinematic" | "edge-only" | "off"

export interface MotionPrefs {
  intensity: MotionIntensity
  camera: CameraMode
  reduceMotion: boolean
}

function osPrefersReducedMotion(): boolean {
  return (
    typeof window !== "undefined" &&
    typeof window.matchMedia === "function" &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches
  )
}

export function motionPrefs(): MotionPrefs {
  const s = useSettingsStore.getState()
  const intensity = (s.get<string>("motion.intensity") as MotionIntensity) ?? "cinematic"
  const camera = (s.get<string>("motion.camera") as CameraMode) ?? "edge-only"
  const rm = (s.get<string>("motion.reducedMotion") as string) ?? "auto"
  const reduceMotion =
    intensity === "off" || rm === "force-on" || (rm === "auto" && osPrefersReducedMotion())
  return { intensity, camera, reduceMotion }
}

// ---------------------------------------------------------------------------
// FX + cue model
// ---------------------------------------------------------------------------

export interface Ripple {
  id: number
  qname: string
  color: string
  state: AgentState
  born: number
  ttl: number
}
export interface Comet {
  id: number
  from: string
  to: string
  color: string
  born: number
  ttl: number
}
export interface Breadcrumb {
  qname: string
  seq: number
  color: string
  born: number
}

// A recorded cue — the unit of the replayable timeline.
export type CueKind = "glance" | "scan" | "write" | "cascade" | "flow"
export interface Cue {
  t: number // ms since turn start
  kind: CueKind
  from?: string
  to?: string
  state: AgentState
}

const RIPPLE_TTL = 1400
const COMET_TTL = 1100
const CUE_LOG_MAX = 600
// Concurrency governance (research A3): at most this many bright ripples/comets.
const MAX_RIPPLES = 6
const MAX_COMETS = 8

let _seq = 0
const nextId = () => ++_seq

interface ConductorStore {
  ripples: Ripple[]
  comets: Comet[]
  breadcrumbs: Breadcrumb[]
  // cue log for replay (ring buffer); turnStart anchors relative times
  cueLog: Cue[]
  turnStart: number
  replaying: boolean
  crumbSeq: number
  lastGlance: string | null

  emitRipple: (qname: string, state: AgentState) => void
  emitComet: (from: string, to: string, state: AgentState) => void
  emitBreadcrumb: (qname: string, state: AgentState) => void
  record: (cue: Omit<Cue, "t">) => void
  tick: (now: number) => boolean
  clearTurn: () => void
  setReplaying: (v: boolean) => void
}

export const useConductor = create<ConductorStore>((set, get) => ({
  ripples: [],
  comets: [],
  breadcrumbs: [],
  cueLog: [],
  turnStart: Date.now(),
  replaying: false,
  crumbSeq: 0,
  lastGlance: null,

  emitRipple: (qname, state) =>
    set((s) => {
      if (motionPrefs().reduceMotion) return {}
      const ripples = [
        ...s.ripples,
        { id: nextId(), qname, color: activityColor(state), state, born: Date.now(), ttl: RIPPLE_TTL },
      ]
      // governance: keep most-recent MAX_RIPPLES
      return { ripples: ripples.slice(-MAX_RIPPLES) }
    }),

  emitComet: (from, to, state) =>
    set((s) => {
      if (motionPrefs().reduceMotion || from === to) return {}
      const comets = [...s.comets, { id: nextId(), from, to, color: activityColor(state), born: Date.now(), ttl: COMET_TTL }]
      return { comets: comets.slice(-MAX_COMETS) }
    }),

  emitBreadcrumb: (qname, state) =>
    set((s) => {
      const seq = s.crumbSeq + 1
      const existing = s.breadcrumbs.filter((b) => b.qname !== qname)
      return {
        crumbSeq: seq,
        breadcrumbs: [...existing, { qname, seq, color: activityColor(state), born: Date.now() }].slice(-40),
      }
    }),

  record: (cue) =>
    set((s) => {
      const log = [...s.cueLog, { ...cue, t: Date.now() - s.turnStart }]
      return { cueLog: log.slice(-CUE_LOG_MAX) }
    }),

  // Advance FX; returns true while anything is still animating (drives the rAF).
  tick: (now) => {
    const s = get()
    const ripples = s.ripples.filter((r) => now - r.born < r.ttl)
    const comets = s.comets.filter((c) => now - c.born < c.ttl)
    if (ripples.length !== s.ripples.length || comets.length !== s.comets.length) {
      set({ ripples, comets })
    }
    return ripples.length > 0 || comets.length > 0
  },

  clearTurn: () =>
    set({
      ripples: [],
      comets: [],
      breadcrumbs: [],
      cueLog: [],
      turnStart: Date.now(),
      crumbSeq: 0,
      lastGlance: null,
    }),

  setReplaying: (replaying) => set({ replaying }),
}))

// ---------------------------------------------------------------------------
// High-level choreography (emits FX + records cues + drives node state)
// ---------------------------------------------------------------------------

// A symbol came under the agent's attention: breadcrumb + a comet from the
// previous step along the real path, all recorded for replay. The Conductor
// tracks the path tail itself so it resets cleanly at turn boundaries.
export function conductGlance(qname: string, state: AgentState): void {
  const c = useConductor.getState()
  const prev = c.lastGlance
  c.emitBreadcrumb(qname, state)
  if (prev && prev !== qname) {
    c.emitComet(prev, qname, state)
    c.record({ kind: "flow", from: prev, to: qname, state })
  }
  c.record({ kind: state === "scanning" ? "scan" : "glance", to: qname, state })
  useConductor.setState({ lastGlance: qname })
}

const RING_STAGGER_MS = 60
const MAX_RING_MS = 900

// Cascade blast radius as a staggered ripple wavefront over the REAL dependency
// graph, ordered by BFS hop (compute_cascade). Lockstep: graphStore node state
// drives the panel + bubbles; the overlay draws the ripple rings.
export async function playCascade(qname: string): Promise<void> {
  const prefs = motionPrefs()
  if (prefs.intensity === "off") return
  let res
  try {
    res = await graphClient.blastRadius(qname)
  } catch {
    return
  }
  const g = useGraphStore.getState()
  const c = useConductor.getState()
  g.setNodeAgentState(qname, "writing")
  g.bumpActivity(qname, 1)
  g.pushTrail(qname, "writing")
  c.emitRipple(qname, "writing")
  c.record({ kind: "write", to: qname, state: "writing" })
  if (!res.cascade?.length) return

  const byHop = new Map<number, string[]>()
  for (const cn of res.cascade) {
    const arr = byHop.get(cn.hop) ?? []
    arr.push(cn.qname)
    byHop.set(cn.hop, arr)
  }
  const hops = [...byHop.keys()].sort((a, b) => a - b)

  if (prefs.reduceMotion) {
    for (const cn of res.cascade) {
      g.setNodeAgentState(cn.qname, "cascade")
      g.setNote(cn.qname, `cascade · ${qname.split(":").pop()} changed`, "cascade")
    }
    return
  }

  hops.forEach((hop, i) => {
    const delay = Math.min(i * RING_STAGGER_MS, MAX_RING_MS)
    setTimeout(() => {
      const cur = useGraphStore.getState()
      const cc = useConductor.getState()
      for (const q of byHop.get(hop) ?? []) {
        cur.setNodeAgentState(q, "cascade")
        cur.bumpActivity(q, 0.7)
        cur.pushTrail(q, "cascade")
        cur.setNote(q, `cascade (hop ${hop}) · ${qname.split(":").pop()} changed`, "cascade")
        cc.emitRipple(q, "cascade")
        cc.emitComet(qname, q, "cascade")
        cc.record({ kind: "cascade", from: qname, to: q, state: "cascade" })
      }
    }, delay)
  })
}

export async function ghostCascade(qname: string): Promise<void> {
  if (motionPrefs().intensity === "off") return
  try {
    const res = await graphClient.blastRadius(qname)
    const g = useGraphStore.getState()
    for (const cn of res.cascade.slice(0, 40))
      g.setNote(cn.qname, `in blast radius of ${qname.split(":").pop()}`, "cascade")
  } catch {
    /* best effort */
  }
}

// Replay the recorded cue log at `speed` (1 = realtime). Re-emits FX with the
// original relative timing. Node bodies are not re-driven (FX-only replay).
export function replayTurn(speed = 1): void {
  const { cueLog, setReplaying, clearTurn } = useConductor.getState()
  if (!cueLog.length) return
  const log = [...cueLog]
  // snapshot then clear live FX so the replay reads cleanly
  clearTurn()
  setReplaying(true)
  const start = performance.now()
  let i = 0
  const step = () => {
    const elapsed = (performance.now() - start) * speed
    while (i < log.length && log[i].t <= elapsed) {
      const cue = log[i++]
      const c = useConductor.getState()
      if (cue.to) c.emitBreadcrumb(cue.to, cue.state)
      if (cue.kind === "write" || cue.kind === "cascade") c.emitRipple(cue.to ?? "", cue.state)
      if (cue.from && cue.to) c.emitComet(cue.from, cue.to, cue.state)
    }
    if (i < log.length) requestAnimationFrame(step)
    else useConductor.getState().setReplaying(false)
  }
  requestAnimationFrame(step)
}
