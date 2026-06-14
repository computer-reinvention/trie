import { describe, expect, it } from "vitest"
import { deepMerge, stripUndefined, isPlainObject } from "./trie-config"

describe("trie-config deepMerge", () => {
  it("merges nested tables without clobbering siblings", () => {
    const base = { sync: { concurrency: 4, file_workers: 8 }, scope: { include: ["**/*.py"] } }
    const out = deepMerge(base, { sync: { concurrency: 12 } })
    expect(out).toEqual({
      sync: { concurrency: 12, file_workers: 8 },
      scope: { include: ["**/*.py"] },
    })
  })

  it("replaces arrays wholesale rather than merging element-wise", () => {
    const base = { scope: { exclude: ["a", "b", "c"] } }
    const out = deepMerge(base, { scope: { exclude: ["x"] } })
    expect(out).toEqual({ scope: { exclude: ["x"] } })
  })

  it("null deletes a key (reset to trie default)", () => {
    const base = { sync: { concurrency: 12 }, debug: { enabled: true } }
    const out = deepMerge(base, { debug: null })
    expect(out).toEqual({ sync: { concurrency: 12 } })
    expect("debug" in out).toBe(false)
  })

  it("preserves hand-authored keys not present in the delta", () => {
    const base = { trie: { version: "0.1.5" }, custom: { foo: 1 } }
    const out = deepMerge(base, { models: { bootstrap: "openai/x" } })
    expect(out.trie).toEqual({ version: "0.1.5" })
    expect(out.custom).toEqual({ foo: 1 })
    expect(out.models).toEqual({ bootstrap: "openai/x" })
  })

  it("does not mutate the base object", () => {
    const base = { sync: { concurrency: 4 } }
    deepMerge(base, { sync: { concurrency: 9 } })
    expect(base.sync.concurrency).toBe(4)
  })
})

describe("trie-config stripUndefined", () => {
  it("drops undefined keys recursively", () => {
    const out = stripUndefined({ a: 1, b: undefined, c: { d: undefined, e: 2 } })
    expect(out).toEqual({ a: 1, c: { e: 2 } })
  })

  it("recurses into arrays", () => {
    expect(stripUndefined([{ a: undefined, b: 1 }])).toEqual([{ b: 1 }])
  })

  it("leaves scalars untouched", () => {
    expect(stripUndefined("x")).toBe("x")
    expect(stripUndefined(5)).toBe(5)
    expect(stripUndefined(false)).toBe(false)
  })
})

describe("trie-config isPlainObject", () => {
  it("distinguishes plain objects from arrays and null", () => {
    expect(isPlainObject({})).toBe(true)
    expect(isPlainObject([])).toBe(false)
    expect(isPlainObject(null)).toBe(false)
    expect(isPlainObject("x")).toBe(false)
  })
})
