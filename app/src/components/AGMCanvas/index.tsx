// AGMCanvas — the Attention Gravity Map renderer.
//
// A self-contained Canvas 2D view driven by the AGM engine (agmStore). The
// gravity simulation IS the layout; this component owns the rAF loop, runs
// gravity.step + model.recompute while the system is not at rest, and stops when
// it settles (motion only on attention change). Manual pan/zoom; user-controlled
// camera (the attention centroid never moves the view). Minimal aesthetic: heat
// reads through opacity/glow/size over fixed role geography.

import { useEffect, useMemo, useRef, useState } from "react"
import { useAGMStore } from "@/store/agmStore"
import {
  step as gravityStep,
  clusterCentroidOf,
  DEFAULT_GRAVITY,
  type Body,
  type Vec,
} from "@/agm/gravity"
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
  const [, force] = useState(0)

  const systemModel = useAGMStore((s) => s.systemModel)
  const roleWells = useAGMStore((s) => s.roleWells)
  const roleByQname = useAGMStore((s) => s.roleByQname)

  // Build/refresh bodies when the topology changes. Role wells are pinned bodies
  // (fixed geography); symbols are free bodies seeded near their well.
  useEffect(() => {
    if (!systemModel) return
    const bodies = bodiesRef.current
    // Role-well bodies (pinned).
    for (const [role, well] of roleWells) {
      const key = `role:${role}`
      if (!bodies.has(key)) {
        bodies.set(key, {
          qname: key,
          role,
          pos: { ...well },
          vel: { x: 0, y: 0 },
          mass: 0,
          pinned: true,
        })
      }
    }
    // Symbol bodies — keep existing positions across refresh (continuity).
    for (const n of systemModel.nodes) {
      if (bodies.has(n.qname)) continue
      const well = roleWells.get(n.role || "untagged") ?? { x: 0, y: 0 }
      bodies.set(n.qname, {
        qname: n.qname,
        role: n.role || "untagged",
        pos: { x: well.x + (Math.random() - 0.5) * 80, y: well.y + (Math.random() - 0.5) * 80 },
        vel: { x: 0, y: 0 },
        mass: 0,
        pinned: false,
      })
    }
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

    // Sync body masses from the current display-mass snapshot (+ propagation).
    const bodies = bodiesRef.current
    const mass = store.massByQname
    const prop = store.propagated
    let maxDisplay = 0
    for (const b of bodies.values()) {
      if (b.pinned) continue
      const m = mass.get(b.qname)
      const propAdd = prop.get(b.qname) ?? 0
      const d = m ? m.display : propAdd > 0 ? displayMass(propAdd) : 0
      b.mass = d
      if (d > maxDisplay) maxDisplay = d
    }

    // Investigation cluster pull (confidence scales the pull strength).
    const inv = store.investigations.active()
    const members = new Set(inv?.scope ?? [])
    const bodyList = [...bodies.values()]
    const clusterCentroid = members.size ? clusterCentroidOf(bodyList, members) : null
    const cfg = {
      ...DEFAULT_GRAVITY,
      clusterPull: DEFAULT_GRAVITY.clusterPull * (inv ? inv.confidence : 0),
    }

    const energy = gravityStep(bodyList, roleWells, clusterCentroid, members, cfg)
    draw(maxDisplay)

    // Stop when settled AND no residual heat motion. Recompute keeps decaying
    // mass, so we keep looping a bit while there's live mass to fade.
    const hasHeat = maxDisplay > 0
    if (energy < cfg.restThreshold && !hasHeat) {
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

    // Role wells (continents) — always visible, low-key.
    for (const [role, well] of roleWells) {
      ctx.beginPath()
      ctx.arc(well.x, well.y, 90, 0, Math.PI * 2)
      ctx.strokeStyle = ROLE_RING_COLOR
      ctx.lineWidth = 1
      ctx.stroke()
      ctx.fillStyle = ROLE_LABEL_COLOR
      ctx.font = "12px ui-sans-serif, system-ui"
      ctx.textAlign = "center"
      ctx.fillText(role, well.x, well.y - 98)
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
      if (b.pinned || b.mass <= 0) continue
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

  const empty = useMemo(() => !systemModel, [systemModel])

  return (
    <div className={className} style={{ position: "relative" }}>
      <canvas
        ref={canvasRef}
        style={{ width: "100%", height: "100%", display: "block", cursor: "grab" }}
      />
      {empty && (
        <div
          style={{
            position: "absolute",
            inset: 0,
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            color: "#64748b",
            fontSize: 13,
            pointerEvents: "none",
          }}
        >
          Attention map — waiting for the graph…
        </div>
      )}
      {/* roleByQname referenced to keep the subscription live for refreshes */}
      <span style={{ display: "none" }}>{roleByQname.size}</span>
    </div>
  )
}
