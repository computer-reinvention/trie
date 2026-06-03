import { useEffect, useMemo, useRef, useState } from "react"
import { useGraphStore } from "@/store/graphStore"
import { roleColor } from "@/graph/style"
import type { SystemModelNode } from "@/api/types"

// Cmd+P symbol search — the top Obsidian-graph gap (search-in-graph). Type to
// filter; Enter/click jumps focus to the symbol (selects it and drills into its
// component so it's visible on the canvas).
export function SearchPalette() {
  const [open, setOpen] = useState(false)
  const [q, setQ] = useState("")
  const [active, setActive] = useState(0)
  const inputRef = useRef<HTMLInputElement>(null)
  const model = useGraphStore((s) => s.model)
  const axis = useGraphStore((s) => s.axis)
  const expandComponent = useGraphStore((s) => s.expandComponent)
  const selectNode = useGraphStore((s) => s.selectNode)

  useEffect(() => {
    function onKey(e: KeyboardEvent) {
      if ((e.metaKey || e.ctrlKey) && e.key === "p") {
        e.preventDefault()
        setOpen((v) => !v)
        setQ("")
        setActive(0)
      } else if (e.key === "Escape") {
        setOpen(false)
      }
    }
    window.addEventListener("keydown", onKey)
    return () => window.removeEventListener("keydown", onKey)
  }, [])

  useEffect(() => {
    if (open) setTimeout(() => inputRef.current?.focus(), 0)
  }, [open])

  const results = useMemo(() => {
    if (!model || !q.trim()) return [] as SystemModelNode[]
    const needle = q.toLowerCase()
    return model.nodes
      .filter((n) => n.name.toLowerCase().includes(needle) || n.qname.toLowerCase().includes(needle))
      .sort((a, b) => b.salience - a.salience)
      .slice(0, 20)
  }, [model, q])

  const jump = (n: SystemModelNode) => {
    const key = axis === "role" ? n.role || "untagged" : n.subsystem
    expandComponent(key)
    selectNode(n.qname)
    window.dispatchEvent(new CustomEvent("trie:node-selected", { detail: { qname: n.qname } }))
    setOpen(false)
  }

  if (!open) return null

  return (
    <div
      className="absolute inset-0 z-20 flex items-start justify-center pt-24 bg-slate-950/50"
      onClick={() => setOpen(false)}
    >
      <div
        className="w-[36rem] max-w-[90%] bg-slate-900 border border-slate-700 rounded-lg shadow-2xl overflow-hidden"
        onClick={(e) => e.stopPropagation()}
      >
        <input
          ref={inputRef}
          className="w-full bg-slate-900 text-slate-100 text-sm px-4 py-3 outline-none border-b border-slate-800 placeholder:text-slate-600"
          placeholder="Search symbols…  (↑↓ to navigate, Enter to jump, Esc to close)"
          value={q}
          onChange={(e) => {
            setQ(e.target.value)
            setActive(0)
          }}
          onKeyDown={(e) => {
            if (e.key === "ArrowDown") setActive((a) => Math.min(a + 1, results.length - 1))
            else if (e.key === "ArrowUp") setActive((a) => Math.max(a - 1, 0))
            else if (e.key === "Enter" && results[active]) jump(results[active])
          }}
        />
        <div className="max-h-80 overflow-y-auto">
          {results.map((n, i) => (
            <button
              key={n.qname}
              className={`w-full text-left px-4 py-2 flex items-center gap-2 ${
                i === active ? "bg-slate-800" : "hover:bg-slate-800/50"
              }`}
              onClick={() => jump(n)}
              onMouseEnter={() => setActive(i)}
            >
              <span
                className="w-2 h-2 rounded-full shrink-0"
                style={{ background: roleColor(n.role || "untagged") }}
              />
              <span className="text-slate-200 font-mono text-sm truncate">{n.name}</span>
              <span className="text-slate-600 text-xs truncate ml-auto">{n.qname}</span>
            </button>
          ))}
          {q.trim() && results.length === 0 && (
            <p className="px-4 py-3 text-slate-600 text-sm">No matches.</p>
          )}
        </div>
      </div>
    </div>
  )
}
