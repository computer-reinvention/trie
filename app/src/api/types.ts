// Shared TypeScript types mirroring the trie Python data model
// and the opencode desktop event protocol.

export type SymbolKind = "function" | "class" | "method" | "constant" | "module"
export type AgentState =
  | "idle"
  | "reading"
  | "writing"
  | "scanning"
  | "cascade"
  | "stale"
  | "error"

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

// ---------------------------------------------------------------------------
// Patch / cascade editing model (mirrors docs/cascade-editing-plan.md).
// Fields beyond the current backend (kind, blast_radius, cascade) are optional
// so the UI renders today's patch_list and lights up extra detail as it lands.
// ---------------------------------------------------------------------------

export type PatchKind = "modify" | "create" | "delete" | "rename"
export type PatchOrigin = "agent" | "cascade" | "mixed"

export interface PatchNote {
  note?: string
  reason?: string
  session_id?: string
  created_at?: number
}

export interface BlastRadius {
  direct: number
  cascade: number
  cascade_count: number
  hubs_stopped_at: string[]
}

// Full blast-radius result from /desktop/graph/blast-radius (real compute_cascade).
export interface CascadeImpactNode {
  qname: string
  hop: number
  file: string
}
export interface BlastRadiusResult {
  qname: string
  file: string
  direct: number
  cascade: CascadeImpactNode[]
  cascade_count: number
  hubs_stopped_at: string[]
}

// One symbol's pending patches (grouped), as returned by patch_list.
export interface PatchEntry {
  qname: string
  count: number
  origin: PatchOrigin
  notes: PatchNote[]
  // cascade-plan extensions (optional until the pipeline lands)
  kind?: PatchKind
  rename_to?: string
  blast_radius?: BlastRadius
}

export interface PatchList {
  patches: PatchEntry[]
  // cascade-plan extensions
  session_note?: string
  apply_in_progress?: boolean
}

// Live apply progress (cascade-plan: activity().apply sub-object).
export interface ApplyProgress {
  phase: string // "merge" | "generate" | "fixup" | "commit" | ...
  done: number
  total: number
  session_note?: string
}

// The hand-off artifact from commit() (cascade-plan §9).
export interface ApplyReport {
  ok: boolean
  session_note?: string
  applied?: {
    symbols: number
    files: number
    files_detail?: Array<{ path: string; ok: boolean; symbols: number; lsp_iterations?: number }>
  }
  cascade_applied?: Array<{ qname: string; note?: string; origin?: PatchOrigin }>
  unresolved?: Array<{
    qname: string
    stage?: string
    code?: string
    message?: string
    source_pointer?: string
    repatch?: { tool: string; args: Record<string, unknown> }
  }>
  totals?: { requested: number; applied: number; unresolved: number }
  // current backend (patch_apply) returns a looser shape; keep it open
  applied_count?: number
  failed?: number
  error?: { code?: string; message?: string }
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

// ---------------------------------------------------------------------------
// AGM (Attention Gravity Map) contracts — mirrors trie/attention.py.
// Keep the numeric constants in sync with the Python source of truth.
//
// There are TWO masses, never conflated:
//   - liveMass: in-memory session signal, continuous wall-clock decay
//     (per-event-type half-lives), drives the visual. Never persisted.
//   - historicalMass: long-term cognitive-importance signal stamped into the
//     triefact (hist_mass=<v>@<ts>), 21-day half-life, updated only at sync.
//     NOT "old live mass" — it answers "how often does cognition return here
//     across investigations?".
// Both are log-compressed for display (displayMass). Mass is never dampened.
// ---------------------------------------------------------------------------

export type AttentionEventType = "grep" | "read" | "trace" | "write"

// Per-event live-mass weights (PRD §Event Interpretation).
export const EVENT_WEIGHTS: Record<AttentionEventType, number> = {
  grep: 10,
  read: 40,
  trace: 80,
  write: 80,
}

// Per-event-type live half-lives (seconds).
export const LIVE_HALFLIFE_SECONDS: Record<AttentionEventType, number> = {
  grep: 30,
  read: 180,
  trace: 600,
  write: 600,
}

// Historical mass half-life (seconds): 21 days.
export const HISTORICAL_HALFLIFE_SECONDS = 21 * 24 * 60 * 60

export function liveLambda(type: AttentionEventType): number {
  return Math.LN2 / LIVE_HALFLIFE_SECONDS[type]
}

export const HISTORICAL_LAMBDA = Math.LN2 / HISTORICAL_HALFLIFE_SECONDS

// Logarithmic compression for rendering; raw mass is unbounded.
export function displayMass(rawMass: number): number {
  return Math.log(Math.max(0, rawMass) + 1)
}

// Repository-graph edge kinds (depends_on deferred — see attention.py).
export type RepoEdgeKind =
  | "calls"
  | "references"
  | "imports"
  | "contains"
  | "inherits"
  | "implements"

export const ATTENTION_EDGE_KIND = "trace"
export const DEFAULT_EDGE_KIND: RepoEdgeKind = "calls"

// Propagation weights per edge kind (PRD §Edge Weights). One weak hop only.
export const EDGE_WEIGHTS: Record<string, number> = {
  trace: 1.0,
  calls: 1.0,
  inherits: 0.9,
  implements: 0.8,
  references: 0.7,
  imports: 0.5,
  contains: 0.2,
}

export const PROPAGATION_FACTOR = 0.15
export const PROPAGATION_HOPS = 1

export function edgeWeight(kind: string): number {
  return EDGE_WEIGHTS[kind] ?? EDGE_WEIGHTS.calls
}

// Synthetic non-code cognition surfaces. Live in the AGM layer only.
export type SyntheticNode = "Filesystem" | "Bash" | "Web" | "Database" | "Git"

export const SYNTHETIC_NODES: readonly SyntheticNode[] = [
  "Filesystem",
  "Bash",
  "Web",
  "Database",
  "Git",
]

export const SYNTHETIC_QNAME_PREFIX = "agm:synthetic/"

export function syntheticQname(node: SyntheticNode): string {
  return `${SYNTHETIC_QNAME_PREFIX}${node}`
}

export function isSyntheticQname(qname: string): boolean {
  return qname.startsWith(SYNTHETIC_QNAME_PREFIX)
}

// One unit of agent attention on a target (symbol qname or synthetic qname).
export interface AttentionEvent {
  ts: number
  eventType: AttentionEventType
  target: string
  weight: number
  agentId?: string
  sessionId?: string
  investigationId?: string
}

// Typed call-graph edge (mirrors the extended all_edges shape).
export interface TypedEdge {
  from: string
  to: string
  kind: RepoEdgeKind
}

// Investigations — explicit, first-class spans of agent cognition.
export type InvestigationStatus = "active" | "resolved" | "abandoned" | "superseded"

export interface Investigation {
  id: string
  label: string
  status: InvestigationStatus
  createdAt: number
  agentId?: string
  sessionId?: string
  // Derived live in the app: concentration of attention (0..1) + symbol scope.
  confidence: number
  scope: string[]
  negativeEvidence: string[]
}

// Per-node live attention state held by the AGM engine (in-memory only).
export interface AttentionState {
  liveMass: number
  historicalMass: number
}
