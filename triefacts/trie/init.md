---
trie_version: 0.1.2
source: trie/init.py
file_fingerprint: 0a0f50d06e8a6f9d4f79bb977d3e2bd80e6beb28d3ea51ded39a2599aad8aeb4
last_synced_at: '2026-05-19T15:24:34Z'
defines:
- kind: module
  qualified_name: trie/init:__module__
  lines: 1-179
- kind: constant
  qualified_name: trie/init:GITIGNORE_LINE
  lines: 9-9
- kind: constant
  qualified_name: trie/init:PreCommitStrategy
  lines: 11-11
- kind: constant
  qualified_name: trie/init:PRE_COMMIT_HOOK_MARKER
  lines: 13-13
- kind: constant
  qualified_name: trie/init:PRE_COMMIT_HOOK_END_MARKER
  lines: 14-14
- kind: constant
  qualified_name: trie/init:PRE_COMMIT_HOOK_BLOCK
  lines: 24-31
- kind: class
  qualified_name: trie/init:InitResult
  lines: 35-45
- kind: class
  qualified_name: trie/init:InitError
  lines: 48-49
- kind: function
  qualified_name: trie/init:_detect_python_project
  lines: 52-67
- kind: function
  qualified_name: trie/init:_ensure_gitignore_entry
  lines: 70-83
- kind: function
  qualified_name: trie/init:install_pre_commit_hook
  lines: 86-115
- kind: function
  qualified_name: trie/init:init_project
  lines: 118-178
incoming_refs: 29
outgoing_refs: 1
---
<!-- trie:section symbol=trie/init:InitResult fingerprint=6159e79af9587c2f4c2280d80e815af142855cae81912c12db1958bb33088be7 body_fp=c2638a39d527c3da8891ef1f9ed301f714b48dd9324f3391a5ab16e793471039 source_ref=2bb407d196526bad43f7647e409c43350e691c45 -->
## `InitResult`

Dataclass capturing the outcome of a `trie init` run.

- `config_written`: always `True` after successful init
- `pre_commit_strategy`: one of `"git_hook"`, `"framework"`, `"none"`, `"skipped"`
- `scan_ran`: `False` if `run_scan=False` was passed to `init_project`
<!-- trie:end -->

<!-- trie:section symbol=trie/init:InitError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=6ac93228090fa1ac2be2abf7a58af1ac2e2da7eeafdd624171eb25d4865f2f7c source_ref=2bb407d196526bad43f7647e409c43350e691c45 -->
## `class InitError(Exception)`

Raised by `init_project` when initialisation preconditions fail.
<!-- trie:end -->

<!-- trie:section symbol=trie/init:install_pre_commit_hook fingerprint=15a712a6e65acf0735cc39913a4311a1400df95b8e6582502023ebf3bb2fd821 body_fp=4f20944378ae44b778f1d14d41df287ebc93eaabd5b01ae255a6bc34b10929f6 source_ref=2bb407d196526bad43f7647e409c43350e691c45 -->
## `install_pre_commit_hook(project_root: Path) -> tuple[bool, PreCommitStrategy, Path | None]`

Install a marker-fenced `trie verify` block into the git pre-commit hook, choosing a strategy based on the project layout.

- `project_root`: repo root; must contain `.git/` for hook installation.
- Returns `(changed, strategy, hook_path)` where `changed` is `False` when already installed or strategy is not `git_hook`.
- `"framework"`: `.pre-commit-config.yaml` detected; caller must add snippet manually.
- `"none"`: no `.git/` directory found; nothing written.
- `"git_hook"`: hook written or appended; idempotent on repeated calls.
<!-- trie:end -->

<!-- trie:section symbol=trie/init:init_project fingerprint=96c40ec7a1db079af60e0e7a3b69c77d33eb36824cd1f0838888f69fb647c494 body_fp=fa3e08cd51298ff5823d6ea74d34a6e4276240feba19bf58a3a0b02e4940c579 source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
## `init_project(root: Path, *, force: bool = False, install_hooks: bool = False, run_scan: bool = True) -> InitResult`

Initialise trie in `root`: write `trie.toml`, update `.gitignore`, and optionally scan the project and install pre-commit hooks.

- `force`: skip non-Python-project and existing-config guards.
- `run_scan`: run initial symbol scan so the graph is ready for `trie sync`.
- `install_hooks`: attempt pre-commit hook installation via `install_pre_commit_hook`.
- Raises `InitError` if `root` is not a directory, not a Python project, or `trie.toml` exists (each suppressible with `force=True`).
<!-- trie:end -->

