// Pure helpers for reading/writing dot-separated JSON pointers into an
// opencode.json-shaped object, plus building the managed-key delta that the
// store sends to the main process. Extracted from opencodeConfigStore so the
// logic is unit-testable without the Electron `window.trie` bridge.

export type Json = unknown

export function getPointer(obj: Record<string, Json>, pointer: string): Json {
  const parts = pointer.split(".")
  let cur: Json = obj
  for (const p of parts) {
    if (cur && typeof cur === "object" && !Array.isArray(cur) && p in (cur as object)) {
      cur = (cur as Record<string, Json>)[p]
    } else {
      return undefined
    }
  }
  return cur
}

/** Set (or, when value is undefined, delete) the value at `pointer`, creating
 *  intermediate objects as needed. Mutates `obj`. */
export function setPointer(obj: Record<string, Json>, pointer: string, value: Json): void {
  const parts = pointer.split(".")
  let cur = obj as Record<string, Json>
  for (let i = 0; i < parts.length - 1; i++) {
    const p = parts[i]
    if (!cur[p] || typeof cur[p] !== "object" || Array.isArray(cur[p])) cur[p] = {}
    cur = cur[p] as Record<string, Json>
  }
  const last = parts[parts.length - 1]
  if (value === undefined) delete cur[last]
  else cur[last] = value
}

/** Build the delta sent to the merge-writer: for each managed top-level key,
 *  emit its current value, or `null` when absent so the writer deletes it. */
export function buildManagedDelta(
  config: Record<string, Json>,
  managedTopKeys: readonly string[],
): Record<string, Json> {
  const delta: Record<string, Json> = {}
  for (const k of managedTopKeys) {
    delta[k] = k in config ? config[k] : null
  }
  return delta
}
