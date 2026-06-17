---
trie_version: 0.1.9
source: app/electron/ipc-handlers.ts
file_fingerprint: 219a64f232fefc7262728a8bc6a42ce6cd53bed0fd18bb7ab2d30e43b58e2a91
last_synced_at: '2026-06-17T16:35:14Z'
defines:
- kind: constant
  qualified_name: app/electron/ipc-handlers:keytarModule
  lines: 16-16
- kind: function
  qualified_name: app/electron/ipc-handlers:getKeytar
  lines: 17-22
- kind: constant
  qualified_name: app/electron/ipc-handlers:KEYCHAIN_SERVICE
  lines: 24-24
- kind: constant
  qualified_name: app/electron/ipc-handlers:RECENT_PROJECTS_KEY
  lines: 25-25
- kind: constant
  qualified_name: app/electron/ipc-handlers:prefsPath
  lines: 29-29
- kind: function
  qualified_name: app/electron/ipc-handlers:readPrefs
  lines: 31-37
- kind: function
  qualified_name: app/electron/ipc-handlers:writePrefs
  lines: 39-42
- kind: function
  qualified_name: app/electron/ipc-handlers:registerIpcHandlers
  lines: 44-411
incoming_refs: 1
outgoing_refs: 11
---
<!-- trie:section symbol=app/electron/ipc-handlers:keytarModule fingerprint=1268e94d62cb55b11b4dd4d12d2957d5928f0aa951ab9db9e569d63880e9db62 body_fp=7805dff85a370c989ccaf98abce2e0ced8310bb787113b9df0811cf2e54a140a source_ref=3471186a97321bbdc361f444a88cd96848f4b6d0 role=config -->
Module-level cache holding the lazily imported `keytar` module, or `null` before first use.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/ipc-handlers:getKeytar fingerprint=fa2564031703f5041cea049e2374d95a61465437c2a8eb7fcb833896be14dc09 body_fp=5f0aea39ad6ab41053b50cba2b65cd896747f1f88881ee38ae264c9a98129494 source_ref=3471186a97321bbdc361f444a88cd96848f4b6d0 role=util -->
Lazily imports and caches the `keytar` native module, returning the cached instance on subsequent calls.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/ipc-handlers:KEYCHAIN_SERVICE fingerprint=234a79066185fb0ec268541d29b6d65b31b0a6c48f91adbe12fa1979ec57ebf5 body_fp=46be84c45939b4fece656b64e99669a74fd226097cfd486612151fb4ac93adff source_ref=3471186a97321bbdc361f444a88cd96848f4b6d0 role=config -->
Keychain service name used as the `service` argument for all `keytar` password operations.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/ipc-handlers:RECENT_PROJECTS_KEY fingerprint=60a127a9f480f661c17dce7eb6bc423d389344df9b24e41c189aa44871038032 body_fp=49bfe3ac5015de4bd5a5879faaca35c7ac0c3afe11658c402765414947c42bde source_ref=3471186a97321bbdc361f444a88cd96848f4b6d0 role=config -->
Key string used to namespace recent-projects entries in `prefs.json`.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/ipc-handlers:prefsPath fingerprint=ff2625c3146720d95c9ef17fae2451e3056aa9a7882c6367edf7e9f36c6fcf70 body_fp=c97c7ba1fd1b304491b22547fc667fe33a0d391832a724d56339b37f3f43aa9f source_ref=3471186a97321bbdc361f444a88cd96848f4b6d0 role=config -->
Absolute path to `prefs.json` inside Electron's `userData` directory, used as the non-secret preferences store.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/ipc-handlers:readPrefs fingerprint=de56bb8e4bf9d2db0bbc4cb70d0a23ef7b0dcea4d9f22b5b07bab85ae3f92589 body_fp=dec180c3865d43e10aec37a7831f1b67e35bf7f774f7eb7b142d1b4d8f37d650 source_ref=3471186a97321bbdc361f444a88cd96848f4b6d0 role=persistence -->
Read and parse the JSON preferences file at `prefsPath`, returning an empty object on any error.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/ipc-handlers:writePrefs fingerprint=9a8d2fa152378c7823e66c0879ae71a9f72b8830c3bcf954109cfdc33de3c03f body_fp=615370282f3d9d8799e25b32ef8552f8c0ee4e0a787a47548c285ec2addf147d source_ref=3471186a97321bbdc361f444a88cd96848f4b6d0 role=persistence -->
Serialize `data` as pretty-printed JSON and write it to `prefsPath`, creating the userData directory if absent.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/ipc-handlers:registerIpcHandlers fingerprint=e6335bc09d0c5abda62ac5156b31be906863eee21c2af52878b84e906f6285b7 body_fp=4f9f769d404c074e8ba7766ec89101218dd6e9889dcc8b1557cbba989c2edb3d source_ref=3471186a97321bbdc361f444a88cd96848f4b6d0 role=orchestration -->
Register all `ipcMain` handlers for the Electron main process, wiring the renderer to project management, config, CLI, and storage operations.

- `pm` — `ProcessManager` used to resolve ports, project dir, and trie binaries across handlers.
- Registers: `http-request` (HTTP proxy with 30 s timeout, synthetic 503/504 on failure), `sse-subscribe`/`sse-unsubscribe` (generation-guarded SSE proxy with 1 s auto-reconnect), `show-open-dialog`, `open-project`, `get-recent-projects`, `settings-{get-all,set,reset}`, `opencode-config-{read,write}`, `opencode-restart`, `trie-config-{read,write}`, `trie-command-{run,cancel,running}`, `provider-key{s-list,-has,-set,-delete}`, `agm-snapshot-{get,set}`, `get-api-key`, `set-api-key`, `read-dir`, `read-file`.
- AGM snapshots are capped at 40 sessions per project to bound file size.
- Connection errors never reject; all HTTP proxy failures resolve as status 503/504.
<!-- trie:end -->