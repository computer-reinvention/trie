# trie Desktop App — Product Requirements Document

> **Ring 4 MSP.** A macOS application where the trie symbol graph is the
> primary work surface. The user types intent — or clicks a node to direct
> attention — and opencode executes it. Every read, write, and graph
> traversal the agent makes is visualized on the canvas in real time.

---

## 1. Vision and Scope

Ring 4 says the IDE goes away. The default work surface stops being a text
editor showing a file and becomes a navigable representation of the system.
This document specifies the first concrete step toward that: an application
where the graph IS the editor, the agent IS the executor, and prose IS the
primary artifact.

The single-sentence product spec:

> The trie symbol graph fills the screen. The user types a prompt — or clicks
> nodes to @-mention specific symbols — and opencode executes. Every node the
> agent reads glows blue; every node it writes pulses amber. The codebase
> describes itself to the user in real time.

### What "full" means

"Full" means the agent can do everything opencode can already do — read files,
write files, run shell commands, apply trie patches, trigger cascades — and all
of it is mirrored on the graph. No capability is withheld. The graph is a
visualization layer on top of a complete coding agent, not a sandboxed subset.

### What this is not

- Not a fork of opencode's frontend. opencode runs as a child process (the
  agent backend). We build a new frontend that talks to it.
- Not a replacement for the opencode CLI. The CLI keeps working unchanged.
  This app is an alternate interface to the same backend.
