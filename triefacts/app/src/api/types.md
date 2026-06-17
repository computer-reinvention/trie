---
trie_version: 0.1.9
source: app/src/api/types.ts
file_fingerprint: af87d934d7b1eba68d022242355f1d370f1db7b7bb35e8ba99ef881a4da7d5ad
last_synced_at: '2026-06-17T16:40:10Z'
defines:
- kind: type
  qualified_name: app/src/api/types:SymbolKind
  lines: 6-16
- kind: type
  qualified_name: app/src/api/types:AgentState
  lines: 17-24
- kind: interface
  qualified_name: app/src/api/types:SymbolHit
  lines: 26-39
- kind: interface
  qualified_name: app/src/api/types:ReadResult
  lines: 41-50
- kind: interface
  qualified_name: app/src/api/types:CallerCallee
  lines: 52-56
- kind: interface
  qualified_name: app/src/api/types:TraceResult
  lines: 58-64
- kind: interface
  qualified_name: app/src/api/types:TraceEdge
  lines: 66-70
- kind: type
  qualified_name: app/src/api/types:NodeClass
  lines: 77-85
- kind: interface
  qualified_name: app/src/api/types:SystemModelNode
  lines: 87-108
- kind: interface
  qualified_name: app/src/api/types:GroupSummary
  lines: 110-115
- kind: interface
  qualified_name: app/src/api/types:GroupFlow
  lines: 117-121
- kind: interface
  qualified_name: app/src/api/types:ComponentAxis
  lines: 123-127
- kind: interface
  qualified_name: app/src/api/types:SystemModel
  lines: 129-141
- kind: type
  qualified_name: app/src/api/types:GroupingAxis
  lines: 143-143
- kind: interface
  qualified_name: app/src/api/types:ProjectSummary
  lines: 145-153
- kind: interface
  qualified_name: app/src/api/types:SymbolsByFileResult
  lines: 155-158
- kind: interface
  qualified_name: app/src/api/types:TriefactSection
  lines: 162-172
- kind: interface
  qualified_name: app/src/api/types:FileTriefactResult
  lines: 174-180
- kind: interface
  qualified_name: app/src/api/types:FileSourceResult
  lines: 184-188
- kind: interface
  qualified_name: app/src/api/types:ActivityStatus
  lines: 192-202
- kind: interface
  qualified_name: app/src/api/types:ActivityPending
  lines: 204-209
- kind: interface
  qualified_name: app/src/api/types:ActivityResult
  lines: 211-214
- kind: interface
  qualified_name: app/src/api/types:OpencodeSession
  lines: 220-228
- kind: interface
  qualified_name: app/src/api/types:OpencodeModelInfo
  lines: 232-235
- kind: interface
  qualified_name: app/src/api/types:OpencodeProviderInfo
  lines: 237-241
- kind: interface
  qualified_name: app/src/api/types:OpencodeProvidersResult
  lines: 243-246
- kind: interface
  qualified_name: app/src/api/types:ModelRef
  lines: 249-252
- kind: interface
  qualified_name: app/src/api/types:OpencodeUserInfo
  lines: 255-262
- kind: interface
  qualified_name: app/src/api/types:OpencodeTokens
  lines: 264-270
- kind: interface
  qualified_name: app/src/api/types:OpencodeAssistantInfo
  lines: 272-285
- kind: type
  qualified_name: app/src/api/types:OpencodeMessageInfo
  lines: 287-287
- kind: interface
  qualified_name: app/src/api/types:TextPart
  lines: 290-296
- kind: interface
  qualified_name: app/src/api/types:ReasoningPart
  lines: 297-301
- kind: type
  qualified_name: app/src/api/types:ToolPartStatus
  lines: 302-302
- kind: interface
  qualified_name: app/src/api/types:ToolPart
  lines: 303-317
- kind: interface
  qualified_name: app/src/api/types:FilePartT
  lines: 318-324
- kind: interface
  qualified_name: app/src/api/types:PatchPartT
  lines: 325-330
- kind: interface
  qualified_name: app/src/api/types:GenericPart
  lines: 331-335
- kind: type
  qualified_name: app/src/api/types:OpencodePart
  lines: 337-337
- kind: interface
  qualified_name: app/src/api/types:OpencodeMessage
  lines: 339-342
- kind: type
  qualified_name: app/src/api/types:PermissionReply
  lines: 345-345
- kind: interface
  qualified_name: app/src/api/types:PermissionRequest
  lines: 346-356
- kind: type
  qualified_name: app/src/api/types:PatchKind
  lines: 364-364
- kind: type
  qualified_name: app/src/api/types:PatchOrigin
  lines: 365-365
- kind: interface
  qualified_name: app/src/api/types:PatchNote
  lines: 367-372
- kind: interface
  qualified_name: app/src/api/types:BlastRadius
  lines: 374-379
- kind: interface
  qualified_name: app/src/api/types:CascadeImpactNode
  lines: 382-386
- kind: interface
  qualified_name: app/src/api/types:BlastRadiusResult
  lines: 387-394
- kind: interface
  qualified_name: app/src/api/types:PatchEntry
  lines: 397-406
- kind: interface
  qualified_name: app/src/api/types:PatchList
  lines: 408-413
- kind: interface
  qualified_name: app/src/api/types:ApplyProgress
  lines: 416-421
- kind: interface
  qualified_name: app/src/api/types:ApplyReport
  lines: 424-446
- kind: interface
  qualified_name: app/src/api/types:DesktopEvent
  lines: 449-453
- kind: interface
  qualified_name: app/src/api/types:DesktopToolStartEvent
  lines: 455-463
- kind: interface
  qualified_name: app/src/api/types:DesktopToolDoneEvent
  lines: 465-475
- kind: interface
  qualified_name: app/src/api/types:DesktopTextDeltaEvent
  lines: 477-482
- kind: interface
  qualified_name: app/src/api/types:DesktopSessionStatusEvent
  lines: 484-487
- kind: interface
  qualified_name: app/src/api/types:DesktopFileEditedEvent
  lines: 489-491
