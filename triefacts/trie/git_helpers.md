---
trie_version: 0.3.0
source: trie/git_helpers.py
file_fingerprint: b8085054d60b993d8ada6ae5210ee923616f8a90852ed4e353d7546a8a138470
last_synced_at: '2026-07-25T00:07:02Z'
description: Quiet, narrowly-scoped git operations for diff-aware regen.
defines:
- kind: module
  qualified_name: trie/git_helpers:__module__
  lines: 1-210
- kind: function
  qualified_name: trie/git_helpers:_run_git
  lines: 32-59
  signature: 'def _run_git( args: list[str], *, cwd: Path, input_bytes: bytes | None = None, ok_returncodes: tuple[int, ...] = (0,), ) -> bytes | None'
- kind: function
  qualified_name: trie/git_helpers:is_git_repo
  lines: 62-65
  signature: 'def is_git_repo(path: Path) -> bool'
- kind: function
  qualified_name: trie/git_helpers:current_head
  lines: 68-82
  signature: 'def current_head(repo_root: Path) -> str | None'
- kind: function
  qualified_name: trie/git_helpers:commit_timestamp
  lines: 85-96
  signature: 'def commit_timestamp(repo_root: Path, ref: str = "HEAD") -> float | None'
- kind: function
  qualified_name: trie/git_helpers:show_file_at_ref
  lines: 99-104
  signature: 'def show_file_at_ref(repo_root: Path, ref: str, relpath: str) -> str | None'
- kind: function
  qualified_name: trie/git_helpers:compute_blob_hash
  lines: 107-146
  signature: 'def compute_blob_hash(file_path: Path, *, max_bytes: int | None = None) -> str | None'
- kind: function
  qualified_name: trie/git_helpers:retrieve_blob
  lines: 149-167
  signature: 'def retrieve_blob(repo_root: Path, blob_hash: str) -> str | None'
- kind: function
  qualified_name: trie/git_helpers:diff_paths
  lines: 170-209
  signature: 'def diff_paths(repo_root: Path, paths: list[str], base: str = "HEAD") -> str | None'
incoming_refs: 15
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
<!-- trie:section symbol=trie/git_helpers:_run_git fingerprint=203e2dbc07911476b9cf29b75127a109387b8225fae8f03904d6d186f351f289 body_fp=046f399defc7c6075f2d4ffc5be38596a1358257544bce1804d1ca4b050a1a68 role=change-detection -->
## `def _run_git( args: list[str], *, cwd: Path, input_bytes: bytes | None = None, ok_returncodes: tuple[int, ...] = (0,), ) -> bytes | None`

Execute a git command with the given arguments in the specified directory, returning the captured stdout bytes on success or None on any failure. Failures include a missing git binary, a timeout after 5 seconds, any OS-level error, or a process exit code not present in `ok_returncodes` (which defaults to `(0,)`, preserving existing behaviour while allowing callers such as `diff_paths` to widen acceptance to additional exit codes like 1 for `git diff --no-index`).
<!-- trie:end -->
<!-- trie:section symbol=trie/git_helpers:is_git_repo fingerprint=675fb860d9da412270ab09ed63e85801dd9f4b3cdba59b53ef8e5ab821a7cf5f body_fp=5944443a73e1faac4353a225fcb993026c74c9e9bab4d0be5cf6f5732d1911ee source_ref=a120f6a20e8bfca8afcb22b8c56ed8d56778c96f role=change-detection -->
## `def is_git_repo(path: Path) -> bool`

Checks if `path` is inside a git working tree by running `git rev-parse --is-inside-work-tree`.
<!-- trie:end -->
<!-- trie:section symbol=trie/git_helpers:current_head fingerprint=1163f4b6594e57f166e08145c0d383952b0e6eb6a09f729fe3c5ca2d2ee6fb8b body_fp=b533f20544c7478cfacbfd9e8c15840bb511548d8bad8dce87d7b5cd10c2c360 source_ref=a120f6a20e8bfca8afcb22b8c56ed8d56778c96f role=change-detection -->
## `def current_head(repo_root: Path) -> str | None`

