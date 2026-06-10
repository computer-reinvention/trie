---
trie_version: 0.1.5
source: trie/attention.py
file_fingerprint: 12a339d9e3d09e224a5bbe3158873ec8a53fecbfd2b80219d0a2d23536ff81d7
last_synced_at: '2026-06-10T13:16:47Z'
description: 'AGM (Attention Gravity Map) contracts: the shared vocabulary for modelling'
defines:
- kind: module
  qualified_name: trie/attention:__module__
  lines: 1-347
- kind: constant
  qualified_name: trie/attention:EventType
  lines: 57-57
- kind: constant
  qualified_name: trie/attention:EVENT_WEIGHTS
  lines: 61-66
- kind: constant
  qualified_name: trie/attention:LIVE_HALFLIFE_SECONDS
  lines: 70-75
- kind: constant
  qualified_name: trie/attention:HISTORICAL_HALFLIFE_SECONDS
  lines: 80-80
- kind: function
  qualified_name: trie/attention:live_lambda
  lines: 83-85
- kind: constant
  qualified_name: trie/attention:HISTORICAL_LAMBDA
  lines: 88-88
- kind: function
  qualified_name: trie/attention:display_mass
  lines: 91-94
- kind: constant
  qualified_name: trie/attention:TOOL_EVENT_TYPE
  lines: 106-144
- kind: function
  qualified_name: trie/attention:classify_tool
  lines: 147-156
- kind: constant
  qualified_name: trie/attention:_DEFAULT_TOOL_EVENTS
  lines: 161-165
- kind: constant
  qualified_name: trie/attention:RepoEdgeKind
  lines: 176-183
- kind: constant
  qualified_name: trie/attention:ATTENTION_EDGE_KIND
  lines: 188-188
- kind: constant
  qualified_name: trie/attention:DEFAULT_EDGE_KIND
  lines: 192-192
- kind: constant
  qualified_name: trie/attention:EDGE_WEIGHTS
  lines: 198-206
- kind: constant
  qualified_name: trie/attention:PROPAGATION_FACTOR
  lines: 208-208
- kind: constant
  qualified_name: trie/attention:PROPAGATION_HOPS
  lines: 209-209
- kind: function
  qualified_name: trie/attention:edge_weight
  lines: 212-214
- kind: constant
  qualified_name: trie/attention:SyntheticNode
  lines: 227-227
- kind: constant
  qualified_name: trie/attention:SYNTHETIC_NODES
  lines: 229-235
- kind: constant
  qualified_name: trie/attention:SYNTHETIC_QNAME_PREFIX
  lines: 239-239
- kind: function
  qualified_name: trie/attention:synthetic_qname
  lines: 242-244
- kind: function
  qualified_name: trie/attention:is_synthetic_qname
  lines: 247-248
- kind: constant
  qualified_name: trie/attention:TOOL_SYNTHETIC_NODE
  lines: 253-258
- kind: function
  qualified_name: trie/attention:classify_synthetic
  lines: 261-264
- kind: class
  qualified_name: trie/attention:AttentionEvent
  lines: 273-311
- kind: method
  qualified_name: trie/attention:AttentionEvent.make
  lines: 292-311
- kind: constant
  qualified_name: trie/attention:InvestigationStatus
  lines: 321-321
- kind: constant
  qualified_name: trie/attention:INVESTIGATION_STATUSES
  lines: 323-328
- kind: class
  qualified_name: trie/attention:Investigation
  lines: 332-346
incoming_refs: 15
outgoing_refs: 0
---
<!-- trie:section symbol=trie/attention:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=9148bd7084ea5908d914343a7eb8eba6a3c4efcc43e2f7bdaef5e2c471cd41ea source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=model -->
Defines AGM (Attention Gravity Map) contracts for modeling agent attention as a field over the symbol graph.

- **EventType**: Four cognitive stages with weights and decay rates for live mass calculation
- **Live mass**: Per-event field decayed by wall-clock time, drives visual gravity and investigations
- **Historical mass**: Long-term cognitive importance signal with 21-day half-life, updated during sync
- **Tool classification**: Maps MCP tools to event types or synthetic nodes for attention routing
- **Edge propagation**: One-hop attention spread with per-kind weights and 0.15 propagation factor
- **Synthetic nodes**: Non-code surfaces (Filesystem, Bash, Web, Database, Git) for complete attention tracking
- **AttentionEvent**: Captured unit at each tool call with timestamp, type, target, and agent context
- **Investigation**: Explicit labeled spans of agent cognition with status tracking
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:EventType fingerprint=d1b9b6acfee16fbf20daafd02b57eec5d7ac65b7fb04517b4e69f9a0eb4c4138 body_fp=c476880dcace455b4d62c18c16010e0330de638dc360eb6feaa0de39c9a09272 source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=model -->
Type alias for attention event types representing cognitive stages from exploration to modification.

