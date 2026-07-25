---
trie_version: 0.1.9
source: tests/test_init.py
file_fingerprint: 38dd348242eea118a3307f734b60263edca9591ac74f687152ecadc46209c008
last_synced_at: '2026-07-25T00:24:00Z'
defines:
- kind: module
  qualified_name: tests/test_init:__module__
  lines: 1-418
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
  qualified_name: tests/test_init:test_init_errors_on_unsupported_without_force
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
- kind: function
  qualified_name: tests/test_init:test_hook_block_includes_diff_write
  lines: 390-417
incoming_refs: 0
outgoing_refs: 46
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
<!-- trie:section symbol=tests/test_init:python_project fingerprint=3c46e839304076e37baaf33fc2ba0f6ef1d265bd95d3c382ef38e43bab36600e body_fp=9344af08d0dd3162bbbe796c6ab8b745191a07c594a6fb90ad3e7d145605307f source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Creates a temporary directory containing a minimal `pyproject.toml` file for testing Python project initialization.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:empty_dir fingerprint=55e26967baf902dc0a8bf6551bb7512f4710c8d3dde4d3799903becb872bb499 body_fp=205081c3c661a8f134d2f1acc88b1db58e3457f48a1fd41e679854078241a636 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Pytest fixture that returns an empty temporary directory for testing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_detect_pyproject fingerprint=4c45a248121bb657bbe48576422a5307631c19c084c34cf9e80982c99e328c01 body_fp=80df7756428ca2683ced051a85c403eae3d9f199f82f3239a93fe7e4d970d633 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Tests that `_detect_python_project` returns `["pyproject.toml"]` when a pyproject.toml file exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_detect_loose_py_files fingerprint=e90cdfa099c11d1f477d766305d7201bf4a4ae4a439fc5a43f834e3c302f33fd body_fp=e5969975e63658c9dfb7185d7057d1df24c069e5a8ba63d293a5ebab04b1d786 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Tests that `_detect_python_project` identifies directories containing Python files as Python projects.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_detect_one_level_deep_py_files fingerprint=8e52c90d54d44272aa2d159ebcbe0b63f110f5a0cf04f2ce64c285af0910e156 body_fp=dad3050e29f9459621b7248d203c6cd8bbeedb0800a8a493ac0b4f3f19084d1b source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Verifies `_detect_python_project` detects Python files nested one directory deep as a Python project marker.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_detect_returns_empty_for_non_python fingerprint=6d714012a2bcfdf712ad18a26ab684641daeadc4190d82e25a4d928b35712006 body_fp=177423b78899ba6a648872ccc13170e0c436d8cc4e656159d06a8187aaad3afd source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Verifies _detect_python_project returns empty list when directory contains no Python project markers.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_gitignore_creates_when_missing fingerprint=1f4d87462de9b7bdbf611d8698fbc43a86738f978ad30b887af2b4918de50e0d body_fp=1e716b705fa4fa637cf211f3e4bcf7a350dd1794a6bd633840af65cf9c9db1ae source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Tests that `_ensure_gitignore_entry` creates a new `.gitignore` file with the trie entry when none exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_gitignore_appends_when_missing_line fingerprint=4edfb60332c83003e3f23a8568441be9d3849cda4943852a54e390bcb4d8c58b body_fp=11135ffd29e2fe93c980eb2ecb2cf95bff4e25b7f47c83c154633c40b3b6545d source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Tests that `_ensure_gitignore_entry` appends the trie line when gitignore exists but lacks it.

- Creates existing gitignore with other content
- Verifies function returns True indicating modification was made
- Confirms trie entry appears in final gitignore content
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_gitignore_no_dup_when_already_present fingerprint=d23d183ba7712f789eb3b07c2286b3c2e05a3bcca0e617da249f0fc190106b2a body_fp=6f6ac872df9816d9fa2e2b1250390a7e4bbf42a3ad1a11a249bd726fad090554 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Tests that _ensure_gitignore_entry returns False and avoids duplicating entries when the gitignore line already exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_gitignore_treats_trailing_slash_as_match fingerprint=4a4f76bafbcc8df0cee594ca8deb071b79390b606e9a0905f9a0b675a6f6d04e body_fp=11bbe7b46c527bc0f427953094bbceb2619620b222e925d92a820ef7f80dc6a2 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Tests that `_ensure_gitignore_entry` treats `.trie` and `.trie/` as equivalent matches.

