---
trie_version: 0.1.0
source: trie/docs_install.py
file_fingerprint: 778f367d7e715af47295fd5d06403d79910ec87e94a14d3813afc9b7c1b3bd90
last_synced_at: '2026-05-18T13:26:13Z'
description: Project-local agent documentation install.
defines:
- kind: class
  qualified_name: trie/docs_install:DocsInstallError
  lines: 38-39
- kind: function
  qualified_name: trie/docs_install:_pointer_line
  lines: 50-64
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
outgoing_refs: 0
---
<!-- trie:section symbol=trie/docs_install:DocsInstallError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=2487fc8e7b3ce809af62d04325d9b5017a0ddd33d7e9f88137e4352318897ee5 source_ref=b224274904f934dc347f86e766330c0b17478f24 -->
## `DocsInstallError`

Raised when the docs install cannot proceed due to a fatal configuration error.
<!-- trie:end -->

<!-- trie:section symbol=trie/docs_install:DocsApplyResult fingerprint=5469133ee021df50b7630b4a4ad3f38862fbcc34810fbcfb3c6a72661e24ffdf body_fp=ae7d98b5f3d1bbd02411ec5304975e0d3c4dda755056fab15387ea76c2bd4fb0 source_ref=b224274904f934dc347f86e766330c0b17478f24 -->
## `DocsApplyResult(target, action, path, detail="")`

Frozen dataclass recording the outcome of a single file operation during docs install.

- `action`: one of `"created"`, `"updated"`, `"skipped"`, `"preview"`, `"error"`
- `detail`: human-readable elaboration; carries preview text or error message
<!-- trie:end -->

<!-- trie:section symbol=trie/docs_install:DocsInstallPlan fingerprint=e447ac57430c778271b66c3d43d5eec6ab935302ac32ec0bcae7f01a0a453c51 body_fp=d80325797f8dd1fd8d928201e2b59615d5f259f71f09b9891ee325fa2e1b3319 source_ref=b224274904f934dc347f86e766330c0b17478f24 -->
## `DocsInstallPlan`

Aggregate result of a full docs install pass.

- `results`: collects one `DocsApplyResult` per file touched.
<!-- trie:end -->

<!-- trie:section symbol=trie/docs_install:_load_trie_doc_body fingerprint=d512ed2b9fcb319a91253ae56e02ab7806a83f8b605f06c5161ff91f18a2a9d2 body_fp=d5c81277496f0a9808c1026272a55aeece0eadc093a813c9a866956552763c3b source_ref=b224274904f934dc347f86e766330c0b17478f24 -->
## `_load_trie_doc_body() -> str`

Load and return the bundled `trie/data/TRIE.md` file contents as a UTF-8 string.

- Raises `DocsInstallError` if the data file is absent from the installed package.
<!-- trie:end -->

<!-- trie:section symbol=trie/docs_install:_write_trie_doc fingerprint=2a575c135629e997e28a2317becd7b8d5af1cf04591492a963845864da371398 body_fp=78082b9cd1aae5556ee06ceff70bb54ef7505e8ee4b8ab4215755059708e4830 source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `_write_trie_doc(project_root: Path, *, print_only: bool, dry_run: bool, target_name: str | None, additional_targets: list[str]) -> DocsApplyResult`

Write the generated `TRIE.md` to `project_root`, skipping if content is unchanged.

- `target_name`: selects harness whose tool-name prefix is baked into the body.
- `additional_targets`: appends a footer listing tool names for other installed harnesses.
- `print_only`: returns `"preview"` action with full body, no disk write.
- `dry_run`: checks staleness, then returns `"preview"` without writing.
- Returns `"skipped"` when existing file is byte-for-byte identical to new content.
- Returns `"error"` if the existing file cannot be read.
<!-- trie:end -->

<!-- trie:section symbol=trie/docs_install:_apply_pointer fingerprint=a763b7d91c68bd1347193a7e2a594af0ab84d377e2ea5b6532b1cd9f1b6646f1 body_fp=a2f6e35f8f39602bb18506d073851271d889a0a1c22c928823d05c8005fb455e source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `_apply_pointer(project_root: Path, filename: str, *, print_only: bool, dry_run: bool, target_name: str | None) -> DocsApplyResult | None`

Append or refresh the trie pointer block in one agent doc file, returning `None` if the file doesn't exist.

- Returns `None` when `filename` is absent — never creates the file.
- Replaces only the fenced marker block if already present; otherwise appends.
- `"skipped"` when existing content already matches exactly.
- `target_name` selects which harness's tool-name prefix is baked into the pointer line.
<!-- trie:end -->

