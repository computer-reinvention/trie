import { useMemo, useState } from "react"
import { useGraphStore } from "@/store/graphStore"
import { graphClient } from "@/api/graphClient"
import { componentView } from "@/graph/doi"
import { depthColor } from "@/graph/style"
import type { MemberGrouping } from "@/store/graphStore"

const MEMBER_GROUPINGS: Array<{ key: MemberGrouping; label: string }> = [
  { key: "subsystem", label: "subsystem" },
  { key: "class", label: "kind" },
  { key: "owningClass", label: "class" },
]

// In-flow panel (lives in the sidebar's bottom half). Lens switcher, call-depth
// key, group list with click-to-isolate, member-grouping selector, tests toggle.
export function Legend() {
  const model = useGraphStore((s) => s.model)
  const axis = useGraphStore((s) => s.axis)
  const setAxis = useGraphStore((s) => s.setAxis)
  const isolatedGroup = useGraphStore((s) => s.isolatedGroup)
  const setIsolatedGroup = useGraphStore((s) => s.setIsolatedGroup)
  const memberGrouping = useGraphStore((s) => s.memberGrouping)
  const setMemberGrouping = useGraphStore((s) => s.setMemberGrouping)
  const setModel = useGraphStore((s) => s.setModel)
  const [showTests, setShowTests] = useState(false)

  const groups = useMemo(() => {
    if (!model) return []
    return [...componentView(model, axis).groups].sort((a, b) => a.order - b.order).slice(0, 20)
  }, [model, axis])

  if (!model) return null

  const toggleTests = async () => {
    const next = !showTests
    setShowTests(next)
    try {
      const [m, edges] = await Promise.all([
        graphClient.systemModel({ includeTests: next }),
        graphClient.allEdges({ limit: 50000 }),
      ])
      setModel(m, edges.edges)
    } catch {
      /* best-effort */
    }
  }

  return (
    <div className="flex flex-col text-xs overflow-hidden">
      <div className="px-3 py-2 border-b border-slate-800">
        <span className="text-slate-500 uppercase tracking-wide text-[10px]">Group by</span>
        <div className="mt-1 flex rounded overflow-hidden border border-slate-700">
          <button
            className={`flex-1 px-1 py-0.5 text-center ${axis === "role" ? "bg-indigo-600 text-white" : "text-slate-400 hover:text-slate-200"}`}
            onClick={() => setAxis("role")}
          >
            roles
          </button>
          <button
            className={`flex-1 px-1 py-0.5 text-center ${axis === "subsystem" ? "bg-indigo-600 text-white" : "text-slate-400 hover:text-slate-200"}`}
            onClick={() => setAxis("subsystem")}
          >
            subsystems
          </button>
        </div>
      </div>

      {/* call-depth gradient key */}
      <div className="px-3 py-2 border-b border-slate-800">
        <div
          className="h-1.5 rounded"
          style={{
            background: `linear-gradient(to right, ${depthColor(0)}, ${depthColor(0.5)}, ${depthColor(1)})`,
          }}
        />
        <div className="flex justify-between text-[10px] text-slate-500 mt-1">
          <span>entry</span>
          <span>foundation</span>
        </div>
      </div>

      <div className="flex-1 overflow-y-auto px-2 py-1.5 space-y-0.5 min-h-0">
        {groups.map((g) => {
          const active = isolatedGroup === g.key
          return (
            <button
              key={g.key}
              className={`w-full flex items-center gap-2 px-1.5 py-1 rounded ${
                active ? "bg-slate-700" : "hover:bg-slate-800"
              } ${isolatedGroup && !active ? "opacity-50" : ""}`}
              onClick={() => setIsolatedGroup(active ? null : g.key)}
              title={active ? "Show all" : `Isolate ${g.key}`}
            >
              <span
                className="w-2.5 h-2.5 rounded-full shrink-0"
                style={{ background: depthColor(g.order) }}
              />
              <span className="text-slate-200 truncate">{g.key.split("/").pop()}</span>
              <span className="text-slate-500 ml-auto tabular-nums">{g.count}</span>
            </button>
          )
        })}
      </div>

      {/* member sub-grouping selector */}
      <div className="px-3 py-2 border-t border-slate-800">
        <span className="text-slate-500 uppercase tracking-wide text-[10px]">Members by</span>
        <div className="mt-1 flex rounded overflow-hidden border border-slate-700">
          {MEMBER_GROUPINGS.map((m) => (
            <button
              key={m.key}
              className={`flex-1 px-1 py-0.5 text-center ${
                memberGrouping === m.key ? "bg-indigo-600 text-white" : "text-slate-400 hover:text-slate-200"
              }`}
              onClick={() => setMemberGrouping(m.key)}
            >
              {m.label}
            </button>
          ))}
        </div>
      </div>

      <div className="px-3 py-2 border-t border-slate-800 flex items-center justify-between">
        <label className="flex items-center gap-1.5 text-slate-400 cursor-pointer">
          <input type="checkbox" checked={showTests} onChange={toggleTests} className="accent-indigo-500" />
          Show tests
        </label>
        <span className="text-slate-600 tabular-nums">{model.stats.production_nodes} symbols</span>
      </div>
    </div>
  )
}
