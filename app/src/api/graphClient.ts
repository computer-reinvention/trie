// HTTP client for /desktop/graph/* endpoints.
// Routes all calls through the Electron main process (IPC proxy) because
// the renderer cannot reach 127.0.0.1 directly on some macOS configurations.

import type {
  ProjectSummary,
  ReadResult,
  SymbolsByFileResult,
  TraceResult,
  SymbolHit,
  SystemModel,
  FileTriefactResult,
  FileSourceResult,
  ActivityResult,
} from "./types"

let baseUrl = ""

export function setGraphClientBase(opencodePort: number): void {
  baseUrl = `http://127.0.0.1:${opencodePort}`
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
const trie = () => (window as any).trie

async function post<T>(path: string, body: unknown): Promise<T> {
  const result = await trie().httpRequest({
    method: "POST",
    url: `${baseUrl}${path}`,
    body: JSON.stringify(body),
  }) as { status: number; body: string }
  if (result.status >= 500) throw new Error(`${path} failed (${result.status}): ${result.body}`)
  return JSON.parse(result.body) as T
}

async function get<T>(path: string, params?: Record<string, string>): Promise<T> {
  const url = new URL(`${baseUrl}${path}`)
  if (params) for (const [k, v] of Object.entries(params)) url.searchParams.set(k, v)
  const result = await trie().httpRequest({
    method: "GET",
    url: url.toString(),
  }) as { status: number; body: string }
  if (result.status >= 500) throw new Error(`${path} failed (${result.status}): ${result.body}`)
  return JSON.parse(result.body) as T
}

export const graphClient = {
  summary(): Promise<ProjectSummary> {
    return get("/desktop/graph/summary")
  },

  // Dedicated initial-load endpoint — no predicate required, returns all symbols.
  allSymbols(opts?: { rank_by?: string; limit?: number }): Promise<{ hits: SymbolHit[] }> {
    const params: Record<string, string> = {}
    if (opts?.rank_by) params.rank_by = opts.rank_by
    if (opts?.limit != null) params.limit = String(opts.limit)
    return get("/desktop/graph/all-symbols", Object.keys(params).length ? params : undefined)
  },

  // Dedicated initial-load endpoint — returns all call-graph edges directly from DB.
  allEdges(opts?: { limit?: number }): Promise<{ edges: Array<{ from: string; to: string }> }> {
    const params: Record<string, string> = {}
    if (opts?.limit != null) params.limit = String(opts.limit)
    return get("/desktop/graph/all-edges", Object.keys(params).length ? params : undefined)
  },

  // The high-level system model — classified+scored nodes, L0 component axes
  // (role/subsystem), landmarks, precomputed layout positions. The primary
  // data source for the graph view. Cached server-side; instant after first call.
  systemModel(opts?: { landmarkLimit?: number; includeTests?: boolean }): Promise<SystemModel> {
    const params: Record<string, string> = {}
    if (opts?.landmarkLimit != null) params.landmark_limit = String(opts.landmarkLimit)
    if (opts?.includeTests) params.include_tests = "true"
    return get("/desktop/graph/system-model", Object.keys(params).length ? params : undefined)
  },

  grep(opts: { predicate?: Record<string, unknown>; rank_by?: string; limit?: number }): Promise<{ hits: SymbolHit[] }> {
    return post("/desktop/graph/grep", opts)
  },

  read(qname: string): Promise<ReadResult> {
    return post("/desktop/graph/read", { qname })
  },

  trace(opts: { from_qname: string; direction?: string; depth?: number }): Promise<TraceResult> {
    return post("/desktop/graph/trace", opts)
  },

  symbolsByFile(path: string): Promise<SymbolsByFileResult> {
    return get("/desktop/graph/symbols-by-file", { path })
  },

  // Full triefact (front matter + per-symbol sections) for a source file.
  fileTriefact(path: string): Promise<FileTriefactResult> {
    return get("/desktop/graph/file-triefact", { path })
  },

  // Raw source text for a file — feeds the editor's source view.
  fileSource(path: string): Promise<FileSourceResult> {
    return get("/desktop/graph/file-source", { path })
  },

  // Live writer status + working-tree stale set (polled by the activity store).
  activity(): Promise<ActivityResult> {
    return get("/desktop/graph/activity")
  },

  createSession(title?: string): Promise<{ id: string }> {
    return post("/desktop/session", title ? { title } : {})
  },
}
