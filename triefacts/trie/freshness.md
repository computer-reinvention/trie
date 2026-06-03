---
trie_version: 0.1.5
source: trie/freshness.py
file_fingerprint: 074a34d242a8aa4a2c1344ccac9d4007b9ebdf04d5de86e61722982b9ff62439
last_synced_at: '2026-06-03T21:11:33Z'
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
<!-- trie:section symbol=trie/freshness:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=d60cccb6d7672a73cd632cf51c0697cfac932f1e9143b45a73e72d8dcf9c0604 source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 -->
Freshness gate module that keeps the graph and triefact tree current with respect to disk and git HEAD.

- `ensure_fresh_before_turn()`: cheap probe at turn start catching HEAD moves and inter-turn edits
- `ensure_fresh_after_turn()`: filesystem sweep at turn end catching in-turn agent edits
- `Stamp`: records git HEAD SHA and file mtimes at last refresh in `.trie/graph.head`
- `NotAGitRepoError`: raised when freshness gate runs outside a git repository
- `FreshnessResult`: outcome carrying refresh status, reason, and incremental result
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:STAMP_FILENAME fingerprint=aac8741000f280bd63bac926ffebec9cbf71b4495987943f78ec277e1b576db7 body_fp=c62d39f17835acdc2f2d1013bc8be96ed181402e6d191a1477a1bf3db7d007a5 source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 -->
Filename for the freshness stamp stored under `.trie/`.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:NotAGitRepoError fingerprint=09b365bfefd9d9b9a72c8c2e217dd31472401ec1d021a77332672cf7cbf20bf4 body_fp=6b5f69da7d66ef5182860f6e63b4efd037d2946c483b83586d68da875247c89c source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 -->
Exception raised when freshness operations are attempted outside a git repository.

- Enforces git requirement for HEAD-based drift detection during eval sessions
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:Stamp fingerprint=d1c55e5f7ac5b2b0f6e9a0f41a992c489b4bbd86c991d1319339a611fd2464a0 body_fp=31aec78ed4d0e13d91a146eabf1bcf7079550cdfc3034b86c450524ba4b34079 source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 -->
Records git HEAD SHA and file modification times to detect staleness between refresh cycles.

- `head`: commit SHA the graph was last built against
- `mtimes`: modification timestamps for in-scope source files at that moment
- `from_json`: returns None for malformed data, triggering full refresh
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:Stamp.to_json fingerprint=ce47e4e6daa8f0c4a250b20134274e9fbfd02aaf9ede1cb7bf37ca91c7410a99 body_fp=cb2d6f3559105752bf1a693a63a0fddf72be597e07acbb1387f5c67775e2323c source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 -->
Returns Stamp data as a JSON-serializable dictionary with 'head' and 'mtimes' keys.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:Stamp.from_json fingerprint=57f4bdcd743fa83a9a5d1df0b2bc7f61f2e798e6aad8a7a1a0c2241a0cf7b47f body_fp=f6b2ef409ce0083f22a240ec650c1b412f5ef7a90602797ffaf0fa8230585c23 source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 -->
Constructs a Stamp from parsed JSON, returning None for malformed data.

- Returns `None` when `head` is not a string or `mtimes` is not a dict
- Coerces numeric mtime values to floats, skipping invalid entries
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:stamp_path fingerprint=80a07e0294097d8da88cd2e3f54676211897796b445097ef0264fc4d82acc379 body_fp=7f7cb24633aa2e6e893ae32a226ff280d1635328c48aab0f9b833cebc285c173 source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 -->
Returns path to freshness stamp file at `.trie/graph.head` within project root.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:read_stamp fingerprint=21f5bc02e5c0a58c5b7dfbbdc12acc2571b335eb41f9160f8fe794c01380e1f9 body_fp=bbce59baf236941902988de4c42141c663e8d02a896d585218def54588ae1c99 source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 -->
Returns the recorded freshness stamp from disk, or None if missing or unreadable.

