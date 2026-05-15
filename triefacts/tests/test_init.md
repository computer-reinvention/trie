---
trie_version: 0.1.0
source: tests/test_init.py
file_fingerprint: 0e184c81d9362c7f73da7b478b840c800a1a07a9c74aec22327683a46e1f8beb
last_synced_at: '2026-05-15T13:10:17Z'
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
<!-- trie:section symbol=tests/test_init:python_project fingerprint=3c46e839304076e37baaf33fc2ba0f6ef1d265bd95d3c382ef38e43bab36600e body_fp=0b5748d6ee0c9d175a9a3e74674e120ab0847abcd2baacdf694c4843ff5b9d74 source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `python_project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal `pyproject.toml` in a temp directory and returns the path.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:empty_dir fingerprint=55e26967baf902dc0a8bf6551bb7512f4710c8d3dde4d3799903becb872bb499 body_fp=6d00dc6648976d2b7a181773ca6eccd73403068155c975dd17656f0eedebefea source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `empty_dir(tmp_path: Path) -> Path`

Return an empty temporary directory as a pytest fixture.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_detect_pyproject fingerprint=4c45a248121bb657bbe48576422a5307631c19c084c34cf9e80982c99e328c01 body_fp=1bd24598a8e290f16f3c5674cf3bf17ff105c984019a59120df4d342f6197797 source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_detect_pyproject(python_project: Path)`

Assert `_detect_python_project` returns `["pyproject.toml"]` for a directory containing `pyproject.toml`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_detect_loose_py_files fingerprint=e90cdfa099c11d1f477d766305d7201bf4a4ae4a439fc5a43f834e3c302f33fd body_fp=f8cd25374df7c1433c4c6a39be46f49dcf64428c144e7c5a195dc7fc9d354ff8 source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_detect_loose_py_files(empty_dir: Path)`

Assert `_detect_python_project` returns `["*.py files"]` when the root directory contains a `.py` file.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_detect_one_level_deep_py_files fingerprint=8e52c90d54d44272aa2d159ebcbe0b63f110f5a0cf04f2ce64c285af0910e156 body_fp=397b39a836f23d6b65eea14a40ccfc5ec37f81d701c655db6bdd14a800c9c468 source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_detect_one_level_deep_py_files(empty_dir: Path)`

Verify `_detect_python_project` recognises `*.py` files nested one directory deep.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_detect_returns_empty_for_non_python fingerprint=6d714012a2bcfdf712ad18a26ab684641daeadc4190d82e25a4d928b35712006 body_fp=a95a0485a6e08d48de97435c7389c77120327493047a7fdf2ca55d07319488b8 source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_detect_returns_empty_for_non_python(empty_dir: Path)`

Assert `_detect_python_project` returns an empty list for a directory containing only non-Python files.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_gitignore_creates_when_missing fingerprint=1f4d87462de9b7bdbf611d8698fbc43a86738f978ad30b887af2b4918de50e0d body_fp=c323081dbdb674952eba79e003d3544180fc04a938f180d4ec5181ccc5b265d4 source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_gitignore_creates_when_missing(empty_dir: Path)`

Assert `_ensure_gitignore_entry` creates a new `.gitignore` containing `GITIGNORE_LINE` when none exists.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_gitignore_appends_when_missing_line fingerprint=4edfb60332c83003e3f23a8568441be9d3849cda4943852a54e390bcb4d8c58b body_fp=f05f4fbc00a8b6f0a78b5446dfbd93c4e9de4f96d28bf169eb962aa47c3c9ef4 source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_gitignore_appends_when_missing_line(empty_dir: Path)`

Assert `_ensure_gitignore_entry` appends the trie line to an existing `.gitignore` that lacks it.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_gitignore_no_dup_when_already_present fingerprint=d23d183ba7712f789eb3b07c2286b3c2e05a3bcca0e617da249f0fc190106b2a body_fp=7d74a1173faedd78f63f80c9b46b30e6e97fa84e80a0a8a6a7d3fce65ff588b8 source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_gitignore_no_dup_when_already_present(empty_dir: Path)`

Assert `_ensure_gitignore_entry` returns `False` and does not duplicate `.trie/` when the line already exists.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_gitignore_treats_trailing_slash_as_match fingerprint=4a4f76bafbcc8df0cee594ca8deb071b79390b606e9a0905f9a0b675a6f6d04e body_fp=4a699988f8f7f56c3145bd3b99d5c049e0cd3caa44509a90d47f1f0dcf6fdbcd source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_gitignore_treats_trailing_slash_as_match(empty_dir: Path)`

Verify that `.trie` without a trailing slash is treated as already matching, preventing a duplicate entry.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_gitignore_handles_no_trailing_newline fingerprint=a48d6e36ac66a29e6f7efd70a5ab6c8e0c3b9d55dfc47cc523e3309e2450d809 body_fp=8e7f4413c72bc5688e1b336c1cc410f86e2a42bf315957a3d47b685e9f161035 source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_gitignore_handles_no_trailing_newline(empty_dir: Path)`

