// AGM tuning constants + pure decay/mass helpers.
//
// Re-exports the canonical contract values from api/types (mirrored from the
// Python source of truth, trie/attention.py) and adds the math the live model
// uses. Pure module: no React, no canvas, no store — unit-testable headless.
//
// Two masses, never conflated:
//   - live mass: per-event field, continuous wall-clock decay (per-event-type
//     half-lives), drives the visual. Computed by foldLiveMass below.
//   - historical mass: long-term recurrence-across-investigations signal, seeded
//     from the triefact at load time and seeding the live field faintly.
//
// Mass is never dampened: no role/test/util/hub coefficient. Correction for
// plumbing happens in propagation/visibility/layout, not here.

import {
  EVENT_WEIGHTS,
  LIVE_HALFLIFE_SECONDS,
  EDGE_WEIGHTS,
  PROPAGATION_FACTOR,
  PROPAGATION_HOPS,
  displayMass,
  edgeWeight,
  liveLambda,
  type AttentionEventType,
} from "@/api/types"

export {
  EVENT_WEIGHTS,
  LIVE_HALFLIFE_SECONDS,
  EDGE_WEIGHTS,
  PROPAGATION_FACTOR,
  PROPAGATION_HOPS,
  displayMass,
  edgeWeight,
  liveLambda,
}
export type { AttentionEventType }

// How strongly historical mass seeds the live field on load. Historical mass is
// a boundary condition (where attention has pooled across sessions), not a
// competitor to live attention — so it contributes only a faint baseline. Live
// events quickly dominate. Tunable against the 5s success criterion.
export const HISTORICAL_SEED_FACTOR = 0.15

// Live mass below this (after log compression) is treated as cold → the symbol
// is a candidate to disappear from the canvas (relative thresholds applied in
// the renderer; this is the absolute floor that lets a node fully settle to 0).
export const COLD_FLOOR = 1e-3

// One decaying contribution to a symbol's live mass: an event's weight at the
// time it landed, decayed continuously by its event-type half-life.
export interface LiveContribution {
  ts: number // unix seconds the event landed
  weight: number // EVENT_WEIGHTS[type]
  lambda: number // per-event-type decay rate (liveLambda(type))
}

export function makeContribution(type: AttentionEventType, ts: number): LiveContribution {
  return { ts, weight: EVENT_WEIGHTS[type], lambda: liveLambda(type) }
}

// Sum a set of decaying contributions to a single live-mass value at `now`.
// exp(-lambda * dt) per contribution — continuous, frame-rate independent.
export function foldLiveMass(contributions: Iterable<LiveContribution>, now: number): number {
  let total = 0
  for (const c of contributions) {
    const dt = Math.max(0, now - c.ts)
    total += c.weight * Math.exp(-c.lambda * dt)
  }
  return total
}

// Decay a single scalar value from `ts` to `now` at `lambda`.
export function decayScalar(value: number, lambda: number, ts: number, now: number): number {
  if (value <= 0) return 0
  const dt = Math.max(0, now - ts)
  return value * Math.exp(-lambda * dt)
}
