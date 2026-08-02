---
trie_version: 0.3.0
source: tests/test_init.py
file_fingerprint: 5736826df42f8be2f947fcbe12980a078586f161eeb76316166dc3c5d846b138
last_synced_at: '2026-07-25T11:18:12Z'
defines:
- kind: module
  qualified_name: tests/test_init:__module__
  lines: 1-398
- kind: function
  qualified_name: tests/test_init:python_project
  lines: 21-23
  signature: 'def python_project(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_init:empty_dir
  lines: 27-28
  signature: 'def empty_dir(tmp_path: Path) -> Path'
- kind: function
  qualified_name: tests/test_init:test_detect_pyproject
  lines: 34-35
  signature: 'def test_detect_pyproject(python_project: Path)'
- kind: function
  qualified_name: tests/test_init:test_detect_loose_py_files
  lines: 38-40
  signature: 'def test_detect_loose_py_files(empty_dir: Path)'
- kind: function
  qualified_name: tests/test_init:test_detect_one_level_deep_py_files
  lines: 43-46
  signature: 'def test_detect_one_level_deep_py_files(empty_dir: Path)'
- kind: function
  qualified_name: tests/test_init:test_detect_returns_empty_for_non_python
  lines: 49-51
  signature: 'def test_detect_returns_empty_for_non_python(empty_dir: Path)'
- kind: function
  qualified_name: tests/test_init:test_gitignore_creates_when_missing
  lines: 57-60
  signature: 'def test_gitignore_creates_when_missing(empty_dir: Path)'
- kind: function
  qualified_name: tests/test_init:test_gitignore_appends_when_missing_line
  lines: 63-67
  signature: 'def test_gitignore_appends_when_missing_line(empty_dir: Path)'
- kind: function
  qualified_name: tests/test_init:test_gitignore_no_dup_when_already_present
  lines: 70-74
  signature: 'def test_gitignore_no_dup_when_already_present(empty_dir: Path)'
- kind: function
  qualified_name: tests/test_init:test_gitignore_treats_trailing_slash_as_match
  lines: 77-80
  signature: 'def test_gitignore_treats_trailing_slash_as_match(empty_dir: Path)'
- kind: function
  qualified_name: tests/test_init:test_gitignore_handles_no_trailing_newline
  lines: 83-89
  signature: 'def test_gitignore_handles_no_trailing_newline(empty_dir: Path)'
- kind: function
  qualified_name: tests/test_init:test_init_happy_path
  lines: 95-101
  signature: 'def test_init_happy_path(python_project: Path)'
- kind: function
  qualified_name: tests/test_init:test_init_errors_on_unsupported_without_force
  lines: 104-107
  signature: 'def test_init_errors_on_unsupported_without_force(empty_dir: Path)'
- kind: function
  qualified_name: tests/test_init:test_init_force_overrides_detection
  lines: 110-113
  signature: 'def test_init_force_overrides_detection(empty_dir: Path)'
- kind: function
  qualified_name: tests/test_init:test_init_refuses_overwrite
  lines: 116-119
  signature: 'def test_init_refuses_overwrite(python_project: Path)'
- kind: function
  qualified_name: tests/test_init:test_init_force_overwrites
  lines: 122-126
  signature: 'def test_init_force_overwrites(python_project: Path)'
- kind: function
  qualified_name: tests/test_init:test_cli_init_runs
  lines: 132-137
  signature: 'def test_cli_init_runs(python_project: Path)'
- kind: function
  qualified_name: tests/test_init:test_cli_init_errors_on_existing
  lines: 140-145
  signature: 'def test_cli_init_errors_on_existing(python_project: Path)'
- kind: function
  qualified_name: tests/test_init:test_cli_init_force_succeeds
  lines: 148-152
  signature: 'def test_cli_init_force_succeeds(python_project: Path)'
- kind: function
  qualified_name: tests/test_init:test_init_runs_scan_by_default
  lines: 158-164
  signature: 'def test_init_runs_scan_by_default(python_project: Path)'
- kind: function
  qualified_name: tests/test_init:test_init_no_scan_skips_graph_db
  lines: 167-171
  signature: 'def test_init_no_scan_skips_graph_db(python_project: Path)'
- kind: function
  qualified_name: tests/test_init:test_install_hook_writes_new_pre_commit_when_git_repo
  lines: 177-191
  signature: 'def test_install_hook_writes_new_pre_commit_when_git_repo(python_project: Path)'
