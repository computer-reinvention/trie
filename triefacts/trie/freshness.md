---
trie_version: 0.1.5
source: trie/freshness.py
file_fingerprint: 2cfbe2407b5c12abfef2c8810d2e08554beed0757be02240a4f1dd954b355b9a
last_synced_at: '2026-05-28T01:38:43Z'
description: 'Freshness gate: keep the graph + triefact tree current with respect
  to disk and HEAD.'
defines:
- kind: module
  qualified_name: trie/freshness:__module__
  lines: 1-353
- kind: constant
  qualified_name: trie/freshness:STAMP_FILENAME
  lines: 50-50
- kind: class
  qualified_name: trie/freshness:NotAGitRepoError
  lines: 53-61
- kind: class
  qualified_name: trie/freshness:Stamp
  lines: 65-94
- kind: method
  qualified_name: trie/freshness:Stamp.to_json
  lines: 77-78
- kind: method
  qualified_name: trie/freshness:Stamp.from_json
  lines: 81-94
- kind: function
  qualified_name: trie/freshness:stamp_path
  lines: 97-99
- kind: function
  qualified_name: trie/freshness:read_stamp
  lines: 102-117
- kind: function
  qualified_name: trie/freshness:write_stamp
  lines: 120-130
- kind: function
  qualified_name: trie/freshness:scan_mtimes
  lines: 133-152
- kind: function
  qualified_name: trie/freshness:_require_git
  lines: 155-171
- kind: function
  qualified_name: trie/freshness:_mtimes_differ
  lines: 174-186
- kind: class
  qualified_name: trie/freshness:FreshnessResult
  lines: 190-202
- kind: function
  qualified_name: trie/freshness:ensure_fresh_before_turn
  lines: 205-234
- kind: function
  qualified_name: trie/freshness:ensure_fresh_after_turn
  lines: 237-264
- kind: function
  qualified_name: trie/freshness:_ensure_fresh
  lines: 267-352
incoming_refs: 23
outgoing_refs: 8
---
<!-- trie:section symbol=trie/freshness:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=a88d62b97e640fee727338aacaedfc5767175a396e71f789ca7fb05f2d82c1c0 source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `trie/freshness`

Keep the graph and triefact tree current with respect to disk and HEAD between agent turns and sessions.

- `ensure_fresh_before_turn`: cheap probe at turn start; detects pulled commits or inter-turn edits
- `ensure_fresh_after_turn`: sweep at turn end; detects files the agent just edited
- `run_incremental` (LLM path) fires only on `mtimes_moved`; `no_stamp`/`head_moved` rebuild graph cheaply without LLM
- Stamp file at `.trie/graph.head` records HEAD SHA and per-file mtimes; missing or malformed stamp forces full refresh
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:STAMP_FILENAME fingerprint=aac8741000f280bd63bac926ffebec9cbf71b4495987943f78ec277e1b576db7 body_fp=fe66fc96fc1c7365d6d20ebbff4990c172e5b5ef9deea143d2794c20f95f6fdb source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `STAMP_FILENAME = "graph.head"`

Filename of the stamp file written under `.trie/`.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:NotAGitRepoError fingerprint=09b365bfefd9d9b9a72c8c2e217dd31472401ec1d021a77332672cf7cbf20bf4 body_fp=7d5beda7fc1aba8e970cee002c19cb915ce102f4687e1cfb50965b417665db9f source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `NotAGitRepoError`

Raised by the freshness gate when the project root is not inside a git repository.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:Stamp fingerprint=d1c55e5f7ac5b2b0f6e9a0f41a992c489b4bbd86c991d1319339a611fd2464a0 body_fp=769e7ce86ee5d7e0c1bf02d3ac377d6dc82163758ae26adbbc421986e8c6450e source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `Stamp(head: str, mtimes: dict[str, float])`

Frozen dataclass recording the git HEAD SHA and per-file mtimes captured at the last graph refresh.

- `head`: commit SHA the graph was built against
- `mtimes`: `{source-rel-path: mtime}` for every in-scope file at refresh time

## `Stamp.to_json(self) -> dict[str, Any]`

Serialise a `Stamp` to a JSON-compatible dict.

## `Stamp.from_json(cls, raw: dict[str, Any]) -> Stamp | None`

Construct a `Stamp` from a parsed JSON dict on the class, returning `None` if the dict is malformed or missing required fields.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:Stamp.to_json fingerprint=ce47e4e6daa8f0c4a250b20134274e9fbfd02aaf9ede1cb7bf37ca91c7410a99 body_fp=3bdcf7da56a3424951ceb38a1546c05ebada7ce91db2ba696d3d7efcac6b7f23 source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `Stamp.to_json(self) -> dict[str, Any]`

Serialize a `Stamp` to a JSON-compatible dict.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:Stamp.from_json fingerprint=57f4bdcd743fa83a9a5d1df0b2bc7f61f2e798e6aad8a7a1a0c2241a0cf7b47f body_fp=99efa29c041eeb3899188da6f40e44fe741342231c065255ebcecf02239e5db3 source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `Stamp.from_json(cls, raw: dict[str, Any]) -> Stamp | None`

Construct a `Stamp` from a parsed JSON dict, returning `None` on any malformed input.

