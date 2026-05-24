---
trie_version: 0.1.2
source: trie/git_helpers.py
file_fingerprint: 0ad427dd3e70edd0d2451be9e7c18fe1d93af86f8c3a2e0b3efba8ba83e39840
last_synced_at: '2026-05-23T23:53:48Z'
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
<!-- trie:section symbol=trie/git_helpers:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=24f948b40a2205a8fbce12ff8f6d00c684d36ff4d83a5ced78cb960130eb6ef1 source_ref=a120f6a20e8bfca8afcb22b8c56ed8d56778c96f -->
## `trie/git_helpers`

Provide quiet, narrowly-scoped git operations for diff-aware section regeneration.

- Returns `None` on any failure; never raises into the sync pipeline.
- Uses content-addressed blob hashes stamped into section sentinels for change detection.
<!-- trie:end -->
<!-- trie:section symbol=trie/git_helpers:_run_git fingerprint=f24bcb15562c359a607a98f1f189a2041a915a24878e60ce8bb1715db27d4d56 body_fp=3225a685078bbb18a458a72d45aade8919e83fad333747e691d60dc3abee0fc3 source_ref=a120f6a20e8bfca8afcb22b8c56ed8d56778c96f -->
## `_run_git(args: list[str], *, cwd: Path, input_bytes: bytes | None = None) -> bytes | None`

Run `git <args>` from `cwd`, returning stdout bytes on success or `None` on any failure.

- `input_bytes`: piped to stdin; pass `None` for commands that take no input.
- Returns `None` on non-zero exit, timeout (5 s), missing git binary, or `OSError`.
<!-- trie:end -->
<!-- trie:section symbol=trie/git_helpers:is_git_repo fingerprint=675fb860d9da412270ab09ed63e85801dd9f4b3cdba59b53ef8e5ab821a7cf5f body_fp=814908aa0b2368c1e104f0a85bc608ecfdc4abd11b1fec4c151ca8e8ee2732b3 source_ref=a120f6a20e8bfca8afcb22b8c56ed8d56778c96f -->
## `is_git_repo(path: Path) -> bool`

Return `True` if `path` is inside a git working tree, `False` otherwise.
<!-- trie:end -->
<!-- trie:section symbol=trie/git_helpers:current_head fingerprint=1163f4b6594e57f166e08145c0d383952b0e6eb6a09f729fe3c5ca2d2ee6fb8b body_fp=40ad72513a0e7bacbce2336ea309b1197200ea67a15bf94ce788b2813481e96c source_ref=a120f6a20e8bfca8afcb22b8c56ed8d56778c96f -->
## `current_head(repo_root: Path) -> str | None`

Return the commit SHA at HEAD for the given repo root, or `None` on any failure.

- Returns `None` for empty repos, unresolvable detached HEAD, or git errors.
<!-- trie:end -->
<!-- trie:section symbol=trie/git_helpers:compute_blob_hash fingerprint=afcadc5bcb6bfdf267b316dd72280d4ca940d06468c430a28dee2d9a0e494747 body_fp=0ed1c9f0bc5c43ecacad4f96f6d9841d3e0ed6a229af6ce65a41951d1c7821a8 source_ref=a120f6a20e8bfca8afcb22b8c56ed8d56778c96f -->
## `compute_blob_hash(file_path: Path, *, max_bytes: int | None = None) -> str | None`

Compute the git blob hash for a working-tree file without writing it to `.git/objects`.

- `max_bytes`: files exceeding this size return `None` without invoking git.
- Returns `None` if the file is unreadable, git is unavailable, or the path is outside a git repo.
- Requires a git repo: hashes computed outside one are unretrievable and silently omitted.
- Returns a 40-char (SHA-1) or 64-char (SHA-256) hex string, or `None` for unexpected output.
<!-- trie:end -->
<!-- trie:section symbol=trie/git_helpers:retrieve_blob fingerprint=8b3c6cd56c34017360f6f9bf3b730b3b9f63220fc40741ff0c91268a7f80a116 body_fp=5f3bd2d8800cd873c72f4a362618db28fe2a8859369ce44b8e7f3635026dd85c source_ref=a120f6a20e8bfca8afcb22b8c56ed8d56778c96f -->
## `retrieve_blob(repo_root: Path, blob_hash: str) -> str | None`

Fetch and decode a git blob by its SHA hash, returning `None` if unreachable or malformed.

- `blob_hash`: must be 40 (SHA-1) or 64 (SHA-256) hex chars; anything else returns `None`.
- Returns `None` if the blob was never committed, the hash is invalid, or git fails.
- Binary content is decoded UTF-8 with `replace`; callers must validate if strict round-tripping is needed.
<!-- trie:end -->