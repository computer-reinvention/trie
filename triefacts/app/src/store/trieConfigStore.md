---
trie_version: 0.1.9
source: app/src/store/trieConfigStore.ts
file_fingerprint: 7d846b4a228dae2f335d160d46ee7a97ea85ec3a8bc1545bcdc6b818f6336395
last_synced_at: '2026-06-17T16:40:44Z'
defines:
- kind: function
  qualified_name: app/src/store/trieConfigStore:trie
  lines: 6-6
- kind: interface
  qualified_name: app/src/store/trieConfigStore:TrieConfigStore
  lines: 14-26
- kind: constant
  qualified_name: app/src/store/trieConfigStore:saveTimer
  lines: 28-28
- kind: constant
  qualified_name: app/src/store/trieConfigStore:useTrieConfigStore
  lines: 30-78
incoming_refs: 5
outgoing_refs: 6
---
<!-- trie:section symbol=app/src/store/trieConfigStore:trie fingerprint=d81964481f895264e77431f65c590a5ffe9eef7a7a98fcfddb6a40ac89d33cf5 body_fp=6d4cf6beeefe9e4f5571d59ba4ffef7771a1c11a9b0755f3b8abdae9b5be42b0 source_ref=8becdf294ba43c9246990591a823f4295fc02c6b role=util -->
Return the `trie` bridge object injected onto `window` by the Tauri/Electron preload script.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/trieConfigStore:TrieConfigStore fingerprint=16fba85d5ce947ceaf2473127047b2647948f1fb83cd2610493cbd0478fb8d58 body_fp=589b99e1d9c304f2a9438e82851c4aae3512c409c51b6b95f59aa8bffd994ed3 source_ref=8becdf294ba43c9246990591a823f4295fc02c6b role=model -->
Zustand store shape for reading and writing the project's `trie.toml` configuration.

- `exists`: `false` when `trie.toml` is absent; UI should prompt to initialise.
- `config`: full parsed config kept as working copy for UI reads.
- `load`: fetches config from disk for the given `projectDir`.
- `getValue`: reads a JSON pointer path from the current `config`.
- `setValue`: writes a JSON pointer path and debounces a `save` call (400 ms).
- `save`: deep-merges only managed top-level tables back to main; skips if `!exists`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/trieConfigStore:saveTimer fingerprint=1b2858ede2cbb7611584732052a198b1d1efeac4f5f6ed6e3c51f8a228e7ca68 body_fp=2efa8b51eab74590e572fe93ca1c1361d2b78a6e0fae1aaf8d99a510d91799c1 source_ref=8becdf294ba43c9246990591a823f4295fc02c6b role=util -->
Module-level debounce handle that holds the pending `setTimeout` ID for deferred `save` calls, or `null` when no save is queued.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/trieConfigStore:useTrieConfigStore fingerprint=d2f283e1b61dafb8dc4caff17ea5ee73825d6a86ecd0effc7f58328ac2e7655a body_fp=ba72053333e89efeb4fefdd265d3a2c28d04f895f6ef92e59e01931cdc4f0db4 source_ref=8becdf294ba43c9246990591a823f4295fc02c6b role=persistence -->
Zustand store managing read/write of the project's `trie.toml`, restricted to app-managed top-level tables.

- `load`: reads config via `trie().trieConfig.read`; sets `exists: false` on failure
- `setValue`: deep-clones config, applies pointer mutation, then debounces `save` by 400 ms
- `save`: no-ops when `exists` is false; sends only `TRIE_MANAGED_TOP_KEYS` delta to `trie().trieConfig.write`
- `exists`: false when `trie.toml` is absent; UI should prompt initialisation in that state
- `lastError`: populated with server error message or stringified exception on write failure
<!-- trie:end -->