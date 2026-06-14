// Convert real trie debug.jsonl telemetry into AGM attention events.
//
// Each mcp_call / cli_call carries the tool + its args. We map the tool to an
// attention event type (via the real classifier) and resolve a target qname:
//   - read/trace/explain*: args.qname | sym | from_qname (already a qname)
//   - grep_symbol / *_neighbours: args.sym (fuzzy → resolve against graph)
//   - read with args.path (file read): → Filesystem synthetic node
//   - grep / grep_str / grep_entry_points / find_files: a scan with no single
//     target → routed to the matched symbols if resolvable, else skipped
//
// Targets that don't resolve to a real symbol in the loaded graph are dropped
// (we can't place what isn't in the topology). Returns timestamped events.

import { readFileSync } from "node:fs"
import { classifyTool, syntheticTarget } from "../../src/agm/toolClassify"
import type { AttentionEventType } from "../../src/api/types"
import { syntheticQname } from "../../src/api/types"

export interface DebugEvent {
  t: number // seconds since first event
  type: AttentionEventType
  target: string
}

interface RawArgs {
  qname?: string
  sym?: string
  from_qname?: string
  symbol1?: string
  symbol2?: string
  path?: string
  predicate?: { name_contains?: string }
  regexp?: string
  query?: string
  pattern?: string
}

// Resolve a raw arg to a real qname present in `known`. Handles exact qnames,
// bare symbol names (suffix match after ':'), and file paths.
function resolveTargets(tool: string, args: RawArgs, known: Set<string>, byLocalName: Map<string, string[]>): string[] {
  const out: string[] = []
  const tryQ = (q?: string) => {
    if (!q) return
    if (known.has(q)) out.push(q)
    else {
      // bare local name → resolve to qname(s) ending in :name
      const hits = byLocalName.get(q)
      if (hits && hits.length) out.push(hits[0])
    }
  }
  tryQ(args.qname)
  tryQ(args.sym)
  tryQ(args.from_qname)
  tryQ(args.symbol1)
  tryQ(args.symbol2)
  // file read → Filesystem synthetic
  if (args.path && tool === "read") {
    out.push(syntheticQname("Filesystem"))
  }
  // explicit synthetic surfaces (find_files, grep_str_all, etc.)
  const synth = syntheticTarget(tool)
  if (synth && out.length === 0) out.push(synth)
  return out
}

export function eventsFromDebug(
  debugPath: string,
  knownQnames: Iterable<string>,
  opts: { sinceDay?: string; max?: number } = {},
): DebugEvent[] {
  const known = new Set(knownQnames)
  const byLocalName = new Map<string, string[]>()
  for (const q of known) {
    const local = q.includes(":") ? q.split(":").pop()! : q
    const list = byLocalName.get(local) ?? []
    list.push(q)
    byLocalName.set(local, list)
  }

  const raw = readFileSync(debugPath, "utf8").split("\n")
  const picked: Array<{ ts: number; type: AttentionEventType; target: string }> = []
  for (const line of raw) {
    if (!line) continue
    let e: { event?: string; tool?: string; ts?: string; args?: RawArgs }
    try {
      e = JSON.parse(line)
    } catch {
      continue
    }
    if (e.event !== "mcp_call" && e.event !== "cli_call") continue
    if (opts.sinceDay && (e.ts ?? "") < opts.sinceDay) continue
    const type = classifyTool(e.tool ?? "")
    if (!type) continue
    const ms = Date.parse(e.ts ?? "")
    if (Number.isNaN(ms)) continue
    const targets = resolveTargets(e.tool ?? "", e.args ?? {}, known, byLocalName)
    for (const target of targets) picked.push({ ts: ms / 1000, type, target })
  }
  if (picked.length === 0) return []
  picked.sort((a, b) => a.ts - b.ts)
  const t0 = picked[0].ts
  let events = picked.map((p) => ({ t: p.ts - t0, type: p.type, target: p.target }))
  if (opts.max && events.length > opts.max) events = events.slice(0, opts.max)
  return events
}
