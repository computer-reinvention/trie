import { useEffect } from "react"
import { useGraphStore } from "@/store/graphStore"
import { useAgentStore } from "@/store/agentStore"
import { useAGMStore } from "@/store/agmStore"
import { choreographFor } from "@/graph/agentChoreography"
import { classifyTool, syntheticTarget } from "@/agm/toolClassify"
import {
  syntheticQname,
  syntheticFileQname,
  looksLikeFilePath,
  isSyntheticQname,
  isSyntheticFileQname,
} from "@/api/types"
import { graphClient } from "@/api/graphClient"
import { motionPrefs, playCascade, ghostCascade, conductGlance, useConductor } from "@/graph/conductor"
import { usePatchesStore } from "@/store/patchesStore"
import type { ToolPart } from "@/api/types"

// Bridges the opencode event bus (the general /event SSE stream) to the
// transcript store and the live graph.
//
// We subscribe to the raw bus stream rather than the /desktop/event mapped
// stream: the raw stream is the battle-tested one (heartbeats + every publish),
// and doing the mapping here keeps a single source of truth. Bus events we use:
//   message.part.updated  -> transcript part upsert + graph choreography
//   message.part.delta    -> streaming text / reasoning (split by `field`)
//   message.updated       -> assistant cost/tokens/finish/error
//   session.status        -> running / idle  (busy => running)
//   session.error         -> chat error
//   permission.asked/.replied -> inline approve-deny
//   file.edited           -> mark graph nodes stale
//
// Tool activity colours nodes (read=blue, scan=violet, write=amber) and animates
// flow comets along edges between the symbols the agent touches. It never moves
// the camera or expands a component — just flashes/highlights, leaving the user
// in control of the view.
export function useOpenCodeSSE(opencodePort: number): void {
  useEffect(() => {
    if (!opencodePort) return

    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const trie = (window as any).trie
    // Raw bus stream — carries all publishes; no directory needed.
    const sseUrl = `http://127.0.0.1:${opencodePort}/event`
    trie.sseSubscribe(sseUrl)

    const graph = () => useGraphStore.getState()
    const agent = () => useAgentStore.getState()

    // Highlight-only choreography: flash the symbols the agent touches and let
    // their glow linger, but never move the camera or expand a component. The
    // user stays in control of the view; activity rolls up to the component
    // bubbles so you can still see *where* the agent is working.
    // Fire a comet along any REAL call-graph edge that connects a symbol the
    // agent just touched to one it touched recently. This visualises the agent
    // "moving" through connected code even without an explicit trace.
    const animateConnections = (touched: string[]) => {
      const g = graph()
      const adj = g.adjacency
      if (!adj || touched.length === 0) return
      // recent trail = the agent's recent attention; cap to keep it cheap
      const recent = g.trail.slice(-8)
      const seen = new Set<string>()
      for (const q of touched) {
        const nbrs = adj.neighbours.get(q)
        if (!nbrs) continue
        for (const prev of recent) {
          if (prev === q) continue
          if (!nbrs.has(prev)) continue // only animate edges that actually exist
          const key = q < prev ? `${q}|${prev}` : `${prev}|${q}`
          if (seen.has(key)) continue
          seen.add(key)
          // direction: from where it was -> to where it is now
          g.flowAlong(prev, q)
        }
      }
    }

    // A short, readable line describing why a node lit up: prefer the first
    // line of the tool's own output, then its title, then the symbol one-liner.
    const noteFor = (q: string, part: ToolPart): string => {
      const out = part.state.output
      if (out) {
        const line = out
          .split("\n")
          .map((s) => s.trim())
          .find((s) => s.length > 0 && !s.startsWith("{") && !s.startsWith("["))
        if (line) return line.length > 160 ? line.slice(0, 157) + "…" : line
      }
      if (part.state.title) return part.state.title
      const ol = graph().nodesByQname.get(q)?.one_liner
      return ol ?? ""
    }

    const applyChoreography = (part: ToolPart) => {
      const g = graph()
      const c = choreographFor(part)
      const rm = motionPrefs().reduceMotion
      // edges connecting prior attention to this step (before pushing new trail)
      if (!rm) animateConnections([...c.reads, ...c.scans, ...c.writes])
      for (const q of c.reads) {
        g.setNodeAgentState(q, "reading")
        if (!rm) g.bumpActivity(q, 0.85) // pulse is movement — skip when reduced
        g.pushTrail(q, "reading")
        g.setNote(q, noteFor(q, part), "reading")
        conductGlance(q, "reading")
      }
      for (const q of c.scans) {
        g.setNodeAgentState(q, "scanning")
        if (!rm) g.bumpActivity(q, 0.6)
        g.pushTrail(q, "scanning")
        const ol = g.nodesByQname.get(q)?.one_liner ?? ""
        g.setNote(q, ol, "scanning")
      }
      for (const q of c.writes) {
        g.setNodeAgentState(q, "writing")
        if (!rm) g.bumpActivity(q, 1)
        g.pushTrail(q, "writing")
        g.setNote(q, noteFor(q, part), "writing")
        conductGlance(q, "writing")
      }
      // Non-symbol tools (bash, shell, fetch, …) have no graph target — surface
      // them as an ambient HUD chip so the agent's off-graph actions are visible.
      if (
        part.state.status === "running" &&
        !c.reads.length &&
        !c.scans.length &&
        !c.writes.length &&
        !c.files.length
      ) {
        const t = part.tool.startsWith("trie_") ? part.tool.slice(5) : part.tool
        const inp = part.state.input ?? {}
        const txt =
          (typeof inp.command === "string" && inp.command) ||
          (typeof inp.description === "string" && inp.description) ||
          (typeof inp.url === "string" && inp.url) ||
          ""
        useConductor.getState().setHud(t, String(txt).slice(0, 80))
      }
      for (const f of c.files) g.setFileAgentState(f, "writing")
      // explicit trace/flow edges animate as comets — unless reduced-motion.
      if (!motionPrefs().reduceMotion) {
        c.flows.slice(0, 40).forEach((e, i) => setTimeout(() => g.flowAlong(e.from, e.to), i * 160))
      }
      if (part.state.status === "completed" || part.state.status === "error") {
        const settle = [...c.reads, ...c.scans]
        setTimeout(() => settle.forEach((q) => g.setNodeAgentState(q, "idle")), 900)
        for (const f of c.files) g.setFileAgentState(f, "stale")
      }

      // --- patch / cascade choreography (real compute_cascade) ---
      const tool = part.tool.startsWith("trie_") ? part.tool.slice(5) : part.tool
      const input = part.state.input ?? {}
      if (tool === "patch" && part.state.status === "completed" && typeof input.qname === "string") {
        ghostCascade(input.qname) // faint preview of the blast radius
      }
      if (tool === "patch_apply" && part.state.status === "running") {
        // play the wavefront for every symbol that had a staged patch
        const staged = [...usePatchesStore.getState().patchedQnames]
        staged.slice(0, 12).forEach((q, i) => setTimeout(() => playCascade(q), i * 120))
      }
    }

    // AGM ingestion: feed the live attention engine from the same tool parts the
    // choreography uses. Only fires on completion so output qnames are present.
    // Records durably via the desktop endpoint (best-effort) AND ingests into the
    // in-memory model for the live canvas.
    const applyAGM = (part: ToolPart) => {
      if (part.state.status !== "completed") return
      const agm = useAGMStore.getState()
      const now = Date.now() / 1000
      const c = choreographFor(part)
      const eventType = classifyTool(part.tool)

      // Only ingest targets that are REAL symbols in the loaded graph. The agent
      // often passes file/module paths (e.g. "trie/mcp_server.py") to read/trace
      // — those aren't symbols, have no role/position. A path-shaped target gets
      // its OWN per-file synthetic node (named by the file, clustered in the
      // FILESYSTEM region) instead of being lumped into one giant "Filesystem"
      // pill; anything else falls back to the single Filesystem surface.
      const known = agm.nodesByQname
      const resolveTarget = (target: string): string => {
        if (known.has(target)) return target
        if (looksLikeFilePath(target)) return syntheticFileQname(target)
        return syntheticQname("Filesystem")
      }
      const record = (
        target: string,
        type: "grep" | "read" | "trace" | "write",
        scale = 1,
      ) => {
        const qname = resolveTarget(target)
        agm.ingest(qname, type, now, scale)
        if (scale === 1) graphClient.recordAttention({ type, qname }).catch(() => {})
      }

      for (const q of c.reads) record(q, "read")
      for (const q of c.writes) {
        record(q, "write")
        // Edited/patched symbols are PINNED: they never leave view for the rest
        // of the session (live mass effectively locked in; radius still drifts).
        if (known.has(q)) agm.model.pin(q)
      }
      // Grep is EXPLORATION: the query commits a little attention, but its many
      // result hits are a faint, capped "maybe relevant" net — not 20 equal
      // full-mass pills (that flooded the canvas). Hits get a small fractional
      // weight and are capped so a broad grep can't dominate the field.
      const GREP_HIT_SCALE = 0.25
      const GREP_HIT_CAP = 8
      c.scans.slice(0, GREP_HIT_CAP).forEach((q, i) => {
        // first scan entry is the query target (full weight); rest are hits.
        record(q, "grep", i === 0 ? 1 : GREP_HIT_SCALE)
      })
      // trace/flow chains build the attention graph (the reasoning trail).
      // Resolve each hop the same way reads do: a real symbol stays itself; a
      // file/module-path hop becomes its per-file synthetic node (rather than
      // being dropped, which used to shatter the chain and produce NO trace
      // edges). This is what makes trace constellations actually render.
      if (c.flows.length) {
        const chain: string[] = []
        const pushHop = (raw: string) => {
          const q = resolveTarget(raw)
          // Skip the catch-all Filesystem/Bash/Web surface as a trace hop — it
          // would draw a hairball of edges into one plumbing node. Real symbols
          // and per-file nodes are kept; dropping a surface hop simply links the
          // surrounding real nodes, which is still a faithful reasoning step.
          if (isSyntheticQname(q) && !isSyntheticFileQname(q)) return
          if (chain[chain.length - 1] !== q) chain.push(q)
        }
        for (const f of c.flows) {
          pushHop(f.from)
          pushHop(f.to)
        }
        if (chain.length > 1) agm.ingestTrace(chain, now)
      }
      // Non-code surfaces (bash/web/fs) → synthetic node attention.
      const synthetic = syntheticTarget(part.tool)
      if (synthetic && eventType) {
        record(synthetic, eventType as "grep" | "read" | "trace" | "write")
      }
      agm.recompute(now)
    }

    const handleEvent = (rawData: string) => {
      let ev: { type: string; properties: Record<string, unknown> }
      try {
        ev = JSON.parse(rawData) as { type: string; properties: Record<string, unknown> }
      } catch {
        return
      }
      const a = agent()
      const p = ev.properties ?? {}

      switch (ev.type) {
        case "message.part.updated": {
          // eslint-disable-next-line @typescript-eslint/no-explicit-any
          const part = (p as any).part
          if (!part) break
          a.applyPartUpdated(part.sessionID, part.messageID, part)
          if (part.type === "tool") {
            applyChoreography(part as ToolPart)
            applyAGM(part as ToolPart)
          }
          break
        }
        case "message.part.delta": {
          // eslint-disable-next-line @typescript-eslint/no-explicit-any
          const pp = p as any
          if (pp.field === "text")
            a.applyTextDelta(pp.sessionID, pp.messageID, pp.partID, pp.delta)
          else if (pp.field === "reasoning")
            a.applyReasoningDelta(pp.sessionID, pp.messageID, pp.partID, pp.delta)
          break
        }
        case "message.updated": {
          // eslint-disable-next-line @typescript-eslint/no-explicit-any
          const info = (p as any).info
          if (info) a.applyMessageInfo(info.sessionID, info)
          break
        }
        case "session.updated": {
          // Carries the full session info incl. the auto-generated title — keep
          // the switcher live as opencode names the chat.
          // eslint-disable-next-line @typescript-eslint/no-explicit-any
          const info = (p as any).info
          if (info?.id) a.upsertSession(info)
          break
        }
        case "session.status": {
          // eslint-disable-next-line @typescript-eslint/no-explicit-any
          const status = (p as any).status
          const sid = (p as any).sessionID
          if (!status || !sid) break
          // NOTE: busy/idle flip multiple times per turn (once per step), so we
          // must NOT clear the trail here — that caused activity cards to blip.
          // The trail is reset when the user sends a new message instead.
          if (status.type === "idle") a.setRunning(sid, false)
          else if (status.type === "busy") a.setRunning(sid, true)
          break
        }
        case "session.idle": {
          // eslint-disable-next-line @typescript-eslint/no-explicit-any
          const sid = (p as any).sessionID
          if (sid) a.setRunning(sid, false)
          break
        }
        case "session.error": {
          // eslint-disable-next-line @typescript-eslint/no-explicit-any
          const pp = p as any
          const msg = pp.error?.data?.message ?? pp.error?.message ?? "Agent error"
          if (pp.sessionID) a.setError(pp.sessionID, msg)
          break
        }
        case "file.edited": {
          // eslint-disable-next-line @typescript-eslint/no-explicit-any
          const file = (p as any).file as string | undefined
          if (file && !file.includes("triefacts/")) graph().setFileAgentState(file, "stale")
          break
        }
        case "permission.asked": {
          // eslint-disable-next-line @typescript-eslint/no-explicit-any
          const pp = p as any
          a.addPermission({
            id: pp.id,
            sessionID: pp.sessionID,
            permission: pp.permission,
            patterns: pp.patterns ?? [],
            metadata: pp.metadata ?? {},
            always: pp.always ?? [],
            callID: pp.tool?.callID,
            messageID: pp.tool?.messageID,
          })
          break
        }
        case "permission.replied": {
          // eslint-disable-next-line @typescript-eslint/no-explicit-any
          const pp = p as any
          if (pp.sessionID && pp.requestID) a.removePermission(pp.sessionID, pp.requestID)
          break
        }
      }
    }

    const unlisten = trie.onSseEvent(handleEvent)
    return () => {
      trie.sseUnsubscribe()
      if (typeof unlisten === "function") unlisten()
    }
  }, [opencodePort])
}
