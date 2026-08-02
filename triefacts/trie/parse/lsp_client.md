---
trie_version: 0.3.0
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
  signature: class LspError(RuntimeError)
- kind: class
  qualified_name: trie/parse/lsp_client:LspClient
  lines: 40-235
  signature: class LspClient
- kind: method
  qualified_name: trie/parse/lsp_client:LspClient.__init__
  lines: 43-59
  signature: 'def __init__( self, command: list[str], root: Path, *, timeout: float = 20.0, ) -> None'
- kind: method
  qualified_name: trie/parse/lsp_client:LspClient.start
  lines: 63-93
  signature: def start(self) -> None
- kind: method
  qualified_name: trie/parse/lsp_client:LspClient.shutdown
  lines: 95-114
  signature: def shutdown(self) -> None
- kind: method
  qualified_name: trie/parse/lsp_client:LspClient.did_open
  lines: 118-129
  signature: 'def did_open(self, path: Path, language_id: str, text: str) -> None'
- kind: method
  qualified_name: trie/parse/lsp_client:LspClient.definition
  lines: 131-146
  signature: 'def definition(self, path: Path, line: int, character: int) -> list[dict[str, Any]]'
- kind: method
  qualified_name: trie/parse/lsp_client:LspClient._request
  lines: 150-169
  signature: 'def _request(self, method: str, params: Any, *, timeout: float | None = None) -> dict[str, Any]'
- kind: method
  qualified_name: trie/parse/lsp_client:LspClient._notify
  lines: 171-174
  signature: 'def _notify(self, method: str, params: Any) -> None'
- kind: method
  qualified_name: trie/parse/lsp_client:LspClient._send
  lines: 176-187
  signature: 'def _send(self, msg: dict[str, Any]) -> None'
- kind: method
  qualified_name: trie/parse/lsp_client:LspClient._read_loop
  lines: 189-219
  signature: def _read_loop(self) -> None
- kind: method
  qualified_name: trie/parse/lsp_client:LspClient._dispatch
  lines: 221-235
  signature: 'def _dispatch(self, msg: dict[str, Any]) -> None'
- kind: function
  qualified_name: trie/parse/lsp_client:_normalise_locations
  lines: 238-250
  signature: 'def _normalise_locations(result: Any) -> list[dict[str, Any]]'
- kind: constant
  qualified_name: trie/parse/lsp_client:__all__
  lines: 253-253
incoming_refs: 11
outgoing_refs: 0
---
<!-- trie:section symbol=trie/parse/lsp_client:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=b9700af35c181b9e59972aae73ff607cb3c04aa9eec3115d5cbd1cd1415ad118 source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=io -->
Minimal synchronous LSP client over stdio, implementing just enough of JSON-RPC to resolve `textDocument/definition` queries for a `ReferenceResolver`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lsp_client:LspError fingerprint=18b25fd2ae8d568208e643520e56cf1385090bd7708ab3d5b877c40cc963c521 body_fp=4f8cbe9e6e95220f264451934b8071162f0e74f8706b742feef756a012518f35 source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=model -->
## `class LspError(RuntimeError)`

Raised by `LspClient` for any failure: process spawn, transport, timeout, or protocol error.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lsp_client:LspClient fingerprint=0bec0a43ce6feabaf4775d0cc2776e9caee21f316ed207fbf1bfffaf11ebfded body_fp=2ea75164a9232692c9d8697bf52d374c9b15d4fc8dab76331151ec9b850aa7e6 source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=io -->
## `class LspClient`

Synchronous LSP client that spawns a language server process, performs the `initialize` handshake, and exposes `did_open` and `definition` over JSON-RPC stdio.

- `command`: argv used to spawn the server process
- `root`: workspace root; resolved to an absolute path on construction
- `timeout`: seconds to wait for each request response; default `20.0`
- All failure modes raise `LspError`; a background daemon thread reads server stdout and dispatches responses by id
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lsp_client:LspClient.__init__ fingerprint=b2dd1a1413435be4014f67011d3606e9770a47719f496f21717085adcc64242e body_fp=26f886c3e637fe025fbac9ad57f360c9006fa0473b199a9b2cb22c3d8d7558d9 source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=model -->
## `def __init__( self, command: list[str], root: Path, *, timeout: float = 20.0, ) -> None`

Initialise `LspClient` with the server command, workspace root, and optional request timeout; does not spawn the process.

- `command`: argv list used to launch the language server binary.
- `root`: resolved to an absolute path before use.
- `timeout`: seconds to wait for each request response; default 20.0.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lsp_client:LspClient.start fingerprint=32b4a2dcf753975b7642aaf3c308a87ace5cad38d68f09f917e59860f63b0a8a body_fp=101a8c4e83adce9f822680ee34b204da14f7032da940ff92c2b4f955622d4576 source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=io -->
## `def start(self) -> None`

Spawn the language server subprocess, start the background reader thread, and complete the LSP `initialize`/`initialized` handshake.

