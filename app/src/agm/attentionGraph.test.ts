import { describe, it, expect } from "vitest"
import { AttentionGraph } from "./attentionGraph"

describe("AttentionGraph (reasoning trail)", () => {
  it("reinforces a directed edge and records the path", () => {
    const g = new AttentionGraph()
    g.setInvestigation("inv1")
    g.reinforce("a", "b", 0)
    const edges = g.liveEdges(0)
    expect(edges.length).toBe(1)
    expect(edges[0]).toMatchObject({ from: "a", to: "b" })
    expect(g.trail()).toEqual(["b"])
  })

  it("reinforceChain builds consecutive edges + ordered trail", () => {
    const g = new AttentionGraph()
    g.setInvestigation("inv1")
    g.reinforceChain(["a", "b", "c"], 0)
    expect(g.liveEdges(0).length).toBe(2)
    expect(g.trail()).toEqual(["b", "c"])
  })

  it("edge heat decays over time", () => {
    const g = new AttentionGraph()
    g.setInvestigation("inv1")
    g.reinforce("a", "b", 0)
    const early = g.liveEdges(0)[0].heat
    const later = g.liveEdges(600)[0]?.heat ?? 0
    expect(later).toBeLessThan(early)
  })

  it("switching investigation resets the trail + edges", () => {
    const g = new AttentionGraph()
    g.setInvestigation("inv1")
    g.reinforceChain(["a", "b"], 0)
    g.setInvestigation("inv2")
    expect(g.liveEdges(0).length).toBe(0)
    expect(g.trail()).toEqual([])
  })

  it("ignores self-edges", () => {
    const g = new AttentionGraph()
    g.setInvestigation("inv1")
    g.reinforce("a", "a", 0)
    expect(g.liveEdges(0).length).toBe(0)
  })
})
