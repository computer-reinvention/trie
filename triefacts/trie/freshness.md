---
trie_version: 0.3.0
source: trie/freshness.py
file_fingerprint: 4d7b60f6ccd58a5b820b98cbefcd04a0bcc4e018cddb3ed23c3f7908c6ef191a
last_synced_at: '2026-08-02T21:19:30Z'
description: 'Freshness gate: keep the graph + triefact tree current with respect to disk and HEAD.'
defines:
- kind: module
  qualified_name: trie/freshness:__module__
  lines: 1-393
- kind: constant
  qualified_name: trie/freshness:STAMP_FILENAME
  lines: 53-53
- kind: class
  qualified_name: trie/freshness:NotAGitRepoError
  lines: 56-64
  signature: class NotAGitRepoError(RuntimeError)
- kind: class
  qualified_name: trie/freshness:Stamp
  lines: 68-97
  signature: class Stamp
- kind: method
  qualified_name: trie/freshness:Stamp.to_json
  lines: 80-81
  signature: def to_json(self) -> dict[str, Any]
- kind: method
  qualified_name: trie/freshness:Stamp.from_json
  lines: 84-97
  signature: 'def from_json(cls, raw: dict[str, Any]) -> Stamp | None'
- kind: function
  qualified_name: trie/freshness:stamp_path
  lines: 100-102
  signature: 'def stamp_path(project_root: Path) -> Path'
- kind: function
  qualified_name: trie/freshness:read_stamp
  lines: 105-120
  signature: 'def read_stamp(project_root: Path) -> Stamp | None'
- kind: function
  qualified_name: trie/freshness:write_stamp
  lines: 123-133
  signature: 'def write_stamp(project_root: Path, stamp: Stamp) -> None'
- kind: function
  qualified_name: trie/freshness:stamp_graph_fresh
  lines: 136-156
  signature: 'def stamp_graph_fresh(project_root: Path, config: Config) -> None'
- kind: function
  qualified_name: trie/freshness:scan_mtimes
  lines: 159-178
  signature: 'def scan_mtimes(project_root: Path, config: Config) -> dict[str, float]'
- kind: function
  qualified_name: trie/freshness:_require_git
  lines: 181-197
  signature: 'def _require_git(project_root: Path) -> str'
- kind: function
  qualified_name: trie/freshness:_mtimes_differ
  lines: 200-212
  signature: 'def _mtimes_differ(a: dict[str, float], b: dict[str, float]) -> bool'
- kind: class
  qualified_name: trie/freshness:FreshnessResult
  lines: 216-232
  signature: class FreshnessResult
- kind: function
  qualified_name: trie/freshness:ensure_fresh_before_turn
  lines: 235-262
  signature: 'def ensure_fresh_before_turn( *, project_root: Path, config: Config, store: Store, progress: ProgressCallback | None = None, ) -> FreshnessResult'
- kind: function
  qualified_name: trie/freshness:ensure_fresh_after_turn
  lines: 265-287
  signature: 'def ensure_fresh_after_turn( *, project_root: Path, config: Config, store: Store, progress: ProgressCallback | None = None, ) -> FreshnessResult'
- kind: function
  qualified_name: trie/freshness:_ensure_fresh
  lines: 290-392
  signature: 'def _ensure_fresh( *, project_root: Path, config: Config, store: Store, progress: ProgressCallback | None, trigger: str, ) -> FreshnessResult'
incoming_refs: 29
outgoing_refs: 11
---
<!-- trie:section symbol=trie/freshness:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=d60cccb6d7672a73cd632cf51c0697cfac932f1e9143b45a73e72d8dcf9c0604 source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 role=change-detection -->
Freshness gate module that keeps the graph and triefact tree current with respect to disk and git HEAD.

- `ensure_fresh_before_turn()`: cheap probe at turn start catching HEAD moves and inter-turn edits
- `ensure_fresh_after_turn()`: filesystem sweep at turn end catching in-turn agent edits
- `Stamp`: records git HEAD SHA and file mtimes at last refresh in `.trie/graph.head`
- `NotAGitRepoError`: raised when freshness gate runs outside a git repository
- `FreshnessResult`: outcome carrying refresh status, reason, and incremental result
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:STAMP_FILENAME fingerprint=aac8741000f280bd63bac926ffebec9cbf71b4495987943f78ec277e1b576db7 body_fp=c62d39f17835acdc2f2d1013bc8be96ed181402e6d191a1477a1bf3db7d007a5 source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 role=change-detection -->
Filename for the freshness stamp stored under `.trie/`.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:NotAGitRepoError fingerprint=09b365bfefd9d9b9a72c8c2e217dd31472401ec1d021a77332672cf7cbf20bf4 body_fp=99c6d804d2997b69c9aeefb8c79553505530c7e4c61288fb54e43da96a944fe7 source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 role=change-detection -->
## `class NotAGitRepoError(RuntimeError)`

