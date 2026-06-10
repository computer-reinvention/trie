// Shared ASCII renderer for AGM simulations. Uses the REAL engine + layout so
// the ASCII frame is a faithful preview of on-screen behaviour. Renders:
//   - fixed centre crosshair (+)  = current attention origin
//   - repo "spring" edges (faint, drawn with · / : )
//   - attention edges (agent traversal, drawn with * )
//   - symbols as name PILLS placed at their polar position
//   - numeric table: radius / angle / mass / role / symbol
//   - role rollup, trail, investigation confidence, convergence gap

import { AttentionModel } from "../../src/agm/attentionModel"
import { AttentionGraph } from "../../src/agm/attentionGraph"
import { InvestigationRegistry } from "../../src/agm/investigations"
import {
  placeSymbol,
  applyClusterCohesion,
  applyVisibleBudget,
  computeRoleClusters,
  type PolarPlacement,
} from "../../src/agm/layout"

const VISIBLE_BUDGET = 60

export interface SimContext {
  model: AttentionModel
  graph: AttentionGraph
  investigations: InvestigationRegistry
  roleByQname: Map<string, string>
  histByQname: Map<string, number>
  roles: string[]
  // repo out-edges by qname (for spring rendering)
  edgesByQname: Map<string, Array<{ to: string; kind: string }>>
}

const W = 90
const H = 35
const CX = Math.floor(W / 2)
const CY = Math.floor(H / 2)
const RS = Math.min(CX / 1.7, CY) - 1
const R_MAX_WORLD = 620
const ASPECT = 1.7 // chars are taller than wide; stretch x

function shortName(q: string): string {
  return q.split(":").pop() ?? q
}

function toScreen(p: { x: number; y: number }): { sx: number; sy: number } {
  return {
    sx: CX + Math.round((p.x / R_MAX_WORLD) * RS * ASPECT),
    sy: CY + Math.round((p.y / R_MAX_WORLD) * RS),
  }
}

// Bresenham line into the grid, only writing onto blank cells with `ch`.
function drawLine(grid: string[][], x0: number, y0: number, x1: number, y1: number, ch: string) {
  let dx = Math.abs(x1 - x0)
  let dy = -Math.abs(y1 - y0)
  const sx = x0 < x1 ? 1 : -1
  const sy = y0 < y1 ? 1 : -1
  let err = dx + dy
  let x = x0
  let y = y0
  let guard = 0
  while (guard++ < 1000) {
    if (x >= 0 && x < W && y >= 0 && y < H && grid[y][x] === " ") grid[y][x] = ch
    if (x === x1 && y === y1) break
    const e2 = 2 * err
    if (e2 >= dy) {
      err += dy
      x += sx
    }
    if (e2 <= dx) {
      err += dx
      y += sy
    }
  }
}

export interface FrameOpts {
  label?: string
  showRepoEdges?: boolean
  maxRows?: number
}

