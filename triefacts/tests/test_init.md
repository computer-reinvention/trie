---
trie_version: 0.1.0
source: tests/test_init.py
file_fingerprint: 0e184c81d9362c7f73da7b478b840c800a1a07a9c74aec22327683a46e1f8beb
last_synced_at: '2026-05-12T18:17:21Z'
defines:
- kind: function
  qualified_name: tests/test_init:python_project
  lines: 21-23
- kind: function
  qualified_name: tests/test_init:empty_dir
  lines: 27-28
- kind: function
  qualified_name: tests/test_init:test_detect_pyproject
  lines: 34-35
- kind: function
  qualified_name: tests/test_init:test_detect_loose_py_files
  lines: 38-40
- kind: function
  qualified_name: tests/test_init:test_detect_one_level_deep_py_files
  lines: 43-46
- kind: function
  qualified_name: tests/test_init:test_detect_returns_empty_for_non_python
  lines: 49-51
- kind: function
  qualified_name: tests/test_init:test_gitignore_creates_when_missing
  lines: 57-60
- kind: function
  qualified_name: tests/test_init:test_gitignore_appends_when_missing_line
  lines: 63-67
- kind: function
  qualified_name: tests/test_init:test_gitignore_no_dup_when_already_present
  lines: 70-74
- kind: function
  qualified_name: tests/test_init:test_gitignore_treats_trailing_slash_as_match
  lines: 77-80
- kind: function
  qualified_name: tests/test_init:test_gitignore_handles_no_trailing_newline
  lines: 83-89
- kind: function
  qualified_name: tests/test_init:test_init_happy_path
  lines: 95-101
- kind: function
  qualified_name: tests/test_init:test_init_errors_on_non_python_without_force
  lines: 104-107
- kind: function
  qualified_name: tests/test_init:test_init_force_overrides_detection
  lines: 110-113
- kind: function
  qualified_name: tests/test_init:test_init_refuses_overwrite
  lines: 116-119
- kind: function
  qualified_name: tests/test_init:test_init_force_overwrites
  lines: 122-126
- kind: function
  qualified_name: tests/test_init:test_cli_init_runs
  lines: 132-137
- kind: function
  qualified_name: tests/test_init:test_cli_init_errors_on_existing
  lines: 140-145
- kind: function
  qualified_name: tests/test_init:test_cli_init_force_succeeds
  lines: 148-152
- kind: function
  qualified_name: tests/test_init:test_init_runs_scan_by_default
  lines: 158-164
- kind: function
  qualified_name: tests/test_init:test_init_no_scan_skips_graph_db
  lines: 167-171
- kind: function
  qualified_name: tests/test_init:test_install_hook_writes_new_pre_commit_when_git_repo
  lines: 177-189
- kind: function
  qualified_name: tests/test_init:test_install_hook_appends_to_existing_pre_commit
  lines: 192-203
- kind: function
  qualified_name: tests/test_init:test_install_hook_idempotent
  lines: 206-211
- kind: function
  qualified_name: tests/test_init:test_install_hook_skips_when_pre_commit_framework_present
  lines: 214-220
- kind: function
  qualified_name: tests/test_init:test_install_hook_skips_when_not_a_git_repo
  lines: 223-227
- kind: function
  qualified_name: tests/test_init:test_init_project_install_hooks_in_git_repo
  lines: 233-238
- kind: function
  qualified_name: tests/test_init:test_init_project_default_does_not_install_hooks
  lines: 241-245
- kind: function
  qualified_name: tests/test_init:test_cli_init_install_hooks_flag_in_git_repo
  lines: 251-257
- kind: function
  qualified_name: tests/test_init:test_cli_init_no_install_hooks_flag_skips
  lines: 260-265
- kind: function
  qualified_name: tests/test_init:test_cli_init_framework_path_prints_snippet
  lines: 268-275
- kind: function
  qualified_name: tests/test_init:test_cli_init_non_interactive_skips_prompt
  lines: 278-282
- kind: function
  qualified_name: tests/test_init:test_cli_init_prints_scan_summary
  lines: 285-291
incoming_refs: 0
outgoing_refs: 27
---
<!-- trie:section symbol=tests/test_init:python_project fingerprint=3c46e839304076e37baaf33fc2ba0f6ef1d265bd95d3c382ef38e43bab36600e body_fp=dc9df52605e96c8fee8ae6c80f22404f639e9f869f1027be8a798035b2b4477f -->
## `python_project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal `pyproject.toml` in a temporary directory and returns its path.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:empty_dir fingerprint=55e26967baf902dc0a8bf6551bb7512f4710c8d3dde4d3799903becb872bb499 body_fp=6d00dc6648976d2b7a181773ca6eccd73403068155c975dd17656f0eedebefea -->
## `empty_dir(tmp_path: Path) -> Path`