Verify `_ensure_gitignore_entry` correctly appends the trie entry when the existing `.gitignore` lacks a trailing newline.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_init_happy_path fingerprint=b86a107b08f2025c14debb7d7fcc47cd753ee00c4e932ef900f9e4658da5f5ea body_fp=cb63d77fa2aab75da8fc618b05db0f7c587aab4919877f6960910e96a18ae67e source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_init_happy_path(python_project: Path)`

Verify `init_project` writes config, creates `.gitignore`, and reports detected markers on a valid Python project.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_init_errors_on_non_python_without_force fingerprint=175132ec9ad82aad871956f864eec5c66355d6bfcebbc0592e4b02b5f5d7f764 body_fp=71533317b0f24808e7c029083c6dac76ad5664556d37a98500d255bdb4da9f12 source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_init_errors_on_non_python_without_force(empty_dir: Path)`

Assert `init_project` raises `InitError` when the directory contains no Python files and `force` is not set.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_init_force_overrides_detection fingerprint=0e7743bfb02091b186cbf1edf0fc412e9e29c88784df204666aae28d8c8bb074 body_fp=83b25ebfc8b171cda0de4e2be99971fb3e76be98f9a49804f9e0a8ee6917338f source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_init_force_overrides_detection(empty_dir: Path)`

Verify that `init_project` with `force=True` succeeds in a non-Python directory.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_init_refuses_overwrite fingerprint=4db7660d8bf07488f7c772980015a065889b8921f1a8506c75e14a2e81f53e5e body_fp=d8f962b7d7df3b9790656a98a9bbab6f857f74a9d982dea84313165d39f824bf source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_init_refuses_overwrite(python_project: Path)`

Assert that `init_project` raises `InitError` matching "already exists" when called twice on the same directory without `force`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_init_force_overwrites fingerprint=866270164c88e6e1aef038e336204617c2de1b1a8802e7cf03b6cf441bf3154b body_fp=29cf7fc58acddbffc9d3a1efbde1b4b82866413667bf8303f47ce80c88276e0f source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_init_force_overwrites(python_project: Path)`

Verify that `init_project` with `force=True` overwrites a tampered `trie.toml` with valid content.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_cli_init_runs fingerprint=ab2e32568377a6f65e5c360ea9ccde1d62a1277e3573a0fa790303b8041b7693 body_fp=94131f33858974724a32bef9d50a4603acd46268d2462e24518cd47f3ebcbab9 source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_cli_init_runs(python_project: Path)`

Verify the `init` CLI command succeeds and writes `trie.toml` for a valid Python project.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_cli_init_errors_on_existing fingerprint=fa25600301629b323b3d18996e88cc8d48dabf1eb750a8da0d4483f05140b0e0 body_fp=27eb0c56569a844be09451f2a8185e68877c0058ed51e54956292fc2e7afcf4f source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_cli_init_errors_on_existing(python_project: Path)`

Assert the CLI exits with code 1 and reports "already exists" when `trie.toml` is already present.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_cli_init_force_succeeds fingerprint=9b36865c88174666eda6c668b5ba26711e69b69ebb8305200bae925c8c8d6fa5 body_fp=e7eb4d0ebca4190d4559e5b6ee6d57c580c59752a42527c98585a441d020fa76 source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_cli_init_force_succeeds(python_project: Path)`

Verify the CLI `init --force` flag exits successfully when `trie.toml` already exists.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_init_runs_scan_by_default fingerprint=24955c7d7458436caac101a5e0c66a9444c6863571676384b0315562ff202e97 body_fp=bfbd3f68c2c3b3b0fe8df4831d74dcce351903ef6c836b065db2edf971f7aa52 source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_init_runs_scan_by_default(python_project: Path)`

Verify that `init_project` runs a scan by default, populating scan stats and creating `graph.db`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_init_no_scan_skips_graph_db fingerprint=8a43923d811342cd52c6745b26f45fe229f5ef19c7f24d1f2de59b0c7fdfc80d body_fp=1452bb05688457c2ea505c7aa059820e39fb857ae95481bf22ec46d1a1b9473f source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_init_no_scan_skips_graph_db(python_project: Path)`

Assert that `init_project` with `run_scan=False` skips scanning and leaves no `graph.db` file.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_install_hook_writes_new_pre_commit_when_git_repo fingerprint=ea202f5549ed284cda7fcdf0c825891eaf4600836200e1a2846c5e4c253e0028 body_fp=be7d561c10497057c2f4900c35ca988748bbedbe31758968359a77e45ee6f325 source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_install_hook_writes_new_pre_commit_when_git_repo(python_project: Path)`

Verify `install_pre_commit_hook` creates an executable pre-commit hook in a new `.git` repo with correct content and marker.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_install_hook_appends_to_existing_pre_commit fingerprint=ab1aa18038215b7dde8e92f583a36876384f058fd046a737eb33efc13757f132 body_fp=b34abf9620c4097c1a161d2fdbb21f1e54998ddb5f6be813f804a76faf7aa43f source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_install_hook_appends_to_existing_pre_commit(python_project: Path)`

