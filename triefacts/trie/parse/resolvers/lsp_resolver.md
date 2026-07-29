---
trie_version: 0.1.9
source: trie/parse/resolvers/lsp_resolver.py
file_fingerprint: d01a8b4b73a6391eb593526cdd8778798617bda7629311b2ce3ffdee0089a5f8
last_synced_at: '2026-07-29T00:05:33Z'
description: Generic, language-agnostic `ReferenceResolver` backed by an LSP server.
defines:
- kind: module
  qualified_name: trie/parse/resolvers/lsp_resolver:__module__
  lines: 1-218
- kind: constant
  qualified_name: trie/parse/resolvers/lsp_resolver:CallSite
  lines: 38-38
- kind: constant
  qualified_name: trie/parse/resolvers/lsp_resolver:CallSiteExtractor
  lines: 42-42
- kind: class
  qualified_name: trie/parse/resolvers/lsp_resolver:LspServerSpec
  lines: 46-65
- kind: method
  qualified_name: trie/parse/resolvers/lsp_resolver:LspServerSpec.is_available
  lines: 63-65
- kind: class
  qualified_name: trie/parse/resolvers/lsp_resolver:LspResolver
  lines: 68-155
- kind: method
  qualified_name: trie/parse/resolvers/lsp_resolver:LspResolver.__init__
  lines: 71-76
- kind: method
  qualified_name: trie/parse/resolvers/lsp_resolver:LspResolver.name
  lines: 79-80
- kind: method
  qualified_name: trie/parse/resolvers/lsp_resolver:LspResolver.resolve_file
  lines: 82-93
- kind: method
  qualified_name: trie/parse/resolvers/lsp_resolver:LspResolver._client_for
  lines: 95-102
- kind: method
  qualified_name: trie/parse/resolvers/lsp_resolver:LspResolver._resolve_file_inner
  lines: 104-149
- kind: method
  qualified_name: trie/parse/resolvers/lsp_resolver:LspResolver.close
  lines: 151-155
- kind: function
  qualified_name: trie/parse/resolvers/lsp_resolver:_symbols_by_line
  lines: 158-169
- kind: function
  qualified_name: trie/parse/resolvers/lsp_resolver:_target_qname
  lines: 172-191
- kind: function
  qualified_name: trie/parse/resolvers/lsp_resolver:_file_symbols_by_line
  lines: 194-207
- kind: function
  qualified_name: trie/parse/resolvers/lsp_resolver:_uri_to_path
  lines: 210-214
- kind: constant
  qualified_name: trie/parse/resolvers/lsp_resolver:__all__
  lines: 217-217
incoming_refs: 9
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
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:LspServerSpec fingerprint=500999689d7f5cb3899768233995dd4c55e8066a0dfc0456c6f760d69771871b body_fp=a6b200196aeac5a10d2345c43ab12dc0f13425df5c9a040cda1579d31d20d5c8 source_ref=192b085a4de586615b738fdd3c7ec0a90135239b role=model -->
Frozen dataclass bundling all language-specific configuration needed to drive one LSP server for member-call resolution.

- `name`: resolver identity string used for telemetry (e.g. `"pyright"`)
- `command`: argv list to spawn the server in stdio mode
- `language_id`: LSP `languageId` string (e.g. `"python"`, `"typescript"`)
- `call_sites`: language-specific extractor yielding member-call sites from raw file bytes
- `init_timeout`: seconds to wait for the LSP initialize handshake; defaults to `15.0`
- `warmup`: seconds to sleep after `didOpen` before querying; defaults to `0.0`
- `is_available()`: returns `True` if `command[0]` is found on `PATH`
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:LspServerSpec.is_available fingerprint=3da08adb8d99c293c0f1d2119418318521e43df83854896945caf451102eab10 body_fp=f2adfa5ac4ceb4abd96adf70ba8247d579e5f78a103b2682ead8a06f451d98d9 source_ref=3be80bbceaf2380ed1dd92b08cafab72d7534c55 role=util -->
Returns `True` if `LspServerSpec.command` is non-empty and its first element resolves via `shutil.which`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:LspResolver fingerprint=52ffdf3e75c97d61d6da4fe31a781708256a54297771fcb64f2e188a8fc8780a body_fp=7cfa1c0c2d65f7df6b4cf1dd397267ce2e034a40f3f2b1550148e3335ec8abcb source_ref=192b085a4de586615b738fdd3c7ec0a90135239b role=domain -->
Resolves member-call `Reference` edges for a source file by driving a language server over LSP via `LspClient`.

- `spec`: `LspServerSpec` supplying the server command, language ID, call-site extractor, init timeout, and optional warmup delay.
- `resolve_file`: returns `[]` on any `LspError` or unexpected exception, never raises.
- `_clients`: one `LspClient` per resolved source-root path, lazily started and reused across files to amortise server warm-up cost; client is constructed with `spec.init_timeout`.
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
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:LspResolver._client_for fingerprint=b576ad5ea10cb9380737c159f0d81cf5d169771aaf78078ddf65431ccc3e70aa body_fp=0af15d48252edac1c26f7b31d8830125467d32d29263ca6eef00a8d26fa04400 source_ref=192b085a4de586615b738fdd3c7ec0a90135239b role=orchestration -->
Return a cached `LspClient` for the given `source_root`, creating and starting one with `spec.init_timeout` if none exists.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/lsp_resolver:LspResolver._resolve_file_inner fingerprint=a762af9710673b82f510feacc88e9a17f55c2dba9085dfd1f2057e336608d374 body_fp=4364ca6d7ea697b3c219f16a0edf32c51a73eb8c88f7a8876650981561729ea0 source_ref=192b085a4de586615b738fdd3c7ec0a90135239b role=domain -->
Core implementation of `LspResolver.resolve_file`; opens the file via LSP, optionally sleeps for `spec.warmup` seconds, queries `textDocument/definition` at each call site, and maps results to project-internal `Reference` edges.

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