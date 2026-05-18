---
trie_version: 0.1.1
source: trie/hook_install.py
file_fingerprint: 7340943fc0bc65b8ec0494c43ed59bb271be3a2571fc20ca736adde2f12da2bf
last_synced_at: '2026-05-16T12:25:59Z'
description: Turn-boundary hook installation for coding agents.
defines:
- kind: class
  qualified_name: trie/hook_install:HookInstallError
  lines: 38-39
- kind: class
  qualified_name: trie/hook_install:HookApplyResult
  lines: 43-55
- kind: class
  qualified_name: trie/hook_install:HookTarget
  lines: 59-75
- kind: function
  qualified_name: trie/hook_install:_render_opencode_plugin
  lines: 86-124
- kind: class
  qualified_name: trie/hook_install:HookInstallPlan
  lines: 204-210
- kind: function
  qualified_name: trie/hook_install:install
  lines: 213-263
- kind: function
  qualified_name: trie/hook_install:apply_one
  lines: 266-338
incoming_refs: 13
outgoing_refs: 0
---
<!-- trie:section symbol=trie/hook_install:HookInstallError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=e3b3e9f037a91f3d2bbffe35bc50639f27f1fe4d6d596635216d3b125227aa90 source_ref=a445360f433e823758f976fd90cbed83047ba05a -->
## `HookInstallError()`

Raised when hook installation fails due to unknown targets or no detected agents.
<!-- trie:end -->

<!-- trie:section symbol=trie/hook_install:HookApplyResult fingerprint=d59e0db810a8f40ec1fa7957cfd958de8ecc47599cb7e029e28289ff8599c846 body_fp=ae3d4ecdf5fffe462228280a448456abb51c1a52562a2bb15f7529dbaf79a6a8 source_ref=a445360f433e823758f976fd90cbed83047ba05a -->
## `HookApplyResult`

Frozen dataclass representing the outcome of a single-target hook install operation.

- `action`: one of `created`, `updated`, `skipped`, `preview`, `error`, `needs_manual_setup`
- `needs_manual_setup`: agent is known but hook automation is unsupported; `detail` carries human-readable instructions
- `detail`: human-readable explanation; present on `skipped`, `error`, and `needs_manual_setup` actions
<!-- trie:end -->

<!-- trie:section symbol=trie/hook_install:HookTarget fingerprint=2406c03d13335a52e7fa5052a208678eafd0e30191b7fd162cda88054bc08dde body_fp=2b14c8d2d149bd3ff56f44e065dbab08fb02a9cf5d9dfa560ca5ab01d779964b source_ref=a445360f433e823758f976fd90cbed83047ba05a -->
## `HookTarget(name, display_name, relative_path=None, render_contents=None, manual_instructions='')`

Describe one agent's turn-boundary hook surface for use by `apply_one`.

- `relative_path`: tuple of path segments under project root; `None` means no automated hook.
- `render_contents`: callable producing file contents; `None` triggers `needs_manual_setup`.
- `manual_instructions`: human-readable fallback shown when automation is unsupported.
<!-- trie:end -->

<!-- trie:section symbol=trie/hook_install:_render_opencode_plugin fingerprint=f1b8f88e514808b840ce27714b7ef6ae45f4e01d76755f4113b04857af757b6f body_fp=7efe5baff06326782e2fa29c3a7d2f18246fc9a7157f16759efc51f68186bcfa source_ref=a445360f433e823758f976fd90cbed83047ba05a -->
## `_render_opencode_plugin(_project_root: Path) -> str`

Return the TypeScript source for an opencode plugin that runs `trie refresh --after-turn` on every `session.idle` event.
<!-- trie:end -->

<!-- trie:section symbol=trie/hook_install:HookInstallPlan fingerprint=baa3478a6300ba11090a4751af386c60014082cfdacfed5157e780649ad9373d body_fp=4b86b781659e477ce10e117e84c4107355424c13ff46d7cb7659ba3e9fef51ad source_ref=a445360f433e823758f976fd90cbed83047ba05a -->
## `HookInstallPlan`

Aggregate result of an `install` call across one or more hook targets.

- `print_only` / `dry_run`: mirror the CLI flags; recorded for display logic upstream.
- `results`: populated entry-by-entry as each target is processed.
<!-- trie:end -->

<!-- trie:section symbol=trie/hook_install:install fingerprint=5fe181bd36c946a52447bddaed8d61ca578458f4d5caa90b8d33b766f90fffec body_fp=cbb97e9b04ede181c6be9b3ab86a055f627d74378d1db79b89d120ccadf556fa source_ref=a445360f433e823758f976fd90cbed83047ba05a -->
## `install(*, target_names: list[str] | None, install_all: bool, print_only: bool, dry_run: bool, project_root: Path) -> HookInstallPlan`

Apply turn-boundary hooks for one or more targets, raising `HookInstallError` for unknown names.

- `install_all`: selects every entry in `TARGETS`; overrides `target_names`
- `target_names`: explicit slugs; auto-detects via MCP presence when `None`
- `print_only` / `dry_run`: passed through to `apply_one`; no files written
- Agents without automation produce `needs_manual_setup` results, not errors
<!-- trie:end -->

<!-- trie:section symbol=trie/hook_install:apply_one fingerprint=becb7077cb9ccac86fc39024af08a398ed282b78c5b6f345b65fe2740770e75b body_fp=4f3000cb202023ffe6d41c218a5ac7f7a47423495f37f9d285fedc8268bc554c source_ref=a445360f433e823758f976fd90cbed83047ba05a -->
## `apply_one(target: HookTarget, project_root: Path, print_only: bool, dry_run: bool, *, scope: Scope = "project") -> HookApplyResult`

Install or preview the turn-boundary hook file for a single `HookTarget`.

- `print_only`: returns `preview` action without touching the filesystem.
- `dry_run`: same as `print_only` but checks idempotency first.
- `scope`: accepted for API symmetry; currently ignored.
- Returns `needs_manual_setup` when `target` has no automatable hook path.
- Returns `skipped` when existing file content is identical to what would be written.
<!-- trie:end -->