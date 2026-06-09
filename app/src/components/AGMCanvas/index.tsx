// AGMCanvas — the Attention Gravity Map renderer.
//
// A self-contained Canvas 2D view driven by the AGM engine (agmStore). The
// gravity simulation IS the layout; this component owns the rAF loop, runs
// gravity.step + model.recompute while the system is not at rest, and stops when
// it settles (motion only on attention change). Manual pan/zoom; user-controlled
// camera (the attention centroid never moves the view). Minimal aesthetic: heat
// reads through opacity/glow/size over fixed role geography.

import { useEffect, useMemo, useRef } from "react"
import { useAGMStore } from "@/store/agmStore"
import { computeTargets, easeToTargets, type Body } from "@/agm/gravity"
import {
  roleColor,
  tierFor,
  nodeOpacity,
  nodeRadius,
  glowAlpha,
  ROLE_LABEL_COLOR,
  ROLE_RING_COLOR,
  ATTENTION_EDGE_COLOR,
} from "@/agm/style"
import { displayMass } from "@/agm/weights"

interface AGMCanvasProps {
  className?: string
}

interface Camera {
  x: number
  y: number
  k: number
}

export function AGMCanvas({ className }: AGMCanvasProps) {
  const canvasRef = useRef<HTMLCanvasElement | null>(null)
  const cameraRef = useRef<Camera>({ x: 0, y: 0, k: 1 })
  const bodiesRef = useRef<Map<string, Body>>(new Map())
  const rafRef = useRef<number | null>(null)
  const restRef = useRef(false)

  const systemModel = useAGMStore((s) => s.systemModel)
  const roleWells = useAGMStore((s) => s.roleWells)
  const roleByQname = useAGMStore((s) => s.roleByQname)
  // Drives the idle hint: true until any symbol has accrued attention.
  const hasAttention = useAGMStore((s) => s.massByQname.size > 0)

  // Bodies are created LAZILY — only when a symbol first receives attention.
  // We never instantiate all 810 nodes (that scattered the canvas). The role map
  // tells us where each active symbol belongs. Topology load just wakes the loop.
  useEffect(() => {
    if (!systemModel) return
    kick()
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [systemModel, roleWells])

  // Wake the simulation (called on topology load + on every attention ingest via
  // the store subscription below).
  const kick = () => {
    restRef.current = false
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

    const bodies = bodiesRef.current
    const mass = store.massByQname
    const prop = store.propagated
    const roleByQ = store.roleByQname

    // The set of qnames that currently carry attention (direct or propagated).
    const active = new Set<string>(mass.keys())
    for (const [q, v] of prop) if (v > 0) active.add(q)

    // Lazily create a body the first time a qname becomes active; place it at its
    // role well so it emerges from the right geography.
    let maxDisplay = 0
    for (const q of active) {
      const m = mass.get(q)
      const propAdd = prop.get(q) ?? 0
      const d = m ? m.display : propAdd > 0 ? displayMass(propAdd) : 0
      if (d <= 0) continue
      let b = bodies.get(q)
      if (!b) {
        const role = roleByQ.get(q) || "untagged"
        const well = roleWells.get(role) ?? { x: 0, y: 0 }
        b = { qname: q, role, pos: { ...well }, target: { ...well }, mass: d }
        bodies.set(q, b)
      }
      b.mass = d
      if (d > maxDisplay) maxDisplay = d
    }
    // Decay-out: drop bodies that have gone cold so they don't linger.
    for (const [q, b] of bodies) {
      if (!active.has(q)) {
        bodies.delete(q)
        continue
      }
      b.mass = mass.get(q)?.display ?? (prop.get(q) ? displayMass(prop.get(q)!) : 0)
    }

    // Deterministic attention layout: arrange active symbols around their role
    // wells (hot = nearer centre), then ease toward targets (calm, no physics).
    const bodyList = [...bodies.values()]
    computeTargets(bodyList, roleWells, maxDisplay)
    const motion = easeToTargets(bodyList, roleWells)
    draw(maxDisplay)

    // Stop when nothing is animating and nothing is hot.
    if (motion < 0.5 && maxDisplay <= 0) {
      restRef.current = true
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

    const cam = cameraRef.current
    ctx.save()
    ctx.translate(w / 2 + cam.x, h / 2 + cam.y)
    ctx.scale(cam.k, cam.k)

    const bodies = bodiesRef.current
    const store = useAGMStore.getState()

    // Progressive emergence: a role well (ring + label) is drawn ONLY when the
    // role has at least one VISIBLE symbol this frame — i.e. the agent has
    // actually attended to something in it and that symbol is above the
    // visibility tier. Roles with only sub-threshold mass draw nothing, so there
    // are never empty labeled circles. Derive visible roles from the symbols we
    // are about to render, not from the raw role-mass sum.
    const visibleRoleHeat = new Map<string, number>()
    for (const b of bodies.values()) {
      if (b.mass <= 0) continue
      if (tierFor(b.mass, maxDisplay) === "hidden") continue
      visibleRoleHeat.set(b.role, Math.max(visibleRoleHeat.get(b.role) ?? 0, b.mass))
    }
    for (const [role, heat] of visibleRoleHeat) {
      const well = roleWells.get(role)
      if (!well) continue
      const intensity = maxDisplay > 0 ? Math.min(1, heat / maxDisplay) : 0
      ctx.beginPath()
      ctx.arc(well.x, well.y, 90, 0, Math.PI * 2)
      ctx.strokeStyle = ROLE_RING_COLOR
      ctx.globalAlpha = 0.25 + 0.4 * intensity
      ctx.lineWidth = 1
      ctx.stroke()
      ctx.globalAlpha = 1
      ctx.fillStyle = ROLE_LABEL_COLOR
      ctx.globalAlpha = 0.5 + 0.5 * intensity
      ctx.font = "12px ui-sans-serif, system-ui"
      ctx.textAlign = "center"
      ctx.fillText(role, well.x, well.y - 98)
      ctx.globalAlpha = 1
    }

    // Attention-graph (reasoning) edges — violet, over the (omitted) repo edges.
    const now = store.lastRecompute || Date.now() / 1000
    for (const e of store.graph.liveEdges(now)) {
      const a = bodies.get(e.from)
      const b = bodies.get(e.to)
      if (!a || !b) continue
      ctx.beginPath()
      ctx.moveTo(a.pos.x, a.pos.y)
      ctx.lineTo(b.pos.x, b.pos.y)
      ctx.strokeStyle = ATTENTION_EDGE_COLOR
      ctx.globalAlpha = Math.min(0.6, 0.2 + e.heat * 0.1)
      ctx.lineWidth = 1.5
      ctx.stroke()
      ctx.globalAlpha = 1
    }

    // Symbol nodes — only those above the relative visibility tier.
    for (const b of bodies.values()) {
      if (b.mass <= 0) continue
      const tier = tierFor(b.mass, maxDisplay)
      if (tier === "hidden") continue
      const r = nodeRadius(b.mass, maxDisplay)
      const color = roleColor(b.role)

      const glow = glowAlpha(b.mass, maxDisplay)
      if (glow > 0) {
        ctx.beginPath()
        ctx.arc(b.pos.x, b.pos.y, r * 2.4, 0, Math.PI * 2)
        ctx.fillStyle = color
        ctx.globalAlpha = glow
        ctx.fill()
        ctx.globalAlpha = 1
      }

      ctx.beginPath()
      ctx.arc(b.pos.x, b.pos.y, r, 0, Math.PI * 2)
      ctx.fillStyle = color
      ctx.globalAlpha = nodeOpacity(b.mass, maxDisplay)
      ctx.fill()
      ctx.globalAlpha = 1

      if (tier === "dominant") {
        const label = b.qname.split(":").pop() ?? b.qname
        ctx.fillStyle = "#e2e8f0"
        ctx.font = "11px ui-sans-serif, system-ui"
        ctx.textAlign = "center"
        ctx.fillText(label, b.pos.x, b.pos.y - r - 4)
      }
    }

    ctx.restore()
  }

  // --- manual pan/zoom (user-controlled camera) ---
  const drag = useRef<{ x: number; y: number } | null>(null)
  useEffect(() => {
    const canvas = canvasRef.current
    if (!canvas) return
    const onDown = (e: MouseEvent) => (drag.current = { x: e.clientX, y: e.clientY })
    const onMove = (e: MouseEvent) => {
      if (!drag.current) return
      cameraRef.current.x += e.clientX - drag.current.x
      cameraRef.current.y += e.clientY - drag.current.y
      drag.current = { x: e.clientX, y: e.clientY }
      kick()
    }
    const onUp = () => (drag.current = null)
    const onWheel = (e: WheelEvent) => {
      e.preventDefault()
      const factor = Math.exp(-e.deltaY * 0.001)
      cameraRef.current.k = Math.min(4, Math.max(0.2, cameraRef.current.k * factor))
      kick()
    }
    canvas.addEventListener("mousedown", onDown)
    window.addEventListener("mousemove", onMove)
    window.addEventListener("mouseup", onUp)
    canvas.addEventListener("wheel", onWheel, { passive: false })
    return () => {
      canvas.removeEventListener("mousedown", onDown)
      window.removeEventListener("mousemove", onMove)
      window.removeEventListener("mouseup", onUp)
      canvas.removeEventListener("wheel", onWheel)
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  // Kick once on mount so the first frame paints.
  useEffect(() => {
    kick()
    return () => {
      if (rafRef.current != null) cancelAnimationFrame(rafRef.current)
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  // The canvas is blank by design until the agent moves. Show a quiet idle hint
  // only when there's no attention yet (and clear it the moment any appears).
  const showIdleHint = useMemo(() => !hasAttention, [hasAttention])
  void systemModel

  return (
    <div className={className} style={{ position: "relative" }}>
      <canvas
        ref={canvasRef}
        style={{ width: "100%", height: "100%", display: "block", cursor: "grab" }}
      />
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
      {/* roleByQname referenced to keep the subscription live for refreshes */}
      <span style={{ display: "none" }}>{roleByQname.size}</span>
    </div>
  )
}
