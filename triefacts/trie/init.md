---
trie_version: 0.1.0
source: trie/init.py
file_fingerprint: f3d1e4aaf968cb9aa30244b8adf95c075197fdc20c8ebf759dd18eee20d1ec2a
last_synced_at: '2026-05-12T18:32:31Z'
defines:
- kind: class
  qualified_name: trie/init:InitResult
  lines: 25-35
- kind: class
  qualified_name: trie/init:InitError
  lines: 38-39
- kind: function
  qualified_name: trie/init:install_pre_commit_hook
  lines: 76-105
- kind: function
  qualified_name: trie/init:init_project
  lines: 108-168
incoming_refs: 29
outgoing_refs: 0
---
<!-- trie:section symbol=trie/init:InitResult fingerprint=6159e79af9587c2f4c2280d80e815af142855cae81912c12db1958bb33088be7 body_fp=9ffd677c95ae7a83fd92512d668aa81e673c4049e13a873477464ba2d12a65b8 -->
## `InitResult`

Dataclass capturing the outcome of a `init_project` call.

- `config_written`: always `True` when set by `init_project`
- `pre_commit_strategy`: one of `"git_hook"`, `"framework"`, `"none"`, `"skipped"`
- `pre_commit_path`: set only when strategy is `"git_hook"`
<!-- trie:end -->

<!-- trie:section symbol=trie/init:InitError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=9018d0fc1e916801b251d19dc2755e7241c3c0162832cbd10bb010e52afd0196 -->
## `class InitError(Exception)`

Raised by `init_project` when project detection or configuration preconditions fail.
<!-- trie:end -->

<!-- trie:section symbol=trie/init:install_pre_commit_hook fingerprint=15a712a6e65acf0735cc39913a4311a1400df95b8e6582502023ebf3bb2fd821 body_fp=350fd22b812d77048bd519bd96b89d866e0c595a016b165e60e430156d26f13f -->
## `install_pre_commit_hook(project_root: Path) -> tuple[bool, PreCommitStrategy, Path | None]`

Install a marker-fenced `trie verify` block into the git pre-commit hook, choosing a strategy based on project state.

- `"framework"`: `.pre-commit-config.yaml` exists; returns `(False, "framework", None)`.
- `"git_hook"`: writes or appends to `.git/hooks/pre-commit`; idempotent via marker.
- `"none"`: no `.git` directory present; returns `(False, "none", None)`.
- First tuple element: `True` only when the hook block was newly written.
<!-- trie:end -->

<!-- trie:section symbol=trie/init:init_project fingerprint=96c40ec7a1db079af60e0e7a3b69c77d33eb36824cd1f0838888f69fb647c494 body_fp=92e0fbcaaa4448984118ffa86da26c90b975ed8ad4690418f078a869f174f05a -->
## `init_project(root: Path, *, force: bool = False, install_hooks: bool = False, run_scan: bool = True) -> InitResult`

Initialise trie in `root`: write `trie.toml`, update `.gitignore`, and optionally scan symbols and install a pre-commit hook.

- `force`: skip "already exists" and "not a Python project" guards.
- `run_scan`: runs `scan_project` and populates `result.scan_*` fields.
- `install_hooks`: calls `install_pre_commit_hook` and populates `result.pre_commit_*` fields.
- Raises `InitError` if `root` is not a directory, not a Python project (without `force`), or `trie.toml` already exists (without `force`).
<!-- trie:end -->