- `raw`: must contain `"head"` (str) and `"mtimes"` (dict); any other shape returns `None`.
- Numeric mtime values are coerced to `float`; non-numeric entries are silently dropped.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:stamp_path fingerprint=80a07e0294097d8da88cd2e3f54676211897796b445097ef0264fc4d82acc379 body_fp=eaf2eff5df02c47b910f43111dbe1b2e1580138cf2866253aa31f1f01b3809c7 source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `stamp_path(project_root: Path) -> Path`

Return the conventional `.trie/graph.head` stamp file path for the given project root.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:read_stamp fingerprint=21f5bc02e5c0a58c5b7dfbbdc12acc2571b335eb41f9160f8fe794c01380e1f9 body_fp=c9cd68728d9322c6e7185bedacfb57f37ec01c23bcc93a1a529ce217083806db source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `read_stamp(project_root: Path) -> Stamp | None`

Read and parse the stamp file from `project_root`, returning `None` on any failure.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:write_stamp fingerprint=3191fba827b0de10432e3d06820239627570d6d361596c9d3abcd01940ccd5d4 body_fp=91bb78d577302298757fe5e397d185111993bdeb881cbeb6c79c1c57a2037bf9 source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `write_stamp(project_root: Path, stamp: Stamp) -> None`

Persist a `Stamp` to `.trie/graph.head` atomically via write-then-rename.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:scan_mtimes fingerprint=bcf189563877e5a915ba69067f3a2d7adf79275e2404d31d4c0507334bd2d3c3 body_fp=a852a927b3a880af2f714995197d5a4003aedb0adde4b03cf9b63ca306d4873d source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `scan_mtimes(project_root: Path, config: Config) -> dict[str, float]`

Return `{source-relative-path: mtime}` for every in-scope file under the configured source root, using `os.stat` without reading file bytes.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:_require_git fingerprint=166feea2e74bf1d5b8f9f739d158f1b9adadb6c127a9c2e746f8f4d11a5f0cb7 body_fp=03c8f5c17149eb91da6dcf5d7a0eef5cf7368729b21205f00d1c1159551efe1d source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `_require_git(project_root: Path) -> str`

Return the current HEAD SHA, or raise `NotAGitRepoError` if the path is not a git repo or has no commits.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:_mtimes_differ fingerprint=2389c54fdae5ee854c5b80798bf3c260d7ac0ce740a8ae1f711ad01fb1e9b551 body_fp=4e8841630d9d414d82598e3a9955dc0789220c5159d4b562ccb4de364f56424b source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `_mtimes_differ(a: dict[str, float], b: dict[str, float]) -> bool`

Return `True` if two mtime maps differ by any key or value, treating additions, deletions, and modifications as drift.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:FreshnessResult fingerprint=8af5e0b2de5104af0d7073dfc753b7f6805d4e4c4ba1333149d51e6ef4a7f2a5 body_fp=f886a41e37122f9f4328a02589ee09b24826e3100c5023aa5c53ee2f8637da0d source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `FreshnessResult`

Immutable outcome record returned by `ensure_fresh_before_turn` and `ensure_fresh_after_turn`.

- `refreshed`: `True` only when `run_incremental` or `scan_project` was invoked.
- `reason`: one of `no_stamp`, `head_moved`, `mtimes_moved`, `unchanged`.
- `head`: git SHA at the time of the check.
- `incremental`: populated only on `mtimes_moved` refresh; `None` otherwise.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:ensure_fresh_before_turn fingerprint=290aa05b8d0d6759bf13117ee5bb21bae127af9708276c98d21a06dfabb4548c body_fp=3f565d4d4bf3409c26fa258b2ed17f6ef0af7efc6c3cb85b8ada6c9b9aef5f02 source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `ensure_fresh_before_turn(*, project_root, config, store, client, progress=None) -> FreshnessResult`

Probe graph freshness at agent turn start, triggering incremental sync only when HEAD or mtimes have drifted.

- `reason="no_stamp"` or `"head_moved"`: rebuilds graph via `scan_project`, no LLM spend.
- `reason="mtimes_moved"`: runs full `run_incremental` including LLM triefact sync.
- `reason="unchanged"`: returns immediately without touching graph or store.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:ensure_fresh_after_turn fingerprint=2a5af9c6a7ef7da3ef3df8784b3650da6731f86f613bc48facb72b3d8bc0d0dc body_fp=ec59d848e476febd83da24aaecf4d0fb1d40ef5e031ba4084361b77e43d59aa6 source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `ensure_fresh_after_turn(*, project_root: Path, config: Config, store: Store, client: ModelClient, progress: ProgressCallback | None = None) -> FreshnessResult`

Run a HEAD/mtime freshness check after an agent turn, capturing files the agent just edited.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:_ensure_fresh fingerprint=0508de7da5c974aebbcd23b7cbea9f212f5a8eaeae4c1f66c578d209397cbd64 body_fp=7cdf7cf321eeedb98ace64b79db552b145701ec746b154d8109b472b91711055 source_ref=b09ef7b11df3129624aefe1f6eb0bbde27cb055a -->
## `_ensure_fresh(*, project_root, config, store, client, progress, trigger) -> FreshnessResult`

Determine staleness reason and run the appropriate refresh, writing an updated stamp on any change.

- `trigger`: telemetry label only; does not affect branching logic.
- `no_stamp` / `head_moved`: runs `scan_project` only; LLM never invoked; calls `backfill_section_records` if section records are missing.
- `mtimes_moved`: runs `run_incremental`, which may invoke the LLM for prose regen.
- `unchanged`: calls `backfill_section_records` if section records are missing, then returns without touching the graph or stamp.
<!-- trie:end -->