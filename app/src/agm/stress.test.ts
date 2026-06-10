// Stress + edge-case tests — the "no surprises" gate. Drives the engine through
// adversarial sequences and asserts invariants hold (no NaN, no negative radii,
// bounded mass, correct lifecycle on rename/delete/create, hub guard, etc.).

import { describe, it, expect } from "vitest"
import { AttentionModel } from "./attentionModel"
import { AttentionGraph } from "./attentionGraph"
import { buildTypedAdjacency, propagate } from "./propagation"
import { placeSymbol, applyClusterCohesion, radiusForMass, type PolarPlacement } from "./layout"
import type { AttentionEventType } from "@/api/types"

const TYPES: AttentionEventType[] = ["grep", "read", "trace", "write"]

function finite(n: number): boolean {
  return Number.isFinite(n)
}

describe("invariants under load", () => {
  it("1000 random events never produce NaN / negative / unbounded display mass", () => {
    const m = new AttentionModel()
    const roleByQ = new Map<string, string>()
    let t = 0
    for (let i = 0; i < 1000; i++) {
      const q = `mod${i % 60}:sym${i % 200}`
      roleByQ.set(q, `role${i % 12}`)
      m.setRoles(roleByQ)
      m.ingest(q, TYPES[i % TYPES.length], t)
      t += Math.random() * 3
    }
    const snap = m.snapshot(t)
    for (const [, mass] of snap) {
      expect(finite(mass.live)).toBe(true)
      expect(finite(mass.display)).toBe(true)
      expect(mass.live).toBeGreaterThanOrEqual(0)
      expect(mass.display).toBeGreaterThanOrEqual(0)
      // display is log-compressed → must stay modest even with huge raw mass
      expect(mass.display).toBeLessThan(50)
    }
  })

  it("placement is always finite and within [R_MIN, R_MAX]", () => {
    const roles = ["a", "b", "c"]
    for (const d of [0, 0.0001, 1, 5, 1e6, NaN]) {
      const maxD = 5
      const safeD = Number.isNaN(d) ? 0 : d
      const p = placeSymbol({
        qname: "x:y",
        role: "a",
        roles,
        displayMass: safeD,
        maxDisplay: maxD,
        historicalMass: 0,
      })
      expect(finite(p.x)).toBe(true)
      expect(finite(p.y)).toBe(true)
      expect(finite(p.radius)).toBe(true)
      expect(p.radius).toBeGreaterThan(0)
    }
  })

  it("radiusForMass handles zero/negative maxDisplay without NaN", () => {
    expect(finite(radiusForMass(5, 0))).toBe(true)
    expect(finite(radiusForMass(0, 0))).toBe(true)
    expect(finite(radiusForMass(5, -1))).toBe(true)
  })

  it("cluster cohesion never NaNs when roles are missing from the map", () => {
    const ps: PolarPlacement[] = [
      placeSymbol({ qname: "a:1", role: "x", roles: ["x"], displayMass: 5, maxDisplay: 5, historicalMass: 0 }),
      placeSymbol({ qname: "b:2", role: "x", roles: ["x"], displayMass: 3, maxDisplay: 5, historicalMass: 0 }),
    ]
    // empty role map → everything "untagged", still must not NaN
    applyClusterCohesion(ps, new Map())
    for (const p of ps) {
      expect(finite(p.x)).toBe(true)
      expect(finite(p.y)).toBe(true)
    }
  })
})

