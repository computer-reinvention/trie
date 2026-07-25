---
trie_version: 0.1.9
source: trie/sync/incremental.py
file_fingerprint: 0860775e4be3fc93396ad749924bcbc2aba687c04865c4c7f14d2723eb4e152f
last_synced_at: '2026-07-25T01:56:36Z'
defines:
- kind: module
  qualified_name: trie/sync/incremental:__module__
  lines: 1-333
- kind: class
  qualified_name: trie/sync/incremental:IncrementalWorklist
  lines: 21-53
- kind: class
  qualified_name: trie/sync/incremental:IncrementalResult
  lines: 57-68
- kind: function
  qualified_name: trie/sync/incremental:compute_incremental_worklist
  lines: 71-147
- kind: function
  qualified_name: trie/sync/incremental:run_incremental
  lines: 150-332
incoming_refs: 20
outgoing_refs: 16
---
<!-- trie:section symbol=trie/sync/incremental:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=cb313a4fac70ff6dc3bad02de5c44f9c60afef2c3f9792c5becb424681fa0201 source_ref=549bb001d03e465de4697570041eabaf93893a7f role=documentation-sync -->
Incremental synchronization engine that refreshes stale triefacts and cascades changes through dependent files.

- Orchestrates scan → check → cascade → sync pipeline for affected files
- Supports symbol-level regeneration to minimize LLM costs on partial changes
- Handles budget constraints and provides progress callbacks for long operations
- Removes orphaned triefacts and maintains section record consistency
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/incremental:IncrementalWorklist fingerprint=cdb0112edfc993b6d288ef8defa85093653d6f39080b9837798d5a3fddcb71a5 body_fp=8f57aeef79b3037acf3178526bbeef2f13d79f8c4b19fa325b0fbdc9a606bfd9 source_ref=549bb001d03e465de4697570041eabaf93893a7f role=change-detection -->
Read-only preview of files and symbols that `run_incremental` would regenerate.

- `hop_by_file`: cascade hop distance from seed files, used to order sync priority
- `regen_qnames_by_file`: qualified names needing regeneration per file; absence means full-file regen
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/incremental:IncrementalResult fingerprint=b6f45c9f8cd5ef42a5e6ec0b0e02659ef4795874c11a42992e111e3112f3b849 body_fp=b1f8043302d769235fd8f9620dfb6c682199eb6f0dba6ffa1da41f620614a8be source_ref=b876570c7fb9908cea4c491d3d247b48a4ae0339 role=model -->
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
<!-- trie:section symbol=trie/sync/incremental:compute_incremental_worklist fingerprint=3c8386c7f8572fc00dc5dc15bce15bda702346e82a53d1bfc3344998aa6c6c47 body_fp=5cb5abe44f02f42ee162b426ac76cca776498797b85b6de3d864d7e4d10966c3 source_ref=0007e08c6d700f4d99f851ebc327be2322a06af4 role=orchestration -->
Scans project, identifies stale triefacts, computes cascade dependencies, and returns worklist without executing sync.

- Filters out staleness items for deleted source files (treats as orphan triefacts)
- `regen_qnames_by_file` maps files to specific symbols needing regeneration (excludes full-file regen cases)
- Returns empty worklist if no directly stale files found
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/incremental:run_incremental fingerprint=7d09cf154875261c5e2036f73a5b4f5b26cfdd77a9092e5ccbc6bd2b86637318 body_fp=53769b6bd274bc4f2b54b0322cbce04f99e7be9c064fcd980be1314313a826cb source_ref=b876570c7fb9908cea4c491d3d247b48a4ae0339 role=orchestration -->
Regenerates stale triefacts and cascade-dependent files using LLM, respecting budget and concurrency limits.

• Scans project, checks staleness, computes cascade, then syncs affected files in hop-ordered waves
• Emits plan summary before processing files, removes orphaned triefacts, backfills missing metadata, auto-fills role tags with error handling, clears pending status
• Returns statistics including files synced, skipped counts, actual cost, detailed sync results, and per-file errors
<!-- trie:end -->