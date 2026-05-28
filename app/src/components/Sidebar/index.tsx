import { useState, useCallback } from "react"
import { useGraphStore } from "@/store/graphStore"
import { FileTree } from "./FileTree"
import { ViewSourceModal } from "./ViewSourceModal"
import { useAppStore } from "@/store/appStore"

export function Sidebar() {
  const { projectDir } = useAppStore()
  const { setSelectedFilePath } = useGraphStore()
  const [viewSourcePath, setViewSourcePath] = useState<string | null>(null)

  const onFileClick = useCallback(
    (filePath: string) => {
      // Map absolute path to project-relative path for graph lookup
      const rel = projectDir ? filePath.replace(projectDir + "/", "") : filePath
      setSelectedFilePath(rel)
    },
    [projectDir, setSelectedFilePath],
  )

  const onFileRightClick = useCallback((filePath: string) => {
    setViewSourcePath(filePath)
  }, [])

  if (!projectDir) return null

  return (
    <aside className="w-56 shrink-0 bg-slate-900 border-r border-slate-800 flex flex-col overflow-hidden">
      <div className="px-3 py-2 border-b border-slate-800">
        <p className="text-slate-500 text-xs font-mono truncate">{projectDir.split("/").pop()}</p>
      </div>
      <div className="flex-1 overflow-y-auto">
        <FileTree
          dir={projectDir}
          onFileClick={onFileClick}
          onFileRightClick={onFileRightClick}
        />
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
