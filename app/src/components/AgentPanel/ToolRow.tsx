import { useState } from "react"
import { opencodeClient } from "@/api/opencodeClient"
import { useGraphStore } from "@/store/graphStore"
import { useTabsStore, GRAPH_TAB_ID } from "@/store/tabsStore"
import type { ToolPart, PermissionRequest, PermissionReply } from "@/api/types"

// A single tool invocation in the transcript: name, a short input summary, a
// status glyph, and (collapsible) the raw input/output. When a permission
// request is correlated to this call, approve/deny controls render inline.

const STATUS: Record<string, { glyph: string; cls: string }> = {
  pending: { glyph: "○", cls: "text-slate-500" },
  running: { glyph: "◐", cls: "text-indigo-400 animate-pulse" },
  completed: { glyph: "✓", cls: "text-green-500" },
  error: { glyph: "✗", cls: "text-red-400" },
}

// One-line summary of the most useful input field per tool.
function inputSummary(tool: string, input: Record<string, unknown> | undefined): string {
  if (!input) return ""
  const pick = (k: string) => (typeof input[k] === "string" ? (input[k] as string) : undefined)
  return (
    pick("qname") ??
    pick("sym") ??
    pick("from_qname") ??
    pick("name_contains") ??
    pick("path") ??
    pick("filePath") ??
    pick("command") ??
    pick("regexp") ??
    ""
  )
}

function bareTool(tool: string): string {
  return tool.startsWith("trie_") ? tool.slice(5) : tool
}

export function ToolRow({
  part,
  permission,
  onResolvePermission,
}: {
  part: ToolPart
  permission?: PermissionRequest
  onResolvePermission: (requestID: string, reply: PermissionReply) => void
}) {
  const [open, setOpen] = useState(false)
  const st = STATUS[part.state.status] ?? STATUS.pending
  const summary = inputSummary(part.tool, part.state.input)
  const name = bareTool(part.tool)

  // Clicking a symbol-bearing tool reveals it in the graph.
  const reveal = () => {
    const q =
      (part.state.input?.qname as string) ??
      (part.state.input?.sym as string) ??
      (part.state.input?.from_qname as string)
    if (q && useGraphStore.getState().revealSymbol(q)) {
      useTabsStore.getState().activate(GRAPH_TAB_ID)
    }
  }

  return (
    <div className="rounded border border-slate-800 bg-slate-900/40 text-xs">
      <button
        className="w-full flex items-center gap-2 px-2 py-1 text-left hover:bg-slate-800/40"
        onClick={() => setOpen((v) => !v)}
      >
        <span className={`shrink-0 ${st.cls}`}>{st.glyph}</span>
        <span className="font-mono text-indigo-300 shrink-0">{name}</span>
        {summary && (
          <span
            className="font-mono text-slate-500 truncate flex-1 hover:text-slate-300"
            onClick={(e) => {
              e.stopPropagation()
              reveal()
            }}
            title={summary}
          >
            {summary}
          </span>
        )}
        {part.state.time?.start && part.state.time.end && (
          <span className="text-slate-600 shrink-0">
            {((part.state.time.end - part.state.time.start) / 1000).toFixed(1)}s
          </span>
        )}
      </button>

      {/* inline permission prompt */}
      {permission && (
        <div className="px-2 py-1.5 border-t border-amber-700/40 bg-amber-500/10">
          <p className="text-amber-200 text-[11px] mb-1">
            Allow <span className="font-mono">{permission.permission}</span>?
            {permission.patterns.length > 0 && (
              <span className="text-amber-300/70 font-mono"> {permission.patterns.join(", ")}</span>
            )}
          </p>
          <div className="flex gap-1.5">
            <PermBtn label="Allow" onClick={() => onResolvePermission(permission.id, "once")} />
            <PermBtn label="Always" onClick={() => onResolvePermission(permission.id, "always")} />
            <PermBtn
              label="Deny"
              danger
              onClick={() => onResolvePermission(permission.id, "reject")}
            />
          </div>
        </div>
      )}

      {open && (
        <div className="px-2 py-1.5 border-t border-slate-800 space-y-1.5">
          {part.state.input && Object.keys(part.state.input).length > 0 && (
            <pre className="text-[10px] text-slate-400 font-mono whitespace-pre-wrap break-all bg-slate-950/60 rounded p-1.5">
              {JSON.stringify(part.state.input, null, 2)}
            </pre>
          )}
          {part.state.output && (
            <pre className="text-[10px] text-slate-400 font-mono whitespace-pre-wrap break-all bg-slate-950/60 rounded p-1.5 max-h-48 overflow-y-auto scroll-thin">
              {part.state.output}
            </pre>
          )}
          {part.state.error && (
            <pre className="text-[10px] text-red-400 font-mono whitespace-pre-wrap break-all bg-red-950/30 rounded p-1.5">
              {part.state.error}
            </pre>
          )}
        </div>
      )}
    </div>
  )
}

function PermBtn({
  label,
  onClick,
  danger,
}: {
  label: string
  onClick: () => void
  danger?: boolean
}) {
  return (
    <button
      className={`rounded px-2 py-0.5 text-[11px] font-medium ${
        danger
          ? "bg-red-500/20 text-red-300 hover:bg-red-500/30"
          : "bg-amber-500/20 text-amber-200 hover:bg-amber-500/30"
      }`}
      onClick={onClick}
    >
      {label}
    </button>
  )
}

// re-export for the client signature used by the panel
export type { ToolPart }
