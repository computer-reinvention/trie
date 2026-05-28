---
trie_version: 0.1.5
source: tests/test_edits_apply_pipeline.py
file_fingerprint: 0cfd4e179c8e1b74f84dd490244328f8a218db59ccd4fe012bc4ef83dcd35b09
last_synced_at: '2026-05-28T01:48:45Z'
defines:
- kind: module
  qualified_name: tests/test_edits_apply_pipeline:__module__
  lines: 1-356
- kind: constant
  qualified_name: tests/test_edits_apply_pipeline:PROJECT_TOML
  lines: 15-23
- kind: function
  qualified_name: tests/test_edits_apply_pipeline:_git
  lines: 26-27
- kind: function
  qualified_name: tests/test_edits_apply_pipeline:_init_repo
  lines: 30-33
- kind: function
  qualified_name: tests/test_edits_apply_pipeline:_extract_old_source
  lines: 36-49
- kind: function
  qualified_name: tests/test_edits_apply_pipeline:_is_merge_prompt
  lines: 52-53
- kind: function
  qualified_name: tests/test_edits_apply_pipeline:_merge_response
  lines: 56-63
- kind: class
  qualified_name: tests/test_edits_apply_pipeline:FakeTriefactClient
  lines: 66-83
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:FakeTriefactClient.generate
  lines: 72-79
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:FakeTriefactClient.count_tokens
  lines: 82-83
- kind: class
  qualified_name: tests/test_edits_apply_pipeline:FakeEditClient
  lines: 86-110
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:FakeEditClient.generate
  lines: 95-106
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:FakeEditClient.count_tokens
  lines: 109-110
- kind: class
  qualified_name: tests/test_edits_apply_pipeline:PassthroughClient
  lines: 113-152
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:PassthroughClient.generate
  lines: 119-148
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:PassthroughClient.count_tokens
  lines: 151-152
- kind: class
  qualified_name: tests/test_edits_apply_pipeline:BrokenClient
  lines: 155-174
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:BrokenClient.generate
  lines: 161-170
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:BrokenClient.count_tokens
  lines: 173-174
- kind: function
  qualified_name: tests/test_edits_apply_pipeline:project
  lines: 178-231
- kind: class
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesEmpty
  lines: 234-254
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesEmpty.test_no_patches_returns_immediately
  lines: 235-241
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesEmpty.test_git_clean_after_empty_apply
  lines: 243-254
- kind: class
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesSuccess
  lines: 257-320
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_applies_single_symbol
  lines: 258-268
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_patches_deleted_after_success
  lines: 270-279
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_no_git_commit_created
  lines: 281-295
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_applies_in_topo_order
  lines: 297-304
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_cascaded_no_change_skips_write
  lines: 306-320
- kind: class
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesFailure
  lines: 323-355
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesFailure.test_compile_error_returns_failure
  lines: 324-331
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesFailure.test_rollback_restores_files
  lines: 333-344
- kind: method
  qualified_name: tests/test_edits_apply_pipeline:TestApplyPatchesFailure.test_patches_preserved_after_rollback
  lines: 346-355
incoming_refs: 0
outgoing_refs: 56
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
<!-- trie:section symbol=tests/test_edits_apply_pipeline:_is_merge_prompt fingerprint=e7cc8f1f0c76289b339ec77e3a7676a04a827c52723c9dd2603a150b70de9e1a body_fp=0c5733e629303e760b91d045a2c6efdb4c4812255bcf2008f9ffb44ac01d10b7 source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `_is_merge_prompt(request: str) -> bool`

Return `True` if `request` contains the merge-notes marker string.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:_merge_response fingerprint=483c4b97cd7ce365cdc919ded795c72a09fe806de584dd2ad6c6e33e03d62abc body_fp=204f577a6386dce48a59acd0be18a5e8d4d97df14b01d9b6500877e68dfe456c source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `_merge_response() -> GenerationResponse`

Return a static `GenerationResponse` used as the fake LLM reply to merge-notes prompts.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:FakeTriefactClient fingerprint=c6ef4c4cf3bd4a4208297e2d635c4677a3a544191ffc526cf03bb688fef419b3 body_fp=462c9cf3e49349bb4923a8527d5d97340f1847ba711850baafd1f304689ca919 source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `FakeTriefactClient`

Test double LLM client that returns a fixed triefact body for use with `sync_single_file`.

- `generate`: always returns a static `"## Symbol\n\nAuto-generated prose.\n"` response.
- `count_tokens`: always returns 100.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:FakeTriefactClient.generate fingerprint=857c836926411795af89467eb90081050a909c660a69f8d05dfb21f49d2c37d8 body_fp=478b5337887f46115f1784715866c8c0eebdd07a503821aa20b3bfb77f057dd7 source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `FakeTriefactClient.generate(req: GenerationRequest) -> GenerationResponse`

Return a static `GenerationResponse` with fixed prose for any `FakeTriefactClient` generation request.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:FakeTriefactClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=b942b2a9557a3dd9792538e03984def6dd4cf6dcccb6a0f3e5e7157efa0e0141 source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `FakeTriefactClient.count_tokens(_req: GenerationRequest) -> int`

