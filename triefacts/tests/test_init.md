---
trie_version: 0.1.2
source: tests/test_init.py
file_fingerprint: e2a72c51fe1f6c7144b6c823ed90adfd1fec4a364d2a34324f3f9196a5a28861
last_synced_at: '2026-05-23T23:25:04Z'
defines:
- kind: module
  qualified_name: tests/test_init:__module__
  lines: 1-382
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
  lines: 177-195
- kind: function
  qualified_name: tests/test_init:test_install_hook_appends_to_existing_pre_commit
  lines: 198-209
- kind: function
  qualified_name: tests/test_init:test_install_hook_idempotent
  lines: 212-217
- kind: function
  qualified_name: tests/test_init:test_install_hook_skips_when_pre_commit_framework_present
  lines: 220-226
- kind: function
  qualified_name: tests/test_init:test_install_hook_skips_when_not_a_git_repo
  lines: 229-233
- kind: function
  qualified_name: tests/test_init:test_init_project_install_hooks_in_git_repo
  lines: 239-244
- kind: function
  qualified_name: tests/test_init:test_init_project_default_does_not_install_hooks
  lines: 247-251
- kind: function
  qualified_name: tests/test_init:test_cli_init_install_hooks_flag_in_git_repo
  lines: 257-263
- kind: function
  qualified_name: tests/test_init:test_cli_init_no_install_hooks_flag_skips
  lines: 266-271
- kind: function
  qualified_name: tests/test_init:test_cli_init_framework_path_prints_snippet
  lines: 274-281
- kind: function
  qualified_name: tests/test_init:test_cli_init_non_interactive_skips_prompt
  lines: 284-288
- kind: function
  qualified_name: tests/test_init:test_cli_init_prints_scan_summary
  lines: 291-297
- kind: function
  qualified_name: tests/test_init:test_cli_init_prints_setup_instruction_in_next_steps
  lines: 305-314
- kind: function
  qualified_name: tests/test_init:test_cli_init_does_not_run_setup_in_non_interactive_env
  lines: 317-332
- kind: function
  qualified_name: tests/test_init:test_cli_init_runs_setup_when_user_accepts_prompt
  lines: 335-359
- kind: function
  qualified_name: tests/test_init:test_cli_init_does_not_run_setup_when_user_declines_prompt
  lines: 362-381
incoming_refs: 0
outgoing_refs: 39
---
<!-- trie:section symbol=tests/test_init:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=0c0e05b67525022c46a3ade1f7f009ff794ba8a982b3447ce1f8f4786cffab4a source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `tests/test_init`

Test suite for `trie.init` project initialisation, gitignore management, pre-commit hook installation, and related CLI commands.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:python_project fingerprint=3c46e839304076e37baaf33fc2ba0f6ef1d265bd95d3c382ef38e43bab36600e body_fp=d4e2862bc5c2216ec3a2ffc4c782480937013509c4811fa85587d15e27907c5f source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `python_project(tmp_path: Path) -> Path`

Pytest fixture providing a temporary directory with a minimal `pyproject.toml`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:empty_dir fingerprint=55e26967baf902dc0a8bf6551bb7512f4710c8d3dde4d3799903becb872bb499 body_fp=ee9c04c6de06ff71b2643568d39ce79682cba70efedf37ba8b8d1e01ceb86f67 source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `empty_dir(tmp_path: Path) -> Path`

Pytest fixture providing a temporary empty directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_detect_pyproject fingerprint=4c45a248121bb657bbe48576422a5307631c19c084c34cf9e80982c99e328c01 body_fp=4da36578ddce649297e12b877b778b42cb3f603dbaa2772eec449902d7be396d source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_detect_pyproject(python_project: Path)`

Assert `_detect_python_project` returns `["pyproject.toml"]` when a `pyproject.toml` exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_detect_loose_py_files fingerprint=e90cdfa099c11d1f477d766305d7201bf4a4ae4a439fc5a43f834e3c302f33fd body_fp=9e674888c5bece4c1618514779b2abe511d52f13df6d30db46f091ce7f55f0da source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_detect_loose_py_files(empty_dir: Path)`

