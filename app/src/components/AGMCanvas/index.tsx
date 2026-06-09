// AGMCanvas — cognitive-state projection (NOT a graph view).
//
// The canvas centre is a FIXED crosshair: the "current attention origin". The
// world deforms around it; the camera never pans or follows. Each touched symbol
// is placed in polar coordinates:
//   radius = f(live mass)   — near centre = hot now, drifts outward as it cools
//   angle  = f(historical mass + role) — stable geography (learnable bearings)
//
// Nothing disappears mid-investigation: a cooled symbol becomes peripheral, not
// hidden. New discoveries enter from the perimeter and move inward. Repository
// edges are faint springs (tension/structure); attention edges are bright,
// temporary reasoning paths. Roles are influence (anchor labels), not boxes.
//
// All placement math lives in agm/layout.ts and is unit-tested; this file only
// eases drawn positions toward those targets and paints.

import { useEffect, useMemo, useRef } from "react"
import { useAGMStore } from "@/store/agmStore"
import { placeSymbol, ease, roleBaseAngle, R_MAX } from "@/agm/layout"
import { displayMass } from "@/agm/weights"
import {
  roleColor,
  nodeOpacity,
  nodeRadius,
  glowAlpha,
  tierFor,
  ROLE_LABEL_COLOR,
  ATTENTION_EDGE_COLOR,
  REPO_EDGE_COLOR,
} from "@/agm/style"

interface AGMCanvasProps {
  className?: string
}

// A drawn node: eased screen position + the live target it's chasing.
interface Drawn {
  qname: string
  role: string
  x: number
  y: number
  mass: number // display mass this frame
}

