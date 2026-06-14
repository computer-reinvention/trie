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
  applyAnchorCohesion,
  roleAnchor,
  ROLE_RING_RADIUS,
  applyVisibleBudget,
  tightenRolesToFit,
  resolveLayout,
  deOverlap,
  hasNoOverlaps,
  type PolarPlacement,
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

  it("resolves the worst case: many large pills + dots all coincident at centre", () => {
    // mimics the failure screenshot: a pile of pills/dots stacked on one point.
    const nodes = Array.from({ length: 40 }, (_, i) => ({
      qname: `n${i}`,
      x: 0,
      y: 0,
      hw: i % 2 ? 40 : 8, // mix of wide pills + small dots
      hh: i % 2 ? 9 : 8,
    }))
    deOverlap(nodes)
    expect(hasNoOverlaps(nodes)).toBe(true)
  })

  it("FIXED nodes never move and movable nodes are pushed out of them", () => {
    const fixed = { qname: "__label__:x", x: 0, y: 0, hw: 30, hh: 8, fixed: true }
    const movable = { qname: "a", x: 0, y: 0, hw: 20, hh: 9 } // starts on the label
    const nodes = [fixed, movable]
    deOverlap(nodes)
    // the fixed label did not move
    expect(fixed.x).toBe(0)
    expect(fixed.y).toBe(0)
    // and nothing overlaps it now
    expect(hasNoOverlaps(nodes)).toBe(true)
  })

  it("two fixed nodes are left alone even if overlapping (no displacement)", () => {
    const a = { qname: "__label__:a", x: 0, y: 0, hw: 20, hh: 8, fixed: true }
    const b = { qname: "__label__:b", x: 5, y: 0, hw: 20, hh: 8, fixed: true }
    deOverlap([a, b])
    expect(a.x).toBe(0)
    expect(b.x).toBe(5)
  })
})

describe("anchor cohesion: region halos sit at a consistent radial band", () => {
  it("roleAnchor places every role on the same ring at its even base angle", () => {
    for (const role of ROLES) {
      const a = roleAnchor(role, ROLES)
      expect(Math.hypot(a.x, a.y)).toBeCloseTo(ROLE_RING_RADIUS, 6)
      const ang = Math.atan2(a.y, a.x)
      expect(ang).toBeCloseTo(roleBaseAngle(role, ROLES), 6)
    }
  })

  it("pulls multi-member regions toward their anchor → centroids land near the ring", () => {
    const roleByQ = new Map<string, string>()
    const placements = []
    // two roles, each with 3 members at wildly different radii (hot..cold)
    for (const role of ["auth", "payments"]) {
      for (let i = 0; i < 3; i++) {
        const q = `${role}:m${i}`
        roleByQ.set(q, role)
        placements.push(
          placeSymbol({
            qname: q,
            role,
            roles: ["auth", "payments"],
            displayMass: (i + 1) * 3, // varied mass → varied radius
            maxDisplay: 9,
            historicalMass: 0,
          }),
        )
      }
    }
    applyAnchorCohesion(placements, roleByQ, ["auth", "payments"])
    // each role's member centroid should be close to the anchor ring radius
    for (const role of ["auth", "payments"]) {
      const members = placements.filter((p) => roleByQ.get(p.qname) === role)
      const cx = members.reduce((s, p) => s + p.x, 0) / members.length
      const cy = members.reduce((s, p) => s + p.y, 0) / members.length
      const anchor = roleAnchor(role, ["auth", "payments"])
      // centroid sits within a modest band of the anchor (cohesion < 1)
      expect(Math.hypot(cx - anchor.x, cy - anchor.y)).toBeLessThan(ROLE_RING_RADIUS * 0.5)
    }
  })

  it("leaves a lone-member region on its own relevance radius (no clustering)", () => {
    const roleByQ = new Map([["solo:a", "auth"]])
    const p = placeSymbol({
      qname: "solo:a",
      role: "auth",
      roles: ["auth"],
      displayMass: 5,
      maxDisplay: 10,
      historicalMass: 0,
    })
    const before = { x: p.x, y: p.y }
    applyAnchorCohesion([p], roleByQ, ["auth"])
    expect(p.x).toBeCloseTo(before.x, 6)
    expect(p.y).toBeCloseTo(before.y, 6)
  })
})

