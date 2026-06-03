#!/usr/bin/env node
// Headless validation of the DOI / regime data spine against trie's real model.
// Bundles the TS modules with esbuild (resolving the @/ alias) and asserts the
// anti-overwhelm invariants on real data. Run: node scripts/validate-doi.mjs
import { build } from "esbuild"
import { readFileSync } from "fs"
import { resolve, dirname } from "path"
import { fileURLToPath } from "url"

const __dirname = dirname(fileURLToPath(import.meta.url))
const appDir = resolve(__dirname, "..")
const srcDir = resolve(appDir, "src")

const result = await build({
  stdin: {
    contents: `
      export { regimeForModel, regimeFor } from "@/graph/regime"
      export { buildAdjacency, selectVisible, componentView, hopDistances } from "@/graph/doi"
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
        b.onResolve({ filter: /^@\// }, (args) => ({
          path: resolve(srcDir, args.path.slice(2) + ".ts"),
        }))
      },
    },
  ],
})

const mod = await import(
  "data:text/javascript;base64," + Buffer.from(result.outputFiles[0].text).toString("base64")
)

const model = JSON.parse(readFileSync("/tmp/trie_model.json", "utf8"))
const edges = JSON.parse(readFileSync("/tmp/trie_edges.json", "utf8"))

let pass = 0
let fail = 0
const ok = (cond, msg) => {
  if (cond) { pass++; console.log("  ✓", msg) }
  else { fail++; console.log("  ✗ FAIL:", msg) }
}

console.log("=== regime ===")
const regime = mod.regimeForModel(model)
console.log("  regime:", JSON.stringify(regime))
ok(regime.regime === "medium", "trie (601 prod nodes) -> medium regime")
ok(regime.budget === 250, "budget 250")
ok(regime.defaultAxis === "role", "default axis role")

console.log("=== adjacency ===")
const adj = mod.buildAdjacency(edges)
ok(adj.neighbours.size > 0, "adjacency built")

console.log("=== component view (L0) ===")
const roleView = mod.componentView(model, "role")
const subView = mod.componentView(model, "subsystem")
console.log(`  role: ${roleView.groups.length} groups, ${roleView.flows.length} flows`)
console.log(`  subsystem: ${subView.groups.length} groups, ${subView.flows.length} flows`)
ok(roleView.groups.length >= 8 && roleView.groups.length <= 20, "L0 role groups in [8,20] (a dozen-ish)")
ok(roleView.flows.length <= 40, "L0 role flows <= 40 (readable, not hairball)")

console.log("=== DOI: whole-system (no focus) ===")
const v0 = mod.selectVisible({
  model, budget: regime.budget, salienceFloor: regime.salienceFloor,
  axis: "role", focus: [], adjacency: adj,
})
console.log(`  shown=${v0.nodes.length} aggregates=${v0.aggregates.length}`)
ok(v0.nodes.length <= regime.budget, `shown (${v0.nodes.length}) within budget (${regime.budget})`)
const totalFolded = v0.aggregates.reduce((a, b) => a + b.count, 0)
ok(v0.nodes.length + totalFolded === model.nodes.filter(n=>!n.is_test).length,
   "every production node is either shown or folded (nothing lost)")

console.log("=== DOI: focus on a HUB (Config) — must stay within budget ===")
const hub = "trie/config:Config"
const vHub = mod.selectVisible({
  model, budget: regime.budget, salienceFloor: regime.salienceFloor,
  axis: "role", focus: [hub], adjacency: adj,
})
console.log(`  Config focus -> shown=${vHub.nodes.length} (raw 2-hop nbhd is ~368)`)
ok(vHub.nodes.length <= regime.budget, `hub focus shown (${vHub.nodes.length}) <= budget — hub explosion folded`)
ok(vHub.nodes.some(n => n.qname === hub), "focused hub is in the visible set")

console.log("=== DOI: focus on a small node — neighborhood fits, little folding ===")
const small = "trie/graph/system_model:build_system_model"
const vSmall = mod.selectVisible({
  model, budget: regime.budget, salienceFloor: regime.salienceFloor,
  axis: "role", focus: [small], adjacency: adj,
})
ok(vSmall.nodes.some(n => n.qname === small), "focused small node visible")

console.log("=== hop distances ===")
const dist = mod.hopDistances(adj, [hub], 2)
ok(dist.get(hub) === 0, "focus node at distance 0")
ok([...dist.values()].every(d => d <= 2), "all distances <= maxHops")

console.log(`\n${fail === 0 ? "ALL PASS" : "FAILURES"}: ${pass} passed, ${fail} failed`)
process.exit(fail === 0 ? 0 : 1)