<!-- trie:section symbol=trie/docs_install:_splice_pointer_block fingerprint=98addae38cee95d44f9b7ff1d1930368317dc0528288f2b6f9ca821341a5028e body_fp=7da8fbce5de9bca4dd9088b8a998ab9d89f153b2ec8533e23d18e5e9f40be086 source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `_splice_pointer_block(existing: str, pointer_block: str = POINTER_BLOCK) -> str`

Return `existing` with the trie pointer block written between its markers, appending if absent.

- `existing`: full text of an agent doc file
- `pointer_block`: the fenced block to write; defaults to the bare (unprefixed) form
- Replaces only the region between `POINTER_MARKER` and `POINTER_END_MARKER` when both are present; otherwise appends with a blank-line separator.
<!-- trie:end -->

<!-- trie:section symbol=trie/docs_install:install fingerprint=136c12139449e631a1f3b3f9ab57857c3bf38a44a342908ca3cac913587f7cd8 body_fp=a9715dc09e04f3b208939a64b4d85d3b29987ed7c36bc3c65475862e62130281 source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `install(*, project_root: Path, print_only: bool, dry_run: bool, target_names: list[str] | None = None) -> DocsInstallPlan`

Run the full docs install: write `TRIE.md` and refresh pointer blocks in existing agent doc files.

- `project_root`: directory where `TRIE.md` and agent doc files are written.
- `print_only`: return preview results without touching the filesystem.
- `dry_run`: compute changes but skip all writes.
- `target_names`: MCP harness slugs; first entry sets tool-name prefix baked into `TRIE.md` and pointer blocks; remainder appear in a footer; `None` falls back to bare unprefixed names.
- Missing agent doc files are silently omitted from results; errors per file don't abort remaining files.
<!-- trie:end -->

<!-- trie:section symbol=trie/docs_install:_pointer_line fingerprint=b80df7a6a54fc2dbd4a11e260664786d188b268f391291b1c1b835705fb0823d body_fp=f5d419876e810cf618cb0b5fcc7a75a280ffc527f3602748a8b6b7aa16ae17de source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `_pointer_line(grep_name: str, read_name: str, trace_name: str) -> str`

Build the agent-facing pointer sentence that links to `TRIE.md` with harness-specific tool names baked in.
<!-- trie:end -->

<!-- trie:section symbol=trie/docs_install:_render_tool_names fingerprint=94cc845e0f7537a1aabcf13f76a256d48091692ca0ce4a4ef9418672108050da body_fp=153df266bfadd292ae6082c8df8862fb70e698888f75647e533f9f529b4f2f23 source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `_render_tool_names(target_name: str | None) -> tuple[str, str, str]`

Resolve the rendered grep/read/trace tool names for a given MCP target, falling back to bare names when the target is unknown.

- `target_name`: key into `MCP_TARGETS`; `None` returns `("grep", "read", "trace")`
- Returns triple of `(grep_name, read_name, trace_name)` with harness prefix applied
<!-- trie:end -->

<!-- trie:section symbol=trie/docs_install:_render_trie_doc_body fingerprint=dd2c68e9b17365e8ea4031617b2c1d8523f81683651cdd3b120b4ee1b072174e body_fp=f251e87c1d3a502cdb0809cc6e7b28bce0d2f68b2487f49332a74732498529b6 source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `_render_trie_doc_body(target_name: str | None, additional_targets: list[str]) -> str`

Render the bundled TRIE.md template with harness-specific tool names substituted in.

- `target_name`: selects the harness whose prefix replaces `«grep»`, `«read»`, `«trace»`
- `additional_targets`: appends a footer listing equivalent tool names for other installed harnesses
<!-- trie:end -->

<!-- trie:section symbol=trie/docs_install:_multi_target_footer fingerprint=a410230a34d4f17180004d15061e507ca025abffc827f63dbb72f0967da54e37 body_fp=368ef6c28c94f1a60e541e0df58d3b6305b3aebeeb2c8602e1e9008f3e0530e0 source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `_multi_target_footer(primary: str | None, additional: list[str]) -> str`

Build a Markdown footer listing tool aliases for each harness beyond the primary.

- `primary`: slug of the harness whose names appear in the main body.
- `additional`: slugs of other installed harnesses; unknown slugs are silently skipped.
<!-- trie:end -->

<!-- trie:section symbol=trie/docs_install:_pointer_block_for fingerprint=d83b756430737cd0b23f0c7aa21d73968e703a3e17668c68942ebdef6e13b323 body_fp=3bd59d0c7ae89af2d26a1b83d540403d80b86de2fcd3a85b1b8dafaaefac06e3 source_ref=f33ef49ae65ead2b16b114b5450c290ad20aff99 -->
## `_pointer_block_for(target_name: str | None) -> str`

Build the marker-fenced pointer block with tool names rendered for the given harness target.

- **`target_name`**: MCP harness slug; `None` falls back to bare unprefixed tool names.
<!-- trie:end -->