- kind: interface
  qualified_name: app/src/api/types:DesktopReasoningDeltaEvent
  lines: 493-498
- kind: interface
  qualified_name: app/src/api/types:DesktopMessageUpdatedEvent
  lines: 501-504
- kind: interface
  qualified_name: app/src/api/types:DesktopPartUpdatedEvent
  lines: 507-511
- kind: interface
  qualified_name: app/src/api/types:DesktopPermissionAskedEvent
  lines: 513-522
- kind: interface
  qualified_name: app/src/api/types:DesktopPermissionRepliedEvent
  lines: 524-528
- kind: interface
  qualified_name: app/src/api/types:TurnEvent
  lines: 531-540
- kind: type
  qualified_name: app/src/api/types:AttentionEventType
  lines: 556-556
- kind: constant
  qualified_name: app/src/api/types:EVENT_WEIGHTS
  lines: 559-564
- kind: constant
  qualified_name: app/src/api/types:LIVE_HALFLIFE_SECONDS
  lines: 567-572
- kind: constant
  qualified_name: app/src/api/types:HISTORICAL_HALFLIFE_SECONDS
  lines: 575-575
- kind: function
  qualified_name: app/src/api/types:liveLambda
  lines: 577-579
- kind: constant
  qualified_name: app/src/api/types:HISTORICAL_LAMBDA
  lines: 581-581
- kind: function
  qualified_name: app/src/api/types:displayMass
  lines: 584-586
- kind: type
  qualified_name: app/src/api/types:RepoEdgeKind
  lines: 589-595
- kind: constant
  qualified_name: app/src/api/types:ATTENTION_EDGE_KIND
  lines: 597-597
- kind: constant
  qualified_name: app/src/api/types:DEFAULT_EDGE_KIND
  lines: 598-598
- kind: constant
  qualified_name: app/src/api/types:EDGE_WEIGHTS
  lines: 601-609
- kind: constant
  qualified_name: app/src/api/types:PROPAGATION_FACTOR
  lines: 611-611
- kind: constant
  qualified_name: app/src/api/types:PROPAGATION_HOPS
  lines: 612-612
- kind: function
  qualified_name: app/src/api/types:edgeWeight
  lines: 614-616
- kind: type
  qualified_name: app/src/api/types:SyntheticNode
  lines: 619-619
- kind: constant
  qualified_name: app/src/api/types:SYNTHETIC_NODES
  lines: 621-627
- kind: constant
  qualified_name: app/src/api/types:SYNTHETIC_QNAME_PREFIX
  lines: 629-629
- kind: function
  qualified_name: app/src/api/types:syntheticQname
  lines: 631-633
- kind: function
  qualified_name: app/src/api/types:isSyntheticQname
  lines: 635-637
- kind: constant
  qualified_name: app/src/api/types:SYNTHETIC_FILE_PREFIX
  lines: 646-646
- kind: function
  qualified_name: app/src/api/types:syntheticFileQname
  lines: 648-650
- kind: function
  qualified_name: app/src/api/types:isSyntheticFileQname
  lines: 652-654
- kind: function
  qualified_name: app/src/api/types:syntheticFilePath
  lines: 657-659
- kind: function
  qualified_name: app/src/api/types:looksLikeFilePath
  lines: 665-669
- kind: interface
  qualified_name: app/src/api/types:AttentionEvent
  lines: 672-680
- kind: interface
  qualified_name: app/src/api/types:TypedEdge
  lines: 683-687
- kind: type
  qualified_name: app/src/api/types:InvestigationStatus
  lines: 690-690
- kind: interface
  qualified_name: app/src/api/types:Investigation
  lines: 692-703
- kind: interface
  qualified_name: app/src/api/types:AttentionState
  lines: 706-709
incoming_refs: 159
outgoing_refs: 0
---
<!-- trie:section symbol=app/src/api/types:SymbolKind fingerprint=e1c2aea88e1eec3cc8404f9e0f7d32a4ecfcd44d4af5a4d120f730140a9cce97 body_fp=b409ef177095fbbcacedfd1728cd510df273d9d935880d108c520c8087854cae source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Union of all valid symbol classification strings, mirroring `trie.parse.types.KINDS` in the Python backend.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:AgentState fingerprint=8a2dcb1861faa61098b2ae0e7cd746f1847a147996f514dd77bc0b733cfb1912 body_fp=ff6cbd522a772ac61de8df72ca7ae8b7a8ef01ed9e8f82c3d5b1e1d7b73fb07d source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Union of all valid agent activity states used across the desktop event protocol.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:SymbolHit fingerprint=3db6bac9768f4ba1a81e1db40fc205e961f12a5cf5dab18b56375b56d3737239 body_fp=e3c65defdaa37dc37712adc3f069fccb6f562298f220a466a6eda63429396d5f source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents a single symbol search result returned from the trie index.

- `signature`: `null` when the symbol has no extractable signature.
- `inbound_count` / `outbound_count`: call-graph edge counts for this symbol.
- `pending_patch_count`: number of uncommitted patches targeting this symbol.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:ReadResult fingerprint=d445f5dbae14c093988c8446165a9c6b5915cedcccd8d5d8f4af26f1ad9d4e64 body_fp=b4add38ef0004b136dc8455117fd98d064d1b7e13ac3070cd83567b8e433b242 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents the full documentation payload returned when reading a single symbol.

- `source_pointer`: opaque reference locating the symbol's source position
- `notes`: optional advisory strings attached by the backend
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:CallerCallee fingerprint=c182d5b9953b77d50a237df492ad72a97ff60eab7bffc595ebcc711909ecb25c body_fp=658bd0a5bbd580ec07aa5ddf1829c65d68b43265ced9c6ce25485434b4ecf955 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents a single caller or callee symbol in a `ReadResult` call graph, carrying its qualified name, signature, and one-line summary.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:TraceResult fingerprint=65d48851d5fd9ddd0fd8c6185e11273ed153ca6f9b747d9ac49a18761afcee98 body_fp=89f9f18aef38a98e841a11ec986ae5360f4ef381da4a5037a42a2b23583b2086 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Holds a call-trace result with a root symbol, a flat node map, and directed edges.

