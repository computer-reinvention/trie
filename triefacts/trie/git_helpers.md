---
trie_version: 0.1.2
source: trie/git_helpers.py
file_fingerprint: 0ad427dd3e70edd0d2451be9e7c18fe1d93af86f8c3a2e0b3efba8ba83e39840
last_synced_at: '2026-05-19T10:40:42Z'
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
<!-- trie:section symbol=trie/git_helpers:is_git_repo fingerprint=675fb860d9da412270ab09ed63e85801dd9f4b3cdba59b53ef8e5ab821a7cf5f body_fp=5511a78edcda1ca1e60ff08f46e4671529420d6584a5965df5f30d19f43602ea source_ref=dbf6fc45f22045181a4f474e363792eb03ff7011 -->
## `is_git_repo(path: Path) -> bool`

Return `True` if `path` lies inside a git working tree.
<!-- trie:end -->

<!-- trie:section symbol=trie/git_helpers:compute_blob_hash fingerprint=afcadc5bcb6bfdf267b316dd72280d4ca940d06468c430a28dee2d9a0e494747 body_fp=c0a9ef15356a8b6d924c1a5ed90a7df18e90f70206ee6faeb5234d63be9aac27 source_ref=eb5f10acce02fe703d0fb96cc4ef4d1429d7695d -->
## `compute_blob_hash(file_path: Path, *, max_bytes: int | None = None) -> str | None`

Compute the git blob hash for `file_path`'s working-tree content without writing to `.git/objects`.

- Returns `None` if the file is unreadable, git is unavailable, the file is outside a git repo, or the file exceeds `max_bytes`.
- `max_bytes=None` (default) imposes no size limit; when set, skips git entirely for oversized files.
- Hash is 40 chars (SHA-1) or 64 chars (SHA-256); anything else returns `None`.
- Runs from the file's directory so `autocrlf`/attribute rules match commit-time behaviour.
<!-- trie:end -->

<!-- trie:section symbol=trie/git_helpers:retrieve_blob fingerprint=8b3c6cd56c34017360f6f9bf3b730b3b9f63220fc40741ff0c91268a7f80a116 body_fp=ad78d7eed1980fde6489a518eeeb0837a44591037c356cb28e9ab376c6612cd7 source_ref=dbf6fc45f22045181a4f474e363792eb03ff7011 -->
## `retrieve_blob(repo_root: Path, blob_hash: str) -> str | None`

Fetch and decode a git blob by its content-addressed hash; returns `None` if unreachable or malformed.

- `blob_hash`: must be a 40- or 64-character hex string; anything else returns `None` immediately.
- Returns decoded UTF-8 text with `replace` error handling for binary content.
<!-- trie:end -->

<!-- trie:section symbol=trie/git_helpers:_run_git fingerprint=f24bcb15562c359a607a98f1f189a2041a915a24878e60ce8bb1715db27d4d56 body_fp=4eb87ce9d155d002327837dd6af7e404ba753420c10b58940cd56d8d083eb4ad source_ref=dbf6fc45f22045181a4f474e363792eb03ff7011 -->
## `_run_git(args: list[str], *, cwd: Path, input_bytes: bytes | None = None) -> bytes | None`

Run `git <args>` from `cwd`, returning stdout bytes on success or `None` on any failure.

- `input_bytes`: piped to stdin if provided.
- Returns `None` on non-zero exit, timeout, missing binary, or OS error.
<!-- trie:end -->

<!-- trie:section symbol=trie/git_helpers:current_head fingerprint=1163f4b6594e57f166e08145c0d383952b0e6eb6a09f729fe3c5ca2d2ee6fb8b body_fp=5be8470cc13660ac119f379ac8b136a40049e33b7b733210932c632c8b49a9af source_ref=a120f6a20e8bfca8afcb22b8c56ed8d56778c96f -->
## `current_head(repo_root: Path) -> str | None`

Return the SHA of HEAD, or None if the lookup fails for any reason.

- Returns None for empty repos, detached HEADs, or any git error.
<!-- trie:end -->

<!-- trie:section symbol=trie/git_helpers:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=6dff4b2348ad98c82151422b031811d85dc24d60e6b8b65c95ed994467b9a08e source_ref=a120f6a20e8bfca8afcb22b8c56ed8d56778c96f -->
## `git_helpers`

Provide quiet, narrowly-scoped git operations for diff-aware section regeneration.

- Returns `None` on any failure; never raises into the sync pipeline.
- Uses content-addressed blob hashes, not commit hashes, for stamping source references.
<!-- trie:end -->