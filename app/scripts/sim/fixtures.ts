// Loads the REAL trie graph snapshot (dumped from the live desktop endpoints)
// and builds a SimContext wired with the same engine the canvas uses. This is
// the single source of truth the ASCII simulation reads from, so the sim is a
// faithful lower-fidelity mirror of the actual visualiser.

import { readFileSync } from "node:fs"
import { resolve, dirname } from "node:path"
import { fileURLToPath } from "node:url"
import { AttentionModel } from "../../src/agm/attentionModel"
import { AttentionGraph } from "../../src/agm/attentionGraph"
import { InvestigationRegistry } from "../../src/agm/investigations"
import type { SimContext } from "./render"

const __dirname = dirname(fileURLToPath(import.meta.url))

export interface RealGraph {
  roleByQname: Map<string, string>
  histByQname: Map<string, number>
  roles: string[]
  edgesByQname: Map<string, Array<{ to: string; kind: string }>>
  qnames: string[]
}

export function loadRealGraph(): RealGraph {
  const symbols = JSON.parse(
    readFileSync(resolve(__dirname, "real-symbols.json"), "utf8"),
  ).hits as Array<{ qname: string; role: string; historical_mass?: number }>
  const edges = JSON.parse(readFileSync(resolve(__dirname, "real-edges.json"), "utf8"))
    .edges as Array<{ from: string; to: string; kind: string }>

  const roleByQname = new Map<string, string>()
  const histByQname = new Map<string, number>()
  const roleSet = new Set<string>()
  const qnames: string[] = []
  for (const s of symbols) {
    const role = s.role || "untagged"
    roleByQname.set(s.qname, role)
    roleSet.add(role)
    qnames.push(s.qname)
    if (s.historical_mass && s.historical_mass > 0) histByQname.set(s.qname, s.historical_mass)
  }
  const edgesByQname = new Map<string, Array<{ to: string; kind: string }>>()
  for (const e of edges) {
    let list = edgesByQname.get(e.from)
    if (!list) {
      list = []
      edgesByQname.set(e.from, list)
    }
    list.push({ to: e.to, kind: e.kind })
  }
  return { roleByQname, histByQname, roles: [...roleSet].sort(), edgesByQname, qnames }
}

// Build a fresh SimContext (engine instances + graph data) from a RealGraph.
export function makeContext(g: RealGraph): SimContext {
  const model = new AttentionModel()
  model.setRoles(g.roleByQname)
  for (const [q, h] of g.histByQname) model.seedHistorical(q, h)
  return {
    model,
    graph: new AttentionGraph(),
    investigations: new InvestigationRegistry(),
    roleByQname: g.roleByQname,
    histByQname: g.histByQname,
    roles: g.roles,
    edgesByQname: g.edgesByQname,
  }
}

// A synthetic graph for stress/edge-case scenarios that don't need real data.
export function makeSyntheticContext(spec: {
  roles: Record<string, string[]> // role -> qnames
  edges?: Array<[string, string, string]> // [from, to, kind]
  hist?: Record<string, number>
}): SimContext {
  const roleByQname = new Map<string, string>()
  for (const [role, qs] of Object.entries(spec.roles)) for (const q of qs) roleByQname.set(q, role)
  const histByQname = new Map<string, number>(Object.entries(spec.hist ?? {}))
  const edgesByQname = new Map<string, Array<{ to: string; kind: string }>>()
  for (const [from, to, kind] of spec.edges ?? []) {
    let list = edgesByQname.get(from)
    if (!list) {
      list = []
      edgesByQname.set(from, list)
    }
    list.push({ to, kind })
  }
  const model = new AttentionModel()
  model.setRoles(roleByQname)
  for (const [q, h] of histByQname) model.seedHistorical(q, h)
  return {
    model,
    graph: new AttentionGraph(),
    investigations: new InvestigationRegistry(),
    roleByQname,
    histByQname,
    roles: [...new Set(roleByQname.values())].sort(),
    edgesByQname,
  }
}
