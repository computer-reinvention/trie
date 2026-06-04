import { contextBridge, ipcRenderer } from "electron"

contextBridge.exposeInMainWorld("trie", {
  // Lifecycle
  openProject: (dir: string) => ipcRenderer.invoke("open-project", dir),
  getRecentProjects: () => ipcRenderer.invoke("get-recent-projects"),
  showOpenDialog: () => ipcRenderer.invoke("show-open-dialog"),

  // Server discovery — fires once per project open; use once() to avoid
  // accumulating listeners across hot reloads in dev.
  onServersReady: (cb: (ports: { opencodePort: number; projectDir: string }) => void) => {
    // Remove any previous listener before adding a new one so hot-reload
    // in dev doesn't stack them up.
    ipcRenderer.removeAllListeners("ipc:servers-ready")
    ipcRenderer.on("ipc:servers-ready", (_event, v) => cb(v))
  },

  // HTTP proxy — routes fetch calls through main process (127.0.0.1 unreachable from renderer)
  httpRequest: (opts: { method: string; url: string; headers?: Record<string, string>; body?: string }) =>
    ipcRenderer.invoke("http-request", opts),

  // SSE proxy — main process subscribes and relays events to renderer
  sseSubscribe: (url: string) => ipcRenderer.invoke("sse-subscribe", url),
  sseUnsubscribe: () => ipcRenderer.invoke("sse-unsubscribe"),
  onSseEvent: (cb: (data: string) => void) => {
    const listener = (_event: Electron.IpcRendererEvent, data: string) => cb(data)
    ipcRenderer.on("sse-event", listener)
    return () => ipcRenderer.removeListener("sse-event", listener)
  },
  onSseError: (cb: (msg: string) => void) => {
    ipcRenderer.on("sse-error", (_event, v) => cb(v))
  },

  // API key management — never touches renderer memory
  getApiKey: (provider: string) => ipcRenderer.invoke("get-api-key", provider),
  setApiKey: (provider: string, key: string) => ipcRenderer.invoke("set-api-key", provider, key),

  // Settings (VS Code-style config persisted in prefs.json)
  settingsGetAll: () => ipcRenderer.invoke("settings-get-all"),
  settingsSet: (key: string, value: unknown) => ipcRenderer.invoke("settings-set", key, value),
  settingsReset: () => ipcRenderer.invoke("settings-reset"),

  // File system (for sidebar tree)
  readDir: (dir: string) => ipcRenderer.invoke("read-dir", dir),
  readFile: (path: string) => ipcRenderer.invoke("read-file", path),

  // opencode process output relay (for debugging)
  onOpencodeStderr: (cb: (line: string) => void) => {
    ipcRenderer.on("ipc:opencode-stderr", (_event, v) => cb(v))
  },
  onOpencodeExited: (cb: (info: { code: number | null }) => void) => {
    ipcRenderer.on("ipc:opencode-exited", (_event, v) => cb(v))
  },
})