- `root`: the starting symbol's qname, signature, and one-liner
- `nodes`: keyed by qname; omits one_liner (only signature + one_liner stored)
- `truncated_at`: qnames where traversal was halted due to depth/fan-out limits
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:TraceEdge fingerprint=b103c85a636802e6f6af101588f4bfe56f9ed3894b7045f89607071221b6ad1b body_fp=780009580ac7ecae7f621dbf1a814d5e01f20d0eac8a9bcf89f09c170c65d5a8 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents a single directed edge in a call-graph trace result.

- `direction`: `"in"` for an inbound caller edge, `"out"` for an outbound callee edge.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:NodeClass fingerprint=d15a5e0af5906c3aa05d12133b90028c39ea04f29a6cda7252bfb747692a8a4a body_fp=5f8081acb606ba5f9c84fb26238a4333767f8d91b018d5925ca8bdd9b03ae5b6 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Discriminated union classifying a `SystemModelNode`'s structural role in the call-graph topology.

- `"door"` — high-inbound entry boundary node
- `"hub"` — high-centrality connector node
- `"bedrock"` — foundational low-level dependency
- `"exit"` — node whose primary purpose is leaving the system boundary
- `"orphan"` — node with no edges
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:SystemModelNode fingerprint=9c46ef1c948d0ea39366fdabc093fb89cd0a660bc6ea1867580e2f53de197c30 body_fp=43b9eacf25729d862a08bc24ddf50882300cf6b4740258d98c0f74c2a046cb1e source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents a single node in the system-model graph, mirroring `system_model_to_dict()` in `trie/graph/system_model.py`.

- `cls`: structural classification (`NodeClass`) used for visual grouping and salience scoring.
- `salience`: computed importance score driving node sizing in the graph view.
- `betweenness`: graph-centrality measure; high values indicate hub nodes.
- `community`: integer cluster ID assigned by community-detection algorithm.
- `prod_inbound_count`: inbound edges from production (non-test) nodes only.
- `x`, `y`: pre-computed layout coordinates.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:GroupSummary fingerprint=35e6655119202da60818add006ba3770e65bb2b68755bdbf923ae3e50161a406 body_fp=1e3dbcf600326b6edfb9fd047e59b541b432eb9a487cd954d3c82c8e0d495e1e source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Describes a grouped set of nodes in a `ComponentAxis`, counting total, door, and hub members.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:GroupFlow fingerprint=c99ceb6f17000ae2ec33fa370a48b76543ef9a053a51ea1ac0c2486be1d856a4 body_fp=d88c17b3b3ce92634cd650adbf590e9255e697c23df6e869ad6b0b156446792b source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents a directed flow between two component groups with an associated edge weight.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:ComponentAxis fingerprint=eb5474d8e11804ac73bf999245366c59978cba115ab3920442be32c1bf865ba6 body_fp=e5849668edb4e2da0839e6a209009243ec133e305c34d2c3899453a3de6587f7 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Groups symbol-graph nodes by one axis and carries inter-group flow data for the system model.

- `axis`: discriminates whether grouping is by architectural role or subsystem.
- `groups`: one `GroupSummary` per distinct axis value.
- `flows`: directed weighted edges between axis groups.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:SystemModel fingerprint=5665f033018ac86c351885ab82d27f947a208ea3364afb2eaa24384702d04cdf body_fp=cf0fc45b4ff8cd7bb4ae21dde3019be0df1e15d2a41e6acee61e6f43d0b6cf6e source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represent the full system-model payload returned by the graph backend, containing all nodes, grouping axes, landmark qnames, and aggregate stats.

- `landmarks`: qnames of structurally significant nodes surfaced by the backend
- `stats.class_counts`: map of `NodeClass` string → count of nodes in that class
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:GroupingAxis fingerprint=01ae21087b6d27a1335eddf0c7ab9250a3699ad0851e3935d4ac936df4345798 body_fp=22f048774973915a2b94a7a9670268a69aaeee200bf0b2a61f3fa44fa4a9c9a8 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Discriminated union constraining the axis used to group `SystemModel` nodes to either `"role"` or `"subsystem"`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:ProjectSummary fingerprint=2529739002db5bb3b96506fd1685ac8d7bdf20d751f2f455cf6c54ed0df48057 body_fp=569dce999e11b22cf802c6956ba9b3f8409fe116f674ed2288b983afa0084b67 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Holds top-level project statistics returned by the project summary endpoint.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:SymbolsByFileResult fingerprint=9fe709ccc69e641d1135628ea50faa637c20af3f2db88adfee39ef7f18fe68df body_fp=717d4438e1b279bcb3a6122b7699d7cb9c4baf94924464ec12fc62332ac3364d source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Groups all `SymbolHit` entries belonging to a single source file.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:TriefactSection fingerprint=d0e3e4d8eb29d2767ed5da793e799dd6df52e3aa377fa559c578362d0f33b90f body_fp=63981d9946bce34c1895e41c54026da1d240f207df16a58c0b38464605abe6a7 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents one symbol section within a file triefact document, mirroring `TrieTools.file_triefact()` output.

- `fingerprint` — hash of the full section (metadata + body)
- `body_fingerprint` — hash of the body text only
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:FileTriefactResult fingerprint=851544f3c2fcd643007c38beb3a6d1e590fd0371ed9d0413d38c88371fd14349 body_fp=54370039234c6615b46226a9bb2ff34fa6cbc17d03844f837f7b28fe818d5e75 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents the full triefact document for a single source file, as returned by `TrieTools.file_triefact()`.

- `exists`: false when no triefact has been generated for the file yet
- `front_matter`: arbitrary YAML/JSON metadata from the triefact header
- `sections`: ordered list of per-symbol triefact sections within the file
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:FileSourceResult fingerprint=5eee8065fb982c0f385e0d75892cd0798ca0fffe6926ddd3e38a08d0e6b14ee4 body_fp=0e36a496aaab041a9b99c43d786623e4b46f25d8b3c72c722aa452960dc9b4d4 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents raw source file content returned by the `/desktop/graph/file-source` endpoint.

