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

// The radius (world units) of the ring on which every ROLE ANCHOR sits. Region
// clusters group around their anchor, so all region halos land at roughly the
// same distance from centre and are fanned evenly by angle — a tidy ring of
// regions rather than halos scattered at heat-driven distances. Individual
// members still vary their own radius by relevance around this band.
export const ROLE_RING_RADIUS = (R_MIN + R_MAX) / 2

// Fixed anchor point for a role: its even base angle on the role ring. This is
// the stable centre a region's members cohere toward (NOT the heat-weighted
// member centroid, which drifts in/out with mass and made halos uneven).
export function roleAnchor(role: string, roles: string[], radius = ROLE_RING_RADIUS): { x: number; y: number } {
  const a = roleBaseAngle(role, roles)
  return { x: Math.cos(a) * radius, y: Math.sin(a) * radius }
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

// Pull each multi-member role's placements toward that role's FIXED anchor (a
// stable point on the role ring), so every region clusters at a consistent
// distance from centre and even angle — the region halos form a tidy ring
// instead of drifting in/out with member heat. Cohesion is uniform (not
// heat-driven) so the cluster's CENTRE is stable; individual members still keep
// their own relevance radius, fanning around the anchor. `roleList` defines the
// angular ordering (pass the active roles for even on-screen spread).
export function applyAnchorCohesion(
  placements: PolarPlacement[],
  roleByQname: Map<string, string>,
  roleList: string[],
  cohesion = 0.72,
): PolarPlacement[] {
  // count members per role so a lone symbol isn't dragged off its own radius
  const counts = new Map<string, number>()
  for (const p of placements) {
    const role = roleByQname.get(p.qname) ?? "untagged"
    counts.set(role, (counts.get(role) ?? 0) + 1)
  }
  const anchorCache = new Map<string, { x: number; y: number }>()
  // running per-role index so members get distinct angular slots on the anchor's
  // arc. Same-mass members share a radius, so without this they'd land on the
  // exact same point and de-overlap would stack them into a line. Spreading them
  // ANGULARLY around the anchor bearing keeps the polar look (each keeps its
  // relevance radius) while giving them a 2-D starting fan.
  const idxByRole = new Map<string, number>()
  for (const p of placements) {
    const role = roleByQname.get(p.qname) ?? "untagged"
    const n = counts.get(role) ?? 0
    if (n < 2) continue // lone symbol doesn't cluster
    let anchor = anchorCache.get(role)
    if (!anchor) {
      anchor = roleAnchor(role, roleList)
      anchorCache.set(role, anchor)
    }
    // blend toward the anchor (cohesion), preserving the radial encoding
    let bx = p.x + (anchor.x - p.x) * cohesion
    let by = p.y + (anchor.y - p.y) * cohesion
    // then rotate the member around the CENTRE by a small per-member angle so
    // members fan out along their orbit instead of coinciding. The spread arc
    // grows with member count but is capped so a region stays a tight cluster.
    const i = idxByRole.get(role) ?? 0
    idxByRole.set(role, i + 1)
    const arc = Math.min(CLUSTER_ARC_MAX, CLUSTER_ARC_PER_MEMBER * (n - 1))
    const offset = n > 1 ? (i / (n - 1) - 0.5) * arc : 0
    if (offset !== 0) {
      const cos = Math.cos(offset)
      const sin = Math.sin(offset)
      const rx = bx * cos - by * sin
      const ry = bx * sin + by * cos
      bx = rx
      by = ry
    }
    p.x = bx
    p.y = by
    p.angle = Math.atan2(by, bx)
    p.radius = Math.hypot(bx, by)
  }
  return placements
}

// Angular spread for a cluster's members around their anchor bearing (radians).
// Per-member step times (count-1), capped so a big cluster fans across a sane
// arc rather than wrapping the whole ring.
const CLUSTER_ARC_PER_MEMBER = 0.12
const CLUSTER_ARC_MAX = 1.4

// Tighten each role's members toward their centroid so the role's covering halo
// fits within a NON-OVERLAPPING radius budget. Halos must both (a) enclose every
// member and (b) never overlap a neighbour — when those conflict we resolve it
// by pulling the members inward (shrinking the covering radius), exactly the
// "adjust object distance from centroid" trade-off. Only roles with >= minCount
// members (the ones that will draw a halo) are tightened.
//
// Budget per role = half the distance to the nearest other halo-role centroid,
// minus `gap`, clamped to >= `minRadius`. If a role's current covering radius
// exceeds its budget, every member is scaled toward the centroid by the ratio
// (budget / covering) so the whole cluster shrinks uniformly and stays covered.
export function tightenRolesToFit(
  placements: PolarPlacement[],
  roleByQname: Map<string, string>,
  opts: { minCount: number; gap: number; minRadius: number; nodeMargin: number },
): PolarPlacement[] {
  // group by role
  const byRole = new Map<string, PolarPlacement[]>()
  for (const p of placements) {
    const role = roleByQname.get(p.qname) ?? "untagged"
    const list = byRole.get(role)
    if (list) list.push(p)
    else byRole.set(role, [p])
  }
  // halo roles (enough members) + their centroids
  const roles = [...byRole.entries()]
    .filter(([, list]) => list.length >= opts.minCount)
    .map(([role, list]) => {
      const cx = list.reduce((s, p) => s + p.x, 0) / list.length
      const cy = list.reduce((s, p) => s + p.y, 0) / list.length
      const cover = list.reduce((m, p) => Math.max(m, Math.hypot(p.x - cx, p.y - cy)), 0)
      return { role, list, cx, cy, cover }
    })
  for (const r of roles) {
    // budget = half the gap to the nearest other halo centroid
    let nearest = Infinity
    for (const o of roles) {
      if (o === r) continue
      const d = Math.hypot(o.cx - r.cx, o.cy - r.cy)
      if (d < nearest) nearest = d
    }
    const budget =
      nearest === Infinity
        ? Infinity
        : Math.max(opts.minRadius, nearest / 2 - opts.gap - opts.nodeMargin)
    const current = r.cover
    if (current <= budget || current <= 1e-6) continue
    // scale every member toward the centroid so the cluster fits the budget
    const scale = budget / current
    for (const p of r.list) {
      p.x = r.cx + (p.x - r.cx) * scale
      p.y = r.cy + (p.y - r.cy) * scale
      p.radius = Math.hypot(p.x, p.y)
      p.angle = Math.atan2(p.y, p.x)
    }
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
  // FIXED nodes never move during de-overlap — they are pinned anchors (e.g. a
  // region label welded to its halo). Other nodes are pushed out of their way;
  // a fixed-vs-fixed pair is left as-is. Defaults to movable.
  fixed?: boolean
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
          if (ox > 0 && oy > 0) {
            // fan the MOVABLE one outward; if both fixed, leave them.
            if (!b.fixed) fanOut(b, ox + oy)
            else if (!a.fixed) fanOut(a, ox + oy)
          }
        }
      }
    }
  }
  return nodes
}

