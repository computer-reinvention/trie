import { memo, useCallback } from "react"
import { Handle, Position, useViewport } from "@xyflow/react"
import type { Node, NodeProps } from "@xyflow/react"
import ReactMarkdown from "react-markdown"
import { graphClient } from "@/api/graphClient"
import { useGraphStore } from "@/store/graphStore"
import { useAgentStore } from "@/store/agentStore"
import type { SymbolNodeData } from "@/api/types"

type SymbolNodeProps = NodeProps<Node<SymbolNodeData>>

const KIND_COLORS: Record<string, string> = {
  function: "bg-indigo-600",
  class: "bg-violet-700",
  method: "bg-blue-600",
  constant: "bg-amber-600",
  module: "bg-slate-600",
}

const KIND_LABELS: Record<string, string> = {
  function: "fn",
  class: "cls",
  method: "mtd",
  constant: "const",
  module: "mod",
}

const AGENT_STATE_STYLES: Record<string, string> = {
  idle: "",
  reading: "ring-2 ring-blue-400 shadow-[0_0_12px_rgba(96,165,250,0.5)] animate-pulse-slow",
  writing: "ring-2 ring-amber-400 shadow-[0_0_12px_rgba(251,191,36,0.6)] animate-pulse-fast",
  stale: "ring-1 ring-dashed ring-orange-400",
}

export const SymbolNode = memo(function SymbolNode({
  data,
}: SymbolNodeProps) {
  const { zoom } = useViewport()
  const graphStore = useGraphStore()
  const agentStore = useAgentStore()

  const onClickHeader = useCallback(() => {
    graphStore.selectNode(data.qname)
    // Dispatch custom event so InputBar can pick it up
    window.dispatchEvent(new CustomEvent("trie:node-selected", { detail: { qname: data.qname } }))
  }, [data.qname])

  const onDoubleClickBody = useCallback(async () => {
    graphStore.expandNode(data.qname)
    if (!data.prose && !data.isProseLoading) {
      graphStore.setNodeProseLoading(data.qname, true)
      try {
        const result = await graphClient.read(data.qname)
        graphStore.setNodeProse(data.qname, result.prose)
      } catch {
        graphStore.setNodeProseLoading(data.qname, false)
      }
    }
  }, [data.qname, data.prose, data.isProseLoading])

  const onExpandCallers = useCallback(
    async (e: React.MouseEvent) => {
      e.stopPropagation()
      const result = await graphClient.trace({ from_qname: data.qname, direction: "callers", depth: 2 })
      graphStore.mergeTraceResult(result)
    },
    [data.qname],
  )

  const onExpandCallees = useCallback(
    async (e: React.MouseEvent) => {
      e.stopPropagation()
      const result = await graphClient.trace({ from_qname: data.qname, direction: "callees", depth: 2 })
      graphStore.mergeTraceResult(result)
    },
    [data.qname],
  )

  const stateClass = AGENT_STATE_STYLES[data.agentState] ?? ""
  const selectedClass = data.isSelected ? "ring-2 ring-lime-400" : ""
  const highlightClass = data.isHighlighted ? "ring-2 ring-sky-400" : ""

  // Semantic zoom: ultra-compact at low zoom
  if (zoom < 0.25) {
    return (
      <div
        className={`bg-slate-800 border border-slate-600 rounded px-2 py-1 cursor-pointer text-xs ${stateClass} ${selectedClass} ${highlightClass}`}
        onClick={onClickHeader}
      >
        <span className={`${KIND_COLORS[data.kind] ?? "bg-slate-600"} text-white rounded px-1 mr-1 text-[9px]`}>
          {KIND_LABELS[data.kind] ?? data.kind}
        </span>
        <span className="text-slate-200 font-mono">{data.name}</span>
        <Handle type="target" position={Position.Top} className="opacity-0" />
        <Handle type="source" position={Position.Bottom} className="opacity-0" />
      </div>
    )
  }

  return (
    <div
      className={`bg-slate-900 border border-slate-700 rounded-lg w-56 cursor-pointer select-none transition-all ${stateClass} ${selectedClass} ${highlightClass}`}
      onClick={onClickHeader}
      onDoubleClick={onDoubleClickBody}
    >
      <Handle type="target" position={Position.Top} className="opacity-0" />

      {/* Header */}
      <div className="flex items-center gap-2 px-3 py-2 border-b border-slate-700">
        <span
          className={`${KIND_COLORS[data.kind] ?? "bg-slate-600"} text-white rounded px-1.5 py-0.5 text-[10px] font-mono shrink-0`}
        >
          {KIND_LABELS[data.kind] ?? data.kind}
        </span>
        <span className="text-slate-100 font-mono text-sm font-medium truncate flex-1">{data.name}</span>
        <div className="flex items-center gap-1 shrink-0">
          <button
            className="text-slate-400 text-[10px] hover:text-blue-300 tabular-nums"
            onDoubleClick={onExpandCallers}
            title="Expand callers (double-click)"
          >
            ↓{data.inboundCount}
          </button>
          <button
            className="text-slate-400 text-[10px] hover:text-blue-300 tabular-nums"
            onDoubleClick={onExpandCallees}
            title="Expand callees (double-click)"
          >
            ↑{data.outboundCount}
          </button>
          <button
            className="text-slate-500 hover:text-slate-200 text-xs ml-1"
            onClick={(e) => { e.stopPropagation(); graphStore.expandNode(data.qname) }}
            title="Toggle prose"
          >
            ⊕
          </button>
        </div>
      </div>

      {/* One-liner — hidden at module zoom */}
      {zoom >= 0.25 && (
        <div className="px-3 py-1.5">
          {data.oneLiner ? (
            <p className="text-slate-400 text-xs truncate">{data.oneLiner}</p>
          ) : (
            <p className="text-slate-600 text-xs italic">no prose yet</p>
          )}
        </div>
      )}

      {/* Expanded prose panel */}
      {data.isExpanded && zoom >= 0.7 && (
        <div className="px-3 pb-3 border-t border-slate-700 mt-1 max-h-72 overflow-y-auto">
          {data.isProseLoading ? (
            <p className="text-slate-500 text-xs py-2">Loading…</p>
          ) : data.prose ? (
            <div className="prose prose-sm prose-invert max-w-none text-xs">
              <ReactMarkdown>{data.prose}</ReactMarkdown>
            </div>
          ) : (
            <p className="text-slate-600 text-xs py-2 italic">Double-click to load prose</p>
          )}
        </div>
      )}

      {/* Footer */}
      {zoom >= 0.7 && (
        <div className="px-3 py-1 border-t border-slate-800 flex items-center justify-between">
          <span className="text-slate-600 text-[10px] font-mono truncate">
            {data.filePath.split("/").pop()}:{data.startLine}
          </span>
          {data.agentState !== "idle" && (
            <span
              className={`w-2 h-2 rounded-full shrink-0 ${
                data.agentState === "reading"
                  ? "bg-blue-400 animate-pulse"
                  : data.agentState === "writing"
                    ? "bg-amber-400 animate-pulse"
                    : "bg-orange-400"
              }`}
            />
          )}
        </div>
      )}

      <Handle type="source" position={Position.Bottom} className="opacity-0" />
    </div>
  )
})
