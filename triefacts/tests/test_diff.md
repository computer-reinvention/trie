---
trie_version: 0.1.5
source: tests/test_diff.py
file_fingerprint: d83d0840359a9c272308c62c367d58bffef9a016ff138381191538600ddfaa56
last_synced_at: '2026-06-03T21:18:35Z'
defines:
- kind: module
  qualified_name: tests/test_diff:__module__
  lines: 1-173
- kind: function
  qualified_name: tests/test_diff:project
  lines: 17-28
- kind: function
  qualified_name: tests/test_diff:test_diff_returns_empty_when_clean
  lines: 31-42
- kind: function
  qualified_name: tests/test_diff:test_diff_shows_regenerated_content
  lines: 45-73
- kind: function
  qualified_name: tests/test_diff:test_diff_writes_to_preview_dir
  lines: 76-93
- kind: function
  qualified_name: tests/test_diff:test_diff_respects_limit
  lines: 96-109
- kind: function
  qualified_name: tests/test_diff:test_diff_respects_budget
  lines: 112-126
- kind: function
  qualified_name: tests/test_diff:test_cli_sync_dry_run_routes_through_diff
  lines: 129-153
- kind: function
  qualified_name: tests/test_diff:test_cli_sync_dry_run_no_stale
  lines: 156-172
incoming_refs: 0
outgoing_refs: 30
---
<!-- trie:section symbol=tests/test_diff:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=8a5c1e54e8a14b26b73a841b05c551b0ade2acc273033838a16557edf974cd7b source_ref=6e1055a06b208b8b3b614db15da47304d012b68a -->
Tests for the diff functionality that compares current documentation state against regenerated content.

- `project`: Creates temporary test project with basic config and Python file
- Tests cover empty diffs when clean, showing changes when stale, preview directory usage, limit/budget constraints, and CLI dry-run behavior
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:project fingerprint=cd6f42afcf67cc71ef8f9decc80cf1252526bcf42bc7ac1d0055f21d53a8719b body_fp=b041ca925f7449984be48929cfbf62b43c74418899baea891895ce0274ecebd4 source_ref=6e1055a06b208b8b3b614db15da47304d012b68a -->
Creates a temporary project directory with trie.toml configuration and a sample Python file for testing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_diff_returns_empty_when_clean fingerprint=d2a7fa508081814258d613ec8b2872d7afd765927bf7186ab357128ee7f9bf0d body_fp=ed66bb542c97912920ef9e0b5a6de42e8ba50fdb675be860be8b8ce1464811e8 source_ref=6e1055a06b208b8b3b614db15da47304d012b68a -->
Verifies that diff_project returns empty diffs when triefacts are synchronized with source files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_diff_shows_regenerated_content fingerprint=89d814a6af063c4e94a927e1ad9a5d3ba321e11e78109c5408a5c8c3fdc11a86 body_fp=e622e713c6eb01591a65dd74be116668586950abd5e7ba11ce12bb044eea8210 source_ref=6e1055a06b208b8b3b614db15da47304d012b68a -->
Tests that diff_project detects stale triefacts and generates unified diffs showing old vs new content.

- Creates initial triefact with v1 content, modifies source to make it stale
- Verifies diff result contains unified diff with both v1 and v2 content
- Confirms preview file is written while canonical file remains unchanged
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_diff_writes_to_preview_dir fingerprint=6186a6b103b571bb8d221bc104bdbe3c8a225ebb2613b5d5158913e45b95d3e5 body_fp=284f0d5cdde4d433812603dd04323377d858591de393c3bb9620803f6e53068d source_ref=6e1055a06b208b8b3b614db15da47304d012b68a -->
Verifies that diff_project writes preview triefacts to `.trie/preview` directory without modifying canonical triefacts.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_diff_respects_limit fingerprint=71c42631990c386a9403ab70f96ea8d4074843ec7a0a344e69c56129512ea813 body_fp=d44eeb44930a679c8a4f0f0664597aff7409a62920da919b954be115bca32017 source_ref=6e1055a06b208b8b3b614db15da47304d012b68a -->
Verifies that diff_project respects the limit parameter by stopping after processing the specified number of files.

- Creates three source files (alpha, beta, gamma) to exceed the limit of 2
- Asserts exactly 2 diffs returned and at least 1 file skipped
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_diff_respects_budget fingerprint=95de6fbbd940c39eb444cde0d455543f20ea4616710b08dff6a0891436f92691 body_fp=f2b000a4bafbc8c53e5b4741376171f023902fd8b359a80c6f0b453487c82a2a source_ref=6e1055a06b208b8b3b614db15da47304d012b68a -->
Verifies that `diff_project` respects USD budget limits by stopping before processing all eligible files.

- Creates multiple source files to exceed tiny budget
- Asserts at least one diff generated but fewer than total files processed
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_cli_sync_dry_run_routes_through_diff fingerprint=010c932914ab38809bb11f22bd06bb023d694dfc73a6ae2319a8b5110c7f2bf6 body_fp=47efefc8791051983ae03e44582eafb4e126d355c9b9350ebddaa14b0735637b source_ref=6e1055a06b208b8b3b614db15da47304d012b68a -->
Tests that `trie sync --dry-run` shows unified diffs without modifying existing triefact files.

- Sets up stale triefact by modifying source after initial sync
- Verifies CLI outputs preview diffs and preserves original triefact content
<!-- trie:end -->
<!-- trie:section symbol=tests/test_diff:test_cli_sync_dry_run_no_stale fingerprint=d6f94373a6ce8ad7631f8fb0e92857adf69fbcb9fa419531cb8d56b4ef087435 body_fp=2c8fea52b3676f703e2d9ab52ff344ef07c45f7ddddaa54cae553c3ee41a5d79 source_ref=6e1055a06b208b8b3b614db15da47304d012b68a -->
Verifies that `trie sync --dry-run` reports "no stale triefacts" when all triefacts are current.
<!-- trie:end -->