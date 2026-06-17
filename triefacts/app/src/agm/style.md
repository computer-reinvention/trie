---
trie_version: 0.1.9
source: app/src/agm/style.ts
file_fingerprint: 47c06ef87c523c1730953799be63dc07b1fc19b8bf2f015325181ff70825762b
last_synced_at: '2026-06-17T16:36:32Z'
defines:
- kind: type
  qualified_name: app/src/agm/style:ActionKind
  lines: 18-18
- kind: constant
  qualified_name: app/src/agm/style:DELIBERATE_KINDS
  lines: 21-25
- kind: function
  qualified_name: app/src/agm/style:isDeliberateKind
  lines: 30-32
- kind: constant
  qualified_name: app/src/agm/style:EXTERNAL_COLOR
  lines: 36-36
- kind: function
  qualified_name: app/src/agm/style:roleColor
  lines: 38-41
- kind: type
  qualified_name: app/src/agm/style:Tier
  lines: 46-46
- kind: function
  qualified_name: app/src/agm/style:tierFor
  lines: 48-54
- kind: function
  qualified_name: app/src/agm/style:nodeOpacity
  lines: 58-62
- kind: function
  qualified_name: app/src/agm/style:nodeRadius
  lines: 66-69
- kind: function
  qualified_name: app/src/agm/style:glowAlpha
  lines: 73-79
- kind: constant
  qualified_name: app/src/agm/style:ROLE_LABEL_COLOR
  lines: 83-83
- kind: constant
  qualified_name: app/src/agm/style:ROLE_RING_COLOR
  lines: 84-84
- kind: constant
  qualified_name: app/src/agm/style:ATTENTION_EDGE_COLOR
  lines: 88-88
- kind: constant
  qualified_name: app/src/agm/style:REPO_EDGE_COLOR
  lines: 89-89
- kind: constant
  qualified_name: app/src/agm/style:INVESTIGATION_RING_COLOR
  lines: 93-93
- kind: constant
  qualified_name: app/src/agm/style:NEGATIVE_EVIDENCE_COLOR
  lines: 94-94
incoming_refs: 3
outgoing_refs: 3
---
<!-- trie:section symbol=app/src/agm/style:ActionKind fingerprint=c32e370a2204b8a079c7c136ea8a88e72119d46cf5768d288ed4380ecb422d1f body_fp=414b23e2cab1909f2626548f89d7000ecbb44ac452abbb7fe3b94baf13408a19 source_ref=08fe3b85a87e1b50e67800917823f035ead6523f role=model -->
Type alias for the `kind` discriminant of `NodeMass`, representing the attention action that produced a node.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/style:DELIBERATE_KINDS fingerprint=6002978db6b396d5c906643c51ce224e50a3ab5208daa57f06c424a683ebc6cf body_fp=eb2626de690328864ab48ef89d6b4db7197a1436ea15c86cd4c93ad947697921 source_ref=08fe3b85a87e1b50e67800917823f035ead6523f role=model -->
Module-level `ReadonlySet` of the three `ActionKind` values that represent committed attention: `"read"`, `"trace"`, and `"write"`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/style:isDeliberateKind fingerprint=d293bb2e34b5416e87c99d34d3b42beea2ec379135fa9dd3b46a46b900578ce5 body_fp=6be6c82a1961fa98ed04c95a8afca7bfafc6fdc454f99dab794ec29c4f876b41 source_ref=08fe3b85a87e1b50e67800917823f035ead6523f role=domain -->
Return `true` when `kind` represents a deliberate, committed attention action (read, trace, or write).
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/style:EXTERNAL_COLOR fingerprint=aee2affa16facd7eca1b4412c20d9ab39e03449fa7f31d95e9b0edd66881ceae body_fp=a4b20bcc06240337dc669fe1039376cec01f36425da81b3a32690bf09fb92dc6 source_ref=08fe3b85a87e1b50e67800917823f035ead6523f role=config -->
Slate hex colour assigned to synthetic/external nodes so they read as outside the codebase without competing with role hues.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/style:roleColor fingerprint=47c58a11a33dd4ad0150cf357d3f735126f2b0b7e9f5f587c581867f4881f291 body_fp=41d07617ec956b4c3a2091c17207e5b270771f163a1552a194cf1efdb5cbe4f2 source_ref=08fe3b85a87e1b50e67800917823f035ead6523f role=util -->
Return the display colour for a role string, substituting a muted slate neutral for `SYNTHETIC_ROLE` instead of delegating to the base palette.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/style:Tier fingerprint=71c9b41f6283e3cba5758f2a6b7f456a24e126b6c47b92616747de0088eb4a60 body_fp=e881c259057a66ac7761b29e77ff0305344df4f03e067a033041e5f2e75eb189 source_ref=08fe3b85a87e1b50e67800917823f035ead6523f role=model -->
Union type representing a node's visibility tier relative to the current maximum display mass on screen.

- `"hidden"` — below 8 % of max mass; node is not rendered
- `"dominant"` — at or above 60 % of max mass; node is visually prominent
- `"visible"` — all cases in between
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/style:tierFor fingerprint=2c5e381695247df6b3941b5ffce290afb4950c0b0f814435654f5eaba5357479 body_fp=1e37c1cdf1415072c1fd6a821f5b68e6d06b3766ff005ca85b6caedd5ef8f9d6 source_ref=08fe3b85a87e1b50e67800917823f035ead6523f role=domain -->
Classify a node into a `Tier` based on its display mass relative to the current on-screen maximum.

