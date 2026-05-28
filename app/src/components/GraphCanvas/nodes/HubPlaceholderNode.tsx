import { memo } from "react"
import type { Node, NodeProps } from "@xyflow/react"

interface HubData extends Record<string, unknown> {
  qname: string
  oneLiner: string
  inboundCount: number
}

type HubNodeProps = NodeProps<Node<HubData>>

export const HubPlaceholderNode = memo(function HubPlaceholderNode({
  data,
}: HubNodeProps) {
  const name = data.qname.split(":").pop()?.split(".").pop() ?? data.qname
  return (
    <div
      className="bg-slate-800 border border-slate-600 rounded-full px-3 py-1 flex items-center gap-1.5 cursor-default"
      title={data.oneLiner}
    >
      <span className="text-amber-400 text-xs">⚡</span>
      <span className="text-slate-400 text-xs font-mono">{name}</span>
      <span className="text-slate-600 text-[10px]">({data.inboundCount})</span>
    </div>
  )
})
