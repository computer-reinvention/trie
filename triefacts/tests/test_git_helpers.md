---
trie_version: 0.1.5
source: tests/test_git_helpers.py
file_fingerprint: f3dcec4ab08da1021c94f58ed56c75875b776e2d27a98e78a6ff7d672154f3f9
last_synced_at: '2026-06-06T13:19:25Z'
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
<!-- trie:section symbol=tests/test_git_helpers:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=935d7c8fc588b21c6a3a3e1213076dd69f0a3a086d3e2bd10e46daefd31e9d23 source_ref=6922d330926218a78e65a95d706a8038d95a55da role=test-infrastructure -->
Tests for narrow git helpers used by diff-aware regen, constructing real git repos to exercise subprocess interactions.

- Functions use real git commands in temporary directories rather than mocking subprocess
- Failure modes tested include missing repos, unreachable blobs, and malformed hashes
- `_git()` helper runs git with CI-safe identity configuration
- `_init_repo()` creates minimal test repositories with required user settings
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:_git fingerprint=403db8e372782e481e7267d4964ff6549c8310ffba151940399e7782b72013b6 body_fp=456e6cfb8d9ba31dd0c57bf8fc2c04c613a8faa01cd775dadf76d216b0d12c59 source_ref=6922d330926218a78e65a95d706a8038d95a55da role=test-infrastructure -->
Runs git commands in the specified directory with error checking and output capture.

- Used by test helper functions to execute git operations in temporary test repositories
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:_init_repo fingerprint=e6a8e59044cd4691a616ada677408e96c9c856caafae13744c548e08d2b462be body_fp=aaf70ef95d1b8cb5b95b856419a49382ff73e58b47a072c10d48aa45aafb6198 source_ref=6922d330926218a78e65a95d706a8038d95a55da role=test-infrastructure -->
Creates a git repository with test identity configuration at the specified path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:repo fingerprint=4866fbf9d304dab9bd4a33e890792c1ea71ef903933d6ab04a99b24be8e16e6a body_fp=8292ec1999740e52a96f739b7780c48aace1af321d1eb9c1f6c866b492f080d6 source_ref=6922d330926218a78e65a95d706a8038d95a55da role=test-infrastructure -->
Creates a pytest fixture that initializes a temporary git repository for testing.

- Returns the path to the initialized git repository
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_is_git_repo_true_inside_repo fingerprint=f035a2b1b05f9fa589c471a17deda0407412bdece3ae9d9306befd237d7c68c6 body_fp=47e1cbe7917229ecf228a4d83a60c43f7ca1245c201592a3bac1871014e5395e source_ref=6922d330926218a78e65a95d706a8038d95a55da role=change-detection -->
Verifies that `is_git_repo` returns `True` when called on a valid git repository path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_is_git_repo_false_outside_repo fingerprint=f54ca20403df43eb511e5fb327df27e05c5956233df94c420661ad82896587be body_fp=fc292cc4516732a7cb175d7a9a9f2339285f8f259bcd77a2cb9f791bbc8917bd source_ref=6922d330926218a78e65a95d706a8038d95a55da role=test-infrastructure -->
Verifies that `is_git_repo` returns False when called on a non-git directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_compute_blob_hash_matches_git_hash_object fingerprint=67962e536e0bd0e5414bcdd9f7e62ccf0edcbce0cf210de021f08d7746b929ab body_fp=3b221cb27f3f2a00ad648554a14e78663503caa387c7783f24aedfa86ebc6e04 source_ref=6922d330926218a78e65a95d706a8038d95a55da role=test-infrastructure -->
Verifies that `compute_blob_hash` produces identical output to `git hash-object` for the same file content.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_compute_blob_hash_is_content_addressed fingerprint=5dd5554fabeaaa27a592e21bc8c03037ae0e53a6489d66592e68c5b4af5913a5 body_fp=6bda29c8a970f494c4820f3414962e9ae2aa67fb256d1c63e86049deb8b46575 source_ref=6922d330926218a78e65a95d706a8038d95a55da role=test-infrastructure -->
Verifies that `compute_blob_hash` produces identical hashes for files with identical content in different paths.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_compute_blob_hash_changes_when_content_changes fingerprint=81ca6ef8125cd827240e4d95d46d06acb5bbb43c955b39e7eb4ba517fca124d6 body_fp=9bb66da1e9b3d1c851245ce45b037812ca5f3486a4200c854ce53506a96ec9bc source_ref=6922d330926218a78e65a95d706a8038d95a55da role=test-infrastructure -->
Verifies that compute_blob_hash produces different hashes when file content changes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_compute_blob_hash_missing_file_returns_none fingerprint=4d866d334bbc0886d1d94d2b532be64b0f0d6975d5ff1cf65f741151a28d5714 body_fp=7102b12360b60a82cb64d717a98c7e2e06d888930574d5fda12b381a4a26ef00 source_ref=6922d330926218a78e65a95d706a8038d95a55da role=test-infrastructure -->
Verifies compute_blob_hash returns None for non-existent files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_retrieve_blob_round_trips_committed_content fingerprint=11ab68f853fc1dd92cfa558f5e000db888c572c2a12480b076f30c023fa33cbe body_fp=106d93d365a5441d2f9d0b0a26cbb7b681eb46612207e6d220fb833ca2604db1 source_ref=6922d330926218a78e65a95d706a8038d95a55da role=test-infrastructure -->
Tests that `retrieve_blob` returns the original content when given a blob hash from a committed file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_retrieve_blob_unreachable_blob_returns_none fingerprint=a18a17d15a7d40ddf94db570112ce8404555d716cadc8093d64e4c81f5ded047 body_fp=dd66f4ab9f8b01341fd43b84cfb1afef729f52b5223abfe0b7afedb374a8ce78 source_ref=6922d330926218a78e65a95d706a8038d95a55da role=test-infrastructure -->
Tests that `retrieve_blob` returns `None` when given a valid hash for content that was never committed to the git object database.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_retrieve_blob_malformed_hash_returns_none fingerprint=2d4a160e495f72e3921f579fd83cec0aaf2d7cd150f75a3b7afbdf477ea20bf5 body_fp=9352aad5732f833b1d75d1c96d7af2d3454390f3c50d910735d0ec91f52d6ae8 source_ref=6922d330926218a78e65a95d706a8038d95a55da role=test-infrastructure -->
Verifies that `retrieve_blob` returns `None` when given malformed git blob hashes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_retrieve_blob_outside_repo_returns_none fingerprint=8a94fd40b788ea22ff0e2768dbb5fe50bfc5a11997f7e70f235204839dff3195 body_fp=b98c977a5fc7a6ce2ec5cfb538a359524e48ebc8d4d686de65122ec88b1f87a5 source_ref=6922d330926218a78e65a95d706a8038d95a55da role=change-detection -->
Tests that `retrieve_blob` returns None when called outside a git repository.

- Creates a valid 40-character SHA-1 hash format but uses a non-repository path
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_compute_blob_hash_outside_repo_returns_none fingerprint=e0c44ccc0765e2f01a9db5b7f7472eaf49d1e437d43767b50938a19402f8c317 body_fp=a8f51767eb8ada0034e1bbdeb622731922f75ec8b84d02075257bfdfcb5efdda source_ref=6922d330926218a78e65a95d706a8038d95a55da role=test-infrastructure -->
Verifies that `compute_blob_hash` returns None when called outside a git repository.
<!-- trie:end -->















