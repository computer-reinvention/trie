import { useEffect, useState } from "react"
import { useRefreshStore } from "@/store/refreshStore"

// Human labels for the freshness-gate reasons emitted by `trie refresh --json`.
const REASON_LABEL: Record<string, string> = {
  empty_store: "Building graph from triefacts",
  no_stamp: "First-time indexing",
  head_moved: "Syncing after branch change",
  mtimes_moved: "Regenerating changed triefacts",
  unchanged: "Graph up to date",
  queued: "Refresh already running",
}

/**
 * Floating status display for triefact generation / graph refresh.
 *
 * Listens to the refreshStore (fed by `trie refresh --json` via IPC) and shows
 * a compact card in the bottom-right: a spinner + reason while running, a live
 * per-file progress bar when a sync actually fires, and a success/error line
 * that auto-dismisses. Idle renders nothing.
 */
export function TriefactStatus() {
  const { phase, reason, current, done, total, filesSynced, runningCostUsd, errorMessage } =
    useRefreshStore()
  const [dismissed, setDismissed] = useState(false)

  // Reset dismissal whenever a new run starts.
  useEffect(() => {
    if (phase === "running") setDismissed(false)
  }, [phase])

  // Auto-dismiss a successful run after a beat.
  useEffect(() => {
    if (phase !== "done") return
    const t = setTimeout(() => setDismissed(true), 2600)
    return () => clearTimeout(t)
  }, [phase])

  if (phase === "idle" || dismissed) return null

  const isSync = total > 0
  const pct = isSync ? Math.round((done / total) * 100) : 0
  const label = reason ? (REASON_LABEL[reason] ?? "Refreshing graph") : "Refreshing graph"

  return (
    <div
      className="absolute bottom-4 right-4 z-50 w-72 rounded-lg border border-subtle surface-pop elev-2 px-3 py-2.5"
    >
      <div className="flex items-center gap-2">
        {phase === "running" && (
          <span
            className="w-3.5 h-3.5 border-2 rounded-full animate-spin shrink-0"
            style={{ borderColor: "var(--border-strong)", borderTopColor: "var(--accent)" }}
          />
        )}
        {phase === "done" && (
          <span className="text-sm shrink-0" style={{ color: "#34d399" }}>✓</span>
        )}
        {phase === "error" && (
          <span className="text-sm shrink-0" style={{ color: "var(--danger)" }}>✗</span>
        )}

        <span className="text-1 text-xs font-medium flex-1 truncate">
          {phase === "error" ? "Refresh failed" : label}
        </span>

        {(phase === "done" || phase === "error") && (
          <button
            className="text-3 hover:text-1 text-xs shrink-0 transition-colors"
            onClick={() => setDismissed(true)}
            title="Dismiss"
          >
            ✕
          </button>
        )}
      </div>

      {/* Per-file progress (only when a sync is actually generating triefacts) */}
      {phase === "running" && isSync && (
        <div className="mt-2">
          <div
            className="h-1 rounded-full overflow-hidden"
            style={{ background: "var(--border-subtle)" }}
          >
            <div
              className="h-full bg-accent transition-[width] duration-300"
              style={{ width: `${pct}%` }}
            />
          </div>
          <div className="flex items-center justify-between mt-1">
            <span className="text-faint text-[10px] font-mono truncate max-w-[11rem]">
              {current ?? "…"}
            </span>
            <span className="text-faint text-[10px] font-mono shrink-0">
              {done}/{total}
            </span>
          </div>
        </div>
      )}

      {/* Indeterminate scan (no per-file work — graph rebuild from triefacts) */}
      {phase === "running" && !isSync && (
        <p className="text-faint text-[10px] mt-1.5">Reading triefacts — no LLM cost.</p>
      )}

      {/* Success summary */}
      {phase === "done" && (
        <p className="text-faint text-[10px] mt-1.5">
          {filesSynced > 0
            ? `Regenerated ${filesSynced} file${filesSynced !== 1 ? "s" : ""}` +
              (runningCostUsd > 0 ? ` · $${runningCostUsd.toFixed(4)}` : "")
            : "Graph is current."}
        </p>
      )}

      {/* Error detail */}
      {phase === "error" && errorMessage && (
        <p
          className="text-[10px] mt-1.5 font-mono line-clamp-3 break-words"
          style={{ color: "color-mix(in srgb, var(--danger) 80%, transparent)" }}
        >
          {errorMessage}
        </p>
      )}
    </div>
  )
}
