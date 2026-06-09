// Synthetic non-code cognition surfaces (Filesystem, Bash, Web, Database, Git).
// These give attention that happens outside indexed code a home so the map isn't
// systematically misleading. They live entirely in the AGM layer — never in the
// symbol graph or triefacts. Treated as pseudo-symbols with a fixed role so they
// roll up and render alongside real nodes.

import { SYNTHETIC_NODES, syntheticQname, type SyntheticNode } from "@/api/types"

// Synthetic nodes form their own role/continent so they cluster together and
// never distort a real role's mass.
export const SYNTHETIC_ROLE = "external"

export interface SyntheticDescriptor {
  node: SyntheticNode
  qname: string
  role: string
  label: string
}

export const SYNTHETIC_DESCRIPTORS: SyntheticDescriptor[] = SYNTHETIC_NODES.map((node) => ({
  node,
  qname: syntheticQname(node),
  role: SYNTHETIC_ROLE,
  label: node,
}))

// qname → descriptor, for quick lookup when rendering / rolling up.
export const SYNTHETIC_BY_QNAME = new Map(SYNTHETIC_DESCRIPTORS.map((d) => [d.qname, d]))

// Seed the attention model's role map with synthetic nodes so role rollups
// include them. Returns qname→role entries to merge into the role map.
export function syntheticRoleEntries(): Array<[string, string]> {
  return SYNTHETIC_DESCRIPTORS.map((d) => [d.qname, d.role])
}