- Not a read-only viewer. The agent writes. The graph shows writes happening.
- Not Ring 4 complete. Gesture-based topology changes ("move auth to
  middleware tier, described in prose, confirmed topologically before code is
  touched") are deferred. This ships the substrate: graph canvas + full agent
  - bidirectional steering.

---

## 2. System Architecture

Two processes run while the app is open (down from the three that were originally
planned — the dedicated trie graph HTTP server replaces what was going to be a
separate process, and the opencode fork gains the desktop route group so there
is no second HTTP server).

```
┌──────────────────────────────────────────────────────────────────┐
│  trie Desktop App  (Electron main process)                       │
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐   │
│  │  BrowserWindow  (React frontend)                          │   │
│  │                                                           │   │
│  │  ┌──────────────┐   ┌─────────────────────────────────┐  │   │
│  │  │   Sidebar    │   │   Graph Canvas  (React Flow)    │  │   │
│  │  │  (file tree) │   │                                 │  │   │
│  │  └──────────────┘   └─────────────────────────────────┘  │   │
│  │                                                           │   │
│  │  ┌─────────────────────────────────────────────────────┐  │   │
│  │  │  Input Bar  (@mention chips + prompt text)          │  │   │
│  │  └─────────────────────────────────────────────────────┘  │   │
│  └───────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐   │
│  │  opencode daemon  (child process, our fork)               │   │
│  │                                                           │   │
│  │  HTTP on 127.0.0.1:4096                                   │   │
│  │                                                           │   │
│  │  /session/*          ← agent turns, message history       │   │
│  │  /desktop/event      ← graph canvas SSE stream (NEW)      │   │
│  │  /desktop/session    ← session create wrapper (NEW)       │   │
│  │  /desktop/graph/*    ← grep/read/trace for graph (NEW)    │   │
│  │                                                           │   │
│  │  Internal: MCP → trie mcp serve (stdio, spawned by       │   │
│  │  opencode via .opencode/opencode.json)                    │   │
│  └───────────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────┘
```

### Process 1: Electron main process

Owns the application lifecycle. Responsibilities:
- Spawn and manage the opencode daemon child process
- Relay IPC between the BrowserWindow renderer and the daemon
- Handle app menu, window management, project open/close
- Manage API key storage in macOS Keychain

### Process 2: opencode daemon (our fork)

Our fork of opencode, run as `opencode` with the project directory. It:
- Exposes its HTTP API on `127.0.0.1:4096` (preferred; falls back to next
  free port if taken)
- Serves the new `/desktop` route group (§3) alongside existing routes
- Spawns `trie mcp serve` internally via its MCP config, giving the agent
  access to all 15 trie tools
- Has trie's tool overrides installed (`.opencode/tools/*.ts`)
- Has the `trie-refresh` plugin installed (`.opencode/plugins/trie-refresh.ts`)

One process, one port, one HTTP server. The `/desktop/graph/*` endpoints
(grep, read, trace) are thin wrappers in the desktop route group that call
through to the same `TrieTools` instance opencode already holds via MCP —
no second SQLite connection, no second trie process for graph queries.

### Data flow summary

```
User types prompt + @mentions
  │
  ▼
Frontend resolves @qname pills
  → GET /desktop/graph/read?qname=... → prose injected into message
  │
  ▼
POST /session/:id/message
  { content: "Symbol context:\n...\n\nUser: Why does this fail?" }
  │
  ▼
opencode runs agent turn → internal bus events
  │
  ├── Bus: message.part.updated (tool, status=running)
  │     → /desktop/event SSE: desktop.tool.start { tool: "trie_read", input: { qname } }
  │     → frontend: node pulses blue
  │
  ├── Bus: message.part.updated (tool, status=completed)
  │     → /desktop/event SSE: desktop.tool.done { tool: "trie_read", output: "..." }
  │     → frontend: node prose updated, fades to idle
  │
  ├── Bus: message.part.delta
  │     → /desktop/event SSE: desktop.text.delta { delta: "token" }
  │     → frontend: streams into response panel
  │
  ├── Bus: file.edited { file: "src/auth.py" }
  │     → /desktop/event SSE: desktop.file.edited { file: "src/auth.py" }
  │     → frontend: nodes for that file set to stale
  │
  └── Bus: session.status { type: "idle" }
        → /desktop/event SSE: desktop.session.status { status: { type: "idle" } }
        → frontend: input bar re-enabled, agent state badges cleared


### Data flow summary

```
User types prompt + @mentions
  │
  ▼
Frontend resolves @qname pills → POST /desktop/graph/read → gets prose
  │
  ▼
Frontend POSTs to opencode HTTP API: POST /session/:id/message
  { content: "Focus on: ...\n<prose>\n...\n\nUser: Why does this fail?" }
  │
  ▼
opencode runs agent turn → streams SSE events
  │
  ├── tool_call { name: "read", input: { qname: "auth/middleware:require_auth" } }
  │     → frontend: set node agentState = "reading", pulse blue
  │
  ├── tool_result { name: "read", output: "..." }
  │     → frontend: update node prose if changed, reset agentState after 800ms
  │
  ├── tool_call { name: "write_file", input: { path: "src/auth.py", ... } }
  │     → frontend: find all nodes for src/auth.py, pulse amber
  │
  ├── tool_call { name: "patch_apply", input: {} }
  │     → frontend: re-query /desktop/graph/read for affected nodes, update prose
  │
  └── agent_finish { ... }
        → frontend: reset all agentStates to idle, re-enable input bar
```

---

## 3. opencode Desktop Server (new route group in the fork)

We own the opencode fork. Rather than consuming the existing general-purpose
SSE stream (designed for the TUI/web app, subject to internal churn), we add
a dedicated `/desktop` HTTP API group to the fork. This group emits events
shaped exactly for the graph canvas and exposes the graph-specific endpoints
the frontend needs. It is a peer route group on the same HTTP server — same
port, zero new processes, zero new ports.

### 3.1 Where it lives in the fork

Four files touched, zero existing behavior changed:

```
packages/opencode/src/server/routes/instance/httpapi/
├── groups/
│   └── desktop.ts          ← NEW: HttpApiGroup definitions
├── handlers/
│   └── desktop.ts          ← NEW: handler implementations
├── api.ts                  ← EDIT: add DesktopApi to InstanceHttpApi
└── server.ts               ← EDIT: add desktopHandlers to Layer.provide([...])
```

### 3.2 New endpoints

All under the `/desktop` prefix.

#### `GET /desktop/event`

The graph canvas SSE stream. One connection per app session, maintained for
the lifetime of the project. Emits graph-canvas-specific events derived from
the opencode internal bus (`Bus.subscribeAll()`).

Wire format — identical to the existing opencode SSE convention:
```
event: message
data: <JSON-stringified DesktopEvent>
\n\n
```

First frame on connect:
```json
{ "id": "...", "type": "desktop.connected", "properties": {} }
```

Heartbeat every 10s:
```json
{ "id": "...", "type": "desktop.heartbeat", "properties": {} }
```

#### `POST /desktop/session`

Thin wrapper around `POST /session`. Creates a session scoped to the opened
project directory and returns the `Session.Info` including the `id` to use
for all subsequent calls.

#### `GET /desktop/session/:sessionID/history`

Returns the last 20 turns (messages + their tool parts) for display in the
turn history panel on load. Wraps `GET /session/:sessionID/message?limit=20`.

### 3.3 Desktop event types

Every `DesktopEvent` has the envelope:
```typescript
{ id: string, type: string, properties: T }
```

The handler in `handlers/desktop.ts` subscribes to `Bus.subscribeAll()` and
maps internal bus events to desktop events. Mapping table:

#### `desktop.tool.start`

Emitted when a `message.part.updated` arrives with `part.type === "tool"` and
`part.state.status === "running"`.

```typescript
{
  type: "desktop.tool.start",
  properties: {
    sessionID: string,
    messageID: string,
    partID: string,
    callID: string,        // LLM tool call ID from ToolPart.callID
    tool: string,          // e.g. "trie_read", "write_file", "bash"
    input: Record<string, unknown>,  // ToolState.input (available at running status)
    time: { start: number }
  }
}
```

#### `desktop.tool.done`

Emitted when `part.state.status === "completed"` or `"error"`.

```typescript
{
  type: "desktop.tool.done",
  properties: {
    sessionID: string,
    messageID: string,
    partID: string,
    callID: string,
    tool: string,
    input: Record<string, unknown>,
    output: string | null,      // ToolState.output (completed) or null (error)
    error: string | null,       // ToolState.error (error) or null (completed)
    time: { start: number, end: number }
  }
}
```

#### `desktop.text.delta`

Emitted on every `message.part.delta` bus event — streaming assistant tokens
for the response panel.

```typescript
{
  type: "desktop.text.delta",
  properties: {
    sessionID: string,
    messageID: string,
    partID: string,
    delta: string
  }
}
```

#### `desktop.session.status`

Emitted on `session.status` bus events. The `status.type` field drives
input bar enable/disable.

```typescript
{
  type: "desktop.session.status",
  properties: {
    sessionID: string,
    status: {
      type: "running" | "idle" | "error",
      error?: string
    }
  }
}
```

#### `desktop.file.edited`

Emitted on `file.edited` bus events — a file was written on disk.

```typescript
{
  type: "desktop.file.edited",
  properties: {
    file: string   // absolute path of the edited file
  }
}
```

### 3.4 Tool-to-graph mapping

The frontend's `useOpenCodeSSE` hook (§11) receives `desktop.tool.start` and
`desktop.tool.done` events and drives graph animations from them.

| `tool` value | `input` field | Graph action on `start` | Graph action on `done` |
|---|---|---|---|
| `trie_read` | `qname` | `setNodeAgentState(qname, 'reading')` | Update prose if output changed; reset to `'idle'` after 800ms |
| `trie_trace` | `from_qname` | `setNodeAgentState(from_qname, 'reading')` | Merge new nodes/edges from output; reset to `'idle'` after 800ms |
| `trie_trace_flow` | `symbol1`, `symbol2` | Animate both nodes `'reading'` | Animate path edges in sequence (200ms between edges) |
| `trie_explain_flow` | `symbol1`, `symbol2` | Same as above | Same as above |
| `trie_explain_symbol` | `sym` | Find node by name, set `'reading'` | Reset to `'idle'` after 800ms |
| `trie_grep` | — | No node animation | No node animation |
| `trie_grep_symbol` | — | No node animation | No node animation |
| `trie_grep_str` | — | No node animation | No node animation |
| `trie_patch` | `qname` | `setNodeAgentState(qname, 'writing')` | Keep `'writing'` until `patch_apply` done |
| `trie_patch_apply` | — | All pending-patch nodes → `'writing'` | Re-fetch prose for each; set `'idle'` |
| `write_file` | `path` | `setFileAgentState(path, 'writing')` | Set `'stale'` on done |
| `str_replace_editor` | `path` | `setFileAgentState(path, 'writing')` | Set `'stale'` on done |
| `bash` | — | No node animation | No node animation |

`desktop.file.edited` is a secondary signal used to clear `'stale'` states
when `trie refresh --after-turn` has run (it rewrites triefact files, which
triggers `file.edited` events for triefact paths). The handler checks whether
the edited path is under `triefacts/` and, if so, re-fetches prose for the
corresponding symbol nodes.

### 3.5 SSE connection in the frontend

```typescript
// hooks/useOpenCodeSSE.ts
const es = new EventSource(
  `http://127.0.0.1:${opencodePort}/desktop/event`
)
es.onmessage = (event) => {
  const data: DesktopEvent = JSON.parse(event.data)
  switch (data.type) {
    case 'desktop.tool.start':   handleToolStart(data.properties, graphStore, agentStore); break
    case 'desktop.tool.done':    handleToolDone(data.properties, graphStore, agentStore); break
    case 'desktop.text.delta':   agentStore.appendToken(data.properties.delta); break
    case 'desktop.session.status':
      if (data.properties.status.type === 'idle') agentStore.endTurn()
      if (data.properties.status.type === 'error') agentStore.failTurn(data.properties.status.error ?? '')
      break
    case 'desktop.file.edited':  handleFileEdited(data.properties.file, graphStore); break
  }
}
```

---

## 4. trie Graph Endpoints (inside the opencode fork's desktop route group)

The frontend needs to query the trie graph directly — for initial graph
population, node expand calls, @mention resolution, and sidebar file clicks.
These are served by `/desktop/graph/*` endpoints added to the opencode fork's
desktop route group (§3.1). No second process. No second port. The handlers
in `packages/opencode/src/server/routes/instance/httpapi/handlers/desktop.ts`
call the trie graph DB through the same MCP tools opencode already has wired.

### 4.1 Endpoint contract

All `/desktop/graph/*` endpoints accept `Content-Type: application/json`
POST bodies (except the `GET` endpoints) and return `application/json`.
Response envelopes are identical to what `trie mcp serve` returns — the same
underlying Python methods, proxied through opencode's MCP client.

### 4.2 Endpoint design

All endpoints accept `Content-Type: application/json` POST bodies and return
`application/json` responses. Response envelopes are identical to what
`trie mcp serve` returns — the same Python methods are called, the same dicts
are serialized.

#### `POST /desktop/graph/grep`

```json
{
  "predicate": { "public_only": true },
  "rank_by": "inbound_count",
  "limit": 5000
}
```
Response: same as MCP `grep` response (`{ "hits": [...] }`).

#### `POST /desktop/graph/read`

```json
{ "qname": "trie/graph/store:Store.grep_symbols" }
```
Response: same as MCP `read` response.

#### `POST /desktop/graph/trace`

```json
{ "from_qname": "trie/graph/store:Store", "direction": "both", "depth": 2 }
```
Response: same as MCP `trace` response.

#### `GET /desktop/graph/symbols-by-file?path=<rel-path>`

Returns all symbols for a source file. Used by sidebar file click.

```json
{
  "file_path": "trie/graph/store.py",
  "symbols": [
    {
      "qname": "trie/graph/store:Store",
      "kind": "class",
      "start_line": 147,
      "end_line": 910,
      "name": "Store",
      "is_public": true,
      "inbound_count": 42,
      "outbound_count": 3,
      "one_liner": "SQLite-backed persistence for trie's symbol graph."
    }
  ]
}
```

#### `GET /desktop/graph/summary`

Project summary for `appStore` and the agent context block.

```json
{
  "project_name": "trie",
  "project_root": "/Users/user/Desktop/trie",
  "total_symbols": 1373,
  "public_symbols": 1079,
  "total_files": 74,
  "total_edges": 2523,
  "trie_version": "0.1.5"
}
```

The remaining MCP tools (`grep_str`, `grep_symbol`, `trace_flow`, etc.) are
available through the same dispatch pattern if needed — add them to the
desktop route group on demand.

### 4.2 Implementation in the opencode fork

The desktop route group handler calls MCP tools through opencode's existing
MCP client (the same client the agent uses). It does not talk directly to the
trie Python process or the SQLite DB — it goes through the MCP stdio channel
that opencode already manages. This means:

- No second trie process.
- No second SQLite connection.
- Correct serialization: MCP calls are already serialized through opencode's
  internal MCP client, which handles the stdio pipe correctly.

For the `/desktop/graph/summary` endpoint specifically, the data is assembled
from opencode's project info (directory name) plus a dedicated `trie_summary`
MCP tool call (add `trie_summary` to `trie/mcp_server.py` — one new tool that
returns the 5 aggregate counts from the DB).

### 4.3 trie CLI changes still needed

The `trie serve --graph` command from the original plan is **dropped** — no
longer needed. The only trie-side changes required are:

1. **stdout line-buffering fix** in `trie/mcp_server.py`:
   ```python
   import sys
   sys.stdout.reconfigure(line_buffering=True)
   sys.stderr.reconfigure(line_buffering=True)
   ```

2. **`trie_summary` MCP tool** — new tool in `trie/mcp_server.py` returning
   `{ total_symbols, public_symbols, total_files, total_edges, trie_version }`.

3. **`Store.symbols_in_file`** — add to `trie/graph/store.py`, returning
   `list[SymbolDetail]` for a given `file_path`. Used by `trie_summary`
   and surfaced via `/desktop/graph/symbols-by-file`.

No new Python dependencies. No new CLI commands. No `fastapi`/`uvicorn`.

---

## 5. Desktop App: Electron Shell

### 5.1 Repository layout

The desktop app lives inside the trie monorepo under `app/`. The Python CLI
(`trie/`) and the Electron app (`app/`) share a single repo, a single git
history, and a single CI pipeline. The Python package and the Node package
are independent — no shared build tool, no workspace linking — but they ship
together from the same repository.

```
trie/                            ← repo root (Python package, existing)
├── trie/                        ← Python source (existing)
├── tests/                       ← Python tests (existing)
├── triefacts/                   ← generated triefacts (existing)
├── docs/                        ← documentation (existing)
├── scripts/                     ← ship.sh etc. (existing)
├── pyproject.toml               ← Python package config (existing)
├── trie.toml                    ← trie project config (existing)
│
└── app/                         ← Electron desktop app (NEW)
    ├── electron/
    │   ├── main.ts              # Electron main process entry
    │   ├── preload.ts           # contextBridge preload
    │   ├── process-manager.ts   # opencode daemon lifecycle
    │   ├── keychain.ts          # macOS Keychain via keytar
    │   └── ipc-handlers.ts      # ipcMain handlers
    ├── src/
    │   ├── main.tsx             # React entry
    │   ├── App.tsx
    │   ├── components/
    │   │   ├── GraphCanvas/
    │   │   │   ├── index.tsx
    │   │   │   ├── nodes/
    │   │   │   │   ├── SymbolNode.tsx
    │   │   │   │   ├── FileGroupNode.tsx
    │   │   │   │   └── HubPlaceholderNode.tsx
    │   │   │   ├── edges/
    │   │   │   │   └── SemanticEdge.tsx
    │   │   │   ├── ElkLayout.tsx
    │   │   │   └── useAgentAnimations.ts
    │   │   ├── Sidebar/
    │   │   │   ├── index.tsx
    │   │   │   ├── FileTree.tsx
    │   │   │   └── ViewSourceModal.tsx
    │   │   ├── InputBar/
    │   │   │   ├── index.tsx
    │   │   │   ├── MentionInput.tsx   # @mention pill input
    │   │   │   ├── MentionPill.tsx
    │   │   │   └── ModelSelector.tsx
    │   │   ├── TurnHistory/
    │   │   │   ├── index.tsx
    │   │   │   └── TurnEvent.tsx
    │   │   └── ResponsePanel.tsx
    │   ├── store/
    │   │   ├── graphStore.ts
    │   │   ├── agentStore.ts
    │   │   └── appStore.ts
    │   ├── api/
    │       │   ├── graphClient.ts   # HTTP client for /desktop/graph/* endpoints
    │   │   ├── opencodeClient.ts # HTTP + SSE client for opencode
    │   │   └── types.ts         # Shared TypeScript types
    │   └── hooks/
    │       ├── useOpenCodeSSE.ts
    │       ├── useGraphPopulation.ts
    │       └── useMentionResolver.ts
    ├── package.json             # Node deps — independent of pyproject.toml
    ├── tsconfig.json
    ├── vite.config.ts           # Vite for renderer
    └── electron-builder.yml
```

### 5.1.1 Monorepo conventions

- `app/` has its own `package.json` and `node_modules/`. It is not a workspace
  member of any root-level Node config — there is no root `package.json`.
  Run `npm install` (or `bun install`) from `app/` to install JS deps.
- Python deps are managed as before: `uv sync --extra dev` from the repo root.
- The `app/` directory is excluded from `trie verify` (add to `trie.toml`
  under `[sync] exclude`). The Electron source is not Python and should not
  be indexed by the trie scanner.
- `app/node_modules/`, `app/dist/`, and `app/out/` are gitignored.
- CI runs two jobs in parallel: the existing `pytest + ruff` Python job, and
  a new `npm run build` Electron job, both triggered on push to `main`.
- `scripts/ship.sh` gains an optional `--app` flag that builds and notarizes
  the `.dmg` in addition to the Python package reinstall. By default it only
  ships the Python package (existing behavior unchanged).

### 5.1.2 trie.toml additions

```toml
# Exclude the Electron app source from trie's Python scanner.
# app/ contains TypeScript, not Python — scanning it would produce
# garbage symbols and slow down trie sync.
[sync]
exclude = ["app/", "landing/", "dist/"]
```

### 5.2 Tech stack

| Layer              | Library                | Notes                                                              |
| ------------------ | ---------------------- | ------------------------------------------------------------------ |
| Shell              | Electron 35+           | Same major version as opencode desktop for ecosystem compatibility |
| Frontend framework | React 19               | React Flow requires React; SolidJS rejected                        |
| Graph canvas       | React Flow v12         | Nodes are React components; content-rich nodes trivial             |
| Layout engine      | ELK.js ≥0.10           | WebWorker build; hierarchical layout                               |
| State              | Zustand 5              | One store per domain                                               |
| Styling            | Tailwind CSS v4        |                                                                    |
| Prose rendering    | react-markdown         | Inside expanded node panels                                        |
| Inline source view | CodeMirror 6           | Read-only; used in ViewSourceModal only                            |
| Build              | Vite + electron-vite   | Same tooling as opencode desktop                                   |
| Language           | TypeScript 5.5+        | Strict mode                                                        |
| Keychain           | keytar                 | macOS Keychain access from Electron main                           |
| IPC                | Electron contextBridge | Typed channel constants                                            |

**Why React over SolidJS:** React Flow v12 has no SolidJS equivalent. Building
a graph editor with content-rich nodes (prose, badges, expand/collapse) on any
other canvas framework would require rebuilding React Flow's node-as-component
architecture from scratch. The productivity cost exceeds the framework
preference cost.

### 5.3 Electron main process (`electron/main.ts`)

```typescript
import { app, BrowserWindow, ipcMain } from "electron";
import { ProcessManager } from "./process-manager";
import { registerIpcHandlers } from "./ipc-handlers";

let win: BrowserWindow | null = null;
let pm: ProcessManager | null = null;

app.whenReady().then(async () => {
  win = new BrowserWindow({
    width: 1440,
    height: 900,
    minWidth: 900,
    minHeight: 600,
    titleBarStyle: "hiddenInset", // macOS native traffic lights
    vibrancy: "sidebar", // macOS sidebar blur on the sidebar region
    backgroundColor: "#0a0a0a",
    webPreferences: {
      preload: path.join(__dirname, "preload.js"),
      contextIsolation: true,
      nodeIntegration: false,
    },
  });

  pm = new ProcessManager(win);
  registerIpcHandlers(pm);

  if (process.env.NODE_ENV === "development") {
    win.loadURL("http://localhost:5173");
    win.webContents.openDevTools();
  } else {
    win.loadFile(path.join(__dirname, "../dist/index.html"));
  }
});

app.on("before-quit", () => pm?.killAll());
```

### 5.4 Process manager (`electron/process-manager.ts`)

One process to manage: the opencode daemon. The trie graph server is a route
group inside it — no separate spawn.

```typescript
import { spawn, ChildProcess } from 'child_process'
import { BrowserWindow } from 'electron'
import net from 'net'

export class ProcessManager {
  private opencodeProc: ChildProcess | null = null
  private opencodePort = 4096

  constructor(private win: BrowserWindow) {}

  async startForProject(projectDir: string): Promise<void> {
    this.opencodePort = await findFreePort(4096)

    this.opencodeProc = spawn('opencode', ['--port', String(this.opencodePort)], {
      cwd: projectDir,
      env: { ...process.env },
      stdio: ['ignore', 'pipe', 'pipe'],
    })

    this.opencodeProc.stderr?.on('data', (d) =>
      this.win.webContents.send('ipc:opencode-stderr', d.toString()))

    this.opencodeProc.on('exit', (code) =>
      this.win.webContents.send('ipc:opencode-exited', { code }))

    // Wait for opencode's HTTP server to be ready (health check on /desktop/event
    // preamble, or fall back to any 200 on the root)
    await waitForPort(this.opencodePort, 15_000)

    this.win.webContents.send('ipc:servers-ready', {
      opencodePort: this.opencodePort,
      projectDir,
    })
  }

  killAll(): void {
    this.opencodeProc?.kill('SIGTERM')
  }

  getOpenCodePort() { return this.opencodePort }
}

  killAll(): void {
    this.opencodeProc?.kill();
    this.trieProc?.kill();
  }

  getOpenCodePort() {
    return this.opencodePort;
  }
  getTriePort() {
  }
}

async function findFreePort(preferred: number): Promise<number> {
  return new Promise((resolve) => {
    const server = net.createServer();
    server.listen(preferred, () => {
      const { port } = server.address() as net.AddressInfo;
      server.close(() => resolve(port));
    });
    server.on("error", () => resolve(findFreePort(preferred + 1)));
  });
}

async function waitForPort(port: number, timeoutMs: number): Promise<void> {
  const deadline = Date.now() + timeoutMs;
  while (Date.now() < deadline) {
    try {
      await fetch(`http://127.0.0.1:${port}/health`);
      return;
    } catch {
      await new Promise((r) => setTimeout(r, 200));
    }
  }
  throw new Error(`Server on port ${port} did not start within ${timeoutMs}ms`);
}
```

### 5.5 IPC channel contract (`electron/preload.ts`)

```typescript
import { contextBridge, ipcRenderer } from "electron";

contextBridge.exposeInMainWorld("trie", {
  // Lifecycle
  openProject: (dir: string) => ipcRenderer.invoke("open-project", dir),
  getRecentProjects: () => ipcRenderer.invoke("get-recent-projects"),

  // Server discovery
  onServersReady: (cb: (ports: ServerPorts) => void) =>
    ipcRenderer.on("ipc:servers-ready", (_, v) => cb(v)),

  // API key management (goes through main process to stay out of renderer)
  getApiKey: (provider: string) => ipcRenderer.invoke("get-api-key", provider),
  setApiKey: (provider: string, key: string) =>
    ipcRenderer.invoke("set-api-key", provider, key),

  // File system (for sidebar tree)
  readDir: (dir: string) => ipcRenderer.invoke("read-dir", dir),
  readFile: (path: string) => ipcRenderer.invoke("read-file", path),

  // opencode stderr relay (for debugging)
  onOpencodeStderr: (cb: (line: string) => void) =>
    ipcRenderer.on("ipc:opencode-stderr", (_, v) => cb(v)),
});

interface ServerPorts {
  opencodePort: number
  projectDir: string
}
```

---

## 6. Layout

```
┌──────────────────────────────────────────────────────────────────────┐
│  [traffic lights]  trie — projectName                    [controls]  │  ← titlebar (hiddenInset)
├──────────────────┬───────────────────────────────────────────────────┤
│                  │                                                   │
│  sidebar         │              graph canvas                        │
│  (220px fixed)   │         (flex, fills remaining width)            │
│                  │                                                   │
│  file tree       │   [symbol nodes + file group containers]         │
│  ─────────────   │                                                   │
│  src/            │   (React Flow canvas — pan, zoom, select)        │
│  ├─ auth/        │                                                   │
│  │  ├─ middlewar │                                                   │
│  │  └─ session   │                                                   │
│  ├─ api/         │                                                   │
│  │  └─ handler   │                                                   │
│  └─ parse/       │                                                   │
│     └─ config    │                                                   │
│                  │                                                   │
│                  ├───────────────────────────────────────────────────┤
│                  │  turn history (collapsible, max 160px)            │
│                  ├───────────────────────────────────────────────────┤
│                  │  input bar (56px fixed)                           │
│                  │  [model ▾] [ @auth/middleware:require_auth × ] [  │
│                  │            type a prompt...            ] [send ▶] │
└──────────────────┴───────────────────────────────────────────────────┘
```

### Sidebar (220px, non-resizable in v1)

- File tree rooted at the open project directory.
- Clicking a file: highlights all graph nodes whose `file_path` matches,
  canvas pans and zooms to fit them (`reactFlowInstance.fitView({ nodes: matchedNodes })`).
- Right-clicking a file: context menu with "View Source" option only.
  Opens `ViewSourceModal`.
- `ViewSourceModal`: floating overlay (portal to `document.body`), CodeMirror 6
  read-only instance, syntax highlighting via `@codemirror/lang-python` (v1),
  dismissed with Escape or outside click.
- Files written during an agent turn do NOT trigger any sidebar visual change.
  The sidebar is a navigation tool, not a status display.
- Directories expand/collapse on click. State persisted to `localStorage` per
  project.

### Graph canvas (flex, all remaining space above the input area)

Full spec in §7.

### Turn history panel (collapsible, sits between canvas and input bar)

- Default state: collapsed (showing only a one-line summary of the last turn,
  e.g. "5 tool calls · 2.3s").
- Click to expand: shows a scrollable log of tool calls for the current and
  recent turns.
- Each entry: `[tool_name]  [truncated input]  →  [status badge]`.
- `trie_read auth/middleware:require_auth  →  ✓`
- `write_file src/auth.py  →  ✓`
- `bash pytest tests/  →  ✓  (2.1s)`
- The panel is never the primary focus. It is evidence, not interface.

### Input bar (56px fixed)

- Model selector pill on the far left (§9).
- `MentionInput` in the center: a contentEditable div that renders @qname
  pills inline with free text. See §8 for full spec.
- Send button on the right (or press Enter).
- Input and send button are disabled (greyed) during an active agent turn.
  A subtle pulsing dot in the send button position indicates the agent is running.
- `Cmd+K` focuses the input bar from anywhere in the app.
- `Cmd+0` fits all nodes to view.
- `Escape` clears selection and collapses any expanded node prose panels.

---

## 7. Graph Canvas Specification

### 7.1 Library configuration

```typescript
// GraphCanvas/index.tsx
import ReactFlow, {
  Background,
  BackgroundVariant,
  Controls,
  MiniMap,
  useReactFlow,
  NodeTypes,
  EdgeTypes,
} from "reactflow";

const nodeTypes: NodeTypes = {
  symbol: SymbolNode,
  fileGroup: FileGroupNode,
  hub: HubPlaceholderNode,
};

const edgeTypes: EdgeTypes = {
  semantic: SemanticEdge,
};

// ReactFlow instance config
const flowConfig = {
  nodeTypes,
  edgeTypes,
  defaultEdgeOptions: { type: "semantic", animated: false },
  minZoom: 0.05,
  maxZoom: 3,
  fitViewOptions: { padding: 0.1 },
  proOptions: { hideAttribution: true },
  selectNodesOnDrag: false, // box select uses shift+drag
  panOnDrag: true,
  zoomOnScroll: true,
  zoomOnPinch: true,
  panOnScroll: false,
};
```

### 7.2 Initial graph population

On project open, after opencode responds to `GET /desktop/graph/summary`:

```typescript
async function populateGraph(opencodePort: number): Promise<void> {
  // 1. Fetch ALL symbols — no limit
  const { hits } = await graphClient.grep({
    predicate: {}, // empty predicate = all symbols
    rank_by: "inbound_count",
    limit: 5000, // hard cap; real projects rarely exceed this
  });

  // 2. Build nodes (no prose loaded yet — lazy)
  const nodes = hits.map((hit) => symbolHitToNode(hit));

  // 3. Fetch edges: trace top-200 by inbound_count (parallel, batched)
  const top200 = hits.slice(0, 200);
  const traceResults = await Promise.all(
    top200.map((h) =>
      graphClient.trace({
        from_qname: h.qname,
        direction: "both",
        depth: 1,
      }),
    ),
  );
  const edges = deduplicateEdges(traceResults.flatMap((r) => r.edges));

  // 4. Group nodes by file into FileGroupNode parents
  const { symbolNodes, groupNodes } = buildFileGroups(nodes);

  // 5. Run ELK layout in WebWorker
  const positioned = await elkLayout([...groupNodes, ...symbolNodes], edges);

  // 6. Set in graphStore
  graphStore.setGraph(positioned.nodes, positioned.edges);
}
```

**On performance:** 1,373 symbols (the size of trie's own codebase) renders
comfortably in React Flow with viewport culling. ELK layout at this scale takes
3–8 seconds in a WebWorker — show a full-screen loading state with a progress
message ("Laying out 1,373 symbols across 74 files...") while it runs. Do not
block the main thread.

For very large codebases (>5,000 symbols), cap the initial `grep` at 5,000 and
show a banner: "Showing 5,000 of N symbols. Use the search to find others."

### 7.3 Node types

#### `SymbolNode`

The primary node type. Used for all symbol kinds.

```
┌────────────────────────────────────────────────────────┐
│ [kind]  name                              ↓14  ↑3  [⊕] │
│ one-liner text (max 1 line, truncated)                  │
│                                                         │
│ ┄ ┄ ┄ ┄ expanded prose panel (hidden by default) ┄ ┄ ┄ │
│                                                         │
│ Full prose rendered as Markdown.                        │
│ Scrollable, max-height 320px.                           │
│ Read-only.                                              │
│ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄│
│                                                         │
│ file.py:14                         [agent state badge]  │
└────────────────────────────────────────────────────────┘
```

**Header row:**

- Left: kind badge — colored pill, short label
  - `fn` → indigo (#6366f1)
  - `cls` → violet (#7c3aed)
  - `mtd` → blue (#2563eb)
  - `const` → amber (#d97706)
  - `mod` → slate (#64748b)
- Center: `symbol.name` in monospace font, full weight
- Right: `↓{inboundCount}` and `↑{outboundCount}` small badges;
  double-clicking either triggers a trace expand (§7.6).
  `⊕` button toggles the prose panel (same as double-clicking the node body).

**One-liner row:**
`symbol.oneLiner` truncated to one line with CSS `text-overflow: ellipsis`.
If `oneLiner` is empty, shows greyed `"no prose yet"`.

**Expanded prose panel** (default hidden, toggled by `⊕` or double-click):

- On first expand: calls `graphClient.read(qname)` to fetch full prose.
  Shows a spinner until loaded.
- Renders `result.prose` via `react-markdown`.
- Max height 320px, overflow scroll.
- Read-only. No editor. Prose editing is the agent's job.

**Footer row:**

- Left: `filePath:startLine` in dimmed monospace.
- Right: agent state badge (see §7.5).

**Minimum node size:** 220px wide, auto height.

**Click behavior:**

- Single click: select the node. Insert `@qname` pill into the input bar.
  Node gets a selection ring (2px solid #a3e635).
- Double-click body: toggle prose panel expansion.
- Double-click `↓` badge: expand callers onto canvas.
- Double-click `↑` badge: expand callees onto canvas.
- Right-click: context menu — "Expand callers", "Expand callees",
  "View source", "Pin @mention", "Remove from canvas".

#### `FileGroupNode`

A React Flow parent/container node. Groups all `SymbolNode`s from the same
source file. Non-interactive (no click handlers). Purely visual.

```
┌─ src/auth/middleware.py ─────────────────────────────────────────────┐
│                                                                      │
│   [SymbolNode]    [SymbolNode]    [SymbolNode]                       │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

- Background: semi-transparent fill, color derived from a hash of the file
  path so the same file always has the same hue.
- Label: filename only (no directory prefix) in the top-left corner, small
  dimmed text.
- No border interaction. React Flow's parent node system handles child
  containment.

#### `HubPlaceholderNode`

Rendered for qnames that appear in `truncated_at` arrays from `trace`
responses — symbols too highly connected to expand.

```
  ⚡ Store  (42 refs)
```

- Pill-shaped, grey.
- Single click: opens a tooltip showing the one-liner and inbound count.
  Does NOT expand into a full node tree (that's the definition of a hub).
- Cannot be @-mentioned (clicking it shows the tooltip, does not insert
  a pill into the input bar).

### 7.4 Edge types

All edges use `SemanticEdge`, a React Flow custom edge. Edge direction:
arrow at the callee end (A → B means "A calls B").

| Edge kind  | Stroke color       | Label     | Determined by                 |
| ---------- | ------------------ | --------- | ----------------------------- |
| `calls`    | `#6366f1` (indigo) | —         | Same-project symbol reference |
| `imports`  | `#06b6d4` (cyan)   | —         | Cross-file module boundary    |
| `inherits` | `#8b5cf6` (purple) | `extends` | Class inheritance             |

In v1, all edges from the `trace` response are rendered as `calls` edges.
`imports` and `inherits` distinction requires richer edge metadata from the
graph DB — this is a v1.1 enhancement (add `kind` column to `edges` table).

**Agent traversal animation:** When the agent makes a `trie_trace` call,
the edges in the response's `edges` array are animated in sequence (200ms
delay between edges) with a travelling dot (CSS `stroke-dashoffset` animation
on the SVG path). Edges already visited in this turn are rendered at 35%
opacity.

### 7.5 Agent state visuals

Each `SymbolNode` has an `agentState` field: `'idle' | 'reading' | 'writing' | 'stale'`.

| State     | Visual                                                                                           |
| --------- | ------------------------------------------------------------------------------------------------ |
| `idle`    | Default style — no special border or glow                                                        |
| `reading` | Node border: 2px solid `#3b82f6` (blue), soft box-shadow glow. CSS keyframe animation, 1.5s loop |
| `writing` | Node border: 2px solid `#f59e0b` (amber), stronger box-shadow glow. 1.0s loop                    |
| `stale`   | Node border: 1px dashed `#f97316` (orange). Static, no animation                                 |

`reading` → `idle`: 800ms after the corresponding `tool.result` event arrives.
`writing` → `idle`: 1200ms after the `tool.result` event arrives, OR after
updated prose is fetched and applied (whichever is later).
`stale`: set when a `write_file` tool result is detected for this node's file
and `trie refresh` has not yet run. Cleared on next project open or when the
graph is refreshed.

**Agent state badge** (bottom-right of node footer):

- `reading` → small blue dot, pulsing
- `writing` → small amber dot, pulsing
- `stale` → small orange triangle icon
- `idle` → nothing shown

### 7.6 Node expand (callers/callees)

When the user double-clicks a `↓` or `↑` badge:

```typescript
async function expandNode(qname: string, direction: "callers" | "callees") {
  const result = await graphClient.trace({
    from_qname: qname,
    direction: direction === "callers" ? "callers" : "callees",
    depth: 2,
  });

  const newQnames = Object.keys(result.nodes).filter(
    (q) => !graphStore.hasNode(q),
  );

  if (newQnames.length === 0) return; // nothing to add

  // Fetch SymbolDetail for each new node
  const details = await Promise.all(
    newQnames.map((q) =>
      graphClient.grep({ predicate: { name_contains: "" } }),
    ),
    // Actually: POST /read for each qname, extract the metadata
  );

  // Add new nodes and edges to graph store
  graphStore.addNodes(newQnames.map(toSymbolNode));
  graphStore.addEdges(result.edges.filter((e) => isNewEdge(e)));

  // Incremental ELK layout: only reposition new nodes, keep existing positions
  await elkLayoutIncremental(newQnames);
}
```

Nodes that are already on the canvas are NOT re-added — their existing
position is preserved. Only genuinely new nodes are laid out.

### 7.7 Semantic zoom levels

Implemented via `onViewportChange` in React Flow. The `zoom` value maps to
three rendering modes inside `SymbolNode`:

| Zoom range          | Mode         | Node renders                                                                                            |
| ------------------- | ------------ | ------------------------------------------------------------------------------------------------------- |
| `zoom < 0.25`       | Architecture | Kind badge + name only. One-liner hidden. All prose panels forced closed. FileGroupNode label enlarged. |
| `0.25 ≤ zoom < 0.7` | Module       | Header row + one-liner. Footer hidden. Prose panel hidden.                                              |
| `zoom ≥ 0.7`        | Symbol       | Full node: header + one-liner + footer. Prose panel shown if expanded.                                  |

`SymbolNode` reads `useViewport()` and conditionally renders content.
No React Flow `hidden` property — nodes stay mounted to preserve culling state.

### 7.8 ELK layout configuration

ELK runs in a WebWorker (`elk.min.js` in the public directory).

```javascript
const ELK_OPTIONS = {
  "elk.algorithm": "layered",
  "elk.direction": "DOWN",
  "elk.layered.spacing.nodeNodeBetweenLayers": "100",
  "elk.spacing.nodeNode": "50",
  "elk.layered.crossingMinimization.strategy": "LAYER_SWEEP",
  "elk.layered.nodePlacement.strategy": "BRANDES_KOEPF",
  "elk.layered.compaction.postCompaction.strategy": "EDGE_LENGTH",
  "elk.hierarchyHandling": "INCLUDE_CHILDREN", // respects FileGroupNode parents
};
```

`INCLUDE_CHILDREN` makes ELK aware of the parent-child relationship between
`FileGroupNode` and its `SymbolNode` children — it layouts children within the
parent's bounding box.

Layout is triggered (debounced 100ms) when:

1. The node or edge count in `graphStore` changes.
2. A new project is opened.

Layout is NOT triggered when:

- Agent state changes (reading/writing animations).
- A prose panel expands/collapses (handled by node auto-height, not relayout).
- The user pans or zooms.

**Incremental layout** (for expand operations): When new nodes are added via
an expand call, only the new nodes are repositioned. Existing nodes keep their
current React Flow positions (`node.position`). New nodes are laid out in a
sub-graph anchored to the expanded node's position.

### 7.9 Multi-node selection

Box selection: shift+drag draws a selection rectangle. All `SymbolNode`s whose
bounds intersect the rectangle are selected.

Shift+click: add/remove individual nodes from selection.

When multiple nodes are selected:

- All selected nodes show the selection ring.
- Clicking any selected node inserts its `@qname` pill into the input bar
  AND inserts the remaining selected nodes' pills too — the entire selection
  is transferred to the input bar at once.
- The selection is cleared after the pills are inserted.

---

## 8. @mention Input System

### 8.1 MentionInput component

The input bar's text field is a `contentEditable` div, not a standard
`<textarea>`. This allows inline rendering of styled pill components mixed
with free text.

```typescript
// MentionInput.tsx
// Renders: [ @auth/middleware:require_auth × ] [ type a prompt... ]
// where the pill is a non-editable inline element and the rest is
// free contentEditable text.
```

**Node click → pill insertion:**

When the user clicks a `SymbolNode`:

1. The node is selected (selection ring applied).
2. A `@{qname}` pill is appended to the input bar's current content.
3. Focus moves to the input bar (cursor placed after the pill).
4. If the node was already in the selection (multi-select scenario), all
   currently selected nodes' pills are inserted at once.

**Pill appearance:**

```
  ┌──────────────────────────────────────┐
  │ @auth/middleware:require_auth  ×     │
  └──────────────────────────────────────┘
```

- Background: `#1e293b` (dark slate), border `#334155`
- Text: `#94a3b8` for the `@` prefix, `#e2e8f0` for the qname
- `×` button removes the pill; the corresponding node loses its selection ring
- Keyboard: Backspace at the start of a pill deletes it

**Typing `@` manually:**
When the user types `@` in the input bar, a small autocomplete dropdown appears
showing the top 10 symbols by inbound count. Typing further characters filters
by `name_contains`. Selecting an entry from the dropdown inserts a pill.
This is the power-user path; most users will click nodes on the canvas.

### 8.2 @mention resolution before send

When the user hits Enter (or the Send button):

```typescript
async function sendMessage(pills: Pill[], freeText: string) {
  // 1. Resolve each pill to its full prose
  const resolved = await Promise.all(
    pills.map(async (pill) => {
      const result = await graphClient.read({ qname: pill.qname });
      return {
        qname: pill.qname,
        prose: result.prose,
        signature: result.signature,
        sourcePointer: result.source_pointer,
      };
    }),
  );

  // 2. Build the message content
  let content = "";
  if (resolved.length > 0) {
    content += "Relevant symbols (from trie graph):\n\n";
    for (const r of resolved) {
      content += `---\n`;
      content += `Symbol: ${r.qname}\n`;
      content += `Source: ${r.sourcePointer}\n`;
      content += `Signature: ${r.signature}\n\n`;
      content += r.prose + "\n";
      content += `---\n\n`;
    }
    if (freeText.trim()) {
      content += `User instruction:\n${freeText.trim()}`;
    }
    // Empty free text with pills: pass the raw pills+content to opencode.
    // The agent decides what to do with the context.
  } else {
    content = freeText.trim();
  }

  // 3. POST to opencode
  await opencodeClient.sendMessage(sessionId, content);
}
```

The resolved prose block is the agent's context. The "User instruction" section
is the explicit directive. The agent is free to roam beyond the pinned symbols
— the selection is a hint, not a constraint.

### 8.3 Empty prompt with @mentions

If `freeText` is empty and pills exist, the message is sent as-is (just the
resolved prose blocks, no explicit instruction). opencode receives the context
and the agent decides what to do — it will typically describe what it sees,
identify relationships, or ask what the user wants to do with these symbols.

---

## 9. Model Configuration

opencode handles model configuration natively. The desktop app surfaces it
through a minimal UI that writes directly to the project's `opencode.json`
or to opencode's global config.

### Model selector pill

Located at the far left of the input bar.

```
  [ claude-sonnet-4-6  ▾ ]
```

Clicking opens a popover:

```
  ┌─────────────────────────────────────┐
  │  Model                              │
  │  ┌─────────────────────────────┐    │
  │  │ claude-sonnet-4-6           │    │  ← freeform text input
  │  └─────────────────────────────┘    │
  │                                     │
  │  Provider                           │
  │  ○ Anthropic  ○ OpenAI             │
  │  ○ OpenRouter  ○ Local (Ollama)    │
  │                                     │
  │  API Key                            │
  │  [ Set key for Anthropic... ]       │  ← opens ApiKeyModal
  │                                     │
  └─────────────────────────────────────┘
```

The provider + model string maps to opencode's `model` config field. The
desktop app writes this to `~/.config/opencode/config.json` via
`POST /config` on the opencode HTTP API (or equivalent opencode config
write endpoint). It does NOT edit config files directly.

### API key storage

API keys are stored in macOS Keychain via `keytar` (Electron main process).
They are never in renderer memory, never in localStorage, never on disk in
plaintext.

```typescript
// electron/keychain.ts
import keytar from "keytar";
const SERVICE = "ai.trie.app";

export async function getApiKey(provider: string): Promise<string | null> {
  return keytar.getPassword(SERVICE, provider);
}

export async function setApiKey(provider: string, key: string): Promise<void> {
  return keytar.setPassword(SERVICE, provider, key);
}
```

When a model API call needs the key, the Electron main process retrieves it
from Keychain and injects it into the opencode daemon's environment on spawn
(via `process.env` in `ProcessManager.startForProject`). The renderer never
touches the key.

---

## 10. State Management

### `graphStore` (Zustand)

```typescript
interface GraphStore {
  // React Flow state — passed directly to <ReactFlow nodes={} edges={} />
  nodes: Node<SymbolNodeData>[];
  edges: Edge<EdgeData>[];

  // Graph operations
  setGraph: (nodes: Node[], edges: Edge[]) => void;
  addNodes: (nodes: Node[]) => void;
  addEdges: (edges: Edge[]) => void;
  removeNode: (qname: string) => void;
  hasNode: (qname: string) => boolean;

  // Node state mutations
  setNodeAgentState: (qname: string, state: AgentState) => void;
  setNodeProse: (qname: string, prose: string) => void;
  expandNode: (qname: string) => void;
  collapseNode: (qname: string) => void;
  selectNode: (qname: string) => void;
  deselectNode: (qname: string) => void;
  deselectAll: () => void;

  // Sidebar integration
  selectedFilePath: string | null;
  setSelectedFilePath: (path: string | null) => void;
  // Derived: Set<qname> of all nodes whose file_path === selectedFilePath
  highlightedQnames: Set<string>;
}

interface SymbolNodeData {
  qname: string;
  name: string;
  kind: SymbolKind;
  filePath: string;
  startLine: number;
  endLine: number;
  signature: string | null;
  oneLiner: string;
  isPublic: boolean;
  inboundCount: number;
  outboundCount: number;
  prose: string | null; // null = not yet loaded
  isProseLoading: boolean;
  isExpanded: boolean;
  agentState: AgentState;
  isSelected: boolean;
  isHighlighted: boolean; // from sidebar file selection
}

type AgentState = "idle" | "reading" | "writing" | "stale";
type SymbolKind = "function" | "class" | "method" | "constant" | "module";
```

### `agentStore` (Zustand)

```typescript
interface AgentStore {
  sessionId: string | null;
  running: boolean;
  currentTurn: TurnEvent[];
  history: Turn[];
  responseText: string | null; // accumulates assistant tokens
  error: string | null;

  setSession: (id: string) => void;
  startTurn: () => void;
  appendEvent: (event: TurnEvent) => void;
  appendToken: (token: string) => void;
  endTurn: () => void;
  failTurn: (error: string) => void;
}

interface TurnEvent {
  id: string; // matches tool call ID from opencode
  type: "tool_call" | "tool_result";
  tool: string;
  input?: Record<string, unknown>;
  output?: string;
  error?: string | null;
  timestamp: number;
  durationMs?: number; // set on tool_result
}

interface Turn {
  id: string;
  events: TurnEvent[];
  response: string;
  startedAt: number;
  completedAt: number;
}
```

### `appStore` (Zustand)

```typescript
interface AppStore {
  // Project
  projectDir: string | null;
  projectName: string;
  totalSymbols: number;
  totalFiles: number;

  // Server ports (set after ProcessManager reports servers-ready)
  opencodePort: number | null;

  serversReady: boolean;

  // Model config
  provider: "anthropic" | "openai" | "openrouter" | "local";
  modelId: string;
  apiKeySet: boolean;

  // UI state
  graphLoading: boolean; // true during initial ELK layout
  graphLoadingMessage: string;

  setProject: (dir: string, summary: ProjectSummary) => void;
  setServers: (ports: ServerPorts) => void;
  setModel: (provider: string, modelId: string) => void;
  setApiKeySet: (set: boolean) => void;
  setGraphLoading: (loading: boolean, message?: string) => void;
}
```

---

## 11. SSE Event Handler (`useOpenCodeSSE.ts`)

This hook is the bridge between opencode's event stream and the graph state.
It is mounted once in `App.tsx` after `serversReady = true`.

```typescript
export function useOpenCodeSSE(opencodePort: number, sessionId: string) {
  const graphStore = useGraphStore();
  const agentStore = useAgentStore();

  useEffect(() => {
    const es = new EventSource(
      `http://127.0.0.1:${opencodePort}/session/${sessionId}/events`,
    );

    es.onmessage = (event) => {
      const data = JSON.parse(event.data);

      switch (data.type) {
        case "tool.call": {
          agentStore.appendEvent({
            id: data.id,
            type: "tool_call",
            tool: data.tool,
            input: data.input,
            timestamp: data.timestamp,
          });
          handleToolCallAnimation(data, graphStore);
          break;
        }

        case "tool.result": {
          agentStore.appendEvent({
            id: data.id,
            type: "tool_result",
            tool: data.tool,
            output: data.output,
            error: data.error,
            timestamp: data.timestamp,
          });
          handleToolResultAnimation(data, graphStore);
          break;
        }

        case "assistant.token": {
          agentStore.appendToken(data.token);
          break;
        }

        case "session.status": {
          if (data.properties?.status?.type === "idle") {
            agentStore.endTurn();
            // trie-refresh plugin fires automatically at this point
            // Schedule a stale-check after 3 seconds to pick up
            // any nodes whose files were written during the turn
            setTimeout(() => refreshStaleNodes(graphStore, opencodePort), 3000);
          } else if (data.properties?.status?.type === "error") {
            agentStore.failTurn(
              data.properties.status.message ?? "Unknown error",
            );
          }
          break;
        }
      }
    };

    return () => es.close();
  }, [opencodePort, sessionId]);
}

function handleToolCallAnimation(
  event: ToolCallEvent,
  graphStore: GraphStore,
): void {
  const { tool, input } = event;

  if (tool === "trie_read" && input.qname) {
    graphStore.setNodeAgentState(input.qname, "reading");
  } else if (tool === "trie_explain_symbol" && input.sym) {
    // sym is a fuzzy name, not a qname — animate the best match
    const match = graphStore.findNodeByName(input.sym);
    if (match) graphStore.setNodeAgentState(match.data.qname, "reading");
  } else if (tool === "trie_patch" && input.qname) {
    graphStore.setNodeAgentState(input.qname, "writing");
  } else if (tool === "trie_patch_apply") {
    // All nodes with pending patches → writing state
    graphStore.nodes
      .filter((n) => n.data.pendingPatchCount > 0)
      .forEach((n) => graphStore.setNodeAgentState(n.data.qname, "writing"));
  } else if (tool === "write_file" && input.path) {
    graphStore.setFileAgentState(input.path, "writing");
  } else if (tool === "str_replace_editor" && input.path) {
    graphStore.setFileAgentState(input.path, "writing");
  } else if (tool === "trie_trace" && input.from_qname) {
    // Edge animation is handled via the trace result (we need the edges array)
    // Mark the root node as reading while the trace runs
    graphStore.setNodeAgentState(input.from_qname, "reading");
  } else if (tool === "trie_trace_flow" || tool === "trie_explain_flow") {
    if (input.symbol1) graphStore.setNodeAgentState(input.symbol1, "reading");
    if (input.symbol2) graphStore.setNodeAgentState(input.symbol2, "reading");
  }
}

function handleToolResultAnimation(
  event: ToolResultEvent,
  graphStore: GraphStore,
): void {
  const { tool, input, output } = event;

  // Reset reading states after a delay
  if (tool === "trie_read" && input?.qname) {
    setTimeout(() => graphStore.setNodeAgentState(input.qname, "idle"), 800);
    // If the output contains updated prose, patch it in
    try {
      const parsed = JSON.parse(output ?? "{}");
      if (parsed.prose) graphStore.setNodeProse(input.qname, parsed.prose);
    } catch {
      /* malformed output — ignore */
    }
  }

  if (tool === "trie_trace" && input?.from_qname) {
    setTimeout(
      () => graphStore.setNodeAgentState(input.from_qname, "idle"),
      800,
    );
    // If trace revealed new nodes not yet on canvas, add them
    try {
      const parsed = JSON.parse(output ?? "{}");
      if (parsed.nodes) graphStore.mergeTraceResult(parsed);
    } catch {
      /* ignore */
    }
  }

  if (tool === "trie_patch_apply") {
    // Re-fetch prose for all nodes that were in writing state
    const writingNodes = graphStore.nodes.filter(
      (n) => n.data.agentState === "writing",
    );
    Promise.all(
      writingNodes.map((n) =>
        graphClient.read({ qname: n.data.qname }).then((r) => {
          graphStore.setNodeProse(n.data.qname, r.prose);
          graphStore.setNodeAgentState(n.data.qname, "idle");
        }),
      ),
    );
  }

  if ((tool === "write_file" || tool === "str_replace_editor") && input?.path) {
    // Mark all nodes for this file as stale (trie-refresh hasn't run yet)
    graphStore.setFileAgentState(input.path, "stale");
  }
}
```

---

## 12. Startup Sequence

```
1. App launches
   ├─ Read stored { provider, modelId } from electron-store
   ├─ Check Keychain for API keys → set appStore.apiKeySet
   └─ Show "Open Project" screen if no recent project

