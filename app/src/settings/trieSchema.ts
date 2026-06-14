// Schema for the editable subset of trie.toml that the desktop app exposes in
// the "trie" section of Settings. Each field declares a dot-separated pointer
// into trie.toml (e.g. "sync.concurrency") so the merge-writer in the main
// process knows exactly which keys we manage. Keys not described here are never
// touched — hand edits to trie.toml are preserved.
//
// Mirrors trie/config.py (the authoritative dataclass defaults). The `default`
// here is shown as a placeholder/hint and used to decide whether a value is at
// trie's default (so we can clear the managed key rather than pin it). It is NOT
// written unless the user changes it.
//
// Scope: per-project <projectDir>/trie.toml.

export type TrieFieldType = "boolean" | "number" | "string" | "enum" | "stringList" | "json"

export interface TrieFieldDef {
  /** Dot-separated pointer into trie.toml (e.g. "models.bootstrap"). */
  pointer: string
  title: string
  description: string
  category: string
  type: TrieFieldType
  default: boolean | number | string | string[]
  enum?: { value: string; label: string }[]
  min?: number
  max?: number
  step?: number
  placeholder?: string
}

// Top-level trie.toml tables this app manages. The store sends only these as
// the merge delta; everything else in trie.toml is preserved untouched.
export const TRIE_MANAGED_TOP_KEYS = [
  "scope",
  "triefacts",
  "models",
  "cascade",
  "sync",
  "mcp",
  "debug",
  "edits",
] as const

