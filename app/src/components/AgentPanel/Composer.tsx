import { useState, useEffect, useRef, useCallback, useLayoutEffect } from "react"
import { graphClient } from "@/api/graphClient"
import { useSetting } from "@/store/settingsStore"
import { ArrowUp, Square, X, AtSign, Sparkles } from "./icons"

interface Pill {
  qname: string
  label: string
}

const MODEL_LABELS: Record<string, string> = {
  "claude-sonnet-4-6": "Sonnet 4.6",
  "claude-opus-4-7": "Opus 4.7",
  "claude-haiku-4-5": "Haiku 4.5",
}

// The message composer at the bottom of the agent panel. Carries symbol context
// pills (added by selecting graph nodes), resolves them to prose on send, and
// shows a Stop button while a turn is running. The textarea auto-grows, and a
// compact toolbar surfaces the active model + a circular send/stop control.
export function Composer({
  running,
  disabled,
  onSend,
  onStop,
}: {
  running: boolean
  disabled: boolean
  onSend: (text: string) => void
  onStop: () => void
}) {
  const [pills, setPills] = useState<Pill[]>([])
  const [text, setText] = useState("")
  const sendOnEnter = useSetting<boolean>("agent.sendOnEnter")
  const model = useSetting<string>("agent.model")
  const inputRef = useRef<HTMLTextAreaElement>(null)

  // Auto-grow the textarea between 1 and 8 rows, then scroll.
  useLayoutEffect(() => {
    const el = inputRef.current
    if (!el) return
    el.style.height = "auto"
    el.style.height = `${Math.min(el.scrollHeight, 200)}px`
  }, [text])

  // Graph node selection adds a context pill.
  useEffect(() => {
    function onNodeSelected(e: Event) {
      const { qname } = (e as CustomEvent).detail as { qname: string }
      const label = qname.split(":").pop() ?? qname
      setPills((prev) => (prev.some((p) => p.qname === qname) ? prev : [...prev, { qname, label }]))
      inputRef.current?.focus()
    }
    window.addEventListener("trie:node-selected", onNodeSelected)
    return () => window.removeEventListener("trie:node-selected", onNodeSelected)
  }, [])

  // Cmd+K focuses the composer.
  useEffect(() => {
    function onKey(e: KeyboardEvent) {
      if ((e.metaKey || e.ctrlKey) && e.key === "k") {
        e.preventDefault()
        inputRef.current?.focus()
      }
    }
    window.addEventListener("keydown", onKey)
    return () => window.removeEventListener("keydown", onKey)
  }, [])

  const removePill = useCallback((qname: string) => {
    setPills((prev) => prev.filter((p) => p.qname !== qname))
  }, [])

  const handleSend = useCallback(async () => {
    if (disabled || (!text.trim() && pills.length === 0)) return
    const pillsCopy = [...pills]
    const textCopy = text.trim()
    setPills([])
    setText("")

    let content = textCopy
    if (pillsCopy.length > 0) {
      let ctx = "Relevant symbols (from the trie graph):\n\n"
      const resolved = await Promise.allSettled(pillsCopy.map((p) => graphClient.read(p.qname)))
      for (let i = 0; i < pillsCopy.length; i++) {
        const r = resolved[i]
        if (r.status === "fulfilled") {
          ctx += `---\nSymbol: ${r.value.qname}\nSource: ${r.value.source_pointer}\nSignature: ${r.value.signature ?? ""}\n\n${r.value.prose}\n---\n\n`
        } else {
          ctx += `---\nSymbol: ${pillsCopy[i].qname}\n---\n\n`
        }
      }
      content = textCopy ? `${ctx}User instruction:\n${textCopy}` : ctx
    }
    onSend(content)
  }, [disabled, text, pills, onSend])

  const onKeyDown = useCallback(
    (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
      const enterSends = sendOnEnter
        ? e.key === "Enter" && !e.shiftKey
        : e.key === "Enter" && (e.metaKey || e.ctrlKey)
      if (enterSends) {
        e.preventDefault()
        handleSend()
      }
      if (e.key === "Backspace" && text === "" && pills.length > 0) {
        setPills((prev) => prev.slice(0, -1))
      }
    },
    [handleSend, text, pills.length, sendOnEnter],
  )

  const canSend = !disabled && (text.trim().length > 0 || pills.length > 0)

  return (
    <div className="surface-1 border-t border-subtle p-3 shrink-0">
      <div
        className={`flex flex-col gap-2 surface-2 rounded-2xl px-3 py-2.5 border transition-all ${
          disabled
            ? "border-subtle opacity-60"
            : "border-strong focus-within:border-accent-soft focus-within:ring-accent-soft"
        }`}
      >
        {pills.length > 0 && (
          <div className="flex flex-wrap gap-1.5">
            {pills.map((pill) => (
              <span
                key={pill.qname}
                className="msg-in inline-flex items-center gap-1 surface-3 border border-subtle rounded-lg pl-1.5 pr-1 py-0.5 text-xs font-mono"
                title={pill.qname}
              >
                <AtSign size={11} className="text-accent" style={{ color: "var(--accent)" }} />
                <span className="text-1">{pill.label}</span>
                <button
                  className="text-3 hover:text-1 leading-none rounded p-0.5 hover:bg-black/20"
                  onClick={() => removePill(pill.qname)}
                  title="Remove"
                >
                  <X size={11} />
                </button>
              </span>
            ))}
          </div>
        )}

        <textarea
          ref={inputRef}
          rows={1}
          className="bg-transparent text-1 text-sm outline-none placeholder:text-faint resize-none scroll-thin leading-relaxed"
          style={{ maxHeight: 200 }}
          placeholder={pills.length === 0 ? "Ask or instruct…  (⌘K to focus)" : "Add an instruction…"}
          value={text}
          onChange={(e) => setText(e.target.value)}
          onKeyDown={onKeyDown}
          disabled={disabled}
        />

        <div className="flex items-center justify-between gap-2">
          <div className="flex items-center gap-2 text-faint text-[11px] min-w-0">
            <span className="inline-flex items-center gap-1 truncate" title="Active model">
              <Sparkles size={12} />
              <span className="truncate">{MODEL_LABELS[model] ?? model}</span>
            </span>
          </div>

          {running ? (
            <button
              className="inline-flex items-center justify-center w-8 h-8 rounded-full text-white transition-transform active:scale-95"
              style={{ background: "var(--danger)" }}
              onClick={onStop}
              title="Stop"
            >
              <Square size={14} fill="currentColor" />
            </button>
          ) : (
            <button
              className={`inline-flex items-center justify-center w-8 h-8 rounded-full transition-transform active:scale-95 ${
                canSend ? "bg-accent text-white" : "surface-3 text-faint cursor-not-allowed"
              }`}
              onClick={handleSend}
              disabled={!canSend}
              title="Send"
            >
              <ArrowUp size={16} strokeWidth={2.5} />
            </button>
          )}
        </div>
      </div>
    </div>
  )
}
