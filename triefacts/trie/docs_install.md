---
trie_version: 0.3.0
source: trie/docs_install.py
file_fingerprint: 670d4594c8a103734c6a5ac146ae9858b2d63d710351ef2a9e11c1d75a6fb7a3
last_synced_at: '2026-08-01T09:20:24Z'
description: Project-local agent documentation install.
defines:
- kind: module
  qualified_name: trie/docs_install:__module__
  lines: 1-502
- kind: constant
  qualified_name: trie/docs_install:Action
  lines: 35-35
- kind: class
  qualified_name: trie/docs_install:DocsInstallError
  lines: 38-39
  signature: class DocsInstallError(Exception)
- kind: constant
  qualified_name: trie/docs_install:POINTER_MARKER
  lines: 46-46
- kind: constant
  qualified_name: trie/docs_install:POINTER_END_MARKER
  lines: 47-47
- kind: function
  qualified_name: trie/docs_install:_pointer_line
  lines: 50-64
  signature: 'def _pointer_line(grep_name: str, read_name: str, trace_name: str) -> str'
- kind: constant
  qualified_name: trie/docs_install:POINTER_LINE
  lines: 69-69
- kind: constant
  qualified_name: trie/docs_install:POINTER_BLOCK
  lines: 70-70
- kind: constant
  qualified_name: trie/docs_install:AGENT_DOC_FILES
  lines: 76-76
- kind: constant
  qualified_name: trie/docs_install:TRIE_DOC_FILENAME
  lines: 82-82
- kind: constant
  qualified_name: trie/docs_install:_GENERATED_NOTICE
  lines: 88-91
- kind: class
  qualified_name: trie/docs_install:DocsApplyResult
  lines: 95-106
  signature: class DocsApplyResult
- kind: class
  qualified_name: trie/docs_install:DocsInstallPlan
  lines: 110-115
  signature: class DocsInstallPlan
- kind: function
  qualified_name: trie/docs_install:_load_trie_doc_body
  lines: 118-133
  signature: def _load_trie_doc_body() -> str
- kind: constant
  qualified_name: trie/docs_install:ALL_TOOL_NAMES
  lines: 136-156
- kind: constant
  qualified_name: trie/docs_install:CORE_TOOL_NAMES
  lines: 158-158
- kind: constant
  qualified_name: trie/docs_install:_BARE_NAME_TARGETS
  lines: 163-163
- kind: constant
  qualified_name: trie/docs_install:_BARE_NAME_OVERRIDES
  lines: 169-172
- kind: function
  qualified_name: trie/docs_install:_select_primary_target
  lines: 175-197
  signature: 'def _select_primary_target(targets: list[str]) -> str | None'
- kind: function
  qualified_name: trie/docs_install:_render_tool_names
  lines: 200-220
  signature: 'def _render_tool_names( target_name: str | None, tool_names: tuple[str, ...] = ALL_TOOL_NAMES, ) -> tuple[str, ...]'
- kind: function
  qualified_name: trie/docs_install:_render_trie_doc_body
  lines: 223-238
  signature: 'def _render_trie_doc_body(target_name: str | None, additional_targets: list[str]) -> str'
- kind: function
  qualified_name: trie/docs_install:_multi_target_footer
  lines: 241-274
  signature: 'def _multi_target_footer(primary: str | None, additional: list[str]) -> str'
- kind: function
  qualified_name: trie/docs_install:_write_trie_doc
  lines: 277-332
  signature: 'def _write_trie_doc( project_root: Path, *, print_only: bool, dry_run: bool, target_name: str | None, additional_targets: list[str], ) -> DocsApplyResult'
- kind: function
  qualified_name: trie/docs_install:_pointer_block_for
  lines: 335-345
  signature: 'def _pointer_block_for(target_name: str | None) -> str'
- kind: function
  qualified_name: trie/docs_install:_apply_pointer
  lines: 348-414
  signature: 'def _apply_pointer( project_root: Path, filename: str, *, print_only: bool, dry_run: bool, target_name: str | None, ) -> DocsApplyResult | None'
