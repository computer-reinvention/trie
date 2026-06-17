---
trie_version: 0.1.9
source: app/src/store/opencodeConfigStore.ts
file_fingerprint: 6b154c8555acf4758a491d01c3581c16f44706058302585904c20f89d6d86fac
last_synced_at: '2026-06-17T16:40:25Z'
defines:
- kind: function
  qualified_name: app/src/store/opencodeConfigStore:trie
  lines: 6-6
- kind: interface
  qualified_name: app/src/store/opencodeConfigStore:OpencodeConfigStore
  lines: 13-24
- kind: constant
  qualified_name: app/src/store/opencodeConfigStore:saveTimer
  lines: 26-26
- kind: constant
  qualified_name: app/src/store/opencodeConfigStore:useOpencodeConfigStore
  lines: 28-80
incoming_refs: 2
outgoing_refs: 6
---
<!-- trie:section symbol=app/src/store/opencodeConfigStore:trie fingerprint=d81964481f895264e77431f65c590a5ffe9eef7a7a98fcfddb6a40ac89d33cf5 body_fp=d24e1aacc7c6983a4c86c07b4944a7125e44ff3fc568fc7f93570e27502ab0fa source_ref=ddeda50a059b9d9c5a467af28bc0a9b8d021b8d0 role=util -->
Return the `trie` bridge object injected onto `window` by the native host.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/opencodeConfigStore:OpencodeConfigStore fingerprint=5b5c32a1aa23115562d3bfa5db7789df679ac4e497b004506293913b56756f73 body_fp=6664e1939d8619c1e15b327d99ea2747d782d52cbc696149a19c9094023df7aa source_ref=ddeda50a059b9d9c5a467af28bc0a9b8d021b8d0 role=model -->
Zustand store shape for reading and mutating the project's `opencode.json` config, restricted to managed keys.

- `projectDir` — absolute path of the currently loaded project, or `null` if none
- `config` — full parsed config object held as an in-memory working copy
- `loaded` — `false` until the first `load` call resolves
- `saving` — `true` while an async write is in flight
- `dirtyRestart` — set to `true` when a pending change requires a process restart
- `getValue` — reads a JSON Pointer path from the working copy
- `setValue` — writes a JSON Pointer path and schedules a debounced save; pass `restart=true` to flag `dirtyRestart`
- `save` — sends only the managed top-level delta to the backend writer
- `restart` — triggers a process restart and clears `dirtyRestart`
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/opencodeConfigStore:saveTimer fingerprint=1b2858ede2cbb7611584732052a198b1d1efeac4f5f6ed6e3c51f8a228e7ca68 body_fp=f9e749db4e837f5633507604a293430575d96101334241ba04fdc2293c246b46 source_ref=ddeda50a059b9d9c5a467af28bc0a9b8d021b8d0 role=util -->
Module-level debounce handle storing the pending `setTimeout` ID for deferred `save` calls, or `null` when no save is queued.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/opencodeConfigStore:useOpencodeConfigStore fingerprint=73c139d9d13e6d8b60710058cd600591567c5f1990be5f20bbc5c36c3a9e82e4 body_fp=7dab3bc84709e98d8e26fa26309174c18d6d30cf0717db2a67da90df8cf1adf5 source_ref=ddeda50a059b9d9c5a467af28bc0a9b8d021b8d0 role=persistence -->
Zustand store managing read/write of the project's `opencode.json`, restricted to app-managed keys.

- `load` — fetches full config via `trie().opencodeConfig.read`; resets `dirtyRestart`
- `getValue` — resolves a JSON Pointer against the in-memory config copy
- `setValue` — deep-clones config, applies pointer mutation, debounces `save` by 400 ms; sets `dirtyRestart` if `restart` is truthy
- `save` — builds a managed-keys-only delta (absent keys sent as `null` to trigger deletion) and writes via `trie().opencodeConfig.write`; best-effort on error
- `dirtyRestart` — true when a pending change requires a process restart to take effect
<!-- trie:end -->