Verify that `install_pre_commit_hook` appends trie's hook marker to an existing pre-commit file without removing prior content.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_install_hook_idempotent fingerprint=932f9f174cf0d9107b44558c658efcda9a1f2f0d3d2957e5cac9a264d035a6ed body_fp=60ad3db1356c866bf787d10bec586f9b7798b73746e3aeac864215d0015f2eb6 source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_install_hook_idempotent(python_project: Path)`

Verify that calling `install_pre_commit_hook` twice returns `installed=False` on the second call without error.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_install_hook_skips_when_pre_commit_framework_present fingerprint=8d3cba0514be0b0dcc8b782d996547f4ec7455d48a6444a185182945288ef03f body_fp=9cbea3cce58fd4a1ace2e9a7c09b6ef81c8ad85befb98f782130f312f3c70650 source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_install_hook_skips_when_pre_commit_framework_present(python_project: Path)`

Assert `install_pre_commit_hook` skips installation when `.pre-commit-config.yaml` exists, returning `(False, "framework", None)`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_install_hook_skips_when_not_a_git_repo fingerprint=e1ec9ca6657e1a57abc01cfc0df3ecf1b8a7372169be2bb262b0e43ecb25796b body_fp=08cb4fffeec1faea1bd60772f8701044c071a5150119fbf3c15a8d5ff2934bb6 source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_install_hook_skips_when_not_a_git_repo(python_project: Path)`

Assert that `install_pre_commit_hook` returns `(False, "none", None)` when no `.git` directory exists.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_init_project_install_hooks_in_git_repo fingerprint=5716a2dfe4f721afce56185d6a4fcb00e454fd33a736f545854f7e6dd2024baa body_fp=ae377eca1d317b89d0284f27aaa6f02ac021913c0426227b3a72c21ff47e3381 source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_init_project_install_hooks_in_git_repo(python_project: Path)`

Verify that `init_project` with `install_hooks=True` installs a pre-commit git hook in a git repo.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_init_project_default_does_not_install_hooks fingerprint=08c6aa12b1373f0efa90b2986a651f58d0f606eaa21bd74e09c181faaf89465c body_fp=671b973ad7783a6dbaef4371f8a019a6d8e50dab0d6cd89c3402297cb727ce09 source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_init_project_default_does_not_install_hooks(python_project: Path)`

Assert that `init_project` without `install_hooks=True` leaves hooks uninstalled and sets strategy to `"skipped"`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_cli_init_install_hooks_flag_in_git_repo fingerprint=39007456c6905639e7e061e74c3a64caa550090cb28f73e42319da4cadc04756 body_fp=58da47deda7c1c84186b44f215587e5e8bfba248e7430d37d8cdc272a3550b60 source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_cli_init_install_hooks_flag_in_git_repo(python_project: Path)`

Verify that `trie init --install-hooks` writes a pre-commit hook file and reports success in a git repo.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_cli_init_no_install_hooks_flag_skips fingerprint=3bcfccd46e0dbd0a09ec4459c018efd346d2d22b19bafbab699ef7f53576b401 body_fp=777493fafa6145d1fb108a6b4e79e930bbe55f2f7f9bfd3fb6e43aa681d3ef35 source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_cli_init_no_install_hooks_flag_skips(python_project: Path)`

Assert that `--no-install-hooks` skips pre-commit hook installation, leaving no hook file on disk.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_cli_init_framework_path_prints_snippet fingerprint=e3019388f23b97c17694c0277d5da5a0966c051b358a4d2556b544878b189455 body_fp=633a79a8de3207aff81e3f9f36fe0f2928d233d013376e5beff475492b26a684 source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_cli_init_framework_path_prints_snippet(python_project: Path)`

Assert the CLI prints a `trie-verify` snippet and `.pre-commit-config.yaml` reference when the pre-commit framework is detected.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_cli_init_non_interactive_skips_prompt fingerprint=1a209efb2677a41cc6651c35e4407517de6d2cc3b87c511bfb0ea3b7b999385f body_fp=82cef1fef96a0adf6f22e4edafd78a9e7632eb3f23f64e79de1776c79eb74e44 source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_cli_init_non_interactive_skips_prompt(python_project: Path)`

Assert that `trie init` completes without blocking when no `--install-hooks` flag is given in a non-interactive environment.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_init:test_cli_init_prints_scan_summary fingerprint=b7d2cd4f6fb563c5b409eb18edff4cfe29ddb0ea702ca49ab2ce7d4da427919b body_fp=86d822a960688d9681f8f97b2ef249061bf44a02fd229f7d2cb80791997f5da2 source_ref=317972724bb6a7134623c85cb88c1b5e6573c462 -->
## `test_cli_init_prints_scan_summary(python_project: Path)`

Assert that `trie init` prints a scan summary containing "scanned" and "symbols" after indexing a Python file.
<!-- trie:end -->