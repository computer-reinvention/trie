---
trie_version: 0.1.9
source: trie/parse/lsp_client.py
file_fingerprint: 2f4c4fe923a2c2c428933b0465e3c1b987cff2fe21882013d263fa3fc91beec9
last_synced_at: '2026-07-28T23:34:17Z'
description: A minimal Language Server Protocol client over stdio.
defines:
- kind: module
  qualified_name: trie/parse/lsp_client:__module__
  lines: 1-254
- kind: class
  qualified_name: trie/parse/lsp_client:LspError
  lines: 36-37
- kind: class
  qualified_name: trie/parse/lsp_client:LspClient
  lines: 40-235
- kind: method
  qualified_name: trie/parse/lsp_client:LspClient.__init__
  lines: 43-59
- kind: method
  qualified_name: trie/parse/lsp_client:LspClient.start
  lines: 63-93
- kind: method
  qualified_name: trie/parse/lsp_client:LspClient.shutdown
  lines: 95-114
- kind: method
  qualified_name: trie/parse/lsp_client:LspClient.did_open
  lines: 118-129
- kind: method
  qualified_name: trie/parse/lsp_client:LspClient.definition
  lines: 131-146
- kind: method
  qualified_name: trie/parse/lsp_client:LspClient._request
  lines: 150-169
- kind: method
  qualified_name: trie/parse/lsp_client:LspClient._notify
  lines: 171-174
- kind: method
  qualified_name: trie/parse/lsp_client:LspClient._send
  lines: 176-187
- kind: method
  qualified_name: trie/parse/lsp_client:LspClient._read_loop
  lines: 189-219
- kind: method
  qualified_name: trie/parse/lsp_client:LspClient._dispatch
  lines: 221-235
- kind: function
  qualified_name: trie/parse/lsp_client:_normalise_locations
  lines: 238-250
- kind: constant
  qualified_name: trie/parse/lsp_client:__all__
  lines: 253-253
incoming_refs: 5
outgoing_refs: 0
---
<!-- trie:section symbol=trie/parse/lsp_client:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=b9700af35c181b9e59972aae73ff607cb3c04aa9eec3115d5cbd1cd1415ad118 source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=io -->
Minimal synchronous LSP client over stdio, implementing just enough of JSON-RPC to resolve `textDocument/definition` queries for a `ReferenceResolver`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lsp_client:LspError fingerprint=18b25fd2ae8d568208e643520e56cf1385090bd7708ab3d5b877c40cc963c521 body_fp=47b26787843c0517903298a59b0fc0f0fc784507103a96b738570bc3ee673aef source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=model -->
Raised by `LspClient` for any failure: process spawn, transport, timeout, or protocol error.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lsp_client:LspClient fingerprint=0bec0a43ce6feabaf4775d0cc2776e9caee21f316ed207fbf1bfffaf11ebfded body_fp=41ff6237884b1e1e7d47360556d3b1851900966c0d87407b3297744f59ea65b4 source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=io -->
Synchronous LSP client that spawns a language server process, performs the `initialize` handshake, and exposes `did_open` and `definition` over JSON-RPC stdio.

- `command`: argv used to spawn the server process
- `root`: workspace root; resolved to an absolute path on construction
- `timeout`: seconds to wait for each request response; default `20.0`
- All failure modes raise `LspError`; a background daemon thread reads server stdout and dispatches responses by id
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lsp_client:LspClient.__init__ fingerprint=b2dd1a1413435be4014f67011d3606e9770a47719f496f21717085adcc64242e body_fp=6e36454b67e524f633f8d72acaac91cb567c6e5701344e9f2ca1571d566670d7 source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=model -->
Initialise `LspClient` with the server command, workspace root, and optional request timeout; does not spawn the process.

- `command`: argv list used to launch the language server binary.
- `root`: resolved to an absolute path before use.
- `timeout`: seconds to wait for each request response; default 20.0.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lsp_client:LspClient.start fingerprint=32b4a2dcf753975b7642aaf3c308a87ace5cad38d68f09f917e59860f63b0a8a body_fp=751fb35cccd6d9d14c8689a21faaa60d142c6740b41cb7d3ea0b0c2ef326ac58 source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=io -->
Spawn the language server subprocess, start the background reader thread, and complete the LSP `initialize`/`initialized` handshake.

