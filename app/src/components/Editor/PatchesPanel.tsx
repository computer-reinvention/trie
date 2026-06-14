import { useState } from "react"
import { usePatchesStore } from "@/store/patchesStore"
import { useGraphStore } from "@/store/graphStore"
import { useTabsStore, TOPOLOGY_TAB_ID } from "@/store/tabsStore"
import { usePatches } from "@/hooks/usePatches"
import { playCascade } from "@/graph/conductor"
import { activityColor } from "@/graph/style"
import type { ApplyReport, PatchEntry, PatchKind } from "@/api/types"

// The patch review surface: every symbol with staged edits, its notes, origin,
// kind and (when the cascade pipeline lands) blast radius. Apply/commit drives
// the pipeline and renders the ApplyReport hand-off (applied / cascade /
// unresolved with one-click repatch).

const KIND_STYLE: Record<PatchKind, { label: string; cls: string }> = {
  modify: { label: "modify", cls: "bg-amber-500/20 text-amber-300" },
  create: { label: "create", cls: "bg-green-500/20 text-green-300" },
  delete: { label: "delete", cls: "bg-red-500/20 text-red-300" },
  rename: { label: "rename", cls: "bg-sky-500/20 text-sky-300" },
}

const ORIGIN_STYLE: Record<string, string> = {
  agent: "bg-accent-soft text-accent",
  cascade: "bg-violet-500/20 text-violet-300",
  mixed: "surface-3 text-2",
}

export function PatchesPanel() {
  const patches = usePatchesStore((s) => s.patches)
  const sessionNote = usePatchesStore((s) => s.sessionNote)
  const applyInProgress = usePatchesStore((s) => s.applyInProgress)
  const applyProgress = usePatchesStore((s) => s.applyProgress)
  const lastError = usePatchesStore((s) => s.lastError)
  const { drop, apply } = usePatches()
  const [report, setReport] = useState<ApplyReport | null>(null)

  const symbolCount = patches.length
  const total = patches.reduce((n, p) => n + p.count, 0)

  const onApply = async () => {
    setReport(null)
    // play the cascade wavefront for each patched symbol as it applies
    const staged = patches.map((p) => p.qname)
    staged.slice(0, 12).forEach((q, i) => setTimeout(() => playCascade(q), i * 120))
    const r = await apply()
    if (r) setReport(r)
  }

  return (
    <div className="flex flex-col h-full min-h-0" style={{ background: "var(--bg-app)" }}>
      {/* header */}
      <div className="shrink-0 px-4 py-2.5 border-b border-subtle flex items-center gap-3">
        <div className="flex-1 min-w-0">
          <h2 className="text-sm text-1 font-medium">Pending patches</h2>
          <p className="text-[11px] text-3">
            {symbolCount === 0
              ? "No staged edits"
              : `${total} patch${total !== 1 ? "es" : ""} across ${symbolCount} symbol${symbolCount !== 1 ? "s" : ""}`}
            {sessionNote ? ` · ${sessionNote}` : ""}
          </p>
        </div>
        {symbolCount > 0 && (
          <>
            <button
              className="rounded px-2 py-1 text-xs text-2 hover:surface-3 border border-strong transition-colors"
              onClick={() => drop()}
              disabled={applyInProgress}
              title="Drop all pending patches"
            >
              Discard all
            </button>
            <button
              className="rounded px-3 py-1 text-xs font-medium text-white hover:opacity-90 disabled:opacity-50 transition-opacity"
              style={{ background: "var(--warn)" }}
              onClick={onApply}
              disabled={applyInProgress}
            >
              {applyInProgress ? "Applying…" : "Apply all"}
            </button>
          </>
        )}
      </div>

      {/* live apply progress */}
      {applyProgress && (
        <div className="shrink-0 px-4 py-1.5 bg-amber-500/10 border-b border-amber-700/30 text-[11px] text-amber-200 flex items-center gap-2">
          <span className="w-3 h-3 border-2 border-amber-700 border-t-amber-300 rounded-full animate-spin" />
          {applyProgress.phase}
          {applyProgress.total > 0 && ` · ${applyProgress.done}/${applyProgress.total}`}
        </div>
      )}

      {lastError && (
        <div
          className="shrink-0 px-4 py-1.5 border-b text-[11px]"
          style={{
            background: "var(--danger-soft)",
            borderColor: "color-mix(in srgb, var(--danger) 40%, transparent)",
            color: "#fda4af",
          }}
        >
          {lastError}
        </div>
      )}

      {/* body */}
      <div className="flex-1 min-h-0 overflow-y-auto scroll-thin">
        {report ? (
          <ApplyReportView report={report} onClose={() => setReport(null)} />
        ) : symbolCount === 0 ? (
          <div className="h-full flex items-center justify-center text-faint text-xs px-6 text-center">
            When the agent stages edits (patch / create / delete / rename), the affected symbols and
            their blast radius will appear here for review before you apply them.
          </div>
        ) : (
          <ul className="divide-y divide-[var(--border-subtle)]">
            {patches.map((p) => (
              <PatchRow key={p.qname} patch={p} onDrop={() => drop(p.qname)} />
            ))}
          </ul>
        )}
      </div>
    </div>
  )
}

