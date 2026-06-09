// AGM layout — deterministic, attention-driven placement (NOT a force sim).
//
// The PRD rejects the force-directed "graph" look. Symbols are not physics
// bodies bouncing off each other; they appear when attention reaches them and
// settle into a calm arrangement around their role. Layout is computed
// deterministically each frame from the current attention field, and bodies ease
// toward their target positions (smooth motion, never jitter, settles to rest).
//
// Geography: role wells sit at fixed deterministic positions (stable/learnable).
// Within a role, its active symbols are arranged on concentric rings — hotter
// symbols pulled toward the well centre (convergence reads as "tightening").

export interface Vec {
  x: number
  y: number
}

export interface Body {
  qname: string
  role: string
  pos: Vec // current (eased) position
  target: Vec // computed target this frame
  mass: number // display mass
}

// Fixed role wells on a circle, ordered by role name — same project, same map.
export function computeRoleWells(roles: string[], radius = 520): Map<string, Vec> {
  const sorted = [...new Set(roles)].sort()
  const wells = new Map<string, Vec>()
  const n = Math.max(1, sorted.length)
  sorted.forEach((role, i) => {
    const angle = (2 * Math.PI * i) / n - Math.PI / 2
    wells.set(role, { x: Math.cos(angle) * radius, y: Math.sin(angle) * radius })
  })
  return wells
}

// Compute target positions for the currently-active bodies, grouped by role and
// arranged around each role's well. Hotter symbols orbit closer to the centre.
// Deterministic: ordering within a role is by qname so positions are stable.
export function computeTargets(
  bodies: Body[],
  wells: Map<string, Vec>,
  maxMass: number,
): void {
  // group active bodies by role
  const byRole = new Map<string, Body[]>()
  for (const b of bodies) {
    if (b.mass <= 0) continue
    let g = byRole.get(b.role)
    if (!g) {
      g = []
      byRole.set(b.role, g)
    }
    g.push(b)
  }

  for (const [role, members] of byRole) {
    const well = wells.get(role) ?? { x: 0, y: 0 }
    // stable order within the role
    members.sort((a, b) => (a.qname < b.qname ? -1 : 1))
    const count = members.length
    members.forEach((b, i) => {
      // hotter → smaller orbit radius (pulled toward the well centre).
      const heat = maxMass > 0 ? Math.min(1, b.mass / maxMass) : 0
      const orbit = 18 + (1 - heat) * 70 // 18 (hot, near centre) .. 88 (cold, rim)
      // spread members around the ring; offset by index for separation.
      const angle = count > 1 ? (2 * Math.PI * i) / count : -Math.PI / 2
      b.target = {
        x: well.x + Math.cos(angle) * orbit,
        y: well.y + Math.sin(angle) * orbit,
      }
    })
  }
}

// Ease every body toward its target. Returns total remaining motion so the
// caller can stop the loop once settled. Cold bodies (mass 0) are not eased
// (they aren't drawn); they snap-reset near their well for next activation.
export function easeToTargets(bodies: Body[], wells: Map<string, Vec>, alpha = 0.18): number {
  let motion = 0
  for (const b of bodies) {
    if (b.mass <= 0) {
      // park near the well so it emerges from the right place when it heats up
      const well = wells.get(b.role) ?? { x: 0, y: 0 }
      b.pos.x = well.x
      b.pos.y = well.y
      continue
    }
    const dx = b.target.x - b.pos.x
    const dy = b.target.y - b.pos.y
    b.pos.x += dx * alpha
    b.pos.y += dy * alpha
    motion += Math.abs(dx) + Math.abs(dy)
  }
  return motion
}