- kind: function
  qualified_name: trie/docs_install:_splice_pointer_block
  lines: 417-446
  signature: 'def _splice_pointer_block(existing: str, pointer_block: str = POINTER_BLOCK) -> str'
- kind: function
  qualified_name: trie/docs_install:install
  lines: 449-501
  signature: 'def install( *, project_root: Path, print_only: bool, dry_run: bool, target_names: list[str] | None = None, ) -> DocsInstallPlan'
incoming_refs: 54
outgoing_refs: 2
---
<!-- trie:section symbol=trie/docs_install:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=1c3538593c9f8d9d4a0de47676ca43fffefb02005e65d98f510a552985bb4fa4 source_ref=637a214fb02121ef02ef39bfc864ca1f54b4ab48 role=agent-integration -->
Installs trie documentation by creating TRIE.md and adding pointer lines to agent documentation files.

- Writes TRIE.md with tool names customized for the target agent harness
- Appends marker-fenced pointer blocks to existing AGENTS.md and CLAUDE.md files  
- Uses idempotent operations that preserve existing content outside marker boundaries
- Supports multi-agent projects by listing tool names for all installed harnesses
- Skips missing agent doc files rather than creating them automatically
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:Action fingerprint=03abe0d9a9f55bacd9af247ac370a3359e892a9cc531f7c6123593afcbcd3922 body_fp=09712802c92b2d15e76015b15f96f6d7001b9fd6d9d1f3b095ee1c16be1960f3 source_ref=637a214fb02121ef02ef39bfc864ca1f54b4ab48 role=agent-integration -->
Type alias for the outcome status of a single docs install file operation.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:DocsInstallError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=e641a08fe224ce060f361d4fe3959ffbdea8f46a18bec58382e7cb9fcaa3be52 source_ref=637a214fb02121ef02ef39bfc864ca1f54b4ab48 role=agent-integration -->
## `class DocsInstallError(Exception)`

Custom exception raised when documentation installation fails.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:POINTER_MARKER fingerprint=c4efd8cc61a968603adee820add608f85f69816fa09687175778245d60136317 body_fp=c4d5af60dffb2222747791069562923297d48a2f0c85e5d98a0f6c137e8789c9 source_ref=637a214fb02121ef02ef39bfc864ca1f54b4ab48 role=agent-integration -->
HTML comment marker that identifies the start of trie's pointer block in agent documentation files.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:POINTER_END_MARKER fingerprint=b09e750c1fcaebd68ee51bd3c1e225fe1e8252883c5367d509be322eae405541 body_fp=4e0284dac5477dbf711ecccb6932bc8fc754a3a5bdb7c07744e775e5c951318c source_ref=637a214fb02121ef02ef39bfc864ca1f54b4ab48 role=agent-integration -->
HTML comment string marking the end of the trie documentation pointer block in agent files.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:_pointer_line fingerprint=b80df7a6a54fc2dbd4a11e260664786d188b268f391291b1c1b835705fb0823d body_fp=c8f1341a36711bc9560219da8d8575becbc5324249ebb0a1511dac1f68fc2985 source_ref=637a214fb02121ef02ef39bfc864ca1f54b4ab48 role=agent-integration -->
## `def _pointer_line(grep_name: str, read_name: str, trace_name: str) -> str`

Builds a formatted pointer line that tells agents about trie tools with their harness-specific names.

