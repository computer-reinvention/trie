---
trie_version: 0.1.5
source: tests/test_init.py
file_fingerprint: 4f7cf1e91a3a43649f2db6b12773746816c15047ce7c0b98276a4bee1ff8996c
last_synced_at: '2026-06-03T20:57:16Z'
defines:
- kind: module
  qualified_name: tests/test_init:__module__
  lines: 1-388
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
  lines: 335-365
- kind: function
  qualified_name: tests/test_init:test_cli_init_does_not_run_setup_when_user_declines_prompt
  lines: 368-387
incoming_refs: 0
outgoing_refs: 46
---
<!-- trie:section symbol=tests/test_init:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=806ffb2e00efa2b0a01d935de07e92c5ec844ceeb8403b7f560666bb014f1cba source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Tests for the `trie.init` module, covering project initialization, Python project detection, gitignore handling, pre-commit hook installation, and CLI integration.

- Fixtures provide `python_project` (tmp dir with pyproject.toml) and `empty_dir` for isolated testing
- Detection tests verify `_detect_python_project` finds pyproject.toml and .py files correctly
- Gitignore tests ensure `_ensure_gitignore_entry` creates/appends/deduplicates .trie/ entries properly
- Init tests cover `init_project` happy path, force mode, overwrite protection, and automatic scanning
- Pre-commit hook tests verify `install_pre_commit_hook` creates git hooks with proper ordering and idempotency
- CLI tests validate `trie init` command behavior including error handling, force flags, and setup prompts
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:python_project fingerprint=3c46e839304076e37baaf33fc2ba0f6ef1d265bd95d3c382ef38e43bab36600e body_fp=07d823bca7d372b2695ea34df71ff7cfd1b7343c3279be97e07304b4274d8709 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Creates a temporary directory with a minimal `pyproject.toml` file for testing Python project detection.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:empty_dir fingerprint=55e26967baf902dc0a8bf6551bb7512f4710c8d3dde4d3799903becb872bb499 body_fp=f28d92905bbad87dd9a7fed32fc8bfc4f06df7708e1d46312ca61a55b6b3011e source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Returns a pytest fixture providing an empty temporary directory for testing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_detect_pyproject fingerprint=4c45a248121bb657bbe48576422a5307631c19c084c34cf9e80982c99e328c01 body_fp=1b89aa6b50ae8f8d1028b1e30ce382877632cba72e2d9cd56f58de3edcfa0110 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Tests that `_detect_python_project` identifies a pyproject.toml file as a Python project marker.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_detect_loose_py_files fingerprint=e90cdfa099c11d1f477d766305d7201bf4a4ae4a439fc5a43f834e3c302f33fd body_fp=db64aae60b5eab50833f0c136cb2bc4a936b43069a429a2058205399a6abdfaa source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Tests that `_detect_python_project` identifies loose Python files in the root directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_detect_one_level_deep_py_files fingerprint=8e52c90d54d44272aa2d159ebcbe0b63f110f5a0cf04f2ce64c285af0910e156 body_fp=9a2851acad4f7b0f306c1d5fbf826ba37280c099301c1a6d530b7ed36d2e885e source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Tests that `_detect_python_project` finds Python files in subdirectories one level deep.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_detect_returns_empty_for_non_python fingerprint=6d714012a2bcfdf712ad18a26ab684641daeadc4190d82e25a4d928b35712006 body_fp=f8e5f0266a6c1077ec6439931a708f1ff6a40b2985237c783e560a78a4b68170 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Verifies that `_detect_python_project` returns empty list when directory contains only non-Python files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_gitignore_creates_when_missing fingerprint=1f4d87462de9b7bdbf611d8698fbc43a86738f978ad30b887af2b4918de50e0d body_fp=50ce995c7117f0fb33d8e4535690f73b5e1f097a53e1783be8a103280659f536 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Tests that `_ensure_gitignore_entry` creates a new `.gitignore` file with the specified entry when the file doesn't exist.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_gitignore_appends_when_missing_line fingerprint=4edfb60332c83003e3f23a8568441be9d3849cda4943852a54e390bcb4d8c58b body_fp=4c3bb14f3778750329282c747c68c99a2117b20eba92f30c449b2d281ffc7161 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Tests that `_ensure_gitignore_entry` appends the trie entry to an existing gitignore file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_gitignore_no_dup_when_already_present fingerprint=d23d183ba7712f789eb3b07c2286b3c2e05a3bcca0e617da249f0fc190106b2a body_fp=5e64187b0046357133c33245992bb1c88030816b9efc1edc25619663ecf16fee source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Verifies `_ensure_gitignore_entry` returns `False` and avoids duplicate entries when the target line already exists in `.gitignore`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_gitignore_treats_trailing_slash_as_match fingerprint=4a4f76bafbcc8df0cee594ca8deb071b79390b606e9a0905f9a0b675a6f6d04e body_fp=cf57296728f089bbdc217d417659a570031597e1ec40d834f64a75344763bcc3 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Verifies that `_ensure_gitignore_entry` recognizes `.trie` as equivalent to `.trie/` when checking for existing entries.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_gitignore_handles_no_trailing_newline fingerprint=a48d6e36ac66a29e6f7efd70a5ab6c8e0c3b9d55dfc47cc523e3309e2450d809 body_fp=04e327d16f74f876b5eb1ea536bde04bbdd61a1b1e2759f3ce537705cc4a4b32 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Tests that `_ensure_gitignore_entry` correctly appends entries when the gitignore file lacks a trailing newline.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_happy_path fingerprint=b86a107b08f2025c14debb7d7fcc47cd753ee00c4e932ef900f9e4658da5f5ea body_fp=97db6b367daaff94b8cf856a8525fd67067b3592228a959ad19ee165de7454c2 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Tests successful project initialization by verifying config file creation, gitignore setup, and project detection.

