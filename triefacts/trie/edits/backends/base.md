---
trie_version: 0.1.9
source: trie/edits/backends/base.py
file_fingerprint: ffc813b8bd8b255e00e3b06c45bce2bd36484fbeec13b46183cc3e2e55b80178
last_synced_at: '2026-07-20T09:53:46Z'
description: The pluggable per-symbol edit backend seam.
defines:
- kind: module
  qualified_name: trie/edits/backends/base:__module__
  lines: 1-86
- kind: class
  qualified_name: trie/edits/backends/base:NeighbourCtx
  lines: 21-32
- kind: class
  qualified_name: trie/edits/backends/base:EditRequest
  lines: 36-53
- kind: class
  qualified_name: trie/edits/backends/base:EditResult
  lines: 57-78
- kind: class
  qualified_name: trie/edits/backends/base:SymbolEditBackend
  lines: 82-85
- kind: method
  qualified_name: trie/edits/backends/base:SymbolEditBackend.generate
  lines: 85-85
incoming_refs: 0
outgoing_refs: 0
---
<!-- trie:section symbol=trie/edits/backends/base:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=c46acbbb1d13825634b6521102a22063639f2fa0362780ceb03fc7050ef3ab3a source_ref=4c1df07d84035f809e84797956cafd68d221c059 role=api -->
Defines the pluggable interface between the edit pipeline and symbol generation backends.

- `NeighbourCtx`: Context about one caller or callee of the edit target
- `EditRequest`: Complete input specification for generating one symbol edit
- `EditResult`: Backend output containing new source code and documentation
- `SymbolEditBackend`: Protocol defining the pure `generate` method contract
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/base:NeighbourCtx fingerprint=d7e38f1c621f3209cd757c5bc518e5f63f63d861849b2a721b6333c08d931005 body_fp=41cb7848144bc3914e4b45e3924a56dbd2815800d9001c3f882c6686565aa3c1 source_ref=4c1df07d84035f809e84797956cafd68d221c059 role=model -->
Represents context information for a graph neighbour (caller or callee) of an edit target symbol.

- `qname`: Qualified name of the neighbour symbol
- `signature`: Function/method signature or type information for the neighbour
- `one_liner`: Optional brief description of the neighbour's purpose
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/base:EditRequest fingerprint=9e9e54864f85d94e02626a7a39da973588049df863f0094f71403e9c150d3c82 body_fp=ce6f2e17b4c13b42c48ad3c71bf9bda75c524c930cf1f54179b5e7e6ae14ff7f source_ref=4c1df07d84035f809e84797956cafd68d221c059 role=model -->
Contains all information needed by a backend to generate new source code and documentation for one symbol.

- `op`: operation type - "modify", "create", "delete", or "rename"
- `old_source`: empty string for create operations
- `merged_notes`: combined intent from patches
- `callees`: context about functions this symbol calls
- `callers`: context about functions that call this symbol
- `new_name`: only populated when op is "rename"
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/base:EditResult fingerprint=e53088cdbfe60c40a44bfd60e95b7b846af4575f37b5d8c1777c637e7a7d2cd3 body_fp=e6c6a825de2d5446154c50f9f51c473ef64dc57085bbcc38fba7c2d44a10c602 source_ref=637e986fe7f89d47636a3bd8e41f753ab033f7fc role=model -->
Contains the generated source code and prose returned by a backend for one symbol edit.

- `ok=False` with populated `error` indicates backend-level failure (no candidate produced)
- `ok=True` with broken code is allowed; downstream gates judge well-formedness
- `module_remarks`: free-text hints for imports/top-level changes; surfaced in `ApplyReport`, not applied
- `new_dependencies`: external package names introduced; deduped across batch and reported for agent to install
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/base:SymbolEditBackend fingerprint=af804fd3d4ad3e4113818da1a6aedee74a6f8605e89abbafea020d15f118c858 body_fp=3de43fb6ce4d965f292d9c3135645c6e4a2ce00670a3fcaa115428aa5ed789ca source_ref=4c1df07d84035f809e84797956cafd68d221c059 role=api -->
Protocol defining the interface for pluggable edit backends that generate symbol modifications.

- `generate`: Takes an EditRequest and returns an EditResult for one symbol modification
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/base:SymbolEditBackend.generate fingerprint=ab5df625bc76dbd4e163bed2dd888df828f90159bb93556525c31821b6541d46 body_fp=d433262a8e2f7bc16ef817153c3c7f2c91bce4f3ef56d7d2fe057dbb8e3ed301 source_ref=4c1df07d84035f809e84797956cafd68d221c059 role=api -->
SymbolEditBackend method that transforms an EditRequest into an EditResult for one symbol edit.
<!-- trie:end -->