- `type`: discriminates how `content` should be rendered (`"text"`, `"binary"`, `"image"`, or `"patch"`).
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:ActivityStatus fingerprint=d9b3eb580b0a0dd870b1c95648387aa09249876829f3563cdf6e7ffc606d3e08 body_fp=2ba107d63110d7edae012f523e15e9ae0deb8dcf5f4144e9de669f0e9ab89d8b source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents the live writer-process status returned by `ActivityResult`.

- `state`: lifecycle phase of the background trie writer process
- `pid`: OS process ID of the writer
- `done` / `total`: progress counters for the current operation
- `updated_at`: Unix timestamp of the last status update
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:ActivityPending fingerprint=c97c4fdf667417ec6353d5f46fd83c6d868e2ee2a099f9ddaa2ad6a5bd18908a body_fp=1a8ff0234a4149193d97617367020e47704f593a9e43a6c67b1b92433cb06308 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents the set of stale symbols awaiting re-indexing, as returned by `TrieTools.activity()`.

- `stale`: qnames of symbols whose triefact is out of date
- `head`: current VCS commit hash at computation time
- `computed_at`: Unix timestamp when this snapshot was taken
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:ActivityResult fingerprint=3e4471507a6e6f530b3ce4eb1641d6741f08de3f01da351b2b306419dbf2ad7b body_fp=0f47f75893ba390cafeba4b4053c58835e3c454da0a61f41ddc98e73f5d577c8 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Combines `ActivityStatus` and optional `ActivityPending` into a single activity query response.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:OpencodeSession fingerprint=42af5ec8558346921641c64b77259ea1209712ed522d3b4122addb6df0acf3c2 body_fp=bee5d753b82a49120fe9929a8a5018d54f3bdc185cc3f0694a386a01fc17b62c source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents an opencode session, typing only the fields consumed by the UI; accepts unknown extra fields via index signature.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:OpencodeModelInfo fingerprint=c1b65619f7cf1c665ba83e58b95720d196423f92507134bb47ee81e62bf94cc2 body_fp=f415783c4f788e17feea60f2fd544233b524cc1ff88cdecdcac269654345d6cc source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents a single model entry returned by `GET /config/providers`, typed to the fields the model switcher needs.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:OpencodeProviderInfo fingerprint=8997eb12ff214ecb3c88c55eb7b9a29506a1d41da24a61a339a3f85131e4ddd8 body_fp=59cb25a79d743b05d035c909d8c887bc72079cff35d16b3cf2f692a74697aed8 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Describes a single provider entry returned by `GET /config/providers`, including its available models.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:OpencodeProvidersResult fingerprint=097100d5e76a1a7f5e6e891ea469a2a393bbdabec66b61105f382bbcd77d878c body_fp=e51279dc144515dc34142ee2016e9f50984607a80b70672a05500814bc53f09f source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Shape returned by `GET /config/providers` listing available providers and the default model per provider.

- `default`: maps provider ID to the selected model ID for that provider.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:ModelRef fingerprint=055b342c08c0c7e94fa61fb79444f70f87a339261c61088b37b98a0f6d189d9e body_fp=b25866b90e248df0aed530078d68997aa3953b06b9386d1954486cd2e99b95b8 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents a concrete model selection identifying a provider and model pair used when sending a message.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:OpencodeUserInfo fingerprint=a84a5e0d794e64ffe928a8e8daecbbf738ede447cfa2d8665604ea1fd1f8ed20 body_fp=dfa36cfc4581531fd29c1ffc0bef75505aba31ccd90514043819458132ad13cb source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents the `info` block for a user-role opencode message.

- `role`: always `"user"`; discriminates this type from `OpencodeAssistantInfo`
- `model`: optional override specifying which provider/model the user selected
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:OpencodeTokens fingerprint=b86e48d3cf419673e0a06dcaefeea86fc8aff38ef5b5f572759e01b97d14ab1c body_fp=6efb350fbb932a3a881c670daddada9291779802e35f54b8bd535ec1e647615f source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents token usage counts for an opencode assistant message turn.

- `total`: optional aggregate; may be absent if not reported by the provider
- `cache`: split into `read` and `write` sub-counts
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:OpencodeAssistantInfo fingerprint=9d145e5a95323b6677a5bc6c82ddb9a2741bdd32dc93d6a0c63cb185f84491bf body_fp=01866b1f14986fffdd6eee735bd5b1c2b9fa2ba14e620b2ef17484e81db92bfe source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Typed shape for an opencode assistant message's `info` block, discriminated by `role: "assistant"`.

- `tokens`: breakdown of token usage via `OpencodeTokens`
- `finish`: stop reason string from the model
- `error.isRetryable`: whether the caller may retry on this error
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:OpencodeMessageInfo fingerprint=4a65ff94457064ca5f54cfaed06fbcfb33fb0f9a2fcc25bf82db7e3d4e0e18c0 body_fp=f833c29171cf1bd40a3a4d5435d19e2853a9c78b49c8456293bd54a5693ab3f8 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Discriminated union of `OpencodeUserInfo` and `OpencodeAssistantInfo`, keyed on `role`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:TextPart fingerprint=ac39f114d4ab2f238f8409b5ba41b9d59974751802d5121ec86e3f4b010494ad body_fp=350fcf6612f40bf313f3f40e896bf55febce9b4ab7b1c92599b71ddd723e4824 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents a plain-text message part in an `OpencodeMessage`, discriminated by `type: "text"`.

- `synthetic`: part was generated outside normal LLM output
- `ignored`: part should be skipped during rendering
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:ReasoningPart fingerprint=7197185dfddb2ebadeb70b83756002c600f45994f1feeefda797920122c7abfb body_fp=7d0a64477d19032428ed16fe86b60073372327b0317b164d465f2a4c9e1e2e48 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents a reasoning-type message part with a fixed `type` discriminant of `"reasoning"` and its text content.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:ToolPartStatus fingerprint=7f4496a78710b7e6fe3eab5699bf6c1f36d4cb92508fedaa142223d5dcd6cf16 body_fp=37248cda5579a94f8b73c6e2eef6a3b97c2d7a9352ed3fa25a2fb82273a577f5 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Discriminated union representing the four lifecycle states of a `ToolPart`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:ToolPart fingerprint=59f08ccf8192311ea1faf8b6511f2d15685798e6a5fa622bf851dc42d33b43b7 body_fp=d2e197cbd5598c349ac29f1dd0f7802979283fac09d8eea4fec51151f3b8457e source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents a tool-call message part, carrying the full mutable `state` of one tool invocation.

