import { useEffect, useRef } from "react"
import { graphClient } from "@/api/graphClient"
import { useActivityStore } from "@/store/activityStore"
import { useGraphStore } from "@/store/graphStore"

// Polls the cross-process activity DB and projects it onto the graph:
//   - the file currently being written glows ("writing")
//   - every stale (pending) file glows ("stale")
//   - everything we previously glowed but is no longer active/stale resets
//
// One interval owns all of this; nothing else writes agentState from activity.

const POLL_MS = 1500
// Re-apply the active file's pulse faster than it decays so the glow holds
// steady instead of strobing between polls.
const SUSTAIN_MS = 300

export function useActivityPoll(enabled: boolean) {
  const setActivity = useActivityStore((s) => s.setActivity)
  // Files we've applied a non-idle state to, so we can reset them next tick.
  const glowed = useRef<Set<string>>(new Set())
  // The file an external writer is currently regenerating (for the sustain loop).
  const currentFile = useRef<string | null>(null)

  useEffect(() => {
    if (!enabled) return
    let cancelled = false
    let pollTimer: ReturnType<typeof setTimeout> | null = null

    const graph = useGraphStore.getState
    const setFileAgentState = graph().setFileAgentState
    const setFileActivity = graph().setFileActivity

    const reconcile = () => {
      const { status, pending } = useActivityStore.getState()
      const next = new Set<string>()

      if (pending) for (const f of pending.stale) next.add(f)
      const current = status?.is_active ? status.current_file : null
      currentFile.current = current ?? null

      // Reset files that dropped out of the glow set.
      for (const f of glowed.current) {
        if (!next.has(f) && f !== current) {
          setFileAgentState(f, "idle")
          setFileActivity(f, 0)
        }
      }
      for (const f of next) setFileAgentState(f, f === current ? "writing" : "stale")
      if (current) {
        setFileAgentState(current, "writing")
        next.add(current)
      }
      glowed.current = next
    }

    const poll = async () => {
      try {
        const a = await graphClient.activity()
        if (cancelled) return
        setActivity(a)
        reconcile()
      } catch {
        // Polling is best-effort; a transient failure just skips a frame.
      }
      if (!cancelled) pollTimer = setTimeout(poll, POLL_MS)
    }

    // Sustain loop: keep the active file's nodes pulsing between polls.
    const sustain = setInterval(() => {
      if (currentFile.current) setFileActivity(currentFile.current, 0.85)
    }, SUSTAIN_MS)

    poll()
    return () => {
      cancelled = true
      if (pollTimer) clearTimeout(pollTimer)
      clearInterval(sustain)
      for (const f of glowed.current) {
        setFileAgentState(f, "idle")
        setFileActivity(f, 0)
      }
      glowed.current = new Set()
      currentFile.current = null
    }
  }, [enabled, setActivity])
}
