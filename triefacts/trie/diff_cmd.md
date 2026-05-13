---
trie_version: 0.1.0
source: trie/diff_cmd.py
file_fingerprint: 08ed6eafaada2d96c6b49b87678500785ee5aebe1173eb337d1ff5b441dd9b07
last_synced_at: '2026-05-12T18:34:10Z'
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
<!-- trie:section symbol=trie/diff_cmd:FileDiff fingerprint=bbaa5525d99c5a921555181054314026e079df655184757146e111be5a021380 body_fp=bd2879bb032bab2aea4e9d9ca522f2a137c3a1dcd2219b663a36e23327a9a71c -->
## `FileDiff`

Frozen dataclass holding the diff result for a single stale source file.

- `source_path`: relative path of the source file
- `canonical_triefact_path`: existing triefact on disk
- `preview_triefact_path`: regenerated triefact written under `.trie/preview/`
- `unified_diff`: unified diff string comparing canonical to preview
- `sync_result`: raw result from the underlying sync operation
<!-- trie:end -->

<!-- trie:section symbol=trie/diff_cmd:DiffResult fingerprint=86f0131d3b4847f6b1543e4465a0b65119ed8675475fa3fbbe50951b01784721 body_fp=ccf28961c20e9c6ba489bee48edd87412afe2538480816a6b196681dc838f58e -->
## `DiffResult`

Frozen dataclass holding the outcome of a `diff_project` run.

- `diffs`: per-file diff records for all regenerated stale triefacts.
- `files_skipped_no_budget`: count of files skipped due to limit or budget exhaustion.
- `actual_cost_usd`: cumulative model cost in USD across all processed files.
<!-- trie:end -->

<!-- trie:section symbol=trie/diff_cmd:diff_project fingerprint=edb982dc1acfc078364a682a2fb826d8e69db0f15f3f08e187b6c2f51c6f41e8 body_fp=b7661dc7e702923a30aa09be1e44e9592db91a26639b18cf52349a8e5b56bd89 -->
## `diff_project(*, project_root, config, client, pricing=None, budget_usd=None, limit=None, progress=None, store=None) -> DiffResult`

Regenerate stale triefacts into `.trie/preview/` and return unified diffs against canonical versions.

- `budget_usd`: stops processing new files once cumulative cost reaches this threshold.
- `limit`: caps the number of diffs produced; excess files counted in `files_skipped_no_budget`.
- `store`: optional graph store passed through to `sync_single_file`.
- Returns `DiffResult` with diffs, skip count, and total estimated cost.
<!-- trie:end -->