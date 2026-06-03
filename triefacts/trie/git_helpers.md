---
trie_version: 0.1.5
source: trie/git_helpers.py
file_fingerprint: 0ad427dd3e70edd0d2451be9e7c18fe1d93af86f8c3a2e0b3efba8ba83e39840
last_synced_at: '2026-06-03T21:11:44Z'
description: Quiet, narrowly-scoped git operations for diff-aware regen.
defines:
- kind: module
  qualified_name: trie/git_helpers:__module__
  lines: 1-143
- kind: function
  qualified_name: trie/git_helpers:_run_git
  lines: 32-56
- kind: function
  qualified_name: trie/git_helpers:is_git_repo
  lines: 59-62
- kind: function
  qualified_name: trie/git_helpers:current_head
  lines: 65-79
- kind: function
  qualified_name: trie/git_helpers:compute_blob_hash
  lines: 82-121
- kind: function
  qualified_name: trie/git_helpers:retrieve_blob
  lines: 124-142
incoming_refs: 17
outgoing_refs: 0
---
<!-- trie:section symbol=trie/git_helpers:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=88ea6f10aafbe5eec4426e9e74f9ab2198af7878d28571842c4f7b0a33d1db60 source_ref=a120f6a20e8bfca8afcb22b8c56ed8d56778c96f -->
Provides quiet git operations for diff-aware regeneration using content-addressed blob hashes.

- `_run_git()` - executes git commands with timeout and error suppression
- `is_git_repo()` - checks if path is inside a git working tree
- `current_head()` - retrieves HEAD commit SHA
- `compute_blob_hash()` - computes git blob hash for working tree files
- `retrieve_blob()` - reads blob content by hash from git object store
<!-- trie:end -->
<!-- trie:section symbol=trie/git_helpers:_run_git fingerprint=f24bcb15562c359a607a98f1f189a2041a915a24878e60ce8bb1715db27d4d56 body_fp=f61fb35b2bfd9974da0859634303bea65ce77c4dd6555dd23bc9fe0912a9cc41 source_ref=a120f6a20e8bfca8afcb22b8c56ed8d56778c96f -->
Execute git command with arguments in specified directory, returning stdout bytes or None on failure.

- `args`: git subcommand and flags to execute
- `cwd`: directory to run git from
- `input_bytes`: optional stdin data to pass to git process
- Returns None for any error: missing git binary, timeout after 5s, or non-zero exit
<!-- trie:end -->
<!-- trie:section symbol=trie/git_helpers:is_git_repo fingerprint=675fb860d9da412270ab09ed63e85801dd9f4b3cdba59b53ef8e5ab821a7cf5f body_fp=d14c0fd0b049d942635cbcdb77326e765af0dac2835e7828fecb8552ea3d8728 source_ref=a120f6a20e8bfca8afcb22b8c56ed8d56778c96f -->
Checks if `path` is inside a git working tree by running `git rev-parse --is-inside-work-tree`.
<!-- trie:end -->
<!-- trie:section symbol=trie/git_helpers:current_head fingerprint=1163f4b6594e57f166e08145c0d383952b0e6eb6a09f729fe3c5ca2d2ee6fb8b body_fp=11334a9111aa7c5a887bae5c6ea34a8b4d41b39dbb3757b3d4df924fe51c31c8 source_ref=a120f6a20e8bfca8afcb22b8c56ed8d56778c96f -->
Returns the commit SHA at HEAD from the given repository root, or None if the lookup fails.

- Returns None for empty repositories, detached states, or any git failure
- Used by trie's freshness gate to compare working tree HEAD against regeneration stamps
<!-- trie:end -->
<!-- trie:section symbol=trie/git_helpers:compute_blob_hash fingerprint=afcadc5bcb6bfdf267b316dd72280d4ca940d06468c430a28dee2d9a0e494747 body_fp=7192cccf5f80c78a99dce6a72f2f61d82d82cb667bc17fee9a6835ca20353a27 source_ref=a120f6a20e8bfca8afcb22b8c56ed8d56778c96f -->
Computes git blob hash for working-tree file content without staging the file.

- `max_bytes`: size limit for processing; larger files return None
- Returns None if file unreadable, git unavailable, outside git repo, or exceeds size limit
<!-- trie:end -->
<!-- trie:section symbol=trie/git_helpers:retrieve_blob fingerprint=8b3c6cd56c34017360f6f9bf3b730b3b9f63220fc40741ff0c91268a7f80a116 body_fp=fbf3f828c5196755ef2fc627dde1158ea39cb1baf32c29ce149bfbeecc8d81b6 source_ref=a120f6a20e8bfca8afcb22b8c56ed8d56778c96f -->
Retrieves git blob content by hash from the specified repository root.

- Returns None if blob is unreachable, hash is malformed, or repo is invalid
- Binary content decoded with UTF-8 replacement on errors
<!-- trie:end -->