// The attention graph — the agent's ACTUAL reasoning paths, distinct from the
// repository graph (possible relationships). A trace event creates trace edges
// between the symbols the agent moved between; this graph IS the trail (paths,
// not coordinates — a major PRD correction). Edge heat decays like node mass.
//
// Scoped to the current investigation: when the investigation changes, the graph
// is reset (continuity lives within an investigation, not across them, and not
// per-turn). Pure data + math; no React/canvas.

import { decayScalar, liveLambda } from "./weights"

export interface AttentionEdge {
  from: string
  to: string
  heat: number // raw heat at last touch
  ts: number // unix seconds of last reinforcement (for decay)
}

// Trace-edge heat decays on the trace half-life (it represents reasoning flow,
// the strongest/longest-lived signal).
const TRACE_LAMBDA = liveLambda("trace")

export class AttentionGraph {
  private edges = new Map<string, AttentionEdge>()
  private investigationId = ""
  // ordered reasoning path within the current investigation (most recent last)
  private path: string[] = []

  // Switch investigation: reset the trail + edges (continuity is per-investigation).
  setInvestigation(id: string): void {
    if (id === this.investigationId) return
    this.investigationId = id
    this.edges.clear()
    this.path = []
  }

  // Reinforce a directed reasoning edge (from a trace/flow transition).
  reinforce(from: string, to: string, ts: number, amount = 1): void {
    if (from === to) return
    const key = `${from}\u0000${to}`
    const e = this.edges.get(key)
    if (e) {
      // decay existing heat to now, then add
      e.heat = decayScalar(e.heat, TRACE_LAMBDA, e.ts, ts) + amount
      e.ts = ts
    } else {
      this.edges.set(key, { from, to, heat: amount, ts })
    }
    if (this.path[this.path.length - 1] !== to) this.path.push(to)
    if (this.path.length > 64) this.path = this.path.slice(-64)
  }

  // Record a sequence of transitions (a trace chain: a→b→c).
  reinforceChain(chain: string[], ts: number, amount = 1): void {
    for (let i = 0; i + 1 < chain.length; i++) {
      this.reinforce(chain[i], chain[i + 1], ts, amount)
    }
  }

  // Live edges with heat above a floor at `now`, heat decayed to now.
  liveEdges(now: number, floor = 1e-3): AttentionEdge[] {
    const out: AttentionEdge[] = []
    for (const e of this.edges.values()) {
      const heat = decayScalar(e.heat, TRACE_LAMBDA, e.ts, now)
      if (heat > floor) out.push({ from: e.from, to: e.to, heat, ts: e.ts })
    }
    return out
  }

  // The current reasoning trail (ordered symbol path) for the investigation.
  trail(): string[] {
    return [...this.path]
  }

  // Drop fully-decayed edges to keep memory bounded.
  prune(now: number, floor = 1e-3): void {
    for (const [key, e] of this.edges) {
      if (decayScalar(e.heat, TRACE_LAMBDA, e.ts, now) <= floor) this.edges.delete(key)
    }
  }
}