- Validates that `init_project` writes `trie.toml` and updates `.gitignore` with `.trie/` entry
- Confirms detection markers include `pyproject.toml` for Python project identification
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_errors_on_non_python_without_force fingerprint=175132ec9ad82aad871956f864eec5c66355d6bfcebbc0592e4b02b5f5d7f764 body_fp=d39b1afd71572949dec9a4e933cde874cac6c4eac259ef78f84d5bd2d50c02fd source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Verifies that init_project raises InitError when given a directory containing only non-Python files.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_force_overrides_detection fingerprint=0e7743bfb02091b186cbf1edf0fc412e9e29c88784df204666aae28d8c8bb074 body_fp=a7c102b5514f762fa77f5889ad29cc038b019334ff7832d127a66718460939de source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Verifies that `init_project` bypasses Python project detection when `force=True` is set.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_refuses_overwrite fingerprint=4db7660d8bf07488f7c772980015a065889b8921f1a8506c75e14a2e81f53e5e body_fp=34384b49d2997f69954c347985725edbc0371e37836aacc82c6a0c48c4a6ee08 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Tests that `init_project` raises `InitError` when attempting to initialize a project that already has a config file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_force_overwrites fingerprint=866270164c88e6e1aef038e336204617c2de1b1a8802e7cf03b6cf441bf3154b body_fp=c8b6cd3a19f2857a68f658bfab1eef1875093f66e29d65bc80b4c2ab2ebace26 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Verifies that `init_project` overwrites existing config when force=True is used.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_runs fingerprint=ab2e32568377a6f65e5c360ea9ccde1d62a1277e3573a0fa790303b8041b7693 body_fp=f238624f37fed66731f0fc1feb4746a09014b8a9c675d601d9c78684ab9309fe source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Tests that the `trie init` CLI command successfully creates a trie.toml configuration file.

- Verifies exit code 0 and presence of "wrote" message in output
- Confirms trie.toml file exists after command execution
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_errors_on_existing fingerprint=fa25600301629b323b3d18996e88cc8d48dabf1eb750a8da0d4483f05140b0e0 body_fp=cf3f539decfdf85f6c2e8bf1a9f79e5c3dfe1ed12c6af5be38e871bdfda4afe6 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Verifies that the CLI init command returns exit code 1 when attempting to initialize a project that already has a trie configuration.

