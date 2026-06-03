// Shared TypeScript types mirroring the trie Python data model
// and the opencode desktop event protocol.

export type SymbolKind = "function" | "class" | "method" | "constant" | "module"
export type AgentState = "idle" | "reading" | "writing" | "stale"

export interface SymbolHit {
  qname: string
  name: string
  kind: SymbolKind
  file_path: string
  start_line: number
  signature: string | null
  is_public: boolean
  inbound_count: number
  outbound_count: number
  one_liner: string
  pending_patch_count: number
  has_pending_patches: boolean
}

export interface ReadResult {
  qname: string
  signature: string
  prose: string
  source_pointer: string
  callers: CallerCallee[]
  callees: CallerCallee[]
  has_pending_patches: boolean
  notes?: string[]
}

export interface CallerCallee {
  qname: string
  signature: string
  one_liner: string
}

export interface TraceResult {
  root: { qname: string; signature: string; one_liner: string }
  nodes: Record<string, { signature: string; one_liner: string }>
  edges: TraceEdge[]
  truncated_at?: string[]
  notes?: string[]
}

export interface TraceEdge {
  from: string
  to: string
  direction: "in" | "out"
}

// ---------------------------------------------------------------------------
// System model — the high-level "model of the system" the graph view renders.
// Mirrors trie/graph/system_model.py system_model_to_dict().
// ---------------------------------------------------------------------------

export type NodeClass =
  | "door"
  | "hub"
  | "bedrock"
  | "exit"
  | "internal"
  | "normal"
  | "orphan"
  | "test"

export interface SystemModelNode {
  qname: string
  name: string
  kind: SymbolKind
  file_path: string
  role: string
  boundary: string
  subsystem: string
  is_public: boolean
  is_test: boolean
  inbound_count: number
  outbound_count: number
  prod_inbound_count: number
  cls: NodeClass
  salience: number
  betweenness: number
  depth: number
  community: number
  one_liner: string
  x: number
  y: number
}

export interface GroupSummary {
  key: string
  count: number
  door_count: number
  hub_count: number
}

export interface GroupFlow {
  source: string
  target: string
  weight: number
}

export interface ComponentAxis {
  axis: "role" | "subsystem"
  groups: GroupSummary[]
  flows: GroupFlow[]
}

export interface SystemModel {
  nodes: SystemModelNode[]
  axes: { role: ComponentAxis; subsystem: ComponentAxis }
  landmarks: string[]
  stats: {
    production_nodes: number
    test_nodes: number
    edges: number
    class_counts: Record<string, number>
    role_count: number
    subsystem_count: number
  }
}

export type GroupingAxis = "role" | "subsystem"

export interface ProjectSummary {
  project_name: string
  project_root: string
  total_symbols: number
  public_symbols: number
  total_files: number
  total_edges: number
  trie_version: string
}

export interface SymbolsByFileResult {
  file_path: string
  symbols: SymbolHit[]
}

// Desktop SSE event types
export interface DesktopEvent {
  id: string
  type: string
  properties: Record<string, unknown>
}

export interface DesktopToolStartEvent {
  sessionID: string
  messageID: string
  partID: string
  callID: string
  tool: string
  input: Record<string, unknown>
  time: { start: number }
}

export interface DesktopToolDoneEvent {
  sessionID: string
  messageID: string
  partID: string
  callID: string
  tool: string
  input: Record<string, unknown>
  output: string | null
  error: string | null
  time: { start: number; end: number }
}

export interface DesktopTextDeltaEvent {
  sessionID: string
  messageID: string
  partID: string
  delta: string
}

export interface DesktopSessionStatusEvent {
  sessionID: string
  status: { type: "running" | "idle" | "error"; error?: string }
}

export interface DesktopFileEditedEvent {
  file: string
}

// Graph node data — stored in React Flow node.data
// Index signature required by React Flow v12's Record<string, unknown> constraint.
export interface SymbolNodeData extends Record<string, unknown> {
  qname: string
  name: string
  kind: SymbolKind
  filePath: string
  startLine: number
  endLine: number
  signature: string | null
  oneLiner: string
  isPublic: boolean
  inboundCount: number
  outboundCount: number
  prose: string | null // null = not yet loaded
  isProseLoading: boolean
  isExpanded: boolean
  agentState: AgentState
  isSelected: boolean
  isHighlighted: boolean
}

export interface EdgeData extends Record<string, unknown> {
  kind: "calls" | "imports" | "inherits"
}

// Turn history
export interface TurnEvent {
  id: string
  type: "tool_call" | "tool_result"
  tool: string
  input?: Record<string, unknown>
  output?: string
  error?: string | null
  timestamp: number
  durationMs?: number
}
