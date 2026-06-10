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
export const R_MIN = 120 // hottest symbols orbit here — clearly OUTSIDE the
// crosshair so the centre reads as the attention origin, never occupied.
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

// Apparent-speed bounds (world px per frame, ~60fps). The CEILING stops a far
// target from lurching in one frame (a rapid grep/read burst can yank targets);
// the FLOOR stops an imperceptible crawl near the end (and lets the loop reach
// rest by snapping the last sub-floor gap). Tunable; chosen so motion reads as
// deliberate, never jittery and never glacial.
export const SPEED_FLOOR = 1.2 // px/frame — below this, snap to target
export const SPEED_CEIL = 12 // px/frame — calm, trackable motion (~0.8s to cross)

// Ease a current position toward a target. The step is the proportional
// `alpha * remaining`, then clamped to [SPEED_FLOOR, SPEED_CEIL] so observed
// motion stays in a comfortable band regardless of how far the target jumped.
// Returns the new position + remaining distance (Manhattan) for rest detection.
export function ease(
  cur: { x: number; y: number },
  target: { x: number; y: number },
  alpha = 0.16,
): { x: number; y: number; dist: number } {
  const dx = target.x - cur.x
  const dy = target.y - cur.y
  const gap = Math.hypot(dx, dy)
  if (gap === 0) return { x: cur.x, y: cur.y, dist: 0 }
  // gap already within the floor → snap home so we settle (no eternal crawl).
  if (gap <= SPEED_FLOOR) {
    return { x: target.x, y: target.y, dist: 0 }
  }
  // proportional step, clamped to the apparent-speed band.
  const step = Math.min(SPEED_CEIL, Math.max(SPEED_FLOOR, gap * alpha))
  const ux = dx / gap
  const uy = dy / gap
  const nx = cur.x + ux * step
  const ny = cur.y + uy * step
  return { x: nx, y: ny, dist: Math.abs(target.x - nx) + Math.abs(target.y - ny) }
}

// --- role clustering -------------------------------------------------------
//
// A role is not a rim label — it is an EMERGENT CLUSTER. When 2+ symbols of the
// same role have attention, they converge into a grouping. Each symbol's base
// polar placement (radius = relevance, angle = stable role bearing) is blended
// toward the role's cluster centroid so members tighten together, while the
// radius still encodes individual relevance. A pill tag is drawn at each
// active cluster (see roleClusters()).

export interface RoleCluster {
  role: string
  cx: number // centroid x
  cy: number // centroid y
  count: number // member count
  maxRadiusFromCentroid: number // for sizing the cluster halo / pill offset
}

// Pull each placement toward its role's centroid. The attraction strength is
// driven by HISTORICAL MASS: symbols that have historically mattered (in this
// role) cluster tighter, while a freshly-touched symbol with no history clusters
// loosely. `baseCohesion` is the floor (so a 2-member cluster still groups
// visibly); historical mass adds up to `histBoost` more. Cohesion stays < 1 so
// individual radius (live relevance) remains readable.
export function applyClusterCohesion(
  placements: PolarPlacement[],
  roleByQname: Map<string, string>,
  historicalByQname?: Map<string, number>,
  baseCohesion = 0.3,
  histBoost = 0.4,
): PolarPlacement[] {
  const clusters = computeRoleClusters(placements, roleByQname)
  for (const p of placements) {
    const role = roleByQname.get(p.qname) ?? "untagged"
    const c = clusters.get(role)
    if (!c || c.count < 2) continue // a lone symbol doesn't cluster
    const hist = historicalByQname?.get(p.qname) ?? 0
    const cohesion = baseCohesion + histBoost * Math.min(1, hist / 5)
    p.x = p.x + (c.cx - p.x) * cohesion
    p.y = p.y + (c.cy - p.y) * cohesion
  }
  return placements
}

// Visible budget: the canvas must stay readable no matter how many symbols are
// hot at once (a trace-heavy turn can light up 200+). Keep the top-`budget`
// symbols by display mass; the rest are folded into a peripheral "+N more"
// count per role so nothing is silently dropped but the field stays legible
// (PRD: 20–100 visible). Returns the kept placements + folded counts by role.
export interface BudgetResult {
  kept: PolarPlacement[]
  foldedByRole: Map<string, number>
  foldedTotal: number
}

