---
trie_version: 0.1.9
source: app/src/components/Editor/TabStrip.tsx
file_fingerprint: adf15d9db08603ba2154c3054b0bed9bf923c28e1b23c227696216523fb24a77
last_synced_at: '2026-06-17T16:37:46Z'
defines:
- kind: function
  qualified_name: app/src/components/Editor/TabStrip:AttentionIcon
  lines: 19-27
- kind: function
  qualified_name: app/src/components/Editor/TabStrip:GraphIcon
  lines: 30-39
- kind: function
  qualified_name: app/src/components/Editor/TabStrip:TrieIcon
  lines: 42-49
- kind: function
  qualified_name: app/src/components/Editor/TabStrip:TrieTabButton
  lines: 51-73
- kind: function
  qualified_name: app/src/components/Editor/TabStrip:CloseIcon
  lines: 75-81
- kind: function
  qualified_name: app/src/components/Editor/TabStrip:PatchesTabButton
  lines: 83-115
- kind: function
  qualified_name: app/src/components/Editor/TabStrip:TabButton
  lines: 117-220
- kind: function
  qualified_name: app/src/components/Editor/TabStrip:TabStrip
  lines: 222-236
incoming_refs: 1
outgoing_refs: 11
---
<!-- trie:section symbol=app/src/components/Editor/TabStrip:AttentionIcon fingerprint=374a09ccbbcfc4030b7feb94cdbcb86671775ef589864eb3a7dae7ba8bba2f4b body_fp=a266767a01de4d1e2876c7ecda6bf2603799b65ad02dd0c2bb4cc8ffa0e3e489 source_ref=0115a10c6e10d66ba7cf091d4de4b465242f5758 role=util -->
Renders a 12×12 SVG focus reticle (concentric rings with crosshair arms) used as the icon for the attention/graph tab.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Editor/TabStrip:GraphIcon fingerprint=09085ba429913487199ffaf06893695f14b57fb2180cb082d2d1035b3f1ab5d6 body_fp=cd3afd0d4c78ff3c6efe9f1f81b5f36bc5f3b2cc4f9af122580bb03a2be3ffa2 source_ref=0115a10c6e10d66ba7cf091d4de4b465242f5758 role=util -->
Render a 12×12 SVG icon depicting three connected nodes representing a structural/topology graph.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Editor/TabStrip:TrieIcon fingerprint=9e53efc8bf06b5dce01d0b46d0615ab0dba8addf788ce19dc7b4ca93a0ea816f body_fp=78c1a70adc305571b96a988a675f60295273bb8a16d3b5dd2b0cb2b3098d6c8a source_ref=0115a10c6e10d66ba7cf091d4de4b465242f5758 role=util -->
Render a 12×12 SVG terminal-prompt glyph used as the trie tab icon.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Editor/TabStrip:TrieTabButton fingerprint=87b275a39735260afe802f6d76bfc0b65e684c71d4e52a32dea68d69f5ffd781 body_fp=278d375aa091180ca9688c6e8891896a322a0c204519da50272bd2c9f7ddf1ac source_ref=0115a10c6e10d66ba7cf091d4de4b465242f5758 role=api -->
Render the trie tab button, showing an animated accent dot when a trie command is running.

- `base`: shared layout/spacing CSS classes for all tab buttons.
- `tone`: active/inactive colour classes applied to this tab.
- `running`: sourced from `useTrieCommandStore`; controls visibility of the pulse indicator.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Editor/TabStrip:CloseIcon fingerprint=3a1496b53dc962fb0ac034a231058ec87cea7c907ae960de36a2abec16f95338 body_fp=2bb45df28248f334507b4048b951be273e72d2aa17c55250210c9890fa7c4d05 source_ref=0115a10c6e10d66ba7cf091d4de4b465242f5758 role=util -->
Render a small SVG × glyph used as the close-tab button icon.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Editor/TabStrip:PatchesTabButton fingerprint=1c55994cea8192d7feddc110583e78aec80d944e272445b6ebdcfe6bff34a3d2 body_fp=c70acacf46426fed7c23ac6e055c7bd0314ff9e35202a0cbb424302edb426b62 source_ref=0115a10c6e10d66ba7cf091d4de4b465242f5758 role=api -->
Render the patches tab button, showing a spinner while `applyInProgress` or a count badge when pending patches exist.

- `base`: shared layout/spacing CSS classes for all tab buttons.
- `tone`: active/inactive colour classes applied to this tab.
- `applying`: drives a spinning border indicator instead of the count badge.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Editor/TabStrip:TabButton fingerprint=39bc9f557f064ffe49398523116c5499f76ed4dd03db5ef0691f343e2a286c07 body_fp=36ed089ca015995891a61693f81cf7a938a0dee4a6e6a11e7f78e2ade0d391ec source_ref=0115a10c6e10d66ba7cf091d4de4b465242f5758 role=api -->
Render a single tab button, delegating to specialised components for `graph`, `topology`, `patches`, and `trie` kinds; file tabs include a source/triefact toggle pill, a close button, and a right-click context menu.

- `tab` — determines rendering branch and carries `id`, `kind`, `view`, `relPath`, `name`
- `active` — applies active surface/text styles when `true`
- Middle-click on a file tab closes it via `close(tab.id)`
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Editor/TabStrip:TabStrip fingerprint=09f80109f22ba192cb2b3e2bb0accfd56ed22415106e5da88440f476f87f81f5 body_fp=46c5a6c587a4eb012097675356b954bd8c4a52ed8ff3d1cf26aabdd13ca54838 source_ref=0115a10c6e10d66ba7cf091d4de4b465242f5758 role=api -->
Render the editor tab strip, mapping all tabs from `useTabsStore` into `TabButton` elements with active state.
<!-- trie:end -->