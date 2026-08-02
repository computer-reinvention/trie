---
trie_version: 0.3.0
source: trie/sync/single_file.py
file_fingerprint: a65680d41fc1670c7ceb695bd718e46f50253ab274fdcd7e4b939f2cc824acaa
last_synced_at: '2026-08-02T21:19:13Z'
defines:
- kind: module
  qualified_name: trie/sync/single_file:__module__
  lines: 1-694
- kind: function
  qualified_name: trie/sync/single_file:backfill_section_records
  lines: 31-64
  signature: 'def backfill_section_records( project_root: Path, config: Config, store: Store, ) -> None'
- kind: class
  qualified_name: trie/sync/single_file:FileSyncResult
  lines: 68-79
  signature: class FileSyncResult
- kind: class
  qualified_name: trie/sync/single_file:MetadataRefreshResult
  lines: 83-91
  signature: class MetadataRefreshResult
- kind: class
  qualified_name: trie/sync/single_file:_SymbolJob
  lines: 95-105
  signature: class _SymbolJob
- kind: function
  qualified_name: trie/sync/single_file:_file_fingerprint
  lines: 108-109
  signature: 'def _file_fingerprint(text: str) -> str'
- kind: function
  qualified_name: trie/sync/single_file:_triefact_path_for
  lines: 112-116
  signature: 'def _triefact_path_for(source_path: Path, project_root: Path, config: Config) -> Path'
- kind: function
  qualified_name: trie/sync/single_file:_file_description
  lines: 119-139
  signature: 'def _file_description(source_path: Path) -> str | None'
- kind: function
  qualified_name: trie/sync/single_file:_symbol_signature
  lines: 142-154
  signature: 'def _symbol_signature(symbol: Symbol) -> str | None'
- kind: function
  qualified_name: trie/sync/single_file:_build_defines
  lines: 157-176
  signature: 'def _build_defines(symbols: list[Symbol]) -> list[dict[str, object]]'
- kind: function
  qualified_name: trie/sync/single_file:_resolve_previous_symbols
  lines: 179-224
  signature: 'def _resolve_previous_symbols( *, source_path: Path, src_root: Path, project_root: Path, existing_section_refs: dict[str, str], ) -> dict[str, Symbol]'
- kind: function
  qualified_name: trie/sync/single_file:refresh_triefact_metadata
  lines: 227-361
  signature: 'def refresh_triefact_metadata( source_path: Path, *, project_root: Path, config: Config, store: Store | None = None, ) -> MetadataRefreshResult'
- kind: function
  qualified_name: trie/sync/single_file:sync_single_file
  lines: 364-693
  signature: 'def sync_single_file( source_path: Path, *, project_root: Path, config: Config, client: TrieClient, dest_triefact_path: Path | None = None, store: Store | None = None, symbols_to_regen: set[str] | None = None, force: bool = False, ) -> FileSyncResult'
incoming_refs: 77
outgoing_refs: 44
---
<!-- trie:section symbol=trie/sync/single_file:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=962cb42fd231e6a72fa197d03a93bef26647d2e4f96f38d6e53a0c5332b417c1 source_ref=da91ee7ba7df534c772bf0cfb02b2cfcdb8bce67 role=documentation-sync -->
Synchronizes individual Python source files to their corresponding triefact documentation files.

- `backfill_section_records` — populates database records from existing triefact files on disk
- `sync_single_file` — generates or refreshes a complete triefact file for one source file
- `refresh_triefact_metadata` — updates front matter without regenerating section bodies
- `FileSyncResult` — captures statistics from a single file sync operation
- `MetadataRefreshResult` — reports whether metadata refresh changed file contents
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/single_file:backfill_section_records fingerprint=e04d7a4617b4fa4fcb3c831d0695318aebbacf834a1086848de9df18a116487d body_fp=36966c62faef5dedbac5d8552d5546324e2d25cdc08de8adc768639d13f49a9a source_ref=fafd0f25e185cf2f2b0b6d0272a456fb02ab100a role=persistence -->
## `def backfill_section_records( project_root: Path, config: Config, store: Store, ) -> None`

Populate `triefact_sections` records from existing triefact files for every section discovered on disk.

