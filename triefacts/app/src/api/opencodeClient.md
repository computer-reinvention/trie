---
trie_version: 0.1.9
source: app/src/api/opencodeClient.ts
file_fingerprint: 903de1181dba8eb4879537e752ad6755c00614e92fc1420acb00ee6876550f9c
last_synced_at: '2026-06-17T16:36:42Z'
defines:
- kind: constant
  qualified_name: app/src/api/opencodeClient:baseUrl
  lines: 22-22
- kind: function
  qualified_name: app/src/api/opencodeClient:setOpenCodeClientBase
  lines: 24-26
- kind: function
  qualified_name: app/src/api/opencodeClient:messageForStatus
  lines: 30-34
- kind: function
  qualified_name: app/src/api/opencodeClient:trie
  lines: 37-37
- kind: function
  qualified_name: app/src/api/opencodeClient:req
  lines: 39-58
- kind: constant
  qualified_name: app/src/api/opencodeClient:opencodeClient
  lines: 60-150
incoming_refs: 4
outgoing_refs: 5
---
<!-- trie:section symbol=app/src/api/opencodeClient:baseUrl fingerprint=1a01530948a7b687a8f996f379c2b9b35256032ca7f83de21e3c5db1c4ac7f6e body_fp=29d4317a9f445ed27685ea733007986276f9b02f6fcbfbf928f78115f0005f59 source_ref=bf7c620ba0f6b61fc588f827510df54670a950a9 role=config -->
Module-level mutable string holding the base URL (`http://127.0.0.1:<port>`) used by all `req` calls; initialised empty and set via `setOpenCodeClientBase`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/opencodeClient:setOpenCodeClientBase fingerprint=8238635467daaf9f4a8c7522cdd89ca6d3e91f744fd0afbf7cea44f414890de2 body_fp=cd75a043e7b765a22a2a9d57ebbdcc2be06f9412522f4814549ba4677b1f7022 source_ref=bf7c620ba0f6b61fc588f827510df54670a950a9 role=config -->
Set the base URL for all `opencodeClient` requests using the given localhost port number.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/opencodeClient:messageForStatus fingerprint=86f92268539c822a51289a3a35fa153e5cb1baeb537f33c79c96e71b979df851 body_fp=c26d615dafcfe8ed7ccf44689db5fb6718d0cf597d79d22101cafcae88ae525d source_ref=bf7c620ba0f6b61fc588f827510df54670a950a9 role=util -->
Return a human-readable error string for a given HTTP status code.

- `503` — server unreachable message
- `504` — timeout message
- other — generic message including the numeric status
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/opencodeClient:trie fingerprint=d81964481f895264e77431f65c590a5ffe9eef7a7a98fcfddb6a40ac89d33cf5 body_fp=6657142ce7470c21e9efeeb1c45a7d27e092f734790040627c52e70d4b9ee6b5 source_ref=bf7c620ba0f6b61fc588f827510df54670a950a9 role=util -->
Return the `trie` IPC proxy object injected onto `window` by the desktop shell.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/opencodeClient:req fingerprint=d69e41f01b48b6cb94c26502ab79c785aed1b7f26e5dc13b200738ea8a5b979c body_fp=601964e1bc95a6e152cf6d3cc0be88e01fc400df3a362a68c4b251711a85fe32 source_ref=bf7c620ba0f6b61fc588f827510df54670a950a9 role=io -->
Send an HTTP request via the IPC proxy (`window.trie.httpRequest`) and return the parsed response body with its status code.

- `body`: serialized to JSON if present; omitted from the request if undefined.
- `data`: `null` if the response body is empty or not valid JSON.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/opencodeClient:opencodeClient fingerprint=0943feff52c70daaf22a561235aa897f1d062bd67d9fa8ed5bf8cddecca69141 body_fp=6fbbc359cdcb36bfe964c83250184ffc80702bca1e76ea050bafc28bdac4d01d source_ref=bf7c620ba0f6b61fc588f827510df54670a950a9 role=api -->
Namespace object exposing all typed async methods for the opencode HTTP API, routed through the IPC proxy.

- `sendMessage` — throws on non-2xx; assistant response arrives separately via SSE
- `hasMessages` — issues a `limit=1` probe; used to prune empty stub sessions
- `listProviders` — returns `{ providers: [], default: {} }` on missing/malformed data
<!-- trie:end -->