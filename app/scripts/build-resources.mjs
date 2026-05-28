#!/usr/bin/env node
/**
 * Build the bundled sidecar binaries for the trie desktop app.
 *
 * Produces:
 *   resources/opencode-server   — bun-compiled opencode server binary
 *   resources/trie-mcp          — pyinstaller-compiled trie MCP server binary
 *
 * Run: npm run build:resources  (from app/)
 */

import { execFileSync, execSync } from "child_process"
import { existsSync, chmodSync, mkdirSync } from "fs"
import { resolve, dirname } from "path"
import { fileURLToPath } from "url"
import { homedir } from "os"

const __dirname = dirname(fileURLToPath(import.meta.url))
const appDir    = resolve(__dirname, "..")
const repoRoot  = resolve(appDir, "..")
const resDir    = resolve(appDir, "resources")
const forkDir   = resolve(repoRoot, "opencode", "packages", "opencode")

mkdirSync(resDir, { recursive: true })

// ---------------------------------------------------------------------------
// 1. opencode-server — bun --compile
// ---------------------------------------------------------------------------
console.log("\n[1/2] Building opencode-server (bun --compile)...")

if (!existsSync(resolve(forkDir, "src", "server-entry.ts"))) {
  console.error(`opencode fork not found at ${forkDir}`)
  console.error("Run: git submodule update --init")
  process.exit(1)
}

function findBun() {
  const candidates = ["bun", resolve(homedir(), ".bun", "bin", "bun")]
  for (const c of candidates) {
    try { execFileSync(c, ["--version"], { stdio: "ignore" }); return c } catch {}
  }
  return null
}

const bun = findBun()
if (!bun) {
  console.error("bun not found. Install: curl -fsSL https://bun.sh/install | bash")
  process.exit(1)
}

// Ensure fork deps are installed
console.log("  Installing opencode fork deps...")
execFileSync(bun, ["install", "--ignore-scripts"], { cwd: forkDir, stdio: "inherit" })

// Build the OPENCODE_MIGRATIONS define value by reading migration SQL files
import { readdirSync, readFileSync } from "fs"

const migrationDir = resolve(forkDir, "migration")
const migrationEntries = readdirSync(migrationDir, { withFileTypes: true })
  .filter(e => e.isDirectory())
  .map(e => e.name)
  .sort()
  .map(name => {
    const sqlFile = resolve(migrationDir, name, "migration.sql")
    const sql = existsSync(sqlFile) ? readFileSync(sqlFile, "utf-8") : ""
    // Parse timestamp from directory name (YYYYMMDDHHmmss prefix)
    const m = /^(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})/.exec(name)
    const timestamp = m
      ? Date.UTC(+m[1], +m[2]-1, +m[3], +m[4], +m[5], +m[6])
      : 0
    return { sql, timestamp, name }
  })

// bun --define treats the value as a JS expression, not a string literal.
// JSON.stringify(array) produces valid JSON which is also valid JS array literal.
// Double-stringifying (the old code) produced a string literal at runtime instead of an array.
const migrationsDefine = JSON.stringify(migrationEntries)

console.log("  Compiling opencode-server binary...")
execFileSync(
  bun,
  [
    "build",
    "--compile",
    `--outfile=${resolve(resDir, "opencode-server")}`,
    "--target=bun",
    "--conditions=browser",
    `--define=OPENCODE_MIGRATIONS=${migrationsDefine}`,
    "--define=OPENCODE_VERSION='0.0.0-desktop'",
    "--define=OPENCODE_CHANNEL='stable'",
    "--define=OPENCODE_LIBC=''",
    "./src/server-entry.ts",
  ],
  { cwd: forkDir, stdio: "inherit" }
)
chmodSync(resolve(resDir, "opencode-server"), 0o755)
console.log(`  ✓ resources/opencode-server`)

// ---------------------------------------------------------------------------
// 2. trie-mcp — pyinstaller
// ---------------------------------------------------------------------------
console.log("\n[2/2] Building trie-mcp (pyinstaller)...")

const entryScript = resolve(repoRoot, "trie_mcp_entry.py")
if (!existsSync(entryScript)) {
  console.error(`trie_mcp_entry.py not found at ${entryScript}`)
  process.exit(1)
}

// Use uv run to get pyinstaller from the trie project venv
try {
  execSync(
    [
      "uv run pyinstaller",
      "--onefile",
      "--name trie-mcp",
      `--distpath ${resDir}`,
      `--workpath ${resolve(resDir, ".pyinstaller-work")}`,
      `--specpath ${resolve(resDir, ".pyinstaller-work")}`,
      "--clean",
      "--noconfirm",
      entryScript,
    ].join(" "),
    { cwd: repoRoot, stdio: "inherit" }
  )
  chmodSync(resolve(resDir, "trie-mcp"), 0o755)
  console.log(`  ✓ resources/trie-mcp`)
} catch (err) {
  console.error("pyinstaller failed:", err.message)
  process.exit(1)
}

console.log("\n✓ All resources built. Ready to npm run build / npm run dist.\n")
