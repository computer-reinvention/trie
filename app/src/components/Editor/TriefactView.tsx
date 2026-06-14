import { useEffect, useRef, useState } from "react"
import ReactMarkdown from "react-markdown"
import { graphClient } from "@/api/graphClient"
import { openContextMenu } from "@/store/contextMenuStore"
import type { FileTriefactResult, TriefactSection } from "@/api/types"

// Renders the generated triefact for a file: a compact front-matter header
// followed by one card per symbol section. Cards are anchored by qname so the
// graph / source views can deep-link straight to a symbol. Each card offers a
// "view source" affordance that flips the tab to the source at that line.

interface TriefactViewProps {
  relPath: string
  focusQname?: string
  onFocusConsumed?: () => void
  // Jump to this symbol's source line in the source view of the same tab.
  onOpenSource?: (line: number, qname: string) => void
  // Open another symbol in the graph (e.g. clicking a referenced qname).
  onRevealInGraph?: (qname: string) => void
}

function anchorId(qname: string): string {
  // qnames contain ":" and "." — make a DOM-safe id.
  return "tf-" + qname.replace(/[^a-zA-Z0-9_-]/g, "_")
}

function RoleBadge({ role }: { role: string }) {
  if (!role) return null
  return (
    <span className="rounded bg-accent-soft text-accent px-1.5 py-0.5 text-[10px] uppercase tracking-wide">
      {role}
    </span>
  )
}

function SectionCard({
  section,
  onOpenSource,
  onRevealInGraph,
}: {
  section: TriefactSection
  onOpenSource?: (line: number, qname: string) => void
  onRevealInGraph?: (qname: string) => void
}) {
  return (
    <div
      id={anchorId(section.qname)}
      className="scroll-mt-4 rounded-lg border border-subtle surface-1 overflow-hidden"
      onContextMenu={(e) =>
        openContextMenu(e, [
          ...(section.start_line > 0 && onOpenSource
            ? [
                {
                  label: "Open Source",
                  onSelect: () => onOpenSource(section.start_line, section.qname),
                },
              ]
            : []),
          ...(onRevealInGraph
            ? [{ label: "Reveal in Graph", onSelect: () => onRevealInGraph(section.qname) }]
            : []),
        ])
      }
    >
      <div className="flex items-center gap-2 px-3 py-2 border-b border-subtle surface-2">
        <span className="text-[10px] text-3 uppercase">{section.kind || "symbol"}</span>
        <span className="font-mono text-xs text-1 truncate flex-1">{section.qname}</span>
        <RoleBadge role={section.role} />
        {section.start_line > 0 && onOpenSource && (
          <button
            className="text-[10px] text-3 hover:text-accent font-mono transition-colors"
            onClick={() => onOpenSource(section.start_line, section.qname)}
            title="Jump to source"
          >
            L{section.start_line}
          </button>
        )}
      </div>
      <div className="px-3 py-2 md md-sm">
        {section.body ? (
          <ReactMarkdown>{section.body}</ReactMarkdown>
        ) : (
          <p className="text-faint italic">{section.one_liner || "No prose."}</p>
        )}
      </div>
    </div>
  )
}

export function TriefactView({
  relPath,
  focusQname,
  onFocusConsumed,
  onOpenSource,
  onRevealInGraph,
}: TriefactViewProps) {
  const [data, setData] = useState<FileTriefactResult | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [loading, setLoading] = useState(true)
  const scrollRef = useRef<HTMLDivElement | null>(null)

  useEffect(() => {
    let cancelled = false
    setLoading(true)
    setError(null)
    graphClient
      .fileTriefact(relPath)
      .then((res) => {
        if (cancelled) return
        setData(res)
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

  // Scroll to a deep-linked symbol card once rendered.
  useEffect(() => {
    if (loading || !focusQname || !data) return
    const el = document.getElementById(anchorId(focusQname))
    if (el) {
      el.scrollIntoView({ block: "center" })
      el.classList.add("ring-1", "ring-accent")
      setTimeout(() => el.classList.remove("ring-1", "ring-accent"), 1600)
    }
    onFocusConsumed?.()
  }, [loading, focusQname, data, onFocusConsumed])

  if (error) {
    return (
      <div className="p-4 text-xs font-mono" style={{ color: "var(--danger)" }}>
        Failed to load triefact: {error}
      </div>
    )
  }
  if (loading) {
    return <div className="p-4 text-xs text-3 font-mono">loading triefact…</div>
  }
  if (!data || !data.exists) {
    return (
      <div className="p-6 text-center text-xs text-3 font-mono">
        No triefact for <span className="text-1">{relPath}</span> yet.
        <br />
        Run a sync to generate prose for this file.
      </div>
    )
  }

  return (
    <div ref={scrollRef} className="h-full min-h-0 overflow-y-auto scroll-thin p-4 space-y-3">
      <div className="flex items-baseline justify-between">
        <h2 className="font-mono text-sm text-1">{relPath}</h2>
        <span className="text-[10px] text-3">{data.sections.length} symbols</span>
      </div>
      {data.sections.map((section) => (
        <SectionCard
          key={section.qname}
          section={section}
          onOpenSource={onOpenSource}
          onRevealInGraph={onRevealInGraph}
        />
      ))}
    </div>
  )
}
