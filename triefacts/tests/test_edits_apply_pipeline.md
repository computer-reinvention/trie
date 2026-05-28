---
trie_version: 0.1.5
source: tests/test_edits_apply_pipeline.py
file_fingerprint: a8be6afe8812a4760ea62849349604169cf88cbc6ed0ef3d5174a17febd490ed
last_synced_at: '2026-05-28T14:59:35Z'
defines:
- kind: module
  qualified_name: tests/test_edits_apply_pipeline:__module__
  lines: 1-402
- kind: constant
  qualified_name: tests/test_edits_apply_pipeline:PROJECT_TOML
  lines: 22-30
- kind: function
  qualified_name: tests/test_edits_apply_pipeline:_git
  lines: 33-34
- kind: function
  qualified_name: tests/test_edits_apply_pipeline:_init_repo
  lines: 37-40
- kind: function
  qualified_name: tests/test_edits_apply_pipeline:_extract_old_source
  lines: 43-56
- kind: function
  qualified_name: tests/test_edits_apply_pipeline:_extract_old_prose
  lines: 59-66
- kind: function
  qualified_name: tests/test_edits_apply_pipeline:_is_merge_prompt
  lines: 69-70
- kind: function
  qualified_name: tests/test_edits_apply_pipeline:_make_usage
  lines: 73-85
- kind: class
  qualified_name: tests/test_edits_apply_pipeline:FakeTriefactClient
  lines: 88-108
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:FakeTriefactClient.run
  lines: 94-104
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:FakeTriefactClient.count_tokens
  lines: 107-108
- kind: class
  qualified_name: tests/test_edits_apply_pipeline:FakeEditClient
  lines: 111-146
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:FakeEditClient.run
  lines: 120-142
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:FakeEditClient.count_tokens
  lines: 145-146
- kind: class
  qualified_name: tests/test_edits_apply_pipeline:PassthroughClient
  lines: 149-183
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:PassthroughClient.run
  lines: 155-179
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:PassthroughClient.count_tokens
  lines: 182-183
- kind: class
  qualified_name: tests/test_edits_apply_pipeline:BrokenClient
  lines: 186-218
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:BrokenClient.run
  lines: 192-214
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:BrokenClient.count_tokens
  lines: 217-218
- kind: function
  qualified_name: tests/test_edits_apply_pipeline:project
  lines: 222-275
- kind: class
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesEmpty
  lines: 278-298
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesEmpty.test_no_patches_returns_immediately
  lines: 279-285
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesEmpty.test_git_clean_after_empty_apply
  lines: 287-298
- kind: class
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesSuccess
  lines: 301-365
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_applies_single_symbol
  lines: 302-313
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_patches_deleted_after_success
  lines: 315-324
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_no_git_commit_created
  lines: 326-340
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_applies_in_topo_order
  lines: 342-349
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_cascaded_no_change_skips_write
  lines: 351-365
- kind: class
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesFailure
  lines: 368-401
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesFailure.test_compile_error_returns_failure
  lines: 369-377
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesFailure.test_rollback_restores_files
  lines: 379-390
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesFailure.test_patches_preserved_after_rollback
  lines: 392-401
incoming_refs: 0
outgoing_refs: 71
---
<!-- trie:section symbol=tests/test_edits_apply_pipeline:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=6265c5e869b245714d5c9f44a244e7710b2706891ec4abb3ff8346dd040dce6c source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `tests/test_edits_apply_pipeline`

Integration tests for the `apply_patches` pipeline covering empty, success, and failure/rollback scenarios.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:PROJECT_TOML fingerprint=ea44d5615a2611cc14e40b5b84f8141a4679269bc80e3914e4fef0417f24d38b body_fp=7895586011efcec470031ad4375cfc3c25b5ed6f6e52691c19e7163e1f8bb54e source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `PROJECT_TOML`

TOML string used to write `trie.toml` in test fixtures.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:_git fingerprint=9efa6f55f9332a871587d0a9f0d4447d61f49c18b4d819e91e90494d14cf2f16 body_fp=058d2f28a55e2fa4f0049fc38c500ad95bb4909249da1d42856d58b6fe934fc7 source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `_git(args: list[str], cwd: Path) -> None`

