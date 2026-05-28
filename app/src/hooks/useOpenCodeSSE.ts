import { useEffect } from "react"
import { useGraphStore } from "@/store/graphStore"
import { useAgentStore } from "@/store/agentStore"
import { graphClient } from "@/api/graphClient"
import type {
  DesktopEvent,
  DesktopToolStartEvent,
  DesktopToolDoneEvent,
  DesktopTextDeltaEvent,
  DesktopSessionStatusEvent,
  DesktopFileEditedEvent,
} from "@/api/types"

export function useOpenCodeSSE(opencodePort: number): void {
  const graphStore = useGraphStore()
  const agentStore = useAgentStore()

  useEffect(() => {
    if (!opencodePort) return

    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const trie = (window as any).trie
    const sseUrl = `http://127.0.0.1:${opencodePort}/desktop/event`

    // Subscribe via IPC proxy (renderer can't reach 127.0.0.1 directly)
    trie.sseSubscribe(sseUrl)

    const handleEvent = (rawData: string) => {
      let data: DesktopEvent
      try {
        data = JSON.parse(rawData) as DesktopEvent
      } catch {
        return
      }

      switch (data.type) {

        case "desktop.tool.start": {
          const p = data.properties as unknown as DesktopToolStartEvent
          agentStore.appendEvent({
            id: p.callID,
            type: "tool_call",
            tool: p.tool,
            input: p.input,
            timestamp: p.time.start,
          })
          handleToolStart(p, graphStore)
          break
        }

        case "desktop.tool.done": {
          const p = data.properties as unknown as DesktopToolDoneEvent
          agentStore.appendEvent({
            id: p.callID,
            type: "tool_result",
            tool: p.tool,
            input: p.input,
            output: p.output ?? undefined,
            error: p.error,
            timestamp: p.time.end,
            durationMs: p.time.end - p.time.start,
          })
          handleToolDone(p, graphStore)
          break
        }

        case "desktop.text.delta": {
          const p = data.properties as unknown as DesktopTextDeltaEvent
          agentStore.appendToken(p.delta)
          break
        }

        case "desktop.session.status": {
          const p = data.properties as unknown as DesktopSessionStatusEvent
          if (p.status.type === "idle") {
            agentStore.endTurn()
            // After idle, stale nodes may have been refreshed. We don't
            // auto-refetch prose here — the stale badge informs the user.
          } else if (p.status.type === "running") {
            agentStore.startTurn()
          } else if (p.status.type === "error") {
            agentStore.failTurn(p.status.error ?? "Unknown agent error")
          }
          break
        }

        case "desktop.file.edited": {
          const p = data.properties as unknown as DesktopFileEditedEvent
          // If the edited file is under triefacts/, the prose for its
          // corresponding symbols may have been refreshed — re-fetch.
          if (p.file.includes("triefacts/")) {
            // Derive the source path from the triefact path and re-fetch prose
            // for any currently-expanded nodes in that file.
            const match = p.file.match(/triefacts\/(.+)\.md$/)
            if (match) {
              const sourcePath = match[1]
              const expanded = useGraphStore
                .getState()
                .nodes.filter((n) => n.data.isExpanded && n.data.filePath.includes(sourcePath))
              for (const node of expanded) {
                graphClient.read(node.id).then((result) => {
                  graphStore.setNodeProse(node.id, result.prose)
                  graphStore.setNodeAgentState(node.id, "idle")
                }).catch(() => {/* best-effort */})
              }
            }
          } else {
            // Source file edited — mark its nodes stale
            graphStore.setFileAgentState(p.file, "stale")
          }
          break
        }
      }
    }

    // Register the IPC listener for events relayed from main process
    const unlisten = trie.onSseEvent(handleEvent)

    return () => {
      trie.sseUnsubscribe()
      if (typeof unlisten === "function") unlisten()
    }
  }, [opencodePort])
}

function handleToolStart(
  p: DesktopToolStartEvent,
  graphStore: ReturnType<typeof useGraphStore.getState>,
): void {
  const { tool, input } = p

  if (tool === "trie_read" && input.qname) {
    graphStore.setNodeAgentState(input.qname as string, "reading")
  } else if (tool === "trie_trace" && input.from_qname) {
    graphStore.setNodeAgentState(input.from_qname as string, "reading")
  } else if (tool === "trie_trace_flow" || tool === "trie_explain_flow") {
    if (input.symbol1) graphStore.setNodeAgentState(input.symbol1 as string, "reading")
    if (input.symbol2) graphStore.setNodeAgentState(input.symbol2 as string, "reading")
  } else if (tool === "trie_explain_symbol" && input.sym) {
    const match = graphStore.findNodeByName(input.sym as string)
    if (match) graphStore.setNodeAgentState(match.id, "reading")
  } else if (tool === "trie_patch" && input.qname) {
    graphStore.setNodeAgentState(input.qname as string, "writing")
  } else if (tool === "trie_patch_apply") {
    graphStore.nodes
      .filter((n) => n.data.agentState === "writing")
      .forEach((n) => graphStore.setNodeAgentState(n.id, "writing"))
  } else if (tool === "write_file" && input.path) {
    graphStore.setFileAgentState(input.path as string, "writing")
  } else if (tool === "str_replace_editor" && input.path) {
    graphStore.setFileAgentState(input.path as string, "writing")
  }
}

function handleToolDone(
  p: DesktopToolDoneEvent,
  graphStore: ReturnType<typeof useGraphStore.getState>,
): void {
  const { tool, input, output } = p

  if (tool === "trie_read" && input.qname) {
    // Update prose inline if output contains it
    if (output) {
      try {
        const parsed = JSON.parse(output) as { prose?: string }
        if (parsed.prose) {
          graphStore.setNodeProse(input.qname as string, parsed.prose)
        }
      } catch { /* ignore */ }
    }
    setTimeout(() => graphStore.setNodeAgentState(input.qname as string, "idle"), 800)
  } else if (tool === "trie_trace" && input.from_qname) {
    if (output) {
      try {
        const parsed = JSON.parse(output) as import("@/api/types").TraceResult
        if (parsed.nodes) graphStore.mergeTraceResult(parsed)
      } catch { /* ignore */ }
    }
    setTimeout(() => graphStore.setNodeAgentState(input.from_qname as string, "idle"), 800)
  } else if (tool === "trie_trace_flow" || tool === "trie_explain_flow") {
    if (input.symbol1) setTimeout(() => graphStore.setNodeAgentState(input.symbol1 as string, "idle"), 800)
    if (input.symbol2) setTimeout(() => graphStore.setNodeAgentState(input.symbol2 as string, "idle"), 800)
  } else if (tool === "trie_patch_apply") {
    // Re-fetch prose for all nodes that were in writing state
    const writingNodes = graphStore.nodes.filter((n) => n.data.agentState === "writing")
    for (const node of writingNodes) {
      graphClient.read(node.id).then((result) => {
        graphStore.setNodeProse(node.id, result.prose)
        graphStore.setNodeAgentState(node.id, "idle")
      }).catch(() => graphStore.setNodeAgentState(node.id, "idle"))
    }
  } else if (tool === "write_file" && input.path) {
    graphStore.setFileAgentState(input.path as string, "stale")
  } else if (tool === "str_replace_editor" && input.path) {
    graphStore.setFileAgentState(input.path as string, "stale")
  }
}