Returns the commit SHA at HEAD from the given repository root, or None if the lookup fails.

- Returns None for empty repositories, detached states, or any git failure
- Used by trie's freshness gate to compare working tree HEAD against regeneration stamps
<!-- trie:end -->
<!-- trie:section symbol=trie/git_helpers:commit_timestamp fingerprint=d400ee6b65d5c7b294677323179a42796f574fc7856b2e99b72a6fec29538508 body_fp=7e4e7b4bdb42a73dc51e9fb749fb538a65643c71f5e31fabcd27746c1047e9f9 source_ref=f91fe734e1682c0cc6b4975661a46c30a5c4d228 role=io -->
## `def commit_timestamp(repo_root: Path, ref: str = "HEAD") -> float | None`

Return the committer unix timestamp of `ref` as a float, or `None` on any git failure or empty output.

- `ref`: any git revision string; defaults to `HEAD`
<!-- trie:end -->
<!-- trie:section symbol=trie/git_helpers:show_file_at_ref fingerprint=9e79e5544c25e730d0c76d7fd574de063cfc72a39b4268f381624aa1423366fa body_fp=d174ae54859c3e18f7af25562fc5272c24d6578857372cd994826ba7e0f906c7 source_ref=e50fc73699fd073532fbbebf68ec2c680ae8870e role=io -->
## `def show_file_at_ref(repo_root: Path, ref: str, relpath: str) -> str | None`

Return the UTF-8 content of `relpath` at the given git `ref`, or `None` on any failure.
<!-- trie:end -->
<!-- trie:section symbol=trie/git_helpers:compute_blob_hash fingerprint=afcadc5bcb6bfdf267b316dd72280d4ca940d06468c430a28dee2d9a0e494747 body_fp=8cb04f41236179dece68ded96815b4c8e420fcc558f4a9f4010a65b32ed483dd source_ref=a120f6a20e8bfca8afcb22b8c56ed8d56778c96f role=change-detection -->
## `def compute_blob_hash(file_path: Path, *, max_bytes: int | None = None) -> str | None`

Computes git blob hash for working-tree file content without staging the file.

- `max_bytes`: size limit for processing; larger files return None
- Returns None if file unreadable, git unavailable, outside git repo, or exceeds size limit
<!-- trie:end -->
<!-- trie:section symbol=trie/git_helpers:retrieve_blob fingerprint=8b3c6cd56c34017360f6f9bf3b730b3b9f63220fc40741ff0c91268a7f80a116 body_fp=be52145f1b4a152dc428f6e04d0569135a96bc0aa04a6ec8b3f5a5e6c9d391c0 source_ref=a120f6a20e8bfca8afcb22b8c56ed8d56778c96f role=change-detection -->
## `def retrieve_blob(repo_root: Path, blob_hash: str) -> str | None`

Retrieves git blob content by hash from the specified repository root.

- Returns None if blob is unreachable, hash is malformed, or repo is invalid
- Binary content decoded with UTF-8 replacement on errors
<!-- trie:end -->
<!-- trie:section symbol=trie/git_helpers:diff_paths fingerprint=60562938743d7aca9692e67827d6149177d7fb9d60d67e75c7c6cb8d323f0dae body_fp=05d2d23fd45e9fbda31450aa0634787341b5512e36cab4c0a443bdab293169bc role=change-detection -->
## `def diff_paths(repo_root: Path, paths: list[str], base: str = "HEAD") -> str | None`

Return a unified `--no-color` diff of `paths` against `base` in `repo_root`, including both tracked changes (via `git diff`) and untracked files under `paths` (each diffed as an add against `/dev/null`), so that brand-new files created during a session appear in the output. Returns `None` only when the initial tracked `git diff` fails; returns `""` when there are no changes anywhere; degrades quietly if the untracked-file listing fails, in which case only the tracked diff is returned. The per-file `git diff --no-index` invocation correctly accepts exit code 1 as a success indicator, since diffing a new file against `/dev/null` always produces differences and a non-zero exit.
<!-- trie:end -->