- `grep` — exploration phase ("this might matter")
- `read` — commitment phase ("this is worth understanding") 
- `trace` — explanation phase ("this explains something important")
- `write` — modification phase (patch or file edit)
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:EVENT_WEIGHTS fingerprint=87e4a4d0036696eeac4d0c63861525dc955f11b540519f8877fc0a509c607894 body_fp=b6a5535cd928218d51e55b7f08892a8223ce01659687ea3804356dbf8506cebb source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=config -->
Maps attention event types to their live mass weights for AGM calculations.

- `grep`: 10 (exploration/search activity)
- `read`: 40 (committed understanding effort) 
- `trace`: 80 (causal reasoning through code)
- `write`: 80 (modification/editing activity)
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:LIVE_HALFLIFE_SECONDS fingerprint=4541da94bed6ea8aadf706817f3fffbc4c41ffa2b9b4a75d61dd0ff442375045 body_fp=30c7282499b3674b327516c8c201439fe7a2040e63e43ac46d988792bd4b941a source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=config -->
Defines per-event-type half-lives in seconds for live mass decay in the Attention Gravity Map.

- `grep`: 30 seconds (exploration cools quickly)
- `read`: 180 seconds (commitment has medium persistence)
- `trace`/`write`: 600 seconds (explanation and edits stay warm longest)
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:HISTORICAL_HALFLIFE_SECONDS fingerprint=2dcf7083f64c06132b7babb471f3716a5887cf325d9fa3b266e4eb32b02ce3be body_fp=cf212717cc0afb801c8d320a140c687446ce4e91b6005777f6c6533418fa58ab source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=config -->
Half-life in seconds for historical mass decay (21 days), controlling how long cross-investigation cognitive importance persists.
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:live_lambda fingerprint=0582a218ef72fba1c98be73177eaf65bb3ddadf2c8867e85a9dbb3d882264373 body_fp=0325291ff36935f24ab49cb8537025445ba93f2679622d9665868cf8134a4849 source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=util -->
Calculates the continuous decay rate λ for a given live event type in units of 1/seconds.

- Returns λ = ln(2) / half_life for exponential decay calculations
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:HISTORICAL_LAMBDA fingerprint=c509b051ecd3032bd599695d005e3e9d30c0755c9f8f5c19bcb929c964d08be6 body_fp=74912d30e69b9b94eeed8c799da4b4faf3a71bfe5b1e1721f013214b1e30af28 source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=config -->
Precomputed continuous decay rate λ for historical mass on a 21-day half-life.
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:display_mass fingerprint=17793c90bd24d90595acf5eba501e71be19cc16b87e1a85d323cf85a26f8b756 body_fp=1dac8cdb0de38573df947e2cf3b8c0919b09705aa7cabbc7dd9f0acc17800999 source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=util -->
Applies logarithmic compression to raw mass values for bounded display rendering.

- Returns `log(max(0, raw_mass) + 1)` to prevent unbounded growth in UI
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:TOOL_EVENT_TYPE fingerprint=62104ead21a7cc71d422c642c0b366a9f1dd2d1b429016529b4ba96c0477ac46 body_fp=deee2b8fd5ed2f06d2010bf73fbabf39ce581f8310865a4306dc09beeb0c5db8 source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=config -->
Maps trie MCP tool names to their corresponding attention event types for AGM classification.

- Tools map to `read`, `trace`, `grep`, `write`, or `None` for no symbol attention
- Navigation/bookkeeping tools return `None` to route attention to synthetic nodes
- Used by both opencode capture path and desktop app for consistent classification
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:classify_tool fingerprint=3d4d616ba519818b8e5e0bce1f3e40f9f4ad6426cf3d159f156362ba0431fc2f body_fp=a20e4277a1f2c181c20a5821864e58ecd7893b27d1b16e8297b76972f5e49392 source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=util -->
Maps tool name to attention event type, returning None for tools with no symbol-level attention.

- Strips `trie_` prefix if present before lookup
- Unknown tools default to None to prevent silent attention injection
- File-edit tools from external surfaces matched by bare name for consistency
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:_DEFAULT_TOOL_EVENTS fingerprint=3750bca50f6508a5ec3c455175a40a094c452a09f6ad56ec3c6c90511ef5870e body_fp=6835e6839a6edff2acac9ae1cb67f631d5ac92644eaf9a437986b2cb671ef287 source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=config -->
Maps bare tool names to event types for file-edit tools from non-trie surfaces.