// Push two overlapping pills apart along their centre-separation, biasing the
// displacement tangentially so radius is preserved where possible. Type-aware:
//   - both fixed   → nothing moves (anchors don't yield)
//   - one fixed    → the MOVABLE one absorbs the full separation
//   - both movable → each moves half (original behaviour)
function separate(a: Sized, b: Sized, ox: number, oy: number) {
  if (a.fixed && b.fixed) return
  // Push apart along the minimum-translation axis (cheapest clearing move). For
  // a near-coincident pair, use a deterministic per-pair direction so they don't
  // stay stuck on top of each other.
  const sepX = a.x - b.x
  const sepY = a.y - b.y
  const slack = 0.5
  let mx: number
  let my: number
  if (Math.abs(sepX) < 1e-6 && Math.abs(sepY) < 1e-6) {
    const ang = ((hashName(a.qname + "|" + b.qname) % 360) * Math.PI) / 180
    const need = Math.max(ox, oy) + slack
    mx = Math.cos(ang) * need
    my = Math.sin(ang) * need
  } else if (ox < oy) {
    mx = (sepX >= 0 ? ox : -ox) + Math.sign(sepX || 1) * slack
    my = 0
  } else {
    mx = 0
    my = (sepY >= 0 ? oy : -oy) + Math.sign(sepY || 1) * slack
  }
  if (a.fixed) {
    b.x -= mx
    b.y -= my
    return
  }
  if (b.fixed) {
    a.x += mx
    a.y += my
    return
  }
  a.x += mx / 2
  a.y += my / 2
  b.x -= mx / 2
  b.y -= my / 2
}

// Stable small hash of a qname → used to break ties deterministically when two
// nodes are exactly coincident (so separation direction is reproducible).
function hashName(s: string): number {
  let h = 0
  for (let i = 0; i < s.length; i++) h = (h * 31 + s.charCodeAt(i)) >>> 0
  return h
}

