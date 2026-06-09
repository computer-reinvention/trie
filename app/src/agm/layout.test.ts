import { describe, it, expect } from "vitest"
import {
  R_MIN,
  R_MAX,
  radiusForMass,
  roleBaseAngle,
  symbolAngle,
  placeSymbol,
  ease,
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

describe("ease", () => {
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
})
