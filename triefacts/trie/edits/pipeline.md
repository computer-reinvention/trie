---
trie_version: 0.1.9
source: trie/edits/pipeline.py
file_fingerprint: 49faae8fe0202c3a6c5276842a1281e7d6d70383ab8a0a1d2a95907f2afead9a
last_synced_at: '2026-07-25T08:07:24Z'
description: The stage/commit edit pipeline.
defines:
- kind: module
  qualified_name: trie/edits/pipeline:__module__
  lines: 1-1654
- kind: function
  qualified_name: trie/edits/pipeline:_splice
  lines: 58-69
- kind: function
  qualified_name: trie/edits/pipeline:_per_symbol_compile_salvage
  lines: 72-115
- kind: function
  qualified_name: trie/edits/pipeline:_fix_imports_for_structural
  lines: 118-162
- kind: function
  qualified_name: trie/edits/pipeline:_read_span
  lines: 165-167
- kind: function
  qualified_name: trie/edits/pipeline:_rename_source
  lines: 170-213
- kind: function
  qualified_name: trie/edits/pipeline:_synthesize_session_note
  lines: 216-229
- kind: class
  qualified_name: trie/edits/pipeline:_GenJob
  lines: 233-243
- kind: function
  qualified_name: trie/edits/pipeline:stage
  lines: 246-589
- kind: function
  qualified_name: trie/edits/pipeline:build_workorder
  lines: 592-710
- kind: function
  qualified_name: trie/edits/pipeline:_expand_caller_jobs
  lines: 713-812
- kind: function
  qualified_name: trie/edits/pipeline:_expand_structural_caller_jobs
  lines: 815-880
- kind: function
  qualified_name: trie/edits/pipeline:_stage_creates
  lines: 883-1071
- kind: function
  qualified_name: trie/edits/pipeline:_place_new_symbol
  lines: 1074-1115
- kind: function
  qualified_name: trie/edits/pipeline:_find_container_span
  lines: 1118-1171
- kind: function
  qualified_name: trie/edits/pipeline:_insert_into_parent
  lines: 1174-1239
- kind: function
  qualified_name: trie/edits/pipeline:_multifile_scratch_lsp
  lines: 1242-1308
- kind: constant
  qualified_name: trie/edits/pipeline:_OVERLAY_SKIP_PARTS
  lines: 1311-1311
- kind: function
  qualified_name: trie/edits/pipeline:_overlay_package
  lines: 1314-1351
- kind: function
  qualified_name: trie/edits/pipeline:commit
  lines: 1354-1538
- kind: function
  qualified_name: trie/edits/pipeline:stage_and_commit
  lines: 1541-1563
- kind: function
  qualified_name: trie/edits/pipeline:record_intent
  lines: 1566-1653
incoming_refs: 36
outgoing_refs: 42
---
<!-- trie:section symbol=trie/edits/pipeline:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=e9452fa5658e80ab55660f3be77286f883bbd5a3f02d8be7a680e82f156d1c30 source_ref=acbee5dfa56099ae5afd4c2ba335609bcbbb64c6 role=orchestration -->
Implements the stage/commit edit pipeline for parallel symbol modification with cascade validation.

- `stage`: generates patched symbols in parallel via pluggable backend, validates compilation and LSP cleanliness in scratch tree
- `commit`: atomically writes validated changes to disk with database transaction wrapping and rollback on failure  
- Auto-cascade: modifies direct callers of changed symbols using LLM-gated filtering for modify ops, deterministic cascade for delete/rename
- Session note gate: multi-symbol applies require authored unifying intent (≥12 chars, not boilerplate)
- LSP integration: multi-file scratch overlay ensures cross-file edits see consistent import graph
- Commit modes: all_or_nothing (default) vs per_item for granular failure handling
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:_splice fingerprint=78befe1c5dd1db9f925a29b101b0eb2afa0a9d9ede0ca2fa6f07675f0f8769f4 body_fp=5e9ae468ddc5cf796925e59c7acb8846a777132a891fd947c6a7686a05f6b5f7 source_ref=acbee5dfa56099ae5afd4c2ba335609bcbbb64c6 role=util -->
Replace a span of file lines with new source code, handling line-based splicing.

