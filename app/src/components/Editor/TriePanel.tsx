import { useEffect, useMemo, useRef, useState } from "react"
import { TRIE_COMMANDS, type CommandDef } from "@/settings/trieCommands"
import { useTrieCommandStore } from "@/store/trieCommandStore"
import { useAppStore } from "@/store/appStore"

// The trie command surface: pick a lifecycle command (sync / plan / verify /
// status / audit / refresh), tune its flags, run it, and watch live output.
// One run at a time — trie itself takes a write lock, so this mirrors reality.
type FlagValues = Record<string, boolean | number | string | undefined>

export function TriePanel() {
  const projectDir = useAppStore((s) => s.projectDir)
  const [selected, setSelected] = useState<string>(TRIE_COMMANDS[0].command)
  const [values, setValues] = useState<Record<string, FlagValues>>({})

  const running = useTrieCommandStore((s) => s.running)
  const activeCommand = useTrieCommandStore((s) => s.command)
  const exitCode = useTrieCommandStore((s) => s.exitCode)
  const output = useTrieCommandStore((s) => s.output)
  const error = useTrieCommandStore((s) => s.error)
  const run = useTrieCommandStore((s) => s.run)
  const cancel = useTrieCommandStore((s) => s.cancel)
  const clear = useTrieCommandStore((s) => s.clear)
  const subscribe = useTrieCommandStore((s) => s.subscribe)

  useEffect(() => subscribe(), [subscribe])

  const def = useMemo(
    () => TRIE_COMMANDS.find((c) => c.command === selected) ?? TRIE_COMMANDS[0],
    [selected],
  )
  const formValues = values[selected] ?? {}

  const setFlag = (key: string, v: boolean | number | string | undefined) =>
    setValues((prev) => ({ ...prev, [selected]: { ...(prev[selected] ?? {}), [key]: v } }))

  const onRun = () => {
    if (running) return
    run(selected, formValues)
  }

  return (
    <div className="flex flex-col h-full min-h-0" style={{ background: "var(--bg-app)" }}>
      {/* command picker */}
      <div className="shrink-0 px-4 py-2.5 border-b border-subtle flex items-center gap-3">
        <div className="flex-1 min-w-0">
          <h2 className="text-sm text-1 font-medium">trie commands</h2>
          <p className="text-[11px] text-3">Run trie lifecycle commands against this project.</p>
        </div>
        {running && activeCommand ? (
          <button
            className="rounded px-3 py-1 text-xs font-medium text-white transition-opacity hover:opacity-90"
            style={{ background: "var(--danger)" }}
            onClick={() => cancel()}
          >
            Stop
          </button>
        ) : (
          <button
            className="rounded px-3 py-1 text-xs font-medium bg-accent text-white disabled:opacity-50"
            onClick={onRun}
            disabled={!projectDir}
            title={projectDir ? `Run trie ${selected}` : "Open a project first"}
          >
            Run {def.title}
          </button>
        )}
      </div>

      <div className="flex-1 min-h-0 flex">
        {/* command list */}
        <div className="w-44 shrink-0 border-r border-subtle overflow-y-auto scroll-thin py-1">
          {TRIE_COMMANDS.map((c) => (
            <button
              key={c.command}
              className={`w-full text-left px-3 py-1.5 text-xs transition-colors border-l-2 ${
                selected === c.command
                  ? "text-1 surface-2 border-accent"
                  : "text-2 hover:text-1 border-transparent"
              }`}
              style={selected === c.command ? { borderColor: "var(--accent)" } : undefined}
              onClick={() => setSelected(c.command)}
            >
              <div className="flex items-center gap-1.5">
                <span className="font-mono">{c.command}</span>
                {c.command === activeCommand && running && (
                  <span
                    className="w-1.5 h-1.5 rounded-full trie-pulse"
                    style={{ background: "var(--accent)" }}
                  />
                )}
              </div>
            </button>
          ))}
        </div>

        {/* flags + output */}
        <div className="flex-1 min-w-0 flex flex-col min-h-0">
          <div className="shrink-0 px-4 py-3 border-b border-subtle">
            <p className="text-xs text-2 leading-snug">{def.description}</p>
            {def.costly && (
              <p
                className="text-[11px] mt-1.5 inline-flex items-center gap-1 rounded px-1.5 py-0.5"
                style={{
                  color: "#fcd34d",
                  background: "color-mix(in srgb, var(--warn) 12%, transparent)",
                }}
              >
                Makes paid LLM calls — cap with budget / limit.
              </p>
            )}
            {def.flags.length > 0 && (
              <div className="mt-3 grid grid-cols-2 gap-x-6 gap-y-2.5">
                {def.flags.map((f) => (
                  <FlagControl
                    key={f.key}
                    flag={f}
                    value={formValues[f.key]}
                    onChange={(v) => setFlag(f.key, v)}
                  />
                ))}
              </div>
            )}
          </div>

          {/* output */}
          <OutputView output={output} running={running} exitCode={exitCode} error={error} onClear={clear} />
        </div>
      </div>
    </div>
  )
}

