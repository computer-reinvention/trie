---
trie_version: 0.1.2
source: trie/docs_install.py
file_fingerprint: 778f367d7e715af47295fd5d06403d79910ec87e94a14d3813afc9b7c1b3bd90
last_synced_at: '2026-05-23T23:49:23Z'
description: Project-local agent documentation install.
defines:
- kind: module
  qualified_name: trie/docs_install:__module__
  lines: 1-434
- kind: constant
  qualified_name: trie/docs_install:Action
  lines: 35-35
- kind: class
  qualified_name: trie/docs_install:DocsInstallError
  lines: 38-39
- kind: constant
  qualified_name: trie/docs_install:POINTER_MARKER
  lines: 46-46
- kind: constant
  qualified_name: trie/docs_install:POINTER_END_MARKER
  lines: 47-47
- kind: function
  qualified_name: trie/docs_install:_pointer_line
  lines: 50-64
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
- kind: class
  qualified_name: trie/docs_install:DocsInstallPlan
  lines: 110-115
- kind: function
  qualified_name: trie/docs_install:_load_trie_doc_body
  lines: 118-133
- kind: function
  qualified_name: trie/docs_install:_render_tool_names
  lines: 136-148
- kind: function
  qualified_name: trie/docs_install:_render_trie_doc_body
  lines: 151-170
- kind: function
  qualified_name: trie/docs_install:_multi_target_footer
  lines: 173-206
- kind: function
  qualified_name: trie/docs_install:_write_trie_doc
  lines: 209-264
- kind: function
  qualified_name: trie/docs_install:_pointer_block_for
  lines: 267-277
- kind: function
  qualified_name: trie/docs_install:_apply_pointer
  lines: 280-346
- kind: function
  qualified_name: trie/docs_install:_splice_pointer_block
  lines: 349-378
- kind: function
  qualified_name: trie/docs_install:install
  lines: 381-433
incoming_refs: 24
outgoing_refs: 2
---
<!-- trie:section symbol=trie/docs_install:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=8a002f73a29a7d431eda685263724e52b6c22535a04357839bfc48c712a4301c source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `trie/docs_install`

Materialise `TRIE.md` at the project root and inject a pointer line into `AGENTS.md` / `CLAUDE.md` so agents discover trie's navigation tools.

- Both writes are idempotent; marker fences isolate the managed block from user content.
- `TRIE.md` is overwritten unconditionally; agent doc files are updated only when they already exist.
- Tool names in generated text are resolved per MCP harness via `target_name`.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:Action fingerprint=03abe0d9a9f55bacd9af247ac370a3359e892a9cc531f7c6123593afcbcd3922 body_fp=a430d2f1e542c9c68dd8b44c8efe9ed15a00a76e0511ca86fe09da5142983ccf source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `Action = Literal["created", "updated", "skipped", "preview", "error"]`

Type alias enumerating the possible outcomes of a single docs-install file operation.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:DocsInstallError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=de8ce848be3b816fe20512323143e7219df89692c38c86087942e08be8223453 source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `DocsInstallError`

Raised when the docs install encounters a fatal error, such as a missing bundled `TRIE.md`.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:POINTER_MARKER fingerprint=c4efd8cc61a968603adee820add608f85f69816fa09687175778245d60136317 body_fp=d95044348775f6d69ea6453e28a9490ec764b49366bb34a18bd01d55b923106d source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `POINTER_MARKER = "<!-- trie:docs (added by \`trie setup\`) -->"`

Opening HTML-comment fence marking the start of the trie pointer block in agent doc files.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:POINTER_END_MARKER fingerprint=b09e750c1fcaebd68ee51bd3c1e225fe1e8252883c5367d509be322eae405541 body_fp=65a86e2569e11fc4819d5995902a13f9696c8700ffd4726339430e39587f0a64 source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `POINTER_END_MARKER = "<!-- end trie:docs -->"`

Closing fence marker that delimits the end of the trie pointer block in agent doc files.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:_pointer_line fingerprint=b80df7a6a54fc2dbd4a11e260664786d188b268f391291b1c1b835705fb0823d body_fp=a2d13b95023cedec5c4d84b6f83a27f25be5679e745c5934c23fdbc27a867e52 source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `_pointer_line(grep_name: str, read_name: str, trace_name: str) -> str`