Run a git command in the given directory, raising on non-zero exit.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:_init_repo fingerprint=e6a8e59044cd4691a616ada677408e96c9c856caafae13744c548e08d2b462be body_fp=83b38a67d8daf54b96043670576a0e5189384469d9f5ac32e2b3fdc25d7ca80d source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `_init_repo(path: Path) -> None`

Initialise a bare Git repository at `path` with a fixed test identity on branch `main`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:_extract_old_source fingerprint=bcd11656d8918f3fa2184a028c94523c815515e979b154d01009499a9c24e786 body_fp=f3054045726a6b393fc48c0aa8e2a4d2523f2fa897fffb30a8c9438a0b782145 source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `_extract_old_source(request: str) -> str`

Extract the non-empty lines from the first fenced Python code block in an infer prompt string.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:_extract_old_prose fingerprint=8717c70ea434bf53fc16753b5930da9e782d3e0318ae3bee95b278c5667c8450 body_fp=2c74d2650563badca2a559c6172cbed24730d257e509253683f865761f0b9813 source_ref=ddb37c0ac4325b2b942f385fddf783792fa16092 -->
## `_extract_old_prose(request: str) -> str`

Extract the old prose section from an infer prompt string, returning empty string if absent.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:_is_merge_prompt fingerprint=13df75d98109396ebce3eeae9f2acd9b95400180791f4b8d1b4d6a5d780269ca body_fp=0c5733e629303e760b91d045a2c6efdb4c4812255bcf2008f9ffb44ac01d10b7 source_ref=ddb37c0ac4325b2b942f385fddf783792fa16092 -->
## `_is_merge_prompt(request: str) -> bool`

Return `True` if `request` contains the merge-notes marker string.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:_make_usage fingerprint=778ea16dee0036412660edb79d77aa94f191365fcd8e9c689ed41ba866b067a1 body_fp=26a5074708d8164a3781259a690aac5df0c081c246d5a28337016a5c15d047a1 source_ref=ddb37c0ac4325b2b942f385fddf783792fa16092 -->
## `_make_usage(**overrides: int)`

Build a fake `Usage` object with default token counts, overridable via keyword arguments.

- `input_tokens`: defaults to 10
- `output_tokens`: defaults to 20
- `cache_creation_input_tokens` / `cache_read_input_tokens`: default to 0
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:FakeTriefactClient fingerprint=afb393792203da3e6a3e2731358c6a81064752259730c585fe6ee9b20ba350e9 body_fp=26d2159bcdb36f0056b5fb53beb866ea9d8e9dcb0cfc352a3d5b631403af9445 source_ref=ddb37c0ac4325b2b942f385fddf783792fa16092 -->
## `FakeTriefactClient`

Test double LLM client that returns a fixed triefact body for use with `sync_single_file`.

- `run`: always returns a static `"## Symbol\n\nAuto-generated prose.\n"` wrapped in a `ModelResult`.
- `count_tokens`: always returns 100.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:FakeTriefactClient.run fingerprint=aa2a88a9411d02e5505faa8a887e26efa9c481c5ae82a19d96ed33eb9a68478b body_fp=f1e1d4b3390dce69a5ebe3c6407bf4d5aa291d47a25f05341a7ee8561d659888 source_ref=ddb37c0ac4325b2b942f385fddf783792fa16092 -->
## `FakeTriefactClient.run(output_type, system_prompt, user_prompt, *, max_tokens=1024) -> ModelResult`

Return a static `ModelResult` wrapping a fixed `SectionBody` string, ignoring all inputs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:FakeTriefactClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=b942b2a9557a3dd9792538e03984def6dd4cf6dcccb6a0f3e5e7157efa0e0141 source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `FakeTriefactClient.count_tokens(_req: GenerationRequest) -> int`

