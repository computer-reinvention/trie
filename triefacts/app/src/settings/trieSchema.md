---
trie_version: 0.1.9
source: app/src/settings/trieSchema.ts
file_fingerprint: a2e90679a55d6d21a56907443851aa606273c6b6b754be9f2d34c09e445d9420
last_synced_at: '2026-06-17T16:40:03Z'
defines:
- kind: type
  qualified_name: app/src/settings/trieSchema:TrieFieldType
  lines: 14-14
- kind: interface
  qualified_name: app/src/settings/trieSchema:TrieFieldDef
  lines: 16-29
- kind: constant
  qualified_name: app/src/settings/trieSchema:TRIE_MANAGED_TOP_KEYS
  lines: 33-42
- kind: constant
  qualified_name: app/src/settings/trieSchema:TRIE_FIELDS
  lines: 44-458
- kind: constant
  qualified_name: app/src/settings/trieSchema:TRIE_CATEGORIES
  lines: 460-460
- kind: function
  qualified_name: app/src/settings/trieSchema:trieFieldDef
  lines: 462-464
incoming_refs: 5
outgoing_refs: 0
---
<!-- trie:section symbol=app/src/settings/trieSchema:TrieFieldType fingerprint=9701df223c1b202d057e94548f287eda088f4038b4aa1aa0eca29984413f033c body_fp=10df9dfd23641d84066b8ad7e826118eb5e19a6981385b9a823071bdaff90d12 source_ref=e267d9b25f86987889e0b6ca05e32441db66cb8e role=model -->
Union type enumerating the six value kinds a `TrieFieldDef` field may represent.
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/trieSchema:TrieFieldDef fingerprint=7fe611b490e935dde95fea5e4481925d3184a28488cc57ba4524b9f571cd7142 body_fp=41447aea77a7e3a06b5c4b9b68b2868a828aeff7bf7167e8b37ffab908ecec68 source_ref=e267d9b25f86987889e0b6ca05e32441db66cb8e role=model -->
Describes a single editable trie.toml field exposed in the desktop Settings UI.

- `pointer` — dot-separated path into trie.toml used by the merge-writer to locate the key
- `default` — mirrors the authoritative default in `trie/config.py`; used to detect whether a value is unchanged so the key can be cleared rather than pinned
- `enum` — required when `type` is `"enum"`; each entry supplies a raw `value` and display `label`
- `min` / `max` / `step` — only meaningful when `type` is `"number"`
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/trieSchema:TRIE_MANAGED_TOP_KEYS fingerprint=c0ed2b3b886fd59d4debb0608164897a2e007aee893dfed027acbd080e3ebd5f body_fp=2747d0de33b70f1e356c3316abba3b17937874b032451d91989defebf5d8293d source_ref=e267d9b25f86987889e0b6ca05e32441db66cb8e role=config -->
Enumerate the top-level `trie.toml` table keys the desktop app manages; the merge-writer sends only these as the delta, leaving all other keys untouched.
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/trieSchema:TRIE_FIELDS fingerprint=5eafdafde7a1b21008c7fb9e362627ed73d531ec52d9777d0005b486b91a6114 body_fp=7b6dc7243437c2f25f8972876bb8e76b98a459b6e19eaad1a8a25319803bdd79 source_ref=e267d9b25f86987889e0b6ca05e32441db66cb8e role=config -->
Ordered array of all `TrieFieldDef` records describing every `trie.toml` key the desktop app exposes in Settings, grouped across categories: Scope, Triefacts, Models, Cascade, Sync, MCP, Edits, and Debug.
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/trieSchema:TRIE_CATEGORIES fingerprint=69ae291492eead0a85202575796a0a8edde091bb7eb4cd97efc46f024f34fb8b body_fp=142c48fedf959de5fa493166c3ab3c2114838bf93ed548efd16fe0afc071be29 source_ref=e267d9b25f86987889e0b6ca05e32441db66cb8e role=config -->
Ordered, deduplicated array of category strings derived from `TRIE_FIELDS`, preserving insertion order.
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/trieSchema:trieFieldDef fingerprint=c87bfe6e1e9a32d56ea4654323c968f8fe1feb505237cdf4169b8fa924304a79 body_fp=f7a1cff77012661feb61f868726ec70ab37b46a8ddcb40efe70e525cc63f36b1 source_ref=e267d9b25f86987889e0b6ca05e32441db66cb8e role=util -->
Look up a `TrieFieldDef` from `TRIE_FIELDS` by its dot-separated `pointer` string, returning `undefined` if not found.
<!-- trie:end -->