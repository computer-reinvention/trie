---
trie_version: 0.3.0
source: tests/test_mcp_edit_tools.py
file_fingerprint: 4ee5c539e04f38d8d6ee284e1d6f4438ab2465963ebd1a402f589a19f16c2a8e
last_synced_at: '2026-08-01T02:17:36Z'
description: 'Tests for the MCP edit tool surface: patch/create/delete/rename/preview/list.'
defines:
- kind: module
  qualified_name: tests/test_mcp_edit_tools:__module__
  lines: 1-173
- kind: constant
  qualified_name: tests/test_mcp_edit_tools:PROJECT_TOML
  lines: 20-27
- kind: function
  qualified_name: tests/test_mcp_edit_tools:project
  lines: 31-54
  signature: 'def project(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_mcp_edit_tools:tools
  lines: 58-61
  signature: 'def tools(project: Path)'
- kind: class
  qualified_name: tests/test_mcp_edit_tools:TestPatchTool
  lines: 64-86
  signature: class TestPatchTool
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestPatchTool.test_patch_with_note_returns_blast_radius
  lines: 65-71
  signature: def test_patch_with_note_returns_blast_radius(self, tools)
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestPatchTool.test_patch_with_source_mode
  lines: 73-75
  signature: def test_patch_with_source_mode(self, tools)
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestPatchTool.test_patch_requires_exactly_one_of_note_source
  lines: 77-81
  signature: def test_patch_requires_exactly_one_of_note_source(self, tools)
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestPatchTool.test_patch_unknown_qname_has_fix
  lines: 83-86
  signature: def test_patch_unknown_qname_has_fix(self, tools)
- kind: class
  qualified_name: tests/test_mcp_edit_tools:TestCreateTool
  lines: 89-106
  signature: class TestCreateTool
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestCreateTool.test_create_stages_create_patch
  lines: 90-95
  signature: def test_create_stages_create_patch(self, tools)
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestCreateTool.test_create_existing_symbol_falls_back_to_patch
  lines: 97-106
  signature: 'def test_create_existing_symbol_falls_back_to_patch(self, tools): # Creating a symbol that already exists is not an error: the note is # recorded as a patch and the result flags the graceful fallback.'
- kind: class
  qualified_name: tests/test_mcp_edit_tools:TestDeleteTool
  lines: 109-117
  signature: class TestDeleteTool
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestDeleteTool.test_delete_lists_dependents
  lines: 110-113
  signature: def test_delete_lists_dependents(self, tools)
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestDeleteTool.test_delete_unknown_errors
  lines: 115-117
  signature: def test_delete_unknown_errors(self, tools)
- kind: class
  qualified_name: tests/test_mcp_edit_tools:TestRenameTool
  lines: 120-128
  signature: class TestRenameTool
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestRenameTool.test_rename_returns_references
  lines: 121-124
  signature: def test_rename_returns_references(self, tools)
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestRenameTool.test_rename_invalid_identifier
  lines: 126-128
  signature: def test_rename_invalid_identifier(self, tools)
- kind: class
  qualified_name: tests/test_mcp_edit_tools:TestPreviewAndList
  lines: 131-148
  signature: class TestPreviewAndList
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestPreviewAndList.test_preview_reports_pending_and_cascade
  lines: 132-136
  signature: def test_preview_reports_pending_and_cascade(self, tools)
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestPreviewAndList.test_preview_flags_multi_symbol_note_need
  lines: 138-142
  signature: def test_preview_flags_multi_symbol_note_need(self, tools)
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestPreviewAndList.test_patch_list_includes_kind
  lines: 144-148
  signature: def test_patch_list_includes_kind(self, tools)
- kind: class
  qualified_name: tests/test_mcp_edit_tools:TestActivityAndSummary
  lines: 151-162
  signature: class TestActivityAndSummary
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestActivityAndSummary.test_activity_includes_patches_block
  lines: 152-157
  signature: def test_activity_includes_patches_block(self, tools)
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestActivityAndSummary.test_patch_summary_counts_creates
  lines: 159-162
  signature: def test_patch_summary_counts_creates(self, tools)
- kind: class
  qualified_name: tests/test_mcp_edit_tools:TestSessionIdInjection
  lines: 165-172
  signature: class TestSessionIdInjection
