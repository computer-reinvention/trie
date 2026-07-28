---
trie_version: 0.1.9
source: trie/parse/resolvers/lsp_resolver.py
file_fingerprint: e9b97e030c37cb055120a83d0fedc5d5b903a961903bd81ef78eeb7f1314ab78
last_synced_at: '2026-07-28T23:34:19Z'
description: Generic, language-agnostic `ReferenceResolver` backed by an LSP server.
defines:
- kind: module
  qualified_name: trie/parse/resolvers/lsp_resolver:__module__
  lines: 1-205
- kind: constant
  qualified_name: trie/parse/resolvers/lsp_resolver:CallSite
  lines: 38-38
- kind: constant
  qualified_name: trie/parse/resolvers/lsp_resolver:CallSiteExtractor
  lines: 42-42
- kind: class
  qualified_name: trie/parse/resolvers/lsp_resolver:LspServerSpec
  lines: 46-56
- kind: method
  qualified_name: trie/parse/resolvers/lsp_resolver:LspServerSpec.is_available
  lines: 54-56
- kind: class
  qualified_name: trie/parse/resolvers/lsp_resolver:LspResolver
  lines: 59-142
- kind: method
  qualified_name: trie/parse/resolvers/lsp_resolver:LspResolver.__init__
  lines: 62-67
- kind: method
  qualified_name: trie/parse/resolvers/lsp_resolver:LspResolver.name
  lines: 70-71
- kind: method
  qualified_name: trie/parse/resolvers/lsp_resolver:LspResolver.resolve_file
  lines: 73-84
- kind: method
  qualified_name: trie/parse/resolvers/lsp_resolver:LspResolver._client_for
  lines: 86-93
- kind: method
  qualified_name: trie/parse/resolvers/lsp_resolver:LspResolver._resolve_file_inner
  lines: 95-136
- kind: method
  qualified_name: trie/parse/resolvers/lsp_resolver:LspResolver.close
  lines: 138-142
- kind: function
  qualified_name: trie/parse/resolvers/lsp_resolver:_symbols_by_line
  lines: 145-156
- kind: function
  qualified_name: trie/parse/resolvers/lsp_resolver:_target_qname
  lines: 159-178
- kind: function
  qualified_name: trie/parse/resolvers/lsp_resolver:_file_symbols_by_line
  lines: 181-194
- kind: function
  qualified_name: trie/parse/resolvers/lsp_resolver:_uri_to_path
  lines: 197-201
- kind: constant
  qualified_name: trie/parse/resolvers/lsp_resolver:__all__
  lines: 204-204
incoming_refs: 5
outgoing_refs: 8
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
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:LspServerSpec fingerprint=2d3160298b4848044c8b1799888ae584e5edf60084c39e573a6347e63257f038 body_fp=28c5350132858a9a43b43b2618ce9cb1e418883eb86090008868cd4afb6cb1ed source_ref=3be80bbceaf2380ed1dd92b08cafab72d7534c55 role=config -->
Frozen dataclass bundling all language-specific configuration needed to drive one LSP server for member-call resolution.

- `name`: resolver identity string used for telemetry (e.g. `"pyright"`)
- `command`: argv list to spawn the server in stdio mode
- `language_id`: LSP `languageId` string (e.g. `"python"`, `"typescript"`)
- `call_sites`: language-specific extractor yielding member-call sites from raw file bytes
- `is_available()`: returns `True` if `command[0]` is found on `PATH`
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:LspServerSpec.is_available fingerprint=3da08adb8d99c293c0f1d2119418318521e43df83854896945caf451102eab10 body_fp=f2adfa5ac4ceb4abd96adf70ba8247d579e5f78a103b2682ead8a06f451d98d9 source_ref=3be80bbceaf2380ed1dd92b08cafab72d7534c55 role=util -->
Returns `True` if `LspServerSpec.command` is non-empty and its first element resolves via `shutil.which`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:LspResolver fingerprint=54a588c7ab333a8bb779c7b831b87eec43ee4638b1bf6191e4b0e7619716e77b body_fp=ac2f344b04c264214f11a7d1fdb28ec68c6f846ff7edc8586fcc85c6ae251a29 source_ref=3be80bbceaf2380ed1dd92b08cafab72d7534c55 role=orchestration -->
Resolves member-call `Reference` edges for a source file by driving a language server over LSP via `LspClient`.

