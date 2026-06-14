import { create } from "zustand"

// Tracks the health of the opencode sidecar + its event stream, so the UI can
// tell the user when the agent backend has died or the stream dropped instead
// of silently appearing to hang.
//
// Status transitions:
//   connecting → live      once servers-ready fires
//   live       → degraded  when the SSE stream errors but the process is alive
//   live       → crashed   when the opencode process exits unexpectedly
//   crashed    → live      after a restart re-emits servers-ready
export type ConnectionStatus = "connecting" | "live" | "degraded" | "crashed"

interface ConnectionStore {
  status: ConnectionStatus
  /** Last process exit code, if it crashed. */
  exitCode: number | null
  /** Most recent stderr/SSE error line, for diagnostics. */
  lastError: string | null

  setLive: () => void
  setDegraded: (error?: string) => void
  setCrashed: (code: number | null, error?: string) => void
  noteError: (line: string) => void
}

export const useConnectionStore = create<ConnectionStore>((set) => ({
  status: "connecting",
  exitCode: null,
  lastError: null,

  setLive: () => set({ status: "live", exitCode: null }),

  setDegraded: (error) =>
    // Don't downgrade a crashed connection to merely degraded — a crash is the
    // stronger signal and an SSE error is its expected side-effect.
    set((s) =>
      s.status === "crashed"
        ? { lastError: error ?? s.lastError }
        : { status: "degraded", lastError: error ?? s.lastError },
    ),

  setCrashed: (code, error) =>
    set({ status: "crashed", exitCode: code, lastError: error ?? null }),

  noteError: (line) => set({ lastError: line }),
}))
