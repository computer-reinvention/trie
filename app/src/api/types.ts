// Shared TypeScript types mirroring the trie Python data model
// and the opencode desktop event protocol.

export type SymbolKind = "function" | "class" | "method" | "constant" | "module"
export type AgentState = "idle" | "reading" | "writing" | "scanning" | "stale"

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

// File triefact — full triefact document for one source file.
// Mirrors TrieTools.file_triefact() in trie/mcp_server.py.
export interface TriefactSection {
  qname: string
  kind: string
  role: string
  body: string
  one_liner: string
  fingerprint: string
  body_fingerprint: string
  start_line: number
  end_line: number
}

export interface FileTriefactResult {
  file_path: string
  triefact_path: string
  exists: boolean
  front_matter: Record<string, unknown>
  sections: TriefactSection[]
}

// File source — raw source text for the editor source view.
// Mirrors the /desktop/graph/file-source endpoint.
export interface FileSourceResult {
  path: string
  type: "text" | "binary" | "image" | "patch"
  content: string
}

// Live activity — writer status + working-tree stale set.
// Mirrors TrieTools.activity() in trie/mcp_server.py.
export interface ActivityStatus {
  state: "idle" | "scanning" | "syncing" | "refreshing" | "error"
  op: string
  pid: number
  is_active: boolean
  current_file: string | null
  done: number
  total: number
  error: string | null
  updated_at: number
}

export interface ActivityPending {
  count: number
  stale: string[]
  head: string
  computed_at: number
}

export interface ActivityResult {
  status: ActivityStatus
  pending: ActivityPending | null
}

// ---------------------------------------------------------------------------
// opencode session + message model (mirrors packages/opencode message-v2.ts)
// ---------------------------------------------------------------------------

export interface OpencodeSession {
  id: string
  title?: string
  directory?: string
  parentID?: string
  time?: { created?: number; updated?: number }
  // opencode returns more; we only type what the UI uses.
  [k: string]: unknown
}

// A message's `info` — discriminated on role.
export interface OpencodeUserInfo {
  id: string
  sessionID: string
  role: "user"
  time: { created: number }
  agent?: string
  model?: { providerID: string; modelID: string }
}

export interface OpencodeTokens {
  total?: number
  input: number
  output: number
  reasoning: number
  cache: { read: number; write: number }
}

export interface OpencodeAssistantInfo {
  id: string
  sessionID: string
  role: "assistant"
  time: { created: number; completed?: number }
  parentID?: string
  modelID?: string
  providerID?: string
  agent?: string
  cost?: number
  tokens?: OpencodeTokens
  finish?: string
  error?: { name?: string; message?: string; statusCode?: number; isRetryable?: boolean }
}

export type OpencodeMessageInfo = OpencodeUserInfo | OpencodeAssistantInfo

// Parts — discriminated on `type`. Only the fields the transcript renders.
export interface TextPart {
  id: string
  type: "text"
  text: string
  synthetic?: boolean
  ignored?: boolean
}
export interface ReasoningPart {
  id: string
  type: "reasoning"
  text: string
}
export type ToolPartStatus = "pending" | "running" | "completed" | "error"
export interface ToolPart {
  id: string
  type: "tool"
  callID: string
  tool: string
  state: {
    status: ToolPartStatus
    input?: Record<string, unknown>
    output?: string
    error?: string
    title?: string
    time?: { start?: number; end?: number }
    metadata?: Record<string, unknown>
  }
}
export interface FilePartT {
  id: string
  type: "file"
  mime: string
  filename?: string
  url: string
}
export interface PatchPartT {
  id: string
  type: "patch"
  hash: string
  files: string[]
}
export interface GenericPart {
  id: string
  type: string
  [k: string]: unknown
}

export type OpencodePart = TextPart | ReasoningPart | ToolPart | FilePartT | PatchPartT | GenericPart

export interface OpencodeMessage {
  info: OpencodeMessageInfo
  parts: OpencodePart[]
}

// Permission request (mirrors permission/index.ts Request).
export type PermissionReply = "once" | "always" | "reject"
export interface PermissionRequest {
  id: string
  sessionID: string
  permission: string
  patterns: string[]
  metadata: Record<string, unknown>
  always: string[]
  // correlation to the originating tool call
  callID?: string
  messageID?: string
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

export interface DesktopReasoningDeltaEvent {
  sessionID: string
  messageID: string
  partID: string
  delta: string
}

// Full message-info upsert (cost/tokens/finish/error) — desktop.message.updated
export interface DesktopMessageUpdatedEvent {
  sessionID: string
  info: OpencodeMessageInfo
}

// Full part upsert — desktop.part.updated (carries the whole part)
export interface DesktopPartUpdatedEvent {
  sessionID: string
  messageID: string
  part: OpencodePart
}

export interface DesktopPermissionAskedEvent {
  id: string
  sessionID: string
  permission: string
  patterns: string[]
  metadata: Record<string, unknown>
  always: string[]
  callID?: string
  messageID?: string
}

export interface DesktopPermissionRepliedEvent {
  sessionID: string
  requestID: string
  reply: PermissionReply
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
