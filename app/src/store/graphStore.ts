import { create } from "zustand"
import type { Node, Edge } from "@xyflow/react"
import type { SymbolNodeData, EdgeData, AgentState, TraceResult } from "@/api/types"

interface GraphStore {
  nodes: Node<SymbolNodeData>[]
  edges: Edge<EdgeData>[]

  setGraph: (nodes: Node<SymbolNodeData>[], edges: Edge<EdgeData>[]) => void
  addNodes: (nodes: Node<SymbolNodeData>[]) => void
  addEdges: (edges: Edge<EdgeData>[]) => void
  removeNode: (qname: string) => void
  hasNode: (qname: string) => boolean
  findNodeByName: (name: string) => Node<SymbolNodeData> | undefined

  // Node state mutations
  setNodeAgentState: (qname: string, state: AgentState) => void
  setFileAgentState: (filePath: string, state: AgentState) => void
  setNodeProse: (qname: string, prose: string) => void
  setNodeProseLoading: (qname: string, loading: boolean) => void
  expandNode: (qname: string) => void
  collapseNode: (qname: string) => void
  selectNode: (qname: string) => void
  deselectNode: (qname: string) => void
  deselectAll: () => void

  // Sidebar integration
  selectedFilePath: string | null
  setSelectedFilePath: (path: string | null) => void
  highlightedQnames: Set<string>

  // Merge a trace result — adds new nodes/edges without disturbing existing positions
  mergeTraceResult: (result: TraceResult) => void
}

export const useGraphStore = create<GraphStore>((set, get) => ({
  nodes: [],
  edges: [],
  selectedFilePath: null,
  highlightedQnames: new Set(),

  setGraph: (nodes, edges) => set({ nodes, edges }),

  addNodes: (newNodes) =>
    set((state) => {
      const existing = new Set(state.nodes.map((n) => n.id))
      const toAdd = newNodes.filter((n) => !existing.has(n.id))
      return toAdd.length > 0 ? { nodes: [...state.nodes, ...toAdd] } : {}
    }),

  addEdges: (newEdges) =>
    set((state) => {
      const existing = new Set(state.edges.map((e) => e.id))
      const toAdd = newEdges.filter((e) => !existing.has(e.id))
      return toAdd.length > 0 ? { edges: [...state.edges, ...toAdd] } : {}
    }),

  removeNode: (qname) =>
    set((state) => ({
      nodes: state.nodes.filter((n) => n.id !== qname),
      edges: state.edges.filter((e) => e.source !== qname && e.target !== qname),
    })),

  hasNode: (qname) => get().nodes.some((n) => n.id === qname),

  findNodeByName: (name) =>
    get().nodes.find(
      (n) =>
        n.data.name === name ||
        n.data.qname.endsWith(`:${name}`) ||
        n.data.qname.includes(`.${name}`),
    ),

  setNodeAgentState: (qname, agentState) =>
    set((state) => ({
      nodes: state.nodes.map((n) =>
        n.id === qname ? { ...n, data: { ...n.data, agentState } } : n,
      ),
    })),

  setFileAgentState: (filePath, agentState) =>
    set((state) => ({
      nodes: state.nodes.map((n) =>
        n.data.filePath === filePath || n.data.filePath.endsWith(filePath)
          ? { ...n, data: { ...n.data, agentState } }
          : n,
      ),
    })),

  setNodeProse: (qname, prose) =>
    set((state) => ({
      nodes: state.nodes.map((n) =>
        n.id === qname
          ? { ...n, data: { ...n.data, prose, isProseLoading: false } }
          : n,
      ),
    })),

  setNodeProseLoading: (qname, isProseLoading) =>
    set((state) => ({
      nodes: state.nodes.map((n) =>
        n.id === qname ? { ...n, data: { ...n.data, isProseLoading } } : n,
      ),
    })),

  expandNode: (qname) =>
    set((state) => ({
      nodes: state.nodes.map((n) =>
        n.id === qname ? { ...n, data: { ...n.data, isExpanded: true } } : n,
      ),
    })),

  collapseNode: (qname) =>
    set((state) => ({
      nodes: state.nodes.map((n) =>
        n.id === qname ? { ...n, data: { ...n.data, isExpanded: false } } : n,
      ),
    })),

  selectNode: (qname) =>
    set((state) => ({
      nodes: state.nodes.map((n) =>
        n.id === qname ? { ...n, data: { ...n.data, isSelected: true } } : n,
      ),
    })),

  deselectNode: (qname) =>
    set((state) => ({
      nodes: state.nodes.map((n) =>
        n.id === qname ? { ...n, data: { ...n.data, isSelected: false } } : n,
      ),
    })),

  deselectAll: () =>
    set((state) => ({
      nodes: state.nodes.map((n) => ({ ...n, data: { ...n.data, isSelected: false } })),
    })),

  setSelectedFilePath: (selectedFilePath) =>
    set((state) => {
      const highlighted = new Set(
        selectedFilePath
          ? state.nodes
              .filter(
                (n) =>
                  n.data.filePath === selectedFilePath ||
                  n.data.filePath.endsWith(selectedFilePath),
              )
              .map((n) => n.id)
          : [],
      )
      return {
        selectedFilePath,
        highlightedQnames: highlighted,
        nodes: state.nodes.map((n) => ({
          ...n,
          data: {
            ...n.data,
            isHighlighted: highlighted.has(n.id),
          },
        })),
      }
    }),

  mergeTraceResult: (result) => {
    const { nodes: existing, edges: existingEdges } = get()
    const existingQnames = new Set(existing.map((n) => n.id))
    const existingEdgeIds = new Set(existingEdges.map((e) => e.id))

    const newNodes: Node<SymbolNodeData>[] = Object.entries(result.nodes)
      .filter(([qname]) => !existingQnames.has(qname))
      .map(([qname, info]) => ({
        id: qname,
        type: "symbol",
        position: { x: 0, y: 0 }, // ELK will reposition
        data: {
          qname,
          name: qname.split(":").pop()?.split(".").pop() ?? qname,
          kind: "function" as const,
          filePath: qname.split(":")[0] + ".py",
          startLine: 0,
          endLine: 0,
          signature: info.signature,
          oneLiner: info.one_liner,
          isPublic: true,
          inboundCount: 0,
          outboundCount: 0,
          prose: null,
          isProseLoading: false,
          isExpanded: false,
          agentState: "idle" as AgentState,
          isSelected: false,
          isHighlighted: false,
        },
      }))

    const newEdges: Edge<EdgeData>[] = result.edges
      .filter((e) => {
        const id = `${e.from}->${e.to}`
        return !existingEdgeIds.has(id)
      })
      .map((e) => ({
        id: `${e.from}->${e.to}`,
        source: e.from,
        target: e.to,
        type: "semantic",
        data: { kind: "calls" as const },
      }))

    if (newNodes.length > 0 || newEdges.length > 0) {
      set((state) => ({
        nodes: [...state.nodes, ...newNodes],
        edges: [...state.edges, ...newEdges],
      }))
    }
  },
}))