- Returns False when `.trie` already exists, even when checking for `.trie/`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_gitignore_handles_no_trailing_newline fingerprint=a48d6e36ac66a29e6f7efd70a5ab6c8e0c3b9d55dfc47cc523e3309e2450d809 body_fp=7df6dad69bd04b3ecfdc759724bb231f9e866855094e830bca8fe4fca60e30f2 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Tests that `_ensure_gitignore_entry` correctly appends to a .gitignore file lacking a trailing newline.

• Verifies the function adds both a newline and the trie entry
• Confirms existing content is preserved
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_happy_path fingerprint=b86a107b08f2025c14debb7d7fcc47cd753ee00c4e932ef900f9e4658da5f5ea body_fp=5b70c79a04f58b89db9890a685f2b826ead148c5b64df53e008c7ace8f9ca490 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Tests successful project initialization, verifying config file creation, gitignore setup, and Python project detection.

- Validates trie.toml creation and gitignore entry addition
- Confirms pyproject.toml is detected as a Python project marker
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_errors_on_unsupported_without_force fingerprint=1acf0f97f1ac873068b9b3f81414311d1cb3908ed6f791863d2bdc1a154e112e body_fp=fb0c81817f0e5f7f9a8ee32c15ce0a5fd2fd1825791a97d416b7041da814c2e8 source_ref=83a82c26e1f4e7fdeba880b286a81c0302c804c1 role=test -->
Assert that `init_project` raises `InitError` matching "does not look like a supported project" when the directory contains no Python indicators and `force` is not set.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_force_overrides_detection fingerprint=0e7743bfb02091b186cbf1edf0fc412e9e29c88784df204666aae28d8c8bb074 body_fp=8c3aa583f95605df5ef239ec3e5e2db3b585f256fff897c3f3192e0eff15cbef source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Tests that `init_project` succeeds in non-Python directories when `force=True` is specified.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_refuses_overwrite fingerprint=4db7660d8bf07488f7c772980015a065889b8921f1a8506c75e14a2e81f53e5e body_fp=157eb17d7fc5cbf9de341f5c211992a970cf3b142f6cd61881ca052de3cc795a source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Tests that init_project raises InitError when trie.toml already exists without force flag.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_force_overwrites fingerprint=866270164c88e6e1aef038e336204617c2de1b1a8802e7cf03b6cf441bf3154b body_fp=3cacf7bab7134e06385d37895696a8ad77405d7806a41a5720ec36a13bfe400e source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Verifies that `init_project` with `force=True` overwrites an existing trie.toml file with fresh configuration content.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_runs fingerprint=ab2e32568377a6f65e5c360ea9ccde1d62a1277e3573a0fa790303b8041b7693 body_fp=fe38231986db2b988e218e69303fd3a44d054ff03f7753d49b4d5448e039dbb5 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=cli-interface -->
Tests that CLI `init` command successfully initializes a Python project and creates configuration file.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_errors_on_existing fingerprint=fa25600301629b323b3d18996e88cc8d48dabf1eb750a8da0d4483f05140b0e0 body_fp=b73bf09ba72f4618d56c34d9ffb542b3e8cf21c1ef64cf17ee3e1794671318d1 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Verifies CLI init command exits with error code 1 when config file already exists.

- Sets up existing config via `init_project()`, then invokes CLI to confirm rejection
- Checks both exit code and error message content
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_force_succeeds fingerprint=9b36865c88174666eda6c668b5ba26711e69b69ebb8305200bae925c8c8d6fa5 body_fp=a4e4fa59555d31389fbe6853392c8fa55c3eea2a08383a89efe64e57dd78dfd2 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Verifies that CLI init command succeeds with --force flag when trie.toml already exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_runs_scan_by_default fingerprint=24955c7d7458436caac101a5e0c66a9444c6863571676384b0315562ff202e97 body_fp=da7b804beeb5ef4d57e8ec0e4f2431dc198477cd20f4809151e4dfe50ed04d68 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Tests that init_project runs a scan by default and creates graph database.