- kind: function
  qualified_name: tests/test_init:test_install_hook_appends_to_existing_pre_commit
  lines: 194-205
  signature: 'def test_install_hook_appends_to_existing_pre_commit(python_project: Path)'
- kind: function
  qualified_name: tests/test_init:test_install_hook_idempotent
  lines: 208-213
  signature: 'def test_install_hook_idempotent(python_project: Path)'
- kind: function
  qualified_name: tests/test_init:test_install_hook_skips_when_pre_commit_framework_present
  lines: 216-222
  signature: 'def test_install_hook_skips_when_pre_commit_framework_present(python_project: Path)'
- kind: function
  qualified_name: tests/test_init:test_install_hook_skips_when_not_a_git_repo
  lines: 225-229
  signature: 'def test_install_hook_skips_when_not_a_git_repo(python_project: Path)'
- kind: function
  qualified_name: tests/test_init:test_init_project_install_hooks_in_git_repo
  lines: 235-240
  signature: 'def test_init_project_install_hooks_in_git_repo(python_project: Path)'
- kind: function
  qualified_name: tests/test_init:test_init_project_default_does_not_install_hooks
  lines: 243-247
  signature: 'def test_init_project_default_does_not_install_hooks(python_project: Path)'
- kind: function
  qualified_name: tests/test_init:test_cli_init_install_hooks_flag_in_git_repo
  lines: 253-259
  signature: 'def test_cli_init_install_hooks_flag_in_git_repo(python_project: Path)'
- kind: function
  qualified_name: tests/test_init:test_cli_init_no_install_hooks_flag_skips
  lines: 262-267
  signature: 'def test_cli_init_no_install_hooks_flag_skips(python_project: Path)'
- kind: function
  qualified_name: tests/test_init:test_cli_init_framework_path_prints_snippet
  lines: 270-277
  signature: 'def test_cli_init_framework_path_prints_snippet(python_project: Path)'
- kind: function
  qualified_name: tests/test_init:test_cli_init_non_interactive_skips_prompt
  lines: 280-284
  signature: 'def test_cli_init_non_interactive_skips_prompt(python_project: Path)'
- kind: function
  qualified_name: tests/test_init:test_cli_init_prints_scan_summary
  lines: 287-293
  signature: 'def test_cli_init_prints_scan_summary(python_project: Path)'
- kind: function
  qualified_name: tests/test_init:test_cli_init_prints_setup_instruction_in_next_steps
  lines: 301-310
  signature: 'def test_cli_init_prints_setup_instruction_in_next_steps(python_project: Path)'
- kind: function
  qualified_name: tests/test_init:test_cli_init_does_not_run_setup_in_non_interactive_env
  lines: 313-328
  signature: 'def test_cli_init_does_not_run_setup_in_non_interactive_env( python_project: Path, )'
- kind: function
  qualified_name: tests/test_init:test_cli_init_runs_setup_when_user_accepts_prompt
  lines: 331-361
  signature: 'def test_cli_init_runs_setup_when_user_accepts_prompt( python_project: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_init:test_cli_init_does_not_run_setup_when_user_declines_prompt
  lines: 364-383
  signature: 'def test_cli_init_does_not_run_setup_when_user_declines_prompt( python_project: Path, monkeypatch: pytest.MonkeyPatch )'
- kind: function
  qualified_name: tests/test_init:test_hook_block_is_one_gate_command
  lines: 386-397
  signature: def test_hook_block_is_one_gate_command()
incoming_refs: 0
outgoing_refs: 47
---
<!-- trie:section symbol=tests/test_init:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=d173e1f300fb749b32b1142f341b1f2b668bd9c9bd80429f01418b414b1e5886 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Test suite for trie project initialization functionality, covering project detection, configuration creation, Git integration, and CLI commands.

- Validates Python project detection logic for pyproject.toml and *.py files
- Tests .gitignore entry management with various existing content scenarios  
- Covers init_project function with force overwrite, scan execution, and error handling
- Verifies CLI init command with flags for hooks installation and force mode
- Tests pre-commit hook installation in Git repos and framework detection
- Includes interactive setup prompt testing with TTY simulation
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:python_project fingerprint=3c46e839304076e37baaf33fc2ba0f6ef1d265bd95d3c382ef38e43bab36600e body_fp=8832154416426ae0274beec35d0606761726221781605f4da417b640dedde370 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def python_project(tmp_path: Path) -> Path`

Creates a temporary directory containing a minimal `pyproject.toml` file for testing Python project initialization.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:empty_dir fingerprint=55e26967baf902dc0a8bf6551bb7512f4710c8d3dde4d3799903becb872bb499 body_fp=f98a3c8750b58d38276ce53848e9ccfeff678950a532fc3ae33c81fc572a1e83 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def empty_dir(tmp_path: Path) -> Path`

