import { describe, it, expect } from "vitest"
import { AttentionModel } from "./attentionModel"

describe("AttentionModel", () => {
  it("ingests events and reports live mass that decays", () => {
    const m = new AttentionModel()
    m.ingest("a:b", "read", 0)
    expect(m.liveMass("a:b", 0)).toBeCloseTo(40, 5)
    // after one read half-life (180s) → ~20
    expect(m.liveMass("a:b", 180)).toBeCloseTo(20, 5)
  })

  it("scaled ingest attenuates weight (grep hits are a faint net)", () => {
    const m = new AttentionModel()
    m.ingest("full", "grep", 0) // weight 10
    m.ingest("hit", "grep", 0, 0.25) // weight 2.5
    expect(m.liveMass("hit", 0)).toBeCloseTo(m.liveMass("full", 0) * 0.25, 5)
  })

  it("trace contributes more than grep (weights)", () => {
    const m = new AttentionModel()
    m.ingest("g", "grep", 0)
    m.ingest("t", "trace", 0)
    expect(m.liveMass("t", 0)).toBeGreaterThan(m.liveMass("g", 0))
  })

  it("never dampens by role/kind — util gets full mass", () => {
    const m = new AttentionModel()
    m.setRoles(new Map([["util:x", "util"]]))
    m.ingest("util:x", "trace", 0)
    expect(m.liveMass("util:x", 0)).toBeCloseTo(80, 5)
  })

  it("rename transfers live state", () => {
    const m = new AttentionModel()
    m.ingest("old", "trace", 0)
    m.rename("old", "new")
    expect(m.liveMass("old", 0)).toBe(0)
    expect(m.liveMass("new", 0)).toBeCloseTo(80, 5)
  })

  it("delete removes live mass immediately", () => {
    const m = new AttentionModel()
    m.ingest("x", "read", 0)
    m.remove("x")
    expect(m.liveMass("x", 0)).toBe(0)
  })

  it("create inherits 0.5x of the creator's live mass", () => {
    const m = new AttentionModel()
    m.ingest("creator", "trace", 0) // 80
    m.inheritFrom("creator", "created", 0)
    expect(m.liveMass("created", 0)).toBeCloseTo(40, 5)
  })

  it("negative evidence subtracts live mass", () => {
    const m = new AttentionModel()
    m.ingest("x", "trace", 0) // +80
    m.applyNegativeEvidence("x", 100, 0) // -100
    expect(m.liveMass("x", 0)).toBe(0) // clamped at 0 (raw -20 → max(0,...))
  })

  it("historical seed contributes only faintly to display mass", () => {
    const m = new AttentionModel()
    m.seedHistorical("x", 100)
    const mass = m.massFor("x", 0)
    expect(mass.live).toBe(0)
    expect(mass.historical).toBe(100)
    // display = log(0 + 0.15*100 + 1) = log(16) ≈ 2.77
    expect(mass.display).toBeCloseTo(Math.log(16), 5)
  })

  it("role rollup sums member live mass", () => {
    const m = new AttentionModel()
    m.setRoles(
      new Map([
        ["auth:a", "auth"],
        ["auth:b", "auth"],
        ["infra:c", "infra"],
      ]),
    )
    m.ingest("auth:a", "trace", 0) // 80
    m.ingest("auth:b", "read", 0) // 40
    m.ingest("infra:c", "grep", 0) // 10
    const roles = m.roleMass(0)
    expect(roles.get("auth")!.live).toBeCloseTo(120, 5)
    expect(roles.get("infra")!.live).toBeCloseTo(10, 5)
  })

  it("centroid ranks the hottest roles first", () => {
    const m = new AttentionModel()
    m.setRoles(
      new Map([
        ["auth:a", "auth"],
        ["infra:c", "infra"],
      ]),
    )
    m.ingest("infra:c", "grep", 0) // 10
    m.ingest("auth:a", "trace", 0) // 80
    const c = m.centroid(0)
    expect(c.topRoles[0].role).toBe("auth")
  })

  it("clearLive drops live mass but keeps historical seed", () => {
    const m = new AttentionModel()
    m.seedHistorical("kept", 50)
    m.ingest("kept", "trace", 0) // live + historical
    m.ingest("transient", "trace", 0) // live only, no history
    m.clearLive()
    // live gone everywhere
    expect(m.liveMass("kept", 0)).toBe(0)
    expect(m.liveMass("transient", 0)).toBe(0)
    // historical seed survives on the node that had one
    expect(m.massFor("kept", 0).historical).toBe(50)
    // node with no history is dropped entirely
    expect(m.snapshot(0).has("transient")).toBe(false)
  })

  it("snapshot excludes cold nodes", () => {
    const m = new AttentionModel()
    m.ingest("hot", "trace", 0)
    // far future → fully decayed below floor
    const snap = m.snapshot(100000)
    expect(snap.has("hot")).toBe(false)
  })

  it("prune keeps a node with a residual negative/inherited contribution", () => {
    const m = new AttentionModel()
    m.ingest("x", "grep", 0)
    m.prune(100000) // grep decays away entirely
    // fully decayed + no historical → dropped
    expect(m.liveMass("x", 100000)).toBe(0)
  })
})
