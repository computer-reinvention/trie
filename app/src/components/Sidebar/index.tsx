import { useState, useCallback, type MouseEvent } from "react"
import { useGraphStore } from "@/store/graphStore"
import { useTabsStore, type TabView } from "@/store/tabsStore"
import { useAppStore } from "@/store/appStore"
import { openContextMenu } from "@/store/contextMenuStore"
import { FileTree } from "./FileTree"
import { Legend } from "@/components/GraphCanvas/Legend"

export function Sidebar() {
  const { projectDir } = useAppStore()
  const { focusFile } = useGraphStore()
  const openFile = useTabsStore((s) => s.openFile)
  // Whether single-clicking a file opens its Source or its Triefact (Prose).
  const [treeMode, setTreeMode] = useState<TabView>("source")

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
        { label: "Reveal in Graph", onSelect: () => focusFile(rel) },
      ])
    },
    [toRel, openFile, focusFile],
  )

  if (!projectDir) return null

  return (
    <aside className="w-60 shrink-0 bg-slate-900 border-r border-slate-800 flex flex-col overflow-hidden">
      <div className="px-3 py-2 border-b border-slate-800 flex items-center justify-between gap-2">
        <p className="text-slate-500 text-xs font-mono truncate">{projectDir.split("/").pop()}</p>
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
      {/* top half: file tree */}
      <div className="h-1/2 overflow-y-auto scroll-thin border-b border-slate-800">
        <FileTree
          dir={projectDir}
          onFileClick={onFileClick}
          onFileRightClick={onFileRightClick}
        />
      </div>
      {/* bottom half: legend / controls */}
      <div className="h-1/2 min-h-0">
        <Legend />
      </div>
    </aside>
  )
}
