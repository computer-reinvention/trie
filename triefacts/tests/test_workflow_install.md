---
trie_version: 0.3.0
source: tests/test_workflow_install.py
file_fingerprint: 15f2cfae1d0141748ee5eded6417189650e2599aac7d68410edbdb429912fcdf
last_synced_at: '2026-08-02T22:23:58Z'
defines:
- kind: module
  qualified_name: tests/test_workflow_install:__module__
  lines: 1-254
- kind: function
  qualified_name: tests/test_workflow_install:_git_repo
  lines: 13-15
  signature: 'def _git_repo(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_workflow_install:test_render_bakes_in_diffs_dir_and_marker
  lines: 18-27
  signature: def test_render_bakes_in_diffs_dir_and_marker() -> None
- kind: function
  qualified_name: tests/test_workflow_install:test_render_comments_every_pr_digest_not_just_latest
  lines: 30-44
  signature: def test_render_comments_every_pr_digest_not_just_latest() -> None
- kind: function
  qualified_name: tests/test_workflow_install:test_render_prettifies_digest_for_display_only
  lines: 47-131
  signature: def test_render_prettifies_digest_for_display_only() -> None
- kind: function
  qualified_name: tests/test_workflow_install:test_render_changes_table_preserves_full_summary_under_utf8_awk
  lines: 134-191
  signature: def test_render_changes_table_preserves_full_summary_under_utf8_awk() -> None
- kind: function
  qualified_name: tests/test_workflow_install:test_install_creates_updates_unchanged
  lines: 194-210
  signature: 'def test_install_creates_updates_unchanged(tmp_path: Path) -> None'
- kind: function
  qualified_name: tests/test_workflow_install:test_install_never_touches_user_owned_file
  lines: 213-222
  signature: 'def test_install_never_touches_user_owned_file(tmp_path: Path) -> None'
- kind: function
  qualified_name: tests/test_workflow_install:test_install_skips_outside_git_repo
  lines: 225-229
  signature: 'def test_install_skips_outside_git_repo(tmp_path: Path) -> None'
- kind: function
  qualified_name: tests/test_workflow_install:test_install_dry_run_writes_nothing
  lines: 232-237
  signature: 'def test_install_dry_run_writes_nothing(tmp_path: Path) -> None'
- kind: function
  qualified_name: tests/test_workflow_install:test_this_repos_installed_workflow_matches_the_template
  lines: 240-253
  signature: def test_this_repos_installed_workflow_matches_the_template() -> None
incoming_refs: 0
outgoing_refs: 16
---
<!-- trie:section symbol=tests/test_workflow_install:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=f264262babba7522a0ddec7e716d25523a5a9ce3d2c4ce32101e58c3b21d0fd4 source_ref=1114060328a6896c14caf5ac33d5cf5b58fbfef8 role=test -->
Tests for `trie.workflow_install`, covering render output, install lifecycle (create/update/unchanged), user-owned file protection, non-git-repo skipping, and dry-run mode.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_workflow_install:_git_repo fingerprint=d9357e09960310a3aa68c6dfa9715c37f0fe5737c9e7724d4a8055ceef75a7cc body_fp=bfb14d4c508e1b35c1864f712b0384f4fa6f119986137e0a2b7dd69e1b0fdc12 source_ref=1114060328a6896c14caf5ac33d5cf5b58fbfef8 role=test -->
## `def _git_repo(tmp_path: Path) -> Path`

Create a minimal fake git repository by adding a `.git` directory inside `tmp_path` and returning it.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_workflow_install:test_render_bakes_in_diffs_dir_and_marker fingerprint=e30c3316a95418c2f25af1ac9b000bc2608cfcc595ab2f0cdc6477355e2ecd57 body_fp=c725f1d8a66ae6ceabc39582e07b4134cd553553911a476bb1ec209ef4576edf source_ref=1114060328a6896c14caf5ac33d5cf5b58fbfef8 role=test -->
## `def test_render_bakes_in_diffs_dir_and_marker() -> None`

Verify that `render_triediff_workflow` embeds the diffs dir, the workflow marker, and GitHub expression syntax; also checks trailing slash normalisation.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_workflow_install:test_render_comments_every_pr_digest_not_just_latest fingerprint=17a4d8af547a745a795b346cba9aa1acf79d5bfc94195aee9c1ed7898f12171e body_fp=edafd54e07e5107e95e8adb429152eb15681876b70fd7d05cda9244808f8b5db source_ref=627f061096890d85cce4ef5f799c85e105f99a79 role=test -->
## `def test_render_comments_every_pr_digest_not_just_latest() -> None`

