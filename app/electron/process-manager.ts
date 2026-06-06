import { spawn, ChildProcess } from "child_process"
import { BrowserWindow, app } from "electron"
import * as net from "net"
import * as path from "path"
import * as fs from "fs"

export class ProcessManager {
  private opencodeProc: ChildProcess | null = null
  private opencodePort = 4096

  constructor(private win: BrowserWindow) {}

  async startForProject(projectDir: string): Promise<void> {
    // Kill any previously-spawned server before starting a new one. Without
    // this, a second open-project (re-open, StrictMode, retry) orphans the
    // prior opencode-server, leaking processes and ports.
    if (this.opencodeProc && !this.opencodeProc.killed) {
      try {
        this.opencodeProc.kill("SIGTERM")
      } catch {
        /* ignore */
      }
      this.opencodeProc = null
    }

    this.opencodePort = await findFreePort(4096)

    const { opencodeBin, trieMcpBin, trieCliBin } = resolveResourcePaths()

    // Write / merge an .opencode/opencode.json in the project directory so
    // opencode uses the bundled trie-mcp binary instead of whatever is on PATH.
    writeOpencodeConfig(projectDir, trieMcpBin)

    // Guarantee the graph is populated before the canvas queries it. A fresh
    // checkout (or a wiped/regenerated .trie/graph.db) leaves the graph empty,
    // which surfaces as "No system model loaded". `trie refresh` is the
    // freshness gate: cheap when fresh, a scan-only rebuild when the store is
    // empty (no LLM spend), and a sync when local edits drift prose. Run it
    // before signalling servers-ready, streaming JSONL progress to the
    // renderer's triefact-generation status display. Fire-and-forget: a
    // refresh failure must never block the app from opening.
    this.runRefresh(projectDir, trieCliBin)

    this.opencodeProc = spawn(
      opencodeBin,
      ["--port", String(this.opencodePort), "--hostname", "0.0.0.0"],
      {
        cwd: projectDir,
        env: { ...process.env },
        stdio: ["ignore", "pipe", "pipe"],
      }
    )

    const stderrLines: string[] = []
    let serverReady: (() => void) | null = null
    const readyPromise = new Promise<void>((resolve) => { serverReady = resolve })

    this.opencodeProc.stdout?.on("data", (d: Buffer) => {
      const text = d.toString()
      console.log("[opencode]", text.trimEnd())
      this.win.webContents.send("ipc:opencode-stdout", text)
      if (text.includes("opencode server listening")) {
        serverReady?.()
      }
    })

    this.opencodeProc.stderr?.on("data", (d: Buffer) => {
      const line = d.toString().trimEnd()
      console.error("[opencode stderr]", line)
      stderrLines.push(line)
      this.win.webContents.send("ipc:opencode-stderr", line)
    })

    this.opencodeProc.on("exit", (code) => {
      console.log("[opencode] exited with code", code)
      this.win.webContents.send("ipc:opencode-exited", { code })
    })

    const timeout = new Promise<void>((_, reject) =>
      setTimeout(() => reject(new Error("timeout")), 30_000)
    )

    try {
      await Promise.race([readyPromise, timeout])
    } catch {
      this.opencodeProc.kill()
      const detail = stderrLines.slice(-15).join("\n")
      throw new Error(
        `opencode server failed to start on port ${this.opencodePort}.\n\n${detail}`
      )
    }

    this.win.webContents.send("ipc:servers-ready", {
      opencodePort: this.opencodePort,
      projectDir,
    })
  }

  /**
   * Run `trie refresh --before-turn --json` in the project directory and relay
   * its JSONL progress stream to the renderer as `ipc:trie-refresh` events.
   *
   * The renderer's TriefactStatus component renders these. Each stdout line is
   * one JSON event ({"kind": "phase"|"start"|"done"|"skip"|"summary"|"error"}).
   * A trailing partial line is buffered across chunks. We never throw: a failed
   * refresh degrades to "graph may be stale", not a broken app launch.
   */
  private runRefresh(projectDir: string, trieCliBin: string): void {
    let proc: ChildProcess
    try {
      proc = spawn(trieCliBin, ["refresh", "--before-turn", "--json"], {
        cwd: projectDir,
        env: { ...process.env },
        stdio: ["ignore", "pipe", "pipe"],
      })
    } catch (err) {
      this.win.webContents.send("ipc:trie-refresh", {
        kind: "error",
        message: `failed to spawn trie refresh: ${String(err)}`,
      })
      return
    }

    this.win.webContents.send("ipc:trie-refresh", { kind: "spawned" })

    let buf = ""
    proc.stdout?.on("data", (d: Buffer) => {
      buf += d.toString()
      const lines = buf.split("\n")
      buf = lines.pop() ?? ""
      for (const line of lines) {
        const trimmed = line.trim()
        if (!trimmed) continue
        try {
          this.win.webContents.send("ipc:trie-refresh", JSON.parse(trimmed))
        } catch {
          // Non-JSON line (stray stderr-on-stdout); ignore.
        }
      }
    })

    const stderrLines: string[] = []
    proc.stderr?.on("data", (d: Buffer) => {
      stderrLines.push(d.toString().trimEnd())
    })

    proc.on("exit", (code) => {
      // Flush any buffered final line.
      const trimmed = buf.trim()
      if (trimmed) {
        try {
          this.win.webContents.send("ipc:trie-refresh", JSON.parse(trimmed))
        } catch {
          /* ignore */
        }
      }
      this.win.webContents.send("ipc:trie-refresh", {
        kind: "exit",
        code: code ?? 0,
        stderr: code && code !== 0 ? stderrLines.slice(-10).join("\n") : undefined,
      })
    })

    proc.on("error", (err) => {
      this.win.webContents.send("ipc:trie-refresh", {
        kind: "error",
        message: String(err),
      })
    })
  }

