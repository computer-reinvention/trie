---
trie_version: 0.1.0
source: trie/init.py
file_fingerprint: f3d1e4aaf968cb9aa30244b8adf95c075197fdc20c8ebf759dd18eee20d1ec2a
last_synced_at: '2026-05-14T17:29:03Z'
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
<!-- trie:section symbol=trie/init:InitResult fingerprint=6159e79af9587c2f4c2280d80e815af142855cae81912c12db1958bb33088be7 body_fp=c2638a39d527c3da8891ef1f9ed301f714b48dd9324f3391a5ab16e793471039 -->
## `InitResult`

Dataclass capturing the outcome of a `trie init` run.

- `config_written`: always `True` after successful init
- `pre_commit_strategy`: one of `"git_hook"`, `"framework"`, `"none"`, `"skipped"`
- `scan_ran`: `False` if `run_scan=False` was passed to `init_project`
<!-- trie:end -->

<!-- trie:section symbol=trie/init:InitError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=6ac93228090fa1ac2be2abf7a58af1ac2e2da7eeafdd624171eb25d4865f2f7c -->
## `class InitError(Exception)`

Raised by `init_project` when initialisation preconditions fail.
<!-- trie:end -->

<!-- trie:section symbol=trie/init:install_pre_commit_hook fingerprint=15a712a6e65acf0735cc39913a4311a1400df95b8e6582502023ebf3bb2fd821 body_fp=4f20944378ae44b778f1d14d41df287ebc93eaabd5b01ae255a6bc34b10929f6 -->
## `install_pre_commit_hook(project_root: Path) -> tuple[bool, PreCommitStrategy, Path | None]`

Install a marker-fenced `trie verify` block into the git pre-commit hook, choosing a strategy based on the project layout.

- `project_root`: repo root; must contain `.git/` for hook installation.
- Returns `(changed, strategy, hook_path)` where `changed` is `False` when already installed or strategy is not `git_hook`.
- `"framework"`: `.pre-commit-config.yaml` detected; caller must add snippet manually.
- `"none"`: no `.git/` directory found; nothing written.
- `"git_hook"`: hook written or appended; idempotent on repeated calls.
<!-- trie:end -->

<!-- trie:section symbol=trie/init:init_project fingerprint=96c40ec7a1db079af60e0e7a3b69c77d33eb36824cd1f0838888f69fb647c494 body_fp=fa3e08cd51298ff5823d6ea74d34a6e4276240feba19bf58a3a0b02e4940c579 -->
## `init_project(root: Path, *, force: bool = False, install_hooks: bool = False, run_scan: bool = True) -> InitResult`

Initialise trie in `root`: write `trie.toml`, update `.gitignore`, and optionally scan the project and install pre-commit hooks.

- `force`: skip non-Python-project and existing-config guards.
- `run_scan`: run initial symbol scan so the graph is ready for `trie sync`.
- `install_hooks`: attempt pre-commit hook installation via `install_pre_commit_hook`.
- Raises `InitError` if `root` is not a directory, not a Python project, or `trie.toml` exists (each suppressible with `force=True`).
<!-- trie:end -->