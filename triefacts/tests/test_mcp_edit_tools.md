---
trie_version: 0.1.5
source: tests/test_mcp_edit_tools.py
file_fingerprint: 9edd924a31a2a7bf05903aa4b7ed50d898d6fb31fd5488703f3767383ee2078a
last_synced_at: '2026-06-10T13:16:52Z'
description: 'Tests for the MCP edit tool surface: patch/create/delete/rename/preview/list.'
defines:
- kind: module
  qualified_name: tests/test_mcp_edit_tools:__module__
  lines: 1-167
- kind: constant
  qualified_name: tests/test_mcp_edit_tools:PROJECT_TOML
  lines: 20-27
- kind: function
  qualified_name: tests/test_mcp_edit_tools:project
  lines: 31-54
- kind: function
  qualified_name: tests/test_mcp_edit_tools:tools
  lines: 58-61
- kind: class
  qualified_name: tests/test_mcp_edit_tools:TestPatchTool
  lines: 64-86
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestPatchTool.test_patch_with_note_returns_blast_radius
  lines: 65-71
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestPatchTool.test_patch_with_source_mode
  lines: 73-75
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestPatchTool.test_patch_requires_exactly_one_of_note_source
  lines: 77-81
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestPatchTool.test_patch_unknown_qname_has_fix
  lines: 83-86
- kind: class
  qualified_name: tests/test_mcp_edit_tools:TestCreateTool
  lines: 89-100
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestCreateTool.test_create_stages_create_patch
  lines: 90-95
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestCreateTool.test_create_existing_symbol_errors_with_fix
  lines: 97-100
- kind: class
  qualified_name: tests/test_mcp_edit_tools:TestDeleteTool
  lines: 103-111
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestDeleteTool.test_delete_lists_dependents
  lines: 104-107
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestDeleteTool.test_delete_unknown_errors
  lines: 109-111
- kind: class
  qualified_name: tests/test_mcp_edit_tools:TestRenameTool
  lines: 114-122
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestRenameTool.test_rename_returns_references
  lines: 115-118
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestRenameTool.test_rename_invalid_identifier
  lines: 120-122
- kind: class
  qualified_name: tests/test_mcp_edit_tools:TestPreviewAndList
  lines: 125-142
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestPreviewAndList.test_preview_reports_pending_and_cascade
  lines: 126-130
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestPreviewAndList.test_preview_flags_multi_symbol_note_need
  lines: 132-136
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestPreviewAndList.test_patch_list_includes_kind
  lines: 138-142
- kind: class
  qualified_name: tests/test_mcp_edit_tools:TestActivityAndSummary
  lines: 145-156
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestActivityAndSummary.test_activity_includes_patches_block
  lines: 146-151
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestActivityAndSummary.test_patch_summary_counts_creates
  lines: 153-156
- kind: class
  qualified_name: tests/test_mcp_edit_tools:TestSessionIdInjection
  lines: 159-166
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestSessionIdInjection.test_env_session_id_used
  lines: 160-166
incoming_refs: 0
outgoing_refs: 8
---
<!-- trie:section symbol=tests/test_mcp_edit_tools:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=2fb06c53c5335479bd3ae505c315da921dbf2ddfe3cde3b36cf55c056be20a59 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
Tests for the MCP edit tool surface: patch, create, delete, rename, preview, and list operations.

- **Scope**: Tests TrieTools directly via the same path FastMCP invokes
- **Fixtures**: Creates temporary project with trie.toml, lib.py, app.py and synced triefacts
- **Coverage**: Tool validation, staging, blast radius analysis, error handling with fixes
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:PROJECT_TOML fingerprint=e9c7735b60c9b4e2a539d27c21376b8f0df51a16c1349855a9eec287b1183875 body_fp=a6f814247c192e6924f8bfbd449eda43859212edcb731a468c687f4e7f56c538 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
String constant containing a complete trie.toml configuration file used in test fixtures.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:project fingerprint=d0dbfbe9ea278eea3e8551d42628ba526aec273db700a76ea914893bf2827538 body_fp=6bd2776a3b574edb5f826647b2a57d85fa94bc8d743603b8b6b2a05063ab1af1 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
Creates a test project with trie.toml config, lib.py with slugify function, and app.py with make_url function that imports slugify, then scans and syncs both files into a graph database.

- Returns the temporary project directory path
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:tools fingerprint=42243bcbe1160f1829c0d29be47560ccd781efb88ffe453c84792a3e6c15d8eb body_fp=630058fb0e304c884c1651d916a56c2c86e7667e8720141ddc4c6e6873f59ef7 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
Creates and yields a TrieTools instance for the test project, ensuring cleanup after use.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestPatchTool fingerprint=2db97d785a0030cac2712191b24cc9965fc95bc4f492d01a1183a600df5f710f body_fp=d2001fe5bf26aa7f3d2ac98dcf9f5ecad9cafb768209d2f4952a675c930f013a source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
Tests the TrieTools patch method behavior across different input modes and error cases.

