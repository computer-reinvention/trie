import { useEffect, useMemo, useState } from "react"
import { SETTINGS, type SettingDef } from "@/settings/schema"
import { OC_FIELDS, OC_CATEGORIES, type OcFieldDef } from "@/settings/opencodeSchema"
import { TRIE_FIELDS, TRIE_CATEGORIES, type TrieFieldDef } from "@/settings/trieSchema"
import { useSettingsStore } from "@/store/settingsStore"
import { useOpencodeConfigStore } from "@/store/opencodeConfigStore"
import { useTrieConfigStore } from "@/store/trieConfigStore"
import { useTrieCommandStore } from "@/store/trieCommandStore"
import { useTabsStore, TRIE_TAB_ID } from "@/store/tabsStore"
import { useAppStore } from "@/store/appStore"
import { X, RotateCcw, Search, Loader2 } from "@/components/AgentPanel/icons"
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

  const loadTrie = useTrieConfigStore((s) => s.load)
  const trieLoaded = useTrieConfigStore((s) => s.loaded)
  const trieExists = useTrieConfigStore((s) => s.exists)
  const trieError = useTrieConfigStore((s) => s.lastError)

  // Load opencode + trie config once when the panel opens (re-read to honour any
  // external edits made since last time).
  useEffect(() => {
    if (projectDir) {
      loadOc(projectDir)
      loadTrie(projectDir)
    }
  }, [projectDir, loadOc, loadTrie])

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

  const trieFiltered = useMemo(
    () =>
      TRIE_FIELDS.filter((f) => {
        if (category && category !== `trie:${f.category}`) return false
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
          <SectionLabel>trie</SectionLabel>
          {TRIE_CATEGORIES.map((c) => (
            <CategoryButton
              key={c}
              label={c}
              active={category === `trie:${c}`}
              onClick={() => setCategory(`trie:${c}`)}
            />
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
            {(category === null ||
              (!category.startsWith("oc:") && !category.startsWith("trie:"))) &&
              appFiltered.map((s) => <AppSettingRow key={s.id} def={s} />)}

            {/* trie.toml settings */}
            {(category === null || category.startsWith("trie:")) && (
              <>
                {!projectDir ? (
                  <p className="text-3 text-sm py-4">Open a project to edit trie settings.</p>
                ) : !trieLoaded ? (
                  <p className="text-3 text-sm py-4">Loading trie.toml…</p>
                ) : !trieExists ? (
                  <TrieMissingNotice onClose={onClose} />
                ) : (
                  <>
                    {trieError && (
                      <p
                        className="text-xs rounded px-3 py-2 my-2"
                        style={{
                          color: "#fda4af",
                          background: "var(--danger-soft)",
                          border: "1px solid color-mix(in srgb, var(--danger) 40%, transparent)",
                        }}
                      >
                        {trieError}
                      </p>
                    )}
                    {trieFiltered.map((f) => (
                      <TrieSettingRow key={f.pointer} def={f} />
                    ))}
                  </>
                )}
              </>
            )}

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

            {appFiltered.length === 0 &&
              ocFiltered.length === 0 &&
              trieFiltered.length === 0 && (
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

// ── trie.toml missing notice ──────────────────────────────────────────────────
function TrieMissingNotice({ onClose }: { onClose: () => void }) {
  const running = useTrieCommandStore((s) => s.running)
  const activeCommand = useTrieCommandStore((s) => s.command)
  const runCommand = useTrieCommandStore((s) => s.run)
  const initing = running && activeCommand === "init"

  const init = () => {
    // Run init through the shared command store so its output streams into the
    // trie command panel exactly like every other command. The graph repopulate
    // + config reload happen via the store's onComplete listeners (wired in App
    // / Settings); here we just kick it off, switch to the panel so the user
    // sees the progress, and close the Settings overlay.
    runCommand("init", {})
    useTabsStore.getState().activate(TRIE_TAB_ID)
    onClose()
  }

  return (
    <div className="py-6 text-center">
      <p className="text-2 text-sm">
        No <span className="font-mono text-1">trie.toml</span> in this project yet.
      </p>
      <p className="text-3 text-xs mt-1 max-w-md mx-auto">
        Initialize trie to create the config and build the symbol graph. Progress streams in the
        trie panel; you can tune every setting here afterwards.
      </p>
      <button
        className="mt-3 inline-flex items-center gap-1.5 rounded-md bg-accent text-white px-3.5 py-1.5 text-xs font-medium disabled:opacity-60"
        onClick={init}
        disabled={initing}
      >
        {initing ? (
          <>
            <Spinner />
            Initializing…
          </>
        ) : (
          "Run trie init"
        )}
      </button>
    </div>
  )
}

// ── trie settings row (trie.toml) ─────────────────────────────────────────────
function TrieSettingRow({ def }: { def: TrieFieldDef }) {
  const value = useTrieConfigStore((s) => s.getValue(def.pointer))
  const setVal = useTrieConfigStore((s) => s.setValue)
  // At-default detection: a value equal to trie's default is cleared from the
  // managed delta (so trie.toml stays minimal) rather than pinned.
  const effective = value === undefined ? def.default : value
  const isDefault =
    JSON.stringify(effective) === JSON.stringify(def.default)
  const onChange = (v: unknown) => {
    // Clearing back to the default removes the key entirely.
    if (JSON.stringify(v) === JSON.stringify(def.default)) setVal(def.pointer, undefined)
    else setVal(def.pointer, v)
  }

  const wide = def.type === "stringList" || def.type === "json"

  return (
    <div className="py-3 border-b border-subtle/60 group">
      <div className={`flex gap-4 ${wide ? "flex-col" : "items-start justify-between"}`}>
        <div className="min-w-0 flex-1">
          <div className="flex items-center gap-2">
            <span className="text-1 text-sm font-medium">{def.title}</span>
            {!isDefault && (
              <button
                className="text-[10px] text-3 hover:text-1 opacity-0 group-hover:opacity-100 transition-opacity"
                onClick={() => setVal(def.pointer, undefined)}
                title="Reset to trie default"
              >
                reset
              </button>
            )}
          </div>
          <p className="text-3 text-xs mt-0.5 leading-snug">{def.description}</p>
          <p className="text-faint text-[10px] mt-0.5 font-mono">{def.pointer}</p>
        </div>
        <div className={wide ? "" : "shrink-0 pt-0.5"}>
          <TrieControl def={def} value={effective} onChange={onChange} />
        </div>
      </div>
    </div>
  )
}

function TrieControl({
  def,
  value,
  onChange,
}: {
  def: TrieFieldDef
  value: unknown
  onChange: (v: unknown) => void
}) {
  switch (def.type) {
    case "boolean":
      return <Toggle value={Boolean(value)} onChange={onChange} />
    case "enum":
      return <Select value={String(value)} options={def.enum ?? []} onChange={onChange} />
    case "number":
      return (
        <input
          type="number"
          className="w-28 surface-2 border border-strong focus:border-accent-soft rounded px-2 py-1 text-sm text-1 outline-none"
          value={value === undefined ? "" : Number(value)}
          min={def.min}
          max={def.max}
          step={def.step}
          onChange={(e) => onChange(e.target.value === "" ? def.default : Number(e.target.value))}
        />
      )
    case "string":
      return (
        <input
          type="text"
          className="w-56 surface-2 border border-strong focus:border-accent-soft rounded px-2 py-1 text-sm text-1 outline-none"
          placeholder={def.placeholder}
          value={value === undefined ? "" : String(value)}
          onChange={(e) => onChange(e.target.value === "" ? def.default : e.target.value)}
        />
      )
    case "stringList":
      return <StringListEditor value={value} placeholder={def.placeholder} onChange={onChange} />
    case "json":
      return <JsonEditor value={value} onChange={onChange} />
    default:
      return null
  }
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
function Spinner() {
  return <Loader2 size={13} className="animate-spin" />
}

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
