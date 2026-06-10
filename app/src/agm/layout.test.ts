import { describe, it, expect } from "vitest"
import {
  R_MIN,
  R_MAX,
  radiusForMass,
  roleBaseAngle,
  symbolAngle,
  placeSymbol,
  ease,
  SPEED_FLOOR,
  SPEED_CEIL,
  computeRoleClusters,
  applyClusterCohesion,
  applyVisibleBudget,
  deOverlap,
  hasNoOverlaps,
} from "./layout"

const ROLES = ["auth", "infra", "observability", "payments"]

describe("radius encodes live relevance (near = hot)", () => {
  it("cold / zero mass sits at the perimeter", () => {
    expect(radiusForMass(0, 10)).toBe(R_MAX)
  })

  it("the hottest symbol orbits near the centre (R_MIN)", () => {
    expect(radiusForMass(10, 10)).toBeCloseTo(R_MIN, 5)
  })

  it("higher live mass → smaller radius (monotonic)", () => {
    const hot = radiusForMass(8, 10)
    const warm = radiusForMass(4, 10)
    const cold = radiusForMass(1, 10)
    expect(hot).toBeLessThan(warm)
    expect(warm).toBeLessThan(cold)
  })

  it("never places anything at the exact centre", () => {
    expect(radiusForMass(1000, 1000)).toBeGreaterThanOrEqual(R_MIN)
    expect(R_MIN).toBeGreaterThan(0)
  })

  it("new discovery (no live mass) enters from the perimeter", () => {
    const p = placeSymbol({
      qname: "x:RedisClient",
      role: "infra",
      roles: ROLES,
      displayMass: 0,
      maxDisplay: 5,
      historicalMass: 0,
    })
    expect(p.radius).toBe(R_MAX)
  })
})

describe("angle is stable geography (historical, not live)", () => {
  it("each role gets a distinct stable bearing", () => {
    const a = roleBaseAngle("auth", ROLES)
    const b = roleBaseAngle("infra", ROLES)
    expect(a).not.toBeCloseTo(b, 5)
  })

  it("a symbol's angle does not change when its LIVE mass changes", () => {
    const cold = placeSymbol({
      qname: "auth:AuthService",
      role: "auth",
      roles: ROLES,
      displayMass: 0,
      maxDisplay: 10,
      historicalMass: 2,
    })
    const hot = placeSymbol({
      qname: "auth:AuthService",
      role: "auth",
      roles: ROLES,
      displayMass: 9,
      maxDisplay: 10,
      historicalMass: 2,
    })
    // radius changes, angle stays put
    expect(hot.radius).toBeLessThan(cold.radius)
    expect(hot.angle).toBeCloseTo(cold.angle, 10)
  })

  it("symbols of the same role cluster within the role's arc", () => {
    const base = roleBaseAngle("auth", ROLES)
    for (const q of ["auth:a", "auth:b", "auth:c", "auth:LoginRoute"]) {
      const ang = symbolAngle(q, "auth", ROLES, 0)
      expect(Math.abs(ang - base)).toBeLessThan(0.6) // within ~half the arc
    }
  })

  it("angle is deterministic across calls (learnable world)", () => {
    const a1 = symbolAngle("auth:AuthService", "auth", ROLES, 1)
    const a2 = symbolAngle("auth:AuthService", "auth", ROLES, 1)
    expect(a1).toBe(a2)
  })

  it("different symbols in a role get different angles (no overlap collapse)", () => {
    const a = symbolAngle("auth:a", "auth", ROLES, 0)
    const b = symbolAngle("auth:bbbb", "auth", ROLES, 0)
    expect(a).not.toBeCloseTo(b, 5)
  })
})

describe("cooling drifts a symbol outward (nothing disappears)", () => {
  it("a cooling symbol's radius grows over a decay sweep", () => {
    const radii = [9, 6, 3, 1, 0.1].map((m) => radiusForMass(m, 10))
    for (let i = 1; i < radii.length; i++) {
      expect(radii[i]).toBeGreaterThan(radii[i - 1])
    }
  })
})