- `displayMassValue` — absolute display mass of the node being classified
- `maxDisplayMass` — highest display mass currently visible; `≤ 0` forces `"hidden"`
- Returns `"hidden"` when `rel < 0.08`, `"dominant"` when `rel ≥ 0.6`, else `"visible"`
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/style:nodeOpacity fingerprint=d0f96d38988246011829c6cc30c8d4f74e6415e18d3e4ff2aa34ceb1ec8c2eb4 body_fp=538e0eb18a39f5d781d8fe5e4e41cb0feedad5eeb216a194ee9907bcd3bfaab6 source_ref=08fe3b85a87e1b50e67800917823f035ead6523f role=util -->
Compute node opacity in the range `[0.25, 1.0]` from the ratio of `displayMassValue` to `maxDisplayMass`.

- `maxDisplayMass ≤ 0`: returns `0` (no visible nodes on screen).
- Floor of `0.25` keeps a just-visible node faintly present rather than fully transparent.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/style:nodeRadius fingerprint=090d809cd6b214a9add76f145d0f03fcb07c091e98685a130331cc80d9495b85 body_fp=4c12d1bf9bc5eb8571e8ba11c253fe01d5b6ccee1b096fede062b7c785fb38df source_ref=08fe3b85a87e1b50e67800917823f035ead6523f role=util -->
Compute node radius in screen pixels (scale 1) from relative heat, ranging 4–12 px.

- `displayMassValue` / `maxDisplayMass`: ratio clamped to [0, 1]; zero if `maxDisplayMass` ≤ 0.
- Returns `4 + rel * 8`, making size a secondary cue behind opacity.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/style:glowAlpha fingerprint=19bbc778e6698132f4a40398f4e59af49141189105e33f7e31b49bfc81273d86 body_fp=0131c27004b16ee597022e5d792c68ff2d50a045634ba122504661b444cf9dc0 source_ref=08fe3b85a87e1b50e67800917823f035ead6523f role=util -->
Compute glow alpha for a node based on its relative heat, returning 0 below 50% and scaling from 0.12–0.30 in the top half.

- `displayMassValue` / `maxDisplayMass`: ratio clamped to [0,1] to guard against lag in smoothed max
- Returns `0` when `rel < 0.5`; otherwise `0.12 + 0.18 * (rel - 0.5) * 2`
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/style:ROLE_LABEL_COLOR fingerprint=78aea54c7149b28d29633cb8b7160e5c26ef96661018acb7e4e57dc072aa7e84 body_fp=9614055e18e48104c68c5f0e595d24be3c8b19d59e8cc8134f7fd195f541aabc source_ref=08fe3b85a87e1b50e67800917823f035ead6523f role=config -->
Text colour (`#cbd5e1`, light slate) applied to role-well labels in the AGM graph.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/style:ROLE_RING_COLOR fingerprint=bdcb192b8f0abe14b34f5a81d519b0674bba80c792aa973aa22c78e2190f4384 body_fp=253bf277bc9905edaaf8155628b2486a0b5749cc31f3481d032887ea118a8487 source_ref=08fe3b85a87e1b50e67800917823f035ead6523f role=config -->
Dark slate border colour applied to role-well (continent) rings in the AGM graph.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/style:ATTENTION_EDGE_COLOR fingerprint=f259875b2d72b883b151461e08d1290cb26468d8f15cb177ec329b1c2568d150 body_fp=4c725a00baf027885fd25b311a6e5b7ca907708c8be5e89bad4ad230cb0f7574 source_ref=08fe3b85a87e1b50e67800917823f035ead6523f role=config -->
Violet colour token (`#a78bfa`) for attention-graph (reasoning) edges, drawn over dim repo edges so reasoning dominates topology.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/style:REPO_EDGE_COLOR fingerprint=369462932d076cac99211f65d45bc2204bbac893284dc6493a63336a60b1e617 body_fp=263863a66aafcfd745ed82e3607d331ea23a12b5d699db8415c04ae9a93e11c0 source_ref=08fe3b85a87e1b50e67800917823f035ead6523f role=config -->
Dark navy colour token (`#1e293b`) for background repository edges, visually subordinate to `ATTENTION_EDGE_COLOR`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/style:INVESTIGATION_RING_COLOR fingerprint=6580db799fb9c60d9123280d26e6237fd8b233e0e10fb1823f54d1fb681ecd99 body_fp=8d3ea7a60f7b59030a9aea222c4b75f4f2a1b83bd418edf558c33bf4c1b1bea7 source_ref=08fe3b85a87e1b50e67800917823f035ead6523f role=config -->
Color constant (`#e2e8f0`) for the investigation ring; confidence encodes via opacity and tightness, not hue.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/style:NEGATIVE_EVIDENCE_COLOR fingerprint=a7a2995195f2b1559760ccff09dc8067481e6fd1dd29034301901855bb3b8785 body_fp=8039d9652e8b8149c8ae5e81532d6b6f9df9bf223464f73b0ca8198af06b24f3 source_ref=08fe3b85a87e1b50e67800917823f035ead6523f role=config -->
Color constant (`#f43f5e`, rose-red) used to render negative evidence in the investigation ring overlay.
<!-- trie:end -->