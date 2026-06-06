// VS Code-style settings schema. Each setting has a stable dotted id, a type,
// a default, a category + title + description for the settings UI. The store
// reads/writes values; components read effective values via useSetting().

export type SettingType = "boolean" | "number" | "string" | "enum"

export interface SettingDef {
  id: string
  title: string
  description: string
  category: string
  type: SettingType
  default: boolean | number | string
  enum?: { value: string; label: string }[]
  min?: number
  max?: number
  step?: number
}

export const SETTINGS: SettingDef[] = [
  // ── Appearance ──────────────────────────────────────────────────────────
  {
    id: "appearance.theme",
    title: "Color Theme",
    description: "Overall color theme for the application.",
    category: "Appearance",
    type: "enum",
    default: "dark",
    enum: [
      { value: "dark", label: "Dark" },
      { value: "midnight", label: "Midnight" },
      { value: "slate", label: "Slate" },
    ],
  },
  {
    id: "appearance.accent",
    title: "Accent Color",
    description: "Accent color used for highlights, buttons, and selection.",
    category: "Appearance",
    type: "enum",
    default: "indigo",
    enum: [
      { value: "indigo", label: "Indigo" },
      { value: "violet", label: "Violet" },
      { value: "emerald", label: "Emerald" },
      { value: "amber", label: "Amber" },
      { value: "rose", label: "Rose" },
    ],
  },
  {
    id: "appearance.uiDensity",
    title: "UI Density",
    description: "Spacing and sizing of interface elements.",
    category: "Appearance",
    type: "enum",
    default: "comfortable",
    enum: [
      { value: "comfortable", label: "Comfortable" },
      { value: "compact", label: "Compact" },
    ],
  },
  {
    id: "appearance.fontSize",
    title: "UI Font Size",
    description: "Base font size for the interface, in pixels.",
    category: "Appearance",
    type: "number",
    default: 13,
    min: 10,
    max: 18,
    step: 1,
  },

  // ── Graph ───────────────────────────────────────────────────────────────
  {
    id: "graph.defaultAxis",
    title: "Default Grouping",
    description: "Whether the system map opens grouped by role or by subsystem.",
    category: "Graph",
    type: "enum",
    default: "role",
    enum: [
      { value: "role", label: "Roles" },
      { value: "subsystem", label: "Subsystems" },
    ],
  },
  {
    id: "graph.showTests",
    title: "Show Tests",
    description: "Include test symbols in the system map by default.",
    category: "Graph",
    type: "boolean",
    default: false,
  },
  {
    id: "graph.hideMinor",
    title: "Hide Minor Symbols",
    description: "Hide symbols referenced at most once inside expanded views.",
    category: "Graph",
    type: "boolean",
    default: true,
  },
  {
    id: "graph.memberGrouping",
    title: "Member Grouping",
    description: "How members are sub-grouped inside an expanded role/subsystem.",
    category: "Graph",
    type: "enum",
    default: "subsystem",
    enum: [
      { value: "subsystem", label: "Subsystem" },
      { value: "class", label: "Kind" },
      { value: "owningClass", label: "Owning class" },
    ],
  },
  {
    id: "graph.budget",
    title: "Visible Node Budget",
    description: "Maximum number of symbols rendered at once before aggregating.",
    category: "Graph",
    type: "number",
    default: 250,
    min: 50,
    max: 1000,
    step: 25,
  },
  {
    id: "graph.followAgent",
    title: "Follow Agent in Graph",
    description:
      "Automatically expand and centre the symbol the agent is reading or editing as it works.",
    category: "Graph",
    type: "boolean",
    default: true,
  },

  // ── Agent ───────────────────────────────────────────────────────────────
  {
    id: "agent.model",
    title: "Model",
    description: "Model used for agent turns.",
    category: "Agent",
    type: "enum",
    default: "claude-sonnet-4-6",
    enum: [
      { value: "claude-sonnet-4-6", label: "Claude Sonnet 4.6" },
      { value: "claude-opus-4-7", label: "Claude Opus 4.7" },
      { value: "claude-haiku-4-5", label: "Claude Haiku 4.5" },
    ],
  },
  {
    id: "agent.sendOnEnter",
    title: "Send on Enter",
    description: "Press Enter to send; use Shift+Enter for a newline.",
    category: "Agent",
    type: "boolean",
    default: true,
  },
  {
    id: "agent.autoSwitchToGraph",
    title: "Auto-switch to Graph on Activity",
    description: "Jump to the graph tab when the agent starts touching symbols.",
    category: "Agent",
    type: "boolean",
    default: true,
  },

  // ── Editor ──────────────────────────────────────────────────────────────
  {
    id: "editor.confirmBeforeApply",
    title: "Confirm Before Apply",
    description: "Ask for confirmation before the agent applies edits.",
    category: "Editor",
    type: "boolean",
    default: true,
  },
]

export const CATEGORIES = Array.from(new Set(SETTINGS.map((s) => s.category)))

export const DEFAULTS: Record<string, boolean | number | string> = Object.fromEntries(
  SETTINGS.map((s) => [s.id, s.default]),
)

export function settingDef(id: string): SettingDef | undefined {
  return SETTINGS.find((s) => s.id === id)
}
