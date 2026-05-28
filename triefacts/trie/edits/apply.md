---
trie_version: 0.1.5
source: trie/edits/apply.py
file_fingerprint: 6872cb464280b74ac7932f505cb23d4221c2fda56e0817ab80bbf073679b1d24
last_synced_at: '2026-05-28T14:59:20Z'
defines:
- kind: module
  qualified_name: trie/edits/apply:__module__
  lines: 1-616
- kind: function
  qualified_name: trie/edits/apply:_parse_pyright_output
  lines: 27-43
- kind: function
  qualified_name: trie/edits/apply:_parse_ruff_output
  lines: 46-64
- kind: constant
  qualified_name: trie/edits/apply:_PARSERS
  lines: 67-70
- kind: function
  qualified_name: trie/edits/apply:_lsp_diagnostics
  lines: 73-98
- kind: function
  qualified_name: trie/edits/apply:_format_diagnostics
  lines: 101-109
- kind: function
  qualified_name: trie/edits/apply:_file_fixup
  lines: 112-135
- kind: function
  qualified_name: trie/edits/apply:_compile_check
  lines: 138-143
- kind: function
  qualified_name: trie/edits/apply:_expand_callers
  lines: 146-176
- kind: function
  qualified_name: trie/edits/apply:_refresh_file
  lines: 179-188
- kind: function
  qualified_name: trie/edits/apply:apply_patches
  lines: 191-537
- kind: function
  qualified_name: trie/edits/apply:_read_source_span
  lines: 540-543
- kind: function
  qualified_name: trie/edits/apply:_write_prose_section
  lines: 546-584
- kind: function
  qualified_name: trie/edits/apply:preview_patches
  lines: 587-615
incoming_refs: 24
outgoing_refs: 2
---
<!-- trie:section symbol=trie/edits/apply:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=37383da3df8b594ba94ac395f0d7a49b032afbce24b4b530fd84bbc07d3097cb source_ref=e8d8084e43a869c493b5fb62f4c6feec96cfec79 -->
## `trie/edits/apply`

Apply pending patches to source symbols with cascade expansion, LSP fixup, and git commit.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/apply:_parse_pyright_output fingerprint=3f78e0d19b87058172379c29ed45d41ac6a2dc8377978626de528aac643d4a90 body_fp=51597a972e683e7791ef013573e2e9a9fc9405dec7b85e5bcf0596c5f1c613c0 source_ref=9308cf9d98e9fd9b6e95c3a8c09e9d395de442f1 -->
## `_parse_pyright_output(stdout: str) -> list[dict]`

Parse pyright `--outputjson` stdout into normalized `{line, column, code, message}` diagnostic dicts.

- `code`: uses `rule` field, or `"pyright"` when `rule` is an empty string.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/apply:_parse_ruff_output fingerprint=73cb22cf0e4be716b9efcefa0839ad9656ee75a89e04bc1f63474b6f5d0ded39 body_fp=24920300b83bb47cd862fdb9fd3bf3962a4293c56c15ed7b8df6a74d707328a9 source_ref=9308cf9d98e9fd9b6e95c3a8c09e9d395de442f1 -->
## `_parse_ruff_output(stdout: str) -> list[dict]`

Parse ruff `--output-format json` stdout into normalised `{line, column, code, message}` dicts.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/apply:_PARSERS fingerprint=b2a5f90b8926406f02cb4d57b896878b47a5719443a5587d105fd7e953b0ffe3 body_fp=77cbdc9871cc15f59995f8d0c9f2e02e645df61543f3144339b16e79bc7390fa source_ref=e8d8084e43a869c493b5fb62f4c6feec96cfec79 -->
## `_PARSERS: dict[str, Callable[[str], list[dict]]]`

Map from LSP backend `output_format` name to its stdout parser function.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/apply:_lsp_diagnostics fingerprint=05ed364b4019b1dd4ee6b40ad27905b4e918ad82dad02288a52221ccf51d3133 body_fp=d8c6b07dc7b150cea044fe366f5ff238ab98f9b76bb644b95f76dd5bcbf2845c source_ref=9308cf9d98e9fd9b6e95c3a8c09e9d395de442f1 -->
## `_lsp_diagnostics(file_path: Path, backends: list[LspBackend]) -> list[dict]`

Run each `LspBackend` in order and return diagnostics from the first that produces results.

- Returns empty list if no backend is installed or all report clean.
- Each dict contains `line`, `column`, `code`, `message` keys.
- Skips backends whose `command` is not on `PATH` or whose `output_format` has no registered parser.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/apply:_format_diagnostics fingerprint=f8f1a2a1db2af1f7d97e5492cd064ae2f56b6574b386af817e0a4e13e5490c56 body_fp=94d698b1803a4c3e11eedff77b638cc760ba914c4dcca0f3920fecda7cd0a2f2 source_ref=9308cf9d98e9fd9b6e95c3a8c09e9d395de442f1 -->
## `_format_diagnostics(diags: list[dict]) -> str`

Format a list of LSP diagnostic dicts into a human-readable newline-joined string.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/apply:_file_fixup fingerprint=bbadd2dda12f9b9865bdf44285d919b279240223f85f1fca9335ac9413ccd9e7 body_fp=c4c49cab001718f9683030ffe784a7c244e3cd7e783ad32a679bae04134e0ae6 source_ref=4da703e107bded20b26978e188fb319c6d98b948 -->
## `_file_fixup(client: TrieClient, file_path: str, file_content: str, diagnostics: list[dict]) -> str | None`

