import { spawn, type ChildProcess } from "child_process"
import * as fs from "fs"
import { BrowserWindow } from "electron"

// ---------------------------------------------------------------------------
// Generic trie-cli command runner.
//
// Spawns the bundled `trie-cli` with an arbitrary subcommand + args in the
// project directory, and relays its lifecycle to the renderer over a single
// `ipc:trie-command` channel keyed by a per-run `runId`:
//
//   { runId, kind: "spawned" }
//   { runId, kind: "stdout"|"stderr", line }     one line at a time
//   { runId, kind: "json", event }               parsed JSON line (--json runs)
//   { runId, kind: "exit", code }
//   { runId, kind: "error", message }
//
// Only one run executes at a time per project (sync/refresh take the same write
// lock in trie itself; running two would exit-2 anyway). A new run cancels the
// previous one so the UI never stacks concurrent commands.
// ---------------------------------------------------------------------------

interface RunSpec {
  /** trie subcommand, e.g. "sync" or "refresh". */
  command: string
  /** Extra args after the subcommand, e.g. ["--all", "--limit", "10"]. */
  args?: string[]
  /** Parse stdout lines as JSON (commands invoked with --json). */
  json?: boolean
}

export class TrieCommandRunner {
  private proc: ChildProcess | null = null
  private currentRunId = 0

  constructor(
    private getProjectDir: () => string | null,
    private getTrieCliBin: () => string,
  ) {}

  private broadcast(payload: Record<string, unknown>): void {
    for (const win of BrowserWindow.getAllWindows()) {
      win.webContents.send("ipc:trie-command", payload)
    }
  }

  /** True while a command is executing. */
  isRunning(): boolean {
    return this.proc != null && !this.proc.killed
  }

  /** Cancel the in-flight command, if any. */
  cancel(): void {
    if (this.proc && !this.proc.killed) {
      try {
        this.proc.kill("SIGTERM")
      } catch {
        /* ignore */
      }
    }
  }

  /**
   * Start a command. Returns the new runId (renderer correlates events by it).
   * Throws synchronously on a precondition failure (no project, missing binary)
   * so the IPC handler can surface it as a rejected invoke.
   */
  start(spec: RunSpec): { runId: number } {
    const projectDir = this.getProjectDir()
    if (!projectDir) throw new Error("No project open.")
    const bin = this.getTrieCliBin()
    if (!fs.existsSync(bin)) {
      throw new Error(
        "trie-cli wrapper not found in app resources. Rebuild sidecars (npm run build:resources).",
      )
    }

    // Cancel any previous run so commands never overlap.
    this.cancel()

    const runId = ++this.currentRunId
    const args = [spec.command, ...(spec.args ?? [])]

    let proc: ChildProcess
    try {
      proc = spawn(bin, args, {
        cwd: projectDir,
        env: { ...process.env },
        stdio: ["ignore", "pipe", "pipe"],
      })
    } catch (err) {
      this.broadcast({ runId, kind: "error", message: String(err) })
      throw err instanceof Error ? err : new Error(String(err))
    }
    this.proc = proc

    this.broadcast({ runId, kind: "spawned", command: spec.command, args })

    // Buffer stdout across chunks; emit complete lines. In JSON mode, parse each
    // line and emit a `json` event (falling back to a raw `stdout` line if it
    // isn't valid JSON — e.g. a stray Rich line that leaked onto stdout).
    let outBuf = ""
    proc.stdout?.on("data", (d: Buffer) => {
      outBuf += d.toString()
      const lines = outBuf.split("\n")
      outBuf = lines.pop() ?? ""
      for (const line of lines) this.emitLine(runId, line, spec.json)
    })

    const errLines: string[] = []
    let errBuf = ""
    proc.stderr?.on("data", (d: Buffer) => {
      errBuf += d.toString()
      const lines = errBuf.split("\n")
      errBuf = lines.pop() ?? ""
      for (const line of lines) {
        if (!line.trim()) continue
        errLines.push(line)
        this.broadcast({ runId, kind: "stderr", line })
      }
    })

    proc.on("exit", (code) => {
      // Flush any trailing partial lines.
      if (outBuf.trim()) this.emitLine(runId, outBuf, spec.json)
      if (errBuf.trim()) this.broadcast({ runId, kind: "stderr", line: errBuf })
      this.broadcast({
        runId,
        kind: "exit",
        code: code ?? 0,
        stderr: code && code !== 0 ? errLines.slice(-15).join("\n") : undefined,
      })
      if (this.proc === proc) this.proc = null
    })

    proc.on("error", (err) => {
      this.broadcast({ runId, kind: "error", message: String(err) })
      if (this.proc === proc) this.proc = null
    })

    return { runId }
  }

  private emitLine(runId: number, line: string, json?: boolean): void {
    const trimmed = line.trim()
    if (!trimmed) return
    if (json) {
      try {
        this.broadcast({ runId, kind: "json", event: JSON.parse(trimmed) })
        return
      } catch {
        // not JSON — fall through to a raw stdout line
      }
    }
    this.broadcast({ runId, kind: "stdout", line })
  }
}