- Sets up an existing trie project, then attempts to initialize it again
- Confirms exit code 1 and "already exists" error message
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_force_succeeds fingerprint=9b36865c88174666eda6c668b5ba26711e69b69ebb8305200bae925c8c8d6fa5 body_fp=638eb5f168e408587d629d0f82c4d8657dc19509021d93e8438bdfec02f89c99 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Verifies that the CLI init command with --force flag succeeds when a trie.toml already exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_runs_scan_by_default fingerprint=24955c7d7458436caac101a5e0c66a9444c6863571676384b0315562ff202e97 body_fp=bba778b6e87eb26ac56c65212d9c637b9ae62c4592fc6d517ae3524ef799ab2c source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Verifies `init_project` runs scan by default, creating graph database and reporting scan metrics.

- Creates a Python file, then asserts scan ran and produced expected file/symbol counts
- Confirms graph.db file exists in .trie directory after initialization
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_no_scan_skips_graph_db fingerprint=8a43923d811342cd52c6745b26f45fe229f5ef19c7f24d1f2de59b0c7fdfc80d body_fp=70fd92971bed48e3939e07e84e0b62ebed925a22e88fe1e65c5cc82ad0eea742 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Tests that `init_project` with `run_scan=False` skips creating the graph database file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_install_hook_writes_new_pre_commit_when_git_repo fingerprint=b18c0c04fcf836bcab6ffd1e5ab09560a6380646800a7832ec95a5287ec39fdf body_fp=eda5e0637b5cf1d35459f3231f2b8475e4f0917b7b7716b5376480c7bc9cc8bc source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Verifies that `install_pre_commit_hook` creates a new pre-commit hook in a Git repository with proper content and permissions.

- Hook contains both `trie -q lock-check` and `trie -q verify` commands
- Lock-check precedes verify to fail fast on contention
- Hook file is executable
- Returns strategy as "git_hook"
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_install_hook_appends_to_existing_pre_commit fingerprint=ab1aa18038215b7dde8e92f583a36876384f058fd046a737eb33efc13757f132 body_fp=70911e5e2d9baea602780261df5b34b6cc1073b8fe2d8136c442126e2476fae9 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Verifies install_pre_commit_hook appends trie commands to existing pre-commit hook while preserving original content.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_install_hook_idempotent fingerprint=932f9f174cf0d9107b44558c658efcda9a1f2f0d3d2957e5cac9a264d035a6ed body_fp=97250753aef9f1418bd3b186a236f1742efd436d5a615d7fd752f00a10c9436e source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Verifies that installing a pre-commit hook twice does not duplicate the hook content.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_install_hook_skips_when_pre_commit_framework_present fingerprint=8d3cba0514be0b0dcc8b782d996547f4ec7455d48a6444a185182945288ef03f body_fp=6f2b23aadb34ab287ccf77b8aae5445ab1b83d498faa4599d6d07e7503fe39bc source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Tests that `install_pre_commit_hook` skips installation when a pre-commit framework config is detected.

- Creates `.pre-commit-config.yaml` to simulate existing framework setup
- Verifies function returns `installed=False`, `strategy="framework"`, `hook_path=None`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_install_hook_skips_when_not_a_git_repo fingerprint=e1ec9ca6657e1a57abc01cfc0df3ecf1b8a7372169be2bb262b0e43ecb25796b body_fp=49d8e9b9acc33c39e63d262b0bb07715101238f1dd100892facbd4ae71875573 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Verifies install_pre_commit_hook returns no-op results when project lacks a .git directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_project_install_hooks_in_git_repo fingerprint=5716a2dfe4f721afce56185d6a4fcb00e454fd33a736f545854f7e6dd2024baa body_fp=620e5993a17d21201c7363965f8dbefef6fdbb9bd0bc419b117f339099909d56 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Verifies that `init_project` installs git hooks when `install_hooks=True` and a `.git` directory exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_project_default_does_not_install_hooks fingerprint=08c6aa12b1373f0efa90b2986a651f58d0f606eaa21bd74e09c181faaf89465c body_fp=2f8f05fa460a1e0a27869076330c433276c1c3ce908f8d114ab5be91e943cf36 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Verifies that init_project does not install pre-commit hooks by default even in a git repository.