- `grep_name`: The agent-visible name for the grep tool (e.g., `mcp__trie__grep`)
- `read_name`: The agent-visible name for the read tool (e.g., `mcp__trie__read`)
- `trace_name`: The agent-visible name for the trace tool (e.g., `mcp__trie__trace`)
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:POINTER_LINE fingerprint=328dcedda39c4ca57c31c9db897a527267b7f9fb0962a44b91fae9076d23ef4e body_fp=18f712dff568e0175c65440402e84cfb054e2d787df73d9e0bfad5bdc2cf5c0a source_ref=637a214fb02121ef02ef39bfc864ca1f54b4ab48 role=agent-integration -->
Default pointer line text that references unprefixed tool names (`grep`, `read`, `trace`).
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:POINTER_BLOCK fingerprint=79ae21e9ab842d77a20345fa0a2336d634ddc9ab79fe1cfa124d897f9adb2746 body_fp=f9acff5c15d8ff29344ae249b502dfb4a7cd8477676b1c2d02f561859c3ef805 source_ref=637a214fb02121ef02ef39bfc864ca1f54b4ab48 role=agent-integration -->
Default pointer block with HTML comment markers wrapping the bare tool names pointer line.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:AGENT_DOC_FILES fingerprint=de7b23421580076632901b01f52eff52a9fb070a8ce8384d7b0b0947f6bb232a body_fp=767cb728562fb8b25328aeca020ba7846030d48bcfbb0b3c25000830ed31506f source_ref=637a214fb02121ef02ef39bfc864ca1f54b4ab48 role=agent-integration -->
Tuple of agent documentation filenames that receive trie pointer blocks during setup.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:TRIE_DOC_FILENAME fingerprint=cf3b380a179b16a13b4d4773331632abe1304ccbd8860a1c8fbd5eb7b771d1fd body_fp=11ae6e7dacf312630bef0316d838f7e6d09bef9184251d221f85f637d291b3e3 source_ref=637a214fb02121ef02ef39bfc864ca1f54b4ab48 role=agent-integration -->
Filename for the project-local trie documentation generated at the project root.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:_GENERATED_NOTICE fingerprint=26b53384195b99f1af3f012cacde75b85176a680c910a7b3edace3b9366b3ea2 body_fp=1a820bd5603677b58eb28bf57009f4babe6d2ffbf664e2b7be3b698600efcbf1 source_ref=637a214fb02121ef02ef39bfc864ca1f54b4ab48 role=agent-integration -->
HTML comment block prepended to `TRIE.md` warning that hand-edits will be overwritten.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:DocsApplyResult fingerprint=5469133ee021df50b7630b4a4ad3f38862fbcc34810fbcfb3c6a72661e24ffdf body_fp=fa17a2617c6eb60dc09d42d16f534efd3d54406fd3d079c04e0561a3f31345bd source_ref=637a214fb02121ef02ef39bfc864ca1f54b4ab48 role=agent-integration -->
## `class DocsApplyResult`

Records the outcome of a single file operation during documentation installation.

- `target`: name of the file being operated on
- `action`: what happened (created/updated/skipped/preview/error)
- `path`: filesystem location of the target file
- `detail`: additional context about the operation result
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:DocsInstallPlan fingerprint=e447ac57430c778271b66c3d43d5eec6ab935302ac32ec0bcae7f01a0a453c51 body_fp=d1aa535c8f31be5435550d6d8d010b4982d12d5a590c45aa4867daa26489ec14 source_ref=637a214fb02121ef02ef39bfc864ca1f54b4ab48 role=agent-integration -->
## `class DocsInstallPlan`

Aggregates results of a complete documentation installation pass.

- `results`: List of file operation outcomes, one per touched file
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:_load_trie_doc_body fingerprint=d512ed2b9fcb319a91253ae56e02ab7806a83f8b605f06c5161ff91f18a2a9d2 body_fp=e35dce405fb15c695d3d7c663a77e0f9ef73171ab0d12952322d65559ba2181d source_ref=637a214fb02121ef02ef39bfc864ca1f54b4ab48 role=agent-integration -->
## `def _load_trie_doc_body() -> str`

Return the bundled `TRIE.md` body as text from the package's data directory.

