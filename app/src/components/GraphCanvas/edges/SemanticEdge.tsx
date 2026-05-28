import { memo } from "react"
import { BaseEdge, getSmoothStepPath, type Edge, type EdgeProps } from "@xyflow/react"
import type { EdgeData } from "@/api/types"

type SemanticEdgeProps = EdgeProps<Edge<EdgeData>>

const EDGE_COLORS: Record<string, string> = {
  calls: "#6366f1",
  imports: "#06b6d4",
  inherits: "#8b5cf6",
}

export const SemanticEdge = memo(function SemanticEdge({
  id,
  sourceX,
  sourceY,
  targetX,
  targetY,
  sourcePosition,
  targetPosition,
  data,
  markerEnd,
}: SemanticEdgeProps) {
  const [edgePath] = getSmoothStepPath({
    sourceX,
    sourceY,
    sourcePosition,
    targetX,
    targetY,
    targetPosition,
  })

  const kind = (data as EdgeData | undefined)?.kind ?? "calls"
  const color = EDGE_COLORS[kind] ?? EDGE_COLORS.calls

  return (
    <BaseEdge
      id={id}
      path={edgePath}
      markerEnd={markerEnd}
      style={{ stroke: color, strokeWidth: 1.5, opacity: 0.7 }}
    />
  )
})