- Raises `LspError` if the process cannot be spawned or the `initialize` request times out.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lsp_client:LspClient.shutdown fingerprint=10ecc28644e24519d43b7b21c8df5868d89ecb27b4a508b2d588dcbe80bd3b57 body_fp=238c6e3531052fc4d86916dcc49bb7f60b644d3ab5cd640ab79c93da1d84a08a source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=io -->
Attempt a graceful `shutdown`/`exit` handshake on `LspClient`, then unconditionally terminate and reap the server process.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lsp_client:LspClient.did_open fingerprint=1f0eb87d8b25b5005850bc44a55100e258eaa16a58673bb72bb0ebacf2de3960 body_fp=e046a863162d8648dc805eaf2ea22001de6409f08c53157db0b118a9c6c5e261 source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=io -->
Send a `textDocument/didOpen` notification to the server for the given file.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lsp_client:LspClient.definition fingerprint=9b26ea234986ee33c0856d8c34b028f96330766f693e8650e5902556ce3418af body_fp=edc5dab0d9fb2215f443620636d2c34bb4d907015bf399a92ce8240317455788 source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=io -->
Send `textDocument/definition` for a 0-based `(line, character)` position and return a normalised list of Location dicts.

- `line`, `character`: 0-based LSP position coordinates.
- Returns dicts with `uri` and `range` keys, regardless of whether the server returned a `Location`, `Location[]`, or `LocationLink[]`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lsp_client:LspClient._request fingerprint=bf6d652d9fc39f0b8b8e8532c6e8a4a34ff6ebaf10c1968ec5a80571baa9cb5f body_fp=30aa20abbf7c4bce22128f17386ab0963ff21d26195a14c48245c0aff91b0d42 source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=io -->
Send a JSON-RPC request from `LspClient` and block until the matching response arrives or timeout elapses.

- `timeout`: overrides `self._timeout` for this call only; `None` uses the instance default.
- Raises `LspError` if the client is not running, the wait times out, or the response contains an error.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lsp_client:LspClient._notify fingerprint=1e8c71c9ed1e72bc31fa6365736e8460132199ede60fdb6f40f76fda0f995af3 body_fp=83d69f73302ae2506415489ece227f01266a21e3779f9e4581b73b7193e4eda6 source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=io -->
Send a fire-and-forget JSON-RPC notification on `LspClient`; silently no-ops if the client is not alive.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lsp_client:LspClient._send fingerprint=6ea86a9068f8546af3529c01b352da3676379ef290e2df13862b167f4074b5fe body_fp=3ac03cd3b845ecf27699c4c82a66725fcf0c807f81c1f5d1bfad2bab9fd6e8b8 source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=io -->
Serialize and write one LSP-framed JSON-RPC message to the server's stdin, raising `LspError` on pipe failure.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lsp_client:LspClient._read_loop fingerprint=355c83b8cc5d0a8579ecfa32850e2435694737a651451598eb9d4abbb6566277 body_fp=c29419314288b2cfa55b278166bb40eaf3606d2079546320174740f73db8063b source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=io -->
Background thread target on `LspClient` that reads LSP-framed messages from the server's stdout and dispatches each parsed JSON message; on any error, marks the client dead and unblocks all pending request waiters.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lsp_client:LspClient._dispatch fingerprint=3bae4d60b73e7bca9eb1f034cd3f33e19e78d9c3bd3d22cdcb5046d10f8e6a1d body_fp=c0a86298a848a400ec62888ff06ba03ce1b99bf92762490ab063d16d7f642c01 source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=io -->
Route a single parsed LSP message: correlate responses to pending requests, stub-reply server→client requests, and silently drop notifications.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lsp_client:_normalise_locations fingerprint=3ca8ead9b6753209a6ad585b7727807d2680b146f279a75582554ebf00a7ab2a body_fp=18b81f4818cb512a35aba9069ed5461a40bea0046e54d8d8a07ce5eacf7c5f61 source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=util -->
Normalise an LSP `textDocument/definition` result into a uniform list of `{"uri": ..., "range": ...}` dicts.

- `result`: accepts `None`, a single Location/LocationLink dict, or a list thereof.
- Returns an empty list for `None` or unrecognised item shapes.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lsp_client:__all__ fingerprint=33ac28f3b76013f3a348a7a19b8c58cd98ae0dcf6921425a4574945aa0285bbf body_fp=2703abbad93964d4f388c58e70d52a37c94cd1e54fd5632911aab49366fe964a source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=config -->
Declares the public API of the module, exporting `LspClient` and `LspError`.
<!-- trie:end -->