- Raises `DocsInstallError` if the bundled file is missing from the package
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:ALL_TOOL_NAMES fingerprint=e9218d394222ca4cd51b8543dd4ee4290e7868053f4e9efa494ac7154398454d body_fp=66a348f456b8b87b0a37f5047808c649fb84bb62bde0f5120fe7693b2fad0cbf source_ref=b11f520c43aa24dfcbd24ba256b957c76b45b6d6 role=config -->
Tuple containing the canonical names of all trie MCP tools for documentation rendering.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:CORE_TOOL_NAMES fingerprint=a01417ad0bf41b11233db4c1efafe4be8cd1310ada273677c106bfa1a6c60159 body_fp=3e6f2e90a54b3efeb99501f1c00c9c7afabeb441a9fae64fff073e65483e7bfd source_ref=637a214fb02121ef02ef39bfc864ca1f54b4ab48 role=agent-integration -->
Tuple of the three core tool names that appear in agent doc pointer lines.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:_BARE_NAME_TARGETS fingerprint=e18bb59a3074732896d7e1791b0d5835544dd5e5b1eeb6b69a46e7259fad0ae9 body_fp=49d386ee99d2a5e2bba236d1305bcdb5434e49983c22d995e4f618ec82949f80 source_ref=637a214fb02121ef02ef39bfc864ca1f54b4ab48 role=agent-integration -->
Frozen set of target names that expose bare tool names without MCP prefixes.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:_BARE_NAME_OVERRIDES fingerprint=5f93cfef34be890e1dd5f86939c5ea90f7803b07133113f2887f7becab0bd59b body_fp=c077e408a38e86efe543585a15cead52abd5d6abfbedef42a1b094facdf3a364 source_ref=b11f520c43aa24dfcbd24ba256b957c76b45b6d6 role=config -->
Maps the two MCP tool names that bare-name targets expose under shortened aliases to those shorter forms.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:_select_primary_target fingerprint=fd021cf8fb6802e99d5fbd75373afbdd62fe9f1fc74db423cbccee067a6e56f4 body_fp=2cf0bf4716ffa4cfa0acf2e22fa48fe8a072f0c78569f6569249844823fcae40 source_ref=18479783bb2e381c26bc3791a8de21514177cbd8 role=util -->
## `def _select_primary_target(targets: list[str]) -> str | None`

Select the primary target from `targets`, preferring any bare-name override harness (e.g. opencode) over registry order.

- Returns `None` when `targets` is empty.
- Returned slug controls which tool-name prefix is baked into `TRIE.md` and the pointer block.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:_render_tool_names fingerprint=1994bcc1f47d5af53555c4fd23dca1537dabc713696c0212bb1cebc6a1c67f8a body_fp=e610d06af0e81cbf68fae2f3b027e400be5c89abf49a70eb12a27b8631ad1cb2 source_ref=b11f520c43aa24dfcbd24ba256b957c76b45b6d6 role=util -->
## `def _render_tool_names( target_name: str | None, tool_names: tuple[str, ...] = ALL_TOOL_NAMES, ) -> tuple[str, ...]`

Resolves tool names for a target harness, applying prefixes according to the target's naming convention or returning bare names for override targets.

- Returns bare tool names for opencode target (with two shortened exceptions via `_BARE_NAME_OVERRIDES`) or when target is None/unknown
- Applies `MCPTarget.tool_name_format` template for other targets (e.g. `mcp__trie__grep`)
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:_render_trie_doc_body fingerprint=f808b5ce80ae80c0f3e96a795081963edfdb15d0d83ff8f244285247d78b367e body_fp=33236ad53dc0d0d31888b7d2105ce5e63396d95002d82bd490dfe50186cd46a6 source_ref=637a214fb02121ef02ef39bfc864ca1f54b4ab48 role=agent-integration -->
## `def _render_trie_doc_body(target_name: str | None, additional_targets: list[str]) -> str`

Renders TRIE.md content with target-specific tool names by substituting placeholders and adding multi-target footer when needed.

- `target_name`: selects which harness's tool name format to use for placeholders
- `additional_targets`: other installed targets that get listed in footer
- Returns: rendered markdown content with `«tool_name»` placeholders replaced
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:_multi_target_footer fingerprint=35857e704e1551a50edb5324952d860180d3f5b39d86dc9a6acd3648cacc5298 body_fp=285a91149f1eb3980ad55501637eebcea718b10e7facad69d81191f94838fd62 source_ref=637a214fb02121ef02ef39bfc864ca1f54b4ab48 role=agent-integration -->
## `def _multi_target_footer(primary: str | None, additional: list[str]) -> str`

Builds a markdown footer listing tool names for additional harness targets beyond the primary one.

