---
trie_version: 0.1.9
source: app/src/agm/attentionModel.ts
file_fingerprint: 763c5b3ed70856bfd6f4fc7727ec25e219f5b60c619d6ebb94ec302dad12abf9
last_synced_at: '2026-06-17T16:36:34Z'
defines:
- kind: interface
  qualified_name: app/src/agm/attentionModel:NodeMass
  lines: 25-31
- kind: interface
  qualified_name: app/src/agm/attentionModel:RoleMass
  lines: 33-37
- kind: interface
  qualified_name: app/src/agm/attentionModel:Centroid
  lines: 39-44
- kind: interface
  qualified_name: app/src/agm/attentionModel:NodeState
  lines: 46-49
- kind: class
  qualified_name: app/src/agm/attentionModel:AttentionModel
  lines: 51-269
- kind: property
  qualified_name: app/src/agm/attentionModel:AttentionModel.nodes
  lines: 53-53
- kind: property
  qualified_name: app/src/agm/attentionModel:AttentionModel.roleOf
  lines: 55-55
- kind: method
  qualified_name: app/src/agm/attentionModel:AttentionModel.setRoles
  lines: 58-60
- kind: method
  qualified_name: app/src/agm/attentionModel:AttentionModel.seedHistorical
  lines: 64-67
- kind: method
  qualified_name: app/src/agm/attentionModel:AttentionModel.clearLive
  lines: 72-81
- kind: method
  qualified_name: app/src/agm/attentionModel:AttentionModel.ingest
  lines: 87-90
- kind: property
  qualified_name: app/src/agm/attentionModel:AttentionModel.pinned
  lines: 96-96
- kind: method
  qualified_name: app/src/agm/attentionModel:AttentionModel.pin
  lines: 98-101
- kind: method
  qualified_name: app/src/agm/attentionModel:AttentionModel.isPinned
  lines: 103-105
- kind: method
  qualified_name: app/src/agm/attentionModel:AttentionModel.pinnedSet
  lines: 107-109
- kind: method
  qualified_name: app/src/agm/attentionModel:AttentionModel.applyNegativeEvidence
  lines: 114-117
- kind: method
  qualified_name: app/src/agm/attentionModel:AttentionModel.rename
  lines: 120-125
- kind: method
  qualified_name: app/src/agm/attentionModel:AttentionModel.remove
  lines: 128-130
- kind: method
  qualified_name: app/src/agm/attentionModel:AttentionModel.inheritFrom
  lines: 136-144
- kind: method
  qualified_name: app/src/agm/attentionModel:AttentionModel.liveMass
  lines: 147-151
- kind: method
  qualified_name: app/src/agm/attentionModel:AttentionModel.massFor
  lines: 154-167
- kind: method
  qualified_name: app/src/agm/attentionModel:AttentionModel.snapshot
  lines: 173-189
- kind: method
  qualified_name: app/src/agm/attentionModel:AttentionModel.dominantKind
  lines: 194-210
- kind: method
  qualified_name: app/src/agm/attentionModel:AttentionModel.roleMass
  lines: 213-226
- kind: method
  qualified_name: app/src/agm/attentionModel:AttentionModel.centroid
  lines: 231-234
- kind: method
  qualified_name: app/src/agm/attentionModel:AttentionModel.prune
  lines: 240-259
- kind: method
  qualified_name: app/src/agm/attentionModel:AttentionModel.ensure
  lines: 261-268
incoming_refs: 9
outgoing_refs: 20
---
<!-- trie:section symbol=app/src/agm/attentionModel:NodeMass fingerprint=7c3822e5ba9ad66b82909872e770103908083366affc9e05658ad6802ba52f36 body_fp=e5ad541125136d23e9004dbf66bd9f379c1b4af7b471cffbdf6a00beb99902f8 source_ref=203fa373ec937b9d062287ebdf20b283bec5718a role=model -->
Per-symbol mass snapshot combining live, historical, and display values for the renderer.

- `historical`: seeded once at load from the graph; static for the session
- `display`: log-compressed `live + seed·historical + 1`; bounded for rendering
- `kind`: dominant event type driving render style (pill, dot, constellation)
- `pinned`: symbol was edited/patched this session; never culled from view
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionModel:RoleMass fingerprint=8148b9b364f958eb5e519513eeaee01dbed1c79bba83277b2f1d1de6a334f429 body_fp=0890f12b044be596b7b3e9c71fab4a66b42e659b860356eccc33dbec5b794b83 source_ref=203fa373ec937b9d062287ebdf20b283bec5718a role=model -->
Holds a single role's aggregated live mass and its log-scaled display value for rendering role rollups.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionModel:Centroid fingerprint=84d202029529ec5712f7e0805ad83028b233f2a0672d1b6c34e461085d77da04 body_fp=4e59ba0dbeaee30e09b3c6b516b42f771305798c5e6eb69e0d0eaf6c753df6a8 source_ref=203fa373ec937b9d062287ebdf20b283bec5718a role=model -->
Represents the attention centroid as a ranked list of active roles rather than an x/y coordinate.