Pytest fixture that returns an empty temporary directory for testing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_detect_pyproject fingerprint=4c45a248121bb657bbe48576422a5307631c19c084c34cf9e80982c99e328c01 body_fp=d87cc6ea875e54606119fd80c8ce40768c54460ffa01da384856baaa830cb835 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_detect_pyproject(python_project: Path)`

Tests that `_detect_python_project` returns `["pyproject.toml"]` when a pyproject.toml file exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_detect_loose_py_files fingerprint=e90cdfa099c11d1f477d766305d7201bf4a4ae4a439fc5a43f834e3c302f33fd body_fp=6ce29dad749f54188112214628440ce57405643a94c561a3428ac6957d0b8972 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_detect_loose_py_files(empty_dir: Path)`

Tests that `_detect_python_project` identifies directories containing Python files as Python projects.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_detect_one_level_deep_py_files fingerprint=8e52c90d54d44272aa2d159ebcbe0b63f110f5a0cf04f2ce64c285af0910e156 body_fp=a30702f78e777e15590c4d4f353b9348ac96e20ba6a7d1f1a69bfda4cd10d365 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_detect_one_level_deep_py_files(empty_dir: Path)`

Verifies `_detect_python_project` detects Python files nested one directory deep as a Python project marker.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_detect_returns_empty_for_non_python fingerprint=6d714012a2bcfdf712ad18a26ab684641daeadc4190d82e25a4d928b35712006 body_fp=e8afc3e2cff1261d23a473735ea724e303d9bd0744343215ff7c4516b63a1be8 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_detect_returns_empty_for_non_python(empty_dir: Path)`

Verifies _detect_python_project returns empty list when directory contains no Python project markers.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_gitignore_creates_when_missing fingerprint=1f4d87462de9b7bdbf611d8698fbc43a86738f978ad30b887af2b4918de50e0d body_fp=d2e96781f7023fe01c8c091c2dc8f1cb02de0d5fb459768dcf04619bd43cc301 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_gitignore_creates_when_missing(empty_dir: Path)`

Tests that `_ensure_gitignore_entry` creates a new `.gitignore` file with the trie entry when none exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_gitignore_appends_when_missing_line fingerprint=4edfb60332c83003e3f23a8568441be9d3849cda4943852a54e390bcb4d8c58b body_fp=672a98ae3136da6d515ed52b901d491c2e16de1ebc8297373a850b5e2db8d4d0 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_gitignore_appends_when_missing_line(empty_dir: Path)`

Tests that `_ensure_gitignore_entry` appends the trie line when gitignore exists but lacks it.

- Creates existing gitignore with other content
- Verifies function returns True indicating modification was made
- Confirms trie entry appears in final gitignore content
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_gitignore_no_dup_when_already_present fingerprint=d23d183ba7712f789eb3b07c2286b3c2e05a3bcca0e617da249f0fc190106b2a body_fp=369566cc5e6ace09f20cb1a04c5fcd4c201cdab269c31ebb4ff7464f12049628 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_gitignore_no_dup_when_already_present(empty_dir: Path)`

Tests that _ensure_gitignore_entry returns False and avoids duplicating entries when the gitignore line already exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_gitignore_treats_trailing_slash_as_match fingerprint=4a4f76bafbcc8df0cee594ca8deb071b79390b606e9a0905f9a0b675a6f6d04e body_fp=4a65cdf33bd5ea2eee8718deb32569de78fe40f9db08d4ef659b88b28500fb4f source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_gitignore_treats_trailing_slash_as_match(empty_dir: Path)`

Tests that `_ensure_gitignore_entry` treats `.trie` and `.trie/` as equivalent matches.

- Returns False when `.trie` already exists, even when checking for `.trie/`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_gitignore_handles_no_trailing_newline fingerprint=a48d6e36ac66a29e6f7efd70a5ab6c8e0c3b9d55dfc47cc523e3309e2450d809 body_fp=eb8762249f74f965d5906ad4b6e5700550a4afe864754f172cc5a162e13a40a6 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_gitignore_handles_no_trailing_newline(empty_dir: Path)`

Tests that `_ensure_gitignore_entry` correctly appends to a .gitignore file lacking a trailing newline.

• Verifies the function adds both a newline and the trie entry
• Confirms existing content is preserved
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_happy_path fingerprint=b86a107b08f2025c14debb7d7fcc47cd753ee00c4e932ef900f9e4658da5f5ea body_fp=00a3c5281ef841a66bf62758512d1be08ff3ebf10b909354b8e593aa20c08d48 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_init_happy_path(python_project: Path)`

