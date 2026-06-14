import { useState, useEffect, type MouseEvent } from "react"

interface DirEntry {
  name: string
  isDirectory: boolean
  path: string
}

interface FileTreeProps {
  dir: string
  onFileClick: (path: string) => void
  onFileRightClick: (path: string, e: MouseEvent) => void
  depth?: number
}

export function FileTree({ dir, onFileClick, onFileRightClick, depth = 0 }: FileTreeProps) {
  const [entries, setEntries] = useState<DirEntry[]>([])
  const [expanded, setExpanded] = useState<Set<string>>(new Set())

  useEffect(() => {
    const trie = (window as any).trie
    if (trie?.readDir) {
      trie.readDir(dir).then((es: DirEntry[]) => {
        // Sort: directories first, then files, both alphabetically
        const sorted = [...es].sort((a, b) => {
          if (a.isDirectory !== b.isDirectory) return a.isDirectory ? -1 : 1
          return a.name.localeCompare(b.name)
        })
        // Skip hidden dirs and common noise
        const filtered = sorted.filter(
          (e) =>
            !e.name.startsWith(".") &&
            e.name !== "node_modules" &&
            e.name !== "__pycache__" &&
            e.name !== "dist" &&
            e.name !== "build",
        )
        setEntries(filtered)
      })
    }
  }, [dir])

  const indent = depth * 12

  return (
    <ul className="text-xs">
      {entries.map((entry) => (
        <li key={entry.path}>
          {entry.isDirectory ? (
            <>
              <button
                className="flex items-center w-full px-2 py-0.5 hover:surface-3 text-2 font-mono transition-colors"
                style={{ paddingLeft: `${8 + indent}px` }}
                onClick={() =>
                  setExpanded((s) => {
                    const n = new Set(s)
                    n.has(entry.path) ? n.delete(entry.path) : n.add(entry.path)
                    return n
                  })
                }
              >
                <span className="mr-1 opacity-50">{expanded.has(entry.path) ? "▾" : "▸"}</span>
                {entry.name}/
              </button>
              {expanded.has(entry.path) && (
                <FileTree
                  dir={entry.path}
                  onFileClick={onFileClick}
                  onFileRightClick={onFileRightClick}
                  depth={depth + 1}
                />
              )}
            </>
          ) : (
            <button
              className="flex items-center w-full px-2 py-0.5 hover:surface-3 text-2 font-mono transition-colors"
              style={{ paddingLeft: `${8 + indent + 12}px` }}
              onClick={() => onFileClick(entry.path)}
              onContextMenu={(e) => {
                e.preventDefault()
                onFileRightClick(entry.path, e)
              }}
            >
              {entry.name}
            </button>
          )}
        </li>
      ))}
    </ul>
  )
}
