import { useGraphStore } from "@/store/graphStore"
import { useSettingsStore } from "@/store/settingsStore"
import { graphClient } from "@/api/graphClient"

// The Conductor — central choreography orchestration (docs/choreography-prd.md §2).
//
// It does NOT own per-node pulse state (graphStore.runtime does, eased by the
// canvas). It owns the *higher-order* performance: the cascade wavefront, motion
// gating (intensity / reduced-motion), and shared preferences every surface
// reads so the graph, chat tool-rows and patches panel stay in lockstep.

export type MotionIntensity = "cinematic" | "restrained" | "off"
export type CameraMode = "cinematic" | "edge-only" | "off"

// Resolve effective motion preferences from settings + the OS reduced-motion
// signal. `auto` honors the OS but the core color/opacity signal always survives.
export interface MotionPrefs {
  intensity: MotionIntensity
  camera: CameraMode
  // true → drop movement (pans, comets, ripples, pulsing); keep color/opacity.
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

// Stagger budget (ms) — keep any reveal sequence under ~500ms (research A2).
const RING_STAGGER_MS = 60 // a touch slower than 20ms so a wavefront reads clearly
const MAX_RING_MS = 900

// Animate a cascade blast radius as a staggered violet wavefront across the real
// dependency graph, ordered by BFS hop distance. Faithful: data comes from the
// backend's compute_cascade. Lockstep: the patches panel rows pulse from the
// same graphStore state.
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
  // seed flares first
  g.setNodeAgentState(qname, "writing")
  g.bumpActivity(qname, 1)
  g.pushTrail(qname, "writing")

  if (!res.cascade?.length) return

  // group by hop so each ring lights together
  const byHop = new Map<number, string[]>()
  for (const c of res.cascade) {
    const arr = byHop.get(c.hop) ?? []
    arr.push(c.qname)
    byHop.set(c.hop, arr)
  }
  const hops = [...byHop.keys()].sort((a, b) => a - b)

  if (prefs.reduceMotion) {
    // no movement — light every cascaded node statically at once
    for (const c of res.cascade) {
      g.setNodeAgentState(c.qname, "cascade")
      g.setNote(c.qname, `cascade · ${qname.split(":").pop()} changed`, "cascade")
    }
    return
  }

  hops.forEach((hop, i) => {
    const delay = Math.min(i * RING_STAGGER_MS, MAX_RING_MS)
    setTimeout(() => {
      const cur = useGraphStore.getState()
      for (const q of byHop.get(hop) ?? []) {
        cur.setNodeAgentState(q, "cascade")
        cur.bumpActivity(q, 0.7)
        cur.pushTrail(q, "cascade")
        cur.setNote(q, `cascade (hop ${hop}) · ${qname.split(":").pop()} changed`, "cascade")
        // ripple along the edge from the seed/previous ring (faithful flow)
        cur.flowAlong(qname, q)
      }
    }, delay)
  })
}

// Pre-fetch a dim "ghost" of the blast radius when a patch is staged (so the
// user sees the impact before applying). Lights cascaded nodes faintly stale.
export async function ghostCascade(qname: string): Promise<void> {
  const prefs = motionPrefs()
  if (prefs.intensity === "off") return
  try {
    const res = await graphClient.blastRadius(qname)
    const g = useGraphStore.getState()
    for (const c of res.cascade.slice(0, 40)) g.setNote(c.qname, `in blast radius of ${qname.split(":").pop()}`, "cascade")
  } catch {
    /* best effort */
  }
}
