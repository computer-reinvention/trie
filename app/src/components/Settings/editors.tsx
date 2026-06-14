import { useEffect, useState } from "react"
import { Plus, X, Trash2 } from "@/components/AgentPanel/icons"
import { defaultEnvVar, type OcFieldDef } from "@/settings/opencodeSchema"

// Typed editors for the structured parts of opencode.json. Each receives the
// current value (from the opencode config store) and an onChange that writes
// back through the store. Scalars are handled inline in the Settings panel; the
// editors here cover lists, maps, providers, MCP, agents, and raw JSON.

type Json = unknown

const inputCls =
  "surface-2 border border-strong focus:border-accent-soft rounded-md px-2 py-1 text-sm text-1 outline-none"

// ── string[] ────────────────────────────────────────────────────────────────
export function StringListEditor({
  value,
  placeholder,
  onChange,
}: {
  value: Json
  placeholder?: string
  onChange: (v: string[] | undefined) => void
}) {
  const list = Array.isArray(value) ? (value as string[]) : []
  const update = (next: string[]) => onChange(next.length ? next : undefined)
  return (
    <div className="space-y-1.5">
      {list.map((item, i) => (
        <div key={i} className="flex items-center gap-1.5">
          <input
            className={`${inputCls} flex-1`}
            value={item}
            placeholder={placeholder}
            onChange={(e) => {
              const next = [...list]
              next[i] = e.target.value
              update(next)
            }}
          />
          <button
            className="text-3 hover:text-1 p-1"
            onClick={() => update(list.filter((_, j) => j !== i))}
            title="Remove"
          >
            <Trash2 size={14} />
          </button>
        </div>
      ))}
      <button
        className="inline-flex items-center gap-1 text-xs text-2 hover:text-1"
        onClick={() => update([...list, ""])}
      >
        <Plus size={13} /> Add
      </button>
    </div>
  )
}

// ── { key: enum } (permission matrix) ─────────────────────────────────────────
export function EnumMapEditor({
  def,
  value,
  onChange,
}: {
  def: OcFieldDef
  value: Json
  onChange: (v: Record<string, string> | undefined) => void
}) {
  const map = (value && typeof value === "object" ? value : {}) as Record<string, string>
  const choices = def.mapChoices ?? []
  const setKey = (key: string, choice: string) => {
    const next = { ...map }
    if (!choice) delete next[key]
    else next[key] = choice
    onChange(Object.keys(next).length ? next : undefined)
  }
  return (
    <div className="space-y-1">
      {(def.mapKeys ?? []).map((key) => (
        <div key={key} className="flex items-center justify-between gap-3 py-0.5">
          <span className="font-mono text-xs text-2">{key}</span>
          <div className="flex rounded-md overflow-hidden border border-strong">
            {choices.map((c) => {
              const active = (map[key] ?? "") === c.value
              return (
                <button
                  key={c.value}
                  className={`px-2 py-0.5 text-[11px] transition-colors ${
                    active ? "bg-accent text-white" : "surface-2 text-3 hover:text-1"
                  }`}
                  onClick={() => setKey(key, c.value)}
                >
                  {c.label}
                </button>
              )
            })}
          </div>
        </div>
      ))}
    </div>
  )
}

// ── { key: boolean } (tools) ──────────────────────────────────────────────────
export function ToggleMapEditor({
  def,
  value,
  onChange,
}: {
  def: OcFieldDef
  value: Json
  onChange: (v: Record<string, boolean> | undefined) => void
}) {
  const map = (value && typeof value === "object" ? value : {}) as Record<string, boolean>
  const toggle = (key: string) => {
    const next = { ...map }
    // tristate → here we only express explicit on/off; clicking cycles off→on→unset
    if (!(key in next)) next[key] = false
    else if (next[key] === false) next[key] = true
    else delete next[key]
    onChange(Object.keys(next).length ? next : undefined)
  }
  const label = (key: string) =>
    !(key in map) ? "default" : map[key] ? "on" : "off"
  return (
    <div className="grid grid-cols-2 gap-1.5">
      {(def.toggleKeys ?? []).map((key) => (
        <button
          key={key}
          className="flex items-center justify-between surface-2 border border-subtle rounded-md px-2 py-1 text-xs hover:border-strong"
          onClick={() => toggle(key)}
        >
          <span className="font-mono text-2">{key}</span>
          <span
            className="text-[10px] uppercase tracking-wide"
            style={{
              color:
                label(key) === "on"
                  ? "var(--accent)"
                  : label(key) === "off"
                    ? "var(--danger)"
                    : "var(--text-faint)",
            }}
          >
            {label(key)}
          </span>
        </button>
      ))}
    </div>
  )
}

