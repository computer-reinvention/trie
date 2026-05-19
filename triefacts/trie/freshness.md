---
trie_version: 0.1.2
source: trie/freshness.py
file_fingerprint: 6ba5cf8f15f23143c865e5e361d1a37583fea064fb26b107a3f97bb650a25b76
last_synced_at: '2026-05-19T10:40:39Z'
description: 'Freshness gate: keep the graph + triefact tree current with respect
  to disk and HEAD.'
defines:
- kind: module
  qualified_name: trie/freshness:__module__
  lines: 1-348
- kind: constant
  qualified_name: trie/freshness:STAMP_FILENAME
  lines: 49-49
- kind: class
  qualified_name: trie/freshness:NotAGitRepoError
  lines: 52-60
- kind: class
  qualified_name: trie/freshness:Stamp
  lines: 64-93
- kind: method
  qualified_name: trie/freshness:Stamp.to_json
  lines: 76-77
- kind: method
  qualified_name: trie/freshness:Stamp.from_json
  lines: 80-93
- kind: function
  qualified_name: trie/freshness:stamp_path
  lines: 96-98
- kind: function
  qualified_name: trie/freshness:read_stamp
  lines: 101-116
- kind: function
  qualified_name: trie/freshness:write_stamp
  lines: 119-129
- kind: function
  qualified_name: trie/freshness:scan_mtimes
  lines: 132-151
- kind: function
  qualified_name: trie/freshness:_require_git
  lines: 154-170
- kind: function
  qualified_name: trie/freshness:_mtimes_differ
  lines: 173-185
- kind: class
  qualified_name: trie/freshness:FreshnessResult
  lines: 189-201
- kind: function
  qualified_name: trie/freshness:ensure_fresh_before_turn
  lines: 204-233
- kind: function
  qualified_name: trie/freshness:ensure_fresh_after_turn
  lines: 236-263
- kind: function
  qualified_name: trie/freshness:_ensure_fresh
  lines: 266-347
incoming_refs: 23
outgoing_refs: 7
---
<!-- trie:section symbol=trie/freshness:NotAGitRepoError fingerprint=09b365bfefd9d9b9a72c8c2e217dd31472401ec1d021a77332672cf7cbf20bf4 body_fp=424ffac6ee9e652161e4317f2d53955d99f30d80ee331e91014c6501eaf4d9d4 source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `class NotAGitRepoError(RuntimeError)`

Raised when the freshness gate is invoked outside a git repository.
<!-- trie:end -->

<!-- trie:section symbol=trie/freshness:Stamp fingerprint=d1c55e5f7ac5b2b0f6e9a0f41a992c489b4bbd86c991d1319339a611fd2464a0 body_fp=b49c24477ff0c57caf283c666d38e7602ec86de77cb1fdcec072b4402b07bc9a source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `Stamp(head: str, mtimes: dict[str, float])`

Immutable record of one graph refresh: the git HEAD SHA and per-file mtimes at that moment.

- **`head`**: commit SHA the graph was built against.
- **`mtimes`**: maps source-relative path → `os.stat` mtime for every in-scope file.
- **`from_json`**: returns `None` for malformed input; caller treats that as missing stamp.
<!-- trie:end -->

<!-- trie:section symbol=trie/freshness:Stamp.to_json fingerprint=ce47e4e6daa8f0c4a250b20134274e9fbfd02aaf9ede1cb7bf37ca91c7410a99 body_fp=c9e88634a681f69714b18e1c4355aa2e3e46dfd13cb038d83d5f5f498be7eb56 source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `Stamp.to_json(self) -> dict[str, Any]`

Serialize the stamp to a JSON-compatible dict.
<!-- trie:end -->

<!-- trie:section symbol=trie/freshness:Stamp.from_json fingerprint=57f4bdcd743fa83a9a5d1df0b2bc7f61f2e798e6aad8a7a1a0c2241a0cf7b47f body_fp=0af8ccf48e68ecb45761f3e008d32083438de112f72c9c7569b99372017c2048 source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `Stamp.from_json(cls, raw: dict[str, Any]) -> Stamp | None`

