import { resolve } from "path"
import { defineConfig } from "vitest/config"

// Headless unit tests for pure logic: the AGM engine (src/agm), the opencode
// config merge-writer (electron/opencode-config) and pointer/delta helpers
// (src/settings/configPointer). The `@/` alias mirrors tsconfig + electron.vite
// so imports resolve.
export default defineConfig({
  resolve: {
    alias: { "@": resolve(__dirname, "src") },
  },
  test: {
    environment: "node",
    include: ["src/**/*.test.ts", "electron/**/*.test.ts"],
  },
})
