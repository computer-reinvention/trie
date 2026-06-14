// Headless Electron renderer: rasterize an SVG file to a PNG at a given size.
// Invoked by build-icon.mjs as `electron render-svg.mjs <in.svg> <out.png> <px>`.
// Uses an offscreen BrowserWindow so Chromium renders gradients/filters exactly
// as the app does, then captures the page to a PNG.

import { app, BrowserWindow } from "electron"
import { readFileSync, writeFileSync } from "node:fs"

const [, , svgPath, outPath, sizeArg] = process.argv
const size = Number(sizeArg) || 1024

app.disableHardwareAcceleration()

app.whenReady().then(async () => {
  const svg = readFileSync(svgPath, "utf-8")
  const win = new BrowserWindow({
    width: size,
    height: size,
    show: false,
    transparent: true,
    frame: false,
    webPreferences: { offscreen: false },
  })

  // Transparent page that sizes the SVG to exactly the icon canvas.
  const html = `<!doctype html><html><head><meta charset="utf-8">
    <style>html,body{margin:0;padding:0;background:transparent}
    svg{display:block;width:${size}px;height:${size}px}</style></head>
    <body>${svg}</body></html>`

  await win.loadURL("data:text/html;charset=utf-8," + encodeURIComponent(html))
  // Give the compositor a beat to paint the gradients/filters.
  await new Promise((r) => setTimeout(r, 250))

  const image = await win.capturePage()
  writeFileSync(outPath, image.toPNG())
  win.destroy()
  app.quit()
})