- `topRoles`: roles sorted by live mass, descending; length capped by caller's `topN`
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionModel:NodeState fingerprint=fb481df2084ba97bf2ede82cfbbeb0c855d753046c2737436bd4a6ddad732ab7 body_fp=8816baf209b1c1a7a9ab7c152a03ddea954b90632678b1f67a9be98383edd30d source_ref=203fa373ec937b9d062287ebdf20b283bec5718a role=model -->
Internal per-symbol mutable state held in `AttentionModel.nodes`, combining decaying event contributions with the seeded historical mass.

- `contributions`: ordered list of live decaying events for this symbol
- `historical`: static in-session seed loaded from the graph; `0` if never seeded
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionModel:AttentionModel fingerprint=65a4540c90d1c24593915f597618bb38b8628707086a30dc740dd339933e9e8f body_fp=3e82254129789bf42e37399dbcf8fe5cbc4578ae757beee73401f1ec2d5c501a source_ref=203fa373ec937b9d062287ebdf20b283bec5718a role=domain -->
In-memory AGM cognitive-state field: tracks per-symbol decaying live-mass contributions and historical-mass seeds, and derives role rollups and the attention centroid.

- `ingest` — appends a typed, decaying `LiveContribution`; `scale` attenuates weight for low-confidence hits.
- `seedHistorical` — sets a symbol's static in-session historical-mass floor from the graph's `historical_mass` field.
- `clearLive` — resets all event contributions and the pinned set, retaining historical seeds; call on new session.
- `pin` — marks a symbol as edited this session; pinned symbols are always included in `snapshot` output.
- `applyNegativeEvidence` — injects a non-decaying negative contribution (`lambda=0`) to subtract live mass.
- `inheritFrom` — seeds a newly created symbol at `factor × creator's live mass`, decaying at the write rate.
- `massFor` — returns a `NodeMass` combining live + seeded historical mass, display log-scale value, and dominant kind.
- `snapshot` — returns all symbols above `COLD_FLOOR` (plus all pinned), computed at wall-clock time `now`.
- `roleMass` — aggregates live mass per role tag; symbols without a role are grouped as `"untagged"`.
- `centroid` — returns the top-N roles by live mass as a `Centroid`; default `topN` is 5.
- `prune` — folds zero-lambda contributions into a single residual and drops fully-decayed entries to bound memory.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionModel:AttentionModel.nodes fingerprint=30edbd856f45e6e637cb209bb1e62396f9ecadcc8df3a3d87b756f2b01a5dd55 body_fp=b643240b05d4c2cd468ffc4d7c2979cce1baf0184fecf4705b56b37e73ccca14 source_ref=203fa373ec937b9d062287ebdf20b283bec5718a role=model -->
Private `AttentionModel` attribute mapping each symbol's qualified name to its live contributions and historical seed.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionModel:AttentionModel.roleOf fingerprint=e2eb89c5a32ba9cc71135b4b192250cff25b9cbdaf928b16ad786ea9f9ab7c82 body_fp=6494ae83d07256122073bb4900b321a2ddf6c4aac18e331249d47dca629390f3 source_ref=203fa373ec937b9d062287ebdf20b283bec5718a role=model -->
Private `AttentionModel` attribute mapping each symbol's qualified name to its architectural role tag, used to compute per-role live-mass rollups.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionModel:AttentionModel.setRoles fingerprint=96f1fe26e24387357f8a5a8eb98d44437baa262a8fa9f0b7cd9d8e7a94844bce body_fp=5114af7721abf0ef88e34cc1d6034d9552522e64c7747cd347fda44f7c2c570e source_ref=203fa373ec937b9d062287ebdf20b283bec5718a role=domain -->
Replace `AttentionModel`'s internal `qname→role` map, called whenever the system model loads or refreshes.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionModel:AttentionModel.seedHistorical fingerprint=c0cbfb0ddac3fc258ea70b5f9c8a33d33575fcf5c307aa0c80f243271c8c84e2 body_fp=619df5efbfbadea1dc56958982c55e36f171af640bfd6eab79c5e037df9fdf2e source_ref=203fa373ec937b9d062287ebdf20b283bec5718a role=domain -->
Set the historical-mass seed for a symbol on `AttentionModel`, clamping negative values to zero.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionModel:AttentionModel.clearLive fingerprint=c0c742dd3103b55e0423b8741532152d1c09e2ed37a8880679a48c0dcc2ccf40 body_fp=a4d95939c99f267376d267b1784ebe58f16ee31755b15de6a27cb4d67c6db1e2 source_ref=203fa373ec937b9d062287ebdf20b283bec5718a role=domain -->
Clear all live event contributions from `AttentionModel`, retaining historical-mass seeds and dropping nodes that have neither.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionModel:AttentionModel.ingest fingerprint=cfe7e5e2f1d285175d18a952d20e354837bcf06ac14861e81ec1676f9c206648 body_fp=ad7d042c24c0f03aff00c66a9398f21fc4b844da276477bbc24d26097f420abb source_ref=203fa373ec937b9d062287ebdf20b283bec5718a role=domain -->
Append a decaying `LiveContribution` to a node's contribution list, optionally attenuating its weight by `scale`.

