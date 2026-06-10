// The AGM live attention model — the in-memory cognitive-state field.
//
// Holds per-symbol live mass as a set of decaying event contributions, plus the
// historical-mass seed loaded from the graph. Derives role rollups and the
// attention centroid. Pure data + math: no React, no canvas. The store ticks it
// (ingest events, recompute at a frame cadence); the renderer reads snapshots.
//
// Design invariants (from the AGM spec):
//   - Live mass = Σ weight·exp(-λ_type·dt). Continuous wall-clock decay, no ticks.
//   - Mass is never dampened (truthful observation).
//   - Historical mass is a faint boundary-condition seed, not a competitor.
//   - display = log(raw+1); raw is unbounded, rendered is bounded.

import type { AttentionEventType } from "@/api/types"
import {
  COLD_FLOOR,
  HISTORICAL_SEED_FACTOR,
  type LiveContribution,
  displayMass,
  foldLiveMass,
  makeContribution,
  liveLambda,
} from "./weights"

export interface NodeMass {
  live: number // raw live mass at the last recompute
  historical: number // seeded historical mass (decayed at load; static thereafter in-session)
  display: number // log(live + seed·historical + 1)
  kind: AttentionEventType | "historical" // dominant intent → drives render style
  pinned?: boolean // edited/patched this session → never leaves view, always named
}

export interface RoleMass {
  role: string
  live: number
  display: number
}

export interface Centroid {
  // mass-weighted role-importance centroid expressed as the dominant roles.
  // The canvas uses fixed role geography, so the centroid is reported as the
  // ranked active roles rather than an x/y (which would imply a moving camera).
  topRoles: RoleMass[]
}

interface NodeState {
  contributions: LiveContribution[]
  historical: number
}

export class AttentionModel {
  // qname -> live contributions + historical seed
  private nodes = new Map<string, NodeState>()
  // qname -> role, supplied by the system model so rollups are possible
  private roleOf = new Map<string, string>()

  // Replace the qname→role map (called whenever the system model loads/refreshes).
  setRoles(roleByQname: Map<string, string>): void {
    this.roleOf = roleByQname
  }

  // Seed historical mass for a symbol (from the graph's historical_mass field).
  // Called at load; historical mass is a static in-session boundary condition.
  seedHistorical(qname: string, historicalMass: number): void {
    const s = this.ensure(qname)
    s.historical = Math.max(0, historicalMass)
  }

  // Clear all LIVE state (event contributions) while KEEPING historical-mass
  // seeds. Called when a new session starts: a new session is fresh working
  // memory, but the cross-session geography (historical mass) persists.
  clearLive(): void {
    this.pinned.clear()
    for (const [q, s] of this.nodes) {
      if (s.historical > 0) {
        s.contributions = []
      } else {
        this.nodes.delete(q) // no history → drop entirely
      }
    }
  }

  // Record one attention event: append a decaying contribution. `scale` lets a
  // caller attenuate the weight — used for grep *result hits*, which are faint
  // "maybe relevant" candidates (a wide low net), not committed attention like
  // the grep query itself or a read/trace.
  ingest(qname: string, type: AttentionEventType, ts: number, scale = 1): void {
    const c = makeContribution(type, ts)
    this.ensure(qname).contributions.push(scale === 1 ? c : { ...c, weight: c.weight * scale })
  }

  // Symbols the agent EDITED / PATCHED this session. They never leave view: their
  // live mass is locked at the current maximum (so they always render and rank
  // top), while their RADIUS can still grow as nothing keeps them artificially
  // hottest — they drift outward only relative to even-hotter live activity.
  private pinned = new Set<string>()

  pin(qname: string): void {
    this.ensure(qname)
    this.pinned.add(qname)
  }

  isPinned(qname: string): boolean {
    return this.pinned.has(qname)
  }

  pinnedSet(): Set<string> {
    return this.pinned
  }

  // Apply negative evidence: an explicit "ruled out" subtracts live mass by
  // injecting a one-shot negative contribution that decays like any other.
  // (Explicit only — never inferred. The caller gates this on an agent signal.)
  applyNegativeEvidence(qname: string, magnitude: number, ts: number): void {
    const s = this.ensure(qname)
    s.contributions.push({ ts, weight: -Math.abs(magnitude), lambda: 0 })
  }

  // Transfer a symbol's full state to a new qname (rename: identity follows).
  rename(from: string, to: string): void {
    const s = this.nodes.get(from)
    if (!s) return
    this.nodes.set(to, s)
    this.nodes.delete(from)
  }

  // Drop a symbol's live state (delete: live mass disappears immediately).
  remove(qname: string): void {
    this.nodes.delete(qname)
  }

  // Create-inherits: a new symbol starts at 0.5× the creator's current live mass
  // (so freshly written code isn't invisible). The inherited mass DECAYS like a
  // write event — otherwise a created symbol would sit at the centre forever and
  // never drift outward as attention moves on.
  inheritFrom(creator: string, created: string, now: number, factor = 0.5): void {
    const live = this.liveMass(creator, now)
    if (live <= 0) return
    this.ensure(created).contributions.push({
      ts: now,
      weight: live * factor,
      lambda: liveLambda("write"),
    })
  }

