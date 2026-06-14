import { useCallback, useEffect, useRef } from "react"
import { opencodeClient } from "@/api/opencodeClient"
import { useAgentStore } from "@/store/agentStore"
import { useAppStore } from "@/store/appStore"
import { useGraphStore } from "@/store/graphStore"
import { useAGMStore } from "@/store/agmStore"
import { useModelStore } from "@/store/modelStore"
import { graphClient } from "@/api/graphClient"
import { useConductor } from "@/graph/conductor"
import { isDefaultTitle } from "@/lib/sessionTitle"

// Orchestrates opencode sessions for the agent panel:
//  - loads the session list on connect, hides empty stub chats, and selects the
//    most-recent real one (creating a fresh chat only when none exist)
//  - lazily fetches transcript history when a session becomes active
//  - exposes new/switch/delete/send/abort + a one-click "clear empty chats"
//
// Chats are NOT given a hardcoded title: opencode's title agent auto-names them
// from the first message (it only does so while the title is still its default).
export function useSessions() {
  const serversReady = useAppStore((s) => s.serversReady)
  const activeId = useAgentStore((s) => s.activeId)
  const loadedRef = useRef<Set<string>>(new Set())
  const store = useAgentStore

  // Decide which sessions are "real": a non-default title means it was used and
  // auto-named; otherwise probe for any messages. Empty stubs are hidden.
  const loadAndPrune = useCallback(async () => {
    const list = await opencodeClient.listSessions()
    if (list.length === 0) {
      const created = await opencodeClient.createSession()
      if (created) store.getState().upsertSession(created)
      return
    }
    const checks = await Promise.all(
      list.map(async (s) => {
        if (!isDefaultTitle(s.title)) return true
        try {
          return await opencodeClient.hasMessages(s.id)
        } catch {
          return false
        }
      }),
    )
    const real = list.filter((_, i) => checks[i])
    if (real.length === 0) {
      const created = await opencodeClient.createSession()
      if (created) store.getState().upsertSession(created)
      return
    }
    store.getState().setSessions(real)
  }, [store])

  useEffect(() => {
    if (!serversReady) return
    let cancelled = false
    ;(async () => {
      if (!cancelled) await loadAndPrune()
      // Populate the model switcher with the available providers/models.
      if (!cancelled) await useModelStore.getState().load()
    })()
    return () => {
      cancelled = true
    }
  }, [serversReady, loadAndPrune])

  // Lazily load history the first time a session is activated.
  useEffect(() => {
    if (!activeId || loadedRef.current.has(activeId)) return
    loadedRef.current.add(activeId)
    ;(async () => {
      const messages = await opencodeClient.getMessages(activeId)
      store.getState().setMessages(activeId, messages)
    })()
  }, [activeId, store])

  const newSession = useCallback(async () => {
    // No title — let opencode auto-name it from the first message.
    const created = await opencodeClient.createSession()
    if (created) {
      store.getState().upsertSession(created)
      store.getState().setActive(created.id)
      // A new session is fresh working memory: clear AGM live state (live mass,
      // trail, investigation). Historical-mass geography persists.
      useAGMStore.getState().resetSession()
      useGraphStore.getState().clearTrail()
    }
  }, [store])

  const switchSession = useCallback(
    (id: string) => {
      store.getState().setActive(id)
      // Switching sessions = switching working memory → reset live AGM state.
      useAGMStore.getState().resetSession()
      useGraphStore.getState().clearTrail()
    },
    [store],
  )

  const deleteSession = useCallback(
    async (id: string) => {
      await opencodeClient.deleteSession(id)
      loadedRef.current.delete(id)
      store.getState().removeSession(id)
    },
    [store],
  )

  // Delete every server-side session that has no messages (reclaims old stubs).
  const clearEmpty = useCallback(async () => {
    const list = await opencodeClient.listSessions()
    const active = store.getState().activeId
    for (const s of list) {
      if (s.id === active) continue
      if (!isDefaultTitle(s.title)) continue
      let empty = true
      try {
        empty = !(await opencodeClient.hasMessages(s.id))
      } catch {
        empty = false
      }
      if (empty) {
        await opencodeClient.deleteSession(s.id)
        loadedRef.current.delete(s.id)
        store.getState().removeSession(s.id)
      }
    }
  }, [store])

  const send = useCallback(
    async (text: string) => {
      const id = store.getState().activeId
      if (!id) return
      // New turn → reset the graph activity trail/notes + choreography FX/cues.
      useGraphStore.getState().clearTrail()
      useConductor.getState().clearTurn()
      // AGM: a user message is an explicit investigation boundary (the unit of
      // continuity, not turns). Open a new investigation labelled from the prompt
      // (user prompt first; an LLM summary could refine it later). Best-effort.
      const invId = `inv-${Date.now().toString(36)}`
      const label = text.trim().slice(0, 80) || "investigation"
      useAGMStore.getState().setInvestigation(invId, label, "active")
      graphClient.setInvestigation({ label, status: "active", investigation_id: invId }).catch(() => {})
      store.getState().appendLocalUser(id, text)
      const model = useModelStore.getState().selected ?? undefined
      try {
        await opencodeClient.sendMessage(id, text, model ? { model } : undefined)
      } catch (err) {
        // The POST failed (server down / timeout) — stop the spinner and show
        // the reason inline instead of leaving the turn hanging forever.
        store.getState().setError(id, err instanceof Error ? err.message : String(err))
      }
    },
    [store],
  )

  const abort = useCallback(async () => {
    const id = store.getState().activeId
    if (!id) return
    await opencodeClient.abort(id)
    store.getState().setRunning(id, false)
  }, [store])

  return { newSession, switchSession, deleteSession, clearEmpty, send, abort }
}
