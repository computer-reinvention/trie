// Playback of REAL recorded trie tool-use (debug.jsonl) through the AGM engine,
// rendered as ASCII frames. This is the closest thing to watching the actual
// agent's attention evolve over a real working session.
//
// Run:
//   cd app && npx tsx scripts/sim/playback.ts            # all resolvable events
//   cd app && npx tsx scripts/sim/playback.ts 2026-06-09 # only that day
//   cd app && npx tsx scripts/sim/playback.ts 2026-06-09 8   # day + N frames

import { resolve, dirname } from "node:path"
import { fileURLToPath } from "node:url"
import { loadRealGraph, makeContext } from "./fixtures"
import { renderFrame } from "./render"
import { eventsFromDebug } from "./from-debug"

const __dirname = dirname(fileURLToPath(import.meta.url))
const DEBUG = resolve(__dirname, "../../..", "debug.jsonl")

// positional args ignore the --session= flag
const positional = process.argv.slice(2).filter((a) => !a.startsWith("--"))
const sinceDay = positional[0] // e.g. "2026-06-09" or undefined for all
const frameCount = Number(positional[1] ?? 10)

const g = loadRealGraph()
const ctx = makeContext(g)
ctx.investigations.set({ id: "real", label: "real recorded session" })
ctx.graph.setInvestigation("real")

const all = eventsFromDebug(DEBUG, g.roleByQname.keys(), { sinceDay })
if (all.length === 0) {
  console.error("No resolvable events found" + (sinceDay ? ` for ${sinceDay}` : "") + ".")
  process.exit(1)
}

// Real telemetry spans many days with long idle gaps. Pick the single densest
// SESSION (events separated by < GAP seconds) so we watch one continuous
// investigation rather than empty inter-session voids. Re-base its timeline to 0.
const GAP = 600
const bursts: Array<typeof all> = []
let cur: typeof all = [all[0]]
for (let k = 1; k < all.length; k++) {
  if (all[k].t - all[k - 1].t > GAP) {
    bursts.push(cur)
    cur = []
  }
  cur.push(all[k])
}
bursts.push(cur)
// Sort by DISTINCT non-trivial activity (most informative session), falling back
// to event count. `--session=N` (0-based, after sort) overrides; default 0.
const distinct = (b: typeof all) => new Set(b.map((e) => e.target)).size
bursts.sort((a, b) => distinct(b) - distinct(a) || b.length - a.length)
const sessionArg = process.argv.find((a) => a.startsWith("--session="))
const sessionIdx = sessionArg ? Number(sessionArg.split("=")[1]) : 0
const session = bursts[Math.min(sessionIdx, bursts.length - 1)]
const base = session[0].t
const events = session.map((e) => ({ ...e, t: e.t - base }))

const span = events[events.length - 1].t
console.log(
  `Playback: densest session = ${events.length} resolved attention events over ${Math.round(span)}s` +
    (sinceDay ? ` (day ${sinceDay})` : " (all sessions scanned)"),
)
// breakdown
const byType: Record<string, number> = {}
for (const e of events) byType[e.type] = (byType[e.type] ?? 0) + 1
console.log("event types:", JSON.stringify(byType))

// Frame at evenly-spaced points across the timeline + a final cool-down frame.
const frameTimes: number[] = []
for (let i = 0; i < frameCount; i++) frameTimes.push((span * (i + 1)) / frameCount)
frameTimes.push(span + 600) // 10 min after last event → cool-down

let i = 0
for (const ft of frameTimes) {
  while (i < events.length && events[i].t <= ft) {
    const e = events[i]
    ctx.model.ingest(e.target, e.type, e.t)
    if (e.type === "trace" && i > 0 && events[i - 1].type === "trace") {
      // chain consecutive traces into the attention graph (agent traversal)
      ctx.graph.reinforce(events[i - 1].target, e.target, e.t)
    }
    i++
  }
  renderFrame(ctx, ft, { label: `[real playback]`, showRepoEdges: true, maxRows: 12 })
}
