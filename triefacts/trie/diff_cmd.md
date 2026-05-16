---
trie_version: 0.1.0
source: trie/diff_cmd.py
file_fingerprint: 4000181a96da75377e49dd956d62958fee83874a5a2404378edb21fb0e9d64cc
last_synced_at: '2026-05-16T11:23:49Z'
defines:
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
outgoing_refs: 5
---
<!-- trie:section symbol=trie/diff_cmd:FileDiff fingerprint=bbaa5525d99c5a921555181054314026e079df655184757146e111be5a021380 body_fp=79735eb295844c7a754b9c9b82fdd2e869b6a646865d6a616d67803c9fddb876 source_ref=6f05daac303d962947af10d1a505706948b32064 -->
## `FileDiff(source_path, canonical_triefact_path, preview_triefact_path, unified_diff, sync_result)`

Immutable record pairing a stale source file with its preview triefact path, unified diff text, and sync result.
<!-- trie:end -->

<!-- trie:section symbol=trie/diff_cmd:DiffResult fingerprint=86f0131d3b4847f6b1543e4465a0b65119ed8675475fa3fbbe50951b01784721 body_fp=b88702a44274db068508df0184c4da0d1440be924b9e20d72b2e1550d1ffd456 source_ref=b27d7657d1e987fdf66bd52ab7c7b86d576cae2b -->
## `DiffResult(diffs: list[FileDiff] = ..., files_skipped_no_budget: int = 0, actual_cost_usd: float = 0.0)`

Frozen dataclass holding the aggregate outcome of a `diff_project` run.

- `files_skipped_no_budget`: count of files skipped due to limit or budget exhaustion.
- `actual_cost_usd`: total estimated USD spent on model calls during the run.
<!-- trie:end -->

<!-- trie:section symbol=trie/diff_cmd:diff_project fingerprint=bf8c5025e2d84ba1b505f054c1303f130e6589b23bd4a0d3c4abfc00ee48f9f2 body_fp=630f2ebd53b0d152d3e84e73fb33d27c100e258f3fcdb92095230f3dca348699 source_ref=6f05daac303d962947af10d1a505706948b32064 -->
## `diff_project(*, project_root, config, client, pricing=None, budget_usd=None, limit=None, progress=None, store=None) -> DiffResult`

Regenerate stale triefacts into `.trie/preview/` and return unified diffs against canonical versions.

- `budget_usd`: stops processing new files once cumulative cost exceeds this value.
- `limit`: caps the number of diffs produced; remaining files are skipped.
- `files_skipped_no_budget`: counts files skipped due to limit, budget, or missing source.
<!-- trie:end -->