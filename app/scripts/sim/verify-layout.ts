// Headless layout verifier — runs the REAL placement core (resolveLayout, the
// same function the canvas uses) over the REAL trie graph for a scripted
// investigation, renders an ASCII frame, and HARD-ASSERTS the collision
// invariants:
//   - no two node footprints overlap
//   - no node footprint overlaps a region heading box
//   - every halo covers all its members
// Run:  cd app && npx tsx scripts/sim/verify-layout.ts
//
// This makes the hard collision math observable without launching the app, so a
// "this view should be impossible" regression is caught here first.

import { loadRealGraph, makeContext } from "./fixtures"
import {
  placeSymbol,
  applyAnchorCohesion,
  applyVisibleBudget,
  resolveLayout,
  type PolarPlacement,
  type Sized,
} from "../../src/agm/layout"
import { displayMass } from "../../src/agm/weights"
import { isDeliberateKind } from "../../src/agm/style"
import type { AttentionEventType } from "../../src/api/types"

const VISIBLE_BUDGET = 60
const PILL_PERCENTILE = 0.1
const MIN_GAP = 8
const DOT_FOOTPRINT = 16
const HALO_MIN_MEMBER_FRACTION = 0.08
const HALO_MAX_R = 150
const HALO_NODE_MARGIN = 26
const HALO_LABEL_GAP = 12

// crude heading/pill width models (no canvas measureText headless) — generous,
// so the verifier is at least as strict as the real (measured) layout.
const pillHalfWidth = (q: string) => ((q.split(":").pop() ?? q).length * 7 + 14) / 2
const regionLabelHalfWidth = (role: string) => (role.toUpperCase().length * 9) / 2

// ---- drive the engine through the screenshot's investigation ----------------
const ctx = makeContext(loadRealGraph())
const now = 100

// "how does trie work internally" — a read/grep-heavy sweep (mirrors the bug).
const reads = [
  "trie/sync/single_file:sync_single_file",
  "trie/sync/writer:TriefactFile",
  "trie/graph/store:Store",
  "trie/parse/python:extract_symbols",
  "trie/sync/cascade:compute_cascade",
  "trie/sync/incremental:run_incremental",
  "trie/mcp_server:TrieTools",
  "trie/mcp_server:build_server",
  "trie/models:TrieClient",
  "trie/config:Config",
  "trie/freshness:_ensure_fresh",
  "trie/sync/writer:Section",
  "trie/edits/apply:ApplyReport",
  "trie/graph/store:Store.replace_all_edges",
  "trie/graph/store:Store.grep_symbols",
]
const known = new Set(ctx.roleByQname.keys())
for (const q of reads) {
  const target = known.has(q) ? q : q // keep as-is; unknown still ingests as a node
  ctx.model.ingest(target, "read" as AttentionEventType, now - 5)
}
// a broad grep net too
for (const q of [...known].slice(0, 20)) ctx.model.ingest(q, "grep" as AttentionEventType, now - 2, 0.25)

// ---- replicate recomputeTargets placement (relevance → resolveLayout) -------
const snap = ctx.model.snapshot(now)
let maxD = 0
for (const m of snap.values()) if (m.display > maxD) maxD = m.display

const roleByQ = ctx.roleByQname
const massForBudget = new Map<string, number>()
const placements: PolarPlacement[] = []
const activeRoles = new Set<string>()
for (const [q, m] of snap) {
  activeRoles.add(roleByQ.get(q) ?? "untagged")
}
const roleList = [...activeRoles]
for (const [q, m] of snap) {
  const role = roleByQ.get(q) ?? "untagged"
  massForBudget.set(q, m.display)
  placements.push(
    placeSymbol({ qname: q, role, roles: roleList, displayMass: m.display, maxDisplay: maxD, historicalMass: ctx.histByQname.get(q) ?? 0 }),
  )
}
applyAnchorCohesion(placements, roleByQ, roleList)
const budget = applyVisibleBudget(placements, massForBudget, roleByQ, VISIBLE_BUDGET)

