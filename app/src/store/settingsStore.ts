import { create } from "zustand"
import { DEFAULTS } from "@/settings/schema"

type Value = boolean | number | string

// eslint-disable-next-line @typescript-eslint/no-explicit-any
const trie = () => (window as any).trie

interface SettingsStore {
  values: Record<string, Value>
  loaded: boolean
  load: () => Promise<void>
  get: <T extends Value>(id: string) => T
  set: (id: string, value: Value) => void
  reset: () => Promise<void>
}

export const useSettingsStore = create<SettingsStore>((set, get) => ({
  values: { ...DEFAULTS },
  loaded: false,

  load: async () => {
    try {
      const stored = (await trie().settingsGetAll()) as Record<string, Value>
      set({ values: { ...DEFAULTS, ...stored }, loaded: true })
    } catch {
      set({ values: { ...DEFAULTS }, loaded: true })
    }
    applyTheme(get().values)
  },

  get: <T extends Value>(id: string): T => (get().values[id] ?? DEFAULTS[id]) as T,

  set: (id, value) => {
    set((s) => ({ values: { ...s.values, [id]: value } }))
    applyTheme(get().values)
    trie()
      .settingsSet(id, value)
      .catch(() => {})
  },

  reset: async () => {
    try {
      await trie().settingsReset()
    } catch {
      /* best-effort */
    }
    set({ values: { ...DEFAULTS } })
    applyTheme(get().values)
  },
}))

// ---------------------------------------------------------------------------
// Apply appearance settings to the document (theme/accent/density/font-size)
// via data-attributes + CSS variables consumed by globals.css.
// ---------------------------------------------------------------------------
function applyTheme(v: Record<string, Value>): void {
  const root = document.documentElement
  root.dataset.theme = String(v["appearance.theme"] ?? "dark")
  root.dataset.accent = String(v["appearance.accent"] ?? "indigo")
  root.dataset.density = String(v["appearance.uiDensity"] ?? "comfortable")
  root.style.setProperty("--ui-font-size", `${Number(v["appearance.fontSize"] ?? 13)}px`)
  // Reduced-motion: mirror the setting to a data attribute so CSS animations
  // (spinners, pulses, message entrances) honour an explicit force-on/off, not
  // just the OS preference. "auto" defers to the @media query in globals.css.
  const rm = String(v["motion.reducedMotion"] ?? "auto")
  if (rm === "force-on") root.dataset.reducedMotion = "on"
  else if (rm === "force-off") root.dataset.reducedMotion = "off"
  else delete root.dataset.reducedMotion
}

// Convenience hook for components.
export function useSetting<T extends Value>(id: string): T {
  return useSettingsStore((s) => (s.values[id] ?? DEFAULTS[id]) as T)
}