- Used as fallback when tool name is not found in main `TOOL_EVENT_TYPE` mapping
- Enables consistent event classification across different agent harnesses
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:RepoEdgeKind fingerprint=c32ccbcb7a4d55c0fd6177ed0c1b8d78c6262373b3e35fa92758bcd449837a84 body_fp=bca9174bf3004eb688967736086d8a4a9ae8283090f3a0774d35f5658ecb7e0c source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=model -->
Type alias defining the repository graph edge kinds extracted from Python AST during parsing.

- `calls` — function/method invocation relationship
- `references` — symbol reference without invocation  
- `imports` — module import dependency
- `contains` — structural containment (class contains method)
- `inherits` — class inheritance relationship
- `implements` — interface implementation relationship
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:ATTENTION_EDGE_KIND fingerprint=7d0b3b6e2b88b60e07d314ec4c50a8a3f4dc83cfdc01b25c96e0558de17c21ad body_fp=5e0c7ac59179549da01ff1c0bad6df2f4cd4fe9f1889125537eecfc0a13d6b2b source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=model -->
Defines the single edge kind used in the attention graph to represent reasoning paths between symbols.
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:DEFAULT_EDGE_KIND fingerprint=2202b5ce40eaac5bf163e3ec2ab0226b031e7c9d205590ed5884ab50a4c77538 body_fp=80d7c2656924ef699e148b01f2961524dfe3b09d8223e567514642df7f99531e source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=config -->
Fallback edge kind used for legacy or ambiguous edges before they are regenerated with explicit typing.
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:EDGE_WEIGHTS fingerprint=6e17741f9c7d91fdec58192d0b48cd381462886c0a6febe735e2a3b1a7d98ae0 body_fp=37723f0f1f31cfa444ae6662debebba32d21c12382c8c802603f1d23492764cf source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=config -->
Propagation weights for each edge kind in the attention gravity map, controlling how attention spreads between connected symbols.

- `trace`: 1.0 (strongest propagation, actual reasoning paths)
- `calls`: 1.0 (direct function/method invocations)
- `inherits`: 0.9 (class inheritance relationships)
- `implements`: 0.8 (interface implementation)
- `references`: 0.7 (symbol references without calls)
- `imports`: 0.5 (module import statements)
- `contains`: 0.2 (weakest, containment relationships)
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:PROPAGATION_FACTOR fingerprint=06a3d076fc1a2fbf7016fd3fb3eeecaf8a86b8ca48482775a1f4271a1c9a9438 body_fp=108d178d66a3be1bb72b5a1d50aeb7dffc40dd3979faca65feaf87d62c90fec2 source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=config -->
Scaling factor for attention propagation across graph edges (0.15).
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:PROPAGATION_HOPS fingerprint=98d72556013a60d0875ac74076eaacbc138ec1c1d61ac0c1b7b4b76057787423 body_fp=2f8cf2aedf37f5b71e8ccb0054258128ecf46efb867d019025ef1cb09e26bc37 source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=config -->
Maximum number of hops for attention propagation in the attention gravity map.
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:edge_weight fingerprint=6ad7fe33b054a3d745ac00f5e15da97779db371da76d8c9e4926300e8fd1f263 body_fp=5c59b12c03099b15e2542df29769fe64f93f4d32db0264d019e7b66f5d14aa76 source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=util -->
Returns the propagation weight for an edge kind, defaulting to 'calls' weight for unknown kinds.
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:SyntheticNode fingerprint=cd001639350f0b30514c7589ef80fcfaff8a281fac1ad6d0eb573f2d42dd1254 body_fp=77e76eab4090b91f345f630a5dc2e95375c4ed1b6ada1f44cd1e013438468eb3 source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=model -->
Type alias for synthetic nodes representing non-code cognition surfaces in the AGM visualization.
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:SYNTHETIC_NODES fingerprint=9cf1d52d4ede2bfc3a92c78c9d12701ace90d16c10527ee45f7791d5f37f6a0b body_fp=ba991b95721d59f31c0184483d5eaae86d0f2a782a59bbe959bcba21c0462ec4 source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=model -->
Tuple of synthetic node names representing non-code cognition surfaces that receive attention outside indexed symbols.
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:SYNTHETIC_QNAME_PREFIX fingerprint=d32e3e66b3b7686036229371f640c24e8012ebfc37996a724ab8926ce7127fcb body_fp=5c5bb2b4ed8d9a259173df6ea8b0c3b82ddaf6a984663e5001d93cec6f98d258 source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=config -->
Reserved prefix for synthetic node qnames to avoid collision with real symbols.
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:synthetic_qname fingerprint=8d791a4eacdfccb299b0f8e48953e843dff440efd97174d4e0eba34e247f34c6 body_fp=abd9881b4238678570ee71599e3a1461bdfdc9f6fc264e9c576b06bd8ca16b36 source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=util -->
Generates a reserved qname string for a synthetic node by prefixing it with `SYNTHETIC_QNAME_PREFIX`.
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:is_synthetic_qname fingerprint=c1eba6c8ab98c1a45bcfb75c58d4c50e3df822d0a297fe6ade1485adb0ba4872 body_fp=ce2e16a08f90e17f34875bba6a9b19600b8c5d63f91a7c8e1829aab3774017bd source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=util -->
Checks whether a qname belongs to a synthetic node by testing for the reserved prefix.
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:TOOL_SYNTHETIC_NODE fingerprint=5e915cc14de0a49b4c7c307dc921948b1cbc5a1a55eb7d55efd8c8013d7c0d3d body_fp=60966bddb61b84a9327c1ee78ed1908c7adcbd04f989503e4ee3f17c611618c4 source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=config -->
Maps bare tool names to synthetic nodes for routing tool attention outside the symbol graph.