function FlagControl({
  flag,
  value,
  onChange,
}: {
  flag: CommandDef["flags"][number]
  value: boolean | number | string | undefined
  onChange: (v: boolean | number | string | undefined) => void
}) {
  if (flag.type === "boolean") {
    return (
      <label className="flex items-center gap-2 cursor-pointer select-none">
        <button
          role="switch"
          aria-checked={Boolean(value)}
          onClick={() => onChange(!value)}
          className={`relative w-8 h-4.5 rounded-full transition-colors shrink-0 ${
            value ? "bg-accent" : "surface-3"
          }`}
          style={{ height: 18, width: 32 }}
        >
          <span
            className="absolute top-0.5 left-0.5 w-3.5 h-3.5 rounded-full bg-white transition-transform"
            style={{ transform: value ? "translateX(14px)" : "none" }}
          />
        </button>
        <span className="min-w-0">
          <span className="text-xs text-1 block truncate">{flag.label}</span>
          <span className="text-[10px] text-faint font-mono">{flag.flag}</span>
        </span>
      </label>
    )
  }

  if (flag.type === "enum") {
    return (
      <div className="min-w-0">
        <span className="text-xs text-1 block truncate mb-1">{flag.label}</span>
        <select
          className="w-full surface-2 border border-strong focus:border-accent-soft rounded px-2 py-1 text-xs text-1 outline-none"
          value={value === undefined ? "" : String(value)}
          onChange={(e) => onChange(e.target.value || undefined)}
        >
          <option value="">default</option>
          {(flag.enum ?? []).map((o) => (
            <option key={o.value} value={o.value}>
              {o.label}
            </option>
          ))}
        </select>
      </div>
    )
  }

  // number / string
  return (
    <div className="min-w-0">
      <span className="text-xs text-1 block truncate mb-1" title={flag.description}>
        {flag.label}
      </span>
      <input
        type={flag.type === "number" ? "number" : "text"}
        className="w-full surface-2 border border-strong focus:border-accent-soft rounded px-2 py-1 text-xs text-1 outline-none"
        placeholder={flag.placeholder ?? flag.flag}
        min={flag.min}
        step={flag.step}
        value={value === undefined ? "" : String(value)}
        onChange={(e) => {
          const raw = e.target.value
          if (raw === "") onChange(undefined)
          else onChange(flag.type === "number" ? Number(raw) : raw)
        }}
      />
    </div>
  )
}

function OutputView({
  output,
  running,
  exitCode,
  error,
  onClear,
}: {
  output: ReturnType<typeof useTrieCommandStore.getState>["output"]
  running: boolean
  exitCode: number | null
  error: string | null
  onClear: () => void
}) {
  const scrollRef = useRef<HTMLDivElement | null>(null)
  const [stick, setStick] = useState(true)

  useEffect(() => {
    if (stick && scrollRef.current) scrollRef.current.scrollTop = scrollRef.current.scrollHeight
  }, [output, stick])

  const onScroll = () => {
    const el = scrollRef.current
    if (!el) return
    setStick(el.scrollHeight - el.scrollTop - el.clientHeight < 40)
  }

  return (
    <div className="flex-1 min-h-0 flex flex-col">
      <div className="shrink-0 flex items-center justify-between px-4 py-1.5 border-b border-subtle">
        <div className="flex items-center gap-2 text-[11px]">
          <span className="text-3">Output</span>
          {running && (
            <span className="inline-flex items-center gap-1 text-accent" style={{ color: "var(--accent)" }}>
              <span
                className="w-2.5 h-2.5 border-2 rounded-full animate-spin"
                style={{ borderColor: "var(--border-strong)", borderTopColor: "var(--accent)" }}
              />
              running
            </span>
          )}
          {!running && exitCode != null && (
            <span style={{ color: exitCode === 0 ? "#34d399" : "var(--danger)" }}>
              {exitCode === 0 ? "✓ exit 0" : `✗ exit ${exitCode}`}
            </span>
          )}
        </div>
        {output.length > 0 && !running && (
          <button className="text-[11px] text-3 hover:text-1 transition-colors" onClick={onClear}>
            Clear
          </button>
        )}
      </div>
      <div
        ref={scrollRef}
        onScroll={onScroll}
        className="flex-1 min-h-0 overflow-y-auto scroll-thin px-4 py-2 font-mono text-[11px] leading-relaxed"
      >
        {output.length === 0 && !error ? (
          <p className="text-faint">No output yet. Pick a command and Run.</p>
        ) : (
          output.map((l, i) => (
            <div
              key={i}
              className="whitespace-pre-wrap break-words"
              style={{
                color:
                  l.stream === "stderr"
                    ? "#fda4af"
                    : l.stream === "system"
                      ? "var(--text-3)"
                      : "var(--text-1)",
              }}
            >
              {l.text}
            </div>
          ))
        )}
        {error && <div className="whitespace-pre-wrap" style={{ color: "var(--danger)" }}>{error}</div>}
      </div>
    </div>
  )
}