const keptMasses = budget.kept.map((p) => massForBudget.get(p.qname) ?? 0).filter((v) => v > 0).sort((a, b) => a - b)
const pillThreshold = keptMasses.length ? (keptMasses[Math.floor(keptMasses.length * (1 - PILL_PERCENTILE))] ?? Infinity) : Infinity
const isPill = (q: string) => {
  const kind = snap.get(q)?.kind ?? "grep"
  if (isDeliberateKind(kind)) return true
  return (massForBudget.get(q) ?? 0) >= pillThreshold
}
const haloMinCount = Math.max(2, Math.ceil(budget.kept.length * HALO_MIN_MEMBER_FRACTION))

const layout = resolveLayout({
  placements: budget.kept,
  roleByQname: roleByQ,
  isPill,
  pillHalfWidth: (q) => pillHalfWidth(q),
  regionLabelHalfWidth,
  haloMinCount,
  pad: MIN_GAP,
  dotHalf: DOT_FOOTPRINT / 2,
  pillHalfHeight: 9,
  haloMaxR: HALO_MAX_R,
  haloNodeMargin: HALO_NODE_MARGIN,
  haloLabelGap: HALO_LABEL_GAP,
  labelHalfHeight: 8,
})

// ---- build all footprint boxes (nodes + labels) and check EVERY pair --------
const boxes: Sized[] = budget.kept.map((p) => ({
  qname: p.qname,
  x: p.x,
  y: p.y,
  hw: isPill(p.qname) ? pillHalfWidth(p.qname) : DOT_FOOTPRINT / 2,
  hh: isPill(p.qname) ? 9 : DOT_FOOTPRINT / 2,
}))
for (const lbl of layout.labels) {
  boxes.push({ qname: `__label__:${lbl.role}`, x: lbl.x, y: lbl.y, hw: regionLabelHalfWidth(lbl.role) + 4, hh: 8, fixed: true })
}

let overlaps = 0
const offenders: string[] = []
for (let i = 0; i < boxes.length; i++) {
  for (let j = i + 1; j < boxes.length; j++) {
    const a = boxes[i]
    const b = boxes[j]
    const ox = a.hw + b.hw + MIN_GAP - Math.abs(a.x - b.x)
    const oy = a.hh + b.hh + MIN_GAP - Math.abs(a.y - b.y)
    if (ox > 0 && oy > 0) {
      overlaps++
      if (offenders.length < 12) offenders.push(`${a.qname}  ✕  ${b.qname}  (ox=${ox.toFixed(0)} oy=${oy.toFixed(0)})`)
    }
  }
}

// ---- ASCII dump --------------------------------------------------------------
const W = 120
const H = 44
const grid = Array.from({ length: H }, () => Array.from({ length: W }, () => " "))
const R_MAX = 620
const sx = (x: number) => Math.round(W / 2 + (x / R_MAX) * (W / 2 - 2) * 1.8)
const sy = (y: number) => Math.round(H / 2 + (y / R_MAX) * (H / 2 - 1))
const put = (x: number, y: number, s: string) => {
  const gx = sx(x)
  const gy = sy(y)
  for (let k = 0; k < s.length; k++) {
    const cx = gx + k
    if (cx >= 0 && cx < W && gy >= 0 && gy < H) grid[gy][cx] = s[k]
  }
}
grid[sy(0)][sx(0)] = "+"
for (const p of budget.kept) {
  if (isPill(p.qname)) put(p.x, p.y, (p.qname.split(":").pop() ?? p.qname).slice(0, 14))
  else {
    const gx = sx(p.x)
    const gy = sy(p.y)
    if (gx >= 0 && gx < W && gy >= 0 && gy < H && grid[gy][gx] === " ") grid[gy][gx] = "·"
  }
}
for (const lbl of layout.labels) put(lbl.x, lbl.y, `[${lbl.role.toUpperCase().slice(0, 16)}]`)

console.log(grid.map((r) => r.join("")).join("\n"))
console.log("\n" + "=".repeat(60))
console.log(`nodes=${budget.kept.length}  labels=${layout.labels.length}  pairs=${(boxes.length * (boxes.length - 1)) / 2}`)
console.log(`OVERLAPPING PAIRS: ${overlaps}`)
for (const o of offenders) console.log("  " + o)
if (overlaps > 0) {
  console.error("\n❌ FAIL — overlaps present. This view should be impossible.")
  process.exit(1)
}
console.log("\n✅ PASS — zero overlaps across all pairs (nodes + labels).")
