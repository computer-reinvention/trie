// AGM polar layout — the cognitive-state projection.
//
// This is NOT a graph layout. The canvas centre is a FIXED crosshair: the
// "current attention origin" (0,0). The world deforms around it; the camera
// never moves. Two independent encodings:
//
//   radius  = f(live mass)      — near centre = hot NOW, far = cold/peripheral
//   angle   = f(historical mass + role) — STABLE geography (a symbol keeps its
//             bearing across frames; Auth always sits in roughly one direction)
//
// Consequences the renderer relies on:
//   - High live mass pulls a symbol toward the centre.
//   - As attention cools, the symbol drifts OUTWARD — it never disappears
//     mid-investigation, it just becomes peripheral.
//   - A newly-discovered symbol (no live mass yet) starts at the perimeter and
//     moves inward as attention lands → "new lead entered from outside".
//   - Angle is anchored to the symbol's role + a stable per-symbol jitter
//     derived from its qname, so geography is learnable and doesn't reshuffle.
//
// Pure math. Fully unit-tested — numbers prove correctness before pixels do.

// Radius bounds in world units. The centre is reserved (nothing sits exactly at
// 0); the perimeter is where cold/new symbols live.
export const R_MIN = 60 // hottest symbols orbit here (never the exact centre)
export const R_MAX = 620 // perimeter — cold / newly-discovered symbols

// Map a display mass (already log-compressed) to a radius. Higher mass → smaller
// radius (closer to centre). `maxDisplay` normalises against the current hottest
// symbol so the most-relevant symbol always sits near R_MIN regardless of scale.
export function radiusForMass(displayMass: number, maxDisplay: number): number {
  if (maxDisplay <= 0 || displayMass <= 0) return R_MAX
  const rel = Math.min(1, displayMass / maxDisplay) // 0..1, 1 = hottest
  return R_MAX - (R_MAX - R_MIN) * rel
}

// Deterministic angle (radians) for a role: each role owns a stable bearing on
// the circle, ordered by name so the same project yields the same geography.
export function roleBaseAngle(role: string, roles: string[]): number {
  const sorted = [...new Set(roles)].sort()
  const i = Math.max(0, sorted.indexOf(role))
  const n = Math.max(1, sorted.length)
  return (2 * Math.PI * i) / n - Math.PI / 2
}

// A small, stable per-symbol angular offset within its role's arc, derived from
// the qname hash + historical mass. Historical mass nudges the bearing so a
// symbol that has historically mattered keeps a consistent, slightly distinct
// position (stable orientation), while live mass (radius) changes freely.
export function symbolAngle(
  qname: string,
  role: string,
  roles: string[],
  historicalMass: number,
  arc = 0.9, // radians of spread allotted per role
): number {
  const base = roleBaseAngle(role, roles)
  // hash the qname to a stable [0,1)
  let h = 0
  for (let i = 0; i < qname.length; i++) h = (h * 31 + qname.charCodeAt(i)) >>> 0
  const jitter = (h % 1000) / 1000 // 0..1
  // historical mass shifts the symbol toward the role's "core" bearing (centre
  // of the arc) — historically important symbols cluster tighter angularly.
  const histPull = Math.min(1, historicalMass / 5) // 0..1
  const spread = (jitter - 0.5) * arc * (1 - 0.5 * histPull)
  return base + spread
}

export interface PolarPlacement {
  qname: string
  x: number
  y: number
  radius: number
  angle: number
}

// Compute the polar target position for one symbol. The renderer eases the
// drawn position toward this target (calm motion); this function is the pure
// source of truth for "where should this symbol be right now".
export function placeSymbol(args: {
  qname: string
  role: string
  roles: string[]
  displayMass: number
  maxDisplay: number
  historicalMass: number
}): PolarPlacement {
  const angle = symbolAngle(args.qname, args.role, args.roles, args.historicalMass)
  const radius = radiusForMass(args.displayMass, args.maxDisplay)
  return {
    qname: args.qname,
    x: Math.cos(angle) * radius,
    y: Math.sin(angle) * radius,
    radius,
    angle,
  }
}

// Ease a current position toward a target by `alpha`. Returns the new position +
// the remaining distance (so the loop can stop when everything has settled).
export function ease(
  cur: { x: number; y: number },
  target: { x: number; y: number },
  alpha = 0.16,
): { x: number; y: number; dist: number } {
  const dx = target.x - cur.x
  const dy = target.y - cur.y
  return { x: cur.x + dx * alpha, y: cur.y + dy * alpha, dist: Math.abs(dx) + Math.abs(dy) }
}
