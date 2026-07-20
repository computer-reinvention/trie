---
trie_version: 0.1.9
source: trie/edits/report.py
file_fingerprint: f38371014a9c65d110640805d01d83957cbcf256f8e720b73643c30c94d7ab51
last_synced_at: '2026-07-20T09:54:09Z'
description: 'The hand-off contract: the staged change-set and the ApplyReport.'
defines:
- kind: module
  qualified_name: trie/edits/report:__module__
  lines: 1-212
- kind: constant
  qualified_name: trie/edits/report:_SESSION_NOTE_STOPLIST
  lines: 14-14
- kind: constant
  qualified_name: trie/edits/report:_SESSION_NOTE_MIN_CHARS
  lines: 15-15
- kind: function
  qualified_name: trie/edits/report:session_note_ok
  lines: 18-27
- kind: constant
  qualified_name: trie/edits/report:STAGE_GENERATE
  lines: 31-31
- kind: constant
  qualified_name: trie/edits/report:STAGE_COMPILE
  lines: 32-32
- kind: constant
  qualified_name: trie/edits/report:STAGE_FIXUP
  lines: 33-33
- kind: constant
  qualified_name: trie/edits/report:STAGE_REFRESH
  lines: 34-34
- kind: constant
  qualified_name: trie/edits/report:STAGE_CASCADE
  lines: 35-35
- kind: constant
  qualified_name: trie/edits/report:CODE_BACKEND_FAILED
  lines: 38-38
- kind: constant
  qualified_name: trie/edits/report:CODE_SYNTAX_AFTER_CAP
  lines: 39-39
- kind: constant
  qualified_name: trie/edits/report:CODE_LSP_UNCLEAN
  lines: 40-40
- kind: constant
  qualified_name: trie/edits/report:CODE_SECOND_ORDER
  lines: 41-41
- kind: constant
  qualified_name: trie/edits/report:CODE_ORPHAN_CREATE
  lines: 42-42
- kind: constant
  qualified_name: trie/edits/report:CODE_FILE_NOT_FOUND
  lines: 43-43
- kind: class
  qualified_name: trie/edits/report:StagedChange
  lines: 47-64
- kind: class
  qualified_name: trie/edits/report:UnresolvedItem
  lines: 68-94
- kind: method
  qualified_name: trie/edits/report:UnresolvedItem.to_dict
  lines: 85-94
- kind: class
  qualified_name: trie/edits/report:AppliedItem
  lines: 98-112
- kind: method
  qualified_name: trie/edits/report:AppliedItem.to_dict
  lines: 105-112
- kind: class
  qualified_name: trie/edits/report:CascadeAppliedItem
  lines: 116-122
- kind: method
  qualified_name: trie/edits/report:CascadeAppliedItem.to_dict
  lines: 121-122
- kind: class
  qualified_name: trie/edits/report:ModuleRemark
  lines: 126-140
- kind: method
  qualified_name: trie/edits/report:ModuleRemark.to_dict
  lines: 139-140
- kind: class
  qualified_name: trie/edits/report:ApplyReport
  lines: 144-211
- kind: method
  qualified_name: trie/edits/report:ApplyReport.blocking_unresolved
  lines: 159-160
- kind: method
  qualified_name: trie/edits/report:ApplyReport.to_dict
  lines: 162-182
- kind: method
  qualified_name: trie/edits/report:ApplyReport._post_apply_actions
  lines: 184-211
incoming_refs: 26
outgoing_refs: 0
---
<!-- trie:section symbol=trie/edits/report:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=a12e01a96f2e880035a99ec411fe16f34189cac4ff4722cbda7a62f64e3037a0 source_ref=72eb7aebeb3590c206ef0fb47bb2a32f97412c09 role=model -->
Defines data structures for the staged change-set and apply report that form the contract between staging and committing edits.