export function renderFrame(ctx: SimContext, now: number, opts: FrameOpts = {}) {
  const { model, graph, roleByQname, histByQname, roles, edgesByQname } = ctx
  const snap = model.snapshot(now)
  let maxD = 0
  for (const m of snap.values()) if (m.display > maxD) maxD = m.display

  const placements: PolarPlacement[] = []
  for (const [q, m] of snap) {
    placements.push(
      placeSymbol({
        qname: q,
        role: roleByQname.get(q) ?? "untagged",
        roles,
        displayMass: m.display,
        maxDisplay: maxD,
        historicalMass: histByQname.get(q) ?? 0,
      }),
    )
  }
  applyClusterCohesion(placements, roleByQname, histByQname)
  // visible budget — same cap as the canvas, keeps the ASCII field readable
  const massForBudget = new Map<string, number>()
  for (const [q, m] of snap) massForBudget.set(q, m.display)
  const budget = applyVisibleBudget(placements, massForBudget, roleByQname, VISIBLE_BUDGET)
  const visible = budget.kept
  const posByQ = new Map(visible.map((p) => [p.qname, p]))

  const grid: string[][] = Array.from({ length: H }, () => Array.from({ length: W }, () => " "))

  // repo spring edges (faint) — only between visible nodes
  if (opts.showRepoEdges) {
    for (const [from, p] of posByQ) {
      const outs = edgesByQname.get(from)
      if (!outs) continue
      const a = toScreen(p)
      for (const e of outs) {
        const tp = posByQ.get(e.to)
        if (!tp) continue
        const b = toScreen(tp)
        drawLine(grid, a.sx, a.sy, b.sx, b.sy, "·")
      }
    }
  }

  // attention edges (agent traversal) — bright, drawn over springs
  for (const ae of graph.liveEdges(now)) {
    const a = posByQ.get(ae.from)
    const b = posByQ.get(ae.to)
    if (!a || !b) continue
    const sa = toScreen(a)
    const sb = toScreen(b)
    drawLine(grid, sa.sx, sa.sy, sb.sx, sb.sy, "*")
  }

  // crosshair
  grid[CY][CX] = "+"

  // role pills at cluster centroids (2+ visible members) — mirrors the canvas.
  const clusterAcc = new Map<string, { sx: number; sy: number; n: number }>()
  for (const p of visible) {
    const role = roleByQname.get(p.qname) ?? "untagged"
    const s = toScreen(p)
    let a = clusterAcc.get(role)
    if (!a) {
      a = { sx: 0, sy: 0, n: 0 }
      clusterAcc.set(role, a)
    }
    a.sx += s.sx
    a.sy += s.sy
    a.n += 1
  }
  const rolePillRanges: Array<[number, number, number]> = []
  for (const [role, a] of clusterAcc) {
    if (a.n < 2) continue
    const cx = Math.round(a.sx / a.n)
    const cy = Math.round(a.sy / a.n)
    const pill = `<${role}>`
    const start = Math.max(0, Math.min(W - pill.length, cx - Math.floor(pill.length / 2)))
    if (cy >= 0 && cy < H) placePill(grid, cy, start, pill, rolePillRanges)
  }

  // symbol pills (name) — hottest first so they win contested cells. Each pill
  // searches outward (row offsets) for a free, non-overlapping slot so labels
  // don't collide. Lower-fidelity analogue of the canvas easing nodes apart.
  const ordered = [...visible].sort((a, b) => a.radius - b.radius)
  const placedRanges: Array<[number, number, number]> = [...rolePillRanges] // sy, sxStart, sxEnd
  for (const p of ordered) {
    const { sx, sy } = toScreen(p)
    const name = shortName(p.qname)
    const pill = `[${name}]`
    const start = Math.max(0, Math.min(W - pill.length, sx - Math.floor(pill.length / 2)))
    // try the home row, then ±1, ±2, ... up to ±4 rows for a clear slot
    let placed = false
    for (const off of [0, 1, -1, 2, -2, 3, -3, 4, -4]) {
      const ry = sy + off
      if (ry < 0 || ry >= H) continue
      const clash = placedRanges.some(
        ([yy, rs, re]) => yy === ry && !(start + pill.length - 1 < rs || start > re),
      )
      if (!clash) {
        placePill(grid, ry, start, pill, placedRanges)
        placed = true
        break
      }
    }
    if (!placed) placePill(grid, sy, start, pill, placedRanges) // give up; overwrite
  }

  // crosshair always wins (drawn last so no pill/edge hides the origin)
  grid[CY][CX] = "+"

  // ---- output ----
  console.log(`\n${"=".repeat(W)}`)
  console.log(
    `  t=${now}s  ${opts.label ?? ""}  active=${snap.size}  maxMass=${maxD.toFixed(2)}`,
  )
  console.log("-".repeat(W))
  for (const line of grid) console.log(line.join(""))
  console.log("-".repeat(W))
  console.log("  + origin   [name] symbol   * attention-edge   · repo-edge")

  // table
  const rows = visible.map((p) => ({
    q: shortName(p.qname),
    role: (roleByQname.get(p.qname) ?? "untagged").slice(0, 18),
    d: snap.get(p.qname)!.display,
    r: Math.round(p.radius),
    ang: Math.round((Math.atan2(p.y, p.x) * 180) / Math.PI),
  }))
  rows.sort((a, b) => a.r - b.r)
  console.log("\n  RADIUS ANGLE  MASS  ROLE                SYMBOL")
  for (const r of rows.slice(0, opts.maxRows ?? 14)) {
    console.log(
      `  ${String(r.r).padStart(5)} ${String(r.ang).padStart(4)}° ${r.d.toFixed(2).padStart(5)}  ${r.role.padEnd(18)}  ${r.q}`,
    )
  }

  // role rollup + trail + convergence + investigation
  const roleMass = [...model.roleMass(now).values()].sort((a, b) => b.live - a.live).slice(0, 5)
  console.log("\n  roles: " + roleMass.map((r) => `${r.role}(${r.live.toFixed(0)})`).join("  "))
  if (budget.foldedTotal > 0)
    console.log(`  visible budget: showing ${visible.length}, folded +${budget.foldedTotal} (over budget)`)
  const trail = graph.trail()
  if (trail.length) console.log("  trail: " + trail.map(shortName).join(" → "))
  const liveOnly = new Map<string, number>()
  for (const [q, m] of snap) liveOnly.set(q, m.live)
  ctx.investigations.updateActive(liveOnly)
  const inv = ctx.investigations.active()
  if (inv) console.log(`  investigation: "${inv.label}"  confidence=${inv.confidence.toFixed(2)}`)
  if (rows.length >= 2) {
    const nearest = rows[0].r
    const meanRest = rows.slice(1).reduce((s, r) => s + r.r, 0) / (rows.length - 1)
    const clusters = [...computeRoleClusters(visible, roleByQname).values()].filter(
      (c) => c.count >= 2,
    )
    console.log(
      `  convergence gap: ${Math.round(meanRest - nearest)}px   multi-clusters: ${clusters.length}`,
    )
  }
}

function placePill(
  grid: string[][],
  sy: number,
  start: number,
  pill: string,
  ranges: Array<[number, number, number]>,
) {
  const s = Math.max(0, Math.min(grid[0].length - pill.length, start))
  for (let i = 0; i < pill.length; i++) grid[sy][s + i] = pill[i]
  ranges.push([sy, s, s + pill.length - 1])
}
