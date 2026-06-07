import { useCallback, useEffect } from "react"
import { graphClient } from "@/api/graphClient"
import { usePatchesStore } from "@/store/patchesStore"
import { useAppStore } from "@/store/appStore"
import type { ApplyReport } from "@/api/types"

const POLL_MS = 2500

// Polls pending patches and exposes drop/apply. Refreshes immediately after a
// mutating action so the panel + graph reflect changes without waiting a tick.
export function usePatches() {
  const enabled = useAppStore((s) => s.serversReady)
  const setPatches = usePatchesStore((s) => s.setPatches)
  const setError = usePatchesStore((s) => s.setError)

  const refresh = useCallback(async () => {
    try {
      const res = await graphClient.patches()
      setPatches(res.patches ?? [], {
        sessionNote: res.session_note,
        applyInProgress: res.apply_in_progress,
      })
    } catch {
      // best-effort poll
    }
  }, [setPatches])

  useEffect(() => {
    if (!enabled) return
    let cancelled = false
    let timer: ReturnType<typeof setTimeout> | null = null
    const tick = async () => {
      if (cancelled) return
      await refresh()
      if (!cancelled) timer = setTimeout(tick, POLL_MS)
    }
    tick()
    return () => {
      cancelled = true
      if (timer) clearTimeout(timer)
    }
  }, [enabled, refresh])

  const drop = useCallback(
    async (qname?: string) => {
      try {
        await graphClient.patchDrop(qname)
      } finally {
        refresh()
      }
    },
    [refresh],
  )

  const apply = useCallback(async (): Promise<ApplyReport | null> => {
    setError(null)
    usePatchesStore.getState().setApplyProgress({ phase: "applying", done: 0, total: 0 })
    try {
      const report = await graphClient.patchApply()
      if (report?.error?.message) setError(report.error.message)
      return report
    } catch (e) {
      setError(String(e))
      return null
    } finally {
      usePatchesStore.getState().setApplyProgress(null)
      refresh()
    }
  }, [refresh, setError])

  return { refresh, drop, apply }
}