- `spec`: `LspServerSpec` supplying the server command, language ID, and call-site extractor.
- `resolve_file`: returns `[]` on any `LspError` or unexpected exception, never raises.
- `_clients`: one `LspClient` per resolved source-root path, lazily started and reused across files to amortise server warm-up cost.
- `close`: must be called to terminate all cached server processes.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:LspResolver.__init__ fingerprint=6497dbfabc7b5d240ffa239ac8550a339b0ccd43e99b55a5bec83230b9838fad body_fp=325fa98761567ea4dede78226c85702645d1db7ede0034e6c5152c3056a4cf8a source_ref=3be80bbceaf2380ed1dd92b08cafab72d7534c55 role=domain -->
Initialize `LspResolver` with the given `LspServerSpec`, setting up an empty per-root `LspClient` cache.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:LspResolver.name fingerprint=7c0cdbac5b2dbb5d3e2d04c41ce73fe13d43032593f87ca9bd7402e63c005888 body_fp=3030586c71ec3182e50ee23d01fa2c72505c00c3080de5031c2eb70c7a81d3c3 source_ref=3be80bbceaf2380ed1dd92b08cafab72d7534c55 role=model -->
`LspResolver.name` is the resolver's identity string, forwarded from its `LspServerSpec`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:LspResolver.resolve_file fingerprint=edbc274f25296c993f6993a8f7befc7edf8dab0c3b001d10a4023cddca1b9d4e body_fp=80d9baed144c2d3e0cbba2e1a65b4403100089f7d9c718ae962b6401f31c231f source_ref=3be80bbceaf2380ed1dd92b08cafab72d7534c55 role=domain -->
Run `LspResolver`'s full LSP-backed resolution for one file, returning `[]` on any failure.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:LspResolver._client_for fingerprint=e0f45553113d9012e3eede83685d73a536a45e6c2120ec095e136c49887d6ce7 body_fp=b7e7a5ad5b7b498196bb3ef55a1c248311fdc2aedd15f2f1ef3672dab151ad45 source_ref=3be80bbceaf2380ed1dd92b08cafab72d7534c55 role=domain -->
Return a cached `LspClient` for the given `source_root`, creating and starting one if none exists.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:LspResolver._resolve_file_inner fingerprint=2f4dcfc268a458c68e3d713c237e798dcdb5fd2e18abcd0c8841bc0b7669bc62 body_fp=513f89e9275ac162d17843364614fa8546cbc6a1b02da4466f6f687367e7cbe5 source_ref=3be80bbceaf2380ed1dd92b08cafab72d7534c55 role=domain -->
Core implementation of `LspResolver.resolve_file`; opens the file via LSP, queries `textDocument/definition` at each call site, and maps results to project-internal `Reference` edges.

- `symbols`: caller-supplied symbols for the file, used to map source lines to qnames.
- Returns one `Reference(kind="calls")` per unique `(src_qname, tgt_qname)` pair; skips self-references and off-project definitions.
- Deduplicates edges via a `seen` set; takes only the first valid definition location per call site.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:LspResolver.close fingerprint=428dd72cb6cb85746554055d4a7afd23d80c7883a82a9f49a4d1a1959d438818 body_fp=35c61def647c60e29acd6a05c662122868366b5322526603f9b1dd8edc458ade source_ref=3be80bbceaf2380ed1dd92b08cafab72d7534c55 role=io -->
Shuts down all cached `LspClient` processes and clears the `LspResolver` client registry.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:_symbols_by_line fingerprint=250f20d873fa6b98dd6551d18e4b532ec3e78c8ea3be0b5d98e6a25573744b16 body_fp=bdbb7cc04856b1c79664b6c2b3b2557b107c27a2fdeff3234956285ac0c26bf2 source_ref=3be80bbceaf2380ed1dd92b08cafab72d7534c55 role=util -->
Map a list of `Symbol` objects to a dict keyed by 1-based line number, resolving overlaps to the innermost (shortest) enclosing symbol.

- Filters to `kind` values `"function"`, `"method"`, or `"class"` only.
- Larger symbols are written first so smaller (inner) ones overwrite their lines.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:_target_qname fingerprint=0c2d5318e886e74b54b30a7fd54dd089db9338d4c1ab4ef7d24c8bb54951a134 body_fp=d247398fd72a9a11566334da59274e739b32e6ee9007d7302e84dcad5bcc3d24 source_ref=3be80bbceaf2380ed1dd92b08cafab72d7534c55 role=domain -->
Map an LSP definition location to the corresponding project symbol qname, or `None` if the definition falls outside the source root.

- `def_line`: 1-based line number as reported by LSP.
- `cache`: mutated in place; populated per resolved file path to avoid re-indexing.
- Returns `None` for off-project definitions (stdlib, `.venv`, `node_modules`).
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:_file_symbols_by_line fingerprint=e256374c6da429fc605bacf2eb0293dea64da00929c4789ac7bb5c202cfaf709 body_fp=42b619f9cf5d4a8967432a5bd105f8babe9ef4b7b5dbb702486960272c873966 source_ref=3be80bbceaf2380ed1dd92b08cafab72d7534c55 role=parsing -->
Index a file's symbols by 1-based start line, returning a `dict[int, str]` mapping line → `qualified_name`.

- Returns `{}` if `registry.extract_symbols` raises any exception.
- Keyed by `start_line` to avoid name-collision when mapping LSP definition locations.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:_uri_to_path fingerprint=964cc0b7330541035d0a849644c84634652e6a8219fd7bcea7f157e6df9ba96d body_fp=acb87a7fdd4c4cc68eee382fdeaad55973cea6cf7fb8437555db42e1645463d0 source_ref=3be80bbceaf2380ed1dd92b08cafab72d7534c55 role=util -->
Convert a `file:`-scheme URI string to a `Path`, returning `None` for non-file URIs.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:__all__ fingerprint=b2c3f5860e0c7a880648e3efa115ea9760f2de66477dc56f3934e05457fe84f0 body_fp=51305da177b38332ddf72377d688a0e7ca50d2a86e8541cf3e99b5ee5d852617 source_ref=3be80bbceaf2380ed1dd92b08cafab72d7534c55 role=config -->
Declares the public API surface of the `lsp_resolver` module.
<!-- trie:end -->