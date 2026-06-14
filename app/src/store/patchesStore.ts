import { create } from "zustand"
import type { PatchEntry, ApplyProgress } from "@/api/types"

// Pending patch state for the desktop. Polled from /desktop/graph/patches; the
// derived `patchedQnames` set lets the graph mark symbols that have staged edits.
// Apply progress is fed from the activity poll (cascade-plan: activity().apply).

interface PatchesStore {
  patches: PatchEntry[]
  sessionNote: string | null
  applyInProgress: boolean
  applyProgress: ApplyProgress | null
  patchedQnames: Set<string>
  lastError: string | null

  setPatches: (patches: PatchEntry[], opts?: { sessionNote?: string; applyInProgress?: boolean }) => void
  setApplyProgress: (p: ApplyProgress | null) => void
  setError: (msg: string | null) => void
}

export const usePatchesStore = create<PatchesStore>((set) => ({
  patches: [],
  sessionNote: null,
  applyInProgress: false,
  applyProgress: null,
  patchedQnames: new Set(),
  lastError: null,

  setPatches: (patches, opts) =>
    set({
      patches,
      patchedQnames: new Set(patches.map((p) => p.qname)),
      ...(opts?.sessionNote !== undefined ? { sessionNote: opts.sessionNote } : {}),
      ...(opts?.applyInProgress !== undefined ? { applyInProgress: opts.applyInProgress } : {}),
    }),

  setApplyProgress: (applyProgress) =>
    set({ applyProgress, applyInProgress: applyProgress != null }),

  setError: (lastError) => set({ lastError }),
}))