describe("tightenRolesToFit: halos cover members AND don't overlap", () => {
  // helper: covering radius of a role's members about their centroid
  const coverOf = (pts: { x: number; y: number }[]) => {
    const cx = pts.reduce((s, p) => s + p.x, 0) / pts.length
    const cy = pts.reduce((s, p) => s + p.y, 0) / pts.length
    return { cx, cy, cover: pts.reduce((m, p) => Math.max(m, Math.hypot(p.x - cx, p.y - cy)), 0) }
  }

  it("shrinks two interleaved roles so their covering circles no longer overlap", () => {
    const roleByQ = new Map<string, string>()
    const place = (qname: string, role: string, x: number, y: number) => {
      roleByQ.set(qname, role)
      return { qname, x, y, radius: Math.hypot(x, y), angle: Math.atan2(y, x) }
    }
    // two roles whose members are wide and close together → halos would overlap
    const ps = [
      place("a:1", "a", -40, 0),
      place("a:2", "a", 40, 0),
      place("a:3", "a", 0, 40),
      place("b:1", "b", 120, 0),
      place("b:2", "b", 200, 0),
      place("b:3", "b", 160, 40),
    ]
    tightenRolesToFit(ps, roleByQ, { minCount: 3, gap: 8, minRadius: 10, nodeMargin: 6 })

    const a = coverOf(ps.filter((p) => p.qname.startsWith("a:")))
    const b = coverOf(ps.filter((p) => p.qname.startsWith("b:")))
    const centreDist = Math.hypot(a.cx - b.cx, a.cy - b.cy)
    // covering circles (radius = cover + margin) must not overlap
    expect(a.cover + b.cover + 6 + 6).toBeLessThanOrEqual(centreDist + 1e-6)
  })

  it("leaves a role untouched when it already fits its budget", () => {
    const roleByQ = new Map<string, string>()
    const place = (qname: string, role: string, x: number, y: number) => {
      roleByQ.set(qname, role)
      return { qname, x, y, radius: Math.hypot(x, y), angle: Math.atan2(y, x) }
    }
    const ps = [
      place("a:1", "a", -10, 0),
      place("a:2", "a", 10, 0),
      place("b:1", "b", 500, 0),
      place("b:2", "b", 520, 0),
    ]
    const before = ps.map((p) => ({ x: p.x, y: p.y }))
    tightenRolesToFit(ps, roleByQ, { minCount: 2, gap: 8, minRadius: 10, nodeMargin: 6 })
    ps.forEach((p, i) => {
      expect(p.x).toBeCloseTo(before[i].x, 6)
      expect(p.y).toBeCloseTo(before[i].y, 6)
    })
  })

  it("ignores roles below the min member count", () => {
    const roleByQ = new Map<string, string>([
      ["a:1", "a"],
      ["a:2", "a"],
    ])
    const ps = [
      { qname: "a:1", x: -100, y: 0, radius: 100, angle: Math.PI },
      { qname: "a:2", x: 100, y: 0, radius: 100, angle: 0 },
    ]
    const before = ps.map((p) => ({ x: p.x, y: p.y }))
    tightenRolesToFit(ps, roleByQ, { minCount: 3, gap: 8, minRadius: 10, nodeMargin: 6 })
    ps.forEach((p, i) => {
      expect(p.x).toBeCloseTo(before[i].x, 6)
      expect(p.y).toBeCloseTo(before[i].y, 6)
    })
  })
})