Tests successful project initialization, verifying config file creation, gitignore setup, and Python project detection.

- Validates trie.toml creation and gitignore entry addition
- Confirms pyproject.toml is detected as a Python project marker
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_errors_on_unsupported_without_force fingerprint=1acf0f97f1ac873068b9b3f81414311d1cb3908ed6f791863d2bdc1a154e112e body_fp=7b7a67f5777fdef362cd521981feb853314d60799dfa9ab74a187817e05aff68 source_ref=83a82c26e1f4e7fdeba880b286a81c0302c804c1 role=test -->
## `def test_init_errors_on_unsupported_without_force(empty_dir: Path)`

Assert that `init_project` raises `InitError` matching "does not look like a supported project" when the directory contains no Python indicators and `force` is not set.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_force_overrides_detection fingerprint=0e7743bfb02091b186cbf1edf0fc412e9e29c88784df204666aae28d8c8bb074 body_fp=2b72addfaee1a6925e6c8d18c9a92ec2add41bb0947c7871681f36b396df000e source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_init_force_overrides_detection(empty_dir: Path)`

Tests that `init_project` succeeds in non-Python directories when `force=True` is specified.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_refuses_overwrite fingerprint=4db7660d8bf07488f7c772980015a065889b8921f1a8506c75e14a2e81f53e5e body_fp=2cd6c349b30920593af2236c4eaa1377eca8de4a30c739842faf2c5b9096e30d source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_init_refuses_overwrite(python_project: Path)`

Tests that init_project raises InitError when trie.toml already exists without force flag.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_force_overwrites fingerprint=866270164c88e6e1aef038e336204617c2de1b1a8802e7cf03b6cf441bf3154b body_fp=2cc222d1d4de4df7b6d3fcb4ee4e54254c5ba0667dec06986584ba424e42a784 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_init_force_overwrites(python_project: Path)`

Verifies that `init_project` with `force=True` overwrites an existing trie.toml file with fresh configuration content.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_runs fingerprint=ab2e32568377a6f65e5c360ea9ccde1d62a1277e3573a0fa790303b8041b7693 body_fp=11bbcb5ee9d6ca3ce37226f8c4bd39784e05d86e54431b8573f4f3428f511405 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=cli-interface -->
## `def test_cli_init_runs(python_project: Path)`

Tests that CLI `init` command successfully initializes a Python project and creates configuration file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_errors_on_existing fingerprint=fa25600301629b323b3d18996e88cc8d48dabf1eb750a8da0d4483f05140b0e0 body_fp=daf75a2fd963a80484a9f07fd0bb71b9a0739c6605bc1b685036d5285435671a source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_cli_init_errors_on_existing(python_project: Path)`

Verifies CLI init command exits with error code 1 when config file already exists.

- Sets up existing config via `init_project()`, then invokes CLI to confirm rejection
- Checks both exit code and error message content
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_force_succeeds fingerprint=9b36865c88174666eda6c668b5ba26711e69b69ebb8305200bae925c8c8d6fa5 body_fp=4d15785b21b1322b40d589d018a556b7e9d18437427b07b5a8674114c3f45f61 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_cli_init_force_succeeds(python_project: Path)`

Verifies that CLI init command succeeds with --force flag when trie.toml already exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_runs_scan_by_default fingerprint=24955c7d7458436caac101a5e0c66a9444c6863571676384b0315562ff202e97 body_fp=b0fa2695ca77a03abf34f36c9a9772efe9d881c143cc31468940acb9059044f5 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_init_runs_scan_by_default(python_project: Path)`

Tests that init_project runs a scan by default and creates graph database.

