// The animation heart: per-node spring interpolation so nothing ever snaps.
//
// State sets TARGETS; the animator eases CURRENT toward them every frame; paint
// draws CURRENT. A node becoming active doesn't jump to blue — it warms into it
// with a slight overshoot, like a physical object. Grounded timings (research
// B4): perceivable but not sluggish; springs settle in a few hundred ms.

export interface AnimChannel {
  current: number
  target: number
  velocity: number
}

function channel(v = 0): AnimChannel {
  return { current: v, target: v, velocity: v }
}

// Critically-damped-ish spring step. `stiffness`/`damping` tuned so a step from
// 0->1 settles in ~300ms at 60fps with a tiny overshoot.
function springStep(c: AnimChannel, dt: number, stiffness: number, damping: number): void {
  const force = (c.target - c.current) * stiffness
  c.velocity = (c.velocity + force * dt) * Math.pow(damping, dt * 60)
  c.current += c.velocity * dt
  // snap when settled to avoid endless tiny work
  if (Math.abs(c.target - c.current) < 0.001 && Math.abs(c.velocity) < 0.001) {
    c.current = c.target
    c.velocity = 0
  }
}

export interface NodeAnim {
  // 0..1 "appeared" — drives the first-load reveal (scale + fade in)
  reveal: AnimChannel
  // 0..1 pulse intensity (agent reading/writing) — spring so it breathes
  pulse: AnimChannel
  // 0..1 size emphasis (hover/selection grow)
  emphasis: AnimChannel
}

export class GraphAnimator {
  private nodes = new Map<string, NodeAnim>()
  private lastT = 0

  ensure(id: string, born = false): NodeAnim {
    let a = this.nodes.get(id)
    if (!a) {
      a = {
        reveal: channel(born ? 0 : 1),
        pulse: channel(0),
        emphasis: channel(0),
      }
      if (born) a.reveal.target = 1
      this.nodes.set(id, a)
    }
    return a
  }

  get(id: string): NodeAnim | undefined {
    return this.nodes.get(id)
  }

  // Drop anims for ids no longer present (prevents unbounded growth on re-layouts).
  prune(presentIds: Set<string>): void {
    for (const id of this.nodes.keys()) {
      if (!presentIds.has(id)) this.nodes.delete(id)
    }
  }

  setTargets(id: string, t: { pulse?: number; emphasis?: number; reveal?: number }): void {
    const a = this.ensure(id)
    if (t.pulse !== undefined) a.pulse.target = t.pulse
    if (t.emphasis !== undefined) a.emphasis.target = t.emphasis
    if (t.reveal !== undefined) a.reveal.target = t.reveal
  }

  // Advance all springs. Returns true if anything is still in motion (so the
  // canvas knows to keep redrawing).
  tick(now: number): boolean {
    const dt = this.lastT ? Math.min(0.05, (now - this.lastT) / 1000) : 0.016
    this.lastT = now
    let moving = false
    for (const a of this.nodes.values()) {
      springStep(a.reveal, dt, 80, 0.75)
      springStep(a.pulse, dt, 120, 0.6) // snappier — pulses are events
      springStep(a.emphasis, dt, 140, 0.7)
      if (
        a.reveal.current !== a.reveal.target ||
        a.pulse.current !== a.pulse.target ||
        a.emphasis.current !== a.emphasis.target ||
        Math.abs(a.pulse.velocity) > 0.001
      ) {
        moving = true
      }
    }
    return moving
  }
}

// easeOutBack-style overshoot for one-shot transitions where a spring is overkill.
export function easeOutBack(t: number): number {
  const c1 = 1.70158
  const c3 = c1 + 1
  return 1 + c3 * Math.pow(t - 1, 3) + c1 * Math.pow(t - 1, 2)
}
