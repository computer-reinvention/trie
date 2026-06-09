---
trie_version: 0.1.5
source: trie/sync/incremental.py
file_fingerprint: f914dd3128be6edd574df711ed0327434590effec8e982f8514944e9b91610fb
last_synced_at: '2026-06-09T09:38:59Z'
defines:
- kind: module
  qualified_name: trie/sync/incremental:__module__
  lines: 1-323
- kind: class
  qualified_name: trie/sync/incremental:IncrementalWorklist
  lines: 21-53
- kind: class
  qualified_name: trie/sync/incremental:IncrementalResult
  lines: 57-65
- kind: function
  qualified_name: trie/sync/incremental:compute_incremental_worklist
  lines: 68-144
- kind: function
  qualified_name: trie/sync/incremental:run_incremental
  lines: 147-322
incoming_refs: 20
outgoing_refs: 15
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
<!-- trie:section symbol=trie/sync/incremental:IncrementalResult fingerprint=44d8d13db810a81ea27f75709b870895913876f1c8dbdc95aa93ed09cc9916cf body_fp=edb4713c88462a2e374290fbcc09b8507eda2eedc9d8e85e33ebf923954dbb17 source_ref=549bb001d03e465de4697570041eabaf93893a7f role=documentation-sync -->
Results and statistics from running incremental sync on a project.

- `files_synced`: number of files successfully processed by the LLM
- `files_skipped_no_budget`: files skipped due to budget or limit constraints
- `files_skipped_no_symbols`: files skipped because they contain no documentable symbols
- `directly_stale_count`: number of files that were directly stale (not cascade-pulled)
- `cascaded_count`: number of files pulled in through the cascade mechanism
- `actual_cost_usd`: total cost in USD for all LLM calls made during sync
- `orphan_triefacts_removed`: list of orphaned triefact files that were deleted
- `sync_results`: detailed results for each file that was successfully synced
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/incremental:compute_incremental_worklist fingerprint=3c8386c7f8572fc00dc5dc15bce15bda702346e82a53d1bfc3344998aa6c6c47 body_fp=5cb5abe44f02f42ee162b426ac76cca776498797b85b6de3d864d7e4d10966c3 source_ref=549bb001d03e465de4697570041eabaf93893a7f role=change-detection -->
Scans project, identifies stale triefacts, computes cascade dependencies, and returns worklist without executing sync.

- Filters out staleness items for deleted source files (treats as orphan triefacts)
- `regen_qnames_by_file` maps files to specific symbols needing regeneration (excludes full-file regen cases)
- Returns empty worklist if no directly stale files found
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/incremental:run_incremental fingerprint=af32bcc03bf89bb4a9221730842af39354b54dbc3e5a2a97470655620280de19 body_fp=2d9ea6df2086b8fed7ab140df2fcaeb4e76c00559d2d352491dc58b7fe822527 source_ref=319d5dde2dc074582af1ce4ea40dc1d43db5fc03 role=orchestration -->
Regenerates stale triefacts and cascade-dependent files using LLM, respecting budget and concurrency limits.

• Scans project, checks staleness, computes cascade, then syncs affected files in hop-ordered waves
• Removes orphaned triefacts, backfills missing metadata, auto-fills role tags with error handling, clears pending status
• Returns statistics including files synced, skipped counts, actual cost, and detailed sync results
<!-- trie:end -->