import { useActivityStore } from "@/store/activityStore"

// Compact title-bar indicator fed by the activity poll. Three states:
//   - active writer: spinner + op + done/total (any process, e.g. terminal sync)
//   - idle but stale: amber "N stale" pill
//   - idle and clean: renders nothing
//
// This is the cross-process counterpart to <TriefactStatus/> (which only shows
// the desktop's own refresh run); here we surface a terminal `trie sync` too.

const OP_LABEL: Record<string, string> = {
  sync: "Syncing",
  bootstrap: "Indexing",
  roles: "Classifying",
  refresh: "Refreshing",
}

export function ActivityBadge() {
  const status = useActivityStore((s) => s.status)
  const pending = useActivityStore((s) => s.pending)

  if (status?.is_active) {
    const label = OP_LABEL[status.op] ?? "Working"
    const counter = status.total > 0 ? `${status.done}/${status.total}` : null
    return (
      <div
        className="flex items-center gap-1.5 rounded px-2 py-0.5 text-[11px] font-mono"
        style={{ background: "var(--bg-panel, #0f172a)", color: "var(--text, #e2e8f0)" }}
        title={status.current_file ?? label}
      >
        <span className="w-3 h-3 border-2 border-slate-600 border-t-accent rounded-full animate-spin" />
        <span>{label}</span>
        {counter && <span className="text-slate-500">{counter}</span>}
      </div>
    )
  }

  if (status?.state === "error") {
    return (
      <div
        className="rounded px-2 py-0.5 text-[11px] font-mono text-red-400 bg-red-500/10"
        title={status.error ?? "Last run failed"}
      >
        sync failed
      </div>
    )
  }

  if (pending && pending.count > 0) {
    return (
      <div
        className="rounded px-2 py-0.5 text-[11px] font-mono text-amber-300 bg-amber-500/10"
        title={`${pending.count} file${pending.count !== 1 ? "s" : ""} need a sync:\n${pending.stale
          .slice(0, 12)
          .join("\n")}${pending.stale.length > 12 ? "\n…" : ""}`}
      >
        {pending.count} stale
      </div>
    )
  }

  return null
}
