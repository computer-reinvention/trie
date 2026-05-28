import { create } from "zustand"

interface AppStore {
  projectDir: string | null
  projectName: string
  totalSymbols: number
  totalFiles: number

  opencodePort: number | null
  serversReady: boolean

  provider: string
  modelId: string
  apiKeySet: boolean

  graphLoading: boolean
  graphLoadingMessage: string

  setProject: (dir: string, name: string, totalSymbols: number, totalFiles: number) => void
  setServers: (ports: { opencodePort: number; projectDir: string }) => void
  setModel: (provider: string, modelId: string) => void
  setApiKeySet: (set: boolean) => void
  setGraphLoading: (loading: boolean, message?: string) => void
}

export const useAppStore = create<AppStore>((set) => ({
  projectDir: null,
  projectName: "",
  totalSymbols: 0,
  totalFiles: 0,

  opencodePort: null,
  serversReady: false,

  provider: "anthropic",
  modelId: "claude-sonnet-4-6",
  apiKeySet: false,

  graphLoading: false,
  graphLoadingMessage: "",

  setProject: (projectDir, projectName, totalSymbols, totalFiles) =>
    set({ projectDir, projectName, totalSymbols, totalFiles }),

  setServers: ({ opencodePort }) =>
    set({ opencodePort, serversReady: true }),

  setModel: (provider, modelId) => set({ provider, modelId }),

  setApiKeySet: (apiKeySet) => set({ apiKeySet }),

  setGraphLoading: (graphLoading, graphLoadingMessage = "") =>
    set({ graphLoading, graphLoadingMessage }),
}))