Always return 100 for any `FakeTriefactClient` token-count request.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:FakeEditClient fingerprint=5ccfeb4f9c57d8afcf6b980aec33a17b28cabddad2411edc019cc9805c4fa770 body_fp=095e4b3786326093752fd81e9522f13d31b2d2bfec4935f96d243aa0c0078179 source_ref=ddb37c0ac4325b2b942f385fddf783792fa16092 -->
## `FakeEditClient`

LLM test double for patch-apply calls that appends `# patch-applied` to source or returns a static merge response.

- `run`: returns merge response for `MergeNotesOutput`, empty decisions for `BatchFilterOutput`, otherwise appends `# patch-applied` to extracted source.
- `count_tokens`: always returns `100`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:FakeEditClient.run fingerprint=bc56c6959c2a9044f8ebbe0632c45e1585f7a0f86c1f9a24568791f931915ab3 body_fp=b0222d7f3833b71a07e9b185fe8b43cf7a8f372d90b8d802f86018ced75bffdd source_ref=ddb37c0ac4325b2b942f385fddf783792fa16092 -->
## `FakeEditClient.run(output_type, system_prompt, user_prompt, *, max_tokens=1024) -> ModelResult`

Return a fake `ModelResult` branching on `output_type`: merge notes, batch filter, or a `SymbolEdit` with `# patch-applied` appended to the extracted old source.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:FakeEditClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=225d1aad76912b5124f832c0497ed893289f3318fd2c776a7a81c9a3bd3028a7 source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `FakeEditClient.count_tokens(_req: GenerationRequest) -> int`

Always return 100 for any `FakeEditClient` token-count request.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:PassthroughClient fingerprint=c84c1b8c854da950a3a570721c0e00b5d73fcfb5c295ac9e88444b8139bc5aca body_fp=2b0bed447c3496fb57cdd3c732aff08db2b7bcb7b457d266e53817e729dcb09d source_ref=ddb37c0ac4325b2b942f385fddf783792fa16092 -->
## `PassthroughClient`

LLM test double that returns the extracted old source and prose verbatim, unchanged.

- `run`: returns merge response for `MergeNotesOutput`, empty decisions for `BatchFilterOutput`, otherwise echoes extracted source and prose as a `ModelResult`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:PassthroughClient.run fingerprint=9346deca9763f8a2f77fea6524e9d1db47b6388696fe2a588f6f0a60583c161d body_fp=a9d222e3ed28fbdea9d7988068f2cfb97db3a46da58a155a39564f4bf524b01f source_ref=ddb37c0ac4325b2b942f385fddf783792fa16092 -->
## `PassthroughClient.run(output_type, system_prompt, user_prompt, *, max_tokens=1024) -> ModelResult`

Return a `ModelResult` echoing the old source and prose extracted from `user_prompt` unchanged, or fixed stub outputs for `MergeNotesOutput`/`BatchFilterOutput` requests.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:PassthroughClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=5e76d16fdf07755c8c6f2605ffb0f37902955e777cee60d33004dd835e6496b2 source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `PassthroughClient.count_tokens(_req: GenerationRequest) -> int`

Return a fixed token count of 100 for any `PassthroughClient` request.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:BrokenClient fingerprint=5ea1701839391bb9a2c9a680e33f9284227dd45596b2535d0d3b491fcd4b0448 body_fp=fc586e19c701a330782a5252e56bfa57ee80d7a05d6c7534a2571ca5cb81685e source_ref=ddb37c0ac4325b2b942f385fddf783792fa16092 -->
## `BrokenClient`

Fake LLM client that always returns syntactically invalid Python source to trigger compile-error failure paths.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:BrokenClient.run fingerprint=409a604a9de51871d52d433242c4dd9b14b28806674d3b6021a89db8fabf9e88 body_fp=d8a2636c0b80d726570a1255b9aeef3534352cd186fa1c1f84245790bebddf53 source_ref=ddb37c0ac4325b2b942f385fddf783792fa16092 -->
## `BrokenClient.run(output_type, system_prompt, user_prompt, *, max_tokens=1024) -> ModelResult`

