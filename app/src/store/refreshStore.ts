import { create } from "zustand"

// Mirrors the JSONL events emitted by `trie refresh --json` (see
// trie/cli.py::_JsonlProgress and emit_jsonl_event), plus a few lifecycle
// events the process-manager adds around the stream.
export type RefreshEvent =
  | { kind: "spawned" }
  | { kind: "phase"; phase: string; mode: string }
  | { kind: "start"; rel_path: string; idx: number; total: number }
  | { kind: "done"; rel_path: string; symbols: number; running_cost_usd: number }
  | { kind: "skip"; rel_path: string; reason: string }
  | {
      kind: "summary"
      mode: string
      refreshed: boolean
      reason: string
      files_synced: number
      cost_usd: number
    }
  | { kind: "error"; message: string }
  | { kind: "exit"; code: number; stderr?: string }

export type RefreshPhase = "idle" | "running" | "done" | "error"

interface RefreshStore {
  phase: RefreshPhase
  // Human-readable reason from the freshness gate (empty_store, head_moved, …).
  reason: string | null
  // Per-file sync progress (only populated when a sync actually fires).
  current: string | null
  done: number
  total: number
  runningCostUsd: number
  filesSynced: number
  errorMessage: string | null
  // Whether the last run actually changed the graph (drives a graph re-fetch).
  refreshed: boolean

  apply: (event: RefreshEvent) => void
  reset: () => void
}

const initial = {
  phase: "idle" as RefreshPhase,
  reason: null as string | null,
  current: null as string | null,
  done: 0,
  total: 0,
  runningCostUsd: 0,
  filesSynced: 0,
  errorMessage: null as string | null,
  refreshed: false,
}

export const useRefreshStore = create<RefreshStore>((set) => ({
  ...initial,

  apply: (event) =>
    set((s) => {
      switch (event.kind) {
        case "spawned":
        case "phase":
          return { phase: "running", errorMessage: null }
        case "start":
          return { phase: "running", current: event.rel_path, total: event.total }
        case "done":
          return {
            done: s.done + 1,
            current: null,
            runningCostUsd: event.running_cost_usd,
          }
        case "skip":
          return { done: s.done + 1, current: null }
        case "summary":
          return {
            reason: event.reason,
            refreshed: event.refreshed,
            filesSynced: event.files_synced,
            runningCostUsd: Math.max(s.runningCostUsd, event.cost_usd),
          }
        case "error":
          return { phase: "error", errorMessage: event.message }
        case "exit":
          // A non-zero exit without a prior summary is an error; otherwise the
          // summary already set the terminal state and we just settle to done.
          if (event.code !== 0 && s.phase !== "error") {
            return { phase: "error", errorMessage: event.stderr || `exited ${event.code}` }
          }
          return { phase: s.phase === "error" ? "error" : "done", current: null }
        default:
          return {}
      }
    }),

  reset: () => set({ ...initial }),
}))
