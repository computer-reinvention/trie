---
trie_version: 0.1.5
source: trie/hook_install.py
file_fingerprint: 4c45a4c792c5b6bae87ec84e58b88d2ad578752f9f4a79108b7a66ac3c0e32a5
last_synced_at: '2026-05-23T23:48:26Z'
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
<!-- trie:section symbol=trie/hook_install:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=1cb4ec0fd402069df93fdb807bdc808f80b8ea8cdafcb4148ff5f04b8bd8e166 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 -->
## `trie/hook_install`

Install turn-boundary hooks for coding agents, keeping the trie graph current without manual intervention.

- `TARGETS`: registry of all known agents; only `opencode` supports automated install
- `Action`: one of `created`, `updated`, `skipped`, `preview`, `error`, `needs_manual_setup`
- Agents without hook automation return `needs_manual_setup` with human-readable instructions
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:Action fingerprint=6d5466b453e0912edae50fab1848c782530de9137450b5c33b3682dc80488f21 body_fp=7de4d868bc0e0da1f5f12ef18124e47ef1a909900d61025b71af2038a2662d14 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 -->
## `Action = Literal["created", "updated", "skipped", "preview", "error", "needs_manual_setup"]`

Type alias for the discrete outcomes of a hook install operation.
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:HookInstallError fingerprint=d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1 body_fp=def629b887bc0bde640d8ffea0f4fc87b06111cd34fafe77169d7d3058073542 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 -->
## `HookInstallError`

Raised by `install` when an unknown hook target name is requested or no agents are detected.
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:HookApplyResult fingerprint=d59e0db810a8f40ec1fa7957cfd958de8ecc47599cb7e029e28289ff8599c846 body_fp=64bb6880007cca02097a49639d9b9e8ced924877c6c3eecc2a0f8ae9172fca92 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 -->
## `HookApplyResult`

Immutable outcome record for a single hook install operation against one agent target.

- `action`: one of `created`, `updated`, `skipped`, `preview`, `error`, `needs_manual_setup`
- `detail`: human-readable notes; carries manual setup instructions when `action == "needs_manual_setup"`
- `path`: `None` when no automatable path exists for the target
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:HookSupportFile fingerprint=f2b9c5f661daad56cefaee809effd0b86de91e09d125e5ec53b64645ec4b297c body_fp=935f6e396ad8de9077ef7c61825fc3ebde55a013f29134c32e3f2e20596c53b8 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 -->
## `HookSupportFile`

Describes a secondary file written silently alongside the primary hook plugin file.

- `relative_path`: path segments joined under the project root
- `render_contents`: called with project root; returns file contents as text
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:HookTarget fingerprint=6f8d90568ee48ee5845d4626975f5a865d71f5e8b79f084815089f8681ef3e12 body_fp=04d7d7f6f4090bae865ec3c8af420c2f25effb89a15b1147b25d9919f9562db2 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 -->
## `HookTarget`

Describe one agent's automatable (or manual-only) turn-boundary hook surface.

- `relative_path`: project-root-relative path segments where the plugin file lands; `None` means no automated install.
- `render_contents`: called with `project_root` to produce the plugin file text; `None` triggers `needs_manual_setup`.
- `manual_instructions`: human-readable steps surfaced when automation is unavailable.
- `support_files`: ancillary files written transparently by `apply_one` under the same idempotency rules.
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:_OPENCODE_PLUGIN_FILENAME fingerprint=7442e6e578a889b0767a95dd3881ed665d3e6834945f3fa54cb3a7c6aceb8925 body_fp=b4daa185138a507caf13675666b75dcc80e6f9d7219881c678c2b4f54029474c source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 -->
## `_OPENCODE_PLUGIN_FILENAME = "trie-refresh.ts"`

Filename of the opencode plugin file written under `.opencode/plugins/`.
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:_render_opencode_plugin fingerprint=2124c7400ce40dcbe5268bec6afb9f79f933b518b9a420739102174413aadae9 body_fp=35f7bd04584a9d0ab3f004dfb3865e024753c7c4402402d2ed12c0a212573526 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 -->
## `_render_opencode_plugin(_project_root: Path) -> str`

Return the TypeScript source for the opencode plugin that runs `trie refresh --after-turn` on every `session.status` idle event.

