---
trie_version: 0.1.9
source: app/electron/process-manager.ts
file_fingerprint: 5fd1106955d0b4dabbc27b90b6fef2bbf61ec9324c02e79a1ce8228407110df6
last_synced_at: '2026-06-17T16:35:35Z'
defines:
- kind: class
  qualified_name: app/electron/process-manager:ProcessManager
  lines: 9-227
- kind: property
  qualified_name: app/electron/process-manager:ProcessManager.opencodeProc
  lines: 10-10
- kind: property
  qualified_name: app/electron/process-manager:ProcessManager.opencodePort
  lines: 11-11
- kind: property
  qualified_name: app/electron/process-manager:ProcessManager.currentProjectDir
  lines: 12-12
- kind: property
  qualified_name: app/electron/process-manager:ProcessManager.currentTrieMcpBin
  lines: 13-13
- kind: property
  qualified_name: app/electron/process-manager:ProcessManager.expectingExit
  lines: 16-16
- kind: method
  qualified_name: app/electron/process-manager:ProcessManager.constructor
  lines: 18-18
- kind: method
  qualified_name: app/electron/process-manager:ProcessManager.getTrieMcpEntry
  lines: 23-26
- kind: method
  qualified_name: app/electron/process-manager:ProcessManager.restart
  lines: 30-32
- kind: method
  qualified_name: app/electron/process-manager:ProcessManager.startForProject
  lines: 34-132
- kind: method
  qualified_name: app/electron/process-manager:ProcessManager.runRefresh
  lines: 143-205
- kind: method
  qualified_name: app/electron/process-manager:ProcessManager.killAll
  lines: 207-212
- kind: method
  qualified_name: app/electron/process-manager:ProcessManager.getOpenCodePort
  lines: 214-216
- kind: method
  qualified_name: app/electron/process-manager:ProcessManager.getProjectDir
  lines: 219-221
- kind: method
  qualified_name: app/electron/process-manager:ProcessManager.getTrieCliBin
  lines: 224-226
- kind: function
  qualified_name: app/electron/process-manager:resolveResourcePaths
  lines: 232-285
- kind: function
  qualified_name: app/electron/process-manager:findFreePort
  lines: 297-314
incoming_refs: 3
outgoing_refs: 4
---
<!-- trie:section symbol=app/electron/process-manager:ProcessManager fingerprint=46e6d383457a27edecb414ce5d9e5e567a6c70ceea7d7a698229e71d3c58f5e9 body_fp=bd1154f0be142ac6db30dcf8d6fcf1ed678b53893634f3de45c389b526b3c19d source_ref=44dcb0dde68765733bfe46fe635cc6ff6fae54de role=orchestration -->
Manages the lifecycle of the bundled `opencode-server` and `trie-cli` subprocesses for a given project directory, relaying their stdio to the renderer via IPC.

