---
trie_version: 0.1.9
source: app/src/agm/investigations.ts
file_fingerprint: cc2adaf018b7e7b542d98fa8e1dcd30e51bc2838d0a52b326945f28bb1bdae00
last_synced_at: '2026-06-17T16:35:58Z'
defines:
- kind: class
  qualified_name: app/src/agm/investigations:InvestigationRegistry
  lines: 13-71
- kind: property
  qualified_name: app/src/agm/investigations:InvestigationRegistry.byId
  lines: 14-14
- kind: property
  qualified_name: app/src/agm/investigations:InvestigationRegistry.activeId
  lines: 15-15
- kind: method
  qualified_name: app/src/agm/investigations:InvestigationRegistry.set
  lines: 18-42
- kind: method
  qualified_name: app/src/agm/investigations:InvestigationRegistry.get
  lines: 44-46
- kind: method
  qualified_name: app/src/agm/investigations:InvestigationRegistry.active
  lines: 48-50
- kind: method
  qualified_name: app/src/agm/investigations:InvestigationRegistry.all
  lines: 52-54
- kind: method
  qualified_name: app/src/agm/investigations:InvestigationRegistry.addNegativeEvidence
  lines: 57-60
- kind: method
  qualified_name: app/src/agm/investigations:InvestigationRegistry.updateActive
  lines: 65-70
- kind: function
  qualified_name: app/src/agm/investigations:topScope
  lines: 74-80
- kind: function
  qualified_name: app/src/agm/investigations:concentration
  lines: 85-99
incoming_refs: 2
outgoing_refs: 8
---
<!-- trie:section symbol=app/src/agm/investigations:InvestigationRegistry fingerprint=5c0e390260ec2a54ee36823d655541fdf7ca19a5aa5032b3c75ad09fa7f070e9 body_fp=7488f0b86ec43a33af0526e3ff246527e022fe4dc49b1dd8b3887fae95b61f67 source_ref=e6ad66a5c7e12b638ae41ac94e8aa24411f27537 role=domain -->
Maintains a keyed registry of `Investigation` objects, tracking one active investigation and updating its confidence and scope from live symbol-mass data.

- `set` — upserts by id, preserving existing `createdAt`, `confidence`, `scope`, and `negativeEvidence`; promotes to active when `status === "active"`
- `active()` — returns the currently active `Investigation`, or `undefined` if none is set
- `addNegativeEvidence` — appends `qname` to an investigation's `negativeEvidence` list only if not already present
- `updateActive` — recomputes `scope` (top-24 symbols by mass) and `confidence` (normalised inverse entropy) on the active investigation
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/investigations:InvestigationRegistry.byId fingerprint=6de6dbb2fbadba25faee3b46eb78f280d4f1265f2b7086f3637b9e0ca81b5db5 body_fp=1e47dcac6f27dfd9aad8768707f07b748ee0ddec59759b880bc22cdb3fdc3951 source_ref=e6ad66a5c7e12b638ae41ac94e8aa24411f27537 role=model -->
`InvestigationRegistry.byId` is the private map storing all `Investigation` records keyed by their string id.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/investigations:InvestigationRegistry.activeId fingerprint=0ee7384a1f71e42b46ddc80f3d0d232b2ed8a031a925b15c4a857e6feb06e51e body_fp=e7f342f1ae1a768203e3aa3917c8d4c52371389837b2d8ab68774d295c9b27f8 source_ref=e6ad66a5c7e12b638ae41ac94e8aa24411f27537 role=model -->
`InvestigationRegistry.activeId` is the id of the currently active investigation, or an empty string if none is active.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/investigations:InvestigationRegistry.set fingerprint=5cd9ceb6e1752ba9a41573d7958e686cb05286209bd07552744008d411345366 body_fp=caffbfc53a516a572c53024410f5414e052a08127ec93107048b44bad42b2b4b source_ref=e6ad66a5c7e12b638ae41ac94e8aa24411f27537 role=domain -->
Upserts an `Investigation` into `InvestigationRegistry`, merging with any existing record and updating `activeId`; returns the investigation id.

