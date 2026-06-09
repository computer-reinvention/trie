import { describe, it, expect } from "vitest"
import { buildTypedAdjacency, propagate } from "./propagation"
import { PROPAGATION_FACTOR } from "./weights"

describe("propagation", () => {
  it("spreads one weak hop weighted by edge kind", () => {
    const adj = buildTypedAdjacency([{ from: "a", to: "b", kind: "calls" }])
    const live = new Map([["a", 100]])
    const gained = propagate(live, adj)
    // calls weight = 1.0; gain = 100 * 1.0 * 0.15
    expect(gained.get("b")).toBeCloseTo(100 * 1.0 * PROPAGATION_FACTOR, 5)
  })

  it("weaker edge kinds propagate less", () => {
    const adj = buildTypedAdjacency([
      { from: "a", to: "b", kind: "calls" }, // 1.0
      { from: "a", to: "c", kind: "contains" }, // 0.2
    ])
    const gained = propagate(new Map([["a", 100]]), adj)
    expect(gained.get("b")!).toBeGreaterThan(gained.get("c")!)
  })

  it("does not propagate from a cold source", () => {
    const adj = buildTypedAdjacency([{ from: "a", to: "b", kind: "calls" }])
    expect(propagate(new Map([["a", 0]]), adj).size).toBe(0)
  })

  it("is one hop only (does not reach a->b->c)", () => {
    const adj = buildTypedAdjacency([
      { from: "a", to: "b", kind: "calls" },
      { from: "b", to: "c", kind: "calls" },
    ])
    const gained = propagate(new Map([["a", 100]]), adj)
    expect(gained.has("b")).toBe(true)
    expect(gained.has("c")).toBe(false) // c is two hops from the only hot node
  })

  it("skips hub sources (very high out-degree)", () => {
    const edges = Array.from({ length: 50 }, (_, i) => ({
      from: "hub",
      to: `n${i}`,
      kind: "calls",
    }))
    const adj = buildTypedAdjacency(edges)
    const gained = propagate(new Map([["hub", 100]]), adj)
    expect(gained.size).toBe(0) // hub not expanded
  })
})