- `win` — the `BrowserWindow` whose `webContents` receives all IPC events.
- `startForProject` — kills any prior server, finds a free port, writes MCP config, fires `trie refresh`, spawns `opencode-server`, and emits `ipc:servers-ready`; throws after 30 s if the server never signals ready.
- `restart` — no-op when no project is open; otherwise re-runs `startForProject`.
- `runRefresh` — fire-and-forget; streams JSONL lines from `trie refresh` as `ipc:trie-refresh` events; never throws.
- `killAll` — SIGTERMs the opencode process and marks the exit as expected.
- `getTrieMcpEntry` — returns `null` until a project has been opened.
- `ipc:opencode-exited` payload includes `expected: boolean` so the renderer can distinguish crashes from intentional teardowns.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/process-manager:ProcessManager.opencodeProc fingerprint=ff5fe49061e1691b71002a197e66f6f4a24215c4f561ecc3e3400a28e9975e8f body_fp=98ceaabbdf412302bc04b89be4dc368aad6f0983b233dde21de489ea35a64ea2 source_ref=44dcb0dde68765733bfe46fe635cc6ff6fae54de role=model -->
`ProcessManager.opencodeProc` is the handle to the currently-running opencode server child process, or `null` when no process is active.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/process-manager:ProcessManager.opencodePort fingerprint=fddae8483eedcf9b484a53fd304bb56d6368fc7d6e94877fbf651a6f6d0a09f3 body_fp=b1101048b488753cd9cfde02ba4255e44cbeeba8c6d667f0d47db7cede22b24a source_ref=44dcb0dde68765733bfe46fe635cc6ff6fae54de role=model -->
`ProcessManager.opencodePort` is the port number the opencode server is currently bound to, defaulting to `4096` and updated by `startForProject` via `findFreePort`.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/process-manager:ProcessManager.currentProjectDir fingerprint=990fe1ca8d41be0c70b85a56a34fd215672bff8f6a632e735a635bc2b2e02e37 body_fp=27e7897b13ee053f628cb8c042e824d006e98a8e8ba3b0f43af53a5d11b0869f source_ref=44dcb0dde68765733bfe46fe635cc6ff6fae54de role=model -->
`ProcessManager.currentProjectDir` stores the filesystem path of the currently-open project, or `null` before any project has been opened.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/process-manager:ProcessManager.currentTrieMcpBin fingerprint=9503bc637197654bea845b1da1150f8f3a8a50983236879085e5e6255027d370 body_fp=a52cb94f0f9c9e753e34566f7818b96c3e7ae8c51a08e7789c1d526dc69af70c source_ref=44dcb0dde68765733bfe46fe635cc6ff6fae54de role=model -->
`ProcessManager` attribute holding the absolute path to the bundled `trie-mcp` binary for the current project, or `null` before any project is opened.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/process-manager:ProcessManager.expectingExit fingerprint=0cbbe497ad93608f53c6e17e55b0c3af51196e90b76340044af6febddd448774 body_fp=499ce8592616ee2278dc1444bd855306a53985cdc53d400d9a4bd179c20f73ea source_ref=44dcb0dde68765733bfe46fe635cc6ff6fae54de role=model -->
`ProcessManager.expectingExit` is a boolean attribute set to `true` during intentional teardowns so the `exit` event is not reported to the renderer as a crash.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/process-manager:ProcessManager.constructor fingerprint=257c1be96ae69f4b01c2c69bdb6d78605f59175819fb007d0bf245bf48444c4a body_fp=8e1859590f0b52bbf6747ed2d9e0e0c78cae0490a4f76d74b48d9a066621a519 source_ref=44dcb0dde68765733bfe46fe635cc6ff6fae54de role=domain -->
Initializes a `ProcessManager` instance, storing the `BrowserWindow` used for all subsequent IPC sends.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/process-manager:ProcessManager.getTrieMcpEntry fingerprint=2e7974ecc6b355921c991d1658c94a61618c9fa8785fc6432cfa8cb7cb5f7a81 body_fp=6b48cfca9afef826501bddee11305b5d233207a002d2f37da0875b11c05d7f05 source_ref=44dcb0dde68765733bfe46fe635cc6ff6fae54de role=domain -->
Return the trie MCP entry for the currently-open project, or `null` if no project has been opened yet.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/process-manager:ProcessManager.restart fingerprint=8db429316ab9f83d2842c31c453cd8e6c39b87e272aa1560feb7263f52146bc2 body_fp=46d0490e5001dc55281837cdcf5dbd7a08e3ef17d6541e0580cd3cc393604b62 source_ref=44dcb0dde68765733bfe46fe635cc6ff6fae54de role=orchestration -->
Restarts the opencode server for the current project by delegating to `ProcessManager.startForProject`; no-op if no project is open.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/process-manager:ProcessManager.startForProject fingerprint=d3a0fe4009522d4402eedb5dec6fe299d34a8c76fb317b5236e1bfa531c41c05 body_fp=c8a5a9fdefbacefe57d705e01d5beb1b4d1ce576d8fa2c62fb32e67a79510b20 source_ref=44dcb0dde68765733bfe46fe635cc6ff6fae54de role=orchestration -->
Kill any running opencode server, then spawn a fresh one for `projectDir`, awaiting its ready signal before notifying the renderer via `ipc:servers-ready`.

- `projectDir` — absolute path used as `cwd` for the spawned server and written into `.opencode/opencode.json`
- Kills the prior process with `SIGTERM` before starting, preventing port/process leaks on re-open
- Finds a free port starting at 4096 via `findFreePort`
- Fires `runRefresh` (fire-and-forget) before spawning the server to pre-populate the trie graph
- Throws if the server does not emit `"opencode server listening"` within 30 seconds, including last 15 stderr lines
- Emits `ipc:opencode-stdout`, `ipc:opencode-stderr`, and `ipc:opencode-exited` IPC events to the renderer throughout the process lifetime
<!-- trie:end -->
<!-- trie:section symbol=app/electron/process-manager:ProcessManager.runRefresh fingerprint=7cf10279be944487963bceb76e12920fc582bfcea01beb7ab05ff5672d5b2988 body_fp=3bfbf3fedcf46b72fb3c25c427d20e95c2de3decf4d3566e56f7d02e14d316d3 source_ref=44dcb0dde68765733bfe46fe635cc6ff6fae54de role=io -->
Spawns `trie refresh --before-turn --json` and relays each JSONL stdout line to the renderer as an `ipc:trie-refresh` event; never throws on failure.

