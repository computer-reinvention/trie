---
trie_version: 0.1.5
source: trie/diff_cmd.py
file_fingerprint: 4000181a96da75377e49dd956d62958fee83874a5a2404378edb21fb0e9d64cc
last_synced_at: '2026-05-28T01:40:22Z'
defines:
- kind: module
  qualified_name: trie/diff_cmd:__module__
  lines: 1-146
- kind: class
  qualified_name: trie/diff_cmd:FileDiff
  lines: 17-22
- kind: class
  qualified_name: trie/diff_cmd:DiffResult
  lines: 26-29
- kind: function
  qualified_name: trie/diff_cmd:diff_project
  lines: 32-145
incoming_refs: 6
outgoing_refs: 6
---
<!-- trie:section symbol=trie/diff_cmd:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=e1fbbc068efeb21a773ba682d164a15db8e5ebb5b4dd6b23d26ea101e8006a9b source_ref=6f05daac303d962947af10d1a505706948b32064 -->
## `trie/diff_cmd`

Regenerate stale triefacts into a preview directory and produce unified diffs without modifying canonical files.

- `FileDiff`: per-file diff result pairing canonical and preview paths with unified diff text
- `DiffResult`: aggregated diff output with cost tracking and skip count
- `diff_project`: entry point; respects budget, limit, and progress callbacks
<!-- trie:end -->
<!-- trie:section symbol=trie/diff_cmd:FileDiff fingerprint=bbaa5525d99c5a921555181054314026e079df655184757146e111be5a021380 body_fp=113e2b442b222f0f3b7fe7a75270d7c49d4a42bdae9ad046c8c4edc7f4e43d5d source_ref=6f05daac303d962947af10d1a505706948b32064 -->
## `FileDiff`

Immutable record of a single file's diff between its canonical and preview triefact.

- `unified_diff`: unified-diff string ready for display or writing.
- `preview_triefact_path`: path under `.trie/preview/` where regenerated content was written.
<!-- trie:end -->
<!-- trie:section symbol=trie/diff_cmd:DiffResult fingerprint=86f0131d3b4847f6b1543e4465a0b65119ed8675475fa3fbbe50951b01784721 body_fp=40e41114bdf3518c0c287fa1e0daf2a0567a25ec9c9f54b36b34dddd120504ff source_ref=6f05daac303d962947af10d1a505706948b32064 -->
## `DiffResult`

Immutable aggregate result returned by `diff_project`.

- `files_skipped_no_budget`: count of files skipped due to limit or budget exhaustion.
- `actual_cost_usd`: cumulative LLM spend across all processed files.
<!-- trie:end -->
<!-- trie:section symbol=trie/diff_cmd:diff_project fingerprint=bf8c5025e2d84ba1b505f054c1303f130e6589b23bd4a0d3c4abfc00ee48f9f2 body_fp=eb11ab922b1be9812c37b49a9b7ef6442a02585a9f7b4b2620fc9db9ef7dd824 source_ref=6f05daac303d962947af10d1a505706948b32064 -->
## `diff_project(*, project_root, config, client, pricing=None, budget_usd=None, limit=None, progress=None, store=None) -> DiffResult`

Regenerate stale triefacts into `.trie/preview/` and return unified diffs against canonical versions.

- `pricing`: when provided, accumulates estimated USD cost across regenerated files.
- `budget_usd`: stops processing new files once cumulative cost meets or exceeds this value.
- `limit`: stops after this many diffs have been collected; remaining files counted as skipped.
- `store`: optional graph `Store` passed through to `sync_single_file`.
- `DiffResult.files_skipped_no_budget`: count of files skipped due to limit, budget, or missing source.
<!-- trie:end -->