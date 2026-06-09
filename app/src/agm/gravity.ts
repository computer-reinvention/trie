// Gravity layout — the AGM force integrator.
//
// NOT a perpetual simulation: it settles to rest and only re-energises when
// attention actually changes (the renderer kicks it on ingest). Roles are FIXED
// geography (deterministic wells, computed once from the system model); symbols
// are pulled toward their role well + the attention they carry + their active
// investigation's cluster, and repel each other to stay readable.
//
// Pure math; no React/canvas. The renderer owns the rAF loop and decides when to
// run `step` (while not at rest) and when to stop.

export interface Vec {
  x: number
  y: number
}

export interface Body {
  qname: string
  role: string
  pos: Vec
  vel: Vec
  mass: number // display mass — scales attention pull + repulsion radius
  pinned: boolean // role wells are pinned (fixed geography)
}

export interface GravityConfig {
  rolePull: number // toward the symbol's role well (geography)
  attentionPull: number // toward the attention centroid, scaled by own mass
  clusterPull: number // toward the active investigation's cluster centroid
  repulsion: number // pairwise repulsion strength
  damping: number // velocity damping per step (settles to rest)
  restThreshold: number // total kinetic energy below which we consider it at rest
}

export const DEFAULT_GRAVITY: GravityConfig = {
  rolePull: 0.04,
  attentionPull: 0.06,
  clusterPull: 0.05,
  repulsion: 1200,
  damping: 0.82,
  restThreshold: 1e-2,
}

// Deterministic fixed role wells laid out on a circle, ordered by role name so
// the same project always yields the same geography (stable, learnable). Roles
// never move. Returns role → well position.
export function computeRoleWells(roles: string[], radius = 600): Map<string, Vec> {
  const sorted = [...new Set(roles)].sort()
  const wells = new Map<string, Vec>()
  const n = Math.max(1, sorted.length)
  sorted.forEach((role, i) => {
    const angle = (2 * Math.PI * i) / n - Math.PI / 2
    wells.set(role, { x: Math.cos(angle) * radius, y: Math.sin(angle) * radius })
  })
  return wells
}

// One integration step. Mutates `bodies` in place; returns the total kinetic
// energy so the caller can stop when the system is at rest.
export function step(
  bodies: Body[],
  wells: Map<string, Vec>,
  clusterCentroid: Vec | null,
  clusterMembers: Set<string>,
  cfg: GravityConfig = DEFAULT_GRAVITY,
): number {
  // Attention centroid: mass-weighted mean position (pull target for hot nodes).
  const centroid = attentionCentroid(bodies)

  for (const b of bodies) {
    if (b.pinned) continue
    let fx = 0
    let fy = 0

    // Role gravity → toward fixed well (geography).
    const well = wells.get(b.role)
    if (well) {
      fx += (well.x - b.pos.x) * cfg.rolePull
      fy += (well.y - b.pos.y) * cfg.rolePull
    }

    // Attention gravity → hot nodes drift toward the attention centroid.
    if (centroid && b.mass > 0) {
      const w = cfg.attentionPull * b.mass
      fx += (centroid.x - b.pos.x) * w
      fy += (centroid.y - b.pos.y) * w
    }

    // Investigation clustering → members tighten toward the cluster centroid,
    // scaled by confidence by the caller (encoded in clusterPull magnitude).
    if (clusterCentroid && clusterMembers.has(b.qname)) {
      fx += (clusterCentroid.x - b.pos.x) * cfg.clusterPull
      fy += (clusterCentroid.y - b.pos.y) * cfg.clusterPull
    }

    // Pairwise repulsion (readability). O(n^2) — fine for the AGM visible set
    // (tens of nodes, never the whole repo).
    for (const o of bodies) {
      if (o === b) continue
      const dx = b.pos.x - o.pos.x
      const dy = b.pos.y - o.pos.y
      const d2 = dx * dx + dy * dy + 0.01
      const f = cfg.repulsion / d2
      fx += (dx / Math.sqrt(d2)) * f
      fy += (dy / Math.sqrt(d2)) * f
    }

    b.vel.x = (b.vel.x + fx) * cfg.damping
    b.vel.y = (b.vel.y + fy) * cfg.damping
  }

  // Integrate + accumulate kinetic energy.
  let energy = 0
  for (const b of bodies) {
    if (b.pinned) continue
    b.pos.x += b.vel.x
    b.pos.y += b.vel.y
    energy += b.vel.x * b.vel.x + b.vel.y * b.vel.y
  }
  return energy
}

export function attentionCentroid(bodies: Body[]): Vec | null {
  let sx = 0
  let sy = 0
  let sm = 0
  for (const b of bodies) {
    if (b.mass <= 0) continue
    sx += b.pos.x * b.mass
    sy += b.pos.y * b.mass
    sm += b.mass
  }
  if (sm <= 0) return null
  return { x: sx / sm, y: sy / sm }
}

export function clusterCentroidOf(bodies: Body[], members: Set<string>): Vec | null {
  let sx = 0
  let sy = 0
  let n = 0
  for (const b of bodies) {
    if (!members.has(b.qname)) continue
    sx += b.pos.x
    sy += b.pos.y
    n++
  }
  if (n === 0) return null
  return { x: sx / n, y: sy / n }
}