- Creates a Python file with a function
- Verifies scan_ran flag is True
- Confirms scan metrics are populated
- Checks graph.db file exists in .trie directory
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_no_scan_skips_graph_db fingerprint=8a43923d811342cd52c6745b26f45fe229f5ef19c7f24d1f2de59b0c7fdfc80d body_fp=9d3836cf3450c342279c1ca58efb276a0d00b99e60248e45145d415a098f0f2f source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_init_no_scan_skips_graph_db(python_project: Path)`

Tests that `init_project` skips graph database creation when `run_scan=False`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_install_hook_writes_new_pre_commit_when_git_repo fingerprint=64a9a95f7c69c270f1385333fb2570b86c968cff3a4761f8382c6d14296f1bb2 body_fp=21fec9ce0c589851bf83e6d80258ea99d6ebba643b755c8c0d289e5fc40d8158 source_ref=3818b67c25669f0bbec2cc0497ecfcf056639ec1 role=test -->
## `def test_install_hook_writes_new_pre_commit_when_git_repo(python_project: Path)`

Tests that `install_pre_commit_hook` creates a new git pre-commit hook in a git repository.

- Verifies hook contains `PRE_COMMIT_HOOK_MARKER`, delegates to `trie gate || exit $?`, and is executable
- Returns `installed=True`, `strategy="git_hook"`, and valid `hook_path`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_install_hook_appends_to_existing_pre_commit fingerprint=ab1aa18038215b7dde8e92f583a36876384f058fd046a737eb33efc13757f132 body_fp=d3db633381009625ff2a511fa54fa5f5e2664a7253c44acede1646a3faec7f63 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_install_hook_appends_to_existing_pre_commit(python_project: Path)`

Tests that `install_pre_commit_hook` appends trie commands to an existing pre-commit hook while preserving the original content.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_install_hook_idempotent fingerprint=932f9f174cf0d9107b44558c658efcda9a1f2f0d3d2957e5cac9a264d035a6ed body_fp=3d5bac0948c730ace243d0bcdda0f3873b70d9a00c2be0d96d7106905ee08323 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_install_hook_idempotent(python_project: Path)`

Verifies that `install_pre_commit_hook` returns `installed=False` when the hook is already present.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_install_hook_skips_when_pre_commit_framework_present fingerprint=8d3cba0514be0b0dcc8b782d996547f4ec7455d48a6444a185182945288ef03f body_fp=6e9bd2b3f8586cc9dddd1fa822b3f3bc754d8c8be514924abd312ab976af2ad3 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_install_hook_skips_when_pre_commit_framework_present(python_project: Path)`

Tests that `install_pre_commit_hook` skips installation when a pre-commit framework configuration file is already present.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_install_hook_skips_when_not_a_git_repo fingerprint=e1ec9ca6657e1a57abc01cfc0df3ecf1b8a7372169be2bb262b0e43ecb25796b body_fp=b21180696b58f7ee9fca31594982e0fbf1f8be099b9da232d0ebb159705423a5 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_install_hook_skips_when_not_a_git_repo(python_project: Path)`

Verifies install_pre_commit_hook returns False with "none" strategy when project lacks .git directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_project_install_hooks_in_git_repo fingerprint=5716a2dfe4f721afce56185d6a4fcb00e454fd33a736f545854f7e6dd2024baa body_fp=b4d64d3b4329575be1f0bce727ac41b455a476999ae88577027ee4f6e3befcaa source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_init_project_install_hooks_in_git_repo(python_project: Path)`

Tests that `init_project` installs pre-commit hooks when `install_hooks=True` and the directory is a git repository.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_project_default_does_not_install_hooks fingerprint=08c6aa12b1373f0efa90b2986a651f58d0f606eaa21bd74e09c181faaf89465c body_fp=2ac307fa5fd1f0debb934ce667397ce6235f0a39f5cafc9a5112674cbd033015 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_init_project_default_does_not_install_hooks(python_project: Path)`

Verifies init_project does not install pre-commit hooks by default even in git repositories.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_install_hooks_flag_in_git_repo fingerprint=39007456c6905639e7e061e74c3a64caa550090cb28f73e42319da4cadc04756 body_fp=9f3e43c9fbb589ee64f9e7e5418b7964bc78863fd6ab176ada08da2fa698bd0f source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_cli_init_install_hooks_flag_in_git_repo(python_project: Path)`

Tests that `trie init --install-hooks` successfully installs pre-commit hook in a git repository.

- Verifies CLI exit code is 0 and output mentions hook installation
- Confirms pre-commit hook file is created in `.git/hooks/`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_no_install_hooks_flag_skips fingerprint=3bcfccd46e0dbd0a09ec4459c018efd346d2d22b19bafbab699ef7f53576b401 body_fp=934ea39d69ea6e85bb72f39c72cc822ca69086ec770ac77760b1ece8879614d5 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_cli_init_no_install_hooks_flag_skips(python_project: Path)`

Tests that CLI init with `--no-install-hooks` flag skips pre-commit hook installation.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_framework_path_prints_snippet fingerprint=e3019388f23b97c17694c0277d5da5a0966c051b358a4d2556b544878b189455 body_fp=8dbd48987189d7c09535c2e86e004702c686b14c99c0b419605642690b4d70c2 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_cli_init_framework_path_prints_snippet(python_project: Path)`

