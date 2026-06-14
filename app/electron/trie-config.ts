import * as fs from "fs"
import * as path from "path"
import TOML from "@iarna/toml"

// ---------------------------------------------------------------------------
// Read / merge-write the project's trie.toml.
//
// Mirrors opencode-config.ts but for trie's own configuration. The renderer
// owns the schema; main only (a) reads the parsed config so the settings UI can
// show effective values, and (b) deep-merges a delta of changed keys back into
// the file, preserving hand-authored keys, comments are NOT preserved (TOML
// round-tripping with comments is lossy) — we accept that trade-off because the
// settings UI becomes the source of truth for managed keys and the defaults are
// reproducible via `trie init`.
// ---------------------------------------------------------------------------

function configPathFor(projectDir: string): string {
  return path.join(projectDir, "trie.toml")
}

export function trieConfigExists(projectDir: string): boolean {
  return fs.existsSync(configPathFor(projectDir))
}

export function readTrieConfig(projectDir: string): Record<string, unknown> {
  const p = configPathFor(projectDir)
  if (!fs.existsSync(p)) return {}
  try {
    return TOML.parse(fs.readFileSync(p, "utf-8")) as Record<string, unknown>
  } catch {
    return {}
  }
}

export function isPlainObject(v: unknown): v is Record<string, unknown> {
  return typeof v === "object" && v !== null && !Array.isArray(v)
}

/** Deep-merge `delta` into `base`. Arrays and scalars in `delta` replace the
 *  base value wholesale; objects merge recursively. A `null` value in `delta`
 *  deletes that key (lets the UI clear a managed key back to trie's default). */
export function deepMerge(
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

/** Merge a delta into trie.toml and write it back. Refuses to create a brand
 *  new trie.toml — that's `trie init`'s job (which also builds the graph). When
 *  the file is missing we throw so the caller can prompt the user to init. */
export function writeTrieConfig(
  projectDir: string,
  delta: Record<string, unknown>,
): void {
  const p = configPathFor(projectDir)
  if (!fs.existsSync(p)) {
    throw new Error("trie.toml not found — run `trie init` first.")
  }
  const existing = readTrieConfig(projectDir)
  const merged = deepMerge(existing, delta)
  // @iarna/toml refuses `undefined`; deepMerge already stripped null deletions,
  // but guard against any stray undefined leaking into the tree.
  fs.writeFileSync(p, TOML.stringify(stripUndefined(merged) as TOML.JsonMap))
}

/** Recursively drop keys whose value is `undefined` so the TOML serializer
 *  (which throws on undefined) always receives a clean object. */
export function stripUndefined(value: unknown): unknown {
  if (Array.isArray(value)) return value.map(stripUndefined)
  if (isPlainObject(value)) {
    const out: Record<string, unknown> = {}
    for (const [k, v] of Object.entries(value)) {
      if (v === undefined) continue
      out[k] = stripUndefined(v)
    }
    return out
  }
  return value
}
