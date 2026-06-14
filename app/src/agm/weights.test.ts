import { describe, it, expect } from "vitest"
import { foldLiveMass, makeContribution, decayScalar, displayMass } from "./weights"
import { liveLambda } from "@/api/types"

describe("weights / decay math", () => {
  it("a contribution decays to half its weight after one half-life", () => {
    const c = makeContribution("grep", 0) // grep half-life = 30s, weight 10
    // at t=30 (one half-life) the value should be ~5
    expect(foldLiveMass([c], 30)).toBeCloseTo(5, 5)
  })

  it("trace stays warmer than grep at the same dt (longer half-life)", () => {
    const grep = makeContribution("grep", 0)
    const trace = makeContribution("trace", 0)
    const t = 60
    expect(foldLiveMass([trace], t)).toBeGreaterThan(foldLiveMass([grep], t))
  })

  it("multiple contributions sum", () => {
    const a = makeContribution("read", 100)
    const b = makeContribution("read", 100)
    expect(foldLiveMass([a, b], 100)).toBeCloseTo(80, 5) // 40 + 40, no decay at dt=0
  })

  it("decayScalar halves at one half-life", () => {
    const lam = liveLambda("trace") // 600s
    expect(decayScalar(8, lam, 0, 600)).toBeCloseTo(4, 5)
  })

  it("displayMass is log compression, clamps negatives", () => {
    expect(displayMass(0)).toBe(0)
    expect(displayMass(-5)).toBe(0)
    expect(displayMass(Math.E - 1)).toBeCloseTo(1, 6)
  })
})