export function applyVisibleBudget(
  placements: PolarPlacement[],
  massByQname: Map<string, number>,
  roleByQname: Map<string, string>,
  budget = 60,
  pinned?: Set<string>,
): BudgetResult {
  if (placements.length <= budget) {
    return { kept: placements, foldedByRole: new Map(), foldedTotal: 0 }
  }
  // PINNED (edited/patched) symbols are never folded — they always stay in view.
  const pinnedPlacements = pinned ? placements.filter((p) => pinned.has(p.qname)) : []
  const rest = pinned ? placements.filter((p) => !pinned.has(p.qname)) : placements
  // rank the rest by display mass desc (hottest kept); stable tiebreak by qname
  const ranked = [...rest].sort((a, b) => {
    const dm = (massByQname.get(b.qname) ?? 0) - (massByQname.get(a.qname) ?? 0)
    return dm !== 0 ? dm : a.qname < b.qname ? -1 : 1
  })
  const room = Math.max(0, budget - pinnedPlacements.length)
  const kept = [...pinnedPlacements, ...ranked.slice(0, room)]
  const folded = ranked.slice(room)
  const foldedByRole = new Map<string, number>()
  for (const p of folded) {
    const role = roleByQname.get(p.qname) ?? "untagged"
    foldedByRole.set(role, (foldedByRole.get(role) ?? 0) + 1)
  }
  return { kept, foldedByRole, foldedTotal: folded.length }
}

// Compute the centroid (+ spread) of each role's active members. Roles with a
// single member still get a cluster entry (count 1) so the caller can decide
// whether to render a pill (typically only count >= 2).
export function computeRoleClusters(
  placements: PolarPlacement[],
  roleByQname: Map<string, string>,
): Map<string, RoleCluster> {
  const acc = new Map<string, { sx: number; sy: number; n: number; pts: PolarPlacement[] }>()
  for (const p of placements) {
    const role = roleByQname.get(p.qname) ?? "untagged"
    let a = acc.get(role)
    if (!a) {
      a = { sx: 0, sy: 0, n: 0, pts: [] }
      acc.set(role, a)
    }
    a.sx += p.x
    a.sy += p.y
    a.n += 1
    a.pts.push(p)
  }
  const out = new Map<string, RoleCluster>()
  for (const [role, a] of acc) {
    const cx = a.sx / a.n
    const cy = a.sy / a.n
    let maxR = 0
    for (const p of a.pts) {
      const d = Math.hypot(p.x - cx, p.y - cy)
      if (d > maxR) maxR = d
    }
    out.set(role, { role, cx, cy, count: a.n, maxRadiusFromCentroid: maxR })
  }
  return out
}

// --- collision resolution (de-overlap) -------------------------------------
//
// Overlap is ILLEGAL — not "mostly resolved". A pill's final position is the
// closest non-overlapping point to its true polar target (radius=relevance,
// angle=role). Radius is the SOFT constraint that yields; overlap-free is the
// HARD invariant. The solver:
//   1. Each pass: push every overlapping pair apart by their full overlap, with
//      a TANGENTIAL bias (slide along the arc → preserve radius when possible).
//   2. After separating, pull each pill back toward its true target by the slack
//      that doesn't reintroduce an overlap (so it stays as close to ideal as it
//      legally can).
//   3. Repeat until a full pass finds ZERO overlaps (guaranteed termination: the
//      push step strictly increases pairwise separation for any overlapping pair;
//      a final hard cap + radial fan-out guarantees exit on pathological input).
//
// Result: deOverlap leaves NO overlaps. Tested as an invariant.

export interface Sized {
  qname: string
  x: number
  y: number
  // half-extents of the pill's footprint (world units), for overlap tests
  hw: number
  hh: number
}

