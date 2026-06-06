import { useCallback, useEffect, useRef } from "react"
import { opencodeClient } from "@/api/opencodeClient"
import { useAgentStore } from "@/store/agentStore"
import { useAppStore } from "@/store/appStore"

// Orchestrates opencode sessions for the agent panel: loads the session list on
// connect, ensures at least one session exists, lazily fetches transcript
// history when a session becomes active, and exposes new/switch/send/abort.
export function useSessions() {
  const serversReady = useAppStore((s) => s.serversReady)
  const activeId = useAgentStore((s) => s.activeId)
  const loadedRef = useRef<Set<string>>(new Set())

  const store = useAgentStore

  // Initial load: list sessions, create one if none, select the first.
  useEffect(() => {
    if (!serversReady) return
    let cancelled = false
    ;(async () => {
      const list = await opencodeClient.listSessions()
      if (cancelled) return
      if (list.length === 0) {
        const created = await opencodeClient.createSession("trie desktop")
        if (created && !cancelled) store.getState().upsertSession(created)
      } else {
        store.getState().setSessions(list)
      }
    })()
    return () => {
      cancelled = true
    }
  }, [serversReady, store])

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
    const created = await opencodeClient.createSession("New chat")
    if (created) {
      store.getState().upsertSession(created)
      store.getState().setActive(created.id)
    }
  }, [store])

  const switchSession = useCallback(
    (id: string) => {
      store.getState().setActive(id)
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

  const send = useCallback(
    async (text: string) => {
      const id = store.getState().activeId
      if (!id) return
      store.getState().appendLocalUser(id, text)
      await opencodeClient.sendMessage(id, text)
    },
    [store],
  )

  const abort = useCallback(async () => {
    const id = store.getState().activeId
    if (!id) return
    await opencodeClient.abort(id)
    store.getState().setRunning(id, false)
  }, [store])

  return { newSession, switchSession, deleteSession, send, abort }
}