• All failure modes (missing file, malformed JSON, encoding errors) return None to force full refresh
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:write_stamp fingerprint=3191fba827b0de10432e3d06820239627570d6d361596c9d3abcd01940ccd5d4 body_fp=87f73609447123b2e8e27ba8ffd57a43601e1781ebcc01b9f57b50902f244540 source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 -->
Writes a freshness stamp to disk atomically using write-then-rename to prevent corruption.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:scan_mtimes fingerprint=bcf189563877e5a915ba69067f3a2d7adf79275e2404d31d4c0507334bd2d3c3 body_fp=0faaea3f8ed87f14aa6f266f222cd44a8b189ca288e6f2f0e89120b38ad93cae source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 -->
Returns modification times for all in-scope source files as a dictionary mapping relative paths to mtime floats.

- Uses `os.stat` instead of reading file contents for performance
- Skips files outside the configured source root or that don't exist
- Runs on every turn boundary to detect file changes without full scans
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:_require_git fingerprint=166feea2e74bf1d5b8f9f739d158f1b9adadb6c127a9c2e746f8f4d11a5f0cb7 body_fp=14454ffe8a0ed45d7ecc28f500d9cc12422f874506518ebb6eabbfe6be60d9fd source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 -->
Returns the current git HEAD SHA or raises NotAGitRepoError if the project lacks git or commits.

- Raises NotAGitRepoError when the project is not in a git repository
- Raises NotAGitRepoError when the repository exists but has no commits
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:_mtimes_differ fingerprint=2389c54fdae5ee854c5b80798bf3c260d7ac0ce740a8ae1f711ad01fb1e9b551 body_fp=1cf8c54cb76f51d4b2bd082edc06c14f30944668415598c951facfd855dfb1be source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 -->
Returns True if two mtime dictionaries disagree on any file path or modification time.

- Detects new files (in `b` but not `a`), removed files (in `a` but not `b`), and modified files (different mtime)
- Uses exact float comparison since filesystem mtimes have fixed precision
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:FreshnessResult fingerprint=8af5e0b2de5104af0d7073dfc753b7f6805d4e4c4ba1333149d51e6ef4a7f2a5 body_fp=8f459fbd3931cc83ba303ca6f4a50188a2ce86f9996555c0da123a6d45ebea87 source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 -->
Records the outcome of a freshness check operation.

- `refreshed`: whether `run_incremental` was invoked during the check
- `reason`: why the freshness check took its specific action path
- `head`: git SHA at check time for telemetry and debugging
- `incremental`: underlying incremental sync result when refresh ran
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:ensure_fresh_before_turn fingerprint=290aa05b8d0d6759bf13117ee5bb21bae127af9708276c98d21a06dfabb4548c body_fp=6640fafb717fe7b34cce9359f7dc120250cf98e10f1985b6b7810240d599c3b3 source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 -->
Runs a cheap freshness probe at the start of an agent turn to ensure the graph and triefacts reflect current state.

- Four possible outcomes: `no_stamp` (first run), `head_moved` (git pull), `mtimes_moved` (local edits), `unchanged` (fast path)
- Only `mtimes_moved` triggers LLM-based triefact regeneration; other cases rebuild graph without prose changes
- Catches edits made outside agent turns that would otherwise leave the first query stale
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:ensure_fresh_after_turn fingerprint=2a5af9c6a7ef7da3ef3df8784b3650da6731f86f613bc48facb72b3d8bc0d0dc body_fp=b6225f82db2d445c2b1a0234a9eeaf0761c96b7d633a8a59e29010ad345ad7b4 source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 -->
Runs freshness sweep after agent turn to catch files edited during the just-finished turn.
<!-- trie:end -->
<!-- trie:section symbol=trie/freshness:_ensure_fresh fingerprint=0508de7da5c974aebbcd23b7cbea9f212f5a8eaeae4c1f66c578d209397cbd64 body_fp=ffb2ce1ba8171b0fe338f9ebc9533aad5b2347ee0110c0fcef28d1280172714f source_ref=03c354e2bc01cc9a770ee44dfa2954fb8bba6f78 -->
Core freshness implementation that decides whether to refresh the graph and triefacts based on git HEAD and file modification times.

- Returns `FreshnessResult` with refresh status, reason, and incremental result
- Four outcomes: `no_stamp` (first run), `head_moved` (git pull), `mtimes_moved` (local edits), `unchanged` (no-op)
- Only `mtimes_moved` triggers LLM-powered triefact regeneration via `run_incremental`
- Other refresh cases rebuild graph via `scan_project` but preserve committed triefacts
- Updates stamp file after any refresh operation
<!-- trie:end -->