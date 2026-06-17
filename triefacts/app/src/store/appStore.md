---
trie_version: 0.1.9
source: app/src/store/appStore.ts
file_fingerprint: 6c57505a5b446137b93d3b5f30e9c00a0e4facb56b0856424ebc8a4bf4d1b03b
last_synced_at: '2026-06-17T16:40:11Z'
defines:
- kind: interface
  qualified_name: app/src/store/appStore:AppStore
  lines: 3-24
- kind: constant
  qualified_name: app/src/store/appStore:useAppStore
  lines: 26-54
incoming_refs: 12
outgoing_refs: 0
---
<!-- trie:section symbol=app/src/store/appStore:AppStore fingerprint=7548bcaba772a3c6c427f79e6c2d1026116eea84ae106b8d93369050bff2e094 body_fp=6070a4749d1fca31b01b35ad4f329ca8bf45f5ab0872133967d7cc3a7fcc1e75 source_ref=6853e3d91ba8228477c3e5801affd5fbbb14fc40 role=model -->
Defines the shape of the global Zustand app store, combining project metadata, server state, model config, and graph loading state with their mutators.

- `projectDir`: null until a project is opened
- `opencodePort`: null until the backend server is ready
- `serversReady`: set to `true` by `setServers` once ports are assigned
- `apiKeySet`: tracks whether the active provider's API key is configured
- `graphLoading` / `graphLoadingMessage`: toggled during symbol graph fetch operations
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/appStore:useAppStore fingerprint=d3bc0570b278e88412ddc10d20d61cf0f3660432d00c0750f95d3b0944638aa4 body_fp=26f14108625d80ac6714a755d032416483b83dcc7ecddeafcabda6d4deac4dad source_ref=6853e3d91ba8228477c3e5801affd5fbbb14fc40 role=config -->
Zustand store hook managing global app state for project metadata, server ports, model selection, and graph loading.

- `serversReady`: set to `true` only via `setServers`, never directly
- `provider` / `modelId`: default to `"anthropic"` / `"claude-sonnet-4-6"`
- `setServers`: accepts `{ opencodePort, projectDir }` but only persists `opencodePort`
- `graphLoadingMessage`: defaults to `""` when not supplied to `setGraphLoading`
<!-- trie:end -->