- Creates a git repository but calls init_project without install_hooks=True
- Asserts pre_commit_installed is False and strategy is "skipped"
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_install_hooks_flag_in_git_repo fingerprint=39007456c6905639e7e061e74c3a64caa550090cb28f73e42319da4cadc04756 body_fp=62a7f66e8d31da2c64dc1170c639707b1b256d03ea120d55c817afea11639d65 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Tests that `trie init --install-hooks` successfully installs git pre-commit hook in a git repository.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_no_install_hooks_flag_skips fingerprint=3bcfccd46e0dbd0a09ec4459c018efd346d2d22b19bafbab699ef7f53576b401 body_fp=5ca95e55784ef6fc0b1628855e85cc3289385cb546c9f25aba8ad66346f0564f source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Verifies the `trie init --no-install-hooks` command skips installing git hooks even in a git repository.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_framework_path_prints_snippet fingerprint=e3019388f23b97c17694c0277d5da5a0966c051b358a4d2556b544878b189455 body_fp=1b737581a234f0da8644a67970f779e50aaed0daf68752fadb8f56a873dd74f3 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Verifies that `trie init --install-hooks` prints framework configuration snippet when pre-commit framework is detected.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_non_interactive_skips_prompt fingerprint=1a209efb2677a41cc6651c35e4407517de6d2cc3b87c511bfb0ea3b7b999385f body_fp=81e351b823b781255b892701c3a4c3aa5121e3253cdc12f70b6822c783531102 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Tests that CLI init command doesn't block on prompts in non-interactive environments.

- Verifies that `trie init` succeeds without hanging when run without TTY
- Ensures exit code is 0 when no `--install-hooks` flag is provided
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_prints_scan_summary fingerprint=b7d2cd4f6fb563c5b409eb18edff4cfe29ddb0ea702ca49ab2ce7d4da427919b body_fp=d6b02541656eca955838f1464cafc85288dd3303f76a9dc2b4dba6fb7a62e8ba source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Verifies that the CLI init command prints scan summary information in its output.

- Creates a Python file with a function to ensure symbols are found during scanning
- Asserts the output contains "scanned" and "symbols" text indicating scan results
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_prints_setup_instruction_in_next_steps fingerprint=36b504ae41a1d76a4264c78b120d4ab32417d40a29c041fd7b8b98b83f4c4014 body_fp=9ba06f44687bd85d1f4561556a72b7d159f3df155dc0293d578f17aa26fad4fa source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Verifies that CLI init command always prints "trie setup" instruction in Next steps output.

- Tests that setup instruction appears regardless of auto-run prompt acceptance
- Ensures fallback guidance for non-TTY environments and declined prompts
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_does_not_run_setup_in_non_interactive_env fingerprint=932d32e892605ad53ea8a369e542e2db3929656966e8dcba24c5046317966fc0 body_fp=24a63c2b00bca6ee24879e71c8f26960190be99df6c8ba2e787425ed45ccafc3 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Verifies that `trie init` in non-interactive environments suppresses the setup auto-run prompt and only shows instructions.

- Checks CLI exits successfully without setup banner or MCP config files
- Ensures non-TTY environments get guidance without automatic setup execution
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_runs_setup_when_user_accepts_prompt fingerprint=75aaed2bda52d5c9835ea382d06aa18b2ede4765c03f92f8a0b6e27efa30d696 body_fp=21cf93a2a2fa73f87544587f486496828556bcc3e3eb36a77c7d597a4440ad1a source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Tests that the CLI init command runs `trie setup` automatically when user accepts the interactive prompt.

- Patches `_is_interactive` to simulate TTY environment
- Uses `--no-install-hooks` to isolate the setup prompt from pre-commit hook prompt
- Changes directory to test project to prevent setup from finding repo's own config
- Verifies setup execution by checking for "Running `trie setup`" banner in output
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_does_not_run_setup_when_user_declines_prompt fingerprint=2b88a1a18da864f17d833277406db5bf219c9e374d807aafa36d720cb4263986 body_fp=4bd491f22accec5dd473f6297d76d879e3ec0c0b3c46ac5a2b43818e65535ad3 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a -->
Verifies that the CLI init command respects user's decline of the interactive setup prompt and still shows instruction.

- Patches `_is_interactive` to simulate TTY environment
- Uses `--no-install-hooks` to isolate setup prompt from pre-commit hook prompt
- Simulates user declining with "n\n" input
- Confirms setup doesn't run but instruction remains in output
<!-- trie:end -->