// Visual encoding for the system map: color by role, marker by class, size by
// salience. Grounded constants — every channel encodes a fact.

import type { NodeClass } from "@/api/types"

// Stable role -> hue. Standard roles get curated colors; unknown roles hash.
const ROLE_COLORS: Record<string, string> = {
  entrypoint: "#f59e0b", // amber — doors into the system
  api: "#6366f1", // indigo
  domain: "#8b5cf6", // violet — core logic
  orchestration: "#a855f7", // purple — coordinators
  persistence: "#0ea5e9", // sky — storage
  io: "#06b6d4", // cyan — outside world
  parsing: "#14b8a6", // teal
  model: "#22c55e", // green — data structures
  config: "#eab308", // yellow
  util: "#64748b", // slate — helpers
  test: "#475569", // dim slate
  untagged: "#374151",
}

export function roleColor(role: string): string {
  const r = role || "untagged"
  if (ROLE_COLORS[r]) return ROLE_COLORS[r]
  // deterministic hue from hash for project-specific roles
  let h = 0
  for (let i = 0; i < r.length; i++) h = (h * 31 + r.charCodeAt(i)) >>> 0
  return `hsl(${h % 360}, 55%, 55%)`
}

// Subsystem -> hue (used when grouping/coloring by subsystem axis).
export function subsystemColor(subsystem: string): string {
  let h = 0
  for (let i = 0; i < subsystem.length; i++) h = (h * 31 + subsystem.charCodeAt(i)) >>> 0
  return `hsl(${h % 360}, 50%, 58%)`
}

// Call-depth gradient: entry (warm amber, left) -> foundation (cool blue, right).
// `t` in [0,1] is the normalized call-flow order. This makes the primary spatial
// axis (left->right) reinforced by an obvious color shift.
export function depthColor(t: number): string {
  const u = Math.max(0, Math.min(1, t))
  // amber(40°) -> magenta/violet(290°) sweep through the warm-to-cool arc
  const hue = 40 + u * 250
  const sat = 70
  const light = 62 - u * 10 // foundations slightly deeper
  return `hsl(${hue}, ${sat}%, ${light}%)`
}

// Discrete depth-band label for the legend.
export function depthBand(t: number): string {
  if (t < 0.2) return "entry"
  if (t < 0.45) return "interface"
  if (t < 0.7) return "logic"
  return "foundation"
}

// Node radius from salience (px at globalScale 1). Hubs visibly larger.
export function nodeRadius(salience: number, cls: NodeClass): number {
  const base = 3 + salience * 9 // 3..12
  if (cls === "hub") return base * 1.35
  if (cls === "door") return base * 1.2
  return base
}

// Class marker style: how the dot is decorated to read its boundary role.
export interface ClassMarker {
  ring?: string // ring color (doors get a ring)
  halo?: string // soft glow (hubs)
  shape: "circle" | "diamond" // bedrock = diamond
  chevron?: boolean // exit = outward chevron
}

export function classMarker(cls: NodeClass, color: string): ClassMarker {
  switch (cls) {
    case "door":
      return { shape: "circle", ring: "#fbbf24" }
    case "hub":
      return { shape: "circle", halo: color }
    case "bedrock":
      return { shape: "diamond" }
    case "exit":
      return { shape: "circle", chevron: true }
    default:
      return { shape: "circle" }
  }
}

// Agent-activity colors (live monitor) — CVD-safe, soft dark-theme glows.
// See docs/choreography-prd.md §1.2.
export const ACTIVITY = {
  read: "#3b82f6", // blue — read / explain / trace target
  scan: "#2dd4bf", // teal — grep / search
  write: "#f59e0b", // amber — write / edit
  patch: "#fb923c", // orange — staged patch
  cascade: "#a78bfa", // violet — cascade wavefront
  stale: "#94a3b8", // slate — stale
  error: "#f43f5e", // rose — error
  heat: "#ef4444", // residual edit warmth
}

// Redundant-with-color line style per state (research E11): so the state is
// legible without color (CVD / monochrome). Returns a canvas dash pattern.
export function activityDash(state: string): number[] {
  switch (state) {
    case "scanning":
      return [3, 2] // dashed — searching
    case "cascade":
      return [1, 2] // dotted — propagation
    case "stale":
      return [4, 3] // long dash — stale
    case "error":
      return [5, 2, 1, 2] // dash-dot — error
    default:
      return [] // solid — read / write
  }
}

// Soft, tinted halo primitive for dark UIs (research E13): semi-transparent,
// no pure white. Draws a filled glow at (x,y).
export function drawHalo(
  ctx: CanvasRenderingContext2D,
  x: number,
  y: number,
  radius: number,
  color: string,
  alpha: number,
): void {
  ctx.save()
  ctx.beginPath()
  ctx.arc(x, y, radius, 0, 2 * Math.PI)
  ctx.fillStyle = color
  ctx.globalAlpha = Math.max(0, Math.min(1, alpha))
  ctx.fill()
  ctx.restore()
}

// Map an agent state to its activity color.
export function activityColor(state: string): string {
  switch (state) {
    case "writing":
      return ACTIVITY.write
    case "scanning":
      return ACTIVITY.scan
    case "cascade":
      return ACTIVITY.cascade
    case "stale":
      return ACTIVITY.stale
    case "error":
      return ACTIVITY.error
    default:
      return ACTIVITY.read
  }
}

// Aggregate "+N" bubble styling.
export const AGGREGATE_COLOR = "#1e293b"
export const AGGREGATE_BORDER = "#334155"
