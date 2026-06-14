// Synthetic non-code cognition surfaces (Filesystem, Bash, Web, Database, Git).
// These give attention that happens outside indexed code a home so the map isn't
// systematically misleading. They live entirely in the AGM layer — never in the
// symbol graph or triefacts. Treated as pseudo-symbols with a fixed role so they
// roll up and render alongside real nodes.

import {
  SYNTHETIC_NODES,
  SYNTHETIC_QNAME_PREFIX,
  syntheticQname,
  isSyntheticFileQname,
  isSyntheticQname,
  syntheticFilePath,
  type SyntheticNode,
} from "@/api/types"

// Synthetic nodes form their own role/continent so they cluster together and
// never distort a real role's mass.
export const SYNTHETIC_ROLE = "external"

// Per-file synthetic nodes share this role so they cluster into one region
// (rendered as the "FILE READS" heading) rather than scattering as lone
// "external" floaters.
export const SYNTHETIC_FILE_ROLE = "file reads"

// Role for any synthetic qname (resolved dynamically — per-file nodes are
// created at ingest time and aren't in the static role map). Returns null for
// non-synthetic qnames so callers can fall through to the real role map.
export function syntheticRole(qname: string): string | null {
  if (isSyntheticFileQname(qname)) return SYNTHETIC_FILE_ROLE
  if (isSyntheticQname(qname)) return SYNTHETIC_ROLE
  return null
}

// Display label for any synthetic qname: a per-file node shows its basename; a
// fixed surface (Filesystem/Bash/…) shows its name. Returns null otherwise.
export function syntheticLabel(qname: string): string | null {
  const path = syntheticFilePath(qname)
  if (path != null) return path.split("/").pop() || path
  if (isSyntheticQname(qname)) return qname.slice(SYNTHETIC_QNAME_PREFIX.length)
  return null
}

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
