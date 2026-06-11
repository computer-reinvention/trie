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
        className="w-9 shrink-0 bg-slate-900 border-r border-slate-800 flex flex-col items-center py-2 gap-3 cursor-pointer hover:bg-slate-800/60 group"
        onClick={() => setCollapsed(false)}
        title="Expand file tree"
      >
        <span className="text-slate-500 group-hover:text-slate-300 text-xs leading-none">›</span>
        <span
          className="text-slate-600 group-hover:text-slate-400 text-[10px] uppercase tracking-widest select-none"
          style={{ writingMode: "vertical-rl" }}
        >
          files
        </span>
      </aside>
    )
  }

  return (
    <aside className="w-60 shrink-0 bg-slate-900 border-r border-slate-800 flex flex-col overflow-hidden">
      <div className="h-8 px-3 border-b border-slate-800 flex items-center justify-between gap-2 shrink-0">
        <button
          className="text-slate-600 hover:text-slate-300 text-xs leading-none shrink-0"
          onClick={() => setCollapsed(true)}
          title="Collapse file tree"
        >
          ‹
        </button>
        <p className="text-slate-500 text-xs font-mono truncate flex-1">
          {projectDir.split("/").pop()}
        </p>
        <div className="flex rounded overflow-hidden border border-slate-700 text-[9px] font-mono shrink-0">
          <button
            className={`px-1.5 py-0.5 ${
              treeMode === "source" ? "bg-slate-700 text-slate-100" : "text-slate-500 hover:text-slate-300"
            }`}
            onClick={() => setTreeMode("source")}
            title="Click opens source"
          >
            src
          </button>
          <button
            className={`px-1.5 py-0.5 ${
              treeMode === "triefact"
                ? "bg-indigo-500/30 text-indigo-200"
                : "text-slate-500 hover:text-slate-300"
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
      <div className="shrink-0 border-t border-slate-800">
        <button
          className="w-full px-3 py-1.5 flex items-center gap-1.5 text-left hover:bg-slate-800/50"
          onClick={() => setLegendOpen((v) => !v)}
        >
          <span className="text-slate-600 text-xs">{legendOpen ? "▾" : "▸"}</span>
          <span className="text-slate-500 text-[10px] uppercase tracking-wide">Graph legend</span>
        </button>
        {legendOpen && (
          <div className="max-h-[45vh] overflow-y-auto scroll-thin border-t border-slate-800">
            <Legend />
          </div>
        )}
      </div>
    </aside>
  )
}
