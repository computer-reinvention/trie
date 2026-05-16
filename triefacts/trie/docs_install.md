---
trie_version: 0.1.0
source: trie/docs_install.py
file_fingerprint: fec8ff2adf95dc3d1a62271823ff1229829f8f45f8b70683e17c159d44449c3f
last_synced_at: '2026-05-16T13:55:00Z'
description: Project-local agent documentation install.
defines:
- kind: class
  qualified_name: trie/docs_install:DocsInstallError
  lines: 36-37
- kind: class
  qualified_name: trie/docs_install:DocsApplyResult
  lines: 76-87
- kind: class
  qualified_name: trie/docs_install:DocsInstallPlan
  lines: 91-96
- kind: function
  qualified_name: trie/docs_install:_load_trie_doc_body
  lines: 99-114
- kind: function
  qualified_name: trie/docs_install:_write_trie_doc
  lines: 117-159
- kind: function
  qualified_name: trie/docs_install:_apply_pointer
  lines: 162-220
- kind: function
  qualified_name: trie/docs_install:_splice_pointer_block
  lines: 223-248
- kind: function
  qualified_name: trie/docs_install:install
  lines: 251-274
incoming_refs: 16
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

<!-- trie:section symbol=trie/docs_install:_write_trie_doc fingerprint=03da19beaa06ee30af278dd28dc7774eb23ac42da6e1d08c7d851eb6cbe195e1 body_fp=bbaf474140bfffe37be8833511f8f3fbaf83b44d95ae349eae13f0fc8a288fb5 source_ref=b224274904f934dc347f86e766330c0b17478f24 -->
## `_write_trie_doc(project_root: Path, *, print_only: bool, dry_run: bool) -> DocsApplyResult`

Write the generated `TRIE.md` to `project_root`, skipping if content is unchanged.

- `print_only`: returns `"preview"` action with full body, no disk write.
- `dry_run`: checks staleness, then returns `"preview"` without writing.
- Returns `"skipped"` when existing file is byte-for-byte identical to new content.
- Returns `"error"` if the existing file cannot be read.
<!-- trie:end -->

<!-- trie:section symbol=trie/docs_install:_apply_pointer fingerprint=20ae022b61d331da6e16a5e843e34078385593bd4bcb7b9a816dd099ab222dbd body_fp=c7513ef53bd76b79347ef82970e83b6cf446b109a29180b407de269c2f47ad6e source_ref=b224274904f934dc347f86e766330c0b17478f24 -->
## `_apply_pointer(project_root: Path, filename: str, *, print_only: bool, dry_run: bool) -> DocsApplyResult | None`

Append or refresh the trie pointer block in one agent doc file, returning `None` if the file doesn't exist.

- Returns `None` when `filename` is absent — never creates the file.
- Replaces only the fenced marker block if already present; otherwise appends.
- `"skipped"` when existing content already matches exactly.
<!-- trie:end -->

<!-- trie:section symbol=trie/docs_install:_splice_pointer_block fingerprint=682c22cf6b9538998318e72973b6be67011ffc81977158e092db399bc95829c8 body_fp=bcb0e5f35bf43c742b2d638b72a35773f06821714cdc41a86f6b3fee4603d26a source_ref=b224274904f934dc347f86e766330c0b17478f24 -->
## `_splice_pointer_block(existing: str) -> str`

Return `existing` with the trie pointer block written between its markers, appending if absent.

- `existing`: full text of an agent doc file
- Replaces only the region between `POINTER_MARKER` and `POINTER_END_MARKER` when both are present; otherwise appends with a blank-line separator.
<!-- trie:end -->

<!-- trie:section symbol=trie/docs_install:install fingerprint=4222df60ecba4e488a7bf1175d38e5927881900bdb35241035eb91daef0fc89f body_fp=6489bfc8d399e34b5602cbae194cd2c3e64e2cc7ed7ea5689485f1a16204fe88 source_ref=b224274904f934dc347f86e766330c0b17478f24 -->
## `install(*, project_root: Path, print_only: bool, dry_run: bool) -> DocsInstallPlan`

Run the full docs install: write `TRIE.md` and refresh pointer blocks in existing agent doc files.

- `project_root`: directory where `TRIE.md` and agent doc files are written.
- `print_only`: return preview results without touching the filesystem.
- `dry_run`: compute changes but skip all writes.
- Missing agent doc files are silently omitted from results; errors per file don't abort remaining files.
<!-- trie:end -->