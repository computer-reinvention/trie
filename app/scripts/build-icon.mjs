#!/usr/bin/env node
// Generate the macOS app icon (build/icon.icns) + a 512px PNG (build/icon.png)
// from build/icon.svg. Reproducible: re-run after editing the SVG.
//
// Rasterization is done by the Chromium engine bundled in `electron` (already a
// devDependency) so gradients/filters render correctly — ImageMagick's built-in
// MSVG renderer drops them, and we don't want a system librsvg dependency just
// for the icon. The macOS toolchain (sips + iconutil) then builds the .icns.
//
//   node scripts/build-icon.mjs

import { execFileSync } from "node:child_process"
import { rmSync, existsSync, mkdirSync } from "node:fs"
import { join, dirname } from "node:path"
import { fileURLToPath } from "node:url"

const here = dirname(fileURLToPath(import.meta.url))
const appDir = join(here, "..")
const buildDir = join(appDir, "build")
const svg = join(buildDir, "icon.svg")

if (!existsSync(svg)) {
  console.error(`[icon] missing source: ${svg}`)
  process.exit(1)
}

function run(cmd, args, opts = {}) {
  execFileSync(cmd, args, { stdio: "inherit", ...opts })
}

// 1) Rasterize the SVG to a 1024px master PNG via headless Electron/Chromium.
const master = join(buildDir, "icon-1024.png")
const electronBin = join(appDir, "node_modules", ".bin", "electron")
run(electronBin, [join(here, "render-svg.mjs"), svg, master, "1024"], {
  env: { ...process.env, ELECTRON_DISABLE_SECURITY_WARNINGS: "1" },
})

if (!existsSync(master)) {
  console.error("[icon] rasterization failed — no master PNG produced")
  process.exit(1)
}

// 2) Build the .iconset with every size macOS expects.
const iconset = join(buildDir, "icon.iconset")
rmSync(iconset, { recursive: true, force: true })
mkdirSync(iconset, { recursive: true })

const sizes = [
  [16, "icon_16x16.png"],
  [32, "icon_16x16@2x.png"],
  [32, "icon_32x32.png"],
  [64, "icon_32x32@2x.png"],
  [128, "icon_128x128.png"],
  [256, "icon_128x128@2x.png"],
  [256, "icon_256x256.png"],
  [512, "icon_256x256@2x.png"],
  [512, "icon_512x512.png"],
  [1024, "icon_512x512@2x.png"],
]
for (const [px, name] of sizes) {
  run("sips", ["-z", String(px), String(px), master, "--out", join(iconset, name)])
}

// 3) iconset -> icns
run("iconutil", ["-c", "icns", iconset, "-o", join(buildDir, "icon.icns")])

// 4) A 512px PNG for Linux / generic use.
run("sips", ["-z", "512", "512", master, "--out", join(buildDir, "icon.png")])

// cleanup
rmSync(iconset, { recursive: true, force: true })
rmSync(master, { force: true })

console.log("[icon] wrote build/icon.icns + build/icon.png")