- `scale`: multiplier < 1 for weak candidates (e.g. grep result hits); defaults to 1 for full-weight events.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionModel:AttentionModel.pinned fingerprint=ced2bab40d7407486b93c6a6a27dfb07f93a673b19c7d199be74a7ef3c54adc3 body_fp=0e05451ad2ec692482ad295c932cd6f53c93e2f58b5992ce1c7293ef46c74d90 source_ref=203fa373ec937b9d062287ebdf20b283bec5718a role=model -->
`AttentionModel.pinned` is the set of qnames edited or patched this session, ensuring they are never removed from view.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionModel:AttentionModel.pin fingerprint=f858da828ee9401260955fde2420f4143a6ebf5e43d022ead77bdd59c785ea25 body_fp=9d7a3d77ac3dfbf4fe9db6e96d25a14c7f9dcb72de3509c1ff9f7a72b9f7a4dc source_ref=203fa373ec937b9d062287ebdf20b283bec5718a role=domain -->
Mark a symbol as pinned on `AttentionModel`, ensuring it is never evicted from the view regardless of live mass.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionModel:AttentionModel.isPinned fingerprint=5d074b7fdc683d17a68900e4e6bb25219d52455733a400ccb045752446893885 body_fp=6454e55abb88e589aea599365ce0336e1cc4d85a6d1064ecf6c07eb564750bbe source_ref=203fa373ec937b9d062287ebdf20b283bec5718a role=domain -->
Returns whether the given `qname` is in `AttentionModel`'s pinned set.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionModel:AttentionModel.pinnedSet fingerprint=ed61d4b5e23e69383b65c61585a590fb998cfba0fd0696b6b4fc9f9ea557195b body_fp=eff9632bd476840e1c5828c1efe4e8e5f4f50e92ea26ce05ce6d3ff5c3814a11 source_ref=203fa373ec937b9d062287ebdf20b283bec5718a role=util -->
Returns the `AttentionModel`'s internal set of pinned qnames directly.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionModel:AttentionModel.applyNegativeEvidence fingerprint=56951c4e6fd0e0b09d8c1a920f775dfa3e00861377bed006c3b9d633b44e9756 body_fp=55c586c1df462316b5d76ef2a329c16077dd20623f7d141b89df73f2fa3dc2cc source_ref=203fa373ec937b9d062287ebdf20b283bec5718a role=domain -->
Injects a non-decaying negative contribution into `qname`'s live mass to represent explicit "ruled out" evidence.

- `magnitude`: absolute value is negated; sign of caller's input is ignored.
- `lambda`: fixed at `0`, so the subtraction persists without decay.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionModel:AttentionModel.rename fingerprint=ed0e51f5cc24b8f26105d7df52295fd3f8fe7b5c54d0b8fbbb9f5cb6579a4bcb body_fp=f82c3db79f40bf635d63615988c4b4ca8649765ac04ecbabc84e848c58461f90 source_ref=203fa373ec937b9d062287ebdf20b283bec5718a role=domain -->
Transfer `AttentionModel`'s full node state from one qname to another, preserving contributions and historical mass under the new key.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionModel:AttentionModel.remove fingerprint=4799cbf23a8524764678744c582a643b4d34cbe2918878b96319bf8ec50708da body_fp=fe109868c986e43c706476410678581a929a936c55d5715dbe90353050786702 source_ref=203fa373ec937b9d062287ebdf20b283bec5718a role=domain -->
Drop a symbol's live state from `AttentionModel` immediately by deleting its node entry.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionModel:AttentionModel.inheritFrom fingerprint=a674f3f58d4bb2abc71eda4f9c70520f56a9d452986f70fc4e3fd1fb93908243 body_fp=aaa4701586ae5376a884d1dd26c1bc50da134d989422d09c3a9971dbb506d021 source_ref=203fa373ec937b9d062287ebdf20b283bec5718a role=domain -->
Bootstrap `created` with a fraction of `creator`'s current live mass, decaying at the write-event rate.

