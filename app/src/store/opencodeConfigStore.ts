import { create } from "zustand"
import { MANAGED_TOP_KEYS } from "@/settings/opencodeSchema"

// eslint-disable-next-line @typescript-eslint/no-explicit-any
const trie = () => (window as any).trie

type Json = unknown

// Read/modify/write of the project's opencode.json, restricted to the keys the
// app manages. The store keeps the full parsed config as a working copy so the
// UI can read effective values; on save it sends only the managed top-level
// keys back to main, which deep-merges them (preserving everything else).

function getPointer(obj: Record<string, Json>, pointer: string): Json {
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

function setPointer(obj: Record<string, Json>, pointer: string, value: Json): void {
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

interface OpencodeConfigStore {
  projectDir: string | null
  config: Record<string, Json>
  loaded: boolean
  saving: boolean
  dirtyRestart: boolean
  load: (projectDir: string) => Promise<void>
  getValue: (pointer: string) => Json
  setValue: (pointer: string, value: Json, restart?: boolean) => void
  save: () => Promise<void>
  restart: () => Promise<void>
}

let saveTimer: ReturnType<typeof setTimeout> | null = null

export const useOpencodeConfigStore = create<OpencodeConfigStore>((set, get) => ({
  projectDir: null,
  config: {},
  loaded: false,
  saving: false,
  dirtyRestart: false,

  load: async (projectDir) => {
    set({ loaded: false, projectDir })
    try {
      const cfg = (await trie().opencodeConfig.read(projectDir)) as Record<string, Json>
      set({ config: cfg ?? {}, loaded: true, dirtyRestart: false })
    } catch {
      set({ config: {}, loaded: true })
    }
  },

  getValue: (pointer) => getPointer(get().config, pointer),

  setValue: (pointer, value, restart) => {
    const config = structuredClone(get().config)
    setPointer(config, pointer, value)
    set((s) => ({ config, dirtyRestart: s.dirtyRestart || Boolean(restart) }))
    // debounce the write
    if (saveTimer) clearTimeout(saveTimer)
    saveTimer = setTimeout(() => get().save(), 400)
  },

  save: async () => {
    const { projectDir, config } = get()
    if (!projectDir) return
    // Send only the managed top-level keys as the delta. Keys absent from the
    // working copy are sent as null so the merge-writer deletes them (e.g. the
    // user cleared a managed value).
    const delta: Record<string, Json> = {}
    for (const k of MANAGED_TOP_KEYS) {
      delta[k] = k in config ? config[k] : null
    }
    set({ saving: true })
    try {
      await trie().opencodeConfig.write(projectDir, delta)
    } catch {
      /* best-effort */
    }
    set({ saving: false })
  },

  restart: async () => {
    try {
      await trie().opencodeConfig.restart()
      set({ dirtyRestart: false })
    } catch {
      /* best-effort */
    }
  },
}))