2. User selects a project directory (file picker or recent project)
   ├─ appStore.setProject(dir)
   ├─ ProcessManager.startForProject(dir)
   │   ├─ Spawn opencode daemon (our fork)
   │   └─ Poll GET /desktop/graph/summary until 200 (15s timeout)
   │
   ├─ On servers-ready:
   │   ├─ POST /desktop/session → get sessionId (fresh session)
   │   ├─ GET /desktop/graph/summary → project summary
   │   ├─ appStore.setServers({ opencodePort })
   │   ├─ appStore.setProject(dir, summary)
   │   ├─ Mount useOpenCodeSSE hook (GET /desktop/event)
   │   └─ Start graph population (§7.2)
   │
   ├─ While ELK layout runs:
   │   appStore.setGraphLoading(true, `Laying out ${N} symbols...`)
   │
   └─ ELK complete → appStore.setGraphLoading(false)
      Input bar enabled.

3. App ready.
```

### Startup error states

| Error condition                  | Recovery                                                                                                                                                 |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `opencode` binary not found      | Modal: "opencode is not installed. Install it with: npm i -g opencode"                                                                                   |
| `trie` binary not found          | Modal: "trie is not installed. Install with: uv tool install trie"                                                                                       |
| opencode daemon port timeout | Retry once; then show error banner + "Retry" button |
| Project has no triefacts         | Banner: "No triefacts found. Run `trie sync` in your terminal to index this project." Graph still shows nodes from the graph DB (symbols without prose). |
| No API key for selected provider | Warning badge on model selector pill. Input bar remains enabled — opencode will surface its own error when the user tries to send.                       |

---

## 13. Component Hierarchy

```
<App>
  ├─ <ServerBootstrap>        # mounts after ipc:servers-ready; establishes session
  │   └─ <OpenCodeSSEProvider> # mounts useOpenCodeSSE hook
  │
  ├─ <OpenProjectScreen>      # shown before a project is loaded
  │
  └─ <Shell>                  # shown once project + servers are ready
       │
       ├─ <Sidebar>
       │   ├─ <FileTree>
       │   │   └─ <FileTreeNode> (recursive)
       │   └─ <ViewSourceModal> (React portal, conditionally mounted)
       │
       └─ <CanvasArea>         # flex column: graph + turn history + input bar
            │
            ├─ <GraphCanvas>
            │   ├─ <ReactFlow>
            │   │   ├─ nodeTypes:
            │   │   │   ├─ <SymbolNode> (×N)
            │   │   │   │   ├─ <KindBadge>
            │   │   │   │   ├─ <CountBadge direction="in">
            │   │   │   │   ├─ <CountBadge direction="out">
            │   │   │   │   ├─ <ProsePanel> (conditional, lazy)
            │   │   │   │   │   └─ <ReactMarkdown>
            │   │   │   │   └─ <AgentStateBadge>
            │   │   │   ├─ <FileGroupNode> (×M)
            │   │   │   └─ <HubPlaceholderNode> (×K)
            │   │   ├─ edgeTypes:
            │   │   │   └─ <SemanticEdge>
            │   │   ├─ <Background variant="dots">
            │   │   └─ <Controls>
            │   └─ <GraphLoadingOverlay> (shown during ELK layout)
            │
            ├─ <TurnHistoryPanel> (collapsible)
            │   ├─ <TurnSummaryBar> (always visible, single line)
            │   └─ <TurnEventList> (expanded)
            │       └─ <TurnEventRow> (×N)
            │
            └─ <InputBar>
                 ├─ <ModelSelector>
                 │   └─ <ModelPopover>
                 │       └─ <ApiKeyModal> (React portal)
                 ├─ <MentionInput>
                 │   └─ <MentionPill> (×N, one per @mention)
                 └─ <SendButton>
