import { useState, useEffect, useRef, useCallback } from "react"
import { graphClient } from "@/api/graphClient"
import { useSetting } from "@/store/settingsStore"

interface Pill {
  qname: string
  label: string
}

// The message composer at the bottom of the agent panel. Carries symbol context
// pills (added by selecting graph nodes), resolves them to prose on send, and
// shows a Stop button while a turn is running.
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
  const inputRef = useRef<HTMLTextAreaElement>(null)

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

  return (
    <div className="border-t border-slate-800 bg-slate-900 p-2 shrink-0">
      <div
        className={`flex flex-col gap-1.5 bg-slate-800 border rounded-lg px-2.5 py-2 transition-colors ${
          disabled ? "border-slate-700 opacity-60" : "border-slate-600 focus-within:border-slate-500"
        }`}
      >
        {pills.length > 0 && (
          <div className="flex flex-wrap gap-1.5">
            {pills.map((pill) => (
              <span
                key={pill.qname}
                className="inline-flex items-center gap-1 bg-slate-700 border border-slate-600 rounded px-2 py-0.5 text-xs font-mono"
                title={pill.qname}
              >
                <span className="text-slate-400">@</span>
                <span className="text-slate-200">{pill.label}</span>
                <button
                  className="text-slate-500 hover:text-slate-200 leading-none ml-0.5"
                  onClick={() => removePill(pill.qname)}
                >
                  ×
                </button>
              </span>
            ))}
          </div>
        )}
        <textarea
          ref={inputRef}
          rows={2}
          className="bg-transparent text-slate-200 text-sm outline-none placeholder:text-slate-600 resize-none scroll-thin"
          placeholder={pills.length === 0 ? "Ask or instruct… (⌘K to focus)" : "Add an instruction…"}
          value={text}
          onChange={(e) => setText(e.target.value)}
          onKeyDown={onKeyDown}
          disabled={disabled}
        />
        <div className="flex items-center justify-end gap-2">
          {running ? (
            <button
              className="rounded-md px-3 py-1 text-xs font-medium bg-red-500/20 text-red-300 hover:bg-red-500/30"
              onClick={onStop}
            >
              Stop
            </button>
          ) : (
            <button
              className={`rounded-md px-3 py-1 text-xs font-medium ${
                disabled ? "bg-slate-800 text-slate-600 cursor-not-allowed" : "bg-accent text-white"
              }`}
              onClick={handleSend}
              disabled={disabled}
            >
              Send
            </button>
          )}
        </div>
      </div>
    </div>
  )
}
