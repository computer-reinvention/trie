import { useEffect, useRef, useState } from "react"
import { EditorState, Compartment } from "@codemirror/state"
import { EditorView, lineNumbers, highlightActiveLine } from "@codemirror/view"
import { syntaxHighlighting, defaultHighlightStyle, foldGutter } from "@codemirror/language"
import { oneDark } from "@codemirror/theme-one-dark"
import { python } from "@codemirror/lang-python"
import { javascript } from "@codemirror/lang-javascript"
import { graphClient } from "@/api/graphClient"

// Read-only source viewer backed by CodeMirror 6. Syntax highlighting is
// chosen by extension; everything else falls back to plain text. The view can
// scroll to a specific 1-based line on open (deep-link from the graph/triefact).

function languageFor(relPath: string) {
  const ext = relPath.split(".").pop()?.toLowerCase()
  if (ext === "py" || ext === "pyi") return python()
  if (ext === "ts" || ext === "tsx") return javascript({ typescript: true, jsx: ext === "tsx" })
  if (ext === "js" || ext === "jsx" || ext === "mjs" || ext === "cjs")
    return javascript({ jsx: ext === "jsx" })
  return []
}

interface SourceViewProps {
  relPath: string
  focusLine?: number
  // Called after we've consumed the focusLine so the parent can clear it.
  onFocusConsumed?: () => void
}

export function SourceView({ relPath, focusLine, onFocusConsumed }: SourceViewProps) {
  const hostRef = useRef<HTMLDivElement | null>(null)
  const viewRef = useRef<EditorView | null>(null)
  const languageComp = useRef(new Compartment())
  const [error, setError] = useState<string | null>(null)
  const [loading, setLoading] = useState(true)

  // Build the editor once the host div exists.
  useEffect(() => {
    if (!hostRef.current) return
    const view = new EditorView({
      parent: hostRef.current,
      state: EditorState.create({
        doc: "",
        extensions: [
          lineNumbers(),
          foldGutter(),
          highlightActiveLine(),
          syntaxHighlighting(defaultHighlightStyle, { fallback: true }),
          oneDark,
          EditorView.editable.of(false),
          EditorState.readOnly.of(true),
          languageComp.current.of([]),
          EditorView.theme({
            "&": { height: "100%", fontSize: "12.5px" },
            ".cm-scroller": { fontFamily: "var(--font-mono, ui-monospace, monospace)" },
          }),
        ],
      }),
    })
    viewRef.current = view
    return () => {
      view.destroy()
      viewRef.current = null
    }
  }, [])

  // Load (or reload) source whenever the path changes.
  useEffect(() => {
    let cancelled = false
    setLoading(true)
    setError(null)
    graphClient
      .fileSource(relPath)
      .then((res) => {
        if (cancelled || !viewRef.current) return
        const content = res.type === "text" ? res.content : `[${res.type} file — not shown]`
        viewRef.current.dispatch({
          changes: { from: 0, to: viewRef.current.state.doc.length, insert: content },
          effects: languageComp.current.reconfigure(languageFor(relPath)),
        })
        setLoading(false)
      })
      .catch((err) => {
        if (cancelled) return
        setError(String(err))
        setLoading(false)
      })
    return () => {
      cancelled = true
    }
  }, [relPath])

  // Scroll to the deep-link line once content is present.
  useEffect(() => {
    if (loading || !focusLine || !viewRef.current) return
    const view = viewRef.current
    const lineCount = view.state.doc.lines
    const target = Math.min(Math.max(1, focusLine), lineCount)
    const pos = view.state.doc.line(target).from
    view.dispatch({
      selection: { anchor: pos },
      effects: EditorView.scrollIntoView(pos, { y: "center" }),
    })
    onFocusConsumed?.()
  }, [loading, focusLine, onFocusConsumed])

  if (error) {
    return (
      <div className="p-4 text-xs font-mono" style={{ color: "var(--danger)" }}>
        Failed to load {relPath}: {error}
      </div>
    )
  }

  return (
    <div className="relative h-full min-h-0">
      {loading && (
        <div className="absolute top-2 right-3 z-10 text-[10px] text-3 font-mono">loading…</div>
      )}
      <div ref={hostRef} className="h-full min-h-0" />
    </div>
  )
}