- kind: method
  qualified_name: tests/test_mcp_edit_tools:TestSessionIdInjection.test_env_session_id_used
  lines: 166-172
  signature: def test_env_session_id_used(self, project, monkeypatch)
incoming_refs: 0
outgoing_refs: 11
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
<!-- trie:section symbol=tests/test_mcp_edit_tools:project fingerprint=d0dbfbe9ea278eea3e8551d42628ba526aec273db700a76ea914893bf2827538 body_fp=2baa3d830834a3c4b9299167601d0ff2d7009771fecb26a5f3a12e7e4fbd98c0 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
## `def project(tmp_path: Path) -> Path`

Creates a test project with trie.toml config, lib.py with slugify function, and app.py with make_url function that imports slugify, then scans and syncs both files into a graph database.

- Returns the temporary project directory path
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:tools fingerprint=42243bcbe1160f1829c0d29be47560ccd781efb88ffe453c84792a3e6c15d8eb body_fp=24152495b5330b5622da54c5aeb7eb3a3eda4eec680c38054b86dc8c9bae263e source_ref=e9a78162908128eaac554c055f1ed9e887f1185d role=test -->
## `def tools(project: Path)`

Creates and yields a TrieTools instance for the test project, ensuring cleanup after use.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestPatchTool fingerprint=2db97d785a0030cac2712191b24cc9965fc95bc4f492d01a1183a600df5f710f body_fp=e2ccbaf623dbda734e6f88501edadacf057400d40196f16c21cf96262770db03 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
## `class TestPatchTool`

Tests the TrieTools patch method behavior across different input modes and error cases.

- `test_patch_with_note_returns_blast_radius`: verifies note-mode patches include cascade impact
- `test_patch_with_source_mode`: confirms source-mode patches work with direct code input
- `test_patch_requires_exactly_one_of_note_source`: validates mutual exclusion of patch parameters
- `test_patch_unknown_qname_has_fix`: checks error handling for nonexistent symbols
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestPatchTool.test_patch_with_note_returns_blast_radius fingerprint=96ce30287c72c46279b29e85c33800c5c709ad34776c89501ae2f34e8949862b body_fp=4d5c4d54119e3ca8a8f85c4364abe7262b2c66ccbb2af047afd8c655f3900202 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
## `def test_patch_with_note_returns_blast_radius(self, tools)`

Verifies TestPatchTool.test_patch_with_note_returns_blast_radius patches with note mode and returns blast radius including cascade dependencies.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestPatchTool.test_patch_with_source_mode fingerprint=cd3964956fc448988b0f2b6f76301a492b3d52b23a767b66583047d26c7405e8 body_fp=f92d87844faf8dfe9ca8169741e4a3132bfeedaada13c5c6f58d2320a3cfba7c source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
## `def test_patch_with_source_mode(self, tools)`

Verifies TestPatchTool patch method accepts source code and returns mode="source" in response.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestPatchTool.test_patch_requires_exactly_one_of_note_source fingerprint=f687ffcd47a170c8d40e127b86d5c9cb8f409406728b863ca9c89bbd05358218 body_fp=7b91b3ff778da36d580c90122f4a01896784d9efe1094cf9c7ae40430984e4d2 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
## `def test_patch_requires_exactly_one_of_note_source(self, tools)`

TestPatchTool.test_patch_requires_exactly_one_of_note_source verifies patch tool rejects both note+source parameters or neither parameter with invalid_argument error.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestPatchTool.test_patch_unknown_qname_has_fix fingerprint=ad36762a25e89b6d8dc5fc8e79f03d3df33b954d5ffe13cdb02e788686df0ddc body_fp=d3b3a17ad5438738bf9519de06d64185bb8c6b32c7f647f6e515a0cc34394e68 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
## `def test_patch_unknown_qname_has_fix(self, tools)`

Verifies TestPatchTool patches for unknown symbols return not_found errors with patch tool fix suggestions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestCreateTool fingerprint=37ec996acafec7e1ba0331f2af6c375a0c9b049dbf729ede3127e3c753820025 body_fp=7ad757703e511d97e8d36dc79acf3184c68d436bb41de7c420849cdf804cac9f source_ref=e9a78162908128eaac554c055f1ed9e887f1185d role=test -->
## `class TestCreateTool`

