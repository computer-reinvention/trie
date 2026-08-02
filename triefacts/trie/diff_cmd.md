---
trie_version: 0.3.0
source: trie/diff_cmd.py
file_fingerprint: aede83b4992eaaf7ba79ed2b696080f3c91639d232164fe2f26f1fe01131e4dd
last_synced_at: '2026-08-02T21:19:28Z'
defines:
- kind: module
  qualified_name: trie/diff_cmd:__module__
  lines: 1-146
- kind: class
  qualified_name: trie/diff_cmd:FileDiff
  lines: 17-22
  signature: class FileDiff
- kind: class
  qualified_name: trie/diff_cmd:DiffResult
  lines: 26-29
  signature: class DiffResult
- kind: function
  qualified_name: trie/diff_cmd:diff_project
  lines: 32-145
  signature: 'def diff_project( *, project_root: Path, config: Config, client: TrieClient, pricing: ModelPricing | None = None, budget_usd: float | None = None, limit: int | None = None, progress: ProgressCallback | None = None, store: Store | None = None, ) -> DiffResult'
incoming_refs: 6
outgoing_refs: 9
---
<!-- trie:section symbol=trie/diff_cmd:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=d810b0b94f518f9a5e682ca34a9a1a2becaad8071293b7ab1e55133ef629d73e source_ref=1e1ead40b2ec4f67fd8bdb317097295a702459f9 role=documentation-sync -->
Generates unified diffs between current triefacts and regenerated previews for stale symbols.

- `FileDiff`: dataclass containing paths and diff information for a single source file
- `DiffResult`: dataclass aggregating all file diffs with cost and skip statistics
- `diff_project()`: main function that checks staleness, regenerates into `.trie/preview/`, and creates unified diffs
<!-- trie:end -->
<!-- trie:section symbol=trie/diff_cmd:FileDiff fingerprint=bbaa5525d99c5a921555181054314026e079df655184757146e111be5a021380 body_fp=cbbf2bb08222e0b486a5d1bebeadbbf09267d9313f606c6c542b53264311a36f source_ref=1e1ead40b2ec4f67fd8bdb317097295a702459f9 role=model -->
## `class FileDiff`

Represents comparison between original and regenerated triefact file with diff metadata.

- `canonical_triefact_path`: path to existing triefact in project
- `preview_triefact_path`: path to regenerated triefact in `.trie/preview/`
- `unified_diff`: text output from difflib.unified_diff
- `sync_result`: token usage and regeneration details from sync operation
<!-- trie:end -->
<!-- trie:section symbol=trie/diff_cmd:DiffResult fingerprint=86f0131d3b4847f6b1543e4465a0b65119ed8675475fa3fbbe50951b01784721 body_fp=17230e727c682ca495f456162a9f8b690ee328c4a826558aefee685a5b272231 source_ref=1e1ead40b2ec4f67fd8bdb317097295a702459f9 role=cli-interface -->
## `class DiffResult`

Contains the result of running `diff_project` with generated diffs and metadata.

- `files_skipped_no_budget`: count of files skipped due to budget or limit constraints
- `actual_cost_usd`: total cost in USD for all API calls made during diff generation
<!-- trie:end -->
<!-- trie:section symbol=trie/diff_cmd:diff_project fingerprint=bf8c5025e2d84ba1b505f054c1303f130e6589b23bd4a0d3c4abfc00ee48f9f2 body_fp=034e0c617add8d71ac56868ca0f5963562ea81265a30fd7fabb1c0eb2dba1d89 source_ref=1e1ead40b2ec4f67fd8bdb317097295a702459f9 role=orchestration -->
## `def diff_project( *, project_root: Path, config: Config, client: TrieClient, pricing: ModelPricing | None = None, budget_usd: float | None = None, limit: int | None = None, progress: ProgressCallback | None = None, store: Store | None = None, ) -> DiffResult`

Regenerates stale triefacts into `.trie/preview/` and produces unified diffs against current versions.

- `budget_usd`: stops processing when cumulative cost exceeds this amount
- `limit`: maximum number of files to process before stopping
- `progress`: callback for tracking file processing status
- Files with missing sources are skipped as they will be handled by reconciliation
<!-- trie:end -->