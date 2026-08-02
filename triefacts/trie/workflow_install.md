---
trie_version: 0.3.0
source: trie/workflow_install.py
file_fingerprint: ee60ce7f97277049fb7608ab59366864d35d8df50753980ed0e49103f7ccc2eb
last_synced_at: '2026-08-02T20:23:33Z'
description: Install the triediff-comment GitHub workflow into a project.
defines:
- kind: module
  qualified_name: trie/workflow_install:__module__
  lines: 1-222
- kind: constant
  qualified_name: trie/workflow_install:WORKFLOW_RELPATH
  lines: 27-27
- kind: constant
  qualified_name: trie/workflow_install:WORKFLOW_MARKER
  lines: 31-31
- kind: constant
  qualified_name: trie/workflow_install:_TEMPLATE
  lines: 35-152
- kind: function
  qualified_name: trie/workflow_install:render_triediff_workflow
  lines: 155-157
  signature: 'def render_triediff_workflow(diffs_dir: str) -> str'
- kind: class
  qualified_name: trie/workflow_install:WorkflowInstallResult
  lines: 161-166
  signature: class WorkflowInstallResult
- kind: function
  qualified_name: trie/workflow_install:_install_managed_workflow
  lines: 169-201
  signature: 'def _install_managed_workflow( project_root: Path, *, relpath: Path, marker: str, desired: str, dry_run: bool = False, ) -> WorkflowInstallResult'
- kind: function
  qualified_name: trie/workflow_install:install_triediff_workflow
  lines: 204-221
  signature: 'def install_triediff_workflow( project_root: Path, *, diffs_dir: str, dry_run: bool = False, ) -> WorkflowInstallResult'
incoming_refs: 15
outgoing_refs: 0
---
<!-- trie:section symbol=trie/workflow_install:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=5c92a8d686643494ef9749da7beca200adce0021d165e97f77fae49810cdf550 source_ref=3391c752d867df7a30064fe8b6630db6123988dd role=orchestration -->
Install the `triediff-comment` GitHub Actions workflow into a project's `.github/workflows/` directory with idempotent, marker-fenced ownership semantics.

- `WORKFLOW_RELPATH` — relative path where the workflow file is written
- `WORKFLOW_MARKER` — comment string that marks the file as trie-managed; absence means user-owned and never touched
<!-- trie:end -->
<!-- trie:section symbol=trie/workflow_install:WORKFLOW_RELPATH fingerprint=6e6597adca5022b45f4af60b22c0c4d033f7a37ece5db4cf2f6880aad53448e4 body_fp=3dd94f8ce4285a14a0e478ee83dd37dea082dab677594a23e785d65787d4c8a0 source_ref=3391c752d867df7a30064fe8b6630db6123988dd role=config -->
Relative `Path` constant pointing to `.github/workflows/triediff-comment.yml`, used as the install target for the managed workflow file.
<!-- trie:end -->
<!-- trie:section symbol=trie/workflow_install:WORKFLOW_MARKER fingerprint=9b09eb6f3644af3aafac7cb3afdb1cb50f7f959b64039a284c439eeb292e63d3 body_fp=4429b62a2192f71004303b073d1b2713ecc09ead9e463f25bcaaaf1c42cc5cd3 source_ref=3391c752d867df7a30064fe8b6630db6123988dd role=config -->
Sentinel comment string written as the first line of managed workflow files to distinguish trie-owned files from user-owned ones.
<!-- trie:end -->
<!-- trie:section symbol=trie/workflow_install:_TEMPLATE fingerprint=08a36d31db98d9017b8abe9deca64ae562dd710725a3a8e3879fd258433709a6 body_fp=ce3f890c9dece91072b2e10b1e95786a01a7c3afb945e01cf9d9403bec06c647 source_ref=a1ce0b959117ddc928b9137655b1542ede698955 role=config -->
Raw template string for the `triediff-comment.yml` GitHub Actions workflow, parameterised by `{marker}` and `{diffs_dir}`; comments every digest file added by the PR (not just the latest), deduped by filename, with an awk pass that reformats the digest into a markdown table before posting.
<!-- trie:end -->
<!-- trie:section symbol=trie/workflow_install:render_triediff_workflow fingerprint=817b837ac4a9ad92c27aab59f560c6ac28fdcc831688abc9ede255a0c16c994d body_fp=aabf9405046e14fe35131f003b53571c0e915a2b13b4e4686751d67ce90f737a source_ref=3391c752d867df7a30064fe8b6630db6123988dd role=util -->
## `def render_triediff_workflow(diffs_dir: str) -> str`

Render the triediff-comment workflow YAML string, substituting `WORKFLOW_MARKER` and a stripped `diffs_dir` into `_TEMPLATE`.

- `diffs_dir`: leading/trailing slashes are stripped before substitution.
<!-- trie:end -->
<!-- trie:section symbol=trie/workflow_install:WorkflowInstallResult fingerprint=af72f221f20351eeb9b1d8797872bcfc37baa270ed6bbeeb275300732deab298 body_fp=93fdea76b49350daf48e6464f218abeffc2f950be7a1d5f790d09f7467fef9de source_ref=3391c752d867df7a30064fe8b6630db6123988dd role=model -->
## `class WorkflowInstallResult`

Frozen dataclass holding the outcome of a single `install_triediff_workflow` call.

- `action`: one of `created`, `updated`, `unchanged`, `skipped`, or `error`
- `path`: workflow file path, or `None` when no git repo was found
- `note`: human-readable detail string, empty when not applicable
<!-- trie:end -->
<!-- trie:section symbol=trie/workflow_install:_install_managed_workflow fingerprint=3ea98e1a89b94c3cf1ae0ea44b9b429e92953b924b9eb47adf60c21be3964841 body_fp=b7ff8c0ab0172caf435479f735d469d4d684ba636cf4f29b8cca30449fa6fec3 source_ref=3ea919f5f84ed0ee6a6c19ac2e68c5afcc2cad37 role=domain -->
## `def _install_managed_workflow( project_root: Path, *, relpath: Path, marker: str, desired: str, dry_run: bool = False, ) -> WorkflowInstallResult`

Apply the marker-fenced create/update/skip install contract for a single workflow file, returning a `WorkflowInstallResult`.

- `relpath`: path relative to `project_root` where the file is written
- `marker`: string whose presence in the existing file signals trie ownership
- `desired`: fully rendered file content to write
- `dry_run`: reports the would-be action without touching the filesystem
<!-- trie:end -->
<!-- trie:section symbol=trie/workflow_install:install_triediff_workflow fingerprint=fc0ffef6816de7aac66e7234529f26667c03c19b2f527fc6fb79bab7320aa141 body_fp=4de863b32e9687f6218293e1852656693d3e6f8057f188c1c62d636a3e1e19c0 source_ref=3ea919f5f84ed0ee6a6c19ac2e68c5afcc2cad37 role=io -->
## `def install_triediff_workflow( project_root: Path, *, diffs_dir: str, dry_run: bool = False, ) -> WorkflowInstallResult`

Idempotently install the triediff-comment GitHub Actions workflow file into `project_root`.

- `diffs_dir`: path (relative to repo root) where digest `.md` files are stored.
- `dry_run`: reports the would-be action without writing or creating any files.
- Returns a `WorkflowInstallResult` with action `created`, `updated`, `unchanged`, `skipped`, or `error`.
- Skips if no `.git` directory exists or if the file lacks `WORKFLOW_MARKER` (user-owned).
<!-- trie:end -->