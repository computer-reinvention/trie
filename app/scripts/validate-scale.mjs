#!/usr/bin/env node
// Anti-overwhelm validation at scale: generate a synthetic 20k-node power-law
// graph (like a large monorepo) and assert the DOI budget machinery holds and
// stays fast. Run: node scripts/validate-scale.mjs
import { build } from "esbuild"
import { resolve, dirname } from "path"
import { fileURLToPath } from "url"

const __dirname = dirname(fileURLToPath(import.meta.url))
const srcDir = resolve(__dirname, "..", "src")

const out = await build({
  stdin: {
    contents: `
      export { regimeFor } from "@/graph/regime"
      export { buildAdjacency, selectVisible } from "@/graph/doi"
    `,
    resolveDir: srcDir,
    loader: "ts",
  },
  bundle: true,
  format: "esm",
  write: false,
  plugins: [
    {
      name: "alias",
      setup(b) {
        b.onResolve({ filter: /^@\// }, (a) => ({ path: resolve(srcDir, a.path.slice(2) + ".ts") }))
      },
    },
  ],
})
const mod = await import(
  "data:text/javascript;base64," + Buffer.from(out.outputFiles[0].text).toString("base64")
)

// --- synthetic power-law graph: 20k nodes, preferential-attachment edges ---
const N = 20000
const ROLES = ["api", "domain", "persistence", "io", "parsing", "model", "config", "util", "orchestration", "entrypoint"]
const SUBS = Array.from({ length: 40 }, (_, i) => `pkg/mod${i}`)
const nodes = []
const degree = new Array(N).fill(0)
for (let i = 0; i < N; i++) {
  nodes.push({
    qname: `n${i}`,
    name: `n${i}`,
    kind: "function",
    file_path: `${SUBS[i % SUBS.length]}/f${i % 200}.py`,
    role: ROLES[i % ROLES.length],
    boundary: "internal",
    subsystem: SUBS[i % SUBS.length],
    is_public: i % 3 === 0,
    is_test: false,
    inbound_count: 0,
    outbound_count: 0,
    prod_inbound_count: 0,
    cls: "normal",
    salience: 0, // set below
    betweenness: 0,
    depth: 1,
    community: i % 50,
    one_liner: "",
    x: 0,
    y: 0,
  })
}
// preferential attachment -> power-law degree
const edges = []
const targets = [0]
for (let i = 1; i < N; i++) {
  const k = 1 + (i % 3) // 1-3 out edges
  for (let j = 0; j < k; j++) {
    const t = targets[Math.floor(Math.random() * targets.length)]
    if (t !== i) {
      edges.push({ from: `n${i}`, to: `n${t}` })
      degree[i]++
      degree[t]++
      targets.push(t) // popular nodes get more popular
    }
  }
  targets.push(i)
}
// salience from degree (saturating), a few hubs near 1
const maxDeg = Math.max(...degree)
for (let i = 0; i < N; i++) {
  nodes[i].salience = Math.min(1, degree[i] / (maxDeg * 0.3))
  nodes[i].inbound_count = degree[i]
}

const model = {
  nodes,
  axes: { role: { axis: "role", groups: [], flows: [] }, subsystem: { axis: "subsystem", groups: [], flows: [] } },
  landmarks: [],
  stats: { production_nodes: N, test_nodes: 0, edges: edges.length, class_counts: {}, role_count: ROLES.length, subsystem_count: SUBS.length },
}

let pass = 0, fail = 0
const ok = (c, m) => { if (c) { pass++; console.log("  ✓", m) } else { fail++; console.log("  ✗ FAIL:", m) } }

console.log(`=== synthetic graph: ${N} nodes, ${edges.length} edges ===`)
const regime = mod.regimeFor(N)
console.log("  regime:", JSON.stringify(regime))
ok(regime.regime === "huge", "20k nodes -> huge regime")
ok(regime.defaultAxis === "subsystem", "huge defaults to subsystem axis")

let t = Date.now()
const adj = mod.buildAdjacency(edges)
console.log(`  adjacency built in ${Date.now() - t}ms`)

console.log("=== whole-system DOI (no focus) ===")
t = Date.now()
const v0 = mod.selectVisible({ model, budget: regime.budget, salienceFloor: regime.salienceFloor, axis: "subsystem", focus: [], adjacency: adj })
const dt0 = Date.now() - t
console.log(`  selectVisible: ${dt0}ms, shown=${v0.nodes.length}, aggregates=${v0.aggregates.length}`)
ok(v0.nodes.length <= regime.budget, `shown (${v0.nodes.length}) <= budget (${regime.budget})`)
ok(dt0 < 500, `selectVisible under 500ms at 20k (${dt0}ms)`)
const folded0 = v0.aggregates.reduce((a, b) => a + b.count, 0)
ok(v0.nodes.length + folded0 === N, `nothing lost: ${v0.nodes.length}+${folded0}==${N}`)

console.log("=== focus on the biggest hub ===")
let hubIdx = 0
for (let i = 0; i < N; i++) if (degree[i] > degree[hubIdx]) hubIdx = i
console.log(`  hub n${hubIdx} has degree ${degree[hubIdx]}`)
t = Date.now()
const vh = mod.selectVisible({ model, budget: regime.budget, salienceFloor: regime.salienceFloor, axis: "subsystem", focus: [`n${hubIdx}`], adjacency: adj })
const dth = Date.now() - t
console.log(`  hub focus: ${dth}ms, shown=${vh.nodes.length}`)
ok(vh.nodes.length <= regime.budget, `hub focus shown (${vh.nodes.length}) <= budget`)
ok(dth < 500, `hub focus under 500ms (${dth}ms)`)
ok(vh.nodes.some((n) => n.qname === `n${hubIdx}`), "hub itself visible")

console.log(`\n${fail === 0 ? "ALL PASS" : "FAILURES"}: ${pass} passed, ${fail} failed`)
process.exit(fail === 0 ? 0 : 1)