// Overlap amount on each axis (positive = overlapping by that much).
function overlapXY(a: Sized, b: Sized, pad: number): { ox: number; oy: number } {
  return {
    ox: a.hw + b.hw + pad - Math.abs(a.x - b.x),
    oy: a.hh + b.hh + pad - Math.abs(a.y - b.y),
  }
}

// True iff the layout has zero overlapping pairs. Exported for tests/asserts.
export function hasNoOverlaps(nodes: Sized[], pad = 4): boolean {
  for (let i = 0; i < nodes.length; i++) {
    for (let j = i + 1; j < nodes.length; j++) {
      const { ox, oy } = overlapXY(nodes[i], nodes[j], pad)
      if (ox > 0 && oy > 0) return false
    }
  }
  return true
}

// Resolve ALL overlaps in place. Guarantees `hasNoOverlaps()` on return.
export function deOverlap(nodes: Sized[], opts: { pad?: number } = {}): Sized[] {
  const pad = opts.pad ?? 4
  if (nodes.length < 2) return nodes

  // true polar targets to pull back toward after separating.
  const tx = nodes.map((n) => n.x)
  const ty = nodes.map((n) => n.y)

  const MAX_PASSES = 400
  let pass = 0
  for (; pass < MAX_PASSES; pass++) {
    let anyOverlap = false
    for (let i = 0; i < nodes.length; i++) {
      for (let j = i + 1; j < nodes.length; j++) {
        const a = nodes[i]
        const b = nodes[j]
        const { ox, oy } = overlapXY(a, b, pad)
        if (ox <= 0 || oy <= 0) continue
        anyOverlap = true
        separate(a, b, ox, oy)
      }
    }
    // Pull each pill back toward its true target by whatever slack is legal.
    for (let i = 0; i < nodes.length; i++) pullBack(nodes, i, tx[i], ty[i], pad)
    if (!anyOverlap) break
  }

  // Pathological fallback: if we somehow hit the cap, fan remaining colliders
  // straight outward until clear (guarantees the invariant).
  if (pass >= MAX_PASSES) {
    for (let guard = 0; guard < 200 && !hasNoOverlaps(nodes, pad); guard++) {
      for (let i = 0; i < nodes.length; i++) {
        for (let j = i + 1; j < nodes.length; j++) {
          const a = nodes[i]
          const b = nodes[j]
          const { ox, oy } = overlapXY(a, b, pad)
          if (ox > 0 && oy > 0) fanOut(b, ox + oy)
        }
      }
    }
  }
  return nodes
}

// Push two overlapping pills fully apart along their centre-separation, biasing
// the displacement tangentially so radius is preserved where possible.
function separate(a: Sized, b: Sized, ox: number, oy: number) {
  let sx = a.x - b.x
  let sy = a.y - b.y
  let d = Math.hypot(sx, sy)
  if (d < 1e-6) {
    // exactly coincident → pick a deterministic tangential direction
    const r = Math.hypot(a.x, a.y) || 1e-6
    sx = -a.y / r
    sy = a.x / r
    d = 1
  } else {
    sx /= d
    sy /= d
  }
  // separate by the FULL smaller-axis overlap (each moves half) so the pair is
  // guaranteed clear after this push.
  const push = Math.min(ox, oy) / 2 + 0.5
  applyTangentialBias(a, sx, sy, push)
  applyTangentialBias(b, -sx, -sy, push)
}

// Move a node by `push` along (dx,dy) with the displacement rotated toward the
// tangent at its bearing (preserve radius) — but never reduce the push length,
// so separation is still guaranteed.
function applyTangentialBias(n: Sized, dx: number, dy: number, push: number) {
  const r = Math.hypot(n.x, n.y) || 1e-6
  const rx = n.x / r
  const ry = n.y / r
  const txx = -ry
  const tyy = rx
  const radial = dx * rx + dy * ry
  const tang = dx * txx + dy * tyy
  // blend toward tangent (0.8) but keep enough radial to honour the push sign
  let mx = (txx * tang * 0.8 + rx * radial * 0.2) * push
  let my = (tyy * tang * 0.8 + ry * radial * 0.2) * push
  // ensure the move is at least `push` long along the original direction so the
  // pair actually clears (tangential blend must not shrink separation).
  const mlen = Math.hypot(mx, my) || 1e-6
  if (mlen < push) {
    mx = (mx / mlen) * push
    my = (my / mlen) * push
  }
  n.x += mx
  n.y += my
}

