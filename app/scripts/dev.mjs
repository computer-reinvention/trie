#!/usr/bin/env node
/**
 * dev.mjs — build resources, then launch the Electron app.
 *
 * Resources are ALWAYS rebuilt before launch so binary bugs are never
 * silently stale. The build is skipped only with --skip-resources.
 *
 * Usage:
 *   npm run dev                      # always rebuild resources, then launch
 *   npm run dev -- --skip-resources  # skip resource build (use existing binaries)
 */

import { execSync, spawn } from "child_process"
import { resolve, dirname } from "path"
import { fileURLToPath } from "url"

const __dirname = dirname(fileURLToPath(import.meta.url))
const appDir    = resolve(__dirname, "..")
const skipRes   = process.argv.includes("--skip-resources")

// ---------------------------------------------------------------------------
// Step 1 — resources (always, unless --skip-resources)
// ---------------------------------------------------------------------------

if (skipRes) {
  console.log("[dev] --skip-resources: skipping resource build.")
} else {
  console.log("[dev] Building resources (opencode-server + trie-mcp)...")
  console.log("      Use --skip-resources to skip if binaries are already current.\n")
  try {
    execSync("node scripts/build-resources.mjs", { cwd: appDir, stdio: "inherit" })
  } catch {
    console.error("\n[dev] Resource build failed. Fix the errors above and retry.")
    process.exit(1)
  }
}

// ---------------------------------------------------------------------------
// Step 2 — electron-vite preview (build + loadFile, no dev server)
// ---------------------------------------------------------------------------

console.log("\n[dev] Launching Electron (file:// — no dev server)...\n")

const evite = spawn(
  /^win/.test(process.platform) ? "npx.cmd" : "npx",
  ["electron-vite", "preview"],
  {
    cwd: appDir,
    stdio: "inherit",
    env: { ...process.env },
  }
)

evite.on("exit", (code) => process.exit(code ?? 0))
process.on("SIGINT",  () => evite.kill("SIGINT"))
process.on("SIGTERM", () => evite.kill("SIGTERM"))