- `StagedChangeSet`: ephemeral in-memory object produced by stage and consumed by commit
- `ApplyReport`: feedback artifact returned to agent with ready-to-send repatch calls for unresolved items
- `session_note_ok()`: validates multi-symbol apply notes reject boilerplate like "fix" or "."
- Stage constants: `STAGE_GENERATE`, `STAGE_COMPILE`, `STAGE_FIXUP`, `STAGE_REFRESH`, `STAGE_CASCADE`
- Error codes: `CODE_BACKEND_FAILED`, `CODE_SYNTAX_AFTER_CAP`, `CODE_LSP_UNCLEAN`, etc.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/report:_SESSION_NOTE_STOPLIST fingerprint=a09ea23a28cadabdce59b05e05933086e628e24bb9089e97fc41fae857e49340 body_fp=1bf7b9a01e620ea0445ee5d24e206d010fe60aa788898233ab21de70465346ba source_ref=72eb7aebeb3590c206ef0fb47bb2a32f97412c09 role=config -->
Set of generic words rejected as session notes to prevent agents using boilerplate like "fix" or ".".
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/report:_SESSION_NOTE_MIN_CHARS fingerprint=603c02b63000bf140fdc373da663206d6d7b0d889a94f1236c02e5ea5b661d6d body_fp=76cbc9cc270ca8d77f7fdb995fc86ff9cca13e4583b1feafab900dbfcefbf783 source_ref=72eb7aebeb3590c206ef0fb47bb2a32f97412c09 role=config -->
Minimum character count for session notes to pass validation.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/report:session_note_ok fingerprint=68e656fbf86214242fc342426bb248a1b47763b6369b424e06e8c5a4ac004723 body_fp=e74667b2b904b86043cd96b7c8c52f1cf51908c7c3070449655fa559e4c35a43 source_ref=72eb7aebeb3590c206ef0fb47bb2a32f97412c09 role=util -->
Validates that a session note meets minimum quality requirements for multi-symbol applies.

- Returns `False` for notes shorter than 12 characters or containing only stoplist words like "fix", "wip", "."
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/report:STAGE_GENERATE fingerprint=517a418bb088685568e992595fcefcd5c57fc96ed7b0092de90de1ddf3d97f4f body_fp=bdb96024efd85601c66e53732fed2d5c15c568343ef14d01301f90d3e1ceeaba source_ref=72eb7aebeb3590c206ef0fb47bb2a32f97412c09 role=model -->
Constant indicating a symbol failed during the generation stage of the edit pipeline.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/report:STAGE_COMPILE fingerprint=52a35079e3aca7bb768e1114a13fbf250a2c71086cf3d5e7450f6c83f6882d7d body_fp=ae131b5b534729f7f709836772e5eaf35635b4a39093ae4ba2ebbae8cd6fbb8e source_ref=72eb7aebeb3590c206ef0fb47bb2a32f97412c09 role=model -->
Stage constant indicating a symbol failed during compilation phase of the edit pipeline.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/report:STAGE_FIXUP fingerprint=4a619fd44f1f3c70c22aeb71bcdc9d9c196113211579281e54371e66ab316c57 body_fp=f13228413f716b55c87bc2a20d49f00d85569e5845a0cce3acb91a522256473c source_ref=72eb7aebeb3590c206ef0fb47bb2a32f97412c09 role=model -->
String constant identifying the fixup stage where a symbol can fail during the edit pipeline.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/report:STAGE_REFRESH fingerprint=1ac2e8c510ac7ac63b80120240e8dad413f5aebeb3fdd6df9404ed559484bac3 body_fp=bf52363a1e8c3db40270eb67d9bb960c137ee1056167be26449fd11f36569cc6 source_ref=72eb7aebeb3590c206ef0fb47bb2a32f97412c09 role=model -->
String constant representing the "refresh" stage where a symbol can fail during edit processing.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/report:STAGE_CASCADE fingerprint=18d6f3dd246c3a7d57299b32d714ae9b3ddb91ae127dc61da99c431863d2b85d body_fp=e7234adef69da818b60cc822417eef5b2e529110abce6fb56af5286a1df43ca5 source_ref=72eb7aebeb3590c206ef0fb47bb2a32f97412c09 role=model -->
Constant identifying the cascade stage where dependent symbols are automatically updated after primary edits.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/report:CODE_BACKEND_FAILED fingerprint=d345b9d262fa3156a2516318ba0707a17ba51f3369c560cf3b09c29819ce9287 body_fp=fac1dc1a91620d64ba09bac126a5cb4b6adfb63aa100047e53181a89acc0e51a source_ref=72eb7aebeb3590c206ef0fb47bb2a32f97412c09 role=model -->
Error code indicating the backend service failed to process a symbol edit request.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/report:CODE_SYNTAX_AFTER_CAP fingerprint=152a1398c439c5084bf3dd2b7951b7e373f9ae38fafabcf2af612ade148ade38 body_fp=ea99cb74827356b41130de084029ce5ac921a404ec7c9635d3b1be691dac18a4 source_ref=72eb7aebeb3590c206ef0fb47bb2a32f97412c09 role=model -->
Error code indicating a symbol failed compilation due to syntax errors after exhausting retry attempts.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/report:CODE_LSP_UNCLEAN fingerprint=0787be1d0fa4b595b94d454f1b523c440189984e9e1007a6f8fe4936de002389 body_fp=02e6cabf7725440c22fb0e527ea6d6558ebe838138709032b6ba24b01ce42a89 source_ref=72eb7aebeb3590c206ef0fb47bb2a32f97412c09 role=model -->
Error code indicating LSP validation failed after edit generation and compilation.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/report:CODE_SECOND_ORDER fingerprint=5f3258f640768ab84252a0e26006e4b79970ef3a532168f21126594bd33a5401 body_fp=01f3e4f3008fa1e2bcac3f87ed27c2fea44512668aec0fd93bbdfdd1eadbf730 source_ref=72eb7aebeb3590c206ef0fb47bb2a32f97412c09 role=model -->
Error code constant for UnresolvedItem indicating a symbol requires attention due to second-order cascade effects.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/report:CODE_ORPHAN_CREATE fingerprint=a980454f79e6df648d03ea4ec14fd05b10cd3054dac03ea6567a2a61c3146b5e body_fp=c00b151ac18b0deafee821a7cd9067a0df41eeb4639bebc64fbeec4ffdd38aac source_ref=72eb7aebeb3590c206ef0fb47bb2a32f97412c09 role=model -->
Error code indicating a symbol creation attempt failed because it lacks a valid parent context.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/report:CODE_FILE_NOT_FOUND fingerprint=bdb334af596cbda1a87c55e9cb37b5642e67a93d54f86f9872adbf0782a19e7c body_fp=1b78ee509179944ddf2fb071f313b4b362d979c352e1ee68329550004e58f31c source_ref=72eb7aebeb3590c206ef0fb47bb2a32f97412c09 role=model -->
String constant identifying UnresolvedItem failures where the target file could not be located.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/report:StagedChange fingerprint=ba2e99ecd549af7e85556f8bbab64d2eecc7e0b5051d2a16534c23da7180eb66 body_fp=34cdf057fd66d8082563d831d4bc782982697e1bd513c7aade6a25290ebb26b5 source_ref=16646a6ef544e59e30c25f799b737ff689e6450f role=model -->
Represents one symbol's proposed edit with complete before/after state for commit processing.

