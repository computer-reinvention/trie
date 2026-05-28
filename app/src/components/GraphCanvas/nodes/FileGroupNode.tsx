import { memo } from "react"
import type { Node, NodeProps } from "@xyflow/react"

interface FileGroupData extends Record<string, unknown> {
  filePath: string
  label: string
}

type FileGroupNodeProps = NodeProps<Node<FileGroupData>>

export const FileGroupNode = memo(function FileGroupNode({
  data,
}: FileGroupNodeProps) {
  return (
    <div
      className="rounded-lg border p-2 pointer-events-none"
      style={{ width: "100%", height: "100%" }}
    >
      <span className="text-[10px] text-slate-500 font-mono select-none">{data.label}</span>
    </div>
  )
})