- Routes filesystem-related tools to the "Filesystem" synthetic node
- Used by `classify_synthetic` to determine non-code attention surfaces
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:classify_synthetic fingerprint=36a9c641e896f2038914f9c323675ef6af0149876458a7068cdfbac60cd5d603 body_fp=6cee32ebad1b92f5970bd63a81396a2eff3597deca2a90c18e2daefce781f08e source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=util -->
Returns the synthetic node that should receive attention from a tool call, or None if the tool targets real symbols.

- Strips `trie_` prefix from tool names before lookup
- Uses `TOOL_SYNTHETIC_NODE` mapping to route filesystem tools to synthetic nodes
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:AttentionEvent fingerprint=8aa2912af2aba999bc69a83d71976974ff8f69c34ee9ae50a688c9a45abd8fae body_fp=e1a2f51ae9fc6f34b1ff3681269ec2a493841ab1c4aa6dab5e9e24db50010d50 source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=model -->
Immutable dataclass representing one unit of agent attention captured at a tool call.

- `target`: symbol qname or synthetic qname for the attention target
- `ts`: unix timestamp in seconds as float
- `weight`: denormalised event weight to avoid replay dependency on weight table
- `make()`: classmethod that auto-fills weight from EVENT_WEIGHTS table
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:AttentionEvent.make fingerprint=d4aa08091ce22cab41d810771a45a8bc6fdd773e9f8f3a9a81ae9707e00b7850 body_fp=385f8ce4c2546250da1ce20b356a534fe9482daddd60b8601a7dd4298e95324c source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=model -->
AttentionEvent.make builds an AttentionEvent instance, automatically setting weight from EVENT_WEIGHTS based on event_type.
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:InvestigationStatus fingerprint=ea0c3af27a990262b9affca042ace9f077a7bb14de50595711de45ea2850f516 body_fp=fa92dd231bc652d4fad6070f4d45fb8cba9d267b652d391283cfa787d1f47006 source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=model -->
Type alias defining valid investigation lifecycle states.

- `active`: investigation is ongoing
- `resolved`: investigation completed successfully
- `abandoned`: investigation stopped without resolution
- `superseded`: investigation replaced by a newer one
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:INVESTIGATION_STATUSES fingerprint=6943d16683b426ae5d1b8781771bfeae51a59e6977305769577325239c0a91f4 body_fp=9a6c905c7713af0b995dc056a9eb2d32ee875811aed0a1cfcb665efbff94261d source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=config -->
Tuple of all valid investigation status values that can be assigned to an Investigation.
<!-- trie:end -->
<!-- trie:section symbol=trie/attention:Investigation fingerprint=b2d7c2a1da822aa1f427ba7c57021eeafe09fa1890debfd17667e20b84e06567 body_fp=47e69301078416fbfe1de0d9067bd74b3ee3f1602a2e2d97219086e37ee73d24 source_ref=b77f44e716b6a6e867058db993e0a0b31177ecb1 role=model -->
Immutable dataclass representing an explicit investigation: a labelled span of agent cognition with durable identity.

- `label`: comes from user prompt first, LLM summary second—never graph-derived
- `created_at`: unix timestamp in seconds
- `status`: defaults to "active"
<!-- trie:end -->