export function AGMCanvas({ className }: AGMCanvasProps) {
  const canvasRef = useRef<HTMLCanvasElement | null>(null)
  // user zoom only (no pan / no follow — the centre is fixed at (0,0)).
  const zoomRef = useRef(1)
  const drawnRef = useRef<Map<string, Drawn>>(new Map())
  const rafRef = useRef<number | null>(null)

  const systemModel = useAGMStore((s) => s.systemModel)
  const hasAttention = useAGMStore((s) => s.massByQname.size > 0)

  useEffect(() => {
    if (!systemModel) return
    kick()
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [systemModel])

  const kick = () => {
    if (rafRef.current == null) loop()
  }

  // Re-kick whenever the attention snapshot changes (ingest happened).
  useEffect(() => {
    const unsub = useAGMStore.subscribe((s, prev) => {
      if (s.lastRecompute !== prev.lastRecompute) kick()
    })
    return unsub
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  const loop = () => {
    const canvas = canvasRef.current
    if (!canvas) {
      rafRef.current = null
      return
    }
    const store = useAGMStore.getState()
    const now = Date.now() / 1000
    store.recompute(now)

    const mass = store.massByQname
    const prop = store.propagated
    const roleByQ = store.roleByQname
    const histByQ = store.historicalByQname
    const roles = store.roles
    const drawn = drawnRef.current

    // The active set: any qname with direct or propagated attention. Once a
    // symbol has been touched it stays in `drawn` until it fully cools AND
    // reaches the perimeter — nothing vanishes mid-investigation.
    const active = new Set<string>(mass.keys())
    for (const [q, v] of prop) if (v > 0) active.add(q)

    let maxDisplay = 0
    for (const q of active) {
      const m = mass.get(q)
      const propAdd = prop.get(q) ?? 0
      const d = m ? m.display : propAdd > 0 ? displayMass(propAdd) : 0
      if (d > maxDisplay) maxDisplay = d
    }

    // Update/insert targets for active symbols; ease drawn positions toward them.
    let motion = 0
    for (const q of active) {
      const m = mass.get(q)
      const propAdd = prop.get(q) ?? 0
      const d = m ? m.display : propAdd > 0 ? displayMass(propAdd) : 0
      const role = roleByQ.get(q) || "untagged"
      const target = placeSymbol({
        qname: q,
        role,
        roles,
        displayMass: d,
        maxDisplay,
        historicalMass: histByQ.get(q) ?? 0,
      })
      let node = drawn.get(q)
      if (!node) {
        // enter from the perimeter at the symbol's stable bearing
        node = { qname: q, role, x: Math.cos(target.angle) * R_MAX, y: Math.sin(target.angle) * R_MAX, mass: d }
        drawn.set(q, node)
      }
      node.mass = d
      const next = ease({ x: node.x, y: node.y }, target)
      node.x = next.x
      node.y = next.y
      motion += next.dist
    }

    // Symbols no longer active: let them drift to the perimeter, then drop once
    // they've arrived (so the canvas doesn't accumulate forever across
    // investigations, but nothing vanishes abruptly mid-investigation).
    for (const [q, node] of drawn) {
      if (active.has(q)) continue
      node.mass = 0
      const target = {
        x: (node.x / (Math.hypot(node.x, node.y) || 1)) * R_MAX,
        y: (node.y / (Math.hypot(node.x, node.y) || 1)) * R_MAX,
      }
      const next = ease({ x: node.x, y: node.y }, target, 0.08)
      node.x = next.x
      node.y = next.y
      motion += next.dist
      if (next.dist < 0.5) drawn.delete(q)
    }

    draw(maxDisplay)

    if (motion < 0.5 && maxDisplay <= 0 && drawn.size === 0) {
      rafRef.current = null
      return
    }
    rafRef.current = requestAnimationFrame(loop)
  }

  const draw = (maxDisplay: number) => {
    const canvas = canvasRef.current
    if (!canvas) return
    const ctx = canvas.getContext("2d")
    if (!ctx) return
    const dpr = window.devicePixelRatio || 1
    const w = canvas.clientWidth
    const h = canvas.clientHeight
    if (canvas.width !== w * dpr || canvas.height !== h * dpr) {
      canvas.width = w * dpr
      canvas.height = h * dpr
    }
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0)
    ctx.clearRect(0, 0, w, h)

    // Fixed coordinate system: centre of the canvas is (0,0). Only zoom scales.
    const k = zoomRef.current
    ctx.save()
    ctx.translate(w / 2, h / 2)
    ctx.scale(k, k)

    const store = useAGMStore.getState()
    const drawn = drawnRef.current
    const roles = store.roles
    const edgesByQ = store.edgesByQname

    // --- the crosshair: current attention origin (always present) ---
    drawCrosshair(ctx)

    // --- role anchor labels: influence, not containment (no boxes) ---
    // Only show a role's label once it has a visible symbol this frame.
    const visibleRoles = new Set<string>()
    for (const n of drawn.values()) if (n.mass > 0) visibleRoles.add(n.role)
    for (const role of visibleRoles) {
      const angle = roleBaseAngle(role, roles)
      const lx = Math.cos(angle) * (R_MAX + 26)
      const ly = Math.sin(angle) * (R_MAX + 26)
      ctx.fillStyle = ROLE_LABEL_COLOR
      ctx.globalAlpha = 0.55
      ctx.font = "12px ui-sans-serif, system-ui"
      ctx.textAlign = "center"
      ctx.fillText(role, lx, ly)
      ctx.globalAlpha = 1
    }

    // --- repository edges as faint springs between visible nodes ---
    ctx.lineWidth = 1
    for (const [from, node] of drawn) {
      const outs = edgesByQ.get(from)
      if (!outs) continue
      for (const e of outs) {
        const to = drawn.get(e.to)
        if (!to) continue
        ctx.beginPath()
        ctx.moveTo(node.x, node.y)
        ctx.lineTo(to.x, to.y)
        ctx.strokeStyle = REPO_EDGE_COLOR
        ctx.globalAlpha = 0.35
        ctx.stroke()
        ctx.globalAlpha = 1
      }
    }

    // --- attention edges: bright, temporary reasoning paths ---
    const now = store.lastRecompute || Date.now() / 1000
    for (const ae of store.graph.liveEdges(now)) {
      const a = drawn.get(ae.from)
      const b = drawn.get(ae.to)
      if (!a || !b) continue
      ctx.beginPath()
      ctx.moveTo(a.x, a.y)
      ctx.lineTo(b.x, b.y)
      ctx.strokeStyle = ATTENTION_EDGE_COLOR
      ctx.globalAlpha = Math.min(0.85, 0.4 + ae.heat * 0.15)
      ctx.lineWidth = 1.75
      ctx.stroke()
      ctx.globalAlpha = 1
      ctx.lineWidth = 1
    }

    // --- symbols: radius already encodes relevance; size/opacity reinforce it ---
    for (const node of drawn.values()) {
      const m = node.mass
      const color = roleColor(node.role)
      // peripheral (cooled) symbols stay visible but dim — never hidden.
      const rel = maxDisplay > 0 ? m / maxDisplay : 0
      const radius = m > 0 ? nodeRadius(m, maxDisplay) : 3
      const opacity = m > 0 ? nodeOpacity(m, maxDisplay) : 0.18

      const glow = m > 0 ? glowAlpha(m, maxDisplay) : 0
      if (glow > 0) {
        ctx.beginPath()
        ctx.arc(node.x, node.y, radius * 2.4, 0, Math.PI * 2)
        ctx.fillStyle = color
        ctx.globalAlpha = glow
        ctx.fill()
        ctx.globalAlpha = 1
      }

      ctx.beginPath()
      ctx.arc(node.x, node.y, radius, 0, Math.PI * 2)
      ctx.fillStyle = color
      ctx.globalAlpha = opacity
      ctx.fill()
      ctx.globalAlpha = 1

      // label the dominant (hottest) symbols only — keeps the map calm.
      if (m > 0 && tierFor(m, maxDisplay) === "dominant") {
        const label = node.qname.split(":").pop() ?? node.qname
        ctx.fillStyle = "#e2e8f0"
        ctx.globalAlpha = 0.5 + 0.5 * rel
        ctx.font = "11px ui-sans-serif, system-ui"
        ctx.textAlign = "center"
        ctx.fillText(label, node.x, node.y - radius - 4)
        ctx.globalAlpha = 1
      }
    }

    ctx.restore()
  }

  // --- zoom only (centre stays fixed; no pan, no camera follow) ---
  useEffect(() => {
    const canvas = canvasRef.current
    if (!canvas) return
    const onWheel = (e: WheelEvent) => {
      e.preventDefault()
      const factor = Math.exp(-e.deltaY * 0.001)
      zoomRef.current = Math.min(4, Math.max(0.25, zoomRef.current * factor))
      kick()
    }
    canvas.addEventListener("wheel", onWheel, { passive: false })
    return () => canvas.removeEventListener("wheel", onWheel)
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  useEffect(() => {
    kick()
    return () => {
      if (rafRef.current != null) cancelAnimationFrame(rafRef.current)
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  const showIdleHint = useMemo(() => !hasAttention, [hasAttention])

  return (
    <div className={className} style={{ position: "relative" }}>
      <canvas ref={canvasRef} style={{ width: "100%", height: "100%", display: "block" }} />
      {showIdleHint && (
        <div
          style={{
            position: "absolute",
            inset: 0,
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            color: "#3f4a5a",
            fontSize: 13,
            pointerEvents: "none",
          }}
        >
          No attention yet — the map fills in as the agent works.
        </div>
      )}
    </div>
  )
}

// The fixed centre crosshair — the current attention origin. Nothing else ever
// occupies the exact centre; this is the coordinate system's (0,0).
function drawCrosshair(ctx: CanvasRenderingContext2D) {
  const s = 7
  ctx.strokeStyle = "#475569"
  ctx.globalAlpha = 0.8
  ctx.lineWidth = 1
  ctx.beginPath()
  ctx.moveTo(-s, 0)
  ctx.lineTo(s, 0)
  ctx.moveTo(0, -s)
  ctx.lineTo(0, s)
  ctx.stroke()
  ctx.globalAlpha = 1
}
