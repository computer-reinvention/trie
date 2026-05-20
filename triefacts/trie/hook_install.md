---
trie_version: 0.1.2
source: trie/hook_install.py
file_fingerprint: 4c45a4c792c5b6bae87ec84e58b88d2ad578752f9f4a79108b7a66ac3c0e32a5
last_synced_at: '2026-05-20T13:55:02Z'
description: Turn-boundary hook installation for coding agents.
defines:
- kind: module
  qualified_name: trie/hook_install:__module__
  lines: 1-468
- kind: constant
  qualified_name: trie/hook_install:Action
  lines: 36-36
- kind: class
  qualified_name: trie/hook_install:HookInstallError
  lines: 39-40
- kind: class
  qualified_name: trie/hook_install:HookApplyResult
  lines: 44-56
- kind: class
  qualified_name: trie/hook_install:HookSupportFile
  lines: 60-71
- kind: class
  qualified_name: trie/hook_install:HookTarget
  lines: 75-97
- kind: constant
  qualified_name: trie/hook_install:_OPENCODE_PLUGIN_FILENAME
  lines: 105-105
- kind: function
  qualified_name: trie/hook_install:_render_opencode_plugin
  lines: 108-164
- kind: function
  qualified_name: trie/hook_install:_render_opencode_package_json
  lines: 167-196
- kind: constant
  qualified_name: trie/hook_install:TARGETS
  lines: 205-279
- kind: class
  qualified_name: trie/hook_install:HookInstallPlan
  lines: 288-294
- kind: function
  qualified_name: trie/hook_install:install
  lines: 297-347
- kind: function
  qualified_name: trie/hook_install:apply_one
  lines: 350-436
- kind: function
  qualified_name: trie/hook_install:_apply_support_files
  lines: 439-467
incoming_refs: 17
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

<!-- trie:section symbol=trie/hook_install:HookTarget fingerprint=6f8d90568ee48ee5845d4626975f5a865d71f5e8b79f084815089f8681ef3e12 body_fp=f071f13ee9ccf603f5297352200482d556a5064cd8786f6f9dc2e26213138969 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 -->
## `HookTarget(name, display_name, relative_path=None, render_contents=None, manual_instructions='', support_files=())`

Describe one agent's turn-boundary hook surface for use by `apply_one`.

- `relative_path`: tuple of path segments under project root; `None` means no automated hook.
- `render_contents`: callable producing file contents; `None` triggers `needs_manual_setup`.
- `manual_instructions`: human-readable fallback shown when automation is unsupported.
- `support_files`: ancillary files written transparently alongside the primary plugin file.
<!-- trie:end -->

<!-- trie:section symbol=trie/hook_install:_render_opencode_plugin fingerprint=2124c7400ce40dcbe5268bec6afb9f79f933b518b9a420739102174413aadae9 body_fp=73c32bcc72a69a5768dd4f6500e7fe51cd42b022ce42588b4574918c4c00b62b source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 -->
## `_render_opencode_plugin(_project_root: Path) -> str`

Return the TypeScript source for an opencode plugin that runs `trie refresh --after-turn` on every `session.status` idle event, using a default-export v1 plugin shape.
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

<!-- trie:section symbol=trie/hook_install:apply_one fingerprint=05838fb0e3219a8d8d7aa3e2f615755e3e98b784efa6949ae5fd585a87f6adaf body_fp=fd6c331acfe3798715790ead9a3255ed341e76b1872ae6e4d4ecb9ebd5b621a7 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 -->
## `apply_one(target: HookTarget, project_root: Path, print_only: bool, dry_run: bool, *, scope: Scope = "project") -> HookApplyResult`

Install or preview the turn-boundary hook file for a single `HookTarget`.

- `print_only`: returns `preview` action without touching the filesystem.
- `dry_run`: same as `print_only` but checks idempotency first.
- `scope`: accepted for API symmetry; currently ignored.
- Returns `needs_manual_setup` when `target` has no automatable hook path.
- Returns `skipped` when existing file content is identical, but still writes support files.
- Also writes `target.support_files` on successful create/update, appending notes to `detail`.
<!-- trie:end -->

