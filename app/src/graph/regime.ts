// Scale regime: how aggressively to aggregate, derived from project size.
//
// Grounded in the empirical analysis of trie's own graph (601 production nodes,
// skeleton of 157 at salience>=0.3) and the research finding that interactive
// node-link views stay legible to a few hundred nodes. The constant-budget
// "flashlight" is the governing rule: on-screen node count stays bounded
// regardless of project size; only WHICH nodes show changes.

import type { SystemModel } from "@/api/types"

export type Regime = "tiny" | "medium" | "large" | "huge"

export interface RegimeConfig {
  regime: Regime
  // Max real nodes drawn at L2 (symbol neighborhood). The hard anti-overwhelm cap.
  budget: number
  // Default L1 salience threshold — nodes below this fold into "+N" until drilled.
  salienceFloor: number
  // Which axis L0 opens on. Roles (functional) for most; folder subsystems for
  // huge projects where a single role would be an unnavigable blob.
  defaultAxis: "role" | "subsystem"
}

// Thresholds in PRODUCTION node count (tests excluded — they are not the
// navigable surface).
export function regimeFor(productionNodeCount: number): RegimeConfig {
  if (productionNodeCount <= 150) {
    // Everything fits; the budget never bites, no folding needed.
    return { regime: "tiny", budget: 250, salienceFloor: 0, defaultAxis: "role" }
  }
  if (productionNodeCount <= 3000) {
    // trie itself lands here. Skeleton (~157) fits comfortably under budget;
    // DOI only bites when drilling a large role (e.g. util=186).
    return { regime: "medium", budget: 250, salienceFloor: 0.3, defaultAxis: "role" }
  }
  if (productionNodeCount <= 10000) {
    return { regime: "large", budget: 250, salienceFloor: 0.45, defaultAxis: "role" }
  }
  // Huge: roles become enormous blobs; open on folder subsystems instead.
  return { regime: "huge", budget: 250, salienceFloor: 0.55, defaultAxis: "subsystem" }
}

export function regimeForModel(model: SystemModel): RegimeConfig {
  return regimeFor(model.stats.production_nodes)
}
