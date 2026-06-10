import { useEffect, useRef, useState } from "react"
import ReactMarkdown from "react-markdown"
import { ToolRow } from "./ToolRow"
import {
  ChevronRight,
  Copy,
  Check,
  FileDiff,
  AlertCircle,
  ArrowDownToLine,
  Brain,
} from "./icons"
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

  const jumpToLatest = () => {
    setStick(true)
    endRef.current?.scrollIntoView({ block: "end", behavior: "smooth" })
  }

  if (messages.length === 0 && !running) {
    return (
      <div className="flex-1 flex flex-col items-center justify-center text-center px-8 gap-3">
        <div
          className="w-11 h-11 rounded-2xl flex items-center justify-center"
          style={{ background: "color-mix(in srgb, var(--accent) 14%, transparent)" }}
        >
          <Brain size={22} style={{ color: "var(--accent)" }} />
        </div>
        <p className="text-2 text-sm max-w-[16rem] leading-relaxed">
          Ask the agent anything. It will read the graph, edit code, and you’ll watch it move.
        </p>
      </div>
    )
  }

  return (
    <div className="relative flex-1 min-h-0">
      <div
        ref={scrollRef}
        onScroll={onScroll}
        className="absolute inset-0 overflow-y-auto scroll-thin px-3.5 py-4 space-y-5"
      >
        {messages.map((m) => (
          <MessageView
            key={m.info.id}
            message={m}
            permissionsByCallID={permissionsByCallID}
            onResolvePermission={onResolvePermission}
          />
        ))}
        {running && <StreamingIndicator />}
        {error && (
          <div
            className="flex items-start gap-2 rounded-xl border px-3 py-2 text-xs"
            style={{
              borderColor: "color-mix(in srgb, var(--danger) 40%, transparent)",
              background: "var(--danger-soft)",
              color: "#fda4af",
            }}
          >
            <AlertCircle size={14} className="shrink-0 mt-0.5" />
            <span>{error}</span>
          </div>
        )}
        <div ref={endRef} />
      </div>

      {!stick && (
        <button
          onClick={jumpToLatest}
          className="absolute bottom-3 left-1/2 -translate-x-1/2 inline-flex items-center gap-1.5 surface-pop border border-strong elev-2 rounded-full px-3 py-1.5 text-xs text-2 hover:text-1 transition-colors"
          title="Jump to latest"
        >
          <ArrowDownToLine size={13} />
          Latest
        </button>
      )}
    </div>
  )
}

function StreamingIndicator() {
  return (
    <div className="flex items-center gap-2 text-3 text-xs pl-1">
      <span className="flex items-center gap-1">
        <span
          className="typing-dot w-1.5 h-1.5 rounded-full"
          style={{ background: "var(--accent)", animationDelay: "0ms" }}
        />
        <span
          className="typing-dot w-1.5 h-1.5 rounded-full"
          style={{ background: "var(--accent)", animationDelay: "150ms" }}
        />
        <span
          className="typing-dot w-1.5 h-1.5 rounded-full"
          style={{ background: "var(--accent)", animationDelay: "300ms" }}
        />
      </span>
      <span className="shimmer-text">thinking</span>
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
      <div className="msg-in flex justify-end group">
        <div className="relative max-w-[88%]">
          <div
            className="rounded-2xl rounded-br-md bg-accent-soft border border-accent-soft px-3.5 py-2 text-sm text-1 whitespace-pre-wrap"
          >
            {text}
          </div>
          <div className="absolute -bottom-5 right-1 opacity-0 group-hover:opacity-100 transition-opacity">
            <CopyButton text={text} />
          </div>
        </div>
      </div>
    )
  }

  const plainText = parts
    .filter((p): p is TextPart => p.type === "text")
    .map((p) => p.text)
    .join("\n")
    .trim()

  return (
    <div className="msg-in group flex gap-2.5">
      <div
        className="shrink-0 w-6 h-6 rounded-lg flex items-center justify-center mt-0.5"
        style={{ background: "color-mix(in srgb, var(--accent) 16%, transparent)" }}
      >
        <Brain size={13} style={{ color: "var(--accent)" }} />
      </div>
      <div className="min-w-0 flex-1 space-y-2">
        {parts.map((p) => (
          <PartView
            key={p.id}
            part={p}
            permissionsByCallID={permissionsByCallID}
            onResolvePermission={onResolvePermission}
          />
        ))}
        <div className="flex items-center gap-2">
          <AssistantFooter info={message.info as OpencodeAssistantInfo} />
          {plainText && (
            <span className="opacity-0 group-hover:opacity-100 transition-opacity">
              <CopyButton text={plainText} />
            </span>
          )}
        </div>
      </div>
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
      <div className="md">
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
      <div
        className="inline-flex items-center gap-2 rounded-lg border px-2.5 py-1 text-[11px]"
        style={{
          borderColor: "color-mix(in srgb, var(--warn) 35%, transparent)",
          background: "color-mix(in srgb, var(--warn) 8%, transparent)",
          color: "#fcd34d",
        }}
        title={pp.files.join(", ")}
      >
        <FileDiff size={13} className="shrink-0" />
        <span className="font-mono truncate max-w-[14rem]">{pp.files.join(", ")}</span>
        <span
          className="shrink-0 rounded-full px-1.5 text-[10px]"
          style={{ background: "color-mix(in srgb, var(--warn) 22%, transparent)" }}
        >
          {pp.files.length}
        </span>
      </div>
    )
  }
  return null
}

function ReasoningView({ part }: { part: ReasoningPart }) {
  const [open, setOpen] = useState(false)
  if (!part.text.trim()) return null
  return (
    <div className="rounded-lg border border-subtle surface-2/40">
      <button
        className="flex items-center gap-1.5 w-full px-2.5 py-1.5 text-xs text-3 hover:text-2 transition-colors"
        onClick={() => setOpen((v) => !v)}
      >
        <ChevronRight
          size={13}
          className="transition-transform"
          style={{ transform: open ? "rotate(90deg)" : "none" }}
        />
        <span className="italic">Reasoning</span>
      </button>
      {open && (
        <div className="px-3 pb-2.5 pt-0.5 text-xs text-2 whitespace-pre-wrap leading-relaxed border-t border-subtle/60">
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
    <div className="flex items-center gap-2.5 text-[10px] text-faint font-mono">
      {info.cost != null && info.cost > 0 && <span>${info.cost.toFixed(4)}</span>}
      {tokens && (
        <span>
          {tokens.input}↓ {tokens.output}↑
          {tokens.reasoning > 0 ? ` ${tokens.reasoning}∴` : ""}
        </span>
      )}
      {info.error?.message && <span style={{ color: "var(--danger)" }}>{info.error.message}</span>}
    </div>
  )
}

function CopyButton({ text }: { text: string }) {
  const [copied, setCopied] = useState(false)
  const copy = () => {
    navigator.clipboard.writeText(text).then(() => {
      setCopied(true)
      setTimeout(() => setCopied(false), 1200)
    })
  }
  return (
    <button
      className="inline-flex items-center justify-center w-6 h-6 rounded-md surface-2 border border-subtle text-3 hover:text-1 transition-colors"
      onClick={copy}
      title={copied ? "Copied" : "Copy"}
    >
      {copied ? <Check size={12} style={{ color: "var(--accent)" }} /> : <Copy size={12} />}
    </button>
  )
}
