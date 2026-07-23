---
trie_version: 0.1.9
source: trie/git_helpers.py
file_fingerprint: ecc4ef6db83aabad83753eb6aacc070995781f82bdd24de9bbab6c705dbd0044
last_synced_at: '2026-07-23T16:52:06Z'
description: Quiet, narrowly-scoped git operations for diff-aware regen.
defines:
- kind: module
  qualified_name: trie/git_helpers:__module__
  lines: 1-202
- kind: function
  qualified_name: trie/git_helpers:_run_git
  lines: 32-59
- kind: function
  qualified_name: trie/git_helpers:is_git_repo
  lines: 62-65
- kind: function
  qualified_name: trie/git_helpers:current_head
  lines: 68-82
- kind: function
  qualified_name: trie/git_helpers:commit_timestamp
  lines: 85-96
- kind: function
  qualified_name: trie/git_helpers:compute_blob_hash
  lines: 99-138
- kind: function
  qualified_name: trie/git_helpers:retrieve_blob
  lines: 141-159
- kind: function
  qualified_name: trie/git_helpers:diff_paths
  lines: 162-201
incoming_refs: 17
outgoing_refs: 0
---
<!-- trie:section symbol=trie/git_helpers:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=88ea6f10aafbe5eec4426e9e74f9ab2198af7878d28571842c4f7b0a33d1db60 source_ref=a120f6a20e8bfca8afcb22b8c56ed8d56778c96f role=change-detection -->
Provides quiet git operations for diff-aware regeneration using content-addressed blob hashes.

- `_run_git()` - executes git commands with timeout and error suppression
- `is_git_repo()` - checks if path is inside a git working tree
- `current_head()` - retrieves HEAD commit SHA
- `compute_blob_hash()` - computes git blob hash for working tree files
- `retrieve_blob()` - reads blob content by hash from git object store
<!-- trie:end -->
<!-- trie:section symbol=trie/git_helpers:_run_git fingerprint=203e2dbc07911476b9cf29b75127a109387b8225fae8f03904d6d186f351f289 body_fp=afeae39aa2a5695734d5054d5958f8dcf50a473d148091e2d10c09795f3e34e4 role=change-detection -->
Execute a git command with the given arguments in the specified directory, returning the captured stdout bytes on success or None on any failure. Failures include a missing git binary, a timeout after 5 seconds, any OS-level error, or a process exit code not present in `ok_returncodes` (which defaults to `(0,)`, preserving existing behaviour while allowing callers such as `diff_paths` to widen acceptance to additional exit codes like 1 for `git diff --no-index`).
<!-- trie:end -->
<!-- trie:section symbol=trie/git_helpers:is_git_repo fingerprint=675fb860d9da412270ab09ed63e85801dd9f4b3cdba59b53ef8e5ab821a7cf5f body_fp=d14c0fd0b049d942635cbcdb77326e765af0dac2835e7828fecb8552ea3d8728 source_ref=a120f6a20e8bfca8afcb22b8c56ed8d56778c96f role=change-detection -->
Checks if `path` is inside a git working tree by running `git rev-parse --is-inside-work-tree`.
<!-- trie:end -->
<!-- trie:section symbol=trie/git_helpers:current_head fingerprint=1163f4b6594e57f166e08145c0d383952b0e6eb6a09f729fe3c5ca2d2ee6fb8b body_fp=11334a9111aa7c5a887bae5c6ea34a8b4d41b39dbb3757b3d4df924fe51c31c8 source_ref=a120f6a20e8bfca8afcb22b8c56ed8d56778c96f role=change-detection -->
Returns the commit SHA at HEAD from the given repository root, or None if the lookup fails.

- Returns None for empty repositories, detached states, or any git failure
- Used by trie's freshness gate to compare working tree HEAD against regeneration stamps
<!-- trie:end -->
<!-- trie:section symbol=trie/git_helpers:commit_timestamp fingerprint=d400ee6b65d5c7b294677323179a42796f574fc7856b2e99b72a6fec29538508 body_fp=7341928b0349e4b571515579a6a8568547f35eda0c08221e6e19b0324fbe2b9e source_ref=f91fe734e1682c0cc6b4975661a46c30a5c4d228 role=io -->
Return the committer unix timestamp of `ref` as a float, or `None` on any git failure or empty output.

- `ref`: any git revision string; defaults to `HEAD`
<!-- trie:end -->
<!-- trie:section symbol=trie/git_helpers:compute_blob_hash fingerprint=afcadc5bcb6bfdf267b316dd72280d4ca940d06468c430a28dee2d9a0e494747 body_fp=7192cccf5f80c78a99dce6a72f2f61d82d82cb667bc17fee9a6835ca20353a27 source_ref=a120f6a20e8bfca8afcb22b8c56ed8d56778c96f role=change-detection -->
Computes git blob hash for working-tree file content without staging the file.

- `max_bytes`: size limit for processing; larger files return None
- Returns None if file unreadable, git unavailable, outside git repo, or exceeds size limit
<!-- trie:end -->
<!-- trie:section symbol=trie/git_helpers:retrieve_blob fingerprint=8b3c6cd56c34017360f6f9bf3b730b3b9f63220fc40741ff0c91268a7f80a116 body_fp=fbf3f828c5196755ef2fc627dde1158ea39cb1baf32c29ce149bfbeecc8d81b6 source_ref=a120f6a20e8bfca8afcb22b8c56ed8d56778c96f role=change-detection -->
Retrieves git blob content by hash from the specified repository root.

- Returns None if blob is unreachable, hash is malformed, or repo is invalid
- Binary content decoded with UTF-8 replacement on errors
<!-- trie:end -->
<!-- trie:section symbol=trie/git_helpers:diff_paths fingerprint=60562938743d7aca9692e67827d6149177d7fb9d60d67e75c7c6cb8d323f0dae body_fp=ba61edb0f21ce52a94f88a9ff4a4ed611c7437019ba6163a7715708679c41243 role=change-detection -->
Return a unified `--no-color` diff of `paths` against `base` in `repo_root`, including both tracked changes (via `git diff`) and untracked files under `paths` (each diffed as an add against `/dev/null`), so that brand-new files created during a session appear in the output. Returns `None` only when the initial tracked `git diff` fails; returns `""` when there are no changes anywhere; degrades quietly if the untracked-file listing fails, in which case only the tracked diff is returned. The per-file `git diff --no-index` invocation correctly accepts exit code 1 as a success indicator, since diffing a new file against `/dev/null` always produces differences and a non-zero exit.
<!-- trie:end -->