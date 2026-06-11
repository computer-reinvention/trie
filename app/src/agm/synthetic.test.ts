import { describe, it, expect } from "vitest"
import {
  syntheticQname,
  syntheticFileQname,
  syntheticFilePath,
  isSyntheticQname,
  isSyntheticFileQname,
  looksLikeFilePath,
} from "@/api/types"
import { syntheticRole, syntheticLabel, SYNTHETIC_ROLE, SYNTHETIC_FILE_ROLE } from "./synthetic"

describe("synthetic file nodes", () => {
  it("round-trips a per-file qname to its path", () => {
    const q = syntheticFileQname("trie/mcp_server.py")
    expect(isSyntheticQname(q)).toBe(true)
    expect(isSyntheticFileQname(q)).toBe(true)
    expect(syntheticFilePath(q)).toBe("trie/mcp_server.py")
  })

  it("a fixed-surface qname is synthetic but NOT a file node", () => {
    const q = syntheticQname("Filesystem")
    expect(isSyntheticQname(q)).toBe(true)
    expect(isSyntheticFileQname(q)).toBe(false)
    expect(syntheticFilePath(q)).toBeNull()
  })

  it("labels a per-file node by its basename", () => {
    expect(syntheticLabel(syntheticFileQname("a/b/config.toml"))).toBe("config.toml")
    expect(syntheticLabel(syntheticFileQname("README.md"))).toBe("README.md")
  })

  it("labels a fixed surface by its name", () => {
    expect(syntheticLabel(syntheticQname("Bash"))).toBe("Bash")
  })

  it("returns null label for a non-synthetic qname", () => {
    expect(syntheticLabel("trie/sync/writer.py:foo")).toBeNull()
  })

  it("resolves roles: per-file → filesystem, surface → external, real → null", () => {
    expect(syntheticRole(syntheticFileQname("x.py"))).toBe(SYNTHETIC_FILE_ROLE)
    expect(syntheticRole(syntheticQname("Web"))).toBe(SYNTHETIC_ROLE)
    expect(syntheticRole("trie/foo:bar")).toBeNull()
  })
})

describe("looksLikeFilePath", () => {
  it("accepts paths with a slash", () => {
    expect(looksLikeFilePath("trie/mcp_server.py")).toBe(true)
    expect(looksLikeFilePath("src/foo/bar")).toBe(true)
  })

  it("accepts a bare filename with an extension", () => {
    expect(looksLikeFilePath("config.toml")).toBe(true)
    expect(looksLikeFilePath("README.md")).toBe(true)
  })

  it("rejects symbol qnames (carry a colon)", () => {
    expect(looksLikeFilePath("trie/sync/writer.py:flush")).toBe(false)
  })

  it("rejects free text and empty strings", () => {
    expect(looksLikeFilePath("")).toBe(false)
    expect(looksLikeFilePath("flush")).toBe(false)
    expect(looksLikeFilePath("some plain words")).toBe(false)
  })
})
