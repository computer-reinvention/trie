---
trie_version: 0.1.9
source: trie/edits/backends/__init__.py
file_fingerprint: 7a4b16bb572d80035b28849b71df1f54c11208e2c6ac849ac41235c6017707ba
last_synced_at: '2026-07-25T01:56:30Z'
description: Pluggable per-symbol edit backends.
defines:
- kind: module
  qualified_name: trie/edits/backends/__init__:__module__
  lines: 1-59
- kind: constant
  qualified_name: trie/edits/backends/__init__:__all__
  lines: 16-24
- kind: function
  qualified_name: trie/edits/backends/__init__:make_backend
  lines: 27-58
incoming_refs: 0
outgoing_refs: 1
---
<!-- trie:section symbol=trie/edits/backends/__init__:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=c078e8d37b3bde3a39b0db13ec3d1f53f5e117fa0b4481e93f84a2c9eecd8df3 source_ref=bdd88e837a46b1e8bcf4e57bdba5c0d75c49bf83 role=api -->
Provides pluggable per-symbol edit backends with a single selection point through `make_backend`.

- Exports core interfaces (`EditRequest`, `EditResult`, `NeighbourCtx`, `SymbolEditBackend`) and concrete backends
- Currently supports LLM backend with planned OpenCode backend support
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/__init__:__all__ fingerprint=0a9c92b8a0355ed64e130aa0fc95db47038999ac9e2bece329e22329e90c4486 body_fp=109100540d036d70ed10a38be478a7db71aa3d73d55d69eb0b2d83f91d1c6c27 source_ref=bdd88e837a46b1e8bcf4e57bdba5c0d75c49bf83 role=config -->
Defines public API exports for the edit backends module, exposing core types, backend implementations, and factory function.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/backends/__init__:make_backend fingerprint=096396cc0b20349d59bd4ae53dc6024dcfa5b905a853964ec6d081ca26b56308 body_fp=7f1e74c92b338174965f33b14ec4883d9e0e8acde64ab5a76c8275c9b1f0b061 source_ref=2025ea943bcaf9f84636664a55cf591092214c1d role=orchestration -->
Constructs and returns a SymbolEditBackend instance based on configuration and optional overrides.

- `backend`: overrides config.edits.backend when provided
- `client`: reuses existing TrieClient instead of creating new one
- `model`: overrides config.models.edits for client creation
<!-- trie:end -->