---
trie_version: 0.1.9
source: app/src/agm/attentionGraph.ts
file_fingerprint: cd947127e69243e3264037156d9fe8932e80a79873f9e9df474aa3960485106d
last_synced_at: '2026-06-17T16:35:51Z'
defines:
- kind: interface
  qualified_name: app/src/agm/attentionGraph:AttentionEdge
  lines: 12-17
- kind: constant
  qualified_name: app/src/agm/attentionGraph:TRACE_LAMBDA
  lines: 21-21
- kind: class
  qualified_name: app/src/agm/attentionGraph:AttentionGraph
  lines: 23-81
- kind: property
  qualified_name: app/src/agm/attentionGraph:AttentionGraph.edges
  lines: 24-24
- kind: property
  qualified_name: app/src/agm/attentionGraph:AttentionGraph.investigationId
  lines: 25-25
- kind: property
  qualified_name: app/src/agm/attentionGraph:AttentionGraph.path
  lines: 27-27
- kind: method
  qualified_name: app/src/agm/attentionGraph:AttentionGraph.setInvestigation
  lines: 30-35
- kind: method
  qualified_name: app/src/agm/attentionGraph:AttentionGraph.reinforce
  lines: 38-51
- kind: method
  qualified_name: app/src/agm/attentionGraph:AttentionGraph.reinforceChain
  lines: 54-58
- kind: method
  qualified_name: app/src/agm/attentionGraph:AttentionGraph.liveEdges
  lines: 61-68
- kind: method
  qualified_name: app/src/agm/attentionGraph:AttentionGraph.trail
  lines: 71-73
- kind: method
  qualified_name: app/src/agm/attentionGraph:AttentionGraph.prune
  lines: 76-80
incoming_refs: 2
outgoing_refs: 4
---
<!-- trie:section symbol=app/src/agm/attentionGraph:AttentionEdge fingerprint=c2e41a9937dba31561afe31b5e986687234c40aea0b58be0f8b296affe871564 body_fp=a16874b1fc4ddaca7f3993aa4c598d54e69d78e35681a12a2bfd5a6cdaf125f8 source_ref=7c21d7d41ee09abb9396014c4d0febd6a6bcd371 role=model -->
Represents a directed reasoning edge in the attention graph, holding decay state.

- `heat`: raw accumulated heat at the moment of last reinforcement, before decay
- `ts`: unix seconds timestamp of last reinforcement, used as decay origin
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionGraph:TRACE_LAMBDA fingerprint=7353ba768432598bdf7b617e3eafbaa6511177fd09003390ca1cd05eedf77eff body_fp=ea38991e3509651dd5022a720564a88e7d340fadde5493d809c18f06c7069a84 source_ref=7c21d7d41ee09abb9396014c4d0febd6a6bcd371 role=config -->
Decay rate constant for trace edges, derived from the `"trace"` half-life configuration via `liveLambda`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionGraph:AttentionGraph fingerprint=c79bed14271336d51d80dc63dab4c2d055fecc1c99fbe5f0bac19b2e3ace1e72 body_fp=0580d86968e95ad68661316669c823bec135642d04844b86f0f3bd87dc305ab8 source_ref=7c21d7d41ee09abb9396014c4d0febd6a6bcd371 role=domain -->
Tracks the agent's directed reasoning trail within a single investigation as a heat-decaying edge graph scoped by investigation ID.