Tests that CLI init with --install-hooks prints pre-commit framework snippet when .pre-commit-config.yaml exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_non_interactive_skips_prompt fingerprint=1a209efb2677a41cc6651c35e4407517de6d2cc3b87c511bfb0ea3b7b999385f body_fp=b1f73929cd0e8defe147cf662b4a24b612e7d9ab65cf46d9baa2422988c82b16 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=cli-interface -->
## `def test_cli_init_non_interactive_skips_prompt(python_project: Path)`

Verifies that CLI init command completes successfully in non-interactive environments without blocking on prompts.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_prints_scan_summary fingerprint=b7d2cd4f6fb563c5b409eb18edff4cfe29ddb0ea702ca49ab2ce7d4da427919b body_fp=56733a7c5c37c257a5cf9f472ea6be4edecae8e025c5edc5a13bf9172be1a360 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_cli_init_prints_scan_summary(python_project: Path)`

Verifies that CLI init command outputs scan statistics after completing project initialization.

- Creates a Python file in the test project before running init
- Asserts that output contains "scanned" and "symbols" text indicating scan summary was printed
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_prints_setup_instruction_in_next_steps fingerprint=36b504ae41a1d76a4264c78b120d4ab32417d40a29c041fd7b8b98b83f4c4014 body_fp=2c1418102a4b470cc25d77d5bbcaa704034c6dcc19862e12628d513564f46c16 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_cli_init_prints_setup_instruction_in_next_steps(python_project: Path)`

Verifies that CLI init always displays "trie setup" instruction in next steps output.

- Tests fallback guidance for non-TTY environments and declined prompts
- Asserts presence of "Next steps:" and "trie setup" strings in command output
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_does_not_run_setup_in_non_interactive_env fingerprint=932d32e892605ad53ea8a369e542e2db3929656966e8dcba24c5046317966fc0 body_fp=6772c366b324b85ba894de2fb8bc54330c8edeee280946ceaa9790fa566885e2 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=agent-integration -->
## `def test_cli_init_does_not_run_setup_in_non_interactive_env( python_project: Path, )`

Verifies that `trie init` in non-interactive environments suppresses the setup prompt and never auto-runs `trie setup`.

- Checks absence of setup banner in output
- Confirms no MCP config files are written to project root
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_runs_setup_when_user_accepts_prompt fingerprint=75aaed2bda52d5c9835ea382d06aa18b2ede4765c03f92f8a0b6e27efa30d696 body_fp=d8c2da462eff44ab5e9668a68c0c43ae9802983e5c30c2d2be93501652a53e95 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_cli_init_runs_setup_when_user_accepts_prompt( python_project: Path, monkeypatch: pytest.MonkeyPatch )`

Tests that the `trie init` command automatically runs `trie setup` when user accepts the interactive prompt.

- Patches `_is_interactive` to simulate TTY environment
- Uses `--no-install-hooks` to isolate setup prompt from pre-commit hook prompt  
- Verifies setup execution by checking for "Running `trie setup`" banner in output
- Changes working directory to test project to prevent setup from modifying trie repo itself
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_does_not_run_setup_when_user_declines_prompt fingerprint=2b88a1a18da864f17d833277406db5bf219c9e374d807aafa36d720cb4263986 body_fp=83047656d0ca2532c56d8237de9725297645f13c7bbf741c317da9fe1e43c47b source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
## `def test_cli_init_does_not_run_setup_when_user_declines_prompt( python_project: Path, monkeypatch: pytest.MonkeyPatch )`

Tests that declining the setup prompt in `trie init` skips auto-setup while preserving manual instruction.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_hook_block_is_one_gate_command fingerprint=d46d254549348d0e35f3a9b624ff6c7b9d945d97cfac5ffa32de6be8deba2fcd body_fp=391e6a72a22e6fc51d68989513f45238f32a0f47c7467f3989d814067d807321 source_ref=3818b67c25669f0bbec2cc0497ecfcf056639ec1 role=test -->
## `def test_hook_block_is_one_gate_command()`

Assert that `PRE_COMMIT_HOOK_BLOCK` delegates entirely to `trie gate || exit $?` and embeds no stale individual gate steps.
<!-- trie:end -->