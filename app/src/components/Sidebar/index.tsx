import { useState, useCallback } from "react"
import { useGraphStore } from "@/store/graphStore"
import { FileTree } from "./FileTree"
import { ViewSourceModal } from "./ViewSourceModal"
import { Legend } from "@/components/GraphCanvas/Legend"
import { useAppStore } from "@/store/appStore"

export function Sidebar() {
  const { projectDir } = useAppStore()
  const { focusFile } = useGraphStore()
  const [viewSourcePath, setViewSourcePath] = useState<string | null>(null)

  const onFileClick = useCallback(
    (filePath: string) => {
      // Map absolute path to project-relative path for graph lookup
      const rel = projectDir ? filePath.replace(projectDir + "/", "") : filePath
      focusFile(rel)
    },
    [projectDir, focusFile],
  )

  const onFileRightClick = useCallback((filePath: string) => {
    setViewSourcePath(filePath)
  }, [])

  if (!projectDir) return null

  return (
    <aside className="w-60 shrink-0 bg-slate-900 border-r border-slate-800 flex flex-col overflow-hidden">
      <div className="px-3 py-2 border-b border-slate-800">
        <p className="text-slate-500 text-xs font-mono truncate">{projectDir.split("/").pop()}</p>
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
      {viewSourcePath && (
        <ViewSourceModal
          filePath={viewSourcePath}
          onClose={() => setViewSourcePath(null)}
        />
      )}
    </aside>
  )
}
