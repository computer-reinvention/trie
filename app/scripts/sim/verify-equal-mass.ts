// Reproduce the FILE READS vertical-stack bug: a large group of EQUAL-mass
// nodes in ONE role (all same radius → all seeded at the same anchor). Asserts
// the cluster spreads in 2-D, not a single column, and has zero overlaps.
// Run:  cd app && npx tsx scripts/sim/verify-equal-mass.ts

import {
  placeSymbol,
  applyAnchorCohesion,
  resolveLayout,
  type PolarPlacement,
  type Sized,
} from "../../src/agm/layout"

const MIN_GAP = 8
const DOT = 16
const pillHalfWidth = (q: string) => (q.length * 7 + 14) / 2
const regionLabelHalfWidth = (r: string) => (r.toUpperCase().length * 9) / 2

// 18 equal-mass "file read" nodes, all in the "file reads" role.
const FILES = [
  "llm.py", "apply.py", "config.py", "single_file.py", "scheduler.py",
  "pipeline.py", "incremental.py", "cascade.py", "reconcile.py", "scan.py",
  "models.py", "references.py", "bootstrap.py", "python.py", "generator.py",
  "mcp_server.py", "check.py", "freshness.py", "writer.py", "store.py",
]
const roleByQ = new Map<string, string>(FILES.map((f) => [f, "file reads"]))
const roleList = ["file reads"]

const placements: PolarPlacement[] = FILES.map((q) =>
  // identical displayMass + maxDisplay → identical radius for ALL of them
  placeSymbol({ qname: q, role: "file reads", roles: roleList, displayMass: 5, maxDisplay: 5, historicalMass: 0 }),
)

// sanity: before cohesion every node is at the SAME point (the bug's seed)
const r0 = Math.hypot(placements[0].x, placements[0].y)
const allSame = placements.every((p) => Math.abs(Math.hypot(p.x, p.y) - r0) < 1e-6)
console.log(`seed: all ${FILES.length} nodes same radius=${r0.toFixed(0)}? ${allSame}`)

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

// metrics: bounding box of the cluster — a healthy 2-D cluster has comparable
// width and height; a vertical COLUMN has width ≪ height.
const xs = placements.map((p) => p.x)
const ys = placements.map((p) => p.y)
const w = Math.max(...xs) - Math.min(...xs)
const h = Math.max(...ys) - Math.min(...ys)
const aspect = w / h

// overlap check across all pairs (nodes + label)
const boxes: Sized[] = placements.map((p) => ({ qname: p.qname, x: p.x, y: p.y, hw: pillHalfWidth(p.qname), hh: 9 }))
for (const l of layout.labels) boxes.push({ qname: `__label__:${l.role}`, x: l.x, y: l.y, hw: regionLabelHalfWidth(l.role) + 4, hh: 8, fixed: true })
let overlaps = 0
for (let i = 0; i < boxes.length; i++)
  for (let j = i + 1; j < boxes.length; j++) {
    const a = boxes[i], b = boxes[j]
    if (a.hw + b.hw + MIN_GAP - Math.abs(a.x - b.x) > 0 && a.hh + b.hh + MIN_GAP - Math.abs(a.y - b.y) > 0) overlaps++
  }

console.log(`cluster bbox: width=${w.toFixed(0)} height=${h.toFixed(0)} aspect(w/h)=${aspect.toFixed(2)}`)
console.log(`overlapping pairs: ${overlaps}`)

let ok = true
if (overlaps > 0) { console.error("❌ FAIL: overlaps present"); ok = false }
// a column would have aspect well below ~0.3; require a genuinely 2-D spread.
if (aspect < 0.45) { console.error(`❌ FAIL: cluster is a vertical column (aspect ${aspect.toFixed(2)} < 0.45)`); ok = false }
if (!ok) process.exit(1)
console.log("✅ PASS: equal-mass cluster spreads in 2-D with zero overlaps.")