function reveal(qname: string) {
  if (useGraphStore.getState().revealSymbol(qname)) {
    useTabsStore.getState().activate(TOPOLOGY_TAB_ID)
  }
}

function PatchRow({ patch, onDrop }: { patch: PatchEntry; onDrop: () => void }) {
  const [open, setOpen] = useState(false)
  const kind = KIND_STYLE[patch.kind ?? "modify"]
  const br = patch.blast_radius
  const name = patch.qname.split(":").pop() ?? patch.qname
  // Lockstep: pulse this row while its symbol is live on the graph (apply/cascade).
  const liveState = useGraphStore((s) => {
    const r = s.runtime.get(patch.qname)
    if (!r) return ""
    return r.agentState !== "idle" || r.activity > 0.05 ? r.agentState : ""
  })
  const live = liveState !== ""
  return (
    <li
      className={`px-3 py-2 ${live ? "trie-pulse" : ""}`}
      style={live ? { boxShadow: `inset 2px 0 10px -5px ${activityColor(liveState)}` } : undefined}
    >
      <div className="flex items-center gap-2">
        <span className={`rounded px-1.5 py-0.5 text-[10px] uppercase tracking-wide ${kind.cls}`}>
          {patch.kind === "rename" && patch.rename_to ? `rename→${patch.rename_to}` : kind.label}
        </span>
        <button
          className="font-mono text-xs text-1 truncate hover:text-accent flex-1 text-left transition-colors"
          onClick={() => reveal(patch.qname)}
          title={`${patch.qname} — reveal in graph`}
        >
          {name}
        </button>
        <span className={`rounded px-1.5 py-0.5 text-[9px] uppercase ${ORIGIN_STYLE[patch.origin] ?? ORIGIN_STYLE.mixed}`}>
          {patch.origin}
        </span>
        {patch.count > 1 && (
          <span className="text-[10px] text-3">{patch.count} notes</span>
        )}
        <button
          className="text-faint text-xs px-1 transition-colors hover:text-[var(--danger)]"
          onClick={onDrop}
          title="Drop this symbol's patches"
        >
          ×
        </button>
      </div>

      {/* qname (full) + blast radius */}
      <div className="mt-0.5 flex items-center gap-3 pl-0.5">
        <span className="text-[10px] font-mono text-faint truncate">{patch.qname}</span>
        {br && (
          <span className="text-[10px] text-3 shrink-0" title="direct callers · cascade symbols">
            ↯ {br.direct} direct · {br.cascade_count} cascade
            {br.hubs_stopped_at?.length ? ` · stops at ${br.hubs_stopped_at.length} hub(s)` : ""}
          </span>
        )}
      </div>

      {/* notes */}
      {patch.notes.length > 0 && (
        <div className="mt-1">
          <button
            className="text-[10px] text-3 hover:text-2 transition-colors"
            onClick={() => setOpen((v) => !v)}
          >
            {open ? "▾" : "▸"} {patch.notes.length} note{patch.notes.length !== 1 ? "s" : ""}
          </button>
          {open && (
            <div className="mt-1 space-y-1 pl-3 border-l border-subtle">
              {patch.notes.map((n, i) => (
                <div key={i} className="text-[11px] text-2">
                  <p className="whitespace-pre-wrap leading-snug">{n.note ?? ""}</p>
                  {n.reason && <p className="text-faint italic mt-0.5">{n.reason}</p>}
                </div>
              ))}
            </div>
          )}
        </div>
      )}
    </li>
  )
}