<!-- trie:section symbol=trie/init:_detect_python_project fingerprint=d6552c9bad1130f26878d296aa1117bad09a3cd47ec50d67215c497e7f3de1eb body_fp=b004f35ebd610c424e83fc058dc245b40bc2cee3304f57bcc6501db4e6dbf398 source_ref=2bb407d196526bad43f7647e409c43350e691c45 -->
## `_detect_python_project(root: Path) -> list[str]`

Return detected Python project marker filenames for `root`, or an empty list if none found.

- Returns `["*.py files"]` as fallback when no standard config files exist but `.py` files are found.
<!-- trie:end -->

<!-- trie:section symbol=trie/init:_ensure_gitignore_entry fingerprint=70d84e5eee964e2def6cf234ec4d0cf31e6e2f6ddb5176994fee2664237d2df1 body_fp=4916e4546fa0969284169cc88e016830f876c740173a1d9772f62922a1eb4aa4 source_ref=2bb407d196526bad43f7647e409c43350e691c45 -->
## `_ensure_gitignore_entry(gitignore: Path, line: str) -> bool`

Append `line` to the gitignore file if absent; return `True` if the file was modified.

- `line`: exact string to match (trailing `/` is ignored during comparison).
<!-- trie:end -->

<!-- trie:section symbol=trie/init:GITIGNORE_LINE fingerprint=b9d82ba13e5468d46b74c1ca13f07a5f91362fb0734d7b6ae7a61507743b06ef body_fp=a3b45f3eb4718c2f382a21a5ab12124f3eefb7211e9c13e68051fe97d53438e6 source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
## `GITIGNORE_LINE = ".trie/"`

The `.gitignore` entry appended to exclude the trie data directory from version control.
<!-- trie:end -->

<!-- trie:section symbol=trie/init:PreCommitStrategy fingerprint=870bb5512347025a866aba447ba3e81c76b145fd766f52f1539aedf49de39247 body_fp=061df27dbf331351d2d03c2c83485561d4e8e3b5185ab1cd9943eee375280f99 source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
## `PreCommitStrategy = Literal["git_hook", "framework", "none", "skipped"]`

Type alias for the four possible pre-commit installation outcomes.
<!-- trie:end -->

<!-- trie:section symbol=trie/init:PRE_COMMIT_HOOK_MARKER fingerprint=db5c85dbdc0d42aa74f25ae1b2955578c9c0d2e12d16c71615b3899b42eae1ef body_fp=092b84ecde640a5e8cff95ee169afffaa23be4e9a274ea5a34b71a6020768b1c source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
## `PRE_COMMIT_HOOK_MARKER = "# trie-verify (added by \`trie init\`)"`

Sentinel comment marking the start of the trie-injected pre-commit hook block.
<!-- trie:end -->

<!-- trie:section symbol=trie/init:PRE_COMMIT_HOOK_END_MARKER fingerprint=d0c3f84018a4b0fdae65792bc7130e5d78252bcf888b935afbcbb1162fee2ec0 body_fp=823ea022d1827b4fda4f2faa1a1130d6b6ed7ac785e9265814607c4e85c1ef11 source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
## `PRE_COMMIT_HOOK_END_MARKER = "# end trie-verify"`

Closing sentinel comment that marks the end of the trie-injected pre-commit hook block.
<!-- trie:end -->

<!-- trie:section symbol=trie/init:PRE_COMMIT_HOOK_BLOCK fingerprint=aea969236fa4acff5bd395cd7cda878d70e23fa931773656426cb6b6397e037e body_fp=6a61889209aac758c8f8dfac24c1d07e19104914303cec4842edcbd7051034c4 source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
## `PRE_COMMIT_HOOK_BLOCK`

Shell script block injected into `.git/hooks/pre-commit`, running `trie lock-check` then `trie verify`, guarded by a `command -v trie` check.
<!-- trie:end -->

<!-- trie:section symbol=trie/init:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=e0c7563501e44750b6c9778ec13472afb19a98d2dec15dd7657aea21eac2e3fc source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
## `trie/init`

Provides project initialisation: writes `trie.toml`, updates `.gitignore`, installs pre-commit hooks, and optionally runs the initial symbol scan.

- `GITIGNORE_LINE`: the `.trie/` entry added to `.gitignore`
- `PRE_COMMIT_HOOK_BLOCK`: shell snippet injected into `.git/hooks/pre-commit`; runs `lock-check` then `verify`
- `PreCommitStrategy`: one of `"git_hook"`, `"framework"`, `"none"`, `"skipped"`
<!-- trie:end -->