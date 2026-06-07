import { useEffect, useRef } from "react"
import { useConductor } from "@/graph/conductor"
import { useGraphStore } from "@/store/graphStore"
import { activityDash } from "@/graph/style"

// A dedicated FX canvas layered over the force graph. One rAF reads the
// Conductor's transient FX (ripples, comet-tails, breadcrumbs) and the agent's
// path, maps each symbol to its component bubble's screen position, and paints.
// Keeping FX on a separate canvas isolates per-frame effect redraws from the
// force-graph's node painting (docs/choreography-prd.md §7).

interface Props {
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  fgRef: React.MutableRefObject<any>
  componentPos: Map<string, { x: number; y: number }>
  width: number
  height: number
}

export function ChoreographyOverlay({ fgRef, componentPos, width, height }: Props) {
  const canvasRef = useRef<HTMLCanvasElement | null>(null)

  useEffect(() => {
    let raf = 0
    let lastSig = ""
    let cleared = false
    const draw = () => {
      const cv = canvasRef.current
      const fg = fgRef.current
      if (!cv || !fg) {
        raf = requestAnimationFrame(draw)
        return
      }
      const ctx = cv.getContext("2d")
      if (!ctx) {
        raf = requestAnimationFrame(draw)
        return
      }
      const epoch = Date.now()
      useConductor.getState().tick(epoch)
      const { ripples, comets, breadcrumbs, replaying } = useConductor.getState()
      const gs = useGraphStore.getState()
      const axis = gs.axis

      // Perf: only repaint when something actually changed — live FX present, a
      // replay running, or the camera transform moved (which shifts anchors).
      const liveFx = ripples.length > 0 || comets.length > 0 || replaying
      let sig = `${breadcrumbs.length}`
      if (fg.graph2ScreenCoords) {
        const o = fg.graph2ScreenCoords(0, 0)
        const u = fg.graph2ScreenCoords(100, 0)
        sig += `:${Math.round(o.x)},${Math.round(o.y)},${Math.round(u.x)}`
      }
      if (!liveFx && sig === lastSig) {
        if (!cleared && breadcrumbs.length === 0) {
          ctx.clearRect(0, 0, width, height)
          cleared = true
        }
        raf = requestAnimationFrame(draw)
        return
      }
      lastSig = sig
      cleared = false

      // resolve a symbol qname → screen point via its component bubble
      const screenOf = (qname: string): { x: number; y: number } | null => {
        const node = gs.nodesByQname.get(qname)
        if (!node) return null
        const group = axis === "role" ? node.role || "untagged" : node.subsystem
        const gp = componentPos.get(group)
        if (!gp) return null
        const s = fg.graph2ScreenCoords(gp.x, gp.y)
        return { x: Math.round(s.x), y: Math.round(s.y) }
      }

      ctx.clearRect(0, 0, width, height)

      // comet-tail: faint polyline through the recent breadcrumb path
      if (breadcrumbs.length > 1) {
        const pts = breadcrumbs
          .slice()
          .sort((a, b) => a.seq - b.seq)
          .map((b) => screenOf(b.qname))
          .filter((p): p is { x: number; y: number } => !!p)
        if (pts.length > 1) {
          ctx.beginPath()
          ctx.moveTo(pts[0].x, pts[0].y)
          for (let i = 1; i < pts.length; i++) ctx.lineTo(pts[i].x, pts[i].y)
          ctx.strokeStyle = "rgba(148,163,184,0.25)"
          ctx.lineWidth = 1.5
          ctx.stroke()
        }
      }

      // ripples — expanding rings (cascade wavefront / writes)
      for (const r of ripples) {
        const p = screenOf(r.qname)
        if (!p) continue
        const age = (epoch - r.born) / r.ttl
        if (age >= 1) continue
        const radius = 8 + age * 46
        ctx.beginPath()
        ctx.arc(p.x, p.y, radius, 0, 2 * Math.PI)
        ctx.strokeStyle = r.color
        ctx.globalAlpha = (1 - age) * 0.7
        ctx.lineWidth = 2
        ctx.setLineDash(activityDash(r.state)) // state legible without colour
        ctx.stroke()
        ctx.setLineDash([])
      }
      ctx.globalAlpha = 1

      // comets — particles travelling source → target
      for (const c of comets) {
        const a = screenOf(c.from)
        const b = screenOf(c.to)
        if (!a || !b) continue
        const age = (epoch - c.born) / c.ttl
        if (age >= 1) continue
        const x = a.x + (b.x - a.x) * age
        const y = a.y + (b.y - a.y) * age
        ctx.beginPath()
        ctx.arc(Math.round(x), Math.round(y), 3, 0, 2 * Math.PI)
        ctx.fillStyle = c.color
        ctx.globalAlpha = Math.min(1, 1.4 - age)
        ctx.fill()
        // soft trail
        ctx.globalAlpha = (1 - age) * 0.3
        ctx.beginPath()
        ctx.moveTo(a.x, a.y)
        ctx.lineTo(x, y)
        ctx.strokeStyle = c.color
        ctx.lineWidth = 1.5
        ctx.stroke()
      }
      ctx.globalAlpha = 1

      // breadcrumbs — numbered dots marking the agent's path this turn
      for (const b of breadcrumbs) {
        const p = screenOf(b.qname)
        if (!p) continue
        ctx.beginPath()
        ctx.arc(p.x, p.y, 7, 0, 2 * Math.PI)
        ctx.fillStyle = "rgba(2,6,23,0.85)"
        ctx.fill()
        ctx.strokeStyle = b.color
        ctx.lineWidth = 1.25
        ctx.stroke()
        ctx.fillStyle = "#e2e8f0"
        ctx.font = "9px ui-sans-serif, system-ui, sans-serif"
        ctx.textAlign = "center"
        ctx.textBaseline = "middle"
        ctx.fillText(String(b.seq), p.x, p.y)
      }

      raf = requestAnimationFrame(draw)
    }
    raf = requestAnimationFrame(draw)
    return () => cancelAnimationFrame(raf)
  }, [fgRef, componentPos, width, height])

  return (
    <canvas
      ref={canvasRef}
      width={width}
      height={height}
      className="absolute inset-0 z-10 pointer-events-none"
    />
  )
}