Assert that `render_triediff_workflow` emits a workflow that enumerates every PR-added digest file and comments each one, not only the newest.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_workflow_install:test_render_prettifies_digest_for_display_only fingerprint=0bf54e6e834e52710b10f4838408ff280ffa2e8f63566c1ece20934d990ad9c9 body_fp=040520698fdf0a3564e036bbddf71c853384bae6f95fef0c9fdd3138bb3bb595 source_ref=b9d5d98e7a2a488130878647fd48d47b8baae16b role=test -->
## `def test_render_prettifies_digest_for_display_only() -> None`

Extracts the embedded awk program from the rendered workflow YAML and runs it against a canonical digest to verify the display transform produces a Markdown table.

- Skips if `awk` is not on `PATH`.
- Asserts overflow records are folded into the table and bullet lines are removed.
- Asserts the auto-generated header comment is stripped from output.
- Asserts the Staged section passes through unmodified.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_workflow_install:test_render_changes_table_preserves_full_summary_under_utf8_awk fingerprint=3d96f81704fb24c9a28041d32008ee910b0cdd387d64deb6ff13820975ef0979 body_fp=0843e96216ce523c92b6aea01d981da3368d60d5a5acb76962c11eff3f3983a3 source_ref=22d94e809a1a8d520a82c9db799360a6a2c5e638 role=test -->
## `def test_render_changes_table_preserves_full_summary_under_utf8_awk() -> None`

Regression test: verifies the embedded awk formatter splits change-bullet summaries by `length(SEP)` rather than a hardcoded byte count, preserving leading characters under a UTF-8 locale.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_workflow_install:test_install_creates_updates_unchanged fingerprint=5ed1532cf5d64694f2368632acc0558fd1878c9369c8b8db7cd0f7d8cfa98fe3 body_fp=7456b0fa127de7a469d4536bcc5e36d6c9eb15f2c7722728457983c6a92f4260 source_ref=1114060328a6896c14caf5ac33d5cf5b58fbfef8 role=test -->
## `def test_install_creates_updates_unchanged(tmp_path: Path) -> None`

Verify `install_triediff_workflow` returns `"created"` on first run, `"unchanged"` on idempotent rerun, and `"updated"` when `diffs_dir` changes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_workflow_install:test_install_never_touches_user_owned_file fingerprint=6148020f65ecfcc2915615b03dd3ca9092c48b430379311d6931139deb7f4790 body_fp=97671a546406b34d5e8e567c0ace3bfd2016253fcfad1a9713acc19cfdbeca5e source_ref=1114060328a6896c14caf5ac33d5cf5b58fbfef8 role=test -->
## `def test_install_never_touches_user_owned_file(tmp_path: Path) -> None`

Assert that `install_triediff_workflow` skips and leaves untouched a workflow file not bearing the managed marker.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_workflow_install:test_install_skips_outside_git_repo fingerprint=57fef1ea1c958dc6800ac6a8db6e0f34565beec07bd60d27b49f6960a37539c8 body_fp=76a754e18f3e0d8b92be365dabbec93044d6191a1ad2374c70035df923d2e7b0 source_ref=1114060328a6896c14caf5ac33d5cf5b58fbfef8 role=test -->
## `def test_install_skips_outside_git_repo(tmp_path: Path) -> None`

Assert that `install_triediff_workflow` returns a `skipped` result and writes no file when the target directory is not a git repository.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_workflow_install:test_install_dry_run_writes_nothing fingerprint=820a646f45dfa30d8ad848addd444ed020f9bd507278c0f50abd84acd72b3b55 body_fp=0fab5ab92a28a1123fb6e699275586cd6a21ee466ea29625c9b6bfa62611dcbc source_ref=1114060328a6896c14caf5ac33d5cf5b58fbfef8 role=test -->
## `def test_install_dry_run_writes_nothing(tmp_path: Path) -> None`

Assert that `install_triediff_workflow` with `dry_run=True` reports `"created"` but writes no file to disk.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_workflow_install:test_this_repos_installed_workflow_matches_the_template fingerprint=b4b56a944939e4c78de6920c4e68b9e314ea138efd7b71b7ee7b6234e70f5749 body_fp=2ef5e5f48b8829fda843ef1459e434ad8f0d0dc7106d25e6217de6fd5777ab4b source_ref=28c3c1c92a110258ef7de761accedd8f2dc8463b role=test -->
## `def test_this_repos_installed_workflow_matches_the_template() -> None`

Assert that the committed `WORKFLOW_RELPATH` file in this repository's root exactly matches `render_triediff_workflow("triefacts/triediffs")`.

- Fails if the installed workflow and the rendered template have drifted; re-run `trie setup` to fix.
<!-- trie:end -->