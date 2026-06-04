import { useMemo, useState } from "react"
import { SETTINGS, CATEGORIES, type SettingDef } from "@/settings/schema"
import { useSettingsStore } from "@/store/settingsStore"

interface SettingsProps {
  onClose: () => void
}

// VS Code-style settings: searchable, category-filtered list of settings with
// inline controls. Changes persist immediately (no Save button), mirroring
// VS Code's settings UI.
export function Settings({ onClose }: SettingsProps) {
  const [query, setQuery] = useState("")
  const [category, setCategory] = useState<string | null>(null)
  const reset = useSettingsStore((s) => s.reset)

  const filtered = useMemo(() => {
    const q = query.trim().toLowerCase()
    return SETTINGS.filter((s) => {
      if (category && s.category !== category) return false
      if (!q) return true
      return (
        s.title.toLowerCase().includes(q) ||
        s.description.toLowerCase().includes(q) ||
        s.id.toLowerCase().includes(q)
      )
    })
  }, [query, category])

  return (
    <div className="absolute inset-0 z-40 bg-slate-950 flex flex-col">
      {/* header */}
      <div className="flex items-center gap-3 px-5 py-3 border-b border-slate-800">
        <h1 className="text-slate-100 text-base font-semibold">Settings</h1>
        <input
          autoFocus
          className="flex-1 max-w-xl bg-slate-900 border border-slate-700 focus:border-accent rounded-md px-3 py-1.5 text-sm text-slate-100 outline-none placeholder:text-slate-600"
          placeholder="Search settings"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button
          className="text-slate-400 hover:text-slate-100 text-xs border border-slate-700 hover:border-slate-500 rounded px-2.5 py-1.5 transition-colors"
          onClick={() => reset()}
          title="Reset all settings to defaults"
        >
          Reset all
        </button>
        <button
          className="text-slate-400 hover:text-slate-100 text-lg leading-none px-2"
          onClick={onClose}
          title="Close (Esc)"
        >
          ×
        </button>
      </div>

      <div className="flex-1 flex min-h-0">
        {/* category nav */}
        <nav className="w-48 shrink-0 border-r border-slate-800 py-2 overflow-y-auto scroll-thin">
          <CategoryButton label="All" active={category === null} onClick={() => setCategory(null)} />
          {CATEGORIES.map((c) => (
            <CategoryButton
              key={c}
              label={c}
              active={category === c}
              onClick={() => setCategory(c)}
            />
          ))}
        </nav>

        {/* settings list */}
        <div className="flex-1 overflow-y-auto scroll-thin px-6 py-4">
          {filtered.length === 0 ? (
            <p className="text-slate-600 text-sm">No settings match “{query}”.</p>
          ) : (
            <div className="max-w-2xl space-y-1">
              {filtered.map((s) => (
                <SettingRow key={s.id} def={s} />
              ))}
            </div>
          )}
        </div>
      </div>
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
      className={`w-full text-left px-4 py-1.5 text-sm transition-colors ${
        active ? "text-slate-100 bg-slate-800 border-l-2 border-accent" : "text-slate-400 hover:text-slate-200 border-l-2 border-transparent"
      }`}
      onClick={onClick}
    >
      {label}
    </button>
  )
}

function SettingRow({ def }: { def: SettingDef }) {
  const value = useSettingsStore((s) => s.values[def.id] ?? def.default)
  const setVal = useSettingsStore((s) => s.set)
  const isDefault = value === def.default

  return (
    <div className="py-3 border-b border-slate-800/60 group">
      <div className="flex items-start gap-4">
        <div className="min-w-0 flex-1">
          <div className="flex items-center gap-2">
            <span className="text-slate-200 text-sm font-medium">{def.title}</span>
            {!isDefault && (
              <button
                className="text-[10px] text-slate-500 hover:text-accent opacity-0 group-hover:opacity-100 transition-opacity"
                onClick={() => setVal(def.id, def.default)}
                title="Reset to default"
              >
                reset
              </button>
            )}
          </div>
          <p className="text-slate-500 text-xs mt-0.5 leading-snug">{def.description}</p>
          <p className="text-slate-700 text-[10px] mt-0.5 font-mono">{def.id}</p>
        </div>
        <div className="shrink-0 pt-0.5">
          <Control def={def} value={value} onChange={(v) => setVal(def.id, v)} />
        </div>
      </div>
    </div>
  )
}

function Control({
  def,
  value,
  onChange,
}: {
  def: SettingDef
  value: boolean | number | string
  onChange: (v: boolean | number | string) => void
}) {
  if (def.type === "boolean") {
    return (
      <button
        role="switch"
        aria-checked={Boolean(value)}
        onClick={() => onChange(!value)}
        className={`relative w-9 h-5 rounded-full transition-colors ${
          value ? "bg-accent" : "bg-slate-700"
        }`}
      >
        <span
          className={`absolute top-0.5 left-0.5 w-4 h-4 rounded-full bg-white transition-transform ${
            value ? "translate-x-4" : ""
          }`}
        />
      </button>
    )
  }
  if (def.type === "enum") {
    return (
      <select
        className="bg-slate-900 border border-slate-700 focus:border-accent rounded px-2 py-1 text-sm text-slate-100 outline-none"
        value={String(value)}
        onChange={(e) => onChange(e.target.value)}
      >
        {def.enum?.map((o) => (
          <option key={o.value} value={o.value}>
            {o.label}
          </option>
        ))}
      </select>
    )
  }
  if (def.type === "number") {
    return (
      <input
        type="number"
        className="w-24 bg-slate-900 border border-slate-700 focus:border-accent rounded px-2 py-1 text-sm text-slate-100 outline-none"
        value={Number(value)}
        min={def.min}
        max={def.max}
        step={def.step}
        onChange={(e) => onChange(Number(e.target.value))}
      />
    )
  }
  return (
    <input
      type="text"
      className="w-48 bg-slate-900 border border-slate-700 focus:border-accent rounded px-2 py-1 text-sm text-slate-100 outline-none"
      value={String(value)}
      onChange={(e) => onChange(e.target.value)}
    />
  )
}