Return a `ModelResult` with syntactically invalid Python source for `SymbolEdit` requests, valid stubs for `MergeNotesOutput` and `BatchFilterOutput`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:BrokenClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=069c7f8c0c03b0cc5fb20eeeb912c52a4e05f38b13e252707eae087b2bf5c670 source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `BrokenClient.count_tokens(_req: GenerationRequest) -> int`

Return a fixed token count of 100 for any `BrokenClient` request.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:project fingerprint=26c6072a1e41f0d8332363602aa260b6b79e16528f847797cda935b864cc4be5 body_fp=32f3ac9c8d7217794ccd1d7564af6fbca3649fbd223ff3b5e2ddedd0a6a1ba26 source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `project(tmp_path: Path) -> Path`

Pytest fixture providing a fully-scanned, triefact-synced, git-committed three-module project rooted at `tmp_path`.

- Returns `tmp_path`: the project root with `trie.toml`, `.gitignore`, `src/`, and a clean initial commit.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesEmpty fingerprint=fe9d42f96f40e8e186b3dfcf3f116213343fed5a7b5704784a2be138c5e63695 body_fp=ca1a1975b479e525bdfe54040a46fd27fa1629911f7fb6601a2e04e10dfb8ad4 source_ref=ddb37c0ac4325b2b942f385fddf783792fa16092 -->
## `TestApplyPatchesEmpty`

Test `apply_patches` behaviour when no patches are pending in the store.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesEmpty.test_no_patches_returns_immediately fingerprint=af1c83bd2eab932f81c972d6026fae8cfc67306e824f0f162b8c6f3fbf645270 body_fp=1bffa0a229f6a5deef8092efb6e44439f26e9ba9cd00d59e0313ebf3e6fccd3c source_ref=ddb37c0ac4325b2b942f385fddf783792fa16092 -->
## `TestApplyPatchesEmpty.test_no_patches_returns_immediately(self, project: Path)`

Assert `apply_patches` returns `ok=True`, `total_files=0`, `total_symbols=0` when no patches exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesEmpty.test_git_clean_after_empty_apply fingerprint=c5893657f0aed624008309b981a1fddcbad56f7dc907a8310567dda75f8b7c68 body_fp=a10d0bd998c47708673c76627a398f7ab41f51b1f83f881c36366cf875167577 source_ref=ddb37c0ac4325b2b942f385fddf783792fa16092 -->
## `TestApplyPatchesEmpty.test_git_clean_after_empty_apply(self, project: Path)`

Assert the working tree has no uncommitted changes after `apply_patches` runs with no pending patches.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesSuccess fingerprint=8484656371c70dea113a63d7c783db6a16e4f4c9ce1f821839d374d3fa0668c7 body_fp=63bec6a76ecbf4c79f8525cad07e938548c4823d8457c265247885f36e083b45 source_ref=ddb37c0ac4325b2b942f385fddf783792fa16092 -->
## `TestApplyPatchesSuccess`

Test suite verifying `apply_patches` succeeds: patches applied, deleted from DB, no git commit created, topo order respected, and no-op cascades skip file writes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_applies_single_symbol fingerprint=41394e4b9a39f3cbfc1e37f0e7f7a97244e4bd498ba7cff518df0f2b1c54f445 body_fp=f856e63c60cfc6f20f6edf211ab9830c132f78c3efc08b0eff4bd770472d63ad source_ref=ddb37c0ac4325b2b942f385fddf783792fa16092 -->
## `TestApplyPatchesSuccess.test_applies_single_symbol(self, project: Path)`

Assert that `apply_patches` succeeds and reports at least one file and symbol processed when a single patch exists for `gamma_fn`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_patches_deleted_after_success fingerprint=24be5af6c0b4e62f5f146b8e27210bd9d6650e7c3e129db0fcd9f87274221c7b body_fp=692a20249a3255ef97ac16c162829bbabd82240964f6f45c43b48b095274b672 source_ref=ddb37c0ac4325b2b942f385fddf783792fa16092 -->
## `TestApplyPatchesSuccess.test_patches_deleted_after_success(self, project: Path)`