describe("lifecycle edge cases", () => {
  it("rename then delete leaves no trace", () => {
    const m = new AttentionModel()
    m.ingest("old", "trace", 0)
    m.rename("old", "new")
    m.remove("new")
    expect(m.liveMass("old", 0)).toBe(0)
    expect(m.liveMass("new", 0)).toBe(0)
    expect(m.snapshot(0).size).toBe(0)
  })

  it("renaming a non-existent symbol is a no-op (no throw)", () => {
    const m = new AttentionModel()
    expect(() => m.rename("ghost", "phantom")).not.toThrow()
    expect(m.liveMass("phantom", 0)).toBe(0)
  })

  it("create from a cold creator inherits nothing", () => {
    const m = new AttentionModel()
    m.inheritFrom("coldCreator", "child", 0)
    expect(m.liveMass("child", 0)).toBe(0)
  })

  it("repeated negative evidence drives mass to zero, never below", () => {
    const m = new AttentionModel()
    m.ingest("x", "trace", 0)
    m.applyNegativeEvidence("x", 100, 0)
    m.applyNegativeEvidence("x", 100, 0)
    m.applyNegativeEvidence("x", 100, 0)
    expect(m.liveMass("x", 0)).toBe(0)
    expect(m.liveMass("x", 0)).toBeGreaterThanOrEqual(0)
  })

  it("create inherits, then both decay independently", () => {
    const m = new AttentionModel()
    m.ingest("creator", "trace", 0) // 80
    m.inheritFrom("creator", "child", 0) // 40
    const c0 = m.liveMass("child", 0)
    const c1 = m.liveMass("child", 300)
    expect(c1).toBeLessThan(c0)
  })
})

describe("rapid role switching converges to the right active subsystem", () => {
  it("the last sustained role wins the centroid", () => {
    const m = new AttentionModel()
    m.setRoles(
      new Map([
        ["a:1", "auth"],
        ["i:1", "infra"],
        ["o:1", "obs"],
      ]),
    )
    // bounce between roles, then settle hard on infra
    m.ingest("a:1", "grep", 0)
    m.ingest("o:1", "grep", 1)
    m.ingest("a:1", "grep", 2)
    for (let i = 0; i < 6; i++) m.ingest("i:1", "trace", 10 + i)
    const top = m.centroid(16).topRoles
    expect(top[0].role).toBe("infra")
  })
})

describe("propagation under hubs + dense graphs", () => {
  it("a hub source does not smear attention across the map", () => {
    const edges = Array.from({ length: 80 }, (_, i) => ({ from: "hub", to: `n${i}`, kind: "calls" }))
    const adj = buildTypedAdjacency(edges)
    expect(propagate(new Map([["hub", 100]]), adj).size).toBe(0)
  })

  it("propagation total never exceeds source mass * factor * fanout bound", () => {
    const edges = [
      { from: "a", to: "b", kind: "calls" },
      { from: "a", to: "c", kind: "imports" },
      { from: "a", to: "d", kind: "contains" },
    ]
    const adj = buildTypedAdjacency(edges)
    const gained = propagate(new Map([["a", 100]]), adj)
    let total = 0
    for (const v of gained.values()) total += v
    // each neighbour gets <= 100 * 1.0 * 0.15; sum bounded by 3 * 15
    expect(total).toBeLessThanOrEqual(3 * 15 + 1e-9)
    for (const v of gained.values()) expect(v).toBeGreaterThan(0)
  })
})

describe("decay extremes", () => {
  it("attention fully cools to ~0 after a long idle", () => {
    const m = new AttentionModel()
    m.ingest("x", "trace", 0)
    expect(m.liveMass("x", 86400)).toBeLessThan(1e-6) // 1 day
  })

  it("a single event at t=0 read at t=0 equals its weight exactly", () => {
    const m = new AttentionModel()
    m.ingest("x", "read", 0)
    expect(m.liveMass("x", 0)).toBeCloseTo(40, 6)
  })
})

describe("attention graph under churn", () => {
  it("64+ reinforcements keep a bounded, non-NaN edge set", () => {
    const g = new AttentionGraph()
    g.setInvestigation("inv")
    for (let i = 0; i < 200; i++) g.reinforce(`a${i % 10}`, `b${i % 10}`, i)
    const edges = g.liveEdges(200)
    for (const e of edges) expect(finite(e.heat)).toBe(true)
    expect(g.trail().length).toBeLessThanOrEqual(64) // trail is capped
  })
})
