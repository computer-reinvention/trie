---
trie_version: 0.1.9
source: trie/workflow_install.py
file_fingerprint: 030b58e8ed76cd9cc0a2f2e48ffc0d5f3ba648c7ecd376d72ad998bdeb0b7a74
last_synced_at: '2026-07-25T06:06:00Z'
description: Install the triediff-comment GitHub workflow into a project.
defines:
- kind: module
  qualified_name: trie/workflow_install:__module__
  lines: 1-253
- kind: constant
  qualified_name: trie/workflow_install:WORKFLOW_RELPATH
  lines: 27-27
- kind: constant
  qualified_name: trie/workflow_install:WORKFLOW_MARKER
  lines: 31-31
- kind: constant
  qualified_name: trie/workflow_install:_TEMPLATE
  lines: 35-101
- kind: function
  qualified_name: trie/workflow_install:render_triediff_workflow
  lines: 104-106
- kind: class
  qualified_name: trie/workflow_install:WorkflowInstallResult
  lines: 110-115
- kind: function
  qualified_name: trie/workflow_install:_install_managed_workflow
  lines: 118-150
- kind: function
  qualified_name: trie/workflow_install:install_triediff_workflow
  lines: 153-170
- kind: constant
  qualified_name: trie/workflow_install:SYNC_BOT_RELPATH
  lines: 173-173
- kind: constant
  qualified_name: trie/workflow_install:SYNC_BOT_MARKER
  lines: 175-175
- kind: constant
  qualified_name: trie/workflow_install:_SYNC_BOT_TEMPLATE
  lines: 177-228
- kind: function
  qualified_name: trie/workflow_install:render_sync_bot_workflow
  lines: 231-233
- kind: function
  qualified_name: trie/workflow_install:install_sync_bot_workflow
  lines: 236-252
incoming_refs: 12
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
<!-- trie:section symbol=trie/workflow_install:_TEMPLATE fingerprint=82343456c6a114e940343298df500dbafaf39954c0cb15570ea93af13d20b89e body_fp=da64f37ec44f9f986e90852a0f8102b68fb809d0e92e2e666591d642f5ebe7ce source_ref=3ea919f5f84ed0ee6a6c19ac2e68c5afcc2cad37 role=config -->
Raw template string for the `triediff-comment.yml` GitHub Actions workflow, parameterised by `{marker}` and `{diffs_dir}`; comments every digest file added by the PR (not just the latest), deduped by filename.
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
<!-- trie:section symbol=trie/workflow_install:_install_managed_workflow fingerprint=3ea98e1a89b94c3cf1ae0ea44b9b429e92953b924b9eb47adf60c21be3964841 body_fp=c2c1e2a3a1db6639430dad48607ccbe64ac9f54f40ffa2477ba8659a4297ad5e source_ref=3ea919f5f84ed0ee6a6c19ac2e68c5afcc2cad37 role=domain -->
Apply the marker-fenced create/update/skip install contract for a single workflow file, returning a `WorkflowInstallResult`.

- `relpath`: path relative to `project_root` where the file is written
- `marker`: string whose presence in the existing file signals trie ownership
- `desired`: fully rendered file content to write
- `dry_run`: reports the would-be action without touching the filesystem
<!-- trie:end -->
<!-- trie:section symbol=trie/workflow_install:install_triediff_workflow fingerprint=fc0ffef6816de7aac66e7234529f26667c03c19b2f527fc6fb79bab7320aa141 body_fp=a08677bc4346a7f081cb00a86bde6c24105a451ff4638891bdf7f3cbc6a30e8c source_ref=3ea919f5f84ed0ee6a6c19ac2e68c5afcc2cad37 role=io -->
Idempotently install the triediff-comment GitHub Actions workflow file into `project_root`.

- `diffs_dir`: path (relative to repo root) where digest `.md` files are stored.
- `dry_run`: reports the would-be action without writing or creating any files.
- Returns a `WorkflowInstallResult` with action `created`, `updated`, `unchanged`, `skipped`, or `error`.
- Skips if no `.git` directory exists or if the file lacks `WORKFLOW_MARKER` (user-owned).
<!-- trie:end -->
<!-- trie:section symbol=trie/workflow_install:SYNC_BOT_RELPATH fingerprint=a7269a859e1e0e350b4f8f0f7efecf421aa5f2d1c1278ccbaeaa041cc36c9f15 body_fp=de1682a2584a551416ac6a67666571c08e55775f98f1b96d0d13de73f2bb01d0 source_ref=3ea919f5f84ed0ee6a6c19ac2e68c5afcc2cad37 role=config -->
Filesystem path constant for the sync-bot workflow file relative to the project root.
<!-- trie:end -->
<!-- trie:section symbol=trie/workflow_install:SYNC_BOT_MARKER fingerprint=75195f80ed4192f8f9095f50ba1c827c50c3c462dc66ae7d0d50212b21ee9c68 body_fp=dd3367e2c10a09ed6b71210a1497692d8abacc12ef27eede4cf8fb5e1be719e0 source_ref=3ea919f5f84ed0ee6a6c19ac2e68c5afcc2cad37 role=config -->
Marker string written as the first comment line of the sync-bot workflow file to identify it as trie-managed.
<!-- trie:end -->
<!-- trie:section symbol=trie/workflow_install:_SYNC_BOT_TEMPLATE fingerprint=9fa87285cd3e9b0746120e31af0bf49f289aeb6c88722fa5b02dca3f2caaf367 body_fp=105f9ad88295f56bd8102fad00f0985011d9f79eb674f8658ef4225955129bd1 source_ref=3ea919f5f84ed0ee6a6c19ac2e68c5afcc2cad37 role=config -->
Template string for the trie-sync-bot GitHub Actions workflow YAML, parameterised by `{marker}` and `{budget}`.
<!-- trie:end -->
<!-- trie:section symbol=trie/workflow_install:render_sync_bot_workflow fingerprint=6543d320079a3cad5144b35ce768961b1d0fdac56213b617599b0e6da2b91bb4 body_fp=71a3fe45bace834f421c8f671648bbd968dd8d66dbc52d6b8814f9900d1c835f source_ref=3ea919f5f84ed0ee6a6c19ac2e68c5afcc2cad37 role=domain -->
Render the sync-bot workflow YAML string with `budget` substituted as the per-run spend cap.

- `budget`: maximum USD spend per CI run; defaults to `5.0`.
<!-- trie:end -->
<!-- trie:section symbol=trie/workflow_install:install_sync_bot_workflow fingerprint=6ca0d4286c8db93c993c2491ead36f58e7d5456ebef697f419bd895bf634adbd body_fp=a13a286e879a1806b5dea899612ba5cf3af509489708e4e61bf5373b2b59f4cb source_ref=3ea919f5f84ed0ee6a6c19ac2e68c5afcc2cad37 role=io -->
Idempotently install the `trie-sync-bot` GitHub Actions workflow into `project_root` using marker-fenced ownership semantics.

- `budget`: per-run API spend cap baked into the rendered YAML; defaults to `5.0`
- `dry_run`: reports the action that would be taken without writing any files
<!-- trie:end -->