- `start_line`, `end_line`: 1-indexed inclusive line range to replace
- `new_src`: replacement text (empty string removes the span entirely)
- Returns new list of file lines with the splice applied
- Ensures replacement text ends with newline unless empty
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:_per_symbol_compile_salvage fingerprint=d20711b1f745f4bd104120c5e579f70ad4c4c9242010cb1971f089380af39035 body_fp=cc29bf8ddec655a5e9dad559ff62fc9592cbe03938ec259ef556d523448e8982 source_ref=3756feeb097f734409469642535809b6daae49f1 role=domain -->
Salvage a failed whole-file compile by re-splicing each successful symbol individually onto the original, keeping only those that compile alone and together.

- Returns `(good_items, combined_after_bytes)`; falls back to `([], original_bytes)` if combined survivors also fail to compile.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:_fix_imports_for_structural fingerprint=da6ef33786c3d50ec51f1170a8f431a4229a1579ce481a6ce0b757a1097c7d1e body_fp=15d7d0d857db7f60c1d3b1f3c16eb701d2564ba5d1a11f413db29b62f83f850b source_ref=acbee5dfa56099ae5afd4c2ba335609bcbbb64c6 role=util -->
Rewrites `from ... import ...` lines after symbol delete/rename operations by dropping deleted names and updating renamed names while preserving aliases.

- `deleted_names`: symbol names to remove from import statements
- `renamed`: mapping from old names to new names for renaming
- Returns the modified text with import lines updated deterministically
- Only processes simple comma-separated imports, skips parenthesized and star imports
- Removes entire import lines that become empty after deletions
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:_read_span fingerprint=15e5eb911ac702b246aabb256829c4446fe1cee81c3c423873bd39b34d9dd72f body_fp=a62ad351e9f6cd74d5d3c2899c31456fc84287d88ac51fae7dc712cffbf329e0 source_ref=acbee5dfa56099ae5afd4c2ba335609bcbbb64c6 role=util -->
Extract lines from file_text between start_line and end_line (1-indexed, inclusive).

- `start_line`: first line to include (1-indexed)
- `end_line`: last line to include (1-indexed, inclusive)
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:_rename_source fingerprint=dccb94859f33d831243668efa6365acef6b1efb1bc838187728f9d7f9df5478c body_fp=fb1fc971f6158e0f0552c11f159d2b28f87670855abdc5fe70ee4a709e32bafe source_ref=acbee5dfa56099ae5afd4c2ba335609bcbbb64c6 role=parsing -->
Renames a symbol's definition header (def/class/async def) within its source span deterministically.

- Returns (new_source, error_message) tuple where error is None on success
- Validates new_name is a valid identifier and differs from current name
- Locates definition header by matching keyword + name token boundaries
- Refuses rename if header cannot be located unambiguously to avoid corruption
- Only replaces the first occurrence of the name after the definition keyword
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:_synthesize_session_note fingerprint=fea1dade456872cf9b45ac658fe7d4666c7959dc65615c2e4309b044b6630622 body_fp=88c2b204a6c8948c2ec5faeebe220073f3cd2b22b65628092e989d5836c65b32 source_ref=acbee5dfa56099ae5afd4c2ba335609bcbbb64c6 role=util -->
Generates a concise session note summarizing pending edit operations from seed symbols and create operations.

