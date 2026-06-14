import { useState, useCallback, type MouseEvent } from "react"
import { useGraphStore } from "@/store/graphStore"
import { useTabsStore, TOPOLOGY_TAB_ID, type TabView } from "@/store/tabsStore"
import { useAppStore } from "@/store/appStore"
import { openContextMenu } from "@/store/contextMenuStore"
import { FileTree } from "./FileTree"
import { Legend } from "@/components/GraphCanvas/Legend"

export function Sidebar() {
  const { projectDir } = useAppStore()
  const focusFile = useGraphStore((s) => s.focusFile)
  const revealFile = useGraphStore((s) => s.revealFile)
  const openFile = useTabsStore((s) => s.openFile)
  // Whether single-clicking a file opens its Source or its Triefact (Prose).
  const [treeMode, setTreeMode] = useState<TabView>("source")
  const [legendOpen, setLegendOpen] = useState(false)
  // Collapsed: the sidebar shrinks to a sleek rail; click to expand.
  const [collapsed, setCollapsed] = useState(false)

  const toRel = useCallback(
    (filePath: string) => (projectDir ? filePath.replace(projectDir + "/", "") : filePath),
    [projectDir],
  )

  // Left-click: open the file in a tab (in the tree's current mode) and focus
  // its symbols in the graph so the two views stay in lockstep.
  const onFileClick = useCallback(
    (filePath: string) => {
      const rel = toRel(filePath)
      focusFile(rel)
      openFile(rel, { view: treeMode })
    },
    [toRel, focusFile, openFile, treeMode],
  )

  // Right-click: a context menu with explicit open-as actions + graph reveal.
  const onFileRightClick = useCallback(
    (filePath: string, e: MouseEvent) => {
      const rel = toRel(filePath)
      openContextMenu(e, [
        { label: "Open Source", onSelect: () => openFile(rel, { view: "source", forceView: true }) },
        {
          label: "Open Triefact",
          onSelect: () => openFile(rel, { view: "triefact", forceView: true }),
        },
        { label: "-", onSelect: () => {} },
        {
          label: "Reveal in Topology",
          onSelect: () => {
            revealFile(rel)
            useTabsStore.getState().activate(TOPOLOGY_TAB_ID)
          },
        },
      ])
    },
    [toRel, openFile, focusFile],
  )

  if (!projectDir) return null

  // Collapsed: a sleek 9px-wide rail with an expand chevron + vertical "files"
  // label. Click anywhere on the rail to expand.
  if (collapsed) {
    return (
      <aside
        className="w-9 shrink-0 surface-1 border-r border-subtle flex flex-col items-center py-2 gap-3 cursor-pointer hover:surface-2 group"
        onClick={() => setCollapsed(false)}
        title="Expand file tree"
      >
        <span className="text-3 group-hover:text-2 text-xs leading-none">›</span>
        <span
          className="text-faint group-hover:text-3 text-[10px] uppercase tracking-widest select-none"
          style={{ writingMode: "vertical-rl" }}
        >
          files
        </span>
      </aside>
    )
  }

  return (
    <aside className="w-60 shrink-0 surface-1 border-r border-subtle flex flex-col overflow-hidden">
      <div className="h-8 px-3 border-b border-subtle flex items-center justify-between gap-2 shrink-0">
        <button
          className="text-faint hover:text-2 text-xs leading-none shrink-0 transition-colors"
          onClick={() => setCollapsed(true)}
          title="Collapse file tree"
        >
          ‹
        </button>
        <p className="text-3 text-xs font-mono truncate flex-1">
          {projectDir.split("/").pop()}
        </p>
        <div className="flex rounded overflow-hidden border border-strong text-[9px] font-mono shrink-0">
          <button
            className={`px-1.5 py-0.5 transition-colors ${
              treeMode === "source" ? "surface-3 text-1" : "text-3 hover:text-2"
            }`}
            onClick={() => setTreeMode("source")}
            title="Click opens source"
          >
            src
          </button>
          <button
            className={`px-1.5 py-0.5 transition-colors ${
              treeMode === "triefact" ? "bg-accent-soft text-accent" : "text-3 hover:text-2"
            }`}
            onClick={() => setTreeMode("triefact")}
            title="Click opens triefact prose"
          >
            tf
          </button>
        </div>
      </div>

      {/* File tree takes all available height and scrolls. */}
      <div className="flex-1 min-h-0 overflow-y-auto scroll-thin">
        <FileTree dir={projectDir} onFileClick={onFileClick} onFileRightClick={onFileRightClick} />
      </div>

      {/* Legend is a collapsible drawer pinned to the bottom; collapsed by
          default so the tree gets the room. Its own bounded scroll when open. */}
      <div className="shrink-0 border-t border-subtle">
        <button
          className="w-full px-3 py-1.5 flex items-center gap-1.5 text-left hover:surface-2 transition-colors"
          onClick={() => setLegendOpen((v) => !v)}
        >
          <span className="text-faint text-xs">{legendOpen ? "▾" : "▸"}</span>
          <span className="text-3 text-[10px] uppercase tracking-wide">Graph legend</span>
        </button>
        {legendOpen && (
          <div className="max-h-[45vh] overflow-y-auto scroll-thin border-t border-subtle">
            <Legend />
          </div>
        )}
      </div>
    </aside>
  )
}
