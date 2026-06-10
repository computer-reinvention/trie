import * as fs from "fs"
import * as path from "path"

// ---------------------------------------------------------------------------
// Read / merge-write the project's .opencode/opencode.json.
//
// The renderer owns the schema; main only needs to (a) read the current file so
// the settings UI can show effective values, and (b) deep-merge a delta of
// managed keys back into the file without clobbering hand-authored keys. The
// trie MCP entry is always re-asserted so user edits can't break navigation.
// ---------------------------------------------------------------------------

export interface TrieMcpEntry {
  trieMcpBin: string
  projectDir: string
}

function configPathFor(projectDir: string): string {
  return path.join(projectDir, ".opencode", "opencode.json")
}

/** Tolerant JSON parse: strips // and /* *​/ comments and trailing commas so
 *  hand-authored JSONC files still load. Returns {} on any failure. */
function parseTolerant(text: string): Record<string, unknown> {
  try {
    return JSON.parse(text) as Record<string, unknown>
  } catch {
    // best-effort JSONC: strip comments + trailing commas
    try {
      const stripped = text
        .replace(/\/\*[\s\S]*?\*\//g, "")
        .replace(/(^|[^:])\/\/.*$/gm, "$1")
        .replace(/,(\s*[}\]])/g, "$1")
      return JSON.parse(stripped) as Record<string, unknown>
    } catch {
      return {}
    }
  }
}

export function readOpencodeConfig(projectDir: string): Record<string, unknown> {
  const p = configPathFor(projectDir)
  if (!fs.existsSync(p)) return {}
  try {
    return parseTolerant(fs.readFileSync(p, "utf-8"))
  } catch {
    return {}
  }
}

function isPlainObject(v: unknown): v is Record<string, unknown> {
  return typeof v === "object" && v !== null && !Array.isArray(v)
}

/** Deep-merge `delta` into `base`. Arrays and scalars in `delta` replace the
 *  base value wholesale; objects merge recursively. A `null` value in `delta`
 *  deletes that key from the result (lets the UI clear a managed key). */
function deepMerge(
  base: Record<string, unknown>,
  delta: Record<string, unknown>,
): Record<string, unknown> {
  const out: Record<string, unknown> = { ...base }
  for (const [k, v] of Object.entries(delta)) {
    if (v === null) {
      delete out[k]
      continue
    }
    if (isPlainObject(v) && isPlainObject(out[k])) {
      out[k] = deepMerge(out[k] as Record<string, unknown>, v)
    } else {
      out[k] = v
    }
  }
  return out
}

function withTrieMcp(
  config: Record<string, unknown>,
  trie: TrieMcpEntry,
): Record<string, unknown> {
  const mcp = isPlainObject(config.mcp) ? { ...(config.mcp as Record<string, unknown>) } : {}
  mcp.trie = {
    type: "local",
    command: [trie.trieMcpBin, trie.projectDir],
    enabled: true,
  }
  return { ...config, mcp }
}

/** Merge a delta of managed keys into opencode.json and write it back,
 *  preserving unmanaged keys and always re-asserting the trie MCP entry. */
export function writeOpencodeConfig(
  projectDir: string,
  delta: Record<string, unknown>,
  trie: TrieMcpEntry,
): void {
  const configDir = path.join(projectDir, ".opencode")
  if (!fs.existsSync(configDir)) fs.mkdirSync(configDir, { recursive: true })

  const existing = readOpencodeConfig(projectDir)
  let merged = deepMerge(existing, delta)
  merged = withTrieMcp(merged, trie)

  fs.writeFileSync(configPathFor(projectDir), JSON.stringify(merged, null, 2) + "\n")
}

/** Convenience used at project-open: just ensure the trie MCP entry exists,
 *  merging with whatever is already there. Equivalent to a no-delta write. */
export function ensureTrieMcp(projectDir: string, trie: TrieMcpEntry): void {
  writeOpencodeConfig(projectDir, {}, trie)
}
