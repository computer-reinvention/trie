---
trie_version: 0.1.9
source: tests/test_intent_gate.py
file_fingerprint: 434132f37bb13a0dc27d4ff6e97b3b829ecf8f9a18eb6b7feadc5d55c6f81131
last_synced_at: '2026-07-25T11:36:47Z'
defines:
- kind: module
  qualified_name: tests/test_intent_gate:__module__
  lines: 1-101
- kind: function
  qualified_name: tests/test_intent_gate:_repo
  lines: 13-25
- kind: function
  qualified_name: tests/test_intent_gate:test_touched_symbols_semantic_changes_only
  lines: 28-45
- kind: function
  qualified_name: tests/test_intent_gate:test_touched_symbols_sees_untracked_files_and_removals
  lines: 48-58
- kind: function
  qualified_name: tests/test_intent_gate:test_evaluate_coverage_from_pending_and_session_log
  lines: 61-93
- kind: function
  qualified_name: tests/test_intent_gate:test_gate_is_silent_outside_git
  lines: 96-100
incoming_refs: 0
outgoing_refs: 9
---
<!-- trie:section symbol=tests/test_intent_gate:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=48fc5e12071387fc4977e174d8fbdc11d23878395a12a7372934c033f3b261fd source_ref=945539ac71d6c4a1e128b30da5bb269e87eddcdf role=test -->
Integration tests for `trie.intent_gate`, covering `touched_symbols` and `evaluate` against temporary git repositories.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_intent_gate:_repo fingerprint=5289f487410b7bdb1e8c13253084d6720e01fe1a829e7e36ed97d197ddf61526 body_fp=42835391de9c245d732e9677cf676b2917fb29b287ac804b47e8a2a5efb9b1bc source_ref=945539ac71d6c4a1e128b30da5bb269e87eddcdf role=test -->
Initialize a temporary directory as a git repo with a default `Config`, `trie.toml`, and a two-function `mod.py` committed as the initial HEAD.

- Returns `(Config, Path)` — default config and the repo root path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_intent_gate:test_touched_symbols_semantic_changes_only fingerprint=571eee6552bfd1ada10b7048d3181c19c1acb1c47700d5883f6b35fda5ef3e73 body_fp=e6b5e8af8a81a17953008623f6b2c5b43e08dbd04f291abff6c1171e1ec5ecea source_ref=12283969949cabe34de0812d48c53ab1ee7c7c4d role=test -->
Assert that `touched_symbols` ignores formatting-only changes, detects semantic modifications and additions, and exempts import-level and unchanged symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_intent_gate:test_touched_symbols_sees_untracked_files_and_removals fingerprint=e4d133fc3c455c52e64415f965501b19736905108da1a76de4b6963dfa959415 body_fp=6c27862dbbc1b59666d97ede49b46ea076887a679ce0263d485cf61b4bd2a6b3 source_ref=12283969949cabe34de0812d48c53ab1ee7c7c4d role=test -->
Verify that `touched_symbols` reports untracked new files as `"added"` and deleted symbols as `"removed"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_intent_gate:test_evaluate_coverage_from_pending_and_session_log fingerprint=8531c76b0d682904a8e462527a421019f471695210b72f58ed795c6ee85c902e body_fp=cd05965a80f6da6c6546f674e8e3c08e77e7ad34ceafd7321a2f72e653b03001 source_ref=12283969949cabe34de0812d48c53ab1ee7c7c4d role=test -->
Verify that `evaluate` correctly tracks uncovered symbols as coverage is added via pending patch notes and session-log entries.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_intent_gate:test_gate_is_silent_outside_git fingerprint=af9a0fc394ebd565d308889e9b1a8cb216b0820cad3c6599dccd031221817197 body_fp=7285d6d5f18bbb6caf0752e59fbc0f312b9c1176214e781172d0b82ca61ae777 source_ref=12283969949cabe34de0812d48c53ab1ee7c7c4d role=test -->
Assert that `touched_symbols` returns an empty list when the given directory is not a Git repository.
<!-- trie:end -->