---
trie_version: 0.1.9
source: app/src/agm/synthetic.ts
file_fingerprint: 11f1634d977ad258aae59c2dd0280a322aaee82e65f4e282fecc1fcc201c5158
last_synced_at: '2026-06-17T16:36:24Z'
defines:
- kind: constant
  qualified_name: app/src/agm/synthetic:SYNTHETIC_ROLE
  lines: 19-19
- kind: constant
  qualified_name: app/src/agm/synthetic:SYNTHETIC_FILE_ROLE
  lines: 24-24
- kind: function
  qualified_name: app/src/agm/synthetic:syntheticRole
  lines: 29-33
- kind: function
  qualified_name: app/src/agm/synthetic:syntheticLabel
  lines: 37-42
- kind: interface
  qualified_name: app/src/agm/synthetic:SyntheticDescriptor
  lines: 44-49
- kind: constant
  qualified_name: app/src/agm/synthetic:SYNTHETIC_DESCRIPTORS
  lines: 51-56
- kind: constant
  qualified_name: app/src/agm/synthetic:SYNTHETIC_BY_QNAME
  lines: 59-59
- kind: function
  qualified_name: app/src/agm/synthetic:syntheticRoleEntries
  lines: 63-65
incoming_refs: 4
outgoing_refs: 8
---
<!-- trie:section symbol=app/src/agm/synthetic:SYNTHETIC_ROLE fingerprint=0923d41fb84c11bee0513b5381e9f667c31dce09e870599b8e3f35d64b5dcee0 body_fp=730ecf8b1c5926322660a0ca6893ead33006244c69bfd1de5a02cd8cddf12f81 source_ref=49d81343ee120f4cee21b475752cca1aa57b428e role=model -->
Role tag assigned to fixed synthetic nodes (Filesystem, Bash, Web, etc.) so they cluster into their own continent in the graph view.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/synthetic:SYNTHETIC_FILE_ROLE fingerprint=6e7ec159ae223b57f799fa7386c3e0bebc8e45ae5e12d982b447282360a3b202 body_fp=e2766dc5e46bfdfdb55a928e10c4480f79058eab5383e8ad214ec0318673131f source_ref=49d81343ee120f4cee21b475752cca1aa57b428e role=config -->
Role string assigned to per-file synthetic nodes so they cluster under a single "FILE READS" region instead of scattering as lone `"external"` floaters.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/synthetic:syntheticRole fingerprint=69d75d3a37e3a2ce89f780ebbcb37e928830e13ce0a7620a2dc619e1e84b9bab body_fp=b1ff7e6a95a769716783748ce31339aa2b8bdfe45642a2cd06b8e4ef5d46bd5f source_ref=49d81343ee120f4cee21b475752cca1aa57b428e role=util -->
Return the role string for a synthetic qname, or `null` if the qname is not synthetic.

- Returns `SYNTHETIC_FILE_ROLE` for per-file synthetic qnames, `SYNTHETIC_ROLE` for other synthetic qnames.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/synthetic:syntheticLabel fingerprint=a908905dc80198b2a3686f67a7f6f2bcdc1d8e3d1ff0cd36d9425e83c6960a91 body_fp=607a18ed40cf365d02f5e459244f46ebf7e54efc72fbd2a1f9abb86cc891fdb4 source_ref=49d81343ee120f4cee21b475752cca1aa57b428e role=util -->
Return a human-readable display label for a synthetic qname, or `null` for non-synthetic qnames.

- Per-file nodes return the basename of the file path (falling back to the full path).
- Fixed surface nodes (e.g. Filesystem, Bash) return the name with the synthetic prefix stripped.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/synthetic:SyntheticDescriptor fingerprint=c4cc4baddfb6572a5e315b92eb3d6dadc4fa7c2f4551b58a9fdcf02bf7acceaa body_fp=1de6b2035b402883ae1bed924326dfb7b9d7124bf83b7f228e2989c13ff8551b source_ref=49d81343ee120f4cee21b475752cca1aa57b428e role=model -->
Shape describing a resolved synthetic node with all fields needed for rendering and rollup.

- `node`: the canonical `SyntheticNode` value (e.g. `"Filesystem"`, `"Bash"`)
- `qname`: fully-qualified synthetic identifier, prefixed with `SYNTHETIC_QNAME_PREFIX`
- `label`: human-readable display name shown in the map UI
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/synthetic:SYNTHETIC_DESCRIPTORS fingerprint=9f16ea432910dd8ad6447408d4d343f7f43ee6f39fe89a20bf3b65e1bb151a25 body_fp=48c6a001464cb08b576b41ab90e99b9649c84c919996f2b05d2d09173a1c234d source_ref=49d81343ee120f4cee21b475752cca1aa57b428e role=model -->
Array of `SyntheticDescriptor` objects built from `SYNTHETIC_NODES`, each holding the node name, its qualified name, `SYNTHETIC_ROLE`, and a label equal to the node name.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/synthetic:SYNTHETIC_BY_QNAME fingerprint=a1da77c9f188933756b723a99d3963f77fed373d7dbbbcd137c06ef2c51aafc7 body_fp=ebffef9827e4dfdf337923f1af1008b76ecc54c5b9bc553531f5e7c6f49ca91b source_ref=49d81343ee120f4cee21b475752cca1aa57b428e role=model -->
Map from synthetic qname to its `SyntheticDescriptor`, built from `SYNTHETIC_DESCRIPTORS` for O(1) lookup during rendering and role rollup.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/synthetic:syntheticRoleEntries fingerprint=289fd1b91df58b165e6e30cc74626c33e5aba268526d44e0bf6eb614f74c1c00 body_fp=65fcebf3c830f89778f2d7a7b2ac28dc4f7f5cb0ce0b5a7fe72269e6779e9d1e source_ref=49d81343ee120f4cee21b475752cca1aa57b428e role=util -->
Return an array of `[qname, role]` pairs from `SYNTHETIC_DESCRIPTORS` to merge into the attention model's role map.
<!-- trie:end -->