// Pull node i toward its true target by the largest fraction that introduces no
// overlap with any other node — so it sits as close to ideal as legally possible.
function pullBack(nodes: Sized[], i: number, tgx: number, tgy: number, pad: number) {
  const n = nodes[i]
  const dx = tgx - n.x
  const dy = tgy - n.y
  if (dx === 0 && dy === 0) return
  // binary-search the largest step in [0,1] toward the target that stays clear.
  let lo = 0
  let hi = 1
  for (let k = 0; k < 12; k++) {
    const mid = (lo + hi) / 2
    const cx = n.x + dx * mid
    const cy = n.y + dy * mid
    if (clearAt(nodes, i, cx, cy, pad)) lo = mid
    else hi = mid
  }
  n.x += dx * lo
  n.y += dy * lo
}

function clearAt(nodes: Sized[], i: number, cx: number, cy: number, pad: number): boolean {
  const n = nodes[i]
  for (let j = 0; j < nodes.length; j++) {
    if (j === i) continue
    const o = nodes[j]
    const ox = n.hw + o.hw + pad - Math.abs(cx - o.x)
    const oy = n.hh + o.hh + pad - Math.abs(cy - o.y)
    if (ox > 0 && oy > 0) return false
  }
  return true
}

function fanOut(n: Sized, amount: number) {
  const r = Math.hypot(n.x, n.y) || 1e-6
  n.x += (n.x / r) * amount
  n.y += (n.y / r) * amount
}

// --- deterministic target spread (frame-stable, no twitch) -----------------
//
// `deOverlap` guarantees zero overlaps but its binary-search pull-back is
// sensitive to node order/positions, so running it on freshly-computed targets
// every frame yields slightly different results → the layout never settles
// ("twitching"). For the live canvas we instead spread overlapping TARGETS
// deterministically: nodes whose pills would collide are fanned apart along
// their shared bearing by angle, in a stable order (by qname). The same inputs
// always produce the same output, so once the active set + masses are steady the
// targets are fixed and nodes ease in and STOP.
//
// `widthOf(qname)` returns the pill's full width (caller measures text). Radius
// (relevance) is preserved exactly; only the angle is nudged.
export function spreadTargets(
  placements: PolarPlacement[],
  widthOf: (qname: string) => number,
  opts: { pad?: number; minAngleStep?: number } = {},
): void {
  const pad = opts.pad ?? 8
  if (placements.length < 2) return

  // Stable order: by radius (inner first) then qname. Deterministic each frame.
  const order = [...placements].sort(
    (a, b) => a.radius - b.radius || (a.qname < b.qname ? -1 : 1),
  )

  // Greedy: place each node; if it collides with an already-placed one, rotate
  // it around its radius until clear. Because order + geometry are deterministic,
  // the result is identical every frame.
  const placed: PolarPlacement[] = []
  for (const p of order) {
    const w = widthOf(p.qname)
    let angle = p.angle
    let tries = 0
    // angular step needed to clear a neighbour at this radius (chord ≈ r·dθ)
    const r = Math.max(1, p.radius)
    while (tries < 72) {
      const x = Math.cos(angle) * r
      const y = Math.sin(angle) * r
      let collides = false
      for (const q of placed) {
        const qw = widthOf(q.qname)
        const ox = w / 2 + qw / 2 + pad - Math.abs(x - q.x)
        const oy = 9 + 9 + pad - Math.abs(y - q.y)
        if (ox > 0 && oy > 0) {
          collides = true
          break
        }
      }
      if (!collides) {
        p.x = x
        p.y = y
        p.angle = angle
        break
      }
      // rotate by an arc-length step (alternating outward so we stay near base)
      const step = Math.max(opts.minAngleStep ?? 0.05, (w + pad) / r)
      angle += tries % 2 === 0 ? step * (tries + 1) : -step * (tries + 1)
      tries++
    }
    placed.push(p)
  }
}
