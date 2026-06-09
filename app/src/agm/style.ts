// AGM visual encoding — minimal, system-monitor aesthetic (NOT a planetarium).
// Heat reads through opacity / glow / weight / border over the stable role hue;
// no rainbow thermal ramps, no neon. Reuses the existing role palette so AGM and
// the legacy view share one colour identity.

import { roleColor as baseRoleColor } from "@/graph/style"
import { SYNTHETIC_ROLE } from "./synthetic"

// Synthetic / external surfaces get a single muted neutral so they read as
// "outside the code" without competing with real roles.
const EXTERNAL_COLOR = "#64748b" // slate

export function roleColor(role: string): string {
  if (role === SYNTHETIC_ROLE) return EXTERNAL_COLOR
  return baseRoleColor(role)
}

// Visibility tiers from a node's display mass, RELATIVE to the current max on
// screen (never fixed thresholds). Hysteresis is applied by the caller (a node
// must cross a slightly higher bar to appear than to stay) to avoid flicker.
export type Tier = "hidden" | "visible" | "dominant"

export function tierFor(displayMassValue: number, maxDisplayMass: number): Tier {
  if (maxDisplayMass <= 0) return "hidden"
  const rel = displayMassValue / maxDisplayMass
  if (rel < 0.08) return "hidden"
  if (rel >= 0.6) return "dominant"
  return "visible"
}

// Node opacity from relative heat: cold nodes fade, hot nodes are solid.
// Floor keeps a just-visible node faintly present rather than invisible.
export function nodeOpacity(displayMassValue: number, maxDisplayMass: number): number {
  if (maxDisplayMass <= 0) return 0
  const rel = Math.min(1, displayMassValue / maxDisplayMass)
  return 0.25 + 0.75 * rel
}

// Node radius (screen px at scale 1) from relative heat. Modest range — size is
// a secondary cue to opacity, kept restrained.
export function nodeRadius(displayMassValue: number, maxDisplayMass: number): number {
  const rel = maxDisplayMass > 0 ? Math.min(1, displayMassValue / maxDisplayMass) : 0
  return 4 + rel * 8
}

// Soft glow alpha for hot nodes — capped low so the map never looks like a
// light show. Only the upper heat band glows at all.
export function glowAlpha(displayMassValue: number, maxDisplayMass: number): number {
  const rel = maxDisplayMass > 0 ? displayMassValue / maxDisplayMass : 0
  if (rel < 0.5) return 0
  return 0.12 + 0.18 * (rel - 0.5) * 2 // 0.12..0.30 over the top half
}

// Role-well (continent) base styling — always visible, low-key. Heat brightens
// the label/ring but the well itself stays put (fixed geography).
export const ROLE_LABEL_COLOR = "#cbd5e1"
export const ROLE_RING_COLOR = "#334155"

// Attention-graph (reasoning) edges: the violet trace colour, drawn over the
// dim repo edges so reasoning dominates topology.
export const ATTENTION_EDGE_COLOR = "#a78bfa"
export const REPO_EDGE_COLOR = "#1e293b"

// Investigation ring — quiet neutral; confidence reads through ring opacity /
// tightness, not hue (no dramatic "storm").
export const INVESTIGATION_RING_COLOR = "#e2e8f0"
export const NEGATIVE_EVIDENCE_COLOR = "#f43f5e"