```

---

## 14. trie CLI Changes Required

Scope is minimal — the heavy lifting moved into the opencode fork. No new CLI
commands, no new Python deps, no new processes. Three targeted additions only.

### 14.1 stdout line-buffering fix

`trie/mcp_server.py`, inside `run_stdio()`:

```python
import sys
sys.stdout.reconfigure(line_buffering=True)
sys.stderr.reconfigure(line_buffering=True)
```

Ensures MCP responses flush immediately when opencode spawns `trie mcp serve`
as a child process.

### 14.2 `Store.symbols_in_file` method

Add to `trie/graph/store.py`:

```python
def symbols_in_file(self, file_path: str) -> list[SymbolDetail]:
    """Return SymbolDetail for all symbols whose file_path matches."""
```

Wraps the existing `symbols_in_file_with_lines` (returns `(qname, start, end)`
tuples) to return full `SymbolDetail` objects by joining with the triefact
one-liner cache. Used by the `trie_symbols_by_file` MCP tool below.

### 14.3 `trie_summary` and `trie_symbols_by_file` MCP tools

Add two new tools to `trie/mcp_server.py` (registered alongside the existing 15):

**`trie_summary`** — returns project aggregate counts:
```python
def trie_summary(self) -> dict:
    """Return project-level counts for the desktop app summary endpoint."""
    # SELECT COUNT(*) FROM symbols
    # SELECT COUNT(*) FROM symbols WHERE is_public = 1
    # SELECT COUNT(DISTINCT file_path) FROM symbols
    # SELECT COUNT(*) FROM edges
    # + trie.__version__ + project root basename
