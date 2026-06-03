---
trie_version: 0.1.5
source: trie/init.py
file_fingerprint: 0a0f50d06e8a6f9d4f79bb977d3e2bd80e6beb28d3ea51ded39a2599aad8aeb4
last_synced_at: '2026-06-03T21:12:44Z'
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
incoming_refs: 36
outgoing_refs: 1
---
<!-- trie:section symbol=trie/init:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=95b8552fa69d3eff65de01deecb2317826321452b0dc87de2cc7fcf12d191a9f source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
Initializes trie projects by writing configuration, updating gitignore, and running initial scans.

- `InitResult`: dataclass capturing initialization outcomes including scan metrics and pre-commit setup
- `InitError`: exception raised when initialization fails due to missing Python project markers or existing config
- `_detect_python_project()`: identifies Python project markers like pyproject.toml or *.py files
- `_ensure_gitignore_entry()`: appends .trie/ to gitignore if not already present
- `install_pre_commit_hook()`: installs git hook running trie verify with framework detection
- `init_project()`: main initialization function with force override and optional scanning
<!-- trie:end -->
<!-- trie:section symbol=trie/init:GITIGNORE_LINE fingerprint=b9d82ba13e5468d46b74c1ca13f07a5f91362fb0734d7b6ae7a61507743b06ef body_fp=5d51e4b1a8e1755dfc8272187b8329a73317627aba076cb1fd99e812bb604ed2 source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
Gitignore entry string that excludes the `.trie/` directory from version control.
<!-- trie:end -->
<!-- trie:section symbol=trie/init:PreCommitStrategy fingerprint=870bb5512347025a866aba447ba3e81c76b145fd766f52f1539aedf49de39247 body_fp=1c0f2f326471c9360081d2eeedcec027215d40baef460fdb4b6c58abbfdd73c0 source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
Type alias defining the four possible pre-commit hook installation strategies.
<!-- trie:end -->
<!-- trie:section symbol=trie/init:PRE_COMMIT_HOOK_MARKER fingerprint=db5c85dbdc0d42aa74f25ae1b2955578c9c0d2e12d16c71615b3899b42eae1ef body_fp=cffacfbf3956982971b759a69f73e30588a98fefcd9c66a1b10b777f88d3faca source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
Comment string marking the start of trie's pre-commit hook block in `.git/hooks/pre-commit`.
<!-- trie:end -->
<!-- trie:section symbol=trie/init:PRE_COMMIT_HOOK_END_MARKER fingerprint=d0c3f84018a4b0fdae65792bc7130e5d78252bcf888b935afbcbb1162fee2ec0 body_fp=0895ada7bc149132af314e0d92132481cf71ef7930b58b73f120bdb8d753f4d3 source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
String constant marking the end of trie's pre-commit hook block in git hooks.
<!-- trie:end -->
<!-- trie:section symbol=trie/init:PRE_COMMIT_HOOK_BLOCK fingerprint=aea969236fa4acff5bd395cd7cda878d70e23fa931773656426cb6b6397e037e body_fp=cfccd35789699ee7020bb51cf59acb93375b6fb4d3e19278c3f879a9126e3ecf source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
Shell script block that checks for trie availability and runs lock-check and verify commands.

- Wrapped in marker comments for idempotent installation
- Degrades gracefully when trie is not on PATH
- Runs two validation steps: lock-check (prevents commits during ongoing writes) and verify (drift detection)
<!-- trie:end -->
<!-- trie:section symbol=trie/init:InitResult fingerprint=6159e79af9587c2f4c2280d80e815af142855cae81912c12db1958bb33088be7 body_fp=22b934ac643593344ab076a020e011cd3c7df79abe8c66349e5cf645293e5978 source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
Dataclass capturing the results of running `init_project`.

- `detected_markers`: Python project markers found (pyproject.toml, setup.py, etc.)
- `scan_files_total`: Number of Python files scanned for symbols
- `scan_symbols_total`: Number of symbols discovered during scan
- `scan_ran`: Whether the initial symbol scan was performed
- `pre_commit_installed`: Whether a new pre-commit hook was actually installed
- `pre_commit_strategy`: How pre-commit integration was handled
- `pre_commit_path`: Path to the pre-commit hook file if using git_hook strategy
<!-- trie:end -->
<!-- trie:section symbol=trie/init:InitError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=0608fb2467addf6ea99f2f342293f5ea72918d08d5ba1536e595d176171c39fd source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
Exception raised when project initialization fails due to validation errors or conflicts.
<!-- trie:end -->
<!-- trie:section symbol=trie/init:_detect_python_project fingerprint=d6552c9bad1130f26878d296aa1117bad09a3cd47ec50d67215c497e7f3de1eb body_fp=462b56136c095071268ace80a0f37ec8a026f2562d00906bd8bedaf1b0ebb8a1 source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
Detects Python project markers in a directory and returns their filenames as a list.

- Checks for standard files (pyproject.toml, setup.py, setup.cfg, requirements.txt) first
- Falls back to scanning for .py files at root level or one directory deep
- Returns empty list if no Python project indicators found
<!-- trie:end -->
<!-- trie:section symbol=trie/init:_ensure_gitignore_entry fingerprint=70d84e5eee964e2def6cf234ec4d0cf31e6e2f6ddb5176994fee2664237d2df1 body_fp=ec00e524ece61f7cd93620290e7d9278a8e032c3bda802430faa753d942433ff source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
Append `line` to `gitignore` if not already present, returning True if file changed.
<!-- trie:end -->
<!-- trie:section symbol=trie/init:install_pre_commit_hook fingerprint=15a712a6e65acf0735cc39913a4311a1400df95b8e6582502023ebf3bb2fd821 body_fp=00ddc45a00b10db599994ac3eddd99a839cfdc22393af1366f05937a03024f8f source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
Installs a pre-commit hook that runs `trie verify --quiet` using different strategies based on project setup.

- Returns tuple of (installed, strategy, hook_path) indicating installation outcome
- "framework" strategy: skips installation when `.pre-commit-config.yaml` exists  
- "git_hook" strategy: appends marker-fenced block to `.git/hooks/pre-commit`
- "none" strategy: no action when `.git` directory absent
<!-- trie:end -->
<!-- trie:section symbol=trie/init:init_project fingerprint=96c40ec7a1db079af60e0e7a3b69c77d33eb36824cd1f0838888f69fb647c494 body_fp=086ac1fb291668d5e50542898d926d28243cc22f4235f3f7f69c60e257be4c83 source_ref=56031699c017974cbab19a9a7bd7bae60bdca190 -->
Initialise trie in a directory, creating configuration and optionally scanning for symbols.

- `force`: bypass Python project detection and overwrite existing configuration
- `install_hooks`: install pre-commit hooks to run `trie verify`
- `run_scan`: perform initial symbol scan to populate the graph database
- Raises `InitError` if directory is not a Python project or configuration exists
<!-- trie:end -->