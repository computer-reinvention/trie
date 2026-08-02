---
trie_version: 0.3.0
source: trie/parse/resolvers/lsp_resolver.py
file_fingerprint: b3e190e71b1c526e835ad200ddb8db11b8dc96f8a2b91ddfe33df32f052b2fd8
last_synced_at: '2026-08-02T21:19:44Z'
description: Generic, language-agnostic `ReferenceResolver` backed by an LSP server.
defines:
- kind: module
  qualified_name: trie/parse/resolvers/lsp_resolver:__module__
  lines: 1-267
- kind: constant
  qualified_name: trie/parse/resolvers/lsp_resolver:CallSite
  lines: 38-38
- kind: constant
  qualified_name: trie/parse/resolvers/lsp_resolver:CallSiteExtractor
  lines: 42-42
- kind: class
  qualified_name: trie/parse/resolvers/lsp_resolver:LspServerSpec
  lines: 46-71
  signature: class LspServerSpec
- kind: method
  qualified_name: trie/parse/resolvers/lsp_resolver:LspServerSpec.is_available
  lines: 69-71
  signature: def is_available(self) -> bool
- kind: class
  qualified_name: trie/parse/resolvers/lsp_resolver:LspResolver
  lines: 74-204
  signature: class LspResolver
- kind: method
  qualified_name: trie/parse/resolvers/lsp_resolver:LspResolver.__init__
  lines: 77-85
  signature: 'def __init__(self, spec: LspServerSpec) -> None'
- kind: method
  qualified_name: trie/parse/resolvers/lsp_resolver:LspResolver.name
  lines: 88-89
  signature: def name(self) -> str
- kind: method
  qualified_name: trie/parse/resolvers/lsp_resolver:LspResolver.resolve_file
  lines: 91-102
  signature: 'def resolve_file( self, file_path: Path, source_root: Path, symbols: list[Symbol], ) -> list[Reference]'
- kind: method
  qualified_name: trie/parse/resolvers/lsp_resolver:LspResolver._client_for
  lines: 104-111
  signature: 'def _client_for(self, source_root: Path) -> LspClient'
- kind: method
  qualified_name: trie/parse/resolvers/lsp_resolver:LspResolver._await_ready
  lines: 113-149
  signature: 'def _await_ready( self, client: LspClient, file_path: Path, source_root: Path, sites: list[CallSite], ) -> None'
- kind: method
  qualified_name: trie/parse/resolvers/lsp_resolver:LspResolver._resolve_file_inner
  lines: 151-198
  signature: 'def _resolve_file_inner( self, file_path: Path, source_root: Path, symbols: list[Symbol], ) -> list[Reference]'
- kind: method
  qualified_name: trie/parse/resolvers/lsp_resolver:LspResolver.close
  lines: 200-204
  signature: def close(self) -> None
- kind: function
  qualified_name: trie/parse/resolvers/lsp_resolver:_symbols_by_line
  lines: 207-218
  signature: 'def _symbols_by_line(symbols: list[Symbol]) -> dict[int, str]'
- kind: function
  qualified_name: trie/parse/resolvers/lsp_resolver:_target_qname
  lines: 221-240
  signature: 'def _target_qname( def_path: Path, def_line: int, # 1-based source_root: Path, cache: dict[Path, dict[int, str]], ) -> str | None'
- kind: function
  qualified_name: trie/parse/resolvers/lsp_resolver:_file_symbols_by_line
  lines: 243-256
  signature: 'def _file_symbols_by_line(abs_path: Path, source_root: Path) -> dict[int, str]'
- kind: function
  qualified_name: trie/parse/resolvers/lsp_resolver:_uri_to_path
  lines: 259-263
  signature: 'def _uri_to_path(uri: str) -> Path | None'
- kind: constant
  qualified_name: trie/parse/resolvers/lsp_resolver:__all__
  lines: 266-266
