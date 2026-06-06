import { useEffect, useRef } from "react"
import { useGraphStore } from "@/store/graphStore"
import { useAgentStore } from "@/store/agentStore"
import { useTabsStore, GRAPH_TAB_ID } from "@/store/tabsStore"
import { useSettingsStore } from "@/store/settingsStore"
import { choreographFor } from "@/graph/agentChoreography"
import type { ToolPart } from "@/api/types"

// Bridges the opencode event bus (the general /event SSE stream) to the
// transcript store and the live graph.
//
// We subscribe to the raw bus stream rather than the /desktop/event mapped
// stream: the raw stream is the battle-tested one (heartbeats + every publish),
// and doing the mapping here keeps a single source of truth. Bus events we use:
//   message.part.updated  -> transcript part upsert + graph choreography
//   message.part.delta    -> streaming text / reasoning (split by `field`)
//   message.updated       -> assistant cost/tokens/finish/error
//   session.status        -> running / idle  (busy => running)
//   session.error         -> chat error
//   permission.asked/.replied -> inline approve-deny
//   file.edited           -> mark graph nodes stale
//
// Tool activity colours nodes (read=blue, scan=violet, write=amber), animates
// flow comets, and — when graph.followAgent is on — expands + softly centres the
// symbol the agent is focused on (debounced so grep bursts never thrash).
export function useOpenCodeSSE(opencodePort: number): void {
  const followQueue = useRef<string | null>(null)
  const followTimer = useRef<ReturnType<typeof setTimeout> | null>(null)

  useEffect(() => {
    if (!opencodePort) return

    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const trie = (window as any).trie
    // Raw bus stream — carries all publishes; no directory needed.
    const sseUrl = `http://127.0.0.1:${opencodePort}/event`
    trie.sseSubscribe(sseUrl)

    const graph = () => useGraphStore.getState()
    const agent = () => useAgentStore.getState()
    const settings = () => useSettingsStore.getState()

    const scheduleFollow = (qname: string) => {
      if (!settings().get<boolean>("graph.followAgent")) return
      followQueue.current = qname
      if (followTimer.current) clearTimeout(followTimer.current)
      followTimer.current = setTimeout(() => {
        const q = followQueue.current
        followQueue.current = null
        if (!q) return
        const ok = graph().revealSymbol(q)
        if (ok && settings().get<boolean>("agent.autoSwitchToGraph")) {
          useTabsStore.getState().activate(GRAPH_TAB_ID)
        }
      }, 250)
    }

    const applyChoreography = (part: ToolPart) => {
      const g = graph()
      const c = choreographFor(part)
      for (const q of c.reads) {
        g.setNodeAgentState(q, "reading")
        g.bumpActivity(q, 0.8)
      }
      for (const q of c.scans) {
        g.setNodeAgentState(q, "scanning")
        g.bumpActivity(q, 0.5)
      }
      for (const q of c.writes) {
        g.setNodeAgentState(q, "writing")
        g.bumpActivity(q, 1)
      }
      for (const f of c.files) g.setFileAgentState(f, "writing")
      c.flows.slice(0, 40).forEach((e, i) => setTimeout(() => g.flowAlong(e.from, e.to), i * 160))
      if (c.follow) scheduleFollow(c.follow)
      if (part.state.status === "completed" || part.state.status === "error") {
        const settle = [...c.reads, ...c.scans]
        setTimeout(() => settle.forEach((q) => g.setNodeAgentState(q, "idle")), 900)
        for (const f of c.files) g.setFileAgentState(f, "stale")
      }
    }

    const handleEvent = (rawData: string) => {
      let ev: { type: string; properties: Record<string, unknown> }
      try {
        ev = JSON.parse(rawData) as { type: string; properties: Record<string, unknown> }
      } catch {
        return
      }
      const a = agent()
      const p = ev.properties ?? {}

      switch (ev.type) {
        case "message.part.updated": {
          // eslint-disable-next-line @typescript-eslint/no-explicit-any
          const part = (p as any).part
          if (!part) break
          a.applyPartUpdated(part.sessionID, part.messageID, part)
          if (part.type === "tool") applyChoreography(part as ToolPart)
          break
        }
        case "message.part.delta": {
          // eslint-disable-next-line @typescript-eslint/no-explicit-any
          const pp = p as any
          if (pp.field === "text")
            a.applyTextDelta(pp.sessionID, pp.messageID, pp.partID, pp.delta)
          else if (pp.field === "reasoning")
            a.applyReasoningDelta(pp.sessionID, pp.messageID, pp.partID, pp.delta)
          break
        }
        case "message.updated": {
          // eslint-disable-next-line @typescript-eslint/no-explicit-any
          const info = (p as any).info
          if (info) a.applyMessageInfo(info.sessionID, info)
          break
        }
        case "session.status": {
          // eslint-disable-next-line @typescript-eslint/no-explicit-any
          const status = (p as any).status
          const sid = (p as any).sessionID
          if (!status || !sid) break
          if (status.type === "idle") a.setRunning(sid, false)
          else if (status.type === "busy") a.setRunning(sid, true)
          break
        }
        case "session.idle": {
          // eslint-disable-next-line @typescript-eslint/no-explicit-any
          const sid = (p as any).sessionID
          if (sid) a.setRunning(sid, false)
          break
        }
        case "session.error": {
          // eslint-disable-next-line @typescript-eslint/no-explicit-any
          const pp = p as any
          const msg = pp.error?.data?.message ?? pp.error?.message ?? "Agent error"
          if (pp.sessionID) a.setError(pp.sessionID, msg)
          break
        }
        case "file.edited": {
          // eslint-disable-next-line @typescript-eslint/no-explicit-any
          const file = (p as any).file as string | undefined
          if (file && !file.includes("triefacts/")) graph().setFileAgentState(file, "stale")
          break
        }
        case "permission.asked": {
          // eslint-disable-next-line @typescript-eslint/no-explicit-any
          const pp = p as any
          a.addPermission({
            id: pp.id,
            sessionID: pp.sessionID,
            permission: pp.permission,
            patterns: pp.patterns ?? [],
            metadata: pp.metadata ?? {},
            always: pp.always ?? [],
            callID: pp.tool?.callID,
            messageID: pp.tool?.messageID,
          })
          break
        }
        case "permission.replied": {
          // eslint-disable-next-line @typescript-eslint/no-explicit-any
          const pp = p as any
          if (pp.sessionID && pp.requestID) a.removePermission(pp.sessionID, pp.requestID)
          break
        }
      }
    }

    const unlisten = trie.onSseEvent(handleEvent)
    return () => {
      trie.sseUnsubscribe()
      if (typeof unlisten === "function") unlisten()
      if (followTimer.current) clearTimeout(followTimer.current)
    }
  }, [opencodePort])
}