  killAll(): void {
    if (this.opencodeProc && !this.opencodeProc.killed) {
      this.opencodeProc.kill("SIGTERM")
    }
  }

  getOpenCodePort(): number {
    return this.opencodePort
  }
}

// ---------------------------------------------------------------------------
// Write .opencode/opencode.json pointing trie MCP at the bundled binary.
// Merges with any existing config so user customisations are preserved.
// ---------------------------------------------------------------------------
function writeOpencodeConfig(projectDir: string, trieMcpBin: string): void {
  const configDir = path.join(projectDir, ".opencode")
  const configPath = path.join(configDir, "opencode.json")

  let existing: Record<string, unknown> = {}
  if (fs.existsSync(configPath)) {
    try {
      existing = JSON.parse(fs.readFileSync(configPath, "utf-8")) as Record<string, unknown>
    } catch {
      // malformed — start fresh
    }
  } else {
    fs.mkdirSync(configDir, { recursive: true })
  }

  const mcp = (existing.mcp as Record<string, unknown> | undefined) ?? {}

  const merged = {
    ...existing,
    mcp: {
      ...mcp,
      trie: {
        type: "local",
        command: [trieMcpBin, projectDir],
        enabled: true,
      },
    },
  }

  fs.writeFileSync(configPath, JSON.stringify(merged, null, 2) + "\n")
  console.log("[trie] wrote opencode config:", configPath)
}

// ---------------------------------------------------------------------------
// Resource path resolution
// ---------------------------------------------------------------------------
function resolveResourcePaths(): { opencodeBin: string; trieMcpBin: string; trieCliBin: string } {
  let resourcesDir: string

  if (app.isPackaged) {
    resourcesDir = process.resourcesPath
  } else {
    // Walk up from __dirname (out/main/) to find app/resources/
    let dir = __dirname
    resourcesDir = path.join(__dirname, "..", "..", "resources") // fallback
    for (let i = 0; i < 6; i++) {
      const candidate = path.join(dir, "resources")
      if (
        fs.existsSync(path.join(candidate, "opencode-server")) &&
        fs.existsSync(path.join(candidate, "trie-mcp"))
      ) {
        resourcesDir = candidate
        break
      }
      dir = path.dirname(dir)
    }
  }

  const opencodeBin = path.join(resourcesDir, "opencode-server")
  const trieMcpBin  = path.join(resourcesDir, "trie-mcp")
  const trieCliBin  = path.join(resourcesDir, "trie-cli")

  for (const bin of [opencodeBin, trieMcpBin]) {
    if (!fs.existsSync(bin)) {
      throw new Error(
        `Bundled binary not found: ${bin}\n` +
        `Run \`npm run build:resources\` from app/ to build the sidecars.`
      )
    }
    fs.chmodSync(bin, 0o755)
  }

  // trie-cli is best-effort: the app still opens (graph just won't auto-refresh)
  // if it's missing. Chmod when present; don't hard-fail when absent.
  if (fs.existsSync(trieCliBin)) {
    fs.chmodSync(trieCliBin, 0o755)
  } else {
    console.warn("[trie] trie-cli wrapper not found; startup auto-refresh disabled:", trieCliBin)
  }

  console.log("[trie] opencode-server:", opencodeBin)
  console.log("[trie] trie-mcp:", trieMcpBin)
  console.log("[trie] trie-cli:", trieCliBin)

  return { opencodeBin, trieMcpBin, trieCliBin }
}

// ---------------------------------------------------------------------------
// Port utilities — use net.createServer to probe, not TCP connect.
// TCP connect to 127.0.0.1 fails on this machine; binding a server works.
// ---------------------------------------------------------------------------

/**
 * Find a free port starting from `preferred`.
 * Uses net.createServer().listen() to probe — works even when
 * TCP connects to 127.0.0.1 are blocked by the OS/firewall.
 */
function findFreePort(preferred: number): Promise<number> {
  return new Promise((resolve) => {
    const server = net.createServer()
    server.unref()
    server.on("error", () => {
      // preferred is in use — let OS pick one
      const fallback = net.createServer()
      fallback.unref()
      fallback.listen(0, "0.0.0.0", () => {
        const { port } = fallback.address() as net.AddressInfo
        fallback.close(() => resolve(port))
      })
    })
    server.listen(preferred, "0.0.0.0", () => {
      server.close(() => resolve(preferred))
    })
  })
}