describe("role clustering (roles are emergent groupings)", () => {
  const place = (qname: string, role: string, mass: number) =>
    placeSymbol({ qname, role, roles: ROLES, displayMass: mass, maxDisplay: 10, historicalMass: 0 })

  it("computes a centroid per role over its active members", () => {
    const ps = [place("auth:a", "auth", 8), place("auth:b", "auth", 6), place("infra:c", "infra", 9)]
    const roleByQ = new Map([
      ["auth:a", "auth"],
      ["auth:b", "auth"],
      ["infra:c", "infra"],
    ])
    const clusters = computeRoleClusters(ps, roleByQ)
    expect(clusters.get("auth")!.count).toBe(2)
    expect(clusters.get("infra")!.count).toBe(1)
  })

  it("cohesion pulls same-role members closer together", () => {
    const a = place("auth:aaaa", "auth", 8)
    const b = place("auth:zzzz", "auth", 6)
    const before = Math.hypot(a.x - b.x, a.y - b.y)
    const roleByQ = new Map([
      ["auth:aaaa", "auth"],
      ["auth:zzzz", "auth"],
    ])
    const [a2, b2] = applyClusterCohesion([{ ...a }, { ...b }], roleByQ)
    const after = Math.hypot(a2.x - b2.x, a2.y - b2.y)
    expect(after).toBeLessThan(before)
  })

  it("historical mass increases same-role attraction (tighter clustering)", () => {
    const roleByQ = new Map([
      ["auth:aaaa", "auth"],
      ["auth:zzzz", "auth"],
    ])
    // no history
    const a0 = place("auth:aaaa", "auth", 8)
    const b0 = place("auth:zzzz", "auth", 6)
    const [a0c, b0c] = applyClusterCohesion([{ ...a0 }, { ...b0 }], roleByQ, new Map())
    const distNoHist = Math.hypot(a0c.x - b0c.x, a0c.y - b0c.y)
    // strong history on both
    const hist = new Map([
      ["auth:aaaa", 10],
      ["auth:zzzz", 10],
    ])
    const a1 = place("auth:aaaa", "auth", 8)
    const b1 = place("auth:zzzz", "auth", 6)
    const [a1c, b1c] = applyClusterCohesion([{ ...a1 }, { ...b1 }], roleByQ, hist)
    const distHist = Math.hypot(a1c.x - b1c.x, a1c.y - b1c.y)
    expect(distHist).toBeLessThan(distNoHist)
  })

  it("a lone role member is not pulled (no cluster of 1)", () => {
    const a = place("auth:solo", "auth", 8)
    const roleByQ = new Map([["auth:solo", "auth"]])
    const [a2] = applyClusterCohesion([{ ...a }], roleByQ)
    expect(a2.x).toBeCloseTo(a.x, 10)
    expect(a2.y).toBeCloseTo(a.y, 10)
  })

  it("clustering preserves rough relevance ordering by radius from centre", () => {
    // the hotter symbol should still be no farther from centre than the cold one
    const hot = place("auth:hot", "auth", 10)
    const cold = place("auth:cold", "auth", 1)
    const roleByQ = new Map([
      ["auth:hot", "auth"],
      ["auth:cold", "auth"],
    ])
    const [h, c] = applyClusterCohesion([{ ...hot }, { ...cold }], roleByQ)
    expect(Math.hypot(h.x, h.y)).toBeLessThanOrEqual(Math.hypot(c.x, c.y) + 1e-6)
  })
})

