---
trie_version: 0.1.9
source: tests/test_workflow_install.py
file_fingerprint: 972d03637e97293d6ab0b344e43229c88ede3749c4d1ff2abf70d82a94f80581
last_synced_at: '2026-07-25T11:30:43Z'
defines:
- kind: module
  qualified_name: tests/test_workflow_install:__module__
  lines: 1-91
- kind: function
  qualified_name: tests/test_workflow_install:_git_repo
  lines: 13-15
- kind: function
  qualified_name: tests/test_workflow_install:test_render_bakes_in_diffs_dir_and_marker
  lines: 18-27
- kind: function
  qualified_name: tests/test_workflow_install:test_render_comments_every_pr_digest_not_just_latest
  lines: 30-44
- kind: function
  qualified_name: tests/test_workflow_install:test_install_creates_updates_unchanged
  lines: 47-63
- kind: function
  qualified_name: tests/test_workflow_install:test_install_never_touches_user_owned_file
  lines: 66-75
- kind: function
  qualified_name: tests/test_workflow_install:test_install_skips_outside_git_repo
  lines: 78-82
- kind: function
  qualified_name: tests/test_workflow_install:test_install_dry_run_writes_nothing
  lines: 85-90
incoming_refs: 0
outgoing_refs: 12
---
<!-- trie:section symbol=tests/test_workflow_install:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=f264262babba7522a0ddec7e716d25523a5a9ce3d2c4ce32101e58c3b21d0fd4 source_ref=1114060328a6896c14caf5ac33d5cf5b58fbfef8 role=test -->
Tests for `trie.workflow_install`, covering render output, install lifecycle (create/update/unchanged), user-owned file protection, non-git-repo skipping, and dry-run mode.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_workflow_install:_git_repo fingerprint=d9357e09960310a3aa68c6dfa9715c37f0fe5737c9e7724d4a8055ceef75a7cc body_fp=d44166225a72259142a76b220576e7f91399be694b132de5a02bdade8dbc3a88 source_ref=1114060328a6896c14caf5ac33d5cf5b58fbfef8 role=test -->
Create a minimal fake git repository by adding a `.git` directory inside `tmp_path` and returning it.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_workflow_install:test_render_bakes_in_diffs_dir_and_marker fingerprint=e30c3316a95418c2f25af1ac9b000bc2608cfcc595ab2f0cdc6477355e2ecd57 body_fp=9df764dc76da3965d9cd0dcfd0d056ce8047ddedd28f0aa2716a2ed80592a377 source_ref=1114060328a6896c14caf5ac33d5cf5b58fbfef8 role=test -->
Verify that `render_triediff_workflow` embeds the diffs dir, the workflow marker, and GitHub expression syntax; also checks trailing slash normalisation.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_workflow_install:test_render_comments_every_pr_digest_not_just_latest fingerprint=17a4d8af547a745a795b346cba9aa1acf79d5bfc94195aee9c1ed7898f12171e body_fp=c3f50cbb6315f6a3bf2907c3e578c8caf832d40d1cd2ebf3fb46fc05f7c3c694 source_ref=627f061096890d85cce4ef5f799c85e105f99a79 role=test -->
Assert that `render_triediff_workflow` emits a workflow that enumerates every PR-added digest file and comments each one, not only the newest.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_workflow_install:test_install_creates_updates_unchanged fingerprint=5ed1532cf5d64694f2368632acc0558fd1878c9369c8b8db7cd0f7d8cfa98fe3 body_fp=00e5962c10480652d08fc6072dc81eb64a5ce14eeb836819c230d4b5af79f168 source_ref=1114060328a6896c14caf5ac33d5cf5b58fbfef8 role=test -->
Verify `install_triediff_workflow` returns `"created"` on first run, `"unchanged"` on idempotent rerun, and `"updated"` when `diffs_dir` changes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_workflow_install:test_install_never_touches_user_owned_file fingerprint=6148020f65ecfcc2915615b03dd3ca9092c48b430379311d6931139deb7f4790 body_fp=f52119a81506a0ba7e8af95f47fe5e09eeac6a27eec014ef90fddd9ea4c10fd6 source_ref=1114060328a6896c14caf5ac33d5cf5b58fbfef8 role=test -->
Assert that `install_triediff_workflow` skips and leaves untouched a workflow file not bearing the managed marker.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_workflow_install:test_install_skips_outside_git_repo fingerprint=57fef1ea1c958dc6800ac6a8db6e0f34565beec07bd60d27b49f6960a37539c8 body_fp=0a3823b184dd01c05be8ecded279922500895bd267233b77dbc7db143199fc72 source_ref=1114060328a6896c14caf5ac33d5cf5b58fbfef8 role=test -->
Assert that `install_triediff_workflow` returns a `skipped` result and writes no file when the target directory is not a git repository.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_workflow_install:test_install_dry_run_writes_nothing fingerprint=820a646f45dfa30d8ad848addd444ed020f9bd507278c0f50abd84acd72b3b55 body_fp=c8c8fbe93099967f983340d88e17d0f0cea19b6d2f756b70c7e48ef7d5674772 source_ref=1114060328a6896c14caf5ac33d5cf5b58fbfef8 role=test -->
Assert that `install_triediff_workflow` with `dry_run=True` reports `"created"` but writes no file to disk.
<!-- trie:end -->