- `op`: Operation type - modify, create, delete, or rename
- `old_source`: Symbol's prior span content, empty string for create operations
- `new_source`: Symbol's new span content, empty string for delete operations
- `before_file_bytes`: Complete original file content for rollback capability
- `after_file_bytes`: Complete proposed file content after applying the edit
- `module_remarks`: New imports or module-level changes the body requires; empty string if none
- `new_dependencies`: External packages introduced by the edit; empty tuple if none
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/report:UnresolvedItem fingerprint=bd316205b7810635b9e0cb4019973afed3bf375e0ccc1c965930b1cd9ae0e0f0 body_fp=47738a4c3b80cedf94fedca796a6a66a20944a0a99a13985ec9cc5c101c93ef7 source_ref=72eb7aebeb3590c206ef0fb47bb2a32f97412c09 role=model -->
Represents a symbol that failed processing and requires agent intervention to resolve.

- `blocking`: when `True`, prevents commit and marks the run as failed; when `False`, advisory only
- `repatch`: contains tool invocation data for one-call recovery
- `stage`: which processing phase failed (generate, compile, fixup, refresh, cascade)
- `code`: specific failure reason code for programmatic handling
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/report:UnresolvedItem.to_dict fingerprint=9e4f0aad15e8d6783ef8acb4ba58c9624fe44ed758242df0d4c040af5a16587f body_fp=25b89d3e232cd24030f4c97477d6ede50925b1563d1898977564306a7ca53bf1 source_ref=72eb7aebeb3590c206ef0fb47bb2a32f97412c09 role=util -->
Converts UnresolvedItem instance to a dictionary with all field values.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/report:AppliedItem fingerprint=be704f3c1cb882bd14143516e0c6084903520c0c90bb8bd147f0f2c78ca9dd30 body_fp=7131b12fc279f923274e64f2fe645efa9fbea47929cdd965144e60fea566ec1c source_ref=72eb7aebeb3590c206ef0fb47bb2a32f97412c09 role=model -->
Records a successfully applied symbol edit with metadata about the operation performed.

- `prose_written`: whether documentation was generated for this symbol
- `lsp_iterations`: number of LSP-guided syntax fix rounds applied
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/report:AppliedItem.to_dict fingerprint=05e1cded306b5f00195fe0e9e2be8f0b92139cc26b3e459615f277a88d4807d2 body_fp=df4cb9fb1c8f1bc7aa8da5ac9ae1bb8004cccc5255d7c735590c61524eb553a9 source_ref=72eb7aebeb3590c206ef0fb47bb2a32f97412c09 role=model -->
Converts AppliedItem instance to a dictionary representation with all field values.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/report:CascadeAppliedItem fingerprint=1931a3db4a8dbd39eca0921e5c9d6408e683f759b8f8301ddf5797a486509c35 body_fp=e8e6475eba5bcff2cad00da224b88946269fc1e2ccef2967b348dd0d19e874e4 source_ref=72eb7aebeb3590c206ef0fb47bb2a32f97412c09 role=model -->
Records a symbol that was automatically updated during cascade application.