function ApplyReportView({ report, onClose }: { report: ApplyReport; onClose: () => void }) {
  const applied = report.applied
  const unresolved = report.unresolved ?? []
  const cascade = report.cascade_applied ?? []
  return (
    <div className="p-4 space-y-4 text-xs">
      <div className="flex items-center gap-2">
        <span className={report.ok ? "text-green-400" : "text-amber-400"}>
          {report.ok ? "✓ Applied" : "Partial apply"}
        </span>
        {report.totals && (
          <span className="text-3">
            {report.totals.applied}/{report.totals.requested} applied
            {report.totals.unresolved > 0 ? ` · ${report.totals.unresolved} unresolved` : ""}
          </span>
        )}
        <button className="ml-auto text-3 hover:text-1 transition-colors" onClick={onClose}>
          ← back to patches
        </button>
      </div>

      {applied && (
        <div>
          <p className="text-2 mb-1">
            Applied {applied.symbols} symbol(s) across {applied.files} file(s)
          </p>
          {applied.files_detail && (
            <ul className="space-y-0.5">
              {applied.files_detail.map((f) => (
                <li key={f.path} className="font-mono text-[11px] text-3 flex items-center gap-2">
                  <span className={f.ok ? "text-green-500" : "text-red-400"}>{f.ok ? "✓" : "✗"}</span>
                  <span className="truncate">{f.path}</span>
                  <span className="text-faint">{f.symbols} sym</span>
                </li>
              ))}
            </ul>
          )}
        </div>
      )}

      {cascade.length > 0 && (
        <div>
          <p className="text-violet-300 mb-1">Cascade-applied ({cascade.length})</p>
          <ul className="space-y-0.5">
            {cascade.map((c) => (
              <li key={c.qname}>
                <button
                  className="font-mono text-[11px] text-2 hover:text-accent transition-colors"
                  onClick={() => reveal(c.qname)}
                >
                  {c.qname.split(":").pop()}
                </button>
              </li>
            ))}
          </ul>
        </div>
      )}

      {unresolved.length > 0 && (
        <div>
          <p className="text-amber-300 mb-1">Needs you ({unresolved.length})</p>
          <ul className="space-y-1.5">
            {unresolved.map((u, i) => (
              <li key={i} className="rounded border border-amber-800/40 bg-amber-500/5 p-2">
                <button
                  className="font-mono text-[11px] text-1 hover:text-accent transition-colors"
                  onClick={() => reveal(u.qname)}
                >
                  {u.qname}
                </button>
                {u.code && <span className="ml-2 text-[10px] text-amber-400 uppercase">{u.code}</span>}
                {u.message && <p className="text-[11px] text-2 mt-0.5">{u.message}</p>}
                {u.source_pointer && (
                  <p className="text-[10px] font-mono text-faint mt-0.5">{u.source_pointer}</p>
                )}
              </li>
            ))}
          </ul>
        </div>
      )}

      {report.error?.message && <p style={{ color: "var(--danger)" }}>{report.error.message}</p>}
    </div>
  )
}
