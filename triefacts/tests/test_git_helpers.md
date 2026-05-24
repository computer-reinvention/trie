---
trie_version: 0.1.2
source: tests/test_git_helpers.py
file_fingerprint: f3dcec4ab08da1021c94f58ed56c75875b776e2d27a98e78a6ff7d672154f3f9
last_synced_at: '2026-05-23T23:52:32Z'
description: Tests for the narrow git helpers used by diff-aware regen.
defines:
- kind: module
  qualified_name: tests/test_git_helpers:__module__
  lines: 1-128
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
<!-- trie:section symbol=tests/test_git_helpers:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=660af60618ca653c73f8b38a2c42f4581fa5381cfc3b475ba54b4d754f8f79d3 source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `tests/test_git_helpers`

Test suite for `is_git_repo`, `compute_blob_hash`, and `retrieve_blob` using real git repositories created in `tmp_path`.

- Tests avoid subprocess mocking; all assertions exercise actual git behaviour.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:_git fingerprint=403db8e372782e481e7267d4964ff6549c8310ffba151940399e7782b72013b6 body_fp=31f9e44d14f4f82e3eed68043fbfcd52651040071fbcd32a66b5d9613cf1054c source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `_git(args: list[str], cwd: Path) -> None`

Run a `git` subprocess in `cwd`, raising on failure.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:_init_repo fingerprint=e6a8e59044cd4691a616ada677408e96c9c856caafae13744c548e08d2b462be body_fp=f9853f2f73811d7139ecbfcda27c0b4e18261a90fbb10808e33863cfc87349bd source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `_init_repo(path: Path) -> None`

Initialise a git repo at `path` with a fixed identity so commits succeed in CI sandboxes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:repo fingerprint=4866fbf9d304dab9bd4a33e890792c1ea71ef903933d6ab04a99b24be8e16e6a body_fp=b2a65c91951c7911c4c74c232f472b6d4e82556f769c8b6336b0f00614eb9208 source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `repo(tmp_path: Path) -> Path`

Pytest fixture that initialises a bare git repo in `tmp_path` and returns its path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_is_git_repo_true_inside_repo fingerprint=f035a2b1b05f9fa589c471a17deda0407412bdece3ae9d9306befd237d7c68c6 body_fp=0d7d5f44526528f90820128906a865734650353760081c115ab51f414e456dda source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `test_is_git_repo_true_inside_repo(repo: Path)`

Assert that `is_git_repo` returns `True` for a valid initialised git repository path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_is_git_repo_false_outside_repo fingerprint=f54ca20403df43eb511e5fb327df27e05c5956233df94c420661ad82896587be body_fp=7545800bb7ba3cd68271e64121a7249416ae0e21e69e714d72af879c4c538702 source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `test_is_git_repo_false_outside_repo(tmp_path: Path)`

Assert `is_git_repo` returns `False` for a plain directory with no git initialisation.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_compute_blob_hash_matches_git_hash_object fingerprint=67962e536e0bd0e5414bcdd9f7e62ccf0edcbce0cf210de021f08d7746b929ab body_fp=edf981deff7291396d48a58341a7b71cb8dfed84fee330fc4ff485c7116bac7a source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `test_compute_blob_hash_matches_git_hash_object(repo: Path)`

Assert that `compute_blob_hash` produces the same SHA-1 as `git hash-object` for the same file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_compute_blob_hash_is_content_addressed fingerprint=5dd5554fabeaaa27a592e21bc8c03037ae0e53a6489d66592e68c5b4af5913a5 body_fp=10b2f588c609e63f773320c3d528047768701a60cb9976ac9d4120dc6b103a30 source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `test_compute_blob_hash_is_content_addressed(repo: Path)`

Assert that `compute_blob_hash` returns identical hashes for files with identical content at different paths.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_compute_blob_hash_changes_when_content_changes fingerprint=81ca6ef8125cd827240e4d95d46d06acb5bbb43c955b39e7eb4ba517fca124d6 body_fp=78d5494a224e55cb15de3ebd0c5d1407eff212b49e97f31f47846e0bd9c58055 source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `test_compute_blob_hash_changes_when_content_changes(repo: Path)`

Assert that `compute_blob_hash` produces a different hash when a file's content is overwritten.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_compute_blob_hash_missing_file_returns_none fingerprint=4d866d334bbc0886d1d94d2b532be64b0f0d6975d5ff1cf65f741151a28d5714 body_fp=6f7e93b13e87898f5bed56c0913d5234441377585b4193a65e05ccd06e60e1bd source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `test_compute_blob_hash_missing_file_returns_none(repo: Path)`

Assert that `compute_blob_hash` returns `None` for a nonexistent file path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_retrieve_blob_round_trips_committed_content fingerprint=11ab68f853fc1dd92cfa558f5e000db888c572c2a12480b076f30c023fa33cbe body_fp=d96d88adcfdc478d4a803b7ce9cd0beabea0fd25af0ffd2655cf936d9e63814a source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `test_retrieve_blob_round_trips_committed_content(repo: Path)`

Verify that `retrieve_blob` returns the original content for a committed blob retrieved by its hash.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_retrieve_blob_unreachable_blob_returns_none fingerprint=a18a17d15a7d40ddf94db570112ce8404555d716cadc8093d64e4c81f5ded047 body_fp=1556f8b7307c80bddc5d14dc787e222205aee775fff52597093ceed537c9dbb3 source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `test_retrieve_blob_unreachable_blob_returns_none(repo: Path)`

Assert that `retrieve_blob` returns `None` when a blob hash was computed but never written to the git object database.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_retrieve_blob_malformed_hash_returns_none fingerprint=2d4a160e495f72e3921f579fd83cec0aaf2d7cd150f75a3b7afbdf477ea20bf5 body_fp=bb2fb832c53910b7b89a3fd49bd91bd030353096cbfca2eb11a9cb07d87ddef8 source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `test_retrieve_blob_malformed_hash_returns_none(repo: Path)`

Assert that `retrieve_blob` returns `None` for malformed, empty, or truncated hash strings.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_retrieve_blob_outside_repo_returns_none fingerprint=8a94fd40b788ea22ff0e2768dbb5fe50bfc5a11997f7e70f235204839dff3195 body_fp=db518ea2824a5c762f5cc1d413019d3ced5e7015acde9264db72530504121ef8 source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `test_retrieve_blob_outside_repo_returns_none(tmp_path: Path)`

Assert that `retrieve_blob` returns `None` when called outside a git repository with a valid-shaped 40-character hash.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_compute_blob_hash_outside_repo_returns_none fingerprint=e0c44ccc0765e2f01a9db5b7f7472eaf49d1e437d43767b50938a19402f8c317 body_fp=50ae3aecfca1c4bf2330506860ab4bf6465482c4c7dfd9e4ce364ebb0853e44f source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
## `test_compute_blob_hash_outside_repo_returns_none(tmp_path: Path)`

Assert that `compute_blob_hash` returns `None` when called outside a git repository.
<!-- trie:end -->