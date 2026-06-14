// Declarative definitions of the trie lifecycle commands the IDE can run, with
// their user-tunable flags. The command panel renders these; the command store
// turns a selection into the actual argv passed to trie-cli.

export type FlagType = "boolean" | "number" | "string" | "enum"

export interface CommandFlag {
  /** The CLI flag, e.g. "--all" (booleans) or "--limit" (value flags). */
  flag: string
  /** Form key, used as React key + state key. */
  key: string
  label: string
  description: string
  type: FlagType
  default?: boolean | number | string
  enum?: { value: string; label: string }[]
  placeholder?: string
  min?: number
  step?: number
}

export interface CommandDef {
  /** trie subcommand. */
  command: string
  title: string
  description: string
  /** Whether this command makes paid LLM calls (shown as a cost warning). */
  costly?: boolean
  /** Emit --json and parse JSONL events (drives a structured progress view). */
  json?: boolean
  /** Args always passed, regardless of the flag form (e.g. init's
   *  --no-install-hooks: the desktop drives refresh, so a git hook is never
   *  wanted). Prepended before the user-selected flags. */
  fixedArgs?: string[]
  flags: CommandFlag[]
}

export const TRIE_COMMANDS: CommandDef[] = [
  {
    command: "init",
    title: "Init",
    description:
      "Create trie.toml, update .gitignore, and build the symbol graph. Run once per project. The desktop drives refresh itself, so the git pre-commit hook is left off.",
    // `init --scan` populates the graph but never calls the LLM — scanning is free.
    fixedArgs: ["--no-install-hooks"],
    flags: [
      {
        flag: "--force",
        key: "force",
        label: "Force overwrite",
        description: "Overwrite an existing trie.toml and skip Python-project detection.",
        type: "boolean",
        default: false,
      },
      {
        flag: "--no-scan",
        key: "noScan",
        label: "Skip initial scan",
        description: "Write config only; don't build the graph yet (build later with Refresh).",
        type: "boolean",
        default: false,
      },
    ],
  },
  {
    command: "refresh",
    title: "Refresh",
    description:
      "Bring the graph + triefacts up to date with the working tree. Graph-only and fast by default; the freshness gate.",
    json: true,
    flags: [
      {
        flag: "--before-turn",
        key: "beforeTurn",
        label: "Before-turn gate",
        description: "Cheap pre-turn freshness gate (no-op unless HEAD/mtimes moved).",
        type: "boolean",
        default: false,
      },
      {
        flag: "--sync",
        key: "sync",
        label: "Sync prose inline",
        description: "Regenerate drifted triefact prose inline (makes LLM calls).",
        type: "boolean",
        default: false,
      },
      {
        flag: "--model",
        key: "model",
        label: "Model override",
        description: "Override the configured model (only used if refresh fires a sync).",
        type: "string",
        placeholder: "anthropic/claude-sonnet-4-6",
      },
    ],
  },
  {
    command: "sync",
    title: "Sync",
    description: "Generate or refresh triefacts. Auto-detects first-run bootstrap vs incremental cascade.",
    costly: true,
    flags: [
      {
        flag: "--all",
        key: "all",
        label: "Full re-pass",
        description: "Force a full re-pass of every in-scope file.",
        type: "boolean",
        default: false,
      },
      {
        flag: "--limit",
        key: "limit",
        label: "File limit",
        description: "Cap the number of files synced.",
        type: "number",
        min: 1,
        step: 1,
        placeholder: "10",
      },
      {
        flag: "--budget",
        key: "budget",
        label: "USD budget",
        description: "Stop once cumulative actual cost reaches this.",
        type: "number",
        min: 0,
        step: 0.5,
        placeholder: "2.00",
      },
      {
        flag: "--metadata-only",
        key: "metadataOnly",
        label: "Metadata only",
        description: "Refresh front matter from the live store; no LLM, no section changes.",
        type: "boolean",
        default: false,
      },
      {
        flag: "--roles-only",
        key: "rolesOnly",
        label: "Roles only",
        description: "Re-infer architectural role tags without regenerating prose.",
        type: "boolean",
        default: false,
      },
      {
        flag: "--model",
        key: "model",
        label: "Model override",
        description: "Override the configured model for this run.",
        type: "string",
        placeholder: "anthropic/claude-sonnet-4-6",
      },
    ],
  },
  {
    command: "plan",
    title: "Plan",
    description:
      "Preview the worklist + estimated cost before paying. Networked but free (uses count_tokens).",
    flags: [
      {
        flag: "--all",
        key: "all",
        label: "Full re-bootstrap view",
        description: "Show the cost of regenerating every in-scope file, not just the incremental worklist.",
        type: "boolean",
        default: false,
      },
      {
        flag: "--model",
        key: "model",
        label: "Model override",
        description: "Override the model used for cost estimation.",
        type: "string",
        placeholder: "anthropic/claude-sonnet-4-6",
      },
    ],
  },
  {
    command: "verify",
    title: "Verify",
    description:
      "Offline drift check. Exits non-zero if any triefact has drifted from its source. No LLM, no writes.",
    flags: [],
  },
  {
    command: "status",
    title: "Status",
    description: "Show trie's working state — like git status for the triefact tree.",
    json: true,
    flags: [],
  },
  {
    command: "audit",
    title: "Audit",
    description: "Summarise the telemetry log: MCP usage, sync activity, retries, CLI invocations.",
    flags: [],
  },
]

/** Build argv (flags after the subcommand) from a command def + form values.
 *  `fixedArgs` (always-on flags like init's --no-install-hooks) come first. */
export function buildArgs(
  def: CommandDef,
  values: Record<string, boolean | number | string | undefined>,
): string[] {
  const args: string[] = [...(def.fixedArgs ?? [])]
  for (const f of def.flags) {
    const v = values[f.key]
    if (f.type === "boolean") {
      if (v === true) args.push(f.flag)
    } else if (v !== undefined && v !== "" && !(typeof v === "number" && Number.isNaN(v))) {
      args.push(f.flag, String(v))
    }
  }
  return args
}
