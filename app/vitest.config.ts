import { resolve } from "path"
import { defineConfig } from "vitest/config"

// Headless unit tests for the AGM engine (pure math modules under src/agm).
// The `@/` alias mirrors tsconfig + electron.vite so imports resolve.
export default defineConfig({
  resolve: {
    alias: { "@": resolve(__dirname, "src") },
  },
  test: {
    environment: "node",
    include: ["src/**/*.test.ts"],
  },
})