- `callID`: correlates this part to a specific tool call within a message
- `state.status`: lifecycle stage — `"pending" | "running" | "completed" | "error"`
- `state.time`: optional start/end epoch timestamps in milliseconds
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:FilePartT fingerprint=4778f84aa6ea7bc6f9087bad30f55e099d37b909a37a59c750a399165b9e73e0 body_fp=b9500311219aa5f66e647ed9d57ce39d5ac9a3cabd55794601a28d7c42cf5f9c source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents a file attachment part within an `OpencodeMessage`, carrying MIME type and a URL reference.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:PatchPartT fingerprint=c5dd35a87bc55ba9795f43416937227c82374a81fd6de1ffc0f6580613981d39 body_fp=593b5298e30b2bd731cc9af438753043451f5f78cda4d4db839bb53feb0526ab source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents a patch-type message part carrying a commit hash and the list of affected file paths.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:GenericPart fingerprint=61388f8e272e53565e9cf401ed88c8df54361ca5d833153031090ff9613c8e8d body_fp=69ca1253c453093eb2997a284936a359a21a96d01b765f44ff03d62d308b16d8 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Fallback message-part shape accepting any `type` string and arbitrary extra fields via index signature.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:OpencodePart fingerprint=e0d2f67c08e6f64ba686b07617b2927b9990a5fa189d5fe5ce830fee6ec5d208 body_fp=09a18339d906a349abc37cacacefdb3dae7a02c33af81c6e130c191b7492cc26 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Discriminated union of all message part variants a transcript message can contain.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:OpencodeMessage fingerprint=ae8fd9a6f610e3d67e65b04fe4a5bddd9270a506ed3a4857425ebbfb2a30b879 body_fp=ad126b1fc1ebcd462ed1641d0f65191c3cc7e695d2dfbf612bf156b07b737af6 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Pairs a discriminated `OpencodeMessageInfo` (user or assistant) with its ordered list of `OpencodePart` content parts.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:PermissionReply fingerprint=1f181a697c02d0c3d67d901ad76d3b91d282180374253237f842fbe3f3740835 body_fp=79b106f53a98576c71d7bcc37a7a8141069d7aa9fcf719af767daaca3ee9bbf4 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Union type representing the three possible replies to an opencode permission request.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:PermissionRequest fingerprint=88511a19ed2fcb421498f7411e4bb85f2fcd442aafb756983e3d38ae078218de body_fp=3e67638bd4d279ed6f70ef824df05a109c33df98976fb5b2c456ecfa8599293b source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents a pending tool-permission request sent from the opencode backend, mirroring `permission/index.ts Request`.

- `patterns`: glob patterns the permission applies to
- `always`: patterns already permanently allowed
- `callID` / `messageID`: optional correlation back to the originating tool call and message
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:PatchKind fingerprint=542e9e9d006e4dc36b00e4c015c5f08b1833bdb87fce76909a4d00631e0837e2 body_fp=82315a9853227f604415975467fea862fc65e1719f8e21b2bd9177ae80f0752c source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Union type enumerating the four mutation kinds a patch can represent.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:PatchOrigin fingerprint=c66ce1445c9a0266f38237c742efd10be2339f98b7584522e2279eb74ad332a7 body_fp=7b7a860fb1756d3c09b83832035ff1a5fcb927bb1441521637cee9b725efb2e1 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Discriminated string union identifying the source of a patch: agent-authored, cascade-propagated, or both.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:PatchNote fingerprint=146add0ef24d7bdf4b16818ed1528a38824df84253c9ca93a975ba597c7dbd6c body_fp=e2996e7eae8e92f5746fd942a1dfc1cafc449ad43624495c51b3fc25d82f19fa source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Holds optional human-readable annotation attached to a pending patch.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:BlastRadius fingerprint=f6bb06b818dfdf4e5fdb7d565c708dba1d55ba4ae220076cd4c5d190ddcc66f6 body_fp=382fd2441d9fac7ca3d7b9ebcf6b45594220479cd031c56c0cc8a68bbe0e79a2 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents the computed blast-radius summary for a pending patch.

- `hubs_stopped_at`: qnames of hub nodes where cascade propagation was halted.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:CascadeImpactNode fingerprint=5a70e11c13c60723e9a91ae7bb7c51921bad737b09ec81f3ae5c8e042d995e40 body_fp=877028f0506e4b70d6e0e9b8a6c2790a82d921f08ddfd21653b0c6b36778c460 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents a single node in a blast-radius cascade result, identifying the affected symbol and its hop distance from the changed symbol.

- `hop`: number of edges from the directly-changed symbol to this node
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:BlastRadiusResult fingerprint=5f0d45d089ccb591dd172e402cd402940a9c3af8fef23b205036a85e69dbf4a5 body_fp=8e34305f1be1cd4ac2e1e6eacf09dad4f20d6c96f768da32900bbe058c86a4e3 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Full blast-radius result returned by `/desktop/graph/blast-radius`, wrapping computed cascade impact for a single symbol.

- `cascade`: ordered list of transitively affected nodes with hop distance and file
- `hubs_stopped_at`: qnames where cascade propagation was halted at hub boundaries
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:PatchEntry fingerprint=bde4904f60a7590c02d95316a432acbf0f68c13298f187f328588fd530e6215b body_fp=6858043264703ce0034424f0d8f6df730d2929f04fc3acff672cb24e7108b9d8 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents one symbol's grouped pending patches as returned by `patch_list`.