Return an empty temporary directory as a pytest fixture.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_detect_pyproject fingerprint=4c45a248121bb657bbe48576422a5307631c19c084c34cf9e80982c99e328c01 body_fp=1bd24598a8e290f16f3c5674cf3bf17ff105c984019a59120df4d342f6197797 -->
## `test_detect_pyproject(python_project: Path)`

Assert `_detect_python_project` returns `["pyproject.toml"]` for a directory containing `pyproject.toml`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_detect_loose_py_files fingerprint=e90cdfa099c11d1f477d766305d7201bf4a4ae4a439fc5a43f834e3c302f33fd body_fp=bd67ee4d888e8ba3b522665bfaf58170ceddddb5f8dc66f8ebb50fc5f1ae977a -->
## `test_detect_loose_py_files(empty_dir: Path)`

Assert that `_detect_python_project` returns `["*.py files"]` when loose `.py` files exist directly in the directory.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_detect_one_level_deep_py_files fingerprint=8e52c90d54d44272aa2d159ebcbe0b63f110f5a0cf04f2ce64c285af0910e156 body_fp=397b39a836f23d6b65eea14a40ccfc5ec37f81d701c655db6bdd14a800c9c468 -->
## `test_detect_one_level_deep_py_files(empty_dir: Path)`

Verify `_detect_python_project` recognises `*.py` files nested one directory deep.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_detect_returns_empty_for_non_python fingerprint=6d714012a2bcfdf712ad18a26ab684641daeadc4190d82e25a4d928b35712006 body_fp=a95a0485a6e08d48de97435c7389c77120327493047a7fdf2ca55d07319488b8 -->
## `test_detect_returns_empty_for_non_python(empty_dir: Path)`

Assert `_detect_python_project` returns an empty list for a directory containing only non-Python files.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_gitignore_creates_when_missing fingerprint=1f4d87462de9b7bdbf611d8698fbc43a86738f978ad30b887af2b4918de50e0d body_fp=a0189504492373b78907bf794e5edc6691f9b9fd9b502356ac02ce3e3332fa32 -->
## `test_gitignore_creates_when_missing(empty_dir: Path)`

Assert that `_ensure_gitignore_entry` creates a new `.gitignore` containing `GITIGNORE_LINE` when no file exists.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_gitignore_appends_when_missing_line fingerprint=4edfb60332c83003e3f23a8568441be9d3849cda4943852a54e390bcb4d8c58b body_fp=f05f4fbc00a8b6f0a78b5446dfbd93c4e9de4f96d28bf169eb962aa47c3c9ef4 -->
## `test_gitignore_appends_when_missing_line(empty_dir: Path)`

Assert `_ensure_gitignore_entry` appends the trie line to an existing `.gitignore` that lacks it.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_gitignore_no_dup_when_already_present fingerprint=d23d183ba7712f789eb3b07c2286b3c2e05a3bcca0e617da249f0fc190106b2a body_fp=5191bdcc0332e996ca5ee723b62e91a4ffbd4d7d3221f0049bec985dd6971389 -->
## `test_gitignore_no_dup_when_already_present(empty_dir: Path)`

Assert `_ensure_gitignore_entry` returns `False` and does not duplicate an already-present `.trie/` entry.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_gitignore_treats_trailing_slash_as_match fingerprint=4a4f76bafbcc8df0cee594ca8deb071b79390b606e9a0905f9a0b675a6f6d04e body_fp=cfe22e9c61d9c3c71e6a20667c545a7646a48140cef94732d67c8ad5b22ba5a4 -->
## `test_gitignore_treats_trailing_slash_as_match(empty_dir: Path)`

Verify that `.trie` without a trailing slash is treated as already matching the `.trie/` gitignore entry.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_gitignore_handles_no_trailing_newline fingerprint=a48d6e36ac66a29e6f7efd70a5ab6c8e0c3b9d55dfc47cc523e3309e2450d809 body_fp=60a8e390848bf3a200fc49f975d6368b1dc63818d1c2f36996ad78687c5b827b -->
## `test_gitignore_handles_no_trailing_newline(empty_dir: Path)`

Verify `_ensure_gitignore_entry` appends correctly when the existing `.gitignore` lacks a trailing newline.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_init_happy_path fingerprint=b86a107b08f2025c14debb7d7fcc47cd753ee00c4e932ef900f9e4658da5f5ea body_fp=09ad167730b962bb4a952a925ac8bac0242385014fea76b11a6ec88aac691346 -->
## `test_init_happy_path(python_project: Path)`