incoming_refs: 40
outgoing_refs: 15
---
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=f2729d82dc68371cccbd25b017140aecb079ffc94f8389b457e123bab863107e source_ref=3be80bbceaf2380ed1dd92b08cafab72d7534c55 role=orchestration -->
Language-agnostic `ReferenceResolver` backed by an LSP server, resolving member-call edges that tree-sitter alone cannot derive.

- Drives a real language server (pyright, tsserver, etc.) over LSP stdio JSON-RPC.
- Language plug-in surface: `LspServerSpec` supplies the server command, LSP `languageId`, and a tree-sitter `CallSiteExtractor`.
- On any failure, `resolve_file` returns `[]`; callers fall back to tree-sitter-only results.
- `LspClient` instances are cached per source root to amortise server warm-up cost.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:CallSite fingerprint=d22e4301b1adf84a4c1b35596bb05d09a0efc7b8cf6046ea7a8b3ddede677f21 body_fp=008a8ecf400d004c6ce35e869814a7ec4a4ccc21f8254408885e7765cbeabf5c source_ref=3be80bbceaf2380ed1dd92b08cafab72d7534c55 role=model -->
Type alias for a 0-based `(line, character)` position identifying a member-call site within a source file.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:CallSiteExtractor fingerprint=a8f182633ed345f7c91813ca2fac2976ab19f7374d1bc13da2f93a49d27cc77a body_fp=f9601ffaa6f06d5f51b2ca77cc263100b1ba238cbe417b367c43cb1797948d28 source_ref=3be80bbceaf2380ed1dd92b08cafab72d7534c55 role=model -->
Type alias for a callable that accepts raw file bytes and yields `CallSite` positions to resolve.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:LspServerSpec fingerprint=dfd873f85d33d1cff5aaf8e55df39bc2b7d8a8fb174804a09f5c7ef0f977a64a body_fp=779566878e05125ec46ca24ebe40f55831e4bd24dd0a8910359e571c2fc198b6 source_ref=4735bbaade7f55f007c85927f5dd3a99e8e6f2da role=model -->
## `class LspServerSpec`

Frozen dataclass bundling all language-specific configuration needed to drive one LSP server for member-call resolution.

- `name`: resolver identity string used for telemetry (e.g. `"pyright"`)
- `command`: argv list to spawn the server in stdio mode
- `language_id`: LSP `languageId` string (e.g. `"python"`, `"typescript"`)
- `call_sites`: language-specific extractor yielding member-call sites from raw file bytes
- `init_timeout`: seconds to wait for the LSP initialize handshake; defaults to `15.0`
- `warmup`: seconds to sleep after `didOpen` before querying; defaults to `0.0`
- `ready_timeout`: max seconds to poll the first call site until the server returns a definition; defaults to `0.0` (no polling)
- `is_available()`: returns `True` if `command[0]` is found on `PATH`
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:LspServerSpec.is_available fingerprint=3da08adb8d99c293c0f1d2119418318521e43df83854896945caf451102eab10 body_fp=f0180a0bd6cc4a29f01fb4b57700f98b5a59a7f66f9ec0f80be70a1e5a4ad59d source_ref=3be80bbceaf2380ed1dd92b08cafab72d7534c55 role=util -->
## `def is_available(self) -> bool`

Returns `True` if `LspServerSpec.command` is non-empty and its first element resolves via `shutil.which`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:LspResolver fingerprint=31266820765cfc9fd95453fbbec805c9c5204b4a986f14faa1d1c8c98856c6d2 body_fp=925ac55bbf875768f71520defa445240de8b18d5d21a06984e5f66d798d151a8 source_ref=4735bbaade7f55f007c85927f5dd3a99e8e6f2da role=domain -->
## `class LspResolver`

Resolves member-call `Reference` edges for a source file by driving a language server over LSP via `LspClient`.

