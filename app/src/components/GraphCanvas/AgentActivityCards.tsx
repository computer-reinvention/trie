import { useEffect, useRef, useState } from "react"
import { useGraphStore } from "@/store/graphStore"
import { ACTIVITY } from "@/graph/style"
import type { AgentState } from "@/api/types"

// Live HTML popup cards that float over the graph, anchored to the component
// bubble of each symbol the agent just touched. Each card shows the symbol name,
// the action (read / search / edit) and a readable snippet of the tool output
// that put it under attention. Cards follow the camera (rAF) and fade out.
//
// This is the reliable, readable replacement for canvas-drawn popups: real DOM,
// always visible (no drilling required), styled, and legible at any zoom.

// Cards stay long enough to read; fade only in the final stretch.
const NOTE_TTL = 9000
const NOTE_FADE = 1200
// Max cards stacked on one component bubble (most recent win).
const STACK_MAX = 3

function actionColor(state: AgentState): string {
  if (state === "writing") return ACTIVITY.write
  if (state === "scanning") return ACTIVITY.scan
  return ACTIVITY.read
}
function actionVerb(state: AgentState): string {
  if (state === "writing") return "editing"
  if (state === "scanning") return "searching"
  return "reading"
}

interface CardsProps {
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  fgRef: React.MutableRefObject<any>
  // group key -> graph-space position of its component bubble
  componentPos: Map<string, { x: number; y: number }>
  width: number
  height: number
}

export function AgentActivityCards({ fgRef, componentPos, width, height }: CardsProps) {
  const notes = useGraphStore((s) => s.notes)
  const axis = useGraphStore((s) => s.axis)
  const nodesByQname = useGraphStore((s) => s.nodesByQname)
  // tick to re-read screen coords as the camera pans/zooms
  const [, setTick] = useState(0)
  const rafRef = useRef<number>(0)

  // Keep repositioning while there are fresh notes.
  useEffect(() => {
    const loop = () => {
      const now = Date.now()
      let anyFresh = false
      for (const n of notes.values()) if (now - n.ts < NOTE_TTL) anyFresh = true
      setTick((t) => (t + 1) % 1_000_000)
      if (anyFresh) rafRef.current = requestAnimationFrame(loop)
      else rafRef.current = 0
    }
    rafRef.current = requestAnimationFrame(loop)
    return () => {
      if (rafRef.current) cancelAnimationFrame(rafRef.current)
    }
  }, [notes])

  const fg = fgRef.current
  if (!fg) return null
  const now = Date.now()

  // Group fresh notes by component, most-recent first, capped per bubble so a
  // burst of reads stacks (and each card lingers its full lifetime) instead of
  // replacing each other in a blink.
  const byGroup = new Map<
    string,
    Array<{ qname: string; text: string; state: AgentState; ts: number }>
  >()
  for (const [qname, note] of notes.entries()) {
    if (now - note.ts >= NOTE_TTL) continue
    const node = nodesByQname.get(qname)
    if (!node) continue
    const group = axis === "role" ? node.role || "untagged" : node.subsystem
    const arr = byGroup.get(group) ?? []
    arr.push({ qname, ...note })
    byGroup.set(group, arr)
  }

  const cards: Array<{
    key: string
    left: number
    top: number
    name: string
    text: string
    state: AgentState
    fade: number
  }> = []
  for (const [group, arr] of byGroup.entries()) {
    const gp = componentPos.get(group)
    if (!gp) continue
    const s = fg.graph2ScreenCoords(gp.x, gp.y)
    if (s.x < -50 || s.y < -50 || s.x > width + 50 || s.y > height + 50) continue
    const recent = arr.sort((a, b) => b.ts - a.ts).slice(0, STACK_MAX)
    recent.forEach((note, i) => {
      const age = now - note.ts
      const fade = age < NOTE_TTL - NOTE_FADE ? 1 : Math.max(0, (NOTE_TTL - age) / NOTE_FADE)
      cards.push({
        key: note.qname,
        left: s.x,
        // stack upward: newest closest to the bubble
        top: s.y - i * 64,
        name: nodesByQname.get(note.qname)?.name ?? note.qname.split(":").pop() ?? note.qname,
        text: note.text,
        state: note.state,
        // older cards in the stack dim slightly so the newest reads first
        fade: fade * (1 - i * 0.25),
      })
    })
  }

  if (cards.length === 0) return null

  return (
    <div className="absolute inset-0 z-20 pointer-events-none overflow-hidden">
      {cards.map((c) => {
        const col = actionColor(c.state)
        return (
          <div
            key={c.key}
            className="absolute -translate-x-1/2"
            style={{
              left: c.left,
              top: c.top - 14,
              transform: "translate(-50%, -100%)",
              opacity: c.fade,
              transition: "opacity 200ms linear",
              maxWidth: 240,
            }}
          >
            <div
              className="rounded-md border bg-slate-950/95 shadow-xl px-2.5 py-1.5"
              style={{ borderColor: col }}
            >
              <div className="flex items-center gap-1.5 mb-0.5">
                <span
                  className="w-1.5 h-1.5 rounded-full shrink-0"
                  style={{ background: col, boxShadow: `0 0 6px ${col}` }}
                />
                <span className="text-[10px] uppercase tracking-wide" style={{ color: col }}>
                  {actionVerb(c.state)}
                </span>
                <span className="text-[11px] font-mono text-slate-200 truncate">{c.name}</span>
              </div>
              <p className="text-[11px] leading-snug text-slate-400 line-clamp-3">{c.text}</p>
            </div>
            {/* pointer */}
            <div
              className="w-2 h-2 rotate-45 mx-auto -mt-1 border-r border-b"
              style={{ background: "rgb(2 6 23 / 0.95)", borderColor: col }}
            />
          </div>
        )
      })}
    </div>
  )
}