- Creates a Python file with a function
- Verifies scan_ran flag is True
- Confirms scan metrics are populated
- Checks graph.db file exists in .trie directory
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_no_scan_skips_graph_db fingerprint=8a43923d811342cd52c6745b26f45fe229f5ef19c7f24d1f2de59b0c7fdfc80d body_fp=5ad10d8236b34348a85c707fc1aa26c9fde49d686a910f6459efd8686e5f0492 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Tests that `init_project` skips graph database creation when `run_scan=False`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_install_hook_writes_new_pre_commit_when_git_repo fingerprint=b18c0c04fcf836bcab6ffd1e5ab09560a6380646800a7832ec95a5287ec39fdf body_fp=d59ba76a04edc78688b27178a9e665c4beb17bf96f4446a430dee09c70a43d73 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Tests that `install_pre_commit_hook` creates a new git pre-commit hook in a git repository.

- Verifies hook contains `PRE_COMMIT_HOOK_MARKER`, runs `trie -q lock-check` before `trie -q verify`, and is executable
- Returns `installed=True`, `strategy="git_hook"`, and valid `hook_path`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_install_hook_appends_to_existing_pre_commit fingerprint=ab1aa18038215b7dde8e92f583a36876384f058fd046a737eb33efc13757f132 body_fp=ad070b5c2a3523a8c21bc937ba43ce7d8802b00bdf2ee370c025a346a455b118 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Tests that `install_pre_commit_hook` appends trie commands to an existing pre-commit hook while preserving the original content.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_install_hook_idempotent fingerprint=932f9f174cf0d9107b44558c658efcda9a1f2f0d3d2957e5cac9a264d035a6ed body_fp=df46b625758fc2dab7db2d4e1215466143a9675a0b6483081997078f5298d331 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Verifies that `install_pre_commit_hook` returns `installed=False` when the hook is already present.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_install_hook_skips_when_pre_commit_framework_present fingerprint=8d3cba0514be0b0dcc8b782d996547f4ec7455d48a6444a185182945288ef03f body_fp=70b8fd6a815a89c78294ac3a96698045ae24ec31dc1e93c890997c6a6404339d source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Tests that `install_pre_commit_hook` skips installation when a pre-commit framework configuration file is already present.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_install_hook_skips_when_not_a_git_repo fingerprint=e1ec9ca6657e1a57abc01cfc0df3ecf1b8a7372169be2bb262b0e43ecb25796b body_fp=22ce65508cdc11af649c54a78c7568dea45f7caa584a7fb22960175b6e310bd7 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Verifies install_pre_commit_hook returns False with "none" strategy when project lacks .git directory.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_project_install_hooks_in_git_repo fingerprint=5716a2dfe4f721afce56185d6a4fcb00e454fd33a736f545854f7e6dd2024baa body_fp=d78ad7656e9a3381db057f6d98311099c0ea0e6a8dad6c3ca1b4ae7aa1916250 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Tests that `init_project` installs pre-commit hooks when `install_hooks=True` and the directory is a git repository.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_init_project_default_does_not_install_hooks fingerprint=08c6aa12b1373f0efa90b2986a651f58d0f606eaa21bd74e09c181faaf89465c body_fp=6ba600abf03e8d19c72645403e135794c9767ead770ec9125c04e7019ea19690 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Verifies init_project does not install pre-commit hooks by default even in git repositories.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_install_hooks_flag_in_git_repo fingerprint=39007456c6905639e7e061e74c3a64caa550090cb28f73e42319da4cadc04756 body_fp=c082178ee700289aa225c1728e7c3241fd18fa3108eba50172106d1ebf0f413d source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Tests that `trie init --install-hooks` successfully installs pre-commit hook in a git repository.

