import { ipcMain, dialog, app } from "electron"
import { readdir, readFile } from "fs/promises"
import { join } from "path"
import * as http from "http"
import type { ProcessManager } from "./process-manager"

let keytarModule: typeof import("keytar") | null = null
async function getKeytar() {
  if (!keytarModule) {
    keytarModule = await import("keytar")
  }
  return keytarModule
}

const KEYCHAIN_SERVICE = "ai.trie.app"
const RECENT_PROJECTS_KEY = "recent-projects"

// Simple JSON-file store for non-secret preferences
import { existsSync, readFileSync, writeFileSync, mkdirSync } from "fs"
const prefsPath = join(app.getPath("userData"), "prefs.json")

function readPrefs(): Record<string, unknown> {
  try {
    return JSON.parse(readFileSync(prefsPath, "utf-8"))
  } catch {
    return {}
  }
}

function writePrefs(data: Record<string, unknown>): void {
  mkdirSync(join(app.getPath("userData")), { recursive: true })
  writeFileSync(prefsPath, JSON.stringify(data, null, 2))
}

export function registerIpcHandlers(pm: ProcessManager): void {

  // ---------------------------------------------------------------------------
  // HTTP proxy — renderer cannot reach 127.0.0.1 directly on this machine.
  // All fetch calls go through here instead.
  // ---------------------------------------------------------------------------
  ipcMain.handle("http-request", async (_event, opts: {
    method: string
    url: string
    headers?: Record<string, string>
    body?: string
  }) => {
    return new Promise<{ status: number; body: string }>((resolve, reject) => {
      const url = new URL(opts.url)
      const reqOpts: http.RequestOptions = {
        hostname: url.hostname,
        port: url.port ? parseInt(url.port) : 80,
        path: url.pathname + url.search,
        method: opts.method,
        headers: { "Content-Type": "application/json", ...(opts.headers ?? {}) },
      }
      const req = http.request(reqOpts, (res) => {
        let data = ""
        res.on("data", (chunk) => { data += chunk })
        res.on("end", () => resolve({ status: res.statusCode ?? 200, body: data }))
      })
      req.on("error", reject)
      if (opts.body) req.write(opts.body)
      req.end()
    })
  })

  // ---------------------------------------------------------------------------
  // SSE proxy — subscribe to opencode's /desktop/event stream from main
  // process and relay events to the renderer via ipc.
  // ---------------------------------------------------------------------------
  let sseReq: http.ClientRequest | null = null

  ipcMain.handle("sse-subscribe", (_event, url: string) => {
    if (sseReq) { sseReq.destroy(); sseReq = null }

    const parsed = new URL(url)
    const opts: http.RequestOptions = {
      hostname: parsed.hostname,
      port: parseInt(parsed.port || "80"),
      path: parsed.pathname + parsed.search,
      method: "GET",
      headers: { Accept: "text/event-stream", "Cache-Control": "no-cache" },
    }

    sseReq = http.request(opts, (res) => {
      let buf = ""
      res.on("data", (chunk: Buffer) => {
        buf += chunk.toString()
        const lines = buf.split("\n")
        buf = lines.pop() ?? ""
        for (const line of lines) {
          if (line.startsWith("data: ")) {
            // Relay to all renderer windows
            const { BrowserWindow } = require("electron")
            for (const win of BrowserWindow.getAllWindows()) {
              win.webContents.send("sse-event", line.slice(6))
            }
          }
        }
      })
      res.on("error", (err) => {
        const { BrowserWindow } = require("electron")
        for (const win of BrowserWindow.getAllWindows()) {
          win.webContents.send("sse-error", err.message)
        }
      })
    })
    sseReq.on("error", () => { /* will reconnect from renderer */ })
    sseReq.end()
    return { ok: true }
  })

  ipcMain.handle("sse-unsubscribe", () => {
    sseReq?.destroy()
    sseReq = null
    return { ok: true }
  })

  // Open project dialog
  ipcMain.handle("show-open-dialog", async () => {
    const result = await dialog.showOpenDialog({
      properties: ["openDirectory"],
      title: "Open Project",
    })
    return result.canceled ? null : result.filePaths[0]
  })

  // Open project — spawn opencode for the chosen directory
  ipcMain.handle("open-project", async (_event, dir: string) => {
    // Save to recent projects
    const prefs = readPrefs()
    const recent = (prefs["recent-projects"] as string[] | undefined) ?? []
    const updated = [dir, ...recent.filter((p) => p !== dir)].slice(0, 10)
    writePrefs({ ...prefs, "recent-projects": updated })

    await pm.startForProject(dir)
    return { ok: true }
  })

  // Recent projects
  ipcMain.handle("get-recent-projects", () => {
    const prefs = readPrefs()
    return (prefs["recent-projects"] as string[] | undefined) ?? []
  })

  // API key — stored in macOS Keychain
  ipcMain.handle("get-api-key", async (_event, provider: string) => {
    try {
      const keytar = await getKeytar()
      return keytar.getPassword(KEYCHAIN_SERVICE, provider)
    } catch {
      return null
    }
  })

  ipcMain.handle("set-api-key", async (_event, provider: string, key: string) => {
    try {
      const keytar = await getKeytar()
      await keytar.setPassword(KEYCHAIN_SERVICE, provider, key)
      return { ok: true }
    } catch (err) {
      return { ok: false, error: String(err) }
    }
  })

  // File system helpers for sidebar
  ipcMain.handle("read-dir", async (_event, dir: string) => {
    const entries = await readdir(dir, { withFileTypes: true })
    return entries.map((e) => ({
      name: e.name,
      isDirectory: e.isDirectory(),
      path: join(dir, e.name),
    }))
  })

  ipcMain.handle("read-file", async (_event, filePath: string) => {
    return readFile(filePath, "utf-8")
  })
}