Tests `TrieTools.create_symbol`: staging new symbols and gracefully falling back to a patch when the symbol already exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestCreateTool.test_create_stages_create_patch fingerprint=95c6806d36629622794e11a08292a5748a6a2fd23ef89c02ef7727ac3bbfb81d body_fp=f1c00c34856feda949d0bb13cf23b2b33851588fa4054ed8251d72d9abaadbce source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
## `def test_create_stages_create_patch(self, tools)`

Tests that TestCreateTool.create_symbol returns a create patch ID and adds the symbol to the patch list.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestCreateTool.test_create_existing_symbol_falls_back_to_patch fingerprint=55f57bc88a5028a2859c677f3247a62d8fa6ba14ebd061b00cdf9d9bd0eeff8e body_fp=049f1412b7be213576cdb7e96b6192f983ebb5548f287792918755b254a9ba08 source_ref=e9a78162908128eaac554c055f1ed9e887f1185d role=test -->
## `def test_create_existing_symbol_falls_back_to_patch(self, tools): # Creating a symbol that already exists is not an error: the note is # recorded as a patch and the result flags the graceful fallback.`

Assert that `TestCreateTool.test_create_existing_symbol_falls_back_to_patch` verifies `create_symbol` silently converts to a patch when the target symbol already exists, returning `op="patch"` and `fell_back=True` with no error.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestDeleteTool fingerprint=8d50af07cbfd5a47a9c79c2e8599971346ff5982e6de53bba663870d99aa6389 body_fp=1b2e394e2d9689dfeb19bff419cc819c8efb7c3a843fa2e7237b4436e7aba3af source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
## `class TestDeleteTool`

Tests the TrieTools delete_symbol operation.

- `test_delete_lists_dependents`: Verifies that deleting an existing symbol returns its dependents
- `test_delete_unknown_errors`: Confirms proper error handling when deleting non-existent symbols
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestDeleteTool.test_delete_lists_dependents fingerprint=2f3942b95c8ffd10db96337da84b03635f682a5a437128ddedc86c91bc2b6722 body_fp=54b559e19a406d806ed746f0c007adc730541d71f5c492da9b6a3f2d01205eaa source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
## `def test_delete_lists_dependents(self, tools)`

TestDeleteTool method that tests delete_symbol returns dependents list including symbols that reference the target.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestDeleteTool.test_delete_unknown_errors fingerprint=de18ecbe65a6c8a89aa73e7049e7eca78fb6392dc1d727fc47bf26222ce0995e body_fp=661e8e76067f8ce7636f41266e9e9584a50dcb41b45dc93499da5c2212f61ea2 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
## `def test_delete_unknown_errors(self, tools)`

Tests that TestDeleteTool.delete_symbol returns a "not_found" error for unknown symbols.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestRenameTool fingerprint=9522d69f4c09870435be93311c41240d9b48bfc91713096488648617d481c8e0 body_fp=2a87e3e7e0f5cb35c28915ea499adb8f2e6598c9eb2bda5772c696b35797d815 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
## `class TestRenameTool`

Tests the TrieTools rename_symbol method behavior and validation.

- `test_rename_returns_references`: verifies renamed symbol metadata includes new name and reference locations
- `test_rename_invalid_identifier`: confirms invalid Python identifiers trigger argument validation errors
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestRenameTool.test_rename_returns_references fingerprint=e51b3031d419d0421c6c2bf0655d2cb3205923f06f6738c1538de86b6555f743 body_fp=37f86f89cd2268b660f3bb955d5d269eb1b8640dcaf5af00c2a67d4330247109 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
## `def test_rename_returns_references(self, tools)`

TestRenameTool.test_rename_returns_references verifies that rename_symbol returns the new name and lists dependent symbols in references.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestRenameTool.test_rename_invalid_identifier fingerprint=e85386992710e377f990eb6928fd51bd21ab7e6dd04a0fe11c58fd048054409a body_fp=ea574bebd06895b29a5df4785fb829041c8bad01a6c8251ded0676009cdc7264 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
## `def test_rename_invalid_identifier(self, tools)`

Tests that TestRenameTool.rename_symbol rejects invalid Python identifiers with "invalid_argument" error code.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestPreviewAndList fingerprint=3a67825ab606a45e1d3b01d2b3d48f1450339fe3e7e42a7b3e0526a4e7ea09da body_fp=240d6c4b30d4451c17f6044012811093ad25d4a940553e0c1c5059672c7f7cf7 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
## `class TestPreviewAndList`