- `factor`: fraction of creator's live mass to inherit; defaults to `0.5`.
- No-ops if the creator's current live mass is zero or negative.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionModel:AttentionModel.liveMass fingerprint=0267fc0c1798e724a32c954451e7ef051d108a631a7ac28d5a6cd259223fd400 body_fp=9b1cbacea00af7a5ca56c9d3cf98a6b0fe7569952f10d2d428229a3108577e27 source_ref=203fa373ec937b9d062287ebdf20b283bec5718a role=domain -->
Return the current raw live mass for one symbol, clamped to zero, by folding its decayed contributions at `now`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionModel:AttentionModel.massFor fingerprint=e5ca6ffe99f2a27ceb15c91e0dc54c11783d4c093f87929fecf1903a9c215760 body_fp=739b2a30e91fb99718d96c4a38cdb9299bb37c1084f2300cd08c4a1e6d790d34 source_ref=203fa373ec937b9d062287ebdf20b283bec5718a role=domain -->
Compute and return the combined `NodeMass` for a single symbol at `now`, merging live and historical contributions.

- `kind`: forced to `"write"` if pinned, `"historical"` if no state exists, else dominant event type.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionModel:AttentionModel.snapshot fingerprint=fa7209bdce298674c5d72571a4cdfebe884228f9e145d8b539d4ca3c6e842123 body_fp=39bbb2870d8b1ce10a924969b60912a1be59e0a479a595273cda82ad705d6635 source_ref=203fa373ec937b9d062287ebdf20b283bec5718a role=domain -->
Return a `NodeMass` map of every `AttentionModel` symbol whose combined mass exceeds `COLD_FLOOR` at `now`, always including pinned symbols regardless of mass.

- `now` — wall-clock timestamp used for decay evaluation
- Pinned entries force `kind` to `"write"` and set `pinned: true`; cold pinned nodes are never filtered out
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionModel:AttentionModel.dominantKind fingerprint=f36daaccb2d1e99a970bef499c80e78b1fbe3e39e579535226bed86d05d3303c body_fp=dcf7c31645d44f4ce39f0a7e23b4dcccc7ec7b9b5f66dffb25ed3f43351e0a4f source_ref=203fa373ec937b9d062287ebdf20b283bec5718a role=domain -->
Returns the `AttentionEventType` contributing the greatest current decayed mass to a node, or `"historical"` if no positive contributions exist.

- `s`: node state whose contributions are scanned
- `now`: wall-clock timestamp used to evaluate per-contribution decay
- Returns `"historical"` when all contributions are absent, typeless, or non-positive
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionModel:AttentionModel.roleMass fingerprint=b4134db3cf2840fc4969d61948964b62e731fb76eb2fc5a9cb6c10e15f980b50 body_fp=0eb23ff7679dcea27a5e7852df729e1b2e9515f5ab949ceafd4d069b11ffe5e3 source_ref=203fa373ec937b9d062287ebdf20b283bec5718a role=domain -->
Sums live mass of all member symbols per role at `now`, returning a derived `RoleMass` map keyed by role string.

- Symbols with no positive live mass are skipped.
- Symbols absent from `roleOf` are bucketed under `"untagged"`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionModel:AttentionModel.centroid fingerprint=51473c52fdb42feea8f96bec50e9939795158ca1b09c9379ae5996e80d515601 body_fp=901838effd06f1aab92b644e6253b1e73cd8ff2825f81b973ba5a4d100dd5246 source_ref=203fa373ec937b9d062287ebdf20b283bec5718a role=domain -->
Return the `AttentionModel` attention centroid as the top-N active roles sorted by descending live mass.

- `topN`: maximum number of roles returned; defaults to 5.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionModel:AttentionModel.prune fingerprint=51c1831d44f1f4143ac46d606b468b093c7b15171db46ca399cf5eff0c2ae877 body_fp=5ad55bcda474951147c7b14d167724a64d85742bc90e1a6235634c0ea621f92d source_ref=203fa373ec937b9d062287ebdf20b283bec5718a role=domain -->
Removes fully-decayed contributions from all `AttentionModel` nodes to keep memory bounded, folding zero-lambda (negative/inherited) entries into a single residual and deleting nodes with no remaining mass.

- `now` — current wall-clock timestamp used to evaluate decayed magnitude against `COLD_FLOOR`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionModel:AttentionModel.ensure fingerprint=03545f4f54a275c8edccd16faa989adda717a72ccbec4e950575622a553e3575 body_fp=5e4c364aa3d08520a482e7020502f5811c50490aec2c37e743318297e3a0e34a source_ref=203fa373ec937b9d062287ebdf20b283bec5718a role=util -->
Return the existing `NodeState` for `qname`, or create and register a blank one if absent.
<!-- trie:end -->