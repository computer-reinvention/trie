import { create } from "zustand"
import type { ActivityResult, ActivityStatus, ActivityPending } from "@/api/types"

// Mirrors the polled /desktop/graph/activity response. This is the cross-process
// truth about what any trie writer is doing right now (terminal sync, refresh
// hook, desktop refresh) plus the working-tree stale set. The graph glow and the
// "N stale" badge read from here; the poll hook is the only writer.

interface ActivityStore {
  status: ActivityStatus | null
  pending: ActivityPending | null
  // Wall-clock ms of the last successful poll — lets the UI fade if polling dies.
  lastPolledAt: number
  setActivity: (a: ActivityResult) => void
}

export const useActivityStore = create<ActivityStore>((set) => ({
  status: null,
  pending: null,
  lastPolledAt: 0,
  setActivity: (a) =>
    set({ status: a.status, pending: a.pending, lastPolledAt: Date.now() }),
}))
