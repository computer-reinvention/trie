---
trie_version: 0.1.9
source: app/electron/preload.ts
file_fingerprint: a8d795fcb9bd6e5f9b0dc06daf96088064b24351bc8e2b5ed5af80a36fb62219
last_synced_at: '2026-06-17T16:35:00Z'
defines:
- kind: module
  qualified_name: app/electron/preload:__module__
  lines: 1-137
incoming_refs: 0
outgoing_refs: 0
---
<!-- trie:section symbol=app/electron/preload:__module__ fingerprint=6ef95087357c1538f92d7ac912e8cd4f439fb756c41d4f7068336854bae8aaa5 body_fp=611bd09d6f4accb1332c0636d94e8ec1781b1ddc3202666b639bd082a6ec392f source_ref=8ab67d9c6e73292d57b6ae527033a5e9a744f749 role=api -->
Exposes the `window.trie` API surface to the renderer via `contextBridge`, bridging all IPC calls through `ipcRenderer`.

- `openProject` / `getRecentProjects` / `showOpenDialog` — project lifecycle IPC invocations
- `onServersReady` — replaces prior listener before registering to prevent dev hot-reload stacking
- `httpRequest` — proxies fetch calls through the main process (renderer cannot reach 127.0.0.1 directly)
- `sseSubscribe` / `sseUnsubscribe` / `onSseEvent` / `onSseError` — SSE relay; `onSseEvent`/`onSseError` return an unsubscribe function
- `getApiKey` / `setApiKey` — legacy per-provider key IPC; key never stored in renderer memory
- `settingsGetAll` / `settingsSet` / `settingsReset` — VS Code-style prefs persisted in `prefs.json`
- `opencodeConfig.{read,write,restart}` — per-project `opencode.json` management
- `trieConfig.{read,write}` — per-project `trie.toml` management; `read` returns `{exists, config}`, `write` returns `{ok, error?}`
- `trieCommand.{run,cancel,isRunning,onEvent}` — trie CLI subprocess control; `run` returns `{ok, runId?, error?}`
- `secrets.{listProviders,hasProviderKey,setProviderKey,deleteProviderKey}` — Keychain-backed provider key management
- `agmSnapshotGet` / `agmSnapshotSet` — AGM frozen-layout snapshots scoped to a session under `.trie/`
- `readDir` / `readFile` — filesystem access for the sidebar tree
- `onOpencodeStderr` / `onOpencodeExited` / `onTrieRefresh` — process-output relays; each replaces any prior listener and returns an unsubscribe function
<!-- trie:end -->