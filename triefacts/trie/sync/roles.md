---
trie_version: 0.1.5
source: trie/sync/roles.py
file_fingerprint: 60be4163dc186100c413d972ab203f666cfcb0d8e01008745d63a2e0e957bb50
last_synced_at: '2026-06-10T13:17:08Z'
description: 'Roles-only sync: (re)infer the architectural role tag for every symbol
  without'
defines:
- kind: module
  qualified_name: trie/sync/roles:__module__
  lines: 1-226
- kind: class
  qualified_name: trie/sync/roles:RolesOnlyResult
  lines: 47-56
- kind: function
  qualified_name: trie/sync/roles:run_roles_only
  lines: 59-220
- kind: function
  qualified_name: trie/sync/roles:_section_prose
  lines: 223-225
incoming_refs: 5
outgoing_refs: 17
---
<!-- trie:section symbol=trie/sync/roles:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=9d9e4c1b62e37bc7574d67ccbdca0e7d6b1d029809ab31c109fb1c3ae791534c source_ref=2760a291866703b29ffecc33cfaae9e9cbba027c role=orchestration -->
Implements roles-only sync to infer and persist architectural role tags for symbols without regenerating documentation prose.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/roles:RolesOnlyResult fingerprint=89d4fecb4da79c89c332e55445fe49c83e3afdf884b61410edbe9f4d15049b25 body_fp=a962bee9d4170cefd1970c4119a483fcbacfda8e3e930a0349d99217b76366f9 source_ref=2760a291866703b29ffecc33cfaae9e9cbba027c role=model -->
Immutable result dataclass tracking counts and token usage from a roles-only sync operation.

- `files_processed`: number of triefact files updated with role classifications
- `symbols_classified`: number of symbols that received role inference calls
- `roles_changed`: number of symbols whose role tag actually changed
- `taxonomy_derived`: whether a new role taxonomy was generated (vs loaded from disk)
- `taxonomy_size`: number of roles in the taxonomy used for classification
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/roles:run_roles_only fingerprint=bcfbeab39e775eee9869f82052331db766409491fc96570ba0a5bd42f97bc7d4 body_fp=1bfca6606465de582892d8bf412b4a6fb44d78a014f96bcea578d99a5f9df34a source_ref=2760a291866703b29ffecc33cfaae9e9cbba027c role=orchestration -->
Infers and persists architectural role tags for all symbols with existing triefacts.

- `only_missing`: when True, only classifies symbols lacking a role tag
- `rederive_taxonomy`: when True, regenerates role vocabulary from scratch
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/roles:_section_prose fingerprint=c63c67b59dea8ec84377ed4cc2e137ff4dfea773f52192cb76ace40f686d9e10 body_fp=d382d92048c7b83441ef4057c93b6b283443562fcad71dad77de12d2d0fd4a47 source_ref=2760a291866703b29ffecc33cfaae9e9cbba027c role=util -->
Extracts the prose body from a triefact section by qualified name, returning None if not found.
<!-- trie:end -->