Tests TrieTools preview and patch listing functionality through staged operations.

- `test_preview_reports_pending_and_cascade`: verifies preview shows pending changes and commit-ready status
- `test_preview_flags_multi_symbol_note_need`: checks multi-symbol patches trigger session note requirement
- `test_patch_list_includes_kind`: confirms patch list contains operation type metadata
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestPreviewAndList.test_preview_reports_pending_and_cascade fingerprint=c1193b5246f1c5823ff5739f1a9b60638e60c84177b4c20f24bbee76f75a5db5 body_fp=93a61d2817258499d11e16b47c070ac481ac96d6efca2cdc330eede75e2895f8 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
## `def test_preview_reports_pending_and_cascade(self, tools)`

TestPreviewAndList.test_preview_reports_pending_and_cascade verifies that preview() includes staged patches in pending and sets ready_to_commit flag.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestPreviewAndList.test_preview_flags_multi_symbol_note_need fingerprint=ff52bc65d34a8a31bcea0a5f7d2ca7cce6afddc11bc507fd261e23b5e7c00ed9 body_fp=5d14751a27d858e2efdfd8cf9638285dabfe2cca5a69308df9b8066fb9c1cfcd source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
## `def test_preview_flags_multi_symbol_note_need(self, tools)`

Tests that TestPreviewAndList.preview flags needs_session_note when multiple symbols have patches staged.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestPreviewAndList.test_patch_list_includes_kind fingerprint=f27baf15c2c895ee25fa5003baa05462b5234115b5ec52188cfa7a81623599e4 body_fp=b67c9f89ce8319f29fe807c80c999e4bc499166e5e38816ff5b1c23d0e98a817 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
## `def test_patch_list_includes_kind(self, tools)`

Verifies TestPreviewAndList.test_patch_list_includes_kind method confirms patch_list() includes kind field for rename operations.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestActivityAndSummary fingerprint=4f34e182635322e108a38e30bc58afe93d2dea6ec7867cf191b5e0597872500e body_fp=03bef302d027f2338e8ca4e03332cda1507c9742324d26439cbfc8051e7529c1 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
## `class TestActivityAndSummary`

Tests activity reporting and patch summary statistics in TrieTools.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestActivityAndSummary.test_activity_includes_patches_block fingerprint=19ce21c0c1b724258f27508681d3f07666b1603d45b10c9a8759cfa026ef6873 body_fp=efd77ddddb4549d3e345647d86410efc9b550c8365609fab10b9dfcb5f0ef3b5 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
## `def test_activity_includes_patches_block(self, tools)`

Verifies that TestActivityAndSummary activity method returns patches block with counts and null apply field.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestActivityAndSummary.test_patch_summary_counts_creates fingerprint=4f11e448170cab69475b333638f0933f5640c9b7a19d50bacc3c04a5d231deb1 body_fp=48106072d5b210fd7ffa97f54f2e06e8ff53c8ed42bb2126b35df4a263b59147 source_ref=1c912ed813dfb58752f16ac3ed6e959695a703b6 role=test -->
## `def test_patch_summary_counts_creates(self, tools)`

TestActivityAndSummary.test_patch_summary_counts_creates verifies that patch_summary includes create operations in its count.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestSessionIdInjection fingerprint=32be77b3725604e6c470312fe57b9b22aa96054fb6643ce293a6dd9ebcbc2bf2 body_fp=e233118ff8841e6bb04b0af8ddd7ce7ae400eda2d6aa91a094bdcfb8fa486742 source_ref=e9a78162908128eaac554c055f1ed9e887f1185d role=test -->
## `class TestSessionIdInjection`

Tests that TrieTools reads session ID from TRIE_SESSION_ID environment variable.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_mcp_edit_tools:TestSessionIdInjection.test_env_session_id_used fingerprint=75dd4f547709e5ab8a430412cac2cfff9fe0af273d58ea4b4637f9dbf46ce237 body_fp=60c0a181565f72f49757e337bce9f2145596afe9fd4c478846dd5beaabe3da30 source_ref=e9a78162908128eaac554c055f1ed9e887f1185d role=test -->
## `def test_env_session_id_used(self, project, monkeypatch)`

Verifies TestSessionIdInjection uses environment variable TRIE_SESSION_ID to set TrieTools session ID.
<!-- trie:end -->