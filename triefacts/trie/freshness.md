---
trie_version: 0.2.0
source: trie/freshness.py
file_fingerprint: 4d7b60f6ccd58a5b820b98cbefcd04a0bcc4e018cddb3ed23c3f7908c6ef191a
last_synced_at: '2026-07-29T18:38:38Z'
description: 'Freshness gate: keep the graph + triefact tree current with respect
  to disk and HEAD.'
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
- kind: class
  qualified_name: trie/freshness:Stamp
  lines: 68-97
- kind: method
  qualified_name: trie/freshness:Stamp.to_json
  lines: 80-81
- kind: method
  qualified_name: trie/freshness:Stamp.from_json
  lines: 84-97
- kind: function
  qualified_name: trie/freshness:stamp_path
  lines: 100-102
- kind: function
  qualified_name: trie/freshness:read_stamp
  lines: 105-120
- kind: function
  qualified_name: trie/freshness:write_stamp
  lines: 123-133
- kind: function
  qualified_name: trie/freshness:stamp_graph_fresh
  lines: 136-156
- kind: function
  qualified_name: trie/freshness:scan_mtimes
  lines: 159-178
- kind: function
  qualified_name: trie/freshness:_require_git
  lines: 181-197
- kind: function
  qualified_name: trie/freshness:_mtimes_differ
  lines: 200-212
- kind: class
  qualified_name: trie/freshness:FreshnessResult
  lines: 216-232
- kind: function
  qualified_name: trie/freshness:ensure_fresh_before_turn
  lines: 235-262
- kind: function
  qualified_name: trie/freshness:ensure_fresh_after_turn
  lines: 265-287
- kind: function
  qualified_name: trie/freshness:_ensure_fresh
  lines: 290-392
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
<!-- trie:section symbol=trie/freshness:NotAGitRepoError fingerprint=09b365bfefd9d9b9a72c8c2e217dd31472401ec1d021a77332672cf7cbf20bf4 body_fp=6b5f69da7d66ef5182860f6e63b4efd037d2946c483b83586d68da875247c89c source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 role=change-detection -->
Exception raised when freshness operations are attempted outside a git repository.

- Enforces git requirement for HEAD-based drift detection during eval sessions
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:Stamp fingerprint=d1c55e5f7ac5b2b0f6e9a0f41a992c489b4bbd86c991d1319339a611fd2464a0 body_fp=31aec78ed4d0e13d91a146eabf1bcf7079550cdfc3034b86c450524ba4b34079 source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 role=change-detection -->
Records git HEAD SHA and file modification times to detect staleness between refresh cycles.

- `head`: commit SHA the graph was last built against
- `mtimes`: modification timestamps for in-scope source files at that moment
- `from_json`: returns None for malformed data, triggering full refresh
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:Stamp.to_json fingerprint=ce47e4e6daa8f0c4a250b20134274e9fbfd02aaf9ede1cb7bf37ca91c7410a99 body_fp=cb2d6f3559105752bf1a693a63a0fddf72be597e07acbb1387f5c67775e2323c source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 role=change-detection -->
Returns Stamp data as a JSON-serializable dictionary with 'head' and 'mtimes' keys.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:Stamp.from_json fingerprint=57f4bdcd743fa83a9a5d1df0b2bc7f61f2e798e6aad8a7a1a0c2241a0cf7b47f body_fp=f6b2ef409ce0083f22a240ec650c1b412f5ef7a90602797ffaf0fa8230585c23 source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 role=change-detection -->
Constructs a Stamp from parsed JSON, returning None for malformed data.

- Returns `None` when `head` is not a string or `mtimes` is not a dict
- Coerces numeric mtime values to floats, skipping invalid entries
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:stamp_path fingerprint=80a07e0294097d8da88cd2e3f54676211897796b445097ef0264fc4d82acc379 body_fp=7f7cb24633aa2e6e893ae32a226ff280d1635328c48aab0f9b833cebc285c173 source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 role=change-detection -->
Returns path to freshness stamp file at `.trie/graph.head` within project root.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:read_stamp fingerprint=21f5bc02e5c0a58c5b7dfbbdc12acc2571b335eb41f9160f8fe794c01380e1f9 body_fp=bbce59baf236941902988de4c42141c663e8d02a896d585218def54588ae1c99 source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 role=change-detection -->
Returns the recorded freshness stamp from disk, or None if missing or unreadable.

• All failure modes (missing file, malformed JSON, encoding errors) return None to force full refresh
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:write_stamp fingerprint=3191fba827b0de10432e3d06820239627570d6d361596c9d3abcd01940ccd5d4 body_fp=87f73609447123b2e8e27ba8ffd57a43601e1781ebcc01b9f57b50902f244540 source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 role=change-detection -->
Writes a freshness stamp to disk atomically using write-then-rename to prevent corruption.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:stamp_graph_fresh fingerprint=0b1a90b1065166768c438840845b30bd86294a57839d5061a4c56422fdf49f2e body_fp=d6c01664fad48134de3b2363c316ebd9ac0eba97fdc661a53ae3f8e6d567fb18 source_ref=0b739aacd3bb27bb550bd07e35677cebc4eb61ea role=persistence -->
Write a freshness stamp recording the current HEAD SHA and all in-scope file mtimes, preventing redundant graph rebuilds on the next turn hook.

