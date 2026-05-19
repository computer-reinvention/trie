---
trie_version: 0.1.1
source: trie/hook_install.py
file_fingerprint: 7340943fc0bc65b8ec0494c43ed59bb271be3a2571fc20ca736adde2f12da2bf
last_synced_at: '2026-05-19T10:40:51Z'
description: Turn-boundary hook installation for coding agents.
defines:
- kind: module
  qualified_name: trie/hook_install:__module__
  lines: 1-339
- kind: constant
  qualified_name: trie/hook_install:Action
  lines: 35-35
- kind: class
  qualified_name: trie/hook_install:HookInstallError
  lines: 38-39
- kind: class
  qualified_name: trie/hook_install:HookApplyResult
  lines: 43-55
- kind: class
  qualified_name: trie/hook_install:HookTarget
  lines: 59-75
- kind: constant
  qualified_name: trie/hook_install:_OPENCODE_PLUGIN_FILENAME
  lines: 83-83
- kind: function
  qualified_name: trie/hook_install:_render_opencode_plugin
  lines: 86-124
- kind: constant
  qualified_name: trie/hook_install:TARGETS
  lines: 133-195
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

<!-- trie:section symbol=trie/hook_install:Action fingerprint=6d5466b453e0912edae50fab1848c782530de9137450b5c33b3682dc80488f21 body_fp=32279c251ea94e7209608bc60332aa0dfffbaa779e46e44c24f4c3e7c25593b4 source_ref=a445360f433e823758f976fd90cbed83047ba05a -->
## `Action = Literal["created", "updated", "skipped", "preview", "error", "needs_manual_setup"]`

Type alias enumerating all possible outcomes of a hook install operation.
<!-- trie:end -->

<!-- trie:section symbol=trie/hook_install:_OPENCODE_PLUGIN_FILENAME fingerprint=7442e6e578a889b0767a95dd3881ed665d3e6834945f3fa54cb3a7c6aceb8925 body_fp=3f12210b383fb1a0bb1b682f931a559c516dddbfc7f60f7d86a63e31b423d629 source_ref=a445360f433e823758f976fd90cbed83047ba05a -->
## `_OPENCODE_PLUGIN_FILENAME = "trie-refresh.ts"`

Filename of the generated opencode plugin TypeScript file.
<!-- trie:end -->

<!-- trie:section symbol=trie/hook_install:TARGETS fingerprint=0c2eda73613bdc004e4565b9007fc5d998c11469e84864f569dcff324137d7c9 body_fp=5d9d8c8220a9cb571754e9ceb1b19c6258c3c4a92368e4c2033283035e1c459c source_ref=a445360f433e823758f976fd90cbed83047ba05a -->
## `TARGETS: dict[str, HookTarget]`

Registry mapping agent slug to its `HookTarget` descriptor for all known turn-boundary hook targets.

- Agents without automated hook support carry `manual_instructions` and no `render_contents`.
- Every key must also exist in `trie.mcp_install.TARGETS` for unified setup reporting.
<!-- trie:end -->

<!-- trie:section symbol=trie/hook_install:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=8cc318cc8763705b8bfe040c5a741c7c6757309e2f4f59ae03460752cbe23250 source_ref=a445360f433e823758f976fd90cbed83047ba05a -->
## `hook_install`

Install turn-boundary hooks for coding agents, keeping the trie graph current after each agent turn.

- `TARGETS`: registry of all known agents; only `opencode` supports automated install
- `install()`: entry point for multi-target hook application
- `apply_one()`: materialises or previews a single target's hook file
- Agents without automated hook support return `needs_manual_setup` with human-readable instructions
<!-- trie:end -->