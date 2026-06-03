import { create } from "zustand"
import type {
  AgentState,
  SystemModel,
  SystemModelNode,
  GroupingAxis,
} from "@/api/types"
import { buildAdjacency, selectVisible, type Adjacency, type VisibleSet } from "@/graph/doi"
import { regimeForModel, type RegimeConfig } from "@/graph/regime"

// Per-node live state, keyed by qname. Kept separate from the immutable model
// so agent activity / selection never forces a model rebuild.
export interface NodeRuntime {
  agentState: AgentState
  selected: boolean
  // transient activity intensity 0..1 driven by SSE (pulse/heat); animator reads it
  activity: number
  // edit-heat 0..1, decays over time
  heat: number
}

// View level: L0 components -> L1 landmarks (a component expanded) -> L2 symbol nbhd
export type ViewLevel = "components" | "landmarks" | "neighborhood"

// How members inside an expanded container are sub-grouped.
export type MemberGrouping = "subsystem" | "class" | "owningClass"

interface GraphStore {
  // --- the model (immutable once loaded) ---
  model: SystemModel | null
  nodesByQname: Map<string, SystemModelNode>
  adjacency: Adjacency | null
  regime: RegimeConfig | null

  // --- view state ---
  axis: GroupingAxis
  level: ViewLevel
  // the single transient expansion (a component key) + the pinned ones
  focusedExpansion: string | null
  pinnedExpansions: Set<string>
  // focus qnames feeding DOI (selection + agent location)
  focus: string[]
  selectedQname: string | null
  hoveredId: string | null
  // legend filter: when set, only this group (on the current axis) is bright
  isolatedGroup: string | null
  // how to sub-group members inside an expanded role/subsystem container
  memberGrouping: MemberGrouping

  // --- live per-node runtime ---
  runtime: Map<string, NodeRuntime>
  // transient "the agent just traversed here" edges -> expiry timestamp (ms).
  // Drives directional comet particles along the real call edges.
  activeFlows: Map<string, number>

  // --- derived visible set (recomputed by recomputeVisible) ---
  visible: VisibleSet

  // --- actions: model lifecycle ---
  setModel: (model: SystemModel, edges: Array<{ from: string; to: string }>) => void
  recomputeVisible: () => void

  // --- actions: view ---
  setAxis: (axis: GroupingAxis) => void
  setIsolatedGroup: (key: string | null) => void
  setMemberGrouping: (g: MemberGrouping) => void
  setLevel: (level: ViewLevel) => void
  expandComponent: (key: string) => void // transient (auto-collapses prior)
  collapseTransient: () => void
  togglePin: (key: string) => void
  selectNode: (qname: string | null) => void
  setHovered: (id: string | null) => void
  focusFile: (relPath: string) => void

  // --- actions: live runtime (driven by SSE) ---
  setNodeAgentState: (qname: string, state: AgentState) => void
  setFileAgentState: (filePath: string, state: AgentState) => void
  bumpActivity: (qname: string, amount?: number) => void
  setHeat: (qname: string, heat: number) => void
  flowAlong: (from: string, to: string, durationMs?: number) => void
  decayActivityAndHeat: (dt: number) => void
}

const DEFAULT_RUNTIME: NodeRuntime = { agentState: "idle", selected: false, activity: 0, heat: 0 }

function emptyVisible(): VisibleSet {
  return { nodes: [], aggregates: [] }
}

