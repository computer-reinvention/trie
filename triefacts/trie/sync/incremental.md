---
trie_version: 0.3.0
source: trie/sync/incremental.py
file_fingerprint: faa44cce2a02bc752acd7d28372ada257a7e7a8f6459e7aadbddf14f105aedae
last_synced_at: '2026-08-02T21:19:50Z'
defines:
- kind: module
  qualified_name: trie/sync/incremental:__module__
  lines: 1-333
- kind: class
  qualified_name: trie/sync/incremental:IncrementalWorklist
  lines: 21-53
  signature: class IncrementalWorklist
- kind: class
  qualified_name: trie/sync/incremental:IncrementalResult
  lines: 57-68
  signature: class IncrementalResult
- kind: function
  qualified_name: trie/sync/incremental:compute_incremental_worklist
  lines: 71-147
  signature: 'def compute_incremental_worklist( *, project_root: Path, config: Config, store: Store ) -> IncrementalWorklist'
- kind: function
  qualified_name: trie/sync/incremental:run_incremental
  lines: 150-332
  signature: 'def run_incremental( *, project_root: Path, config: Config, store: Store, client: TrieClient, pricing: ModelPricing | None = None, budget_usd: float | None = None, limit: int | None = None, progress: ProgressCallback | None = None, ) -> IncrementalResult'
incoming_refs: 18
outgoing_refs: 19
---
<!-- trie:section symbol=trie/sync/incremental:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=cb313a4fac70ff6dc3bad02de5c44f9c60afef2c3f9792c5becb424681fa0201 source_ref=549bb001d03e465de4697570041eabaf93893a7f role=documentation-sync -->
Incremental synchronization engine that refreshes stale triefacts and cascades changes through dependent files.

- Orchestrates scan → check → cascade → sync pipeline for affected files
- Supports symbol-level regeneration to minimize LLM costs on partial changes
- Handles budget constraints and provides progress callbacks for long operations
- Removes orphaned triefacts and maintains section record consistency
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/incremental:IncrementalWorklist fingerprint=cdb0112edfc993b6d288ef8defa85093653d6f39080b9837798d5a3fddcb71a5 body_fp=d60b9893075467350d859d4da2211565e3d334babc2e142bd3261c018a186600 source_ref=549bb001d03e465de4697570041eabaf93893a7f role=change-detection -->
## `class IncrementalWorklist`

Read-only preview of files and symbols that `run_incremental` would regenerate.

- `hop_by_file`: cascade hop distance from seed files, used to order sync priority
- `regen_qnames_by_file`: qualified names needing regeneration per file; absence means full-file regen
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/incremental:IncrementalResult fingerprint=b6f45c9f8cd5ef42a5e6ec0b0e02659ef4795874c11a42992e111e3112f3b849 body_fp=6b63b0e78694fd2cd05a4be4a7d183570cbf4bbd32066189cd8bcdde9f175c36 source_ref=b2c1029e3d5ee3383f0a2886a9fba9ab6dbc4657 role=model -->
## `class IncrementalResult`

Results and statistics from running incremental sync on a project.

- `files_synced`: number of files successfully processed by the LLM
- `files_skipped_no_budget`: files skipped due to budget or limit constraints
- `files_skipped_no_symbols`: files skipped because they contain no documentable symbols
- `directly_stale_count`: number of files that were directly stale (not cascade-pulled)
- `cascaded_count`: number of files pulled in through the cascade mechanism
- `actual_cost_usd`: total cost in USD for all LLM calls made during sync
- `orphan_triefacts_removed`: list of orphaned triefact files that were deleted
- `sync_results`: detailed results for each file that was successfully synced
- `file_errors`: `(rel_path, error)` pairs for files whose generation raised an exception
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/incremental:compute_incremental_worklist fingerprint=c83d60644bece6bde13a27329d9e7626e65e3f41e4b8032ca0531310721b37ca body_fp=52062cd41592d65abb2298f7be47cc5cf03d0df9aa92d0a82ca28648730c1b71 source_ref=b2c1029e3d5ee3383f0a2886a9fba9ab6dbc4657 role=orchestration -->
## `def compute_incremental_worklist( *, project_root: Path, config: Config, store: Store ) -> IncrementalWorklist`

Scans project, identifies stale triefacts, computes cascade dependencies, and returns worklist without executing sync.

- Filters out staleness items for deleted source files (treats as orphan triefacts)
- `regen_qnames_by_file` maps files to specific symbols needing regeneration (excludes full-file regen cases)
- Returns empty worklist if no directly stale files found
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/incremental:run_incremental fingerprint=7d09cf154875261c5e2036f73a5b4f5b26cfdd77a9092e5ccbc6bd2b86637318 body_fp=4c4d13bf5f7e69cf50cce143cf73557f300917435345d8aed5abd9e02091720e source_ref=b2c1029e3d5ee3383f0a2886a9fba9ab6dbc4657 role=orchestration -->
## `def run_incremental( *, project_root: Path, config: Config, store: Store, client: TrieClient, pricing: ModelPricing | None = None, budget_usd: float | None = None, limit: int | None = None, progress: ProgressCallback | None = None, ) -> IncrementalResult`

Regenerates stale triefacts and cascade-dependent files using LLM, respecting budget and concurrency limits.

• Scans project, checks staleness, computes cascade, then syncs affected files in hop-ordered waves
• Emits plan summary before processing files, removes orphaned triefacts, backfills missing metadata, auto-fills role tags with error handling, clears pending status
• Returns statistics including files synced, skipped counts, actual cost, detailed sync results, and per-file errors
<!-- trie:end -->