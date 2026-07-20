---
trie_version: 0.1.9
source: trie/edits/backends/fake.py
file_fingerprint: cff35eb864a705df0b7e0211c4591cceb73d5dd7dd3203b0050ab2b07bc3fcd5
last_synced_at: '2026-07-20T09:53:55Z'
description: Deterministic edit backend for tests.
defines:
- kind: module
  qualified_name: trie/edits/backends/fake:__module__
  lines: 1-65
- kind: constant
  qualified_name: trie/edits/backends/fake:_MARKER
  lines: 20-20
- kind: class
  qualified_name: trie/edits/backends/fake:FakeBackend
  lines: 23-64
- kind: method
  qualified_name: trie/edits/backends/fake:FakeBackend.__init__
  lines: 24-31
- kind: method
  qualified_name: trie/edits/backends/fake:FakeBackend.generate
  lines: 33-64
incoming_refs: 2
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
<!-- trie:section symbol=trie/edits/backends/fake:FakeBackend fingerprint=a560664262f051cd77c9184bb72b8b781b1d9ad2d78665bf25714b1ca52e23bc body_fp=f2379fed7b35613f81c22e07b733bbd7c7ed5981f13570d515bb656cd57739f1 source_ref=c0297533d4c82b096edd5095e005cc59756e77b2 role=test -->
Deterministic edit backend for testing that generates predictable EditResults without LLM calls.

- mode: Controls behavior - "passthrough" (no-op), "append" (adds marker), "broken" (invalid syntax), "fail" (returns failure)
- per_qname: Override mode for specific qualified names
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/fake:FakeBackend.__init__ fingerprint=d775149011872238e192f9a80b17888d617a5bd1b069e72d02c0ad147ed637bc body_fp=de55c134108e442f435c676739e912a1c5ad048627e52c1cabd0b591281c5c94 source_ref=2700505cf5e68eb718fb1786893850aeff90d003 role=model -->
Initializes FakeBackend with a default edit mode and optional per-symbol mode overrides.

- `mode`: default behavior for all symbols ("passthrough", "append", "broken", "fail")
- `per_qname`: maps qualified names to specific modes, overriding the default
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/fake:FakeBackend.generate fingerprint=37b6c6adf23cd07d65deb15f2453a1c68aaca2b9bebb8dfe5af34b3ab614ad82 body_fp=0fd1d5f8ad70441942277363fb6aa8848bcbc42afc4cfd8555502a61ac9184d6 source_ref=c0297533d4c82b096edd5095e005cc59756e77b2 role=test -->
FakeBackend.generate returns deterministic EditResult based on configured mode for testing edit pipeline.

- "fail" mode returns ok=False with error message
- "broken" mode returns syntactically invalid source code
- "create" op always synthesizes valid function definition regardless of mode; method qnames (containing ".") get a `self` param
- "append" mode adds marker comment to existing source
- "passthrough" mode returns unchanged old_source
<!-- trie:end -->