describe("visible budget (keeps the field readable under load)", () => {
  const mk = (n: number) =>
    Array.from({ length: n }, (_, i) =>
      placeSymbol({
        qname: `m:s${i}`,
        role: `r${i % 4}`,
        roles: ["r0", "r1", "r2", "r3"],
        displayMass: i, // s{n-1} hottest
        maxDisplay: n,
        historicalMass: 0,
      }),
    )

  it("is a no-op when under budget", () => {
    const ps = mk(10)
    const mass = new Map(ps.map((p) => [p.qname, Number(p.qname.slice(3))]))
    const r = applyVisibleBudget(ps, mass, new Map(), 60)
    expect(r.kept.length).toBe(10)
    expect(r.foldedTotal).toBe(0)
  })

  it("keeps exactly `budget` hottest and folds the rest", () => {
    const ps = mk(200)
    const mass = new Map(ps.map((p) => [p.qname, Number(p.qname.slice(3))]))
    const roleBy = new Map(ps.map((p) => [p.qname, `r${Number(p.qname.slice(3)) % 4}`]))
    const r = applyVisibleBudget(ps, mass, roleBy, 60)
    expect(r.kept.length).toBe(60)
    expect(r.foldedTotal).toBe(140)
    // hottest (s199) must be kept; coldest (s0) must be folded
    expect(r.kept.some((p) => p.qname === "m:s199")).toBe(true)
    expect(r.kept.some((p) => p.qname === "m:s0")).toBe(false)
  })

  it("folded counts sum to the folded total", () => {
    const ps = mk(200)
    const mass = new Map(ps.map((p) => [p.qname, Number(p.qname.slice(3))]))
    const roleBy = new Map(ps.map((p) => [p.qname, `r${Number(p.qname.slice(3)) % 4}`]))
    const r = applyVisibleBudget(ps, mass, roleBy, 60)
    let sum = 0
    for (const n of r.foldedByRole.values()) sum += n
    expect(sum).toBe(r.foldedTotal)
  })
})

describe("ease (bounded apparent speed)", () => {
  const stepLen = (a: { x: number; y: number }, b: { x: number; y: number }) =>
    Math.hypot(b.x - a.x, b.y - a.y)

  it("moves toward the target and reports shrinking distance", () => {
    let p = { x: 0, y: 0 }
    const target = { x: 100, y: 0 }
    const first = ease(p, target)
    p = { x: first.x, y: first.y }
    const second = ease(p, target)
    expect(first.x).toBeGreaterThan(0)
    expect(second.x).toBeGreaterThan(first.x)
    expect(second.dist).toBeLessThan(first.dist)
  })

  it("never moves faster than the ceiling, even for a very far target", () => {
    const cur = { x: 0, y: 0 }
    const far = { x: 5000, y: 0 }
    const next = ease(cur, far)
    expect(stepLen(cur, next)).toBeLessThanOrEqual(SPEED_CEIL + 1e-9)
  })

  it("a huge target jump takes many frames to arrive (no lurch)", () => {
    let p = { x: 0, y: 0 }
    const target = { x: 2000, y: 0 }
    let frames = 0
    while (Math.hypot(target.x - p.x, target.y - p.y) > 0 && frames < 1000) {
      const n = ease(p, target)
      // every single frame respects the ceiling
      expect(stepLen(p, n)).toBeLessThanOrEqual(SPEED_CEIL + 1e-9)
      p = { x: n.x, y: n.y }
      frames++
    }
    expect(frames).toBeGreaterThan(2000 / SPEED_CEIL - 1) // can't beat the ceiling
  })

  it("snaps home when within the floor (no eternal crawl)", () => {
    const cur = { x: 0, y: 0 }
    const target = { x: SPEED_FLOOR * 0.5, y: 0 }
    const n = ease(cur, target)
    expect(n.x).toBe(target.x)
    expect(n.dist).toBe(0)
  })

  it("every mid-flight step is at least the floor (no imperceptible crawl)", () => {
    let p = { x: 0, y: 0 }
    const target = { x: 300, y: 0 }
    for (let i = 0; i < 200; i++) {
      const remaining = Math.hypot(target.x - p.x, target.y - p.y)
      if (remaining === 0) break
      const n = ease(p, target)
      const moved = stepLen(p, n)
      // either it snapped home (remaining <= floor) or moved >= floor
      if (n.dist !== 0) expect(moved).toBeGreaterThanOrEqual(SPEED_FLOOR - 1e-9)
      p = { x: n.x, y: n.y }
    }
  })
})