Verify `init_project` writes config, creates `.gitignore`, and detects `pyproject.toml` in a valid Python project.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_init_errors_on_non_python_without_force fingerprint=175132ec9ad82aad871956f864eec5c66355d6bfcebbc0592e4b02b5f5d7f764 body_fp=caef84ddf91442641efda82d4daf6710b588de6ebac80e4c471f99ca4f987e1f -->
## `test_init_errors_on_non_python_without_force(empty_dir: Path)`

Assert `init_project` raises `InitError` when the directory contains no Python markers and `force` is not set.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_init_force_overrides_detection fingerprint=0e7743bfb02091b186cbf1edf0fc412e9e29c88784df204666aae28d8c8bb074 body_fp=ad8264b12af110b02cc686a70688e6658f95c81e414b991270e21b713c8ff272 -->
## `test_init_force_overrides_detection(empty_dir: Path)`

Verify that `force=True` allows `init_project` to succeed in a non-Python directory.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_init_refuses_overwrite fingerprint=4db7660d8bf07488f7c772980015a065889b8921f1a8506c75e14a2e81f53e5e body_fp=dad0684dd8c1cecb4572274c8871876a89e138b8749ae7a395d3a63d09975f13 -->
## `test_init_refuses_overwrite(python_project: Path)`

Assert that calling `init_project` twice on the same directory raises `InitError` matching "already exists".
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_init_force_overwrites fingerprint=866270164c88e6e1aef038e336204617c2de1b1a8802e7cf03b6cf441bf3154b body_fp=29cf7fc58acddbffc9d3a1efbde1b4b82866413667bf8303f47ce80c88276e0f -->
## `test_init_force_overwrites(python_project: Path)`

Verify that `init_project` with `force=True` overwrites a tampered `trie.toml` with valid content.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_cli_init_runs fingerprint=ab2e32568377a6f65e5c360ea9ccde1d62a1277e3573a0fa790303b8041b7693 body_fp=7b12935ee92123b10820278ffb0779a0d20638338db4cf99fcfda36001682da0 -->
## `test_cli_init_runs(python_project: Path)`

Verify the CLI `init` command exits 0, prints "wrote", and creates `trie.toml`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_cli_init_errors_on_existing fingerprint=fa25600301629b323b3d18996e88cc8d48dabf1eb750a8da0d4483f05140b0e0 body_fp=16c7b0d37b0422a79688fdbbe5fd6c585f0ea4cfa8698019402bb59086d0cf62 -->
## `test_cli_init_errors_on_existing(python_project: Path)`

Assert the CLI exits with code 1 and reports "already exists" when `trie.toml` is present.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_cli_init_force_succeeds fingerprint=9b36865c88174666eda6c668b5ba26711e69b69ebb8305200bae925c8c8d6fa5 body_fp=eb2e7d05f8987ca1c6b12a08ba1275851f68b1223d58ec4f5c01868cb8ca8ae3 -->
## `test_cli_init_force_succeeds(python_project: Path)`

Verify that `trie init --force` exits successfully when `trie.toml` already exists.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_init_runs_scan_by_default fingerprint=24955c7d7458436caac101a5e0c66a9444c6863571676384b0315562ff202e97 body_fp=c43b06abaea7ff04c1f511f9a557392d209e5072e067d8b03aef06a2ed0665ed -->
## `test_init_runs_scan_by_default(python_project: Path)`

Verify that `init_project` scans source files and writes `graph.db` by default.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_init_no_scan_skips_graph_db fingerprint=8a43923d811342cd52c6745b26f45fe229f5ef19c7f24d1f2de59b0c7fdfc80d body_fp=8868dddbbc270a8a6e8d926ccd07df9d8c19a24df45306d95ecd39f984f70573 -->
## `test_init_no_scan_skips_graph_db(python_project: Path)`

Assert that `init_project` with `run_scan=False` leaves `scan_ran` false and does not create `graph.db`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_install_hook_writes_new_pre_commit_when_git_repo fingerprint=ea202f5549ed284cda7fcdf0c825891eaf4600836200e1a2846c5e4c253e0028 body_fp=25ffcdb3b3a126149e98c87fd67dee65da6d4e99768d2e49d1462af19ead1300 -->
## `test_install_hook_writes_new_pre_commit_when_git_repo(python_project: Path)`

Verify that `install_pre_commit_hook` creates an executable pre-commit hook in a new `.git` repo.

- Asserts `strategy == "git_hook"` and hook file contains the marker and `trie -q verify`.
- Checks the hook file has the user-executable bit set.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_install_hook_appends_to_existing_pre_commit fingerprint=ab1aa18038215b7dde8e92f583a36876384f058fd046a737eb33efc13757f132 body_fp=568ec2e76f5ee529ce58d473b059f368d51b1cc711f9af0ccbd4d8917b828c94 -->
## `test_install_hook_appends_to_existing_pre_commit(python_project: Path)`

