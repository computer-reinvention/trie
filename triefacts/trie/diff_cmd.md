---
trie_version: 0.1.0
source: trie/diff_cmd.py
file_fingerprint: 08ed6eafaada2d96c6b49b87678500785ee5aebe1173eb337d1ff5b441dd9b07
last_synced_at: '2026-05-14T17:30:26Z'
defines:
- kind: class
  qualified_name: trie/diff_cmd:FileDiff
  lines: 17-22
- kind: class
  qualified_name: trie/diff_cmd:DiffResult
  lines: 26-29
- kind: function
  qualified_name: trie/diff_cmd:diff_project
  lines: 32-128
incoming_refs: 6
outgoing_refs: 5
---
<!-- trie:section symbol=trie/diff_cmd:FileDiff fingerprint=bbaa5525d99c5a921555181054314026e079df655184757146e111be5a021380 body_fp=b1e6021bf4676f2ac12a94e7f90753f24469a55a42bb5c86d8161f45a0ddbd67 -->
## `FileDiff(source_path, canonical_triefact_path, preview_triefact_path, unified_diff, sync_result)`

Immutable record pairing a stale source file with its regenerated preview triefact and unified diff output.
<!-- trie:end -->

<!-- trie:section symbol=trie/diff_cmd:DiffResult fingerprint=86f0131d3b4847f6b1543e4465a0b65119ed8675475fa3fbbe50951b01784721 body_fp=d776a96dfb585a96328cfcb99e4dcaaab4e0d99d77239a5c4541864ac4e3d5e6 -->
## `DiffResult`

Frozen dataclass holding the outcome of a `diff_project` run.

- `diffs`: per-file diff records for every regenerated stale source.
- `files_skipped_no_budget`: count of files skipped due to limit or budget exhaustion.
- `actual_cost_usd`: cumulative model cost for the run in USD.
<!-- trie:end -->

<!-- trie:section symbol=trie/diff_cmd:diff_project fingerprint=edb982dc1acfc078364a682a2fb826d8e69db0f15f3f08e187b6c2f51c6f41e8 body_fp=adef52cd659ed2c6a279852eeebc0d33e3f60b2b0af80df5e5265128623f468f -->
## `diff_project(*, project_root, config, client, pricing=None, budget_usd=None, limit=None, progress=None, store=None) -> DiffResult`

Regenerate stale triefacts into `.trie/preview/` and return unified diffs against canonical versions.

- `budget_usd`: stops processing new files once cumulative cost reaches this threshold.
- `limit`: caps the number of diffs produced; remaining files are skipped.
- `files_skipped_no_budget`: counts files skipped due to limit, budget, or missing source.
<!-- trie:end -->