- `spec`: `LspServerSpec` supplying the server command, language ID, call-site extractor, init timeout, and optional warmup delay.
- `resolve_file`: returns `[]` on any `LspError` or unexpected exception, never raises.
- `_clients`: one `LspClient` per resolved source-root path, lazily started and reused across files to amortise server warm-up cost; client is constructed with `spec.init_timeout`.
- `_ready`: set of source-root keys whose server has passed the readiness probe; limits the `_await_ready` polling cost to once per workspace.
- `close`: must be called to terminate all cached server processes.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:LspResolver.__init__ fingerprint=999d40b53770a405c971151f29372cf4105bec5ac87e83e09743cca774e4ede9 body_fp=7dc8fa8ceca469397340bee024a1bed1d4aab03bc003ea7b086d56b075204f12 source_ref=4735bbaade7f55f007c85927f5dd3a99e8e6f2da role=domain -->
## `def __init__(self, spec: LspServerSpec) -> None`

Initialize `LspResolver` with the given `LspServerSpec`, setting up an empty per-root `LspClient` cache and an empty set of ready source roots.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:LspResolver.name fingerprint=7c0cdbac5b2dbb5d3e2d04c41ce73fe13d43032593f87ca9bd7402e63c005888 body_fp=65bc4714e885845eaf755d999dec1a949de2c03a5a28244edd7aefcd05666cd2 source_ref=3be80bbceaf2380ed1dd92b08cafab72d7534c55 role=model -->
## `def name(self) -> str`

`LspResolver.name` is the resolver's identity string, forwarded from its `LspServerSpec`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:LspResolver.resolve_file fingerprint=edbc274f25296c993f6993a8f7befc7edf8dab0c3b001d10a4023cddca1b9d4e body_fp=c348b21feca2909abf3014a80869ad8ccd5fcb8cc2f77bd7f4911f2f6edaf90c source_ref=3be80bbceaf2380ed1dd92b08cafab72d7534c55 role=domain -->
## `def resolve_file( self, file_path: Path, source_root: Path, symbols: list[Symbol], ) -> list[Reference]`

Run `LspResolver`'s full LSP-backed resolution for one file, returning `[]` on any failure.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:LspResolver._client_for fingerprint=b576ad5ea10cb9380737c159f0d81cf5d169771aaf78078ddf65431ccc3e70aa body_fp=2948c70a7fbaa86c041390901e97510f83248eea2dc349b484991911f559461d source_ref=192b085a4de586615b738fdd3c7ec0a90135239b role=orchestration -->
## `def _client_for(self, source_root: Path) -> LspClient`

Return a cached `LspClient` for the given `source_root`, creating and starting one with `spec.init_timeout` if none exists.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:LspResolver._await_ready fingerprint=12625e540844e19423f25cbe11f2182f0c75f6fa75c7bd5b7cb48fc7820f77e2 body_fp=7b5390b21d62b26f819dfdf8ac4d889009996461944ac07fe88c9a67b041c30d source_ref=4735bbaade7f55f007c85927f5dd3a99e8e6f2da role=domain -->
## `def _await_ready( self, client: LspClient, file_path: Path, source_root: Path, sites: list[CallSite], ) -> None`

Poll the first call site with exponential backoff until the LSP server returns a definition or `ready_timeout` is exhausted, then mark the workspace ready.

- `sites`: only the first entry is probed; no-op if empty.
- `ready_timeout ≤ 0`: returns immediately, skipping all polling.
- Workspace is marked ready regardless of whether a definition was found, so the probe runs at most once per `(server, workspace)` pair.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:LspResolver._resolve_file_inner fingerprint=162ebcb599b73be42cf509698b798138cebe6facb9f6d352eb8d49dc4b6f0556 body_fp=97d3b44a1c259af413b10a300dc43adf1f4a5acb9fc5e10f4297ad35d00fdbda source_ref=4735bbaade7f55f007c85927f5dd3a99e8e6f2da role=domain -->
## `def _resolve_file_inner( self, file_path: Path, source_root: Path, symbols: list[Symbol], ) -> list[Reference]`

Core implementation of `LspResolver.resolve_file`; opens the file via LSP, optionally sleeps for `spec.warmup` seconds, polls for server readiness via `_await_ready`, queries `textDocument/definition` at each call site, and maps results to project-internal `Reference` edges.