  // Current raw live mass for one symbol at `now`.
  liveMass(qname: string, now: number): number {
    const s = this.nodes.get(qname)
    if (!s) return 0
    return Math.max(0, foldLiveMass(s.contributions, now))
  }

  // Combined display mass: log(live + seed·historical + 1).
  massFor(qname: string, now: number): NodeMass {
    const s = this.nodes.get(qname)
    const historical = s?.historical ?? 0
    const live = s ? Math.max(0, foldLiveMass(s.contributions, now)) : 0
    const raw = live + HISTORICAL_SEED_FACTOR * historical
    const pinned = this.pinned.has(qname)
    return {
      live,
      historical,
      display: displayMass(raw),
      kind: pinned ? "write" : s ? this.dominantKind(s, now) : "historical",
      pinned,
    }
  }

  // Snapshot of every symbol with non-trivial mass at `now`. PINNED symbols
  // (edited/patched) are always included even if cold, flagged so the budget
  // never folds them and the renderer always names them — their real (decaying)
  // display still drives their radius, so they drift outward but never vanish.
  snapshot(now: number): Map<string, NodeMass> {
    const out = new Map<string, NodeMass>()
    for (const [qname, s] of this.nodes) {
      const live = Math.max(0, foldLiveMass(s.contributions, now))
      const raw = live + HISTORICAL_SEED_FACTOR * s.historical
      const pinned = this.pinned.has(qname)
      if (raw <= COLD_FLOOR && !pinned) continue
      out.set(qname, {
        live,
        historical: s.historical,
        display: displayMass(raw),
        kind: pinned ? "write" : this.dominantKind(s, now),
        pinned,
      })
    }
    return out
  }

  // The event type contributing the most CURRENT (decayed) mass to a node —
  // i.e. how it's predominantly being attended to right now. Drives the render
  // style: grep → dot, read/patch(write) → pill, trace → constellation node.
  private dominantKind(s: NodeState, now: number): AttentionEventType | "historical" {
    const byType = new Map<AttentionEventType, number>()
    for (const c of s.contributions) {
      if (!c.type || c.weight <= 0) continue
      const v = c.weight * Math.exp(-c.lambda * Math.max(0, now - c.ts))
      byType.set(c.type, (byType.get(c.type) ?? 0) + v)
    }
    let best: AttentionEventType | "historical" = "historical"
    let bestV = 0
    for (const [t, v] of byType) {
      if (v > bestV) {
        bestV = v
        best = t
      }
    }
    return best
  }

  // Role rollups: sum live mass of member symbols per role. Derived, not stored.
  roleMass(now: number): Map<string, RoleMass> {
    const acc = new Map<string, number>()
    for (const [qname, s] of this.nodes) {
      const live = Math.max(0, foldLiveMass(s.contributions, now))
      if (live <= 0) continue
      const role = this.roleOf.get(qname) || "untagged"
      acc.set(role, (acc.get(role) ?? 0) + live)
    }
    const out = new Map<string, RoleMass>()
    for (const [role, live] of acc) {
      out.set(role, { role, live, display: displayMass(live) })
    }
    return out
  }

  // The attention "center": the top-N active roles by live mass. Reported as a
  // ranking (not an x/y) because role geography is fixed and the camera is
  // user-controlled — we never force a single winning subsystem.
  centroid(now: number, topN = 5): Centroid {
    const roles = [...this.roleMass(now).values()].sort((a, b) => b.live - a.live)
    return { topRoles: roles.slice(0, topN) }
  }

  // Drop fully-decayed contributions to keep memory bounded. Call periodically.
  // A contribution is prunable when its decayed magnitude is below COLD_FLOOR.
  // Negative (lambda=0) and inherited one-shots never decay, so we fold them
  // into a single residual contribution rather than letting them accumulate.
  prune(now: number): void {
    for (const [qname, s] of this.nodes) {
      let residual = 0
      const kept: LiveContribution[] = []
      for (const c of s.contributions) {
        if (c.lambda === 0) {
          residual += c.weight
          continue
        }
        const mag = c.weight * Math.exp(-c.lambda * Math.max(0, now - c.ts))
        if (Math.abs(mag) > COLD_FLOOR) kept.push(c)
      }
      if (residual !== 0) kept.push({ ts: now, weight: residual, lambda: 0 })
      if (kept.length === 0 && s.historical <= 0 && !this.pinned.has(qname)) {
        this.nodes.delete(qname)
      } else {
        s.contributions = kept
      }
    }
  }

  private ensure(qname: string): NodeState {
    let s = this.nodes.get(qname)
    if (!s) {
      s = { contributions: [], historical: 0 }
      this.nodes.set(qname, s)
    }
    return s
  }
}
