// Schema for the editable subset of opencode.json that the desktop app exposes
// in the "opencode" section of Settings. Each field declares a JSON pointer
// (top-level key, dot-separated for nesting) into opencode.json so the
// merge-writer in the main process knows exactly which keys we manage. Keys not
// described here are never touched — hand edits to opencode.json are preserved.
//
// Deliberately excluded:
//   - everything in tui.json (we run `opencode serve`, not the TUI)
//   - mcp.trie (managed automatically; rendered read-only in the MCP editor)
//   - deprecated keys (mode, autoshare, layout, maxSteps)
//
// Scope: per-project <projectDir>/.opencode/opencode.json (matches where the
// app already injects the trie MCP entry).

export type OcFieldType =
  | "boolean"
  | "number"
  | "string"
  | "enum"
  | "stringList" // string[] — instructions, watcher.ignore, cors, provider lists
  | "enumMap" // { key: oneOf(enum) } — permission matrix
  | "toggleMap" // { key: boolean } — tools on/off
  | "providerList" // provider.* with Keychain-backed apiKey
  | "mcpList" // mcp.* (local/remote)
  | "agentTable" // agent.* sub-editor
  | "json" // arbitrary blob edited as JSONC (experimental, policies)

export interface OcFieldDef {
  /** JSON pointer into opencode.json, dot-separated (e.g. "attachment.image.max_width"). */
  pointer: string
  title: string
  description: string
  category: string
  type: OcFieldType
  /** Whether changing this requires restarting the opencode server to take effect. */
  restart?: boolean
  enum?: { value: string; label: string }[]
  /** For enumMap: the keys (rows) and the choices each can take. */
  mapKeys?: string[]
  mapChoices?: { value: string; label: string }[]
  /** For toggleMap: the keys to render. */
  toggleKeys?: string[]
  min?: number
  max?: number
  step?: number
  placeholder?: string
}

const PERMISSION_TOOLS = [
  "read",
  "edit",
  "glob",
  "grep",
  "list",
  "bash",
  "task",
  "webfetch",
  "websearch",
  "skill",
]

const PERMISSION_CHOICES = [
  { value: "allow", label: "Allow" },
  { value: "ask", label: "Ask" },
  { value: "deny", label: "Deny" },
]

