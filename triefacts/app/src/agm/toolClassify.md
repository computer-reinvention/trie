---
trie_version: 0.1.9
source: app/src/agm/toolClassify.ts
file_fingerprint: ea736873b680a1d15afcefd807be9356c523b6d2b31032c628e77d35b2bd3880
last_synced_at: '2026-06-17T16:36:26Z'
defines:
- kind: constant
  qualified_name: app/src/agm/toolClassify:TOOL_EVENT_TYPE
  lines: 8-34
- kind: constant
  qualified_name: app/src/agm/toolClassify:TOOL_SYNTHETIC_NODE
  lines: 36-46
- kind: function
  qualified_name: app/src/agm/toolClassify:bare
  lines: 48-50
- kind: function
  qualified_name: app/src/agm/toolClassify:classifyTool
  lines: 52-54
- kind: function
  qualified_name: app/src/agm/toolClassify:classifySynthetic
  lines: 56-58
- kind: function
  qualified_name: app/src/agm/toolClassify:syntheticTarget
  lines: 61-64
incoming_refs: 2
outgoing_refs: 5
---
<!-- trie:section symbol=app/src/agm/toolClassify:TOOL_EVENT_TYPE fingerprint=acbfb5786c2205b132a267969480a0bc5ad646f6d15376e28edae2a015f15206 body_fp=c0263868ce09b14b39467be140c04d99682aa971014bacaff43b64090ddff389 source_ref=1e44358470deccda6a7b80db6ef3fdca792b8bb4 role=config -->
Maps bare tool names to their `AttentionEventType` (`"read"`, `"trace"`, `"grep"`, `"write"`, or `null` for unclassified tools).
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/toolClassify:TOOL_SYNTHETIC_NODE fingerprint=37dbe2bad90233da420ed48bf7f95ad4575e7e9e568aebd64eb1a420d4bb3289 body_fp=787d5c857c8cfd5f9a718319f0a1de400a753f7d10666263bf8e13ed4d0d6935 source_ref=1e44358470deccda6a7b80db6ef3fdca792b8bb4 role=model -->
Map tool names to their `SyntheticNode` surface type for tools that target non-code nodes (filesystem, bash, web).
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/toolClassify:bare fingerprint=2c654faaff2aabbc1649e2593d811b1c6f5f58bb5e0ddbf19e0f4e00da337dcd body_fp=8d1f1061de0af8cdda6f0c1bff4cdb96a56a4ff97780f8a94ff04ec87b6730ee source_ref=1e44358470deccda6a7b80db6ef3fdca792b8bb4 role=util -->
Strip the `trie_` prefix from a tool name, returning the bare name unchanged if no prefix is present.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/toolClassify:classifyTool fingerprint=364cb23a77c4e5cb66a05296ac67270ac719f0c7c1740cd32952023e24c6afca body_fp=dc31ec0079614fd354595553b820eb7f2ea0a40db3562bf849b0c1052f9d2336 source_ref=1e44358470deccda6a7b80db6ef3fdca792b8bb4 role=domain -->
Map a tool name to its `AttentionEventType` (`"read"`, `"trace"`, `"grep"`, or `"write"`), stripping any `trie_` prefix before lookup.

- **returns** `null` if the tool name is not recognised.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/toolClassify:classifySynthetic fingerprint=c08b9543734e8dae4c727a58974ed20a0f15b405b813c9473ec803c61fb22f40 body_fp=42cdad1e033de9a7ab81c24eaa667e48c1638bb71137525bc12920ed6dbd41f4 source_ref=1e44358470deccda6a7b80db6ef3fdca792b8bb4 role=util -->
Look up the `SyntheticNode` surface (e.g. `"Filesystem"`, `"Bash"`, `"Web"`) for the given tool name, stripping any `trie_` prefix before lookup.

- **returns** `null` if the tool targets no synthetic node.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/toolClassify:syntheticTarget fingerprint=6a79f7afaf60d305bca9b735a32f1ecadb4390e0a7be5077ecf49e118541aada body_fp=d83e9d36b53aab7ef96dda2f72f8fd9b36bed03870704ce0eb1b1c3d7099b615 source_ref=1e44358470deccda6a7b80db6ef3fdca792b8bb4 role=util -->
Return the synthetic qname for the non-code surface targeted by `tool`, or `null` if none applies.
<!-- trie:end -->