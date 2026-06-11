// Verify RIGID CLUSTER SEPARATION: multiple roles, each a cluster, must occupy
// SEPARATE regions — no two cluster bounding discs overlap — AND no node/label
// overlaps. Mirrors the screenshot (ORCHESTRATION vs CONFIG-MANAGEMENT bleeding
// into each other). Run:  cd app && npx tsx scripts/sim/verify-clusters.ts

import {
  placeSymbol,
  applyAnchorCohesion,
  resolveLayout,
  type PolarPlacement,
  type Sized,
} from "../../src/agm/layout"

const MIN_GAP = 8
const DOT = 16
const pillHalfWidth = (q: string) => ((q.split(":").pop() ?? q).length * 7 + 14) / 2
const regionLabelHalfWidth = (r: string) => (r.toUpperCase().length * 9) / 2

// three roles, several members each, varied masses (like the real graph)
const ROLES: Record<string, string[]> = {
  orchestration: ["scan_project", "run_incremental", "sync_single_file", "stage", "apply_patches", "generate_section", "_ensure_fresh", "stage_and_commit"],
  "config-management": ["Config", "build_system_model", "InProcessLLMBackend", "trie", "TrieClient", "build_server"],
  "source-parsing": ["extract_symbols", "extract_file_data", "Store", "ActivityWriter", "build_cascade_plan"],
}
const roleByQ = new Map<string, string>()
const roleList = Object.keys(ROLES)
const placements: PolarPlacement[] = []
let mass = 5
for (const [role, qs] of Object.entries(ROLES)) {
  qs.forEach((q, i) => {
    roleByQ.set(q, role)
    // varied mass within a role → varied radius (realistic)
    const m = 2 + ((i * 3) % 7)
    placements.push(placeSymbol({ qname: q, role, roles: roleList, displayMass: m, maxDisplay: 9, historicalMass: 0 }))
  })
  mass++
}

applyAnchorCohesion(placements, roleByQ, roleList)
const layout = resolveLayout({
  placements,
  roleByQname: roleByQ,
  isPill: () => true,
  pillHalfWidth: (q) => pillHalfWidth(q),
  regionLabelHalfWidth,
  haloMinCount: 2,
  pad: MIN_GAP,
  dotHalf: DOT / 2,
  pillHalfHeight: 9,
  haloMaxR: 150,
  haloNodeMargin: 26,
  haloLabelGap: 12,
  labelHalfHeight: 8,
})

// per-cluster discs (centroid + covering radius)
const discs = Object.keys(ROLES).map((role) => {
  const ms = placements.filter((p) => roleByQ.get(p.qname) === role)
  const cx = ms.reduce((s, p) => s + p.x, 0) / ms.length
  const cy = ms.reduce((s, p) => s + p.y, 0) / ms.length
  let r = 0
  for (const p of ms) r = Math.max(r, Math.hypot(p.x - cx, p.y - cy) + pillHalfWidth(p.qname))
  return { role, cx, cy, r }
})

let discOverlaps = 0
for (let i = 0; i < discs.length; i++)
  for (let j = i + 1; j < discs.length; j++) {
    const a = discs[i], b = discs[j]
    const d = Math.hypot(a.cx - b.cx, a.cy - b.cy)
    if (d < a.r + b.r) {
      discOverlaps++
      console.log(`  DISC OVERLAP: ${a.role} ✕ ${b.role}  gap=${(d - a.r - b.r).toFixed(0)}`)
    }
  }

// node + label overlap check
const boxes: Sized[] = placements.map((p) => ({ qname: p.qname, x: p.x, y: p.y, hw: pillHalfWidth(p.qname), hh: 9 }))
for (const l of layout.labels) boxes.push({ qname: `__label__:${l.role}`, x: l.x, y: l.y, hw: regionLabelHalfWidth(l.role) + 4, hh: 8, fixed: true })
let nodeOverlaps = 0
for (let i = 0; i < boxes.length; i++)
  for (let j = i + 1; j < boxes.length; j++) {
    const a = boxes[i], b = boxes[j]
    if (a.hw + b.hw + MIN_GAP - Math.abs(a.x - b.x) > 0 && a.hh + b.hh + MIN_GAP - Math.abs(a.y - b.y) > 0) nodeOverlaps++
  }

console.log(`clusters=${discs.length}  disc-overlaps=${discOverlaps}  node/label-overlaps=${nodeOverlaps}`)
let ok = true
if (discOverlaps > 0) { console.error("❌ FAIL: clusters share a region (disc overlap)"); ok = false }
if (nodeOverlaps > 0) { console.error("❌ FAIL: node/label overlaps"); ok = false }
if (!ok) process.exit(1)
console.log("✅ PASS: clusters occupy separate regions, zero node/label overlaps.")
