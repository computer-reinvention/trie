#!/usr/bin/env node
/**
 * Postinstall: install the opencode fork's dependencies using bun.
 * Runs automatically after `npm install` in app/.
 * Safe to re-run — bun install is idempotent.
 */

import { execFileSync } from "child_process"
import { existsSync } from "fs"
import { resolve, dirname } from "path"
import { fileURLToPath } from "url"
import { homedir } from "os"

const __dirname = dirname(fileURLToPath(import.meta.url))
const repoRoot = resolve(__dirname, "..", "..")
const forkDir = resolve(repoRoot, "opencode", "packages", "opencode")

if (!existsSync(resolve(forkDir, "src", "index.ts"))) {
  console.warn(
    "[trie setup] opencode submodule not found at",
    forkDir,
    "— run `git submodule update --init` first.",
  )
  process.exit(0)
}

// Find bun — prefer PATH, fall back to ~/.bun/bin/bun
function findBun() {
  const candidates = ["bun", resolve(homedir(), ".bun", "bin", "bun")]
  for (const candidate of candidates) {
    try {
      execFileSync(candidate, ["--version"], { stdio: "ignore" })
      return candidate
    } catch {
      // not found
    }
  }
  return null
}

const bun = findBun()
if (!bun) {
  console.warn("[trie setup] bun not found — skipping opencode dep install.")
  console.warn("  Install bun: curl -fsSL https://bun.sh/install | bash")
  process.exit(0)
}

console.log("[trie setup] Installing opencode fork deps with bun...")
try {
  execFileSync(bun, ["install", "--ignore-scripts"], {
    cwd: forkDir,
    stdio: "inherit",
  })
  console.log("[trie setup] Done.")
} catch (err) {
  console.error("[trie setup] bun install failed:", err.message)
  process.exit(1)
}
