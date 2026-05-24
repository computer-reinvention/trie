---
trie_version: 0.1.2
source: trie/scope.py
file_fingerprint: 054b9955d944f35c87b1470e69533098f2d084f385d175c520128b2371d44638
last_synced_at: '2026-05-23T23:54:48Z'
defines:
- kind: module
  qualified_name: trie/scope:__module__
  lines: 1-36
- kind: function
  qualified_name: trie/scope:discover_files
  lines: 8-35
incoming_refs: 15
outgoing_refs: 0
---
<!-- trie:section symbol=trie/scope:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=9c0e0c64b1647e95fa0c1fdbbe48dc795c8958288462341511671e06a0a2759c source_ref=f8a23f982fb02a3a1ba2e235a94683e1984a2cd4 -->
## `trie/scope`

Provides file discovery filtered by include/exclude glob patterns from a `Scope` config.
<!-- trie:end -->
<!-- trie:section symbol=trie/scope:discover_files fingerprint=dcf6cef5f7f1965b7f70313f806c1e1e0168f483eaa0b6ac4448e2d1990c8edd body_fp=758ad8fe48a26bcb3b57cfee2b52e8f529a5f1acd9b9fdb6aa0856cb13c12913 source_ref=f8a23f982fb02a3a1ba2e235a94683e1984a2cd4 -->
## `discover_files(project_root: Path, scope: Scope) -> list[Path]`

Return sorted absolute paths of files matching `scope.include` glob patterns, minus any matched by `scope.exclude` patterns.

- `scope.exclude`: directory matches recursively exclude all files beneath them.
<!-- trie:end -->