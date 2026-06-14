// Shared builder for the symbol right-click context menu. Used by BOTH the AGM
// canvas and the legacy graph view so the action set stays consistent. Returns
// grouped ContextMenuItem[] (separators are items with label "-").
//
// Side-effecting actions are wired to existing infra:
//   - navigation  → tabsStore.openFile (source / triefact)
//   - ask agent   → "trie:node-selected" window event (adds a composer pill)
//   - AGM verbs   → agmStore (negative evidence, investigation)
//   - clipboard   → navigator.clipboard
//   - blast radius / patch / stats → host-provided callbacks (UI varies by view)

import type { ContextMenuItem } from "@/store/contextMenuStore"
import { useTabsStore } from "@/store/tabsStore"
import { useAGMStore } from "@/store/agmStore"

export interface SymbolMenuContext {
  qname: string
  filePath?: string
  signature?: string | null
  // Host callbacks — each view supplies how it surfaces these (panel, toast…).
  onShowBlastRadius?: (qname: string) => void
  onTracecallers?: (qname: string) => void
  onTraceCallees?: (qname: string) => void
  onStagePatch?: (qname: string) => void
  onRename?: (qname: string) => void
  onDelete?: (qname: string) => void
  onShowStats?: (qname: string) => void
  onReadProse?: (qname: string) => void
}

const SEP: ContextMenuItem = { label: "-", onSelect: () => {} }

// Ask the agent about this symbol: add a context pill to the composer.
function askAgentAbout(qname: string) {
  window.dispatchEvent(new CustomEvent("trie:node-selected", { detail: { qname } }))
}

function copy(text: string) {
  void navigator.clipboard?.writeText(text)
}

export function buildSymbolMenu(ctx: SymbolMenuContext): ContextMenuItem[] {
  const { qname, filePath, signature } = ctx
  const open = useTabsStore.getState().openFile
  const agm = useAGMStore.getState()
  const items: ContextMenuItem[] = []

  // --- navigation / inspection ---
  if (filePath) {
    items.push({
      label: "Open triefact",
      onSelect: () => open(filePath, { view: "triefact", forceView: true, focusQname: qname }),
    })
    items.push({
      label: "Open source",
      onSelect: () => open(filePath, { view: "source", forceView: true }),
    })
  }
  if (ctx.onReadProse) items.push({ label: "Read prose", onSelect: () => ctx.onReadProse!(qname) })

  // --- graph exploration ---
  items.push(SEP)
  if (ctx.onTracecallers)
    items.push({ label: "Trace callers", onSelect: () => ctx.onTracecallers!(qname) })
  if (ctx.onTraceCallees)
    items.push({ label: "Trace callees", onSelect: () => ctx.onTraceCallees!(qname) })
  if (ctx.onShowBlastRadius)
    items.push({ label: "Show blast radius", onSelect: () => ctx.onShowBlastRadius!(qname) })

  // --- AGM attention verbs ---
  items.push(SEP)
  items.push({
    label: "Mark as ruled out",
    onSelect: () => agm.addNegativeEvidence(qname),
  })
  items.push({
    label: "Start investigation here",
    onSelect: () => {
      const id = `inv-${Date.now().toString(36)}`
      agm.setInvestigation(id, qname.split(":").pop() ?? qname, "active")
      agm.ingest(qname, "read")
      agm.recompute()
    },
  })
  if (ctx.onShowStats)
    items.push({ label: "Show attention stats", onSelect: () => ctx.onShowStats!(qname) })

  // --- agent handoff ---
  items.push(SEP)
  items.push({ label: "Ask agent about this", onSelect: () => askAgentAbout(qname) })

  // --- editing / patches ---
  if (ctx.onStagePatch || ctx.onRename || ctx.onDelete) {
    items.push(SEP)
    if (ctx.onStagePatch)
      items.push({ label: "Stage patch…", onSelect: () => ctx.onStagePatch!(qname) })
    if (ctx.onRename) items.push({ label: "Rename…", onSelect: () => ctx.onRename!(qname) })
    if (ctx.onDelete)
      items.push({ label: "Delete symbol", danger: true, onSelect: () => ctx.onDelete!(qname) })
  }

  // --- clipboard ---
  items.push(SEP)
  items.push({ label: "Copy qname", onSelect: () => copy(qname) })
  if (signature) items.push({ label: "Copy one-liner", onSelect: () => copy(signature) })

  return items
}
