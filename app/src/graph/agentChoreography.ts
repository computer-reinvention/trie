// Translates live agent tool activity into graph choreography: which symbols
// the agent is reading / scanning / writing, what colour they glow, and where
// the camera should follow. Driven by `desktop.part.updated` (full tool parts).
//
// The agent's real tool vocabulary (verified from telemetry) is the trie_* MCP
// tools plus the file-edit tools. Tools fall into three intents:
//   - read:  trie_read, trie_explain_symbol(_references), trie_trace(_flow),
//            trie_explain_flow            -> blue, primary target FOLLOWED
//   - scan:  trie_grep(_symbol|_str|_entry_points|_symbol_and_neighbours)
//                                          -> violet, hits coloured, NOT followed
//   - write: trie_patch, write/edit tools -> amber, target FOLLOWED
//
// A separate camera controller (in useOpenCodeSSE) consumes the returned
// `follow` qname (if any), debounced, so a burst of scans never thrashes.

import type { ToolPart } from "@/api/types"

export type Intent = "read" | "scan" | "write"

export interface ChoreographyResult {
  // symbols to glow + the state to glow them in
  reads: string[]
  scans: string[]
  writes: string[]
  // file paths the agent edited (glow whole file)
  files: string[]
  // a single primary symbol the camera should follow (read/write targets only)
  follow: string | null
  // edge sequences to animate as comets (from trace/flow results)
  flows: Array<{ from: string; to: string }>
}

const EMPTY: ChoreographyResult = {
  reads: [],
  scans: [],
  writes: [],
  files: [],
  follow: null,
  flows: [],
}

// Strip the MCP server prefix the model sees ("trie_read" -> "read").
function bareTool(tool: string): string {
  return tool.startsWith("trie_") ? tool.slice(5) : tool
}

function asString(v: unknown): string | null {
  return typeof v === "string" && v.length > 0 ? v : null
}

// Pull qnames out of a tool's JSON result text (grep/trace/explain hits).
function qnamesFromOutput(output: string | undefined): { hits: string[]; flows: Array<{ from: string; to: string }> } {
  if (!output) return { hits: [], flows: [] }
  let parsed: unknown
  try {
    parsed = JSON.parse(output)
  } catch {
    return { hits: [], flows: [] }
  }
  const hits: string[] = []
  const flows: Array<{ from: string; to: string }> = []
  const o = parsed as Record<string, unknown>

  const pushQ = (q: unknown) => {
    const s = asString(q)
    if (s) hits.push(s)
  }

  // grep family: { hits: [{qname}] }
  if (Array.isArray(o?.hits)) for (const h of o.hits) pushQ((h as Record<string, unknown>)?.qname)
  // grep_symbol: { match: {qname}, similar: [{qname}] }
  if (o?.match) pushQ((o.match as Record<string, unknown>)?.qname)
  if (Array.isArray(o?.similar)) for (const m of o.similar) pushQ((m as Record<string, unknown>)?.qname)
  // grep_symbol_and_neighbours: callers/callees
  for (const key of ["callers", "callees"]) {
    if (Array.isArray(o?.[key])) for (const m of o[key] as unknown[]) pushQ((m as Record<string, unknown>)?.qname)
  }
  // fuzzy/text fallback: { matches: [{qname}] } under `fallback`
  const fb = o?.fallback as Record<string, unknown> | undefined
  if (fb && Array.isArray(fb.matches)) for (const m of fb.matches) pushQ((m as Record<string, unknown>)?.qname)

  // trace: { edges: [{from,to}] }
  if (Array.isArray(o?.edges)) {
    for (const e of o.edges as unknown[]) {
      const from = asString((e as Record<string, unknown>)?.from)
      const to = asString((e as Record<string, unknown>)?.to)
      if (from && to) flows.push({ from, to })
    }
  }
  // trace_flow / explain_flow: { paths: [[qname,...]] } or { paths:[{chain:[...]}] }
  if (Array.isArray(o?.paths)) {
    for (const p of o.paths as unknown[]) {
      const chain = Array.isArray(p) ? (p as unknown[]) : ((p as Record<string, unknown>)?.chain as unknown[])
      if (Array.isArray(chain)) {
        for (let i = 0; i + 1 < chain.length; i++) {
          const from = asString(chain[i])
          const to = asString(chain[i + 1])
          if (from && to) flows.push({ from, to })
        }
      }
    }
  }
  return { hits, flows }
}

// Compute choreography for a single tool part at its current state.
export function choreographFor(part: ToolPart): ChoreographyResult {
  const tool = bareTool(part.tool)
  const input = part.state.input ?? {}
  const status = part.state.status
  const done = status === "completed"

  // --- read intent ----------------------------------------------------
  if (tool === "read" || tool === "explain_symbol" || tool === "explain_symbol_references") {
    const q = asString(input.sym) ?? asString(input.qname)
    return { ...EMPTY, reads: q ? [q] : [], follow: q }
  }
  if (tool === "trace" || tool === "explain_flow_single") {
    const q = asString(input.from_qname) ?? asString(input.sym)
    const { flows } = done ? qnamesFromOutput(part.state.output) : { flows: [] }
    return { ...EMPTY, reads: q ? [q] : [], follow: q, flows }
  }
  if (tool === "trace_flow" || tool === "explain_flow") {
    const a = asString(input.symbol1)
    const b = asString(input.symbol2)
    const reads = [a, b].filter((x): x is string => !!x)
    const { flows } = done ? qnamesFromOutput(part.state.output) : { flows: [] }
    return { ...EMPTY, reads, follow: a ?? b, flows }
  }

  // --- scan intent (grep family) -- colour hits, never move the camera --
  if (
    tool === "grep" ||
    tool === "grep_symbol" ||
    tool === "grep_str" ||
    tool === "grep_entry_points" ||
    tool === "grep_symbol_and_neighbours"
  ) {
    // an explicit name target also breathes while searching
    const target = asString(input.sym) ?? asString(input.name_contains)
    const { hits } = done ? qnamesFromOutput(part.state.output) : { hits: [] }
    const scans = [...(target ? [target] : []), ...hits]
    return { ...EMPTY, scans }
  }

  // --- write intent ---------------------------------------------------
  if (tool === "patch") {
    const q = asString(input.qname)
    return { ...EMPTY, writes: q ? [q] : [], follow: q }
  }
  if (tool === "write" || tool === "edit" || tool === "write_file" || tool === "str_replace_editor") {
    const path = asString(input.path) ?? asString(input.filePath)
    return { ...EMPTY, files: path ? [path] : [], follow: null }
  }

  return EMPTY
}