- `origin`: whether patches came from the agent, cascade propagation, or both
- `kind`: optional until the cascade pipeline lands; classifies the edit
- `blast_radius`: optional pre-computed impact summary for the symbol
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:PatchList fingerprint=4a774a18c2e584aedb4984abc88aec980a19bb56bbc7824ed24a9f8d350f9767 body_fp=42868502cffa352207386085387f76a2bed9c10d215fd3aef753703a2f0bbc50 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Holds the full list of pending symbol patches returned by `patch_list`, with optional cascade-plan metadata.

- `patches`: ordered list of per-symbol `PatchEntry` records
- `apply_in_progress`: set when a commit/apply operation is running
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:ApplyProgress fingerprint=89ae756b089e6aa58e92dce1189d18ff8ab524fdbe111b57617591a385d9d3b5 body_fp=836e899252076374a65e686936936ff470098c1f513c1119a7389534343f2822 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents live progress of a cascade apply operation.

- `phase`: current pipeline stage; known values include `"merge"`, `"generate"`, `"fixup"`, `"commit"`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:ApplyReport fingerprint=b3991ff0e3391987ade31e896c41132a7a4ac52752e63c7a774df73c1f91c937 body_fp=ed4b06de114931d626355a133ce2ca20d47376c6fe6f1eb9a27b7b6d23c9f654 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Hand-off artifact returned by `commit()` describing the outcome of a cascade patch apply.

- `ok` — top-level success flag
- `applied` — counts and per-file detail for successfully applied symbols
- `cascade_applied` — symbols resolved via cascade propagation
- `unresolved` — symbols that failed, with stage, error code, and optional repatch hint
- `totals` — aggregate requested/applied/unresolved counts
- `applied_count` / `failed` — looser shape from current `patch_apply` backend; both optional
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:DesktopEvent fingerprint=a3e1aea951aff2d5eda9fdfb856b9ff2b56497f1ea948cf9e77ec5943dd7b4c9 body_fp=15a760ea121e776a53626c7bc9fbc768ee1edcc828c63d10472e9553651248ae source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Generic SSE event envelope sent by the desktop backend, carrying an opaque `properties` bag discriminated by `type`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:DesktopToolStartEvent fingerprint=759c7c9e744bc450ae9b7d68b566ca1a500e5d32fec3b98875224f06f81559c0 body_fp=1f5a4399b385e18b4610d448a402e4b5420abff3d94683708fad3ba42025b854 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
SSE event payload fired when a tool call begins within an opencode session message.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:DesktopToolDoneEvent fingerprint=58510d4b8aa2fbf8e6ad3344a3ac0093a72865f8e461764812536fbee898e1d0 body_fp=48316bb76e4bab92691191af22f1715ecfcc04006ab1aa20449a58bc51a307ef source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
SSE payload for a completed tool call, carrying full input/output and wall-clock timing.

- `output`: tool result text, or `null` if the tool produced no output
- `error`: error message string, or `null` on success
- `time`: both `start` and `end` timestamps are present (unlike `DesktopToolStartEvent`)
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:DesktopTextDeltaEvent fingerprint=5b47925c8ac738fc9aa6a4082e8cdeff1f7fab739ba13b01394fbc2a0de70dcd body_fp=1c9b8a02b09929ec4a1d1e9ce9be2186ca1975fef28dc50b2de7ceb7b75268f4 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
SSE event carrying an incremental text delta for a specific message part within a session.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:DesktopSessionStatusEvent fingerprint=ed0f6189f5a3e7feb910c8b8c965916e0a02be94140720f71f3c2150eb76770f body_fp=cfd4cc8a6196cef03529c141b0fd80e04db89f82e8d722b9a4678c84eaca8732 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
SSE event carrying a session's current run status and optional error string.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:DesktopFileEditedEvent fingerprint=7bbe35d4886b74d3198e06b583ce612ecfed9fe327d2d8b64e35a9d7e011f118 body_fp=057640cd8cf9057e09e26599c3b68f4cf6dc6014a898ecad524efeb5ea6ef7a6 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
SSE event payload emitted when a file is edited on the desktop.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:DesktopReasoningDeltaEvent fingerprint=562726884b101ca379a0dae857b3a0312381e120035ce0a2bac035dd5742f732 body_fp=c3e2110f69a43ec866d5157b07dc698d272ce762c8f3476eb81623e0e66cb732 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
SSE event carrying a single reasoning-text delta for a specific message part.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:DesktopMessageUpdatedEvent fingerprint=49031cffd2540ce7a500bb13b47c137772e7369d948f3946df781f44f2acb073 body_fp=b86bb3ae6fda5070084563276090724675bd5b43f697c568c932207af6f0894c source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Carries a full `desktop.message.updated` SSE event, delivering the complete message info for a given session.

- `info`: discriminated union of `OpencodeUserInfo` or `OpencodeAssistantInfo`
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:DesktopPartUpdatedEvent fingerprint=71e1244b374ec21c6f7263e4258922fee3a726272c789273a9ad5a4ca65b3c99 body_fp=46ec756f0ed13b7de9198136b3dd1af09f928c9d2934a7b659f065c348330ed0 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
SSE payload for `desktop.part.updated` events carrying a full `OpencodePart` upsert for a specific message.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:DesktopPermissionAskedEvent fingerprint=56ca81ae19db3f5e4cf8cc8a1f439411d31f275e4c0bea7d5bbec779b60d8e4b body_fp=da8cd0a73b28da949e3e7433ce5ea7e9d5a3438c7b74f8d9c4ebd99c7a67c27f source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
SSE event payload for a permission request surfaced to the UI from the desktop backend.

- `always`: list of patterns already granted unconditionally
- `callID` / `messageID`: optional correlation to the originating tool call and message
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:DesktopPermissionRepliedEvent fingerprint=90922d3b4e941e692113e1323365be5e4bacf59f8d7a560f55dae35563607f1d body_fp=fb472924a17ad1b2901bf180ee2fa3dd775980522f0e5f3159621db9b0aca07d source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Desktop SSE event carrying the user's reply to a permission request.

