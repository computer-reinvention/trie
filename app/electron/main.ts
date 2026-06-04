import { app, BrowserWindow } from "electron"
import { join } from "path"
import { ProcessManager } from "./process-manager"
import { registerIpcHandlers } from "./ipc-handlers"

let win: BrowserWindow | null = null
let pm: ProcessManager | null = null

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
  }

  win.on("closed", () => {
    win = null
  })
}

app.whenReady().then(() => {
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
