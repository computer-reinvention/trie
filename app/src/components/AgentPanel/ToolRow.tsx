import { useState } from "react"
import { useGraphStore } from "@/store/graphStore"
import { useTabsStore, TOPOLOGY_TAB_ID } from "@/store/tabsStore"
import { ACTIVITY, activityColor } from "@/graph/style"
import { Check, Loader2, AlertCircle, ChevronRight, Copy, ShieldQuestion } from "./icons"
import type { ToolPart, PermissionRequest, PermissionReply } from "@/api/types"

// Lockstep color: the same intent hue the graph uses for this tool, so the chat
// row and the graph node read as one event (docs/choreography-prd.md §3).
function intentColor(tool: string): string {
  const t = tool.startsWith("trie_") ? tool.slice(5) : tool
  if (t.startsWith("grep")) return ACTIVITY.scan
  if (t === "patch" || t === "patch_apply") return ACTIVITY.patch
  if (t === "write" || t === "edit" || t === "write_file" || t === "str_replace_editor")
    return ACTIVITY.write
  if (t.startsWith("read") || t.startsWith("explain") || t.startsWith("trace")) return ACTIVITY.read
  return "#475569"
}

// A single tool invocation in the transcript: name, a short input summary, a
// status icon, and (collapsible) the raw input/output. When a permission
// request is correlated to this call, approve/deny controls render inline.

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

function StatusIcon({ status, color }: { status: string; color: string }) {
  if (status === "running")
    return <Loader2 size={13} className="animate-spin" style={{ color }} />
  if (status === "completed")
    return <Check size={13} style={{ color: "var(--accent)" }} />
  if (status === "error") return <AlertCircle size={13} style={{ color: "var(--danger)" }} />
  return (
    <span className="w-2 h-2 rounded-full" style={{ background: "var(--text-faint)" }} />
  )
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
  const summary = inputSummary(part.tool, part.state.input)
  const name = bareTool(part.tool)

  // Lockstep: pulse the row's accent while its target symbol is live on the graph.
  const target =
    (part.state.input?.qname as string) ??
    (part.state.input?.sym as string) ??
    (part.state.input?.from_qname as string) ??
    undefined
  const liveState = useGraphStore((s) => {
    if (!target) return ""
    const r = s.runtime.get(target)
    if (!r) return ""
    return r.agentState !== "idle" || r.activity > 0.05 ? r.agentState : ""
  })
  const live = liveState !== ""
  const barColor = live ? activityColor(liveState) : intentColor(part.tool)

  // Clicking a symbol-bearing tool reveals it in the graph.
  const reveal = () => {
    const q =
      (part.state.input?.qname as string) ??
      (part.state.input?.sym as string) ??
      (part.state.input?.from_qname as string)
    if (q && useGraphStore.getState().revealSymbol(q)) {
      useTabsStore.getState().activate(TOPOLOGY_TAB_ID)
    }
  }

  return (
    <div
      className={`rounded-lg border border-subtle surface-2 text-xs overflow-hidden ${live ? "trie-pulse" : ""}`}
      style={{
        borderLeft: `${live ? 3 : 2}px solid ${barColor}`,
        boxShadow: live ? `inset 2px 0 8px -4px ${barColor}` : undefined,
      }}
    >
      <button
        className="w-full flex items-center gap-2 px-2.5 py-1.5 text-left hover:bg-black/15 transition-colors"
        onClick={() => setOpen((v) => !v)}
      >
        <span className="shrink-0 flex items-center">
          <StatusIcon status={part.state.status} color={barColor} />
        </span>
        <span className="font-mono font-medium shrink-0" style={{ color: barColor }}>
          {name}
        </span>
        {summary && (
          <span
            className="font-mono text-3 truncate flex-1 hover:text-1 transition-colors"
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
          <span className="text-faint shrink-0 tabular-nums">
            {((part.state.time.end - part.state.time.start) / 1000).toFixed(1)}s
          </span>
        )}
        <ChevronRight
          size={12}
          className="shrink-0 text-faint transition-transform"
          style={{ transform: open ? "rotate(90deg)" : "none" }}
        />
      </button>

      {/* inline permission prompt */}
      {permission && (
        <div
          className="px-2.5 py-2 border-t"
          style={{
            borderColor: "color-mix(in srgb, var(--warn) 35%, transparent)",
            background: "color-mix(in srgb, var(--warn) 9%, transparent)",
          }}
        >
          <p className="flex items-center gap-1.5 text-[11px] mb-1.5" style={{ color: "#fcd34d" }}>
            <ShieldQuestion size={13} className="shrink-0" />
            <span>
              Allow <span className="font-mono">{permission.permission}</span>?
              {permission.patterns.length > 0 && (
                <span className="font-mono opacity-80"> {permission.patterns.join(", ")}</span>
              )}
            </span>
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
        <div className="px-2.5 py-2 border-t border-subtle space-y-1.5">
          {part.state.input && Object.keys(part.state.input).length > 0 && (
            <Pre text={JSON.stringify(part.state.input, null, 2)} />
          )}
          {part.state.output && <Pre text={part.state.output} scrollable />}
          {part.state.error && <Pre text={part.state.error} danger />}
        </div>
      )}
    </div>
  )
}

function Pre({
  text,
  scrollable,
  danger,
}: {
  text: string
  scrollable?: boolean
  danger?: boolean
}) {
  const [copied, setCopied] = useState(false)
  const copy = () => {
    navigator.clipboard.writeText(text).then(() => {
      setCopied(true)
      setTimeout(() => setCopied(false), 1200)
    })
  }
  return (
    <div className="relative group/pre">
      <pre
        className={`text-[10px] font-mono whitespace-pre-wrap break-all rounded-md p-1.5 ${
          scrollable ? "max-h-48 overflow-y-auto scroll-thin" : ""
        }`}
        style={{
          background: "rgba(0,0,0,0.35)",
          color: danger ? "var(--danger)" : "var(--text-2)",
        }}
      >
        {text}
      </pre>
      <button
        className="absolute top-1 right-1 opacity-0 group-hover/pre:opacity-100 transition-opacity inline-flex items-center justify-center w-5 h-5 rounded surface-3 text-3 hover:text-1"
        onClick={copy}
        title={copied ? "Copied" : "Copy"}
      >
        {copied ? <Check size={11} style={{ color: "var(--accent)" }} /> : <Copy size={11} />}
      </button>
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
      className="rounded-md px-2.5 py-1 text-[11px] font-medium transition-colors"
      style={
        danger
          ? { background: "var(--danger-soft)", color: "#fda4af" }
          : { background: "color-mix(in srgb, var(--warn) 18%, transparent)", color: "#fcd34d" }
      }
      onClick={onClick}
    >
      {label}
    </button>
  )
}

// re-export for the client signature used by the panel
export type { ToolPart }
