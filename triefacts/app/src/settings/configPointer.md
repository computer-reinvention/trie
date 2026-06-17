---
trie_version: 0.1.9
source: app/src/settings/configPointer.ts
file_fingerprint: c1b178de3b3d437a63376070038c9c78a7328ac7916b0748d543ab05f7bb722b
last_synced_at: '2026-06-17T16:39:39Z'
defines:
- kind: type
  qualified_name: app/src/settings/configPointer:Json
  lines: 6-6
- kind: function
  qualified_name: app/src/settings/configPointer:getPointer
  lines: 8-19
- kind: function
  qualified_name: app/src/settings/configPointer:setPointer
  lines: 23-34
- kind: function
  qualified_name: app/src/settings/configPointer:buildManagedDelta
  lines: 38-47
incoming_refs: 10
outgoing_refs: 0
---
<!-- trie:section symbol=app/src/settings/configPointer:Json fingerprint=193f4839518d0f5eabe96a6dc95b04eefbb128b2db55a3d41445f6b7a64b27f7 body_fp=b65a334059d47bbe58a3f2114034c30ce3926eca024517d0d9290adc0919c479 source_ref=a1daf626a857a0380517bb7c76ce6e03703a1cc9 role=model -->
Type alias representing any JSON-compatible value throughout the config pointer utilities.
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/configPointer:getPointer fingerprint=99af5d8514fcb8e5446586c0f771cafbfd074b4fe933127535fdce32e1f5dbb6 body_fp=22cacc1caf65ae43a824359e5079c1df63d30f040cc66d6cbaefaaa263ebdf08 source_ref=a1daf626a857a0380517bb7c76ce6e03703a1cc9 role=util -->
Traverse `obj` by dot-separated `pointer` and return the value found, or `undefined` if any segment is missing or non-traversable.
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/configPointer:setPointer fingerprint=a16d14174490f73b74caa4dce1dfba2491fa032c3ef8d22d627335dd003e1fa9 body_fp=23bcaf5987ff3dbc7f304ed2e932ab17f5936d9a438025d97f298d2f97079af2 source_ref=a1daf626a857a0380517bb7c76ce6e03703a1cc9 role=util -->
Set or delete the value at a dot-separated `pointer` within `obj`, creating intermediate objects as needed; mutates `obj` in place.

- `pointer`: dot-separated path string, e.g. `"a.b.c"`
- `value`: pass `undefined` to delete the key at the final path segment
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/configPointer:buildManagedDelta fingerprint=16d3a3cb4e8543a2c9421e309ab86a9727eafd026dc135f851785ee657d0920e body_fp=21594b221784fb30de6f3f626b88759dd36c9ec5f0b2299aa2abfcd3be60533d source_ref=a1daf626a857a0380517bb7c76ce6e03703a1cc9 role=util -->
Build a delta object for each managed top-level key, mapping it to its current value or `null` if absent.

- `managedTopKeys` — top-level keys the store is responsible for managing
- `null` signals the merge-writer to delete that key in `opencode.json`
<!-- trie:end -->