Assert that `_detect_python_project` returns `["*.py files"]` when the directory contains a top-level `.py` file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_detect_one_level_deep_py_files fingerprint=8e52c90d54d44272aa2d159ebcbe0b63f110f5a0cf04f2ce64c285af0910e156 body_fp=b5e36e3a5c0caaa1c25e3a3fe2592fb877f4d82ee930864c78249f4b4f0b83cf source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_detect_one_level_deep_py_files(empty_dir: Path)`

Verify `_detect_python_project` detects `*.py` files nested one directory deep.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_detect_returns_empty_for_non_python fingerprint=6d714012a2bcfdf712ad18a26ab684641daeadc4190d82e25a4d928b35712006 body_fp=a95a0485a6e08d48de97435c7389c77120327493047a7fdf2ca55d07319488b8 source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_detect_returns_empty_for_non_python(empty_dir: Path)`

Assert `_detect_python_project` returns an empty list for a directory containing only non-Python files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_gitignore_creates_when_missing fingerprint=1f4d87462de9b7bdbf611d8698fbc43a86738f978ad30b887af2b4918de50e0d body_fp=308d0011ac4c75d7bbd640c47048e4e219aec68d8b62acb821606f09d505631a source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_gitignore_creates_when_missing(empty_dir: Path)`

Assert `_ensure_gitignore_entry` creates a new `.gitignore` containing `.trie/\n` when no file exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_gitignore_appends_when_missing_line fingerprint=4edfb60332c83003e3f23a8568441be9d3849cda4943852a54e390bcb4d8c58b body_fp=d7d2d1c9c97efd4c7c68b307516a534efd6890cd1b55303e9bdf1a7868eba7ed source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_gitignore_appends_when_missing_line(empty_dir: Path)`

Verify `_ensure_gitignore_entry` appends `.trie/` to an existing `.gitignore` that lacks it.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_gitignore_no_dup_when_already_present fingerprint=d23d183ba7712f789eb3b07c2286b3c2e05a3bcca0e617da249f0fc190106b2a body_fp=bf418e5be0b904173e5ba1777ee74a0ce0ed1c503c5abd5d9157a2a264b0e34f source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_gitignore_no_dup_when_already_present(empty_dir: Path)`

Assert `_ensure_gitignore_entry` returns `False` and writes no duplicate when the entry already exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_gitignore_treats_trailing_slash_as_match fingerprint=4a4f76bafbcc8df0cee594ca8deb071b79390b606e9a0905f9a0b675a6f6d04e body_fp=6f8d45a46595692777d4e9b3347257ad6bff15d1ca00b90bebc1b7bfc68bb2c4 source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_gitignore_treats_trailing_slash_as_match(empty_dir: Path)`

Verify `_ensure_gitignore_entry` treats `.trie` (no trailing slash) as an existing match for `.trie/`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_gitignore_handles_no_trailing_newline fingerprint=a48d6e36ac66a29e6f7efd70a5ab6c8e0c3b9d55dfc47cc523e3309e2450d809 body_fp=3c543cec0c4d96f43819a2a963686d819c3b1729641dc6561bfd885250f6b3bb source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_gitignore_handles_no_trailing_newline(empty_dir: Path)`

Verify `_ensure_gitignore_entry` correctly appends to a `.gitignore` file that lacks a trailing newline.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_happy_path fingerprint=b86a107b08f2025c14debb7d7fcc47cd753ee00c4e932ef900f9e4658da5f5ea body_fp=658aa80a172800249cfdcfd645089160e539c7ef8af7843c5d4f2bf14eb05aa6 source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_init_happy_path(python_project: Path)`