- Listens only for `session.status`; ignores deprecated `session.idle` to prevent double-firing.
- Uses `.quiet()` to suppress Bun shell output in the opencode TUI.
- Exports a v1 `PluginModule` object (`{ id, server }`) required for path-plugin resolution.
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:_render_opencode_package_json fingerprint=f27176a9598f9a874b8858a56a2f9b2bf6bcbbc273719242e1c3adcaa000bf2a body_fp=4142bd26f800b353265b41c68addaa3c94bf8596414f7521295cf21d197458a8 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 -->
## `_render_opencode_package_json(_project_root: Path) -> str`

Render a `.opencode/package.json` that pins `@opencode-ai/plugin` to `"latest"`, preventing bun from writing a broken `"local"` version sentinel that silently kills opencode sessions.
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:TARGETS fingerprint=7eb650c1091fe74c8c5781751a1c3aba97b671ce9d6ea1b316bfb82060ccaea3 body_fp=e27a763ba34919d4d582b30f48712d06df3361f295ecf36bd4fd0b8dfc9de816 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 -->
## `TARGETS: dict[str, HookTarget]`

Registry mapping agent slug to its `HookTarget`; only `"opencode"` has automated install; all others carry `manual_instructions` and return `needs_manual_setup`.

- Slugs must match keys in `trie.mcp_install.TARGETS` for `trie setup` pairing.
- `"opencode"` includes a `package.json` support file to pre-empt `@opencode-ai/plugin@local` failures.
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:HookInstallPlan fingerprint=baa3478a6300ba11090a4751af386c60014082cfdacfed5157e780649ad9373d body_fp=40d3ab2fe7a93e9eb4c024dc7d5c0e8c4a6f007fe3aafbb878db99d62e57102a source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 -->
## `HookInstallPlan`

Aggregate result of an `install` call across one or more hook targets.

- `results`: populated with one `HookApplyResult` per resolved target.
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:install fingerprint=5fe181bd36c946a52447bddaed8d61ca578458f4d5caa90b8d33b766f90fffec body_fp=020280b26d4c09b327909eaff97514a581568e9a248fa84e5c164684eec5a532 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 -->
## `install(*, target_names: list[str] | None, install_all: bool, print_only: bool, dry_run: bool, project_root: Path) -> HookInstallPlan`

Apply turn-boundary hooks for one or more targets, returning a `HookInstallPlan` with per-target results.

- `target_names`: explicit slugs; raises `HookInstallError` if any are unknown.
- `install_all`: overrides `target_names`; selects every registered target.
- `target_names=None, install_all=False`: auto-detects installed agents via `mcp_install.detect()`.
- Agents without automation produce `needs_manual_setup` results, not errors.
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:apply_one fingerprint=05838fb0e3219a8d8d7aa3e2f615755e3e98b784efa6949ae5fd585a87f6adaf body_fp=c1ead57cde21471a0fd1b9cfb69603ee18c5f2fda988642c0322174666dfc756 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 -->
## `apply_one(target: HookTarget, project_root: Path, print_only: bool, dry_run: bool, *, scope: Scope = "project") -> HookApplyResult`

Install or preview the turn-boundary hook file for a single `HookTarget`, with idempotency and support-file handling.

- `print_only`: returns `preview` action without touching the filesystem.
- `dry_run`: previews after the idempotency check; still writes support files if contents match.
- `scope`: accepted for API symmetry with `mcp_install.apply_one`; currently ignored.
- Returns `needs_manual_setup` when `target.render_contents` or `target.relative_path` is `None`.
- Returns `skipped` when existing file matches generated contents; still writes support files.
- Support-file write notes are appended to `HookApplyResult.detail`.
<!-- trie:end -->
<!-- trie:section symbol=trie/hook_install:_apply_support_files fingerprint=db30752fe89cf626824026104a5750b0cb0ffeeacd5ddb86cdd79d485feee1f0 body_fp=f21f1e30999fac494ce9b24b15432c598773a645043d28fa085b29910222b1a2 source_ref=cb692e0d7dc84ae8309d2b609725bd11b6f84389 -->
## `_apply_support_files(files: tuple[HookSupportFile, ...], project_root: Path) -> list[str]`

Write each `HookSupportFile` under `project_root`, returning human-readable status notes per file.

- Write failures are caught and noted, never raised; the primary hook result is unaffected.
- Returns one string per file: `"<rel>: created"`, `"updated"`, `"up to date"`, or `"write failed (<exc>)"`.
<!-- trie:end -->