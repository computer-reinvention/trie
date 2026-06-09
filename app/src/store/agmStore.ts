// AGM store — ties the attention model, attention graph, investigations, and
// gravity layout together and exposes snapshots to the canvas. Separate from
// graphStore (which serves the legacy renderer) so the two engines coexist
// behind the viz.engine toggle until cutover.
//
// Lifecycle:
//   setModel(model, edges)  — load topology, seed historical mass, build wells
//                              (attention-preserving: live state survives refreshes)
//   ingest(qname,type,ts)   — record a live attention event (from SSE)
//   recompute(now)          — refresh derived snapshots (mass, roles, centroid)
//   the canvas owns the rAF loop: calls recompute + gravity.step while not at rest.

import { create } from "zustand"
import type { AttentionEventType, SystemModel, TypedEdge, InvestigationStatus } from "@/api/types"
import { AttentionModel, type NodeMass } from "@/agm/attentionModel"
import { AttentionGraph } from "@/agm/attentionGraph"
import { InvestigationRegistry } from "@/agm/investigations"
import { buildTypedAdjacency, propagate, type TypedAdjacency } from "@/agm/propagation"
import { computeRoleWells, type Vec } from "@/agm/gravity"
import { syntheticRoleEntries } from "@/agm/synthetic"

interface AGMState {
  // --- engines (stable instances, not React state) ---
  model: AttentionModel
  graph: AttentionGraph
  investigations: InvestigationRegistry
  adjacency: TypedAdjacency | null
  roleWells: Map<string, Vec>

  // --- loaded topology ---
  systemModel: SystemModel | null
  roleByQname: Map<string, string>

  // --- derived snapshots (set by recompute, read by the canvas) ---
  massByQname: Map<string, NodeMass>
  propagated: Map<string, number>
  roleMass: Map<string, number>
  lastRecompute: number

  // --- actions ---
  setModel: (model: SystemModel, edges: TypedEdge[]) => void
  ingest: (qname: string, type: AttentionEventType, ts?: number) => void
  ingestTrace: (chain: string[], ts?: number) => void
  setInvestigation: (id: string, label: string, status?: InvestigationStatus) => void
  addNegativeEvidence: (qname: string, magnitude?: number, ts?: number) => void
  onRename: (from: string, to: string) => void
  onDelete: (qname: string) => void
  onCreate: (creator: string, created: string, ts?: number) => void
  recompute: (now?: number) => void
}

export const useAGMStore = create<AGMState>((set, get) => ({
  model: new AttentionModel(),
  graph: new AttentionGraph(),
  investigations: new InvestigationRegistry(),
  adjacency: null,
  roleWells: new Map(),

  systemModel: null,
  roleByQname: new Map(),

  massByQname: new Map(),
  propagated: new Map(),
  roleMass: new Map(),
  lastRecompute: 0,

  setModel: (systemModel, edges) => {
    const { model } = get()
    // Build role map from the model + synthetic nodes.
    const roleByQname = new Map<string, string>()
    for (const n of systemModel.nodes) roleByQname.set(n.qname, n.role || "untagged")
    for (const [q, r] of syntheticRoleEntries()) roleByQname.set(q, r)

    // Attention-preserving: keep the existing AttentionModel instance (its live
    // contributions survive a topology refresh). Re-point its role map and
    // re-seed historical mass from the new model. Renamed/deleted symbols are
    // handled via onRename/onDelete from edit events; here we just refresh roles
    // + historical seeds for everything currently present.
    model.setRoles(roleByQname)
    for (const n of systemModel.nodes) {
      const hist = (n as { historical_mass?: number }).historical_mass ?? 0
      if (hist > 0) model.seedHistorical(n.qname, hist)
    }

    const adjacency = buildTypedAdjacency(edges)
    const roles = [...new Set(roleByQname.values())]
    const roleWells = computeRoleWells(roles)

    set({ systemModel, roleByQname, adjacency, roleWells })
    get().recompute()
  },

  ingest: (qname, type, ts) => {
    get().model.ingest(qname, type, ts ?? Date.now() / 1000)
  },

  ingestTrace: (chain, ts) => {
    const now = ts ?? Date.now() / 1000
    const { graph, model } = get()
    graph.reinforceChain(chain, now)
    // a trace also commits attention to each node it visits
    for (const q of chain) model.ingest(q, "trace", now)
  },

  setInvestigation: (id, label, status) => {
    const { investigations, graph } = get()
    investigations.set({ id, label, status })
    if (!status || status === "active") graph.setInvestigation(id)
  },

  addNegativeEvidence: (qname, magnitude = 100, ts) => {
    const { model, investigations } = get()
    model.applyNegativeEvidence(qname, magnitude, ts ?? Date.now() / 1000)
    const active = investigations.active()
    if (active) investigations.addNegativeEvidence(active.id, qname)
  },

  onRename: (from, to) => get().model.rename(from, to),
  onDelete: (qname) => get().model.remove(qname),
  onCreate: (creator, created, ts) =>
    get().model.inheritFrom(creator, created, ts ?? Date.now() / 1000),

  recompute: (now) => {
    const ts = now ?? Date.now() / 1000
    const { model, adjacency, investigations } = get()
    model.prune(ts)
    const massByQname = model.snapshot(ts)
    const liveOnly = new Map<string, number>()
    for (const [q, m] of massByQname) liveOnly.set(q, m.live)
    const propagated = adjacency ? propagate(liveOnly, adjacency) : new Map<string, number>()
    const roleMass = new Map<string, number>()
    for (const [role, rm] of model.roleMass(ts)) roleMass.set(role, rm.display)
    investigations.updateActive(liveOnly)
    set({ massByQname, propagated, roleMass, lastRecompute: ts })
  },
}))
