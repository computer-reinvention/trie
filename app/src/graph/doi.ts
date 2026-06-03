// Degree-of-Interest visible-set selection — the anti-overwhelm engine.
//
// The governing law: on-screen real-node count stays within `budget` at all
// times, at any zoom and any project size. DOI = salience - k*distance(focus)
// decides WHICH nodes survive; everything folded is represented by an openable
// aggregate ("+N"), never silently dropped.
//
// This module is pure (no React, no canvas) so it can be unit-tested headless.

import type { SystemModel, SystemModelNode, GroupingAxis } from "@/api/types"

export interface Adjacency {
  // undirected neighbours by qname (production subgraph)
  neighbours: Map<string, Set<string>>
}

// Build an undirected adjacency index from a flat edge list.
export function buildAdjacency(edges: Array<{ from: string; to: string }>): Adjacency {
  const neighbours = new Map<string, Set<string>>()
  const add = (a: string, b: string) => {
    let s = neighbours.get(a)
    if (!s) {
      s = new Set()
      neighbours.set(a, s)
    }
    s.add(b)
  }
  for (const e of edges) {
    add(e.from, e.to)
    add(e.to, e.from)
  }
  return { neighbours }
}

// Hop distance from a focus set via BFS, capped at maxHops (Infinity beyond).
export function hopDistances(
  adj: Adjacency,
  focus: Iterable<string>,
  maxHops: number,
): Map<string, number> {
  const dist = new Map<string, number>()
  const queue: string[] = []
  for (const f of focus) {
    if (!dist.has(f)) {
      dist.set(f, 0)
      queue.push(f)
    }
  }
  let head = 0
  while (head < queue.length) {
    const v = queue[head++]
    const d = dist.get(v)!
    if (d >= maxHops) continue
    const nbrs = adj.neighbours.get(v)
    if (!nbrs) continue
    for (const w of nbrs) {
      if (!dist.has(w)) {
        dist.set(w, d + 1)
        queue.push(w)
      }
    }
  }
  return dist
}

export interface AggregateBubble {
  // synthetic node id, e.g. "+agg:role:util" — distinct from real qnames
  id: string
  axis: GroupingAxis
  key: string // group key (role/subsystem) the folded nodes belong to
  count: number // how many real nodes folded here
  members: string[] // qnames folded (for expand-on-click)
}

export interface VisibleSet {
  nodes: SystemModelNode[] // real nodes to draw (<= budget)
  aggregates: AggregateBubble[] // "+N" placeholders for everything folded
}

export interface DoiParams {
  model: SystemModel
  budget: number
  salienceFloor: number
  axis: GroupingAxis
  // focus qnames (selection + agent location); empty = whole-system view
  focus: string[]
  adjacency: Adjacency
  // distance penalty per hop applied to DOI
  distancePenalty?: number
  // restrict the candidate pool to nodes in these group keys (on `axis`).
  // Used when a component is expanded (L1): only its members are eligible.
  restrictToGroups?: Set<string>
}

const groupKeyOf = (n: SystemModelNode, axis: GroupingAxis): string =>
  axis === "role" ? n.role || "untagged" : n.subsystem

// Select the bounded visible node set + aggregates for everything folded.
//
// DOI(n) = salience(n) - penalty * hopDistance(n, focus).
// With no focus, DOI == salience (the whole-system "what matters" view).
// Nodes below salienceFloor AND not pulled in by focus proximity are folded.
export function selectVisible(params: DoiParams): VisibleSet {
  const { model, budget, axis, focus, adjacency, restrictToGroups } = params
  const penalty = params.distancePenalty ?? 0.25
  // When restricted to a drilled component, drop the salience floor so all its
  // members are eligible (the budget still caps them; the rest fold to "+N").
  const salienceFloor = restrictToGroups ? 0 : params.salienceFloor

  let prod = model.nodes.filter((n) => !n.is_test)
  if (restrictToGroups) {
    prod = prod.filter((n) => restrictToGroups.has(groupKeyOf(n, axis)))
  }

  // distances from focus (cap at 4 hops; beyond is effectively "far")
  const dist = focus.length ? hopDistances(adjacency, focus, 4) : new Map<string, number>()

  const doi = new Map<string, number>()
  for (const n of prod) {
    const d = dist.get(n.qname)
    const distTerm = d === undefined ? (focus.length ? 1.0 : 0) : penalty * d
    doi.set(n.qname, n.salience - distTerm)
  }

  // Candidate set: focused nodes always qualify; otherwise must clear the floor.
  const focusSet = new Set(focus)
  const eligible = prod.filter(
    (n) => focusSet.has(n.qname) || dist.has(n.qname) || n.salience >= salienceFloor,
  )

  // Rank by DOI desc, take up to budget.
  eligible.sort((a, b) => (doi.get(b.qname)! - doi.get(a.qname)!) || (b.salience - a.salience))
  const shown = eligible.slice(0, budget)
  const shownIds = new Set(shown.map((n) => n.qname))

  // Everything not shown folds into per-group aggregates.
  const folded = new Map<string, string[]>()
  for (const n of prod) {
    if (shownIds.has(n.qname)) continue
    const key = groupKeyOf(n, axis)
    const arr = folded.get(key)
    if (arr) arr.push(n.qname)
    else folded.set(key, [n.qname])
  }
  const aggregates: AggregateBubble[] = [...folded.entries()]
    .filter(([, members]) => members.length > 0)
    .map(([key, members]) => ({
      id: `+agg:${axis}:${key}`,
      axis,
      key,
      count: members.length,
      members,
    }))

  return { nodes: shown, aggregates }
}

// L0 component view: one synthetic node per group on the chosen axis, plus the
// thresholded group->group flows. This is the opening frame (~11-26 nodes).
export interface ComponentView {
  groups: Array<{ key: string; count: number; doorCount: number; hubCount: number }>
  flows: Array<{ source: string; target: string; weight: number }>
}

export function componentView(model: SystemModel, axis: GroupingAxis): ComponentView {
  const a = model.axes[axis]
  return {
    groups: a.groups.map((g) => ({
      key: g.key,
      count: g.count,
      doorCount: g.door_count,
      hubCount: g.hub_count,
    })),
    flows: a.flows.map((f) => ({ source: f.source, target: f.target, weight: f.weight })),
  }
}
