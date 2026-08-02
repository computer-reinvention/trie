---
trie_version: 0.3.0
source: tests/test_intent_gate.py
file_fingerprint: c6b7991bd20e8c38745e6cc17ec3c3f4d9ad1c0eef6abc6b068d2f3ae64323fe
last_synced_at: '2026-07-29T23:17:26Z'
defines:
- kind: module
  qualified_name: tests/test_intent_gate:__module__
  lines: 1-200
- kind: function
  qualified_name: tests/test_intent_gate:_repo
  lines: 12-24
  signature: 'def _repo(tmp_path: Path) -> tuple[Config, Path]'
- kind: function
  qualified_name: tests/test_intent_gate:test_touched_symbols_semantic_changes_only
  lines: 27-44
  signature: 'def test_touched_symbols_semantic_changes_only(tmp_path: Path) -> None'
- kind: function
  qualified_name: tests/test_intent_gate:test_touched_symbols_sees_untracked_files_and_removals
  lines: 47-57
  signature: 'def test_touched_symbols_sees_untracked_files_and_removals(tmp_path: Path) -> None'
- kind: function
  qualified_name: tests/test_intent_gate:test_evaluate_coverage_from_pending_and_session_log
  lines: 60-89
  signature: 'def test_evaluate_coverage_from_pending_and_session_log(tmp_path: Path) -> None'
- kind: function
  qualified_name: tests/test_intent_gate:test_class_note_covers_its_methods
  lines: 92-133
  signature: 'def test_class_note_covers_its_methods(tmp_path: Path) -> None'
- kind: function
  qualified_name: tests/test_intent_gate:test_record_intent_reports_uncovered_symbols
  lines: 136-165
  signature: 'def test_record_intent_reports_uncovered_symbols(tmp_path: Path) -> None'
- kind: function
  qualified_name: tests/test_intent_gate:test_gate_is_silent_outside_git
  lines: 168-172
  signature: 'def test_gate_is_silent_outside_git(tmp_path: Path) -> None'
- kind: function
  qualified_name: tests/test_intent_gate:test_record_intent_empty_queue_still_reports_uncovered
  lines: 175-199
  signature: 'def test_record_intent_empty_queue_still_reports_uncovered(tmp_path: Path) -> None'
incoming_refs: 0
outgoing_refs: 19
---
<!-- trie:section symbol=tests/test_intent_gate:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=48fc5e12071387fc4977e174d8fbdc11d23878395a12a7372934c033f3b261fd source_ref=945539ac71d6c4a1e128b30da5bb269e87eddcdf role=test -->
Integration tests for `trie.intent_gate`, covering `touched_symbols` and `evaluate` against temporary git repositories.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_intent_gate:_repo fingerprint=5289f487410b7bdb1e8c13253084d6720e01fe1a829e7e36ed97d197ddf61526 body_fp=ae0459a030a93599ec8323e9820f50f7aaa99b0facb34b9bdabb676f4678f526 source_ref=945539ac71d6c4a1e128b30da5bb269e87eddcdf role=test -->
## `def _repo(tmp_path: Path) -> tuple[Config, Path]`

Initialize a temporary directory as a git repo with a default `Config`, `trie.toml`, and a two-function `mod.py` committed as the initial HEAD.

- Returns `(Config, Path)` — default config and the repo root path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_intent_gate:test_touched_symbols_semantic_changes_only fingerprint=571eee6552bfd1ada10b7048d3181c19c1acb1c47700d5883f6b35fda5ef3e73 body_fp=e866c4df6bfa4c2d85ebfecaaa830af520ecbb6fd32601e15cbb8a30dcccc9ee source_ref=12283969949cabe34de0812d48c53ab1ee7c7c4d role=test -->
## `def test_touched_symbols_semantic_changes_only(tmp_path: Path) -> None`

Assert that `touched_symbols` ignores formatting-only changes, detects semantic modifications and additions, and exempts import-level and unchanged symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_intent_gate:test_touched_symbols_sees_untracked_files_and_removals fingerprint=e4d133fc3c455c52e64415f965501b19736905108da1a76de4b6963dfa959415 body_fp=d7b788cecc09beba7dbd0227798a6485f51998bb011ff9c258e851743fcebf02 source_ref=12283969949cabe34de0812d48c53ab1ee7c7c4d role=test -->
## `def test_touched_symbols_sees_untracked_files_and_removals(tmp_path: Path) -> None`

Verify that `touched_symbols` reports untracked new files as `"added"` and deleted symbols as `"removed"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_intent_gate:test_evaluate_coverage_from_pending_and_session_log fingerprint=2176fe785d7443d41d719d8ed1479c0dc9f199d4dcf96f609fff6b928e0f712e body_fp=451923e830c8fe5dc8769914bf483a24e6e387bc85346a1e88110cca152a8eeb source_ref=2b83adb43e3b1d78f38bf0f77a8150c97c9638d7 role=test -->
## `def test_evaluate_coverage_from_pending_and_session_log(tmp_path: Path) -> None`

Verify that `evaluate` correctly tracks uncovered symbols as coverage is added via pending patch notes and applied (sealed) store patch rows.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_intent_gate:test_class_note_covers_its_methods fingerprint=b8fa1a8d88404cf78f481c49263617976756e225499992b67475956bca0d92e2 body_fp=4321534372c73e5508ad1236aa0dcf625c016721ecf93f7e3ded7c6e13400818 source_ref=a7a08e1e946842e9a20ea6b94c26c0530ef07fda role=test -->
## `def test_class_note_covers_its_methods(tmp_path: Path) -> None`

Assert that a patch note on a class covers all its methods, but a method note does not cover the class or sibling methods.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_intent_gate:test_record_intent_reports_uncovered_symbols fingerprint=10395894f7a4684448c77de40ca5f863cf0e2bc42bce56edd5cae31a6bfb0f39 body_fp=9bba36b46e76c3f778d161f971a3ee781f3152e55fc3935f99d2f02d2ed65435 source_ref=a7a08e1e946842e9a20ea6b94c26c0530ef07fda role=test -->
## `def test_record_intent_reports_uncovered_symbols(tmp_path: Path) -> None`

Verify that `record_intent` returns uncovered symbol names in the envelope and clears them once all touched symbols are noted.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_intent_gate:test_gate_is_silent_outside_git fingerprint=af9a0fc394ebd565d308889e9b1a8cb216b0820cad3c6599dccd031221817197 body_fp=072d3f4849adcc427f04f0554356b554705241c20b51b1f3d61d437ab3460c7a source_ref=12283969949cabe34de0812d48c53ab1ee7c7c4d role=test -->
## `def test_gate_is_silent_outside_git(tmp_path: Path) -> None`

Assert that `touched_symbols` returns an empty list when the given directory is not a Git repository.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_intent_gate:test_record_intent_empty_queue_still_reports_uncovered fingerprint=396c88b18c275494e82150e8bd699449c1f0361fbb2db690cb643992d1a44cf3 body_fp=96666bcd53fb15b7ec61bb208579388c4e83d0c459618ebf9536c2a8eb05619b source_ref=5148c4884c0ae6159f6587bd38df45463ccbe306 role=test -->
## `def test_record_intent_empty_queue_still_reports_uncovered(tmp_path: Path) -> None`

Verify that `record_intent` reports uncovered symbols even when the patch queue is empty, preventing silent early-return before commit time.
<!-- trie:end -->