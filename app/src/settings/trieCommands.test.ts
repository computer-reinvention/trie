import { describe, expect, it } from "vitest"
import { TRIE_COMMANDS, buildArgs } from "./trieCommands"

const sync = TRIE_COMMANDS.find((c) => c.command === "sync")!
const refresh = TRIE_COMMANDS.find((c) => c.command === "refresh")!
const init = TRIE_COMMANDS.find((c) => c.command === "init")!

describe("buildArgs", () => {
  it("emits boolean flags only when true", () => {
    expect(buildArgs(sync, { all: true })).toEqual(["--all"])
    expect(buildArgs(sync, { all: false })).toEqual([])
    expect(buildArgs(sync, {})).toEqual([])
  })

  it("emits value flags with their value", () => {
    expect(buildArgs(sync, { limit: 10 })).toEqual(["--limit", "10"])
    expect(buildArgs(sync, { model: "anthropic/claude-sonnet-4-6" })).toEqual([
      "--model",
      "anthropic/claude-sonnet-4-6",
    ])
  })

  it("skips empty / NaN value flags", () => {
    expect(buildArgs(sync, { limit: undefined, model: "" })).toEqual([])
    expect(buildArgs(sync, { limit: Number.NaN })).toEqual([])
  })

  it("combines multiple flags in declaration order", () => {
    const args = buildArgs(sync, { all: true, limit: 5, budget: 2 })
    expect(args).toEqual(["--all", "--limit", "5", "--budget", "2"])
  })

  it("handles the refresh command's flags", () => {
    expect(buildArgs(refresh, { beforeTurn: true, sync: true })).toEqual([
      "--before-turn",
      "--sync",
    ])
  })

  it("prepends fixedArgs (init always passes --no-install-hooks)", () => {
    expect(init.fixedArgs).toEqual(["--no-install-hooks"])
    expect(buildArgs(init, {})).toEqual(["--no-install-hooks"])
    expect(buildArgs(init, { force: true })).toEqual(["--no-install-hooks", "--force"])
    expect(buildArgs(init, { noScan: true })).toEqual(["--no-install-hooks", "--no-scan"])
  })

  it("init is selectable as a command", () => {
    expect(init).toBeDefined()
    expect(init.title).toBe("Init")
  })

  it("every command def has a unique command name", () => {
    const names = TRIE_COMMANDS.map((c) => c.command)
    expect(new Set(names).size).toBe(names.length)
  })

  it("every flag has a unique key within its command", () => {
    for (const cmd of TRIE_COMMANDS) {
      const keys = cmd.flags.map((f) => f.key)
      expect(new Set(keys).size, `dup key in ${cmd.command}`).toBe(keys.length)
    }
  })
})