Build the Markdown pointer sentence that directs agents to TRIE.md with harness-specific tool names baked in.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:POINTER_LINE fingerprint=328dcedda39c4ca57c31c9db897a527267b7f9fb0962a44b91fae9076d23ef4e body_fp=10d376b22a2a687525413c9a831d7e47be84c6f1c4252d6ac92be50e4819e72e source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `POINTER_LINE`

Default pointer-line text rendered with bare, unprefixed tool names (`grep`, `read`, `trace`).
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:POINTER_BLOCK fingerprint=79ae21e9ab842d77a20345fa0a2336d634ddc9ab79fe1cfa124d897f9adb2746 body_fp=2ca99dfd3446ca19327357053ac349f1903f4b8769aca236412485e4b5dc9ddd source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `POINTER_BLOCK`

Marker-fenced block combining `POINTER_MARKER`, `POINTER_LINE`, and `POINTER_END_MARKER`, ready to splice into agent doc files.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:AGENT_DOC_FILES fingerprint=de7b23421580076632901b01f52eff52a9fb070a8ce8384d7b0b0947f6bb232a body_fp=f7fd4864ab30b9c7609e093e5e16a50cb9ce4915fbc9ebc59e149a413565bafd source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `AGENT_DOC_FILES: tuple[str, ...] = ("AGENTS.md", "CLAUDE.md")`

Agent doc filenames that receive the trie pointer block if they already exist at the project root.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:TRIE_DOC_FILENAME fingerprint=cf3b380a179b16a13b4d4773331632abe1304ccbd8860a1c8fbd5eb7b771d1fd body_fp=08b8eb736bf62154c95b66db735e2ffba65f3f4144ac8829a97e62b392cab8f9 source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `TRIE_DOC_FILENAME = "TRIE.md"`

Filename of the generated project-local trie documentation artefact written to the project root.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:_GENERATED_NOTICE fingerprint=26b53384195b99f1af3f012cacde75b85176a680c910a7b3edace3b9366b3ea2 body_fp=ebca84e5d3bd8d71f5899d2664103b97cb7d15230c585b294dbfd961d0c9faf2 source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `_GENERATED_NOTICE: str`

HTML comment prepended to `TRIE.md` warning readers the file is generated and hand-edits will be overwritten.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:DocsApplyResult fingerprint=5469133ee021df50b7630b4a4ad3f38862fbcc34810fbcfb3c6a72661e24ffdf body_fp=a62d421c7d3d23d04bd16dfa686890277190d1728d8d00f526254e60c0bfd4ed source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `DocsApplyResult(target, action, path, detail="")`

Frozen dataclass recording the outcome of one file operation during a docs install pass.

- `target`: filename (e.g. `"TRIE.md"`, `"AGENTS.md"`) that was operated on.
- `action`: one of `"created"`, `"updated"`, `"skipped"`, `"preview"`, `"error"`.
- `path`: resolved `Path` to the file, or `None` if unavailable.
- `detail`: human-readable elaboration; carries preview text or error message.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:DocsInstallPlan fingerprint=e447ac57430c778271b66c3d43d5eec6ab935302ac32ec0bcae7f01a0a453c51 body_fp=776fb964e9a7f9c8920fd03bee183416493ce7f67d0c98528bf063abd9b70e62 source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `DocsInstallPlan`

Aggregate result of a full docs install pass.

- `results`: one `DocsApplyResult` per file touched during the pass.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:_load_trie_doc_body fingerprint=d512ed2b9fcb319a91253ae56e02ab7806a83f8b605f06c5161ff91f18a2a9d2 body_fp=91832252fc59d467a84654edc2838499284dfaf551c4a8451a25e462d843f604 source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `_load_trie_doc_body() -> str`

Load the bundled `trie/data/TRIE.md` text via `importlib.resources`.

- Raises `DocsInstallError` if the data file is missing from the installed package.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:_render_tool_names fingerprint=94cc845e0f7537a1aabcf13f76a256d48091692ca0ce4a4ef9418672108050da body_fp=9b15a8d0b209e9039288f3344ad723252861fa72352ec4bb9f5c33f7599d2f0d source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `_render_tool_names(target_name: str | None) -> tuple[str, str, str]`

Resolve harness-specific rendered names for the three trie tools, falling back to bare names when target is unknown.

- `target_name`: MCP target slug; `None` yields unprefixed `"grep"`, `"read"`, `"trace"`.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:_render_trie_doc_body fingerprint=dd2c68e9b17365e8ea4031617b2c1d8523f81683651cdd3b120b4ee1b072174e body_fp=affb05c23e0288519039fbc77e178f883cabfce5c9b981d3aca0cd9a2a1a3631 source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `_render_trie_doc_body(target_name: str | None, additional_targets: list[str]) -> str`