Verify `init_project` writes `trie.toml`, updates `.gitignore`, and reports correct detection markers on a valid Python project.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_errors_on_non_python_without_force fingerprint=175132ec9ad82aad871956f864eec5c66355d6bfcebbc0592e4b02b5f5d7f764 body_fp=caef84ddf91442641efda82d4daf6710b588de6ebac80e4c471f99ca4f987e1f source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_init_errors_on_non_python_without_force(empty_dir: Path)`

Assert `init_project` raises `InitError` when the directory contains no Python markers and `force` is not set.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_force_overrides_detection fingerprint=0e7743bfb02091b186cbf1edf0fc412e9e29c88784df204666aae28d8c8bb074 body_fp=83b25ebfc8b171cda0de4e2be99971fb3e76be98f9a49804f9e0a8ee6917338f source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_init_force_overrides_detection(empty_dir: Path)`

Verify that `init_project` with `force=True` succeeds in a non-Python directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_refuses_overwrite fingerprint=4db7660d8bf07488f7c772980015a065889b8921f1a8506c75e14a2e81f53e5e body_fp=62d4cb6a8b625db6e4bdc72bb40a920f2ca9a8c3e92ffe1fc79c22a40c8a2875 source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_init_refuses_overwrite(python_project: Path)`

Assert `init_project` raises `InitError` when `trie.toml` already exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_force_overwrites fingerprint=866270164c88e6e1aef038e336204617c2de1b1a8802e7cf03b6cf441bf3154b body_fp=29cf7fc58acddbffc9d3a1efbde1b4b82866413667bf8303f47ce80c88276e0f source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_init_force_overwrites(python_project: Path)`

Verify that `init_project` with `force=True` overwrites a tampered `trie.toml` with valid content.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_runs fingerprint=ab2e32568377a6f65e5c360ea9ccde1d62a1277e3573a0fa790303b8041b7693 body_fp=ab57f3367afee873e80e9060258e3071bc4723371e1b139077088cd282fb3b69 source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_cli_init_runs(python_project: Path)`

Verify the `init` CLI command exits 0, prints "wrote", and creates `trie.toml` in a Python project directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_errors_on_existing fingerprint=fa25600301629b323b3d18996e88cc8d48dabf1eb750a8da0d4483f05140b0e0 body_fp=f629a4fbd7b8b6293fedc9efbe95e608e294e49fda8fcee9253140f8ab8fd0fb source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_cli_init_errors_on_existing(python_project: Path)`

Assert the `init` CLI exits with code 1 and prints "already exists" when `trie.toml` is already present.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_force_succeeds fingerprint=9b36865c88174666eda6c668b5ba26711e69b69ebb8305200bae925c8c8d6fa5 body_fp=eb2e7d05f8987ca1c6b12a08ba1275851f68b1223d58ec4f5c01868cb8ca8ae3 source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_cli_init_force_succeeds(python_project: Path)`

Verify that `trie init --force` exits successfully when `trie.toml` already exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_runs_scan_by_default fingerprint=24955c7d7458436caac101a5e0c66a9444c6863571676384b0315562ff202e97 body_fp=3d8b84f6c92378b470b44bf45801ef1a64cfa793803d27f06656a644ddaba459 source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_init_runs_scan_by_default(python_project: Path)`

Assert that `init_project` scans Python files and writes `graph.db` by default.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_no_scan_skips_graph_db fingerprint=8a43923d811342cd52c6745b26f45fe229f5ef19c7f24d1f2de59b0c7fdfc80d body_fp=1fb039d4c07649aafb279879a25679a49725a406fb3fe9b2d9029e4ccc9b8ba3 source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_init_no_scan_skips_graph_db(python_project: Path)`

Verify that `init_project` with `run_scan=False` skips the scan and leaves `graph.db` uncreated.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_install_hook_writes_new_pre_commit_when_git_repo fingerprint=b18c0c04fcf836bcab6ffd1e5ab09560a6380646800a7832ec95a5287ec39fdf body_fp=be2808d6bc74d05ff8cc8ccdd807536a102e118b126c749766652544a7c92191 source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_install_hook_writes_new_pre_commit_when_git_repo(python_project: Path)`

