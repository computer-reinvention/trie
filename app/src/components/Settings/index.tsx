import { useEffect, useMemo, useState } from "react"
import { SETTINGS, type SettingDef } from "@/settings/schema"
import { OC_FIELDS, OC_CATEGORIES, type OcFieldDef } from "@/settings/opencodeSchema"
import { useSettingsStore } from "@/store/settingsStore"
import { useOpencodeConfigStore } from "@/store/opencodeConfigStore"
import { useAppStore } from "@/store/appStore"
import { X, RotateCcw, Search } from "@/components/AgentPanel/icons"
import {
  StringListEditor,
  EnumMapEditor,
  ToggleMapEditor,
  ProviderListEditor,
  McpListEditor,
  AgentTableEditor,
  JsonEditor,
} from "./editors"

interface SettingsProps {
  onClose: () => void
}

const APP_CATEGORIES = Array.from(new Set(SETTINGS.map((s) => s.category)))

// VS Code-style settings: searchable, two sections — App preferences (persisted
// in prefs.json) and opencode configuration (written to the project's
// opencode.json). Changes persist immediately (no Save button).
export function Settings({ onClose }: SettingsProps) {
  const [query, setQuery] = useState("")
  const [category, setCategory] = useState<string | null>(null)
  const reset = useSettingsStore((s) => s.reset)

  const projectDir = useAppStore((s) => s.projectDir)
  const loadOc = useOpencodeConfigStore((s) => s.load)
  const ocLoaded = useOpencodeConfigStore((s) => s.loaded)
  const dirtyRestart = useOpencodeConfigStore((s) => s.dirtyRestart)
  const restart = useOpencodeConfigStore((s) => s.restart)

  // Load opencode config once when the panel opens (re-read to honour any
  // external edits made since last time).
  useEffect(() => {
    if (projectDir) loadOc(projectDir)
  }, [projectDir, loadOc])

  const q = query.trim().toLowerCase()

  const appFiltered = useMemo(
    () =>
      SETTINGS.filter((s) => {
        if (category && s.category !== category) return false
        if (!q) return true
        return (
          s.title.toLowerCase().includes(q) ||
          s.description.toLowerCase().includes(q) ||
          s.id.toLowerCase().includes(q)
        )
      }),
    [q, category],
  )

  const ocFiltered = useMemo(
    () =>
      OC_FIELDS.filter((f) => {
        if (category && f.category !== `oc:${f.category}` && category !== `oc:${f.category}`)
          return false
        if (!q) return true
        return (
          f.title.toLowerCase().includes(q) ||
          f.description.toLowerCase().includes(q) ||
          f.pointer.toLowerCase().includes(q)
        )
      }),
    [q, category],
  )

  return (
    <div className="absolute inset-0 z-40 surface-1 flex flex-col">
      {/* header */}
      <div className="flex items-center gap-3 px-5 py-3 border-b border-subtle">
        <h1 className="text-1 text-base font-semibold">Settings</h1>
        <div className="flex-1 max-w-xl flex items-center gap-2 surface-2 border border-strong focus-within:border-accent-soft rounded-md px-3 py-1.5">
          <Search size={14} className="text-faint shrink-0" />
          <input
            autoFocus
            className="flex-1 bg-transparent text-sm text-1 outline-none placeholder:text-faint"
            placeholder="Search settings"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
        </div>
        <button
          className="inline-flex items-center gap-1.5 text-2 hover:text-1 text-xs border border-subtle hover:border-strong rounded-md px-2.5 py-1.5 transition-colors"
          onClick={() => reset()}
          title="Reset app settings to defaults"
        >
          <RotateCcw size={13} /> Reset app
        </button>
        <button
          className="text-2 hover:text-1 p-1 rounded-md hover:surface-2"
          onClick={onClose}
          title="Close (Esc)"
        >
          <X size={18} />
        </button>
      </div>

      {dirtyRestart && (
        <div
          className="flex items-center justify-between px-5 py-2 text-xs"
          style={{
            background: "color-mix(in srgb, var(--warn) 12%, transparent)",
            color: "#fcd34d",
          }}
        >
          <span>Some changes require restarting opencode to take effect.</span>
          <button
            className="rounded-md px-2.5 py-1 font-medium"
            style={{ background: "color-mix(in srgb, var(--warn) 22%, transparent)" }}
            onClick={() => restart()}
          >
            Restart opencode
          </button>
        </div>
      )}

      <div className="flex-1 flex min-h-0">
        {/* category nav */}
        <nav className="w-52 shrink-0 border-r border-subtle py-2 overflow-y-auto scroll-thin">
          <CategoryButton label="All" active={category === null} onClick={() => setCategory(null)} />
          <SectionLabel>App</SectionLabel>
          {APP_CATEGORIES.map((c) => (
            <CategoryButton key={c} label={c} active={category === c} onClick={() => setCategory(c)} />
          ))}
          <SectionLabel>opencode</SectionLabel>
          {OC_CATEGORIES.map((c) => (
            <CategoryButton
              key={c}
              label={c}
              active={category === `oc:${c}`}
              onClick={() => setCategory(`oc:${c}`)}
            />
          ))}
        </nav>

        {/* settings list */}
        <div className="flex-1 overflow-y-auto scroll-thin px-6 py-4">
          <div className="max-w-2xl space-y-1">
            {/* App settings */}
            {(category === null || !category.startsWith("oc:")) &&
              appFiltered.map((s) => <AppSettingRow key={s.id} def={s} />)}

            {/* opencode settings */}
            {(category === null || category.startsWith("oc:")) && (
              <>
                {!projectDir ? (
                  <p className="text-3 text-sm py-4">Open a project to edit opencode settings.</p>
                ) : !ocLoaded ? (
                  <p className="text-3 text-sm py-4">Loading opencode config…</p>
                ) : (
                  ocFiltered
                    .filter((f) => !category || category === `oc:${f.category}`)
                    .map((f) => <OcSettingRow key={f.pointer} def={f} />)
                )}
              </>
            )}

            {appFiltered.length === 0 && ocFiltered.length === 0 && (
              <p className="text-3 text-sm">No settings match “{query}”.</p>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

function SectionLabel({ children }: { children: React.ReactNode }) {
  return (
    <div className="px-4 pt-3 pb-1 text-[10px] uppercase tracking-wider text-faint font-medium">
      {children}
    </div>
  )
}

function CategoryButton({
  label,
  active,
  onClick,
}: {
  label: string
  active: boolean
  onClick: () => void
}) {
  return (
    <button
      className={`w-full text-left px-4 py-1.5 text-sm transition-colors border-l-2 ${
        active
          ? "text-1 surface-2 border-accent"
          : "text-2 hover:text-1 border-transparent"
      }`}
      style={active ? { borderColor: "var(--accent)" } : undefined}
      onClick={onClick}
    >
      {label}
    </button>
  )
}

// ── App settings row (prefs.json) ─────────────────────────────────────────────
function AppSettingRow({ def }: { def: SettingDef }) {
  const value = useSettingsStore((s) => s.values[def.id] ?? def.default)
  const setVal = useSettingsStore((s) => s.set)
  const isDefault = value === def.default

  return (
    <div className="py-3 border-b border-subtle/60 group">
      <div className="flex items-start gap-4">
        <div className="min-w-0 flex-1">
          <div className="flex items-center gap-2">
            <span className="text-1 text-sm font-medium">{def.title}</span>
            {!isDefault && (
              <button
                className="text-[10px] text-3 hover:text-1 opacity-0 group-hover:opacity-100 transition-opacity"
                onClick={() => setVal(def.id, def.default)}
                title="Reset to default"
              >
                reset
              </button>
            )}
          </div>
          <p className="text-3 text-xs mt-0.5 leading-snug">{def.description}</p>
          <p className="text-faint text-[10px] mt-0.5 font-mono">{def.id}</p>
        </div>
        <div className="shrink-0 pt-0.5">
          <AppControl def={def} value={value} onChange={(v) => setVal(def.id, v)} />
        </div>
      </div>
    </div>
  )
}

function AppControl({
  def,
  value,
  onChange,
}: {
  def: SettingDef
  value: boolean | number | string
  onChange: (v: boolean | number | string) => void
}) {
  if (def.type === "boolean") return <Toggle value={Boolean(value)} onChange={onChange} />
  if (def.type === "enum")
    return (
      <Select
        value={String(value)}
        options={def.enum ?? []}
        onChange={onChange}
      />
    )
  if (def.type === "number")
    return (
      <input
        type="number"
        className="w-24 surface-2 border border-strong focus:border-accent-soft rounded px-2 py-1 text-sm text-1 outline-none"
        value={Number(value)}
        min={def.min}
        max={def.max}
        step={def.step}
        onChange={(e) => onChange(Number(e.target.value))}
      />
    )
  return (
    <input
      type="text"
      className="w-48 surface-2 border border-strong focus:border-accent-soft rounded px-2 py-1 text-sm text-1 outline-none"
      value={String(value)}
      onChange={(e) => onChange(e.target.value)}
    />
  )
}

// ── opencode settings row (opencode.json) ─────────────────────────────────────
function OcSettingRow({ def }: { def: OcFieldDef }) {
  const value = useOpencodeConfigStore((s) => s.getValue(def.pointer))
  const setVal = useOpencodeConfigStore((s) => s.setValue)
  const onChange = (v: unknown) => setVal(def.pointer, v, def.restart)

  const wide =
    def.type === "providerList" ||
    def.type === "mcpList" ||
    def.type === "agentTable" ||
    def.type === "json" ||
    def.type === "enumMap" ||
    def.type === "toggleMap" ||
    def.type === "stringList"

  return (
    <div className="py-3 border-b border-subtle/60">
      <div className={`flex gap-4 ${wide ? "flex-col" : "items-start justify-between"}`}>
        <div className="min-w-0 flex-1">
          <div className="flex items-center gap-2">
            <span className="text-1 text-sm font-medium">{def.title}</span>
            {def.restart && (
              <span className="text-[9px] uppercase tracking-wide text-faint border border-subtle rounded px-1">
                restart
              </span>
            )}
          </div>
          <p className="text-3 text-xs mt-0.5 leading-snug">{def.description}</p>
          <p className="text-faint text-[10px] mt-0.5 font-mono">{def.pointer}</p>
        </div>
        <div className={wide ? "" : "shrink-0 pt-0.5"}>
          <OcControl def={def} value={value} onChange={onChange} />
        </div>
      </div>
    </div>
  )
}

function OcControl({
  def,
  value,
  onChange,
}: {
  def: OcFieldDef
  value: unknown
  onChange: (v: unknown) => void
}) {
  switch (def.type) {
    case "boolean":
      return <Toggle value={Boolean(value)} onChange={onChange} />
    case "enum":
      return (
        <Select
          value={value === undefined ? "" : String(value)}
          options={def.enum ?? []}
          onChange={(v) => onChange(coerceEnum(v))}
        />
      )
    case "number":
      return (
        <input
          type="number"
          className="w-28 surface-2 border border-strong focus:border-accent-soft rounded px-2 py-1 text-sm text-1 outline-none"
          value={value === undefined ? "" : Number(value)}
          min={def.min}
          max={def.max}
          step={def.step}
          onChange={(e) => onChange(e.target.value === "" ? undefined : Number(e.target.value))}
        />
      )
    case "string":
      return (
        <input
          type="text"
          className="w-56 surface-2 border border-strong focus:border-accent-soft rounded px-2 py-1 text-sm text-1 outline-none"
          placeholder={def.placeholder}
          value={value === undefined ? "" : String(value)}
          onChange={(e) => onChange(e.target.value || undefined)}
        />
      )
    case "stringList":
      return <StringListEditor value={value} placeholder={def.placeholder} onChange={onChange} />
    case "enumMap":
      return <EnumMapEditor def={def} value={value} onChange={onChange} />
    case "toggleMap":
      return <ToggleMapEditor def={def} value={value} onChange={onChange} />
    case "providerList":
      return <ProviderListEditor value={value} onChange={onChange} />
    case "mcpList":
      return <McpListEditor value={value} onChange={onChange} />
    case "agentTable":
      return <AgentTableEditor value={value} onChange={onChange} />
    case "json":
      return <JsonEditor value={value} onChange={onChange} />
    default:
      return null
  }
}

// boolean/notify enums and the empty "default" option round-trip as real types.
function coerceEnum(v: string): unknown {
  if (v === "") return undefined
  if (v === "true") return true
  if (v === "false") return false
  return v
}

// ── shared controls ───────────────────────────────────────────────────────────
function Toggle({ value, onChange }: { value: boolean; onChange: (v: boolean) => void }) {
  return (
    <button
      role="switch"
      aria-checked={value}
      onClick={() => onChange(!value)}
      className={`relative w-9 h-5 rounded-full transition-colors ${value ? "bg-accent" : "surface-3"}`}
    >
      <span
        className={`absolute top-0.5 left-0.5 w-4 h-4 rounded-full bg-white transition-transform ${
          value ? "translate-x-4" : ""
        }`}
      />
    </button>
  )
}

function Select({
  value,
  options,
  onChange,
}: {
  value: string
  options: { value: string; label: string }[]
  onChange: (v: string) => void
}) {
  return (
    <select
      className="surface-2 border border-strong focus:border-accent-soft rounded px-2 py-1 text-sm text-1 outline-none"
      value={value}
      onChange={(e) => onChange(e.target.value)}
    >
      {options.map((o) => (
        <option key={o.value} value={o.value}>
          {o.label}
        </option>
      ))}
    </select>
  )
}