- `qname`: qualified name of the symbol that was updated
- `note`: description of what change was made
- `origin`: source of the cascade update (defaults to "cascade")
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/report:CascadeAppliedItem.to_dict fingerprint=25a5a2c0d19dcc47d1024b368b2a714f13c1e2fa37f424b34e3aa247acb81e5c body_fp=f4eb7e652d6a4fb3d775c7a72fbd762fc5d58c9bbd563fbb829313a462bb9e38 source_ref=72eb7aebeb3590c206ef0fb47bb2a32f97412c09 role=util -->
Converts CascadeAppliedItem to a dictionary with qname, note, and origin fields.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/report:ModuleRemark fingerprint=1d7df70284a8feac91295bb843572c29cfb20e74e034002bc25b0131fe2afbed body_fp=588b2d29e04013a7d5f87d8b991c01acca8f8a1bfd67320d9103f896637d159c source_ref=16646a6ef544e59e30c25f799b737ff689e6450f role=model -->
Immutable advisory record of a module-level change (e.g. a new import) the agent must apply after a symbol commits.

- `remarks`: human-readable description of the required module-level edit to apply via `force`
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/report:ModuleRemark.to_dict fingerprint=54693b8d8b8864a7ab503c8d479a387a6ec520b646cc17055d937087dc223d33 body_fp=285e052893e0ca63127cdd6fd854be8e34061c2cc7d8267f314e2a5ad62cb4a0 source_ref=16646a6ef544e59e30c25f799b737ff689e6450f role=model -->
Serialize a `ModuleRemark` instance to a plain dict with `qname`, `file_path`, and `remarks` keys.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/report:ApplyReport fingerprint=7add20cbd826dc8af1ac8d79822efc2a67a8369434560385c017f073fc19f65d body_fp=bbff876f5774c5fcf22e9a36aaeec81e06fb541f107c24fac731792f49e02f5b source_ref=16646a6ef544e59e30c25f799b737ff689e6450f role=model -->
Read-only feedback artifact returned by commit operations containing apply results and any unresolved items.

- `ok`: overall success status; false if any blocking unresolved items exist
- `committed`: whether changes were actually written to disk
- `applied`: successfully processed symbol changes
- `cascade_applied`: additional symbols modified due to cascading effects
- `unresolved`: symbols that failed processing, with repatch calls for recovery
- `module_remarks`: advisory module-level fixups the agent must apply manually
- `new_dependencies`: external packages introduced by the edit, for agent to install
- `blocking_unresolved`: property filtering unresolved items that prevent commits
- `requested`: total number of symbols originally requested for processing
- `to_dict`: output includes a `post_apply_actions` block consolidating formatter, dependency, and module-remark follow-ups for the agent
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/report:ApplyReport.blocking_unresolved fingerprint=64d443eec2ddb0daad218693cad07c9293e8637001ebf0bd3a5228df3c477f63 body_fp=e4a94c987144eac039043abb5ede394ddbe2db22a00017dc91a01c06b07003c2 source_ref=72eb7aebeb3590c206ef0fb47bb2a32f97412c09 role=util -->
Filters ApplyReport.unresolved to return only items with blocking=True.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/report:ApplyReport.to_dict fingerprint=60e1c50a73cb06077e571f72df98468729b843c5ac9a16ad3c83c5528f24ab82 body_fp=e54f286d652503a8a7ff70c01e479aa2474aef47c9aeea7356ee494408ffb652 source_ref=16646a6ef544e59e30c25f799b737ff689e6450f role=model -->
Serializes `ApplyReport` instance to a dictionary with aggregated file counts, nested item details, and a `post_apply_actions` block.
<!-- trie:end -->
<!-- trie:section symbol=trie/edits/report:ApplyReport._post_apply_actions fingerprint=b0acaf9e2950a73996b507e4bdd4d8415b989e1159b10d9249d63982dce95a4a body_fp=47ec17545a8a428f70ffd3a669ed5178c31b102b70dfb842844b55d985d7631b source_ref=16646a6ef544e59e30c25f799b737ff689e6450f role=domain -->
Build and return `ApplyReport`'s consolidated post-commit action dict covering files to format, new dependencies to install, and module remarks to apply manually.
<!-- trie:end -->