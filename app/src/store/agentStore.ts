import { create } from "zustand"
import type { TurnEvent } from "@/api/types"

interface Turn {
  id: string
  events: TurnEvent[]
  response: string
  startedAt: number
  completedAt: number
}

interface AgentStore {
  sessionId: string | null
  running: boolean
  currentTurn: TurnEvent[]
  history: Turn[]
  responseText: string
  error: string | null

  setSession: (id: string) => void
  startTurn: () => void
  appendEvent: (event: TurnEvent) => void
  appendToken: (token: string) => void
  endTurn: () => void
  failTurn: (error: string) => void
  clearError: () => void
}

export const useAgentStore = create<AgentStore>((set, get) => ({
  sessionId: null,
  running: false,
  currentTurn: [],
  history: [],
  responseText: "",
  error: null,

  setSession: (sessionId) => set({ sessionId }),

  startTurn: () =>
    set({
      running: true,
      currentTurn: [],
      responseText: "",
      error: null,
    }),

  appendEvent: (event) =>
    set((state) => ({ currentTurn: [...state.currentTurn, event] })),

  appendToken: (token) =>
    set((state) => ({ responseText: state.responseText + token })),

  endTurn: () => {
    const { currentTurn, responseText, history } = get()
    const completed: Turn = {
      id: crypto.randomUUID(),
      events: currentTurn,
      response: responseText,
      startedAt: currentTurn[0]?.timestamp ?? Date.now(),
      completedAt: Date.now(),
    }
    set({
      running: false,
      history: [completed, ...history].slice(0, 50),
      currentTurn: [],
    })
  },

  failTurn: (error) =>
    set({
      running: false,
      error,
      currentTurn: [],
    }),

  clearError: () => set({ error: null }),
}))
