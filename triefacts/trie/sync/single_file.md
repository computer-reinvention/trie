---
trie_version: 0.1.5
source: trie/sync/single_file.py
file_fingerprint: 5b0ac8d20f15d69cceb609de803aa7e24f1fb1b6e1dcc1c43970d8d1d8bf0533
last_synced_at: '2026-06-03T21:16:39Z'
defines:
- kind: module
  qualified_name: trie/sync/single_file:__module__
  lines: 1-589
- kind: function
  qualified_name: trie/sync/single_file:backfill_section_records
  lines: 25-53
- kind: class
  qualified_name: trie/sync/single_file:FileSyncResult
  lines: 57-68
- kind: class
  qualified_name: trie/sync/single_file:MetadataRefreshResult
  lines: 72-80
- kind: class
  qualified_name: trie/sync/single_file:_SymbolJob
  lines: 84-94
- kind: function
  qualified_name: trie/sync/single_file:_file_fingerprint
  lines: 97-98
- kind: function
  qualified_name: trie/sync/single_file:_triefact_path_for
  lines: 101-105
- kind: function
  qualified_name: trie/sync/single_file:_file_description
  lines: 108-123
- kind: function
  qualified_name: trie/sync/single_file:_build_defines
  lines: 126-139
- kind: function
  qualified_name: trie/sync/single_file:_resolve_previous_symbols
  lines: 142-187
- kind: function
  qualified_name: trie/sync/single_file:refresh_triefact_metadata
  lines: 190-284
- kind: function
  qualified_name: trie/sync/single_file:sync_single_file
  lines: 287-588
incoming_refs: 56
outgoing_refs: 22
---
<!-- trie:section symbol=trie/sync/single_file:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=962cb42fd231e6a72fa197d03a93bef26647d2e4f96f38d6e53a0c5332b417c1 source_ref=da91ee7ba7df534c772bf0cfb02b2cfcdb8bce67 -->
Synchronizes individual Python source files to their corresponding triefact documentation files.

- `backfill_section_records` — populates database records from existing triefact files on disk
- `sync_single_file` — generates or refreshes a complete triefact file for one source file
- `refresh_triefact_metadata` — updates front matter without regenerating section bodies
- `FileSyncResult` — captures statistics from a single file sync operation
- `MetadataRefreshResult` — reports whether metadata refresh changed file contents
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/single_file:backfill_section_records fingerprint=dec06899d9b80748da3f949a0b97ccdb9c0cfd7a048bf544ccb3e0c4025e7c21 body_fp=3dbc857864d35b09fb7b901abc25f9b76e8bb3e0c85b26d3443d0192f973997d source_ref=da91ee7ba7df534c772bf0cfb02b2cfcdb8bce67 -->
Populate triefact_sections database records from existing triefact files on disk.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/single_file:FileSyncResult fingerprint=f658b6cb6f956faf262f29751e15b6efaad12e661c2976d58946940db38a0ed7 body_fp=fc9dee2a0b539e96f0df663b0399d746688457fc2350fd97ba5e605e8c7e2594 source_ref=da91ee7ba7df534c772bf0cfb02b2cfcdb8bce67 -->
Records the outcome of syncing a single source file to its triefact.

- `symbols_skipped`: Symbols whose existing sections were left untouched because they were not in `symbols_to_regen`
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/single_file:MetadataRefreshResult fingerprint=0049c0670ad0f133fe15a0c3be095e1eeb57d78e4751912b0e33094080c9e04e body_fp=35d00b34d0299807ae6b8c08fbb8ba08873b8cc84e39f12fbeeead450982cf00 source_ref=da91ee7ba7df534c772bf0cfb02b2cfcdb8bce67 -->
Represents the outcome of refreshing triefact metadata for a single file.

- `changed`: True when the rewritten triefact bytes differ from the previous bytes
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/single_file:_SymbolJob fingerprint=0f7b75b7a065300e3f0be7a0e01b8244c10ca3f48b6706b7dbfea7ecaacef021 body_fp=eb221f55b2367269359b5ae986754ecea9eff7835a2c7239175aed0dc83fd888 source_ref=da91ee7ba7df534c772bf0cfb02b2cfcdb8bce67 -->
Carries Symbol and optional previous content to thread pool workers for parallel section generation.

