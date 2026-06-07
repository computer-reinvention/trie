import { useEffect, useRef, useState } from "react"
import ReactMarkdown from "react-markdown"
import { ToolRow } from "./ToolRow"
import type {
  OpencodeMessage,
  OpencodePart,
  PermissionRequest,
  PermissionReply,
  ReasoningPart,
  TextPart,
  ToolPart,
  PatchPartT,
  OpencodeAssistantInfo,
} from "@/api/types"

// Renders the conversation: user bubbles, assistant markdown, collapsible
// reasoning, inline tool rows (with permission prompts), edit chips, and a
// per-assistant cost/token footer. Auto-scrolls to the bottom while streaming.

export function Transcript({
  messages,
  permissionsByCallID,
  onResolvePermission,
  running,
  error,
}: {
  messages: OpencodeMessage[]
  permissionsByCallID: Record<string, PermissionRequest>
  onResolvePermission: (requestID: string, reply: PermissionReply) => void
  running: boolean
  error: string | null
}) {
  const endRef = useRef<HTMLDivElement | null>(null)
  // stick-to-bottom only when the user is already near the bottom
  const scrollRef = useRef<HTMLDivElement | null>(null)
  const [stick, setStick] = useState(true)

  useEffect(() => {
    if (stick) endRef.current?.scrollIntoView({ block: "end" })
  }, [messages, running, stick])

  const onScroll = () => {
    const el = scrollRef.current
    if (!el) return
    setStick(el.scrollHeight - el.scrollTop - el.clientHeight < 80)
  }

  if (messages.length === 0 && !running) {
    return (
      <div className="flex-1 flex items-center justify-center text-slate-600 text-xs px-6 text-center">
        Ask the agent anything. It will read the graph, edit code, and you’ll watch it move.
      </div>
    )
  }

  return (
    <div
      ref={scrollRef}
      onScroll={onScroll}
      className="flex-1 min-h-0 overflow-y-auto scroll-thin px-3 py-3 space-y-4"
    >
      {messages.map((m) => (
        <MessageView
          key={m.info.id}
          message={m}
          permissionsByCallID={permissionsByCallID}
          onResolvePermission={onResolvePermission}
        />
      ))}
      {running && (
        <div className="flex items-center gap-2 text-slate-500 text-xs">
          <span className="w-3 h-3 border-2 border-slate-600 border-t-accent rounded-full animate-spin" />
          thinking…
        </div>
      )}
      {error && (
        <div className="rounded border border-red-800 bg-red-950/30 text-red-300 text-xs px-3 py-2">
          {error}
        </div>
      )}
      <div ref={endRef} />
    </div>
  )
}

function MessageView({
  message,
  permissionsByCallID,
  onResolvePermission,
}: {
  message: OpencodeMessage
  permissionsByCallID: Record<string, PermissionRequest>
  onResolvePermission: (requestID: string, reply: PermissionReply) => void
}) {
  const isUser = message.info.role === "user"
  // Drop server-injected text parts: `ignored` (excluded from model input) and
  // `synthetic` (system plumbing like the plan→build mode notice, file-mention
  // expansions, etc.). These are not real conversation content.
  const isHiddenText = (p: OpencodePart) => {
    if (p.type !== "text") return false
    const tp = p as TextPart
    if (tp.ignored || tp.synthetic) return true
    // Defensive: hide raw system-reminder plumbing even if flags are absent.
    return tp.text.trimStart().startsWith("<system-reminder>")
  }
  const parts = message.parts.filter((p) => !isHiddenText(p))

  if (isUser) {
    const text = parts
      .filter((p): p is TextPart => p.type === "text")
      .map((p) => p.text)
      .join("\n")
      .trim()
    if (!text) return null
    return (
      <div className="flex justify-end">
        <div className="max-w-[88%] rounded-lg bg-accent/20 border border-accent/30 px-3 py-2 text-sm text-slate-100 whitespace-pre-wrap">
          {text}
        </div>
      </div>
    )
  }

  return (
    <div className="space-y-1.5">
      {parts.map((p) => (
        <PartView
          key={p.id}
          part={p}
          permissionsByCallID={permissionsByCallID}
          onResolvePermission={onResolvePermission}
        />
      ))}
      <AssistantFooter info={message.info as OpencodeAssistantInfo} />
    </div>
  )
}

function PartView({
  part,
  permissionsByCallID,
  onResolvePermission,
}: {
  part: OpencodePart
  permissionsByCallID: Record<string, PermissionRequest>
  onResolvePermission: (requestID: string, reply: PermissionReply) => void
}) {
  if (part.type === "text") {
    const t = part as TextPart
    if (!t.text.trim()) return null
    return (
      <div className="prose prose-sm prose-invert max-w-none text-sm">
        <ReactMarkdown>{t.text}</ReactMarkdown>
      </div>
    )
  }
  if (part.type === "reasoning") return <ReasoningView part={part as ReasoningPart} />
  if (part.type === "tool") {
    const tp = part as ToolPart
    return (
      <ToolRow
        part={tp}
        permission={permissionsByCallID[tp.callID]}
        onResolvePermission={onResolvePermission}
      />
    )
  }
  if (part.type === "patch") {
    const pp = part as PatchPartT
    return (
      <div className="rounded border border-amber-700/40 bg-amber-500/5 text-[11px] text-amber-200 px-2 py-1 font-mono">
        edited {pp.files.length} file{pp.files.length !== 1 ? "s" : ""}: {pp.files.join(", ")}
      </div>
    )
  }
  return null
}

function ReasoningView({ part }: { part: ReasoningPart }) {
  const [open, setOpen] = useState(false)
  if (!part.text.trim()) return null
  return (
    <div className="text-xs">
      <button
        className="flex items-center gap-1 text-slate-500 hover:text-slate-300"
        onClick={() => setOpen((v) => !v)}
      >
        <span>{open ? "▾" : "▸"}</span>
        <span className="italic">thinking</span>
      </button>
      {open && (
        <div className="mt-1 pl-3 border-l border-slate-700 text-slate-400 whitespace-pre-wrap leading-relaxed">
          {part.text}
        </div>
      )}
    </div>
  )
}

function AssistantFooter({ info }: { info: OpencodeAssistantInfo }) {
  if (!info.finish && info.cost == null) return null
  const tokens = info.tokens
  return (
    <div className="flex items-center gap-2 text-[10px] text-slate-600 font-mono pt-0.5">
      {info.cost != null && info.cost > 0 && <span>${info.cost.toFixed(4)}</span>}
      {tokens && (
        <span>
          {tokens.input}↓ {tokens.output}↑
          {tokens.reasoning > 0 ? ` ${tokens.reasoning}∴` : ""}
        </span>
      )}
      {info.error?.message && <span className="text-red-400">{info.error.message}</span>}
    </div>
  )
}