```

**`trie_symbols_by_file`** — returns all symbols for one source file:
```python
def trie_symbols_by_file(self, file_path: str) -> dict:
    """Return all symbols in file_path with their SymbolDetail fields."""
```

These are called by the opencode fork's `/desktop/graph/summary` and
`/desktop/graph/symbols-by-file` handlers via the existing MCP channel.

---

## 15. Implementation Phases

Each phase ships something runnable and useful. Each phase's completion
is a prerequisite for the next.

### Phase 0 — Scaffold

**Goal:** Electron app launches, shows a blank canvas, no crashes.

- `electron-vite` scaffold with React + TypeScript
- Tailwind CSS + basic layout (sidebar 220px, canvas flex, input bar 56px)
- React Flow installed, renders 3 hardcoded nodes
- ELK.js WebWorker running, positions those 3 nodes
- All 3 Zustand stores defined with initial state
- `ProcessManager` stub (logs "would spawn opencode" without spawning)

**Done when:** `npm run dev` launches the Electron window showing 3 positioned
nodes, TypeScript compiles cleanly.

### Phase 1 — opencode Fork: Desktop Route Group

**Goal:** The opencode fork serves `/desktop/*` endpoints. Frontend can query
real trie data and receive the graph-canvas SSE stream.

- Add `groups/desktop.ts` and `handlers/desktop.ts` to the opencode fork
- Wire into `api.ts` and `server.ts` (four-file change, §3.1)
- `POST /desktop/session`, `GET /desktop/event`, `GET /desktop/graph/summary`,
  `POST /desktop/graph/grep`, `POST /desktop/graph/read`,
  `POST /desktop/graph/trace`, `GET /desktop/graph/symbols-by-file` all live
- `graphClient.ts` in the frontend with typed wrappers for all `/desktop/graph/*`
- `trie_summary` and `trie_symbols_by_file` added to `trie/mcp_server.py`
- Smoke test: `ProcessManager` spawns opencode, frontend calls
  `POST /desktop/graph/grep` with `{ predicate: {}, limit: 10 }`, logs real
  symbol hits to console. `GET /desktop/event` stream delivers `desktop.connected`.

**Done when:** opencode fork running against trie's own repo responds correctly
to all `/desktop/*` endpoints, and the SSE stream delivers heartbeats.

### Phase 2 — Full Graph Population

**Goal:** Opening a real project shows the full symbol graph, laid out.

- `ProcessManager` spawns opencode fork as a child process
- Electron IPC relays `servers-ready` to renderer
- `useGraphPopulation` hook calls `POST /grep` (no limit), then batches
  `POST /trace` for top-200, builds nodes and edges
- `FileGroupNode` clustering implemented
- ELK layout with `INCLUDE_CHILDREN` running in WebWorker
- `GraphLoadingOverlay` with "Laying out N symbols..." message
- `fitView()` after layout completes
- Semantic zoom (§7.7) implemented in `SymbolNode`

**Done when:** Opening trie's own repo (1,373 symbols, 74 files) renders the
full graph, correctly clustered by file, within 15 seconds of project open.

### Phase 3 — Sidebar + Source Modal

**Goal:** Sidebar file tree works. Clicking a file highlights graph nodes.
Right-clicking shows source.

- `FileTree` component using Electron IPC `read-dir`
- Click handler → `graphStore.setSelectedFilePath` → `highlightedQnames`
  computed → `SymbolNode.isHighlighted` triggers highlight border
- `reactFlowInstance.fitView({ nodes: highlightedNodes })` on file click
- `ViewSourceModal` with CodeMirror 6 read-only, Python syntax highlighting
- Escape + outside-click dismiss

**Done when:** Clicking `trie/graph/store.py` in the sidebar highlights the
Store class and all its methods on the canvas and pans to them.

### Phase 4 — @mention Input System

**Goal:** Clicking a node inserts an @qname pill. Pill is styled, deletable.
Mention autocomplete on `@` keypress.

- `MentionInput` component (contentEditable + pill rendering)
- `MentionPill` component with delete button
- Node click → `graphStore.selectNode` → pill inserted into `MentionInput`
- Box select (shift+drag) → all selected nodes' pills inserted
- Autocomplete dropdown on `@` keypress (top-10 by inbound from `POST /grep`)
- Prose resolution logic (`useMentionResolver` hook) — calls `POST /read` for
  each pill before send

**Done when:** Clicking any node inserts a correctly styled pill. Hitting Send
with a pill attached logs the resolved prose + user text to the console.

### Phase 5 — opencode Integration + Agent Loop

**Goal:** Full agent loop working. Typing a prompt and hitting Send runs the
agent. The graph animates.

- `ProcessManager` spawns `opencode` daemon and waits for its HTTP server
- `opencodeClient.ts` with `createSession()`, `sendMessage()` methods
- `useOpenCodeSSE` hook connected to opencode's SSE stream
- `handleToolCallAnimation` and `handleToolResultAnimation` fully implemented
- All agent state visuals working (blue reading pulse, amber writing pulse)
- `TurnHistoryPanel` showing live tool call log
- `ResponsePanel` streaming assistant tokens above the input bar
- Input bar disabled during agent turn

**Done when:** Typing "what does require_auth do?" sends the message to
opencode, the `trie_read` call causes `require_auth`'s node to pulse blue,
and the answer appears in the response panel.

### Phase 6 — Write Visualization

**Goal:** Agent code writes are visible on the graph. Patch pipeline visualized.

- `write_file` and `str_replace_editor` tool calls → file nodes pulse amber
- `trie_patch` → node pulses amber (pending state)
- `trie_patch_apply` → nodes pulse amber, prose re-fetched after result,
  updated in place
- `stale` state shown after file writes until next session open
- Node prose updates rendered live as they arrive from `tool.result`

**Done when:** Asking the agent to "add a docstring to `slugify`" causes
`slugify`'s node to pulse amber during the write and then show updated prose
after `trie_patch_apply` completes.

### Phase 7 — Node Expand

**Goal:** Double-clicking a badge expands callers/callees onto the canvas.

- Double-click `↓` badge → `POST /trace` callers → new nodes added
- Double-click `↑` badge → `POST /trace` callees → new nodes added
- `HubPlaceholderNode` rendered for `truncated_at` qnames
- Incremental ELK layout for new nodes only
- Right-click context menu: "Expand callers", "Expand callees",
  "View source", "Remove from canvas"

**Done when:** Double-clicking the `↓` badge on `require_auth` adds its caller
nodes to the canvas with edges connecting them.

### Phase 8 — Model Config + API Key UI

**Goal:** User can change model and set API keys without touching a config file.

- `ModelSelector` pill + popover
- Provider radio buttons + freeform model input
- `ApiKeyModal` with password input → stored in macOS Keychain via `keytar`
- Stored `{ provider, modelId }` in `electron-store`
- API key injected into opencode daemon environment at spawn time
- Warning badge on model selector when no key set for current provider

**Done when:** User opens model popover, selects OpenAI, pastes an API key,
and the next agent turn uses GPT without touching any config file.

### Phase 9 — Distribution

**Goal:** Signed, notarized `.dmg`. Installable on a clean macOS machine.

- App icon (1024×1024 PNG, `electron-builder` generates `.icns`)
- `electron-builder.yml` with bundle ID `ai.trie.app`, universal binary target
- Code signing via `APPLE_CERTIFICATE` env var in CI
- Notarization via `electron-notarize` post-sign hook
- GitHub Actions workflow in `.github/workflows/app.yml`: build → sign →
  notarize → upload `.dmg` to GitHub Releases on version tag push.
  Runs from `app/` working directory. Triggered independently of the
  Python package release workflow.
- "Open Project" file picker as first-run screen (not hardcoded path)
- `Cmd+K` focus input, `Cmd+0` fit view, `Escape` clear selection
- Onboarding check: if trie or opencode not found on PATH, show installation
  instructions modal

**Done when:** A `.dmg` downloaded from GitHub Releases installs and runs
correctly on a fresh macOS machine with only opencode and trie installed
as prerequisites.

---

## 16. Non-Goals (v1)

These are explicitly deferred. Implementing any of them in v1 would delay
shipping without proportional user value at this stage.

| Deferred                                       | Rationale                                                                        | Target             |
| ---------------------------------------------- | -------------------------------------------------------------------------------- | ------------------ |
| Gesture-based topology changes                 | Requires topology validation + autonomous refactoring; unsolved research problem | v3+                |
| Simulation review (before/after graph diff)    | Requires versioned graph snapshots + topology diff algorithm                     | v2                 |
| Inline prose editing in nodes                  | Risk of coupling read and write surfaces before the edit model is clear          | v2                 |
| TypeScript support in graph                    | trie's parser is Python-only; SCIP integration needed                            | post-v0.2 trie CLI |
| Multi-repo / monorepo cross-graph              | Layout complexity; single project is the right first target                      | v3                 |
| Windows / Linux                                | Tauri supports them but Electron + keytar on macOS is the first target           | post-v1            |
| Multiplayer / shared sessions                  | Needs CRDTs or a sync server                                                     | v3+                |
| Mac App Store                                  | Sandboxing breaks spawning opencode/trie child processes                         | post-v1            |
| Graph search on canvas (Cmd+F)                 | Use the `@` autocomplete in the input bar instead                                | v1.1               |
| Auto-refresh stale nodes                       | `trie-refresh` plugin fires; nodes clear on next session open                    | v1.1               |
| Edge kind distinction (calls/imports/inherits) | Needs `kind` column in `edges` table                                             | v1.1               |
| Undo/redo for agent actions                    | opencode sessions are append-only by design                                      | v2                 |
| "New node" by drawing on canvas                | Semantic meaning of canvas-created nodes is undefined until gesture model lands  | v3+                |

---

## 17. Resolved Design Decisions

The questions that were open are now closed. This section records the
decisions and their rationale so future implementors don't re-open them.

**D1: opencode API stability — resolved by ownership**
We own the fork. The HTTP API is not a third-party contract we depend on; it
is ours to read and modify. API stability is a non-issue: if the desktop app
needs a shape change, we make it in the fork. Pin the fork at a specific
commit SHA in `app/package.json` (or lock via the monorepo) and update
deliberately. No versioning ceremony needed.

**D2: SSE event shape — resolved by adding a dedicated desktop route group**
Rather than parsing the existing general-purpose SSE stream (whose shape is
designed for the TUI/web app and changes without notice), we add a dedicated
`/desktop` HTTP API group to the opencode fork. This group owns its own
`GET /desktop/event` SSE endpoint that emits events shaped exactly for the
graph canvas — no inference, no fragile field extraction from a stream
designed for something else. See §3 (rewritten) for the full spec.

**D3: ELK performance ceiling — resolved as a runtime decision**
Measure on Phase 2 completion against a real large codebase. If ELK with
`INCLUDE_CHILDREN` exceeds 15 seconds for a project's full symbol set,
switch the initial load to a force-directed layout (d3-force, no WebWorker
needed, sub-second for 5k nodes) and reserve ELK for the per-file-group
sub-layouts only. This is a one-line config change in `ElkLayout.tsx` — not
a PRD-level decision.

**D4: opencode session lifecycle — resolved**
Create a fresh opencode session on each project open via `POST /session`.
Display recent turns from `GET /session/:sessionID/message` in the turn
history panel on load (last 20, paginated via the `?limit=20` param). No
session resumption — context bloat is a worse problem than history loss, and
the graph itself is the persistent state the user cares about.

**D5: trie MCP server ownership — dissolved by architecture change**
There is no second trie process. The opencode fork's `/desktop/graph/*`
endpoints proxy through opencode's own MCP client to the single `trie mcp
serve` stdio process opencode already manages. One MCP connection, one SQLite
WAL reader/writer. The `refresh_lock` mechanism already serializes concurrent
writes (`patch_apply` vs `trie refresh`). No new coordination needed.