Assert `install_pre_commit_hook` creates an executable `pre-commit` hook containing both trie commands in correct order.

- `lock-check` must appear before `verify` in the written hook file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_install_hook_appends_to_existing_pre_commit fingerprint=ab1aa18038215b7dde8e92f583a36876384f058fd046a737eb33efc13757f132 body_fp=fc62404217e7017116f4bd56529d224442d5f11ef23d1b6870a626f130080bbb source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_install_hook_appends_to_existing_pre_commit(python_project: Path)`

Verify that `install_pre_commit_hook` appends trie's hook content to an existing `pre-commit` file without removing prior content.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_install_hook_idempotent fingerprint=932f9f174cf0d9107b44558c658efcda9a1f2f0d3d2957e5cac9a264d035a6ed body_fp=62fc2c55cafcbe34ec28dc5fe98a99ca39165ac02f9fc430551a5a277cd11b6a source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_install_hook_idempotent(python_project: Path)`

Verify that calling `install_pre_commit_hook` twice returns `installed=False` on the second call.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_install_hook_skips_when_pre_commit_framework_present fingerprint=8d3cba0514be0b0dcc8b782d996547f4ec7455d48a6444a185182945288ef03f body_fp=796889187454d58ad1774709975bf55dd015ee14ad5bc2d1501b7031bb1ec94e source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_install_hook_skips_when_pre_commit_framework_present(python_project: Path)`

Assert that `install_pre_commit_hook` skips installation and returns `strategy="framework"` when `.pre-commit-config.yaml` exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_install_hook_skips_when_not_a_git_repo fingerprint=e1ec9ca6657e1a57abc01cfc0df3ecf1b8a7372169be2bb262b0e43ecb25796b body_fp=340f21fd5fbbc9fa65e9af394c201e65ad9382e36b83a9d19ec595c017678fb7 source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_install_hook_skips_when_not_a_git_repo(python_project: Path)`

Assert `install_pre_commit_hook` returns `(False, "none", None)` when no `.git` directory exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_project_install_hooks_in_git_repo fingerprint=5716a2dfe4f721afce56185d6a4fcb00e454fd33a736f545854f7e6dd2024baa body_fp=f479c2a6eea4ea30f12dbe5e07bfac8893c670afe2265f848b64df06db3e02d9 source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_init_project_install_hooks_in_git_repo(python_project: Path)`

Assert that `init_project` with `install_hooks=True` installs a git pre-commit hook in a valid git repository.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_project_default_does_not_install_hooks fingerprint=08c6aa12b1373f0efa90b2986a651f58d0f606eaa21bd74e09c181faaf89465c body_fp=fa6ae53b84294b8a81f7745d4c6f18f2406d15108dd236fbe13f2db870a6cf18 source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_init_project_default_does_not_install_hooks(python_project: Path)`

Assert that `init_project` skips hook installation when `install_hooks` is not passed.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_install_hooks_flag_in_git_repo fingerprint=39007456c6905639e7e061e74c3a64caa550090cb28f73e42319da4cadc04756 body_fp=8b0432770c26984f4e6988584f2f6b300febcf676f3f0ea688c89b5741168f14 source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_cli_init_install_hooks_flag_in_git_repo(python_project: Path)`

Verify that `trie init --install-hooks` writes a `pre-commit` hook and prints confirmation in a git repo.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_no_install_hooks_flag_skips fingerprint=3bcfccd46e0dbd0a09ec4459c018efd346d2d22b19bafbab699ef7f53576b401 body_fp=6488b08b54c09aaf45cae37720e9ad369673044dd837c8a1e28839175a6ae8c3 source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_cli_init_no_install_hooks_flag_skips(python_project: Path)`