- Reads all triefact files in the project and ensures database records exist
- Skips source files not recognized as indexable by the parser registry
- Idempotent operation safe for repeated execution
- Preserves role tags from persisted sentinels to avoid re-running the LLM
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/single_file:FileSyncResult fingerprint=f658b6cb6f956faf262f29751e15b6efaad12e661c2976d58946940db38a0ed7 body_fp=3bb28201ef2a3d6bcbe83bbe6f999701d133f69ae6a084b52b6b559094cf77ab source_ref=da91ee7ba7df534c772bf0cfb02b2cfcdb8bce67 role=documentation-sync -->
## `class FileSyncResult`

Records the outcome of syncing a single source file to its triefact.

- `symbols_skipped`: Symbols whose existing sections were left untouched because they were not in `symbols_to_regen`
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/single_file:MetadataRefreshResult fingerprint=0049c0670ad0f133fe15a0c3be095e1eeb57d78e4751912b0e33094080c9e04e body_fp=c6eda755de5e571d2ed17d2f06cf2a3843b0c9afeed1e9a54e0ac8358fce5430 source_ref=da91ee7ba7df534c772bf0cfb02b2cfcdb8bce67 role=documentation-sync -->
## `class MetadataRefreshResult`

Represents the outcome of refreshing triefact metadata for a single file.

- `changed`: True when the rewritten triefact bytes differ from the previous bytes
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/single_file:_SymbolJob fingerprint=0f7b75b7a065300e3f0be7a0e01b8244c10ca3f48b6706b7dbfea7ecaacef021 body_fp=a1f38b4acc11934efed9e247c92b02cc66671b310d5000fd34370941c543ae4b source_ref=da91ee7ba7df534c772bf0cfb02b2cfcdb8bce67 role=documentation-sync -->
## `class _SymbolJob`

Carries Symbol and optional previous content to thread pool workers for parallel section generation.

- `previous_source`: Previous symbol signature+body text for diff-aware generation, None for cold-write
- `previous_prose`: Previous section body text for diff-aware generation, None for cold-write
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/single_file:_file_fingerprint fingerprint=46c7c51a18ded3953f42cbf0478b0794532566079fd73b079dc9950d2c108e07 body_fp=e591f3e03c6feda39c2bbae1c7db0e69967af32f37d639ca46348296e46e1128 source_ref=da91ee7ba7df534c772bf0cfb02b2cfcdb8bce67 role=documentation-sync -->
## `def _file_fingerprint(text: str) -> str`

Computes a SHA256 hash of the input text as a hexadecimal string.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/single_file:_triefact_path_for fingerprint=1c2e2cf4fa444cf778b7950d1adb2c52f77952ba318f32650aa629fbcb6ee9a5 body_fp=06573aa6cfd30157ee904fa6ca7f446100204e51d055ca9d4dc11ebbd1d75552 source_ref=da91ee7ba7df534c772bf0cfb02b2cfcdb8bce67 role=documentation-sync -->
## `def _triefact_path_for(source_path: Path, project_root: Path, config: Config) -> Path`

Computes the triefact file path for a given source file by mapping its relative position under the source root to the triefacts root with a .md extension.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/single_file:_file_description fingerprint=bc5c4ab179593304d4c7bfa09b1ce03affab3167c1f68d40a19bf0dce86bb1c7 body_fp=bc9135e5d8bb06e6b2ecb1971c9aa8bd19467325aa71445539ae2244396aa4ca source_ref=e0ec1aff11d8b03d0bd7c2ee3e874a2551f88c6f role=util -->
## `def _file_description(source_path: Path) -> str | None`

Extracts the first non-empty line from a source file's module docstring as a description.

- Returns `None` for non-Python files or files with no module docstring
- Strips string literal syntax and whitespace from the raw docstring content
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/single_file:_symbol_signature fingerprint=67bbad5d3c3162c80c6acea422010a6ee31abbd3f7f9c0e6e60f373b242e18d2 body_fp=dd7bb713956a295fd86e7a3223270229d0ab8cd601371f692e1cb11183bbb778 source_ref=d83a1e6a3144da19df3ee405ba84f79752885725 role=util -->
## `def _symbol_signature(symbol: Symbol) -> str | None`

Return the squeezed single-line signature for a symbol, or `None` for signatureless kinds.

