---
trie_version: 0.1.9
source: app/src/api/graphClient.ts
file_fingerprint: 985f936d0690aebc7a8e4e03768235bb68790481b45843bb2261cabca76d4ab0
last_synced_at: '2026-06-17T16:36:44Z'
defines:
- kind: constant
  qualified_name: app/src/api/graphClient:baseUrl
  lines: 20-20
- kind: function
  qualified_name: app/src/api/graphClient:setGraphClientBase
  lines: 22-24
- kind: function
  qualified_name: app/src/api/graphClient:trie
  lines: 27-27
- kind: function
  qualified_name: app/src/api/graphClient:post
  lines: 29-37
- kind: function
  qualified_name: app/src/api/graphClient:get
  lines: 39-48
- kind: constant
  qualified_name: app/src/api/graphClient:graphClient
  lines: 50-173
incoming_refs: 15
outgoing_refs: 12
---
<!-- trie:section symbol=app/src/api/graphClient:baseUrl fingerprint=1a01530948a7b687a8f996f379c2b9b35256032ca7f83de21e3c5db1c4ac7f6e body_fp=0256d0e4cf2ea45f59e73be351736b90954ab92188b494b1897162a7e3130c53 source_ref=5944ddf08ea91eb7ce47115d18fcadbfd9ca7263 role=config -->
Module-level mutable string holding the base URL prefix for all graph API requests; defaults to `""` and is set by `setGraphClientBase`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/graphClient:setGraphClientBase fingerprint=8238635467daaf9f4a8c7522cdd89ca6d3e91f744fd0afbf7cea44f414890de2 body_fp=8ede3ee0428d0684cc1e09b2b822c53e1206ed7292756987e8f9cbfd34bbb63f source_ref=5944ddf08ea91eb7ce47115d18fcadbfd9ca7263 role=config -->
Set the base URL for all `graphClient` requests using the given Opencode server port.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/graphClient:trie fingerprint=d81964481f895264e77431f65c590a5ffe9eef7a7a98fcfddb6a40ac89d33cf5 body_fp=56d5276b2e4b12135c9bd7e2e4bad27bf8560d87bfd313b3d36436f5f221bc24 source_ref=5944ddf08ea91eb7ce47115d18fcadbfd9ca7263 role=util -->
Return the `trie` IPC proxy object injected onto `window` by the Electron preload script.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/graphClient:post fingerprint=42dd4ca7c468cd41d0cab7f622db3daba9bfa367a6ea0cd6dd923d2a025ddc5a body_fp=91b329c5252e5e86a862b1da105f53b102662ad37a115ce154fb0a4d6fc89a4d source_ref=5944ddf08ea91eb7ce47115d18fcadbfd9ca7263 role=io -->
Send a POST request via the Electron IPC proxy to `baseUrl + path`, returning the parsed JSON response.

- `body`: serialised to JSON before dispatch
- Throws `Error` on HTTP 5xx responses
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/graphClient:get fingerprint=3ad3d4a089f3504c8dd240fcafec0753daeea8490adcab2d67d6d8b5aee30153 body_fp=276d8d739b80ee976ff28098c87199e7478116df66ae826d147787a9b6f73ed9 source_ref=5944ddf08ea91eb7ce47115d18fcadbfd9ca7263 role=io -->
Send a GET request via the IPC proxy to `baseUrl + path`, appending optional query params, and return the parsed JSON response.

- `params`: key-value pairs appended as URL search parameters.
- Throws `Error` if the response status is ≥ 500.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/graphClient:graphClient fingerprint=39dcc928da093d920dfaf14f361dfb8aa06ae4d2b8878ada69fe4dbc75a3a336 body_fp=7d5737767dcd7cd216037c315a9816d157266a440e11d07f899b04f8c6b11740 source_ref=5944ddf08ea91eb7ce47115d18fcadbfd9ca7263 role=api -->
Typed facade over all `/desktop/graph/*` endpoints, routing every call through the Electron IPC proxy via `get`/`post`.

- `summary` — fetches `ProjectSummary` for the current project.
- `allSymbols` — returns all indexed symbols, optionally ranked/limited.
- `allEdges` — returns all typed call-graph edges (`calls/references/imports/contains/inherits/implements`).
- `attention` — fetches AGM attention events and weight tables; `since` filters by Unix timestamp.
- `recordAttention` — persists a single durable attention event to the AGM.
- `setInvestigation` — declares or updates the current investigation task boundary.
- `systemModel` — fetches the classified, scored, layout-positioned system model; server-side cached.
- `grep` — searches symbols by predicate, with optional ranking and limit.
- `read` — reads full symbol detail by qualified name.
- `trace` — traces call-graph paths from a symbol, with optional direction and depth.
- `symbolsByFile` — lists symbols belonging to a given file path.
- `fileTriefact` — fetches the full triefact document (front matter + per-symbol sections) for a file.
- `fileSource` — fetches raw source text for a file.
- `activity` — fetches live writer status and working-tree stale set.
- `patches` — fetches pending patches grouped by symbol.
- `patchDrop` — drops pending patches for one symbol, or all session patches if `qname` is omitted.
- `patchApply` — applies all pending patches and returns an `ApplyReport`.
- `blastRadius` — computes cascade edit impact with hop distances for a symbol.
<!-- trie:end -->