Exception raised when freshness operations are attempted outside a git repository.

- Enforces git requirement for HEAD-based drift detection during eval sessions
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:Stamp fingerprint=d1c55e5f7ac5b2b0f6e9a0f41a992c489b4bbd86c991d1319339a611fd2464a0 body_fp=77546c743849d781da4ea708096ec060b26c0f9778ec4717724ad4f363942bc3 source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 role=change-detection -->
## `class Stamp`

Records git HEAD SHA and file modification times to detect staleness between refresh cycles.

- `head`: commit SHA the graph was last built against
- `mtimes`: modification timestamps for in-scope source files at that moment
- `from_json`: returns None for malformed data, triggering full refresh
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:Stamp.to_json fingerprint=ce47e4e6daa8f0c4a250b20134274e9fbfd02aaf9ede1cb7bf37ca91c7410a99 body_fp=54eaf1dbb822f9c95b9e3089d731b879edea40825bdf1385a0af4adecf848dd3 source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 role=change-detection -->
## `def to_json(self) -> dict[str, Any]`

Returns Stamp data as a JSON-serializable dictionary with 'head' and 'mtimes' keys.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:Stamp.from_json fingerprint=57f4bdcd743fa83a9a5d1df0b2bc7f61f2e798e6aad8a7a1a0c2241a0cf7b47f body_fp=17b24e71d3bf84776ca936d298926c81ceef68bee932bc06b133f129f18e0ac9 source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 role=change-detection -->
## `def from_json(cls, raw: dict[str, Any]) -> Stamp | None`

Constructs a Stamp from parsed JSON, returning None for malformed data.

- Returns `None` when `head` is not a string or `mtimes` is not a dict
- Coerces numeric mtime values to floats, skipping invalid entries
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:stamp_path fingerprint=80a07e0294097d8da88cd2e3f54676211897796b445097ef0264fc4d82acc379 body_fp=96a7b18f2f935bf04eeaf54abdb222b3b1267a61e1c6e32f80a2bde49b7f6dfa source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 role=change-detection -->
## `def stamp_path(project_root: Path) -> Path`

Returns path to freshness stamp file at `.trie/graph.head` within project root.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:read_stamp fingerprint=21f5bc02e5c0a58c5b7dfbbdc12acc2571b335eb41f9160f8fe794c01380e1f9 body_fp=c1fb6cf7184b250770787550b825816f3b8f4fb23d9b2b13dd9384c2bce7a7d9 source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 role=change-detection -->
## `def read_stamp(project_root: Path) -> Stamp | None`

Returns the recorded freshness stamp from disk, or None if missing or unreadable.

• All failure modes (missing file, malformed JSON, encoding errors) return None to force full refresh
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:write_stamp fingerprint=3191fba827b0de10432e3d06820239627570d6d361596c9d3abcd01940ccd5d4 body_fp=bc540096141a58ae9dd182bc8086e88edcd3ada966e5ab7f43581d0ef1bd6ed9 source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 role=change-detection -->
## `def write_stamp(project_root: Path, stamp: Stamp) -> None`

Writes a freshness stamp to disk atomically using write-then-rename to prevent corruption.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:stamp_graph_fresh fingerprint=0b1a90b1065166768c438840845b30bd86294a57839d5061a4c56422fdf49f2e body_fp=f4c0acf50558ee09e32b7042a5fb8641cb3c0fd0c5f5860acc578f557ecb9227 source_ref=0b739aacd3bb27bb550bd07e35677cebc4eb61ea role=persistence -->
## `def stamp_graph_fresh(project_root: Path, config: Config) -> None`

Write a freshness stamp recording the current HEAD SHA and all in-scope file mtimes, preventing redundant graph rebuilds on the next turn hook.

- No-op when `project_root` is not a git repo or has no commits yet.
- Must not be called after `trie sync --file`; single-file scans do not justify stamping the full mtime map.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:scan_mtimes fingerprint=bcf189563877e5a915ba69067f3a2d7adf79275e2404d31d4c0507334bd2d3c3 body_fp=b750ea98f2ca63a0fa9934620bbb01a7c0dc549ec08ee4576061277f088481c5 source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 role=change-detection -->
## `def scan_mtimes(project_root: Path, config: Config) -> dict[str, float]`

Returns modification times for all in-scope source files as a dictionary mapping relative paths to mtime floats.