- `reply`: one of `"once"`, `"always"`, or `"reject"`
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:TurnEvent fingerprint=2e8cf5aae122f346a7d8e69a41639725277b2e3365a9866a565969760944596d body_fp=83a9ecd97b08073b78d21358e37257d45c3ac19656bd11e47e9f2c7960d4230a source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents a single tool-call or tool-result event in a session's turn history.

- `type`: discriminates between the invocation and its response
- `durationMs`: round-trip duration; absent until the result is received
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:AttentionEventType fingerprint=387d9c55147b4b6a506d1472bf893a9ec902e75a9f984a3116be2505656f78e5 body_fp=b645e7eca86d9bcbb0c76c818cb5541ea305b5c212df1e38736b25af91b2272c source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Union type enumerating the four agent attention event kinds used by the AGM layer.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:EVENT_WEIGHTS fingerprint=b08ec8bd8dc21ec853c7a8bff3024115c20a33ece1bbe60a9ebce0b81fbb8a1d body_fp=8f57498673fa67645304dd861a9e4693e826ad8b29afdbcf2c3104fadaf27154 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=config -->
Maps each `AttentionEventType` to its raw live-mass weight applied when that event is recorded.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:LIVE_HALFLIFE_SECONDS fingerprint=ecbe2c45858381c3d820a56893da43a40e0b1063995af0211636569d69c1c99f body_fp=1ad1ef57e939d4f9fdb08462e547e30731c68619729376f0fc1438428f672043 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=config -->
Per-event-type live attention half-lives in seconds, keyed by `AttentionEventType`.

- `grep`: 30 s — shortest decay, ephemeral signal
- `read`: 180 s — medium decay
- `trace` / `write`: 600 s — slowest decay, strongest cognitive signal
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:HISTORICAL_HALFLIFE_SECONDS fingerprint=65bcfaa700d5cccebe5515cac0e063ef77d6048f58caa7a6e5256b395fdcada1 body_fp=56f30d36e50c54b8a05890fdc40891fca291367c0b7b657d1a2b05400f4a6502 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=config -->
Half-life duration for historical attention mass decay, fixed at 21 days in seconds.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:liveLambda fingerprint=be5b4a545c59be08f5d6ea5187b9e146620fc4497bb3dfdf516a9a6fe26b266a body_fp=95389dafe6c6dfb6d38f6d62273e59e4a645aeab9c5d2baa29334268d6af7694 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=util -->
Compute the exponential-decay lambda for a live attention event type using its half-life.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:HISTORICAL_LAMBDA fingerprint=3de05bae94a3824c630eca75be0ae37c8faabee8a1413d1b53a5e4ae90c4a812 body_fp=cb278857ce3ae3350e2f060e74a5233ab0250f93aedb2b875006b9f5d1924324 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Decay rate constant for historical mass, computed as `ln(2) / HISTORICAL_HALFLIFE_SECONDS` (21-day half-life).
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:displayMass fingerprint=52d25097200b2c6a7fdc9839e95ea3a6a98f130809e4614ce44c3a02b539925d body_fp=f6de396b92e43bfea51bdc1b1635fa5ce645a7012f66083717aecd3ae1d5a453 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=util -->
Apply logarithmic compression to a raw attention mass value for rendering purposes.

- `rawMass` — unbounded raw mass; negative values are clamped to 0 before compression.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:RepoEdgeKind fingerprint=bb06a4dcb3127caa4693738d4acc72b595e5754bf74a32fe2c2c86abe2c281e4 body_fp=c7357d3d20dc02e7a93324a1dd361162adb9c0c41a991ae3549aee46c9048eea source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Union type enumerating the six structural edge kinds in the repository call-graph.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:ATTENTION_EDGE_KIND fingerprint=d6ee6ad292e8b8a45dbc80f792af89146b4f9109fe7e1ff81017dc679f0587e7 body_fp=e83b01f74c125e6fde48d099dd74386febb34822e5372372a4e7145083f24a97 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Edge-kind constant identifying attention-propagation edges in the repository graph; always `"trace"`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:DEFAULT_EDGE_KIND fingerprint=2202b5ce40eaac5bf163e3ec2ab0226b031e7c9d205590ed5884ab50a4c77538 body_fp=77803dcd88e046bf1f7c31f59287974c9c5191828279041e8288af24c49153c0 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Default `RepoEdgeKind` used when no specific edge kind is provided; set to `"calls"`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:EDGE_WEIGHTS fingerprint=f3c846fd7fd2d297b212246ac68844c391de137ea568cb8230eec56dc1838671 body_fp=0e695723c6192fb9015d324bb6ed8c576e4832a57e09e4a2468908322cc9c9e1 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Map of propagation weights per repository-graph edge kind used by the AGM engine.