Construct a `Stamp` from a parsed JSON dict, returning `None` if the dict is malformed or missing required fields.

- `raw`: must contain `"head"` (str) and `"mtimes"` (dict) keys.
- Returns `None` on schema mismatch; caller treats this identically to a missing stamp.
<!-- trie:end -->

<!-- trie:section symbol=trie/freshness:stamp_path fingerprint=80a07e0294097d8da88cd2e3f54676211897796b445097ef0264fc4d82acc379 body_fp=eaf2eff5df02c47b910f43111dbe1b2e1580138cf2866253aa31f1f01b3809c7 source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `stamp_path(project_root: Path) -> Path`

Return the conventional `.trie/graph.head` stamp file path for the given project root.
<!-- trie:end -->

<!-- trie:section symbol=trie/freshness:read_stamp fingerprint=21f5bc02e5c0a58c5b7dfbbdc12acc2571b335eb41f9160f8fe794c01380e1f9 body_fp=42d40f3f6e5b50bae55b3e57a9920e893d25a8501b8bac23402f6c4bf99bb602 source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `read_stamp(project_root: Path) -> Stamp | None`

Return the recorded stamp, or `None` if the stamp file is missing or unreadable.

- Any failure (missing file, bad JSON, wrong schema) collapses to `None`, triggering a full refresh.
<!-- trie:end -->

<!-- trie:section symbol=trie/freshness:write_stamp fingerprint=3191fba827b0de10432e3d06820239627570d6d361596c9d3abcd01940ccd5d4 body_fp=99a85fd2b22443cc799b5d3128c229b2515e8be8af3dd1098c3e230056f1fc04 source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `write_stamp(project_root: Path, stamp: Stamp) -> None`

Write a `Stamp` to disk atomically using a write-then-rename strategy.

- Prevents partial writes from leaving a corrupt stamp on disk.
<!-- trie:end -->

<!-- trie:section symbol=trie/freshness:scan_mtimes fingerprint=bcf189563877e5a915ba69067f3a2d7adf79275e2404d31d4c0507334bd2d3c3 body_fp=54866cb839f41e5ce16896aed1d37b90715550389a0d8ab5bf30a5d7528a0237 source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `scan_mtimes(project_root: Path, config: Config) -> dict[str, float]`

Return `{source-rel-path: mtime}` for every in-scope file under the configured source root.

- Uses `os.stat`, not file reads — cheap for the common no-change path.
- Files not relative to `source_root` or missing at stat time are silently skipped.
<!-- trie:end -->

<!-- trie:section symbol=trie/freshness:_require_git fingerprint=166feea2e74bf1d5b8f9f739d158f1b9adadb6c127a9c2e746f8f4d11a5f0cb7 body_fp=96ecd5710318f4d69574545f822f47033718185b0a13d6c0bdcd13f90a907e7e source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `_require_git(project_root: Path) -> str`

Return the current HEAD SHA, raising `NotAGitRepoError` if the directory is not a git repo or has no commits.
<!-- trie:end -->

<!-- trie:section symbol=trie/freshness:_mtimes_differ fingerprint=2389c54fdae5ee854c5b80798bf3c260d7ac0ce740a8ae1f711ad01fb1e9b551 body_fp=21747347cdbbc3e66c14f02ac61c3008f8bceaa2225adf75cf04cbaca2584ea9 source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `_mtimes_differ(a: dict[str, float], b: dict[str, float]) -> bool`

Return `True` if two mtime maps disagree on any key or value.

- Detects additions, removals, and modifications as drift.
- Uses exact float equality; safe because values come from `os.stat` on the same filesystem.
<!-- trie:end -->

<!-- trie:section symbol=trie/freshness:FreshnessResult fingerprint=8af5e0b2de5104af0d7073dfc753b7f6805d4e4c4ba1333149d51e6ef4a7f2a5 body_fp=31df6453a2d392a9fff89e1afb44cb30649d8ec048752f6fed451ace6d4bd805 source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `FreshnessResult`

Frozen dataclass capturing the outcome of an `ensure_fresh_before_turn` or `ensure_fresh_after_turn` call.