- Verifies CLI exit code is 0 and output mentions hook installation
- Confirms pre-commit hook file is created in `.git/hooks/`
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_no_install_hooks_flag_skips fingerprint=3bcfccd46e0dbd0a09ec4459c018efd346d2d22b19bafbab699ef7f53576b401 body_fp=f52c1e46b76614061da1e2559bd8a30d1e339c74666e75c345b4a485ef0d0e28 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Tests that CLI init with `--no-install-hooks` flag skips pre-commit hook installation.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_framework_path_prints_snippet fingerprint=e3019388f23b97c17694c0277d5da5a0966c051b358a4d2556b544878b189455 body_fp=bc16768f8eabe22eb14b49e0862d3269c76cc2c2902263990a111a597d3fe2c8 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Tests that CLI init with --install-hooks prints pre-commit framework snippet when .pre-commit-config.yaml exists.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_non_interactive_skips_prompt fingerprint=1a209efb2677a41cc6651c35e4407517de6d2cc3b87c511bfb0ea3b7b999385f body_fp=6a5e0f0787d0028c493d32dfc8714f2afc830e59abfaad85648d5dcff6682352 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=cli-interface -->
Verifies that CLI init command completes successfully in non-interactive environments without blocking on prompts.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_prints_scan_summary fingerprint=b7d2cd4f6fb563c5b409eb18edff4cfe29ddb0ea702ca49ab2ce7d4da427919b body_fp=d4ca75057edfa3d44b8e5734e65f56b718881211d8cfff81e8cb0eb378d88d05 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Verifies that CLI init command outputs scan statistics after completing project initialization.

- Creates a Python file in the test project before running init
- Asserts that output contains "scanned" and "symbols" text indicating scan summary was printed
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_prints_setup_instruction_in_next_steps fingerprint=36b504ae41a1d76a4264c78b120d4ab32417d40a29c041fd7b8b98b83f4c4014 body_fp=8da1ea18003307729d0f6a991821a88e82380910aa2e306e9ffb5b941d8492b8 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Verifies that CLI init always displays "trie setup" instruction in next steps output.

- Tests fallback guidance for non-TTY environments and declined prompts
- Asserts presence of "Next steps:" and "trie setup" strings in command output
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_does_not_run_setup_in_non_interactive_env fingerprint=932d32e892605ad53ea8a369e542e2db3929656966e8dcba24c5046317966fc0 body_fp=d550920cb183c1cf004b431b35458573896572b9611cd0bfe06d0a8c677eee0f source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=agent-integration -->
Verifies that `trie init` in non-interactive environments suppresses the setup prompt and never auto-runs `trie setup`.

- Checks absence of setup banner in output
- Confirms no MCP config files are written to project root
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_runs_setup_when_user_accepts_prompt fingerprint=75aaed2bda52d5c9835ea382d06aa18b2ede4765c03f92f8a0b6e27efa30d696 body_fp=1d56842c4c85325afc975fe155cc76d677d3dc92216fff6aad9062bd55b92784 source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Tests that the `trie init` command automatically runs `trie setup` when user accepts the interactive prompt.

- Patches `_is_interactive` to simulate TTY environment
- Uses `--no-install-hooks` to isolate setup prompt from pre-commit hook prompt  
- Verifies setup execution by checking for "Running `trie setup`" banner in output
- Changes working directory to test project to prevent setup from modifying trie repo itself
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_cli_init_does_not_run_setup_when_user_declines_prompt fingerprint=2b88a1a18da864f17d833277406db5bf219c9e374d807aafa36d720cb4263986 body_fp=40c757ce965b70c083f760acd74cb81ec53dc3bbeb4285e8fdd8082be1c3a71a source_ref=0f97acda485ff7a046c788feb9cbfd63ccd9448a role=test-infrastructure -->
Tests that declining the setup prompt in `trie init` skips auto-setup while preserving manual instruction.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_init:test_hook_block_includes_diff_write fingerprint=bc9f4d7d98243a3ec2077e4aa65b23d319d34b3b1ef75cec532ed1a14ff75a77 body_fp=14f9abe11e16b5a534fed521c39fb291c886a8d09f8c5a869c41b32fe59032d1 source_ref=62122c53380f7912b9b35093f36c531b681820bb role=test -->
Assert that `PRE_COMMIT_HOOK_BLOCK` contains `trie -q diff --write` and `git add TRIE_DIFF.md triediffs`, that the diff-write command appears after `trie -q verify`, and that the diff-write line is non-blocking (no `|| exit`).
<!-- trie:end -->