- Returns `None` for `module` and `constant` kinds (`SIGNATURELESS_KINDS`) so callers omit the field rather than emit a synthetic value.
- Returns `None` when `squeeze_signature` produces an empty string.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/single_file:_build_defines fingerprint=9e3059116f6aac5cb383685fb714c5b89235dae44fd41055d8f44b1925490d51 body_fp=53c8c158ddb30fad8afbbe825d23576533e0d1e603ec6031878a376a88132766 source_ref=d83a1e6a3144da19df3ee405ba84f79752885725 role=util -->
## `def _build_defines(symbols: list[Symbol]) -> list[dict[str, object]]`

Builds a list of dictionaries containing symbol metadata for triefact front matter.

- Returns entries with `kind`, `qualified_name`, `lines`, and optionally `signature` fields for each symbol
- `signature` is the parser-captured declaration squeezed to one line; key is omitted entirely for signatureless kinds (`module`, `constant`)
- Sorted by start line to match source file order
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/single_file:_resolve_previous_symbols fingerprint=8fc33ac4cad57a5d5e9a3db964b2bf5766b470e96a0556c471e7c51c9e16544f body_fp=5eda8efb6d8d2b9d74dcbfac5b626400258149ded79fb9d45e55ef02745e0237 source_ref=e0ec1aff11d8b03d0bd7c2ee3e874a2551f88c6f role=util -->
## `def _resolve_previous_symbols( *, source_path: Path, src_root: Path, project_root: Path, existing_section_refs: dict[str, str], ) -> dict[str, Symbol]`

Retrieve previous Symbol instances for qualified names that have git blob references by fetching and parsing historical file content.

- Groups lookups by blob hash to minimize git calls and parsing overhead
- Returns empty dict when no section references exist
- Skips symbols that can't be resolved due to unreachable blobs or parse errors
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/single_file:refresh_triefact_metadata fingerprint=2df3adb0d6464a166fa54b1a44f4d9dbf8b2847fe3e47f846553eaabd6049cd8 body_fp=4dba7050e920423aaa7025c62c145fda1b9a73b3eb7ddf43c21c5adcfecba7f2 source_ref=d83a1e6a3144da19df3ee405ba84f79752885725 role=orchestration -->
## `def refresh_triefact_metadata( source_path: Path, *, project_root: Path, config: Config, store: Store | None = None, ) -> MetadataRefreshResult`

Refreshes a triefact file's front matter from the current store without calling the LLM.

- `store` — when None, skips reference counts in front matter; other metadata still updates
- Returns `MetadataRefreshResult` with `changed=True` if rewritten bytes differ from disk
- Normalizes each section body to begin with the parser-derived `## \`signature\`` heading via `ensure_signature_heading`; prose after the heading is preserved verbatim
- Preserves existing `last_synced_at` timestamp; section fingerprints are not recomputed
- No-op returning `changed=False` when the triefact file doesn't exist
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/single_file:sync_single_file fingerprint=b4ad886392c8824a1f1f1b870ac44b11c507f06f4b7b478044d0f3058e3f80e2 body_fp=a5b1152e60d840ef26392ec678cf8b0f0c3a6d8f402a2ce35fb86f1e408f7130 source_ref=d83a1e6a3144da19df3ee405ba84f79752885725 role=orchestration -->
## `def sync_single_file( source_path: Path, *, project_root: Path, config: Config, client: TrieClient, dest_triefact_path: Path | None = None, store: Store | None = None, symbols_to_regen: set[str] | None = None, force: bool = False, ) -> FileSyncResult`

Generate or refresh the triefact file for a single Python source file using LLM calls.

- `symbols_to_regen`: when None, regenerates all symbols; when a set, only regenerates listed symbols
- `dest_triefact_path`: when provided, writes to this path instead of canonical location
- `force`: bypasses diff-aware regeneration and forces cold generation for all symbols
- Uses thread pool for parallel LLM calls bounded by `config.sync.concurrency`
- Preserves existing hand-written prose between section sentinels
- Removes sections for symbols no longer present in source
- Implements three-phase execution: plan (partition symbols), generate (parallel LLM calls), apply (serial mutations)
- In the apply phase, enforces parser-derived `## \`signature\`` heading on every section body before upsert; signatureless kinds are left verbatim
- In the apply phase, carries the previous role forward when regenerated prose is byte-identical to the previous section, preventing non-deterministic role churn
<!-- trie:end -->