Verify that `install_pre_commit_hook` appends trie's marker to a pre-existing pre-commit hook without removing existing content.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_install_hook_idempotent fingerprint=932f9f174cf0d9107b44558c658efcda9a1f2f0d3d2957e5cac9a264d035a6ed body_fp=7fa52f515d85864c52bc1ab67ab64afc0bd1d442fa8b3e49bc70edd0c38ba0e7 -->
## `test_install_hook_idempotent(python_project: Path)`

Assert that calling `install_pre_commit_hook` twice returns `installed=False` on the second call without error.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_install_hook_skips_when_pre_commit_framework_present fingerprint=8d3cba0514be0b0dcc8b782d996547f4ec7455d48a6444a185182945288ef03f body_fp=7c8b056905953163821d71235f310d5e27f38df3e324dcf152566a1737b7a885 -->
## `test_install_hook_skips_when_pre_commit_framework_present(python_project: Path)`

Assert that `install_pre_commit_hook` skips installation when `.pre-commit-config.yaml` exists, returning `(False, "framework", None)`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_install_hook_skips_when_not_a_git_repo fingerprint=e1ec9ca6657e1a57abc01cfc0df3ecf1b8a7372169be2bb262b0e43ecb25796b body_fp=340f21fd5fbbc9fa65e9af394c201e65ad9382e36b83a9d19ec595c017678fb7 -->
## `test_install_hook_skips_when_not_a_git_repo(python_project: Path)`

Assert `install_pre_commit_hook` returns `(False, "none", None)` when no `.git` directory exists.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_init_project_install_hooks_in_git_repo fingerprint=5716a2dfe4f721afce56185d6a4fcb00e454fd33a736f545854f7e6dd2024baa body_fp=dada8b7884622e08ad35a1d6c84a0598c86831c0e0e2ceb1249bb9c4d7354e5a -->
## `test_init_project_install_hooks_in_git_repo(python_project: Path)`

Verify that `init_project` with `install_hooks=True` writes a pre-commit hook in a git repo.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_init_project_default_does_not_install_hooks fingerprint=08c6aa12b1373f0efa90b2986a651f58d0f606eaa21bd74e09c181faaf89465c body_fp=671b973ad7783a6dbaef4371f8a019a6d8e50dab0d6cd89c3402297cb727ce09 -->
## `test_init_project_default_does_not_install_hooks(python_project: Path)`

Assert that `init_project` without `install_hooks=True` leaves hooks uninstalled and sets strategy to `"skipped"`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_cli_init_install_hooks_flag_in_git_repo fingerprint=39007456c6905639e7e061e74c3a64caa550090cb28f73e42319da4cadc04756 body_fp=58da47deda7c1c84186b44f215587e5e8bfba248e7430d37d8cdc272a3550b60 -->
## `test_cli_init_install_hooks_flag_in_git_repo(python_project: Path)`

Verify that `trie init --install-hooks` writes a pre-commit hook file and reports success in a git repo.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_cli_init_no_install_hooks_flag_skips fingerprint=3bcfccd46e0dbd0a09ec4459c018efd346d2d22b19bafbab699ef7f53576b401 body_fp=6205b1797968e41941cbf7130112a8719c9137dd7ff6c121950c51503a1849ae -->
## `test_cli_init_no_install_hooks_flag_skips(python_project: Path)`

Verify that `--no-install-hooks` prevents pre-commit hook creation in a git repo.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_cli_init_framework_path_prints_snippet fingerprint=e3019388f23b97c17694c0277d5da5a0966c051b358a4d2556b544878b189455 body_fp=35f90f3ee2ff372f6a689b023794b6ea01317c03a1eb91f26283137bf069fbc1 -->
## `test_cli_init_framework_path_prints_snippet(python_project: Path)`

Assert that `trie init --install-hooks` prints a `.pre-commit-config.yaml` snippet when the pre-commit framework is detected.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_cli_init_non_interactive_skips_prompt fingerprint=1a209efb2677a41cc6651c35e4407517de6d2cc3b87c511bfb0ea3b7b999385f body_fp=13ed6e6ae034f2b2714bdcf67e704335f147961c87b2f61a37a58cb55875e686 -->
## `test_cli_init_non_interactive_skips_prompt(python_project: Path)`

Verify that `trie init` completes without blocking when run non-interactively and `--install-hooks` is omitted.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_cli_init_prints_scan_summary fingerprint=b7d2cd4f6fb563c5b409eb18edff4cfe29ddb0ea702ca49ab2ce7d4da427919b body_fp=c753ef7e0a4c374a3421140a0be2d673e4c122f7f82208c943cdd4506e1ac678 -->
## `test_cli_init_prints_scan_summary(python_project: Path)`

Assert the CLI `init` command prints scan summary lines containing "scanned" and "symbols".
<!-- trie:end -->