Assert that `--no-install-hooks` causes the CLI `init` command to skip writing the pre-commit hook file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_framework_path_prints_snippet fingerprint=e3019388f23b97c17694c0277d5da5a0966c051b358a4d2556b544878b189455 body_fp=bdc884c818a02e208b81ad9aea5cd745daf916ded1dba592840008ac7c6e7bc3 source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_cli_init_framework_path_prints_snippet(python_project: Path)`

Assert that `trie init --install-hooks` prints a `.pre-commit-config.yaml` snippet when a pre-commit framework config is detected.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_non_interactive_skips_prompt fingerprint=1a209efb2677a41cc6651c35e4407517de6d2cc3b87c511bfb0ea3b7b999385f body_fp=95ba1bcfb68cce1932a5c877bedb5e8cd70b77dd41697569b8222b87d07cb211 source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_cli_init_non_interactive_skips_prompt(python_project: Path)`

Assert that `trie init` exits cleanly without blocking on an interactive prompt in a non-TTY environment.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_prints_scan_summary fingerprint=b7d2cd4f6fb563c5b409eb18edff4cfe29ddb0ea702ca49ab2ce7d4da427919b body_fp=2f97935d711d69da364bcfed0529734fb2ea8be6dfdcd292afeeed6aedae7be0 source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_cli_init_prints_scan_summary(python_project: Path)`

Assert the `trie init` CLI output contains scan summary words "scanned" and "symbols".
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_prints_setup_instruction_in_next_steps fingerprint=36b504ae41a1d76a4264c78b120d4ab32417d40a29c041fd7b8b98b83f4c4014 body_fp=757276979af73ffa308f182ad70d47445669559e1673f27eca28c0571fb8cd8c source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_cli_init_prints_setup_instruction_in_next_steps(python_project: Path)`

Assert that `trie init` always prints `trie setup` in the "Next steps:" output block.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_does_not_run_setup_in_non_interactive_env fingerprint=932d32e892605ad53ea8a369e542e2db3929656966e8dcba24c5046317966fc0 body_fp=310778f74256b7e45193ee98f0bbb28ccbf71849d7b479b851ec3cd8034adb57 source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_cli_init_does_not_run_setup_in_non_interactive_env(python_project: Path)`

Assert that `trie init` in a non-TTY environment never invokes `trie setup` or writes MCP config files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_runs_setup_when_user_accepts_prompt fingerprint=4fc6f3632b51dadbf4b6aa8d4dc094ff81e0779ee67530c414bb6f9da2d60e01 body_fp=4399ac2bb7dd5bde9bc6daa47505052a21cd88d3921434e05f44e391693366a2 source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_cli_init_runs_setup_when_user_accepts_prompt(python_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that accepting the interactive setup prompt triggers `trie setup` by verifying the "Running `trie setup`" banner appears in output.

- `_is_interactive` is patched to `True` to simulate a TTY environment.
- Uses `--no-install-hooks` so the single `"y\n"` input targets only the setup prompt.
- Asserts on banner text only; exit code is not checked due to host-dependent tool availability.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_does_not_run_setup_when_user_declines_prompt fingerprint=2b88a1a18da864f17d833277406db5bf219c9e374d807aafa36d720cb4263986 body_fp=3d8c8f6317794bc33a854a17c9581a6c1e4f6a08395acf0244a03688654f78a2 source_ref=63ee7ba4f36a8d241236d5cae670d2020ba31a9b -->
## `test_cli_init_does_not_run_setup_when_user_declines_prompt(python_project: Path, monkeypatch: pytest.MonkeyPatch)`

Assert that declining the setup prompt suppresses `trie setup` invocation while keeping the "Next steps" instruction.

- `monkeypatch`: patches `trie.cli._is_interactive` to simulate a TTY session.
<!-- trie:end -->