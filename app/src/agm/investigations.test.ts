import { describe, it, expect } from "vitest"
import { InvestigationRegistry, concentration } from "./investigations"

describe("concentration (investigation confidence)", () => {
  it("is 0 with no attention", () => {
    expect(concentration(new Map())).toBe(0)
  })

  it("is 1 when all attention is on one symbol (converged)", () => {
    expect(concentration(new Map([["a", 100]]))).toBe(1)
  })

  it("is low when attention is spread uniformly (uncertain)", () => {
    const wide = new Map([
      ["a", 50],
      ["b", 50],
      ["c", 50],
      ["d", 50],
    ])
    expect(concentration(wide)).toBeCloseTo(0, 5)
  })

  it("rises as attention concentrates", () => {
    const spread = new Map([
      ["a", 50],
      ["b", 50],
      ["c", 50],
      ["d", 50],
    ])
    const tight = new Map([
      ["a", 1000],
      ["b", 5],
      ["c", 5],
      ["d", 5],
    ])
    expect(concentration(tight)).toBeGreaterThan(concentration(spread))
  })
})

describe("InvestigationRegistry", () => {
  it("opens and tracks the active investigation", () => {
    const r = new InvestigationRegistry()
    r.set({ id: "inv1", label: "fix login" })
    expect(r.active()?.id).toBe("inv1")
    expect(r.active()?.label).toBe("fix login")
  })

  it("resolving clears active", () => {
    const r = new InvestigationRegistry()
    r.set({ id: "inv1", label: "x" })
    r.set({ id: "inv1", label: "x", status: "resolved" })
    expect(r.active()).toBeUndefined()
  })

  it("supports multiple investigations by id", () => {
    const r = new InvestigationRegistry()
    r.set({ id: "inv1", label: "a" })
    r.set({ id: "inv2", label: "b" })
    expect(r.all().length).toBe(2)
    expect(r.active()?.id).toBe("inv2")
  })

  it("records explicit negative evidence", () => {
    const r = new InvestigationRegistry()
    r.set({ id: "inv1", label: "x" })
    r.addNegativeEvidence("inv1", "auth:AuthService")
    expect(r.get("inv1")!.negativeEvidence).toContain("auth:AuthService")
  })

  it("updates active confidence + scope from live mass", () => {
    const r = new InvestigationRegistry()
    r.set({ id: "inv1", label: "x" })
    r.updateActive(new Map([["a", 1000], ["b", 5]]))
    const inv = r.active()!
    expect(inv.scope).toContain("a")
    expect(inv.confidence).toBeGreaterThan(0)
  })
})