export const useGraphStore = create<GraphStore>((set, get) => ({
  model: null,
  nodesByQname: new Map(),
  adjacency: null,
  regime: null,

  axis: "role",
  level: "components",
  focusedExpansion: null,
  pinnedExpansions: new Set(),
  focus: [],
  selectedQname: null,
  hoveredId: null,
  isolatedGroup: null,
  memberGrouping: "subsystem",

  runtime: new Map(),
  activeFlows: new Map(),
  visible: emptyVisible(),

  setModel: (model, edges) => {
    const nodesByQname = new Map(model.nodes.map((n) => [n.qname, n]))
    const adjacency = buildAdjacency(edges)
    const regime = regimeForModel(model)
    set({
      model,
      nodesByQname,
      adjacency,
      regime,
      axis: regime.defaultAxis,
      level: "components",
      focusedExpansion: null,
      focus: [],
      runtime: new Map(),
    })
    get().recomputeVisible()
  },

  recomputeVisible: () => {
    const { model, adjacency, regime, axis, focus, focusedExpansion, pinnedExpansions } = get()
    if (!model || !adjacency || !regime) {
      set({ visible: emptyVisible() })
      return
    }
    // When components are expanded (transient + pinned), restrict the symbol
    // pool to their groups. Empty restriction = whole-system (no expansion).
    const expanded = new Set(pinnedExpansions)
    if (focusedExpansion) expanded.add(focusedExpansion)
    const restrictToGroups = expanded.size > 0 ? expanded : undefined
    const visible = selectVisible({
      model,
      budget: regime.budget,
      salienceFloor: regime.salienceFloor,
      axis,
      focus,
      adjacency,
      restrictToGroups,
    })
    set({ visible })
  },

  setAxis: (axis) => {
    set({ axis, focusedExpansion: null, level: "components", isolatedGroup: null })
    get().recomputeVisible()
  },

  setIsolatedGroup: (key) => set({ isolatedGroup: key }),

  setMemberGrouping: (memberGrouping) => set({ memberGrouping }),

  setLevel: (level) => set({ level }),

  expandComponent: (key) => {
    // exactly one transient expansion: replaces the previous unpinned one
    set({ focusedExpansion: key, level: "landmarks" })
    get().recomputeVisible()
  },

  collapseTransient: () => {
    const { pinnedExpansions } = get()
    // collapsing the transient expansion returns to L0 unless pins keep us at L1
    set({
      focusedExpansion: null,
      level: pinnedExpansions.size > 0 ? "landmarks" : "components",
      focus: [],
      selectedQname: null,
    })
    get().recomputeVisible()
  },

  togglePin: (key) => {
    set((s) => {
      const pinned = new Set(s.pinnedExpansions)
      if (pinned.has(key)) pinned.delete(key)
      else pinned.add(key)
      return { pinnedExpansions: pinned }
    })
    get().recomputeVisible()
  },

  selectNode: (qname) => {
    set((s) => {
      const runtime = new Map(s.runtime)
      if (s.selectedQname) {
        const prev = runtime.get(s.selectedQname) ?? { ...DEFAULT_RUNTIME }
        runtime.set(s.selectedQname, { ...prev, selected: false })
      }
      if (qname) {
        const cur = runtime.get(qname) ?? { ...DEFAULT_RUNTIME }
        runtime.set(qname, { ...cur, selected: true })
      }
      return {
        runtime,
        selectedQname: qname,
        focus: qname ? [qname] : [],
      }
    })
    get().recomputeVisible()
  },

  setHovered: (id) => set({ hoveredId: id }),

  focusFile: (relPath) => {
    const { model } = get()
    if (!model) return
    const qnames = model.nodes
      .filter((n) => n.file_path === relPath || n.file_path.endsWith(relPath))
      .map((n) => n.qname)
    set({ focus: qnames })
    get().recomputeVisible()
  },

  setNodeAgentState: (qname, agentState) =>
    set((s) => {
      const runtime = new Map(s.runtime)
      const cur = runtime.get(qname) ?? { ...DEFAULT_RUNTIME }
      runtime.set(qname, { ...cur, agentState })
      return { runtime }
    }),

  setFileAgentState: (filePath, agentState) =>
    set((s) => {
      if (!s.model) return {}
      const runtime = new Map(s.runtime)
      for (const n of s.model.nodes) {
        if (n.file_path === filePath || n.file_path.endsWith(filePath)) {
          const cur = runtime.get(n.qname) ?? { ...DEFAULT_RUNTIME }
          runtime.set(n.qname, { ...cur, agentState })
        }
      }
      return { runtime }
    }),

  bumpActivity: (qname, amount = 1) =>
    set((s) => {
      const runtime = new Map(s.runtime)
      const cur = runtime.get(qname) ?? { ...DEFAULT_RUNTIME }
      runtime.set(qname, { ...cur, activity: Math.min(1, cur.activity + amount) })
      return { runtime }
    }),

  setHeat: (qname, heat) =>
    set((s) => {
      const runtime = new Map(s.runtime)
      const cur = runtime.get(qname) ?? { ...DEFAULT_RUNTIME }
      runtime.set(qname, { ...cur, heat: Math.max(0, Math.min(1, heat)) })
      return { runtime }
    }),

  flowAlong: (from, to, durationMs = 1600) =>
    set((s) => {
      const activeFlows = new Map(s.activeFlows)
      activeFlows.set(`${from}|${to}`, Date.now() + durationMs)
      // also light up the destination as it's "reached"
      const runtime = new Map(s.runtime)
      const cur = runtime.get(to) ?? { ...DEFAULT_RUNTIME }
      runtime.set(to, { ...cur, activity: Math.min(1, cur.activity + 0.6) })
      return { activeFlows, runtime }
    }),

  decayActivityAndHeat: (dt) =>
    set((s) => {
      // activity decays fast (~0.5s), heat decays slow (~minutes)
      const aK = Math.exp(-dt / 500)
      const hK = Math.exp(-dt / 120000)
      const runtime = new Map(s.runtime)
      let changed = false
      for (const [q, r] of runtime) {
        if (r.activity > 0.001 || r.heat > 0.001) {
          runtime.set(q, { ...r, activity: r.activity * aK, heat: r.heat * hK })
          changed = true
        }
      }
      // expire finished flows
      let flows = s.activeFlows
      if (flows.size) {
        const now = Date.now()
        const next = new Map<string, number>()
        for (const [k, exp] of flows) if (exp > now) next.set(k, exp)
        if (next.size !== flows.size) {
          flows = next
          changed = true
        }
      }
      return changed ? { runtime, activeFlows: flows } : {}
    }),
}))