Send file content and LSP diagnostics to the model and return fixed source code via a structured `FixupOutput` response.

- Returns `file_content` unchanged if `diagnostics` format to an empty string.
- Returns `fixup.content` directly from the structured output; no longer parses a fenced code block.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/apply:_compile_check fingerprint=7a854ad40befe46ef361c13e67a4678144ea8a66457bd5ceeb3562379b1703cf body_fp=af3832d6dfc421d01292785216cfc8635a87c71cc387605c90c16101621032ac source_ref=9308cf9d98e9fd9b6e95c3a8c09e9d395de442f1 -->
## `_compile_check(source: str) -> bool`

Return `True` if `source` compiles as valid Python, `False` on `SyntaxError`.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/apply:_expand_callers fingerprint=3b8ad849b2ca5152c41cf726107bdb2e7194d9434696c747cf3a92eb2c4dabd8 body_fp=c3e338b0c6a7f6c8a5eccdf8d6de48e340184c9a986c0c6b1e25e3d8ac6840cb source_ref=9308cf9d98e9fd9b6e95c3a8c09e9d395de442f1 -->
## `_expand_callers(seed_qnames: list[str], store: Store, cascade_depth: int, hub_threshold: int) -> set[str]`

BFS from seed symbols through caller edges up to `cascade_depth` hops, returning reachable callers.

- `seed_qnames`: starting symbols; excluded from the returned set.
- `hub_threshold`: symbols with more inbound edges than this are not traversed.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/apply:_refresh_file fingerprint=cb12cf48ef733d72f2273ca2661a206c03fd153e474426a121e05919824950cf body_fp=b8ee2a31868abdeecfeca704ae8aa48dd577b452486188e7e0bf8ed4caaad21c source_ref=9308cf9d98e9fd9b6e95c3a8c09e9d395de442f1 -->
## `_refresh_file(file_path: str, project_root: Path, config: Config, store: Store) -> None`

Refresh triefact metadata for a single source file after it has been patched.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/apply:apply_patches fingerprint=34152c4a10101626598cdf65b430179eaebdc1213a49e9710db538fcb37aee10 body_fp=6f49d8eb6d762873a6de4931de194f1fb31f841a5f04ca2cc95e090d53f1007e source_ref=cc1f6acfd303f2f5f4ce93250a206220e69621c9 -->
## `apply_patches(store: Store, config: Config, client: TrieClient, project_root: Path, progress: Any | None = None) -> dict[str, Any]`

Expand pending patches via caller-cascade, regenerate affected source files, run LSP fixup loops, refresh triefact metadata, and verify project consistency.

- `progress`: optional reporter; must implement `stage`, `file_start`, `file_symbol`, `file_generate`, `file_fixup`, `file_prose`, `file_done`, `refresh`, `verify`.
- `store`: source of pending patches; cleared for all affected qnames on success.
- Returns `ok=False` immediately on syntax error, LSP fixup failure, refresh error, or verify failure.
- `files`: one dict per processed file with keys `path`, `ok`, `symbols`, `notes`, `lsp_iterations`, `prose_written`, `error`.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/apply:_read_source_span fingerprint=43f69c6b8bf7cdf184ce904aba0f8a6e02e68bdef37b33c43b59ff4df640eb73 body_fp=b98adcd92f77c498e6be8600c2389e1d755ac9f23d54f8b8c0ac20a0bad44e17 source_ref=9308cf9d98e9fd9b6e95c3a8c09e9d395de442f1 -->
## `_read_source_span(detail: Any, src_root: Path) -> str`

Read the source lines of a symbol span from disk using its start/end line metadata.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/apply:_write_prose_section fingerprint=8af674914055253618af885b0cd4c3668e2e7e6ddb737d486007b02b58a61a00 body_fp=f050c428053d51aec1f0e7ae936c3e0c9bf513ef720f74a17917b52d5218d27c source_ref=cc1f6acfd303f2f5f4ce93250a206220e69621c9 -->
## `_write_prose_section(qname: str, file_path: str, prose: str, triefacts_root: Path, src_root: Path | None = None) -> None`

Upsert a symbol's prose into its corresponding triefact Markdown file, then write the result to disk.

- `src_root`: when provided, computes the symbol's `body_normalized_hash` fingerprint from the updated source file before upserting.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/apply:preview_patches fingerprint=40df1bfff989b701a17843747fb88bcd6b9a12a390a9f1fbf23fc30b1d899b30 body_fp=bb864cf19096334c749ac097c0af09be6db4b22e942f111ea50293f4f325b6e9 source_ref=9308cf9d98e9fd9b6e95c3a8c09e9d395de442f1 -->
## `preview_patches(store: Store, config: Config) -> dict[str, Any]`

Summarise pending patches and their cascade impact without applying any changes.

- Returns `total_patches`, `patched_symbols`, `patched_list`, `cascade_symbols`, `cascade_list`.
- `cascade_list`: callers reachable within `config.cascade.default_depth` that are not direct patch targets.
<!-- trie:end -->