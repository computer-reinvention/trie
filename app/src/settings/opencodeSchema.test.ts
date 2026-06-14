import { describe, it, expect } from "vitest"
import {
  defaultEnvVar,
  MANAGED_TOP_KEYS,
  OC_FIELDS,
  ocFieldByPointer,
} from "./opencodeSchema"

describe("defaultEnvVar", () => {
  it("maps known providers to their canonical env var", () => {
    expect(defaultEnvVar("anthropic")).toBe("ANTHROPIC_API_KEY")
    expect(defaultEnvVar("openai")).toBe("OPENAI_API_KEY")
    expect(defaultEnvVar("gemini")).toBe("GOOGLE_GENERATIVE_AI_API_KEY")
  })

  it("derives a sane env var for unknown providers", () => {
    expect(defaultEnvVar("my-provider")).toBe("MY_PROVIDER_API_KEY")
    expect(defaultEnvVar("foo.bar")).toBe("FOO_BAR_API_KEY")
  })
})

describe("MANAGED_TOP_KEYS", () => {
  it("is derived from field pointers' top-level segment, de-duplicated", () => {
    // every field's top key must appear exactly once
    for (const f of OC_FIELDS) {
      const top = f.pointer.split(".")[0]
      expect(MANAGED_TOP_KEYS).toContain(top)
    }
    expect(new Set(MANAGED_TOP_KEYS).size).toBe(MANAGED_TOP_KEYS.length)
  })

  it("includes the expected core keys", () => {
    for (const k of ["model", "permission", "provider", "mcp", "agent", "instructions"]) {
      expect(MANAGED_TOP_KEYS).toContain(k)
    }
  })

  it("never manages tui-only or deprecated keys", () => {
    for (const forbidden of ["theme", "keybinds", "mode", "autoshare", "layout"]) {
      expect(MANAGED_TOP_KEYS).not.toContain(forbidden)
    }
  })
})

describe("OC_FIELDS integrity", () => {
  it("has unique pointers", () => {
    const seen = new Set<string>()
    for (const f of OC_FIELDS) {
      expect(seen.has(f.pointer)).toBe(false)
      seen.add(f.pointer)
    }
  })

  it("enum fields declare options", () => {
    for (const f of OC_FIELDS) {
      if (f.type === "enum") expect(f.enum && f.enum.length).toBeTruthy()
    }
  })

  it("ocFieldByPointer resolves a known field", () => {
    expect(ocFieldByPointer("model")?.title).toBeTruthy()
    expect(ocFieldByPointer("does.not.exist")).toBeUndefined()
  })
})
