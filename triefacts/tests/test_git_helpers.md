---
trie_version: 0.1.5
source: tests/test_git_helpers.py
file_fingerprint: f3dcec4ab08da1021c94f58ed56c75875b776e2d27a98e78a6ff7d672154f3f9
last_synced_at: '2026-06-03T20:56:17Z'
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
<!-- trie:section symbol=tests/test_git_helpers:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=72968d5a1330152c64caffe60fc1b6df1725131301856365bea8c02fde6cb24e source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
Tests for git helper functions that interact with real git repositories via subprocess.

- Constructs actual git repos in tmp_path to test real git behavior
- Tests blob hash computation, git repo detection, and blob retrieval
- Does not mock subprocess calls to exercise authentic failure modes
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:_git fingerprint=403db8e372782e481e7267d4964ff6549c8310ffba151940399e7782b72013b6 body_fp=95042b47b3a99f35df95fd48e43405f43c416dac8857c5f7ac68e3e52097023d source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
Runs git subprocess with given arguments in specified directory, capturing output and raising on failure.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:_init_repo fingerprint=e6a8e59044cd4691a616ada677408e96c9c856caafae13744c548e08d2b462be body_fp=76feb6f10a89767f0eea7d8d3b426ba76d9160d005c1eacaf803693160b4109b source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
Initializes a git repository at the given path with default user configuration for testing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:repo fingerprint=4866fbf9d304dab9bd4a33e890792c1ea71ef903933d6ab04a99b24be8e16e6a body_fp=4e3ce5775f8ceaf18f31a5ab38f8c6cf4bf4fb6b93873f6cbe9989f7b46d1e76 source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
Creates a temporary git repository initialized with default user config for testing.

- Returns the path to the initialized repository directory
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_is_git_repo_true_inside_repo fingerprint=f035a2b1b05f9fa589c471a17deda0407412bdece3ae9d9306befd237d7c68c6 body_fp=f8ddb25ea00e6852e520772235b749a45901d44a76ea9ebc1acfb713f7a849dc source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
Verifies is_git_repo returns True when called on a directory containing a git repository.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_is_git_repo_false_outside_repo fingerprint=f54ca20403df43eb511e5fb327df27e05c5956233df94c420661ad82896587be body_fp=451dbe24a8b5316b29fbede8030773728179e6c238baf66c066c3275700191f7 source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
Tests that `is_git_repo` returns False for directories that are not git repositories.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_compute_blob_hash_matches_git_hash_object fingerprint=67962e536e0bd0e5414bcdd9f7e62ccf0edcbce0cf210de021f08d7746b929ab body_fp=f49a2f4be52bca5d2d83f7e2b1c0f0044df7023e13ee50058c3538772b7dfc3e source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
Verifies that `compute_blob_hash` returns the same hash as `git hash-object` for a test file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_compute_blob_hash_is_content_addressed fingerprint=5dd5554fabeaaa27a592e21bc8c03037ae0e53a6489d66592e68c5b4af5913a5 body_fp=5e52ca078508d5b8a4499a6ed7e21489557fb3c1444ef922842e1041025d014b source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
Verifies that compute_blob_hash generates identical hashes for files with identical content regardless of path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_compute_blob_hash_changes_when_content_changes fingerprint=81ca6ef8125cd827240e4d95d46d06acb5bbb43c955b39e7eb4ba517fca124d6 body_fp=2ff07fd2945dc976ea52523fdb3b1fd84dd1bbe574d14d3a0d47cdde90b634d8 source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
Verifies that `compute_blob_hash` returns different hashes when file content changes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_compute_blob_hash_missing_file_returns_none fingerprint=4d866d334bbc0886d1d94d2b532be64b0f0d6975d5ff1cf65f741151a28d5714 body_fp=5a299a5464562be5c03658426a86304aa9b75c139036a17ad87776dc45712bf2 source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
Verifies compute_blob_hash returns None when called on a nonexistent file path.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_retrieve_blob_round_trips_committed_content fingerprint=11ab68f853fc1dd92cfa558f5e000db888c572c2a12480b076f30c023fa33cbe body_fp=ad3f16d6087be6a809c7b3149aa71088e34d368b60f4d76602c4413ab5c1dbc6 source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
Tests that `retrieve_blob` returns committed file content when given the blob hash.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_retrieve_blob_unreachable_blob_returns_none fingerprint=a18a17d15a7d40ddf94db570112ce8404555d716cadc8093d64e4c81f5ded047 body_fp=d152154a49b68fe7c23a96c211e9d507f51dbf75f474119a3c579df92e02e5bf source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
Verifies that `retrieve_blob` returns None when attempting to fetch a blob hash that was never committed to the git object database.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_retrieve_blob_malformed_hash_returns_none fingerprint=2d4a160e495f72e3921f579fd83cec0aaf2d7cd150f75a3b7afbdf477ea20bf5 body_fp=2dc885a13f70daf6760d6f449595b8d43a9ff48338c037921b15f74a9bab5c21 source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
Tests that `retrieve_blob` returns None for invalid hash formats including non-hex strings, empty strings, and truncated hashes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_retrieve_blob_outside_repo_returns_none fingerprint=8a94fd40b788ea22ff0e2768dbb5fe50bfc5a11997f7e70f235204839dff3195 body_fp=01fd0dd363d1c0419661b1136061a4026d60fc16c7b6c1c1ea9f9df6a4fd11d3 source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
Tests that retrieve_blob returns None when called outside a git repository with a valid-shaped hash.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_git_helpers:test_compute_blob_hash_outside_repo_returns_none fingerprint=e0c44ccc0765e2f01a9db5b7f7472eaf49d1e437d43767b50938a19402f8c317 body_fp=a2707094e4f0b6735fccf43c1a2c7279995c64e77d7966830a7fbeaad09bba7c source_ref=6922d330926218a78e65a95d706a8038d95a55da -->
Tests that `compute_blob_hash` returns None when called outside a git repository.
<!-- trie:end -->