- `seed_qnames`: qualified names of symbols being modified/deleted/renamed
- `create_grouped`: dictionary mapping file paths to lists of create patch dictionaries
- Returns: formatted summary like "edit symbol1, symbol2, create symbol3" or "batch edit" if empty
- Truncates to first 8 operations to keep the summary manageable
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:_GenJob fingerprint=635fb56198b8aaedb5ed3e9b32123856d097065b5bbeaf695faac30603604833 body_fp=23d7d5043e4ae9761ecceb45c763a9faa4e48627cb6fc5e0643e49c85dcd8a90 source_ref=1f152994a6c01e47af87fa54c3ae20b8aedcc1d9 role=model -->
Holds parameters for one symbol's edit generation job during parallel processing.

- `op`: operation type - "modify", "delete", or "rename"
- `new_name`: target name for rename operations (empty for modify/delete)
- `callees`/`callers`: neighbor context lists for generation backend
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:stage fingerprint=327c639cc30077c47133560af0bc2a77d94cbbab2230142f494f42003c4c36ec body_fp=58796615c92d33d69c33b057c09f670ec0754c47207b571c2662ebbc118478a4 source_ref=3756feeb097f734409469642535809b6daae49f1 role=orchestration -->
Generate and validate all pending patches in parallel without writing to the real source tree.

- `staged_changes`: ready for commit if report.ok is True, otherwise carry repatch calls
- Requires session_note for multi-symbol applies (>= 12 chars, not boilerplate)
- Performs auto-cascade to callers of modified/deleted/renamed symbols
- Runs parallel generation via backend, then splices results per-file
- Gates on compile-check and multi-file LSP validation in scratch overlay
- Returns (ApplyReport, list[StagedChange]) tuple
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:build_workorder fingerprint=6b88963e5f909bcda742fe8a23e0a6db7c55659a3c7ecf961004410a13f8ec7c body_fp=d4135453ce2385b79b4785294b2b48f5891d6328202a34722508509e443d6f59 source_ref=1f152994a6c01e47af87fa54c3ae20b8aedcc1d9 role=orchestration -->
Resolve all pending patches into a structured work-order dict for native (non-LLM-pipeline) editing, without writing any files.

- `items`: one entry per modify/delete/rename seed with merged notes, line span, and `callers_to_review`
- `creates`: flattened list of create-patch descriptors
- `expected_symbols`: sorted union of seed and create qnames
- `unresolved`: symbols whose `store` detail could not be found
- Returns `ok: False` with `session_note_required` when `> 1` item and note is absent/boilerplate
- `next`: advisory string instructing the caller to edit natively, then `trie refresh` and `patch drop --all`
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:_expand_caller_jobs fingerprint=6a6443f4a4ca9125ad76cf2a7e0c59856afe4c6143435976f369a63d15b0bc3e body_fp=4fb39c7c1226dc9737fda9718a5738c4ab8376041a618616b422f7ad00cb4c45 source_ref=acbee5dfa56099ae5afd4c2ba335609bcbbb64c6 role=orchestration -->
Expands the generation job list with callers that need updates due to modified seeds.

- Uses `references_in()` for symbol-accurate caller discovery, not file-level cascade
- LLM-gates via `pre_filter_batch` when client is available; otherwise surfaces as advisory items
- Skips hub symbols (inbound count > threshold) to prevent cascade explosion
- Without client, adds non-blocking unresolved items if `surface_unresolved` is enabled
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:_expand_structural_caller_jobs fingerprint=75e516e62dc8e336546438293d9f214c73b789212024f4eaf3ebf2ed2dadc71c body_fp=1d222f790d5d9dcedddaeecb527228747c519e8f22b315018a9e7e9464bdd9c2 source_ref=acbee5dfa56099ae5afd4c2ba335609bcbbb64c6 role=orchestration -->
Cascade callers of deleted/renamed symbols by adding generation jobs to rewrite their call sites.

