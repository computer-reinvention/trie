import { useEffect, useState } from "react"
import { SourceView } from "./SourceView"
import { TriefactView } from "./TriefactView"
import { useTabsStore, TOPOLOGY_TAB_ID, type FileTab } from "@/store/tabsStore"
import { useGraphStore } from "@/store/graphStore"

// Renders a single file tab's body and the per-tab Source⇄Triefact toggle.
// Deep-linking within a tab: clicking "view source" on a triefact card flips
// the face to source and scrolls to the symbol's line.

export function FileTabContent({ tab }: { tab: FileTab }) {
  const setView = useTabsStore((s) => s.setView)
  const activate = useTabsStore((s) => s.activate)
  const clearPendingFocus = useTabsStore((s) => s.clearPendingFocus)
  const clearPendingLine = useTabsStore((s) => s.clearPendingLine)
  const revealSymbol = useGraphStore((s) => s.revealSymbol)
  // One-shot line to scroll the source view to, set when crossing from triefact
  // or when the graph deep-links straight to a symbol's source line.
  const [pendingLine, setPendingLine] = useState<number | undefined>(undefined)

  // Adopt a deep-link line that arrived via the store (e.g. graph "Open Source").
  useEffect(() => {
    if (tab.pendingFocusLine != null) {
      setPendingLine(tab.pendingFocusLine)
      clearPendingLine(tab.id)
    }
  }, [tab.pendingFocusLine, tab.id, clearPendingLine])

  return (
    <div className="flex flex-col h-full min-h-0">
      <div className="flex items-center gap-1 px-3 py-1.5 border-b border-subtle surface-1 shrink-0">
        <span className="font-mono text-[11px] text-2 truncate flex-1">{tab.relPath}</span>
        <div className="flex rounded overflow-hidden border border-strong text-[10px] font-mono">
          <button
            className={`px-2 py-0.5 transition-colors ${
              tab.view === "source" ? "surface-3 text-1" : "text-3 hover:text-2"
            }`}
            onClick={() => setView(tab.id, "source")}
          >
            source
          </button>
          <button
            className={`px-2 py-0.5 transition-colors ${
              tab.view === "triefact" ? "bg-accent-soft text-accent" : "text-3 hover:text-2"
            }`}
            onClick={() => setView(tab.id, "triefact")}
          >
            triefact
          </button>
        </div>
      </div>

      <div className="flex-1 min-h-0">
        {tab.view === "source" ? (
          <SourceView
            relPath={tab.relPath}
            focusLine={pendingLine}
            onFocusConsumed={() => setPendingLine(undefined)}
          />
        ) : (
          <TriefactView
            relPath={tab.relPath}
            focusQname={tab.pendingFocusQname}
            onFocusConsumed={() => clearPendingFocus(tab.id)}
            onOpenSource={(line) => {
              setPendingLine(line)
              setView(tab.id, "source")
            }}
            onRevealInGraph={(qname) => {
              revealSymbol(qname)
              activate(TOPOLOGY_TAB_ID)
            }}
          />
        )}
      </div>
    </div>
  )
}