export const OC_FIELDS: OcFieldDef[] = [
  // ── Model ─────────────────────────────────────────────────────────────────
  {
    pointer: "model",
    title: "Default Model",
    description: "Primary model for agent turns, as provider/model (e.g. anthropic/claude-sonnet-4-5).",
    category: "Model",
    type: "string",
    restart: true,
    placeholder: "anthropic/claude-sonnet-4-5",
  },
  {
    pointer: "small_model",
    title: "Small Model",
    description: "Cheaper model for lightweight tasks like title generation.",
    category: "Model",
    type: "string",
    restart: true,
    placeholder: "anthropic/claude-haiku-4-5",
  },
  {
    pointer: "default_agent",
    title: "Default Agent",
    description: "Primary agent used when none is specified (e.g. build, plan).",
    category: "Model",
    type: "string",
    placeholder: "build",
  },
  {
    pointer: "enabled_providers",
    title: "Enabled Providers",
    description: "Allowlist — when set, ONLY these providers are loaded. Leave empty for all.",
    category: "Model",
    type: "stringList",
    restart: true,
    placeholder: "anthropic",
  },
  {
    pointer: "disabled_providers",
    title: "Disabled Providers",
    description: "Providers to never load, even if credentials are present. Takes priority over the allowlist.",
    category: "Model",
    type: "stringList",
    restart: true,
    placeholder: "openai",
  },

  // ── Permissions ─────────────────────────────────────────────────────────────
  {
    pointer: "permission",
    title: "Tool Permissions",
    description: "Require approval per tool. Allow runs freely, Ask prompts you, Deny blocks the tool.",
    category: "Permissions",
    type: "enumMap",
    mapKeys: PERMISSION_TOOLS,
    mapChoices: PERMISSION_CHOICES,
  },
  {
    pointer: "tools",
    title: "Enabled Tools",
    description: "Turn individual built-in tools on or off for the model.",
    category: "Permissions",
    type: "toggleMap",
    toggleKeys: ["write", "edit", "bash", "read", "grep", "glob", "webfetch", "task"],
  },

  // ── Context ─────────────────────────────────────────────────────────────────
  {
    pointer: "instructions",
    title: "Instruction Files",
    description: "Extra instruction files / globs to include (e.g. CONTRIBUTING.md, .cursor/rules/*.md).",
    category: "Context",
    type: "stringList",
    placeholder: "docs/guidelines.md",
  },
  {
    pointer: "compaction.auto",
    title: "Auto Compaction",
    description: "Automatically compact the session when the context window fills up.",
    category: "Context",
    type: "boolean",
  },
  {
    pointer: "compaction.prune",
    title: "Prune Old Tool Output",
    description: "Drop old tool outputs during compaction to save tokens.",
    category: "Context",
    type: "boolean",
  },
  {
    pointer: "compaction.reserved",
    title: "Compaction Reserved Tokens",
    description: "Token buffer left free so compaction doesn't overflow the window.",
    category: "Context",
    type: "number",
    min: 0,
    step: 1000,
  },
  {
    pointer: "tool_output.max_lines",
    title: "Tool Output Max Lines",
    description: "Lines of tool output before it is truncated to disk (default 2000).",
    category: "Context",
    type: "number",
    min: 1,
    step: 100,
  },
  {
    pointer: "tool_output.max_bytes",
    title: "Tool Output Max Bytes",
    description: "Bytes of tool output before truncation (default 51200).",
    category: "Context",
    type: "number",
    min: 1,
    step: 1024,
  },
  {
    pointer: "attachment.image.auto_resize",
    title: "Auto-resize Images",
    description: "Resize oversized image attachments instead of rejecting them.",
    category: "Context",
    type: "boolean",
  },
  {
    pointer: "attachment.image.max_width",
    title: "Image Max Width",
    description: "Maximum image width (px) before resize/reject (default 2000).",
    category: "Context",
    type: "number",
    min: 1,
    step: 100,
  },
  {
    pointer: "attachment.image.max_height",
    title: "Image Max Height",
    description: "Maximum image height (px) before resize/reject (default 2000).",
    category: "Context",
    type: "number",
    min: 1,
    step: 100,
  },

  // ── Providers ───────────────────────────────────────────────────────────────
  {
    pointer: "provider",
    title: "Providers",
    description:
      "Custom provider settings. API keys are stored in the system Keychain and injected as environment variables — never written to opencode.json.",
    category: "Providers",
    type: "providerList",
    restart: true,
  },

  // ── Integrations ─────────────────────────────────────────────────────────────
  {
    pointer: "mcp",
    title: "MCP Servers",
    description: "Model Context Protocol servers. The bundled trie server is managed automatically.",
    category: "Integrations",
    type: "mcpList",
    restart: true,
  },
  {
    pointer: "lsp",
    title: "Enable LSP Servers",
    description: "Turn on built-in language servers for richer code intelligence.",
    category: "Integrations",
    type: "boolean",
    restart: true,
  },
  {
    pointer: "formatter",
    title: "Enable Formatters",
    description: "Turn on built-in code formatters (prettier, etc.).",
    category: "Integrations",
    type: "boolean",
    restart: true,
  },
  {
    pointer: "plugin",
    title: "Plugins",
    description: "npm plugin packages to load (e.g. @my-org/custom-plugin).",
    category: "Integrations",
    type: "stringList",
    restart: true,
    placeholder: "opencode-helicone-session",
  },

  // ── Agents ──────────────────────────────────────────────────────────────────
  {
    pointer: "agent",
    title: "Agents",
    description: "Per-agent overrides: model, prompt, mode, and behavior.",
    category: "Agents",
    type: "agentTable",
  },

  // ── Behavior ─────────────────────────────────────────────────────────────────
  {
    pointer: "share",
    title: "Sharing",
    description: "Conversation sharing behavior.",
    category: "Behavior",
    type: "enum",
    enum: [
      { value: "manual", label: "Manual" },
      { value: "auto", label: "Automatic" },
      { value: "disabled", label: "Disabled" },
    ],
  },
  {
    pointer: "autoupdate",
    title: "Auto Update",
    description: "Automatically update opencode on startup.",
    category: "Behavior",
    type: "enum",
    enum: [
      { value: "true", label: "On" },
      { value: "false", label: "Off" },
      { value: "notify", label: "Notify only" },
    ],
  },
  {
    pointer: "snapshot",
    title: "Snapshots",
    description: "Track file changes so agent edits can be undone/reverted. Disable for huge repos.",
    category: "Behavior",
    type: "boolean",
    restart: true,
  },
  {
    pointer: "shell",
    title: "Shell",
    description: "Shell used for the terminal and bash tool (absolute path or short name).",
    category: "Behavior",
    type: "string",
    restart: true,
    placeholder: "/bin/zsh",
  },
  {
    pointer: "username",
    title: "Username",
    description: "Custom name shown in conversations instead of your system username.",
    category: "Behavior",
    type: "string",
  },
  {
    pointer: "watcher.ignore",
    title: "File Watcher Ignore",
    description: "Glob patterns to exclude from file watching (e.g. node_modules/**).",
    category: "Behavior",
    type: "stringList",
    restart: true,
    placeholder: "dist/**",
  },
  {
    pointer: "logLevel",
    title: "Log Level",
    description: "Verbosity of opencode logs.",
    category: "Behavior",
    type: "enum",
    restart: true,
    enum: [
      { value: "", label: "Default" },
      { value: "DEBUG", label: "Debug" },
      { value: "INFO", label: "Info" },
      { value: "WARN", label: "Warn" },
      { value: "ERROR", label: "Error" },
    ],
  },

  // ── Advanced ─────────────────────────────────────────────────────────────────
  {
    pointer: "server.port",
    title: "Server Port",
    description: "Port opencode serve listens on. The desktop app manages this automatically; override with care.",
    category: "Advanced",
    type: "number",
    restart: true,
    min: 1,
    max: 65535,
  },
  {
    pointer: "server.hostname",
    title: "Server Hostname",
    description: "Hostname opencode serve binds to.",
    category: "Advanced",
    type: "string",
    restart: true,
    placeholder: "127.0.0.1",
  },
  {
    pointer: "experimental",
    title: "Experimental",
    description:
      "Unstable options edited as raw JSON (batch_tool, openTelemetry, mcp_timeout, continue_loop_on_deny, policies). May change without notice.",
    category: "Advanced",
    type: "json",
    restart: true,
  },
]

