---
trie_version: 0.1.9
source: trie/edits/pipeline.py
file_fingerprint: 8c5fb54d4570e43c8a68ad40e5992e262a2c5151c5a82c62ea78c4dcaf229642
last_synced_at: '2026-06-17T16:41:27Z'
description: The stage/commit edit pipeline.
defines:
- kind: module
  qualified_name: trie/edits/pipeline:__module__
  lines: 1-1094
- kind: function
  qualified_name: trie/edits/pipeline:_splice
  lines: 55-66
- kind: function
  qualified_name: trie/edits/pipeline:_fix_imports_for_structural
  lines: 69-113
- kind: function
  qualified_name: trie/edits/pipeline:_read_span
  lines: 116-118
- kind: function
  qualified_name: trie/edits/pipeline:_rename_source
  lines: 121-164
- kind: function
  qualified_name: trie/edits/pipeline:_synthesize_session_note
  lines: 167-180
- kind: class
  qualified_name: trie/edits/pipeline:_GenJob
  lines: 184-194
- kind: function
  qualified_name: trie/edits/pipeline:stage
  lines: 197-519
- kind: function
  qualified_name: trie/edits/pipeline:_expand_caller_jobs
  lines: 522-621
- kind: function
  qualified_name: trie/edits/pipeline:_expand_structural_caller_jobs
  lines: 624-689
- kind: function
  qualified_name: trie/edits/pipeline:_stage_creates
  lines: 692-822
- kind: function
  qualified_name: trie/edits/pipeline:_place_new_symbol
  lines: 825-843
- kind: function
  qualified_name: trie/edits/pipeline:_multifile_scratch_lsp
  lines: 846-910
- kind: constant
  qualified_name: trie/edits/pipeline:_OVERLAY_SKIP_PARTS
  lines: 913-913
- kind: function
  qualified_name: trie/edits/pipeline:_overlay_package
  lines: 916-953
- kind: function
  qualified_name: trie/edits/pipeline:commit
  lines: 956-1076
- kind: function
  qualified_name: trie/edits/pipeline:stage_and_commit
  lines: 1079-1093
incoming_refs: 32
outgoing_refs: 35
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
<!-- trie:section symbol=trie/edits/pipeline:_GenJob fingerprint=635fb56198b8aaedb5ed3e9b32123856d097065b5bbeaf695faac30603604833 body_fp=23d7d5043e4ae9761ecceb45c763a9faa4e48627cb6fc5e0643e49c85dcd8a90 source_ref=acbee5dfa56099ae5afd4c2ba335609bcbbb64c6 role=model -->
Holds parameters for one symbol's edit generation job during parallel processing.

- `op`: operation type - "modify", "delete", or "rename"
- `new_name`: target name for rename operations (empty for modify/delete)
- `callees`/`callers`: neighbor context lists for generation backend
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:stage fingerprint=26f5bfa86b685e8c174fe3fa652967449aa9e219212806e074117248fc8c5846 body_fp=58796615c92d33d69c33b057c09f670ec0754c47207b571c2662ebbc118478a4 source_ref=acbee5dfa56099ae5afd4c2ba335609bcbbb64c6 role=orchestration -->
Generate and validate all pending patches in parallel without writing to the real source tree.

- `staged_changes`: ready for commit if report.ok is True, otherwise carry repatch calls
- Requires session_note for multi-symbol applies (>= 12 chars, not boilerplate)
- Performs auto-cascade to callers of modified/deleted/renamed symbols
- Runs parallel generation via backend, then splices results per-file
- Gates on compile-check and multi-file LSP validation in scratch overlay
- Returns (ApplyReport, list[StagedChange]) tuple
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
<!-- trie:section symbol=trie/edits/pipeline:_stage_creates fingerprint=dcefb272df37ca2ef10688261bbc5196feacbd85e156b6ae8cbed23042a4682f body_fp=2fef5ca8f84de04dc484cc31f5ccff8e1882cf32fb61d6c6a1bba26a529a60dd source_ref=acbee5dfa56099ae5afd4c2ba335609bcbbb64c6 role=orchestration -->
Generate and stage each new symbol creation, appending StagedChanges with op='create'.

- placement: after anchor symbol if resolvable, otherwise at end-of-file  
- stacks creates atop existing file modifications to maintain single coherent after_file_bytes
- compile-gates each file after placement; failures go to unresolved with generated source
- updates prior staged changes to share final file content for atomic commit
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:_place_new_symbol fingerprint=15f7408a31b1e11cdb6104b1687251d43f2c606af404e399394eaa81d99cc475 body_fp=51d3e273af37dd7ae1015db49b0d7c7cdfb49d7f558ad093bfa006e93331ba5a source_ref=acbee5dfa56099ae5afd4c2ba335609bcbbb64c6 role=util -->
Insert new_source after the anchor symbol's span, else at end-of-file.

- If anchor exists and is found, places new symbol after its end_line with two newlines
- For empty files, returns just the new symbol block
- Otherwise appends with three newlines at end-of-file
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:_multifile_scratch_lsp fingerprint=91329a859cefe2c13d6b4a424e7cdfc8a3bc2a8f42fa82a1a73d700a4713a472 body_fp=a6cc3bf47aaf19757cbd0fca63b77cc38d268e0bda47fff9654c8dab004bde7e source_ref=afa6244798668a85b5b12de47f75345fb12f3148 role=io -->
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
<!-- trie:section symbol=trie/edits/pipeline:commit fingerprint=2d6d9be2fe2e9cc86fc4fbfd7b8402de57292fc992035d9c68e7fe6aa0e547a7 body_fp=b484ac98666bc29ac23de20359288f430ff387b8fe1f3c8e4c7c259c443a8ee0 source_ref=acbee5dfa56099ae5afd4c2ba335609bcbbb64c6 role=orchestration -->
Writes validated staged changes to disk atomically, rescans affected files, updates prose sections, and drops applied patches.

- `commit_mode`: "all_or_nothing" (default) blocks write if blocking unresolved exist; "per_item" writes each file independently
- Returns updated report with `committed` flag and populated `applied` list
- Rolls back source files from in-memory before-images on any failure
- Surfaces orphan created symbols (no inbound references) as advisory unresolved items
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/pipeline:stage_and_commit fingerprint=f3c9c0549a51b6d0981b55e34a9abc544268459499eb490329eadc4e21956b96 body_fp=7fcdd9c33e30220e28f31d8d26c36069b20e25d9ca7988040f95bd0854cb3dfa source_ref=acbee5dfa56099ae5afd4c2ba335609bcbbb64c6 role=orchestration -->
Executes stage then commit in sequence, returning the final report.

- Used by the `commit()` MCP tool for one-shot patch application
<!-- trie:end -->