import { describe, it, expect } from "vitest"
import { deepMerge, withTrieMcp, parseTolerant } from "./opencode-config"

const TRIE = { trieMcpBin: "/bundled/trie-mcp", projectDir: "/proj" }

describe("deepMerge", () => {
  it("preserves hand-authored top-level keys not present in the delta", () => {
    const base = { customKey: "keep-me", model: "old" }
    const merged = deepMerge(base, { model: "new" })
    expect(merged.customKey).toBe("keep-me")
    expect(merged.model).toBe("new")
  })

  it("merges nested objects rather than replacing them", () => {
    const base = { permission: { edit: "ask", bash: "ask" } }
    const merged = deepMerge(base, { permission: { edit: "deny" } })
    expect(merged.permission).toEqual({ edit: "deny", bash: "ask" })
  })

  it("replaces arrays wholesale (no element merge)", () => {
    const base = { instructions: ["a.md", "b.md"] }
    const merged = deepMerge(base, { instructions: ["c.md"] })
    expect(merged.instructions).toEqual(["c.md"])
  })

  it("deletes a key when the delta value is null", () => {
    const base = { share: "auto", model: "x" }
    const merged = deepMerge(base, { share: null })
    expect("share" in merged).toBe(false)
    expect(merged.model).toBe("x")
  })

  it("treats a scalar overwriting an object as a replacement", () => {
    const base = { lsp: { typescript: { disabled: true } } }
    const merged = deepMerge(base, { lsp: true })
    expect(merged.lsp).toBe(true)
  })

  it("does not mutate the base object", () => {
    const base = { permission: { edit: "ask" } }
    const snapshot = JSON.stringify(base)
    deepMerge(base, { permission: { edit: "deny" } })
    expect(JSON.stringify(base)).toBe(snapshot)
  })

  it("creates a nested object when the base lacks it", () => {
    const merged = deepMerge({}, { compaction: { auto: false } })
    expect(merged.compaction).toEqual({ auto: false })
  })
})

describe("withTrieMcp", () => {
  it("injects the trie MCP entry when none exists", () => {
    const out = withTrieMcp({}, TRIE)
    expect(out.mcp).toEqual({
      trie: { type: "local", command: ["/bundled/trie-mcp", "/proj"], enabled: true },
    })
  })

  it("preserves other MCP servers while asserting trie", () => {
    const out = withTrieMcp({ mcp: { jira: { type: "remote", url: "u" } } }, TRIE)
    const mcp = out.mcp as Record<string, unknown>
    expect(mcp.jira).toEqual({ type: "remote", url: "u" })
    expect((mcp.trie as Record<string, unknown>).command).toEqual([
      "/bundled/trie-mcp",
      "/proj",
    ])
  })

  it("overwrites a stale/user-broken trie entry with the bundled binary", () => {
    const out = withTrieMcp(
      { mcp: { trie: { type: "local", command: ["wrong-bin"], enabled: false } } },
      TRIE,
    )
    const trie = (out.mcp as Record<string, unknown>).trie as Record<string, unknown>
    expect(trie.command).toEqual(["/bundled/trie-mcp", "/proj"])
    expect(trie.enabled).toBe(true)
  })

  it("does not mutate the input config's mcp object", () => {
    const base = { mcp: { jira: { url: "u" } } }
    const snapshot = JSON.stringify(base)
    withTrieMcp(base, TRIE)
    expect(JSON.stringify(base)).toBe(snapshot)
  })
})

describe("full merge + trie assertion (writer pipeline)", () => {
  it("preserves unmanaged keys, applies the delta, and asserts trie", () => {
    const existing = {
      $schema: "x",
      customKey: "keep-me",
      mcp: { jira: { type: "remote", url: "u" } },
      permission: { edit: "ask", bash: "ask" },
    }
    const delta = { permission: { edit: "deny" }, instructions: ["a.md"] }
    let merged = deepMerge(existing, delta)
    merged = withTrieMcp(merged, TRIE)

    expect(merged.customKey).toBe("keep-me")
    expect(merged.$schema).toBe("x")
    expect((merged.permission as Record<string, unknown>).edit).toBe("deny")
    expect((merged.permission as Record<string, unknown>).bash).toBe("ask")
    expect(merged.instructions).toEqual(["a.md"])
    const mcp = merged.mcp as Record<string, unknown>
    expect(mcp.jira).toBeTruthy()
    expect(mcp.trie).toBeTruthy()
  })
})

describe("parseTolerant", () => {
  it("parses plain JSON", () => {
    expect(parseTolerant('{"a":1}')).toEqual({ a: 1 })
  })

  it("strips line comments", () => {
    expect(parseTolerant('{\n  // a comment\n  "a": 1\n}')).toEqual({ a: 1 })
  })

  it("strips block comments", () => {
    expect(parseTolerant('{ /* block */ "a": 1 }')).toEqual({ a: 1 })
  })

  it("tolerates trailing commas", () => {
    expect(parseTolerant('{ "a": 1, "b": 2, }')).toEqual({ a: 1, b: 2 })
  })

  it("returns {} on unrecoverable input", () => {
    expect(parseTolerant("not json at all {{{")).toEqual({})
  })

  it("does not mistake a URL's // for a comment", () => {
    // The comment stripper requires the // to not be preceded by a colon.
    const out = parseTolerant('{ "url": "https://example.com/mcp" }')
    expect(out).toEqual({ url: "https://example.com/mcp" })
  })
})
