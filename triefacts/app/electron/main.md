---
trie_version: 0.1.9
source: app/electron/main.ts
file_fingerprint: 56b95608475f8f0575396b1d6fe844ecfd72bddd39fd9d986a4461fdc5c6dcb5
last_synced_at: '2026-06-17T16:35:03Z'
defines:
- kind: module
  qualified_name: app/electron/main:__module__
  lines: 1-95
- kind: constant
  qualified_name: app/electron/main:win
  lines: 11-11
- kind: constant
  qualified_name: app/electron/main:pm
  lines: 12-12
- kind: function
  qualified_name: app/electron/main:brandIconPath
  lines: 16-23
- kind: function
  qualified_name: app/electron/main:createWindow
  lines: 25-66
incoming_refs: 0
outgoing_refs: 3
---
<!-- trie:section symbol=app/electron/main:__module__ fingerprint=38e097b17c8e58dc0cc33a16f38c36ed4236c7d5478c8e75ebb8c207426fda7f body_fp=252f8f0ec7748aa611bc472e098a8fd4a9f7cab1bf1bbd9a20f4d18e31ed1f3c source_ref=3afe26a370f2a8693b035ac65b64a3f93380e538 role=entrypoint -->
Electron main-process entry module that bootstraps the app, creates the `BrowserWindow`, registers IPC handlers, and manages lifecycle events.

- Sets app name to `"trie"` and overrides the macOS dock icon in dev builds.
- Calls `pm.killAll()` on `before-quit` and on `window-all-closed` (non-macOS) before `app.quit()`.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/main:win fingerprint=79b38863065c898dc1dfde929f5e7a354a80c447ce89ffaaf74be4c35cd53dc3 body_fp=b83d60c19902f62be93cc532326524f572d772000ab4091f8595d55f9011bcf4 source_ref=3afe26a370f2a8693b035ac65b64a3f93380e538 role=model -->
Module-level reference to the single `BrowserWindow` instance; `null` when no window exists.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/main:pm fingerprint=7557f6ffa83df4b887a3228831a90af422f6ed65daa320812c33d921e10cac13 body_fp=5ba7cb3c81745b2bc335e2e3dc8eb184aba1a51023824202785bfa4a9d924e3c source_ref=3afe26a370f2a8693b035ac65b64a3f93380e538 role=model -->
Module-level reference to the active `ProcessManager` instance; initialized in `createWindow` and used to clean up child processes on quit.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/main:brandIconPath fingerprint=a94a5a4aff246aebd9c14e444042af207ee2a01c89f26e9f85eccdaf14776db1 body_fp=c33183fe631b203fc9afd344c2d3d89563544c7748e6eba2da419dfb7e93bc67 source_ref=3afe26a370f2a8693b035ac65b64a3f93380e538 role=util -->
Resolve the first existing candidate path to `build/icon.png` relative to `__dirname`, returning `null` if none exist.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/main:createWindow fingerprint=657df1988f31443b27f67275682e7f4bd792de891adca93917430c25699b5d58 body_fp=102fa80362a4614f811e2412b8e8dc73d0114366a0b021bae443ceac01bbcc1f source_ref=3afe26a370f2a8693b035ac65b64a3f93380e538 role=orchestration -->
Instantiate the main `BrowserWindow`, attach a `ProcessManager`, register IPC handlers, and load the renderer via `file://`.

- In unpackaged builds, opens DevTools and forwards renderer console messages to main-process stdout.
- Sets `win` to `null` on window close.
<!-- trie:end -->