// ── providers (Keychain-backed apiKey) ────────────────────────────────────────
interface ProviderInfo {
  provider: string
  hasKey: boolean
  envVar: string
}

export function ProviderListEditor({
  value,
  onChange,
}: {
  value: Json
  onChange: (v: Record<string, Json> | undefined) => void
}) {
  const providers = (value && typeof value === "object" ? value : {}) as Record<string, Json>
  const [keyed, setKeyed] = useState<ProviderInfo[]>([])
  const [newName, setNewName] = useState("")

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const trie = () => (window as any).trie

  const refresh = () => {
    trie()
      .secrets.listProviders()
      .then((l: ProviderInfo[]) => setKeyed(l ?? []))
      .catch(() => {})
  }
  useEffect(refresh, [])

  const names = Array.from(
    new Set([...Object.keys(providers), ...keyed.map((k) => k.provider)]),
  )

  const addProvider = () => {
    const name = newName.trim()
    if (!name) return
    onChange({ ...providers, [name]: providers[name] ?? {} })
    setNewName("")
  }

  return (
    <div className="space-y-2">
      {names.map((name) => (
        <ProviderRow
          key={name}
          name={name}
          config={(providers[name] as Record<string, Json>) ?? {}}
          info={keyed.find((k) => k.provider === name)}
          onConfig={(c) => onChange({ ...providers, [name]: c })}
          onAfterKeyChange={refresh}
        />
      ))}
      <div className="flex items-center gap-1.5 pt-1">
        <input
          className={`${inputCls} flex-1`}
          placeholder="Add provider (e.g. anthropic)"
          value={newName}
          onChange={(e) => setNewName(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && addProvider()}
        />
        <button className="inline-flex items-center gap-1 text-xs text-2 hover:text-1" onClick={addProvider}>
          <Plus size={13} /> Add
        </button>
      </div>
    </div>
  )
}

function ProviderRow({
  name,
  config,
  info,
  onConfig,
  onAfterKeyChange,
}: {
  name: string
  config: Record<string, Json>
  info?: ProviderInfo
  onConfig: (c: Record<string, Json>) => void
  onAfterKeyChange: () => void
}) {
  const [keyInput, setKeyInput] = useState("")
  const [envVar, setEnvVar] = useState(info?.envVar ?? defaultEnvVar(name))
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const trie = () => (window as any).trie
  const options = (config.options as Record<string, Json>) ?? {}

  const saveKey = async () => {
    await trie().secrets.setProviderKey(name, keyInput, envVar)
    setKeyInput("")
    // reference the env var in opencode.json so opencode picks it up
    onConfig({
      ...config,
      options: { ...options, apiKey: `{env:${envVar}}` },
    })
    onAfterKeyChange()
  }
  const clearKey = async () => {
    await trie().secrets.deleteProviderKey(name)
    onAfterKeyChange()
  }

  return (
    <div className="surface-2 border border-subtle rounded-lg p-2.5 space-y-2">
      <div className="flex items-center justify-between">
        <span className="font-mono text-sm text-1">{name}</span>
        <span
          className="text-[10px] uppercase tracking-wide"
          style={{ color: info?.hasKey ? "var(--accent)" : "var(--text-faint)" }}
        >
          {info?.hasKey ? "key set" : "no key"}
        </span>
      </div>
      <div className="flex items-center gap-1.5">
        <input
          type="password"
          className={`${inputCls} flex-1`}
          placeholder={info?.hasKey ? "••••••  (replace)" : "API key"}
          value={keyInput}
          onChange={(e) => setKeyInput(e.target.value)}
        />
        <button
          className="text-xs px-2 py-1 rounded-md bg-accent text-white disabled:opacity-40"
          onClick={saveKey}
          disabled={!keyInput.trim()}
        >
          Save
        </button>
        {info?.hasKey && (
          <button className="text-3 hover:text-1 p-1" onClick={clearKey} title="Remove key">
            <Trash2 size={14} />
          </button>
        )}
      </div>
      <div className="flex items-center gap-2">
        <label className="text-[11px] text-3 w-16 shrink-0">Env var</label>
        <input
          className={`${inputCls} flex-1 font-mono text-xs`}
          value={envVar}
          onChange={(e) => setEnvVar(e.target.value)}
        />
      </div>
      <div className="flex items-center gap-2">
        <label className="text-[11px] text-3 w-16 shrink-0">Base URL</label>
        <input
          className={`${inputCls} flex-1`}
          placeholder="(optional)"
          value={(options.baseURL as string) ?? ""}
          onChange={(e) =>
            onConfig({
              ...config,
              options: { ...options, baseURL: e.target.value || undefined },
            })
          }
        />
      </div>
    </div>
  )
}

// ── MCP servers ───────────────────────────────────────────────────────────────
export function McpListEditor({
  value,
  onChange,
}: {
  value: Json
  onChange: (v: Record<string, Json> | undefined) => void
}) {
  const servers = (value && typeof value === "object" ? value : {}) as Record<string, Json>
  const [newName, setNewName] = useState("")

  const names = Object.keys(servers)
  const addRemote = () => {
    const name = newName.trim()
    if (!name || name === "trie") return
    onChange({ ...servers, [name]: { type: "remote", url: "", enabled: true } })
    setNewName("")
  }
  const remove = (name: string) => {
    const next = { ...servers }
    delete next[name]
    onChange(Object.keys(next).length ? next : undefined)
  }
  const patch = (name: string, p: Record<string, Json>) =>
    onChange({ ...servers, [name]: { ...(servers[name] as object), ...p } })

  return (
    <div className="space-y-2">
      {names.map((name) => {
        const srv = servers[name] as Record<string, Json>
        const locked = name === "trie"
        return (
          <div key={name} className="surface-2 border border-subtle rounded-lg p-2.5 space-y-2">
            <div className="flex items-center justify-between">
              <span className="font-mono text-sm text-1">
                {name}
                {locked && <span className="ml-2 text-[10px] text-faint">(managed)</span>}
              </span>
              {!locked && (
                <button className="text-3 hover:text-1 p-1" onClick={() => remove(name)}>
                  <Trash2 size={14} />
                </button>
              )}
            </div>
            {!locked && srv?.type === "remote" && (
              <input
                className={`${inputCls} w-full`}
                placeholder="https://server/mcp"
                value={(srv.url as string) ?? ""}
                onChange={(e) => patch(name, { url: e.target.value })}
              />
            )}
            {!locked && srv?.type === "local" && (
              <input
                className={`${inputCls} w-full font-mono text-xs`}
                placeholder="command arg1 arg2"
                value={Array.isArray(srv.command) ? (srv.command as string[]).join(" ") : ""}
                onChange={(e) => patch(name, { command: e.target.value.split(/\s+/).filter(Boolean) })}
              />
            )}
            {!locked && (
              <label className="flex items-center gap-2 text-xs text-2">
                <input
                  type="checkbox"
                  checked={srv?.enabled !== false}
                  onChange={(e) => patch(name, { enabled: e.target.checked })}
                />
                Enabled
              </label>
            )}
          </div>
        )
      })}
      <div className="flex items-center gap-1.5 pt-1">
        <input
          className={`${inputCls} flex-1`}
          placeholder="Add remote MCP server name"
          value={newName}
          onChange={(e) => setNewName(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && addRemote()}
        />
        <button className="inline-flex items-center gap-1 text-xs text-2 hover:text-1" onClick={addRemote}>
          <Plus size={13} /> Add
        </button>
      </div>
    </div>
  )
}

// ── agents ────────────────────────────────────────────────────────────────────
export function AgentTableEditor({
  value,
  onChange,
}: {
  value: Json
  onChange: (v: Record<string, Json> | undefined) => void
}) {
  const agents = (value && typeof value === "object" ? value : {}) as Record<string, Json>
  const [newName, setNewName] = useState("")
  const [openName, setOpenName] = useState<string | null>(null)

  const names = Object.keys(agents)
  const add = () => {
    const name = newName.trim()
    if (!name) return
    onChange({ ...agents, [name]: agents[name] ?? {} })
    setNewName("")
    setOpenName(name)
  }
  const remove = (name: string) => {
    const next = { ...agents }
    delete next[name]
    onChange(Object.keys(next).length ? next : undefined)
  }
  const patch = (name: string, p: Record<string, Json>) => {
    const cur = (agents[name] as Record<string, Json>) ?? {}
    const merged = { ...cur, ...p }
    for (const k of Object.keys(p)) if (p[k] === "" || p[k] === undefined) delete merged[k]
    onChange({ ...agents, [name]: merged })
  }

  return (
    <div className="space-y-2">
      {names.map((name) => {
        const a = (agents[name] as Record<string, Json>) ?? {}
        const open = openName === name
        return (
          <div key={name} className="surface-2 border border-subtle rounded-lg">
            <div className="flex items-center justify-between px-2.5 py-1.5">
              <button
                className="font-mono text-sm text-1 flex-1 text-left"
                onClick={() => setOpenName(open ? null : name)}
              >
                {name}
              </button>
              <button className="text-3 hover:text-1 p-1" onClick={() => remove(name)}>
                <Trash2 size={14} />
              </button>
            </div>
            {open && (
              <div className="px-2.5 pb-2.5 space-y-2 border-t border-subtle pt-2">
                <Labeled label="Model">
                  <input
                    className={`${inputCls} w-full`}
                    placeholder="provider/model"
                    value={(a.model as string) ?? ""}
                    onChange={(e) => patch(name, { model: e.target.value })}
                  />
                </Labeled>
                <Labeled label="Mode">
                  <select
                    className={`${inputCls} w-full`}
                    value={(a.mode as string) ?? ""}
                    onChange={(e) => patch(name, { mode: e.target.value })}
                  >
                    <option value="">default</option>
                    <option value="primary">primary</option>
                    <option value="subagent">subagent</option>
                    <option value="all">all</option>
                  </select>
                </Labeled>
                <Labeled label="Description">
                  <input
                    className={`${inputCls} w-full`}
                    value={(a.description as string) ?? ""}
                    onChange={(e) => patch(name, { description: e.target.value })}
                  />
                </Labeled>
                <Labeled label="Prompt">
                  <textarea
                    className={`${inputCls} w-full resize-y min-h-[60px]`}
                    value={(a.prompt as string) ?? ""}
                    onChange={(e) => patch(name, { prompt: e.target.value })}
                  />
                </Labeled>
              </div>
            )}
          </div>
        )
      })}
      <div className="flex items-center gap-1.5 pt-1">
        <input
          className={`${inputCls} flex-1`}
          placeholder="Add agent name (e.g. code-reviewer)"
          value={newName}
          onChange={(e) => setNewName(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && add()}
        />
        <button className="inline-flex items-center gap-1 text-xs text-2 hover:text-1" onClick={add}>
          <Plus size={13} /> Add
        </button>
      </div>
    </div>
  )
}

function Labeled({ label, children }: { label: string; children: React.ReactNode }) {
  return (
    <div className="space-y-1">
      <label className="text-[11px] text-3">{label}</label>
      {children}
    </div>
  )
}

// ── raw JSON (experimental, policies) ─────────────────────────────────────────
export function JsonEditor({
  value,
  onChange,
}: {
  value: Json
  onChange: (v: Json | undefined) => void
}) {
  const [text, setText] = useState(() =>
    value === undefined ? "" : JSON.stringify(value, null, 2),
  )
  const [error, setError] = useState<string | null>(null)

  // re-sync when the underlying value changes externally (e.g. reload)
  useEffect(() => {
    setText(value === undefined ? "" : JSON.stringify(value, null, 2))
  }, [value])

  const commit = (next: string) => {
    setText(next)
    if (!next.trim()) {
      setError(null)
      onChange(undefined)
      return
    }
    try {
      const parsed = JSON.parse(next)
      setError(null)
      onChange(parsed)
    } catch (e) {
      setError(String(e instanceof Error ? e.message : e))
    }
  }

  return (
    <div className="space-y-1">
      <textarea
        className={`${inputCls} w-full font-mono text-xs resize-y min-h-[120px] ${error ? "border-red-500" : ""}`}
        spellCheck={false}
        value={text}
        onChange={(e) => commit(e.target.value)}
      />
      {error && (
        <p className="text-[11px]" style={{ color: "var(--danger)" }}>
          {error}
        </p>
      )}
    </div>
  )
}
