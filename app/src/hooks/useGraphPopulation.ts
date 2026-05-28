import { useEffect } from "react"
import type { Node, Edge } from "@xyflow/react"
import { graphClient } from "@/api/graphClient"
import { useGraphStore } from "@/store/graphStore"
import { useAppStore } from "@/store/appStore"
import type { SymbolNodeData, EdgeData, SymbolHit } from "@/api/types"

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

// ---------------------------------------------------------------------------
// Simple grid layout — no ELK, no async layout engine.
//
// Files are laid out in columns (up to MAX_COLS). Within each file column
// symbols are stacked vertically. File group nodes are sized to contain
// their children.
// ---------------------------------------------------------------------------

const NODE_W = 240
const NODE_H = 72
const NODE_GAP_Y = 12    // vertical gap between symbols
const GROUP_PAD = 20     // padding inside file group
const COL_GAP = 60       // horizontal gap between file columns
const ROW_GAP = 60       // vertical gap between file groups in same column
const MAX_COLS = 6

function gridLayout(
  byFile: Map<string, SymbolHit[]>,
): { groupNodes: Node[]; symbolNodes: Node<SymbolNodeData>[] } {
  const files = [...byFile.entries()]
  const numCols = Math.min(MAX_COLS, Math.ceil(Math.sqrt(files.length)))

  // Track current Y offset per column
  const colY = new Array(numCols).fill(0)
  // Track X position per column
  const colX = new Array(numCols).fill(0).map((_, i) => i * (NODE_W + GROUP_PAD * 2 + COL_GAP))

  const groupNodes: Node[] = []
  const symbolNodes: Node<SymbolNodeData>[] = []

  files.forEach(([filePath, symbols], fileIdx) => {
    const col = fileIdx % numCols
    const hue = fileHue(filePath)

    const groupH = GROUP_PAD * 2 + symbols.length * (NODE_H + NODE_GAP_Y) - NODE_GAP_Y
    const groupW = NODE_W + GROUP_PAD * 2
    const gx = colX[col]
    const gy = colY[col]

    const groupId = `__file__${filePath}`
    groupNodes.push({
      id: groupId,
      type: "fileGroup",
      position: { x: gx, y: gy },
      style: {
        width: groupW,
        height: groupH,
        background: `hsla(${hue}, 40%, 18%, 0.35)`,
        border: `1px solid hsla(${hue}, 40%, 40%, 0.4)`,
        borderRadius: 8,
      },
      data: { filePath, label: filePath.split("/").pop() ?? filePath },
    })

    symbols.forEach((hit, symIdx) => {
      const node = symbolHitToNode(hit, groupId)
      node.position = {
        x: GROUP_PAD,
        y: GROUP_PAD + symIdx * (NODE_H + NODE_GAP_Y),
      }
      symbolNodes.push(node)
    })

    colY[col] += groupH + ROW_GAP
  })

  return { groupNodes, symbolNodes }
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
        // Fetch symbols and edges in parallel — both wait server-side for trie MCP.
        appStore.setGraphLoading(true, "Loading symbols and edges…")
        const [symbolsRes, edgesRes] = await Promise.all([
          graphClient.allSymbols({ rank_by: "inbound_count", limit: 5000 }),
          graphClient.allEdges({ limit: 50000 }),
        ])
        if (cancelled) return

        if (!symbolsRes?.hits?.length) {
          console.error("[graph] allSymbols returned no hits:", symbolsRes)
          appStore.setGraphLoading(false)
          return
        }

        const hits = symbolsRes.hits
        const rawEdges = edgesRes?.edges ?? []
        console.log(`[graph] ${hits.length} symbols, ${rawEdges.length} edges`)

        appStore.setGraphLoading(true, `Laying out ${hits.length} symbols…`)

        // Group by file
        const byFile = new Map<string, SymbolHit[]>()
        for (const hit of hits) {
          const arr = byFile.get(hit.file_path) ?? []
          arr.push(hit)
          byFile.set(hit.file_path, arr)
        }

        // Simple grid layout — synchronous, no ELK needed
        const { groupNodes, symbolNodes } = gridLayout(byFile)

        // Build edge set — only include edges where both endpoints are in our symbol set
        const knownQnames = new Set(hits.map((h) => h.qname))
        const edges: Edge<EdgeData>[] = []
        const seen = new Set<string>()
        for (const e of rawEdges) {
          const id = `${e.from}->${e.to}`
          if (!seen.has(id) && knownQnames.has(e.from) && knownQnames.has(e.to)) {
            seen.add(id)
            edges.push({
              id,
              source: e.from,
              target: e.to,
              type: "semantic",
              data: { kind: "calls" },
            })
          }
        }

        if (cancelled) return

        const allNodes = [...groupNodes, ...symbolNodes]
        console.log(`[graph] rendering ${allNodes.length} nodes, ${edges.length} edges`)
        graphStore.setGraph(
          allNodes as Node<SymbolNodeData>[],
          edges as Edge<EdgeData>[],
        )
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
