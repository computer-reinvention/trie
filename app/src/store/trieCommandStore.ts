import { create } from "zustand"
import { TRIE_COMMANDS, buildArgs, type CommandDef } from "@/settings/trieCommands"

// eslint-disable-next-line @typescript-eslint/no-explicit-any
const trie = () => (window as any).trie

export interface OutputLine {
  stream: "stdout" | "stderr" | "system"
  text: string
}

/** Fired when a command finishes. Listeners react to side-effects (e.g. init /
 *  sync / refresh changed the graph → repopulate; init created trie.toml →
 *  reload config). `ok` is true only on a clean exit 0. */
export type CommandCompleteListener = (info: { command: string; ok: boolean }) => void

interface TrieCommandStore {
  /** runId of the active/last run, or null. */
  runId: number | null
  command: string | null
  running: boolean
  /** Exit code of the last completed run, null while running / never run. */
  exitCode: number | null
  output: OutputLine[]
  /** Parsed JSON events from --json commands, for structured progress. */
  jsonEvents: Record<string, unknown>[]
  error: string | null
  /** Whether the global IPC listener is wired. */
  subscribed: boolean
  /** Completion listeners (registered by App / Settings). */
  completeListeners: Set<CommandCompleteListener>

  subscribe: () => void
  onComplete: (cb: CommandCompleteListener) => () => void
  run: (command: string, values: Record<string, boolean | number | string | undefined>) => Promise<void>
  cancel: () => Promise<void>
  clear: () => void
}

function defFor(command: string): CommandDef | undefined {
  return TRIE_COMMANDS.find((c) => c.command === command)
}

export const useTrieCommandStore = create<TrieCommandStore>((set, get) => ({
  runId: null,
  command: null,
  running: false,
  exitCode: null,
  output: [],
  jsonEvents: [],
  error: null,
  subscribed: false,
  completeListeners: new Set(),

  onComplete: (cb) => {
    get().completeListeners.add(cb)
    return () => get().completeListeners.delete(cb)
  },

  subscribe: () => {
    if (get().subscribed) return
    const t = trie()
    if (!t?.trieCommand?.onEvent) return
    t.trieCommand.onEvent((ev: Record<string, unknown>) => {
      const s = get()
      // Ignore events from a superseded run (a newer run cancelled this one).
      if (typeof ev.runId === "number" && s.runId != null && ev.runId !== s.runId) return
      const kind = ev.kind as string
      if (kind === "spawned") {
        return
      }
      if (kind === "stdout") {
        set((st) => ({ output: [...st.output, { stream: "stdout", text: String(ev.line ?? "") }] }))
      } else if (kind === "stderr") {
        set((st) => ({ output: [...st.output, { stream: "stderr", text: String(ev.line ?? "") }] }))
      } else if (kind === "json") {
        const event = ev.event as Record<string, unknown>
        set((st) => ({
          jsonEvents: [...st.jsonEvents, event],
          // Also surface a readable line so the raw log stays useful.
          output: [...st.output, { stream: "stdout", text: summariseJson(event) }],
        }))
      } else if (kind === "exit") {
        const code = (ev.code as number) ?? 0
        const finishedCommand = get().command
        set((st) => ({
          running: false,
          exitCode: code,
          output:
            code !== 0 && ev.stderr
              ? [...st.output, { stream: "stderr", text: String(ev.stderr) }]
              : st.output,
        }))
        // Notify listeners so the graph/config can refresh after a state-changing
        // command. Errors in a listener must not break the others.
        if (finishedCommand) {
          for (const cb of get().completeListeners) {
            try {
              cb({ command: finishedCommand, ok: code === 0 })
            } catch {
              /* ignore listener error */
            }
          }
        }
      } else if (kind === "error") {
        set((st) => ({
          running: false,
          error: String(ev.message ?? "command error"),
          output: [...st.output, { stream: "system", text: String(ev.message ?? "error") }],
        }))
      }
    })
    set({ subscribed: true })
  },

  run: async (command, values) => {
    get().subscribe()
    const def = defFor(command)
    if (!def) return
    const args = buildArgs(def, values)
    if (def.json) args.push("--json")
    // Reset output for the new run.
    set({
      running: true,
      command,
      exitCode: null,
      error: null,
      output: [{ stream: "system", text: `$ trie ${command} ${args.join(" ")}`.trimEnd() }],
      jsonEvents: [],
    })
    try {
      const res = (await trie().trieCommand.run({ command, args, json: def.json })) as {
        ok: boolean
        runId?: number
        error?: string
      }
      if (!res?.ok) {
        set({ running: false, error: res?.error ?? "Failed to start command" })
        return
      }
      set({ runId: res.runId ?? null })
    } catch (err) {
      set({ running: false, error: String(err) })
    }
  },

  cancel: async () => {
    try {
      await trie().trieCommand.cancel()
    } catch {
      /* best-effort */
    }
    set((st) => ({
      running: false,
      output: [...st.output, { stream: "system", text: "— cancelled —" }],
    }))
  },

  clear: () =>
    set({ output: [], jsonEvents: [], exitCode: null, error: null, command: null, runId: null }),
}))

// Compress a JSONL refresh/status event into a one-line human summary.
function summariseJson(ev: Record<string, unknown>): string {
  const kind = ev.kind as string | undefined
  if (kind === "phase") return `▸ ${ev.phase ?? "phase"}${ev.mode ? ` (${ev.mode})` : ""}`
  if (kind === "start") return `  syncing ${ev.file ?? ev.rel_path ?? "…"}`
  if (kind === "done") return `  ✓ ${ev.file ?? ev.rel_path ?? "done"}`
  if (kind === "skip") return `  · skip ${ev.file ?? ev.rel_path ?? ""} (${ev.reason ?? ""})`
  if (kind === "summary")
    return `summary: ${ev.refreshed ? "refreshed" : "no change"}${ev.reason ? ` (${ev.reason})` : ""}`
  if (kind === "error") return `error: ${ev.message ?? ""}`
  // Fallback: compact JSON.
  return JSON.stringify(ev)
}
