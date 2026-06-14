// AGM main simulation — drives the REAL engine over the REAL trie graph and
// renders the polar attention field as ASCII (with attention edges + repo
// springs + name pills), second by second.
//
// Run:  cd app && npx tsx scripts/sim/simulate.ts

import { loadRealGraph, makeContext } from "./fixtures"
import { renderFrame } from "./render"
import type { AttentionEventType } from "../../src/api/types"

const ctx = makeContext(loadRealGraph())
ctx.investigations.set({ id: "inv1", label: "how does sync write triefacts?" })
ctx.graph.setInvestigation("inv1")

// Scripted investigation using REAL qnames + REAL trace edges.
type Ev = [number, "grep" | "read" | "trace", string, string?]
const SCRIPT: Ev[] = [
  [0, "grep", "trie/sync/single_file:sync_single_file"],
  [1, "grep", "trie/sync/writer:TriefactFile"],
  [2, "grep", "trie/graph/store:Store"],
  [3, "grep", "trie/parse/python:extract_symbols"],
  [5, "read", "trie/sync/single_file:sync_single_file"],
  [7, "read", "trie/sync/writer:TriefactFile"],
  // trace chain (builds attention edges)
  [10, "trace", "trie/sync/single_file:sync_single_file", "trie/sync/writer:Section"],
  [11, "trace", "trie/sync/writer:Section", "trie/graph/store:Store"],
  [12, "trace", "trie/graph/store:Store", "trie/sync/writer:TriefactFile"],
  // converge on the writer
  [16, "read", "trie/sync/writer:TriefactFile"],
  [17, "trace", "trie/sync/writer:TriefactFile", "trie/sync/writer:Section"],
  [18, "read", "trie/sync/writer:TriefactFile"],
  [20, "trace", "trie/sync/writer:TriefactFile", "trie/sync/writer:Section"],
  [22, "read", "trie/sync/writer:TriefactFile"],
  // new discovery
  [26, "grep", "trie/sync/attention_fold:fold_historical_mass"],
  [28, "read", "trie/sync/attention_fold:fold_historical_mass"],
]

const FRAMES = [0, 3, 8, 13, 19, 23, 28, 45, 120]

console.log(
  `Loaded REAL graph: ${ctx.roleByQname.size} symbols, ${[...ctx.edgesByQname.values()].reduce((s, a) => s + a.length, 0)} edges, ${ctx.roles.length} roles`,
)

let i = 0
for (const frame of FRAMES) {
  while (i < SCRIPT.length && SCRIPT[i][0] <= frame) {
    const [t, type, q, traceTo] = SCRIPT[i]
    ctx.model.ingest(q, type as AttentionEventType, t)
    if (type === "trace" && traceTo) {
      ctx.model.ingest(traceTo, "trace", t)
      ctx.graph.reinforce(q, traceTo, t)
    }
    i++
  }
  renderFrame(ctx, frame, { label: "[sync investigation]", showRepoEdges: true })
}