- `symbols`: caller-supplied symbols for the file, used to map source lines to qnames.
- Returns one `Reference(kind="calls")` per unique `(src_qname, tgt_qname)` pair; skips self-references and off-project definitions.
- Deduplicates edges via a `seen` set; takes only the first valid definition location per call site.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:LspResolver.close fingerprint=428dd72cb6cb85746554055d4a7afd23d80c7883a82a9f49a4d1a1959d438818 body_fp=2efb70016b20b6a2df28fa7bbe7b832c9f1a9326c913be4b19b24e6827c63cc8 source_ref=3be80bbceaf2380ed1dd92b08cafab72d7534c55 role=io -->
## `def close(self) -> None`

Shuts down all cached `LspClient` processes and clears the `LspResolver` client registry.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:_symbols_by_line fingerprint=250f20d873fa6b98dd6551d18e4b532ec3e78c8ea3be0b5d98e6a25573744b16 body_fp=eb583a49dd8b10d57d9ddc2311a31da7b886d3e865833e42b054236dae7e75d0 source_ref=3be80bbceaf2380ed1dd92b08cafab72d7534c55 role=util -->
## `def _symbols_by_line(symbols: list[Symbol]) -> dict[int, str]`

Map a list of `Symbol` objects to a dict keyed by 1-based line number, resolving overlaps to the innermost (shortest) enclosing symbol.

- Filters to `kind` values `"function"`, `"method"`, or `"class"` only.
- Larger symbols are written first so smaller (inner) ones overwrite their lines.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:_target_qname fingerprint=0c2d5318e886e74b54b30a7fd54dd089db9338d4c1ab4ef7d24c8bb54951a134 body_fp=6171bd055146c0232723f942129f6a5ad93d1cebda9be32ffe79e7e510c4fc91 source_ref=3be80bbceaf2380ed1dd92b08cafab72d7534c55 role=domain -->
## `def _target_qname( def_path: Path, def_line: int, # 1-based source_root: Path, cache: dict[Path, dict[int, str]], ) -> str | None`

Map an LSP definition location to the corresponding project symbol qname, or `None` if the definition falls outside the source root.

- `def_line`: 1-based line number as reported by LSP.
- `cache`: mutated in place; populated per resolved file path to avoid re-indexing.
- Returns `None` for off-project definitions (stdlib, `.venv`, `node_modules`).
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:_file_symbols_by_line fingerprint=e256374c6da429fc605bacf2eb0293dea64da00929c4789ac7bb5c202cfaf709 body_fp=1e4a8f0451d2cd09ed16d91e71e23e902457de7ff72d1330fa73fbecd2e8e8f0 source_ref=3be80bbceaf2380ed1dd92b08cafab72d7534c55 role=parsing -->
## `def _file_symbols_by_line(abs_path: Path, source_root: Path) -> dict[int, str]`

Index a file's symbols by 1-based start line, returning a `dict[int, str]` mapping line → `qualified_name`.

- Returns `{}` if `registry.extract_symbols` raises any exception.
- Keyed by `start_line` to avoid name-collision when mapping LSP definition locations.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:_uri_to_path fingerprint=964cc0b7330541035d0a849644c84634652e6a8219fd7bcea7f157e6df9ba96d body_fp=88b69c2c4903f241dc43834b1aac6ba76da4be52c84d2b53d88a714c70d1b983 source_ref=3be80bbceaf2380ed1dd92b08cafab72d7534c55 role=util -->
## `def _uri_to_path(uri: str) -> Path | None`

Convert a `file:`-scheme URI string to a `Path`, returning `None` for non-file URIs.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:__all__ fingerprint=b2c3f5860e0c7a880648e3efa115ea9760f2de66477dc56f3934e05457fe84f0 body_fp=51305da177b38332ddf72377d688a0e7ca50d2a86e8541cf3e99b5ee5d852617 source_ref=3be80bbceaf2380ed1dd92b08cafab72d7534c55 role=config -->
Declares the public API surface of the `lsp_resolver` module.
<!-- trie:end -->