Assert that `apply_patches` removes all pending patches from the store on successful application.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_no_git_commit_created fingerprint=f2bc664e521f06056a3dce2808add1d4fbb73e45b9cce8e531978eaf89de20ad body_fp=fed4eae8dc554383549067dd547c07eb21005237fa612cd46b4a8ebefc660e22 source_ref=ddb37c0ac4325b2b942f385fddf783792fa16092 -->
## `TestApplyPatchesSuccess.test_no_git_commit_created(self, project: Path)`

Assert that `apply_patches` does not create a git commit after successfully applying a patch.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_applies_in_topo_order fingerprint=83a3756abbd4ab057503ebffbda8d9858b92bb32acc1337a17ec8b865b053b14 body_fp=025d9ddcbd80af7fa97aaf656902d7b0534c78b55960c683afc6ffe9ee4b3db7 source_ref=ddb37c0ac4325b2b942f385fddf783792fa16092 -->
## `TestApplyPatchesSuccess.test_applies_in_topo_order(self, project: Path)`

Assert that `apply_patches` succeeds when a patch targets the deepest callee in an alpha→beta→gamma call chain.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_cascaded_no_change_skips_write fingerprint=923eb26667401b656cfd51d1f0237b3048e0ecc743f1081d52d1d7d9f0f9523b body_fp=f595ee5ac43aa775acb526e6f5e34a49fef9a3b640dc4c9eb204f7ffda2d990d source_ref=ddb37c0ac4325b2b942f385fddf783792fa16092 -->
## `TestApplyPatchesSuccess.test_cascaded_no_change_skips_write(self, project: Path)`

Assert that `apply_patches` leaves cascaded neighbour files unmodified when the LLM returns identical source.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesFailure fingerprint=5ac26c9416b77970ac3457f98df492327a9ece1720de2c8afc2ece3626be42ff body_fp=d54ae9113343e3092e323b3bddfc55b02676218c482bf7d5666bb53f0a461215 source_ref=ddb37c0ac4325b2b942f385fddf783792fa16092 -->
## `TestApplyPatchesFailure`

Test suite for `apply_patches` error-handling: syntax errors, rollback, and patch DB preservation.

- `test_compile_error_returns_failure`: asserts `ok=False`, at least one failed file entry, and a non-null `error` when LLM emits invalid syntax.
- `test_rollback_restores_files`: asserts source files revert to committed state after failure.
- `test_patches_preserved_after_rollback`: asserts patches remain in DB after failure for retry.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesFailure.test_compile_error_returns_failure fingerprint=7b976fafa7a1afc907025f2a67b3d835498e614f830138b4237e1b326f1dc85e body_fp=770d451d75a57a6493d99fbd5ae2ee0209e06881372ce43d49d20765af29a03d source_ref=ddb37c0ac4325b2b942f385fddf783792fa16092 -->
## `TestApplyPatchesFailure.test_compile_error_returns_failure(self, project: Path)`

Assert that `apply_patches` returns `ok=False`, at least one failed file entry, and a non-None `error` when the LLM emits syntactically invalid source.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesFailure.test_rollback_restores_files fingerprint=9c9c2b5d980a1af2036d0ade4a96141ba1d5d81042ef0ee3defc9ee40a3adecf body_fp=e0fe5dbb9728396d86bf4db80ad967527b23a6d0bfb26f005448b46d901978f9 source_ref=ddb37c0ac4325b2b942f385fddf783792fa16092 -->
## `TestApplyPatchesFailure.test_rollback_restores_files(self, project: Path)`

Assert that `apply_patches` restores source files to their committed state after a `BrokenClient`-induced failure.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesFailure.test_patches_preserved_after_rollback fingerprint=1a3f1e74c954f82a8471c620bf35e0f09bcfc22a8ac69d6e9d69acf38ff84ab4 body_fp=99b24f41ae002dbcce9c920109e1b6e75c131690619c23aa1a8cd10b5bfeb4bc source_ref=ddb37c0ac4325b2b942f385fddf783792fa16092 -->
## `TestApplyPatchesFailure.test_patches_preserved_after_rollback(self, project: Path)`

Assert that a failed `apply_patches` call leaves the patch record intact in the database for retry.
<!-- trie:end -->