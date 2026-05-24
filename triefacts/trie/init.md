---
trie_version: 0.1.2
source: trie/init.py
file_fingerprint: 0a0f50d06e8a6f9d4f79bb977d3e2bd80e6beb28d3ea51ded39a2599aad8aeb4
last_synced_at: '2026-05-23T23:53:14Z'
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
<!-- trie:section symbol=trie/init:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=6a7c8120c961f3a8e796d75d5cf20cfafc8391159a20a859ee056bb01fd6f77e source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
## `trie/init`

Provide project initialisation: write `trie.toml`, update `.gitignore`, install pre-commit hooks, and optionally run the initial symbol scan.
<!-- trie:end -->
<!-- trie:section symbol=trie/init:GITIGNORE_LINE fingerprint=b9d82ba13e5468d46b74c1ca13f07a5f91362fb0734d7b6ae7a61507743b06ef body_fp=a3b45f3eb4718c2f382a21a5ab12124f3eefb7211e9c13e68051fe97d53438e6 source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
## `GITIGNORE_LINE = ".trie/"`

The `.gitignore` entry appended to exclude the trie data directory from version control.
<!-- trie:end -->
<!-- trie:section symbol=trie/init:PreCommitStrategy fingerprint=870bb5512347025a866aba447ba3e81c76b145fd766f52f1539aedf49de39247 body_fp=df74d55ca54ffe50bce344d87cf6119f8b4186259b8bf3ed059d29c49aa97735 source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
## `PreCommitStrategy = Literal["git_hook", "framework", "none", "skipped"]`

Type alias enumerating how `trie init` installs or skips pre-commit verification.

- `"git_hook"`: wrote/found block in `.git/hooks/pre-commit`
- `"framework"`: `.pre-commit-config.yaml` detected; user must add snippet manually
- `"none"`: no `.git` directory found; nothing installed
- `"skipped"`: hook installation was not requested
<!-- trie:end -->
<!-- trie:section symbol=trie/init:PRE_COMMIT_HOOK_MARKER fingerprint=db5c85dbdc0d42aa74f25ae1b2955578c9c0d2e12d16c71615b3899b42eae1ef body_fp=03e953c3791dcf5a9448a86ecc2de79ae08a955e3a50e2a6c9cb1316529c2f48 source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
## `PRE_COMMIT_HOOK_MARKER = "# trie-verify (added by \`trie init\`)"`

Opening sentinel comment used to detect an existing trie-managed block in a pre-commit hook file.
<!-- trie:end -->
<!-- trie:section symbol=trie/init:PRE_COMMIT_HOOK_END_MARKER fingerprint=d0c3f84018a4b0fdae65792bc7130e5d78252bcf888b935afbcbb1162fee2ec0 body_fp=474829c96762226a36391bdb1302560ebcb72fea832b04ec01d286b274ec019b source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
## `PRE_COMMIT_HOOK_END_MARKER = "# end trie-verify"`

Closing fence comment that marks the end of the trie-managed pre-commit hook block.
<!-- trie:end -->
<!-- trie:section symbol=trie/init:PRE_COMMIT_HOOK_BLOCK fingerprint=aea969236fa4acff5bd395cd7cda878d70e23fa931773656426cb6b6397e037e body_fp=282ebbc2384d11bd41fb117861144549cfd1911fa885923f3dee105f7711915e source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
## `PRE_COMMIT_HOOK_BLOCK`

Marker-fenced shell block injected into `.git/hooks/pre-commit`, running `trie lock-check` then `trie verify`, guarded by a `command -v trie` check.
<!-- trie:end -->
<!-- trie:section symbol=trie/init:InitResult fingerprint=6159e79af9587c2f4c2280d80e815af142855cae81912c12db1958bb33088be7 body_fp=48a0e8818acb0c2135e32eae6596b53e2b133af6e0a367284813b699c3da599f source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
## `InitResult`

Record the outcome of a `init_project` call.

- `detected_markers`: project-type markers found (e.g. `"pyproject.toml"`).
- `pre_commit_strategy`: one of `"git_hook"`, `"framework"`, `"none"`, `"skipped"`.
- `pre_commit_path`: path to the written hook file, or `None`.
<!-- trie:end -->
<!-- trie:section symbol=trie/init:InitError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=5681fda0f218c4d1cf2474727ce3739a333a7405658a217c8156cece5a8b9814 source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
## `class InitError(Exception)`

Raised by `init_project` when project initialisation fails.
<!-- trie:end -->
<!-- trie:section symbol=trie/init:_detect_python_project fingerprint=d6552c9bad1130f26878d296aa1117bad09a3cd47ec50d67215c497e7f3de1eb body_fp=d19f65d849b371f1d7569783e5f2ef5fd202e20ccc927ec2b909a18593bb6868 source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
## `_detect_python_project(root: Path) -> list[str]`

Return detected Python project marker filenames found under `root`, or `[]` if none.

- Falls back to scanning for `*.py` files one level deep if no standard config files exist.
<!-- trie:end -->
<!-- trie:section symbol=trie/init:_ensure_gitignore_entry fingerprint=70d84e5eee964e2def6cf234ec4d0cf31e6e2f6ddb5176994fee2664237d2df1 body_fp=74a027ea3304ffe4ba94378ce4f835c5b076bf2096be38fda29378e67bcbe8c5 source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
## `_ensure_gitignore_entry(gitignore: Path, line: str) -> bool`

Append `line` to a `.gitignore` file if not already present, returning `True` if the file was modified.

- `line`: trailing slash is stripped when checking for duplicates.
<!-- trie:end -->
<!-- trie:section symbol=trie/init:install_pre_commit_hook fingerprint=15a712a6e65acf0735cc39913a4311a1400df95b8e6582502023ebf3bb2fd821 body_fp=e3e0c5f42b0af0bad29f381be38e43ba3b501a10f1869be31392bb9c65967642 source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
## `install_pre_commit_hook(project_root: Path) -> tuple[bool, PreCommitStrategy, Path | None]`

Install a marker-fenced `trie lock-check && trie verify` block into `.git/hooks/pre-commit`, choosing a strategy based on the project layout.

- `bool`: `True` only when the hook block was newly written.
- `"framework"`: `.pre-commit-config.yaml` detected; caller must add trie manually.
- `"git_hook"`: hook written or already present; `Path` is the hook file.
- `"none"`: no `.git` directory found; nothing written.
<!-- trie:end -->
<!-- trie:section symbol=trie/init:init_project fingerprint=96c40ec7a1db079af60e0e7a3b69c77d33eb36824cd1f0838888f69fb647c494 body_fp=86f42a59e689e856fbf45b402c4f8443a99a5ba2ebd4c4adb3440d16d42f7ee1 source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
## `init_project(root: Path, *, force: bool = False, install_hooks: bool = False, run_scan: bool = True) -> InitResult`

Initialise trie in `root`: write `trie.toml`, update `.gitignore`, and optionally scan and install hooks.

- `force`: skip Python-project detection and existing-config guards.
- `run_scan`: run `scan_project` immediately so the symbol graph is populated.
- `install_hooks`: call `install_pre_commit_hook` and record the result.
- Raises `InitError` if `root` is not a directory, not a Python project (without `force`), or `trie.toml` already exists (without `force`).
<!-- trie:end -->