Unlike modify cascades, this requires no LLM gate since call sites referencing vanishing/renamed symbols are definitively affected. For each caller of a deleted symbol, queues a modify job with instructions to remove all calls. For rename callers, queues jobs to update call syntax from old to new name.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:_stage_creates fingerprint=317951afc6dcd5ab116cc56d031ba4afec5a5dfe87577e0935326c2547eb6fa0 body_fp=57dca16dc21b7b02661bb49cb1bcdb21419a0dfd360a43254c9ece114afcb4da source_ref=1f152994a6c01e47af87fa54c3ae20b8aedcc1d9 role=orchestration -->
Generate and stage each new symbol creation, appending StagedChanges with op='create'.

- placement: after anchor symbol if resolvable, otherwise at end-of-file; member creates route into the parent container via `_place_new_symbol`
- stacks creates atop existing file modifications to maintain single coherent after_file_bytes
- `FileNotFoundError` on the target file scaffolds from empty (true new-file creation)
- each StagedChange carries `module_remarks` and `new_dependencies` captured from the backend result
- compile-gates the whole file after placement; on failure, re-places each symbol alone against the pre-creates base image and salvages the compiling subset — only genuinely broken symbols surface as unresolved
- updates prior staged changes to share final file content for atomic commit
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:_place_new_symbol fingerprint=a7c48ded07d7d6fc8dc439292d4b0e564ffeda96c8a5354905a0d38f43efa4da body_fp=81c3e268c5b79f5f284803a795344579a84f51850b6393b341e1a5f98e470d04 source_ref=3756feeb097f734409469642535809b6daae49f1 role=util -->
Insert `new_source` into `file_text` using a three-priority placement strategy.

- `qname` with a dotted local (e.g. `module:Parent.child`) inserts inside the parent body via `_insert_into_parent`, re-indented to member level
- `anchor_qname` (if resolvable) places the block after that symbol's end line with two newlines
- Empty file returns the block alone; otherwise appends with three newlines at end-of-file
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:_find_container_span fingerprint=4c489a60377f7ac90db90e55664c010b01bcbb6e8777a95febf1a5c4dd9b8ae9 body_fp=c1f316c0ed6aee7e8534d2922538862ea3e9e913f5668bdc4f60c725c99adeb8 source_ref=3756feeb097f734409469642535809b6daae49f1 role=util -->
Scan `lines` for a container declaration matching `name` and return its `(start, end)` span as 0-indexed start and exclusive end.

- Supports brace-delimited (TS/JS) and indentation-delimited (Python) bodies.
- Returns `None` if `name` is falsy or no matching header is found.
- Brace style: balances `{`/`}` from the opening line; returns `None` if unmatched.
- Indent style: span ends at the first line at or below the header's indentation level.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:_insert_into_parent fingerprint=65da59d298cf892b1f20473a442f662218e99d2728058845124608fefb9c0dfb body_fp=a9b4dbfe901fff4442e0545acd9a5c3c80ba3cbd18a1a59188f8ca44e466c7ce source_ref=3756feeb097f734409469642535809b6daae49f1 role=util -->
Re-indent `block` to member level and splice it as the last member inside the parent container's body in `file_text`.

- `parent_detail`: stored `SymbolDetail`; span may be stale if a prior in-batch modify shifted lines — recomputed from text when `parent_name` is provided.
- `parent_name`: used to locate the container via `_find_container_span`; falls back to stored span if `None`.
- Returns `None` when the span is unusable; caller falls back to file-scope placement.
- Brace languages (TS/JS): inserts before the closing `}` line; indentation languages (Python): appends after the body.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:_multifile_scratch_lsp fingerprint=43f30c715415f30a62d2017424c263b2fe640486d22b7689c61c609d5531f61a body_fp=a6cc3bf47aaf19757cbd0fca63b77cc38d268e0bda47fff9654c8dab004bde7e source_ref=3756feeb097f734409469642535809b6daae49f1 role=orchestration -->
Runs LSP diagnostics + fixup over all changed files in one consistent scratch tree.

