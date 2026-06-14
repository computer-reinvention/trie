import { describe, it, expect } from "vitest"
import { getPointer, setPointer, buildManagedDelta } from "./configPointer"

describe("getPointer", () => {
  it("reads a top-level scalar", () => {
    expect(getPointer({ model: "x" }, "model")).toBe("x")
  })

  it("reads a nested value", () => {
    expect(getPointer({ compaction: { auto: true } }, "compaction.auto")).toBe(true)
  })

  it("returns undefined for a missing path", () => {
    expect(getPointer({}, "a.b.c")).toBeUndefined()
    expect(getPointer({ a: {} }, "a.b.c")).toBeUndefined()
  })

  it("does not descend into arrays", () => {
    expect(getPointer({ list: [{ x: 1 }] }, "list.x")).toBeUndefined()
  })
})

describe("setPointer", () => {
  it("sets a top-level value", () => {
    const obj: Record<string, unknown> = {}
    setPointer(obj, "model", "anthropic/x")
    expect(obj).toEqual({ model: "anthropic/x" })
  })

  it("creates intermediate objects for a nested path", () => {
    const obj: Record<string, unknown> = {}
    setPointer(obj, "attachment.image.max_width", 1024)
    expect(obj).toEqual({ attachment: { image: { max_width: 1024 } } })
  })

  it("preserves sibling keys when writing a nested value", () => {
    const obj: Record<string, unknown> = { compaction: { auto: true } }
    setPointer(obj, "compaction.prune", true)
    expect(obj).toEqual({ compaction: { auto: true, prune: true } })
  })

  it("deletes the leaf when value is undefined", () => {
    const obj: Record<string, unknown> = { share: "auto" }
    setPointer(obj, "share", undefined)
    expect("share" in obj).toBe(false)
  })

  it("overwrites a non-object intermediate with an object", () => {
    const obj: Record<string, unknown> = { server: "not-an-object" }
    setPointer(obj, "server.port", 4096)
    expect(obj).toEqual({ server: { port: 4096 } })
  })

  it("round-trips with getPointer", () => {
    const obj: Record<string, unknown> = {}
    setPointer(obj, "experimental.policies", [{ effect: "deny" }])
    expect(getPointer(obj, "experimental.policies")).toEqual([{ effect: "deny" }])
  })
})

describe("buildManagedDelta", () => {
  const managed = ["model", "permission", "mcp"] as const

  it("emits present keys and nulls absent ones", () => {
    const delta = buildManagedDelta({ model: "x" }, managed)
    expect(delta.model).toBe("x")
    expect(delta.permission).toBeNull()
    expect(delta.mcp).toBeNull()
  })

  it("passes managed object values through by reference value", () => {
    const cfg = { permission: { edit: "deny" } }
    const delta = buildManagedDelta(cfg, managed)
    expect(delta.permission).toEqual({ edit: "deny" })
  })

  it("only includes managed keys (ignores unmanaged config keys)", () => {
    const delta = buildManagedDelta({ customKey: "y", model: "x" }, managed)
    expect("customKey" in delta).toBe(false)
    expect(Object.keys(delta).sort()).toEqual(["mcp", "model", "permission"])
  })
})
