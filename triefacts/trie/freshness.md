---
trie_version: 0.1.9
source: trie/freshness.py
file_fingerprint: 6667a9d9073e66122b06cf34d53d4644f1e6880d1097dfc5cc726682e13e9bca
last_synced_at: '2026-07-25T00:07:15Z'
description: 'Freshness gate: keep the graph + triefact tree current with respect
  to disk and HEAD.'
defines:
- kind: module
  qualified_name: trie/freshness:__module__
  lines: 1-397
- kind: constant
  qualified_name: trie/freshness:STAMP_FILENAME
  lines: 55-55
- kind: class
  qualified_name: trie/freshness:NotAGitRepoError
  lines: 58-66
- kind: class
  qualified_name: trie/freshness:Stamp
  lines: 70-99
- kind: method
  qualified_name: trie/freshness:Stamp.to_json
  lines: 82-83
- kind: method
  qualified_name: trie/freshness:Stamp.from_json
  lines: 86-99
- kind: function
  qualified_name: trie/freshness:stamp_path
  lines: 102-104
- kind: function
  qualified_name: trie/freshness:read_stamp
  lines: 107-122
- kind: function
  qualified_name: trie/freshness:write_stamp
  lines: 125-135
- kind: function
  qualified_name: trie/freshness:scan_mtimes
  lines: 138-157
- kind: function
  qualified_name: trie/freshness:_require_git
  lines: 160-176
- kind: function
  qualified_name: trie/freshness:_mtimes_differ
  lines: 179-191
- kind: class
  qualified_name: trie/freshness:FreshnessResult
  lines: 195-213
- kind: function
  qualified_name: trie/freshness:ensure_fresh_before_turn
  lines: 216-247
- kind: function
  qualified_name: trie/freshness:ensure_fresh_after_turn
  lines: 250-278
- kind: function
  qualified_name: trie/freshness:_ensure_fresh
  lines: 281-396
incoming_refs: 24
outgoing_refs: 10
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
<!-- trie:section symbol=trie/freshness:FreshnessResult fingerprint=816abdf4f2c58da17b2e70bf2657d6a3129edae01b967d49e8fad0bafdf1f19b body_fp=49f08a6f25c8cd0fdd11f233a48b5f42ee83a6b7db413b02f729eb8694c0912c source_ref=c6ce1d9dad031d3054b2bceb7224cbf06f70da61 role=model -->
Immutable result of a freshness check containing rebuild status and metadata.

- `refreshed`: whether the graph was rebuilt during this check
- `reason`: why the check triggered (unchanged, head_moved, mtimes_moved, no_stamp, empty_store)
- `head`: git HEAD SHA at time of check
- `incremental`: LLM sync result when `sync_prose=True`, otherwise None
- `stale_files`: triefact files needing regeneration after mtimes_moved refresh
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:ensure_fresh_before_turn fingerprint=2ab9f9c71b811b89d971b1353c6d8caf51709091ea4b8e0d36261d6723e89dc6 body_fp=df55c6f6b80b896848d26ce6b52dffaf96e5c95d332627a130c6c8d68235bbdd source_ref=14929b2b4fde4589611c3467f8350de2b33f88a9 role=orchestration -->
Runs a cheap freshness probe at the start of an agent turn to ensure the graph and triefacts reflect current state.

- Four possible outcomes: `no_stamp` (first run), `head_moved` (git pull), `mtimes_moved` (local edits), `unchanged` (fast path)
- `mtimes_moved` marks stale triefacts in pending file by default; `sync_prose=True` triggers inline LLM regeneration
- Other cases rebuild graph without prose changes to keep turn boundaries fast
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:ensure_fresh_after_turn fingerprint=a30ef723c61c2ba342a5b1102ec6c4d348bbb691b0472fbe2c9b1bed47cf523b body_fp=3124f5788dd9b2fe1de25a18e31b1b4ac80e16c9f6abf62b61cae14ab8b2176c source_ref=14929b2b4fde4589611c3467f8350de2b33f88a9 role=orchestration -->
Runs freshness sweep after agent turn to catch files edited during the just-finished turn.

- `sync_prose`: whether to regenerate prose inline instead of marking files stale
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:_ensure_fresh fingerprint=90bcf94f867b3a92154d10bf07e4212c396f7fd58fc4fca4bafbe1e54fd56450 body_fp=4cd1516dc444d4af3b78852ce3f19ad62ddb9d1d5f33459bc0ce75dec3f2279c source_ref=c6ce1d9dad031d3054b2bceb7224cbf06f70da61 role=orchestration -->
Core freshness gate implementation that rebuilds the graph when git HEAD or file mtimes change since last refresh.

- Checks git HEAD, stamp file, and current mtimes to determine refresh reason
- `unchanged` returns early without rebuilding anything
- `mtimes_moved` with `sync_prose=False` marks stale files for later sync
- `mtimes_moved` with `sync_prose=True` runs inline LLM regeneration
- All other reasons (`no_stamp`, `head_moved`, `empty_store`) rebuild graph without LLM
- Updates stamp file and pending stale list after successful refresh
<!-- trie:end -->