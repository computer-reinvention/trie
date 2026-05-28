import { useCallback, useMemo } from "react"
import {
  ReactFlow,
  Background,
  BackgroundVariant,
  Controls,
  MiniMap,
  type Node,
  type Edge,
} from "@xyflow/react"
import "@xyflow/react/dist/style.css"
import { SymbolNode } from "./nodes/SymbolNode"
import { FileGroupNode } from "./nodes/FileGroupNode"
import { HubPlaceholderNode } from "./nodes/HubPlaceholderNode"
import { SemanticEdge } from "./edges/SemanticEdge"
import { useGraphStore } from "@/store/graphStore"
import { useAppStore } from "@/store/appStore"

const nodeTypes = {
  symbol: SymbolNode,
  fileGroup: FileGroupNode,
  hub: HubPlaceholderNode,
}

const edgeTypes = {
  semantic: SemanticEdge,
}

interface GraphCanvasProps {
  className?: string
}

export function GraphCanvas({ className }: GraphCanvasProps) {
  const { nodes, edges: rawEdges, deselectAll } = useGraphStore()
  const edges = rawEdges as Edge[]
  const { graphLoading, graphLoadingMessage } = useAppStore()

  const onPaneClick = useCallback(() => {
    deselectAll()
  }, [deselectAll])

  return (
    <div className={`relative flex-1 bg-slate-950 ${className ?? ""}`}>
      <ReactFlow
        nodes={nodes as Node[]}
        edges={edges}
        nodeTypes={nodeTypes}
        edgeTypes={edgeTypes}
        defaultEdgeOptions={{ type: "semantic", animated: false }}
        minZoom={0.05}
        maxZoom={3}
        fitView
        fitViewOptions={{ padding: 0.1 }}
        proOptions={{ hideAttribution: true }}
        selectNodesOnDrag={false}
        panOnDrag
        zoomOnScroll
        zoomOnPinch
        onPaneClick={onPaneClick}
      >
        <Background
          variant={BackgroundVariant.Dots}
          gap={24}
          size={1}
          color="#1e293b"
        />
        <Controls
          className="!border-slate-700 !bg-slate-800"
          showInteractive={false}
        />
        <MiniMap
          className="!border-slate-700 !bg-slate-900"
          nodeColor={(n) => (n.type === "fileGroup" ? "#1e293b" : "#334155")}
          maskColor="rgba(0,0,0,0.6)"
        />
      </ReactFlow>

      {/* Loading overlay */}
      {graphLoading && (
        <div className="absolute inset-0 bg-slate-950/80 flex flex-col items-center justify-center gap-3 z-10">
          <div className="w-8 h-8 border-2 border-slate-600 border-t-indigo-400 rounded-full animate-spin" />
          <p className="text-slate-400 text-sm">{graphLoadingMessage || "Loading…"}</p>
        </div>
      )}
    </div>
  )
}
