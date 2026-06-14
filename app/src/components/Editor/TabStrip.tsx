import {
  useTabsStore,
  GRAPH_TAB_ID,
  TOPOLOGY_TAB_ID,
  PATCHES_TAB_ID,
  TRIE_TAB_ID,
  type Tab,
} from "@/store/tabsStore"
import { useGraphStore } from "@/store/graphStore"
import { usePatchesStore } from "@/store/patchesStore"
import { useTrieCommandStore } from "@/store/trieCommandStore"
import { openContextMenu } from "@/store/contextMenuStore"

// The tab strip across the top of the editor area. Tab #1 is the graph
// (permanent, no close button); the rest are files. Each file tab shows a
// tiny Source/Triefact pill so the active face is visible at a glance.

// Attention (AGM): a focus reticle — concentric rings around a centre.
function AttentionIcon() {
  return (
    <svg width="12" height="12" viewBox="0 0 16 16" fill="none" className="opacity-70">
      <circle cx="8" cy="8" r="6" stroke="currentColor" strokeWidth="1" />
      <circle cx="8" cy="8" r="1.6" fill="currentColor" />
      <path d="M8 0.5V3M8 13v2.5M0.5 8H3M13 8h2.5" stroke="currentColor" strokeWidth="1" />
    </svg>
  )
}

// Topology (structural graph): connected nodes.
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

// trie commands: a terminal prompt glyph.
function TrieIcon() {
  return (
    <svg width="12" height="12" viewBox="0 0 16 16" fill="none" className="opacity-70">
      <path d="M3 4l3 3-3 3" stroke="currentColor" strokeWidth="1.3" strokeLinecap="round" strokeLinejoin="round" />
      <path d="M8.5 11H13" stroke="currentColor" strokeWidth="1.3" strokeLinecap="round" />
    </svg>
  )
}

function TrieTabButton({
  base,
  tone,
  onClick,
}: {
  base: string
  tone: string
  onClick: () => void
}) {
  const running = useTrieCommandStore((s) => s.running)
  return (
    <div className={`${base} ${tone}`} onClick={onClick} title="trie lifecycle commands">
      <TrieIcon />
      <span>trie</span>
      {running && (
        <span
          className="w-2 h-2 rounded-full trie-pulse"
          style={{ background: "var(--accent)" }}
        />
      )}
    </div>
  )
}

function CloseIcon() {
  return (
    <svg width="10" height="10" viewBox="0 0 10 10" fill="none">
      <path d="M1 1L9 9M9 1L1 9" stroke="currentColor" strokeWidth="1.4" strokeLinecap="round" />
    </svg>
  )
}

function PatchesTabButton({
  base,
  tone,
  onClick,
}: {
  base: string
  tone: string
  onClick: () => void
}) {
  const count = usePatchesStore((s) => s.patches.length)
  const applying = usePatchesStore((s) => s.applyInProgress)
  return (
    <div className={`${base} ${tone}`} onClick={onClick} title="Pending patches">
      <span>patches</span>
      {applying ? (
        <span
          className="w-2.5 h-2.5 border-2 rounded-full animate-spin"
          style={{ borderColor: "var(--border-strong)", borderTopColor: "var(--warn)" }}
        />
      ) : count > 0 ? (
        <span
          className="rounded-full text-[10px] px-1.5 leading-4 min-w-4 text-center"
          style={{
            background: "color-mix(in srgb, var(--warn) 25%, transparent)",
            color: "#fcd34d",
          }}
        >
          {count}
        </span>
      ) : null}
    </div>
  )
}

function TabButton({ tab, active }: { tab: Tab; active: boolean }) {
  const { activate, close, toggleView, setView, tabs } = useTabsStore()
  const revealFile = useGraphStore((s) => s.revealFile)

  const base =
    "group flex items-center gap-1.5 h-8 px-3 text-xs font-mono border-r border-subtle select-none cursor-pointer whitespace-nowrap transition-colors"
  const tone = active
    ? "surface-1 text-1"
    : "text-3 hover:text-2 hover:surface-1"

  if (tab.kind === "graph") {
    return (
      <div
        className={`${base} ${tone}`}
        onClick={() => activate(GRAPH_TAB_ID)}
        title="Attention — live agent cognitive state (AGM)"
      >
        <AttentionIcon />
        <span>attention</span>
      </div>
    )
  }

  if (tab.kind === "topology") {
    return (
      <div
        className={`${base} ${tone}`}
        onClick={() => activate(TOPOLOGY_TAB_ID)}
        title="Topology — codebase structure (roles, subsystems, dependencies)"
      >
        <GraphIcon />
        <span>topology</span>
      </div>
    )
  }

  if (tab.kind === "patches") {
    return <PatchesTabButton base={base} tone={tone} onClick={() => activate(PATCHES_TAB_ID)} />
  }

  if (tab.kind === "trie") {
    return <TrieTabButton base={base} tone={tone} onClick={() => activate(TRIE_TAB_ID)} />
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
            label: "Reveal in Topology",
            onSelect: () => {
              revealFile(tab.relPath)
              activate(TOPOLOGY_TAB_ID)
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
        className={`ml-0.5 rounded px-1 py-0.5 text-[9px] uppercase tracking-wide transition-colors ${
          tab.view === "triefact" ? "bg-accent-soft text-accent" : "surface-3 text-2"
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
        className="ml-0.5 rounded p-0.5 text-faint opacity-0 group-hover:opacity-100 hover:surface-3 hover:text-1 transition-all"
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
    <div
      className="flex items-stretch h-8 border-b border-subtle overflow-x-auto scroll-thin shrink-0"
      style={{ background: "var(--bg-app)" }}
    >
      {tabs.map((tab) => (
        <TabButton key={tab.id} tab={tab} active={tab.id === activeId} />
      ))}
    </div>
  )
}
