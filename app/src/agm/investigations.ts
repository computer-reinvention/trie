// Investigations — explicit, first-class spans of agent cognition (the unit of
// continuity, NOT turns). Created from the user task; labelled from the prompt
// (LLM summary as fallback); never inferred from graph clustering. Multiple may
// exist (keyed by id) even if the UI shows one. Confidence is a measure of
// attention CONCENTRATION (0..1), derived live, and is a real clustering force
// in the layout (see gravity.ts).
//
// Pure data + math; no React/canvas.

import type { Investigation, InvestigationStatus } from "@/api/types"
import { displayMass } from "./weights"

export class InvestigationRegistry {
  private byId = new Map<string, Investigation>()
  private activeId = ""

  // Open or update an investigation (explicit task boundary). Returns the id.
  set(inv: {
    id: string
    label: string
    status?: InvestigationStatus
    createdAt?: number
    agentId?: string
    sessionId?: string
  }): string {
    const existing = this.byId.get(inv.id)
    const merged: Investigation = {
      id: inv.id,
      label: inv.label,
      status: inv.status ?? existing?.status ?? "active",
      createdAt: existing?.createdAt ?? inv.createdAt ?? Date.now() / 1000,
      agentId: inv.agentId ?? existing?.agentId,
      sessionId: inv.sessionId ?? existing?.sessionId,
      confidence: existing?.confidence ?? 0,
      scope: existing?.scope ?? [],
      negativeEvidence: existing?.negativeEvidence ?? [],
    }
    this.byId.set(inv.id, merged)
    if (merged.status === "active") this.activeId = inv.id
    else if (this.activeId === inv.id) this.activeId = ""
    return inv.id
  }

  get(id: string): Investigation | undefined {
    return this.byId.get(id)
  }

  active(): Investigation | undefined {
    return this.activeId ? this.byId.get(this.activeId) : undefined
  }

  all(): Investigation[] {
    return [...this.byId.values()]
  }

  // Record explicit negative evidence ("ruled out X") on an investigation.
  addNegativeEvidence(id: string, qname: string): void {
    const inv = this.byId.get(id)
    if (inv && !inv.negativeEvidence.includes(qname)) inv.negativeEvidence.push(qname)
  }

  // Recompute confidence + scope for the active investigation from the current
  // live-mass field. Confidence = concentration of attention: a tight cluster
  // (most mass in few symbols) → high; a wide spread → low.
  updateActive(liveMass: Map<string, number>): void {
    const inv = this.active()
    if (!inv) return
    inv.scope = topScope(liveMass, 24)
    inv.confidence = concentration(liveMass)
  }
}

// Scope = the symbols currently carrying the investigation's attention, ranked.
function topScope(liveMass: Map<string, number>, n: number): string[] {
  return [...liveMass.entries()]
    .filter(([, m]) => m > 0)
    .sort((a, b) => b[1] - a[1])
    .slice(0, n)
    .map(([q]) => q)
}

// Concentration as normalised inverse entropy of the (display-compressed) mass
// distribution: 1 = all attention on one symbol (converged), 0 = uniform spread
// across many (uncertain). Returns 0 when there's no attention yet.
export function concentration(liveMass: Map<string, number>): number {
  const weights = [...liveMass.values()].map((m) => displayMass(m)).filter((w) => w > 0)
  const k = weights.length
  if (k <= 1) return k === 1 ? 1 : 0
  const total = weights.reduce((a, b) => a + b, 0)
  if (total <= 0) return 0
  let entropy = 0
  for (const w of weights) {
    const p = w / total
    entropy -= p * Math.log(p)
  }
  const maxEntropy = Math.log(k) // uniform distribution
  // inverse normalised entropy: 1 - H/Hmax → 1 when concentrated, 0 when uniform
  return maxEntropy > 0 ? 1 - entropy / maxEntropy : 0
}
