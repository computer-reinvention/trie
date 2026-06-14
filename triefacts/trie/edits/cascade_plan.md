---
trie_version: 0.1.5
source: trie/edits/cascade_plan.py
file_fingerprint: 8b9be52af92719542fe0dffce372ffe71ce5dfddd52a9c994ad24c7b6ce10edf
last_synced_at: '2026-06-09T09:26:02Z'
description: "CascadePlan \u2014 the full edit target set, produced once, up front."
defines:
- kind: module
  qualified_name: trie/edits/cascade_plan:__module__
  lines: 1-117
- kind: class
  qualified_name: trie/edits/cascade_plan:CascadeNode
  lines: 21-24
- kind: class
  qualified_name: trie/edits/cascade_plan:CascadePlan
  lines: 28-36
- kind: method
  qualified_name: trie/edits/cascade_plan:CascadePlan.all_qnames
  lines: 35-36
- kind: function
  qualified_name: trie/edits/cascade_plan:build_cascade_plan
  lines: 39-87
- kind: function
  qualified_name: trie/edits/cascade_plan:neighbour_context
  lines: 90-116
incoming_refs: 3
outgoing_refs: 1
---
<!-- trie:section symbol=trie/edits/cascade_plan:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=aac8eb427dc5c43eed48b9a37aaa0ac82bce2fd990a315a0f76cfe7f49177d54 source_ref=f562d84d4ac86fdec4841a96af6aa2e0da4b71e6 role=orchestration -->
Defines CascadePlan data structure and functions for computing the full edit target set from seed symbols.

- **CascadeNode**: represents a symbol in the cascade with its qualified name, file path, and hop distance
- **CascadePlan**: contains seeds, cascaded nodes, file-to-qnames mapping, and hub stops
- **build_cascade_plan()**: walks caller graph from seed qnames using compute_cascade to build the plan
- **neighbour_context()**: returns callees and callers context for a symbol, capped at max_each per direction
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/cascade_plan:CascadeNode fingerprint=bdd121fd6ebb8d11962a6dabc7f6d4e27fbd40e1c2e8966528d3713a8976d38f body_fp=e59b229a31847ae24e707488b27bb82f25120243e921f34b71147cb48f3795c2 source_ref=f562d84d4ac86fdec4841a96af6aa2e0da4b71e6 role=model -->
Represents a single symbol in the cascade walk with its qualified name, file location, and hop distance from seed symbols.

- `hop`: 0 for directly patched seeds, 1+ for callers at increasing distances
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/cascade_plan:CascadePlan fingerprint=a1030a7584c88fb176a1a28420138de1f39b5afded6bf601f5000238f667788f body_fp=2f27a7b09d748ac9ddf6698a08781ee605c14b28282d580596ee1308f31eb4fb source_ref=f562d84d4ac86fdec4841a96af6aa2e0da4b71e6 role=model -->
Container for the complete set of symbols to edit after cascade expansion.

- `seeds`: initial directly patched qnames
- `cascaded`: caller symbols pulled in by the cascade walk
- `by_file`: groups qnames by file path for regeneration
- `hub_stops`: seed qnames whose expansion was halted at hub symbols
- `all_qnames`: property returning union of seeds and cascaded qnames
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/cascade_plan:CascadePlan.all_qnames fingerprint=67cbc4ccc20e1b2706d50532e87c62d0435369ad60b3bc91450a55e41f4d0fe6 body_fp=72e0d7a3db4c4ffba37293436b95be77086a86e9f33eb45863890bc1a60e39d6 source_ref=f562d84d4ac86fdec4841a96af6aa2e0da4b71e6 role=util -->
CascadePlan attribute that returns the union of seed qnames and all cascaded node qnames.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/cascade_plan:build_cascade_plan fingerprint=9ecdecd83b202e715ce0059a0f2f8ef1fc4c5a266080324ef31897838703163f body_fp=72121e6830f2a26420f877a5f464965ba53e9502d3341602f642170a69004e2d source_ref=f562d84d4ac86fdec4841a96af6aa2e0da4b71e6 role=orchestration -->
Walks the caller graph from seed symbols to build a complete CascadePlan for edit propagation.

- Collects unique files from seed symbols, then calls compute_cascade to find all affected callers
- Creates CascadeNode entries with hop distances for each cascaded symbol
- Groups all symbols (seeds + cascaded) by file path for batch processing
- Returns empty hub_stops list (feature not yet implemented)
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/cascade_plan:neighbour_context fingerprint=611864a5532f1d6e242ce13c4bc3460ca23521947181c9dfb59eb524533b5cfa body_fp=df7d45a87d0dfd535eb7cce03620f8b315c2b1d7fb202161625c4438f26e2b8b source_ref=f562d84d4ac86fdec4841a96af6aa2e0da4b71e6 role=util -->
Returns NeighbourCtx lists for callees and callers of the specified symbol from the store.

- `max_each`: limits results per direction to bound prompt size on hub symbols
<!-- trie:end -->