Always return 100 for any `FakeTriefactClient` token-count request.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:FakeEditClient fingerprint=e6b867c3dc7441d6ee7ea1a0c9a7c1c97373b5d2cb55c08dd6932ec8dd1199b3 body_fp=35a4b1c7b4cf8dc94bc1647a5137bf2d037c4f956ed61966994b688b48b9e674 source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `FakeEditClient`

LLM test double for patch-apply calls that appends `# patch-applied` to source or returns a static merge response.

- `generate`: returns merge response for merge prompts; otherwise appends `# patch-applied` to extracted source.
- `count_tokens`: always returns `100`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:FakeEditClient.generate fingerprint=920fc59179e4790f1bc9623e954869323f93a7a0c8cb64099ff3c5ce5388fcb7 body_fp=9070e6acfd8e76c3c8e254fd00ddf1c8faca46540d83d60e4d626b8306a67c66 source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `FakeEditClient.generate(req: GenerationRequest) -> GenerationResponse`

Simulate `FakeEditClient` LLM response, appending `# patch-applied` to extracted source or returning a merge response.

- For merge prompts, delegates to `_merge_response()`.
- Otherwise, appends `\n# patch-applied` to the extracted old source and wraps it with prose.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:FakeEditClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=225d1aad76912b5124f832c0497ed893289f3318fd2c776a7a81c9a3bd3028a7 source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `FakeEditClient.count_tokens(_req: GenerationRequest) -> int`

Always return 100 for any `FakeEditClient` token-count request.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:PassthroughClient fingerprint=51dd8936db16a90332c501e2d9b323b847cf85c5c157809b4ecdc56a140b5e84 body_fp=a592d3d7d7f2d3afe41807847de06ce27c8d535fae15447d1d2b77069d010f4f source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `PassthroughClient`

LLM test double that returns the extracted old source and prose verbatim, unchanged.

- `generate`: returns merge response for merge prompts; otherwise echoes extracted source and prose.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:PassthroughClient.generate fingerprint=888e5c3d32868c3d270f0ae3b93c35c919010b08a9ad111a4dc58fcbf3d22b3e body_fp=b0dee53736e645f87108a878b3f163770181b80ac05717c3efb6cab0900ec395 source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `PassthroughClient.generate(req: GenerationRequest) -> GenerationResponse`

Echo the original source and prose from `req` back unchanged, or return a static merge response for merge prompts.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:PassthroughClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=5e76d16fdf07755c8c6f2605ffb0f37902955e777cee60d33004dd835e6496b2 source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `PassthroughClient.count_tokens(_req: GenerationRequest) -> int`

Return a fixed token count of 100 for any `PassthroughClient` request.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:BrokenClient fingerprint=fb0101b67ab373fc7321d9a16743a6af6768ecd74e9864ca63bd6b6ee1e187ff body_fp=fc586e19c701a330782a5252e56bfa57ee80d7a05d6c7534a2571ca5cb81685e source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `BrokenClient`

Fake LLM client that always returns syntactically invalid Python source to trigger compile-error failure paths.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:BrokenClient.generate fingerprint=6749133bad2c81e9f6d0340206d75b0b881745fd4bc7a4554a569a04f5312a6d body_fp=fce5fe922ff84077cc97f28555a21c3bbef1e8ec626e997089dc7788c44573a4 source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `BrokenClient.generate(req: GenerationRequest) -> GenerationResponse`

Return a syntactically invalid Python source block for any non-merge `GenerationRequest`.
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
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesEmpty fingerprint=d5d453264c31545e04928781f7b0ca8d421448c0243758bed2c08af92c26526b body_fp=ca1a1975b479e525bdfe54040a46fd27fa1629911f7fb6601a2e04e10dfb8ad4 source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `TestApplyPatchesEmpty`

Test `apply_patches` behaviour when no patches are pending in the store.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesEmpty.test_no_patches_returns_immediately fingerprint=bfaad18d0b3e7e96a1a6413424f858b5ca78506eb09328de6a8e455074452d7f body_fp=baf48e08c2f33c5a7032a322612c7624845a08d147b9db95b2eac3c37779289d source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `TestApplyPatchesEmpty.test_no_patches_returns_immediately(self, project: Path)`

Assert `apply_patches` returns `ok=True`, `applied=0`, `failed=0` when no patches exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesEmpty.test_git_clean_after_empty_apply fingerprint=c5893657f0aed624008309b981a1fddcbad56f7dc907a8310567dda75f8b7c68 body_fp=a10d0bd998c47708673c76627a398f7ab41f51b1f83f881c36366cf875167577 source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `TestApplyPatchesEmpty.test_git_clean_after_empty_apply(self, project: Path)`

