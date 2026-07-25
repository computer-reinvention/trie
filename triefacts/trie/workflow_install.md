---
trie_version: 0.1.9
source: trie/workflow_install.py
file_fingerprint: 5a33fbee1fb8d356c6d7d7db04504fbe9dc52ebab67452ff5400a71d14727ce4
last_synced_at: '2026-07-25T01:16:54Z'
description: Install the triediff-comment GitHub workflow into a project.
defines:
- kind: module
  qualified_name: trie/workflow_install:__module__
  lines: 1-142
- kind: constant
  qualified_name: trie/workflow_install:WORKFLOW_RELPATH
  lines: 27-27
- kind: constant
  qualified_name: trie/workflow_install:WORKFLOW_MARKER
  lines: 31-31
- kind: constant
  qualified_name: trie/workflow_install:_TEMPLATE
  lines: 33-89
- kind: function
  qualified_name: trie/workflow_install:render_triediff_workflow
  lines: 92-94
- kind: class
  qualified_name: trie/workflow_install:WorkflowInstallResult
  lines: 98-103
- kind: function
  qualified_name: trie/workflow_install:install_triediff_workflow
  lines: 106-141
incoming_refs: 11
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
<!-- trie:section symbol=trie/workflow_install:_TEMPLATE fingerprint=03e4643dd556b390be0b459076f18900e7e90d2ebeadbda6633d1f3526e105de body_fp=efdfa495ad57cb5aaf60ff5f8bf11a6b93dbe0e3eecbb2364f7d907755ff0012 source_ref=3391c752d867df7a30064fe8b6630db6123988dd role=config -->
Raw template string for the `triediff-comment.yml` GitHub Actions workflow, parameterised by `{marker}` and `{diffs_dir}`.
<!-- trie:end -->
<!-- trie:section symbol=trie/workflow_install:render_triediff_workflow fingerprint=817b837ac4a9ad92c27aab59f560c6ac28fdcc831688abc9ede255a0c16c994d body_fp=db0ea67bc39ef45ffe5496ab32f00ca1a4854df065d75b012a5a5fd7935b84e5 source_ref=3391c752d867df7a30064fe8b6630db6123988dd role=util -->
Render the triediff-comment workflow YAML string, substituting `WORKFLOW_MARKER` and a stripped `diffs_dir` into `_TEMPLATE`.

- `diffs_dir`: leading/trailing slashes are stripped before substitution.
<!-- trie:end -->
<!-- trie:section symbol=trie/workflow_install:WorkflowInstallResult fingerprint=af72f221f20351eeb9b1d8797872bcfc37baa270ed6bbeeb275300732deab298 body_fp=f3c913123cad95d0f65ed54fbc9472bb7ccafb77b162c794f805f1fa769a2067 source_ref=3391c752d867df7a30064fe8b6630db6123988dd role=model -->
Frozen dataclass holding the outcome of a single `install_triediff_workflow` call.

- `action`: one of `created`, `updated`, `unchanged`, `skipped`, or `error`
- `path`: workflow file path, or `None` when no git repo was found
- `note`: human-readable detail string, empty when not applicable
<!-- trie:end -->
<!-- trie:section symbol=trie/workflow_install:install_triediff_workflow fingerprint=1953105a07f5eca3a4bd8e79c73ad094d6d7f13faff82115e3a18f57093acf5a body_fp=a08677bc4346a7f081cb00a86bde6c24105a451ff4638891bdf7f3cbc6a30e8c source_ref=3391c752d867df7a30064fe8b6630db6123988dd role=io -->
Idempotently install the triediff-comment GitHub Actions workflow file into `project_root`.

- `diffs_dir`: path (relative to repo root) where digest `.md` files are stored.
- `dry_run`: reports the would-be action without writing or creating any files.
- Returns a `WorkflowInstallResult` with action `created`, `updated`, `unchanged`, `skipped`, or `error`.
- Skips if no `.git` directory exists or if the file lacks `WORKFLOW_MARKER` (user-owned).
<!-- trie:end -->