- `test_patch_with_note_returns_blast_radius`: verifies note-mode patches include cascade impact
- `test_patch_with_source_mode`: confirms source-mode patches work with direct code input
- `test_patch_requires_exactly_one_of_note_source`: validates mutual exclusion of patch parameters
- `test_patch_unknown_qname_has_fix`: checks error handling for nonexistent symbols
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestPatchTool.test_patch_with_note_returns_blast_radius fingerprint=96ce30287c72c46279b29e85c33800c5c709ad34776c89501ae2f34e8949862b body_fp=406f87461e06fd39018629dc37467db39884fe15288828e9b367e7dccf129137 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
Verifies TestPatchTool.test_patch_with_note_returns_blast_radius patches with note mode and returns blast radius including cascade dependencies.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestPatchTool.test_patch_with_source_mode fingerprint=cd3964956fc448988b0f2b6f76301a492b3d52b23a767b66583047d26c7405e8 body_fp=ef34e933c4c4f04c4b1e27b1a7c1a7a73d23c2cb0c42914696ad870af4ea0846 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
Verifies TestPatchTool patch method accepts source code and returns mode="source" in response.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestPatchTool.test_patch_requires_exactly_one_of_note_source fingerprint=f687ffcd47a170c8d40e127b86d5c9cb8f409406728b863ca9c89bbd05358218 body_fp=2f115160057f57beb8232c14dbcb5a4b1339a849f3a6c24b357adb016da3e00f source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
TestPatchTool.test_patch_requires_exactly_one_of_note_source verifies patch tool rejects both note+source parameters or neither parameter with invalid_argument error.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestPatchTool.test_patch_unknown_qname_has_fix fingerprint=ad36762a25e89b6d8dc5fc8e79f03d3df33b954d5ffe13cdb02e788686df0ddc body_fp=ecd510a557ea6f38e6f51c768567e44ade77513fdf582415b15b2b1ba9252908 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
Verifies TestPatchTool patches for unknown symbols return not_found errors with patch tool fix suggestions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestCreateTool fingerprint=0fdcb6b8d972aab1447fd26e9431e6df8e70a82e788f059931e92d6272b4f0cc body_fp=04fc9bc2426f353f0e3587795cee97025b7913858f7374a00d8282a66ad40412 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
Tests the TrieTools.create_symbol method functionality for creating new symbols via MCP interface.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestCreateTool.test_create_stages_create_patch fingerprint=95c6806d36629622794e11a08292a5748a6a2fd23ef89c02ef7727ac3bbfb81d body_fp=ee053053c0d6522fd16b6cba6d43988d590646299b886d5e272b541fbf359c98 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
Tests that TestCreateTool.create_symbol returns a create patch ID and adds the symbol to the patch list.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestCreateTool.test_create_existing_symbol_errors_with_fix fingerprint=0457e02c40828ed0b1f327de30343b02ae85566681a0bb0ce1f48d2939733a82 body_fp=b9564683efe75267ad4efb1e82f224bdec994dcd57c2b6ed8ed6099a5269b19c source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
Tests that TestCreateTool.test_create_existing_symbol_errors_with_fix returns an error with patch tool suggestion when attempting to create an existing symbol.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestDeleteTool fingerprint=8d50af07cbfd5a47a9c79c2e8599971346ff5982e6de53bba663870d99aa6389 body_fp=c5fb35bc23b52a8e3e4c8adef90b7516795ec8d0add47f173584b714d63896b4 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
Tests the TrieTools delete_symbol operation.

- `test_delete_lists_dependents`: Verifies that deleting an existing symbol returns its dependents
- `test_delete_unknown_errors`: Confirms proper error handling when deleting non-existent symbols
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestDeleteTool.test_delete_lists_dependents fingerprint=2f3942b95c8ffd10db96337da84b03635f682a5a437128ddedc86c91bc2b6722 body_fp=9811963714ffa463aa79f8f0977ed2ffb6eb4d769ab9a7779d3e7df4cfe9b4aa source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
TestDeleteTool method that tests delete_symbol returns dependents list including symbols that reference the target.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestDeleteTool.test_delete_unknown_errors fingerprint=de18ecbe65a6c8a89aa73e7049e7eca78fb6392dc1d727fc47bf26222ce0995e body_fp=f27bc3900761c19d216b2edef079b9a710a0d6993616cf90f8c1c2a850bf18f8 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
Tests that TestDeleteTool.delete_symbol returns a "not_found" error for unknown symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestRenameTool fingerprint=9522d69f4c09870435be93311c41240d9b48bfc91713096488648617d481c8e0 body_fp=88a7671699a6ca5607ea904d7c199e0f76b78fe8fc898d0803e5f32d04151251 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
Tests the TrieTools rename_symbol method behavior and validation.

