---
trie_version: 0.1.0
source: trie/diff_cmd.py
file_fingerprint: 08ed6eafaada2d96c6b49b87678500785ee5aebe1173eb337d1ff5b441dd9b07
last_synced_at: '2026-05-14T18:31:23Z'
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
<!-- trie:section symbol=trie/diff_cmd:FileDiff fingerprint=bbaa5525d99c5a921555181054314026e079df655184757146e111be5a021380 body_fp=1678b8f2952a74c0cbd3bab02fc06c78cbda53743b3c12b8242351cdfd415723 -->
## `FileDiff`

Frozen dataclass holding the diff artefacts for one stale source file.

- `unified_diff`: unified-diff string comparing canonical vs preview triefact.
- `sync_result`: full `FileSyncResult` including token usage from regeneration.
<!-- trie:end -->

<!-- trie:section symbol=trie/diff_cmd:DiffResult fingerprint=86f0131d3b4847f6b1543e4465a0b65119ed8675475fa3fbbe50951b01784721 body_fp=8b5f3a73229fa2c09ac77e2b21950f3653f4894bfa1a8007f0d0371e8f1b8bf1 -->
## `DiffResult(diffs: list[FileDiff] = [], files_skipped_no_budget: int = 0, actual_cost_usd: float = 0.0)`

Frozen dataclass holding the aggregate output of a `diff_project` run.

- `files_skipped_no_budget`: count of sources skipped due to limit or budget exhaustion.
- `actual_cost_usd`: total estimated spend across all regenerated files.
<!-- trie:end -->

<!-- trie:section symbol=trie/diff_cmd:diff_project fingerprint=edb982dc1acfc078364a682a2fb826d8e69db0f15f3f08e187b6c2f51c6f41e8 body_fp=c8e9948eec51d0e681608765e7fde2ecdb4ae9aedbb7b192420f15585dd5e6a0 -->
## `diff_project(*, project_root, config, client, pricing=None, budget_usd=None, limit=None, progress=None, store=None) -> DiffResult`

Regenerate stale triefacts into `.trie/preview/` and return unified diffs against canonical versions.

- `budget_usd`: stops processing new files once cumulative cost reaches this threshold.
- `limit`: caps the number of diffs produced; excess files are counted as skipped.
- `pricing`: when `None`, cost tracking is disabled and `actual_cost_usd` stays `0.0`.
- `files_skipped_no_budget`: count of files skipped due to limit, budget, or missing source.
<!-- trie:end -->