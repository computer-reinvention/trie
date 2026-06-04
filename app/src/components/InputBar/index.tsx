import { useState, useEffect, useRef, useCallback } from "react"
import { graphClient } from "@/api/graphClient"
import { opencodeClient } from "@/api/opencodeClient"
import { useAgentStore } from "@/store/agentStore"
import { useAppStore } from "@/store/appStore"
import { useSetting } from "@/store/settingsStore"

interface Pill {
  qname: string
  label: string
}

export function InputBar() {
  const [pills, setPills] = useState<Pill[]>([])
  const [text, setText] = useState("")
  const { running, sessionId } = useAgentStore()
  const { serversReady } = useAppStore()
  const sendOnEnter = useSetting<boolean>("agent.sendOnEnter")
  const inputRef = useRef<HTMLInputElement>(null)

  // Listen for node-selected events from the graph canvas
  useEffect(() => {
    function onNodeSelected(e: Event) {
      const { qname } = (e as CustomEvent).detail as { qname: string }
      const label = qname.split(":").pop() ?? qname
      setPills((prev) =>
        prev.some((p) => p.qname === qname) ? prev : [...prev, { qname, label }],
      )
      inputRef.current?.focus()
    }
    window.addEventListener("trie:node-selected", onNodeSelected)
    return () => window.removeEventListener("trie:node-selected", onNodeSelected)
  }, [])

  // Cmd+K focuses the input
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
    if (!sessionId || (!text.trim() && pills.length === 0)) return

    const pillsCopy = [...pills]
    const textCopy = text.trim()
    setPills([])
    setText("")

    // Resolve pills to prose
    let content = ""
    if (pillsCopy.length > 0) {
      content += "Relevant symbols (from trie graph):\n\n"
      const resolved = await Promise.allSettled(pillsCopy.map((p) => graphClient.read(p.qname)))
      for (let i = 0; i < pillsCopy.length; i++) {
        const result = resolved[i]
        if (result.status === "fulfilled") {
          const r = result.value
          content += `---\nSymbol: ${r.qname}\nSource: ${r.source_pointer}\nSignature: ${r.signature ?? ""}\n\n${r.prose}\n---\n\n`
        } else {
          content += `---\nSymbol: ${pillsCopy[i].qname}\n---\n\n`
        }
      }
      if (textCopy) {
        content += `User instruction:\n${textCopy}`
      }
    } else {
      content = textCopy
    }

    await opencodeClient.sendMessage(sessionId, content)
  }, [sessionId, pills, text])

  const onKeyDown = useCallback(
    (e: React.KeyboardEvent<HTMLInputElement>) => {
      // Send on Enter (Shift+Enter = newline) when enabled; otherwise require
      // the modifier to send (Cmd/Ctrl+Enter).
      const enterSends = sendOnEnter ? e.key === "Enter" && !e.shiftKey : e.key === "Enter" && (e.metaKey || e.ctrlKey)
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

  const disabled = running || !serversReady

  return (
    <div className="border-t border-slate-800 bg-slate-900 px-3 py-2 flex items-center gap-2">
      {/* Pills + text input */}
      <div
        className={`flex-1 flex flex-wrap items-center gap-1.5 bg-slate-800 border rounded-lg px-3 py-2 min-h-[40px] transition-colors ${
          disabled ? "border-slate-700 opacity-60" : "border-slate-600 hover:border-slate-500"
        }`}
        onClick={() => inputRef.current?.focus()}
      >
        {pills.map((pill) => (
          <span
            key={pill.qname}
            className="inline-flex items-center gap-1 bg-slate-700 border border-slate-600 rounded px-2 py-0.5 text-xs font-mono"
          >
            <span className="text-slate-400">@</span>
            <span className="text-slate-200">{pill.label}</span>
            <button
              className="text-slate-500 hover:text-slate-200 leading-none ml-0.5"
              onClick={(e) => { e.stopPropagation(); removePill(pill.qname) }}
            >
              ×
            </button>
          </span>
        ))}
        <input
          ref={inputRef}
          className="flex-1 bg-transparent text-slate-200 text-sm outline-none placeholder:text-slate-600 min-w-32"
          placeholder={pills.length === 0 ? "Ask or instruct… (⌘K to focus)" : ""}
          value={text}
          onChange={(e) => setText(e.target.value)}
          onKeyDown={onKeyDown}
          disabled={disabled}
        />
      </div>

      {/* Send button */}
      <button
        className={`w-9 h-9 rounded-lg flex items-center justify-center shrink-0 transition-colors ${
          disabled ? "bg-slate-800 text-slate-600 cursor-not-allowed" : "bg-accent text-white"
        }`}
        onClick={handleSend}
        disabled={disabled}
        title="Send (Enter)"
      >
        {running ? (
          <span className="w-3 h-3 border border-slate-400 border-t-white rounded-full animate-spin" />
        ) : (
          <span className="text-sm">▶</span>
        )}
      </button>
    </div>
  )
}
