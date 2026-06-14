import { app, BrowserWindow, nativeImage } from "electron"
import { join } from "path"
import { existsSync } from "fs"
import { ProcessManager } from "./process-manager"
import { registerIpcHandlers } from "./ipc-handlers"

// Branding: name the app "trie" everywhere (menu bar, About, dock tooltip)
// instead of the default "Electron".
app.setName("trie")

let win: BrowserWindow | null = null
let pm: ProcessManager | null = null

/** Resolve the brand icon PNG for dev dock override. In a packaged build the
 *  .icns from electron-builder is used automatically, so this is dev-only. */
function brandIconPath(): string | null {
  // From out/main/ walk up to app/, then build/icon.png.
  const candidates = [
    join(__dirname, "..", "..", "build", "icon.png"),
    join(__dirname, "..", "..", "..", "build", "icon.png"),
  ]
  return candidates.find((p) => existsSync(p)) ?? null
}

function createWindow(): void {
  win = new BrowserWindow({
    width: 1440,
    height: 900,
    minWidth: 960,
    minHeight: 640,
    titleBarStyle: "hiddenInset",
    // vertically center the traffic lights within the 38px title bar:
    // (38 - ~12px light height) / 2 ≈ 13
    trafficLightPosition: { x: 16, y: 13 },
    backgroundColor: "#020617",
    webPreferences: {
      preload: join(__dirname, "../preload/preload.js"),
      contextIsolation: true,
      nodeIntegration: false,
      sandbox: false,
    },
  })

  pm = new ProcessManager(win)
  registerIpcHandlers(pm)

  // Always load from the built renderer output via file:// protocol.
  // This avoids all network-related issues (ERR_ADDRESS_INVALID, ERR_EMPTY_RESPONSE)
  // that occur when trying to reach a Vite dev server from the Electron renderer
  // on macOS with restricted loopback access.
  win.loadFile(join(__dirname, "../renderer/index.html"))

  // Open DevTools in development (not when packaged)
  if (!app.isPackaged) {
    win.webContents.openDevTools()
    // Forward renderer console to the main stdout so logs are capturable
    // outside the in-window DevTools (dev diagnostics only).
    win.webContents.on("console-message", (_e, level, message, line, sourceId) => {
      console.log(`[renderer:${level}] ${message}  (${sourceId}:${line})`)
    })
  }

  win.on("closed", () => {
    win = null
  })
}

app.whenReady().then(() => {
  // In dev the dock shows the generic Electron logo (the running binary's
  // icon). Override it with the trie brand icon so dev matches the packaged
  // app. Packaged builds get the .icns from electron-builder automatically.
  if (!app.isPackaged && process.platform === "darwin") {
    const iconPath = brandIconPath()
    if (iconPath) {
      const img = nativeImage.createFromPath(iconPath)
      if (!img.isEmpty()) app.dock?.setIcon(img)
    }
  }
  createWindow()
  app.on("activate", () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    pm?.killAll()
    app.quit()
  }
})

app.on("before-quit", () => {
  pm?.killAll()
})
