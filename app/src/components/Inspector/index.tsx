import { useEffect, useState } from "react"
import ReactMarkdown from "react-markdown"
import { graphClient } from "@/api/graphClient"
import { useGraphStore } from "@/store/graphStore"
import { roleColor } from "@/graph/style"
import type { ReadResult, NodeClass } from "@/api/types"

const CLASS_LABEL: Record<NodeClass, string> = {
  door: "entry point",
  hub: "hub",
  bedrock: "foundation",
  exit: "exit point",
  internal: "internal",
  normal: "internal",
  orphan: "unreferenced",
  test: "test",
}

const CLASS_COLOR: Record<NodeClass, string> = {
  door: "#fbbf24",
  hub: "#a855f7",
  bedrock: "#0ea5e9",
  exit: "#06b6d4",
  internal: "#64748b",
  normal: "#64748b",
  orphan: "#ef4444",
  test: "#475569",
}

// Right-side detail panel. Prose lives here (not crammed into canvas nodes).
// Opens on symbol select; lazily loads full prose + callers/callees.
export function Inspector() {
  const selectedQname = useGraphStore((s) => s.selectedQname)
  const nodesByQname = useGraphStore((s) => s.nodesByQname)
  const selectNode = useGraphStore((s) => s.selectNode)
  const expandComponent = useGraphStore((s) => s.expandComponent)
  const axis = useGraphStore((s) => s.axis)
  const [detail, setDetail] = useState<ReadResult | null>(null)
  const [loading, setLoading] = useState(false)

  const node = selectedQname ? nodesByQname.get(selectedQname) : undefined

  useEffect(() => {
    if (!selectedQname) {
      setDetail(null)
      return
    }
    let cancelled = false
    setLoading(true)
    setDetail(null)
    graphClient
      .read(selectedQname)
      .then((r) => {
        if (!cancelled) setDetail(r)
      })
      .catch(() => {
        if (!cancelled) setDetail(null)
      })
      .finally(() => {
        if (!cancelled) setLoading(false)
      })
    return () => {
      cancelled = true
    }
  }, [selectedQname])

  // navigate to a caller/callee: select it and drill into its component
  const navigate = (qname: string) => {
    const target = nodesByQname.get(qname)
    if (target) {
      const key = axis === "role" ? target.role || "untagged" : target.subsystem
      expandComponent(key)
    }
    selectNode(qname)
    window.dispatchEvent(new CustomEvent("trie:node-selected", { detail: { qname } }))
  }

  if (!selectedQname || !node) return null

  return (
    <aside className="w-80 shrink-0 bg-slate-900 border-l border-slate-800 flex flex-col overflow-hidden">
      <div className="px-4 py-3 border-b border-slate-800 flex items-start gap-2">
        <span
          className="w-2.5 h-2.5 rounded-full mt-1.5 shrink-0"
          style={{ background: roleColor(node.role || "untagged") }}
        />
        <div className="min-w-0 flex-1">
          <p className="text-slate-100 font-mono text-sm font-medium truncate">{node.name}</p>
          <p className="text-slate-500 text-xs font-mono truncate">
            {node.file_path}:{node.depth >= 0 ? "" : ""}
          </p>
        </div>
        <button
          className="text-slate-500 hover:text-slate-200 text-sm"
          onClick={() => selectNode(null)}
          title="Close"
        >
          ×
        </button>
      </div>

      {/* badges */}
      <div className="px-4 py-2 flex flex-wrap gap-1.5 border-b border-slate-800">
        <Badge label={CLASS_LABEL[node.cls]} color={CLASS_COLOR[node.cls]} />
        {node.role && <Badge label={node.role} color={roleColor(node.role)} />}
        <Badge label={`↓${node.inbound_count}`} color="#334155" />
        <Badge label={`↑${node.outbound_count}`} color="#334155" />
        {node.is_public ? null : <Badge label="private" color="#334155" />}
      </div>

      {/* prose */}
      <div className="flex-1 overflow-y-auto scroll-thin px-4 py-3">
        {detail?.signature && (
          <pre className="text-[11px] text-slate-400 font-mono whitespace-pre-wrap mb-3 bg-slate-950/50 rounded p-2 border border-slate-800">
            {detail.signature}
          </pre>
        )}
        {loading ? (
          <p className="text-slate-500 text-sm">Loading…</p>
        ) : detail?.prose ? (
          <div className="prose prose-sm prose-invert max-w-none text-xs">
            <ReactMarkdown>{detail.prose}</ReactMarkdown>
          </div>
        ) : (
          <p className="text-slate-600 text-xs italic">{node.one_liner || "No prose yet."}</p>
        )}

        {/* callers / callees */}
        {detail && (detail.callers.length > 0 || detail.callees.length > 0) && (
          <div className="mt-4 space-y-3">
            <NeighbourList title="Called by" items={detail.callers} onNav={navigate} />
            <NeighbourList title="Calls" items={detail.callees} onNav={navigate} />
          </div>
        )}
      </div>
    </aside>
  )
}

function Badge({ label, color }: { label: string; color: string }) {
  return (
    <span
      className="text-[10px] font-mono rounded px-1.5 py-0.5 text-slate-100"
      style={{ background: color + "33", border: `1px solid ${color}` }}
    >
      {label}
    </span>
  )
}

function NeighbourList({
  title,
  items,
  onNav,
}: {
  title: string
  items: Array<{ qname: string; signature: string; one_liner: string }>
  onNav: (qname: string) => void
}) {
  if (items.length === 0) return null
  return (
    <div>
      <p className="text-slate-500 text-[10px] uppercase tracking-wide mb-1">{title}</p>
      <div className="space-y-0.5">
        {items.map((it) => (
          <button
            key={it.qname}
            className="w-full text-left px-2 py-1 rounded hover:bg-slate-800 group"
            onClick={() => onNav(it.qname)}
            title={it.one_liner}
          >
            <span className="text-slate-300 font-mono text-xs truncate block group-hover:text-indigo-300">
              {it.qname.split(":").pop()}
            </span>
          </button>
        ))}
      </div>
    </div>
  )
}
