---
trie_version: 0.1.5
source: trie/scope.py
file_fingerprint: 1b638c9f8e9743015b5553ea9d7079bb89a43773f0324dbe991a9c8ea263bedd
last_synced_at: '2026-06-03T20:46:49Z'
defines:
- kind: module
  qualified_name: trie/scope:__module__
  lines: 1-88
- kind: function
  qualified_name: trie/scope:_compiled
  lines: 13-20
- kind: function
  qualified_name: trie/scope:_matches
  lines: 23-25
- kind: function
  qualified_name: trie/scope:_dir_is_pruned
  lines: 28-47
- kind: function
  qualified_name: trie/scope:discover_files
  lines: 50-87
incoming_refs: 16
outgoing_refs: 0
---
<!-- trie:section symbol=trie/scope:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=c91d4962c75a0f92b924660595497f89f7cd4b3b54330b21c344627507ef2d78 source_ref=e4bcb4b8e83b584c506a6b0265fd3d4aa747e920 role=config-management -->
Provides file discovery utilities for filtering project files by glob patterns.

- Uses pathlib glob semantics where `**` matches any number of directory segments
- Prunes excluded directories before traversal to avoid scanning large vendored trees
- Returns absolute paths sorted lexicographically
<!-- trie:end -->
<!-- trie:section symbol=trie/scope:_compiled fingerprint=bc56d15c32090793e00a2cbc1877b117665e205f6ad0b442107eea10a6ed7e30 body_fp=706a814e70e190610355835e824d2a43767bab8d24a570a0e7106ee0507b5919 source_ref=e4bcb4b8e83b584c506a6b0265fd3d4aa747e920 role=config-management -->
Compiles a pathlib-style glob pattern to a regex with pathlib-compatible `**` semantics.

- Uses `glob.translate(..., recursive=True)` to ensure `**` matches zero or more directory segments
- Results are cached with LRU cache (maxsize=512) to avoid recompilation
<!-- trie:end -->
<!-- trie:section symbol=trie/scope:_matches fingerprint=692f4e55474c08ccc5dfbd896ee9ba36f5b33309eabefd0ff4471fc9a101f9e9 body_fp=bc123a107c3585988a152d135f2324a98b12de0d400f21874e2e2e8b5cbe94f3 source_ref=e4bcb4b8e83b584c506a6b0265fd3d4aa747e920 role=config-management -->
Returns True if the project-relative POSIX path matches a pathlib-style glob pattern.
<!-- trie:end -->
<!-- trie:section symbol=trie/scope:_dir_is_pruned fingerprint=80113400cd112fd80435d2bbd9d70dc9969f244deb8d6f6c950e6e19d356082a body_fp=e0eb6c696b9073a14391e86cc0b28ff4ad1e1a27d3389503f189d64a74d0230b source_ref=e4bcb4b8e83b584c506a6b0265fd3d4aa747e920 role=config-management -->
Returns True if the directory path matches any exclude pattern that would prune its entire subtree.

- Checks patterns ending in `/**` by stripping the suffix and matching the container directory
- Also matches bare directory patterns that exclude the directory itself
<!-- trie:end -->
<!-- trie:section symbol=trie/scope:discover_files fingerprint=c362744eb909798f47967d66c51bbc6433b2f501863cd4b27eae78a4ee9349e2 body_fp=2f56b102e75cad9eaea691594b7574d93e6a7f3f49256c0f63a62c2814f58f78 source_ref=e4bcb4b8e83b584c506a6b0265fd3d4aa747e920 role=config-management -->
Returns absolute paths of files under project_root matching scope include patterns and not excluded.

- Prunes excluded directories before traversal to avoid scanning large ignored subtrees
- Uses pathlib glob semantics where `**` matches any number of directory segments
<!-- trie:end -->