- `status`: defaults to existing status, then `"active"` if absent.
- `createdAt`: preserved from existing record; falls back to `Date.now() / 1000`.
- `confidence`, `scope`, `negativeEvidence`: always carried over from the existing record if present; never overwritten by the caller.
- Sets `activeId` to this id when `status === "active"`; clears `activeId` if this id was active and status changed.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/investigations:InvestigationRegistry.get fingerprint=daf4674a0932c8bcf4ff4d8c653c92c78588eb3ec5cf03f797447ca3fed44d93 body_fp=ea78ffff71cfb97e5facd4f2a876f72e5780b60a5ee8bf5927cf5c3e44dd3351 source_ref=e6ad66a5c7e12b638ae41ac94e8aa24411f27537 role=domain -->
Return the `Investigation` with the given `id` from `InvestigationRegistry`, or `undefined` if not found.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/investigations:InvestigationRegistry.active fingerprint=b6e8276d06d5a6d5ba6f0f20fb7d331f0312a353ee7049504210a2c8239ee5a5 body_fp=3e2579de49358d61b6530454df443901ad025d294d5b8892c2149643f96db445 source_ref=e6ad66a5c7e12b638ae41ac94e8aa24411f27537 role=domain -->
Returns the currently active `Investigation` from `InvestigationRegistry`, or `undefined` if no investigation is active.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/investigations:InvestigationRegistry.all fingerprint=6a428add2e4de6cffe716cffce193c6d9e264afcef9c59941d67e2cd46468277 body_fp=e686340be600a39e75ea640c8569126572ac25ca32d876e92600933f32f9c220 source_ref=e6ad66a5c7e12b638ae41ac94e8aa24411f27537 role=domain -->
Returns all registered investigations in `InvestigationRegistry` as an array.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/investigations:InvestigationRegistry.addNegativeEvidence fingerprint=acb2af8e39706047f9d4513a4ce1e4756c0903a69531319ea1c3fb9037007557 body_fp=7e2fca6a7dae6c96157b2d0ec2133f0cf5aa7c87b9b5ab1aa9f83f25628408f1 source_ref=e6ad66a5c7e12b638ae41ac94e8aa24411f27537 role=domain -->
Appends `qname` to `InvestigationRegistry`'s `negativeEvidence` list for the given investigation, skipping duplicates.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/investigations:InvestigationRegistry.updateActive fingerprint=8d202fa6eea27be929a957fbbd030ac793689e1012fec9eb4f59910483ba203f body_fp=6c9e368f2329b7c3f702413108e0e93b881d407522d465ba665797da9f1ab6b9 source_ref=e6ad66a5c7e12b638ae41ac94e8aa24411f27537 role=domain -->
Recomputes `scope` (top-24 symbols by live mass) and `confidence` (attention concentration) on the active `InvestigationRegistry` investigation.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/investigations:topScope fingerprint=dcf706979cb834a1b2cfe10d1d1c702cf96dbb01209e32592b7bb35560955181 body_fp=4465cb6af1b4dfdc30bc30260f305425b8f01cee401b0924d7dc7335017d9e2d source_ref=e6ad66a5c7e12b638ae41ac94e8aa24411f27537 role=util -->
Return the top `n` symbol qualified-names from `liveMass`, ranked by descending mass, excluding zero-mass entries.

- `n`: maximum number of symbols to return
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/investigations:concentration fingerprint=f326429af30ba6e8d326028f9482547abf694941e3eddbb09011fa6b7724bdcc body_fp=3ebfcae55b04ba798c4a76c923168a602e9e32936625334c0911f034f81f33d6 source_ref=e6ad66a5c7e12b638ae41ac94e8aa24411f27537 role=domain -->
Compute attention concentration as normalised inverse entropy of the display-compressed `liveMass` distribution, returning a `0..1` scalar.

- `liveMass` — map of qualified symbol names to raw mass values; zero-mass entries are excluded.
- Returns `1` when all mass is on one symbol, `0` when spread is uniform or mass is absent.
<!-- trie:end -->