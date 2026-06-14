// Visual stress scenarios — render adversarial sequences through the ASCII
// mirror so we can eyeball them too (the assertions live in stress.test.ts).
//
// Run:  cd app && npx tsx scripts/sim/scenarios.ts

import { makeSyntheticContext, loadRealGraph, makeContext } from "./fixtures"
import { renderFrame } from "./render"

function header(title: string) {
  console.log(`\n\n${"#".repeat(90)}\n#  SCENARIO: ${title}\n${"#".repeat(90)}`)
}

// 1) Many concurrent symbols across many roles (dense field).
function scenarioDense() {
  header("dense field — 20 symbols across 6 roles, all warm")
  const roles: Record<string, string[]> = {}
  for (let r = 0; r < 6; r++) roles[`role${r}`] = []
  for (let i = 0; i < 20; i++) roles[`role${i % 6}`].push(`mod${i}:sym${i}`)
  const ctx = makeSyntheticContext({ roles })
  ctx.investigations.set({ id: "s", label: "dense field" })
  let t = 0
  for (let i = 0; i < 20; i++) {
    ctx.model.ingest(`mod${i}:sym${i}`, i % 3 === 0 ? "trace" : "read", t)
    t += 0.2
  }
  renderFrame(ctx, t, { label: "dense", showRepoEdges: false })
}

// 2) Rapid role switching then convergence.
function scenarioRoleSwitch() {
  header("rapid role switching → convergence on infra")
  const ctx = makeSyntheticContext({
    roles: { auth: ["a:1", "a:2"], infra: ["i:1", "i:2"], obs: ["o:1"] },
  })
  ctx.investigations.set({ id: "s", label: "role switching" })
  ctx.model.ingest("a:1", "grep", 0)
  ctx.model.ingest("o:1", "grep", 1)
  ctx.model.ingest("a:2", "read", 2)
  for (let i = 0; i < 8; i++) ctx.model.ingest("i:1", "trace", 10 + i)
  ctx.model.ingest("i:2", "read", 18)
  renderFrame(ctx, 19, { label: "converged on infra" })
}

// 3) Rename / delete / create mid-run.
function scenarioLifecycle() {
  header("lifecycle — rename, delete, create(0.5x) mid-run")
  const ctx = makeSyntheticContext({ roles: { core: ["c:Old", "c:Helper"] } })
  ctx.investigations.set({ id: "s", label: "lifecycle" })
  ctx.model.ingest("c:Old", "trace", 0)
  ctx.model.ingest("c:Helper", "read", 1)
  console.log("\n-- before --")
  renderFrame(ctx, 2, { label: "before" })
  // rename Old -> New, register role for New
  ctx.roleByQname.set("c:New", "core")
  ctx.model.setRoles(ctx.roleByQname)
  ctx.model.rename("c:Old", "c:New")
  // create a child from New at 0.5x
  ctx.roleByQname.set("c:Child", "core")
  ctx.model.setRoles(ctx.roleByQname)
  ctx.model.inheritFrom("c:New", "c:Child", 2)
  console.log("\n-- after rename + create --")
  renderFrame(ctx, 2, { label: "after rename+create" })
  // delete Helper
  ctx.model.remove("c:Helper")
  console.log("\n-- after delete Helper --")
  renderFrame(ctx, 3, { label: "after delete" })
}

// 4) Negative evidence pushes a ruled-out symbol outward.
function scenarioNegative() {
  header("negative evidence — rule out a hot symbol")
  const ctx = makeSyntheticContext({ roles: { auth: ["a:Suspect", "a:Real"] } })
  ctx.investigations.set({ id: "s", label: "rule-out" })
  ctx.model.ingest("a:Suspect", "trace", 0)
  ctx.model.ingest("a:Suspect", "read", 0)
  ctx.model.ingest("a:Real", "read", 0)
  console.log("\n-- Suspect is hot --")
  renderFrame(ctx, 0, { label: "suspect hot" })
  ctx.model.applyNegativeEvidence("a:Suspect", 100, 1)
  ctx.investigations.addNegativeEvidence("s", "a:Suspect")
  console.log("\n-- after ruling out Suspect --")
  renderFrame(ctx, 1, { label: "ruled out" })
}

// 5) Idle → everything cools to the rim.
function scenarioIdle() {
  header("idle decay — investigation goes quiet")
  const ctx = makeSyntheticContext({ roles: { core: ["c:A", "c:B", "c:C"] } })
  ctx.investigations.set({ id: "s", label: "idle" })
  ctx.model.ingest("c:A", "trace", 0)
  ctx.model.ingest("c:B", "read", 0)
  ctx.model.ingest("c:C", "grep", 0)
  renderFrame(ctx, 0, { label: "active" })
  renderFrame(ctx, 120, { label: "2 min idle" })
  renderFrame(ctx, 1200, { label: "20 min idle" })
}

// 6) Real-graph hub: hammer a high-fan-in symbol, check propagation stays sane.
function scenarioRealHub() {
  header("real graph — converge on a real hub (Store)")
  const ctx = makeContext(loadRealGraph())
  ctx.investigations.set({ id: "s", label: "real hub" })
  for (let i = 0; i < 6; i++) ctx.model.ingest("trie/graph/store:Store", "trace", i)
  renderFrame(ctx, 6, { label: "Store hammered", showRepoEdges: true })
}

scenarioDense()
scenarioRoleSwitch()
scenarioLifecycle()
scenarioNegative()
scenarioIdle()
scenarioRealHub()
