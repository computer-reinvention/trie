import { useTabsStore, GRAPH_TAB_ID, type Tab } from "@/store/tabsStore"
import { useGraphStore } from "@/store/graphStore"
import { openContextMenu } from "@/store/contextMenuStore"

// The tab strip across the top of the editor area. Tab #1 is the graph
// (permanent, no close button); the rest are files. Each file tab shows a
// tiny Source/Triefact pill so the active face is visible at a glance.

function GraphIcon() {
  return (
    <svg width="12" height="12" viewBox="0 0 16 16" fill="none" className="opacity-70">
      <circle cx="3" cy="8" r="2" fill="currentColor" />
      <circle cx="13" cy="4" r="2" fill="currentColor" />
      <circle cx="13" cy="12" r="2" fill="currentColor" />
      <path d="M4.7 7L11.3 4.5M4.7 9L11.3 11.5" stroke="currentColor" strokeWidth="1" />
    </svg>
  )
}

function CloseIcon() {
  return (
    <svg width="10" height="10" viewBox="0 0 10 10" fill="none">
      <path d="M1 1L9 9M9 1L1 9" stroke="currentColor" strokeWidth="1.4" strokeLinecap="round" />
    </svg>
  )
}

function TabButton({ tab, active }: { tab: Tab; active: boolean }) {
  const { activate, close, toggleView, setView, tabs } = useTabsStore()
  const revealFile = useGraphStore((s) => s.revealFile)

  const base =
    "group flex items-center gap-1.5 h-8 px-3 text-xs font-mono border-r border-slate-800 select-none cursor-pointer whitespace-nowrap"
  const tone = active
    ? "bg-slate-900 text-slate-100"
    : "bg-slate-950 text-slate-500 hover:text-slate-300 hover:bg-slate-900/60"

  if (tab.kind === "graph") {
    return (
      <div className={`${base} ${tone}`} onClick={() => activate(GRAPH_TAB_ID)} title="System graph">
        <GraphIcon />
        <span>graph</span>
      </div>
    )
  }

  return (
    <div
      className={`${base} ${tone}`}
      onClick={() => activate(tab.id)}
      onAuxClick={(e) => {
        // middle-click closes
        if (e.button === 1) close(tab.id)
      }}
      onContextMenu={(e) =>
        openContextMenu(e, [
          {
            label: tab.view === "triefact" ? "Show Source" : "Show Triefact",
            onSelect: () => setView(tab.id, tab.view === "triefact" ? "source" : "triefact"),
          },
          {
            label: "Reveal in Graph",
            onSelect: () => {
              revealFile(tab.relPath)
              activate(GRAPH_TAB_ID)
            },
          },
          { label: "-", onSelect: () => {} },
          { label: "Close", onSelect: () => close(tab.id) },
          {
            label: "Close Others",
            onSelect: () =>
              tabs
                .filter((t) => t.kind === "file" && t.id !== tab.id)
                .forEach((t) => close(t.id)),
          },
        ])
      }
      title={tab.relPath}
    >
      <span className="truncate max-w-[160px]">{tab.name}</span>
      <button
        className={`ml-0.5 rounded px-1 py-0.5 text-[9px] uppercase tracking-wide ${
          tab.view === "triefact"
            ? "bg-indigo-500/20 text-indigo-300"
            : "bg-slate-700/40 text-slate-400"
        }`}
        onClick={(e) => {
          e.stopPropagation()
          toggleView(tab.id)
        }}
        title={tab.view === "triefact" ? "Showing triefact — click for source" : "Showing source — click for triefact"}
      >
        {tab.view === "triefact" ? "tf" : "src"}
      </button>
      <button
        className="ml-0.5 rounded p-0.5 text-slate-600 opacity-0 group-hover:opacity-100 hover:bg-slate-700 hover:text-slate-200"
        onClick={(e) => {
          e.stopPropagation()
          close(tab.id)
        }}
        title="Close tab"
      >
        <CloseIcon />
      </button>
    </div>
  )
}

export function TabStrip() {
  const tabs = useTabsStore((s) => s.tabs)
  const activeId = useTabsStore((s) => s.activeId)

  return (
    <div className="flex items-stretch h-8 bg-slate-950 border-b border-slate-800 overflow-x-auto scroll-thin shrink-0">
      {tabs.map((tab) => (
        <TabButton key={tab.id} tab={tab} active={tab.id === activeId} />
      ))}
    </div>
  )
}