- `refreshed`: `True` only when `run_incremental` or `scan_project` was actually invoked.
- `reason`: one of `no_stamp`, `head_moved`, `mtimes_moved`, `unchanged`.
- `incremental`: populated only on `mtimes_moved`; `None` for all other reasons.
<!-- trie:end -->

<!-- trie:section symbol=trie/freshness:ensure_fresh_before_turn fingerprint=290aa05b8d0d6759bf13117ee5bb21bae127af9708276c98d21a06dfabb4548c body_fp=64fcd48dcd7ca438a8b5d557ec92d4f37ede941ab1fe6215b77797e1035ea249 source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `ensure_fresh_before_turn(*, project_root: Path, config: Config, store: Store, client: ModelClient, progress: ProgressCallback | None = None) -> FreshnessResult`

Probe graph freshness at agent turn start, refreshing only when HEAD or mtimes have drifted.

- `refreshed=False` when nothing changed; no I/O beyond stat and stamp read.
- `no_stamp`/`head_moved`: rebuilds graph via `scan_project`, skips LLM.
- `mtimes_moved`: runs full `run_incremental` including LLM-backed prose sync.
- Raises `NotAGitRepoError` if the project root is not a git repository.
<!-- trie:end -->

<!-- trie:section symbol=trie/freshness:ensure_fresh_after_turn fingerprint=2a5af9c6a7ef7da3ef3df8784b3650da6731f86f613bc48facb72b3d8bc0d0dc body_fp=dff1d7c09cb73a585b1e4df4efbe643b8a928683dafd4d5bf5b0efb2f5275365 source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `ensure_fresh_after_turn(*, project_root: Path, config: Config, store: Store, client: ModelClient, progress: ProgressCallback | None = None) -> FreshnessResult`

Run the HEAD/mtime freshness check after an agent turn completes, picking up files the agent just edited.

- Delegates entirely to `_ensure_fresh`; see `ensure_fresh_before_turn` for branch semantics.
<!-- trie:end -->

<!-- trie:section symbol=trie/freshness:_ensure_fresh fingerprint=9cd5bb51c0c2f61fcc7445e251bbafefc7fa2745eb3f050ba41b5e55b4df903c body_fp=c655cd64007734d33d548f1b674fa84fb8b6f77ba5a5f2fc4a449d21755bd7db source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `_ensure_fresh(*, project_root, config, store, client, progress, trigger) -> FreshnessResult`

Shared implementation backing both `ensure_fresh_before_turn` and `ensure_fresh_after_turn`; branches on stamp state to decide whether and how to refresh.

- `trigger`: telemetry label only; does not affect logic.
- `no_stamp` / `head_moved`: rebuilds graph via `scan_project`, no LLM.
- `mtimes_moved`: runs full `run_incremental` (graph + triefact prose, LLM as needed).
- `unchanged`: returns immediately without I/O or LLM calls.
<!-- trie:end -->

<!-- trie:section symbol=trie/freshness:STAMP_FILENAME fingerprint=aac8741000f280bd63bac926ffebec9cbf71b4495987943f78ec277e1b576db7 body_fp=9f17a4fdc4005fca371706a1454b4d629fda232eedc4ed20c66321a0ebd87100 source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `STAMP_FILENAME = "graph.head"`

Filename of the per-checkout freshness stamp stored under `.trie/`.
<!-- trie:end -->

<!-- trie:section symbol=trie/freshness:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=f7bee85abbb8ccbe9217945fce1258fb1b42256711dfa06f94a2538e0f9c54cc source_ref=f0e0b9f3488673b79d087d3bee139798c331d329 -->
## `freshness`

Keep the dependency graph and triefact tree current with respect to disk and HEAD across agent turns and `git pull` events.

- `ensure_fresh_before_turn`: cheap probe at turn start; detects HEAD or mtime drift.
- `ensure_fresh_after_turn`: sweep at turn end; catches files the agent just edited.
- Both delegate to `_ensure_fresh`, which calls `run_incremental` only for local edits (`mtimes_moved`); other stale states rebuild the graph without invoking the LLM.
- Stamp file at `.trie/graph.head` records HEAD SHA and per-file mtimes; missing or malformed stamp triggers a full refresh.
<!-- trie:end -->