Substitute `«grep»`, `«read»`, `«trace»` placeholders in the bundled TRIE.md template with harness-specific tool names, appending a multi-harness footer when needed.

- `target_name`: selects the harness whose tool-name prefix is baked into the body.
- `additional_targets`: each extra harness gets a footer row listing its tool aliases.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:_multi_target_footer fingerprint=a410230a34d4f17180004d15061e507ca025abffc827f63dbb72f0967da54e37 body_fp=34e7132fdb02d85f5cfc8d481dae8e281e8398e2469c5592827c99a2ddbe1991 source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `_multi_target_footer(primary: str | None, additional: list[str]) -> str`

Build a Markdown footer section listing harness-specific tool name aliases for every entry in `additional`.

- `primary`: slug of the harness whose names appear in the main doc body; used for the intro sentence.
- `additional`: slugs of other installed harnesses; unknown slugs are silently skipped.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:_write_trie_doc fingerprint=2a575c135629e997e28a2317becd7b8d5af1cf04591492a963845864da371398 body_fp=ce75ae05a49f08c197c8fb3b71ff42fdc2f6c7b8beeddfe0a6cf73a10bc62b4b source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `_write_trie_doc(project_root, *, print_only, dry_run, target_name, additional_targets) -> DocsApplyResult`

Write (or preview) `TRIE.md` at `project_root`, skipping when content is already identical.

- `target_name`: harness slug whose tool-name prefix is baked into the body; `None` uses bare names.
- `additional_targets`: other installed harness slugs appended as a footer in the doc.
- `print_only`: returns a `preview` result without touching disk, bypassing the dry-run check.
- Returns `skipped` when the existing file matches byte-for-byte; `created` or `updated` otherwise.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:_pointer_block_for fingerprint=d83b756430737cd0b23f0c7aa21d73968e703a3e17668c68942ebdef6e13b323 body_fp=26379a25c9a802efb658f9bef1294f514ea06e3af3b2519705675c0cb515f699 source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `_pointer_block_for(target_name: str | None) -> str`

Build the complete marker-fenced pointer block using harness-specific tool names for `target_name`.

- `target_name`: MCP harness slug; `None` falls back to bare unprefixed names.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:_apply_pointer fingerprint=a763b7d91c68bd1347193a7e2a594af0ab84d377e2ea5b6532b1cd9f1b6646f1 body_fp=7bac5438cdb05042d5e8643adc2ccb9b7c6816f563594fcf2bfe0989c42f503a source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `_apply_pointer(project_root, filename, *, print_only, dry_run, target_name) -> DocsApplyResult | None`

Append or refresh the trie pointer block in one agent doc file, returning `None` if the file doesn't exist.

- `target_name`: selects harness whose tool-name prefix appears in the pointer line.
- Returns `None` silently when `filename` is absent; never creates the file.
- `action` is `"skipped"` when block content is already identical, `"updated"` otherwise.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:_splice_pointer_block fingerprint=98addae38cee95d44f9b7ff1d1930368317dc0528288f2b6f9ca821341a5028e body_fp=67656a1cb19ff6d046cfbb61b914ee18e901966e1a0e2ac642b40224922aee5b source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `_splice_pointer_block(existing: str, pointer_block: str = POINTER_BLOCK) -> str`

Return `existing` with `pointer_block` inserted or replaced between the trie marker fences.

- If markers are absent, appends with a blank-line separator.
- If markers are present, replaces only the fenced block, discarding hand-edits.
<!-- trie:end -->
<!-- trie:section symbol=trie/docs_install:install fingerprint=136c12139449e631a1f3b3f9ab57857c3bf38a44a342908ca3cac913587f7cd8 body_fp=f7dc68568571d900c3227e90d9e11091ae80e450dc17dc48bfab2ca416bc09ef source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `install(*, project_root: Path, print_only: bool, dry_run: bool, target_names: list[str] | None = None) -> DocsInstallPlan`

Write `TRIE.md` and refresh pointer blocks in any existing `AGENT_DOC_FILES` at `project_root`.

- `target_names`: first entry drives tool-name prefix in doc body; remaining entries appear in a footer.
- Missing agent doc files are silently skipped; per-file errors don't abort remaining files.
<!-- trie:end -->