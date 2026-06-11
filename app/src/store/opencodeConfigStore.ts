import { create } from "zustand"
import { MANAGED_TOP_KEYS } from "@/settings/opencodeSchema"
import { getPointer, setPointer, buildManagedDelta, type Json } from "@/settings/configPointer"

// eslint-disable-next-line @typescript-eslint/no-explicit-any
const trie = () => (window as any).trie

// Read/modify/write of the project's opencode.json, restricted to the keys the
// app manages. The store keeps the full parsed config as a working copy so the
// UI can read effective values; on save it sends only the managed top-level
// keys back to main, which deep-merges them (preserving everything else).

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
    const delta = buildManagedDelta(config, MANAGED_TOP_KEYS)
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
