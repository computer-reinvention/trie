---
trie_version: 0.1.9
source: app/src/App.tsx
file_fingerprint: f45d999d9c93fc5f29a6fd15c79e998b508ae6a5095cca96692fb1ff4f4969b3
last_synced_at: '2026-06-17T16:35:23Z'
defines:
- kind: function
  qualified_name: app/src/App:trie
  lines: 25-25
- kind: function
  qualified_name: app/src/App:AppShell
  lines: 27-87
- kind: function
  qualified_name: app/src/App:OpenProjectScreen
  lines: 89-193
- kind: function
  qualified_name: app/src/App:App
  lines: 195-248
incoming_refs: 0
outgoing_refs: 26
---
<!-- trie:section symbol=app/src/App:trie fingerprint=d81964481f895264e77431f65c590a5ffe9eef7a7a98fcfddb6a40ac89d33cf5 body_fp=359d99e581512a81d123a106f2707a6783657c3ef9784b94fcfb063cbdd0b45e source_ref=774f521925a4e288ebf7ae2d10e2abd81930d82e role=util -->
Return the `trie` native bridge object injected onto `window` by the Electron preload script.
<!-- trie:end -->
<!-- trie:section symbol=app/src/App:AppShell fingerprint=5670c6286747f8821c5a60bccac9aa1f007e431851eaf85f8dd2ee393d0adab7 body_fp=9b47ffd31d44c823e03650cc6cc2a931187f7de2e31a21147e15da8f24dd87a6 source_ref=774f521925a4e288ebf7ae2d10e2abd81930d82e role=orchestration -->
Render the main application shell composing all primary UI regions once a project is open.

- Returns `null` if `projectDir` is not yet set in app store.
- Registers `⌘,` / `Ctrl+,` to toggle and `Escape` to close the settings overlay.
- Mounts all background hooks: SSE stream, graph population, trie refresh, activity polling, connection health, and command effects.
<!-- trie:end -->
<!-- trie:section symbol=app/src/App:OpenProjectScreen fingerprint=b79e593f4633204af61226ffc5dffdfc37a2b9e0b6009fc69afd4dae1d4d1427 body_fp=130aaf71270014c933e1b51aff7d3e5765106d271a81d6ff51a9ec5450749a1b source_ref=774f521925a4e288ebf7ae2d10e2abd81930d82e role=api -->
Render the project-selection screen, auto-opening the most recent project on mount or falling back to a manual open dialog with a recent-projects list.

- `onOpen`: called after `trie().openProject()` resolves, signalling the parent to switch to `AppShell`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/App:App fingerprint=5362b430f2c0f5462b6c0ebf2566a657f35ae15f38fceea378a0221fcc0cbd62 body_fp=9930206b1401f3caf37c008ba640b715d16ab608df9f70215e037f517447cde5 source_ref=774f521925a4e288ebf7ae2d10e2abd81930d82e role=entrypoint -->
Root React component that bootstraps the app by registering the `onServersReady` sidecar callback, wiring API clients, loading settings/config, and rendering either `AppShell` or `OpenProjectScreen`.

- `onServersReady`: fires once; sets API base URLs, marks connection live, loads `trie.toml`, fetches project summary, then flips `projectOpened`.
<!-- trie:end -->