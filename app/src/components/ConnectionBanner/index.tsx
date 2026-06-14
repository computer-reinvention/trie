import { useState } from "react"
import { useConnectionStore } from "@/store/connectionStore"

// eslint-disable-next-line @typescript-eslint/no-explicit-any
const trie = () => (window as any).trie

/**
 * Surfaces opencode backend health. When the sidecar crashes, a blocking banner
 * across the top of the workspace offers a one-click restart; when the event
 * stream merely drops, a quiet chip notes the temporary degradation (the main
 * process auto-reconnects). Live/connecting render nothing.
 */
export function ConnectionBanner() {
  const status = useConnectionStore((s) => s.status)
  const exitCode = useConnectionStore((s) => s.exitCode)
  const lastError = useConnectionStore((s) => s.lastError)
  const [restarting, setRestarting] = useState(false)

  if (status === "live" || status === "connecting") return null

  if (status === "degraded") {
    return (
      <div
        className="absolute top-2 left-1/2 -translate-x-1/2 z-50 inline-flex items-center gap-2 rounded-full px-3 py-1 text-[11px] elev-2"
        style={{
          background: "color-mix(in srgb, var(--warn) 14%, var(--surface-pop))",
          border: "1px solid color-mix(in srgb, var(--warn) 38%, transparent)",
          color: "var(--warn)",
        }}
        title={lastError ?? undefined}
      >
        <span className="w-1.5 h-1.5 rounded-full trie-pulse" style={{ background: "var(--warn)" }} />
        Reconnecting to opencode…
      </div>
    )
  }

  // crashed
  const restart = async () => {
    setRestarting(true)
    try {
      await trie()?.opencodeConfig?.restart()
    } finally {
      // useConnectionHealth flips back to live on the next servers-ready; if the
      // restart fails we re-enable the button so the user can retry.
      setRestarting(false)
    }
  }

  return (
    <div
      className="absolute top-0 left-0 right-0 z-50 flex items-center gap-3 px-4 py-2"
      style={{
        background: "color-mix(in srgb, var(--danger) 16%, var(--surface-pop))",
        borderBottom: "1px solid color-mix(in srgb, var(--danger) 40%, transparent)",
      }}
    >
      <span className="w-2 h-2 rounded-full shrink-0" style={{ background: "var(--danger)" }} />
      <div className="min-w-0 flex-1">
        <div className="text-xs font-medium" style={{ color: "var(--danger)" }}>
          opencode stopped responding
        </div>
        {lastError && (
          <div className="text-[11px] text-3 truncate font-mono" title={lastError}>
            {exitCode != null ? `exit ${exitCode} · ` : ""}
            {lastError}
          </div>
        )}
      </div>
      <button
        className="shrink-0 inline-flex items-center gap-1.5 rounded-md px-3 py-1 text-xs font-medium text-white transition-transform active:scale-95 disabled:opacity-60"
        style={{ background: "var(--danger)" }}
        onClick={restart}
        disabled={restarting}
      >
        {restarting ? "Restarting…" : "Restart"}
      </button>
    </div>
  )
}
