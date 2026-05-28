import { useEffect, useRef, useState } from "react"
import { createPortal } from "react-dom"

interface ViewSourceModalProps {
  filePath: string
  onClose: () => void
}

export function ViewSourceModal({ filePath, onClose }: ViewSourceModalProps) {
  const [source, setSource] = useState<string | null>(null)
  const overlayRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    const trie = (window as any).trie
    if (trie?.readFile) {
      trie.readFile(filePath).then((text: string) => setSource(text))
    }
  }, [filePath])

  useEffect(() => {
    function onKey(e: KeyboardEvent) {
      if (e.key === "Escape") onClose()
    }
    window.addEventListener("keydown", onKey)
    return () => window.removeEventListener("keydown", onKey)
  }, [onClose])

  const fileName = filePath.split("/").pop() ?? filePath

  return createPortal(
    <div
      ref={overlayRef}
      className="fixed inset-0 bg-black/70 z-50 flex items-center justify-center p-8"
      onClick={(e) => {
        if (e.target === overlayRef.current) onClose()
      }}
    >
      <div className="bg-slate-900 border border-slate-700 rounded-xl w-full max-w-4xl max-h-[80vh] flex flex-col shadow-2xl">
        <div className="flex items-center justify-between px-4 py-3 border-b border-slate-700">
          <span className="text-slate-300 font-mono text-sm">{fileName}</span>
          <button
            className="text-slate-500 hover:text-slate-200 text-lg leading-none"
            onClick={onClose}
          >
            ×
          </button>
        </div>
        <div className="flex-1 overflow-auto">
          {source === null ? (
            <p className="text-slate-500 text-sm p-4">Loading…</p>
          ) : (
            <pre className="text-slate-300 text-xs font-mono p-4 leading-relaxed whitespace-pre overflow-x-auto">
              {source}
            </pre>
          )}
        </div>
      </div>
    </div>,
    document.body,
  )
}
