---
trie_version: 0.1.5
source: trie/edits/backends/fake.py
file_fingerprint: 76e78a6cdf5abaf7fe49d73578036333d95796d23fdbc9a6417661a97b04bea6
last_synced_at: '2026-06-09T09:25:19Z'
description: Deterministic edit backend for tests.
defines:
- kind: module
  qualified_name: trie/edits/backends/fake:__module__
  lines: 1-58
- kind: constant
  qualified_name: trie/edits/backends/fake:_MARKER
  lines: 20-20
- kind: class
  qualified_name: trie/edits/backends/fake:FakeBackend
  lines: 23-57
- kind: method
  qualified_name: trie/edits/backends/fake:FakeBackend.__init__
  lines: 24-31
- kind: method
  qualified_name: trie/edits/backends/fake:FakeBackend.generate
  lines: 33-57
incoming_refs: 0
outgoing_refs: 0
---
<!-- trie:section symbol=trie/edits/backends/fake:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=b3cdc48c17026a413b1b543cd5522b6ed9be1f499c2e075eb19e85778e41a275 source_ref=2700505cf5e68eb718fb1786893850aeff90d003 role=test -->
Provides a deterministic edit backend for testing that simulates different edit outcomes without LLM calls.

- **passthrough**: returns source unchanged
- **append**: adds marker comment to source  
- **broken**: returns invalid syntax for compile testing
- **fail**: returns failure result for error handling tests
- **per_qname**: allows symbol-specific mode overrides
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/fake:_MARKER fingerprint=b0bc33c20d395adfec4ac274b6c4a72b6881b344a6d7ebdebe7cd06b53229ffb body_fp=409dea179c151a9f982562b43679b215e3325ebb557375b3af2adace24af9740 source_ref=2700505cf5e68eb718fb1786893850aeff90d003 role=util -->
String constant containing a comment line appended by FakeBackend in "append" mode.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/fake:FakeBackend fingerprint=bc6b99ce4556dd7c44c3c8dfd6b95e41c6a44a04c5bbb52714c56b48ba1224ab body_fp=f2379fed7b35613f81c22e07b733bbd7c7ed5981f13570d515bb656cd57739f1 source_ref=2700505cf5e68eb718fb1786893850aeff90d003 role=test -->
Deterministic edit backend for testing that generates predictable EditResults without LLM calls.

- mode: Controls behavior - "passthrough" (no-op), "append" (adds marker), "broken" (invalid syntax), "fail" (returns failure)
- per_qname: Override mode for specific qualified names
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/fake:FakeBackend.__init__ fingerprint=d775149011872238e192f9a80b17888d617a5bd1b069e72d02c0ad147ed637bc body_fp=de55c134108e442f435c676739e912a1c5ad048627e52c1cabd0b591281c5c94 source_ref=2700505cf5e68eb718fb1786893850aeff90d003 role=model -->
Initializes FakeBackend with a default edit mode and optional per-symbol mode overrides.

- `mode`: default behavior for all symbols ("passthrough", "append", "broken", "fail")
- `per_qname`: maps qualified names to specific modes, overriding the default
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/fake:FakeBackend.generate fingerprint=e54aed683bf15bbc7f5a8f4143ee69cd4321d4e819415ae571311ca0d3add0ec body_fp=277fcb05b07d0691b8fd2dfa150d5b94bd31038f04c5bdc622fd84fef41ce0a4 source_ref=2700505cf5e68eb718fb1786893850aeff90d003 role=domain -->
FakeBackend.generate returns deterministic EditResult based on configured mode for testing edit pipeline.

- "fail" mode returns ok=False with error message
- "broken" mode returns syntactically invalid source code
- "create" op always synthesizes valid function definition regardless of mode
- "append" mode adds marker comment to existing source
- "passthrough" mode returns unchanged old_source
<!-- trie:end -->