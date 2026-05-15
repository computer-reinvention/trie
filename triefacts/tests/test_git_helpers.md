---
trie_version: 0.1.0
source: tests/test_git_helpers.py
file_fingerprint: f3dcec4ab08da1021c94f58ed56c75875b776e2d27a98e78a6ff7d672154f3f9
last_synced_at: '2026-05-15T13:41:06Z'
description: Tests for the narrow git helpers used by diff-aware regen.
defines:
- kind: function
  qualified_name: tests/test_git_helpers:_git
  lines: 19-21
- kind: function
  qualified_name: tests/test_git_helpers:_init_repo
  lines: 24-27
- kind: function
  qualified_name: tests/test_git_helpers:repo
  lines: 31-33
- kind: function
  qualified_name: tests/test_git_helpers:test_is_git_repo_true_inside_repo
  lines: 36-37
- kind: function
  qualified_name: tests/test_git_helpers:test_is_git_repo_false_outside_repo
  lines: 40-42
- kind: function
  qualified_name: tests/test_git_helpers:test_compute_blob_hash_matches_git_hash_object
  lines: 45-56
- kind: function
  qualified_name: tests/test_git_helpers:test_compute_blob_hash_is_content_addressed
  lines: 59-65
- kind: function
  qualified_name: tests/test_git_helpers:test_compute_blob_hash_changes_when_content_changes
  lines: 68-74
- kind: function
  qualified_name: tests/test_git_helpers:test_compute_blob_hash_missing_file_returns_none
  lines: 77-78
- kind: function
  qualified_name: tests/test_git_helpers:test_retrieve_blob_round_trips_committed_content
  lines: 81-91
- kind: function
  qualified_name: tests/test_git_helpers:test_retrieve_blob_unreachable_blob_returns_none
  lines: 94-103
- kind: function
  qualified_name: tests/test_git_helpers:test_retrieve_blob_malformed_hash_returns_none
  lines: 106-109
- kind: function
  qualified_name: tests/test_git_helpers:test_retrieve_blob_outside_repo_returns_none
  lines: 112-115
- kind: function
  qualified_name: tests/test_git_helpers:test_compute_blob_hash_outside_repo_returns_none
  lines: 118-127
incoming_refs: 0
outgoing_refs: 13
---
<!-- trie:section symbol=tests/test_git_helpers:repo fingerprint=4866fbf9d304dab9bd4a33e890792c1ea71ef903933d6ab04a99b24be8e16e6a body_fp=8a2e7fdb5a44df2377bfa047badb5be48cfdc206361b2235863d3db222f5bda4 source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `repo(tmp_path: Path) -> Path`

Pytest fixture that initialises a bare-minimum git repo in `tmp_path` and returns its path.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_git_helpers:test_is_git_repo_true_inside_repo fingerprint=f035a2b1b05f9fa589c471a17deda0407412bdece3ae9d9306befd237d7c68c6 body_fp=7509d69f42ac34db0e70e782f2cca5c2575f78b513412ff597ea8617c70df456 source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `test_is_git_repo_true_inside_repo(repo: Path)`

Assert that `is_git_repo` returns `True` when called inside an initialised git repository.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_git_helpers:test_is_git_repo_false_outside_repo fingerprint=f54ca20403df43eb511e5fb327df27e05c5956233df94c420661ad82896587be body_fp=faaee2dc94ba8fc338980fb6f08ab21adbbdf2b848932d6a2775bfedab2f0eaf source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `test_is_git_repo_false_outside_repo(tmp_path: Path)`

Assert that `is_git_repo` returns `False` for a directory with no git repository initialised.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_git_helpers:test_compute_blob_hash_matches_git_hash_object fingerprint=67962e536e0bd0e5414bcdd9f7e62ccf0edcbce0cf210de021f08d7746b929ab body_fp=24a5c7659537b74ce9e2d3fe83347b84114cda281e5e214de5d1a22dc24b5fe9 source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `test_compute_blob_hash_matches_git_hash_object(repo: Path)`

Verify that `compute_blob_hash` produces the same SHA as `git hash-object` for a real file.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_git_helpers:test_compute_blob_hash_is_content_addressed fingerprint=5dd5554fabeaaa27a592e21bc8c03037ae0e53a6489d66592e68c5b4af5913a5 body_fp=9c1761acbea99916578ae116c5574057451e1a11f74e8f4a1a94572d000338df source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `test_compute_blob_hash_is_content_addressed(repo: Path)`

