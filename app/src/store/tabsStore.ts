import { create } from "zustand"

// The editor is tab-driven. Tab #1 is always the graph (the "model of the
// system" view); it is permanent and cannot be closed. Every other tab is a
// file, identified by its project-relative path. Each file tab remembers which
// face it shows — the raw Source or the generated Triefact prose — so the user
// can flip between them per-tab without losing the other tabs' modes.

export type TabView = "source" | "triefact"

// The graph tab id is kept as "graph" for back-compat (deep links, showGraph),
// but it now represents the ATTENTION (AGM) view. Topology (legacy structural
// graph) is a separate permanent tab.
export const GRAPH_TAB_ID = "graph" // Attention (AGM)
export const TOPOLOGY_TAB_ID = "topology" // Topology (legacy structural graph)
export const PATCHES_TAB_ID = "patches"

export interface GraphTab {
  id: typeof GRAPH_TAB_ID
  kind: "graph"
}

export interface TopologyTab {
  id: typeof TOPOLOGY_TAB_ID
  kind: "topology"
}

export interface PatchesTab {
  id: typeof PATCHES_TAB_ID
  kind: "patches"
}

export interface FileTab {
  id: string // === relPath
  kind: "file"
  relPath: string
  // Display name (basename) — precomputed so the strip never re-splits paths.
  name: string
  view: TabView
  // Optional deep-link targets, consumed once by the view on open:
  //  - triefact view scrolls to / highlights pendingFocusQname
  //  - source view scrolls to pendingFocusLine
  pendingFocusQname?: string
  pendingFocusLine?: number
}

export type Tab = GraphTab | TopologyTab | PatchesTab | FileTab

interface TabsStore {
  tabs: Tab[]
  activeId: string

  // Open (or focus, if already open) a file tab. `view` sets the initial face
  // only when the tab is first created; an already-open tab keeps its own view
  // unless `view` is explicitly passed AND `forceView` is true.
  openFile: (
    relPath: string,
    opts?: { view?: TabView; forceView?: boolean; focusQname?: string; focusLine?: number },
  ) => void
  // Activate the graph tab.
  showGraph: () => void
  activate: (id: string) => void
  close: (id: string) => void
  // Flip the active (or named) file tab between source and triefact.
  setView: (id: string, view: TabView) => void
  toggleView: (id: string) => void
  // Clear the one-shot deep-link targets once the view has consumed them.
  clearPendingFocus: (id: string) => void
  clearPendingLine: (id: string) => void
}

function basename(relPath: string): string {
  const parts = relPath.split("/")
  return parts[parts.length - 1] || relPath
}

export const useTabsStore = create<TabsStore>((set, get) => ({
  tabs: [
    { id: GRAPH_TAB_ID, kind: "graph" }, // Attention (AGM)
    { id: TOPOLOGY_TAB_ID, kind: "topology" }, // Topology (legacy)
    { id: PATCHES_TAB_ID, kind: "patches" },
  ],
  activeId: GRAPH_TAB_ID,

  openFile: (relPath, opts) => {
    const existing = get().tabs.find((t) => t.id === relPath)
    if (existing && existing.kind === "file") {
      set((s) => ({
        activeId: relPath,
        tabs: s.tabs.map((t) =>
          t.id === relPath && t.kind === "file"
            ? {
                ...t,
                view: opts?.forceView && opts.view ? opts.view : t.view,
                pendingFocusQname: opts?.focusQname ?? t.pendingFocusQname,
                pendingFocusLine: opts?.focusLine ?? t.pendingFocusLine,
              }
            : t,
        ),
      }))
      return
    }
    const tab: FileTab = {
      id: relPath,
      kind: "file",
      relPath,
      name: basename(relPath),
      view: opts?.view ?? "source",
      pendingFocusQname: opts?.focusQname,
      pendingFocusLine: opts?.focusLine,
    }
    set((s) => ({ tabs: [...s.tabs, tab], activeId: relPath }))
  },

  showGraph: () => set({ activeId: GRAPH_TAB_ID }),

  activate: (id) => set({ activeId: id }),

  close: (id) => {
    if (id === GRAPH_TAB_ID || id === TOPOLOGY_TAB_ID || id === PATCHES_TAB_ID) return // permanent
    set((s) => {
      const idx = s.tabs.findIndex((t) => t.id === id)
      if (idx === -1) return {}
      const tabs = s.tabs.filter((t) => t.id !== id)
      // If we closed the active tab, fall back to the neighbour to the left
      // (or the graph tab, which is always index 0).
      const activeId =
        s.activeId === id ? (tabs[Math.max(0, idx - 1)]?.id ?? GRAPH_TAB_ID) : s.activeId
      return { tabs, activeId }
    })
  },

  setView: (id, view) =>
    set((s) => ({
      tabs: s.tabs.map((t) => (t.id === id && t.kind === "file" ? { ...t, view } : t)),
    })),

  toggleView: (id) =>
    set((s) => ({
      tabs: s.tabs.map((t) =>
        t.id === id && t.kind === "file"
          ? { ...t, view: t.view === "source" ? "triefact" : "source" }
          : t,
      ),
    })),

  clearPendingFocus: (id) =>
    set((s) => ({
      tabs: s.tabs.map((t) =>
        t.id === id && t.kind === "file" ? { ...t, pendingFocusQname: undefined } : t,
      ),
    })),

  clearPendingLine: (id) =>
    set((s) => ({
      tabs: s.tabs.map((t) =>
        t.id === id && t.kind === "file" ? { ...t, pendingFocusLine: undefined } : t,
      ),
    })),
}))
