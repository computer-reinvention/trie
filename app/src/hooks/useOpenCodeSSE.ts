import { useEffect } from "react"
import { useGraphStore } from "@/store/graphStore"
import { useAgentStore } from "@/store/agentStore"
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
          // corresponding symbols may have been refreshed. We don't re-fetch
          // prose here (the inspector loads it on demand); just mark stale.
          if (!p.file.includes("triefacts/")) {
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

// Map agent tool calls onto the graph's live runtime. Reading a symbol breathes
// it blue (reading); writing pulses amber. The richer comet/heat choreography
// lands in the live-monitor pass; this is the grounded baseline.
function handleToolStart(
  p: DesktopToolStartEvent,
  graphStore: ReturnType<typeof useGraphStore.getState>,
): void {
  const { tool, input } = p
  const read = (q: string) => {
    graphStore.setNodeAgentState(q, "reading")
    graphStore.bumpActivity(q, 0.8)
  }
  if (tool === "trie_read" && input.qname) read(input.qname as string)
  else if (tool === "trie_trace" && input.from_qname) read(input.from_qname as string)
  else if (tool === "trie_trace_flow" || tool === "trie_explain_flow") {
    if (input.symbol1) read(input.symbol1 as string)
    if (input.symbol2) read(input.symbol2 as string)
  } else if (tool === "trie_patch" && input.qname) {
    graphStore.setNodeAgentState(input.qname as string, "writing")
    graphStore.bumpActivity(input.qname as string, 1)
  } else if (tool === "write_file" && input.path) {
    graphStore.setFileAgentState(input.path as string, "writing")
  } else if (tool === "str_replace_editor" && input.path) {
    graphStore.setFileAgentState(input.path as string, "writing")
  }
}

// Fire directional comets along traversed edges, in sequence, so the user
// watches the agent's attention flow through the call graph.
function animateFlows(
  output: string | null,
  graphStore: ReturnType<typeof useGraphStore.getState>,
): void {
  if (!output) return
  let edges: Array<{ from: string; to: string }> = []
  try {
    const parsed = JSON.parse(output) as {
      edges?: Array<{ from: string; to: string }>
      paths?: string[][]
    }
    if (parsed.edges) edges = parsed.edges
    else if (parsed.paths) {
      // explain/trace_flow returns paths (lists of qnames) -> consecutive edges
      for (const path of parsed.paths) {
        for (let i = 0; i + 1 < path.length; i++) edges.push({ from: path[i], to: path[i + 1] })
      }
    }
  } catch {
    return
  }
  edges.slice(0, 40).forEach((e, i) => {
    setTimeout(() => graphStore.flowAlong(e.from, e.to), i * 180)
  })
}

function handleToolDone(
  p: DesktopToolDoneEvent,
  graphStore: ReturnType<typeof useGraphStore.getState>,
): void {
  const { tool, input, output } = p
  const settle = (q: string) => setTimeout(() => graphStore.setNodeAgentState(q, "idle"), 800)

  if (tool === "trie_read" && input.qname) settle(input.qname as string)
  else if (tool === "trie_trace" && input.from_qname) {
    animateFlows(output, graphStore)
    settle(input.from_qname as string)
  } else if (tool === "trie_trace_flow" || tool === "trie_explain_flow") {
    animateFlows(output, graphStore)
    if (input.symbol1) settle(input.symbol1 as string)
    if (input.symbol2) settle(input.symbol2 as string)
  } else if (tool === "write_file" && input.path) {
    graphStore.setFileAgentState(input.path as string, "stale")
    // residual edit heat that lingers (persistent monitor dimension)
    const m = graphStore.model
    if (m) {
      for (const n of m.nodes) {
        if (n.file_path === input.path || n.file_path.endsWith(input.path as string)) {
          graphStore.setHeat(n.qname, 1)
        }
      }
    }
  } else if (tool === "str_replace_editor" && input.path) {
    graphStore.setFileAgentState(input.path as string, "stale")
  }
}