Assert that two files with identical content produce the same blob hash.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_git_helpers:test_compute_blob_hash_changes_when_content_changes fingerprint=81ca6ef8125cd827240e4d95d46d06acb5bbb43c955b39e7eb4ba517fca124d6 body_fp=0d7354b3b3675e74beda2d5c5adac8e2230d3b8ff80eb63043318d41fd6389b1 source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `test_compute_blob_hash_changes_when_content_changes(repo: Path)`

Assert that rewriting a file's content produces a different blob hash.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_git_helpers:test_compute_blob_hash_missing_file_returns_none fingerprint=4d866d334bbc0886d1d94d2b532be64b0f0d6975d5ff1cf65f741151a28d5714 body_fp=6f7e93b13e87898f5bed56c0913d5234441377585b4193a65e05ccd06e60e1bd source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `test_compute_blob_hash_missing_file_returns_none(repo: Path)`

Assert that `compute_blob_hash` returns `None` for a nonexistent file path.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_git_helpers:test_retrieve_blob_round_trips_committed_content fingerprint=11ab68f853fc1dd92cfa558f5e000db888c572c2a12480b076f30c023fa33cbe body_fp=2b581ae1477c93486a960f01e38c804c4abac2e8432a90a889b82fc9a535772e source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `test_retrieve_blob_round_trips_committed_content(repo: Path)`

Verify that a committed blob's content is retrievable via its hash using `retrieve_blob`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_git_helpers:test_retrieve_blob_unreachable_blob_returns_none fingerprint=a18a17d15a7d40ddf94db570112ce8404555d716cadc8093d64e4c81f5ded047 body_fp=92689a0d97151e96751296fde85a48129b4d11ea7225d5b55d93bf74af9a5ef5 source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `test_retrieve_blob_unreachable_blob_returns_none(repo: Path)`

Assert that `retrieve_blob` returns `None` for a hash computed but never written to the object database.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_git_helpers:test_retrieve_blob_malformed_hash_returns_none fingerprint=2d4a160e495f72e3921f579fd83cec0aaf2d7cd150f75a3b7afbdf477ea20bf5 body_fp=a7b200d4986aaba4f63bc1df285d3dabaf32c6434d5b28108d19e708811ff877 source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `test_retrieve_blob_malformed_hash_returns_none(repo: Path)`

Assert that `retrieve_blob` returns `None` for empty, non-hex, and truncated hash strings.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_git_helpers:test_retrieve_blob_outside_repo_returns_none fingerprint=8a94fd40b788ea22ff0e2768dbb5fe50bfc5a11997f7e70f235204839dff3195 body_fp=8417c0927316850135f53592cee1d68e89835e7cee45807dbc51dbb3544049c1 source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `test_retrieve_blob_outside_repo_returns_none(tmp_path: Path)`

Assert that `retrieve_blob` returns `None` when called outside a git repository, even with a well-formed 40-character hash.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_git_helpers:test_compute_blob_hash_outside_repo_returns_none fingerprint=e0c44ccc0765e2f01a9db5b7f7472eaf49d1e437d43767b50938a19402f8c317 body_fp=50ae3aecfca1c4bf2330506860ab4bf6465482c4c7dfd9e4ce364ebb0853e44f source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `test_compute_blob_hash_outside_repo_returns_none(tmp_path: Path)`

Assert that `compute_blob_hash` returns `None` when called outside a git repository.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_git_helpers:_git fingerprint=403db8e372782e481e7267d4964ff6549c8310ffba151940399e7782b72013b6 body_fp=6e15525727c23fc1bd344dc8d1bfc1d3212d12aea483347ec2b4a6694fe2d1f2 source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `_git(args: list[str], cwd: Path) -> None`

Run a `git` subprocess in `cwd`, injecting no extra config beyond what the shell provides.

- **`check=True`**: raises `CalledProcessError` on non-zero exit.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_git_helpers:_init_repo fingerprint=e6a8e59044cd4691a616ada677408e96c9c856caafae13744c548e08d2b462be body_fp=4747c14c52ba5d0c736b538ee435c1faef12957485894003a3254da1b08511c5 source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `_init_repo(path: Path) -> None`

Initialize a git repository at `path` with a `main` branch and test identity config.
<!-- trie:end -->