- Raises `LspError` if the process cannot be spawned or the `initialize` request times out.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lsp_client:LspClient.shutdown fingerprint=10ecc28644e24519d43b7b21c8df5868d89ecb27b4a508b2d588dcbe80bd3b57 body_fp=9de15a4c65c15e2929589bff4f07056290a9230e9182c7f88e15ac605a1d91b4 source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=io -->
## `def shutdown(self) -> None`

Attempt a graceful `shutdown`/`exit` handshake on `LspClient`, then unconditionally terminate and reap the server process.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lsp_client:LspClient.did_open fingerprint=1f0eb87d8b25b5005850bc44a55100e258eaa16a58673bb72bb0ebacf2de3960 body_fp=0a7d83fdec714085344e9012e9e00338bbf6ca119ecdf24b4a8715af8743e538 source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=io -->
## `def did_open(self, path: Path, language_id: str, text: str) -> None`

Send a `textDocument/didOpen` notification to the server for the given file.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lsp_client:LspClient.definition fingerprint=9b26ea234986ee33c0856d8c34b028f96330766f693e8650e5902556ce3418af body_fp=955e695912e3ad57ef8bc40b2e67d424516371960c9a9165fb659676a62876bf source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=io -->
## `def definition(self, path: Path, line: int, character: int) -> list[dict[str, Any]]`

Send `textDocument/definition` for a 0-based `(line, character)` position and return a normalised list of Location dicts.

- `line`, `character`: 0-based LSP position coordinates.
- Returns dicts with `uri` and `range` keys, regardless of whether the server returned a `Location`, `Location[]`, or `LocationLink[]`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lsp_client:LspClient._request fingerprint=bf6d652d9fc39f0b8b8e8532c6e8a4a34ff6ebaf10c1968ec5a80571baa9cb5f body_fp=f5b97be212d36dd50b04b31a0d0be1f687b8ead4619cbf924d300889c09ba1c7 source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=io -->
## `def _request(self, method: str, params: Any, *, timeout: float | None = None) -> dict[str, Any]`

Send a JSON-RPC request from `LspClient` and block until the matching response arrives or timeout elapses.

- `timeout`: overrides `self._timeout` for this call only; `None` uses the instance default.
- Raises `LspError` if the client is not running, the wait times out, or the response contains an error.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lsp_client:LspClient._notify fingerprint=1e8c71c9ed1e72bc31fa6365736e8460132199ede60fdb6f40f76fda0f995af3 body_fp=96d9a3eed1894c337c32134ee97be00ab3558c47a802c8a6cf9e730183350e00 source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=io -->
## `def _notify(self, method: str, params: Any) -> None`

Send a fire-and-forget JSON-RPC notification on `LspClient`; silently no-ops if the client is not alive.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lsp_client:LspClient._send fingerprint=6ea86a9068f8546af3529c01b352da3676379ef290e2df13862b167f4074b5fe body_fp=58d7c45814323438d0bbfcc43b75f2376956de3ea36e2f4c1ab0c76c1776a273 source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=io -->
## `def _send(self, msg: dict[str, Any]) -> None`

Serialize and write one LSP-framed JSON-RPC message to the server's stdin, raising `LspError` on pipe failure.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lsp_client:LspClient._read_loop fingerprint=355c83b8cc5d0a8579ecfa32850e2435694737a651451598eb9d4abbb6566277 body_fp=3425302ec6593deaf977de86b6ab75caa2c225f0c176fc50c68ef32b8a67e211 source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=io -->
## `def _read_loop(self) -> None`

Background thread target on `LspClient` that reads LSP-framed messages from the server's stdout and dispatches each parsed JSON message; on any error, marks the client dead and unblocks all pending request waiters.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lsp_client:LspClient._dispatch fingerprint=3bae4d60b73e7bca9eb1f034cd3f33e19e78d9c3bd3d22cdcb5046d10f8e6a1d body_fp=cfb234d18e2e19d42bcf2333158ac92565ce86ec1d94efe9c40a3e200116ac88 source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=io -->
## `def _dispatch(self, msg: dict[str, Any]) -> None`

Route a single parsed LSP message: correlate responses to pending requests, stub-reply server→client requests, and silently drop notifications.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lsp_client:_normalise_locations fingerprint=3ca8ead9b6753209a6ad585b7727807d2680b146f279a75582554ebf00a7ab2a body_fp=dcde2fe3ef90290d7611c7c392913abc02b130fcd810adc8f5e400b128cc3aad source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=util -->
## `def _normalise_locations(result: Any) -> list[dict[str, Any]]`

Normalise an LSP `textDocument/definition` result into a uniform list of `{"uri": ..., "range": ...}` dicts.

- `result`: accepts `None`, a single Location/LocationLink dict, or a list thereof.
- Returns an empty list for `None` or unrecognised item shapes.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lsp_client:__all__ fingerprint=33ac28f3b76013f3a348a7a19b8c58cd98ae0dcf6921425a4574945aa0285bbf body_fp=2703abbad93964d4f388c58e70d52a37c94cd1e54fd5632911aab49366fe964a source_ref=fe66e47012604dcb92db451756c135a70a8b5192 role=config -->
Declares the public API of the module, exporting `LspClient` and `LspError`.
<!-- trie:end -->