export const OC_CATEGORIES = Array.from(new Set(OC_FIELDS.map((f) => f.category)))

export function ocFieldByPointer(pointer: string): OcFieldDef | undefined {
  return OC_FIELDS.find((f) => f.pointer === pointer)
}

/** The top-level opencode.json keys this app manages (used by the merge writer). */
export const MANAGED_TOP_KEYS = Array.from(
  new Set(OC_FIELDS.map((f) => f.pointer.split(".")[0])),
)

/** Fixed provider → env var name map for Keychain-injected API keys.
 *  Each provider can override this in the provider editor. */
export const PROVIDER_ENV_DEFAULTS: Record<string, string> = {
  anthropic: "ANTHROPIC_API_KEY",
  openai: "OPENAI_API_KEY",
  "google": "GOOGLE_GENERATIVE_AI_API_KEY",
  gemini: "GOOGLE_GENERATIVE_AI_API_KEY",
  groq: "GROQ_API_KEY",
  openrouter: "OPENROUTER_API_KEY",
  mistral: "MISTRAL_API_KEY",
  deepseek: "DEEPSEEK_API_KEY",
  xai: "XAI_API_KEY",
}

export function defaultEnvVar(provider: string): string {
  return PROVIDER_ENV_DEFAULTS[provider] ?? `${provider.toUpperCase().replace(/[^A-Z0-9]/g, "_")}_API_KEY`
}
