---
trie_version: 0.1.0
source: trie/git_helpers.py
file_fingerprint: 7eac35fb496950fc01ebfed52b837b5a8ae494ed0c1223efa36b3f6f71ce09e7
last_synced_at: '2026-05-15T13:05:04Z'
description: Quiet, narrowly-scoped git operations for diff-aware regen.
defines:
- kind: function
  qualified_name: trie/git_helpers:_run_git
  lines: 32-56
- kind: function
  qualified_name: trie/git_helpers:is_git_repo
  lines: 59-62
- kind: function
  qualified_name: trie/git_helpers:compute_blob_hash
  lines: 65-95
- kind: function
  qualified_name: trie/git_helpers:retrieve_blob
  lines: 98-116
incoming_refs: 15
outgoing_refs: 0
---
<!-- trie:section symbol=trie/git_helpers:is_git_repo fingerprint=675fb860d9da412270ab09ed63e85801dd9f4b3cdba59b53ef8e5ab821a7cf5f body_fp=5511a78edcda1ca1e60ff08f46e4671529420d6584a5965df5f30d19f43602ea source_ref=dbf6fc45f22045181a4f474e363792eb03ff7011 -->
## `is_git_repo(path: Path) -> bool`

Return `True` if `path` lies inside a git working tree.
<!-- trie:end -->

<!-- trie:section symbol=trie/git_helpers:compute_blob_hash fingerprint=c4b13a76b7637c7a239a65ee75230528e8dabf018de33ffedb4ab4aec5b2d82b body_fp=1f3d128b2166b4aea004ce3056aa9651a01ef38f6a32f1de4365685974912eeb source_ref=dbf6fc45f22045181a4f474e363792eb03ff7011 -->
## `compute_blob_hash(file_path: Path) -> str | None`

Compute the git blob hash for `file_path`'s working-tree content without writing to `.git/objects`.

- Returns `None` if the file is unreadable, git is unavailable, or the file is outside a git repo.
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