- `setInvestigation`: resets all edges and the path when the investigation ID changes.
- `reinforce`: adds heat to a directed `from→to` edge, decaying existing heat to `ts` before adding `amount`; appends `to` to the ordered path (capped at 64 entries).
- `reinforceChain`: calls `reinforce` for each consecutive pair in `chain`.
- `liveEdges`: returns edges whose heat, decayed to `now`, exceeds `floor`.
- `trail`: returns a shallow copy of the ordered symbol path (most recent last).
- `prune`: deletes edges whose decayed heat falls at or below `floor` to bound memory.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionGraph:AttentionGraph.edges fingerprint=44ae99a89de5a04ce0ff26c06098fbb9999a5dee2a3265cd5e57d1d4e00a1c3d body_fp=1953233a71202dd9c9555bb77ca01f18ada298bcac4a9ee5011a6bf2f11f664e source_ref=7c21d7d41ee09abb9396014c4d0febd6a6bcd371 role=model -->
Private `AttentionGraph` attribute storing all directed attention edges, keyed by `"from\0to"` composite string.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionGraph:AttentionGraph.investigationId fingerprint=34c012dc7f73908911b84ecaea2dab3f28cd5ebc52b91467be1ab000fbfd37dd body_fp=1c9227648ff9d7088d599edebee0cda549a2dadf4ca2b26618d17d7bd2869d00 source_ref=7c21d7d41ee09abb9396014c4d0febd6a6bcd371 role=model -->
`AttentionGraph.investigationId` is the ID of the currently active investigation; reset to `""` clears continuity state.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionGraph:AttentionGraph.path fingerprint=43897d89a56cb90116f20adb9fa9da083e6f652436494e2a0fe2568adc5599e8 body_fp=2527ef9eb356887731e1fb207cf4af56589b39420f8f8997784ab1a73ae504b7 source_ref=7c21d7d41ee09abb9396014c4d0febd6a6bcd371 role=model -->
`AttentionGraph.path` is the ordered sequence of symbol identifiers visited during the current investigation, capped at 64 entries (most recent last).
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionGraph:AttentionGraph.setInvestigation fingerprint=f713150e7d61a2d38881f863c6d695acb931051cd3dcfcd5cc6dd138ece4ded8 body_fp=978c240d90a1c235aa12200f15dccb41aa2e409ff529938b5fc28c9af9db2679 source_ref=7c21d7d41ee09abb9396014c4d0febd6a6bcd371 role=domain -->
Reset `AttentionGraph` state to a new investigation, clearing all edges and the reasoning path if `id` differs from the current investigation.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionGraph:AttentionGraph.reinforce fingerprint=73084b4fe77ea5d82d371d702d57b4bad449d59c024d7c17fa2512255de75d28 body_fp=47c3faed3515095d775b34d2da871e583062ae494df947a59c47daa1e354c1d3 source_ref=7c21d7d41ee09abb9396014c4d0febd6a6bcd371 role=domain -->
Reinforce a directed edge in `AttentionGraph`, decaying its existing heat to `ts` before adding `amount`, and appending `to` to the ordered path (capped at 64 entries).

- `from` / `to`: no-op when equal; null byte used as key separator.
- `amount`: heat units added after decay; defaults to `1`.
- `ts`: unix seconds of this reinforcement, used as the new decay origin.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionGraph:AttentionGraph.reinforceChain fingerprint=dac2e0682ed2e1b5a3ffa8f81908262bdd2495560006b760de91074182d92278 body_fp=65f1fad2b7beafe1d90fc9837aa8e06a50a7dca495e1e99a8cbd222bd75e7c8d source_ref=7c21d7d41ee09abb9396014c4d0febd6a6bcd371 role=domain -->
Call `AttentionGraph.reinforce` for each consecutive pair in `chain`, recording a full transition sequence (e.g. a→b→c) at timestamp `ts`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionGraph:AttentionGraph.liveEdges fingerprint=3eb117c62a71e3ae52728fae62e71eb3aa43c7ee76683d617eb0fae86b3c4657 body_fp=6811ab892d1123a20972be54f08c6d9998ea09856ffd9d12c53a13827541da51 source_ref=7c21d7d41ee09abb9396014c4d0febd6a6bcd371 role=domain -->
Return all `AttentionGraph` edges whose decay-adjusted heat exceeds `floor` at `now`, with heat values decayed to `now`.

- `now`: current unix seconds used as the decay reference point
- `floor`: minimum heat threshold; defaults to `1e-3`
- Returns edges with `heat` field reflecting decayed value, not stored raw value
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionGraph:AttentionGraph.trail fingerprint=b64da6a7f20887006e33060ff31750f6ce698a3ea357d5d8373b6139e4cc5d7d body_fp=f40d68c37f1aa393af472fbbf36d945904b3ab013cbde2891320173a757f854d source_ref=7c21d7d41ee09abb9396014c4d0febd6a6bcd371 role=domain -->
Return a shallow copy of `AttentionGraph`'s ordered symbol path for the current investigation.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/attentionGraph:AttentionGraph.prune fingerprint=644c54dac8ac14b556a8362aab659ba93e2e6dcc3602a37e4efa854f22f25be7 body_fp=f6a1cb9eafa0fe79f2c43a7367e2c35ae95d28c90679470b973d07b790a9c62f source_ref=7c21d7d41ee09abb9396014c4d0febd6a6bcd371 role=domain -->
Remove all `AttentionGraph` edges whose decayed heat at `now` is at or below `floor`.
<!-- trie:end -->