import { useEffect } from "react"
import type { Node, Edge } from "@xyflow/react"
import { graphClient } from "@/api/graphClient"
import { useGraphStore } from "@/store/graphStore"
import { useAppStore } from "@/store/appStore"
import type { SymbolNodeData, EdgeData, SymbolHit } from "@/api/types"

// eslint-disable-next-line @typescript-eslint/no-explicit-any
type AnyNode = Node<any>
// eslint-disable-next-line @typescript-eslint/no-explicit-any
type AnyEdge = Edge<any>

// Stable file-path → hue mapping
function fileHue(filePath: string): number {
  let hash = 0
  for (let i = 0; i < filePath.length; i++) {
    hash = (hash * 31 + filePath.charCodeAt(i)) >>> 0
  }
  return hash % 360
}

export function symbolHitToNode(hit: SymbolHit, parentId?: string): Node<SymbolNodeData> {
  return {
    id: hit.qname,
    type: "symbol",
    parentId,
    extent: parentId ? ("parent" as const) : undefined,
    position: { x: 0, y: 0 },
    data: {
      qname: hit.qname,
      name: hit.name,
      kind: hit.kind,
      filePath: hit.file_path,
      startLine: hit.start_line,
      endLine: 0,
      signature: hit.signature,
      oneLiner: hit.one_liner,
      isPublic: hit.is_public,
      inboundCount: hit.inbound_count,
      outboundCount: hit.outbound_count,
      prose: null,
      isProseLoading: false,
      isExpanded: false,
      agentState: "idle",
      isSelected: false,
      isHighlighted: false,
    },
  }
}

export function useGraphPopulation(opencodePort: number | null): void {
  const appStore = useAppStore()
  const graphStore = useGraphStore()

  useEffect(() => {
    if (!opencodePort) return

    let cancelled = false

    async function populate(): Promise<void> {
      appStore.setGraphLoading(true, "Connecting to trie graph…")

      try {
        // 1. Fetch all symbols. The server-side handler waits for trie MCP
        //    to be connected before responding, so this is a single blocking call.
        appStore.setGraphLoading(true, "Connecting to trie graph…")
        const res = await graphClient.allSymbols({ rank_by: "inbound_count", limit: 5000 })
        if (cancelled) return

        if (!res || !Array.isArray(res.hits) || res.hits.length === 0) {
          console.error("[graph] allSymbols returned no hits:", res)
          appStore.setGraphLoading(false)
          return
        }
        const hits = res.hits

        appStore.setGraphLoading(
          true,
          `Building graph for ${hits.length} symbols…`,
        )

        // 2. Group by file → build FileGroupNodes + SymbolNodes
        const byFile = new Map<string, SymbolHit[]>()
        for (const hit of hits) {
          const arr = byFile.get(hit.file_path) ?? []
          arr.push(hit)
          byFile.set(hit.file_path, arr)
        }

        const groupNodes: Node[] = []
        const symbolNodes: Node<SymbolNodeData>[] = []

        for (const [filePath, symbols] of byFile) {
          const groupId = `__file__${filePath}`
          const hue = fileHue(filePath)
          groupNodes.push({
            id: groupId,
            type: "fileGroup",
            position: { x: 0, y: 0 },
            style: {
              background: `hsla(${hue}, 40%, 20%, 0.3)`,
              border: `1px solid hsla(${hue}, 40%, 40%, 0.5)`,
            },
            data: { filePath, label: filePath.split("/").pop() ?? filePath },
          })
          for (const hit of symbols) {
            symbolNodes.push(symbolHitToNode(hit, groupId))
          }
        }

        // 3. Fetch edges for top-200 by inbound_count, batched 10 at a time
        // to avoid saturating the IPC channel.
        const top200 = hits.slice(0, 200)
        const traceResults: PromiseSettledResult<Awaited<ReturnType<typeof graphClient.trace>>>[] = []
        const BATCH = 10
        for (let i = 0; i < top200.length; i += BATCH) {
          if (cancelled) return
          const batch = top200.slice(i, i + BATCH)
          const batchResults = await Promise.allSettled(
            batch.map((h) => graphClient.trace({ from_qname: h.qname, direction: "both", depth: 1 }))
          )
          traceResults.push(...batchResults)
        }
        if (cancelled) return

        const edgeSet = new Map<string, Edge<EdgeData>>()
        for (const result of traceResults) {
          if (result.status !== "fulfilled") continue
          if (!Array.isArray(result.value?.edges)) continue
          for (const e of result.value.edges) {
            const id = `${e.from}->${e.to}`
            if (!edgeSet.has(id)) {
              edgeSet.set(id, {
                id,
                source: e.from,
                target: e.to,
                type: "semantic",
                data: { kind: "calls" },
              })
            }
          }
        }

        // 4. ELK layout
        appStore.setGraphLoading(
          true,
          `Laying out ${symbolNodes.length} symbols across ${groupNodes.length} files…`,
        )

        const allNodes: AnyNode[] = [...groupNodes, ...symbolNodes]
        const allEdges: AnyEdge[] = [...edgeSet.values()]

        const positioned = await runElkLayout(allNodes, allEdges)
        if (cancelled) return

        graphStore.setGraph(positioned.nodes as unknown as Node<SymbolNodeData>[], positioned.edges as unknown as Edge<EdgeData>[])
      } catch (err) {
        console.error("Graph population failed:", err)
      } finally {
        if (!cancelled) appStore.setGraphLoading(false)
      }
    }

    populate()
    return () => { cancelled = true }
  }, [opencodePort])
}

// ELK layout using a Web Worker for the heavy lifting
async function runElkLayout(
  nodes: AnyNode[],
  edges: AnyEdge[],
): Promise<{ nodes: AnyNode[]; edges: AnyEdge[] }> {
  // Dynamic import so ELK only loads when needed
  const ELK = (await import("elkjs/lib/elk.bundled.js")).default
  const elk = new ELK()

  const elkNodes = nodes.map((n) => {
    const isGroup = n.type === "fileGroup"
    return {
      id: n.id,
      width: isGroup ? 300 : 240,
      height: isGroup ? 200 : 80,
      children: isGroup
        ? nodes
            .filter((c) => c.parentId === n.id)
            .map((c) => ({ id: c.id, width: 220, height: 70, children: undefined, layoutOptions: undefined }))
        : undefined,
      layoutOptions: isGroup
        ? { "elk.direction": "DOWN", "elk.spacing.nodeNode": "20" }
        : undefined,
    }
  })

  const elkEdges = edges.map((e) => ({
    id: e.id,
    sources: [e.source],
    targets: [e.target],
  }))

  const graph = await elk.layout({
    id: "root",
    layoutOptions: {
      "elk.algorithm": "layered",
      "elk.direction": "DOWN",
      "elk.layered.spacing.nodeNodeBetweenLayers": "100",
      "elk.spacing.nodeNode": "50",
      "elk.hierarchyHandling": "INCLUDE_CHILDREN",
    },
    children: elkNodes,
    edges: elkEdges,
  })

  // Map positions back to React Flow nodes
  const positionMap = new Map<string, { x: number; y: number }>()
  function extractPositions(elkChildren: typeof graph.children): void {
    if (!elkChildren) return
    for (const n of elkChildren) {
      positionMap.set(n.id, { x: n.x ?? 0, y: n.y ?? 0 })
      if (n.children) extractPositions(n.children)
    }
  }
  extractPositions(graph.children)

  const positionedNodes = nodes.map((n) => {
    const pos = positionMap.get(n.id)
    return pos ? { ...n, position: pos } : n
  })

  return { nodes: positionedNodes, edges }
}
