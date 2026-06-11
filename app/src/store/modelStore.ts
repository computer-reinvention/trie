import { create } from "zustand"
import { opencodeClient } from "@/api/opencodeClient"
import type { ModelRef, OpencodeProviderInfo } from "@/api/types"

// Holds the list of available providers/models (from /config/providers) and the
// user's selected model for new turns. The selection is persisted to
// localStorage so it survives reloads; on first load it seeds from opencode's
// configured default. The selected model is threaded into sendMessage().

const SELECTED_KEY = "trie.agent.selectedModel"

interface FlatModel extends ModelRef {
  label: string
  providerLabel: string
}

interface ModelStore {
  providers: OpencodeProviderInfo[]
  flat: FlatModel[]
  selected: ModelRef | null
  loaded: boolean
  load: () => Promise<void>
  select: (m: ModelRef) => void
  labelFor: (m: ModelRef | null) => string
}

function readStored(): ModelRef | null {
  try {
    const raw = localStorage.getItem(SELECTED_KEY)
    if (!raw) return null
    const parsed = JSON.parse(raw)
    if (parsed && typeof parsed.providerID === "string" && typeof parsed.modelID === "string") {
      return { providerID: parsed.providerID, modelID: parsed.modelID }
    }
  } catch {
    /* ignore */
  }
  return null
}

function flatten(providers: OpencodeProviderInfo[]): FlatModel[] {
  const out: FlatModel[] = []
  for (const p of providers) {
    const providerLabel = p.name || p.id
    for (const [modelID, info] of Object.entries(p.models ?? {})) {
      out.push({
        providerID: p.id,
        modelID,
        label: info?.name || modelID,
        providerLabel,
      })
    }
  }
  return out
}

export const useModelStore = create<ModelStore>((set, get) => ({
  providers: [],
  flat: [],
  selected: readStored(),
  loaded: false,

  load: async () => {
    try {
      const { providers, default: defaults } = await opencodeClient.listProviders()
      const flat = flatten(providers)
      let selected = get().selected

      // Validate the stored selection still exists; otherwise seed from the
      // configured default (first provider that has one), else the first model.
      const exists = selected && flat.some((m) => m.providerID === selected!.providerID && m.modelID === selected!.modelID)
      if (!exists) {
        selected = null
        for (const p of providers) {
          const modelID = defaults[p.id]
          if (modelID && (p.models?.[modelID] || flat.some((m) => m.providerID === p.id && m.modelID === modelID))) {
            selected = { providerID: p.id, modelID }
            break
          }
        }
        if (!selected && flat.length > 0) {
          selected = { providerID: flat[0].providerID, modelID: flat[0].modelID }
        }
      }

      set({ providers, flat, selected, loaded: true })
    } catch {
      set({ loaded: true })
    }
  },

  select: (m) => {
    set({ selected: m })
    try {
      localStorage.setItem(SELECTED_KEY, JSON.stringify(m))
    } catch {
      /* ignore */
    }
  },

  labelFor: (m) => {
    if (!m) return "Default model"
    const found = get().flat.find((f) => f.providerID === m.providerID && f.modelID === m.modelID)
    return found?.label ?? m.modelID
  },
}))
