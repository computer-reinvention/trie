---
trie_version: 0.1.9
source: trie/edits/backends/__init__.py
file_fingerprint: c13b3f1dda7644f4ce97b621e74739819410ea544b2216ee05fe14f983e258ea
last_synced_at: '2026-07-25T08:07:23Z'
description: Pluggable per-symbol edit backends.
defines:
- kind: module
  qualified_name: trie/edits/backends/__init__:__module__
  lines: 1-68
- kind: constant
  qualified_name: trie/edits/backends/__init__:__all__
  lines: 16-24
- kind: function
  qualified_name: trie/edits/backends/__init__:make_backend
  lines: 27-67
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
<!-- trie:section symbol=trie/edits/backends/__init__:make_backend fingerprint=caf10862a8825bf8943bbe7dae484901d22d86fe6130904a71246a33d14db8f9 body_fp=cc078b8ed109293557f308d999681e6239d20ddd171ab481235f8cfcb54f7d1b source_ref=3fb41e759d304113c0d373b6da08eaf0b2c91ea4 role=orchestration -->
Constructs and returns a SymbolEditBackend instance based on configuration and optional overrides.

- `backend`: overrides config.edits.backend when provided; defaults to `"record"` if unset
- `client`: reuses existing TrieClient instead of creating new one
- `model`: overrides config.models.edits for client creation
- Raises `ValueError` if resolved name is `"record"`, as that backend performs no generation
<!-- trie:end -->