- `primary`: name of primary target or None for default "primary" display
- `additional`: list of target slugs to include in footer
- Returns: markdown section with harness names and their prefixed tool names
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:_write_trie_doc fingerprint=2a575c135629e997e28a2317becd7b8d5af1cf04591492a963845864da371398 body_fp=096c4ed5ecb79a9015a2f1810120a275639587f6ae170496adb338dd13e42abf source_ref=637a214fb02121ef02ef39bfc864ca1f54b4ab48 role=agent-integration -->
## `def _write_trie_doc( project_root: Path, *, print_only: bool, dry_run: bool, target_name: str | None, additional_targets: list[str], ) -> DocsApplyResult`

Writes TRIE.md at project root with target-specific tool names, skipping if content unchanged.

- `target_name`: harness whose tool prefix is baked into doc body 
- `additional_targets`: other harnesses listed in footer for multi-agent projects
- Returns `DocsApplyResult` with action "created", "updated", "skipped", "preview", or "error"
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:_pointer_block_for fingerprint=cbd860bde347ee152ae7440d1a192b98cec61357cb8c7cd5e501ebfbed0ffad0 body_fp=045a825cd4372729c8f8ad3c1111bbbe1f90de12df0b6b53b164502237dafec9 source_ref=637a214fb02121ef02ef39bfc864ca1f54b4ab48 role=agent-integration -->
## `def _pointer_block_for(target_name: str | None) -> str`

Builds the marker-fenced pointer block for a target harness with harness-specific tool names.

- Falls back to bare tool names when target_name is None or unknown
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:_apply_pointer fingerprint=a763b7d91c68bd1347193a7e2a594af0ab84d377e2ea5b6532b1cd9f1b6646f1 body_fp=cfe83bc8c562086ac03a80a51f068242b93711384276149127c1bd5a00ddf99e source_ref=637a214fb02121ef02ef39bfc864ca1f54b4ab48 role=agent-integration -->
## `def _apply_pointer( project_root: Path, filename: str, *, print_only: bool, dry_run: bool, target_name: str | None, ) -> DocsApplyResult | None`

Appends or refreshes the trie pointer block in agent doc files like AGENTS.md or CLAUDE.md.

- Returns `None` when the target file doesn't exist (won't create user-authored files)
- `target_name`: selects harness tool name format for the pointer line
- Preserves existing content, only modifying the marker-fenced trie block
- Returns `DocsApplyResult` with action: "skipped", "updated", "preview", or "error"
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:_splice_pointer_block fingerprint=98addae38cee95d44f9b7ff1d1930368317dc0528288f2b6f9ca821341a5028e body_fp=d3cfac7c67150045b94975811c4cda2d0a6a408e1704e7ffde441a427d028119 source_ref=637a214fb02121ef02ef39bfc864ca1f54b4ab48 role=agent-integration -->
## `def _splice_pointer_block(existing: str, pointer_block: str = POINTER_BLOCK) -> str`

Replaces existing marker-fenced block or appends pointer block to text with proper spacing.

- Uses `POINTER_MARKER` and `POINTER_END_MARKER` to locate existing block for replacement
- Appends with blank line separation when markers not found  
- Preserves content before/after markers when replacing
- Defaults to `POINTER_BLOCK` when `pointer_block` parameter not provided
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:install fingerprint=49f37c5c4badcfccee3a113011f0084a617fb5a0f4f6d2f4efb72c76932ea439 body_fp=ecf31e255d7ad92ba930480644f15ef12ab1a867ba87d32d2e561c0d0d91c74a source_ref=18479783bb2e381c26bc3791a8de21514177cbd8 role=orchestration -->
## `def install( *, project_root: Path, print_only: bool, dry_run: bool, target_names: list[str] | None = None, ) -> DocsInstallPlan`

Installs trie documentation by writing TRIE.md and adding pointer blocks to existing agent doc files.

- `target_names`: MCP harnesses list; bare-name (override) target is preferred as primary when present, else first entry; rest appear in footer
- `print_only`/`dry_run`: control whether changes are actually written to disk
- Returns plan with results for each file operation (TRIE.md always included, agent files only if they exist)
<!-- trie:end -->