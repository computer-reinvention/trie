---
trie_version: 0.3.0
source: tests/test_git_helpers.py
file_fingerprint: f9b0feea8faa5462a9150bae40b56ac5d09e613f63fbcf4d7083712702cb57ff
last_synced_at: '2026-07-25T00:07:04Z'
description: Tests for the narrow git helpers used by diff-aware regen.
defines:
- kind: module
  qualified_name: tests/test_git_helpers:__module__
  lines: 1-306
- kind: function
  qualified_name: tests/test_git_helpers:_git
  lines: 22-24
  signature: 'def _git(args: list[str], cwd: Path) -> None'
- kind: function
  qualified_name: tests/test_git_helpers:_init_repo
  lines: 27-30
  signature: 'def _init_repo(path: Path) -> None'
incoming_refs: 0
outgoing_refs: 0
---
<!-- trie:section symbol=tests/test_git_helpers:__module__ fingerprint=7b508a0b69ba2077d06ed36962951d03e1b5de35b9270c9f620fcc497fcb4334 body_fp=935d7c8fc588b21c6a3a3e1213076dd69f0a3a086d3e2bd10e46daefd31e9d23 source_ref=1c54b4516222789ca66b19532c3dbee32df14674 role=test -->
Tests for narrow git helpers used by diff-aware regen, constructing real git repos to exercise subprocess interactions.

- Functions use real git commands in temporary directories rather than mocking subprocess
- Failure modes tested include missing repos, unreachable blobs, and malformed hashes
- `_git()` helper runs git with CI-safe identity configuration
- `_init_repo()` creates minimal test repositories with required user settings
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:_git fingerprint=403db8e372782e481e7267d4964ff6549c8310ffba151940399e7782b72013b6 body_fp=13dfc31ac1bfa7aced450eafa0a60f9618e7a34abc1fac9855d421905c80ea79 source_ref=6922d330926218a78e65a95d706a8038d95a55da role=test-infrastructure -->
## `def _git(args: list[str], cwd: Path) -> None`

Runs git commands in the specified directory with error checking and output capture.

- Used by test helper functions to execute git operations in temporary test repositories
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:_init_repo fingerprint=e6a8e59044cd4691a616ada677408e96c9c856caafae13744c548e08d2b462be body_fp=5a0960d1bcaad27129a04e01a4361adac1c24c6b34cd89918dff14f42764f95a source_ref=6922d330926218a78e65a95d706a8038d95a55da role=test-infrastructure -->
## `def _init_repo(path: Path) -> None`

Creates a git repository with test identity configuration at the specified path.
<!-- trie:end -->