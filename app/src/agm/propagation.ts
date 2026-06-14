// Attention propagation over the repository graph.
//
// When a symbol heats up, a fraction of that heat spreads to its immediate
// neighbours, weighted by edge kind (calls 1.0 … contains 0.2). ONE hop only,
// weak (factor 0.15): multi-hop propagation hallucinates attention. Propagated
// heat is TRANSIENT — it tints the live view but is never persisted and never
// contributes to historical mass (that reflects direct attention only).
//
// Pure function: given current live masses + a typed-edge adjacency, returns the
// transient propagated heat to add per neighbour. The caller overlays this on
// the direct live field for rendering; it is recomputed each frame and never
// stored back into the model.

import { PROPAGATION_FACTOR, PROPAGATION_HOPS, edgeWeight } from "./weights"

export interface TypedAdjacency {
  // qname -> list of (neighbour, edge kind), directed source→target
  out: Map<string, Array<{ to: string; kind: string }>>
}

// Build a directed typed adjacency from the typed edge list (all_edges).
export function buildTypedAdjacency(
  edges: Array<{ from: string; to: string; kind: string }>,
): TypedAdjacency {
  const out = new Map<string, Array<{ to: string; kind: string }>>()
  for (const e of edges) {
    let list = out.get(e.from)
    if (!list) {
      list = []
      out.set(e.from, list)
    }
    list.push({ to: e.to, kind: e.kind })
  }
  return { out }
}

// Hubs (very high out-degree) are not expanded during propagation — spreading
// from a node that calls everything would smear attention across the map. This
// mirrors the trace/cascade hub guard.
const HUB_OUT_DEGREE = 40

// Compute transient propagated heat. `liveMass` is qname→raw live mass (the
// direct field). Returns qname→added heat for neighbours (excludes sources).
export function propagate(
  liveMass: Map<string, number>,
  adj: TypedAdjacency,
): Map<string, number> {
  const gained = new Map<string, number>()
  const addGain = (q: string, amount: number) => {
    if (amount <= 0) return
    gained.set(q, (gained.get(q) ?? 0) + amount)
  }

  // One weak hop from every hot source (PROPAGATION_HOPS === 1).
  for (const [source, mass] of liveMass) {
    if (mass <= 0) continue
    const neighbours = adj.out.get(source)
    if (!neighbours || neighbours.length > HUB_OUT_DEGREE) continue
    for (const { to, kind } of neighbours) {
      addGain(to, mass * edgeWeight(kind) * PROPAGATION_FACTOR)
    }
  }

  // PROPAGATION_HOPS is 1 by design; guard kept so the constant is honoured if
  // ever raised (additional hops would iterate `gained` as the new frontier).
  void PROPAGATION_HOPS

  return gained
}