- Creates temporary directory with hardlinked package structure for import resolution
- Overlays staged file candidates and runs per-file LSP check (via `lsp_backends_for_file`) with bounded retry fixup
- Skips entirely if no candidate file has a registered LSP checker
- Mutates `staged` in place with LSP-cleaned versions of `after_file_bytes`
- Cross-file consistency: renamed symbols appear defined to checker, preventing reversion
- Degrades gracefully on errors, leaving candidates unchanged
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:_OVERLAY_SKIP_PARTS fingerprint=3ae41bda7d1b2f3ec7baba171162384d44b95e98599b4bcdbc251301c4a79533 body_fp=69e39da3ddbc683a431d8fe63e873cf1f3833327a81d8434ad989e66249f5f42 source_ref=afa6244798668a85b5b12de47f75345fb12f3148 role=config -->
Directory name segments skipped during `_overlay_package` hardlink traversal.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:_overlay_package fingerprint=2aea15a23cf210178914b315eff21e723dd0c415ce825cf600fb06750973d284 body_fp=a112aa647285b1f298c276fa7d484d2e2baaa71bd1c7a48fc104bb92ea17340a source_ref=afa6244798668a85b5b12de47f75345fb12f3148 role=io -->
Hardlinks all indexable source files and language-specific config files (e.g. `tsconfig.json`) from `src_root` into `scratch_root`, using globs from registered language backends.

- Skips paths containing any part in `_OVERLAY_SKIP_PARTS` (`.trie`, `__pycache__`, `.git`, etc.)
- File sets are driven by `registry.all_backends()` — covers all registered languages, not just Python
- Extra config files (e.g. `tsconfig.json`) are linked via `backend.overlay_extra_files()`
- Falls back to copying on hardlink failure
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:commit fingerprint=c67fb5db394af86089cae1d139b87f7c3c782cebb5cc0635cdc679a984c61bf1 body_fp=3de8aaffc9b84f7dea2b5e5f5c7c58163b98323efdf9d7f9f12aac364d4b76e0 source_ref=1f152994a6c01e47af87fa54c3ae20b8aedcc1d9 role=orchestration -->
Writes validated staged changes to disk atomically, rescans affected files, updates prose sections, and drops applied patches.

- `commit_mode`: "all_or_nothing" (default) blocks write if blocking unresolved exist; "per_item" writes each file independently
- `session_note`: archived alongside applied-patch records in the session log via `record_applied`
- Returns updated report with `committed` flag and populated `applied` list
- Rolls back source files from in-memory before-images on any failure; newly created files are unlinked rather than restored
- Populates `report.new_dependencies` and `report.module_remarks` from staged changes
- Surfaces orphan created symbols (no inbound references) as advisory unresolved items
- Archives patch notes to the session log after a successful write; failures are suppressed
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:stage_and_commit fingerprint=89f655eee91fd326d520a21e68afacb42ad9a979b3852e1e8b77773cdc8243b1 body_fp=7fcdd9c33e30220e28f31d8d26c36069b20e25d9ca7988040f95bd0854cb3dfa source_ref=1f152994a6c01e47af87fa54c3ae20b8aedcc1d9 role=orchestration -->
Executes stage then commit in sequence, returning the final report.

- Used by the `commit()` MCP tool for one-shot patch application
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:record_intent fingerprint=d372f18929e5f40eb4325c068083295320f3308d2a25d4b7c64917804873710b body_fp=b1045c415ae6e561660ae422fc41b08dcb589d987bd3ed82c329530438ee3520 source_ref=e27cc08374574437a8cec87850a73230a84f1186 role=orchestration -->
Archive all pending patch notes to the session log and clear the queue, without generating any code.

- `session_note`: required when `total > 1`; returns `ok=False` with `"session_note_required"` otherwise.
- Returns a dict with `ok`, `recorded` count, `symbols` list, and a `next` advisory string.
<!-- trie:end -->