<!-- trie:section symbol=trie/hook_install:Action fingerprint=6d5466b453e0912edae50fab1848c782530de9137450b5c33b3682dc80488f21 body_fp=32279c251ea94e7209608bc60332aa0dfffbaa779e46e44c24f4c3e7c25593b4 source_ref=a445360f433e823758f976fd90cbed83047ba05a -->
## `Action = Literal["created", "updated", "skipped", "preview", "error", "needs_manual_setup"]`

Type alias enumerating all possible outcomes of a hook install operation.
<!-- trie:end -->

<!-- trie:section symbol=trie/hook_install:_OPENCODE_PLUGIN_FILENAME fingerprint=7442e6e578a889b0767a95dd3881ed665d3e6834945f3fa54cb3a7c6aceb8925 body_fp=3f12210b383fb1a0bb1b682f931a559c516dddbfc7f60f7d86a63e31b423d629 source_ref=a445360f433e823758f976fd90cbed83047ba05a -->
## `_OPENCODE_PLUGIN_FILENAME = "trie-refresh.ts"`

Filename of the generated opencode plugin TypeScript file.
<!-- trie:end -->

<!-- trie:section symbol=trie/hook_install:TARGETS fingerprint=7eb650c1091fe74c8c5781751a1c3aba97b671ce9d6ea1b316bfb82060ccaea3 body_fp=a9e7242da0af0762f4b7f69def2c1b6b8f1856225576d287269d495b254004a9 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 -->
## `TARGETS: dict[str, HookTarget]`

Registry mapping agent slug to its `HookTarget` descriptor for all known turn-boundary hook targets.

- Agents without automated hook support carry `manual_instructions` and no `render_contents`.
- Every key must also exist in `trie.mcp_install.TARGETS` for unified setup reporting.
- The `opencode` entry includes a `support_files` tuple writing `.opencode/package.json` to pre-empt broken `@opencode-ai/plugin` resolution.
<!-- trie:end -->

<!-- trie:section symbol=trie/hook_install:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=8cc318cc8763705b8bfe040c5a741c7c6757309e2f4f59ae03460752cbe23250 source_ref=a445360f433e823758f976fd90cbed83047ba05a -->
## `hook_install`

Install turn-boundary hooks for coding agents, keeping the trie graph current after each agent turn.

- `TARGETS`: registry of all known agents; only `opencode` supports automated install
- `install()`: entry point for multi-target hook application
- `apply_one()`: materialises or previews a single target's hook file
- Agents without automated hook support return `needs_manual_setup` with human-readable instructions
<!-- trie:end -->

<!-- trie:section symbol=trie/hook_install:HookSupportFile fingerprint=f2b9c5f661daad56cefaee809effd0b86de91e09d125e5ec53b64645ec4b297c body_fp=e4634d62c9e8d08492566abb588978293ba4159c5270fa313cc3c6e4227a9828 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 -->
## `HookSupportFile(relative_path: tuple[str, ...], render_contents: Callable[[Path], str])`

Describe a secondary file written alongside the primary hook plugin file during `apply_one`.

- `relative_path`: project-root-relative path components for the file to write.
- `render_contents`: callable receiving project root, returning file contents as text.
<!-- trie:end -->

<!-- trie:section symbol=trie/hook_install:_render_opencode_package_json fingerprint=f27176a9598f9a874b8858a56a2f9b2bf6bcbbc273719242e1c3adcaa000bf2a body_fp=af3cd9e52c065588941ce9fc00639129fd8f928a4f19331ba8d94e7f79842d93 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 -->
## `_render_opencode_package_json(_project_root: Path) -> str`

Render `.opencode/package.json` pinning `@opencode-ai/plugin` to `"latest"` to prevent bun from writing a broken `"local"` sentinel.
<!-- trie:end -->

<!-- trie:section symbol=trie/hook_install:_apply_support_files fingerprint=db30752fe89cf626824026104a5750b0cb0ffeeacd5ddb86cdd79d485feee1f0 body_fp=75bcd59446f7a886c4a5462c422110d58d42ed75a688a6eed80fba37ca6bc241 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 -->
## `_apply_support_files(files: tuple[HookSupportFile, ...], project_root: Path) -> list[str]`

Write each support file idempotently and return human-readable status notes per file.

- Failures are caught and noted rather than raised, so a bad support-file write never masks a successful primary hook install.
<!-- trie:end -->