- `projectDir` — working directory for the subprocess
- `trieCliBin` — absolute path to the `trie-cli` binary
- Partial lines are buffered across chunks and flushed on exit
- Spawn errors emit `{ kind: "error" }` instead of propagating
- Non-JSON stdout lines are silently dropped
- On non-zero exit, last 10 stderr lines are included in the `exit` event
<!-- trie:end -->
<!-- trie:section symbol=app/electron/process-manager:ProcessManager.killAll fingerprint=f1a4200fa163ddf04b08820e38db9c9744602fc300627b1043f977ed4f321c76 body_fp=50ccdce0396d91e6dbffb59e0e7339b1917d9e70265b3d77c0fdafecb39d0e1a source_ref=44dcb0dde68765733bfe46fe635cc6ff6fae54de role=orchestration -->
Sends `SIGTERM` to the running opencode process and sets `expectingExit` so the exit event is not reported as a crash.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/process-manager:ProcessManager.getOpenCodePort fingerprint=7c89ce1f6ec35079e64bfcb61ef7c87ab4b72c41f01ff564d3c12ac2944cfa0a body_fp=fbbf46ad9150959d76528bfea6abc59ef2b367e59d0807e038a913ada617d221 source_ref=44dcb0dde68765733bfe46fe635cc6ff6fae54de role=util -->
Return the port number on which the `ProcessManager`'s opencode server is currently bound.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/process-manager:ProcessManager.getProjectDir fingerprint=3dfc20350ce742b6df39662f99520a959907422747e1b375f84d27efafc8ea21 body_fp=cb20f06ee1cae50880861e8c9d213325f2ffe8958264fbab2ff4eb342c86b9c3 source_ref=44dcb0dde68765733bfe46fe635cc6ff6fae54de role=domain -->
`ProcessManager.getProjectDir` returns the absolute path of the currently-open project, or `null` if no project has been opened yet.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/process-manager:ProcessManager.getTrieCliBin fingerprint=285ddf0019827afe27eb0341410799e02ae5f15dddfc1b4b47e65b9839016768 body_fp=5c10597bc514b7f91cec4de6b33d018d94160c6cfb86df9299a164185ed655b3 source_ref=44dcb0dde68765733bfe46fe635cc6ff6fae54de role=util -->
`ProcessManager.getTrieCliBin` returns the absolute path to the bundled `trie-cli` wrapper binary by delegating to `resolveResourcePaths()`.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/process-manager:resolveResourcePaths fingerprint=ea378379e540ff185341b22e08463f8598569098e20020cb1b5ef88d55d8ede4 body_fp=c3f10e05074ad633af92e069ebcb2e2acd4dae27706a46e679e86741686712cc source_ref=44dcb0dde68765733bfe46fe635cc6ff6fae54de role=config -->
Resolve absolute paths to the three bundled sidecar binaries (`opencode-server`, `trie-mcp`, `trie-cli`), chmod them executable, and return the paths.

- `opencodeBin` / `trieMcpBin`: throws `Error` if either binary is absent from the resources dir.
- `trieCliBin`: best-effort; logs a warning and continues if missing.
- In dev mode, walks up to 6 ancestor directories from `__dirname` to locate `resources/`.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/process-manager:findFreePort fingerprint=7880e6d59ccd9d6da16db3bcfe9189752ee276e1a64036b018e752bde7c0e871 body_fp=0560aee11d3603661fed7b475b86b70670ffb8c2dcf0c000d3396854acf5ddaa source_ref=44dcb0dde68765733bfe46fe635cc6ff6fae54de role=util -->
Resolve a free TCP port by binding a `net.createServer`, falling back to an OS-assigned port if `preferred` is occupied.

- `preferred`: starting port candidate, typically `4096`
- Returns the preferred port if free, otherwise an OS-chosen ephemeral port
<!-- trie:end -->