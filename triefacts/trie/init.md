---
trie_version: 0.3.0
source: trie/init.py
file_fingerprint: 8404d66cb90bf481d446d9ccb779bc363964239677831a79109ab2db39daabfe
last_synced_at: '2026-07-29T17:55:31Z'
defines:
- kind: module
  qualified_name: trie/init:__module__
  lines: 1-197
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
  lines: 23-29
- kind: class
  qualified_name: trie/init:InitResult
  lines: 33-43
  signature: class InitResult
- kind: class
  qualified_name: trie/init:InitError
  lines: 46-47
  signature: class InitError(Exception)
- kind: function
  qualified_name: trie/init:_detect_supported_project
  lines: 50-78
  signature: 'def _detect_supported_project(root: Path) -> list[str]'
- kind: constant
  qualified_name: trie/init:_detect_python_project
  lines: 82-82
- kind: function
  qualified_name: trie/init:_ensure_gitignore_entry
  lines: 85-98
  signature: 'def _ensure_gitignore_entry(gitignore: Path, line: str) -> bool'
- kind: function
  qualified_name: trie/init:install_pre_commit_hook
  lines: 101-132
  signature: 'def install_pre_commit_hook(project_root: Path) -> tuple[bool, PreCommitStrategy, Path | None]'
- kind: function
  qualified_name: trie/init:init_project
  lines: 135-196
  signature: 'def init_project( root: Path, *, force: bool = False, install_hooks: bool = False, run_scan: bool = True, ) -> InitResult'
incoming_refs: 37
outgoing_refs: 6
---
<!-- trie:section symbol=trie/init:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=95b8552fa69d3eff65de01deecb2317826321452b0dc87de2cc7fcf12d191a9f source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 role=agent-integration -->
Initializes trie projects by writing configuration, updating gitignore, and running initial scans.

- `InitResult`: dataclass capturing initialization outcomes including scan metrics and pre-commit setup
- `InitError`: exception raised when initialization fails due to missing Python project markers or existing config
- `_detect_python_project()`: identifies Python project markers like pyproject.toml or *.py files
- `_ensure_gitignore_entry()`: appends .trie/ to gitignore if not already present
- `install_pre_commit_hook()`: installs git hook running trie verify with framework detection
- `init_project()`: main initialization function with force override and optional scanning
<!-- trie:end -->
<!-- trie:section symbol=trie/init:GITIGNORE_LINE fingerprint=b9d82ba13e5468d46b74c1ca13f07a5f91362fb0734d7b6ae7a61507743b06ef body_fp=5d51e4b1a8e1755dfc8272187b8329a73317627aba076cb1fd99e812bb604ed2 source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 role=config-management -->
Gitignore entry string that excludes the `.trie/` directory from version control.
<!-- trie:end -->
<!-- trie:section symbol=trie/init:PreCommitStrategy fingerprint=870bb5512347025a866aba447ba3e81c76b145fd766f52f1539aedf49de39247 body_fp=1c0f2f326471c9360081d2eeedcec027215d40baef460fdb4b6c58abbfdd73c0 source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 role=agent-integration -->
Type alias defining the four possible pre-commit hook installation strategies.
<!-- trie:end -->
<!-- trie:section symbol=trie/init:PRE_COMMIT_HOOK_MARKER fingerprint=db5c85dbdc0d42aa74f25ae1b2955578c9c0d2e12d16c71615b3899b42eae1ef body_fp=cffacfbf3956982971b759a69f73e30588a98fefcd9c66a1b10b777f88d3faca source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 role=agent-integration -->
Comment string marking the start of trie's pre-commit hook block in `.git/hooks/pre-commit`.
<!-- trie:end -->
<!-- trie:section symbol=trie/init:PRE_COMMIT_HOOK_END_MARKER fingerprint=d0c3f84018a4b0fdae65792bc7130e5d78252bcf888b935afbcbb1162fee2ec0 body_fp=0895ada7bc149132af314e0d92132481cf71ef7930b58b73f120bdb8d753f4d3 source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 role=agent-integration -->
String constant marking the end of trie's pre-commit hook block in git hooks.
<!-- trie:end -->
<!-- trie:section symbol=trie/init:PRE_COMMIT_HOOK_BLOCK fingerprint=5a219e8e67a8defa9814ce8d096f3b227e7bb2864a8c3452c8767bbc81aa304e body_fp=ed551e42bd898b89fd05cd00b97de30fba06c890be9da383525b872c47a57286 source_ref=2c03dbb203a0074b0a5d9c3a83ed9291f6d2df11 role=config -->
Shell script block embedded between marker comments for idempotent injection into `.git/hooks/pre-commit`, gating commits via a single `trie gate` call.