- No-op when `project_root` is not a git repo or has no commits yet.
- Must not be called after `trie sync --file`; single-file scans do not justify stamping the full mtime map.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:scan_mtimes fingerprint=bcf189563877e5a915ba69067f3a2d7adf79275e2404d31d4c0507334bd2d3c3 body_fp=0faaea3f8ed87f14aa6f266f222cd44a8b189ca288e6f2f0e89120b38ad93cae source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 role=change-detection -->
Returns modification times for all in-scope source files as a dictionary mapping relative paths to mtime floats.

- Uses `os.stat` instead of reading file contents for performance
- Skips files outside the configured source root or that don't exist
- Runs on every turn boundary to detect file changes without full scans
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:_require_git fingerprint=166feea2e74bf1d5b8f9f739d158f1b9adadb6c127a9c2e746f8f4d11a5f0cb7 body_fp=77dc9ebfafe28c0852dcf11b7d1a9edc758729845904d60d5c40ab6b41818ad3 source_ref=c6ce1d9dad031d3054b2bceb7224cbf06f70da61 role=util -->
Returns the current git HEAD SHA or raises `NotAGitRepoError` if the project lacks git or commits.

- Raises `NotAGitRepoError` when the project is not in a git repository
- Raises `NotAGitRepoError` when the repository exists but has no commits
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:_mtimes_differ fingerprint=2389c54fdae5ee854c5b80798bf3c260d7ac0ce740a8ae1f711ad01fb1e9b551 body_fp=1cf8c54cb76f51d4b2bd082edc06c14f30944668415598c951facfd855dfb1be source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 role=change-detection -->
Returns True if two mtime dictionaries disagree on any file path or modification time.

- Detects new files (in `b` but not `a`), removed files (in `a` but not `b`), and modified files (different mtime)
- Uses exact float comparison since filesystem mtimes have fixed precision
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:FreshnessResult fingerprint=5eae57f3d9585a593370963bf41d436caa989cdfe075f5202a117eb5b585a08c body_fp=ef124e322f468b65e876374e37410b6113214b6e4729b2939c4e6c8d52e27ae8 source_ref=7e6722fd1b66993dbea88cf1540dccfc6de0e0b9 role=model -->
Immutable result of a freshness check containing rebuild status and metadata.

- `refreshed`: whether the graph was rebuilt during this check
- `reason`: why the check triggered (unchanged, head_moved, mtimes_moved, no_stamp, empty_store)
- `head`: git HEAD SHA at time of check
- `stale_files`: triefact files needing regeneration; populated on every outcome, including `unchanged`
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:ensure_fresh_before_turn fingerprint=9bd92efe7814f139c1e2681404fd205f803d06123991753a0fbdbc5696083712 body_fp=8fb56bcf9b7998c9e4a6f1244a406bd5abba49bc49c2978192a442fe38938398 source_ref=7e6722fd1b66993dbea88cf1540dccfc6de0e0b9 role=orchestration -->
Probe graph freshness at agent turn start, rebuilding the symbol graph from source if HEAD or mtimes have drifted; never calls the LLM.

- `project_root`: absolute path to the project checkout root
- `store`: symbol graph store to read from and potentially rebuild
- `progress`: optional callback receiving incremental scan progress
- Returns `FreshnessResult` with reason, HEAD SHA, and any pending stale files
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:ensure_fresh_after_turn fingerprint=48dd45a63bab3fe35535c3879c7eed58025b6d88f18182bf77cca144b797b7cf body_fp=9d55488d96454effed1ab475a2db8a436e0d9a986a622bf7edc2dd01440f14a0 source_ref=7e6722fd1b66993dbea88cf1540dccfc6de0e0b9 role=orchestration -->
Run a post-turn graph-sync sweep, catching files edited by the agent during the just-finished turn without calling the LLM.

- `progress`: optional callback for sync progress reporting; passed through to `_ensure_fresh`.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:_ensure_fresh fingerprint=5af148c97ba112e86af09a298434b51603110de685efa1434415b504d50939c1 body_fp=7d5fe16d9803f31c48e6588f8818b5d9532493193b953780b6ec265c60f5525a source_ref=7e6722fd1b66993dbea88cf1540dccfc6de0e0b9 role=orchestration -->
Core freshness gate implementation that rebuilds the graph when git HEAD or file mtimes change since last refresh.

- Checks git HEAD, stamp file, and current mtimes to determine refresh reason
- `unchanged` surfaces pending prose staleness from the activity DB and returns early without rebuilding
- `mtimes_moved` always marks stale files for later sync; `sync_prose` opt-in is removed
- All other reasons (`no_stamp`, `head_moved`, `empty_store`) rebuild graph without LLM and surface existing pending stale files
- Updates stamp file and pending stale list after successful refresh
<!-- trie:end -->