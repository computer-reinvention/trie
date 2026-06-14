import { create } from "zustand"
import { TRIE_MANAGED_TOP_KEYS } from "@/settings/trieSchema"
import { getPointer, setPointer, buildManagedDelta, type Json } from "@/settings/configPointer"

// eslint-disable-next-line @typescript-eslint/no-explicit-any
const trie = () => (window as any).trie

// Read/modify/write of the project's trie.toml, restricted to the tables the app
// manages. Mirrors opencodeConfigStore: keeps the full parsed config as a
// working copy so the UI reads effective values; on save it sends only the
// managed top-level tables back to main, which deep-merges them (preserving
// everything else, including hand-authored keys).

interface TrieConfigStore {
  projectDir: string | null
  config: Record<string, Json>
  /** Whether trie.toml exists on disk; when false the UI prompts to init. */
  exists: boolean
  loaded: boolean
  saving: boolean
  lastError: string | null
  load: (projectDir: string) => Promise<void>
  getValue: (pointer: string) => Json
  setValue: (pointer: string, value: Json) => void
  save: () => Promise<void>
}

let saveTimer: ReturnType<typeof setTimeout> | null = null

export const useTrieConfigStore = create<TrieConfigStore>((set, get) => ({
  projectDir: null,
  config: {},
  exists: false,
  loaded: false,
  saving: false,
  lastError: null,

  load: async (projectDir) => {
    set({ loaded: false, projectDir, lastError: null })
    try {
      const res = (await trie().trieConfig.read(projectDir)) as {
        exists: boolean
        config: Record<string, Json>
      }
      set({ config: res?.config ?? {}, exists: Boolean(res?.exists), loaded: true })
    } catch {
      set({ config: {}, exists: false, loaded: true })
    }
  },

  getValue: (pointer) => getPointer(get().config, pointer),

  setValue: (pointer, value) => {
    const config = structuredClone(get().config)
    setPointer(config, pointer, value)
    set({ config })
    // debounce the write
    if (saveTimer) clearTimeout(saveTimer)
    saveTimer = setTimeout(() => get().save(), 400)
  },

  save: async () => {
    const { projectDir, config, exists } = get()
    if (!projectDir || !exists) return
    const delta = buildManagedDelta(config, TRIE_MANAGED_TOP_KEYS)
    set({ saving: true, lastError: null })
    try {
      const res = (await trie().trieConfig.write(projectDir, delta)) as {
        ok: boolean
        error?: string
      }
      if (!res?.ok) set({ lastError: res?.error ?? "Failed to write trie.toml" })
    } catch (err) {
      set({ lastError: String(err) })
    }
    set({ saving: false })
  },
}))