- Entire block is a no-op if `trie` is not on `PATH`.
- `trie gate` runs lock-check, verify, intent gate, and advisory digest write; blocks the commit on failure.
<!-- trie:end -->
<!-- trie:section symbol=trie/init:InitResult fingerprint=6159e79af9587c2f4c2280d80e815af142855cae81912c12db1958bb33088be7 body_fp=2c574796ecd3bd7932a5bff9771e3817dde9ba441eb0dc5747db45be13d3033d source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 role=config-management -->
## `class InitResult`

Dataclass capturing the results of running `init_project`.

- `detected_markers`: Python project markers found (pyproject.toml, setup.py, etc.)
- `scan_files_total`: Number of Python files scanned for symbols
- `scan_symbols_total`: Number of symbols discovered during scan
- `scan_ran`: Whether the initial symbol scan was performed
- `pre_commit_installed`: Whether a new pre-commit hook was actually installed
- `pre_commit_strategy`: How pre-commit integration was handled
- `pre_commit_path`: Path to the pre-commit hook file if using git_hook strategy
<!-- trie:end -->
<!-- trie:section symbol=trie/init:InitError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=6f4c56742878e74ba8827d78644985c3cef8875aebf95281aca452cf73cf85ff source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 role=config-management -->
## `class InitError(Exception)`

Exception raised when project initialization fails due to validation errors or conflicts.
<!-- trie:end -->
<!-- trie:section symbol=trie/init:_detect_supported_project fingerprint=e93bb812f3d47d42259fa3390f77e4a44476de0f308e4131805d5e1c6efe0f94 body_fp=beae480898112f7a2da17e760daab50dad68f2c99881860fe8cde7d7fa5171cb source_ref=0bc865bbbbdbcc66c09082ed000b5e52b1a2994b role=domain -->
## `def _detect_supported_project(root: Path) -> list[str]`

Return a list of detected project-type markers under `root`, or `[]` if none are found.

- Falls back to scanning top-level and one-directory-deep files via the language backend registry if no well-known config file exists.
- Fallback entries are formatted as `*<ext> files` strings, not filenames.
<!-- trie:end -->
<!-- trie:section symbol=trie/init:_detect_python_project fingerprint=3f2725d49b3f8ac9cf540f3717eaebc0e0bb8745bf2c4e453d961f8839362d84 body_fp=91caaf5aac1141f436776eb3c89a2543bb7d3fc5e04013eb68517f8950b5c365 source_ref=0bc865bbbbdbcc66c09082ed000b5e52b1a2994b role=util -->
Backward-compatible alias for `_detect_supported_project`; retains the old name for tests and external callers.
<!-- trie:end -->
<!-- trie:section symbol=trie/init:_ensure_gitignore_entry fingerprint=70d84e5eee964e2def6cf234ec4d0cf31e6e2f6ddb5176994fee2664237d2df1 body_fp=1c0636b109177e97c62bc850c3806d78a0e0445b2a728585664fde265d22af9f source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 role=agent-integration -->
## `def _ensure_gitignore_entry(gitignore: Path, line: str) -> bool`

Append `line` to `gitignore` if not already present, returning True if file changed.
<!-- trie:end -->
<!-- trie:section symbol=trie/init:install_pre_commit_hook fingerprint=d7786183af45b0f0b1c62bad0d5ceb58d2d2c31149d77e585959170621d8fc52 body_fp=c9a083891453431a72609010be9754e63c820c409c920b2420f7ca842841d45b role=agent-integration -->
## `def install_pre_commit_hook(project_root: Path) -> tuple[bool, PreCommitStrategy, Path | None]`

Installs a trie-managed pre-commit hook into a project's `.git/hooks/pre-commit` file using one of three strategies: skipping silently when a pre-commit framework configuration is already present ("framework"), appending a marker-fenced shell block that runs lock-check, verify, and digest refresh steps when a `.git` directory exists ("git_hook", idempotent on repeated calls), or doing nothing when no `.git` directory is found ("none"). Returns a tuple of (installed, strategy, hook_path) describing the outcome.
<!-- trie:end -->
<!-- trie:section symbol=trie/init:init_project fingerprint=8d32d68da2ffa430f2ff755cfab94b08979379fa9364f896a299dffdecad2d3a body_fp=d68b7238aba745a9bfa4725268c0d9c6b0f873b31f2ceaa186019b40b7e34962 source_ref=2c03dbb203a0074b0a5d9c3a83ed9291f6d2df11 role=orchestration -->
## `def init_project( root: Path, *, force: bool = False, install_hooks: bool = False, run_scan: bool = True, ) -> InitResult`

Initialise trie in a directory, creating configuration and optionally scanning for symbols.

- `force`: bypass supported-project detection and overwrite existing configuration
- `install_hooks`: install pre-commit hooks to run `trie verify`
- `run_scan`: perform initial symbol scan to populate the graph database
- Raises `InitError` if directory is not a supported project or configuration exists
<!-- trie:end -->