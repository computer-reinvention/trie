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

    const { opencodeBin, trieMcpBin } = resolveResourcePaths()

    // Write / merge an .opencode/opencode.json in the project directory so
    // opencode uses the bundled trie-mcp binary instead of whatever is on PATH.
    writeOpencodeConfig(projectDir, trieMcpBin)

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
function resolveResourcePaths(): { opencodeBin: string; trieMcpBin: string } {
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

  for (const bin of [opencodeBin, trieMcpBin]) {
    if (!fs.existsSync(bin)) {
      throw new Error(
        `Bundled binary not found: ${bin}\n` +
        `Run \`npm run build:resources\` from app/ to build the sidecars.`
      )
    }
    fs.chmodSync(bin, 0o755)
  }

  console.log("[trie] opencode-server:", opencodeBin)
  console.log("[trie] trie-mcp:", trieMcpBin)

  return { opencodeBin, trieMcpBin }
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