describe("deOverlap (collision resolution)", () => {
  const overlaps = (a: any, b: any, pad = 0) =>
    a.hw + b.hw + pad - Math.abs(a.x - b.x) > 0 && a.hh + b.hh + pad - Math.abs(a.y - b.y) > 0

  it("separates two stacked pills", () => {
    const nodes = [
      { qname: "a", x: 100, y: 0, hw: 40, hh: 9 },
      { qname: "b", x: 110, y: 2, hw: 40, hh: 9 }, // heavily overlapping
    ]
    expect(overlaps(nodes[0], nodes[1])).toBe(true)
    deOverlap(nodes)
    expect(overlaps(nodes[0], nodes[1])).toBe(false)
  })

  it("leaves already-separated pills untouched", () => {
    const nodes = [
      { qname: "a", x: 100, y: 0, hw: 20, hh: 9 },
      { qname: "b", x: 400, y: 0, hw: 20, hh: 9 },
    ]
    const before = nodes.map((n) => ({ x: n.x, y: n.y }))
    deOverlap(nodes)
    expect(nodes[0].x).toBeCloseTo(before[0].x, 6)
    expect(nodes[1].x).toBeCloseTo(before[1].x, 6)
  })

  it("INVARIANT: leaves zero overlaps for a tight triple", () => {
    const nodes = [
      { qname: "a", x: 100, y: 0, hw: 40, hh: 9 },
      { qname: "b", x: 105, y: 0, hw: 40, hh: 9 },
      { qname: "c", x: 110, y: 0, hw: 40, hh: 9 },
    ]
    deOverlap(nodes)
    expect(hasNoOverlaps(nodes)).toBe(true)
  })

  it("INVARIANT: zero overlaps for a dense same-radius pile (no compromise)", () => {
    const nodes = Array.from({ length: 12 }, (_, i) => ({
      qname: `s${i}`,
      x: 120 + (i % 3),
      y: (i % 2) * 2,
      hw: 30,
      hh: 9,
    }))
    deOverlap(nodes)
    expect(hasNoOverlaps(nodes)).toBe(true)
  })

  it("INVARIANT: zero overlaps even when all pills are exactly coincident", () => {
    const nodes = Array.from({ length: 6 }, (_, i) => ({
      qname: `s${i}`,
      x: 200,
      y: 0,
      hw: 35,
      hh: 9,
    }))
    deOverlap(nodes)
    expect(hasNoOverlaps(nodes)).toBe(true)
  })

  it("INVARIANT: stress — 40 random pills end with zero overlaps", () => {
    const nodes = Array.from({ length: 40 }, (_, i) => ({
      qname: `s${i}`,
      x: (Math.sin(i * 1.7) * 200) | 0,
      y: (Math.cos(i * 2.3) * 200) | 0,
      hw: 25,
      hh: 9,
    }))
    deOverlap(nodes)
    expect(hasNoOverlaps(nodes)).toBe(true)
  })

  it("stays as close to the true target as legal (pull-back works)", () => {
    // two pills far apart: pull-back must keep them near their targets (no drift)
    const nodes = [
      { qname: "a", x: 100, y: 0, hw: 20, hh: 9 },
      { qname: "b", x: 100, y: 60, hw: 20, hh: 9 }, // not overlapping
    ]
    deOverlap(nodes)
    expect(nodes[0].x).toBeCloseTo(100, 6)
    expect(nodes[1].y).toBeCloseTo(60, 6)
  })

  it("is a no-op for <2 nodes", () => {
    const one = [{ qname: "a", x: 1, y: 2, hw: 3, hh: 3 }]
    deOverlap(one)
    expect(one[0].x).toBe(1)
  })
})
