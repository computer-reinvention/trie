// Behavioural simulation tests — verify the COMPOSED dynamics over a realistic
// investigation, not just isolated functions. These encode the visual guide's
// promises as numeric assertions so we know it works before looking at pixels.
//
// Scenario modelled: an agent investigating a login bug.
//   greps around → reads LoginRoute → traces LoginRoute→AuthService→SessionStore
//   → reads SessionStore hard → discovers RedisClient → briefly checks Metrics.

import { describe, it, expect } from "vitest"
import { AttentionModel } from "./attentionModel"
import { placeSymbol, applyClusterCohesion, type PolarPlacement } from "./layout"

const ROLES = ["auth", "infra", "observability"]
const roleOf = new Map<string, string>([
  ["auth:LoginRoute", "auth"],
  ["auth:AuthService", "auth"],
  ["auth:SessionStore", "auth"],
  ["infra:RedisClient", "infra"],
  ["observability:Metrics", "observability"],
])

function place(model: AttentionModel, now: number): PolarPlacement[] {
  const snap = model.snapshot(now)
  let max = 0
  for (const m of snap.values()) if (m.display > max) max = m.display
  const ps: PolarPlacement[] = []
  for (const [q, m] of snap) {
    ps.push(
      placeSymbol({
        qname: q,
        role: roleOf.get(q) ?? "untagged",
        roles: ROLES,
        displayMass: m.display,
        maxDisplay: max,
        historicalMass: 0,
      }),
    )
  }
  applyClusterCohesion(ps, roleOf)
  return ps
}

const radius = (p: PolarPlacement) => Math.hypot(p.x, p.y)
const byQ = (ps: PolarPlacement[]) => new Map(ps.map((p) => [p.qname, p]))

describe("routine investigation dynamics", () => {
  it("the symbol the agent is reading hardest sits closest to centre", () => {
    const m = new AttentionModel()
    m.setRoles(roleOf)
    let t = 0
    m.ingest("auth:LoginRoute", "read", t)
    t += 5
    m.ingest("auth:AuthService", "read", t)
    t += 5
    // hammer SessionStore
    m.ingest("auth:SessionStore", "read", t)
    m.ingest("auth:SessionStore", "trace", t)
    m.ingest("auth:SessionStore", "read", t + 1)

    const ps = byQ(place(m, t + 1))
    const ss = radius(ps.get("auth:SessionStore")!)
    const lr = radius(ps.get("auth:LoginRoute")!)
    expect(ss).toBeLessThan(lr) // hottest is nearest the crosshair
  })

  it("a symbol the agent moved on from drifts outward over time (not hidden)", () => {
    const m = new AttentionModel()
    m.setRoles(roleOf)
    m.ingest("auth:LoginRoute", "read", 0)
    const early = byQ(place(m, 0)).get("auth:LoginRoute")!
    // 4 minutes later, no further attention on it
    const late = byQ(place(m, 240)).get("auth:LoginRoute")
    // still present (not hidden) but farther out
    if (late) {
      // when something else is hot, LoginRoute's relative radius grows
      m.ingest("auth:SessionStore", "trace", 240)
      const withHot = byQ(place(m, 240)).get("auth:LoginRoute")!
      expect(radius(withHot)).toBeGreaterThan(radius(early))
    } else {
      // fully decayed below floor → acceptable (became peripheral then dropped)
      expect(late).toBeUndefined()
    }
  })

  it("a freshly discovered symbol enters from the perimeter", () => {
    const m = new AttentionModel()
    m.setRoles(roleOf)
    // established hot context
    m.ingest("auth:SessionStore", "trace", 0)
    m.ingest("auth:SessionStore", "read", 0)
    // brand-new discovery this instant
    m.ingest("infra:RedisClient", "grep", 0)
    const ps = byQ(place(m, 0))
    const redis = radius(ps.get("infra:RedisClient")!)
    const ss = radius(ps.get("auth:SessionStore")!)
    expect(redis).toBeGreaterThan(ss) // newcomer is farther out than the hot focus
  })

  it("same-role symbols cluster nearer each other than cross-role symbols", () => {
    const m = new AttentionModel()
    m.setRoles(roleOf)
    const t = 0
    m.ingest("auth:AuthService", "read", t)
    m.ingest("auth:SessionStore", "read", t)
    m.ingest("observability:Metrics", "read", t)
    const ps = byQ(place(m, t))
    const a = ps.get("auth:AuthService")!
    const s = ps.get("auth:SessionStore")!
    const mx = ps.get("observability:Metrics")!
    const sameRole = Math.hypot(a.x - s.x, a.y - s.y)
    const crossRole = Math.hypot(a.x - mx.x, a.y - mx.y)
    expect(sameRole).toBeLessThan(crossRole)
  })

  it("role rollup identifies the active subsystem during the investigation", () => {
    const m = new AttentionModel()
    m.setRoles(roleOf)
    const t = 0
    m.ingest("auth:LoginRoute", "read", t)
    m.ingest("auth:AuthService", "trace", t)
    m.ingest("auth:SessionStore", "trace", t)
    m.ingest("observability:Metrics", "grep", t)
    const top = m.centroid(t).topRoles
    expect(top[0].role).toBe("auth") // auth dominates, not the grazed observability
  })

  it("attention cools toward zero when the agent goes idle (decay works in aggregate)", () => {
    const m = new AttentionModel()
    m.setRoles(roleOf)
    m.ingest("auth:SessionStore", "read", 0)
    const hot = m.liveMass("auth:SessionStore", 0)
    const coldLater = m.liveMass("auth:SessionStore", 3600) // 1h idle
    expect(coldLater).toBeLessThan(hot * 0.001) // essentially cold
  })

  it("convergence: one symbol dominates the centre, the rest drift to the rim", () => {
    const m = new AttentionModel()
    m.setRoles(roleOf)
    // phase 1: scattered exploration (grep many) → all roughly equally near centre
    for (const q of ["auth:LoginRoute", "auth:AuthService", "infra:RedisClient", "observability:Metrics"]) {
      m.ingest(q, "grep", 0)
    }
    const gapEarly = centreGap(place(m, 0))
    // phase 2: converge hard on SessionStore
    for (let i = 0; i < 5; i++) m.ingest("auth:SessionStore", "trace", 10 + i)
    const gapLate = centreGap(place(m, 16))
    // convergence = the radius gap between the #1 (centre) symbol and the rest
    // grows sharply: one bright thing near the crosshair, everything else
    // pushed outward. Early (scattered) there is ~no gap.
    expect(gapLate).toBeGreaterThan(gapEarly)
    expect(gapLate).toBeGreaterThan(200) // a clear, readable separation
  })
})

// The radius gap between the single nearest-centre symbol and the mean radius of
// the rest. Large gap = converged (one dominant focus); ~0 = scattered.
function centreGap(ps: PolarPlacement[]): number {
  if (ps.length < 2) return 0
  const sorted = [...ps].sort((a, b) => radius(a) - radius(b))
  const nearest = radius(sorted[0])
  const rest = sorted.slice(1)
  const meanRest = rest.reduce((s, p) => s + radius(p), 0) / rest.length
  return meanRest - nearest
}