- `test_rename_returns_references`: verifies renamed symbol metadata includes new name and reference locations
- `test_rename_invalid_identifier`: confirms invalid Python identifiers trigger argument validation errors
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestRenameTool.test_rename_returns_references fingerprint=e51b3031d419d0421c6c2bf0655d2cb3205923f06f6738c1538de86b6555f743 body_fp=a125c892beef64717f43dafb562a65a2e3b4d610a7a5208f6fcbcea457c1478f source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
TestRenameTool.test_rename_returns_references verifies that rename_symbol returns the new name and lists dependent symbols in references.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestRenameTool.test_rename_invalid_identifier fingerprint=e85386992710e377f990eb6928fd51bd21ab7e6dd04a0fe11c58fd048054409a body_fp=d0758322c71034bc4ac1a5edc98b6fa5e8ef2b203065bceea055072a8b1df006 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
Tests that TestRenameTool.rename_symbol rejects invalid Python identifiers with "invalid_argument" error code.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestPreviewAndList fingerprint=3a67825ab606a45e1d3b01d2b3d48f1450339fe3e7e42a7b3e0526a4e7ea09da body_fp=f4fa25bb04bb068d4181bd5abfe4e9705151dd217b7b747ebc77a9798f66296f source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
Tests TrieTools preview and patch listing functionality through staged operations.

- `test_preview_reports_pending_and_cascade`: verifies preview shows pending changes and commit-ready status
- `test_preview_flags_multi_symbol_note_need`: checks multi-symbol patches trigger session note requirement
- `test_patch_list_includes_kind`: confirms patch list contains operation type metadata
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestPreviewAndList.test_preview_reports_pending_and_cascade fingerprint=c1193b5246f1c5823ff5739f1a9b60638e60c84177b4c20f24bbee76f75a5db5 body_fp=4d614264e6100d70543abf72e95a4c20f1dd231a78aabe927691392d6935f28e source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
TestPreviewAndList.test_preview_reports_pending_and_cascade verifies that preview() includes staged patches in pending and sets ready_to_commit flag.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestPreviewAndList.test_preview_flags_multi_symbol_note_need fingerprint=ff52bc65d34a8a31bcea0a5f7d2ca7cce6afddc11bc507fd261e23b5e7c00ed9 body_fp=217e6a84c4a657faa0733fb67355cf86648840dfd0f34ee0bf7172a3cf7d63ad source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
Tests that TestPreviewAndList.preview flags needs_session_note when multiple symbols have patches staged.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestPreviewAndList.test_patch_list_includes_kind fingerprint=f27baf15c2c895ee25fa5003baa05462b5234115b5ec52188cfa7a81623599e4 body_fp=80f704b0c657c815d5cdc38a81af3c39e8bc2adbf0909f97bb0022ae2b981c1d source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
Verifies TestPreviewAndList.test_patch_list_includes_kind method confirms patch_list() includes kind field for rename operations.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestActivityAndSummary fingerprint=4f34e182635322e108a38e30bc58afe93d2dea6ec7867cf191b5e0597872500e body_fp=300ae981c2a7f64f0ecf72ed1c47367141fc6a16a4ac9f146f4b42246385731e source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
Tests activity reporting and patch summary statistics in TrieTools.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestActivityAndSummary.test_activity_includes_patches_block fingerprint=19ce21c0c1b724258f27508681d3f07666b1603d45b10c9a8759cfa026ef6873 body_fp=3fe5ed4a7b3cdf721df9acd25f78ba8f91ca14f58ed1119b98238f63aa021da6 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
Verifies that TestActivityAndSummary activity method returns patches block with counts and null apply field.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestActivityAndSummary.test_patch_summary_counts_creates fingerprint=4f11e448170cab69475b333638f0933f5640c9b7a19d50bacc3c04a5d231deb1 body_fp=69c8343de4f5ea067e204da183a1b6eac74d93725cf1965be6499b519672b380 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
TestActivityAndSummary.test_patch_summary_counts_creates verifies that patch_summary includes create operations in its count.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestSessionIdInjection fingerprint=32be77b3725604e6c470312fe57b9b22aa96054fb6643ce293a6dd9ebcbc2bf2 body_fp=c0f702509e00bb661e63392a5309a86be4a9f883c27295fd52aeeaea31aac005 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
Tests that TrieTools reads session ID from TRIE_SESSION_ID environment variable.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestSessionIdInjection.test_env_session_id_used fingerprint=75dd4f547709e5ab8a430412cac2cfff9fe0af273d58ea4b4637f9dbf46ce237 body_fp=f628ba6ddb2ffdffe87bfc669bfc29379672208e01f6b49cce14d8cf43d45009 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
Verifies TestSessionIdInjection uses environment variable TRIE_SESSION_ID to set TrieTools session ID.
<!-- trie:end -->