- `previous_source`: Previous symbol signature+body text for diff-aware generation, None for cold-write
- `previous_prose`: Previous section body text for diff-aware generation, None for cold-write
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/single_file:_file_fingerprint fingerprint=46c7c51a18ded3953f42cbf0478b0794532566079fd73b079dc9950d2c108e07 body_fp=e68aa9775ae9b778503c33b325143f9a12b6ce6552f8b4c88c1e6477eae7fe3a source_ref=da91ee7ba7df534c772bf0cfb02b2cfcdb8bce67 -->
Computes a SHA256 hash of the input text as a hexadecimal string.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/single_file:_triefact_path_for fingerprint=1c2e2cf4fa444cf778b7950d1adb2c52f77952ba318f32650aa629fbcb6ee9a5 body_fp=f3af242cde387d60e322268b4dc3f74f73599045beed4a87abeba99d881e0cc2 source_ref=da91ee7ba7df534c772bf0cfb02b2cfcdb8bce67 -->
Computes the triefact file path for a given source file by mapping its relative position under the source root to the triefacts root with a .md extension.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/single_file:_file_description fingerprint=97cc879f813f006954b5d0e6ede8050e2fe029e19ecc73d275a9986d8eaed371 body_fp=1381706f5e1497febc88fededae11ae982aeeb37aadbf1d614a2147844e4fdb7 source_ref=da91ee7ba7df534c772bf0cfb02b2cfcdb8bce67 -->
Extracts the first non-empty line from a source file's module docstring as a description.

- Returns None when the file has no module docstring
- Strips string literal syntax and whitespace from the raw docstring content
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/single_file:_build_defines fingerprint=ff4c3234574641e864f5fd19df73f86a54f735ea2a1cb641153e502aca6f4f1a body_fp=b2334208541a186a51f8bdc0e3a4d9d975d9342bd83bc9f5fd7eb17596feb6e0 source_ref=da91ee7ba7df534c772bf0cfb02b2cfcdb8bce67 -->
Builds a list of dictionaries containing symbol metadata for triefact front matter.

- Returns entries with `kind`, `qualified_name`, and `lines` fields for each symbol
- Sorted by start line to match source file order
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/single_file:_resolve_previous_symbols fingerprint=7248cfa7303b0870f3a978ae9e249057d98b22401fd3291ebff715fa17660edf body_fp=3ef5d1ca85f338214adda448cc6ab6e663574abfbbd1fd7d649152fbe09a75d1 source_ref=da91ee7ba7df534c772bf0cfb02b2cfcdb8bce67 -->
Retrieve previous Symbol instances for qualified names that have git blob references by fetching and parsing historical file content.

- Groups lookups by blob hash to minimize git calls and parsing overhead
- Returns empty dict when no section references exist
- Skips symbols that can't be resolved due to unreachable blobs or parse errors
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/single_file:refresh_triefact_metadata fingerprint=22c4df71adb33d8327a2ecbd2d9475971bd9a0f875943e7b3a4a251f85b8ab92 body_fp=a937a868bc56aca5b842b6ac79a293451b67b3e9320335e0f68c81e301406c64 source_ref=da91ee7ba7df534c772bf0cfb02b2cfcdb8bce67 -->
Refreshes a triefact file's front matter from the current store without calling the LLM.

- `store` — when None, skips reference counts in front matter; other metadata still updates
- Returns `MetadataRefreshResult` with `changed=True` if rewritten bytes differ from disk
- Preserves existing `last_synced_at` timestamp and all section bodies unchanged
- No-op returning `changed=False` when the triefact file doesn't exist
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/single_file:sync_single_file fingerprint=33830059212986a596cd483079c63d317a0b8111691cb98fd21894eaa6712230 body_fp=d85fb7fc833c91b4c28bedddf2d8e5e128ba5aef72a63fbf60662d483b2ec4c5 source_ref=da91ee7ba7df534c772bf0cfb02b2cfcdb8bce67 -->
Generate or refresh the triefact file for a single Python source file using LLM documentation.

- `symbols_to_regen`: None regenerates all symbols; set of qnames regenerates only listed symbols
- `dest_triefact_path`: writes to custom path instead of canonical triefact location when provided
- `force`: bypasses diff-aware regeneration and generates all sections cold regardless of source changes
- Uses thread pool bounded by `config.sync.concurrency` for parallel symbol generation
- Preserves existing hand-written prose between trie:section sentinels
- Removes sections for symbols no longer present in source code
- Warms prompt cache serially with first symbol then parallelizes remaining generation
<!-- trie:end -->