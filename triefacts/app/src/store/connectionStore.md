---
trie_version: 0.1.9
source: app/src/store/connectionStore.ts
file_fingerprint: ef29eb0bef70997a5edcbc2039423f5a3d7437ba8cb2a13864837d14f8fc8eff
last_synced_at: '2026-06-17T16:40:16Z'
defines:
- kind: type
  qualified_name: app/src/store/connectionStore:ConnectionStatus
  lines: 12-12
- kind: interface
  qualified_name: app/src/store/connectionStore:ConnectionStore
  lines: 14-25
- kind: constant
  qualified_name: app/src/store/connectionStore:useConnectionStore
  lines: 27-47
incoming_refs: 5
outgoing_refs: 0
---
<!-- trie:section symbol=app/src/store/connectionStore:ConnectionStatus fingerprint=b243a666de0440716185b0eb002918536885792029e0e71e176ab5cee7384b7e body_fp=fed01c34aa8d6ebd31bc9f843712d8c41d65d38e17e62407b337f6a10605d32a source_ref=88a187b5eabfe184d87b91553c5e47bb0467c645 role=model -->
Union type representing the health state of the opencode sidecar connection.

- `connecting` — initial state before `servers-ready` fires
- `live` — sidecar is running and the SSE stream is healthy
- `degraded` — SSE stream errored but the process is still alive
- `crashed` — opencode process exited unexpectedly
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/connectionStore:ConnectionStore fingerprint=fdb9e77859cc5945bb5cd6ed2997916dd39a4697ae18f4a3e541741febce7bdb body_fp=1affaec5187cd4e3359e48d7549989d288402c549d391c98ebd7daaeb89c0544 source_ref=88a187b5eabfe184d87b91553c5e47bb0467c645 role=model -->
Zustand store interface tracking sidecar connection health and exposing state-transition actions.

- `exitCode`: process exit code captured on crash; `null` otherwise.
- `lastError`: most recent stderr or SSE error line; `null` if none recorded.
- `setDegraded`: ignored when `status` is already `"crashed"`.
- `setCrashed`: sets both exit code and optional error message atomically.
- `noteError`: updates `lastError` without changing `status`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/connectionStore:useConnectionStore fingerprint=a33bc6530c38df0cbaa0d58dc969db10a9007073ad40f2925cb14c2eeddc0c69 body_fp=28a9bcdfcc0d7bd8d0d22cf07e6cedc4634526027ff4ccaa98eeadaa05a2a26d source_ref=88a187b5eabfe184d87b91553c5e47bb0467c645 role=persistence -->
Zustand store tracking sidecar connection health, exposing `status`, `exitCode`, and `lastError` with four state-transition actions.

- `setLive` — resets to `"live"` and clears `exitCode`
- `setDegraded` — moves to `"degraded"` unless already `"crashed"`; optionally records error
- `setCrashed` — sets `"crashed"` with exit code and optional error message
- `noteError` — updates `lastError` without changing `status`
<!-- trie:end -->