export const TRIE_FIELDS: TrieFieldDef[] = [
  // ── Scope ───────────────────────────────────────────────────────────────
  {
    pointer: "scope.include",
    title: "Include Globs",
    description: "Glob patterns (relative to project root) for files trie indexes.",
    category: "Scope",
    type: "stringList",
    default: ["**/*.py"],
    placeholder: "**/*.py",
  },
  {
    pointer: "scope.exclude",
    title: "Exclude Globs",
    description: "Glob patterns to skip (vendored dirs, build output, optionally tests).",
    category: "Scope",
    type: "stringList",
    default: ["**/__pycache__/**", "**/.venv/**", "**/build/**", "**/dist/**"],
    placeholder: "**/tests/**",
  },

  // ── Triefacts ─────────────────────────────────────────────────────────────
  {
    pointer: "triefacts.root",
    title: "Triefacts Root",
    description: "Directory where the generated triefact tree lives, relative to project root.",
    category: "Triefacts",
    type: "string",
    default: "triefacts",
    placeholder: "triefacts",
  },
  {
    pointer: "triefacts.source_root",
    title: "Source Root",
    description: "Root of the source tree relative to trie.toml. '.' means project root.",
    category: "Triefacts",
    type: "string",
    default: ".",
    placeholder: ".",
  },

  // ── Models ────────────────────────────────────────────────────────────────
  {
    pointer: "models.bootstrap",
    title: "Bootstrap Model",
    description: "Model for the first full triefact generation pass (provider/model).",
    category: "Models",
    type: "string",
    default: "anthropic/claude-sonnet-4-6",
    placeholder: "anthropic/claude-sonnet-4-6",
  },
  {
    pointer: "models.cascade",
    title: "Cascade Model",
    description: "Model for incremental cascade re-syncs (provider/model).",
    category: "Models",
    type: "string",
    default: "anthropic/claude-sonnet-4-6",
    placeholder: "anthropic/claude-sonnet-4-6",
  },
  {
    pointer: "models.edits",
    title: "Edits Model",
    description: "Model for the patch-apply / edit-generation backend (provider/model).",
    category: "Models",
    type: "string",
    default: "anthropic/claude-sonnet-4-6",
    placeholder: "anthropic/claude-sonnet-4-6",
  },

  // ── Cascade ───────────────────────────────────────────────────────────────
  {
    pointer: "cascade.default_depth",
    title: "Default Depth",
    description: "Reference-graph traversal depth on incremental sync.",
    category: "Cascade",
    type: "number",
    default: 1,
    min: 0,
    max: 5,
    step: 1,
  },
  {
    pointer: "cascade.hub_symbol_threshold",
    title: "Hub Symbol Threshold",
    description:
      "Symbols with more inbound references than this are treated as depth-0 only, so utility hubs don't invalidate the world.",
    category: "Cascade",
    type: "number",
    default: 20,
    min: 1,
    step: 1,
  },
  {
    pointer: "cascade.max_judgments",
    title: "Max Judgments",
    description: "Hard cap on cascade pre-filter LLM calls per apply run.",
    category: "Cascade",
    type: "number",
    default: 50,
    min: 1,
    step: 1,
  },
  {
    pointer: "cascade.surface_unresolved",
    title: "Surface Unresolved",
    description: "Report second-order cascade as ApplyReport.unresolved rather than chasing it in-pipeline.",
    category: "Cascade",
    type: "boolean",
    default: true,
  },

  // ── Sync ──────────────────────────────────────────────────────────────────
  {
    pointer: "sync.concurrency",
    title: "Per-file Concurrency",
    description: "Parallel per-symbol LLM calls inside a single file's sync. 1 = serial.",
    category: "Sync",
    type: "number",
    default: 4,
    min: 1,
    max: 32,
    step: 1,
  },
  {
    pointer: "sync.file_workers",
    title: "File Workers",
    description: "How many files the scheduler generates concurrently.",
    category: "Sync",
    type: "number",
    default: 8,
    min: 1,
    max: 64,
    step: 1,
  },
  {
    pointer: "sync.max_inflight_requests",
    title: "Max Inflight Requests",
    description: "Process-wide cap on total concurrent LLM calls (the real throttle). 0 disables.",
    category: "Sync",
    type: "number",
    default: 8,
    min: 0,
    max: 128,
    step: 1,
  },
  {
    pointer: "sync.max_retries",
    title: "Max Retries",
    description: "Retry attempts for the model client on 429/529 before propagating the error.",
    category: "Sync",
    type: "number",
    default: 8,
    min: 0,
    max: 20,
    step: 1,
  },
  {
    pointer: "sync.retry_base_delay_seconds",
    title: "Retry Base Delay (s)",
    description: "Base delay for exponential backoff on rate limits.",
    category: "Sync",
    type: "number",
    default: 1.0,
    min: 0,
    step: 0.5,
  },
  {
    pointer: "sync.retry_cap_seconds",
    title: "Retry Cap (s)",
    description: "Maximum backoff delay between retries.",
    category: "Sync",
    type: "number",
    default: 60.0,
    min: 1,
    step: 5,
  },
  {
    pointer: "sync.request_timeout_seconds",
    title: "Request Timeout (s)",
    description: "Per-request timeout for a single LLM call before it's retried.",
    category: "Sync",
    type: "number",
    default: 120.0,
    min: 10,
    step: 10,
  },

  // ── MCP ───────────────────────────────────────────────────────────────────
  {
    pointer: "mcp.grep_max_limit",
    title: "grep — Max Limit",
    description: "Maximum hits a single grep call may return.",
    category: "MCP",
    type: "number",
    default: 50,
    min: 1,
    step: 5,
  },
  {
    pointer: "mcp.grep_one_liner_max_chars",
    title: "grep — One-liner Max Chars",
    description: "Truncate each grep hit's one-liner to this length.",
    category: "MCP",
    type: "number",
    default: 200,
    min: 20,
    step: 10,
  },
  {
    pointer: "mcp.grep_default_rank_by",
    title: "grep — Default Ranking",
    description: "How grep ranks results when no rank_by is supplied.",
    category: "MCP",
    type: "enum",
    default: "public_first",
    enum: [
      { value: "public_first", label: "Public first" },
      { value: "inbound_count", label: "Inbound count" },
      { value: "alphabetical", label: "Alphabetical" },
    ],
  },
  {
    pointer: "mcp.grep_fallback_max_files",
    title: "grep — Fallback Max Files",
    description: "Cap on in-scope files the rg-backed grep fallback walks.",
    category: "MCP",
    type: "number",
    default: 200,
    min: 10,
    step: 10,
  },
  {
    pointer: "mcp.grep_fallback_match_limit",
    title: "grep — Fallback Match Limit",
    description: "Cap on candidate symbols returned by the grep fallback.",
    category: "MCP",
    type: "number",
    default: 30,
    min: 1,
    step: 5,
  },
  {
    pointer: "mcp.fuzzy_cutoff",
    title: "Fuzzy Cutoff",
    description: "Minimum rapidfuzz score (0-100) for a fuzzy hit to be included.",
    category: "MCP",
    type: "number",
    default: 45,
    min: 0,
    max: 100,
    step: 5,
  },
  {
    pointer: "mcp.read_max_neighbours_per_direction",
    title: "read — Max Neighbours / Direction",
    description: "Cap callers/callees shown per direction in read. 0 = unlimited.",
    category: "MCP",
    type: "number",
    default: 0,
    min: 0,
    step: 1,
  },
  {
    pointer: "mcp.read_prose_max_chars",
    title: "read — Prose Max Chars",
    description: "Truncate prose returned by read. 0 = unlimited.",
    category: "MCP",
    type: "number",
    default: 0,
    min: 0,
    step: 100,
  },
  {
    pointer: "mcp.trace_max_depth",
    title: "trace — Max Depth",
    description: "Maximum hop depth a trace may expand.",
    category: "MCP",
    type: "number",
    default: 5,
    min: 1,
    max: 20,
    step: 1,
  },
  {
    pointer: "mcp.trace_hub_threshold",
    title: "trace — Hub Threshold",
    description: "Skip expanding symbols with more inbound refs than this during trace.",
    category: "MCP",
    type: "number",
    default: 50,
    min: 1,
    step: 5,
  },
  {
    pointer: "mcp.trace_max_nodes",
    title: "trace — Max Nodes",
    description: "Cap total nodes a trace may visit.",
    category: "MCP",
    type: "number",
    default: 200,
    min: 10,
    step: 10,
  },

  // ── Edits ─────────────────────────────────────────────────────────────────
  {
    pointer: "edits.backend",
    title: "Edit Backend",
    description: "Per-symbol edit generation backend.",
    category: "Edits",
    type: "enum",
    default: "llm",
    enum: [
      { value: "llm", label: "LLM (in-process)" },
      { value: "opencode", label: "opencode (per-symbol)" },
    ],
  },
  {
    pointer: "edits.commit_mode",
    title: "Commit Mode",
    description: "How a multi-item apply commits on partial failure.",
    category: "Edits",
    type: "enum",
    default: "all_or_nothing",
    enum: [
      { value: "all_or_nothing", label: "All or nothing" },
      { value: "per_item", label: "Per item" },
      { value: "per_group", label: "Per group" },
    ],
  },
  {
    pointer: "edits.lsp_max_retries",
    title: "LSP Max Retries",
    description: "Diagnostic-driven fixup attempts during patch apply.",
    category: "Edits",
    type: "number",
    default: 3,
    min: 0,
    max: 10,
    step: 1,
  },
  {
    pointer: "edits.compile_retry_cap",
    title: "Compile Retry Cap",
    description: "Regeneration attempts for a symbol whose generated source won't compile.",
    category: "Edits",
    type: "number",
    default: 2,
    min: 0,
    max: 10,
    step: 1,
  },
  {
    pointer: "edits.lsp_backends",
    title: "LSP Backends",
    description:
      "Ordered list of language-server / checker backends for source diagnostics. Each entry: {command, check_args?, output_format?, exit_ok_codes?}.",
    category: "Edits",
    type: "json",
    default: "",
  },

  // ── Debug ─────────────────────────────────────────────────────────────────
  {
    pointer: "debug.enabled",
    title: "Telemetry Enabled",
    description: "Append-only JSONL telemetry for trie's own operations. Off by default.",
    category: "Debug",
    type: "boolean",
    default: false,
  },
  {
    pointer: "debug.log_path",
    title: "Log Path",
    description: "Where the debug.jsonl is written, relative to project root or absolute.",
    category: "Debug",
    type: "string",
    default: "debug.jsonl",
    placeholder: "debug.jsonl",
  },
  {
    pointer: "debug.log_to_stderr",
    title: "Log to stderr",
    description: "Mirror telemetry events to stderr (dev only; noisy).",
    category: "Debug",
    type: "boolean",
    default: false,
  },
  {
    pointer: "debug.capture_args",
    title: "Capture Tool Args",
    description: "Include MCP tool arguments in mcp_call telemetry events.",
    category: "Debug",
    type: "boolean",
    default: true,
  },
  {
    pointer: "debug.capture_responses",
    title: "Capture Responses",
    description: "Include full response bodies in telemetry (large; off by default).",
    category: "Debug",
    type: "boolean",
    default: false,
  },
  {
    pointer: "debug.redact_keys",
    title: "Redact Keys",
    description: "Field paths to elide from telemetry, e.g. args.predicate.",
    category: "Debug",
    type: "stringList",
    default: [],
    placeholder: "args.predicate",
  },
]

export const TRIE_CATEGORIES = Array.from(new Set(TRIE_FIELDS.map((f) => f.category)))

export function trieFieldDef(pointer: string): TrieFieldDef | undefined {
  return TRIE_FIELDS.find((f) => f.pointer === pointer)
}