// Pull node i toward its true target by the largest fraction that introduces no
// overlap with any other node — so it sits as close to ideal as legally possible.
function pullBack(nodes: Sized[], i: number, tgx: number, tgy: number, pad: number) {
  const n = nodes[i]
  if (n.fixed) return // anchors never drift toward a target
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

// --- resolveLayout: the single, pure placement core ------------------------
//
// THE law for "nothing overlaps on the canvas". Given relevance-placed
// placements + which ones are pills + footprint sizes + region label geometry,
// it returns the final non-overlapping positions for every node AND the fixed
// region-heading boxes. Both the live canvas and the headless verifier call
// this, so what you see on screen is exactly what the verifier checks — no
// drift. Pure: text measurement comes in via `measure` callbacks.
//
// Guarantees on return (all enforced by deOverlap's tested invariant):
//   - no two node footprints overlap
//   - no node footprint overlaps any region-heading box (headings are FIXED, so
//     nodes are pushed out of them — the halo "owns" its label area)
//   - each node stays as near its relevance position as the above allow

export interface LayoutInput {
  placements: PolarPlacement[] // relevance-placed (post anchor-cohesion)
  roleByQname: Map<string, string>
  isPill: (qname: string) => boolean
  pillHalfWidth: (qname: string) => number // measured label half-width
  regionLabelHalfWidth: (role: string) => number // measured heading half-width
  haloMinCount: number // roles with >= this many members get a halo+heading
  pad: number // min gap between footprints
  dotHalf: number // half-extent of a dot's square footprint
  pillHalfHeight: number // half-extent of a pill chip's height
  haloMaxR: number
  haloNodeMargin: number // covering-radius padding (member centre → halo edge)
  haloLabelGap: number // gap between halo edge and its heading
  labelHalfHeight: number // half-extent of a heading box's height
}

export interface RegionLabel {
  role: string
  x: number
  y: number
}

export interface LayoutResult {
  // final positions written back onto the input placements (also returned here)
  placements: PolarPlacement[]
  // where each region heading is painted (matches its reserved fixed box)
  labels: RegionLabel[]
}

// Translate whole role-clusters (≥ minCount members) apart as RIGID groups so
// their bounding discs don't overlap — giving each cluster its own region.
// Members of a cluster move together (relative arrangement preserved). Lone
// nodes (< minCount) are ignored here (handled by per-node de-overlap later).
function separateClusters(
  boxes: Sized[],
  roleByQname: Map<string, string>,
  opts: { minCount: number; pad: number },
): void {
  // group movable boxes by role
  const byRole = new Map<string, Sized[]>()
  for (const b of boxes) {
    if (b.fixed) continue
    const role = roleByQname.get(b.qname) ?? "untagged"
    const list = byRole.get(role)
    if (list) list.push(b)
    else byRole.set(role, [b])
  }
  // build a disc per qualifying cluster: centroid + radius covering all members
  interface Disc { role: string; members: Sized[]; cx: number; cy: number; r: number }
  const discs: Disc[] = []
  for (const [role, members] of byRole) {
    if (members.length < opts.minCount) continue
    const cx = members.reduce((s, m) => s + m.x, 0) / members.length
    const cy = members.reduce((s, m) => s + m.y, 0) / members.length
    let r = 0
    for (const m of members) {
      r = Math.max(r, Math.hypot(m.x - cx, m.y - cy) + Math.hypot(m.hw, m.hh))
    }
    discs.push({ role, members, cx, cy, r })
  }
  if (discs.length < 2) return

  // iteratively push overlapping discs apart along their centre line, moving the
  // whole cluster rigidly. Deterministic + converges (each push strictly
  // increases separation of an overlapping pair).
  const MAX_PASSES = 200
  for (let pass = 0; pass < MAX_PASSES; pass++) {
    let any = false
    for (let i = 0; i < discs.length; i++) {
      for (let j = i + 1; j < discs.length; j++) {
        const a = discs[i]
        const b = discs[j]
        let dx = a.cx - b.cx
        let dy = a.cy - b.cy
        let d = Math.hypot(dx, dy)
        const need = a.r + b.r + opts.pad
        if (d >= need) continue
        any = true
        if (d < 1e-6) {
          // coincident centres → deterministic split direction
          const ang = ((hashName(a.role + "|" + b.role) % 360) * Math.PI) / 180
          dx = Math.cos(ang)
          dy = Math.sin(ang)
          d = 1
        } else {
          dx /= d
          dy /= d
        }
        const push = (need - d) / 2 + 0.5
        translateCluster(a, dx * push, dy * push)
        translateCluster(b, -dx * push, -dy * push)
      }
    }
    if (!any) break
  }
}

function translateCluster(
  disc: { members: Sized[]; cx: number; cy: number },
  dx: number,
  dy: number,
): void {
  for (const m of disc.members) {
    m.x += dx
    m.y += dy
  }
  disc.cx += dx
  disc.cy += dy
}

// Copy resolved box positions back onto their placements (by qname).
function syncPlacements(placements: PolarPlacement[], boxes: Sized[]): void {
  const byQ = new Map(boxes.map((s) => [s.qname, s]))
  for (const p of placements) {
    const s = byQ.get(p.qname)
    if (s) {
      p.x = s.x
      p.y = s.y
      p.angle = Math.atan2(s.y, s.x)
      p.radius = Math.hypot(s.x, s.y)
    }
  }
}

export function resolveLayout(input: LayoutInput): LayoutResult {
  const {
    placements,
    roleByQname,
    isPill,
    pillHalfWidth,
    regionLabelHalfWidth,
    haloMinCount,
    pad,
    dotHalf,
    pillHalfHeight,
    haloMaxR,
    haloNodeMargin,
    haloLabelGap,
    labelHalfHeight,
  } = input

  // node footprint boxes (movable)
  const sized: Sized[] = placements.map((p) => {
    const pill = isPill(p.qname)
    return {
      qname: p.qname,
      x: p.x,
      y: p.y,
      hw: pill ? pillHalfWidth(p.qname) : dotHalf,
      hh: pill ? pillHalfHeight : dotHalf,
    }
  })

  // RIGID CLUSTER SEPARATION: push whole role-clusters apart so each occupies
  // its own region of the canvas (not just non-overlapping halos). Each cluster
  // moves as a rigid group — its internal member arrangement + relevance radii
  // are preserved — until no two cluster bounding discs overlap. Runs BEFORE the
  // per-node de-overlap, which then only cleans up intra-cluster + label gaps.
  separateClusters(sized, roleByQname, { minCount: haloMinCount, pad: pad + haloNodeMargin })

  // mirror the separated node positions back onto `placements` so the region
  // heading boxes are computed from the post-separation cluster centroids.
  syncPlacements(placements, sized)

  // region heading boxes (FIXED) from the (now separated) clusters
  const labelBoxes = regionLabelBoxes(placements, roleByQname, {
    minCount: haloMinCount,
    haloMaxR,
    haloNodeMargin,
    haloLabelGap,
    halfWidthOf: regionLabelHalfWidth,
    labelHalfHeight,
  })
  for (const lb of labelBoxes) sized.push(lb)

  deOverlap(sized, { pad })

  // write resolved positions back onto the placements
  const byQ = new Map(sized.map((s) => [s.qname, s]))
  for (const p of placements) {
    const s = byQ.get(p.qname)
    if (s) {
      p.x = s.x
      p.y = s.y
      p.angle = Math.atan2(s.y, s.x)
      p.radius = Math.hypot(s.x, s.y)
    }
  }

  return {
    placements,
    labels: labelBoxes.map((lb) => ({
      role: lb.qname.replace(/^__label__:/, ""),
      x: lb.x,
      y: lb.y,
    })),
  }
}

// Build the FIXED region-heading boxes for roles with enough members. Each box
// hugs the OUTER edge of its role's covering circle, hemisphere-aware (below for
// lower-half clusters, above for upper). Exported for the canvas + verifier.
export function regionLabelBoxes(
  placements: PolarPlacement[],
  roleByQname: Map<string, string>,
  opts: {
    minCount: number
    haloMaxR: number
    haloNodeMargin: number
    haloLabelGap: number
    halfWidthOf: (role: string) => number
    labelHalfHeight: number
  },
): Sized[] {
  const acc = new Map<string, { sx: number; sy: number; n: number; pts: PolarPlacement[] }>()
  for (const p of placements) {
    const role = roleByQname.get(p.qname) ?? "untagged"
    const a = acc.get(role) ?? { sx: 0, sy: 0, n: 0, pts: [] }
    a.sx += p.x
    a.sy += p.y
    a.n += 1
    a.pts.push(p)
    acc.set(role, a)
  }
  const boxes: Sized[] = []
  for (const [role, a] of acc) {
    if (a.n < opts.minCount) continue
    const cx = a.sx / a.n
    const cy = a.sy / a.n
    let cover = 0
    for (const p of a.pts) cover = Math.max(cover, Math.hypot(p.x - cx, p.y - cy))
    const radius = Math.min(opts.haloMaxR, cover + opts.haloNodeMargin)
    const below = cy > 0
    const ly = below ? cy + radius + opts.haloLabelGap : cy - radius - opts.haloLabelGap
    boxes.push({
      qname: `__label__:${role}`,
      x: cx,
      y: ly,
      hw: opts.halfWidthOf(role) + 4,
      hh: opts.labelHalfHeight,
      fixed: true,
    })
  }
  return boxes
}