Assert the working tree has no uncommitted changes after `apply_patches` runs with no pending patches.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesSuccess fingerprint=bbadd08789f92d475873ea3e00f600e06af88c77ddc9297dbe304c45e40b830d body_fp=63bec6a76ecbf4c79f8525cad07e938548c4823d8457c265247885f36e083b45 source_ref=d0b01151af5169a7474ad73c4f11a1077fd70dc4 -->
## `TestApplyPatchesSuccess`

Test suite verifying `apply_patches` succeeds: patches applied, deleted from DB, no git commit created, topo order respected, and no-op cascades skip file writes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_applies_single_symbol fingerprint=b08ec7ef325ae3df513d11e04cf00ba4af49f4a6183a3963c550d1a8dfd97719 body_fp=95362d497548b2ffdc60f43e5287b92e21a382af96257a7838fd7cd259e5812c source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `TestApplyPatchesSuccess.test_applies_single_symbol(self, project: Path)`

Assert that `apply_patches` succeeds and reports at least one applied patch when a single patch exists for `gamma_fn`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_patches_deleted_after_success fingerprint=24be5af6c0b4e62f5f146b8e27210bd9d6650e7c3e129db0fcd9f87274221c7b body_fp=692a20249a3255ef97ac16c162829bbabd82240964f6f45c43b48b095274b672 source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `TestApplyPatchesSuccess.test_patches_deleted_after_success(self, project: Path)`

Assert that `apply_patches` removes all pending patches from the store on successful application.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_no_git_commit_created fingerprint=f2bc664e521f06056a3dce2808add1d4fbb73e45b9cce8e531978eaf89de20ad body_fp=fed4eae8dc554383549067dd547c07eb21005237fa612cd46b4a8ebefc660e22 source_ref=d0b01151af5169a7474ad73c4f11a1077fd70dc4 -->
## `TestApplyPatchesSuccess.test_no_git_commit_created(self, project: Path)`

Assert that `apply_patches` does not create a git commit after successfully applying a patch.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_applies_in_topo_order fingerprint=83a3756abbd4ab057503ebffbda8d9858b92bb32acc1337a17ec8b865b053b14 body_fp=025d9ddcbd80af7fa97aaf656902d7b0534c78b55960c683afc6ffe9ee4b3db7 source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `TestApplyPatchesSuccess.test_applies_in_topo_order(self, project: Path)`

Assert that `apply_patches` succeeds when a patch targets the deepest callee in an alpha→beta→gamma call chain.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesSuccess.test_cascaded_no_change_skips_write fingerprint=7f32f521c96c6440394d238e1bd039b186d3d390b6554d3143f19a1e073825c2 body_fp=f595ee5ac43aa775acb526e6f5e34a49fef9a3b640dc4c9eb204f7ffda2d990d source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `TestApplyPatchesSuccess.test_cascaded_no_change_skips_write(self, project: Path)`

Assert that `apply_patches` leaves cascaded neighbour files unmodified when the LLM returns identical source.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesFailure fingerprint=c8f20dd0e194f101835c92c7f149ada4e73af533374629d1cbe5fe872d96913f body_fp=b12fdaedf69ce28e0cac5f534f29d6287f50d048c19fbcd681245d948316cba8 source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `TestApplyPatchesFailure`

Test suite for `apply_patches` error-handling: syntax errors, rollback, and patch DB preservation.

- `test_compile_error_returns_failure`: asserts `ok=False` and `failed≥1` when LLM emits invalid syntax.
- `test_rollback_restores_files`: asserts source files revert to committed state after failure.
- `test_patches_preserved_after_rollback`: asserts patches remain in DB after failure for retry.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesFailure.test_compile_error_returns_failure fingerprint=87da20b4408f6ec1ea5afb45fc56635cb8a4c5d472e6fbf436304dffab1e41a5 body_fp=0128a6b74b6deabbdd3063eaf1a2db844c474966bd61ace2e820c80f84750eb1 source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `TestApplyPatchesFailure.test_compile_error_returns_failure(self, project: Path)`

Assert that `apply_patches` returns `ok=False` and `failed>=1` when the LLM emits syntactically invalid source.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesFailure.test_rollback_restores_files fingerprint=9c9c2b5d980a1af2036d0ade4a96141ba1d5d81042ef0ee3defc9ee40a3adecf body_fp=e0fe5dbb9728396d86bf4db80ad967527b23a6d0bfb26f005448b46d901978f9 source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `TestApplyPatchesFailure.test_rollback_restores_files(self, project: Path)`

Assert that `apply_patches` restores source files to their committed state after a `BrokenClient`-induced failure.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_edits_apply_pipeline:TestApplyPatchesFailure.test_patches_preserved_after_rollback fingerprint=1a3f1e74c954f82a8471c620bf35e0f09bcfc22a8ac69d6e9d69acf38ff84ab4 body_fp=99b24f41ae002dbcce9c920109e1b6e75c131690619c23aa1a8cd10b5bfeb4bc source_ref=1cd5cf31fd04c06ef688ceea497dfd197600810e -->
## `TestApplyPatchesFailure.test_patches_preserved_after_rollback(self, project: Path)`

Assert that a failed `apply_patches` call leaves the patch record intact in the database for retry.
<!-- trie:end -->