- Uses `os.stat` instead of reading file contents for performance
- Skips files outside the configured source root or that don't exist
- Runs on every turn boundary to detect file changes without full scans
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:_require_git fingerprint=166feea2e74bf1d5b8f9f739d158f1b9adadb6c127a9c2e746f8f4d11a5f0cb7 body_fp=8480d8e817386da0bf487f1e49d03238aaacf2336e5f7947723734c983f615d3 source_ref=c6ce1d9dad031d3054b2bceb7224cbf06f70da61 role=util -->
## `def _require_git(project_root: Path) -> str`

Returns the current git HEAD SHA or raises `NotAGitRepoError` if the project lacks git or commits.

- Raises `NotAGitRepoError` when the project is not in a git repository
- Raises `NotAGitRepoError` when the repository exists but has no commits
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:_mtimes_differ fingerprint=2389c54fdae5ee854c5b80798bf3c260d7ac0ce740a8ae1f711ad01fb1e9b551 body_fp=f6db9a64f57a6734ddc84016216eb81732d281027d5ffa2a8b97eeaff1d73d46 source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 role=change-detection -->
## `def _mtimes_differ(a: dict[str, float], b: dict[str, float]) -> bool`

Returns True if two mtime dictionaries disagree on any file path or modification time.

- Detects new files (in `b` but not `a`), removed files (in `a` but not `b`), and modified files (different mtime)
- Uses exact float comparison since filesystem mtimes have fixed precision
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:FreshnessResult fingerprint=5eae57f3d9585a593370963bf41d436caa989cdfe075f5202a117eb5b585a08c body_fp=75a123de5cf75f4846b32e036034d7346900d8814ffb2bb8e88d53fad638dedb source_ref=7e6722fd1b66993dbea88cf1540dccfc6de0e0b9 role=model -->
## `class FreshnessResult`

Immutable result of a freshness check containing rebuild status and metadata.

- `refreshed`: whether the graph was rebuilt during this check
- `reason`: why the check triggered (unchanged, head_moved, mtimes_moved, no_stamp, empty_store)
- `head`: git HEAD SHA at time of check
- `stale_files`: triefact files needing regeneration; populated on every outcome, including `unchanged`
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:ensure_fresh_before_turn fingerprint=9bd92efe7814f139c1e2681404fd205f803d06123991753a0fbdbc5696083712 body_fp=3d6bd6dc709e2a00c27dce64577e51dc126956609a103d767fb4ddb2355f92a8 source_ref=7e6722fd1b66993dbea88cf1540dccfc6de0e0b9 role=orchestration -->
## `def ensure_fresh_before_turn( *, project_root: Path, config: Config, store: Store, progress: ProgressCallback | None = None, ) -> FreshnessResult`

Probe graph freshness at agent turn start, rebuilding the symbol graph from source if HEAD or mtimes have drifted; never calls the LLM.

- `project_root`: absolute path to the project checkout root
- `store`: symbol graph store to read from and potentially rebuild
- `progress`: optional callback receiving incremental scan progress
- Returns `FreshnessResult` with reason, HEAD SHA, and any pending stale files
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:ensure_fresh_after_turn fingerprint=48dd45a63bab3fe35535c3879c7eed58025b6d88f18182bf77cca144b797b7cf body_fp=659984012ae92568c0bd5718d907431a9a4d75ec15a1406411a285ea18bc4674 source_ref=7e6722fd1b66993dbea88cf1540dccfc6de0e0b9 role=orchestration -->
## `def ensure_fresh_after_turn( *, project_root: Path, config: Config, store: Store, progress: ProgressCallback | None = None, ) -> FreshnessResult`

Run a post-turn graph-sync sweep, catching files edited by the agent during the just-finished turn without calling the LLM.

- `progress`: optional callback for sync progress reporting; passed through to `_ensure_fresh`.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:_ensure_fresh fingerprint=5af148c97ba112e86af09a298434b51603110de685efa1434415b504d50939c1 body_fp=879efbe8e47771686a6833731bb976131bb43990d849397a5707b92b37c8476f source_ref=0b739aacd3bb27bb550bd07e35677cebc4eb61ea role=orchestration -->
## `def _ensure_fresh( *, project_root: Path, config: Config, store: Store, progress: ProgressCallback | None, trigger: str, ) -> FreshnessResult`

Core freshness gate implementation that rebuilds the graph when git HEAD or file mtimes change since last refresh.

- Checks git HEAD, stamp file, and current mtimes to determine refresh reason
- `unchanged` surfaces pending prose staleness from the activity DB and returns early without rebuilding
- `mtimes_moved` always marks stale files for later sync; `sync_prose` opt-in is removed
- All other reasons (`no_stamp`, `head_moved`, `empty_store`) rebuild graph without LLM and surface existing pending stale files
- Updates stamp file and pending stale list after successful refresh
<!-- trie:end -->