- `trace`/`calls`: full weight 1.0; `contains`: weakest at 0.2
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:PROPAGATION_FACTOR fingerprint=c078a9e53c7cf639f7235c9d6fb592a9224536fad711f92c8559481c3d4e5dac body_fp=0d0b2ace4ca6b8bbcc0fcfc0766b33cb92bcda9f376ad76370d2fe32d8e831de source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Scalar multiplier (0.15) applied to neighbour mass during single-hop AGM edge propagation.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:PROPAGATION_HOPS fingerprint=339374dcd667de88e6c07d4ceb35592e02f6d079cce4530a3d93bcf46b7f8186 body_fp=e45702e77d52593865dc106f29a9d474afd94a3d453c85ee01b679aaaa947816 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=config -->
Caps neighbour-hop propagation depth in the AGM edge-weight spread at one hop.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:edgeWeight fingerprint=55cea5f8b744cb8295706c18e0d6b647136ee5a17e0492ce7bd2531398a428c6 body_fp=e498b44627aef164c9ff19bdcd922562f1f5ab8e99bed13d14a6a92bf0cbabb5 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=util -->
Look up a propagation weight from `EDGE_WEIGHTS` by edge kind, falling back to the `calls` weight for unknown kinds.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:SyntheticNode fingerprint=0232df2106fc976319d4ea0401e9f9777d336ed730287a66acba0e9e119d8111 body_fp=1f60a5f2d1e3a85d28e8ef539289f9003be044e5e4ff04650b93d163d46b87c2 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Union type enumerating the five non-code cognition surfaces tracked in the AGM layer.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:SYNTHETIC_NODES fingerprint=c7a3856a0965ef49e8584b905332f417021d58840f82483c7c86435fede08f9f body_fp=1c27f983378a61bfc4428ac719d340d46bcdef642a9ac7d310861dd29cb5ef46 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Read-only tuple of all valid `SyntheticNode` values used for AGM synthetic non-code cognition surfaces.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:SYNTHETIC_QNAME_PREFIX fingerprint=ac9b93917d821af9888b0f4c810e7d287461afa0e77e7e779c7dcda9b02eca32 body_fp=bddec5bf50280db90c933ff9c99af357f02dcb0ecc9b55c0cb2021a13e9faff8 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
URI prefix string used to namespace all synthetic AGM node qnames.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:syntheticQname fingerprint=4a26d6ca53f0e66c99618771f80d2615953bb64317f63750706e552ff063a8c8 body_fp=f7b2035bccb3c1374c210aa8174c0cbea1c498c036ad4ee6d7b7e83d35c7aa75 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=util -->
Build the canonical AGM qname for a `SyntheticNode` by prepending `SYNTHETIC_QNAME_PREFIX`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:isSyntheticQname fingerprint=4d5a07d6153b2ba330ee6d82fe8bd5b30d25df25cb2e2b86f49a1eae8b765412 body_fp=828b20dcf5b3b13cb003205eaf8c7f31991d43ab386c797e8dd23b6cb8c31e99 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=util -->
Returns `true` if `qname` begins with `SYNTHETIC_QNAME_PREFIX`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:SYNTHETIC_FILE_PREFIX fingerprint=07f1ba6e7c98b98c971b7ef4b67ea78450a47717d81ccc0260917c849831156d body_fp=baa9ebe121871cd33944c647e17846f08cfee6941610c2a4aaf84b7545f5eac7 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Prefix string for per-file synthetic AGM qnames, formed by appending `file/` to `SYNTHETIC_QNAME_PREFIX`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:syntheticFileQname fingerprint=c4fb26721e40b72d1c57f9ee5a7424d37e126021eec9f39e3d6ea3e3507bc013 body_fp=a5b4d90711e6afe941287d15057994bc024b08b34acc977bd7bba5eca481b1ca source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=util -->
Build the AGM synthetic qname for a per-file node by prepending `SYNTHETIC_FILE_PREFIX` to `path`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:isSyntheticFileQname fingerprint=dfdef1e1418fdc050cd629b15da0c284f39a13a5ba1e4a9082b3f9ac51fb2253 body_fp=ede8f948a277e3d2d3c4534dc0c76fc384be11b596e04287c4ff00c9e2f7ec32 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=util -->
Return `true` if `qname` begins with `SYNTHETIC_FILE_PREFIX`, identifying it as a per-file synthetic node.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:syntheticFilePath fingerprint=fd4f4d1652f34660e1eaa4e44990fee42c706a24dd610bed6d6e9ca8923df300 body_fp=bfe796ac3e28b057a1fe5e5d76212db6637aa94bd1dc6a07f5292ae1eb1cf1ae source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=util -->
Extract the file path from a per-file synthetic qname, returning `null` if `qname` is not a synthetic file qname.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:looksLikeFilePath fingerprint=e5746802aef072f86bc094590d349e37dc82804f49e4dddc7274f36b664c0e58 body_fp=6450e0a670bc607c0bedd8dfd396002c635b86e7652ccfd4086200063b824c83 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=util -->
Return `true` if `target` looks like a file path rather than a symbol qname or free text.

- Returns `false` for empty strings or any string containing `:` (symbol qnames).
- Returns `true` for strings containing `/` or matching a dotted extension (1–8 chars).
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:AttentionEvent fingerprint=eb0cc0f36d154c3b511c7a727a6fc10ad002535f627f243651cc3dad8a353571 body_fp=770a8f7b58616ea70e902268d3b1bf71dc79200dbb5bffc3563ac30e5f1f248f source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents one unit of agent attention on a symbol qname or synthetic qname, carrying timing and weight for AGM mass calculations.

- `ts`: Unix timestamp of the event in milliseconds.
- `target`: symbol qname or synthetic qname receiving attention.
- `weight`: pre-computed mass contribution for this event.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:TypedEdge fingerprint=26b11b3e391822e2e7e12785b627ca2e11bc5019ec9f4c25557e1afabef0e3e3 body_fp=9812d5ee9b1c5ac0411c575c4eb5c41a004bb949a81a7dab961b5f670e34b3ac source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents a typed call-graph edge with source, destination, and relationship kind.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:InvestigationStatus fingerprint=6eb2fd0ef474ea1878c56855edd83b776a42ff9e7a136121621b99531d2c14ac body_fp=87fc32065ca0ba22e8be74ebb7c0024bd1add6087e76c2bc7ed52a1503ee8382 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Union type representing the lifecycle state of an `Investigation`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:Investigation fingerprint=2a1ac136fe5c7dc8a2db3a9074ad54c68ac21e000f592fea9933575d48e4f663 body_fp=03f597eff556ad4c7301febc515f7d4b31daf44ad2a3ff1dfef5d3eb5a87e832 source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Represents a first-class span of agent cognition tracking a named investigation over time.

- `confidence`: concentration of attention, derived live in-app; range 0..1
- `scope`: symbol qnames currently in focus for this investigation
- `negativeEvidence`: qnames ruled out during this investigation
<!-- trie:end -->
<!-- trie:section symbol=app/src/api/types:AttentionState fingerprint=e1929c7f37300891629dca6d0f6120a411196d71e9211ae806ad6eedf49cec1e body_fp=0d62a9ca1b6ce5a7778efba4f3f861ad313434cdfa0f540ac9759c3fc32fdd4c source_ref=4c78fd61fabf82d1da14be785030bd93bb5ec609 role=model -->
Per-node live attention state held in-memory by the AGM engine.

- `liveMass`: decaying in-session signal; never persisted
- `historicalMass`: long-term cognitive-importance signal stamped into the triefact; 21-day half-life
<!-- trie:end -->