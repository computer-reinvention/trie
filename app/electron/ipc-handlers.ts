import { ipcMain, dialog, app } from "electron"
import { readdir, readFile } from "fs/promises"
import { join } from "path"
import * as http from "http"
import type { ProcessManager } from "./process-manager"
import { readOpencodeConfig, writeOpencodeConfig } from "./opencode-config"
import { readTrieConfig, writeTrieConfig, trieConfigExists } from "./trie-config"
import { TrieCommandRunner } from "./trie-command"
import {
  listProviderKeys,
  hasProviderKey,
  setProviderKey,
  deleteProviderKey,
} from "./provider-keys"

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
  // Per-request timeout. opencode operations (graph queries, session writes)
  // should complete in well under this; a request that hangs longer than this
  // is treated as a failure so the renderer's promise never dangles forever.
  const HTTP_REQUEST_TIMEOUT_MS = 30_000

  ipcMain.handle("http-request", async (_event, opts: {
    method: string
    url: string
    headers?: Record<string, string>
    body?: string
    timeoutMs?: number
  }) => {
    return new Promise<{ status: number; body: string }>((resolve) => {
      const url = new URL(opts.url)
      const reqOpts: http.RequestOptions = {
        hostname: url.hostname,
        // Default to the opencode port, not 80 — every URL we proxy is the
        // local opencode server. A portless URL almost certainly means a
        // mis-constructed base, so fall back to the live server port.
        port: url.port ? parseInt(url.port) : pm.getOpenCodePort(),
        path: url.pathname + url.search,
        method: opts.method,
        headers: { "Content-Type": "application/json", ...(opts.headers ?? {}) },
      }
      let settled = false
      const req = http.request(reqOpts, (res) => {
        let data = ""
        res.on("data", (chunk) => { data += chunk })
        res.on("end", () => {
          if (settled) return
          settled = true
          resolve({ status: res.statusCode ?? 200, body: data })
        })
      })
      // Guard against a hung connection: abort after the timeout and surface a
      // synthetic 504 so callers can show "request timed out" instead of
      // spinning forever.
      req.setTimeout(opts.timeoutMs ?? HTTP_REQUEST_TIMEOUT_MS, () => {
        if (settled) return
        settled = true
        req.destroy()
        resolve({ status: 504, body: JSON.stringify({ error: "request timed out" }) })
      })
      // A connection-level failure (server down / refused) resolves as a
      // synthetic 503 rather than rejecting. Rejecting forces every caller to
      // wrap each call in try/catch or risk an unhandled rejection; a uniform
      // status code lets the clients treat "server unreachable" like any other
      // non-2xx.
      req.on("error", (err) => {
        if (settled) return
        settled = true
        resolve({ status: 503, body: JSON.stringify({ error: String(err) }) })
      })
      if (opts.body) req.write(opts.body)
      req.end()
    })
  })

  // ---------------------------------------------------------------------------
  // SSE proxy — subscribe to opencode's /desktop/event stream from main
  // process and relay events to the renderer via ipc.
  //
  // The renderer effect that drives this subscribes/unsubscribes more than
  // once during startup: React StrictMode double-invokes effects, and the
  // `opencodePort` dep flips 0 -> realPort once servers are ready. Without a
  // guard, a stale unsubscribe (from the prior mount's cleanup) destroys the
  // live request opened by the newer mount — the stream connects then drops
  // and never comes back. We defend with a monotonic generation token: only
  // the current generation may tear down the socket, and reconnects re-check
  // their generation before retrying. The upstream also closes its bus
  // subscription when the socket drops, so reconnecting re-establishes it.
  // ---------------------------------------------------------------------------
  let sseReq: http.ClientRequest | null = null
  let sseGeneration = 0
  let sseUrl: string | null = null
  let sseReconnectTimer: NodeJS.Timeout | null = null

  function relayToRenderers(channel: string, payload: string): void {
    const { BrowserWindow } = require("electron")
    for (const win of BrowserWindow.getAllWindows()) {
      win.webContents.send(channel, payload)
    }
  }

  function openSseStream(generation: number): void {
    if (generation !== sseGeneration || !sseUrl) return

    const parsed = new URL(sseUrl)
    const opts: http.RequestOptions = {
      hostname: parsed.hostname,
      port: parseInt(parsed.port || "80"),
      path: parsed.pathname + parsed.search,
      method: "GET",
      headers: { Accept: "text/event-stream", "Cache-Control": "no-cache" },
    }

    const scheduleReconnect = () => {
      // Only the live generation reconnects, and only if not torn down.
      if (generation !== sseGeneration || !sseUrl) return
      if (sseReconnectTimer) return
      sseReconnectTimer = setTimeout(() => {
        sseReconnectTimer = null
        openSseStream(generation)
      }, 1000)
    }

    const req = http.request(opts, (res) => {
      let buf = ""
      res.on("data", (chunk: Buffer) => {
        buf += chunk.toString()
        const lines = buf.split("\n")
        buf = lines.pop() ?? ""
        for (const line of lines) {
          if (line.startsWith("data: ")) relayToRenderers("sse-event", line.slice(6))
        }
      })
      res.on("error", (err) => {
        relayToRenderers("sse-error", err.message)
        scheduleReconnect()
      })
      // Upstream closed the stream (server shutdown, idle GC, etc.) — retry.
      res.on("end", scheduleReconnect)
      res.on("close", scheduleReconnect)
    })
    req.on("error", () => { scheduleReconnect() })
    req.end()
    sseReq = req
  }

  ipcMain.handle("sse-subscribe", (_event, url: string) => {
    // Bump the generation: any in-flight reconnect/teardown from a prior
    // subscription is now stale and becomes a no-op.
    sseGeneration += 1
    const generation = sseGeneration
    if (sseReconnectTimer) { clearTimeout(sseReconnectTimer); sseReconnectTimer = null }
    if (sseReq) { sseReq.destroy(); sseReq = null }
    sseUrl = url
    openSseStream(generation)
    return { ok: true }
  })

  ipcMain.handle("sse-unsubscribe", () => {
    // Invalidate the current generation so no reconnect fires, then tear down.
    sseGeneration += 1
    if (sseReconnectTimer) { clearTimeout(sseReconnectTimer); sseReconnectTimer = null }
    sseReq?.destroy()
    sseReq = null
    sseUrl = null
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

  // ---------------------------------------------------------------------------
  // Settings — VS Code-style flat key/value config persisted in prefs.json
  // under a `settings` namespace. The renderer owns the schema/defaults.
  // ---------------------------------------------------------------------------
  ipcMain.handle("settings-get-all", () => {
    const prefs = readPrefs()
    return (prefs["settings"] as Record<string, unknown> | undefined) ?? {}
  })

  ipcMain.handle("settings-set", (_event, key: string, value: unknown) => {
    const prefs = readPrefs()
    const settings = (prefs["settings"] as Record<string, unknown> | undefined) ?? {}
    if (value === undefined || value === null) delete settings[key]
    else settings[key] = value
    writePrefs({ ...prefs, settings })
    return { ok: true }
  })

  ipcMain.handle("settings-reset", () => {
    const prefs = readPrefs()
    writePrefs({ ...prefs, settings: {} })
    return { ok: true }
  })

  // ---------------------------------------------------------------------------
  // opencode.json — read the project's config (effective values for the UI) and
  // merge-write a delta of app-managed keys, preserving hand-authored keys and
  // always re-asserting the trie MCP entry. Per-project scope.
  // ---------------------------------------------------------------------------
  ipcMain.handle("opencode-config-read", (_event, projectDir: string) => {
    return readOpencodeConfig(projectDir)
  })

  ipcMain.handle(
    "opencode-config-write",
    (_event, projectDir: string, delta: Record<string, unknown>) => {
      const trie = pm.getTrieMcpEntry() ?? { trieMcpBin: "trie-mcp", projectDir }
      writeOpencodeConfig(projectDir, delta, { ...trie, projectDir })
      return { ok: true }
    },
  )

  ipcMain.handle("opencode-restart", async () => {
    await pm.restart()
    return { ok: true }
  })

  // ---------------------------------------------------------------------------
  // trie.toml — read the project's trie config and merge-write a delta of
  // changed keys, preserving hand-authored keys. Per-project scope. The
  // renderer's trie settings UI is the source of truth for managed keys.
  // ---------------------------------------------------------------------------
  ipcMain.handle("trie-config-read", (_event, projectDir: string) => {
    return { exists: trieConfigExists(projectDir), config: readTrieConfig(projectDir) }
  })

  ipcMain.handle(
    "trie-config-write",
    (_event, projectDir: string, delta: Record<string, unknown>) => {
      try {
        writeTrieConfig(projectDir, delta)
        return { ok: true }
      } catch (err) {
        return { ok: false, error: String(err) }
      }
    },
  )

  // ---------------------------------------------------------------------------
  // trie CLI commands — run a trie subcommand (sync / plan / verify / status /
  // audit / refresh) in the open project, streaming lifecycle events to the
  // renderer over `ipc:trie-command`. One run at a time; a new run cancels the
  // previous. trie itself takes a write lock, so overlap would exit-2 anyway.
  // ---------------------------------------------------------------------------
  const trieRunner = new TrieCommandRunner(
    () => pm.getProjectDir(),
    () => pm.getTrieCliBin(),
  )

  ipcMain.handle(
    "trie-command-run",
    (_event, spec: { command: string; args?: string[]; json?: boolean }) => {
      try {
        return { ok: true, ...trieRunner.start(spec) }
      } catch (err) {
        return { ok: false, error: String(err) }
      }
    },
  )

  ipcMain.handle("trie-command-cancel", () => {
    trieRunner.cancel()
    return { ok: true }
  })

  ipcMain.handle("trie-command-running", () => ({ running: trieRunner.isRunning() }))

  // ---------------------------------------------------------------------------
  // Provider API keys — stored in the Keychain, injected as env vars at spawn.
  // ---------------------------------------------------------------------------
  ipcMain.handle("provider-keys-list", () => listProviderKeys())
  ipcMain.handle("provider-key-has", (_e, provider: string) => hasProviderKey(provider))
  ipcMain.handle(
    "provider-key-set",
    (_e, provider: string, key: string, envVar?: string) =>
      setProviderKey(provider, key, envVar),
  )
  ipcMain.handle("provider-key-delete", (_e, provider: string) => deleteProviderKey(provider))

  // ---------------------------------------------------------------------------
  // AGM frozen-layout snapshots — per opencode session, persisted in the
  // project's .trie/agm-snapshots.json (gitignored, project-scoped, rebuildable).
  // The renderer saves the final layout when a turn ends and restores it (no
  // decay replay) when a session is opened/switched, so a restarted editor shows
  // the chat AND its attention map.
  // ---------------------------------------------------------------------------
  const snapPath = (projectDir: string) => join(projectDir, ".trie", "agm-snapshots.json")
  ipcMain.handle("agm-snapshot-get", (_e, projectDir: string, sessionId: string) => {
    try {
      const all = JSON.parse(readFileSync(snapPath(projectDir), "utf-8")) as Record<string, unknown>
      return all[sessionId] ?? null
    } catch {
      return null
    }
  })
  ipcMain.handle(
    "agm-snapshot-set",
    (_e, projectDir: string, sessionId: string, snapshot: unknown) => {
      try {
        mkdirSync(join(projectDir, ".trie"), { recursive: true })
        let all: Record<string, unknown> = {}
        try {
          all = JSON.parse(readFileSync(snapPath(projectDir), "utf-8"))
        } catch {
          all = {}
        }
        all[sessionId] = snapshot
        // cap: keep the 40 most-recent sessions to bound the file
        const keys = Object.keys(all)
        if (keys.length > 40) {
          for (const k of keys.slice(0, keys.length - 40)) delete all[k]
        }
        writeFileSync(snapPath(projectDir), JSON.stringify(all))
        return { ok: true }
      } catch {
        return { ok: false }
      }
    },
  )

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