describe("resolveLayout: equal-mass clusters fan in 2-D, never a column", () => {
  it("20 equal-mass members in one role spread 2-D with zero overlaps", () => {
    const FILES = Array.from({ length: 20 }, (_, i) => `f${i}.py`)
    const roleByQ = new Map<string, string>(FILES.map((f) => [f, "file reads"]))
    const roleList = ["file reads"]
    // identical mass → identical radius → all seeded at the same point
    const placements: PolarPlacement[] = FILES.map((q) =>
      placeSymbol({ qname: q, role: "file reads", roles: roleList, displayMass: 5, maxDisplay: 5, historicalMass: 0 }),
    )
    applyAnchorCohesion(placements, roleByQ, roleList)
    const out = resolveLayout({
      placements,
      roleByQname: roleByQ,
      isPill: () => true,
      pillHalfWidth: (q) => (q.length * 7 + 14) / 2,
      regionLabelHalfWidth: (r) => (r.length * 9) / 2,
      haloMinCount: 2,
      pad: 8,
      dotHalf: 8,
      pillHalfHeight: 9,
      haloMaxR: 150,
      haloNodeMargin: 26,
      haloLabelGap: 12,
      labelHalfHeight: 8,
    })
    // build all footprint boxes and assert no overlaps
    const boxes = out.placements.map((p) => ({ qname: p.qname, x: p.x, y: p.y, hw: (p.qname.length * 7 + 14) / 2, hh: 9 }))
    expect(hasNoOverlaps(boxes, 8)).toBe(true)
    // NOT a vertical column: width and height must be comparable (aspect > 0.5)
    const xs = out.placements.map((p) => p.x)
    const ys = out.placements.map((p) => p.y)
    const w = Math.max(...xs) - Math.min(...xs)
    const h = Math.max(...ys) - Math.min(...ys)
    expect(w / h).toBeGreaterThan(0.5)
  })
})

describe("resolveLayout: clusters occupy separate regions (rigid separation)", () => {
  it("multiple role-clusters have non-overlapping bounding discs", () => {
    const ROLES: Record<string, string[]> = {
      orchestration: ["a1", "a2", "a3", "a4", "a5", "a6"],
      config: ["b1", "b2", "b3", "b4", "b5"],
      parsing: ["c1", "c2", "c3", "c4"],
    }
    const roleByQ = new Map<string, string>()
    const roleList = Object.keys(ROLES)
    const placements: PolarPlacement[] = []
    for (const [role, qs] of Object.entries(ROLES)) {
      qs.forEach((q, i) => {
        roleByQ.set(q, role)
        placements.push(placeSymbol({ qname: q, role, roles: roleList, displayMass: 2 + ((i * 3) % 7), maxDisplay: 9, historicalMass: 0 }))
      })
    }
    applyAnchorCohesion(placements, roleByQ, roleList)
    resolveLayout({
      placements, roleByQname: roleByQ, isPill: () => true,
      pillHalfWidth: (q) => (q.length * 7 + 14) / 2,
      regionLabelHalfWidth: (r) => (r.length * 9) / 2,
      haloMinCount: 2, pad: 8, dotHalf: 8, pillHalfHeight: 9,
      haloMaxR: 150, haloNodeMargin: 26, haloLabelGap: 12, labelHalfHeight: 8,
    })
    // bounding disc per role
    const discs = roleList.map((role) => {
      const ms = placements.filter((p) => roleByQ.get(p.qname) === role)
      const cx = ms.reduce((s, p) => s + p.x, 0) / ms.length
      const cy = ms.reduce((s, p) => s + p.y, 0) / ms.length
      let r = 0
      for (const p of ms) r = Math.max(r, Math.hypot(p.x - cx, p.y - cy) + (p.qname.length * 7 + 14) / 2)
      return { cx, cy, r }
    })
    for (let i = 0; i < discs.length; i++)
      for (let j = i + 1; j < discs.length; j++) {
        const a = discs[i], b = discs[j]
        const d = Math.hypot(a.cx - b.cx, a.cy - b.cy)
        expect(d).toBeGreaterThanOrEqual(a.r + b.r - 1) // discs don't overlap
      }
  })
})
